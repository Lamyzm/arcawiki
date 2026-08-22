# 모델 카드 — 하나하나 정확히

> 두루뭉실한 설명 대신 **파일명·숫자·원문 인용**으로만 적는다.
> 확인 못 한 항목은 "확인 안 됨"이라고 적었지 추측하지 않았다.
>
> 근거: 채널 글 8,001건 + safetensors 헤더 실측 + ComfyUI 0.33.0 공식 템플릿.

---

## 계보 — 무엇과 무엇이 남남인가

이걸 먼저 알아야 "왜 로라가 안 붙나"가 풀린다.

```
SDXL ─┬─ Illustrious XL (Onoma AI, 한국)
      │      └─ NoobAI-XL (Laxhar Lab)
      │      └─ WAI-illustrious-SDXL
      │
NVIDIA Cosmos-Predict2 ── ANIMA (CircleStone Labs)
      │      └─ waiANIMA (병합본)
      │
알리바바 ── Z-Image (S3-DiT)
NovelAI 자체 ── NAI V4.5 / V5
```

> 아니마는 Cosmos-Predict2 기반이고 일러스트리어스는 SDXL 기반이니
> **둘은 서로 다른 핏줄인 남남**이라고 할 수 있다.

> sdxl 이랑 anima 는 **휘발유차랑 경유차 정도의 차이**라 보면 됨. **호환되는 거 하나도 없음**

!!! danger "이름에 속지 말 것"
    **`waiANIMA` 는 SDXL 이 아니다.** 이름에 WAI 가 붙었을 뿐 ANIMA 계열이다.
    부속(Qwen 텍스트 인코더·VAE)도 ANIMA 것을 쓴다.

---

# 이미지 모델

## ANIMA

| | |
|---|---|
| **정체** | CircleStone Labs. **2B DiT**, NVIDIA Cosmos-Predict2-2B 기반. Transformer 블록 28개 |
| **크기** | **4.18 GB / 2.09B BF16** (실측) |
| **VRAM** | 최소 6GB. 30스텝 1k 에서 **7.6~7.9GB** |
| **속도** | 5070Ti **16~17초** / 4060 45~50초 |
| **컷오프** | **2025년 9월** |
| **입력 한계** | **512 토큰, 영어만** |

### 권장 설정 (공식)

```
steps      30~50
CFG        4.0~6.0
sampler    er_sde  또는 euler_a
scheduler  simple  또는 beta
shift      3.0          ← 0 이면 검은 화면
denoise    1.0
해상도      512²~1536²   (832×1216 · 1024×1536 · 1216×832)
```

### 부속 — 세 조각을 각각 다른 폴더에

```
anima-aesthetic-v1.1.safetensors  →  models/diffusion_models   (checkpoints 아님!)
qwen_3_06b_base.safetensors       →  models/text_encoders      CLIPLoader type "stable_diffusion"
qwen_image_vae.safetensors        →  models/vae
```

!!! warning "텍스트 인코더는 순정이어야 한다"
    > 반드시 **튜닝되지 않은 순정 Qwen3-0.6B-base** 를 사용해야 한다.
    > 그렇지 않으면 모델에서 나오는 토큰이 어긋나면서 타율이 떨어질 수 있다.

### 특수 문법

**작가 태그에 `@` 가 필수다.**

```
newest, year2024, (masterpiece, best quality), score_7, aesthetic, general, safe,
1girl, @ayaxno, @miokuri, (@suisei 1121), (@signalviolet:0.7)
```

**가중치를 SDXL 보다 크게 준다.**
> 가중치가 필요하다면 **`:2` 정도에서 시작** … **4 이상 남발하면 검은 화면**

작성 순서: `[quality/meta/year/safety] [1girl] [character] [series] [artist] [general]`

### 잘하는 것 / 못하는 것

> **208×304 해상도인데 충실하게 프롬프트를 이행한다.** SDXL 기반 모델에선 절대 불가능했던 이행력임.

> ilxl 과 아니마의 가장 큰 차이점은 자연체 어쩌구가 아니다.
> **480i급 구린 폴더폰의 사진기가 1080p 스마트폰 카메라가 된 것**이 가장 큰 차이점이다.

> 아니마의 최대단점이 **노이즈를 너무 제거해서 그림의 채색들을 단순하게 만들고
> 보더를 강조**해서 굉장히 ai틱한 게 두드러진다는 것임

> Anima 는 상당히 음란해서 **안 야한 거 뽑고 싶으면 꼭 `safe` 태그**를 넣는 것이 좋음

### 버전 차이

| | |
|---|---|
| **base v1.0** | 원판 |
| **aesthetic v1.1** | base + 증류/채색 로라 병합 후 파인튜닝 |
| **2.9B** | 제3자 튜닝. 블록 28→40개로 확장, 컷오프 **2026-07** |

v1.1 실측 소감:
> **손가락 찐빠율이 확 줄어들었다** · 전반적으로 **컬러톤이 쿨톤**이 됨 ·
> 기존 아니마가 너무 프롬대로만 만들었다면 **대충 던져줘도 배경·조명·이펙트를 그럴싸하게 말아준다**

2.9B 평가는 갈린다:
> 호 — 신캐를 로라 없이 뽑을 수 있다는 점에서 커스텀 노드 정도의 불편함은 감수할 만하지
> 혹 — 그 소모값 대비 **너무 날것이라 쓰까먹기로 했음**

### 터보 로라

`anima-turbo-lora-v0.2.safetensors` · **로라 1.0 / 8 steps / CFG 1**

실측: 로라 없이 CFG5·30스텝 **13.29초** → 로라 1.0·CFG1·8스텝 **2.85초**

---

## WAI Illustrious — SDXL 계열

| | |
|---|---|
| **정체** | Illustrious 1 파인튜닝. **SDXL UNet** |
| **크기** | **6.94 GB / 3.47B** (UNet+CLIP+VAE 통합) |
| **VRAM** | 최소 6GB |
| **속도** | 4060 Laptop 1024² + SAM3 디테일러 **약 40초** |

> 참고로 **WAI NSFW 는 이름만 다르고 같은 것**이니 괜히 이상한 곳 찾아 헤매지 마.

### 권장 설정

```
sampler    Euler a          국룰 조합
scheduler  SGM Uniform
CFG        5~7
steps      28~30
clip skip  2
해상도      1024×1024 · 832×1216
```

### 특수 문법 — ANIMA 와 정반대

**`artist:` 접두가 필수다.**

> ILXL 공식 문법으로 `artist:~~` 를 사용해야 작가 태그의 오염이 적어진다.
> `yd_(orange_maru)` 를 `artist:` 없이 쓰면 **배경에 갑자기 오렌지가 하나 나오고**,
> `artist:lunch_(shin_new)` 를 `artist:` 없이 쓰면 갑자기 **식당에서 점심식사 하는 찐빠**가 터진다.

**`rating` 태그가 없으면 작가가 무효화된다.**

> `general / sensitive / questionable / explicit` **중 하나라도 안 들어가 있으면
> 작가 이름을 넣어도 밍숭맹숭하게 나오는 경우가 있음**

**작가·퀄리티 태그를 앞뒤 양쪽에 넣는다.** 프롬프트가 77토큰을 넘으면 positional encoding 이 꼬이기 때문이다.

가중치 상한이 ANIMA 보다 훨씬 낮다:
> IL 이든 아니마든 **1.5 넘기는 일은 사실상 없음.** 작가 조합은 `0.3~0.5` 구간

### 버전 차이

| | |
|---|---|
| **v14** | 사실상 표준. 로라 배포글 30여 편이 전부 v140 고정 |
| v15 | NSFW 특화. 대신 고속화 특성을 잃어 steps 28 필요 |
| v16 | **손 찐빠 회귀.** 글 제목이 아예 「손가락 찐빠 타율 높이기」 |
| **v17** | 최신. 손발 개선. 대신 **채도가 높고 3D 느낌이 강함** |

### 공통 약점

> **vae 해상도가 구려서 손가락 찐빠가 심하고** … hires fix 와 디테일러가 필수.
> 그리고 **자연어를 안 먹어서** 단독 일러가 아닌 상호작용·다인 출현·자세 잡기까지
> 아니마나 krea 에 비빌 수가 없음

> 아직도 WAI 쓰는 **석기시대 사람**이래

---

## Z-Image — 있지만 우리 용도가 아니다

| | |
|---|---|
| **정체** | 알리바바 Tongyi-MAI. **S3-DiT 6B** |
| **크기** | bf16 **12.31 GB** + 텍스트 인코더 `qwen_3_4b` **8.04 GB** = 20GB 급 |
| **채널 티어** | **2티어** (ANIMA·NAI 보다 위) |

> 적절한 크기에 적절한 성능으로 **일반 생성 로컬 모델 중에서 가장 인기 있는 모델**임.
> 다만 여기는 **애니메이션 AI 그림 위주라서 잘 다루지는 않고** 다른 곳에서 인기가 많음.

**태그가 아니라 자연어 캡션**을 쓴다. 애니메 특화가 아니므로 우리 용도에서는 우선순위가 낮다.

---

## NAI V5 — 비교 기준 (클라우드 유료)

2026-08-20 출시. 채널이 하루 만에 뒤집혔다.

| | V4.5 | **V5** |
|---|---|---|
| 모델 크기 | — | **2배 이상**. B200 **268,000 GPU-hour** |
| VAE | 16채널 | **커스텀 32채널** + 알파 채널 |
| 토크나이저 | Google T5 | **Qwen 계열** |
| 토큰 한도 | 512 | **1471** |
| 캐릭터 슬롯 | 6 | **32** (테스트에서 22명 동시 성공) |
| 기본 Guidance | 5 | **7** |

**기본값**: 832×1216 / Steps 23 / Guidance 7 / Euler Ancestral / Karras 고정

**신규 태그**: `depthness` `attractive male` `low~ultra complexity`(권장 high) `transparent background` `visual novel art/bg/cg`

평가는 갈린다:
> 호 — **배경하고 신체는 이제 그냥 완벽해졌는데** 정작 캐릭터가 별로
> 혹 — **그림체 개같이 사망** / 작가 쪽 데이터를 점점 안 쓰려는 것 같음

**사용량 제한이 새로 생겼다** — 기본 1,700장, 하루 190장 리필, 월 최대 7,400장.

---

# 영상 모델

## MiniMax H3 — 지금 최강

| | |
|---|---|
| **정체** | MiniMax(중). **omni-modal packed-DiT**, 블록 50개 |
| **특징** | **비디오 + 스테레오 오디오를 한 번의 forward pass 로 동시 생성** |
| **공개** | 2026-08-03 |
| **총 크기** | **약 39.6GB** (모델 19.5 + 인코더 14.6 + VAE 5.5) |

> **미맥 나오고는 로컬 동영상 쪽은 걍 미맥이 넘사임.**

> 미니맥스가 오픈웨이트 비디오 모델의 **저점을 너무 상향평준화** 시켜놔서 어쩔 수 없는 듯

### 부속 — 정확한 조합

```
models/diffusion_models/  minimax_h3_fl2va_pruned_int8_convrot.safetensors     ← t2va·fl2va
models/text_encoders/     qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors         ← CLIPLoader type "minimax"
models/vae/               minimax_h3_video_vae_fp16.safetensors                ← VAEDecode
                          minimax_h3_audio_vae_fp32.safetensors                ← VAEDecodeAudio
models/vae_approx/        taeh3.safetensors                                    ← 미리보기. 없으면 워크플로우가 막힌다
```

**VAE 2개가 둘 다 필수다.** 하나의 packed latent 에서 각자 자기 절반을 꺼내간다.

!!! tip "ref2va 모델은 안 받아도 된다"
    레퍼런스 전용 가중치가 따로 있지만, 채널 결론은 반대다.

    > 참고로, **래퍼런스도 fl2va 모델로 돌리는 게 더 품질이 나은 듯.**
    > → 댓글: **"챈 와서 건진 최고의 정보 = r2v 도 fl2v 로 돌려라"**

    공식도 인정했다 — *"Ref2Va 모델에서 영상 퀄리티가 FL2VA 보다 낮은 문제를 인지하고 있다."*

### 권장 설정 (ComfyUI 네이티브 기본값)

```
sampler    res_multistep
scheduler  simple            (ref2va 는 beta 또는 normal 이 낫다)
steps      20                denoise 1.0
CFG        없음               BasicGuider = CFG-free
shift      video 12.0 / audio 3.0
해상도      짧은 변 768 기준, 상한 768×1344, 반드시 32의 배수
프레임      24fps.  frames = 17k + 5   →  5초 = 124 · 10초 = 243 · 15초 = 362
```

!!! danger "해상도가 32의 배수가 아니면 shape 에러가 난다"
    `RuntimeError: shape … is invalid for input of size …` 가 뜨면 검열이 아니라 **해상도 문제**다.

### 속도 (동일 조건 실측)

544×800 · 5초 · 20스텝 · 가속 없음:

| GPU | 총 시간 |
|---|---|
| RTX 5090 | **1분 04초** |
| RTX 3090 | 2분 41초 |
| RTX 3060 12GB | **8분 59초** |
| Intel B580 | **구동 실패** |

해상도를 올리면 급격히 느려진다(5090 기준, 15초):

| 해상도 | 총 시간 |
|---|---|
| 608×352 | 74초 |
| 864×480 | 152초 |
| **1344×768** | **576초** |

### 가속 조합 (5090, 1MP·5초)

| 조합 | 시간 |
|---|---|
| 기본 | 309초 |
| **Cache + Mem Eff Sage + Patch Sage KJ** | **95초 (3배)** |
| Cache + Spectrum | **Error** |

!!! warning "터보 로라와 캐시는 같이 못 쓴다"
    > H3-Cache 는 변화량이 적은 부분에서 이전 계산을 재활용하는 노드인데,
    > Turbo LoRA 는 **재활용할 스텝 자체를 처음부터 안 만들게 설계**된 거라 겹쳐서 못 씀.

### 프롬프트 문법 — 여기가 승부처다

**6개 섹션 양식**을 요구한다.

```
subject_definitions:   각 참조에서 뭘 따올지 정하고 <Subject N> 라벨 부여
summary:               [reference generation + audio reuse] 처럼 작업 종류 선언
retention_analysis:    라벨별 참조 강도
detailed_description:  [Shot N] At MM:SS.mmm, ...
overall_soundscape:    환경음·효과음
non_diegetic_music:    배경음악
```

> 미니맥스도 프롬프트에 굉장히 민감하다. **입학원서 서류양식대로 작성해주세요**라고 해놨는데
> "좋은 곳 들어갈 거임" 식의 자연어는 **미니맥스가 극혐하는 것 같다**

대사: `The girl (S1) says: <d>[Korean] 안녕하세요.</d>`
**한국어 프롬프트도 통한다.**

### 못하는 것

- **저해상도가 약하다** — 공식: *"현재 모델은 고해상도 생성을 중점에 뒀기 때문에 저해상도 성능이 낮다"*
- **롱테이크** — *"5~6초 넘어가면서부터 무너짐이 가속됨"*
- **얼굴 일관성** — *"의외로 얼굴 변형이나 일관성 틀어짐이 꽤 심해요. 이건 차라리 wan 이 우위"*

---

## WAN 2.2 · LTX 2.5 — 밀려난 것들

**WAN 2.2** — high noise + low noise 2단 구조. 16fps, 81프레임 = 5초.
채널 국룰 조합은 **High = SmoothMix, Low = DaSiWa**.

> 스+스 = 모션이 동적이나 그림체가 뭉개져요 / 다+다 = 그림체 유지가 잘되나 모션이 뻣뻣해요
> / **섞어쓰면 황밸**

지금 위치: *"wan 마지막 야짤"*, *"Wan 졸업하는 김에"*, *"wan ltx 공동묘지에 헌화"*

**LTX 2.5** — 2026-08-11 출시. 3090에서 0.4MP·5초 **43초**, H3 대비 **3.72배 빠름**.

한 줄 평이 원문에 그대로 있다:

> **결론: 발전 = 있음 / 포지션 = 범부 / 속도 = 독보적 / 용도 = 장난감**

> ltx 저건 **2d 에선 그냥 쓸 게 못 됨**

---

## 세력도 — 시계열

```
~2025-05   Hunyuan · FramePack · LTX-Video  →  Wan 2.1 이 평정
2025-08~   Wan 2.2 + SmoothMix/DaSiWa 가 압도적 국룰
2026-03~   LTX 2.3 이 "오디오 동시 생성"으로 2군 형성. 2D 약점으로 Wan 을 못 밀어냄
2026-08    MiniMax H3 등장 → Wan·LTX 모두 급격히 밀려남
```

---

## 관련 문서

- [처음부터](start-here.md) — 실제로 뽑는 순서
- [작가 태그 사전](artist-tags.md)
- [작업 프로세스](workflow-process.md)
