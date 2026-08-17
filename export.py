"""DB → 마크다운 → MkDocs.

마크다운은 원본이 아니라 빌드 산출물이다 (ADR-0001). 원본은 항상 Postgres 이고,
이 스크립트는 언제든 다시 돌려서 site/ 를 통째로 다시 만들 수 있다.

usage:
    python export.py
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import queue_api as q

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

ROOT = Path(__file__).parent
OUT = ROOT / "site_src"


def reconcile_sources(cur) -> int:
    """`page_sources` 를 항목별 인용(`wiki_entry_sources`)에 맞춘다.

    문서를 다시 쓰면 인용이 끊긴 원문이 `page_sources` 에 남는다. 그대로 두면
    문서 머리의 압축률과 꼬리의 출처 목록이 **쓰지도 않은 글을 쓴 것처럼** 보여준다.
    위키가 거짓말을 하게 되므로 내보내기 전에 맞춘다.

    항목이 아직 하나도 없는 문서는 건드리지 않는다 — 작성 중일 수 있다.
    """
    cur.execute(
        """DELETE FROM page_sources ps
            WHERE ps.page_id IN (
                    SELECT e.page_id FROM wiki_entries e
                    JOIN wiki_entry_sources es ON es.entry_id = e.id
                  )
              AND NOT EXISTS (
                    SELECT 1 FROM wiki_entries e
                    JOIN wiki_entry_sources es ON es.entry_id = e.id
                    WHERE e.page_id = ps.page_id AND es.post_id = ps.post_id
                  )"""
    )
    return cur.rowcount


SRC_SHOWN = 4  # 이보다 많으면 접어 둔다. 근거 12건이 본문보다 길어지면 안 읽힌다.
TITLE_MAX = 34
BLURB_MAX = 100

_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_SENT = re.compile(r"(?<=다)\.(?:\s|$)|\.\s")


def blurb(intro: str | None) -> str:
    """표지 목록에 붙는 한 줄 소개.

    `intro.split(".")` 로 자르면 마크다운 링크의 `.md` 가 먼저 걸려
    `— [설치와 환경 구성](install` 처럼 링크 한복판에서 끊긴다.
    링크를 글자로 되돌린 다음 문장 끝에서 자른다.
    """
    if not intro:
        return ""
    text = _LINK.sub(r"\1", intro).replace("**", "").strip()
    text = " ".join(text.split())  # 줄바꿈을 공백으로
    m = _SENT.search(text)
    if m:
        text = text[: m.start() + 1]
    if len(text) > BLURB_MAX:
        text = text[:BLURB_MAX].rsplit(" ", 1)[0] + "…"
    return text


def demote_headings(body: str) -> str:
    """항목 본문 안의 `##` 제목을 한 단계 내린다.

    항목 제목 자체가 `##` 로 나가므로, 본문이 또 `##` 를 쓰면 같은 급으로 붙어서
    목차가 어긋나고 항목 끝의 '근거' 줄이 엉뚱한 자리에 붙는다.
    코드 블록 안의 `#` 는 주석이나 셸 프롬프트라 건드리면 안 된다.
    """
    out, fence = [], False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and line.startswith("## ") and not line.startswith("### "):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def entry_sources_md(rows: list[dict]) -> list[str]:
    """항목 바로 아래에 붙는 근거 줄.

    읽다가 "이 말은 어디서 나왔나" 를 그 자리에서 확인할 수 있어야 한다.
    문서 맨 아래 목록만으로는 어느 대목이 어느 글에서 왔는지 알 수 없다.
    """
    if not rows:
        return []

    def one(r: dict) -> str:
        t = r["title"]
        if len(t) > TITLE_MAX:
            t = t[: TITLE_MAX - 1] + "…"
        t = t.replace("[", "(").replace("]", ")")  # 링크 문법이 깨지지 않게
        when = f" {r['posted_at']:%y.%m}" if r["posted_at"] else ""
        return f"[{t}{when}]({r['url']})"

    head = " · ".join(one(r) for r in rows[:SRC_SHOWN])
    if len(rows) <= SRC_SHOWN:
        return [f"<small>근거 — {head}</small>", ""]

    rest = " · ".join(one(r) for r in rows[SRC_SHOWN:])
    return [
        f"<small>근거 — {head}</small>",
        "",
        f'??? note "근거 {len(rows)}건 전부 보기"',
        f"    {head} · {rest}",
        "",
    ]


def main() -> None:
    (OUT / "docs").mkdir(parents=True, exist_ok=True)

    with q._conn() as c, c.cursor() as cur:
        dropped = reconcile_sources(cur)
        c.commit()
        if dropped:
            print(f"출처 정리: 인용이 끊긴 {dropped}건 제거")

        cur.execute(
            "SELECT id, slug, title, section, kind, stage, intro, generated_at FROM wiki_pages "
            "WHERE published ORDER BY title"
        )
        pages = cur.fetchall()

        for p in pages:
            cur.execute(
                """SELECT id, seq, heading, body_md, confidence, as_of, has_conflict
                   FROM wiki_entries WHERE page_id=%s ORDER BY seq""",
                (p["id"],),
            )
            entries = cur.fetchall()

            cur.execute(
                """SELECT DISTINCT po.id, po.title, po.url, po.posted_at, po.recommend
                   FROM page_sources ps JOIN posts po ON po.id = ps.post_id
                   WHERE ps.page_id=%s ORDER BY po.recommend DESC""",
                (p["id"],),
            )
            sources = cur.fetchall()

            # 항목마다 근거 원문. 아래 '출처' 목록만 있으면 어떤 대목이 어느 글에서
            # 왔는지 알 수 없어서, 읽다가 확인하려면 목록 전체를 뒤져야 한다.
            cur.execute(
                """SELECT es.entry_id, po.id, po.title, po.url, po.posted_at
                   FROM wiki_entries e
                   JOIN wiki_entry_sources es ON es.entry_id = e.id
                   JOIN posts po ON po.id = es.post_id
                   WHERE e.page_id = %s
                   ORDER BY es.entry_id, po.recommend DESC""",
                (p["id"],),
            )
            by_entry: dict[int, list[dict]] = {}
            for r in cur.fetchall():
                by_entry.setdefault(r["entry_id"], []).append(r)

            # 이 문서가 실제로 인용한 원문에서 나온 주장만 센다.
            # 섹션으로 고르면 같은 섹션의 다른 문서 주장까지 딸려와, 원문 7편짜리
            # 문서가 주장 86개를 나열하는 꼴이 된다 — 읽는 사람이 오해한다.
            cur.execute(
                """SELECT cs.canonical, cs.support, cs.contradict, cs.earliest, cs.latest
                   FROM claim_strength cs
                   WHERE EXISTS (
                       SELECT 1
                         FROM card_claims cc
                         JOIN knowledge_cards k ON k.id = cc.card_id
                         JOIN wiki_entries e ON e.page_id = %s
                         JOIN wiki_entry_sources es
                              ON es.entry_id = e.id AND es.post_id = k.post_id
                        WHERE cc.claim_id = cs.claim_id
                   )
                   ORDER BY cs.support DESC""",
                (p["id"],),
            )
            claims = cur.fetchall()

            L: list[str] = [f"# {p['title']}", ""]
            # 압축률. 이 프로젝트가 일하고 있다는 유일한 지표다 (ADR-0005).
            L.append(
                f"> **원문 {len(sources)}건 → 이 문서 하나** · 주장 {len(claims)}개 · "
                f"정리 {p['generated_at']:%Y-%m-%d}"
            )
            L.append("")
            if p["intro"]:
                L.append(p["intro"])
                L.append("")

            for e in entries:
                L.append(f"## {e['heading']}")
                mark = []
                if e["as_of"]:
                    old = (date.today() - e["as_of"]).days > 365
                    mark.append(f"{'⚠️ ' if old else ''}{e['as_of']:%Y-%m} 기준")
                # 근거는 범주 대신 **개수**로 적는다. `medium` 이 전체의 69% 라
                # "근거 보통" 은 거의 모든 항목에 붙어 아무것도 가려 주지 못했다.
                # "근거 3건" 은 읽는 사람이 스스로 무게를 잴 수 있는 정보다.
                n_src = len(by_entry.get(e["id"], []))
                if n_src:
                    mark.append(f"근거 {n_src}건")
                if e["confidence"] == "low":
                    mark.append("**근거 약함**")
                if e["has_conflict"]:
                    mark.append("자료 엇갈림")
                if mark:
                    L.append(f"<small>{' · '.join(mark)}</small>")
                L.append("")
                L.append(demote_headings(e["body_md"]))
                L.append("")
                L += entry_sources_md(by_entry.get(e["id"], []))

            if claims:
                # 근거가 센 것부터 자른다. 감춘 개수는 반드시 밝힌다 —
                # 조용히 잘라내면 "이게 전부"로 읽힌다.
                CLAIM_LIMIT = 40
                shown, hidden = claims[:CLAIM_LIMIT], max(0, len(claims) - CLAIM_LIMIT)
                L.append("## 이 문서가 딛고 선 주장")
                L.append("")
                L.append(
                    "이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, "
                    "근거가 1건뿐인 주장은 그만큼 약하다."
                )
                if hidden:
                    L.append("")
                    L.append(f"근거가 센 {CLAIM_LIMIT}개만 싣는다 (나머지 {hidden}개는 생략).")
                L.append("")
                L.append("| 주장 | 찬성 | 반대 | 시점 |")
                L.append("|---|---:|---:|---|")
                for cl in shown:
                    span = (
                        f"{cl['earliest']:%Y-%m}"
                        if cl["earliest"] == cl["latest"]
                        else f"{cl['earliest']:%Y-%m}~{cl['latest']:%Y-%m}"
                    ) if cl["earliest"] else "—"
                    L.append(f"| {cl['canonical']} | {cl['support']} | {cl['contradict']} | {span} |")
                L.append("")

            # 역링크 — 이 문서가 개체 문서일 때, 이 개체를 언급하는 다른 문서들
            cur.execute(
                """SELECT DISTINCT b.page_slug, b.page_title, b.kind, b.mentions
                   FROM entity_backlinks b
                   JOIN entities e ON e.id = b.entity_id
                   WHERE e.page_id = %s AND b.page_id <> %s
                   ORDER BY b.mentions DESC""",
                (p["id"], p["id"]),
            )
            backlinks = cur.fetchall()

            # 함께 등장하는 개체 — "관련 항목"
            cur.execute(
                """SELECT e2.name, e2.slug, e2.page_id, co.together
                   FROM entities e1
                   JOIN entity_cooccurrence co ON co.entity_id = e1.id
                   JOIN entities e2 ON e2.id = co.related_id
                   WHERE e1.page_id = %s
                   ORDER BY co.together DESC LIMIT 12""",
                (p["id"],),
            )
            related = cur.fetchall()

            if backlinks or related:
                L.append("## 이 문서와 이어진 곳")
                L.append("")
                if backlinks:
                    L.append("**이 개체를 다루는 다른 문서**")
                    L.append("")
                    for b in backlinks:
                        L.append(f"- [{b['page_title']}]({b['page_slug']}.md) ({b['kind']})")
                    L.append("")
                if related:
                    L.append("**함께 등장하는 것들** — 숫자는 같은 글에 함께 나온 횟수")
                    L.append("")
                    line = []
                    for r in related:
                        label = (
                            f"[{r['name']}]({r['slug']}.md)" if r["page_id"] else r["name"]
                        )
                        line.append(f"{label} {r['together']}")
                    L.append(" · ".join(line))
                    L.append("")

            L.append("## 출처")
            L.append("")
            L.append("본문은 아카라이브에 있다. 여기서는 링크만 건다.")
            L.append("")
            for s in sources:
                when = f"{s['posted_at']:%Y-%m}" if s["posted_at"] else "?"
                L.append(f"- [{s['title']}]({s['url']}) — {when}, 추천 {s['recommend']}")

            (OUT / "docs" / f"{p['slug']}.md").write_text("\n".join(L), encoding="utf-8")
            print(f"  {p['slug']}.md  항목{len(entries)} 원문{len(sources)} 주장{len(claims)}")

        # 표지
        cur.execute(
            """SELECT (SELECT count(*) FROM posts WHERE status='ok') posts,
                      (SELECT count(*) FROM comments) comments,
                      (SELECT count(*) FROM knowledge_cards) cards,
                      (SELECT count(*) FROM claims) claims,
                      (SELECT count(*) FROM work_queue WHERE job='extract' AND status='pending') pending"""
        )
        st = cur.fetchone()

    idx = [
        "# AI그림채널 위키",
        "",
        "아카라이브 AI그림채널 글을 주제별로 압축한 것이다. "
        "원문을 다 읽지 않고도 짤·비디오를 만들 수 있게 하는 것이 목적이다.",
        "",
    ]

    # 처음 오는 사람이 어디로 갈지 알 수 있게, 종류별로 묶는다.
    ORDER = [
        ("개념", "**모르는 게 있으면 여기부터**"),
        ("튜토리얼", "**따라 하기**"),
        ("국룰", "**채널 기본값**"),
        ("가이드", "**주제별**"),
        ("개체", "**모델·도구별**"),
        ("문제해결", "**막혔을 때**"),
        ("자원", "**받는 곳**"),
        ("용어", ""),
    ]
    by_kind: dict[str, list] = {}
    for p in pages:
        by_kind.setdefault(p.get("kind") or "가이드", []).append(p)

    for kind, label in ORDER:
        items = by_kind.pop(kind, [])
        if not items:
            continue
        idx.append(f"## {kind}" + (f"  <small>{label}</small>" if label else ""))
        idx.append("")
        for p in items:
            b = blurb(p["intro"])
            idx.append(f"- [{p['title']}]({p['slug']}.md)" + (f" — {b}" if b else ""))
        idx.append("")
    for kind, items in by_kind.items():  # 분류에 없는 종류가 생기면 뒤에 붙인다
        idx.append(f"## {kind}")
        idx.append("")
        for p in items:
            idx.append(f"- [{p['title']}]({p['slug']}.md)")
        idx.append("")

    # 터널 주소는 컨테이너를 재시작할 때마다 바뀐다. 표지에 적어두면
    # 어디서 보든 현재 주소를 알 수 있다.
    url_file = ROOT / "TUNNEL_URL.txt"
    if url_file.exists():
        url = url_file.read_text(encoding="utf-8").strip()
        if url:
            idx += [
                "",
                f"> 이 위키의 현재 주소: <{url}>",
                "> 임시 터널이라 서버를 다시 띄우면 주소가 바뀐다.",
            ]

    idx += [
        "",
        "## 지금까지",
        "",
        "| | |",
        "|---|---:|",
        f"| 수집한 원문 | {st['posts']:,} |",
        f"| 수집한 댓글 | {st['comments']:,} |",
        f"| 지식카드 | {st['cards']:,} |",
        f"| 주장(Claim) | {st['claims']:,} |",
        f"| 추출 대기 | {st['pending']:,} |",
        "",
        "## 읽는 법",
        "",
        "- **⚠️ 표시**는 1년이 넘은 정보다. 이 분야는 반년이면 낡는다.",
        "- **근거 N건**은 그 항목이 원문 몇 편에 기대고 있는지다. 1건이면 그만큼 약하다.",
        "- **근거 약함**은 건수와 별개다 — 여러 글이 있어도 **서로 어긋나 결론이 안 난** 것이다.",
        "- **자료 엇갈림**이 붙은 항목은 양쪽 주장을 다 적어 두었다. 골라 읽으면 된다.",
        "- 각 문서 끝의 **주장 목록**은 몇 개의 글이 같은 말을 하는지 센 것이다.",
        "- 본문은 전부 아카라이브 원문 링크로 확인할 수 있다.",
    ]
    (OUT / "docs" / "index.md").write_text("\n".join(idx), encoding="utf-8")

    (OUT / "mkdocs.yml").write_text(
        """site_name: AI그림채널 위키
theme:
  name: material
  language: ko
  palette:
    - scheme: default
      toggle: {icon: material/weather-night, name: 다크 모드}
    - scheme: slate
      toggle: {icon: material/weather-sunny, name: 라이트 모드}
  features: [navigation.instant, navigation.top, search.suggest, content.code.copy]
markdown_extensions:
  - tables
  - admonition
  - attr_list
  - md_in_html
  - pymdownx.superfences
  # 항목별 근거가 많을 때 접어 두는 데 쓴다. 없으면 `???` 가 글자 그대로 나온다.
  - pymdownx.details
plugins:
  - search:
      lang: ko
""",
        encoding="utf-8",
    )
    print(f"\nsite_src/ 생성 완료 — 문서 {len(pages)}개")


if __name__ == "__main__":
    main()
