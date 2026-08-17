"""국룰 문서를 만든다.

여러 글이 독립적으로 같은 말을 한 것만 모은다. 어느 한 글에도 이렇게 정리돼 있지 않다.
consensus_settings 뷰(찬성-반대×2)가 재료다.
"""

import queue_api as q


def srcs(*keywords):
    """주장 문구로 근거 원문 id 를 모은다."""
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


PAGE = dict(
    slug="kukroul", title="국룰 — 채널이 합의한 기본값", kind="국룰", stage=None, section="",
    intro=("여러 글이 **독립적으로 같은 말을 한 것**만 모았다. 어느 한 글에도 이렇게 정리돼 "
           "있지 않다. 괄호 안 숫자는 그렇게 말한 글의 수이며, 클수록 채널의 합의에 가깝다."),
)

ENTRIES = [
    dict(seq=1, heading="ComfyUI 통합팩 — 딸깍 규약", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs("run_nvidia_gpu_fast_fp16", "negpip", "지원 GPU는 지포스",
                    "한글이 없는 경로", "Easy-Models-Linker", "본체를 업데이트하지"),
         body="""채널에는 같은 사람이 만든 딸깍 통합팩 계보가 있다
(`0.11.1 → 0.15.1 → 0.20.1 → 0.22.0 → 0.23.0 → 0.26.0 → 0.30.0 → 0.31.0`, 여덟 판).
같은 규칙이 여덟 판에 걸쳐 반복돼서, 사실상 **성문화된 국룰**이다.

| 규칙 | 근거 |
|---|---|
| sage attention을 쓰려면 `run_nvidia_gpu.bat` 이 아니라 **`run_nvidia_gpu_fast_fp16_accumulation.bat`** 으로 실행 | 8건 |
| negpip 덕에 일반 프롬프트 칸에서 **`(tag:-1),`** 음수 가중치를 쓸 수 있다 | 6건 |
| 지원 GPU는 **지포스 3000~5000번대**, 라데온은 미확인 | 6건 |
| 출력물은 `output/날짜`, 중간 과정은 그 아래 `WIP` | 6건 |
| **한글이 없는 경로**에 압축을 푼다 | 3건 |
| 기존 모델 폴더는 `Add-Ons/Easy-Models-Linker.bat` 또는 `extra_model_paths.yaml` 복사로 공유 | 5건 |
| **본체를 업데이트하지 말고**, 새 판이 나오면 처음부터 새로 받는다 | 4건 |
| 설정 > Comfy > Nodes 2.0 > **모던 노드 디자인을 켜면** 워크플로우 배열이 깨지고 일부 노드가 오작동 | 4건 |

> **조건 하나** — sage attention을 끄면 **지포스 2000번대에서도** 동작한다 (2건)."""),

    dict(seq=2, heading="SDXL / Illustrious 기본값", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs("WAI-illustrious-SDXL", "VAE Select", "aspect_ratio.py",
                    "Controlnet Mode Select", "autocomplete tag source", "NoobAI"),
         body="""| 항목 | 값 | 근거 |
|---|---|---|
| 체크포인트 | **WAI-illustrious-SDXL** (`models/checkpoints`) | 5건 |
| 결과물이 탁하거나 흰 점이 찍히면 | **VAE Select = 2** (`fixFP16ErrorsSDXLLowerMemoryUse_v10`) | 4건 |
| Controlnet Mode Select | **1=일반, 2=오픈포즈, 3=리저널** (ANIMA 워크플로우는 1=일반, 2=컨트롤넷) | 5건 |
| 해상도 프리셋 수정 위치 | Illustrious·SDXL은 `ComfyUi_NakoNode/py/aspect_ratio.py`, ANIMA는 `comfyui-kjnodes/custom_dimensions.json` | 5건 |
| 태그 자동완성 | `autocomplete tag source` 를 **danbooru** 로 두면 e621 태그가 빠진다 | 3건 |
| NoobAI·V-pred 계열 | Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘다. **하나씩 바이패스**해 원인을 찾는다 | 5건 |"""),

    dict(seq=3, heading="ANIMA 배치", conf="high", as_of="2026-08-08", cf=False,
         posts=srcs("ANIMA는 Base v1.0", "ANIMA 는 NVIDIA Cosmos", "ANIMA INT8"),
         body="""파일 세 개를 각각 다른 폴더에 넣어야 한다 (5건).

```
Base v1.0        →  models/diffusion_models
텍스트 인코더     →  models/text_encoders   (qwen_3_06b_base.safetensors 로 개명)
VAE              →  models/vae
```

- ANIMA는 **NVIDIA Cosmos-Predict2 2B** 기반이다 (3건)
- **INT8 판은 모델+텍스트인코더+VAE 합쳐 4GB 미만**이라 VRAM 8GB급에서도 무난하다 (2건)"""),

    dict(seq=4, heading="WAN 2.2 — High/Low 분리가 표준", conf="high", as_of="2026-04-13", cf=False,
         posts=srcs("WAN 2.2 계열 워크플로우", "라이트닝·디스틸 로라가 병합된"),
         body="""**High/Low 모델을 나눠 쓰고 lightx2v(라이트닝) 로라를 별도로 물리는 것**이 표준 구성이다 (5건).
그냥 쓰면 느리고 품질도 나쁘다.

라이트닝·디스틸 로라가 **이미 병합된** 모델이라면 **cfg 1, 4~6스텝**으로 돌린다 (3건).

실측값은 [비디오 생성](video-generation.md) 참조."""),

    dict(seq=5, heading="MiniMax H3 가속 — 2026년 8월 기준", conf="high", as_of="2026-08-07", cf=False,
         posts=srcs("MiniMaxH3 Cache", "MiniMax H3 최속 조합", "int8convrot 양자화",
                    "RTX 3060 12GB", "Spectrum Apply"),
         body="""**이 절은 유효기간이 짧다.** 아래 합의가 만들어지는 데 며칠밖에 안 걸렸다.

| 합의 | 근거 |
|---|---|
| 가속은 **MiniMaxH3 Cache** 가 사실상 표준. TeaCache 계열로 스텝을 건너뛰는 게 아니라 계산 결과를 재사용해서 EasyCache·Spectrum보다 품질 손실이 적다 | 4건 |
| **int8convrot** 양자화가 fp8 tensorwise보다 품질이 좋고(Q8_0급) 조금 빠르며 캘리브레이션이 필요 없어 대세 | 4건 |
| **RTX 3060 12GB + RAM 32GB** 급에서도 구동된다 | 4건 |
| 최속은 **Cache + Mem Eff Sage Attention Patch + Patch Sage Attention KJ** 3종. 309.58초 → 94.73초 | 2건 |
| `MiniMaxH3*` 노드는 ComfyUI **0.30.0 이상에 내장**, `MiniMaxH3Cache` 만 git으로 별도 설치 | 3건 |
| Mem Eff Sage Patch·Patch Sage KJ는 **KJNodes 소속**이며 **Nightly** 를 지정해야 나타난다 | 2건 |
| **Spectrum Apply는 Cache·EasyCache와 같이 쓸 수 없다** | 3건 |
| 터보 LoRA는 Cache와 **원리가 겹쳐 병용 불가**. 품질은 Cache 쪽이 낫다 | 4건 |

자세한 것은 [MiniMax H3](minimax-h3.md) 참조."""),

    dict(seq=6, heading="LTX 2.3", conf="medium", as_of="2026-06-04", cf=False,
         posts=srcs("LTX 계열은 2D", "LTX2.3 distilled", "LTX2.3 은 비디오용", "dynamic_vram"),
         body="""- **2D·애니메이션이 약하다.** 아니메 LoRA를 물리거나 프롬프트에 스타일을 명시해야 한다 (3건)
- distilled 8스텝은 **cfg 1.0 고정**, 품질은 시그마·스케줄러(`linear_quadratic`)로 조절 (3건)
- 비디오용·오디오용 **VAE 두 개**와 듀얼 클립(`gemma3-12B-it` + `ltx-2.3_text_projection`)이 필요 (2건)
- **`dynamic_vram` 은 영상에서 반드시 켠다.** RAM 사용이 약 80GB → 10~15GB로 준다.
  반대로 **이미지 생성에서는 끄는 편이 낫다** (2건)"""),

    dict(seq=7, heading="여러 곳에서 반복되는 것", conf="high", as_of="2026-08-09", cf=False,
         posts=srcs("EXIF 가 든 이미지", "frame_interpolation", "ComfyUI Manager 로 업데이트",
                    "긴 영상은 통짜", "신규 모델 소식"),
         body="""| | 근거 |
|---|---|
| 워크플로우는 **EXIF가 든 이미지·영상**을 받아 ComfyUI 창에 드래그앤드롭해서 불러온다 | 5건 |
| VFI(프레임 보간) rife 모델은 **`models/frame_interpolation`** 폴더에 넣어야 인식된다 (`vfi`·`rife` 폴더 아님) | 3건 |
| **ComfyUI Manager로 업데이트하면 코어(내장 노드) 변경이 반영되지 않는다.** 본체는 git 또는 `update_comfyui.bat` | 2건 |
| 긴 영상은 통짜로 만들면 타이밍과 두 번째 상황을 제대로 못 그린다. **프롬프트를 나눠 이어붙인다** | 4건 |
| 채널에 올라오는 **신규 모델 소식의 상당수는 제작사 주장·유출·LLM 요약**이라 실사용 검증이 없다 | 5건 |"""),

    dict(seq=8, heading="⚠️ 뒤집힌 것들", conf="high", as_of="2026-08-05", cf=True,
         posts=srcs("0.31.0", "easycache", "Spectrum Apply", "dreamina"),
         body="""**국룰은 고정된 게 아니다.** 실제로 뒤집힌 사례들이다. 옛 글을 읽을 때 주의할 것.

| 지금 | ← 예전 | 언제 |
|---|---|---|
| 통합팩은 **0.31.0 판** | 0.11.1 권장 / 0.15.1은 충돌 잦아 비권장 | 2026-02 → 2026-08 |
| easycache는 **PR #12231로 수정됨** (nightly 필요) | easycache는 LTX2에서 동작하지 않는다 | — |
| **MiniMaxH3 Cache가 표준**, Spectrum은 충돌 대상 | Spectrum Apply로 30% 단축 | **2026-08-04 → 08-05** |
| Seedance는 **dreamina.capcut.com** | 2/24 글로벌 출시 예정, 중국 계정 필요 | 2026-02 |

세 번째를 보라. **하루 만에 뒤집혔다.** 8월 4일에 "Spectrum으로 30% 단축"이 올라왔고,
8월 5일에 더 나은 Cache가 등장하면서 Spectrum은 권장이 아니라 **충돌 대상**이 됐다.
이 분야의 정보 수명이 이 정도다."""),

    dict(seq=9, heading="아직 갈리는 것", conf="low", as_of="2026-08-09", cf=True,
         posts=srcs("sage attention은 ComfyUI 작업 속도", "sage attention을 켜면 손가락",
                    "터보(고속) LoRA 4스텝", "0.31.0"),
         body="""**sage attention이 10~15% 빠르다** — 찬성 8 / 반대 1
반대 근거: LTX2.3에서는 it/s만 11% 오를 뿐 실제 생성시간 차이는 크지 않다.
→ SDXL·t2i에서는 합의, **비디오 distilled 모델에서는 이견**.

**부작용**: sage를 켜면 **손가락 찐빠(손 왜곡)가 늘어난다**는 보고가 있다 (3건).

**터보 LoRA** — 찬성 2 / 반대 4
"25스텝 30분 → 4스텝 4분"은 속도만 보면 사실이다. 그러나 Cache와 병용이 안 되고
품질이 떨어져서, Cache를 이미 쓰고 있다면 **실사용에서는 Cache가 우세**하다는 게 다수 의견이다.

**portable 0.31.0** — 찬성 1 / 반대 1
라데온 ROCm sage 빌드 쪽에서는 "0.31.0은 버그로 안 되고 0.30.0에서만 동작"이라는 반례가 있다."""),
]


def main() -> None:
    with q._conn() as c, c.cursor() as cur:
        cur.execute(
            """INSERT INTO wiki_pages (slug,title,section,kind,stage,intro,generated_at,published)
               VALUES (%(slug)s,%(title)s,%(section)s,%(kind)s,%(stage)s,%(intro)s,now(),true)
               ON CONFLICT (slug) DO UPDATE SET intro=EXCLUDED.intro, kind=EXCLUDED.kind,
                    title=EXCLUDED.title, generated_at=now()
               RETURNING id""",
            PAGE,
        )
        pid = cur.fetchone()["id"]
        # 사람이 고친 항목은 남긴다
        cur.execute("DELETE FROM wiki_entries WHERE page_id=%s AND human_edited=false", (pid,))

        allp: set[int] = set()
        for e in ENTRIES:
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
        print(f"page {pid} | 항목 {len(ENTRIES)} | 원문 {len(allp)} | 출처없는항목 {cur.fetchone()['n']}")


if __name__ == "__main__":
    main()
