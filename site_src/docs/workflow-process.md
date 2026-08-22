# 워크플로우 안쪽 — 무엇을 만지나

> 워크플로우 **안쪽**을 다룬다 — 그룹 구조, 어느 노드를 만지나, 초안에서 무엇을 끄나.
> 숫자는 실측이거나 원문 인용이고, 추측은 넣지 않았다.

---

## 1. 모델 개요 — 무엇을 쓰고 무엇을 안 쓰나

### 채널 티어표 (2026-05 기준, 글 169601993)

| 티어 | 모델 | 성격 |
|---|---|---|
| 1 | GPT-Image 2 · Nano-Banana 2/Pro | 클라우드. 애니메 특화 아님 |
| 2 | Z-Image Turbo/Base · Qwen-Image-Edit-2511 | 로컬 일반 생성 |
| 3 | Flux.2 Kevin 9B · Chroma1-HD | Chroma 는 "무검열 중 성능 최고, 대신 엄청 느림" |
| **4** | **ANIMA 시리즈** · **NAI 4.5/V5** | **애니메 무검열** |
| 5 | NoobAI / ILXL 기반 SDXL | "가볍고 빠르지만 **구식**" |

**ANIMA 와 NAI 가 같은 티어다.** 로컬 최상위와 유료 서비스가 대등하다는 뜻이다.
해외 추천 리스트가 미는 WAI·NoobAI·Illustrious 는 채널 기준 한 단계 아래지만,
"노하우가 많아 가볍게 쓸 만하다"고도 하며 2인 영역분리는 실제로 이쪽으로 한다.

### 2026년 8월의 변화 두 가지

**ANIMA 2.9B (8/12 출시)** — `Gazingstars123/Anima-2.9B`

| | v1.1 | 2.9B |
|---|---|---|
| 지식 컷오프 | 2025-09 | **2026-07** |
| 추가 학습 | — | 170만 장 |
| 학습 해상도 | 512 비중 큼 | **70% 가 1k** |
| 태깅 | 단부루 | 단부루 + 자연어 |

단서 둘 — **제3자 튜닝본**(공식 아님)이고 **전용 커스텀 노드**를 따로 깔아야 한다.

**NAI V5 정식 출시 (8/21)** — 채널이 하루 만에 V5 글로 뒤덮였다.
유료 클라우드라 로컬로 가져올 수 없지만 **프롬프트는 가져올 수 있다**(아래 6절).

---

## 2. 왜 모델마다 작가 태그가 다르게 먹나

이걸 모르면 작가 조합이 왜 안 되는지 영원히 모른다.

| | 인코딩 방식 | 결과 |
|---|---|---|
| **SDXL / Illustrious** | 태그를 **개별 토큰화** | 가중치 조절만으로 작가가 섞인다 |
| **ANIMA** | qwen3 LLM 이 **프롬프트를 통째로** 인코딩 | 임베딩이 섞여 **평균이 나온다**. 가중치로 섞기 매우 힘들다 |

> ANIMA 는 비빔밥이다. 옷·인체·배경은 초코칩·건포도라 구분되는데,
> **작가는 파우더·시럽이라** 여러 개를 부으면 구분이 안 된다. — 글 177376366

여기에 **압축 평균 현상**이 겹친다 — 데이터가 많은 작가가 적은 작가를 이긴다.
후자에 가중치를 더 줘도 그렇다.

**Illustrious 는 또 다르다.** `rating`(general/sensitive/questionable/explicit) 태그가
하나라도 없으면 **작가 태그 자체가 무력화**된다.

---

## 3. 작가 태그 — 채널이 실제로 쓰는 법

채널 글에서 뽑은 작가 사용 기록 1,921행 / 고유 916명 기준이다.

**1. 혼자 안 쓴다.** 5~16명을 섞는다. 2명 이상이 **82.8%**, 중앙값 8명.

**2. 순서가 가중치보다 세다.**

> **앞쪽 작가 = 채색·몸매. 뒤쪽 작가 = 얼굴·눈.**
> 작가가 많아질수록 이 경향이 강해진다.
> 강조를 3.0 줘도 안 나오던 것이 **위치만 바꾸니** 나왔다. — 글 122522153, 151423873

**3. 가중치는 눌러 쓴다.** 명시하는 경우가 **8.4%** 뿐이고, 쓸 때는 **0.7~0.89 에 37%** 가 몰린다.
중앙값 0.80. 1.0 을 넘기는 경우는 드물다.

**4. 네거티브에도 작가를 박는다.**
`xinzoruo` `milkpanda` `bkub` `kurukurumagical` 처럼 싫은 그림체를 네거에 넣는다.
그리고 `-6::artist collaboration::` — 다인 캐릭터의 화풍 분열을 막는 표준 관용구다(39개 글에서 실사용).

**5. 탐색은 노가다가 아니라 파이프라인이다.**

```
작가 리스트 → 3~5명 랜덤 조합 100~300개 → 와일드카드 자동사냥
→ 생존작 EXIF 에서 작가 중복 카운트 → 8~12명으로 수렴
→ 가중치 랜덤 가차 → 이상형 월드컵
```

### 실제로 많이 쓰이는 작가

| 작가 | 사용 | 최빈 가중치 |
|---|---|---|
| `healthyman` | 34 | 0.55 |
| `wagashi (dagashiya)` | 32 | — |
| `tianliang duohe fangdongye` | 27 | — |
| `blue gk` | 26 | 0.8 |
| `mx2j` | 24 | — |
| `freng` | 22 | 0.85 |
| `ie (raarami)` | 18 | 0.4 |

반복되는 조합: `chomoran + inoue kiyoshirou + tianliang duohe fangdongye` (12회)

!!! tip "작가를 그림 보고 고르기"
    `comfyui-anima-artist-browser` 노드 + `Leo0186/anima-style-explorer` 미러(MIT).
    작가 **42,509명**의 프리뷰가 있고, 그 프리뷰는 단부루 스크랩이 아니라
    **고정 프롬프트로 ANIMA 가 직접 생성한 이미지**다 — 즉 그 모델에서 실제로 어떻게 나오는지 보여준다.

    ⚠ 원본 `ThetaCursed` 계정이 통째로 404 가 됐다. `js/config.js` 의 `CDN_BASE` 를
    미러로 바꿔야 이미지가 뜬다.

---

## 4. 워크플로우 구조 — AiO 의 그룹 12개

ANIMA All in One 워크플로우는 노드 103개, 그룹 12개다. 그룹이 좌→우로 **단계 순서대로** 놓여 있다.

```
LoRA → T2I → I2I → 2.모델로드 → 3.ANIMA생성 → 4.HighRes
     → 5.Inpainting → 6.1얼굴 → 6.2눈 → 7.Upscale → 8.저장 → 8.1메타
```

이게 조작판이다. **워크플로우는 배관이고, 그룹 스위치가 밸브다.**

| 그룹 | 하는 일 |
|---|---|
| LoRA | 로라 스택 + 트리거워드 |
| T2I / I2I | 시작점 — 글에서 시작할지, 그림에서 시작할지 |
| 2. 모델 로드 | 체크포인트/UNET · CLIP · VAE |
| **3. ANIMA 생성** | **1차 샘플러. 여기서 그림이 생긴다** |
| 4. HighRes | 1.5배 확대 후 재생성 (denoise 0.5) |
| 5. Inpainting | 부분 수정 |
| 6.1 / 6.2 | 얼굴 · 눈 디테일러 (SAM3 마스킹) |
| 7. Upscale | 2배 (denoise 0.1~0.4) |
| 8 / 8.1 | 저장 · 메타데이터 |

### 눈에 보이는 것은 조작판이고, 일은 서브그래프 안에서 한다

노드 103개를 다 이해할 필요가 없다. 실제 구조는 이렇다.

| 보이는 노드 | 정체 |
|---|---|
| `MarkdownNote` | **배포자가 넣어둔 그룹별 가이드.** 파라미터 권장값이 다 적혀 있다 |
| UUID 이름의 노드 (`889edc0f-…`) | **서브그래프.** 샘플러·디테일러 같은 실제 작업이 이 안에 들어 있다 |
| `SetNode` / `GetNode` | KJNodes 변수. 선을 안 끌고 값을 옮긴다 |
| `Image Comparer` · `PreviewImage` | 단계별 결과 확인용 |

**즉 겉면은 손잡이만 모아 둔 판이다.** 각 그룹의 `MarkdownNote` 를 먼저 읽는 것이
이 워크플로우를 배우는 가장 빠른 길이다 — 아래 표가 그 요약이다.

### 그룹별로 무엇을 만지나

<small>배포자의 in-workflow 가이드에서 옮긴 것. 권장값은 원문 표기 그대로다.</small>

| 그룹 | 만지는 값 | 권장 · 주의 |
|---|---|---|
| **LoRA** | `lora_stack` · `strength` · `trigger_words` · `style_prompt` | 트리거워드를 **프롬프트에서 직접 고치지 말 것** — 프리셋 기준을 먼저 본다. 로라 경로가 다르면 모델 로드가 아니라 **로라 적용 단계**에서 실패한다 |
| **T2I** | `width`/`height` · Quality Tags · `use_anima_mod_guidance` | 프롬프트 칸은 **위에서 아래 순서로 조립**된다. 꺼진(`enabled` off) 칸은 안 들어간다. Mod Guidance 를 켜면 색감·구도가 과하게 고정될 수 있어 OFF 와 비교한다 |
| **I2I** | `LoadImage` · `megapixels` · `vae_name` | **T2I 만 쓸 때도 `LoadImage` 가 잘못돼 있으면** I2I 를 켜는 순간 실패한다. VAE 는 모델 로드 섹션과 맞춘다 |
| **2. 모델 로드** | `unet_name`/`clip_name`/`vae_name` · `cfg` · `steps_total` · `shift` | **`Sage_Attention` · `TorchCompile` 은 기본 OFF.** 기본 생성이 성공한 뒤에만 켠다. Windows 에서 Triton 오류가 나면 도로 끈다 |
| **3. ANIMA 생성** | DCW `lambda_l/h` · CWM `alpha_l/h` · SMC | 기본값 `0.05`/`0.01`. **Flow 계열은 약 2배.** CWM 은 과하면 과선명·구도 고정이 생긴다 |
| **4. HighRes** | 확대 배율 · denoise | 1.5배 재생성. 여기가 **그림체와 디테일**을 정한다 |
| **5. Inpainting** | `PreviewBridge` 마스크 · `lllite_name` · `strength` · `denoise` | LLLite `strength` 는 **1.0 부터 시작해 과하면 낮춘다**. 커스텀 노드와 controlnet 모델이 없으면 아예 실행 불가 |
| **6.1 / 6.2 디테일러** | 검출 임계값 · denoise | 얼굴·눈을 SAM3 로 잡아 확대 후 다시 그린다 |
| **7. Upscale** | `upscale model` · `upscale_by` · `denoise` · 타일 | 권장 `4x-AnimeSharp.pth` / `2` / **`denoise 0.11`** / `euler`+`sgm_uniform` / `steps 15` / 타일 `512` · `mask_blur 8` · `tile_padding 128`. **VRAM 부족의 주범이 타일 패딩이다** |
| **8. 이미지 저장** | `filename_prefix` · `format` | 배포본 기본이 **webp** 다. 호환성이 필요하면 png 로 바꾼다 |
| **8.1 Metadata** | 자동 | prompt·모델·LoRA·샘플러·크기를 이미지에 박는다. **선별 재실행이 되려면 이게 켜져 있어야 한다** |

!!! tip "오류가 나면 어디를 의심하나"
    배포자가 명시한 순서다 — **기본 해상도 + Mod Guidance OFF + Sage_Attention disabled** 조합으로
    먼저 한 장을 성공시키고, 거기서부터 하나씩 켠다.
    그리고 **이미지 저장 오류와 메타데이터 오류를 구분**해서 봐야 한다. 8.1 은 Civitai 접근을 타므로
    저장 자체가 목적이면 이 섹션 문제는 따로 취급한다.

### 프롬프트는 4칸으로 쪼갠다

```
1번  작가 태그 + 로라 트리거     ← 그림체
2번  메타 태그                  ← 인원수·작품명·rating
3번  일반 프롬프트              ← 캐릭터·동작·배경   ★ 매일 만지는 곳
4번  후행 퀄리티 태그
```

> "편의성을 위해 분리해놨을 뿐, **다 합쳐서 들어감**" — 글 171941799

와일드카드나 LLM 출력은 **3번 칸을 덮어쓰는 방식**으로 붙는다.

!!! warning "퀄리티 태그는 눌러서 쓴다"
    `masterpiece` 를 1.0 으로 넣으면 오히려 촌스러워진다.
    배포자 기본값은 `(score_8:0.65)` 처럼 **전부 1 아래로** 눌려 있다.

---

## 5. 초안 → 마감 — 세 가지 방식

채널이 쓰는 방식은 셋이고, **AiO 하나로 전부 된다.**

| 방식 | 어떻게 | 언제 |
|---|---|---|
| **(a) 2패스** | `3.생성`(저해상도) → `4.HighRes` → `7.Upscale` | 한 장을 끝까지 밀 때 |
| **(b) 모델 릴레이** | ANIMA 로 구도 → `I2I` 로 WAI 에 넘겨 마감 | ANIMA 에 없는 SDXL 로라·화풍을 얹을 때 |
| **(c) 대량 초안 → 선별** | 다 뽑고, 마음에 드는 PNG 를 끌어다 놓아 **같은 시드로 재실행** | 평소 |

> "**저해상도 스텝이 구도**에 큰 영향, **고해상도 스텝이 그림체 및 디테일**" — 글 170829356

> "IL 로 hires fix 하는 과정에서 화풍을 덮어쓰기 때문에 **기존 IL 생태계를 활용할 수 있음**" — 글 161453678

**(c) 가 성립하려면 `8.1 Metadata 저장`이 켜져 있어야 한다.** PNG 에 워크플로우가 박혀야
나중에 끌어다 놓았을 때 시드·설정이 복원된다.

### 그룹 온오프 표

| 그룹 | 초안 | (a) 2패스 | (b) 릴레이 | (c) 선별 재실행 |
|---|---|---|---|---|
| LoRA · T2I · 2 · 3 | ⭕ | ⭕ | ⭕ | ⭕ |
| I2I | ✗ | ✗ | **⭕** | ✗ |
| 4. HighRes | **✗** | ⭕ | ✗ | ⭕ |
| 5. Inpainting | ✗ | ✗ | ✗ | ✗ |
| 6.1 · 6.2 디테일러 | **✗** | ⭕ | ⭕ | ⭕ |
| 7. Upscale | **✗** | ⭕ | ⭕ | ⭕ |
| 8 · 8.1 저장 | ⭕ | ⭕ | ⭕ | **⭕ 필수** |

> "**업스케일까지 하면 2분이 넘는다.** 굳이 할 이유가 없는 것 같으니…
> **디테일러만 돌려도 1분이나 걸리니까**" — 글 171941799

초안에서 4·6·7 을 끄면 **20초대**가 된다.

### 전환 스위치를 심는 법

그룹을 하나씩 끄는 건 실수가 난다. `Fast Groups Bypasser (rgthree)` 로 한 번에 토글한다.
**이 노드는 프론트엔드 전용이라 `/object_info` 에 안 뜬다** — 서버 목록에 없다고 없는 게 아니다.
노드 타입 문자열은 `Fast Groups Bypasser (rgthree)` 이고, `properties.matchColors` 로 색을 지정한다.

색을 나눠 두지 않으면 필터가 걸리지 않는다. 우리는 이렇게 나눴다.

| 색 | 그룹 | 뜻 |
|---|---|---|
| **노랑** `#b58b2a` | 4. HighRes · 6.1 얼굴 · 6.2 눈 · 7. Upscale | **마감. 초안에서는 끈다** |
| **보라** `#8e3f9e` | 5. Inpainting | 가끔 쓰는 수정 |
| **초록** `#3f7e3f` | I2I | 모델 릴레이용 시작점 |
| 파랑(기본) | 나머지 | 항상 켜 둔다 — 손대지 않는다 |

```json
"properties": {
  "matchColors": "yellow, purple, green",
  "sort": "position",
  "showNav": true
}
```

`sort: position` 을 주면 목록이 워크플로우의 좌→우 순서 그대로 나온다.

!!! danger "스위치만 꺼서는 안 되는 경우가 있다"
    워크플로우 안의 다른 출력 노드(`PreviewImage`·`Image Comparer`)가 그 단계를 요구하면
    꺼도 결국 다 돈다(실측 157초). 그래서 별도의 초안 전용 최소 그래프를 짜기도 한다.

---

## 6. 남의 그림에서 프롬프트 가져오기

아카는 본문에 보이는 `ac.arca.live` 이미지를 WEBP 로 바꾸며 메타데이터를 지운다.
그러나 `<img data-originalurl="...ac-o.arca.live/...&type=orig">` 에 **원본 PNG 링크가 살아 있다.**

!!! warning "호스트만 바꾸면 403 이다"
    서명 키가 다르다. HTML 의 `data-originalurl` 속성값을 **그대로** 써야 한다.
    그리고 생성정보는 PNG 맨 앞에 있으므로 **앞 64KB 만 받으면 된다**
    (9장 통째로 받으면 90초, Range 요청이면 6초).

### NAI 프롬프트를 로컬로 옮길 때 — 실측 함정

| 원문 | 그대로 옮기면 | 대응 |
|---|---|---|
| 구도 태그 없음 | **극단적 클로즈업** | `portrait` 등을 채운다 |
| `blurry Edge` | **어두운 비네팅** | → `blurry background` |
| `thick lines` | 단부루에 없어 버려짐 | → **`thick outlines`** |
| `-6::saturated::` | **채도 전멸** | 네거티브 가중치 1.30 상한 |
| `year 2025` | 우리 CSV 에 없어 버려짐 | **살려야 한다**(실제 태그다) |
| 캐릭터 이름 | ANIMA 가 모름 | 로라 필요 |

**NAI 는 프롬프트에 구도가 없으면 알아서 잡아주지만 ANIMA 는 안 그런다.**

**로라 강도는 인물이 화면을 차지하는 비율에 비례한다.** 배경이 넓으면 0.45 로도 버티지만,
얼굴 클로즈업에서 0.45 로 낮추면 캐릭터가 통째로 무너진다(검은머리·파란눈). **0.65 가 안전선.**

---

## 7. 제어 기능 — ANIMA 에서 되는 것

| 기능 | ANIMA | SDXL / WAI |
|---|---|---|
| ControlNet (openpose 등) | ❌ **구조적으로 불가** | ⭕ 단 모델 파일을 받아야 함 |
| **LLLite** | ⭕ **유일한 수단** | — |
| 시점 제어 | ⭕ `KR_CameraControl` | — |
| 영역분리 | ⭕ `EasyUseAnimaRegional`(베타) | ⭕ `Regional Script 💬ED` |
| 인페인팅 | ⭕ LLLite inpainting | ⭕ noobai inpainting |
| SAM3 마스킹 · 디테일러 | ⭕ | ⭕ |

> "SDXL 용이라 anima 랑 호환이 안 돼서 쓰려고 하면 **100% 오류**" — 글 169455470

ANIMA 는 Cosmos 기반 DiT + Qwen3 인코더라 SDXL ControlNet 텐서가 애초에 맞지 않는다.
배포자들이 워크플로우를 **SDXL 판 / ANIMA 판으로 아예 분리 배포**하는 이유다.

**우회로**: ANIMA 로 뽑고 → 포즈 추출 → IL/ILXL 에서 ControlNet 적용 (하이브리드).

### LLLite 실전값

| | 값 |
|---|---|
| 완전 복제 | strength 1.0 / start 0.0 / end 1.0 |
| **구도만 딸 때** | **strength 0.8 / start 0.0 / end 0.4** |
| 제약 | **LLLite 끼리 중복 적용 불가** |

!!! danger "파일 크기로 진품을 확인하라"
    커뮤니티판을 파일명만 바꿔 배포하는 경우가 있다.
    `anima-lllite-inpainting-v2` 는 **정품이 65.8MB** 다. 23.3MB 짜리는 hanzogak 015 리네임판이다.

---

## 8. 함정 모음

- **`DiTSpectrumPatch` 는 ComfyUI 프로세스를 죽인다.** `copy.deepcopy` 무한 재귀 → 스택 오버플로.
  잡을 수 없고 포트가 닫힌다. 반드시 bypass.
- **VRAM.** 16GB 카드에서 ollama 가 9GB 를 쥔 채 샘플러가 돌면
  `CUDA error: unknown error` 로 **프로세스째 사망**한다. 그림 뽑을 때 로컬 LLM 은 9B 이하로.
  `OLLAMA_KEEP_ALIVE=0` 을 걸어 두면 응답 직후 VRAM 을 놓는다.
- **GGUF 에 파라미터가 없는 경우가 많다.** `num_ctx` 가 기본 4096 으로 돌고 stop 토큰이 없어
  모델이 안 멈춘다. Modelfile 로 파생본을 만들어 박아야 한다.
- **`AiO_v60_local.json` 의 LLLite 노드가 ComfyUI 0.33 코어와 충돌한다.**
  코어가 같은 노드 ID 를 가져가서 bypass 를 풀면 검증 실패한다.
  `Apply Anima ControlNet-LLLite (sd-scripts)` 로 재배치해야 한다.
- **`Getting Started` 폴더를 "기본 샘플"로 착각하지 말 것.** 진짜 샘플은 11개뿐이고
  나머지는 사용자가 저장한 것이다. 현역 워크플로우가 여기 묻혀 있을 수 있다.

---

## 9. 워크플로우 관리 — 규칙은 없다

한국 채널과 해외 커뮤니티 **양쪽 다 파일명 규칙이 없다.**
ComfyUI 공식 답변조차 2026년에 *"탐색기로 `user/default/workflows` 에 주제 폴더를 만들어라"* 다.
UI 에서 폴더를 만드는 기능 요청은 16개월째 열려 있다.

그래서 해외가 실제로 하는 것:

- **쌓인 것을 다 살리지 않는다.** *"Short answer, we don't lol."*
  실제 추천 프로세스는 **2-설치본 승격 모델** — 실험은 사본에서 하고,
  **한 달 넘게 살아남은 것만** 본 설치로 옮긴다.
- **모듈러가 압승.** 최고 득표 이유: *"**ComfyUI 가 업데이트로 워크플로우를 자주 깨뜨린다.**
  그래서 하나를 너무 복잡하게 안 만든다"*
- **Subgraph 를 재사용 라이브러리로 믿지 마라.** 공식 문서가 인정한다 —
  블루프린트 인스턴스는 **독립 복사본**이라 고쳐도 다른 워크플로우에 전파되지 않는다.
- **git 은 diff 가 무의미하다**(링크 ID 가 매번 바뀐다). 백업용으로만.
  **API 포맷으로는 절대 커밋하지 마라** — 복구 불가 사례가 있다.

### 진짜 표준은 워크플로우 *안쪽*에 있다

Nathan Shipley 규약이 사실상의 커뮤니티 표준이다.

1. 줌아웃해도 보이는 **큰 라벨**
2. **기능별 그룹** — Input / Model / Conditioning / Sampling / Output
3. **좌→우 흐름**, 모델 파이프라인은 상단
4. **Set/Get 노드**로 선 줄이기 — 서술적 이름, 남용 금지
5. **색상**: 파랑 image · 보라 model · 노랑 conditioning · 빨강 sampling · 초록 output
6. **rgthree Fast Group Bypasser** — 선택 기능은 노란 그룹에 몰아넣고 한 번에 토글

AiO 의 그룹 12개가 정확히 이 구조다. **파일 정리보다 이쪽이 투자 대비 효과가 크다.**

---

## 10. 쓸 만한 외부 자원

| 용도 | 자원 | 상태 |
|---|---|---|
| 작가 썸네일 | `Leo0186/anima-style-explorer` — 42,509명 | MIT 미러. 원본 계정은 404 |
| 작가 브라우저 노드 | `Shiba-2-shiba/comfyui-anima-artist-browser` | CDN 주소를 미러로 고쳐야 뜬다 |
| 로라 관리 | `willmiao/ComfyUI-Lora-Manager` | ★1,384, 활발. 프리뷰·트리거워드 자동 |
| 태그 사전 | `DraconicDragon/dbr-e621-lists-archive` — 201,269개 | 매월 갱신 |
| 자동완성 | `newtextdoc1111/ComfyUI-Autocomplete-Plus` | 한국어 별칭 검색 |
| 와일드카드 | Impact Pack **v2** 문법 | 2025-11 대개편 |
| 태그 생성 LLM | `KohakuBlueleaf/z-tipo-extension` (TIPO) | ★616 |

### 죽은 것

```
comfyui-dynamicprompts / sd-dynamic-prompts / Comfyroll   2024-07 정지
IF_AI_tools                                                archived
ThetaCursed 계정 전체 · Illustrious Style Explorer          404
comfyui-workspace-manager                                  저자가 종료 선언
```

---

## 관련 문서

- [ANIMA](anima.md) — 모델 자체의 설정값
- [프롬프트](prompting.md) — 태그 작성법 전반
- [로라 사용법](lora-usage.md)
- [ControlNet](controlnet.md)
- [디테일러](detailer.md) · [업스케일](upscale.md) · [인페인팅](inpainting.md)
- [VRAM](vram.md) — 메모리 부족 대응
- [문제 해결](troubleshooting.md)
