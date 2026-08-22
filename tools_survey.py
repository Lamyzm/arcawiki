# -*- coding: utf-8 -*-
"""채널에 공유된 도구를 전수 조사한다.

무엇을 또 만들지 정하기 전에 이미 있는 것을 세는 것이 먼저다.
글 제목/본문에서 배포·공유 신호를 잡고 용도별로 분류한다.
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
sys.path.insert(0, r"F:\Project\arcawiki")

import psycopg
import queue_api as q

# 도구 글로 볼 신호. "그림체 공유"·"짤 공유" 같은 결과물 공유는 걸러야 한다.
TOOL_HINT = re.compile(
    r"(툴|도구|프로그램|앱|생성기|뷰어|매니저|헬퍼|helper|manager|viewer|"
    r"\.html|익스텐션|확장|커스텀\s*노드|노드\s*공유|스크립트|자동화|"
    r"워크플로우|와일드카드|편집기|정리기|추출|다운로더|설치)", re.I)

NOT_TOOL = re.compile(r"(그림체 공유|짤|후기|질문|봐주|추천 좀|뽑아|생성했|만들어봤어요\?)", re.I)

CATS = [
    ("프롬프트 작성·관리", r"(프롬프트|프롬|prompt|와일드카드|랜덤|프리셋)"),
    ("태그 사전·검색",     r"(태그|단부루|danbooru|사전|자동완성|번역)"),
    ("이미지 관리·뷰어",   r"(뷰어|갤러리|분류|exif|메타데이터|이미지 관리|정리)"),
    ("커스텀 노드",        r"(커스텀\s*노드|노드 공유|comfyui-|익스텐션|확장)"),
    ("워크플로우",         r"(워크플로우|workflow|\.json)"),
    ("로라 제작·관리",     r"(로라|lora|학습|kohya|병합|머지)"),
    ("설치·환경",          r"(설치|portable|포터블|가이드|입문|셋팅|세팅)"),
    ("영상",               r"(영상|비디오|i2v|t2v|wan|ltx|미니맥스|minimax|h3)"),
]


def categorize(title, body):
    t = (title or "") + " " + (body or "")[:400]
    hits = [name for name, pat in CATS if re.search(pat, t, re.I)]
    return hits or ["기타"]


def main():
    c = psycopg.connect(q._dsn())
    rows = c.execute("""
        SELECT id, posted_at::date, title, recommend, views, left(body, 600)
        FROM posts
        WHERE recommend >= 10 AND title IS NOT NULL
        ORDER BY recommend DESC
        LIMIT 1200""").fetchall()

    picked = []
    for pid, day, title, rec, views, body in rows:
        if NOT_TOOL.search(title or ""):
            continue
        if not TOOL_HINT.search((title or "") + " " + (body or "")[:300]):
            continue
        picked.append((pid, day, title, rec, views, categorize(title, body)))

    print("도구성 글 %d개 (추천 10 이상)\n" % len(picked))

    by_cat = {}
    for p in picked:
        # 가장 앞선 분류 하나로만 센다 - 중복 집계를 피한다
        by_cat.setdefault(p[5][0], []).append(p)

    for name, _ in CATS + [("기타", "")]:
        items = by_cat.get(name)
        if not items:
            continue
        print("=" * 72)
        print("[%s]  %d개" % (name, len(items)))
        for pid, day, title, rec, views, _cats in items[:14]:
            print("  %-10d %s  추천%-4s 조회%-7s %s" % (pid, day, rec, views, title[:56]))
        if len(items) > 14:
            print("  ... 그 외 %d개" % (len(items) - 14))
        print()


if __name__ == "__main__":
    main()
