-- 개체(entity) 층과 문서 분류 두 축.
--
-- 문서를 "가이드" 하나로만 두면 친구가 "WAN 2.2가 뭐지" 로는 들어올 수 없다.
-- 개체를 독립 문서로 두고 역링크를 걸면, 채널이 아는 것의 전체 구조가 드러난다.

-- ── 문서 분류 두 축 ────────────────────────────────────────────────
-- kind  : 무슨 종류의 문서인가
-- stage : 만드는 과정의 어느 단계인가 (생성만이 아니라 전 과정을 덮기 위해)

ALTER TABLE wiki_pages ADD COLUMN IF NOT EXISTS kind  TEXT NOT NULL DEFAULT '가이드';
ALTER TABLE wiki_pages ADD COLUMN IF NOT EXISTS stage TEXT;

COMMENT ON COLUMN wiki_pages.kind IS
    '개체 | 개념 | 튜토리얼 | 국룰 | 문제해결 | 자원 | 용어 | 가이드';
COMMENT ON COLUMN wiki_pages.stage IS
    '준비 | 기획 | 프롬프트 | 생성 | 후처리 | 정리   (개체·용어 문서는 NULL)';

CREATE INDEX IF NOT EXISTS wiki_pages_kind_idx  ON wiki_pages (kind);
CREATE INDEX IF NOT EXISTS wiki_pages_stage_idx ON wiki_pages (stage);

-- ── 개체 ───────────────────────────────────────────────────────────
-- 카드의 software/models 배열에서 도출되지만, 표기가 제각각이라
-- (rgthree / rgthree-comfy, LTX 2.3 / LTX2 FP8) 정규화가 필요하다.

CREATE TABLE IF NOT EXISTS entities (
    id        BIGSERIAL PRIMARY KEY,
    slug      TEXT UNIQUE NOT NULL,
    name      TEXT NOT NULL,                  -- 정규 표기
    kind      TEXT NOT NULL,                  -- model | software | node | service | concept
    aliases   TEXT[] NOT NULL DEFAULT '{}',   -- 원문에 나타난 다른 표기들
    summary   TEXT NOT NULL DEFAULT '',
    page_id   BIGINT REFERENCES wiki_pages (id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS entities_kind_idx    ON entities (kind);
CREATE INDEX IF NOT EXISTS entities_aliases_idx ON entities USING gin (aliases);

-- 카드가 어떤 개체를 언급했는가. 역링크의 뿌리.
CREATE TABLE IF NOT EXISTS card_entities (
    card_id   BIGINT NOT NULL REFERENCES knowledge_cards (id) ON DELETE CASCADE,
    entity_id BIGINT NOT NULL REFERENCES entities (id)        ON DELETE CASCADE,
    role      TEXT   NOT NULL DEFAULT 'mentions',  -- mentions | subject | requires
    PRIMARY KEY (card_id, entity_id)
);

-- 위키 항목이 어떤 개체를 언급했는가. 문서 → 문서 링크.
CREATE TABLE IF NOT EXISTS entry_entities (
    entry_id  BIGINT NOT NULL REFERENCES wiki_entries (id) ON DELETE CASCADE,
    entity_id BIGINT NOT NULL REFERENCES entities (id)     ON DELETE CASCADE,
    PRIMARY KEY (entry_id, entity_id)
);

-- ── 역링크 ─────────────────────────────────────────────────────────

-- 이 개체를 언급하는 문서들. 개체 문서 하단에 붙는다.
CREATE OR REPLACE VIEW entity_backlinks AS
SELECT e.id   AS entity_id,
       e.slug AS entity_slug,
       e.name AS entity_name,
       w.id   AS page_id,
       w.slug AS page_slug,
       w.title AS page_title,
       w.kind,
       count(*) AS mentions
FROM entities e
JOIN entry_entities ee ON ee.entity_id = e.id
JOIN wiki_entries en   ON en.id = ee.entry_id
JOIN wiki_pages w      ON w.id = en.page_id
GROUP BY e.id, e.slug, e.name, w.id, w.slug, w.title, w.kind;

-- 함께 등장하는 개체들. "관련 항목" 을 자동으로 만든다.
CREATE OR REPLACE VIEW entity_cooccurrence AS
SELECT a.entity_id AS entity_id,
       b.entity_id AS related_id,
       count(*)    AS together
FROM card_entities a
JOIN card_entities b ON b.card_id = a.card_id AND b.entity_id <> a.entity_id
GROUP BY a.entity_id, b.entity_id
HAVING count(*) >= 2;

-- 문서로 만들 만한 개체. 카드가 충분히 쌓인 것만.
CREATE OR REPLACE VIEW entity_candidates AS
SELECT e.id, e.slug, e.name, e.kind,
       count(ce.card_id) AS cards,
       min(k.as_of) AS earliest,
       max(k.as_of) AS latest
FROM entities e
JOIN card_entities ce   ON ce.entity_id = e.id
JOIN knowledge_cards k  ON k.id = ce.card_id
WHERE e.page_id IS NULL
GROUP BY e.id, e.slug, e.name, e.kind
HAVING count(ce.card_id) >= 3
ORDER BY count(ce.card_id) DESC;

-- ── 국룰 후보 ──────────────────────────────────────────────────────
-- 국룰을 명시한 글은 37건뿐이지만, 실제 국룰은 수백 건에 흩어진 설정값의
-- 합의점으로만 존재한다. 그것을 셀 수 있다는 게 이 프로젝트의 값어치다.

CREATE OR REPLACE VIEW consensus_settings AS
SELECT cs.topic,
       cs.canonical,
       cs.support,
       cs.contradict,
       cs.earliest,
       cs.latest,
       -- 찬성이 많고 반대가 없을수록, 최근일수록 국룰에 가깝다
       (cs.support - cs.contradict * 2) AS strength
FROM claim_strength cs
WHERE cs.support >= 2
ORDER BY (cs.support - cs.contradict * 2) DESC, cs.latest DESC NULLS LAST;
