# arcawiki 지식층 구현 플랜

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 원본 → 위키 직행 구조를, 원안대로 `원본 → 지식카드 → Claim → 위키` 4층으로 되돌리고, 그 위에 Claude Code 가 큐를 소비하는 스킬을 얹는다.

**Architecture:** Docker 안의 `pipeline` 컨테이너가 수집·적재·변경감지·큐적재까지 판단 없이 자동 수행한다(ADR-0006). LLM 이 필요한 세 단계 — Extractor(글→지식카드), Resolver(카드→Claim 통합), WikiWriter(Claim+카드→문서) — 는 `work_queue` 를 통해 Claude Code 세션에 위임된다. WikiWriter 는 원문을 읽지 않고 지식카드와 Claim 만 읽는다. 웹은 DB 를 읽기만 한다(ADR-0002).

**Tech Stack:** PostgreSQL 17 + pgvector, Python 3.13 (psycopg3, requests, bs4/lxml), Docker Compose, Claude Code 스킬

## Global Constraints

- **원본 불변**: `posts` 테이블과 `posts/*.json` 은 수집 이후 수정하지 않는다. 위키는 언제든 재생성 가능해야 한다.
- **멱등**: 모든 적재·큐적재는 몇 번을 다시 돌려도 결과가 같아야 한다. `refs` 는 병합만 하고 삭제하지 않는다.
- **status 가 `ok` 인 글만 재수집에서 건너뛴다.** 실패·차단 건은 다시 시도한다.
- **LLM 호출은 Claude Code 세션 안에서만** 일어난다. `pipeline.py`, 웹, 컨테이너는 LLM 을 호출하지 않는다 (ADR-0002, ADR-0006).
- **출처 없는 지식은 저장하지 않는다.** 모든 지식카드는 `post_id` 를, 모든 Claim 은 최소 1건의 카드를 근거로 가진다.
- **시점 필수**: 지식카드와 Claim 은 근거 원문의 `posted_at` 을 물려받는다 (ADR-0004).
- **주제 우선순위** (ADR-0005): 비디오 10 / ANIMA 20 / ComfyUI 30 / VRAM 40 / 프롬프트 50 / LoRA 60 / 기타 90. 낮을수록 먼저.
- **rate**: 수집 간격 5~7초, 451·429·403 은 재시도 없이 중단.
- 커밋 메시지는 한국어 한 줄 요약. 각 태스크 끝에 커밋한다.

---

## 현재 상태 (플랜 시작 시점)

이미 있는 것:

| 항목 | 상태 |
|---|---|
| `crawler.py` | 동작. 허브 링크추적 + 카테고리 수집, status/refs 병합, 차단 감지 |
| `ingest.py` | 동작. `posts/*.json` → Postgres 멱등 적재 |
| `pipeline.py` | 작성됨. 수집→적재→큐적재 순환. **아직 컨테이너화 안 됨** |
| `db/schema.sql` | 적용됨. RAW + WIKI 층 |
| `db/002-work-queue.sql` | 적용됨. `work_queue`, `page_sources`, 3개 뷰 |
| Postgres | `127.0.0.1:5433` 가동 중. posts 1,149 / comments 13,966 / refs 388 / queue 983 |
| `wiki/lora-학습.md` | 형식 검증용 목업 (DB 미반영) |

없는 것: **지식카드 층, Claim 층, 벡터, Source Adapter 구조, 스킬 3종, 웹**

정리 대상: 루트의 일회성 산출물 `*.txt` 14개 (`audit.txt`, `lora_dump.txt`, `probe2.txt` 등)

---

## 파일 구조

```
arcawiki/
├── db/
│   ├── schema.sql              (있음) RAW + WIKI
│   ├── 002-work-queue.sql      (있음) 작업 큐
│   └── 003-knowledge.sql       [Task 1] 지식카드 + Claim + 벡터 컬럼
├── sources/                    [Task 2] Source Adapter — 사이트 의존 코드 격리
│   ├── __init__.py
│   ├── base.py                 Source 추상 클래스, Post 데이터클래스
│   └── arcalive.py             아카라이브 구현 (crawler.py 에서 이관)
├── crawler.py                  [Task 2] Adapter 를 쓰도록 수정
├── ingest.py                   (있음)
├── pipeline.py                 [Task 3] 컨테이너용 진입점으로 정리
├── Dockerfile.pipeline         [Task 3]
├── docker-compose.yml          [Task 3] pipeline 서비스 + pgvector 이미지
├── queue_api.py                [Task 4] 스킬이 큐를 읽고 쓰는 얇은 함수 모음
├── .claude/skills/
│   ├── extract/SKILL.md        [Task 5] 글 → 지식카드
│   ├── resolve/SKILL.md        [Task 6] 카드 → Claim 통합
│   └── write-wiki/SKILL.md     [Task 7] Claim+카드 → 문서
├── tests/
│   ├── test_sources.py         [Task 2]
│   ├── test_queue_api.py       [Task 4]
│   └── test_knowledge.py       [Task 1]
└── docs/adr/                   (있음) 0001~0006
```

**Task 8(벡터)과 Task 9(웹)는 지식층이 실제로 채워진 뒤에 착수한다.** 카드가 0건인 상태에서 벡터 인덱스를 만들 이유가 없다.

---

### Task 1: 지식카드 + Claim 스키마

원안의 `KNOWLEDGE DB` 와 `Claim Ledger` 를 만든다. 지금은 `posts → wiki_entries` 직행이라, 문서를 다시 쓸 때마다 원문 수천 건을 다시 읽어야 하고 "몇 개의 글이 같은 주장을 하는가"를 셀 수 없다.

**Files:**
- Create: `db/003-knowledge.sql`
- Create: `tests/test_knowledge.py`

**Interfaces:**
- Consumes: `posts(id, posted_at, content_hash)`, `wiki_entries(id)` from existing schema
- Produces: 테이블 `knowledge_cards`, `card_claims`, `claims`, `claim_sources`; 뷰 `claim_strength`, `pending_resolution`

- [ ] **Step 1: 실패하는 테스트를 쓴다**

```python
# tests/test_knowledge.py
import os, psycopg, pytest

DSN = os.environ["DATABASE_URL"]

@pytest.fixture
def conn():
    with psycopg.connect(DSN) as c:
        yield c
        c.rollback()

def test_지식카드는_출처_없이_저장할_수_없다(conn):
    """출처 없는 지식은 LLM 이 지어낸 것이다 (Global Constraints)."""
    with conn.cursor() as cur, pytest.raises(psycopg.errors.NotNullViolation):
        cur.execute(
            "INSERT INTO knowledge_cards (post_id, topic, summary) VALUES (NULL, 'x', 'y')"
        )

def test_같은_글에_같은_추출버전_카드는_하나만(conn):
    """재추출을 돌려도 카드가 중복으로 쌓이면 안 된다."""
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM posts WHERE status='ok' LIMIT 1")
        pid = cur.fetchone()[0]
        for _ in range(2):
            cur.execute(
                """INSERT INTO knowledge_cards (post_id, extractor_version, topic, summary)
                   VALUES (%s, 'v1', 'LoRA', '요약')
                   ON CONFLICT (post_id, extractor_version) DO NOTHING""",
                (pid,),
            )
        cur.execute(
            "SELECT count(*) FROM knowledge_cards WHERE post_id=%s AND extractor_version='v1'",
            (pid,),
        )
        assert cur.fetchone()[0] == 1

def test_claim_strength_는_찬반을_센다(conn):
    """여러 글이 같은 주장을 하는지가 위키의 신뢰도 근거가 된다."""
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM posts WHERE status='ok' ORDER BY id LIMIT 3")
        pids = [r[0] for r in cur.fetchall()]
        cur.execute(
            "INSERT INTO claims (canonical) VALUES ('테스트 주장') RETURNING id"
        )
        claim_id = cur.fetchone()[0]
        for pid, rel in zip(pids, ["support", "support", "contradict"]):
            cur.execute(
                """INSERT INTO knowledge_cards (post_id, extractor_version, topic, summary)
                   VALUES (%s,'vtest','t','s') RETURNING id""",
                (pid,),
            )
            card_id = cur.fetchone()[0]
            cur.execute(
                "INSERT INTO card_claims (card_id, claim_id, relation) VALUES (%s,%s,%s)",
                (card_id, claim_id, rel),
            )
        cur.execute(
            "SELECT support, contradict FROM claim_strength WHERE claim_id=%s", (claim_id,)
        )
        assert cur.fetchone() == (2, 1)
```

- [ ] **Step 2: 테스트를 돌려 실패를 확인한다**

Run: `cd /f/Project/arcawiki && DATABASE_URL="postgres://arcawiki:$(grep POSTGRES_PASSWORD .env | cut -d= -f2)@127.0.0.1:5433/arcawiki" python -m pytest tests/test_knowledge.py -v`
Expected: FAIL — `relation "knowledge_cards" does not exist`

- [ ] **Step 3: 스키마를 쓴다**

```sql
-- db/003-knowledge.sql
-- 원안의 KNOWLEDGE DB 와 Claim Ledger.
-- 원본(posts)과 위키(wiki_pages) 사이의 중간층이다. 이 층이 있어야
-- 문서를 다시 쓸 때 원문을 다시 읽지 않아도 되고, 주장의 찬반을 셀 수 있다.

-- 글 하나에서 뽑아낸 구조화된 지식.
CREATE TABLE IF NOT EXISTS knowledge_cards (
    id                BIGSERIAL PRIMARY KEY,
    post_id           BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,

    -- 프롬프트를 고치면 버전을 올린다. 옛 카드를 지우지 않고 나란히 둔다.
    extractor_version TEXT   NOT NULL DEFAULT 'v1',

    topic             TEXT   NOT NULL,          -- 주 주제 (LoRA, ANIMA, 비디오...)
    summary           TEXT   NOT NULL,          -- 이 글이 무엇을 말하는가
    software          TEXT[] NOT NULL DEFAULT '{}',   -- ComfyUI, kohya_ss...
    models            TEXT[] NOT NULL DEFAULT '{}',   -- ANIMA, ILXL, MiniMax H3...
    settings          JSONB  NOT NULL DEFAULT '{}',   -- 구체 수치. 이게 위키의 값어치다
    usefulness        INTEGER NOT NULL DEFAULT 5,     -- 0~10
    as_of             DATE,                            -- 원문 작성 시점을 물려받는다
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),

    -- 같은 글을 같은 버전으로 두 번 추출하지 않는다
    UNIQUE (post_id, extractor_version)
);

CREATE INDEX IF NOT EXISTS cards_topic_idx  ON knowledge_cards (topic);
CREATE INDEX IF NOT EXISTS cards_as_of_idx  ON knowledge_cards (as_of DESC);
CREATE INDEX IF NOT EXISTS cards_settings_idx ON knowledge_cards USING gin (settings);

-- 통합된 주장. 여러 글이 같은 말을 하면 하나로 모인다.
CREATE TABLE IF NOT EXISTS claims (
    id            BIGSERIAL PRIMARY KEY,
    canonical     TEXT NOT NULL,               -- 대표 문장
    topic         TEXT NOT NULL DEFAULT '',
    as_of_earliest DATE,
    as_of_latest   DATE,
    status        TEXT NOT NULL DEFAULT 'open', -- open | settled | disputed | obsolete
    note          TEXT NOT NULL DEFAULT '',
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS claims_topic_idx ON claims (topic);

-- 카드가 주장을 지지하는가 반박하는가.
CREATE TABLE IF NOT EXISTS card_claims (
    card_id  BIGINT NOT NULL REFERENCES knowledge_cards (id) ON DELETE CASCADE,
    claim_id BIGINT NOT NULL REFERENCES claims (id)          ON DELETE CASCADE,
    relation TEXT   NOT NULL,   -- support | contradict | context
    quote    TEXT   NOT NULL DEFAULT '',
    PRIMARY KEY (card_id, claim_id)
);

-- 주장의 찬반 집계. 위키가 "여러 글이 같은 말을 한다" 고 쓸 근거.
CREATE OR REPLACE VIEW claim_strength AS
SELECT c.id AS claim_id,
       c.canonical,
       c.topic,
       count(*) FILTER (WHERE cc.relation = 'support')    AS support,
       count(*) FILTER (WHERE cc.relation = 'contradict') AS contradict,
       min(k.as_of) AS earliest,
       max(k.as_of) AS latest
FROM claims c
LEFT JOIN card_claims cc     ON cc.claim_id = c.id
LEFT JOIN knowledge_cards k  ON k.id = cc.card_id
GROUP BY c.id, c.canonical, c.topic;

-- 아직 Claim 으로 통합되지 않은 카드. Resolver 의 입력.
CREATE OR REPLACE VIEW pending_resolution AS
SELECT k.topic, count(*) AS cards, min(k.as_of) AS earliest, max(k.as_of) AS latest
FROM knowledge_cards k
WHERE NOT EXISTS (SELECT 1 FROM card_claims cc WHERE cc.card_id = k.id)
GROUP BY k.topic
HAVING count(*) >= 3;
```

- [ ] **Step 4: 적용하고 테스트가 통과하는지 본다**

Run:
```bash
cd /f/Project/arcawiki
docker exec -i arcawiki-db psql -U arcawiki -d arcawiki < db/003-knowledge.sql
DATABASE_URL="postgres://arcawiki:$(grep POSTGRES_PASSWORD .env | cut -d= -f2)@127.0.0.1:5433/arcawiki" python -m pytest tests/test_knowledge.py -v
```
Expected: 3 passed

- [ ] **Step 5: 커밋**

```bash
git add db/003-knowledge.sql tests/test_knowledge.py
git commit -m "지식카드와 Claim Ledger 스키마 추가"
```

---

### Task 2: Source Adapter 구조

원안의 `sources/base.py, arcalive.py, reddit.py...` 구조. 지금은 `crawler.py` 에 아카라이브 DOM 셀렉터가 하드코딩돼 있어서, 사이트가 바뀌면 크롤러 전체를 손대야 하고 다른 채널을 붙일 수 없다.

**Files:**
- Create: `sources/__init__.py`, `sources/base.py`, `sources/arcalive.py`
- Modify: `crawler.py` (파싱 로직을 `sources/arcalive.py` 로 이관, Adapter 를 호출하도록)
- Create: `tests/test_sources.py`

**Interfaces:**
- Consumes: 없음 (기반 계층)
- Produces:
  - `sources.base.RawPost` — 데이터클래스. 필드: `id:int, url:str, title:str, category:str, posted_at:str, views:int, recommend:int, body:str, comments:list[str], images:list[str], outlinks:list[dict]`
  - `sources.base.Source` — 추상 클래스. 메서드: `list_ids(pages:int, category:str|None) -> list[int]`, `fetch_post(pid:int) -> tuple[str, RawPost|None]` (status, post)
  - `sources.arcalive.ArcaLive(channel:str)` — `Source` 구현
  - `sources.get_source(name:str, **kw) -> Source` — 팩토리

- [ ] **Step 1: 실패하는 테스트를 쓴다**

```python
# tests/test_sources.py
import pytest
from sources import get_source
from sources.base import RawPost, Source

def test_팩토리가_아카라이브_어댑터를_준다():
    s = get_source("arcalive", channel="aiart")
    assert isinstance(s, Source)

def test_모르는_소스는_거부한다():
    with pytest.raises(ValueError, match="reddit"):
        get_source("reddit")

def test_본문_파싱이_구조를_뽑는다():
    """DOM 셀렉터가 바뀌면 여기서 먼저 깨져야 한다."""
    html = """
    <div class="article-head"><div class="title">
      <span class="badge category-badge">정보/자료</span>테스트 제목</div></div>
    <div class="article-info"><time datetime="2026-01-02T03:04:05.000Z"></time>
      조회수 1,234 추천 56</div>
    <div class="article-content">
      <b>[LoRA/로라 학습]</b>
      <a href="/b/aiart/999">참고글</a>
      본문 내용
      <img src="//img.example/1.png">
    </div>
    <div class="comment-item"><div class="message">댓글 하나</div></div>
    """
    from sources.arcalive import ArcaLive
    post = ArcaLive("aiart").parse(html, 123)
    assert post.id == 123
    assert post.title == "테스트 제목"          # 카테고리 뱃지는 제거된다
    assert post.category == "정보/자료"
    assert post.posted_at.startswith("2026-01-02")
    assert post.views == 1234
    assert post.recommend == 56
    assert "본문 내용" in post.body
    assert post.comments == ["댓글 하나"]
    assert post.images == ["https://img.example/1.png"]
    assert post.outlinks == [
        {"id": 999, "section": "[LoRA/로라 학습]", "anchor": "참고글"}
    ]
```

- [ ] **Step 2: 테스트를 돌려 실패를 확인한다**

Run: `cd /f/Project/arcawiki && python -m pytest tests/test_sources.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'sources'`

- [ ] **Step 3: base.py 를 쓴다**

```python
# sources/base.py
"""수집 소스의 공통 인터페이스.

사이트마다 DOM 도 API 도 다르지만, 위층(크롤러·적재·지식화)이 보는 모양은 같아야
한다. 아카라이브가 개편돼도 arcalive.py 만 고치면 되도록 여기서 경계를 긋는다.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class RawPost:
    id: int
    url: str
    title: str = ""
    category: str = ""
    posted_at: str = ""          # ISO8601 문자열. 파싱 실패 시 빈 문자열
    views: int = 0
    recommend: int = 0
    body: str = ""
    comments: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    outlinks: list[dict] = field(default_factory=list)  # {id, section, anchor}


class Source(ABC):
    """수집 대상 사이트 하나."""

    name: str

    @abstractmethod
    def list_ids(self, pages: int, category: str | None = None) -> list[int]:
        """목록에서 글 번호를 최신순으로 모은다. 공지는 제외한다."""

    @abstractmethod
    def fetch_post(self, pid: int) -> tuple[str, RawPost | None]:
        """글 하나를 받는다.

        Returns:
            (status, post). status 는 ok | gated | notfound | error.
            ok 가 아니면 post 는 None.
        """
```

- [ ] **Step 4: arcalive.py 를 쓴다 — crawler.py 에서 파싱 로직 이관**

```python
# sources/arcalive.py
"""아카라이브 어댑터. 사이트에 의존하는 코드는 전부 이 파일에만 있다."""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from .base import RawPost, Source

BASE = "https://arca.live"

# <b>/<strong> 은 본문 강조에도 쓰여서 그대로 믿으면 URL·날짜가 섹션으로 잡힌다.
_SECTION_REJECT = re.compile(
    r"^(https?://|www\.)|^\+?\d{2}[/.\-]\d{2}|^Ctrl\+F$", re.I
)


def _parse_int(text: str | None) -> int:
    if not text:
        return 0
    m = re.search(r"-?\d[\d,]*", text)
    return int(m.group().replace(",", "")) if m else 0


def _clean_section(text: str) -> str | None:
    text = " ".join(text.split())
    if not (2 <= len(text) <= 40) or _SECTION_REJECT.search(text):
        return None
    return text


class ArcaLive(Source):
    name = "arcalive"

    def __init__(self, channel: str = "aiart", fetcher=None):
        self.channel = channel
        # fetcher 를 주입받아 테스트에서 네트워크 없이 파싱만 검증할 수 있게 한다
        self._fetch = fetcher

    # ---- 파싱 (네트워크 없음, 테스트 대상) ----

    def parse(self, html: str, pid: int) -> RawPost:
        soup = BeautifulSoup(html, "lxml")
        post = RawPost(id=pid, url=f"{BASE}/b/{self.channel}/{pid}")

        title_el = soup.select_one(".article-head .title")
        if title_el:
            clone = BeautifulSoup(str(title_el), "lxml")
            for badge in clone.select(".badge"):
                badge.decompose()
            post.title = clone.get_text(" ", strip=True)

        cat = soup.select_one(".article-head .category-badge")
        post.category = cat.get_text(strip=True) if cat else ""

        date_el = soup.select_one(".article-info time, time")
        post.posted_at = (date_el.get("datetime") or "") if date_el else ""

        info = soup.select_one(".article-info")
        info_text = info.get_text(" ", strip=True) if info else ""
        m = re.search(r"조회\s*수?\s*([\d,]+)", info_text)
        post.views = _parse_int(m.group(1)) if m else 0
        m = re.search(r"추천\s*수?\s*(-?[\d,]+)", info_text)
        post.recommend = _parse_int(m.group(1)) if m else 0

        body_el = soup.select_one(".article-content")
        if body_el:
            for img in body_el.select("img, video source, video"):
                src = img.get("src") or img.get("data-src") or ""
                if src:
                    post.images.append(src if src.startswith("http") else "https:" + src)
            post.body = body_el.get_text("\n", strip=True)
            post.outlinks = self._extract_links(body_el)

        for c in soup.select(".comment-item"):
            body = c.select_one(".message, .text")
            text = body.get_text("\n", strip=True) if body else ""
            if text:
                post.comments.append(text)

        return post

    def _extract_links(self, body) -> list[dict]:
        """같은 채널 글 링크를 소제목 문맥과 함께 뽑는다.

        허브 글의 소제목이 곧 주제 분류라, 이것이 위키 목차의 뼈대가 된다.
        """
        found: list[dict] = []
        current, bracketed = "(머리말)", None
        for el in body.descendants:
            name = getattr(el, "name", None)
            if name in ("h1", "h2", "h3", "h4", "strong", "b"):
                sec = _clean_section(el.get_text(" ", strip=True))
                if sec:
                    current = sec
                    if sec.startswith("[") and sec.endswith("]"):
                        bracketed = sec
            elif name == "a" and el.get("href"):
                m = re.search(r"arca\.live/b/([a-z0-9]+)/(\d+)", el["href"]) or re.match(
                    r"/b/([a-z0-9]+)/(\d+)", el["href"]
                )
                if not m or m.group(1) != self.channel:
                    continue
                anchor = " ".join(el.get_text(" ", strip=True).split())[:80]
                found.append({
                    "id": int(m.group(2)),
                    "section": bracketed or current,
                    "anchor": "" if anchor.startswith("http") else anchor,
                })
        return found

    def list_ids_from_html(self, html: str) -> list[int]:
        soup = BeautifulSoup(html, "lxml")
        out, seen = [], set()
        for row in soup.select("a.vrow"):
            if "notice" in (row.get("class") or []):
                continue
            m = re.match(r"/b/[^/]+/(\d+)", row.get("href") or "")
            if m and int(m.group(1)) not in seen:
                seen.add(int(m.group(1)))
                out.append(int(m.group(1)))
        return out

    # ---- 네트워크 (crawler.py 가 주입한 fetcher 사용) ----

    def list_ids(self, pages: int, category: str | None = None) -> list[int]:
        ids, seen = [], set()
        for page in range(1, pages + 1):
            url = f"{BASE}/b/{self.channel}?p={page}"
            if category:
                from urllib.parse import quote
                url += f"&category={quote(category)}"
            status, html = self._fetch(url)
            if status != "ok" or not html:
                break
            page_ids = [i for i in self.list_ids_from_html(html) if i not in seen]
            if not page_ids:
                break
            seen.update(page_ids)
            ids.extend(page_ids)
        return ids

    def fetch_post(self, pid: int) -> tuple[str, RawPost | None]:
        status, html = self._fetch(f"{BASE}/b/{self.channel}/{pid}")
        if status != "ok" or not html:
            return status, None
        return "ok", self.parse(html, pid)
```

```python
# sources/__init__.py
"""수집 소스 팩토리. 새 사이트를 붙일 때 여기에만 한 줄 추가한다."""

from .base import RawPost, Source

_REGISTRY = {}


def get_source(name: str, **kwargs) -> Source:
    if name not in _REGISTRY:
        raise ValueError(f"모르는 소스: {name} (등록된 것: {sorted(_REGISTRY)})")
    return _REGISTRY[name](**kwargs)


def _register():
    from .arcalive import ArcaLive
    _REGISTRY["arcalive"] = ArcaLive


_register()

__all__ = ["get_source", "Source", "RawPost"]
```

- [ ] **Step 5: 테스트가 통과하는지 본다**

Run: `cd /f/Project/arcawiki && python -m pytest tests/test_sources.py -v`
Expected: 3 passed

- [ ] **Step 6: crawler.py 가 Adapter 를 쓰도록 바꾼다**

`crawler.py` 에서 `parse_post`, `extract_links`, `clean_section`, `ids_of` 를 삭제하고, 대신:

```python
from sources import get_source

def make_source(channel: str):
    """네트워크 계층(fetch)은 crawler 가 갖고, 파싱은 Adapter 가 한다."""
    return get_source("arcalive", channel=channel, fetcher=fetch)
```

`crawl_one` 을 다음으로 교체한다:

```python
def crawl_one(pid: int, source, refs: list[dict]) -> tuple[str, dict | None]:
    status, raw = source.fetch_post(pid)
    if status != "ok" or raw is None:
        stub(pid, source.channel, status, refs)
        return status, None

    post = {
        "id": raw.id, "url": raw.url, "channel": source.channel, "status": "ok",
        "title": raw.title, "category": raw.category, "date": raw.posted_at,
        "views": raw.views, "recommend": raw.recommend, "body": raw.body,
        "comments": [{"text": t} for t in raw.comments],
        "images": raw.images, "outlinks": raw.outlinks,
        "content_hash": hashlib.sha256(raw.body.encode("utf-8")).hexdigest()[:16],
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    if not post["body"].strip() and not post["images"]:
        stub(pid, source.channel, "empty", refs)
        return "empty", None
    save_post(post, refs)
    return "ok", post
```

- [ ] **Step 7: 회귀 확인 — 기존 수집이 그대로 동작하는지**

Run: `cd /f/Project/arcawiki && python crawler.py --pages 1 --category 일반정보 --limit 3`
Expected: 3건 수집 성공, 본문·댓글·추천 숫자가 이전과 같은 형태로 출력됨

- [ ] **Step 8: 커밋**

```bash
git add sources/ crawler.py tests/test_sources.py
git commit -m "Source Adapter 구조로 분리 — 사이트 의존 코드를 sources/arcalive.py 로 격리"
```

---

### Task 3: 파이프라인 컨테이너화

ADR-0006 의 "손으로 안 돌린다"를 실제로 만든다. 지금은 내가 터미널에서 `python crawler.py` 를 친다.

**Files:**
- Create: `Dockerfile.pipeline`, `requirements.txt`
- Modify: `docker-compose.yml` (pipeline 서비스 추가, db 이미지를 pgvector 로)
- Modify: `pipeline.py` (컨테이너 경로 대응)
- Create: `.dockerignore`

**Interfaces:**
- Consumes: `crawler.py`, `ingest.py`, `pipeline.py:fill_queue()`
- Produces: `arcawiki-pipeline` 컨테이너. 환경변수 `PIPELINE_INTERVAL_HOURS`, `CRAWL_PAGES`, `CRAWL_CATEGORIES`

- [ ] **Step 1: requirements.txt 를 쓴다**

```
requests>=2.32
beautifulsoup4>=4.13
lxml>=5.3
psycopg[binary]>=3.2
pytest>=8.0
```

- [ ] **Step 2: Dockerfile.pipeline 을 쓴다**

```dockerfile
FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sources/ ./sources/
COPY crawler.py ingest.py pipeline.py ./

# posts/ 와 cookie.txt 는 볼륨으로 마운트한다 (이미지에 굽지 않는다)
CMD ["python", "-u", "pipeline.py"]
```

- [ ] **Step 3: .dockerignore 를 쓴다**

```
posts/
wiki/
docs/
tests/
.git/
.venv/
__pycache__/
*.txt
!requirements.txt
.env
```

- [ ] **Step 4: docker-compose.yml 을 고친다**

`db` 서비스의 image 를 바꾼다 (pgvector 확장이 Task 8 에서 필요하고, 나중에 바꾸면 볼륨 마이그레이션이 번거롭다):

```yaml
  db:
    image: pgvector/pgvector:pg17
```

`pipeline` 서비스를 추가한다:

```yaml
  pipeline:
    build:
      context: .
      dockerfile: Dockerfile.pipeline
    container_name: arcawiki-pipeline
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
    environment:
      DATABASE_URL: postgres://arcawiki:${POSTGRES_PASSWORD:-arcawiki}@db:5432/arcawiki
      PIPELINE_INTERVAL_HOURS: ${PIPELINE_INTERVAL_HOURS:-6}
      CRAWL_PAGES: ${CRAWL_PAGES:-5}
      CRAWL_CATEGORIES: ${CRAWL_CATEGORIES:-일반정보,실험정보}
    volumes:
      - ./posts:/app/posts
      - ./cookie.txt:/app/cookie.txt:ro
```

- [ ] **Step 5: 한 바퀴만 돌려 확인한다**

Run:
```bash
cd /f/Project/arcawiki
docker compose build pipeline
docker compose run --rm pipeline python -u pipeline.py --once
```
Expected: 수집 → 적재 → `큐 추가: {...}` → `대기 중: {...}` 가 순서대로 출력되고 exit 0

- [ ] **Step 6: 상시 기동하고 로그를 확인한다**

Run: `docker compose up -d pipeline && sleep 20 && docker compose logs --tail 20 pipeline`
Expected: `파이프라인 시작 — 6.0시간 주기` 이후 한 주기 로그

- [ ] **Step 7: 커밋**

```bash
git add Dockerfile.pipeline requirements.txt .dockerignore docker-compose.yml pipeline.py
git commit -m "파이프라인 컨테이너화 — 수집·적재·큐적재를 6시간 주기 자동 실행"
```

---

### Task 4: 큐 API

스킬 3종이 공통으로 쓸 얇은 함수 모음. 스킬 안에 SQL 을 흩뿌리면 스키마가 바뀔 때마다 마크다운 세 개를 고쳐야 한다.

**Files:**
- Create: `queue_api.py`
- Create: `tests/test_queue_api.py`

**Interfaces:**
- Consumes: `work_queue`, `knowledge_cards`, `claims`, `card_claims`, `posts` 테이블
- Produces:
  - `take(job:str, limit:int=20) -> list[dict]` — 우선순위 순으로 pending 작업을 꺼낸다 (상태는 안 바꾼다)
  - `done(job:str, target_key:str, note:str="") -> None`
  - `skip(job:str, target_key:str, note:str) -> None`
  - `load_posts(ids:list[int]) -> list[dict]` — 본문·댓글 포함. 본문은 `max_chars` 로 자른다
  - `save_card(post_id:int, card:dict, version:str="v1") -> int` — 카드 id 반환, 멱등
  - `save_claim(canonical:str, topic:str, links:list[dict]) -> int` — `links` 는 `{card_id, relation, quote}`
  - `queue_status() -> dict`

- [ ] **Step 1: 실패하는 테스트를 쓴다**

```python
# tests/test_queue_api.py
import os, pytest, psycopg
import queue_api as q

@pytest.fixture(autouse=True)
def _dsn(monkeypatch):
    monkeypatch.setattr(q, "DSN", os.environ["DATABASE_URL"])

def test_take_는_우선순위_낮은_것부터_준다():
    rows = q.take("extract", limit=5)
    assert rows, "큐가 비어 있으면 이 테스트는 의미가 없다"
    assert [r["priority"] for r in rows] == sorted(r["priority"] for r in rows)
    assert all(r["status"] == "pending" for r in rows)

def test_done_은_같은_작업을_다시_주지_않는다():
    first = q.take("extract", limit=1)[0]
    q.done("extract", first["target_key"], note="테스트")
    again = q.take("extract", limit=5)
    assert first["target_key"] not in [r["target_key"] for r in again]

def test_save_card_는_멱등이다():
    pid = int(q.take("extract", limit=1)[0]["target_key"])
    card = {"topic": "테스트", "summary": "요약", "software": ["ComfyUI"],
            "models": [], "settings": {"steps": 1000}, "usefulness": 7,
            "as_of": "2026-01-01"}
    a = q.save_card(pid, card, version="vtest")
    b = q.save_card(pid, card, version="vtest")
    assert a == b

def test_load_posts_는_본문을_자른다():
    pid = int(q.take("extract", limit=1)[0]["target_key"])
    rows = q.load_posts([pid], max_chars=100)
    assert len(rows[0]["body"]) <= 100
    assert "comments" in rows[0]
```

- [ ] **Step 2: 테스트를 돌려 실패를 확인한다**

Run: `cd /f/Project/arcawiki && DATABASE_URL="postgres://arcawiki:$(grep POSTGRES_PASSWORD .env | cut -d= -f2)@127.0.0.1:5433/arcawiki" python -m pytest tests/test_queue_api.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'queue_api'`

- [ ] **Step 3: queue_api.py 를 쓴다**

```python
"""스킬이 DB 를 다루는 통로.

스킬(마크다운)에 SQL 을 적으면 스키마가 바뀔 때마다 세 파일을 고쳐야 한다.
여기 한 곳만 고치면 되도록 모아 둔다.
"""

from __future__ import annotations

import json
import os

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

DSN = os.environ.get(
    "DATABASE_URL",
    "postgres://arcawiki:{}@127.0.0.1:5433/arcawiki".format(
        os.environ.get("POSTGRES_PASSWORD", "arcawiki")
    ),
)


def _conn():
    return psycopg.connect(DSN, row_factory=dict_row)


def take(job: str, limit: int = 20) -> list[dict]:
    """우선순위 순으로 대기 작업을 꺼낸다. 상태는 바꾸지 않는다.

    세션이 중간에 끊겨도 작업이 사라지지 않게, 처리를 마친 뒤에 done() 을 부른다.
    """
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """SELECT id, target_type, target_key, job, reason, detail, priority, status
               FROM work_queue
               WHERE job = %s AND status = 'pending'
               ORDER BY priority, created_at
               LIMIT %s""",
            (job, limit),
        )
        return cur.fetchall()


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


def load_posts(ids: list[int], max_chars: int = 8000) -> list[dict]:
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
        r["comments"] = by_post.get(r["id"], [])[:30]
    return rows


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


def save_claim(canonical: str, topic: str, links: list[dict]) -> int:
    """주장 하나와 그 근거 카드들을 저장한다.

    links: [{"card_id": int, "relation": "support|contradict|context", "quote": str}]
    """
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            "INSERT INTO claims (canonical, topic) VALUES (%s,%s) RETURNING id",
            (canonical, topic),
        )
        claim_id = cur.fetchone()["id"]
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
                 as_of_earliest = (SELECT min(k.as_of) FROM knowledge_cards k
                                   JOIN card_claims cc ON cc.card_id=k.id
                                   WHERE cc.claim_id=%s),
                 as_of_latest   = (SELECT max(k.as_of) FROM knowledge_cards k
                                   JOIN card_claims cc ON cc.card_id=k.id
                                   WHERE cc.claim_id=%s)
               WHERE id=%s""",
            (claim_id, claim_id, claim_id),
        )
        c.commit()
        return claim_id


def queue_status() -> dict:
    with _conn() as c, c.cursor() as cur:
        cur.execute(
            """SELECT job, status, count(*) AS n
               FROM work_queue GROUP BY job, status ORDER BY job, status"""
        )
        return {f"{r['job']}/{r['status']}": r["n"] for r in cur.fetchall()}
```

- [ ] **Step 4: 테스트가 통과하는지 본다**

Run: `cd /f/Project/arcawiki && DATABASE_URL="postgres://arcawiki:$(grep POSTGRES_PASSWORD .env | cut -d= -f2)@127.0.0.1:5433/arcawiki" python -m pytest tests/test_queue_api.py -v`
Expected: 4 passed

- [ ] **Step 5: 커밋**

```bash
git add queue_api.py tests/test_queue_api.py
git commit -m "큐 API 추가 — 스킬이 쓸 DB 통로를 한 곳에 모음"
```

---

### Task 5: Extractor 스킬 (글 → 지식카드)

원안의 ① 단계. 글을 읽고 구조화된 카드로 만든다. 이후 단계는 원문 대신 카드를 읽는다.

**Files:**
- Create: `.claude/skills/extract/SKILL.md`

**Interfaces:**
- Consumes: `queue_api.take("extract")`, `queue_api.load_posts()`, `queue_api.save_card()`, `queue_api.done()`, `queue_api.skip()`
- Produces: `knowledge_cards` 행. 이후 Resolver 가 `pending_resolution` 뷰로 읽는다

- [ ] **Step 1: 스킬을 쓴다**

```markdown
---
name: extract
description: 수집된 아카라이브 글에서 지식카드를 뽑아 DB에 저장한다. "추출해줘", "카드 만들어", "큐 처리해" 같은 요청에 사용.
---

# 지식 추출

원문 한 건에서 구조화된 지식카드 한 장을 만든다. 이후 단계(Claim 통합, 위키 작성)는
원문을 다시 읽지 않고 이 카드만 읽는다. 그래서 **카드에 없는 것은 위키에도 없다.**

## 절차

1. 처리할 것을 꺼낸다. 우선순위는 큐가 정한다 (비디오 → ANIMA → ComfyUI → …).

   ```python
   import queue_api as q
   jobs = q.take("extract", limit=20)
   posts = q.load_posts([int(j["target_key"]) for j in jobs], max_chars=8000)
   ```

2. 글마다 카드를 만든다. **한 번에 20건씩** 처리한다 — 한 건씩 왕복하면 20배 느리다.

3. 저장하고 큐를 비운다.

   ```python
   q.save_card(post_id, card, version="v1")
   q.done("extract", str(post_id))
   ```

## 카드 형태

```python
card = {
  "topic": "LoRA학습",              # 하나만. 아래 목록에서 고른다
  "summary": "…",                   # 2~4문장. 이 글이 무엇을 말하는가
  "software": ["ComfyUI", "kohya_ss"],
  "models": ["ANIMA", "ILXL"],
  "settings": {"steps": 1000, "lr": 0.0003, "rank": 32},   # 구체 수치
  "usefulness": 7,                  # 0~10
  "as_of": "2026-03-30",            # 원문 posted_at 을 그대로
}
```

`topic` 은 다음 중 하나: `비디오`, `ANIMA`, `ComfyUI`, `NAI`, `LoRA학습`, `프롬프트`,
`업스케일`, `VRAM최적화`, `설치`, `오류해결`, `모델정보`, `기타`

## 규칙

1. **원문에 없는 것을 쓰지 않는다.** 일반 지식으로 보충하지 않는다. 모르면 비운다.
2. **`settings` 가 이 카드의 값어치다.** 구체적인 수치·명령어·파일명·버전을 그대로
   옮긴다. "적절한 값을 설정한다" 같은 문장은 버린다.
3. **댓글을 읽는다.** 이 채널은 본문의 오류를 댓글이 정정하는 일이 잦다. 본문과
   댓글이 어긋나면 `summary` 에 그 사실을 적는다.
4. **`as_of` 는 반드시 채운다.** 이 분야는 반년이면 낡아서, 시점 없는 수치는 위험하다.
5. **글이 스스로 낡았다고 말하면 `summary` 첫 문장에 적는다.** 실제로 "오래된 글이니
   읽지말고 최신정보 찾기바람" 으로 시작하는 글이 있다.
6. **`usefulness` 기준**: 8~10 구체적 설정값과 절차가 있음 / 5~7 유용하나 부분적 /
   2~4 감상·후기 위주 / 0~1 위키 재료 아님.

## 건너뛰기

다음은 카드를 만들지 말고 `q.skip("extract", str(pid), 이유)` 한다.

- 그림·영상만 있고 본문이 사실상 없는 글
- 잡담, 감상, 인사
- 질문만 있고 답이 안 달린 글

건너뛴 이유를 반드시 남긴다. 나중에 기준을 바꿀 때 다시 볼 근거가 된다.

## 마치고

사용자에게 보고한다: 처리 건수, 건너뛴 건수와 대표 사유, `q.queue_status()`,
**추출 중 발견한 것** (자료가 유난히 부실한 주제, 반복해서 나오는 오류 등).
```

- [ ] **Step 2: 5건으로 시험한다**

Run: Claude Code 세션에서 `/extract` 를 호출하되 `q.take("extract", limit=5)` 로 제한
Expected: `knowledge_cards` 에 5행 추가, `work_queue` 의 해당 5건이 `done`

- [ ] **Step 3: 저장 결과를 눈으로 확인한다**

Run:
```bash
docker exec arcawiki-db psql -U arcawiki -d arcawiki -c \
  "SELECT post_id, topic, usefulness, as_of, settings FROM knowledge_cards ORDER BY id DESC LIMIT 5;"
```
Expected: `settings` 에 실제 수치가 들어 있고 `as_of` 가 비어 있지 않음

- [ ] **Step 4: 커밋**

```bash
git add .claude/skills/extract/SKILL.md
git commit -m "Extractor 스킬 추가 — 글에서 지식카드 추출"
```

---

### Task 6: Resolver 스킬 (카드 → Claim 통합)

원안의 ② 단계. 여러 글이 같은 말을 하는지, 어긋나는지를 판정해 Claim 으로 묶는다.
LoRA 목업에서 데이터셋 장수 충돌을 손으로 표로 만들었던 작업이 여기에 해당한다.

**Files:**
- Create: `.claude/skills/resolve/SKILL.md`

**Interfaces:**
- Consumes: `pending_resolution` 뷰, `knowledge_cards`, `queue_api.save_claim()`
- Produces: `claims` + `card_claims` 행. 이후 WikiWriter 가 `claim_strength` 뷰로 읽는다

- [ ] **Step 1: 스킬을 쓴다**

```markdown
---
name: resolve
description: 지식카드들을 읽고 같은 주장끼리 묶어 Claim Ledger를 만든다. "주장 통합해줘", "claim 정리" 같은 요청에 사용.
---

# 주장 통합

카드에 흩어진 주장을 하나로 묶고, 찬성·반대를 센다. 이게 있어야 위키가
"게시판에서는 대체로 ○○라고 하지만, 일부 글은 △△ 조건에서 다르다고 보고한다"
처럼 쓸 수 있다. 없으면 요약봇이 된다.

## 절차

1. 통합 대상 주제를 고른다.

   ```sql
   SELECT topic, cards, earliest, latest FROM pending_resolution ORDER BY cards DESC;
   ```

2. 그 주제의 카드를 전부 읽는다.

   ```sql
   SELECT k.id, k.post_id, k.summary, k.settings, k.as_of, p.title, p.recommend
   FROM knowledge_cards k JOIN posts p ON p.id = k.post_id
   WHERE k.topic = %s ORDER BY k.as_of;
   ```

3. 같은 말을 하는 것끼리 묶어 Claim 을 만든다.

   ```python
   import queue_api as q
   q.save_claim(
       canonical="캐릭터 고유 외형 태그는 학습 전에 제거한다",
       topic="LoRA학습",
       links=[
           {"card_id": 12, "relation": "support",    "quote": "머리와 눈색은…"},
           {"card_id": 34, "relation": "support",    "quote": "horns 태그를 지워야…"},
           {"card_id": 56, "relation": "contradict", "quote": "의상 태그는 지우면 안 됨"},
       ],
   )
   ```

## 판정 규칙

1. **`canonical` 은 검증 가능한 한 문장으로 쓴다.** "LoRA 는 어렵다" 는 주장이 아니다.
   "데이터셋은 최소 30장이 필요하다" 는 주장이다.
2. **시점이 다른 같은 주제는 서로 다른 Claim 이다.** 2023년 "rank 128" 과
   2026년 "rank 32" 는 한 주장의 찬반이 아니라 시대가 바뀐 것이다. 각각 Claim 으로
   두고 `claims.note` 에 관계를 적는다.
3. **`relation` 판정**
   - `support` — 같은 결론
   - `contradict` — 반대 결론. **조건이 다른 경우는 contradict 가 아니다** (VRAM 8GB 와
     24GB 의 권장값이 다른 것은 충돌이 아니라 조건 분기다). 이때는 `context`.
   - `context` — 조건·배경을 더하는 것
4. **`quote` 를 반드시 넣는다.** 나중에 위키에서 이 판정이 맞는지 사람이 확인할 통로다.
5. **하나의 카드가 여러 Claim 에 연결될 수 있다.** 긴 가이드 글은 대개 그렇다.
6. **주장이 3건 미만인 것은 Claim 으로 만들지 않는다.** 한 사람 의견은 아직 주장이 아니다.
   대신 카드에 남아 있으므로 위키가 "한 글에서만 언급됨" 으로 쓸 수 있다.

## 마치고

`claim_strength` 를 보고 보고한다: 만든 Claim 수, **찬반이 갈린 것**(위키에서
따로 다뤄야 함), **시대가 바뀐 것**(옛 주장이 뒤집힌 사례), 근거가 약한 것.
```

- [ ] **Step 2: 카드가 가장 많은 주제 하나로 시험한다**

Run: `/resolve` 호출, `pending_resolution` 최상단 주제 1개만
Expected: `claims` 에 3~10행, `claim_strength` 에서 support/contradict 가 집계됨

- [ ] **Step 3: 판정 결과를 눈으로 확인한다**

Run:
```bash
docker exec arcawiki-db psql -U arcawiki -d arcawiki -c \
  "SELECT canonical, support, contradict, earliest, latest FROM claim_strength ORDER BY support DESC LIMIT 10;"
```
Expected: 찬성이 여럿인 주장과 충돌이 있는 주장이 함께 보임

- [ ] **Step 4: 커밋**

```bash
git add .claude/skills/resolve/SKILL.md
git commit -m "Resolver 스킬 추가 — 카드를 Claim으로 통합"
```

---

### Task 7: WikiWriter 스킬 (Claim + 카드 → 문서)

원안의 ③ 단계. **원문을 읽지 않는다.** 카드와 Claim 만 읽는다. 이게 토큰 비용을
줄이는 동시에, 근거 없는 문장이 들어갈 통로를 막는다.

**Files:**
- Create: `.claude/skills/write-wiki/SKILL.md`
- Delete: `.claude/skills/wiki-writer/SKILL.md` (원문을 직접 읽던 구버전)

**Interfaces:**
- Consumes: `claim_strength` 뷰, `knowledge_cards`, `queue_api.take("write_page")`
- Produces: `wiki_pages`, `wiki_entries`, `wiki_entry_sources`, `page_sources` 행

- [ ] **Step 1: 스킬을 쓴다**

```markdown
---
name: write-wiki
description: Claim과 지식카드로 위키 문서를 작성해 DB에 저장한다. "위키 써줘", "비디오 문서 만들어" 같은 요청에 사용.
---

# 위키 작성

**원문을 읽지 않는다.** `claim_strength` 와 `knowledge_cards` 만 읽는다.
원문이 필요하다고 느껴지면 추출이 부실한 것이므로, 그 글을 다시 `extract` 큐에
올리고 이 문서는 미룬다.

## 절차

1. 작업을 꺼낸다.

   ```python
   import queue_api as q
   jobs = q.take("write_page", limit=1)     # 한 번에 문서 하나
   ```

2. 재료를 모은다.

   ```sql
   SELECT claim_id, canonical, support, contradict, earliest, latest
   FROM claim_strength WHERE topic = %s ORDER BY support DESC;

   SELECT k.id, k.post_id, k.summary, k.settings, k.as_of,
          p.title, p.url, p.recommend
   FROM knowledge_cards k JOIN posts p ON p.id = k.post_id
   WHERE k.topic = %s AND k.usefulness >= 5 ORDER BY k.as_of DESC;
   ```

3. 문서를 **항목 단위**로 나눠 저장한다. 통짜 마크다운으로 쓰지 않는다 —
   항목이 나뉘어 있어야 사람이 고친 부분을 보존하며 재생성할 수 있다.

   ```sql
   INSERT INTO wiki_pages (slug, title, section, intro, generated_at)
   VALUES (%s,%s,%s,%s, now())
   ON CONFLICT (slug) DO UPDATE SET intro=EXCLUDED.intro, generated_at=now()
   RETURNING id;

   -- human_edited 인 항목은 건드리지 않는다
   DELETE FROM wiki_entries WHERE page_id=%s AND human_edited=false;

   INSERT INTO wiki_entries (page_id, seq, heading, body_md, confidence, as_of, has_conflict)
   VALUES (…);
   INSERT INTO wiki_entry_sources (entry_id, post_id) VALUES (…);
   INSERT INTO page_sources (page_id, post_id, content_hash)
   SELECT %s, id, content_hash FROM posts WHERE id = ANY(%s)
   ON CONFLICT (page_id, post_id) DO UPDATE SET content_hash=EXCLUDED.content_hash;
   ```

   `page_sources.content_hash` 를 채워야 나중에 원문이 바뀐 것을 파이프라인이
   감지해 `refresh_page` 를 큐에 넣는다.

## 작성 규칙

1. **Claim 에 없는 주장을 쓰지 않는다.** 카드 하나에만 있는 내용은
   "한 글에서만 언급됨" 으로 표시해서 쓴다.
2. **`confidence`**: `support>=3 and contradict=0` → high / 충돌 있음 → low /
   그 외 → medium.
3. **충돌은 양쪽을 쓴다.** 임의로 하나를 고르지 않는다. `has_conflict=true`.
4. **`as_of` 를 항목마다 채운다.** 1년 넘은 정보는 본문에도 `(2023-03 기준)` 을 붙인다.
5. **시대가 바뀐 주장은 변화 자체를 쓴다.** "2023년에는 rank 128 이 권장됐으나
   2026년 도구 기본값은 32" 처럼. 옛 값을 지우지 않는다.
6. **`settings` 의 수치는 그대로 옮긴다.** 이게 위키를 읽는 이유다.
7. 채널 은어는 첫 등장 때 표준 용어를 병기한다 (`짤뽑(이미지 생성)`).
8. 이미지는 넣지 않는다. 원문 링크로 보낸다 (ADR-0003).

## 문서 앞머리에 반드시 넣는 것

```
> 원문 N건 → 이 문서 하나 | Claim M개 | 최신 자료 YYYY-MM
```

압축률이 이 프로젝트가 일하고 있다는 유일한 지표다 (ADR-0005).

## 마치고

`q.done("write_page", target_key)` 하고 보고한다: 문서 slug, 항목 수, 원문 건수,
**자료가 부족했던 절**, 충돌한 주장. 부족한 곳을 말하지 않으면 검증할 수 없다.
```

- [ ] **Step 2: 구버전 스킬을 지운다**

```bash
rm -rf .claude/skills/wiki-writer
```

- [ ] **Step 3: 문서 하나로 시험한다**

Run: `/write-wiki` 호출, `take("write_page", limit=1)`
Expected: `wiki_pages` 1행, `wiki_entries` 5~15행, 각 항목에 `wiki_entry_sources` 존재

- [ ] **Step 4: 출처 없는 항목이 없는지 확인한다**

Run:
```bash
docker exec arcawiki-db psql -U arcawiki -d arcawiki -c \
  "SELECT e.id, e.heading FROM wiki_entries e
   LEFT JOIN wiki_entry_sources s ON s.entry_id=e.id
   WHERE s.entry_id IS NULL;"
```
Expected: 0 rows — 출처 없는 항목은 지어낸 것이다

- [ ] **Step 5: 커밋**

```bash
git add .claude/skills/write-wiki/SKILL.md
git rm -r .claude/skills/wiki-writer
git commit -m "WikiWriter 스킬 추가 — 원문 대신 Claim과 카드만 읽고 문서 작성"
```

---

### Task 8: 정리

일회성 산출물이 루트에 14개 쌓여 있다. 어느 것이 자산이고 어느 것이 부스러기인지
구분이 안 되면 다음 사람(또는 다음 세션)이 판단할 수 없다.

**Files:**
- Delete: 루트의 조사용 `*.txt` 13개
- Delete: `graph.py`, `audit.py` (기능이 DB 뷰로 대체됨)
- Modify: `README.md`

**Interfaces:**
- Consumes: 없음
- Produces: 없음

- [ ] **Step 1: 무엇이 대체됐는지 확인한다**

`graph.py` 의 섹션 집계 → `refs` 테이블 + `pending_resolution` 뷰
`audit.py` 의 수집률 점검 → `posts.status` 집계 쿼리

Run:
```bash
docker exec arcawiki-db psql -U arcawiki -d arcawiki -c \
  "SELECT status, count(*) FROM posts GROUP BY status;" -c \
  "SELECT section, count(*) FROM refs WHERE section<>'' GROUP BY section ORDER BY 2 DESC LIMIT 10;"
```
Expected: `audit.py`, `graph.py` 가 주던 정보가 그대로 나옴

- [ ] **Step 2: 지운다**

```bash
cd /f/Project/arcawiki
rm -f audit.txt check_out.txt gate2.txt gate_probe.txt graph_probe.txt \
      index.txt lora_dump.txt lora_recent.txt lora_sel.txt nsfw_probe.txt \
      probe2.txt seed_probe.txt topics.txt link_graph.json index.json
rm -f graph.py audit.py
```

`cookie.txt` 는 지우지 않는다 (수집에 필요, `.gitignore` 로 보호됨).
`wiki/lora-학습.md` 는 형식 목업으로 남긴다.

- [ ] **Step 3: README 를 현재 구조로 고친다**

```markdown
# arcawiki

아카라이브 AI그림채널을 수집해 주제별 위키로 압축한다.
목표는 위키 자체가 아니라 **원문을 읽지 않고도 짤·비디오를 잘 만드는 것**이다.

## 구조

    원본 ─▶ 지식카드 ─▶ Claim ─▶ 위키
     ↑          ↑         ↑        ↑
    자동      extract   resolve  write-wiki   ← Claude Code 스킬
    (도커)

`pipeline` 컨테이너가 수집·적재·변경감지·큐적재를 6시간마다 자동 수행한다.
LLM 이 필요한 지점만 `work_queue` 를 통해 Claude Code 세션에 위임된다 (ADR-0006).

## 쓰는 법

```bash
docker compose up -d          # db + pipeline
docker compose logs -f pipeline
```

이후 Claude Code 에서 `/extract` → `/resolve` → `/write-wiki` 순으로 호출한다.
무엇을 처리할지는 큐가 정한다.

## 문서

- `docs/adr/` — 설계 결정과 이유 (0001~0006)
- `docs/glossary.md` — 용어
- `docs/superpowers/plans/` — 구현 플랜

## 수집 메모

- Cloudflare 차단 없음. 일반 UA + 5~7초 간격.
- 성인 등급 글은 비로그인 시 **HTTP 451** 이고 목록에도 안 나온다. `cookie.txt` 필요.
- 카테고리 URL 값과 화면 표시가 다르다: `일반정보`→정보/자료, `일반질문`→질문.
  로그인해야만 보이는 카테고리: `실험정보`, `실험적`, `NAI`, `AiVid`, `대회`, `질문`.
- 본문 길이 편차가 크다 (중앙값 380자, 최대 15만 자). LLM 에 넘길 때 상한 필수.
```

- [ ] **Step 4: 커밋**

```bash
git add -A
git commit -m "일회성 조사 산출물 정리, README를 현재 구조로 갱신"
```

---

## 이후 (이 플랜 범위 밖)

지식층이 실제로 채워진 뒤에 판단한다. 지금 착수하면 데이터 없이 인프라만 만든다.

- **벡터검색** — 원안의 `chunk + claim + wiki section` 3종 임베딩. `pgvector/pgvector:pg17`
  이미지는 Task 3 에서 미리 깔아둔다. Claim 이 100개쯤 쌓이면 착수한다.
- **웹** — MkDocs(반나절, 편집 불가) vs Next.js(2~4주, 편집 가능). 미결정.
  문서가 5개쯤 나온 뒤 실제로 읽어보고 정한다.
- **CF 터널** — 웹이 정해진 다음.
- **다른 소스 어댑터** — `sources/reddit.py` 등. Task 2 로 자리는 마련됨.

## 자체 점검

**스펙 커버리지**

| 원안 요소 | 태스크 |
|---|---|
| ① 크롤러 + Source Adapter | Task 2 |
| RAW DB | 완료 (기존) |
| ② 전처리·분류 | Task 3 (큐 우선순위) |
| **지식카드 DB** | Task 1 + Task 5 |
| **Claim Ledger** | Task 1 + Task 6 |
| ③ Extractor / Resolver / WikiWriter | Task 5 / 6 / 7 |
| WIKI | Task 7 |
| ④ 증분 업데이트 | Task 3 (`stale_pages` → `refresh_page`) |
| 벡터검색 | 범위 밖 (이미지만 Task 3 에서 준비) |
| 자동화 (손 안 대기) | Task 3 |

**타입 일관성**: `RawPost` 필드명이 Task 2 정의와 Task 2 Step 6 의 `crawl_one` 사용처에서
일치함. `queue_api` 함수 시그니처가 Task 4 정의와 Task 5·6·7 사용처에서 일치함.
`save_card(post_id, card, version)` / `save_claim(canonical, topic, links)` 확인.

**미해결**: 웹 스택 선택. Task 7 까지 마치고 문서를 실제로 읽어본 뒤 결정한다.
