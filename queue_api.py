"""스킬이 DB 를 다루는 통로.

스킬(마크다운)에 SQL 을 적으면 스키마가 바뀔 때마다 여러 파일을 고쳐야 한다.
여기 한 곳만 고치면 되도록 모아 둔다.
"""

from __future__ import annotations

import os

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb


def _dsn() -> str:
    if os.environ.get("DATABASE_URL"):
        return os.environ["DATABASE_URL"]
    pw = os.environ.get("POSTGRES_PASSWORD")
    if not pw:
        # .env 를 직접 읽는다. 스킬에서 환경변수를 챙기지 않아도 동작하게.
        env = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        if os.path.exists(env):
            for line in open(env, encoding="utf-8"):
                if line.startswith("POSTGRES_PASSWORD="):
                    pw = line.split("=", 1)[1].strip()
                    break
    return f"postgres://arcawiki:{pw or 'arcawiki'}@127.0.0.1:5433/arcawiki"


def _conn():
    return psycopg.connect(_dsn(), row_factory=dict_row)


# ------------------------------------------------------------------ 큐


STALE_MINUTES = 45  # 이보다 오래 붙들려 있으면 처리하던 세션이 죽은 것으로 본다


def take(
    job: str,
    limit: int = 20,
    worker: str = "",
    priority: int | None = None,
) -> list[dict]:
    """우선순위 순으로 작업을 꺼내면서 **잠근다**.

    **우선순위는 낮은 수가 먼저다** (`ORDER BY priority`). 10 이 15보다 먼저 나온다.
    특정 묶음만 처리하고 싶으면 `priority=15` 처럼 정확한 값을 지정한다.
    지정하지 않으면 전체에서 가장 앞선 것부터 꺼낸다.

    여러 세션을 동시에 돌릴 때 같은 글을 중복 처리하지 않도록,
    꺼내는 것과 잠그는 것을 한 트랜잭션에서 한다.
    `FOR UPDATE SKIP LOCKED` 라서 다른 세션이 보고 있는 행은 건너뛴다.

    처리 도중 세션이 죽으면 그 몫은 STALE_MINUTES 뒤에 자동으로 회수된다.
    """
    worker = worker or f"pid{os.getpid()}"
    where_pri = "AND priority = %(priority)s" if priority is not None else ""
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            f"""UPDATE work_queue q
                   SET status='claimed', claimed_at=now(), claimed_by=%(worker)s
                 WHERE q.id IN (
                     SELECT id FROM work_queue
                      WHERE job = %(job)s
                        {where_pri}
                        AND (status = 'pending'
                             OR (status = 'claimed'
                                 AND claimed_at < now() - interval '{STALE_MINUTES} minutes'))
                      ORDER BY priority, created_at
                      LIMIT %(limit)s
                      FOR UPDATE SKIP LOCKED
                 )
             RETURNING id, target_type, target_key, job, reason, detail, priority, status""",
            {"worker": worker, "job": job, "limit": limit, "priority": priority},
        )
        rows = cur.fetchall()
        c.commit()
        return rows


def release(job: str, target_keys: list[str]) -> None:
    """처리하지 못하고 넘길 때 잠금을 푼다."""
    if not target_keys:
        return
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """UPDATE work_queue SET status='pending', claimed_at=NULL, claimed_by=''
               WHERE job=%s AND target_key=ANY(%s) AND status='claimed'""",
            (job, target_keys),
        )
        c.commit()


def done(job: str, target_key: str, note: str = "") -> None:
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """UPDATE work_queue SET status='done', done_at=now(), note=%s
               WHERE job=%s AND target_key=%s""",
            (note, job, target_key),
        )
        c.commit()


def skip(job: str, target_key: str, note: str) -> None:
    """위키 재료가 못 되는 것. 왜 건너뛰었는지는 반드시 남긴다."""
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """UPDATE work_queue SET status='skipped', done_at=now(), note=%s
               WHERE job=%s AND target_key=%s""",
            (note, job, target_key),
        )
        c.commit()


def queue_status() -> dict:
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            "SELECT job, status, count(*) AS n FROM work_queue GROUP BY job, status ORDER BY 1,2"
        )
        return {f"{r['job']}/{r['status']}": r["n"] for r in cur.fetchall()}


# ------------------------------------------------------------------ 읽기


def load_posts(ids: list[int], max_chars: int = 8000, max_comments: int = 30) -> list[dict]:
    """원문과 댓글을 읽는다.

    본문이 15만 자인 글이 실제로 있어서 상한을 둔다. 댓글은 본문의 오류를
    정정하는 경우가 많아 함께 싣는다.
    """
    if not ids:
        return []
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """SELECT id, url, title, category, posted_at, recommend, views,
                      left(body, %s) AS body, body_len, is_adult
               FROM posts WHERE id = ANY(%s) ORDER BY recommend DESC""",
            (max_chars, ids),
        )
        rows = cur.fetchall()
        cur.execute(
            "SELECT post_id, body FROM comments WHERE post_id = ANY(%s) ORDER BY post_id, seq",
            (ids,),
        )
        by_post: dict[int, list[str]] = {}
        for r in cur.fetchall():
            by_post.setdefault(r["post_id"], []).append(r["body"])
    for r in rows:
        r["comments"] = by_post.get(r["id"], [])[:max_comments]
    return rows


# ------------------------------------------------------------------ 쓰기


def save_card(post_id: int, card: dict, version: str = "v1") -> int:
    """지식카드를 저장한다. 같은 글·같은 버전은 갱신한다(멱등)."""
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """INSERT INTO knowledge_cards
                   (post_id, extractor_version, topic, summary, software, models,
                    settings, usefulness, as_of)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
               ON CONFLICT (post_id, extractor_version) DO UPDATE SET
                   topic=EXCLUDED.topic, summary=EXCLUDED.summary,
                   software=EXCLUDED.software, models=EXCLUDED.models,
                   settings=EXCLUDED.settings, usefulness=EXCLUDED.usefulness,
                   as_of=EXCLUDED.as_of
               RETURNING id""",
            (
                post_id, version, card["topic"], card["summary"],
                card.get("software", []), card.get("models", []),
                Jsonb(card.get("settings", {})), card.get("usefulness", 5),
                card.get("as_of") or None,
            ),
        )
        cid = cur.fetchone()["id"]
        c.commit()
        return cid


def find_or_create_claim(canonical: str, topic: str) -> int:
    """같은 주장이 이미 있으면 그것을 쓴다.

    재통합을 돌릴 때마다 같은 주장이 새로 생기면 Claim 이 계속 불어난다.
    """
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            "SELECT id FROM claims WHERE topic=%s AND lower(canonical)=lower(%s)",
            (topic, canonical),
        )
        row = cur.fetchone()
        if row:
            return row["id"]
        cur.execute(
            "INSERT INTO claims (canonical, topic) VALUES (%s,%s) RETURNING id",
            (canonical, topic),
        )
        cid = cur.fetchone()["id"]
        c.commit()
        return cid


def link_cards(claim_id: int, links: list[dict]) -> None:
    """카드를 주장에 붙인다. links: [{card_id, relation, quote}]"""
    with _conn() as c, c.cursor() as cur:
        for l in links:
            cur.execute(
                """INSERT INTO card_claims (card_id, claim_id, relation, quote)
                   VALUES (%s,%s,%s,%s)
                   ON CONFLICT (card_id, claim_id) DO UPDATE
                     SET relation=EXCLUDED.relation, quote=EXCLUDED.quote""",
                (l["card_id"], claim_id, l["relation"], l.get("quote", "")),
            )
        cur.execute(
            """UPDATE claims SET
                 as_of_earliest=(SELECT min(k.as_of) FROM knowledge_cards k
                                 JOIN card_claims cc ON cc.card_id=k.id WHERE cc.claim_id=%s),
                 as_of_latest  =(SELECT max(k.as_of) FROM knowledge_cards k
                                 JOIN card_claims cc ON cc.card_id=k.id WHERE cc.claim_id=%s),
                 updated_at=now()
               WHERE id=%s""",
            (claim_id, claim_id, claim_id),
        )
        c.commit()


def relate_claims(from_claim: int, to_claim: int, relation: str, note: str = "") -> None:
    """주장끼리 잇는다. supersedes | refines | conditional_on | contradicts"""
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """INSERT INTO claim_relations (from_claim, to_claim, relation, note)
               VALUES (%s,%s,%s,%s)
               ON CONFLICT (from_claim, to_claim, relation) DO UPDATE SET note=EXCLUDED.note""",
            (from_claim, to_claim, relation, note),
        )
        c.commit()
