"""아카라이브 채널 크롤러.

두 가지 수집 모드가 있다.

  허브 모드 (기본)  : 튜토리얼 허브 글의 본문에 걸린 링크를 따라간다.
                      사람이 큐레이션한 목록이라 품질이 보장되고,
                      허브의 소제목이 그대로 주제 라벨이 된다.
  카테고리 모드     : 목록 페이지를 훑는다. 허브에 안 걸린 글을 보충할 때.

수집 원칙
  - 글 하나 = posts/<id>.json 하나. 어느 경로로 도달하든 같은 파일로 수렴한다.
  - refs(어느 허브의 어느 섹션에서 참조됐는지)는 덮어쓰지 않고 병합한다.
  - status 가 ok 인 글만 건너뛴다. 실패/차단된 글은 다음 실행에서 다시 시도한다.
  - 본문도 이미지도 없으면 ok 로 저장하지 않는다 (빈 껍데기 고착 방지).

usage:
    python crawler.py --check                      # 로그인 상태만 확인
    python crawler.py --seeds                      # 허브 모드 (기본 시드)
    python crawler.py --pages 10 --category 일반정보
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# 윈도우 콘솔이 cp949 로 뜨면 한글 출력이 깨진다
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

BASE = "https://arca.live"
ROOT = Path(__file__).parent
POSTS = ROOT / "posts"
COOKIE_FILE = ROOT / "cookie.txt"

# AI그림채널의 튜토리얼 허브. 본문이 다른 글로 가는 링크 모음이다.
SEED_HUBS: dict[int, str] = {
    70255821: "정보글모음",
    70417374: "오류해결",
    70275172: "FAQ",
    70269083: "뉴비용",
    61235642: "통합공지",
    123263240: "압축공지",
    109424774: "질문전에",
}

# 계정이 걸리면 IP 차단과 달리 복구가 어렵다. 여유 있게 간다.
DELAY_BASE = 5.0
DELAY_JITTER = 2.0
MAX_CONSECUTIVE_FAILURES = 5

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
}

session = requests.Session()
session.headers.update(HEADERS)


class Blocked(Exception):
    """차단 신호(429/403). 재시도하지 않고 실행 전체를 멈춘다."""


def load_cookie() -> bool:
    """cookie.txt 의 Cookie 헤더 값을 세션에 싣는다. ID/PW 는 다루지 않는다."""
    if not COOKIE_FILE.exists():
        return False
    raw = COOKIE_FILE.read_text(encoding="utf-8").strip()
    if raw.lower().startswith("cookie:"):
        raw = raw.split(":", 1)[1].strip()
    if not raw:
        return False
    session.headers["Cookie"] = raw
    return True


def polite_sleep(base: float = DELAY_BASE) -> None:
    """요청 간격. 고정값이면 패턴이 뚜렷해지므로 지터를 준다."""
    time.sleep(base + random.uniform(0, DELAY_JITTER))


def fetch(url: str, retries: int = 3) -> tuple[str, str | None]:
    """(status, html) 을 돌려준다.

    status: ok | gated | notfound | error
    429/403 은 물러나야 하는 신호이므로 Blocked 를 올린다. 경고를 무시하고
    계속 두드리는 것이 정지로 이어진다.
    """
    for attempt in range(retries):
        try:
            r = session.get(url, timeout=20)
        except requests.RequestException as e:
            print(f"    ! {type(e).__name__}", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
            continue

        if r.status_code == 200:
            if "Just a moment" in r.text or "cf_chl" in r.text:
                raise Blocked("cloudflare challenge")
            return "ok", r.text
        if r.status_code == 451:
            # 연령 게이트. 재시도해도 달라지지 않으므로 즉시 확정한다.
            return "gated", None
        if r.status_code == 404:
            return "notfound", None
        if r.status_code in (403, 429):
            raise Blocked(f"HTTP {r.status_code}")
        print(f"    ! HTTP {r.status_code}", file=sys.stderr)
        time.sleep(3 * (attempt + 1))

    return "error", None


def parse_int(text: str | None) -> int:
    if not text:
        return 0
    m = re.search(r"-?\d[\d,]*", text)
    return int(m.group().replace(",", "")) if m else 0


def ids_of(html: str) -> set[int]:
    soup = BeautifulSoup(html, "lxml")
    out: set[int] = set()
    for row in soup.select("a.vrow"):
        if "notice" in (row.get("class") or []):
            continue
        m = re.match(r"/b/[^/]+/(\d+)", row.get("href") or "")
        if m:
            out.add(int(m.group(1)))
    return out


# ---------------------------------------------------------------- 링크 그래프

_SECTION_REJECT = re.compile(
    r"^(https?://|www\.)"          # URL 이 굵게 표시된 경우
    r"|^\+?\d{2}[/.\-]\d{2}"       # +23/03/16 같은 변경 이력
    r"|^Ctrl\+F$",
    re.I,
)


def clean_section(text: str) -> str | None:
    """소제목 후보를 정규화한다.

    <b>/<strong> 은 본문 강조에도 쓰여서 그대로 믿으면 URL·날짜가 섹션으로
    잡힌다. 대괄호로 감싼 것이 실제 목차 마커라 그쪽을 우선한다.
    """
    text = " ".join(text.split())
    if not (2 <= len(text) <= 40):
        return None
    if _SECTION_REJECT.search(text):
        return None
    return text


def extract_links(body, channel: str) -> list[dict]:
    """본문에서 같은 채널의 글 링크를 소제목 문맥과 함께 뽑는다."""
    found: list[dict] = []
    current = "(머리말)"
    bracketed = None

    for el in body.descendants:
        name = getattr(el, "name", None)
        if name in ("h1", "h2", "h3", "h4", "strong", "b"):
            sec = clean_section(el.get_text(" ", strip=True))
            if sec:
                current = sec
                if sec.startswith("[") and sec.endswith("]"):
                    bracketed = sec
        elif name == "a" and el.get("href"):
            m = re.search(r"arca\.live/b/([a-z0-9]+)/(\d+)", el["href"]) or re.match(
                r"/b/([a-z0-9]+)/(\d+)", el["href"]
            )
            if not m or m.group(1) != channel:
                continue
            anchor = " ".join(el.get_text(" ", strip=True).split())[:80]
            if anchor.startswith("http"):
                anchor = ""  # 앵커가 URL 그대로면 라벨로 쓸 수 없다
            found.append(
                {
                    "id": int(m.group(2)),
                    "section": bracketed or current,
                    "anchor": anchor,
                }
            )
    return found


# ------------------------------------------------------------------- 저장/병합


def load_post(pid: int) -> dict | None:
    path = POSTS / f"{pid}.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def is_done(pid: int) -> bool:
    """ok 로 저장된 글만 건너뛴다. 실패/차단 건은 다시 시도해야 결손이 안 굳는다."""
    existing = load_post(pid)
    return bool(existing and existing.get("status") == "ok")


def merge_refs(old: list[dict], new: list[dict]) -> list[dict]:
    """참조 정보를 덮어쓰지 않고 합친다.

    같은 글을 여러 허브가 가리키고, 나중에 카테고리 수집을 돌려도
    앞서 쌓인 라벨이 날아가면 안 된다.
    """
    merged = list(old)
    seen = {(r.get("hub"), r.get("section"), r.get("anchor")) for r in merged}
    for r in new:
        key = (r.get("hub"), r.get("section"), r.get("anchor"))
        if key not in seen:
            seen.add(key)
            merged.append(r)
    return merged


def save_post(post: dict, refs: list[dict]) -> str:
    """글을 저장하고 처리 결과를 문자열로 돌려준다."""
    pid = post["id"]
    existing = load_post(pid) or {}

    post["refs"] = merge_refs(existing.get("refs", []), refs)

    # 수정된 글은 이전 본문을 남겨둔다. 나중에 위키 내용을 역추적할 때 필요하다.
    versions = existing.get("versions", [])
    if (
        existing.get("status") == "ok"
        and existing.get("content_hash")
        and existing["content_hash"] != post["content_hash"]
    ):
        versions.append(
            {
                "content_hash": existing["content_hash"],
                "body": existing.get("body", ""),
                "captured_at": existing.get("fetched_at", ""),
            }
        )
    post["versions"] = versions

    (POSTS / f"{pid}.json").write_text(
        json.dumps(post, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    return "갱신" if existing else "신규"


def stub(pid: int, channel: str, status: str, refs: list[dict]) -> None:
    """본문을 못 받은 글도 기록은 남긴다. status 가 ok 가 아니라 다음에 재시도된다."""
    existing = load_post(pid) or {}
    existing.update(
        {
            "id": pid,
            "url": f"{BASE}/b/{channel}/{pid}",
            "channel": channel,
            "status": status,
            "refs": merge_refs(existing.get("refs", []), refs),
            "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    (POSTS / f"{pid}.json").write_text(
        json.dumps(existing, ensure_ascii=False, indent=1), encoding="utf-8"
    )


# --------------------------------------------------------------------- 파싱


def parse_post(html: str, channel: str, pid: int) -> dict:
    soup = BeautifulSoup(html, "lxml")

    title_el = soup.select_one(".article-head .title")
    category_el = soup.select_one(".article-head .category-badge")
    body_el = soup.select_one(".article-content")
    date_el = soup.select_one(".article-info time, time")

    title = ""
    if title_el:
        clone = BeautifulSoup(str(title_el), "lxml")
        for badge in clone.select(".badge"):
            badge.decompose()
        title = clone.get_text(" ", strip=True)

    images: list[str] = []
    body_text = ""
    links: list[dict] = []
    if body_el:
        for img in body_el.select("img, video source, video"):
            src = img.get("src") or img.get("data-src") or ""
            if src:
                images.append(src if src.startswith("http") else "https:" + src)
        body_text = body_el.get_text("\n", strip=True)
        links = extract_links(body_el, channel)

    comments: list[dict] = []
    for c in soup.select(".comment-item"):
        c_body = c.select_one(".message, .text")
        text = c_body.get_text("\n", strip=True) if c_body else ""
        if text:
            comments.append({"text": text})

    info = soup.select_one(".article-info")
    info_text = info.get_text(" ", strip=True) if info else ""
    views = parse_int((re.search(r"조회\s*수?\s*([\d,]+)", info_text) or [None, None])[1])

    vote_el = soup.select_one(".vote-area .vote-count, #recommendCount")
    recommend = parse_int(vote_el.get_text() if vote_el else None)
    if not recommend:
        m = re.search(r"추천\s*수?\s*(-?[\d,]+)", info_text)
        if m:
            recommend = parse_int(m.group(1))

    return {
        "id": pid,
        "url": f"{BASE}/b/{channel}/{pid}",
        "channel": channel,
        "status": "ok",
        "title": title,
        "category": category_el.get_text(strip=True) if category_el else "",
        "date": date_el.get("datetime") if date_el and date_el.get("datetime") else "",
        "views": views,
        "recommend": recommend,
        "body": body_text,
        "comments": comments,
        "images": images,
        "outlinks": links,
        "content_hash": hashlib.sha256(body_text.encode("utf-8")).hexdigest()[:16],
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


# --------------------------------------------------------------------- 수집


def crawl_one(
    pid: int, channel: str, refs: list[dict], since: str | None = None
) -> tuple[str, dict | None]:
    """글 하나를 받아 저장한다. (status, post) 를 돌려준다.

    since 가 있으면 그보다 오래된 글은 저장하지 않고 'old' 로 표시한다 (ADR-0004).
    허브가 링크한 글은 날짜와 무관하게 받으므로, 이 필터는 카테고리 수집에만 건다.
    """
    status, html = fetch(f"{BASE}/b/{channel}/{pid}")
    if status != "ok" or not html:
        stub(pid, channel, status, refs)
        return status, None

    post = parse_post(html, channel, pid)

    if since and post["date"] and post["date"][:10] < since:
        stub(pid, channel, "old", refs)
        return "old", None

    # 본문도 이미지도 없으면 정상 수집으로 보지 않는다
    if not post["body"].strip() and not post["images"]:
        stub(pid, channel, "empty", refs)
        return "empty", None

    save_post(post, refs)
    return "ok", post


def collect_ids(channel: str, pages: int, category: str | None) -> list[int]:
    ids: list[int] = []
    seen: set[int] = set()
    for page in range(1, pages + 1):
        url = f"{BASE}/b/{channel}?p={page}"
        if category:
            url += f"&category={requests.utils.quote(category)}"
        status, html = fetch(url)
        if status != "ok" or not html:
            break
        soup = BeautifulSoup(html, "lxml")
        page_ids = 0
        for row in soup.select("a.vrow"):
            if "notice" in (row.get("class") or []):
                continue
            m = re.match(r"/b/[^/]+/(\d+)", row.get("href") or "")
            if not m:
                continue
            pid = int(m.group(1))
            if pid in seen:
                continue
            seen.add(pid)
            ids.append(pid)
            page_ids += 1
        print(f"[목록] p{page}  글 {page_ids}개 (누적 {len(ids)})")
        if page_ids == 0:
            break
        polite_sleep()
    return ids


def crawl_seeds(channel: str, limit: int) -> None:
    """허브를 받아 링크 그래프를 만들고, 참조된 글을 수집한다."""
    print(f"[1단계] 허브 {len(SEED_HUBS)}건 수집\n")

    graph: dict[int, list[dict]] = {}
    for pid, name in SEED_HUBS.items():
        if is_done(pid):
            post = load_post(pid)
            print(f"  {name:<10} 기존 사용")
        else:
            status, post = crawl_one(pid, channel, [{"hub": "(시드)", "section": "", "anchor": name}])
            if status != "ok" or not post:
                print(f"  {name:<10} 실패 ({status})")
                polite_sleep()
                continue
            polite_sleep()
        for link in (post or {}).get("outlinks", []):
            if link["id"] in SEED_HUBS:
                continue
            graph.setdefault(link["id"], []).append(
                {"hub": name, "section": link["section"], "anchor": link["anchor"]}
            )
        print(f"  {name:<10} 링크 {len((post or {}).get('outlinks', []))}개")

    targets = sorted(graph, key=lambda k: -len({r["hub"] for r in graph[k]}))
    todo = [t for t in targets if not is_done(t)]
    if limit:
        todo = todo[:limit]

    print(f"\n[2단계] 참조된 고유 글 {len(targets)}건 / 신규 {len(todo)}건")
    print(f"        간격 {DELAY_BASE}~{DELAY_BASE + DELAY_JITTER}초 "
          f"→ 예상 {len(todo) * (DELAY_BASE + DELAY_JITTER / 2) / 60:.0f}분\n")

    counts: dict[str, int] = {}
    consecutive = 0
    for n, pid in enumerate(todo, 1):
        refs = graph[pid]
        status, post = crawl_one(pid, channel, refs)
        counts[status] = counts.get(status, 0) + 1

        if status == "ok":
            consecutive = 0
            hubs = ",".join(sorted({r["hub"] for r in refs}))
            print(f"[{n}/{len(todo)}] {pid} 본문{len(post['body']):>6}자 "
                  f"댓글{len(post['comments']):>3} 추천{post['recommend']:>4} "
                  f"| {hubs[:18]:<18} | {post['title'][:30]}")
        else:
            consecutive += 1
            print(f"[{n}/{len(todo)}] {pid} {status}")
            if consecutive >= MAX_CONSECUTIVE_FAILURES:
                print(f"\n연속 실패 {consecutive}회. 차단 가능성이 있어 중단합니다.",
                      file=sys.stderr)
                break
        polite_sleep()

    print("\n[결과]")
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {k:<10} {v:>4}건")


# --------------------------------------------------------------------- 점검


COOKIE_HELP = f"""  cookie.txt 를 만들거나 갱신하세요:
    1. 브라우저에서 arca.live 로그인
    2. F12 → Network 탭 → 페이지 새로고침
    3. 아무 arca.live 요청 클릭 → Request Headers 의 Cookie: 값 전체 복사
    4. {COOKIE_FILE} 에 한 줄로 붙여넣기"""


def check_access(channel: str) -> bool:
    """같은 목록을 쿠키 있이/없이 받아 비교한다. 로그인 전용 글이 보이면 성공."""
    url = f"{BASE}/b/{channel}"
    print("[검사] 로그인 상태 확인 중...\n")

    status, html = fetch(url)
    if status != "ok" or not html:
        print(f"  요청 실패 ({status})")
        return False

    logged_in = "/u/logout" in html
    polite_sleep(2.0)

    anon = requests.Session()
    anon.headers.update(HEADERS)
    try:
        anon_html = anon.get(url, timeout=20).text
    except requests.RequestException as e:
        print(f"  비교 요청 실패: {type(e).__name__}")
        return False

    mine, base = ids_of(html), ids_of(anon_html)
    print(f"  쿠키 적용       {'Cookie' in session.headers}")
    print(f"  로그인 상태     {logged_in}")
    print(f"  비로그인 목록   {len(base):>3}건")
    print(f"  현재 세션 목록  {len(mine):>3}건")
    print(f"  로그인 전용     {len(mine - base):>3}건\n")

    if not logged_in:
        print("  판정: 로그인 안 됨.")
        print(COOKIE_HELP)
        return False
    print("  판정: 로그인 확인.")
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="aiart")
    ap.add_argument("--seeds", action="store_true", help="허브 모드 (기본)")
    ap.add_argument("--pages", type=int, default=0, help="카테고리 모드: 목록 페이지 수")
    ap.add_argument("--category", default=None)
    ap.add_argument("--limit", type=int, default=0, help="수집 개수 상한")
    ap.add_argument("--since", default=None,
                    help="이 날짜(YYYY-MM-DD)보다 오래된 글은 건너뛴다. 카테고리 수집용 (ADR-0004)")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    POSTS.mkdir(exist_ok=True)
    has_cookie = load_cookie()
    print(f"쿠키: {'cookie.txt 로드됨' if has_cookie else '없음 (비로그인)'}\n")

    try:
        if args.check:
            sys.exit(0 if check_access(args.channel) else 1)

        if args.pages:
            ids = collect_ids(args.channel, args.pages, args.category)
            todo = [i for i in ids if not is_done(i)]
            if args.limit:
                todo = todo[: args.limit]
            print(f"\n대상 {len(ids)}건 / 신규 {len(todo)}건\n")
            consecutive = 0
            for n, pid in enumerate(todo, 1):
                status, post = crawl_one(pid, args.channel, [], since=args.since)
                if status == "ok":
                    consecutive = 0
                    print(f"[{n}/{len(todo)}] {pid} 본문{len(post['body']):>6}자 "
                          f"| {post['title'][:34]}")
                else:
                    consecutive += 1
                    print(f"[{n}/{len(todo)}] {pid} {status}")
                    if consecutive >= MAX_CONSECUTIVE_FAILURES:
                        print("\n연속 실패로 중단.", file=sys.stderr)
                        break
                polite_sleep()
        else:
            crawl_seeds(args.channel, args.limit)

    except Blocked as e:
        print(f"\n차단 신호 감지 ({e}). 즉시 중단합니다.", file=sys.stderr)
        print("한동안 쉬었다가 다시 실행하세요. 수집한 것은 그대로 남습니다.",
              file=sys.stderr)
        sys.exit(2)
    except KeyboardInterrupt:
        print("\n중단됨. 다시 실행하면 이어서 받습니다.", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
