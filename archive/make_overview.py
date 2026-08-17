"""초보자용 개요와 용어집.

기존 문서들은 ComfyUI·ANIMA·LoRA 가 뭔지 이미 안다고 가정하고 쓰였다.
아무것도 모르는 사람이 들어올 입구가 없어서 만든다.

정의 자체는 일반 설명이지만, 구체적인 수치·설정은 전부 출처가 붙은 문서로 넘긴다.
"""

import queue_api as q


def srcs_by_entity(*names, limit=6):
    """개체를 언급한 카드의 원문 id."""
    out = set()
    with q._conn() as c, c.cursor() as cur:
        for n in names:
            cur.execute(
                """SELECT k.post_id, p.recommend FROM knowledge_cards k
                   JOIN card_entities ce ON ce.card_id = k.id
                   JOIN entities e ON e.id = ce.entity_id
                   JOIN posts p ON p.id = k.post_id
                   WHERE e.name = %s ORDER BY p.recommend DESC LIMIT %s""",
                (n, limit),
            )
            out |= {r["post_id"] for r in cur.fetchall()}
    return sorted(out)


def srcs_by_claim(*keywords):
    out = set()
    with q._conn() as c, c.cursor() as cur:
        for kw in keywords:
            cur.execute(
                """SELECT DISTINCT k.post_id FROM claims cl
                   JOIN card_claims cc ON cc.claim_id = cl.id
                   JOIN knowledge_cards k ON k.id = cc.card_id
                   WHERE cl.canonical LIKE %s""",
                (f"%{kw}%",),
            )
            out |= {r["post_id"] for r in cur.fetchall()}
    return sorted(out)


# ─────────────────────────────────────────────── 개요

OVERVIEW = dict(
    slug="overview", title="처음이라면 — 전체 지도", kind="개념", stage="준비", section="",
    intro=("아무것도 모르는 상태에서 **로컬로 그림을 뽑을 수 있는 데까지** 가는 길을 그린다. "
           "구체적인 설정값은 전부 링크한 문서에 있고, 여기서는 '무엇이 무엇인지'만 다룬다."),
)

OV = [
    dict(seq=1, heading="먼저 — 길이 두 개로 갈린다", conf="medium", as_of="2026-08-09", cf=False,
         posts=srcs_by_entity("NovelAI", "Dreamina", "ComfyUI", limit=3),
         body="""AI로 그림을 만드는 방법은 크게 둘이다. **둘은 거의 다른 세계다.**

| | 웹 서비스 | 로컬 실행 |
|---|---|---|
| 예 | NovelAI, Dreamina(Seedance), Civitai, 나노바나나, Grok | ComfyUI, WebUI(Forge) |
| 돈 | 구독·포인트 결제 | 전기값만 |
| 장비 | 없어도 됨 | **엔비디아 GPU 필요** |
| 자유도 | 서비스가 허용하는 것만 | 사실상 무제한 |
| 난이도 | 가입하고 바로 | 설치·설정에 하루 |
| 검열 | 있음 | 없음 |

이 채널은 **로컬 쪽 이야기가 대부분**이다. 웹 서비스 이야기는 주로 "새 모델이 나왔다" 는 소식이다.

**장비가 없으면 로컬은 시작할 수 없다.** 아래 하드웨어 절을 먼저 볼 것."""),

    dict(seq=2, heading="장비 — 이게 안 되면 나머지는 의미 없다", conf="high", as_of="2026-08-05", cf=False,
         posts=srcs_by_claim("엔비디아 RTX 16GB", "RTX 3060 12GB", "지원 GPU는 지포스"),
         body="""**엔비디아 지포스 3000~5000번대**가 사실상 전제다.
AMD·Intel도 되기는 하지만 훨씬 느리고 설정이 어렵다. 자세한 것은 [오류 해결](troubleshooting.md)의
환경별 절에 실측표가 있다.

| | 최소 | 권장 |
|---|---|---|
| GPU | RTX 3060 12GB | RTX 5070 Ti 16GB 이상 |
| RAM | 32GB | 64GB (영상은 96GB도 고려) |
| 저장장치 | — | 1TB 이상 NVMe SSD |

**VRAM 8GB 이하는 권장되지 않는다.** 12GB면 영상 생성까지 가능은 하다
(MiniMax H3가 RTX 3060 12GB + RAM 32GB에서 돈다는 보고가 4건).

자세한 수치는 [VRAM·속도 최적화](vram.md) 참조."""),

    dict(seq=3, heading="로컬 실행기 — 무엇을 깔 것인가", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs_by_entity("ComfyUI", "Stable Diffusion WebUI", limit=4),
         body="""그림을 만들려면 **실행기**가 필요하다. 모델 파일만으로는 아무것도 못 한다.

| 실행기 | 성격 |
|---|---|
| **ComfyUI** | 노드를 선으로 잇는 방식. 이 채널의 사실상 표준. 자유도가 높은 대신 처음엔 복잡해 보인다 |
| **Stable Diffusion WebUI / Forge Neo** | 버튼과 입력칸 위주. 쉽지만 최신 모델 대응이 느리다 |
| Wan2GP | 저사양 GPU용 영상 생성 전용 |

**ComfyUI를 직접 설치할 필요는 없다.** 채널에 **딸깍 통합팩**이 있다 — ComfyUI 본체와
가속 도구(SageAttention, Triton), 커스텀 노드, 워크플로우까지 전부 넣어 압축해둔 것이다.
압축 풀고 배치 파일 실행하면 끝난다.

통합팩 사용 규칙은 [국룰](kukroul.md)에 정리돼 있다. **본체를 업데이트하면 망가지니
새 판이 나오면 새로 받는다**는 것이 가장 중요한 규칙이다.

설치 절차는 [설치와 환경 구성](install.md) 참조."""),

    dict(seq=4, heading="모델 — 그림체를 정하는 것", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs_by_entity("Illustrious", "ANIMA", "SDXL", "FLUX", limit=3),
         body="""실행기가 '프로그램'이라면 모델은 '엔진'이다. 같은 프롬프트도 모델이 다르면 전혀 다른 그림이 나온다.

### 이미지 모델

| 모델 | 성격 |
|---|---|
| **Illustrious** (계열) | 애니 그림체의 현재 주류. 채널 기본 권장은 `WAI-illustrious-SDXL` |
| **[ANIMA](anima.md)** | 자연어 이해가 좋다. 대신 화풍이 약해서 Illustrious와 2단으로 엮어 쓴다 |
| SDXL | Illustrious의 조상. 지금은 "쓸 이유가 없으니 Illustrious나 ANIMA를 쓰라"는 안내가 나온다 |
| FLUX, Qwen Image | 실사·텍스트에 강한 계열 |

### 영상 모델

| 모델 | 성격 |
|---|---|
| **[MiniMax H3](minimax-h3.md)** | 2026년 8월 현재 채널 주력. 오픈웨이트 |
| **Wan 2.2** | 그 전 주력. High/Low 분리 + lightx2v 로라가 표준 구성 |
| LTX 2.3 | 2D·애니가 약해 아니메 LoRA를 물려야 한다 |
| Seedance 2.0, Sora 2 | 웹 서비스. 가중치가 공개되지 않아 로컬 실행 불가 |

상세는 [비디오 생성](video-generation.md) 참조."""),

    dict(seq=5, heading="순서 — 뭘 먼저 하나", conf="medium", as_of="2026-08-08", cf=False,
         posts=srcs_by_claim("통합팩", "WAI-illustrious-SDXL", "EXIF 가 든 이미지"),
         body="""```
1. 장비 확인          →  엔비디아 3000~5000번대, VRAM 12GB 이상, RAM 32GB
2. 통합팩 설치        →  한글 없는 경로에 압축 해제
3. 체크포인트 받기    →  WAI-illustrious-SDXL 을 models/checkpoints 에
4. 워크플로우 불러오기 →  EXIF 든 이미지를 ComfyUI 창에 드래그앤드롭
5. 프롬프트 넣고 생성
6. 안 되면            →  오류 해결 문서에서 증상으로 찾기
```

4번이 낯설 텐데, **ComfyUI 워크플로우는 이미지 파일 안에 들어 있다.** 채널에서 배포하는
"워크플로우"는 대개 그냥 png/mp4 파일이고, 그걸 ComfyUI 창에 끌어다 놓으면 노드 구성이 복원된다.

> ⚠️ 아카라이브에 올릴 때 **`exif 데이터 보존`을 체크하지 않으면 워크플로우가 날아간다.**
> 받은 파일에서 워크플로우가 안 나오면 이것 때문일 가능성이 높다."""),

    dict(seq=6, heading="더 하고 싶어지면", conf="medium", as_of="2026-08-08", cf=False,
         posts=srcs_by_claim("LoRA", "업스케일", "컨트롤넷", "인페인팅"),
         body="""기본 생성이 되기 시작하면 대개 이 순서로 넘어간다.

| 하고 싶은 것 | 필요한 것 |
|---|---|
| 특정 캐릭터·화풍을 고정하고 싶다 | **LoRA** — 남이 만든 걸 받아 쓰거나 직접 학습 |
| 포즈·구도를 지정하고 싶다 | **ControlNet** |
| 그림 일부만 고치고 싶다 | **인페인팅** |
| 해상도를 올리고 싶다 | **업스케일** (SeedVR2, PiD, SUPIR 등) |
| 얼굴·손이 뭉개진다 | **디테일러** |
| 움직이게 하고 싶다 | **영상 모델** (MiniMax H3, Wan 2.2) |

각 항목의 구체적인 설정값은 해당 문서에 있다. 용어가 낯설면 [용어집](glossary.md)을 먼저 볼 것."""),
]

# ─────────────────────────────────────────────── 용어집

GLOSSARY = dict(
    slug="glossary", title="용어집", kind="용어", stage=None, section="",
    intro="채널 글을 읽는 데 필요한 최소한의 용어. 채널 은어도 함께 정리한다.",
)

GL = [
    dict(seq=1, heading="채널 은어", conf="medium", as_of="2026-08-08", cf=False,
         posts=srcs_by_claim("통합팩", "찐빠"),
         body="""이걸 모르면 글이 안 읽힌다.

| 말 | 뜻 |
|---|---|
| **짤뽑** | 이미지 생성 |
| **찐빠** | 결과물의 결함. 특히 손·얼굴이 뭉개진 것 |
| **딸깍** | 설정 없이 버튼만 눌러 되는 것. "딸깍 통합팩" = 압축 풀고 실행만 하면 되는 패키지 |
| **국룰** | 채널에서 통용되는 기본 설정 |
| **챈** | 채널 |
| **뉴비** | 초보자 |
| **개추** | 추천 |"""),

    dict(seq=2, heading="파일 종류", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs_by_claim("WAI-illustrious-SDXL", "VAE Select", "LoRA"),
         body="""| 용어 | 뜻 |
|---|---|
| **체크포인트** | 그림체를 결정하는 본체 모델 파일. `models/checkpoints` 에 넣는다 |
| **LoRA (로라)** | 체크포인트에 얹는 작은 추가 파일. 특정 캐릭터나 화풍을 학습시킨 것. `models/loras` |
| **VAE** | 잠재 이미지를 실제 픽셀로 바꾸는 부품. 결과가 탁하거나 흰 점이 찍히면 이걸 바꾼다 |
| **ControlNet** | 포즈·윤곽 같은 구조를 지정하는 보조 모델 |
| **워크플로우** | ComfyUI의 노드 구성. **이미지·영상 파일 안에 들어 있어서** 드래그앤드롭으로 불러온다 |

**양자화**(`fp8`, `int8`, `GGUF`, `w4a8`)는 모델을 작게 줄여 적은 VRAM에서 돌리는 기법이다.
용량과 속도를 얻는 대신 품질이 조금 떨어진다. 어떤 양자화가 나은지는 [국룰](kukroul.md)에 있다."""),

    dict(seq=3, heading="생성 설정", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs_by_claim("Euler A + automatic", "cfg 1", "denoise"),
         body="""| 용어 | 뜻 |
|---|---|
| **프롬프트** | 무엇을 그릴지 적는 글. **네거티브 프롬프트**는 "이건 그리지 마라" |
| **태그** | 단부루식 단어 나열형 프롬프트 (`1girl, blue hair, smile`) |
| **스텝** | 그림을 다듬는 횟수. 많을수록 오래 걸린다 |
| **CFG** | 프롬프트를 얼마나 강하게 따를지. 높으면 프롬프트에 충실하지만 그림이 망가질 수 있다 |
| **샘플러 / 스케줄러** | 그림을 만들어가는 알고리즘. **조합을 잘못 고르면 그림이 기괴해진다** ([ANIMA](anima.md) 참조) |
| **시드** | 난수 값. 같은 시드 + 같은 설정 = 같은 그림 |
| **디노이즈** | 원본을 얼마나 바꿀지 (0~1). 낮으면 원본 유지, 높으면 새로 그린다 |
| **와일드카드** | 프롬프트 일부를 목록에서 무작위로 뽑아 넣는 기능 |

**라이트닝·디스틸·터보 로라**는 적은 스텝으로 뽑게 해주는 가속용 LoRA다.
이걸 쓰면 CFG를 1로 고정하는 등 설정이 달라진다."""),

    dict(seq=4, heading="작업 종류", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs_by_claim("I2V", "인페인팅", "업스케일"),
         body="""| 약어 | 뜻 |
|---|---|
| **T2I** | Text to Image — 글로 그림 만들기 |
| **I2I** | Image to Image — 그림을 고쳐 그리기 |
| **T2V** | Text to Video — 글로 영상 만들기 |
| **I2V** | Image to Video — 그림 한 장을 영상으로 |
| **FL2V** | First-Last to Video — 첫 프레임과 끝 프레임을 주고 사이를 채우기 |
| **R2V** | Reference to Video — 참조 이미지들을 주고 영상 만들기 |

| 용어 | 뜻 |
|---|---|
| **인페인팅** | 그림의 일부만 다시 그리기 |
| **업스케일** | 해상도 올리기 |
| **hires fix** | 낮은 해상도로 뽑고 키우면서 다시 그려 디테일을 넣는 2단 방식 |
| **디테일러** | 얼굴·손 같은 특정 부위만 골라 다시 그려 품질을 올리는 것 |
| **VFI / 프레임 보간** | 영상 프레임 사이를 채워 부드럽게 만드는 것 |"""),
]


def write_page(cur, page, entries):
    cur.execute(
        """INSERT INTO wiki_pages (slug,title,section,kind,stage,intro,generated_at,published)
           VALUES (%(slug)s,%(title)s,%(section)s,%(kind)s,%(stage)s,%(intro)s,now(),true)
           ON CONFLICT (slug) DO UPDATE SET intro=EXCLUDED.intro, kind=EXCLUDED.kind,
                title=EXCLUDED.title, stage=EXCLUDED.stage, generated_at=now() RETURNING id""",
        page,
    )
    pid = cur.fetchone()["id"]
    cur.execute("DELETE FROM wiki_entries WHERE page_id=%s AND human_edited=false", (pid,))
    allp = set()
    for e in entries:
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
    return pid, len(entries), len(allp)


def main() -> None:
    with q._conn() as c, c.cursor() as cur:
        for page, entries in ((OVERVIEW, OV), (GLOSSARY, GL)):
            pid, n, np_ = write_page(cur, page, entries)
            print(f"{page['slug']:<10} page{pid} 항목{n} 원문{np_}")
        c.commit()
        cur.execute(
            """SELECT count(*) n FROM wiki_entries e
               LEFT JOIN wiki_entry_sources s ON s.entry_id=e.id WHERE s.entry_id IS NULL"""
        )
        print("출처 없는 항목(전체):", cur.fetchone()["n"])


if __name__ == "__main__":
    main()
