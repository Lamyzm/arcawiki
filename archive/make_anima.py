"""ANIMA 개체 문서.

카드 30장 넘게 쌓였고 Claim 21개가 붙었다. 샘플러 주장은 support 7 로
이 프로젝트에서 가장 여러 글이 같은 말을 한 항목이다.
"""

import queue_api as q


def srcs(*keywords):
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
    slug="anima", title="ANIMA", kind="개체", stage=None, section="ANIMA",
    intro=("NVIDIA Cosmos-Predict2 2B 기반 이미지 모델. 자연어 이해가 좋은 대신 화풍이 약해서, "
           "**Illustrious 와 2단으로 엮어 쓰는 것**이 채널의 표준 운용이다."),
)

E = [
    dict(seq=1, heading="샘플러 — 이것만은 지킬 것", conf="high", as_of="2026-08-06", cf=False,
         posts=srcs("Euler A + automatic"),
         body="""**일곱 개 글이 독립적으로 같은 말을 했다.** 이 프로젝트에서 가장 강한 합의다.

```
쓸 것    Euler  또는  ER SDE     +   simple  또는  SGM uniform
쓰지 말 것    Euler A  +  automatic/normal
```

Euler A + automatic 조합에서 **그림이 기괴해진다.** 다른 설정을 아무리 만져도 이걸 바꾸지 않으면
해결되지 않는다."""),

    dict(seq=2, heading="2단 구성 — ANIMA로 구도, Illustrious로 화풍", conf="high", as_of="2026-04-20", cf=False,
         posts=srcs("hires fix 해 화풍을 덮는", "LLM 인코더가 프롬프트를 통째로"),
         body="""ANIMA는 **자연어 이해력은 좋지만 화풍과 미학적 구도가 약하다** (4건).
그래서 ANIMA로 구도를 잡고 **Illustrious/SDXL로 hires fix 해서 화풍을 덮는** 2단 구성이 쓰인다.

**왜 화풍이 약한가** — ANIMA는 qwen3 기반 LLM 인코더가 프롬프트를 **통째로** 인코딩한다.
그래서 작가 태그 임베딩이 평균으로 뭉개지고, **SDXL처럼 가중치만으로 화풍을 섞을 수 없다** (4건).

> 작가별 Conditioning을 분리해 average/concat 하는 우회도 시도됐지만,
> **가장 앞 작가의 그림체만 나와 사실상 실패**했다 (2건)."""),

    dict(seq=3, heading="프롬프트 쓰는 법", conf="medium", as_of="2026-07-25", cf=True,
         posts=srcs("ANIMA 자연어 프롬프트는 최소 2문장", "작가 태그별 Conditioning"),
         body="""- **최소 2문장 이상** 쓴다
- 품질·아티스트 태그는 **앞부분**에 둔다
- 여러 캐릭터를 넣을 때는 **이름만 나열하지 말고 외형을 설명**한다

*(3건)*

> ⚠️ **여기는 자료가 갈린다.** 한쪽은 "태그를 자연어로 변환해 넣는 쪽이 타율이 좋다"고 하고,
> 다른 쪽(gems v5)은 "서술형 자연어 금지, 순수 단부루 태그만"이라고 한다. 찬성 1 / 반대 1로
> **결론이 안 났다.** 둘 다 해보고 판단할 것.

**Regional Prompter**는 가로·세로 2등분 또는 3등분까지만 지원하고 아직 베타 수준이다.
구역과 구역별 LoRA가 늘수록 고속 로라를 써도 느려진다 (2건)."""),

    dict(seq=4, heading="LLLite 컨트롤넷 — 경로가 바뀌었다", conf="high", as_of="2026-05-22", cf=False,
         posts=srcs("models/model_patches 로 옮기고", "ComfyUI\\\\models\\\\controlnet 에 넣고"),
         body="""> ⚠️ **ComfyUI 업데이트로 경로가 바뀌었다.** 서로 다른 두 글에서 **각각 댓글로 같은 정정**이
> 나왔다. 본문만 읽으면 둘 다 옛 경로를 알려준다.

| | 경로 | 노드 |
|---|---|---|
| **지금** | `models/model_patches` | `ModelPatchLoader` 를 `Apply Anima ControlNet-LLLite` **앞에** 연결 |
| 예전 | `models/controlnet` | `Apply Anima ControlNet-LLLite` 만 |

**인페인팅에서 특히 중요하다.** LLLite 인페인팅 모델을 물리면 **denoise 0.9 이상에서도 원본
일관성이 유지**되지만, LLLite 없이는 **0.7 이상에서 마스크 경계가 깨진다** (2건)."""),

    dict(seq=5, heading="가속 — 무엇이 얼마나", conf="high", as_of="2026-06-04", cf=False,
         posts=srcs("Spectrum 계열 가속은 ANIMA 단일", "sage attention 은 약 9~11%",
                    "블록 컴파일", "torch.compile 의 ANIMA 가속 효과"),
         body="""| 방법 | 효과 | 근거 |
|---|---|---|
| **Spectrum 계열** | **+116~124%** (2배 이상) — 단일 최적화 중 최대 | 3건 |
| torch.compile | 14~41% — **GPU에 따라 편차가 크고 일부는 오히려 느려지거나 동작 안 함** | 2건 |
| 블록 컴파일 (`compile_transformer_blocks_only`) | 전체 컴파일보다 **컴파일 시간이 짧아 실용적** | 3건 |
| sage attention | 9~11%, 품질 손상 거의 없음 | 3건 |
| int8rowwise 양자화 | bf16 대비 +43~47%. 단 **로라를 적용하면 +21~28%로 절반 가까이 줄어든다** | 2건 |

**`dynamic vram` 은 끈다** (4건). 이미지 생성에서는 끄는 쪽이 빠르고,
**torch.compile을 쓸 때는 `--disable-dynamic-vram` 이 사실상 필수**다.

> 영상 생성은 반대다 — LTX 등에서는 켜야 RAM이 80GB → 10~15GB로 준다. [국룰](kukroul.md) 참조.

**튜링(RTX20·GTX16) 세대**는 bf16을 못 써서 `KSampler(spectrum)` 대신
`ruwwww/ComfyUI-Spectrum-sdxl` 와 Anzhc의 `Anima Mod Guidance` 로 우회한다 (2건)."""),

    dict(seq=6, heading="같이 쓰면 안 되는 조합", conf="high", as_of="2026-05-31", cf=False,
         posts=srcs("터보(고속) 로라를 쓸 때는 Spectrum", "Anima Artist Mixer 는 KSampler",
                    "Spectrum 가속 노드는 ancestral", "ComfyUI-SPEED 는 샘플링 중"),
         body="""| A | B | 결과 |
|---|---|---|
| Spectrum | **ancestral(euler a)·sde 샘플러, karras 스케줄러** | 호환 안 됨 |
| Spectrum | Anima Artist Mixer | **노이즈만 나옴** → `ruwwww/comfyui-spectrum-sdxl` 의 모델 패치형을 쓰면 함께 동작 |
| Spectrum·Layer Replay | **터보(고속) 로라** | 부적합. **터보 로라를 쓰면 Anima NAG 를, 안 쓰면 정반대로 Spectrum 을 쓰고 NAG 를 뺀다** |
| ComfyUI-SPEED | euler 계열 아닌 샘플러 | 노이즈 재주입 구조라 euler 계열에서만 정상 동작 |

**SPEED vs Spectrum 은 스텝 수에 따라 역전된다:**
30스텝에서는 SPEED 7초 / Spectrum 10초인데, **50스텝에서는 13초 / 12초로 뒤집힌다** (2건)."""),

    dict(seq=7, heading="워크플로우와 버전", conf="high", as_of="2026-06-07", cf=False,
         posts=srcs("All in One 워크플로우는 V5/V5.1", "All in One v5 는 ComfyUI 포터블 0.20.1",
                    "All in One 워크플로우 v2 는 생성", "EasyUseAnima 는 릴리스보다"),
         body="""**All in One V5 / V5.1 (2026-06) 이 기준판**이다. 그 이전 preview3 시절 판들은
**작성자 스스로 낡았다고 철회**했다 (4건).

**포터블 버전을 가린다** (2건):
```
0.20.0 미만  →  sam3 노드 미지원
0.20.1       →  권장
0.21.0 이상  →  node2.0 문제로 UI 가 깨질 수 있음
```

**EasyUseAnima 는 릴리스가 아니라 git(main 브랜치)** 으로 설치해야 한다.
수정이 main 에 먼저 올라가서, 릴리스를 받으면 인풋 소켓 누락 같은 버그가 남아 있다 (2건).

*(참고)* v2 구조는 `생성 → SeedVR2 1차 업스케일 → SAM3 디텍터 디테일러 → USDU 2차 업스케일` 이었다."""),

    dict(seq=8, heading="디테일러 — 방침이 뒤집혔다", conf="medium", as_of="2026-06-03", cf=True,
         posts=srcs("디테일러 자체가 맞는 방법이 아니라", "디테일러는 전신 → 얼굴 → 눈"),
         body="""| 지금 | ← 예전 |
|---|---|
| **디테일러 자체가 ANIMA에 맞는 방법이 아니다.** Highres 를 먼저 하고 **눈 정도만** 디테일러를 돌린다 (3건) | 전신 → 얼굴 → 눈 순으로 돌리며, 전신 디테일러가 머리카락·손 찐빠를 잡아준다 (2건) |

**같은 작성자가 철회했다.** 옛 글을 보고 전신 디테일러부터 돌리면 헛수고다."""),
]


def main() -> None:
    with q._conn() as c, c.cursor() as cur:
        cur.execute(
            """INSERT INTO wiki_pages (slug,title,section,kind,stage,intro,generated_at,published)
               VALUES (%(slug)s,%(title)s,%(section)s,%(kind)s,%(stage)s,%(intro)s,now(),true)
               ON CONFLICT (slug) DO UPDATE SET intro=EXCLUDED.intro, kind=EXCLUDED.kind,
                    title=EXCLUDED.title, generated_at=now() RETURNING id""",
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
        cur.execute("UPDATE entities SET page_id=%s WHERE name='ANIMA'", (pid,))
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
