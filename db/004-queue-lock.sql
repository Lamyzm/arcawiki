-- 병렬 처리 안전장치.
-- 여러 세션이 동시에 큐를 꺼내면 같은 글을 중복 처리한다. 꺼내는 순간 잠근다.
-- 처리 도중 죽은 세션의 몫은 일정 시간이 지나면 자동으로 회수된다.

ALTER TABLE work_queue ADD COLUMN IF NOT EXISTS claimed_at TIMESTAMPTZ;
ALTER TABLE work_queue ADD COLUMN IF NOT EXISTS claimed_by TEXT NOT NULL DEFAULT '';

CREATE INDEX IF NOT EXISTS work_queue_claimed_idx
    ON work_queue (job, claimed_at) WHERE status = 'claimed';
