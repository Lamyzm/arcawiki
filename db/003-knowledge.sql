-- 원안의 KNOWLEDGE DB 와 Claim Ledger.
-- 원본(posts)과 위키(wiki_pages) 사이의 중간층. 이 층이 있어야 문서를 다시 쓸 때
-- 원문을 다시 읽지 않아도 되고, 주장의 찬반을 셀 수 있다.

CREATE TABLE IF NOT EXISTS knowledge_cards (
    id                BIGSERIAL PRIMARY KEY,
    post_id           BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,
    -- 프롬프트를 고치면 버전을 올린다. 옛 카드를 지우지 않고 나란히 둔다.
    extractor_version TEXT   NOT NULL DEFAULT 'v1',
    topic             TEXT   NOT NULL,
    summary           TEXT   NOT NULL,
    software          TEXT[] NOT NULL DEFAULT '{}',
    models            TEXT[] NOT NULL DEFAULT '{}',
    settings          JSONB  NOT NULL DEFAULT '{}',   -- 구체 수치. 이게 위키의 값어치다
    usefulness        INTEGER NOT NULL DEFAULT 5,
    as_of             DATE,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (post_id, extractor_version)
);

CREATE INDEX IF NOT EXISTS cards_topic_idx    ON knowledge_cards (topic);
CREATE INDEX IF NOT EXISTS cards_as_of_idx    ON knowledge_cards (as_of DESC);
CREATE INDEX IF NOT EXISTS cards_settings_idx ON knowledge_cards USING gin (settings);

CREATE TABLE IF NOT EXISTS claims (
    id             BIGSERIAL PRIMARY KEY,
    canonical      TEXT NOT NULL,
    topic          TEXT NOT NULL DEFAULT '',
    as_of_earliest DATE,
    as_of_latest   DATE,
    status         TEXT NOT NULL DEFAULT 'open',
    note           TEXT NOT NULL DEFAULT '',
    created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS claims_topic_idx ON claims (topic);

CREATE TABLE IF NOT EXISTS card_claims (
    card_id  BIGINT NOT NULL REFERENCES knowledge_cards (id) ON DELETE CASCADE,
    claim_id BIGINT NOT NULL REFERENCES claims (id)          ON DELETE CASCADE,
    relation TEXT   NOT NULL,   -- support | contradict | context
    quote    TEXT   NOT NULL DEFAULT '',
    PRIMARY KEY (card_id, claim_id)
);

-- 주장끼리의 관계. 2023년 "rank 128" 을 2026년 "rank 32" 가 대체한 것처럼,
-- 시대가 바뀌어 뒤집힌 주장을 무관한 두 주장으로 두면 이 프로젝트의 핵심 발견이 사라진다.
CREATE TABLE IF NOT EXISTS claim_relations (
    from_claim BIGINT NOT NULL REFERENCES claims (id) ON DELETE CASCADE,
    to_claim   BIGINT NOT NULL REFERENCES claims (id) ON DELETE CASCADE,
    relation   TEXT   NOT NULL,   -- supersedes | refines | conditional_on | contradicts
    note       TEXT   NOT NULL DEFAULT '',
    PRIMARY KEY (from_claim, to_claim, relation),
    CHECK (from_claim <> to_claim)
);

CREATE OR REPLACE VIEW claim_strength AS
SELECT c.id AS claim_id,
       c.canonical,
       c.topic,
       count(*) FILTER (WHERE cc.relation = 'support')    AS support,
       count(*) FILTER (WHERE cc.relation = 'contradict') AS contradict,
       min(k.as_of) AS earliest,
       max(k.as_of) AS latest
FROM claims c
LEFT JOIN card_claims cc    ON cc.claim_id = c.id
LEFT JOIN knowledge_cards k ON k.id = cc.card_id
GROUP BY c.id, c.canonical, c.topic;

CREATE OR REPLACE VIEW pending_resolution AS
SELECT k.topic, count(*) AS cards, min(k.as_of) AS earliest, max(k.as_of) AS latest
FROM knowledge_cards k
WHERE NOT EXISTS (SELECT 1 FROM card_claims cc WHERE cc.card_id = k.id)
GROUP BY k.topic
HAVING count(*) >= 3;
