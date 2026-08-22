"""재료 조회 — 채널에서 실제로 쓰인 값을 꺼낸다.

이 도구가 있어야 재료층이 쓸모가 있다. 문서로만 두면 3MB 마크다운을 매번 훑어야 하고,
프롬프트를 지어내게 된다. 이미지를 뽑기 직전에 여기서 검증된 값을 꺼내 쓴다.

    python lookup.py artist --top 30            많이 쓰인 작가 (가중치 실측 범위 포함)
    python lookup.py artist hyocorou            그 작가가 어떻게 쓰였나 + 주변 문맥
    python lookup.py outfit 교복                의상/스타일 이름으로 태그 줄 찾기
    python lookup.py tag "thigh-high"           태그 문자열이 든 블록 찾기
    python lookup.py stack --min 4              작가 4명 이상 쌓인 화풍 스택
    python lookup.py negative                   실제로 쓰인 네거티브 프롬프트
    python lookup.py exif                       EXIF 통짜 덤프
    python lookup.py post 172954099             그 글의 재료 전부

옵션: --limit N  --since YYYY-MM-DD  --json  --full(자르지 않고 전문)
"""

import argparse
import json
import re
import sys

import queue_api as q

sys.stdout.reconfigure(encoding="utf-8")

# 작가로 잘못 잡히는 것들. 품질 태그와 단부루 메타 태그가 `artist:` 문법 없이
# 가중치 괄호 안에 들어가 있으면 구분이 안 된다. 이름 기준으로 거른다.
NOT_ARTIST = {
    "artist collaboration", "censored", "uncensored", "monochrome", "greyscale",
    "lowres", "highres", "absurdres", "bad quality", "worst quality", "low quality",
    "normal quality", "best quality", "masterpiece", "simple illustration",
    "multiple views", "approximate", "echo", "blurry", "jpeg artifacts", "watermark",
    "signature", "username", "text", "logo", "artist name", "web address",
    "bad anatomy", "bad hands", "extra digits", "missing finger", "sketch",
    "traditional media", "photo", "3d", "realistic", "chibi", "duplicate",
    "very displeasing", "displeasing", "aesthetic", "quality", "source_anime",
}
JUNK_RE = re.compile(r"^(bad|worst|low|normal|best)\s|quality$|^extra\s|^missing\s")


def is_artist(name):
    return bool(name) and name not in NOT_ARTIST and not JUNK_RE.search(name)


def cut(s, n, full):
    s = re.sub(r"\s+", " ", (s or "").strip())
    return s if full or len(s) <= n else s[:n] + " …"


def url(pid):
    return "https://arca.live/b/aiart/%s" % pid


def q_artist(cur, a):
    if a.query:
        cur.execute(
            """SELECT name, uses, posts, avg_weight, min_weight, max_weight, latest
                 FROM artist_usage WHERE name ILIKE %s ORDER BY posts DESC, uses DESC LIMIT %s""",
            ("%" + a.query + "%", a.limit))
    else:
        cur.execute(
            """SELECT name, uses, posts, avg_weight, min_weight, max_weight, latest
                 FROM artist_usage WHERE posts >= 2 ORDER BY posts DESC, uses DESC LIMIT %s""",
            (a.limit * 3,))
    rows = [r for r in cur.fetchall() if is_artist(r["name"])][: a.limit]
    if a.json:
        return rows

    for r in rows:
        w = ("%s (%s~%s)" % (r["avg_weight"], r["min_weight"], r["max_weight"])
             if r["avg_weight"] is not None else "가중치 없이 쓰임")
        print("  %-32s 글%3d  %-24s 최근 %s" % (r["name"][:32], r["posts"], w, r["latest"]))

    # 한 명만 찍어서 봤다면 그 작가가 어떤 맥락에서 언급됐는지도 보여준다.
    # "이 작가는 눈을 뭉갠다" 같은 거동 주석이 여기 붙어 있다.
    if a.query and len(rows) == 1:
        cur.execute(
            """SELECT DISTINCT post_id, raw, context FROM prompt_assets
                WHERE kind='artist' AND name=%s ORDER BY post_id DESC LIMIT 8""",
            (rows[0]["name"],))
        print("\n  --- 쓰인 자리")
        for r in cur.fetchall():
            print("   %s  %s" % (url(r["post_id"]), r["raw"]))
            print("      %s" % cut(r["context"], 150, a.full))
    return None


def q_blocks(cur, a, roles, by_label):
    where = ["role = ANY(%s)"]
    args = [list(roles)]
    if a.query:
        where.append("(label ILIKE %s OR body ILIKE %s)" if by_label else "body ILIKE %s")
        args += ["%" + a.query + "%"] * (2 if by_label else 1)
    if a.since:
        where.append("posted_at >= %s")
        args.append(a.since)
    if getattr(a, "min", None):
        where.append("n_artists >= %s")
        args.append(a.min)
    args.append(a.limit)

    cur.execute(
        "SELECT post_id, comment_seq, label, body, n_artists, posted_at FROM prompt_blocks"
        " WHERE " + " AND ".join(where) +
        " ORDER BY n_artists DESC, posted_at DESC LIMIT %s", args)
    rows = cur.fetchall()
    if a.json:
        return rows

    for r in rows:
        head = r["label"] or ("작가 %d명" % r["n_artists"] if r["n_artists"] else "")
        where_s = "댓글 %s" % r["comment_seq"] if r["comment_seq"] is not None else "본문"
        print("\n  ▸ %s   [%s · %s · %s]" % (head, r["posted_at"], where_s, url(r["post_id"])))
        print("    %s" % cut(r["body"], 400, a.full))
    if not rows:
        print("  없음")
    return None


def q_post(cur, a):
    pid = int(a.query)
    cur.execute("SELECT title, posted_at::date d, category FROM posts WHERE id=%s", (pid,))
    p = cur.fetchone()
    if not p:
        print("  그 글이 DB에 없다"); return None
    print("  %s  [%s · %s]" % (p["title"], p["d"], p["category"]))
    print("  %s\n" % url(pid))

    cur.execute(
        """SELECT kind, name, raw, weight FROM prompt_assets
            WHERE post_id=%s ORDER BY kind, name""", (pid,))
    by = {}
    for r in cur.fetchall():
        by.setdefault(r["kind"], []).append(r)
    for kind, rows in by.items():
        vals = sorted({(r["name"], r["weight"]) for r in rows})
        s = ", ".join("%s%s" % (n, ":%s" % w if w is not None else "") for n, w in vals)
        print("  %-13s %s" % (kind, cut(s, 300, a.full)))

    cur.execute(
        "SELECT role, label, body, n_artists FROM prompt_blocks WHERE post_id=%s ORDER BY id",
        (pid,))
    bl = cur.fetchall()
    if bl:
        print("\n  --- 블록 %d개" % len(bl))
        for r in bl:
            print("  ▸ %s" % (r["label"] or r["role"]))
            print("    %s" % cut(r["body"], 300, a.full))
    return None


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("what", choices=["artist", "outfit", "tag", "stack", "negative", "exif", "post"])
    p.add_argument("query", nargs="?")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--top", type=int)
    p.add_argument("--min", type=int)
    p.add_argument("--since")
    p.add_argument("--json", action="store_true")
    p.add_argument("--full", action="store_true")
    a = p.parse_args()
    if a.top:
        a.limit = a.top

    with q._conn() as c, c.cursor() as cur:
        if a.what == "artist":
            out = q_artist(cur, a)
        elif a.what == "post":
            out = q_post(cur, a)
        elif a.what == "outfit":
            out = q_blocks(cur, a, ("tag_list",), by_label=True)
        elif a.what == "tag":
            out = q_blocks(cur, a, ("tag_list", "negative"), by_label=False)
        elif a.what == "stack":
            a.min = a.min or 3
            out = q_blocks(cur, a, ("tag_list",), by_label=True)
        elif a.what == "negative":
            out = q_blocks(cur, a, ("negative",), by_label=False)
        else:
            out = q_blocks(cur, a, ("exif",), by_label=False)

    if a.json and out is not None:
        print(json.dumps(out, ensure_ascii=False, default=str, indent=2))


if __name__ == "__main__":
    main()
