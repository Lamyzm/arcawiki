"""자원(링크) 문서를 만든다.

카드의 settings·summary 에 이미 URL 이 들어 있다. 그것을 용도별로 갈라 모으고,
살아 있는지 확인해서 표시한다. "받으러 갔더니 없더라" 를 미리 거르는 것이 목적이다.

usage:
    python make_resources.py            # 링크 검사 없이 (빠름)
    python make_resources.py --check    # HEAD 요청으로 생존 확인 (느림)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict

import requests

import queue_api as q

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

URL_RE = re.compile(r"https?://[^\s\"'\\)\]}>,]+")

# 도메인 → (분류, 설명). 분류가 곧 문서 안의 절이 된다.
DOMAIN_KIND = {
    "huggingface.co": ("모델·LoRA", "모델 가중치 원본 배포처"),
    "civitai.com": ("모델·LoRA", "커뮤니티 모델·LoRA 공유"),
    "civitai.red": ("모델·LoRA", "civitai 미러"),
    "github.com": ("커스텀 노드·도구", "노드 저장소, 이슈, PR"),
    "gist.github.com": ("커스텀 노드·도구", "코드 조각"),
    "drive.google.com": ("워크플로우·배포", "워크플로우 파일"),
    "kio.ac": ("워크플로우·배포", "임시 파일 공유 — 기한 만료 잦음"),
    "pastebin.com": ("프롬프트·텍스트", "프롬프트 전문"),
    "reddit.com": ("원출처·소식", "해외 커뮤니티"),
    "x.com": ("원출처·소식", ""),
    "seed.bytedance.com": ("원출처·소식", "제작사 공식"),
    "arxiv.org": ("원출처·소식", "논문"),
    "youtube.com": ("영상 자료", ""),
    "youtu.be": ("영상 자료", ""),
    "dreamina.capcut.com": ("웹 서비스", "Seedance 글로벌"),
    "jimeng.jianying.com": ("웹 서비스", "Seedance 중국 — 해외 접속 차단"),
    "download.pytorch.org": ("커스텀 노드·도구", "PyTorch 휠"),
}

SKIP_DOMAINS = {"arca.live", "127.0.0.1", "localhost"}  # 채널 내부 링크는 출처로 이미 붙는다


def collect() -> dict[str, list[dict]]:
    """카드에서 URL 을 뽑아 분류별로 모은다."""
    buckets: dict[str, dict[str, dict]] = defaultdict(dict)
    with q._conn() as c, c.cursor() as cur:
        cur.execute(
            """SELECT k.id, k.post_id, k.topic, k.summary, k.settings, k.as_of,
                      p.title, p.url, p.recommend
               FROM knowledge_cards k JOIN posts p ON p.id = k.post_id
               ORDER BY k.as_of DESC"""
        )
        for card in cur.fetchall():
            blob = json.dumps(card["settings"], ensure_ascii=False) + " " + card["summary"]
            for raw in URL_RE.findall(blob):
                url = raw.rstrip(".,;·")
                try:
                    host = url.split("/")[2].lower().replace("www.", "")
                except IndexError:
                    continue
                if any(host.startswith(s) for s in SKIP_DOMAINS) or "<" in host:
                    continue
                kind, _ = DOMAIN_KIND.get(host, ("기타", ""))
                # 같은 URL 이 여러 카드에 나오면 가장 최근 것으로 둔다
                buckets[kind].setdefault(
                    url,
                    {
                        "url": url,
                        "host": host,
                        "post_id": card["post_id"],
                        "title": card["title"],
                        "as_of": card["as_of"],
                        "topic": card["topic"],
                        "recommend": card["recommend"],
                    },
                )
    return {k: sorted(v.values(), key=lambda r: (r["as_of"] or ""), reverse=True)
            for k, v in buckets.items()}


def check_alive(items: list[dict]) -> None:
    """HEAD 요청으로 생존 확인. 실패해도 죽었다고 단정하지 않는다."""
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0"})
    for it in items:
        try:
            r = s.head(it["url"], timeout=8, allow_redirects=True)
            if r.status_code in (403, 405):  # HEAD 를 막는 곳이 많다
                r = s.get(it["url"], timeout=8, stream=True)
            it["status"] = r.status_code
        except requests.RequestException:
            it["status"] = 0


def render(buckets: dict[str, list[dict]], checked: bool) -> list[dict]:
    entries = []
    order = ["모델·LoRA", "커스텀 노드·도구", "워크플로우·배포", "프롬프트·텍스트",
             "웹 서비스", "원출처·소식", "영상 자료", "기타"]
    seq = 0
    for kind in order:
        items = buckets.get(kind, [])
        if not items:
            continue
        seq += 1
        lines = []
        if kind == "워크플로우·배포":
            lines.append("> ⚠️ 이 분류는 **링크가 잘 죽는다.** kio.ac 는 기한이 30일이고 "
                         "구글 드라이브도 삭제되는 경우가 많다. 받을 수 있을 때 받아 두는 편이 낫다.")
            lines.append("")
        lines.append("| 링크 | 어디서 나왔나 | 시점 |")
        lines.append("|---|---|---|")
        for it in items[:60]:
            mark = ""
            if checked:
                st = it.get("status", -1)
                mark = " ❌" if st in (0, 404, 410) else ""
            label = it["url"]
            if len(label) > 78:
                label = label[:75] + "…"
            when = f"{it['as_of']:%Y-%m}" if it["as_of"] else "?"
            lines.append(
                f"| [`{label}`]({it['url']}){mark} | [{it['title'][:34]}](https://arca.live/b/aiart/{it['post_id']}) | {when} |"
            )
        if len(items) > 60:
            lines.append("")
            lines.append(f"*{len(items) - 60}개 더 있음 — 추출이 진행되면 늘어난다.*")
        entries.append(dict(seq=seq, heading=kind, conf="high",
                            as_of=max((i["as_of"] for i in items if i["as_of"]), default=None),
                            cf=False, posts=sorted({i["post_id"] for i in items}),
                            body="\n".join(lines)))
    return entries


PAGE = dict(
    slug="resources", title="자원 — 받는 곳 모음", kind="자원", stage=None, section="",
    intro=("채널 글에 흩어진 다운로드·저장소 링크를 용도별로 모았다. "
           "**❌ 표시는 확인 시점에 응답하지 않은 링크다.**"),
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="HEAD 요청으로 생존 확인")
    args = ap.parse_args()

    buckets = collect()
    total = sum(len(v) for v in buckets.values())
    print(f"수집한 링크 {total}개 / 분류 {len(buckets)}종")

    if args.check:
        for kind, items in buckets.items():
            print(f"  검사 중: {kind} ({len(items)})")
            check_alive(items)
        dead = sum(1 for v in buckets.values() for i in v if i.get("status") in (0, 404, 410))
        print(f"  응답 없음 {dead}개")

    entries = render(buckets, args.check)

    with q._conn() as c, c.cursor() as cur:
        cur.execute(
            """INSERT INTO wiki_pages (slug,title,section,kind,stage,intro,generated_at,published)
               VALUES (%(slug)s,%(title)s,%(section)s,%(kind)s,%(stage)s,%(intro)s,now(),true)
               ON CONFLICT (slug) DO UPDATE SET intro=EXCLUDED.intro, kind=EXCLUDED.kind,
                    title=EXCLUDED.title, generated_at=now() RETURNING id""",
            PAGE,
        )
        pid = cur.fetchone()["id"]
        cur.execute("DELETE FROM wiki_entries WHERE page_id=%s AND human_edited=false", (pid,))
        allp = set()
        for e in entries:
            cur.execute(
                """INSERT INTO wiki_entries (page_id,seq,heading,body_md,confidence,as_of,has_conflict)
                   VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id""",
                (pid, e["seq"], e["heading"], e["body"], e["conf"], e["as_of"], e["cf"]),
            )
            eid = cur.fetchone()["id"]
            for p in e["posts"]:
                cur.execute(
                    "INSERT INTO wiki_entry_sources (entry_id,post_id) VALUES (%s,%s) ON CONFLICT DO NOTHING",
                    (eid, p),
                )
                allp.add(p)
        cur.execute(
            """INSERT INTO page_sources (page_id,post_id,content_hash)
               SELECT %s,id,content_hash FROM posts WHERE id=ANY(%s)
               ON CONFLICT (page_id,post_id) DO UPDATE SET content_hash=EXCLUDED.content_hash""",
            (pid, list(allp)),
        )
        c.commit()
    print(f"page {pid} | 항목 {len(entries)} | 원문 {len(allp)}")


if __name__ == "__main__":
    main()
