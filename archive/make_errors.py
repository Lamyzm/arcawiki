"""오류해결 문서를 만든다.

오류 정보는 `오류해결` 주제 글에만 있지 않다. 워크플로우 배포글의 댓글에 흩어져 있고,
그중 상당수는 본문이 아니라 댓글에만 있다. 카드 139장 중 64장에 오류 내용이 있었다.
증상으로 찾을 수 있게 배열한다.
"""

import queue_api as q

PAGE = dict(
    slug="troubleshooting", title="오류 해결", kind="문제해결", stage="생성", section="",
    intro=("증상으로 찾는 문서다. **여기 있는 것의 절반 이상은 원문 본문이 아니라 댓글에서 나왔다.** "
           "글만 읽고 따라 하다 막히는 이유가 대개 그것이다."),
)

E = [
    dict(seq=1, heading="먼저 — 증상별 빠른 찾기", conf="high", as_of="2026-08-09", cf=False,
         posts=[179251955, 174448928, 179114541, 179342860, 175163102],
         body="""| 증상 | 원인 | 어디로 |
|---|---|---|
| `time_shift_slope` 오류 | ComfyUI 버전 × MiniMaxH3-Cache | ↓ 버전 충돌 |
| 영상이 **검은 화면** | int8convrot VAE 환경 | ↓ 버전 충돌 |
| ADetailer 후 **검은 사각형** → 전체 검게 | Forge Neo 확장 호환 | ↓ 결과물 이상 |
| 안 시켰는데 **비키니**가 나옴 | 퀄리티 태그 부작용 | ↓ 결과물 이상 |
| 인페인팅이 **Pause 0%** 에서 멈춤 | 대기 상태 (오류 아님) | ↓ 멈춘 것처럼 보임 |
| 커스텀 노드가 **매니저에서 안 나옴** | 매니저 등록 안 됨 | ↓ 설치 |
| 업데이트했는데 **반영이 안 됨** | 매니저 ≠ 코어 | ↓ 설치 |
| 노드 이름이 **엔크립트/어노말리**로 뜸 | 오인식 (실제로는 KJNodes) | ↓ 설치 |"""),

    dict(seq=2, heading="버전 충돌", conf="high", as_of="2026-08-07", cf=False,
         posts=[179251955, 179215559, 179254934, 179114541, 179413848],
         body="""### `time_shift_slope` 오류 — MiniMaxH3-Cache

**경계 버전이 특정돼 있다:**

```
정상   ComfyUI v0.30.0-1-g14b05228c   (2026-08-02)
오류   v0.30.0-19-g88fec4b6 이후
```

**해결 세 가지** — 위로 갈수록 권장:

1. 원 저장소에 **PR이 올라와 있다.** 먼저 최신을 확인한다
2. 직접 고친다 — `__init__.py` 에서 `time_shift_slope` 로 구한 `slope_a` 를 오디오 출력에 곱하는
   부분을 지우고 `-audio_out` 을 그대로 반환한다 *(같은 내용의 업스트림 PR이 이유 없이 닫힌 적 있음)*
3. 업데이트를 미루거나 다운그레이드한다

### 영상이 검은 화면 (int8convrot Video VAE)

**해결 조건 네 가지를 모두 만족해야 한다:**
ComfyUI 최신 + torch `+cu130` 이후 + comfy-aimdo 최신 + comfy-kitchen 최신

> ⚠️ **미해결 사례가 있다.** PyTorch 2.11.0+cu130 신규 설치 환경에서도 검은 화면이 났다는
> 보고가 댓글에 남아 있다.

### 라데온: 0.31.0 에서 sage가 안 된다

ROCm on Windows 11 기준으로 **ComfyUI portable 0.30.0에서만 동작**하고 0.31.0은 버그로 안 됐다.
9070XT에서 스텝당 약 11.5초."""),

    dict(seq=3, heading="노드 충돌 — 같이 쓰면 안 되는 조합", conf="high", as_of="2026-08-07", cf=False,
         posts=[179038650, 179280493, 179342860],
         body="""| A | B | 결과 |
|---|---|---|
| MiniMaxH3 Cache | Spectrum Apply | **Error** |
| MiniMaxH3 Cache | EasyCache | 같이 못 씀 |
| MiniMaxH3 Cache | **터보 LoRA** | **결과물 박살남** — Cache는 계산 재사용, Turbo는 스텝 자체를 생략해 원리가 겹침 |
| NoobAI·V-pred 체크포인트 | Kohya Deep Shrink / DCW / Spectrum | 상성 나쁨 — **하나씩 바이패스**해서 범인을 찾는다 |

**최속 조합** (에러 없이 되는 것): `Cache + Mem Eff Sage Attention Patch + Patch Sage Attention KJ`
→ 309.58초가 94.73초로. 여기에 Spectrum을 더하면 에러다.

**Easy-Use 썸네일 충돌**: 설정 → easyuse → `모델 미리보기 썸네일 활성화`, `컨텍스트 메뉴에서
자동으로 하위 디렉토리를 중첩` 을 끈다."""),

    dict(seq=4, heading="설치 — 안 찾아지거나 반영이 안 될 때", conf="high", as_of="2026-08-07", cf=False,
         posts=[179226965, 178949797, 175458978, 160657113],
         body="""**매니저에서 검색이 안 되는 노드가 있다.** `SimpleMathInt+`, `CacheDiT`, `MiniMaxH3Cache` 등.
깃허브 zip을 받아 `custom_nodes` 에 풀거나 나이틀리로 설치한다.

**매니저 업데이트는 코어를 갱신하지 않는다.** 내장 노드 변경은 반영되지 않으므로
본체는 git 또는 `update_comfyui.bat` 로 올린다.

**릴리스가 아니라 main 브랜치여야 하는 경우도 있다.** EasyUseAnima는 리저널 노드의 인풋 소켓
누락 버그 때문에 git(main)으로 설치해야 수정본을 받는다.

**노드 이름이 이상하게 뜬다면 오인식이다.** `MiniMax H3 Mem Eff Sage Attention Patch` 와
`Patch Sage Attention KJ` 는 원래 **KJNodes 노드**인데, '엔크립트'·'어노말리' 계열로 표시되는 건
ComfyUI의 오인식 오류다. 그 이름의 노드를 따로 설치할 필요 없다.

**미싱 노드**는 ComfyUI Manager의 `Custom nodes in workflow` 로 한번에 설치한다."""),

    dict(seq=5, heading="결과물이 이상할 때", conf="high", as_of="2026-08-08", cf=False,
         posts=[179342860, 174448928, 173213921, 178880588],
         body="""### 안 시켰는데 비키니가 나온다

원인은 **퀄리티 태그**다. `masterpiece`, `best quality`, `score_7` 같은 태그가 사실상
"고평점 = 야짤"을 부른다.

> **네거티브에 `bikini` 를 넣어도 안 된다.** 프롬프트에 **`safe` 태그**를 넣어야 해결된다.

### ADetailer 후 검은 사각형 → 이미지 전체가 검게 (Forge Neo)

`COMMANDLINE_ARGS` 를 아무리 바꿔도 소용없다(`--sage --uv`, 빈 값, `--uv` 만 등 전부 실패).
`Haoming02/ADetailer-Neo` 로도 재발한다.

**해결**: extensions 에서 기존 adetailer 체크를 해제하고 `abzaloff/aadetailer-neoforge` 로 교체.
*(작성자도 5시간 이상 검증하지는 못했다고 밝힘)*

### ANIMA 그림이 기괴해진다

**Euler A / automatic 조합에서 발생한다.** `Euler` 또는 `ER SDE` + `simple` 또는 `SGM uniform` 을 쓴다.

### LTX LoRA에서 중국어 음성이 나온다

중국어로 훈련된 LoRA다. **LoRA Audio 강도를 0으로** 둔다. 그리고
`ltx-2.3-22b-distilled-1.1_transformer_only_fp8_scaled.safetensors` 로만 써야 강도를 올려도 화면이 안 깨진다.

### SDXL/Illustrious 결과가 탁하거나 흰 점

**VAE Select = 2** (`fixFP16ErrorsSDXLLowerMemoryUse_v10`)"""),

    dict(seq=6, heading="멈춘 것처럼 보일 때", conf="high", as_of="2026-06-27", cf=False,
         posts=[175163102, 179083162, 179254885],
         body="""**인페인팅이 `Pause 0%` 에서 멈춘다** — 오류가 아니다. 워크플로우 안에서 **파랗게 깜빡이는
`Continue` 버튼**을 누르면 진행된다.

> 이 질문에 제미나이는 "하드웨어 병목"이라고 답했다. **오답이다.**

**`Validate Prompt` 서브그래프 오류** — 검사 실패 시 에러를 내도록 만든 것인데 오류가 잦다.
비활성화하거나 지우고 직접 연결해도 된다 *(작성자도 없애겠다고 함)*.

**`FALLBACK` 로그**는 오류가 아니다. "이번 스텝은 불안정하니 정상 계산했다"는 뜻이다.

**Grok 워크플로우**는 프롬프트를 비우면 오류가 난다. **마침표 하나라도** 넣는다.
인증 파일은 `c:\\사용자\\.grok\\auth.json`."""),

    dict(seq=7, heading="환경별 — AMD / Intel", conf="medium", as_of="2026-08-05", cf=False,
         posts=[179069083, 160894544, 179413848],
         body="""**Intel B580 은 구동 실패**했다. 세 시간 씨름 끝에:
- int8convrot — 1회는 13분, 2회차에 `UR_LOST` 에러
- fp8 — **BSOD**
- dynamic vram 불안정

**AMD는 되기는 한다.** 다만 느리다:

| GPU | MiniMax H3 I2VA (544x800, 20스텝) |
|---|---|
| RTX 5090 | 1분 04초 |
| RTX 3090 | 2분 41초 |
| **R9700** | 3분 27초 |
| **RX 7900XT** | 6분 53초 |
| RTX 3060 | 8분 59초 |

R9700은 sage attention이, RX 7900XT는 flash attention이 빨랐다.
AI Max 395 + rocm 7.2에서 Wan 2.2는 960x640 81프레임에 거의 1시간이 걸렸고,
우분투로 옮겨도 향상이 미미해 윈도우가 권장됐다."""),

    dict(seq=8, heading="아직 답이 없는 것", conf="low", as_of="2026-08-09", cf=True,
         posts=[179114541, 178949797, 179445963],
         body="""정직하게 — 채널에서 해결되지 않은 것들이다.

- **int8convrot 검은 화면** — 권장 조건을 다 맞춘 환경(PyTorch 2.11.0+cu130 신규 설치)에서도 재현 보고
- **DaSiWa 워크플로우** — MiniMax H3 Director 노드 업데이트 이후 작동하지 않는다는 보고
- **묵직·둔탁한 효과음** — MiniMax H3 I2V에서 "무슨 짓을 해도 제거 안 됨"
- **로라 확장자가 `.safetensors` 로 안 나옴** (2023년 LoRA 학습) — 여러 명이 같은 증상을 겪었고
  답이 안 달렸다

**오류 로그를 그록에 붙여넣으면 대부분 해결된다**는 조언이 반복해서 나온다. 채널에 답이 없을 때
쓸 만한 마지막 수단이다."""),
]


def main() -> None:
    with q._conn() as c, c.cursor() as cur:
        cur.execute(
            """INSERT INTO wiki_pages (slug,title,section,kind,stage,intro,generated_at,published)
               VALUES (%(slug)s,%(title)s,%(section)s,%(kind)s,%(stage)s,%(intro)s,now(),true)
               ON CONFLICT (slug) DO UPDATE SET intro=EXCLUDED.intro, kind=EXCLUDED.kind,
                    title=EXCLUDED.title, stage=EXCLUDED.stage, generated_at=now()
               RETURNING id""",
            PAGE,
        )
        pid = cur.fetchone()["id"]
        cur.execute("DELETE FROM wiki_entries WHERE page_id=%s AND human_edited=false", (pid,))

        allp: set[int] = set()
        for e in E:
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

        cur.execute(
            """SELECT count(*) n FROM wiki_entries e
               LEFT JOIN wiki_entry_sources s ON s.entry_id = e.id
               WHERE e.page_id=%s AND s.entry_id IS NULL""",
            (pid,),
        )
        print(f"page {pid} | 항목 {len(E)} | 원문 {len(allp)} | 출처없는항목 {cur.fetchone()['n']}")


if __name__ == "__main__":
    main()
