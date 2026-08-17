-- 작업 큐: 코드가 채우고 Claude 가 비운다.
--
-- 파이프라인(크롤 → 적재)은 판단이 필요 없어 자동으로 돈다. 그러다 LLM 이 있어야
-- 하는 지점을 만나면 여기에 쌓아둔다. Claude Code 세션이 스킬로 꺼내 처리한다.
-- 무엇이 밀렸는지가 DB 상태로 남아서, 세션이 끊겨도 잊히지 않는다.

CREATE TABLE IF NOT EXISTS work_queue (
    id           BIGSERIAL PRIMARY KEY,

    -- 무엇에 대한 작업인가
    target_type  TEXT   NOT NULL,          -- post | section | page
    target_key   TEXT   NOT NULL,          -- post id, 섹션명, page slug

    -- 어떤 작업인가
    job          TEXT   NOT NULL,          -- extract | write_page | refresh_page

    -- 왜 필요한가 (사람이 읽고 판단할 수 있게)
    reason       TEXT   NOT NULL DEFAULT '',  -- new | source_changed | requested
    detail       TEXT   NOT NULL DEFAULT '',

    -- 우선순위. ADR-0005 의 주제 우선순위를 숫자로 옮긴 것. 낮을수록 먼저.
    priority     INTEGER NOT NULL DEFAULT 50,

    status       TEXT   NOT NULL DEFAULT 'pending',  -- pending | done | skipped
    note         TEXT   NOT NULL DEFAULT '',         -- 건너뛴 이유 등

    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    done_at      TIMESTAMPTZ,

    -- 같은 대상에 같은 작업이 중복으로 쌓이지 않게 한다.
    -- 원문이 또 바뀌면 done 을 pending 으로 되돌리는 방식으로 재처리한다.
    UNIQUE (target_type, target_key, job)
);

CREATE INDEX IF NOT EXISTS work_queue_pending_idx
    ON work_queue (priority, created_at)
    WHERE status = 'pending';

-- 문서가 어떤 원문에서 나왔는지 + 그때 원문의 해시가 무엇이었는지.
-- 나중에 원문이 바뀌면 이 해시와 비교해서 갱신 대상을 찾는다.
CREATE TABLE IF NOT EXISTS page_sources (
    page_id      BIGINT NOT NULL REFERENCES wiki_pages (id) ON DELETE CASCADE,
    post_id      BIGINT NOT NULL REFERENCES posts (id)      ON DELETE CASCADE,
    content_hash TEXT   NOT NULL DEFAULT '',   -- 문서를 쓸 당시 원문의 해시
    PRIMARY KEY (page_id, post_id)
);

-- 아직 지식 추출이 안 된 글.
-- 본문이 짧은 글은 위키 재료가 못 되므로 제외한다(그림만 올린 글 등).
CREATE OR REPLACE VIEW pending_extraction AS
SELECT p.id, p.title, p.posted_at, p.recommend, p.body_len
FROM posts p
WHERE p.status = 'ok'
  AND p.body_len >= 200
  AND NOT EXISTS (
      SELECT 1 FROM wiki_entry_sources s WHERE s.post_id = p.id
  )
  AND NOT EXISTS (
      SELECT 1 FROM work_queue q
      WHERE q.target_type = 'post' AND q.target_key = p.id::text
        AND q.job = 'extract' AND q.status <> 'pending'
  );

-- 원문이 바뀌어서 문서를 다시 봐야 하는 경우.
-- 문서를 쓸 당시 해시와 현재 해시가 다르면 내용이 낡았을 수 있다.
CREATE OR REPLACE VIEW stale_pages AS
SELECT w.id        AS page_id,
       w.slug,
       w.title,
       count(*)    AS changed_sources,
       max(p.fetched_at) AS last_change
FROM wiki_pages w
JOIN page_sources ps ON ps.page_id = w.id
JOIN posts p         ON p.id = ps.post_id
WHERE p.content_hash IS DISTINCT FROM ps.content_hash
GROUP BY w.id, w.slug, w.title;

-- 큐 현황 한눈에 보기. 스킬이 처음 읽는 곳.
CREATE OR REPLACE VIEW queue_summary AS
SELECT job, reason, status, count(*) AS n, min(priority) AS top_priority
FROM work_queue
GROUP BY job, reason, status;
