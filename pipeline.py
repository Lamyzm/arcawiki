"""자동 파이프라인. 컨테이너 안에서 정기적으로 돈다.

판단이 필요 없는 일만 한다 (ADR-0006):
    수집 → 적재 → 변경 감지 → 작업 큐 채우기

LLM 이 필요한 지점은 work_queue 에 쌓아두고 끝낸다. 그것은 Claude Code 세션이
스킬로 꺼내 처리한다. 이 스크립트는 LLM 을 호출하지 않는다.

usage:
    python pipeline.py --once      # 한 바퀴 돌고 종료
    python pipeline.py             # 주기 실행 (컨테이너 기본)
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

import psycopg

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

DSN = os.environ.get(
    "DATABASE_URL",
    "postgres://arcawiki:{}@127.0.0.1:5433/arcawiki".format(
        os.environ.get("POSTGRES_PASSWORD", "arcawiki")
    ),
)
INTERVAL_HOURS = float(os.environ.get("PIPELINE_INTERVAL_HOURS", "6"))
CRAWL_PAGES = int(os.environ.get("CRAWL_PAGES", "5"))
CRAWL_CATEGORIES = [
    c.strip() for c in os.environ.get("CRAWL_CATEGORIES", "일반정보,실험정보").split(",") if c.strip()
]

# ADR-0005 의 주제 우선순위. 낮을수록 먼저 처리한다.
# 목표가 '짤·비디오를 잘 만드는 것' 이므로 제작에 가까운 순서로 둔다.
TOPIC_PRIORITY = [
    # 낮은 수가 먼저다. 입문 자료가 맨 앞인 이유는 이 위키의 목적이
    # "아무것도 모르는 사람이 제 손으로 한 장 뽑는 데까지" 이기 때문이다.
    # 이 규칙이 없으면 뉴비용 글이 기본값 90 으로 밀려 영영 처리되지 않는다.
    (5, r"입문|뉴비|초보|처음|기초|설치|용어|가이드|FAQ|자주.?묻|정리글|모음"),
    (10, r"MiniMax|미니맥스|Wan2|I2V|T2V|비디오|영상|동영상"),
    (20, r"ANIMA|아니마"),
    (30, r"ComfyUI|컴피"),
    (40, r"VRAM|브램|최적화|양자화|fp8|gguf|sage"),
    (50, r"프롬프트|프롬|태그|와일드카드"),
    (55, r"업스케일|upscale|hires|디테일러|화질"),
    (60, r"로라|LoRA"),
    (70, r"오류|에러|error|해결|버그"),
    (80, r"포토샵|photoshop|레이어|보정|합성|편집"),
]


def log(msg: str) -> None:
    stamp = datetime.now(timezone.utc).astimezone().strftime("%H:%M:%S")
    print(f"[{stamp}] {msg}", flush=True)


def run(cmd: list[str], label: str) -> bool:
    log(f"{label} 시작")
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    except subprocess.TimeoutExpired:
        log(f"{label} 시간 초과")
        return False
    tail = (r.stdout or "").strip().splitlines()[-3:]
    for line in tail:
        log(f"  {line}")
    if r.returncode == 2:
        # crawler 가 차단 신호로 중단한 경우. 다음 주기까지 쉰다.
        log(f"{label} 차단 감지 — 이번 주기는 여기서 멈춘다")
        return False
    if r.returncode != 0:
        log(f"{label} 실패 (exit {r.returncode})")
        for line in (r.stderr or "").strip().splitlines()[-3:]:
            log(f"  ! {line}")
        return False
    log(f"{label} 완료")
    return True


def fill_queue(conn: psycopg.Connection) -> dict[str, int]:
    """LLM 이 손대야 할 것을 큐에 넣는다. 판단은 하지 않고 표시만 한다."""
    added = {}
    with conn.cursor() as cur:
        # 1) 아직 추출되지 않은 글
        priority_sql = " ".join(
            f"WHEN p.title ~* '{pat}' OR left(p.body, 3000) ~* '{pat}' THEN {pri}"
            for pri, pat in TOPIC_PRIORITY
        )
        cur.execute(
            f"""
            INSERT INTO work_queue (target_type, target_key, job, reason, detail, priority)
            SELECT 'post', p.id::text, 'extract', 'new',
                   left(p.title, 200),
                   CASE {priority_sql} ELSE 90 END
            FROM pending_extraction pe
            JOIN posts p ON p.id = pe.id
            ON CONFLICT (target_type, target_key, job) DO NOTHING
            """
        )
        added["extract"] = cur.rowcount

        # 2) 원문이 바뀐 문서 — 이미 done 이어도 다시 pending 으로 되돌린다
        cur.execute(
            """
            INSERT INTO work_queue (target_type, target_key, job, reason, detail, priority)
            SELECT 'page', s.slug, 'refresh_page', 'source_changed',
                   s.changed_sources || '건 변경', 20
            FROM stale_pages s
            ON CONFLICT (target_type, target_key, job)
            DO UPDATE SET status = 'pending',
                          reason = 'source_changed',
                          detail = EXCLUDED.detail,
                          done_at = NULL
            """
        )
        added["refresh_page"] = cur.rowcount

        # 3) 글이 충분히 모였는데 아직 문서가 없는 섹션
        cur.execute(
            """
            INSERT INTO work_queue (target_type, target_key, job, reason, detail, priority)
            SELECT 'section', r.section, 'write_page', 'new',
                   count(*) || '건 확보', 40
            FROM refs r
            JOIN posts p ON p.id = r.post_id AND p.status = 'ok' AND p.body_len >= 200
            WHERE r.section <> '' AND r.section <> '(머리말)'
              AND NOT EXISTS (SELECT 1 FROM wiki_pages w WHERE w.section = r.section)
            GROUP BY r.section
            HAVING count(*) >= 3
            ON CONFLICT (target_type, target_key, job) DO NOTHING
            """
        )
        added["write_page"] = cur.rowcount
    conn.commit()
    return added


def cycle(root: str) -> None:
    log("=" * 50)

    for cat in CRAWL_CATEGORIES:
        ok = run(
            [sys.executable, f"{root}/crawler.py", "--pages", str(CRAWL_PAGES), "--category", cat],
            f"수집({cat})",
        )
        if not ok:
            break

    run([sys.executable, f"{root}/ingest.py"], "적재")

    try:
        with psycopg.connect(DSN) as conn:
            added = fill_queue(conn)
            log(f"큐 추가: {added}")
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT job, count(*) FROM work_queue WHERE status='pending' GROUP BY job"
                )
                pending = dict(cur.fetchall())
            log(f"대기 중: {pending or '없음'}")
    except psycopg.OperationalError as e:
        log(f"DB 연결 실패: {e}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    args = ap.parse_args()

    root = os.path.dirname(os.path.abspath(__file__))

    if args.once:
        cycle(root)
        return

    log(f"파이프라인 시작 — {INTERVAL_HOURS}시간 주기")
    while True:
        try:
            cycle(root)
        except Exception as e:  # 한 주기가 실패해도 다음 주기는 돌아야 한다
            log(f"주기 실패: {type(e).__name__}: {e}")
        log(f"{INTERVAL_HOURS}시간 대기")
        time.sleep(INTERVAL_HOURS * 3600)


if __name__ == "__main__":
    main()
