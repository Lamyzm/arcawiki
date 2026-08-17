"""posts/*.json 을 PostgreSQL 로 적재한다.

몇 번을 다시 돌려도 결과가 같아야 한다(멱등). 크롤러를 또 돌리고 다시 적재해도
중복이 쌓이거나 앞서 넣은 refs 가 사라지지 않는다.

usage:
    python ingest.py                 # 전체
    python ingest.py --only 70255821 # 한 건만
    python ingest.py --dry-run       # 세어보기만
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import psycopg
from psycopg.types.json import Jsonb

import queue_api as q

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

ROOT = Path(__file__).parent
POSTS = ROOT / "posts"

# 접속 정보를 아는 곳은 queue_api 한 곳뿐이다. 컨테이너 안에서는 DATABASE_URL 을,
# 로컬에서 직접 부를 때는 .env 를 읽는다 — 여기서 따로 조립하면 로컬에서만 인증이 깨진다.
DSN = q._dsn()

ADULT_MARK = re.compile(r"🔞|19금|성인")


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def upsert_post(cur, post: dict) -> None:
    pid = post["id"]
    title = post.get("title", "")
    # 🔞 는 제목이 아니라 카테고리에 붙는다 ("🔞정보/자료")
    is_adult = (
        bool(ADULT_MARK.search(title))
        or bool(ADULT_MARK.search(post.get("category", "")))
        or post.get("status") == "gated"
    )

    cur.execute(
        """
        INSERT INTO posts (id, channel, url, status, title, category, posted_at,
                           views, recommend, body, image_count, is_adult,
                           content_hash, fetched_at, raw)
        VALUES (%(id)s, %(channel)s, %(url)s, %(status)s, %(title)s, %(category)s,
                %(posted_at)s, %(views)s, %(recommend)s, %(body)s, %(image_count)s,
                %(is_adult)s, %(content_hash)s, %(fetched_at)s, %(raw)s)
        ON CONFLICT (id) DO UPDATE SET
            status       = EXCLUDED.status,
            title        = EXCLUDED.title,
            category     = EXCLUDED.category,
            posted_at    = COALESCE(EXCLUDED.posted_at, posts.posted_at),
            views        = GREATEST(EXCLUDED.views, posts.views),
            recommend    = GREATEST(EXCLUDED.recommend, posts.recommend),
            body         = EXCLUDED.body,
            image_count  = EXCLUDED.image_count,
            is_adult     = EXCLUDED.is_adult,
            content_hash = EXCLUDED.content_hash,
            fetched_at   = EXCLUDED.fetched_at,
            raw          = EXCLUDED.raw
        """,
        {
            "id": pid,
            "channel": post.get("channel", "aiart"),
            "url": post.get("url", ""),
            "status": post.get("status", "ok"),
            "title": title,
            "category": post.get("category", ""),
            "posted_at": parse_dt(post.get("date")),
            "views": post.get("views", 0),
            "recommend": post.get("recommend", 0),
            "body": post.get("body", ""),
            "image_count": len(post.get("images", [])),
            "is_adult": is_adult,
            "content_hash": post.get("content_hash"),
            "fetched_at": parse_dt(post.get("fetched_at")) or datetime.now(),
            "raw": Jsonb(post),
        },
    )

    # 댓글과 이미지는 통째로 다시 넣는다. 순번이 밀릴 수 있어 부분 갱신이 더 위험하다.
    cur.execute("DELETE FROM comments WHERE post_id = %s", (pid,))
    for seq, c in enumerate(post.get("comments", [])):
        text = (c.get("text") or "").strip()
        if text:
            cur.execute(
                "INSERT INTO comments (post_id, seq, body) VALUES (%s, %s, %s)",
                (pid, seq, text),
            )

    cur.execute("DELETE FROM images WHERE post_id = %s", (pid,))
    for seq, url in enumerate(post.get("images", [])):
        cur.execute(
            "INSERT INTO images (post_id, seq, url) VALUES (%s, %s, %s)",
            (pid, seq, url),
        )

    # refs 는 지우지 않는다. 수집 경로가 늘어날수록 쌓이기만 해야 한다.
    for r in post.get("refs", []):
        cur.execute(
            """
            INSERT INTO refs (post_id, hub_name, section, anchor)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (post_id, hub_name, section, anchor) DO NOTHING
            """,
            (pid, r.get("hub", ""), r.get("section", ""), r.get("anchor", "")),
        )

    for l in post.get("outlinks", []):
        cur.execute(
            """
            INSERT INTO outlinks (from_id, to_id, section, anchor)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (from_id, to_id, section, anchor) DO NOTHING
            """,
            (pid, l.get("id"), l.get("section", ""), l.get("anchor", "")),
        )

    for v in post.get("versions", []):
        cur.execute(
            """
            INSERT INTO post_versions (post_id, content_hash, body, captured_at)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (post_id, content_hash) DO NOTHING
            """,
            (pid, v.get("content_hash", ""), v.get("body", ""), parse_dt(v.get("captured_at"))),
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = sorted(POSTS.glob("*.json"))
    if args.only:
        files = [POSTS / f"{args.only}.json"]

    if args.dry_run:
        print(f"적재 대상 {len(files)}건 (dry-run)")
        return

    try:
        conn = psycopg.connect(DSN)
    except psycopg.OperationalError as e:
        print(f"DB 연결 실패: {e}", file=sys.stderr)
        print("docker compose up -d db 로 DB를 먼저 띄우세요.", file=sys.stderr)
        sys.exit(1)

    done = skipped = 0
    with conn:
        with conn.cursor() as cur:
            for n, f in enumerate(files, 1):
                try:
                    post = json.loads(f.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError):
                    skipped += 1
                    continue
                # 오는 순서가 뒤죽박죽이면 outlinks 의 to_id 가 아직 없을 수 있는데,
                # 외래키를 안 걸어둬서 문제되지 않는다 (참조는 나중에 채워진다).
                upsert_post(cur, post)
                done += 1
                if n % 200 == 0:
                    print(f"  {n}/{len(files)}")
                    conn.commit()

    print(f"\n적재 완료: {done}건 (건너뜀 {skipped}건)")

    with psycopg.connect(DSN) as conn, conn.cursor() as cur:
        for label, sql in [
            ("posts", "SELECT count(*) FROM posts"),
            ("  ok", "SELECT count(*) FROM posts WHERE status='ok'"),
            ("  성인표시", "SELECT count(*) FROM posts WHERE is_adult"),
            ("comments", "SELECT count(*) FROM comments"),
            ("refs", "SELECT count(*) FROM refs"),
            ("outlinks", "SELECT count(*) FROM outlinks"),
            ("섹션 종류", "SELECT count(DISTINCT section) FROM refs WHERE section<>''"),
        ]:
            cur.execute(sql)
            print(f"  {label:<12} {cur.fetchone()[0]:>8,}")


if __name__ == "__main__":
    main()
