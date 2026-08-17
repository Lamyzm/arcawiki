-- arcawiki 스키마
--
-- 층이 세 개다.
--   1) 원본   : 크롤러가 받은 그대로. 절대 수정하지 않는다. 위키는 언제든 다시 만들 수 있다.
--   2) 큐레이션: 허브 글이 남긴 링크와 소제목. 사람이 몇 년에 걸쳐 만든 분류라 가장 값지다.
--   3) 위키   : 정제 대상. 항목 단위로 쪼개서 재생성해도 사람 편집이 살아남게 한다.

CREATE EXTENSION IF NOT EXISTS pg_trgm;   -- 한국어 부분일치 검색용

-- ─────────────────────────────────────────────── 1) 원본

CREATE TABLE IF NOT EXISTS posts (
    id            BIGINT PRIMARY KEY,          -- 아카라이브 글 번호
    channel       TEXT        NOT NULL,
    url           TEXT        NOT NULL,
    status        TEXT        NOT NULL,        -- ok | gated | notfound | empty | error
    title         TEXT        NOT NULL DEFAULT '',
    category      TEXT        NOT NULL DEFAULT '',
    posted_at     TIMESTAMPTZ,
    views         INTEGER     NOT NULL DEFAULT 0,
    recommend     INTEGER     NOT NULL DEFAULT 0,
    body          TEXT        NOT NULL DEFAULT '',
    body_len      INTEGER     GENERATED ALWAYS AS (length(body)) STORED,
    image_count   INTEGER     NOT NULL DEFAULT 0,
    is_adult      BOOLEAN     NOT NULL DEFAULT FALSE,  -- 웹 계층에서 가리기 위한 표시
    content_hash  TEXT,
    fetched_at    TIMESTAMPTZ NOT NULL,
    raw           JSONB                                 -- 파서를 고쳐도 재파싱할 수 있게 원본 보관
);

CREATE INDEX IF NOT EXISTS posts_category_idx  ON posts (category);
CREATE INDEX IF NOT EXISTS posts_recommend_idx ON posts (recommend DESC);
CREATE INDEX IF NOT EXISTS posts_posted_idx    ON posts (posted_at DESC);
CREATE INDEX IF NOT EXISTS posts_title_trgm    ON posts USING gin (title gin_trgm_ops);
CREATE INDEX IF NOT EXISTS posts_body_trgm     ON posts USING gin (body  gin_trgm_ops);

CREATE TABLE IF NOT EXISTS comments (
    id      BIGSERIAL PRIMARY KEY,
    post_id BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,
    seq     INTEGER NOT NULL,
    body    TEXT    NOT NULL,
    UNIQUE (post_id, seq)
);

-- 글이 수정되면 이전 본문을 남긴다. 위키 내용을 역추적할 때 필요하다.
CREATE TABLE IF NOT EXISTS post_versions (
    id           BIGSERIAL PRIMARY KEY,
    post_id      BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,
    content_hash TEXT   NOT NULL,
    body         TEXT   NOT NULL,
    captured_at  TIMESTAMPTZ,
    UNIQUE (post_id, content_hash)
);

CREATE TABLE IF NOT EXISTS images (
    id      BIGSERIAL PRIMARY KEY,
    post_id BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,
    seq     INTEGER NOT NULL,
    url     TEXT    NOT NULL,
    UNIQUE (post_id, seq)
);

-- ─────────────────────────────────────────────── 2) 큐레이션 (링크 그래프)

-- 허브 글이 어떤 소제목 아래에서 이 글을 가리켰는가.
-- section 이 곧 주제 라벨이라, 이것만으로 위키 목차가 나온다.
CREATE TABLE IF NOT EXISTS refs (
    id       BIGSERIAL PRIMARY KEY,
    post_id  BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,
    hub_id   BIGINT,
    hub_name TEXT   NOT NULL,
    section  TEXT   NOT NULL DEFAULT '',
    anchor   TEXT   NOT NULL DEFAULT '',
    -- 같은 조합은 한 번만. 여러 경로로 수집해도 중복이 쌓이지 않는다.
    UNIQUE (post_id, hub_name, section, anchor)
);

CREATE INDEX IF NOT EXISTS refs_section_idx ON refs (section);
CREATE INDEX IF NOT EXISTS refs_post_idx    ON refs (post_id);

CREATE TABLE IF NOT EXISTS outlinks (
    id      BIGSERIAL PRIMARY KEY,
    from_id BIGINT NOT NULL REFERENCES posts (id) ON DELETE CASCADE,
    to_id   BIGINT NOT NULL,
    section TEXT   NOT NULL DEFAULT '',
    anchor  TEXT   NOT NULL DEFAULT '',
    UNIQUE (from_id, to_id, section, anchor)
);

-- 허브 참조 수가 곧 중요도. 위키 작성 시 어떤 글부터 읽을지 정하는 데 쓴다.
CREATE OR REPLACE VIEW post_importance AS
SELECT p.id,
       p.title,
       p.recommend,
       p.body_len,
       COUNT(DISTINCT r.hub_name) AS hub_count,
       array_agg(DISTINCT r.section) FILTER (WHERE r.section <> '') AS sections
FROM posts p
LEFT JOIN refs r ON r.post_id = p.id
WHERE p.status = 'ok'
GROUP BY p.id, p.title, p.recommend, p.body_len;

-- ─────────────────────────────────────────────── 3) 위키 (정제 대상)

CREATE TABLE IF NOT EXISTS wiki_pages (
    id           BIGSERIAL PRIMARY KEY,
    slug         TEXT UNIQUE NOT NULL,
    title        TEXT        NOT NULL,
    section      TEXT        NOT NULL DEFAULT '',   -- 출처가 된 허브 섹션
    intro        TEXT        NOT NULL DEFAULT '',
    is_adult     BOOLEAN     NOT NULL DEFAULT FALSE,
    published    BOOLEAN     NOT NULL DEFAULT FALSE,
    generated_at TIMESTAMPTZ,
    updated_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 문서를 항목 단위로 쪼갠다. 이게 '정제 가능'의 실체다.
-- 재생성할 때 human_edited = TRUE 인 항목은 건드리지 않는다.
CREATE TABLE IF NOT EXISTS wiki_entries (
    id           BIGSERIAL PRIMARY KEY,
    page_id      BIGINT  NOT NULL REFERENCES wiki_pages (id) ON DELETE CASCADE,
    seq          INTEGER NOT NULL,
    heading      TEXT    NOT NULL DEFAULT '',
    body_md      TEXT    NOT NULL,
    confidence   TEXT    NOT NULL DEFAULT 'medium',  -- high | medium | low
    as_of        DATE,                               -- 이 정보가 언제 기준인지
    has_conflict BOOLEAN NOT NULL DEFAULT FALSE,     -- 자료끼리 어긋남
    human_edited BOOLEAN NOT NULL DEFAULT FALSE,     -- 사람이 손댔으면 재생성에서 보존
    updated_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (page_id, seq)
);

CREATE INDEX IF NOT EXISTS wiki_entries_page_idx ON wiki_entries (page_id, seq);

-- 항목마다 근거가 된 원문. 출처 없는 항목이 생기지 않게 강제한다.
CREATE TABLE IF NOT EXISTS wiki_entry_sources (
    entry_id BIGINT NOT NULL REFERENCES wiki_entries (id) ON DELETE CASCADE,
    post_id  BIGINT NOT NULL REFERENCES posts (id)        ON DELETE CASCADE,
    note     TEXT   NOT NULL DEFAULT '',
    PRIMARY KEY (entry_id, post_id)
);

-- 사람이 고친 이력. 친구들이 편집한 걸 되돌릴 수 있어야 한다.
CREATE TABLE IF NOT EXISTS wiki_edits (
    id         BIGSERIAL PRIMARY KEY,
    entry_id   BIGINT NOT NULL REFERENCES wiki_entries (id) ON DELETE CASCADE,
    before_md  TEXT   NOT NULL,
    after_md   TEXT   NOT NULL,
    editor     TEXT   NOT NULL DEFAULT '',
    edited_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
