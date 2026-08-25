# 워크플로우 13개

ComfyUI 워크플로우다. 받아서 캔버스에 끌어다 놓으면 열린다.

**계열이 섞이지 않는다.** ANIMA 는 Cosmos-Predict2 기반 DiT + Qwen3 인코더,
SDXL 은 UNet + CLIP 이라 **모델도 로라도 컨트롤넷도 호환되지 않는다.**
파일마다 어느 계열인지 표시해 뒀다.

---

## 00_ACTIVE — 그림 뽑기

| 파일 | 계열 | 노드 | 무엇 |
|---|---|---|---|
| `ANIMA simple t2i.json` | ANIMA | 4 | **처음 배울 때.** 모델 3조각이 한 노드에 다 보인다 |
| `AiO_v60_local.json` | ANIMA | 104 | **주력.** 그룹 12개, 초안→마감 한 판에 |
| `AiO_run.json` | ANIMA | 103 | AiO 변형본 |
| `WAI_ILXL_T2I_local.json` | SDXL | 41 | WAI Illustrious 계열 |
| `90 Grid4 + Variation4.json` | ANIMA | 17 | 미드저니식 — 4장 그리드 → 고른 것 변형 4장 |

## 01_ORIGINAL — 채널 원본 보관

| 파일 | 계열 | 무엇 |
|---|---|---|
| `T2I_179637421_ORIGINAL.json` | SDXL | 채널 배포본 원형 |
| `from_p1_02.json` | SDXL | 〃 |

## 02_VIDEO — 영상

| 파일 | 무엇 | 실측 시간 |
|---|---|---|
| `60 MinimaxH3 Reference I2V local 0.4MP.json` | 레퍼런스 I2V · 544×800 | **약 3분** |
| `61 … 0.9MP.json` | 800×1184 | 8분 28초 |
| `62 … 1.6MP.json` | 1056×1600 | **27분 49초** |
| `70 LTX25 I2V.json` | LTX-2.5 (ComfyUI 공식 템플릿 기반) | — |

세 H3 워크플로우는 `megapixels` 값 하나만 다르다.
**화소가 4배일 때 시간은 8.2배**라, 0.4MP 로 여럿 뽑아 고른 뒤 올리는 쪽이 싸다.

## 03_INPAINT — 부분 수정

| 파일 | 계열 | 무엇 |
|---|---|---|
| `80 ANIMA LLLite Inpaint.json` | ANIMA | `Painter` 노드에서 붓으로 칠한다. LLLite 로 제어 |
| `81 WAI SAM3 Inpaint.json` | SDXL | **자연어로 부위 지정** — `face` `hand` `hair` 라고 쓰면 마스크가 나온다 |

---

## 필요한 모델

### ANIMA — 세 조각을 각각 다른 폴더에

```
anima-aesthetic-v1.1.safetensors  →  models/diffusion_models   ← checkpoints 아님!
qwen_3_06b_base.safetensors       →  models/text_encoders      CLIPLoader type "stable_diffusion"
qwen_image_vae.safetensors        →  models/vae
```

> **가장 흔한 사고** — "체크포인트 파일이라길래 `checkpoints` 에 넣었는데 목록에 안 뜬다".
> ANIMA 는 한 덩어리가 아니다.

### SDXL

```
waiIllustriousSDXL_v170.safetensors  →  models/checkpoints
```

로라 배포글 상당수가 **v14 고정**이라, 남의 로라를 쓸 때는 v14 가 안전하다.

### 영상 (MiniMax H3) — 다섯 개 다 필요하다

```
models/diffusion_models/  minimax_h3_fl2va_pruned_int8_convrot.safetensors   19.5 GB
models/text_encoders/     qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors       14.6 GB
models/vae/               minimax_h3_video_vae_fp16.safetensors               4.9 GB
models/vae/               minimax_h3_audio_vae_fp32.safetensors               0.6 GB
models/vae_approx/        taeh3.safetensors                                   22 MB
```

**VAE 두 개가 둘 다 필요하다** — 하나의 latent 에서 영상과 소리를 각각 꺼내간다.
`taeh3` 는 미리보기용인데 **없으면 워크플로우가 아예 안 돈다.**

### 커스텀 노드

`ComfyUI-Manager` · `ComfyUI-EasyUseAnima` · `Impact-Pack`+`Subpack` · `easy-sam3` ·
`rgthree-comfy` · `KJNodes` · `UltimateSDUpscale` · `Anima-LLLite` ·
`Spectrum-KSampler` · `ComfyUI-DCW` · `Autocomplete-Plus`

---

## 밟고 나서 적어 두는 것들

**영상 워크플로우가 예외도 없이 죽으면** 다른 프로세스가 VRAM 을 쥔 것이다.
`ollama` 가 흔한 범인이고, **`/api/ps` 는 이 상황에서 "모델 없음"이라고 거짓 보고한다.**
프로세스를 직접 확인해야 한다.

**ANIMA 에서 `batch_size` 를 2 이상으로 올리면** Mod Guidance 가 조용히 꺼진다.
에러가 안 나서 더 위험하다. 한 장씩 여러 번 돌리는 편이 낫다.

**`shift` 가 0 이면 검은 화면**이 나온다. ANIMA 는 3.0 이 기본이다.

**인페인팅에서 `VAEEncodeForInpaint` 는 마스크 영역을 지운다.** 빈 구멍을 채우는 노드라,
얼굴을 다듬으려고 쓰면 원본이 사라진 자리에 엉뚱한 것이 그려진다.
원본을 남기려면 `VAEEncode` → `SetLatentNoiseMask` 를 쓴다.
`81 WAI SAM3 Inpaint` 는 그렇게 짜여 있다.

**`8.1 Metadata 저장` 을 끄지 마라.** PNG 에 워크플로우가 박혀야
나중에 캔버스에 끌어다 놓아 시드·설정을 복원할 수 있다. 초안을 많이 뽑아
고르는 방식이 성립하려면 이게 켜져 있어야 한다.

---

## 태그 문법이 계열마다 다르다

| | ANIMA | SDXL / Illustrious |
|---|---|---|
| 작가 | `@이름` | `artist:이름` |
| 가중치 | `:2` 부터. 4 이상은 검은 화면 | 1.5 를 넘기는 일이 거의 없다 |
| 등급 | `safe` / `sensitive` / `nsfw` / `explicit` | `general` / `sensitive` / **`questionable`** / `explicit` |
| 연도 | `year2024` 사용 | 쓰지 않는다 |

**Illustrious 는 등급 태그가 하나도 없으면 작가 태그가 통째로 무효화된다.**
