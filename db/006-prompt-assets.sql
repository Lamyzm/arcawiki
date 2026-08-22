-- 재료층 (prompt assets)
--
-- 기존 파이프라인(posts -> knowledge_cards -> claims -> wiki_entries)은 요약기다.
-- "무엇이 맞는가"에는 강하지만 열거형 자료를 못 담는다. 감사 결과:
--   고유 작가명 원문 737명 -> 위키 96명(13%)
--   EXIF 통짜 덤프 168건 -> 1건
--   복붙 가능한 작가 스택: 197만자 위키 전체에 6벌
-- 원인은 "한 글당 카드 1장, 본문 중앙 1,062자" 상한이다. 1만자 넘는 글의
-- 보존율이 7%인데, 작가 대조표/프리셋 저장글이 정확히 그 구간에 있다.
--
-- 그래서 판단이 필요 없는 값은 요약하지 않고 원문 그대로 따로 받는다.
-- LLM 없이 정규식으로 채우므로 전 글에 돌릴 수 있다.

CREATE TABLE IF NOT EXISTS prompt_assets (
    id          bigserial PRIMARY KEY,
    post_id     bigint NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    comment_seq integer,              -- NULL 이면 본문, 아니면 그 댓글
    kind        text   NOT NULL,      -- artist | lora | weighted_tag | model_file | resolution | sampler | steps | cfg | seed
    raw         text   NOT NULL,      -- 원문 표기 그대로. 이게 핵심이다
    name        text,                 -- 정규화된 이름 (작가명/로라명/샘플러명)
    weight      numeric,
    syntax      text,                 -- at | artist_colon | nai_colons | angle | paren | exif
    context     text,                 -- 주변 문장. "이 작가를 넣으면 눈이 뭉개진다" 같은 거동 주석이 여기 붙는다
    posted_at   date,
    UNIQUE (post_id, comment_seq, kind, raw)
);

CREATE INDEX IF NOT EXISTS prompt_assets_kind_name ON prompt_assets (kind, name);
CREATE INDEX IF NOT EXISTS prompt_assets_post      ON prompt_assets (post_id);
CREATE INDEX IF NOT EXISTS prompt_assets_posted    ON prompt_assets (posted_at DESC);

-- 통짜 블록. 태그 나열 프롬프트와 EXIF 덤프를 자르지 않고 통째로 보관한다.
CREATE TABLE IF NOT EXISTS prompt_blocks (
    id          bigserial PRIMARY KEY,
    post_id     bigint NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    comment_seq integer,
    role        text   NOT NULL,      -- positive | negative | exif | tag_list
    body        text   NOT NULL,      -- 전문 그대로
    n_artists   integer NOT NULL DEFAULT 0,
    n_commas    integer NOT NULL DEFAULT 0,
    posted_at   date,
    body_hash   text GENERATED ALWAYS AS (md5(body)) STORED,
    UNIQUE (post_id, comment_seq, role, body_hash)
);

CREATE INDEX IF NOT EXISTS prompt_blocks_role   ON prompt_blocks (role);
CREATE INDEX IF NOT EXISTS prompt_blocks_posted ON prompt_blocks (posted_at DESC);

-- 작가 한 명이 어디에 몇 번 나왔고 어떤 가중치로 쓰였나
CREATE OR REPLACE VIEW artist_usage AS
SELECT name,
       count(*)                                    AS uses,
       count(DISTINCT post_id)                     AS posts,
       count(*) FILTER (WHERE weight IS NOT NULL)  AS weighted,
       round(avg(weight), 2)                       AS avg_weight,
       min(weight)                                 AS min_weight,
       max(weight)                                 AS max_weight,
       max(posted_at)                              AS latest,
       min(posted_at)                              AS earliest
  FROM prompt_assets
 WHERE kind = 'artist' AND name IS NOT NULL
 GROUP BY name;
