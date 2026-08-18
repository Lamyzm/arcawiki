# ANIMA

> **원문 172건 → 이 문서 하나** · 주장 315개 · 정리 2026-08-14

NVIDIA Cosmos-Predict2 2B 기반 이미지 모델. 자연어 이해가 좋은 대신 화풍이 약해서, **Illustrious 와 2단으로 엮어 쓰는 것**이 채널의 표준 운용이다.

## 시작하기 — 포터블로 30분 안에
<small>2026-05 기준 · 근거 3건</small>

ANIMA 는 **2026-05-15 정식 출시**됐고, 그 시점 채널 FAQ 의 답은 *"체감 대세는 웹이면 NAI 4.5 Full, 로컬이면 Anima"* 였다.

**최소 경로는 생각보다 짧다.** ComfyUI 포터블을 쓰면 파이썬도 git 도 필요 없다.

| 단계 | 하는 일 |
|---|---|
| 1 | 최신 GPU 드라이버로 업데이트 |
| 2 | `ComfyUI_windows_portable_nvidia.7z` 를 **한글이 없는 짧은 경로**(가능하면 SSD)에 압축 해제 |
| 3 | 모델 3개를 각 폴더에 넣기 (아래) |
| 4 | RTX 2000 대는 `run_nvidia_gpu.bat`, RTX 3000 대 이상은 `run_nvidia_gpu_fast_fp16_accumulation.bat` |
| 5 | 좌측 **템플릿** 버튼 → 검색창에 `anima` → *Anima 애니메이션 텍스트-이미지 생성* → 파란 실행 버튼 |

모델은 `https://huggingface.co/circlestone-labs/Anima` 의 `split_files` 아래에서 받는다.

```text
diffusion_models/anima-base-v1.0.safetensors   →  ComfyUI/models/diffusion_models
text_encoders/qwen_3_06b_base.safetensors      →  ComfyUI/models/text_encoders
vae/qwen_image_vae.safetensors                 →  ComfyUI/models/vae
```

| 항목 | 값 |
|---|---|
| 최소 사양 | **VRAM 6GB / RTX 2060 이상** |
| AMD | RX 7000(RDNA3) 이상 필요, 동급 엔비디아 대비 **2~3배 느림**. 파이토치 프리뷰가 아닌 **일반 최신 드라이버** 권장 |
| 접속 | `http://127.0.0.1:8188` (본체가 도는 컴퓨터에서만) |
| 권장 해상도 | ⚠️ **`768` 근처부터 시작하라** — 아래 "해상도 — 1024가 아니라 768로 시작하라" 참조. 공식 버킷은 세로 832x1216 / 896x1152 / 768x1344, 가로 1152x896 / 1216x832 / 1344x768, 정사각 1024x1024 |
| 업데이트 | `update` 폴더의 `update_comfyui.bat` |
| 결과 | `ComfyUI/output` |

포터블은 폴더 위치만 다르면 여러 개를 설치해도 서로 영향을 주지 않는다.

**첫 트러블슈팅** *(댓글)*

- 템플릿에 anima 가 안 뜨면 → 최신 포터블인지 확인, 그래도 안 되면 `.../Anima/blob/main/example.png` 를 수동 로드
- "누락된 모델" 경고 → **프리뷰 1 버전 워크플로우**라서 나는 것이니 *확산 모델 로드* 에서 최신 버전을 고르면 된다
- `offload-arch failed with return code 1` → ComfyUI 측 패키징 문제. `Comfy-Org/ComfyUI` 이슈 #11546 참고해 심볼릭 링크 생성

설치 전반은 [설치와 환경 구성](install.md), 화면 조작은 [ComfyUI 쓰는 법](comfyui.md) 을 함께 보라.

<small>근거 — [응애도 할 수 있는 ComfyUI Anima 로컬 아니메 이… 26.02](https://arca.live/b/aiart/163553760) · [초보자용 아니마+IL 워크플로우 VER.2 26.02](https://arca.live/b/aiart/163201876) · [최근 AI 그림 자주 묻는 질문 (26년 5월 기준) 26.05](https://arca.live/b/aiart/170655900)</small>

## ⭐ 판 계보 — 어느 판 이야기인지부터 확인하라
<small>2026-07 기준 · 근거 7건</small>

ANIMA 자료를 읽을 때 **가장 먼저 확인할 것은 날짜가 아니라 판(버전)** 이다.
**판이 다르면 같은 값이 반대 결과를 낸다** — 같은 로라가 한 판에서는 멀쩡하고 다음 판에서 노이즈를 뿜으며,
작가 태그와 로라 중 무엇이 나은가도 판을 건너면서 뒤집혔다.

### 계보

```text
PREVIEW1 · PREVIEW2 · PREVIEW3  →  BASE v1.0(정출)  →  aesthetic v1.0 / v1.0b / v1.1  ·  Turbo
```

| 판 | 시점 | 성격 |
|---|---|---|
| `PREVIEW1` ~ `PREVIEW3` | ~2026-04 | 공개 시험판. **PREVIEW3** 은 PREVIEW2 대비 1024 해상도 학습량을 늘리고 덜 알려진 작가 지식을 강화했다 |
| **`anima-base-v1.0`** | **2026-05-14** | 정식 출시. 공식 설명은 *"The pretrained, unrefined base model. Maximum flexibility, diversity, and style adherence"* — **정제되지 않은 사전학습 원본**이라 유연성·다양성·화풍 준수가 최대인 대신 **바로 예쁜 그림이 나오는 판은 아니다.** 가장 눈에 띄는 개선은 고해상도 안정성 |
| `anima-aesthetic-v1.0` · **`Anima Turbo`** | 2026-07-08 | BASE 위에 미적 튜닝을 얹은 판. Turbo 는 증류판 |
| `anima-aesthetic-v1.0b` | 2026-07-08 | ⚠️ **베타가 아니다.** 모델 카드 원문은 *"추가적인 스타일 조정이나 안정화 LoRA 를 병합하지 않고 순수하게 미적 요소(Aesthetics)만 전체 파인튜닝한 대안 버전"* 이고, **개발자 본인은 v1.0 이 더 낫다고 적었다.** b 가 더 늦게 올라와 혼란이 있었으나 순서와 무관한 '대안 판' 이라는 뜻이다 |
| `anima-aesthetic-v1.1` | 2026-07-11~13 | 손가락 찐빠 급감, 컬러톤 전환, **프롬프트 해석 성향이 뒤집힌 판** (아래) |
| **`Anima-2.9B`** | **2026-08-12** | ⚠️ **공식 판이 아니다.** 제3자가 튜닝 + 레이어 확장한 판이고 **블록이 28 → 40 으로 늘어** 기존 로라를 그대로 물릴 수 없다. 컷오프 2026-07. 바로 다음 절 참조 |

배포처는 `https://huggingface.co/circlestone-labs/Anima` 의 `split_files/diffusion_models` 와
Civitai `models/2458426` 다.

### 실검증 메모 — 처음엔 터보로 방향을 잡고, 저장은 베이스로

2026-08-18 로컬 실검증에서는 같은 프롬프트·같은 해상도(`832x1216`)에서
**BASE v1.0** 이 약 **23.7초**, **공식 `anima-turbo-lora-v0.2`** 가 약 **4.6초**였다
(RTX 5070 Ti, ComfyUI).

| 모드 | 실측 | 세팅 | 느낌 |
|---|---|---|---|
| **BASE v1.0** | **약 23.7초** | `steps 30` · `cfg 4` · `er_sde`/`euler` | 디테일과 표정 결이 더 풍부하다 |
| **터보 로라** | **약 4.6초** | `steps 8` · `cfg 1` · `euler` | 매우 빠르지만 더 단순하고 네거티브가 약하다 |

그래서 입문자 기준 실제 운용은 이렇게 정리된다.

- **프롬프트 탐색**: 터보 로라
- **마음에 든 프롬프트로 최종 저장**: BASE v1.0

공식 모델 카드도 **"Anima-Turbo 로 시작하는 것을 추천"** 한다.
다만 같은 카드가 바로 이어서 **"Turbo 는 더 안정적이지만 다양성과 디테일은 줄어든다"** 고 못박는다.
즉, 빠른 시안 확인에는 좋지만 **최종 한 장의 저점과 결은 베이스 쪽이 낫다**는 것이 실검증과도 맞아떨어졌다.

### PREVIEW3 은 이제 쓸 것이 못 된다

동일 프롬프트·동일 시드로 PREVIEW3 / BASE v1.0 / aesthetic v1.1 을 나란히 돌린 비교의 첫 결론이
**"PREVIEW3 는 예전에는 좋아 보였지만 BASE 와 나란히 놓으면 하자가 심해 이제 쓸 것이 못 된다"** 였다
*(2026-07-13, 30스텝 / CFG 4.0 / Euler A + beta57)*.

### v1.1 에서 실제로 달라진 것

| | BASE v1.0 | aesthetic v1.1 |
|---|---|---|
| 손가락 | — | **찐빠율이 크게 줄었다** |
| 컬러톤 | 웜브라운 | **쿨그레이** |
| 가슴 기본값 | — | **지정하지 않으면 대체로 `large`, 같은 `large` 라도 더 크다** |
| 프롬프트 해석 | 지정한 것만 그린다 → 배경·조명·이펙트를 하나하나 써 줘야 완성도가 오른다 | **대충 던져도 배경·조명·이펙트를 알아서 채운다** |

> ⚠️ **프롬프트 해석 성향이 뒤집힌 것이 v1.1 의 가장 큰 변화다.** PREVIEW~BASE 기준으로 쓰인
> "Anima 는 배경을 일일이 지정해야 한다" 는 조언은 **그 판에서는 맞고 v1.1 에서는 과잉**이다.
> 옛 조언을 지우지 말고 어느 판 이야기인지를 보고 판단할 것.

세부 관찰 — v1.1 은 `jacket on left shoulder` 같은 지시를 더 정확히 이행한 사례가 있었던 반면,
복장 디테일이 원작에 가깝게 나오는 것은 PREVIEW3/BASE 쪽이었고 머리 앞뒤로 카타나 위치 축이 안 맞는 현상은 1.1 에서도 그대로다.

바로 다음 절에 **판이 바뀌면서 뒤집힌 것들**을 표로 모았다.

<small>근거 — [마참내! anima-base-v1.0 떳다 26.05](https://arca.live/b/aiart/170688430) · [anima preview 3 떳다 26.04](https://arca.live/b/aiart/167051252) · [anima2.9b 출시 26.08](https://arca.live/b/aiart/179710466) · [아니마 1.1 대충 찍먹 26.07](https://arca.live/b/aiart/176800461)</small>

??? note "근거 7건 전부 보기"
    [마참내! anima-base-v1.0 떳다 26.05](https://arca.live/b/aiart/170688430) · [anima preview 3 떳다 26.04](https://arca.live/b/aiart/167051252) · [anima2.9b 출시 26.08](https://arca.live/b/aiart/179710466) · [아니마 1.1 대충 찍먹 26.07](https://arca.live/b/aiart/176800461) · [Anima preview2 / preview3 / base … 26.05](https://arca.live/b/aiart/170773343) · [아니마 Aesthetic V1.0쓰는 삣삐들스탑 26.07](https://arca.live/b/aiart/176406993) · [anima-aesthetic-v1.0, turbo 모델 출시 26.07](https://arca.live/b/aiart/176286183)

## ANIMA 2.9B (2026-08-12) — 제3자 확장판, 40블록이라 로라를 재매핑해야 한다
<small>2026-08 기준 · 근거 3건</small>

**공식 판이 아니다.** 제3자(`Gazingstars123`)가 기존 ANIMA 를 튜닝하고 레이어를 확장해 만든 판이다.
`2.9B` 는 **파라미터 29억 개**라는 뜻이고 버전 번호 2.9 가 아니다 (기존 2.0B 대비 +0.9B).

| 항목 | 값 |
|---|---|
| 받는 곳 | `https://huggingface.co/Gazingstars123/Anima-2.9B` |
| **지식 컷오프** | **2026년 7월** — 모델 카드 원문은 *"Knowledge cutoff in July 2026, training data included both new and old samples prior to September 2025"*. **글쓴이가 본문에 처음 '9월' 로 적었다가 댓글 지적을 받고 7월로 정정했다** |
| 추가 데이터셋 | 약 **170만 장** |
| 학습 해상도 | **70% 가 1k** |
| 태깅 | danbooru 태그 + 자연어 |
| VRAM (생성 후) | 기존 ANIMA 약 **8GB** → 2.9B 약 **9.5GB** *(Radeon 사용자 측정이라 정확하지 않을 수 있다)* |
| 모델 파일 | 기존 대비 약 **+1.6GB** |
| WebUI · reForge Neo | 이 시점에 지원 여부 미정 |

### 구조가 바뀌었다 — 기존 28블록 **사이에** 12블록을 끼웠다

지우거나 뒤에 덧붙인 것이 아니다. 기존 Transformer 28개 블록 **사이사이에** 신규 12개를 삽입해 **총 40블록**이 됐다.
그래서 기존 28블록은 그대로 보존돼 있지만 **인덱스가 밀린다.**

```text
기존 0~27  →  2.9B 에서의 위치
0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 20,
22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 39

새로 삽입된 블록 (로라 delta 를 넣지 않는다)
2, 5, 8, 11, 14, 17, 21, 24, 27, 30, 33, 36

예)  기존 로라의 transformer_blocks.2.attn.to_q  →  2.9B 의 blocks.3
```

> ⚠️ **인덱스를 그대로 쓰거나 뒤에 12개를 padding 하는 변환은 틀렸다.**
> 삽입 지점 이후의 로라가 통째로 엉뚱한 블록에 걸린다.

변환 방식은 로라 행렬(`W' = W + α·B·A` 의 `A`, `B`)을 건드리지 않고 **키의 블록 인덱스만 바꾸는 것**이다.
LoRA · LoHa · LoKr 처럼 내부 표현이 달라도 같은 방식으로 처리된다.
삽입된 12블록에는 로라 delta 를 얹지 않는데, 이는 비활성화가 아니라 **2.9B 가 학습한 기본 가중치로 정상 동작하되
로라 변화량만 안 얹는다**는 뜻이다.

> ⚠️ **재매핑해도 원본과 동일한 효과는 보장되지 않는다.** 계승 블록의 `W` 와 `ΔW` 가 같아도
> **앞쪽 삽입 블록이 hidden state 를 먼저 바꾸므로 `h ≠ h'`** 가 된다.
> 최대 품질과 재현성이 필요하면 **2.9B 에서 직접 학습한 로라**를 쓰라고 권한다.

### 무엇으로 돌리나

| 방법 | 비고 |
|---|---|
| **EasyUseAnima 1.1.1 이상** *(권장)* | 별도 커스텀노드 없이 `Easy Use Anima Input` / `Anima AiO Generator` 에서 40블록 모델을 바로 로드한다. 기존 28블록 로딩 방식도 그대로 유지된다. 일부 블록만 든 애매한 로라는 `Anima 2.9B LoRA Stack Loader` 노드를 쓴다 |
| 전용 커스텀노드 | `https://github.com/gazingstars123/ComfyUI-Anima-2.9B` |
| 급조 로라 로더 | `https://github.com/qweqweewqe7-create/ComfyUI-Anima-2.9B-LoRA-Loader` — 출시 당일 만들어진 임시방편. 제작자가 *"99% 바이브 코딩"* 이라 모든 상황을 보장하지 못한다고 밝혔다. **기본 로라 로더로는 2.9B 에서 로라가 아예 작동하지 않는다** |

실사용 보고는 *'적용 잘 된다'*, *'일부 고속(터보) 로라도 잘 적용된다'*(공식 터보 0.2 확인) 수준이고,
**'로라를 쓰는 조건에서도 2.9B 가 더 나은가' 에는 확답이 나오지 않았다.**

→ 로라 학습 쪽은 [로라 쓰는 법](lora-usage.md), 커스텀노드팩은 아래 'EasyUseAnima' 절.

<small>근거 — [anima2.9b 출시 26.08](https://arca.live/b/aiart/179710466) · [초간단 급조 2.9b 호환 로라 로더 만들어옴 26.08](https://arca.live/b/aiart/179726548) · [EasyUseAnima 1.1.1: ANIMA 2.9B 지원… 26.08](https://arca.live/b/aiart/179735645)</small>

## 판이 바뀌면 뒤집히는 것 — 로라·작가 태그 대조표
<small>2026-07 기준 · 근거 12건 · 자료 엇갈림</small>

같은 값이 판에 따라 반대 결과를 내는 지점들이다. **어느 쪽도 지우지 않고 판별로 적는다.**

### 로라를 다시 구워야 하나

| 학습한 판 | 돌리는 판 | 결과 |
|---|---|---|
| `PREVIEW1` 등 PREVIEW3 이전 | BASE v1.0 | ⚠️ **호환은 되지만 결과가 지저분해지고 자글자글해진다 — 재학습 대상** (2건) |
| `PREVIEW2` | PREVIEW3 | **그대로 잘 먹힌다** (여러 명 확인) |
| `PREVIEW3` | BASE v1.0 | **그대로 굴릴 만하다.** 같은 데이터셋으로 2x2 교차 비교한 결과 BASE 학습 쪽이 질감·옷 주름이 더 디테일하지만 *"무조건 재학습해야 한다 수준은 아니다"* |
| `BASE v1.0` | aesthetic v1.1 | **그대로 잘 인식된다** |

> **새로 구울 거면 BASE 로.** aesthetic v1.1 에는 이미 LoRA 가 병합돼 있으므로
> 학습 베이스는 v1.1 이 아니라 `anima-base-v1.0` 이 낫다는 것이 댓글의 조언이다.
> (Aesthetic 이 무엇으로 만들어졌는지는 다음 절)
>
> 여기서 말하는 '기존 로라' 는 전부 **Anima 전용 로라**다. SDXL·Illustrious 계열 로라는 어느 판에서도 안 된다.

### 작가 태그와 로라의 우열이 뒤집혔다

| 판 | 어느 쪽이 나은가 |
|---|---|
| BASE v1.0 | **로라** — 작가 학습분이 과적합 느낌이 강했다 |
| aesthetic | **작가 태그** — *"Aesthetic 에 와서 그 반대가 된 느낌"* 이라는 체감 |

*(한 글의 댓글 체감이다. 다만 판을 명시한 관찰이라 남긴다.)*

그리고 **판이 올라갈 때마다 작가 조합이 틀어진다.** PREVIEW2 에서 맞춰 깎아 둔 작가 태그 조합이
PREVIEW3 에서 다른 결과를 냈고, 그래서 *"정식판 나올 때까지 작가 조합을 정밀하게 깎는 건 낭비"* 라는 말이 나왔다.
PREVIEW3 은 작가 그림체 반영도가 올라간 대가로 **워터마크가 결과물에 등장하는 비율도 같이 올라갔다.**

### PREVIEW 용 보조 로라가 정출에서 깨진다

| 것 | 문제 | 대체 |
|---|---|---|
| `age control 年齢操作 - anima_v1.0` | PREVIEW 시절작이라 **정식판(BASE)에서 노이즈가 낀다.** 제작자가 업데이트를 방치했다 | **`Age Slider LoRA \| ANIMA - v0.9`** — 트리거 워드 없이 강도 `-3.00 ~ 3.00` 으로 조절. 다만 양수(고령) 방향은 얼굴 외 체형이 잘 안 따라온다 |
| 챈산 `anima-lllite-inpainting-0XX` | LLLite 에 인페인팅 기능이 없던 시절의 억지 구현 | kohya `anima-lllite-inpainting-v1` → `v2` (아래 "LLLite 인페인팅" 절) |
| 공식 `anima-highresaesthetic-boost` | PREVIEW 시절작이라 BASE 에서 노이즈가 낀다는 보고와, 파인튜닝판에서 0.7 로 잘 쓴다는 보고가 갈린다 | 아래 "⚠ 공식 퀄리티 로라" 절에 양쪽을 적어 두었다 |

### 판이 명시된 자료 — 받기 전에 확인할 것

| 자료 | 대상 판 |
|---|---|
| `Anima Detail Tweaker - preview3-test` | **PREVIEW3** (이름 자체에 들어 있다). 트리거 없이 강도 `-1.0 ~ 1.0` 으로 Aesthetics 조정, 음수는 덜어내는 방향 |
| 블아 작가 로라 `@mx2jstyle` · `@7peachstyle` | **PREVIEW3** |
| '브더2 느낌' 그림체 로라 (2026-03) | **PREVIEW2**, 학습 해상도 1536 · **링크 만료** |
| T-LoRA 실험 배포본 `damada21/anima-tlora` | **PREVIEW2** |
| `AnimaYume V02` 전용 로라 (트리거 `ricostyle`) | 순정 Anima 가 아니라 **AnimaYume 파인튜닝 구판** · **링크 만료** |

→ 받는 곳과 로라별 함정은 [자원](resources.md), 학습 쪽은 [로라 쓰는 법](lora-usage.md).

<small>근거 — [anima preview 3 떳다 26.04](https://arca.live/b/aiart/167051252) · [아니마 1.1 대충 찍먹 26.07](https://arca.live/b/aiart/176800461) · [아니마 디테일 트위커 로라 나왔음. 26.05](https://arca.live/b/aiart/170584706) · [Anima preview2 / preview3 / base … 26.05](https://arca.live/b/aiart/170773343)</small>

??? note "근거 12건 전부 보기"
    [anima preview 3 떳다 26.04](https://arca.live/b/aiart/167051252) · [아니마 1.1 대충 찍먹 26.07](https://arca.live/b/aiart/176800461) · [아니마 디테일 트위커 로라 나왔음. 26.05](https://arca.live/b/aiart/170584706) · [Anima preview2 / preview3 / base … 26.05](https://arca.live/b/aiart/170773343) · [kohya가 만든 Anima용 인페인팅 LLLite 컨트롤넷 26.05](https://arca.live/b/aiart/170374198) · [블아 작가로라 2개 26.04](https://arca.live/b/aiart/167677263) · [브더2 느낌의 amima 로라 26.03](https://arca.live/b/aiart/165231841) · [아니마 프리뷰v3 / 베이스v1 동일 데이터셋으로 학습한 로… 26.05](https://arca.live/b/aiart/170810380) · [허접한 AnimaYumeV02 용 LoRA 공유함 26.03](https://arca.live/b/aiart/164800666) · [(anima, 페, 할) 연령 조절 슬라이더 로라 26.06](https://arca.live/b/aiart/174677230) · [채신기법으로 anima lora 학습시켜봄 (2) 26.03](https://arca.live/b/aiart/165954535) · [아니마 연령 조절 로라 26.05](https://arca.live/b/aiart/170858259)

## Aesthetic 은 무엇으로 만들어졌나 — LoRA 3종 병합
<small>2026-07 기준 · 근거 2건 · 자료 엇갈림</small>

출시 이틀 뒤 개발자 설명으로 밝혀진 것이다. **aesthetic 은 순수 파인튜닝이 아니라 LoRA 3종을 병합한 판이다.**
(출시 글의 글쓴이는 *"RL 된 모델이라는 건가"* 라고 추측했는데, 실제로는 RL 이 아니다.)

| 섞인 것 | 가중치 | 무엇을 하나 |
|---|---|---|
| **DMD 계 distillation LoRA** | 낮게 | 실제 증류 효과는 거의 없고 **분포를 약간 수축시키면서 스타일에 편향을 주고 디테일을 더한다.** v1.1 에서 가장 많이 손본 부분이며 방향은 *선을 매끄럽게, 노이즈 감소* |
| **anime coloring LoRA** | **1 미만** | 단부루 `anime coloring` 태그가 붙은 고평점 이미지 수천 장을 학습. 그냥 두면 나는 **2.5D 느낌을 좀 더 평평하게(애니 채색답게)** 만든다 |
| **heavy sweating LoRA** | ⚠️ **음수** | DMD 계열의 부작용인 **땀방울(sweatdrop) 과다를 제거**한다. 같은 시드에서 이 로라를 안 넣었을 때와 거의 픽셀 단위로 같은 이미지가 유지된다 |

### 여기서 나오는 실전 응용

> **Anima 결과물에 땀방울이 너무 많이 붙는다면, `heavy sweating` 계열을 음수 가중치로 거는 것이 공식이 쓰는 해법이다.**
> Turbo 모델에도 이 로라가 포함돼 turbo LoRA 의 과도한 땀방울 문제를 고쳤다.

이 LoRA 들 자체는 따로 공개되지 않았지만 모델에서 추출해 뽑아 쓸 수는 있다는 언급이 있다.

### Turbo 가 빠른 이유는 모델이 아니라 CFG 다

**`CFG 1` 로 돌리기 때문이다.** CFG 를 1 로 두면 네거티브 프롬프트 경로를 계산하지 않아 **연산이 절반**이 된다.
그래서 터보 계열은 CFG 1 이 정상값이고, 대신 **네거티브 프롬프트가 죽는다.**

### 그리고 이것이 '학습은 BASE 로' 의 근거다

aesthetic 판에는 이미 LoRA 가 병합돼 있다. 그 위에 또 학습을 얹으면 무엇이 무엇 때문인지 알 수 없어진다.
**새 로라를 구울 베이스는 `anima-base-v1.0` 이다.**

<small>근거 — [아니마 Aesthetic V1.0쓰는 삣삐들스탑 26.07](https://arca.live/b/aiart/176406993) · [anima-aesthetic-v1.0, turbo 모델 출시 26.07](https://arca.live/b/aiart/176286183)</small>

## 샘플러 — 이것만은 지킬 것
<small>2026-08 기준 · 근거 10건</small>

**일곱 개 글이 독립적으로 같은 말을 했다.** 이 프로젝트에서 가장 강한 합의다.

```
쓸 것    Euler  또는  ER SDE     +   simple  또는  SGM uniform
쓰지 말 것    Euler A  +  automatic/normal
```

Euler A + automatic 조합에서 **그림이 기괴해진다.** 다른 설정을 아무리 만져도 이걸 바꾸지 않으면
해결되지 않는다.

### 2026-08-18 로컬 실검증 — **입문 기본값은 `er_sde` 로 두는 편이 낫다**

공식 모델 카드는 `er_sde` 를 *"reasonable default"* 로 적고, `euler` 는
**Turbo / Aesthetic 처럼 기본적으로 더 안정한 판에서 좋다**고 적는다.
이걸 그대로 두지 않고 같은 로컬 환경에서 한 번 더 비교했다.

조건:

- `anima-base-v1.0`
- `832x1216`
- `steps 30`
- `cfg 4`
- `simple`
- 자연어 2문장 프롬프트, 같은 네거티브

실측:

| 샘플러 | 시간 | 관찰 |
|---|---:|---|
| `er_sde` | **23.7초** | 선이 더 또렷하고, 얼굴·옷 주름이 더 **중립적이고 안정적**이었다 |
| `euler` | **23.4초** | 시간 차이는 거의 없었지만, 더 **말랑하고 귀여운 쪽**으로 기울고 2.5D 느낌이 조금 더 섞였다 |

즉 둘 다 틀린 값은 아니다. 다만 **처음 기본값**을 하나만 고르라면:

- **기본값**: `er_sde`
- **조금 더 부드럽고 귀엽게**: `euler`
- **피해야 할 것**: `euler a + automatic/normal`

### CFG 는 판을 밝혀 적어야 한다

문서의 여러 ANIMA 자료가 **CFG 5** 를 기본으로 적지만, 실제 출품작 기록에는 다른 값도 남아 있다.

| 판 | 설정 | 출처 |
|---|---|---|
| **Anima-preview** | `er_sde` / `sgm_uniform` · **30스텝 · CFG 4** | 2026-02-27 대회 출품작 (최종 6144x3456) |
| 로컬 판 (2026-07) | `er_sde` / `sgm_uniform` 위주 (`beta1_1` 일부, ays 계열도 가능) · **CFG 5 고정** · 스텝은 2단으로 30/4, 30/3, 24/2, 16/4 | 2026-07-29 실사용 세팅 |
| 초보자용 아니마+IL VER.2 | **CFG 4 · shift 8** | 아래 'VER.2' 절 |

**같은 CFG 라도 판이 다르면 다른 이야기다.** 값을 옮겨 적을 때는 어느 판에서 나온 값인지 함께 적을 것.

*(preview 판 출품작의 작업 순서도 참고할 만하다 — T2I 초안 → 1차 업스케일에서 **튀는 배경과 thick line 을
`soften` 처리해** 메인 피사체로 시선을 몰고 → 얼굴·손만 국소 수정 → 색보정과 가벼운 노이즈로 마무리.
업스케일 단계에서 배경 디테일을 '더 살리는' 게 아니라 '눌러서' 주제를 부각시켰다는 점이 요령이다.)*

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [초보자를 위한 초보자의 ANIMA 워크플로우 26.04](https://arca.live/b/aiart/168821026) · [로컬 comfyui 찍먹해보기 - Spectrum 가속 26.05](https://arca.live/b/aiart/171935194) · [(anima) DyPE를 쓰면 깡으로 초고해상도 이미지를 뽑… 26.07](https://arca.live/b/aiart/176872950)</small>

??? note "근거 10건 전부 보기"
    [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [초보자를 위한 초보자의 ANIMA 워크플로우 26.04](https://arca.live/b/aiart/168821026) · [로컬 comfyui 찍먹해보기 - Spectrum 가속 26.05](https://arca.live/b/aiart/171935194) · [(anima) DyPE를 쓰면 깡으로 초고해상도 이미지를 뽑… 26.07](https://arca.live/b/aiart/176872950) · [저처럼 forge neo쓰다가 여러 문제를 겪으시는분들 혹시… 26.06](https://arca.live/b/aiart/174448928) · [Anima로 NAI 느낌 짤털 26.07](https://arca.live/b/aiart/178404708) · [(개쩌는대회) 사자왕의 봄 26.02](https://arca.live/b/aiart/163475234) · [뉴비의 아니마 워크플로우 공유 (2) 26.05](https://arca.live/b/aiart/172332889) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264) · [(anima) DyPE 노드 업데이트 (+SEGA 노드 추가) 26.08](https://arca.live/b/aiart/179097719)

## shift — 기본값 3, 0 은 검은 화면
<small>2026-06 기준 · 근거 4건</small>

`shift` 는 **스케쥴러 시그마(노이즈 세기) 곡선의 기울기**를 바꾸는 값이다.
값이 클수록 **높은 시그마 구간 — 그림의 큰 구도가 결정되는 초반 — 에 머무는 스텝 수가 늘어난다.**

| 항목 | 값 |
|---|---|
| **기본값** | **3** — 설정하지 않고 뽑은 것과 `shift 3` 의 결과물이 같았고, 댓글에서 ComfyUI `comfy/supported_models.py` 로 **3.0** 이 확인됐다 |
| **금지값** | **0** — CFG 3/18스텝, 3.5/24스텝, 4/30스텝 세 조합 **모두에서 검은 화면**이 나왔다 |
| 저스텝일 때 | 10스텝처럼 낮게 뽑으면 **5~8 로 올린다** |

왜 저스텝에서 올려야 하는가 — 구도가 높은 시그마 구간에서 이미 망가진 채 낮은 시그마 구간으로 넘어가면 기괴한 그림이 나오는데,

```text
shift 3 · 28스텝  →  높은 시그마 구간에 약 14스텝  →  구도가 무너질 일이 적다
shift 3 · 10스텝  →  같은 구간이  5스텝뿐          →  구도 자체가 자주 무너진다
```

> ⚠️ **이 설명은 `simple` 스케쥴러에만 해당한다** *(댓글 정정)*.
> 스케쥴러 10여 종 중 특성에 따라 shift 를 올리면 **의도와 정반대 효과**가 날 수 있다.
> 원 글쓴이도 본문을 뇌피셜이라 밝혔다.

**작성자 본인의 최종 권고는 손이 덜 가는 쪽이다** — *"사실 그냥 모델 권장값인 28스텝 이상으로
깡스텝을 높여 뽑는 게 가장 편하고 예쁘게 나온다."*

**다른 자료도 같은 값을 말한다.** 「Comfy ANIMA 정보글 모음」(2026-06)은 *"ANIMA 공식 기본 시프트 값은 3이다"*
라고 그대로 못박고, All in One 워크플로우 V5 의 설정값도 `shift: 3` 이다.

<small>근거 — [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [ANIMA All in One 워크플로우 v5: i2i와 인… 26.05](https://arca.live/b/aiart/171941799) · [아니마 모델의 시프트 값에 대해 알아보자 26.02](https://arca.live/b/aiart/163123039) · [아니마 모델시프트0~9까지 3번비교 26.02](https://arca.live/b/aiart/163239744)</small>

## 2단 구성 — ANIMA로 구도, Illustrious로 화풍
<small>2026-04 기준 · 근거 8건</small>

ANIMA는 **자연어 이해력은 좋지만 화풍과 미학적 구도가 약하다** (4건).
그래서 ANIMA로 구도를 잡고 **Illustrious/SDXL로 hires fix 해서 화풍을 덮는** 2단 구성이 쓰인다.

**왜 화풍이 약한가** — ANIMA는 qwen3 기반 LLM 인코더가 프롬프트를 **통째로** 인코딩한다.
그래서 작가 태그 임베딩이 평균으로 뭉개지고, **SDXL처럼 가중치만으로 화풍을 섞을 수 없다** (4건).

> 작가별 Conditioning을 분리해 average/concat 하는 우회도 시도됐지만,
> **가장 앞 작가의 그림체만 나와 사실상 실패**했다 (2건).

<small>근거 — [comfyui) Anima 찍먹용 - anima+ill 워크… 26.02](https://arca.live/b/aiart/162677789) · [Anima to XL 워크플로 공유 26.02](https://arca.live/b/aiart/161453678) · [Anima에서 작가 태그 혼합을 도와주는 커스텀 노드 제작함… 26.05](https://arca.live/b/aiart/171947113) · [아티스트 태그를 섞는 Anima Artist Mixer 노드 26.05](https://arca.live/b/aiart/172080673)</small>

??? note "근거 8건 전부 보기"
    [comfyui) Anima 찍먹용 - anima+ill 워크… 26.02](https://arca.live/b/aiart/162677789) · [Anima to XL 워크플로 공유 26.02](https://arca.live/b/aiart/161453678) · [Anima에서 작가 태그 혼합을 도와주는 커스텀 노드 제작함… 26.05](https://arca.live/b/aiart/171947113) · [아티스트 태그를 섞는 Anima Artist Mixer 노드 26.05](https://arca.live/b/aiart/172080673) · [XL to Anima 워크플로 공유 26.02](https://arca.live/b/aiart/161442385) · [(중급자를 위한) 개조 아니마-IL 워크플로우 26.04](https://arca.live/b/aiart/168234596) · [아니마용 @Conditioning쓰까쓰까 노드 26.04](https://arca.live/b/aiart/167592729) · [Anima용 작가 태그 섞기 커스텀 노드 26.05](https://arca.live/b/aiart/171467099)

## 작가 태그는 `@` — ANIMA 만의 표기 규칙
<small>2026-06 기준 · 근거 9건</small>

ANIMA 는 SDXL 계열과 **프롬프트 표기 규칙 자체가 다르다.** 여기를 틀리면 태그가 그냥 안 먹는다.

### 작가 태그에는 `@` 를 붙인다 *(3건)*

```text
단부루 표기  aaaaa_bbb   →   ANIMA   @aaaaa bbb
작가 이름    abcd efg    →   ANIMA   @abcd efg
```

**`@` 를 안 붙이면 태그 효과가 미미하다.**

> ⚠️ **이 문법은 ANIMA 전용이다.** WAI Illustrious(SDXL) 에 `(@erufura:2)` 처럼 그대로 넣으면 그림이 깨진다.
> Illustrious 계열은 모델 배포자가 올린 샘플 프롬프트를 따르고, NAI 는 `artist:이름` + `숫자:: ::` 를 쓴다.
> *"SDXL 과 ANIMA 는 휘발유차와 경유차 정도의 차이라 호환되는 것이 하나도 없다"* — 로라도 각각 받아야 한다.

**곁가지로 밝혀진 것** — SDXL 에서 `2::artist:X::` 가 먹히는 것처럼 보이는 이유는,
로컬 모델이 NAI 의 `::` 문법을 모르므로 **`2::` 와 `::` 가 그냥 노이즈로 소비되고 실제로는 `artist:X` 만 적용**되기 때문이다.
질문자가 `2` 를 전부 지우고 돌려 **결과가 동일함으로 검증됐다.**

> ⚠️ **이 문법이 아카라이브 호출 문법과 같다.** 아니마 프롬프트를 채널 글이나 댓글에 옮겨 적으면
> 엉뚱한 사람이 호출되니 주의할 것 *(2건)*.

### 퀄리티 태그는 두 계통이다 *(3건)*

| 계통 | 태그 |
|---|---|
| 사람 좋아요/싫어요 기준 | `masterpiece` · `best quality` · `good quality` · `normal quality` · `low quality` · `worst quality` |
| PonyV7 품질 판정 AI 기준 | `score_1`(최하) ~ `score_9`(최상) |

**둘 다 써도 되고, 하나만 쓰거나 아예 안 써도 동작한다.**

### 공식 프롬프트 순서

```text
[quality/meta/year/safety tags] [1girl/1boy/1other] [character] [series] [artist] [general tags]
```

대괄호 **안**의 순서는 자유고, **섹션 간** 순서만 지키면 된다. *(한 글에서만 언급됨 — 원문 171031030)*

| 섹션 | 값 |
|---|---|
| meta | `highres` · `absurdres` · `anime screenshot` · `jpeg artifacts` · `official art`. `highres` 를 넣는다고 실제 해상도가 커지지는 않고 **고해상도 이미지의 선명함 같은 특성**을 부른다 |
| year | `year 2025` · `year 2024` … 또는 `newest` / `recent` / `mid` / `early` / `old` |
| safety | `safe` · `sensitive` · `nsfw` · `explicit` — **모델이 상당히 음란해서 안 야한 것을 뽑으려면 `safe` 를 꼭 넣는다** |

### 공식 권장 네거티브

```text
worst quality, low quality, score_1, score_2, score_3, artist name
```

여기에 자기가 안 나왔으면 하는 것을 더한다. *(한 글에서만 언급됨 — 원문 171031030)*

### 2026-08-18 로컬 실검증 — **입문 기본값은 짧게 시작해도 된다**

같은 시드·같은 자연어 프롬프트·같은 `er_sde`/`simple` 로 아래 둘을 다시 맞붙였다.

| 형식 | 내용 |
|---|---|
| **짧은 입문형** | `worst quality, low quality, blurry, jpeg artifacts, realistic, photo, 3d, extra fingers, bad hands` |
| **길어진 공식형** | 위에 `score_1~3`, `artist name`, `chromatic aberration`, `bad anatomy`, `bad proportions` 등을 더한 버전 |

결과는 **길어진 쪽이 아주 약간 더 정리돼 보일 수는 있었지만 차이가 매우 작았다.**
즉 이 실검증 기준으로는 **네거티브를 길게 늘린다고 품질이 확 뛰지는 않았다.**

- **처음 한 장 / 탐색용**: 짧은 네거티브
- **문제가 생길 때만**: `score_1~3`, `artist name`, `chromatic aberration` 등을 덧붙인 공식형

특히 ANIMA 는 **긍정 프롬프트, 해상도, 샘플러 쪽이 결과를 더 크게 흔드는 경우가 많다.**
네거티브를 무작정 고봉밥으로 늘리기 전에 그쪽부터 먼저 고쳐라.

### 가중치는 SDXL 보다 훨씬 높게

문법은 ComfyUI 에서 SDXL 과 같은 `(tag:weight)` 인데 **필요한 값의 크기가 다르다.**

| | |
|---|---|
| 시작점 | `(chibi:2)` — **`:2` 정도부터** |
| 왜 | Qwen3+LLM 어댑터가 만든 임베딩 공간의 벡터를 스케일하는 방식이라 **cross attention 구조상 SDXL 보다 훨씬 높은 가중치가 필요**하다 *(공식 답변)* |
| ⚠️ 상한 | **4 이상을 남발하면 연산이 깨져 검은 화면**이 나올 수 있다 |

음수 가중치도 적용된다.

### 태그 표기 잔규칙

- 소문자로 쓴다
- 언더스코어 대신 **스페이스** (`score_` 태그만 예외로 언더스코어 유지)
- Danbooru 와 Gelbooru 태그가 다르면 **Gelbooru 버전 우선**
- Tag dropout 으로 학습돼서 **모든 태그를 빠짐없이 넣을 필요는 없다**

### 콤마와 띄어쓰기 — ANIMA 는 여기를 본다 *(2026-06)*

```text
단어,          ←  단어와 콤마 사이에 공백을 두지 않는다
, 다음단어     ←  콤마와 다음 단어 사이에는 공백을 둔다

자연어 문장 →  대문자로 시작해 온점(.) 으로 끝낸다
태그        →  소문자로 시작해 콤마(,) 로 끝낸다
맨 마지막   →  아무것도 안 붙여도 된다
```

**시점 태그는 혼용할 수 없다** — `from above` · `from below` · `from side` 를 한꺼번에 섞으면 성립하지 않는다
(`from above` + `from side` 정도는 가능). 역할이 비슷한 태그는 모아서 쓴다.

서식 민감성(언더바 하나로 캐릭터를 못 알아보는 문제, 괄호 이스케이프)은 바로 다음 절에 이어진다.

> **가중치 상한은 조건에 따라 갈린다.** 위의 `4` 는 일반 t2i 에서 프롬프트 전체에 높은 값을 뿌릴 때 이야기이고,
> lllite 인페인팅으로 구도를 고정하고 **단일 태그 하나에만** 가중치를 주면 `15.3` 까지 올라간다.
> 아래 "프롬프트 가중치의 실제 상한" 절에 조건별로 정리했다.

> **같은 태그도 프롬프트 안에서의 위치에 따라 conditioning 이 달라진다**는 실험 결과가 있다 —
> 위 공식 순서 규칙(작가 태그는 인원수 태그 바로 뒤)에 근거가 생긴 셈이다. → [프롬프트 쓰는 법](prompting.md)


<small>근거 — [웹 아니마 26.06](https://arca.live/b/aiart/173582055) · [로컬 아니메 모델 Anima에 대한 잡다한 정보 개정판 26.05](https://arca.live/b/aiart/170924904) · [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651)</small>

??? note "근거 9건 전부 보기"
    [웹 아니마 26.06](https://arca.live/b/aiart/173582055) · [로컬 아니메 모델 Anima에 대한 잡다한 정보 개정판 26.05](https://arca.live/b/aiart/170924904) · [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [anima용 슈퍼울트라작가믹스 26.07](https://arca.live/b/aiart/177376366) · [로컬 아니메 모델 Anima에 대한 잡다한 정보 26.02](https://arca.live/b/aiart/161337087) · [마이크로 비키니 크기로 anima lllite 가중치 강도 … 26.06](https://arca.live/b/aiart/174717928) · [로컬 anima로 팬티 내리기 태그 하는데 26.06](https://arca.live/b/aiart/173497043) · [wai illustious SDXL은 아니마 프롬프트가 안먹… 26.06](https://arca.live/b/aiart/174739881)

## 프롬프트 쓰는 법
<small>2026-07 기준 · 근거 6건 · 자료 엇갈림</small>

- **최소 2문장 이상** 쓴다
- 품질·아티스트 태그는 **앞부분**에 둔다
- 여러 캐릭터를 넣을 때는 **이름만 나열하지 말고 외형을 설명**한다

*(3건)*

> ⚠️ **여기는 자료가 갈린다.** 한쪽은 "태그를 자연어로 변환해 넣는 쪽이 타율이 좋다"고 하고,
> 다른 쪽(gems v5)은 "서술형 자연어 금지, 순수 단부루 태그만"이라고 한다. 찬성 1 / 반대 1로
> **결론이 안 났다.** 둘 다 해보고 판단할 것.

### 2026-08-18 로컬 실검증 — **외형 고정은 자연어 2문장이 더 나았다**

실제로 같은 로컬 환경에서 **태그 나열 vs 2문장 자연어**를 한 번 더 맞붙여 봤다.
설정은 `anima-base-v1.0`, `832x1216`, `steps 30`, `cfg 4`, `er_sde`, `simple` 이고
네거티브는 같게 둔 상태였다.

| 형식 | 관찰 |
|---|---|
| 짧은 태그 나열 | `long black hair` 를 넣었는데도 **짧은 보브컷 쪽으로 기운 결과**가 나왔다 |
| 2문장 자연어 | **긴 검은 머리와 상반신 구도**를 더 안정적으로 유지했다 |

이 비교는 **"자연어가 언제나 더 좋다"** 는 증거가 아니다.
다만 입문자가 처음 한 장을 뽑을 때는 **속성 보존이 먼저냐, 빠른 변주가 먼저냐**로 갈라 잡는 편이 실용적이다.

- **외형 고정이 먼저**: 자연어 2문장으로 시작
- **태그 실험이 먼저**: 짧은 단부루 태그 나열로 시작

즉 ANIMA 입문 기본값은 이렇게 두면 된다.

> **정확한 머리 길이·복장·배경 관계를 먼저 잡고 싶으면 자연어 2문장,  
> 익숙한 태그를 빠르게 갈아 보며 방향만 볼 거면 태그 나열.**

**Regional Prompter**는 가로·세로 2등분 또는 3등분까지만 지원하고 아직 베타 수준이다.
구역과 구역별 LoRA가 늘수록 고속 로라를 써도 느려진다 (2건).

---

**서식에 이례적으로 민감하다.** ANIMA 의 텍스트 인코더 `qwen3 0.6b` 는 예전 SD 의 CLIP 과 달라
**의미 없는 공백(스페이스) 하나만 추가해도 그림이 살짝 달라진다** *(2026-05)*.

가장 자주 밟는 지뢰는 **언더바**다. 단부루에서 캐릭터명을 그대로 복사하면 `_` 가 남는데,

> 글쓴이가 든 예의 캐릭터는 데이터셋에 **최소 2500장, 해당 복장만 800장 이상** 들어 있는데도
> **언더바 하나로 고증이 무너졌다.**

| 하지 말 것 | 할 것 |
|---|---|
| `hakurei_reimu` | `hakurei reimu` (언더바 → 공백) |
| `(작품명)` 그대로 | `\(작품명\)` (괄호는 `\` 로 이스케이프) |
| 의미 없는 줄바꿈·연속 공백 | 정리해서 넣기 |

정리 노드가 있다 — `https://github.com/1lch2/ComfyUI-AnimaPromptFormatter`
(**동명의 다른 노드가 있으니 주의**). `tag1,tag2,  tag3\n,tag4, ,tag5` → `tag1, tag2, tag3, tag4, tag5` 로 정리해 준다.
단 **기본 CLIP 텍스트 인코딩 노드가 아니라 이 노드에** 프롬프트를 적어야 한다.

<small>근거 — [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463) · [아니마 자연어 프롬프트 공식 팁 26.05](https://arca.live/b/aiart/171082011) · [ANIMA용 잼민이 gems v5 26.07](https://arca.live/b/aiart/177929816) · [comfyUI ANIMA 그림체 및 워크플로우 공유 26.04](https://arca.live/b/aiart/168777426)</small>

??? note "근거 6건 전부 보기"
    [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463) · [아니마 자연어 프롬프트 공식 팁 26.05](https://arca.live/b/aiart/171082011) · [ANIMA용 잼민이 gems v5 26.07](https://arca.live/b/aiart/177929816) · [comfyUI ANIMA 그림체 및 워크플로우 공유 26.04](https://arca.live/b/aiart/168777426) · [아니마용 @Conditioning쓰까쓰까 노드 26.04](https://arca.live/b/aiart/167592729) · [Anima용 작가 태그 섞기 커스텀 노드 26.05](https://arca.live/b/aiart/171467099)

## 여러 명 뽑기 — 리저널 대신 아니마
<small>2026-07 기준 · 근거 5건 · 자료 엇갈림</small>

로컬에서 캐릭터를 여러 명 뽑는 표준 답은 오랫동안 **리저널 프롬프트 + 컨트롤넷**이었다.
그 방법을 가르치는 글(원문 161686015)의 **댓글 4번에서 제작자 본인이** 더 근본적인 대안을 적었다.

> **"두 명 이상 뽑는 게 목적이면 요즘 나온 Anima 모델을 쓰는 게 낫다.
> 컨트롤넷이나 리저널 없이도 잘 뽑아 준다."**

리저널이 힘든 이유가 그 글 안에 그대로 있다 — **캐릭터 위치가 시드마다 랜덤이라, 손으로 칠한 마스크와
실제 캐릭터 위치가 어긋나면 특성이 이상하게 섞인다.** 시드 고정 + 트레이싱, openpose 컨트롤넷 같은
우회가 전부 이 문제를 메우려는 것이다. 그 글의 결론도 *"컨트롤넷만 쓰면 사람은 두 명 나오지만 특성을
먹이기 힘들어서 리저널과 같이 써야 한다"* 였다. ANIMA 는 자연어를 통째로 읽어 인물을 나누므로
그 단계가 통째로 없어진다.

### 단서 — 당시엔 "LoRA 가 안 먹힌다" 였다

같은 댓글이 조건을 달았다.

> "다만 Anima 는 LoRA 가 안 먹혀서 **창작 캐릭터 LoRA 를 쓸 거면** 이 방법(리저널)이 필요하다." *(2026-02-06)*

**이 단서는 그 뒤 갱신됐다.**

| 2026-02 (프리뷰 시절) | 2026-05 정식 출시 이후 |
|---|---|
| ANIMA 용 LoRA 자체가 없어 "로라가 안 먹힌다"로 통했다 | **ANIMA 전용으로 학습된 LoRA 는 정상 동작한다** — 캐릭터 LoRA(강도 1) · 터보 로라 · 디테일러 로라가 실제로 쓰인다 *(4건)* |

지금도 참인 것은 **"SDXL(Illustrious·NoobAI)용 LoRA·임베딩·컨트롤넷은 전혀 호환되지 않는다"** 쪽이다.
쓰려는 LoRA 가 **ANIMA 용으로 구워진 것인지**만 확인하면 된다 → [로라 쓰는 법](lora-usage.md)

### 그래도 아니마가 다 해주지는 않는다

여러 명을 뽑을 때 실제로 걸리는 것들 *(원문 171042669 댓글)*:

- 자연어로 쓸 때는 **문장마다 캐릭터 이름을 반복**해야 한다. 이름 없이 묘사만 쓰면 그 묘사를 누구에게 적용할지 모델이 헤맨다
- **위치 지정과 프롬프트 순서, 해상도**가 결과에 영향을 준다
- **디테일러 사용이 사실상 필수**다 — 운이 나쁘면 캐릭터 간 프롬프트가 섞인다
- 비슷한 캐릭터끼리 섞이면 **다른 캐릭터의 트리거를 네거티브에 넣어 밀어내는** 방식이 쓰인다

2인 예시(원문 171042669 댓글):

```text
masterpiece, best quality, score_9, score_8, score_7, highres, newest, 2 girls, lesbians.
This is an illustration in @SGJ style. This image illustrates one tall girl and one short girl kissing.
The taller girl, lmy, is on the left side of the image. lmy is kissing khy. khy is on the right side...
```

*맨 위 인용은 원문 161686015 한 글의 댓글에서 나온 말이다. 다만 뒤집힌 LoRA 단서 쪽은 4건이 뒷받침한다.*

> ⚠️ **한때 표준처럼 돌던 `Left girl is tpp \( 외형 태그 \).` 문법은 2026-07-28 에 부정됐다.**
> 이스케이프가 인물을 묶어 준다는 설명이 해골물이었다는 것 — **바로 다음 절**에 정정을 실어 두었다.

→ 같은 캐릭터를 계속 유지하는 문제는 [같은 캐릭터 계속 뽑기](consistency.md)

<small>근거 — [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [로컬 comfyui 찍먹해보기 - 리저널 프롬프트 26.02](https://arca.live/b/aiart/161686015) · [오늘의 한요일은 여자다 "Anima" 올인원(거의)로라 공유 26.05](https://arca.live/b/aiart/171042669) · [아니마 디테일러 로라 5종 간단 비교 26.06](https://arca.live/b/aiart/175333518)</small>

??? note "근거 5건 전부 보기"
    [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [로컬 comfyui 찍먹해보기 - 리저널 프롬프트 26.02](https://arca.live/b/aiart/161686015) · [오늘의 한요일은 여자다 "Anima" 올인원(거의)로라 공유 26.05](https://arca.live/b/aiart/171042669) · [아니마 디테일러 로라 5종 간단 비교 26.06](https://arca.live/b/aiart/175333518) · [ANIMA 터보 로라 3종 테스트. 26.07](https://arca.live/b/aiart/175962147)

## ⚠ 다인물 문법의 이스케이프 `\( \)` — 이 설명은 부정됐다
<small>2026-07 기준 · 근거 3건 · 자료 엇갈림</small>

채널에 널리 퍼진 다인물 프롬프트 문법이 있다. 원 출처는 2026-05-26 의 실험글(171855587)이고,
**이스케이프 괄호가 인물을 묶어 준다**는 설명과 **`\)` 뒤를 반점으로 끝내면 인물이 섞인다**는 규칙이 함께 따라다녔다.

```text
3girls, 1orc, white background.
Left girl is tpp \( 외형 태그, 외형 태그 \).
Background : A bald green orc ... in the left.
```

### 이 설명은 부정됐다 *(2026-07-28, 두 글 · 여러 명 수긍)*

| 퍼져 있던 설명 | 실제 |
|---|---|
| `\( \)` 이스케이프가 인물을 묶어 프롬프트 오염을 막는다 | ❌ **이스케이프를 빼도 결과가 똑같다.** 작가 태그도 빼고 돌려도 그대로 적용된다 |
| `\)` 뒤는 반드시 온점(`.`) — 반점(`,`)이면 다음 인물과 섞인다 | ❌ 위 전제 위에 세워진 규칙이라 근거가 함께 무너졌다 |
| `Quality:` · `Background:` 같은 **레이블 접두어**로 항목을 나눈다 | ❌ **ANIMA 에서 레이블 접두어는 전혀 먹지 않는다.** `\<` 도 아예 안 먹는다 |
| 원 참고글의 문법 자체 | ❌ *"애초에 글쓴이가 참고했다는 글 자체가 잘못됐다"* 는 지적이 나왔고, 여러 사람이 *"지금까지 해골물을 퍼먹고 있었다"* 고 수긍했다 |

### 그러면 이스케이프는 왜 붙이나 — 진짜 역할

이스케이프는 **모델이 아니라 ComfyUI 가 파라미터의 성질을 분류하는 장치**다.

```text
(  ...  )     →  가중치 문법으로 해석된다 — 덩어리 전체에 가중치가 걸린다
\( ... \)     →  "이건 가중치용이 아니다" — 그냥 글자로서의 괄호
```

그러므로 **묶으려고 괄호를 쓴 것이라면 이스케이프를 붙이는 쪽이 맞다.**
안 붙이면 그 덩어리 전체에 의도하지 않은 가중치가 걸린다.
다만 이스케이프가 하는 일은 **거기까지이고, 인물을 분리해 주지는 않는다.**

### 그럼 무엇을 쓰나

- 괄호 안에는 **외형과 의상만** 넣고, **행동·상황·상호작용은 괄호 밖에서 자연어로 제대로 서술한다**
- *"왼쪽의 여성은 (lying, on back)하고 있다"* 처럼 **한국어로 쓴 뒤 번역해 넣는 자연어 + 태그 혼용**이 실제로 권장됐다
- 레이블을 붙이고 싶은 자리는 레이블 대신 자연어 문장으로 쓴다

### 이 문법으로도 안 되는 것

- **의상 태그는 여전히 서로 섞인다.** 인물과 상황은 분리되는데 옷이 상대 인물에게 넘어간다
- **디테일러 프롬프트에 눈 색을 적어 두면 얼굴이 그쪽을 따라간다** — 디테일러 프롬프트가 본 프롬프트를 덮어쓴다
- 대명사가 먹히는지(`A girl who is XXX on the left, ( ... ). XXX is doing something...`)는 질문만 나오고 답이 없었다

> **원 글의 타율 수치(위치만 약 70% / 이름까지 약 90% / 상대 위치까지 약 99%)도 부정된 전제 위에서 잰 값이다.**
> 다인물 자체는 ANIMA 가 리저널·컨트롤넷 없이 잘 뽑아 주므로(바로 앞 절) 그 부분까지 버릴 필요는 없다.
> **버려야 하는 것은 "이스케이프가 그 공을 세웠다" 는 설명이다.**

*이 문법을 그대로 실어 둔 [프롬프트 쓰는 법](prompting.md) 의 '여러 명을 섞이지 않게' 절도 이 정정과 함께 읽을 것.*

<small>근거 — [오크의 가슴잡기로 알아보는 태그형에 가까운 아니마의 하이브리… 26.05](https://arca.live/b/aiart/171855587) · [ANIMA 자연어 프롬 오염 어쩌구... 이걸 원한거임? 26.07](https://arca.live/b/aiart/178231780) · [ANIMA 자연어 프롬 오염 26.07](https://arca.live/b/aiart/178230466)</small>

## 그래도 리저널이 필요하다면 — 마스크를 SAM3 에게 맡겨라
<small>2026-02 기준 · 근거 1건</small>

창작 캐릭터 LoRA 를 여러 개 써야 하는 등 리저널을 피할 수 없을 때, **마스크를 손으로 칠하지 않는 방법**이
있다 *(2026-02, 원문 162598061)*.

핵심은 한 줄이다 — **디테일러에 쓰던 SAM3 에게 `left people` / `right people` 이라고 써서 넘겨라.**
SAM3 는 자연어 텍스트 프롬프트로 이미지에서 대상을 찾아 마스크를 따 주는 세그멘테이션 모델이다.

| 인원 | SAM3 `text prompt` |
|---|---|
| 2인 | `left people` · `right people` (각각 따로) |
| 3인 | `left people, middle people, right people` |

### 절차

| 단계 | 하는 일 |
|---|---|
| 1 | **가안 뽑기** — 사람이 대충 어디 있는지만 잡으면 되므로 **스텝을 최대한 줄여** '사람 비스무리하게'만 뽑는다. 이때 잠재이미지 너비·높이를 **별도 노드로 빼 두면** 뒤에서 재사용할 수 있다 |
| 2 | **마스크 자동 생성** — 가안 이미지를 그대로 SAM3 에 넣고 위 표대로 text prompt 를 적는다. 마스크가 **딱 맞게** 잡히므로 여유 있게 조금 늘려 준다 |
| 3 | **본 생성** — 아래 두 가지를 지킨다 |

> ⚠️ **잠재 데이터는 빈 latent 가 아니라 가안에서 나온 latent 를 가져다 써야 한다.**
> 빈 latent 로 하면 **찐빠가 많이 났다.**
>
> ⚠️ **denoise 는 최대한 높게.** `0.8` 까지 낮추면 프롬프트에 지정한 옷을 안 입고
> **가안에서 뽑힌 옷을 그대로 입으려 한다.** 스텝은 평소보다 조금 줄인다.

글로벌 프롬프트용 마스크는 빈 이미지에 1단계에서 빼 둔 너비·높이 노드를 연결하고 색상만 맞춰
마스크로 변환해 만든다.

**실제 예시**

```text
베이스   2girls, park  /  standing on street, cowboy shot
좌측     1girl, solo, green hair, blue eyes, short hair, smile
        brown trench coat, black skinny jeans, teal scarf, leather boots, standing, cowboy shot
우측     1girl, solo, yellow eyes, long hair, black hair
        charcoal sleeveless dress, silver bracelet, minimalist watch, tote bag, standing, cowboy shot
```

3인도 되고 컨트롤넷도 되며, 댓글에서 **LoRA 와 highres 를 얹어도 잘 된다**고 확인됐다.

*한 글에서만 나온 방법이다 — 작성자 본인도 ComfyUI 를 배운 지 이틀 됐다고 미리 밝혔다.
수치보다 발상 자체를 가져다 쓰는 쪽이 맞다.*

리저널 프롬프트 노드 조작은 [ComfyUI 쓰는 법](comfyui.md), 마스크 편집은 [인페인팅](inpainting.md) 을 보라.

<small>근거 — [comfy에서 리저널+SAM3로 여러캐릭 한번에 뽑기 26.02](https://arca.live/b/aiart/162598061)</small>

## LLLite 컨트롤넷 — 경로가 바뀌었다
<small>2026-05 기준 · 근거 6건</small>

> ⚠️ **ComfyUI 업데이트로 경로가 바뀌었다.** 서로 다른 두 글에서 **각각 댓글로 같은 정정**이
> 나왔다. 본문만 읽으면 둘 다 옛 경로를 알려준다.

| | 경로 | 노드 |
|---|---|---|
| **지금** | `models/model_patches` | `ModelPatchLoader` 를 `Apply Anima ControlNet-LLLite` **앞에** 연결 |
| 예전 | `models/controlnet` | `Apply Anima ControlNet-LLLite` 만 |

**인페인팅에서 특히 중요하다.** LLLite 인페인팅 모델을 물리면 **denoise 0.9 이상에서도 원본
일관성이 유지**되지만, LLLite 없이는 **0.7 이상에서 마스크 경계가 깨진다** (2건).

**어느 파일을 받을 것인가는 다음 절에서 다룬다** — 인페인팅 LLLite 는 챈산 0XX → kohya v1 → v2 로 세 세대를 거쳤고,
지금 받아야 하는 것은 **정식판 기준으로 재학습된 kohya v2** 다.


<small>근거 — [Anima 찍먹해보기 - 인페인팅 26.05](https://arca.live/b/aiart/171376566) · [Anima 찍먹해보기 - LLLite Controlnet 26.05](https://arca.live/b/aiart/171458536) · [kohya가 만든 Anima용 인페인팅 LLLite 컨트롤넷 26.05](https://arca.live/b/aiart/170374198) · [kohya 제작 Anima용 인페인팅 LLLite 컨트롤넷 … 26.05](https://arca.live/b/aiart/170867594)</small>

??? note "근거 6건 전부 보기"
    [Anima 찍먹해보기 - 인페인팅 26.05](https://arca.live/b/aiart/171376566) · [Anima 찍먹해보기 - LLLite Controlnet 26.05](https://arca.live/b/aiart/171458536) · [kohya가 만든 Anima용 인페인팅 LLLite 컨트롤넷 26.05](https://arca.live/b/aiart/170374198) · [kohya 제작 Anima용 인페인팅 LLLite 컨트롤넷 … 26.05](https://arca.live/b/aiart/170867594) · [kohya의 ComfyUI-Anima-LLLite 커스텀 노드 26.05](https://arca.live/b/aiart/169455470) · [ANIMA 야매 레퍼런스 인페인팅(?) 워크플로우. 26.05](https://arca.live/b/aiart/171682435)

## LLLite 인페인팅 — 챈산 0XX 에서 kohya v1/v2 로
<small>2026-05 기준 · 근거 4건 · 자료 엇갈림</small>

앞 절이 **경로**(모델을 어디에 넣고 어느 노드로 부르는가) 이야기라면, 여기는 **어느 파일을 받을 것인가** 다.
Anima 인페인팅 LLLite 는 **세 세대를 거쳤고 지금 받아야 하는 것은 kohya 판 v2** 다.

| 세대 | 파일 | 성격 |
|---|---|---|
| 챈산 0XX | `anima-lllite-inpainting-001` · `-006` (`huggingface.co/hanzogak/Anima-LLLite-Inpainting`) | ⚠️ **LLLite 에 인페인팅 기능이 없던 시절의 억지 구현.** 성능 불이익이 구조적으로 필연이었다. 제작자도 넓은 범위의 인페인팅에 취약하고 다른 LLLite 와 중복 사용이 안 되는 것 같다고 밝혔다 |
| **kohya v1** | `anima-lllite-inpainting-v1.safetensors` (`huggingface.co/kohya-ss/Anima-LLLite`) | **LLLite 쪽에 인페인팅 기능이 추가되면서 만들어진 진짜 인페인팅 컨트롤넷.** 0XX 사용자는 빠르게 넘어가는 것이 권장된다 |
| **kohya v2** | `anima-lllite-inpainting-v2.safetensors` | **Anima 정식판(BASE) 기준으로 새로 학습 + 고해상도 대응.** v1 을 쓰던 사람은 v2 로 올리는 것이 맞다 |

확장은 `https://github.com/kohya-ss/ComfyUI-Anima-LLLite` 이고 **기존 사용자도 커스텀 노드 업데이트가 필요**하다.
워크플로우 json 은 `huggingface.co/hanzogak/Anima-Comradeship/blob/main/workflow/kohya-inpainting-v1.json`
(kohya 공식이 아니라 이해하기 쉽게 손본 것).

### 수정 부위 밖의 색까지 변할 때 *(댓글 해결)*

```text
Set Latent Noise Mask 를 적용   또는   VAE Encode 를 인페인팅용(VAE Encode for Inpainting)으로 교체
+ 완화책으로 CFG 를 낮춘다
```

> ⚠️ **[인페인팅](inpainting.md) 문서에는 반대 방향의 권고가 있다** — `VAE Encode (for Inpainting)` 은
> 마스킹 주변부가 깨지니 `VAE Encode` + `Set Latent Noise Mask` 를 쓰라는 것이다.
> 이 글의 댓글은 **둘 중 아무 쪽이나 색 변화 문제를 해결한다**고 정리했다. 양쪽을 병기하니 직접 대 보고 고를 것.

손 찐빠 수정에도 성능이 좋다는 반응이 여럿이었고, NoobAI 인페인팅도 억지 구현이라 Anima 쪽으로 넘어올 이유가 된다는 언급이 있다.

→ [인페인팅](inpainting.md) · [컨트롤넷](controlnet.md)

<small>근거 — [대충 만든 Anima용 인페인팅 LLLite 컨트롤넷 26.05](https://arca.live/b/aiart/169549288) · [kohya가 만든 Anima용 인페인팅 LLLite 컨트롤넷 26.05](https://arca.live/b/aiart/170374198) · [조금 더 좋은 Anima용 인페인팅 LLLite 컨트롤넷 만… 26.05](https://arca.live/b/aiart/169700812) · [kohya 제작 Anima용 인페인팅 LLLite 컨트롤넷 … 26.05](https://arca.live/b/aiart/170867594)</small>

## 가속 — 무엇이 얼마나
<small>2026-06 기준 · 근거 9건</small>

| 방법 | 효과 | 근거 |
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
`ruwwww/ComfyUI-Spectrum-sdxl` 와 Anzhc의 `Anima Mod Guidance` 로 우회한다 (2건).

---

**SageAttention 을 어디서 받나** *(2026-06)*

```text
공식 wheels    https://comfy-org.github.io/wheels
튜링(RTX 20)   https://github.com/woct0rdho/SageAttention    ← Windows wheel fork
```

⚠️ **컴피가 배포하는 wheels 는 튜링(RTX 20) 세대에 대응하지 않는다.** 댓글 제보로 원문에 경고문이 추가된 사항이다.

> **공유받은 워크플로우에서 오류가 터지는 가장 흔한 범인이 sage-attention 이다** — 미설치이거나 버전이 안 맞는 경우다.
> 매니저에서 검색되는 `ComfyUI-SageAttention3` 가 아니라 `kijai/ComfyUI-KJNodes` 의 sageattention 노드를 써야 하고,
> **애초에 sageattention 자체를 ComfyUI 에 설치해야 한다.**

<small>근거 — [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [초보자를 위한 ANIMA All in One 워크플로우 v2 26.05](https://arca.live/b/aiart/169548769)</small>

??? note "근거 9건 전부 보기"
    [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [초보자를 위한 ANIMA All in One 워크플로우 v2 26.05](https://arca.live/b/aiart/169548769) · [anima PID 업스케일링 원클릭 노드 배포 26.06](https://arca.live/b/aiart/172741115) · [로컬 comfyui 찍먹해보기 - Spectrum 가속 26.05](https://arca.live/b/aiart/171935194) · [개인용 아니마 워크플로우 공유 26.06](https://arca.live/b/aiart/174806461) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264) · [torch.compile 캐시 저장으로 최초로딩속도 줄이기 26.05](https://arca.live/b/aiart/171503442)

## 가속을 붙이는 순서 — 45초를 12초로
<small>2026-05 기준 · 근거 1건</small>

가속 노드를 **하나씩 붙여 나간 총집편**이 있다 *(2026-05, ComfyUI 기본은 아는 사람 대상)*.
기준 환경은 **5060Ti 16GB / 30스텝 / 1k 해상도**.

```text
아무것도 안 붙였을 때   약 45초
전부 적용 후          약 12~15초
VRAM                7.6GB → 7.9GB  (거의 그대로)
```

| 순서 | 붙이는 것 | 단축 |
|---|---|---|
| 1 | **fp16 가속** — 포터블 실행파일 중 `fast_fp16_accumulation` 이 붙은 것 (`--fast fp16_accumulation`) | **5~10초** |
| 2 | **SageAttention** — kjnodes 의 `patch sage attention kj` | 0.5~2초 |
| 3 | **Spectrum** — 생성 도중 일부를 캐싱해 빠르게 넘김 | **약 10초** |
| 4 | **컴파일** — **모델 변조가 전부 끝난 다음에** 붙일 것 | 약 8초 |
| 5 | **SPEED** (`ruwwww/ComfyUI-SPEED`) — 절반 해상도로 뽑다가 단계적으로 올림 | 1~2초 |

**실행 인자와 노드의 차이** — `--fast fp16_accumulation` 실행 인자는 모델뿐 아니라 **VAE·CLIP 에도** 영향을 주고,
kjnodes 의 `model patch torch settings` 노드는 **해당 모델에만** 영향을 준다.
세이지 노드를 거쳤는데 오히려 느려지면 앞에 `model patch torch settings` 를 붙여 fp16 가속을 다시 켜 보라.

**컴파일 주의** — 첫 1회 생성만 오래 걸리고 그다음부터 정상이다.
에러가 나면 **다이나믹 VRAM 을 비활성화**해 본다.
*(댓글: block compile 과 fp16 accumulation 은 동시 사용이 안 되는 것 같다는 보고가 있다.)*

**SPEED 연결** — 일반 KSampler 가 아니라 `SamplerCustomAdvanced`(고급 사용자 정의 샘플러)에
요소를 분리해 연결해야 한다 — 무작위 노이즈=시드 / CFG 가이드=모델+프롬+네거 / base_sampler=쓸 샘플러 / 스케줄러+스텝(여기에도 모델 연결).

수치별 세부는 [VRAM·속도 최적화](vram.md) 에 더 있다.

<small>근거 — [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463)</small>

## int8 양자화로 SDXL 만큼 — 최적화를 다 붙였을 때의 실측
<small>2026-04 기준 · 근거 1건</small>

위 "가속" 표가 *무엇이 얼마나 빠른가* 라면, 여기는 **그것들을 한꺼번에 붙인 실측 한 벌**이다.
결론부터 — **ANIMA 가 같은 조건의 SDXL 보다 빨라진다.**

### 붙인 것 다섯

| 요소 | 무엇 |
|---|---|
| **Int8rowwise 양자화 모델** | `ComfyUI/models/diffusion_models` 에 넣는다. TE·VAE 는 원래 저장소 것을 `text_encoders` · `vae` 에 |
| **sage attention** | RTX 2000 시리즈는 **1.0.6** |
| **torch.compile** | triton-windows 필요 — RTX 2000 시리즈는 **3.2.0** |
| **EasyCache** | 기본설정 그대로 |
| **Scheduled CFG** | `end 0.6` |

```text
실행 옵션 전체
--fast fp16_accumulation fp8_matrix_mult cublas_ops --use-sage-attention
--disable-api-nodes --disable-dynamic-vram
```

필요한 커스텀 노드는 **KJNodes** 와 **ComfyUI-INT8-Fast** 이고, RTX 2000 시리즈 이상 NVIDIA GPU 가 전제다.

### RTX 3060 실측

| 모델 | 그냥 | EasyCache + Scheduled CFG |
|---|---|---|
| `anima-preview3-base` (bf16) | 1.09 s/it · **33.36초** | 1.53 it/s · **20.23초** |
| **int8rowwise** | 1.35 it/s · 23.05초 | **1.94 it/s · 16.29초** |
| *(참고)* 같은 조건 SDXL — 832x1216 / 30steps | | 1.89 it/s · 17.09초 |

```text
VRAM   6.2GB  →  4.9GB
```

**품질은 bf16 과 int8rowwise 가 거의 차이 없고**, 양자화·캐시에서 흔히 깨지는 망사스타킹 같은
디테일도 크게 상하지 않았다고 한다.

> ⚠️ **대가는 첫 생성 한 번이다.** torch.compile 때문에 **첫 장이 2분 가까이** 걸린다.
> 그다음부터는 위 수치대로 나온다.

### 왜 INT8 인가 — FP8 과 갈리는 지점

양자화는 원본 2차원 행렬을 더 작은 데이터타입으로 바꾸면서 **소수점 부분을 FP32 스케일팩터가 담당**하게 하는 것이다.
`int8rowwise` 는 행렬을 int8 로 두고 **스케일팩터를 행마다 하나씩** 준다.

| | 지원 시작 |
|---|---|
| **INT8 행렬곱 가속** | **RTX 2000(Turing)부터** |
| FP8 행렬곱 가속 | RTX 4000부터 |

**그래서 구형 카드에는 INT8 이 유리하다.** 정수만 표현해 생기는 오차는 row-wise 스케일로 보완한다.
(참고로 GGUF Q8 은 32개 블록마다 FP32 하나라 더 정밀하다 — 형식별 비교는
[모델 고르기](models.md) 의 "양자화 파일 고르기" 항목에 있다.)

### INT8 모델에 로라를 붙일 때

| 항목 | 값 |
|---|---|
| 노드 | **ComfyUI-INT8-Fast 의 전용 `Load Lora (INT8)`** (`https://github.com/BobJohnson24/ComfyUI-INT8-Fast`) |
| 위치 | model 출력선 아무 데나 붙여도 되지만 **Torch Compile 과 KSampler 사이**가 좋다 |

**자주 나는 오류 하나** *(질문자 확인)*

```text
torch._dynamo.exc.TorchRuntimeError ... a and b must have same reduction dim
   →  워크플로우의 Torch Compile 노드에서 dynamic 을 false 로 바꾼다
```

그 밖 — 워크플로우가 자꾸 App 모드로 열리면 좌측 상단 워크플로 전환 버튼을 쓰고,
이미지가 webp 로만 저장되는 것은 마지막 노드가 `Save AnimatedWEBP` 라서이니 `Save Image` 로 바꾼다.
**8GB VRAM(4060)에서도 무리 없을 것**이라는 것이 작성자 답변이다.

워크플로우 JSON(LoRA 로더 포함): `https://drive.google.com/file/d/1MB4hpzPrY3Pdlp5CWSJbuCU0-ceM4lAP`

*(2026-04, 원문 167246595 한 글의 실측이다. 다만 개별 요소의 효과는 위 "가속 — 무엇이 얼마나" 표와 어긋나지 않는다.
양자화판을 받는 곳은 [자원](resources.md), 옵션 전반은 [VRAM·속도 최적화](vram.md).)*

<small>근거 — [워크플로) SDXL만큼 빠른 Anima T2I 26.04](https://arca.live/b/aiart/167246595)</small>

## 화질 보정 노드 넷 — 겹쳐 쓰면 탄다
<small>2026-07 기준 · 근거 3건</small>

속도가 아니라 **화질을 올리는** 노드 묶음이다. 넷 다 같은 함정을 공유한다 — **겹쳐 쓰면 그림이 탄다.**

**1. Anima Mod Guidance** (Anzhc) — `https://github.com/Anzhc/Anima-Mod-Guidance-ComfyUI-Node`

clip-l 을 받아 `clip` 폴더에 넣고 CLIP 로드 노드로 고른다. **연결 방향을 틀리기 쉽다:**

```text
생성에 쓴 프롬프트  →  clip_base_conditioning
퀄리티 프롬프트     →  clip_positive_conditioning
네거티브           →  네거티브 그대로,  모델  →  Spectrum 에서 연결
```

> 원문이 처음에 **반대로 적었다가 댓글 지적으로 정정**됐다. 옛 판을 보고 따라 했다면 뒤집혀 있을 수 있다.

**2. Skimmed CFG** — `https://github.com/Extraltodeus/Skimmed_CFG`

CFG 수치 때문에 그림이 타거나 과채도가 나는 AI스러움을 자연스럽게 풀어 준다.
사람에 따라 뿌예졌다고 느낄 수 있다. **터보(CFG 1)를 쓰면 네거가 거의 무시되므로 의미가 없다** *(댓글)*.

**3. DCW + CWM + SMC** — `https://github.com/namemechan/ComfyUI-DCW`

| 항목 | 값 |
|---|---|
| SMC 무난한 값 | **6 / 0.2** |
| SMC 를 꺼야 할 때 | 가로로 긴 해상도에 **한 명만** 뽑는데 인물 분리가 일어날 때 (SMC 기술 자체의 문제) |
| 수치 찾는 순서 | DCW 의 `l` 만 남기고 나머지를 0 → `h` 조절 → `cwm` 조절 |
| ⚠️ | **cfg 리스케일을 쓰면 CWM 과 SMC 가 비활성화된다** |

> DCW 시리즈는 장면에 따라 역효과가 나므로 무지성으로 쓰지 말 것 —
> **저점 올리는 용도는 안전하고 고점 올리는 용도는 그림·세팅에 따라 다르다**는 것이 글쓴이 답이다.

**4. Anima Safe PAG** — `https://github.com/iljung1106/comfyui-anima-safe-pag`

PAG(Perturbed Attention Guidance)는 일부러 낮은 퀄리티 이미지를 함께 만들어 그 차이로 가중치를 주는 방식인데,
원본 알고리즘이 ANIMA 를 공식 지원하지 않아 일부 노드에서 오류가 났다. 그것을 고친 것이다.

- 연결 위치: **확산 모델 로드에서 뽑아 로라 스태커 앞**에 붙인다 (기본값만으로 동작)
- 효과: 과녁처럼 일그러지기 쉬운 부분이 제대로 원형으로, 눈·머리카락 선 처리가 선명해짐
- 비용: **약 6초 추가** *(제보자 기준)*
- 한계: 모델 성능 자체를 늘리는 게 아니라 **작가(화풍)에 따라 개선되기도 악화되기도** 한다

> ⚠️ **네 개를 다 켜지 마라.** Anima Mod Guidance · Skimmed CFG · DCW+CWM+SMC · Safe PAG 가 겹치면
> 그림이 타 버리므로 강도를 낮춰야 한다 *(작성자 답변)*.

### 곁가지 — 필름 그레인은 GLSL 셰이더 노드로 *(2026-07-31, 한 글)*

포토샵 같은 별도 프로그램으로 색보정하지 않고 ANIMA 출력에 필름 그레인을 얹는 방법이다.
Krea2 워크플로우에서는 이 노드가 KSampler **이전**에 붙어 있었는데, 글쓴이는 VAE 디코드 **뒤**로 옮겨 썼다.

```text
VAE Decode → 이미지 선명화(DCW) → Film Grain(GLSL) → Save Image
```

| uniform | 뜻 |
|---|---|
| `u_float0` | grain amount (0.0~1.0, 보통 **0.2~0.8**) |
| `u_float1` | grain size (0.3~3.0, **낮을수록 고운 입자**) |
| `u_float2` | color amount (**0 = 흑백 그레인 / 1 = RGB 그레인**) |
| `u_float3` | luminance bias (**0 = 균일 / 1 = 어두운 부분에만**) |
| `u_int0` | noise mode (**0 = smooth 보간 / 1 = grainy 순수 해시 노이즈**) |

내부적으로 PCG 해시로 난수를 만들어 4회 평균으로 가우시안에 근사시키고, Rec.709 휘도로 밝은 부분의 그레인을 줄인다.

> **효과는 크지 않다** — Anima baseV10 에서 동일 프롬프트로 적용 전/후를 비교한 결과는
> *"엄청 자세히 봐야 아주 미세하게 필터처럼 덧씌워진 게 보이는"* 정도로, Krea 특유의 색감이 살짝 얹히는 느낌이다.

*(같은 글 댓글에서 쓴 로라를 밝혔다 — `rdbt` 0.5~1.0, `betabee` 0.5, `IREADING` 0.6, 전부 CivitAI. 작가 태그로 피부 질감을 다듬었다.)*

<small>근거 — [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463) · [Anima용 디테일 개선 노드 만들어왔습니다. (Comfy … 26.07](https://arca.live/b/aiart/175940996) · [Anima로 이미지 선명화와 GLSL 셰이더 26.07](https://arca.live/b/aiart/178612795)</small>

## 터보(고속) 로라 3종 실측
<small>2026-07 기준 · 근거 1건</small>

터보(고속) 로라는 스텝과 CFG 를 낮춰도 그림이 나오게 해 주는 가속용 로라다.
같은 시드·프롬프트·워크플로우에서 3종을 잰 실측이 있다 *(2026-07, ComfyUI 0.26.0, ANIMA base 1.0, 1차 K샘플러 시간만)*.

| 조건 | rdbt v0.39.b | Cosmos-Predict2.5 distilled | **공식 anima-turbo-lora-v0.2** |
|---|---|---|---|
| 로라 0.5 / CFG 2 / 16스텝 | 8.22초 | 8.57초 | 8.17초 |
| 로라 0.5 / CFG 2 / 8스텝 | 4.07초 | 3.96초 | 4.69초 |
| 로라 1.0 / CFG 1 / 8스텝 | **2.92초** | 3.19초 | 3.16초 |
| 로라 1.0 / CFG 1 / 12스텝 | | | 3.11초 |

기준선: **로라 없이 CFG 5 · 30스텝 = 13.29~13.34초**, 참고로 로라 없이 CFG 2 · 8스텝만 낮추면 4.16초.

**품질 결론** — 공식 터보 로라가 **가장 양호**하고, RDBT 는 구도는 잘 유지하지만 **화풍 유지에 애로**가 있으며,
Cosmos Predict 는 아니마 전용이 아닌데도 의외로 선방한다.

⚠️ **CFG 1 이 되면 네거티브 프롬프트가 죽어 그림이 딴판이 된다.** 로라 영향이 강해질수록 디테일도 조금씩 준다.

**화풍이 바뀐다는 점이 진짜 비용이다.**

| 유리 | 불리 |
|---|---|
| 셀 채색·만화책처럼 **선이 단순한 그림** — 터보 로라의 장점이 산다 | **작가 태그로 특정 화풍을 깎는 작업** — 신중해야 한다 |
| AI 특유의 과도한 디테일·높은 채도가 얌전해져 오히려 나아 보이는 경우 | 2.5D·반실사 지향 — 디테일이 밋밋해지고 선이 단순해짐 |

> 댓글은 **그림이 단순해지는 것은 SD 시절부터 있던 터보 로라의 특징**이므로 깔끔한 그림체를 원하면
> 오히려 써도 좋다고 정리한다.

터보 로라를 쓸 때의 노드 조합 제약(Spectrum·Layer Replay 부적합, Anima NAG 사용)은 아래 "같이 쓰면 안 되는 조합" 절에 있다.

<small>근거 — [ANIMA 터보 로라 3종 테스트. 26.07](https://arca.live/b/aiart/175962147)</small>

## 디테일러 로라 — 비교 조건과 함정
<small>2026-06 기준 · 근거 1건 · **근거 약함**</small>

디테일러 로라는 그림의 **세부 묘사·질감을 끌어올리는 보조 로라**다.
Civitai 좋아요 상위 5종을 같은 조건에서 비교한 글이 있다 *(2026-06)*.

**공통 세팅**

| 항목 | 값 |
|---|---|
| 해상도 | `840x1256` |
| 스텝 | 고속 로라 **8스텝** |
| CFG | **1** |
| 샘플러 / 스케쥴러 | `er_sde` / `simple` |
| 로라 강도 | **1.0** |

비교 대상: `anima-base-1-masterpiece-v51` · `gpt-image-2_anima-base1_v1-1` ·
`rendering_detailer_base10-000400` · `background_detailer_v1-step00000200` · `anima_context_detailer_base10`

> ⚠️ **따봉 수를 품질 지표로 믿지 마라** *(댓글)*. 1번 로라(anima-base-1-masterpiece)의 좋아요가 압도적으로 보이는 이유는
> **XL 용으로 나오던 이전 버전 로라들의 좋아요가 합산된 수치**이기 때문이다.

본문에는 `[Style] / [Environment] / [Subject] / [Elements] / [Lighting] / [Technical]` 로 섹션을 나눈
**ANIMA 식 긴 자연어 프롬프트와 그 한국어 번역**이 함께 실려 있어, 자연어 프롬프트 구성법을 배우기에도 좋다.

*이 글은 로라 간 우열을 결론짓지 않았다 — 비교 조건과 함정만 정리된 상태다.*

<small>근거 — [아니마 디테일러 로라 5종 간단 비교 26.06](https://arca.live/b/aiart/175333518)</small>

## 같이 쓰면 안 되는 조합
<small>2026-07 기준 · 근거 14건</small>

| A | B | 결과 |
|---|---|---|
| Spectrum | **ancestral(euler a)·sde 샘플러, karras 스케줄러** | 호환 안 됨 |
| Spectrum | Anima Artist Mixer | **노이즈만 나옴** → `ruwwww/comfyui-spectrum-sdxl` 의 모델 패치형을 쓰면 함께 동작 |
| Spectrum·Layer Replay | **터보(고속) 로라** | 부적합. **터보 로라를 쓰면 Anima NAG 를, 안 쓰면 정반대로 Spectrum 을 쓰고 NAG 를 뺀다** |
| ComfyUI-SPEED | euler 계열 아닌 샘플러 | 노이즈 재주입 구조라 euler 계열에서만 정상 동작 |
| Sampler SPEED | Spectrum Adaptive Forecaster | latent 크기가 동적으로 변해 에러가 날 수 있다 *(댓글)* |
| cfg 리스케일 | CWM · SMC | **켜면 CWM 과 SMC 가 비활성화된다** |
| 퀄리티 보정 노드 여럿 | 서로 | Anima Mod Guidance · Skimmed CFG · DCW+CWM+SMC · Safe PAG 를 겹치면 **그림이 탄다** |
| 터보(CFG 1) | Skimmed CFG | 네거가 거의 무시되므로 **의미가 없다** |
| block compile | fp16 accumulation | 동시 사용이 안 되는 것 같다는 보고 *(댓글, 미확인)* |

**SPEED vs Spectrum 은 스텝 수에 따라 역전된다:**
30스텝에서는 SPEED 7초 / Spectrum 10초인데, **50스텝에서는 13초 / 12초로 뒤집힌다** (2건).

**고속화 로라는 화풍 열화와 AI 느낌 증가가 숙명이다** *(댓글)* — 자세한 실측은 "터보 로라" 절 참조.

### 뒤에 밝혀진 두 가지 (2026-07)

| A | B | 결과 |
|---|---|---|
| **KJNodes `Scheduled CFG Guidance`** | **cfg pp 계열 샘플러** | ⚠️ **그림이 탄다.** 그 노드는 일부 구간만 CFG 를 적용하고 나머지를 1 로 돌리는 방식이라, CFG 를 건드리는 노드가 여럿이면 충돌한다. `end_percent` 를 1.00 으로 되돌리면 멀쩡해지지만 그러면 쓰는 의미가 없다 |
| 챈산 디테일 개선(PAG) 노드 | 다른 보정 노드 · `scale 1` | 그림이 탄다. **약하게만 쓴다** — 켜면 매번 7~10초가 더 걸리고(PAG 특성상 50~60% 증가) 색감이 전반적으로 밝아지며, 강도를 70% 이상 주면 역광 아웃라인이 생긴다 |

⚠️ 위 "int8 양자화로 SDXL 만큼" 절은 가속 조합의 일부로 `Scheduled CFG(end 0.6)` 를 권하는데,
**그 권장은 cfg pp 계열 샘플러를 쓰지 않는 경우에 한한다.**


<small>근거 — [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463) · [Anima용 디테일 개선 노드 만들어왔습니다. (Comfy … 26.07](https://arca.live/b/aiart/175940996) · [(모델공유) Anitional-v1.0-int8c (병합모델) 26.07](https://arca.live/b/aiart/178360790) · [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670)</small>

??? note "근거 14건 전부 보기"
    [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463) · [Anima용 디테일 개선 노드 만들어왔습니다. (Comfy … 26.07](https://arca.live/b/aiart/175940996) · [(모델공유) Anitional-v1.0-int8c (병합모델) 26.07](https://arca.live/b/aiart/178360790) · [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [Anima에서 작가 태그 혼합을 도와주는 커스텀 노드 제작함… 26.05](https://arca.live/b/aiart/171947113) · [로컬 comfyui 찍먹해보기 - Spectrum 가속 26.05](https://arca.live/b/aiart/171935194) · [아티스트 태그를 섞는 Anima Artist Mixer 노드 26.05](https://arca.live/b/aiart/172080673) · [Anima 샘플링 속도 개선 SPEED 커스텀 노드 26.05](https://arca.live/b/aiart/171255449) · [아니마만을 위한 아니마를 위한 아니마 전용 노드들 26.05](https://arca.live/b/aiart/171378660) · [뉴비의 아니마 워크플로우 공유 (2) 26.05](https://arca.live/b/aiart/172332889) · [ANIMA 터보 로라 3종 테스트. 26.07](https://arca.live/b/aiart/175962147) · [아니마 5070 ti 1024x1280 기준 약 10초 내외… 26.05](https://arca.live/b/aiart/171745858) · [첸럼발 아니마 디테일 개선 노드 후기 26.07](https://arca.live/b/aiart/175950158)

## 워크플로우와 버전
<small>2026-06 기준 · 근거 12건</small>

**All in One V5 / V5.1 (2026-06) 이 기준판**이다. 그 이전 preview3 시절 판들은
**작성자 스스로 낡았다고 철회**했다 (4건).

**포터블 버전을 가린다** (2건):
```
0.20.0 미만  →  sam3 노드 미지원
0.20.1       →  권장
0.21.0 이상  →  node2.0 문제로 UI 가 깨질 수 있음
```

**EasyUseAnima 는 릴리스가 아니라 git(main 브랜치)** 으로 설치해야 한다.
수정이 main 에 먼저 올라가서, 릴리스를 받으면 인풋 소켓 누락 같은 버그가 남아 있다 (2건).

*(참고)* v2 구조는 `생성 → SeedVR2 1차 업스케일 → SAM3 디텍터 디테일러 → USDU 2차 업스케일` 이었다.

---

**철회된 v4 를 만났을 때** *(2026-05)* — 인페인팅을 추가한 판이지만 **본문 상단에 스스로 실험적이라
일부가 정상 작동하지 않는다고 적고 최신 안정 버전을 쓰라고 안내**한다. 그래도 v4 를 열게 됐다면:

- 인페인팅은 block 설정이 있으면 실행이 그 단계에서 **멈추는 구조**다. ① 멈추지 않고 다 뽑은 뒤 잘 나온 이미지를 같은 시드로 다시 불러오거나 ② 멈춘 상태에서 마스킹하고 재실행 — 둘 중 고른다
- 프롬프트는 `1+2+3+4` 구조이고 인페인트 시에는 **3번만** 새로 쓰게 만들어져 있다
- 긍정 프롬에 `(@sushispin:0.8)` 같은 **작가 태그가 계속 고정돼 나오는 것은 로라 프리셋이 1번 자리를 채우고 있기 때문**이다.
  `profile select` 를 1로 바꾸거나, `get_style_TEXT` 노드와 `positive_1` 의 연결을 끊고 직접 편집한다
  (**`positive_1` 이 회색이면 그 값을 안 쓰고 연결된 다른 text 노드 값을 받는다는 뜻**)
- `comfyui-lora-manager` / `comfyui-naia-bridge` / `comfyui-spectrum-ksampler` 는 매니저의 *누락 노드 설치* 로 해결되지 않는다.
  워크플로우 왼쪽 readme 를 읽고 따로 설치할 것
- `Fast Groups Bypasser (rgthree)` 누락 경고는 rgthree 가 아니라 **ComfyUI 매니저 버전 문제**일 가능성이 크다

---

**편집기형 워크플로우** *(2026-06)* — 노드 배치 대신 편집기 한 곳에서 프롬프트를 섹션으로 나눠 관리하는 배포판도 있다.
`== ` 로 프리셋 전개 / `__` 로 와일드카드 / `%%내용%%` 로 자동 번역 / `[P]프롬프트[P]` 묶음 문법을 쓴다.

> ⚠️ **전제 조건이 특이하다.** 설치·세팅에 **Codex·Claude Code 같은 파일 편집 AI 코딩 에이전트가 필요**하고
> 작성자도 안정성을 보장하지 못한다고 밝혔다. 이후 *"대대적으로 손보는 중"* 이라는 답이 달려
> **배포 링크가 죽었을 가능성이 높다.**

---

**All in One v3 도 제작자가 철회했다** *(2026-05)*. 본문 맨 앞에 경고가 붙어 있다 —
*"ANIMA preview 3 시절에 만들어져 Anima 라는 DiT 모델에 가능한 신기술이 반영되지 않았고
SDXL 시절 노드를 그대로 써서 비효율적인 부분이 많으니 최신 안정 버전을 쓰라."*
아카 서버가 죽으면 `https://civitai.com/models/2613172/anima-all-in-one-workflow` 에서 받는다.

**그래도 v3 계열을 열게 됐다면 — 샘플러 교체는 '뮤트' 여야 한다**

> 서브그래프를 열면 일반 KSampler 와 특수 버전(SpectrumKSampler)이 함께 들어 있다.
> **하나를 켜고 하나는 반드시 '뮤트(음소거)' 한 뒤** 잠재데이터를 VAE 디코드로 연결한다.
> **건너뛰기(우회/bypass)가 아니다 — bypass 로 하면 샘플러가 두 번 돌아간다.**
> ComfyUI 특성상 서브그래프 내부를 Switch 로 통제할 수 없어 수동이다.

**SpectrumKSampler 는 BF16 미지원 그래픽카드에서 쓸 수 없다** → 일반 KSampler 로 바꾼다
(튜링 세대 대응은 이 문서의 "가속 — 무엇이 얼마나" 절과 같은 이야기다).

**NAIA 를 붙일 때** *(v3 에서 추가된 기능)*

```text
ComfyUI\user\__manager\config.ini  →  security_level = weak
설치 중 파이썬 오류 : NAIA2.0\venv 폴더를 통째로 지우고  py -3.12 -m venv venv  로 재설치
NAIA 쪽 설정        : NAI 가 아니라 '컴피' 로 설정하고 아니마로 맞춘 뒤 검색을 끝내면 준비 완료
```

> **가장 중요한 사용 원칙 — NAIA 에서 작가 태그와 퀄리티 태그를 싹 빼고 가져와야 한다.**
> 워크플로우에서 NAIA 프롬은 긍정3 자리에 들어가고 **작가·퀄리티는 워크플로우 쪽에서 따로 붙기** 때문이다.

NAIA 를 켜 둔 채 컴피에서 생성 버튼만 누르면 알아서 랜덤 프롬으로 뽑히고 큐를 100개씩 넣어도 굴러가며,
워크플로우와 결과물 양쪽에 프롬프트가 남아 재현이 된다.
**참고로 ANIMA 는 모델 이름이고 NAIA 는 프롬프트 작성용 프로그램이다** — 이름이 비슷해 자주 혼동된다.

*잔팁 (댓글)* — latent 이미지 사이즈는 `rgthree` 나 `kjnodes` 의 **프리셋 선택식 노드**를 쓰는 편이 좋고
kjnodes 는 사용자 커스텀 프리셋도 지원한다.

### 워크플로우를 받아 노드를 다 깔았는데도 안 될 때 (2026-05)

**미설치 노드 중 SAM 계열은 노드만 깔린다고 되는 것이 아니라 SAM 모델 파일을 직접 받아 넣어야 한다.**
매니저의 '누락 노드 설치' 로 초록불이 떴는데도 실행이 멈춘다면 여기를 본다.

같은 글의 속도 실측 — **터보 LoRA + 업스케일까지 포함해 600x800 시작 기준 RTX 5070 Ti 에서 약 15초, 디테일러까지 쓰면 약 30초.**
CFG 는 `1.0` 인데, **터보/고속 LoRA 를 쓰면 CFG 1.0 근처가 정상이다.**

<small>근거 — [바보멍청이를 위한 아니마 워크플로우 26.06](https://arca.live/b/aiart/174818684) · [ANIMA Easy Use workflow v1: 복잡한 워… 26.07](https://arca.live/b/aiart/175755179) · [초보자를 위한 초보자의 ANIMA 워크플로우 26.04](https://arca.live/b/aiart/168821026) · [ANIMA All in One 워크플로우 v5: i2i와 인… 26.05](https://arca.live/b/aiart/171941799)</small>

??? note "근거 12건 전부 보기"
    [바보멍청이를 위한 아니마 워크플로우 26.06](https://arca.live/b/aiart/174818684) · [ANIMA Easy Use workflow v1: 복잡한 워… 26.07](https://arca.live/b/aiart/175755179) · [초보자를 위한 초보자의 ANIMA 워크플로우 26.04](https://arca.live/b/aiart/168821026) · [ANIMA All in One 워크플로우 v5: i2i와 인… 26.05](https://arca.live/b/aiart/171941799) · [초보자를 위한 ANIMA All in One 워크플로우 v2 26.05](https://arca.live/b/aiart/169548769) · [ANIMA All in One 워크플로우 v5.1: 오류 수… 26.06](https://arca.live/b/aiart/172676286) · [ANIMA All in One 워크플로우 v4: 인페이팅 추가 26.05](https://arca.live/b/aiart/170572804) · [EasyUseAnima 0.5.5: 해상도와 자동완성 편의성… 26.07](https://arca.live/b/aiart/177930483) · [ANIMA All in One 워크플로우 v3: NAIA 추가 26.05](https://arca.live/b/aiart/169978553) · [초보자의 초보자를 위한 ANIMA all in one 워크플… 26.04](https://arca.live/b/aiart/169127262) · [뉴비의 아니마 워크플로우 공유 26.05](https://arca.live/b/aiart/170889404) · [EasyUseAnima 0.2.0: 다양한 편의성 노드와 리… 26.06](https://arca.live/b/aiart/175458978)

## EasyUseAnima — 커스텀 노드팩 하나로 끝내기
<small>2026-07 기준 · 근거 8건 · 자료 엇갈림</small>

`ComfyUI-EasyUseAnima` 는 ANIMA 용 기능을 한 노드팩에 몰아넣은 것이고, 위의 Easy Use 워크플로우가 이것 위에 얹혀 있다. **버전이 빠르게 오르고 릴리스와 git 이 어긋나므로 설치 방법부터 정해져 있다.**

```text
https://github.com/n0va39/ComfyUI-EasyUseAnima      문서 README.ko.md
```

| | |
|---|---|
| **설치** | **릴리스가 아니라 GIT(main 브랜치)으로** 받는다. 수정이 main 에 먼저 올라가 릴리스에는 인풋 소켓 누락 같은 버그가 남는다 |
| **쓸 버전** | **0.5.2 이상** (와일드카드 버그를 고친 **0.5.3** 이 그다음). 0.4.0 을 소개한 글도 본문 하단에서 *"0.5.2 를 쓰라"* 로 끝난다 |

### 기능 일곱 갈래 (0.2.3 기준 총정리)

| 갈래 | 내용 |
|---|---|
| **자동완성** | 한국어 단어 제안 지원. 적용 범위를 전용 노드로 제한하거나 끌 수 있다. 전용 노드는 미리보기를 지원하는 대신 검색 제안이 **일치 검색**으로 바뀐다 |
| **프롬프트 교정** | `Anima 프롬프트 교정기 Simple` 이 순서 교정·쉼표 오타 교정을 하고 태그 DB 로 캐릭터·작품 태그를 자동 감지한다. `Anima 프롬프트 스튜디오 고급` 은 ANIMA mod guidance 를 쓸 때 Boolean 값과 퀄리티 태그를 따로 내보낼 수 있다 |
| **NAIA 연동** | 호출과 해상도를 직접 받고, 받은 결과를 워크플로우에 저장하면 **NAIA 2.0 이 없어도 같은 프롬프트로 재현**된다. 설정에서 'NAIA 포터블 설정을 사용' 을 켜는 것이 권장된다 |
| **와일드카드** | 임팩트팩 문법 + 순차(sequential) 모드 |
| **LoRA 프리셋** | 프롬프트 자리에 작가 태그를 넣고 아래에서 LoRA 를 설정하면 각각 스타일 프롬프트와 LoRA 스택으로 출력된다. 트리 구조·리스트 방식 둘 다 지원하고 이름만 표기할지 상대 경로 전체를 표기할지, 가중치 조절 민감도까지 옵션이다 |
| **호환성 노드** | `Anima 디테일러 정렬 Hook` · `Anima 이미지 유효 배율 확대` (아래 32배수 항목) |
| **AiO 노드** | `Anima AiO Generator` · `Easy Use Anima Input`. 0.4.0 에서 **프로필 저장·불러오기**가 들어갔다 |

```text
와일드카드 경로  user\__easyuse_anima\wildcards      (다른 경로 추가 가능)
프로필 경로      user\__easyuse_anima\profiles
```

### 왜 32배수인가

**해상도 프리셋이 가로·세로를 32배수로 맞추는 것은 16채널 VAE 와 여러 DiT 최적화 기법과의 호환성 때문**이다.
같은 이유로 호환성 노드 둘이 있다.

| 노드 | 하는 일 |
|---|---|
| `Anima 디테일러 정렬 Hook` | 임팩트팩 디테일러의 이미지 **crop 을 32배수로 조절**해 Spectrum 등 최적화 노드에서 나는 크기 오류를 막는다 |
| `Anima 이미지 유효 배율 확대` | 확대 시 가로·세로를 32배수에 맞추면서 **설정한 배율에 최대한 근접**한 값을 쓴다 |

All in One V5 의 "highres 해상도는 32배수" 제약과 같은 뿌리다.

### 와일드카드 — 입력란이 안 보인다

가장 자주 나오는 질문의 답이다.

> **워크플로우에 와카 입력 목록란이 따로 보이지 않는다. 프롬프트 칸에 언더바 두 개(`__`)를 치면 자동완성이 뜬다.**

자동완성으로 태그를 넣을 때 **쉼표 뒤에 한 칸을 띄우는 옵션**(`1girl, ` 형태)은 설정창에 이미 있다.
와일드카드만 따로 뽑아 보려면 **'와일드카드' 단독 노드**를 쓰고,
프롬프트 데이터의 각 항목은 context 노드처럼 dict 를 반환하는 전용 노드나 v1 노드로 나눠 받는다.

### NAIA FILL — 켜면 덮어쓴다

| FILL | 동작 |
|---|---|
| **OFF** | NAIA 로 받은 출력을 **수동으로 조절할 수 있다** |
| ON | 받은 값으로 **무조건 덮어쓴다** |

'일반 태그 자동 토글' 로 원클릭 수동/자동 전환이 된다.

### ⚠️ 프롬프트 스튜디오에 `<lora:...>` 를 넣으면 안 먹는다

> **일반 태그 칸에 `<lora:~~~:1>` 형태나 캐릭터 로라 프롬프트가 든 와일드카드를 쓰면 로라가 적용되지 않는다.**
> ComfyUI 특성상 프롬프트 스튜디오에서는 불가능하므로, **다른 로라 노드를 쓰거나
> 텍스트를 string 관련 노드로 처리해 로라 노드로 보내야** 한다.

로라 트리거워드를 골라 넣고 싶으면 **로라 스태커를 2개 두고 하나만 트리거 출력을 프롬프트 스튜디오에 연결**한다.

### Artist Mix (0.2.1~) — exact 를 쓰면 가속을 포기해야 한다

여러 작가 태그의 그림체를 섞는 컨디셔닝 노드이고 모드가 셋이다.

| 모드 | 평가 |
|---|---|
| **exact** | **퀄리티 차이가 압도적** — *"믹싱 노드를 쓸 거면 느려도 exact 를 쓸 수밖에 없어 보인다"* (작성자) |
| average / off | — |

> ⚠️ **exact 에는 Spectrum 가속을 적용할 수 없고, 섞는 작가 수가 늘면 비용이 선형으로 늘어난다.**

ANIMA 에서 작가 태그가 왜 잘 안 섞이는지의 구조적 이유는 [프롬프트 쓰는 법](prompting.md) 의
"작가 태그 섞기" 항목에 있다.

### Spectrum 과 함께 쓰려면 브랜치를 받아야 한다

```bash
git clone -b codex/dit-spectrum-advanced-compat --single-branch \
  https://github.com/n0va39/ComfyUI-Spectrum-KSampler.git
```

PR 이 머지되기 전까지는 이 브랜치로 설치하고 **compat policy 를 '레거시' 가 아닌 값으로** 바꾼다.
예시 워크플로우 기준 **일반 71초 → spectrum 43초**.

### 알려진 버그

| 증상 | 상태 |
|---|---|
| 업스케일 모델 목록이 생성기 상세설정창에서 초기값만 뜸 / SAM3 체크포인트 선택 문제 | **0.5.2 에서 수정** |
| 프롬프트 스튜디오 고급으로 실행을 여러 개 걸면 와일드카드 시드가 첫 번째 값으로 고정 | **0.5.2 에서 수정** |
| 큐 다중 실행 시 와일드카드 시드 버그 | 0.5.2 에서 수정했다고 릴리스 노트에 적혔으나 **아래를 볼 것** |
| **생성 프로필 저장 시 `프로필 작업 실패: prompt() is not supported`** | **미해결.** ComfyUI 0.27.0 + EasyUseAnima 0.5.2/0.5.3 + SpectrumKSampler 2.7.0(**데스크톱판**) 조합에서 재현되며 오류창이 뜬 뒤로는 프롬프트 수정이 안 된다 |

> ### ⚠️ 0.5.2 릴리스 노트의 "와일드카드 시드 버그 수정" 은 반쪽이었다
>
> **본문은 고쳤다고 적었지만 '재현' 모드는 여전히 깨져 있었다** *(댓글)*.
> 일반 채우기/고정에서 **'재현' 으로 바꾸면 와일드카드 제목이나 `{내용|내용|내용}` 이
> 치환되지 않고 글자 그대로 출력**됐다.
>
> 작성자가 원인을 **"임팩트팩 와카 출력부의 편집 결과를 프롬프트 스튜디오에 그대로 넣어서 꼬인 것 —
> 프롬프트 스튜디오는 노드에 출력 미리보기가 없어 재현이 동작하지 않는다"** 로 특정하고 수정본을 따로 올렸다.
>
> **정리된 동작 규칙** — 프롬프트 스튜디오는 **시드로만 제어**하며 순차 모드와 일반 모드 두 가지뿐이고,
> 이전 결과를 원하면 **'이전 시드'** 기능을 쓴다. 와카 시드는 **'생성 후 제어'** 라서 실행하면
> 현재 입력된 값이 들어가고 표시값이 바뀐다 — 저장된 워크플로우를 불러오면 고정 시드로 재현되게 의도한 것이다.

### 맥에서 `triton no module` 로 막힐 때

맥에는 triton 을 설치할 수 없다.

```text
AiO Generator 설정의 [...] 과 톱니 아이콘  →  최적화 전부 끄기 + 스펙트럼 끄기
실제 해결 사례                             →  Mod Guidance 의 prompt_data 프로필을 off
```

### 인페인팅

Preview Bridge 로 block 하는 방식과 저장 후 불러오는 방식 **둘 다 되고**, 캐싱이 안 깨지게 해 놔서
워크플로우에서 바로 재실행해도 인페인팅까지 끝난다. **단 외부 이미지를 넣어 인페인팅하는 기능은 없다.**

*(2026-06 ~ 2026-07. 다섯 편의 릴리스 노트·총정리 글에서 모았다. 최적화 옵션 기본값이 대부분 꺼져 있는 것은
호환성 문제를 겪는 뉴비를 막으려는 것이며 AiO 노드 상세설정에서 켤 수 있다.)*

### 1.1.0 (2026-08-12) — 프롬프트 로라 태그와 **AiO Hook API**

| 더해진 것 | |
|---|---|
| **A1111 / LoraManager 방식 로라 태그** | `Prompt Studio Advanced V2` 가 프롬프트 안의 **`<lora:이름:강도>`** 를 인식한다. 와일드카드를 펼친 뒤 로라 태그를 찾아 Prompt Data 에 저장하고 `Anima AiO Generator` 가 자동 적용하므로, **와일드카드 파일에서 나온 로라도 같은 실행에서 바로 적용**된다. 적용 순서는 **기존 `LORA_STACK` 이 먼저**이고 프롬프트에서 가져온 로라가 뒤에 원래 순서대로 붙는다. AiO 는 구조화된 로라만 적용하며 positive prompt 의 생 텍스트를 임의로 재해석하지 않는다 |
| `Anima Prompt Studio Advanced LoRA` / `Anima Wildcard LoRA` | 기존 노드에 `LORA_STACK` 입출력을 붙인 판. 로라 입력칸에 **`<:` 또는 `<<:`** 를 치면 설치된 로라가 자동완성되고, 고르면 닫는 태그까지 완성되며 strength 부분이 바로 선택된다 |
| **AiO Hook v1** | 다른 커스텀노드가 `Anima AiO Generator` 에 기능을 끼워 넣는 **공개 Hook API** ↓ |

```text
aio_hook 소켓으로 연결한다

first pass       MODEL 교체
                 steps · cfg · sampler · scheduler · denoise 덮어쓰기
postprocess      전/후 훅 — 이미지 보정 · 메타데이터 추가 · 프리뷰 출력
여러 훅 조합 가능

v1 에서 열지 않은 것 : conditioning · latent · 저장 동작 · 샘플링 백엔드 전체 교체
```

**버그 수정** — `Prompt Corrector` 와 `Prompt Builder` 가 `Prompt Studio` 의 자동완성 데이터를 함께 쓰도록 고쳐
캐릭터/작품 태그가 `unknown` 으로 뜨거나 artist 뒤로 잘못 정렬되던 문제, artist validation 을 꺼 둔 상태에서
명시적으로 넣은 `@artist` 태그가 `unknown` 으로 표시되던 문제를 해결했다.
프로필이 지정 폴더 밖으로 새던 문제, 한 워크플로우 실행이 다른 워크플로우의 시드 시퀀스까지 진행시키던 문제,
한 번의 queue 에서 필드마다 다른 와일드카드 결과를 받던 문제도 고쳤다.
**기존 워크플로우·노드 식별자·설정·소켓 순서는 그대로 호환된다.**

### 1.1.1 (2026-08-12) — 2.9B 지원과 그 밖에

- **별도 커스텀노드 없이 40블록(2.9B) 모델을 직접 로드**한다 (위 'ANIMA 2.9B' 절)
- `AiO Upscale` 에서 **FlashAttention 이 켜져 있어 USDU 오류가 나는 경우를 감지**해 ComfyUI 또는 KJNodes 의 어떤 설정을 꺼야 하는지 안내한다 *(1.1.0 시점에는 스크립트에서 해당 오류 호출을 주석 처리하고 쓴다는 제보가 있었다)*
- `Mod Guidance` 를 쓰려면 **`ComfyUI-Spectrum-KSampler` 포크**를 쓰라고 안내한다
- 업데이트 후에는 **ComfyUI 재시작 + 브라우저 강력 새로고침**을 권한다

> ⚠️ **미해결 버그** — 와일드카드 파일의 내용이 `@111` 같은 짧은 단어면 정상 작동하지만,
> `1girl, sweat, messy hair, A girl in a school uniform is holding a phone ...` 처럼
> **danbooru 태그 + 자연어로 된 긴 내용은 프롬프트에 적용되지 않는다.**

<small>근거 — [ANIMA Easy Use workflow v1: 복잡한 워… 26.07](https://arca.live/b/aiart/175755179) · [EasyUseAnima 0.2.3: 기능 총정리 26.07](https://arca.live/b/aiart/175754499) · [EasyUseAnima 0.5.2: 디테일러 설정, 와카 시… 26.07](https://arca.live/b/aiart/177337756) · [EasyUseAnima 0.4.0: AiO 생성기 프리셋 기… 26.07](https://arca.live/b/aiart/176677452)</small>

??? note "근거 8건 전부 보기"
    [ANIMA Easy Use workflow v1: 복잡한 워… 26.07](https://arca.live/b/aiart/175755179) · [EasyUseAnima 0.2.3: 기능 총정리 26.07](https://arca.live/b/aiart/175754499) · [EasyUseAnima 0.5.2: 디테일러 설정, 와카 시… 26.07](https://arca.live/b/aiart/177337756) · [EasyUseAnima 0.4.0: AiO 생성기 프리셋 기… 26.07](https://arca.live/b/aiart/176677452) · [EasyUseAnima 0.2.1: Artist Mix와 s… 26.07](https://arca.live/b/aiart/175613721) · [EasyUseAnima 1.1.0: Webui(A1111) … 26.08](https://arca.live/b/aiart/179713666) · [EasyUseAnima 1.1.1: ANIMA 2.9B 지원… 26.08](https://arca.live/b/aiart/179735645) · [EasyUseAnima 0.1.9 와카 추가 26.06](https://arca.live/b/aiart/175389876)

## 워크플로우 없이 아니마 쓰기 — 래핑 도구 셋
<small>2026-08 기준 · 근거 3건</small>

ComfyUI 의 노드 그래프 자체가 입문자에게 가장 큰 벽이다. **그 단계를 통째로 건너뛰고 Anima 만 쓰게 해 주는 도구가 셋** 나와 있다. 셋 다 성격이 다르다.

| | **PeroPixfy** | **anima-studio** | **iOS 앱** |
|---|---|---|---|
| 무엇인가 | ComfyUI 안에 설치하는 **플러그인** | ComfyUI 를 통째로 감싼 **데스크톱 프로그램** | 아이폰·아이패드 앱 |
| ComfyUI 가 필요한가 | **필요하다** (포터블) | **아니다** — 자체적으로 설치해 함께 실행한다 | 아니다 |
| 시점 | 2026-06 | 2026-08 | 2026-07 |

### PeroPixfy — ComfyUI 사이드바에 붙는다

```text
릴리즈    https://github.com/mrm987/PeroPixfy/releases/latest
설치      peropixfy_install.bat 과 peropixfy_update.bat 를 ComfyUI 포터블 폴더에 넣고 install 실행
전제      ComfyUI 포터블  https://docs.comfy.org/ko/installation/comfyui_portable_windows
```

> ⚠️ **포터블 기준으로 만들어져 임베디드 파이썬 폴더가 있어야 한다** — `comfyui easy install` 같은
> 다른 설치본에서는 안 될 수 있다 *(댓글)*.

설치되면 왼쪽 사이드바에 아이콘이 생기고, 클릭하면 **ComfyUI 화면 전체를 덮는 새 UI** 가 나와
NovelAI 쓰듯 프롬프트만 바꿔 가며 뽑을 수 있다. Anima 모델이 없으면 첫 실행 때 다운받기 버튼이 뜬다.
**t2i / i2i / 인페인트 / hires fix** 를 지원한다. 아니마 모델만 지원한다.

**가장 값어치 있는 기능은 로라 매니저다.**

- 켤 때마다 또는 `Scan` 을 누르면 **로컬의 미등록 로라를 civitai 에서 자동 검색**해 썸네일·베이스모델·트리거워드를 등록한다
- 제작자가 civitai 양식대로 안 썼으면 트리거워드가 비는데 수정 버튼으로 직접 넣으면 되고, **civitai 에 없는 자체 제작 로라도 직접 등록**해 관리할 수 있다
- 로라를 켜고 끌 때 **프롬프트에 트리거워드를 자동으로 써 준다**

> **삽입 위치에 규칙이 있다** — `@` 가 달린 태그 중 **마지막 태그 뒤**에 붙는다.
> 그래서 트리거워드나 작가태그가 하나도 없는 상태에서 추가하면 **맨 앞에 들어간다.**
> 처음에만 적절한 위치로 옮겨 주면 이후에는 그 위치 뒤에 자동으로 추가된다.

스타일 매니저에 저장해 두면 **사용한 로라 목록과 가중치까지 포함해** 같은 세팅을 불러 쓸 수 있고,
베이스 프롬프트에 슬롯별 추가 프롬프트를 더해 **같은 캐릭터로 여러 표정·체위를 한 번에** 뽑을 수 있다.
멀티 탭은 대량생산용이며 '싱글 옵션 가져오기' 로 방금 쓰던 세팅을 그대로 가져온다.
채널에 올라온 spectrum 노드가 벤더링 형태로 탑재돼 있다.

### anima-studio — ComfyUI 를 아예 안 만진다

```text
https://github.com/cstria0106/anima-studio
```

ComfyUI 와 필요한 커스텀 노드를 **자체적으로 설치해 함께 실행**해 주므로 ComfyUI 를 따로 깔거나
노드를 만질 필요가 없다(외부 ComfyUI 를 지정하는 옵션도 있으나 **제작자가 테스트해 보지 않았다**고 밝혔다).

| 기능 | |
|---|---|
| 참조 이미지 | 이미지 한 장을 로라처럼 쓰는 기능 |
| 인페인트 · 업스케일 | |
| 태그 자동완성 | 채널에 올라온 CSV 로 만들었다 |
| 모델 관리 | Anima 를 huggingface 에서 직접 받고 civitai 에서 LoRA 를 받는다 |
| 이미지 폴더 관리 | |

제작자가 혼자 쓰려고 만든 것을 공유한 것이라 지원 범위는 제한적일 수 있다.
**ComfyUI 노드 학습을 건너뛰고 바로 Anima 를 써 보기에 적합한 경로**다 → [처음이라면](overview.md)

### iOS 앱 — PC 없이

원 출처는 레딧 `https://www.reddit.com/r/StableDiffusion/comments/1uwb8lc/i_made_app_that_runs_anima_on_iphones/` 다.

| 항목 | |
|---|---|
| 기본 출력 | **4스텝 512x512** (더 높은 해상도는 업데이트 예정) |
| 최초 1회 | 모델 컴파일 **약 2분** |

**기기별 실측** *(본문 + 댓글)*

| 기기 | 장당 |
|---|---|
| iPhone 17 | **약 5~6초** |
| M1 iPad | 약 9~10초 |
| iPhone 14 | 약 10~15초 |
| iPad mini 5 (A12, 6년 된 기기) | **1~2분** |

구형 기기는 실행하자마자 '지원 안 함' 경고가 뜨지만 **그래도 진행하는 버튼이 있어 계속할 수 있다.**
즉 본문의 "1~2분" 은 6년 된 기기의 수치이고 **M1 급 이상이면 10초 안팎**이다.
**PC 없이 그림을 뽑아 보고 싶은 입문자에게 가장 진입장벽이 낮은 경로**이지만,
앱스토어 배포라 라이선스 문제가 있을 수 있다는 우려도 댓글에 나왔다.

*(셋 다 각각 한 글에서만 소개된 도구다. iOS 앱의 기기별 속도만 본문과 댓글이 함께 채웠다.)*

<small>근거 — [아니마 쉽게 뽑는툴 26.08](https://arca.live/b/aiart/179069358) · [PeroPixfy) ComfyUI에서 워크플로우 없이 아니마… 26.06](https://arca.live/b/aiart/174926997) · [아이폰용 아니마 돌린 간단 후기 26.07](https://arca.live/b/aiart/177129172)</small>

## 디테일러 — 방침이 뒤집혔다
<small>2026-06 기준 · 근거 6건 · 자료 엇갈림</small>

| 지금 | ← 예전 |
|---|---|
| **디테일러 자체가 ANIMA에 맞는 방법이 아니다.** Highres 를 먼저 하고 **눈 정도만** 디테일러를 돌린다 (3건) | 전신 → 얼굴 → 눈 순으로 돌리며, 전신 디테일러가 머리카락·손 찐빠를 잡아준다 (2건) |

**같은 작성자가 철회했다.** 옛 글을 보고 전신 디테일러부터 돌리면 헛수고다.

<small>근거 — [초보자를 위한 초보자의 ANIMA 워크플로우 26.04](https://arca.live/b/aiart/168821026) · [ANIMA All in One 워크플로우 v5.1: 오류 수… 26.06](https://arca.live/b/aiart/172676286) · [comfyUI ANIMA 그림체 및 워크플로우 공유 26.04](https://arca.live/b/aiart/168777426) · [초보자의 초보자를 위한 ANIMA all in one 워크플… 26.04](https://arca.live/b/aiart/169127262)</small>

??? note "근거 6건 전부 보기"
    [초보자를 위한 초보자의 ANIMA 워크플로우 26.04](https://arca.live/b/aiart/168821026) · [ANIMA All in One 워크플로우 v5.1: 오류 수… 26.06](https://arca.live/b/aiart/172676286) · [comfyUI ANIMA 그림체 및 워크플로우 공유 26.04](https://arca.live/b/aiart/168777426) · [초보자의 초보자를 위한 ANIMA all in one 워크플… 26.04](https://arca.live/b/aiart/169127262) · [뉴비의 아니마 워크플로우 공유 (2) 26.05](https://arca.live/b/aiart/172332889) · [ANIMA 로라 적용시 스타일이 불안정할 때 팁 26.05](https://arca.live/b/aiart/171818770)

## 해상도 임계점 — 어디까지 깡으로 뽑히나
<small>2026-07 기준 · 근거 2건</small>

공식 허용 범위는 **3MP(1536x1536)** 이지만, 실제 붕괴 지점을 1536 부터 **64씩 올려가며** 확인한 실험이 있다
*(2026-07, RTX 2070 SUPER)*.

| 구간 | 결과 |
|---|---|
| ~ **2112x2112** | DyPE 없이도 **생각보다 잘 버틴다** |
| **2560x2560** 부근부터 | 배경 디테일부터 죽고 최후에는 낙서가 된다 |

출발점이 된 추론은 *"학습 시 2048x1152 같은 와이드 버킷이 포함됐다면 위치 인코딩이 2048 이라는 좌표값을 이미 겪었을 것"* 이었다.

**DyPE 를 붙이면 해상도마다 써야 할 조합이 갈린다.**

| 목표 해상도 | 성공한 조합 |
|---|---|
| 2112x2112 | `method=vision_yarn` + **`base_resolution` 1920** (1536 도 2048 도 아니다) |
| 2112 · 2560 | `method=yarn` + `yarn_alt_scaling=True` + `base_resolution=1536` |
| 2240 · 2448 · 2656 | `method=vision_yarn` + `base_resolution=1536` |

⚠️ **교차 적용하면 품질이 폭락한다.** `vision_yarn` 으로 성공했던 해상도를 `yarn+yarn_alt_scaling` 으로 돌리면 무너진다.
**직사각형(1792x2304, 2048x3072)은 성대하게 실패**했고, 글쓴이도 왜 해상도마다 최적 method 가 갈리는지 결론을 내지 못했다.

> `Fault failed: 2` 오류의 뒤 `2` 는 **CUDA 에러 코드 2 = cudaErrorMemoryAllocation = OOM** 이다.
> ComfyUI 가 아니라 **그래픽 드라이버가 터진 것**이라 PC 재시작 후 타일 디코드로 전환해 회피했다.

DyPE 설치·`base_resolution` 값의 최신 정리는 [업스케일과 화질](upscale.md) 에 있다.

<small>근거 — [(anima) DyPE를 쓰면 깡으로 초고해상도 이미지를 뽑… 26.07](https://arca.live/b/aiart/176872950) · [(anima, 스압) 해상도 임계점 실험, DyPE 추가 실험 26.07](https://arca.live/b/aiart/177102053)</small>

## 저사양·비엔비디아 실측
<small>2026-04 기준 · 근거 3건 · **근거 약함**</small>

엔비디아 데스크톱이 아닌 환경의 실측이 두 건 있다. **둘 다 한 글에서만 언급된 수치**다.

**Intel Core Ultra 258V 노트북** — RAM 32GB 중 **16GB 를 VRAM 으로 할당**, 템플릿 위주로 추가 기능 없이 측정 *(2026-04)*.

| 모델 | 1차(모델 로드 포함) | 2차 |
|---|---|---|
| **ANIMA** | **3분 30초** | 1·2회차 차이 크지 않음 |
| **ANIMA + 고속 로라** | **55초** | **44초** |
| WAI 20스텝 | 47초 | 23초 |
| WAI 30스텝 | 48초 | 31초 |
| rin anime artflow 20스텝 | 52초 | 25초 |

Wan 은 VRAM 부족이 뻔해 생략했다. 댓글 평가는 **RTX 3060 수준이고 M4 맥미니보다 빠르며 M4 Pro 맥미니보다는 느린 정도**다.

**AMD** — RX 7000(RDNA3) 이상이면 돌아가지만 동급 엔비디아 대비 **2~3배 느리고** 호환성·트러블 이슈가 있다.
그래도 **9070XT 에서 성공했고 NAI 보다 빠르다**는 보고가 있다 *(2026-02)*.

> 채널 FAQ 의 기본 입장은 **애플 맥 비추천**이다 — `RTX 5060 8GB 가 M4 맥미니보다 대략 8배 이상 빠르다`.

그래픽카드 선택 전반은 [설치와 환경 구성](install.md) · [VRAM·속도 최적화](vram.md) 를 보라.

<small>근거 — [응애도 할 수 있는 ComfyUI Anima 로컬 아니메 이… 26.02](https://arca.live/b/aiart/163553760) · [최근 AI 그림 자주 묻는 질문 (26년 5월 기준) 26.05](https://arca.live/b/aiart/170655900) · [intel portable 벤?치마크 26.04](https://arca.live/b/aiart/168411491)</small>

## 해상도 — 1024가 아니라 768로 시작하라
<small>2026-02 기준 · 근거 6건 · 자료 엇갈림</small>

> ⚠️ **정정** — 이 문서는 오래 **1024 급 해상도(832x1216 등)를 기본값**으로 안내해 왔다.
> **초보자용 아니마+IL 워크플로우 VER.2** 작성자가 댓글에서 이유를 붙여 반박했고, 이유가 구조적이라 여기서 바로잡는다.

**ANIMA 는 대부분의 시간을 `512` 해상도에서 학습한 모델이다.** 그래서 `1024` 로 뽑지 않고
**`768` 근처에서 뽑을 때 그림이 더 잘 나온다.** 속도 이득은 덤이 아니라 절반이다.

| | `1024` | **`768`** |
|---|---|---|
| 총 픽셀 수 | `1024 x 1024 = 1,048,576` | `768 x 768 = 589,824` — **약 절반** |
| 컴퓨팅 자원 | 기준 | **절반** |
| 속도 | 기준 | **약 2배** |
| 품질 | 학습 해상도에서 먼 쪽 | **학습 비중이 몰린 쪽** |

그 워크플로우가 *"잠재 이미지 크기를 정한 뒤 다시 `0.75` 배 한다"* 는 이상한 짓을 하는 이유가 이것이다.
`1024` 계열 버킷을 고르게 해 놓고 마지막에 `0.75` 를 곱해 `768` 근처로 떨어뜨린다.

```text
1024 x 1024  x 0.75  →   768 x  768
 832 x 1216  x 0.75  →   624 x  912
1216 x  832  x 0.75  →   912 x  624
```

### ⚠️ 다른 실측은 "`1024` 가 적정" 이라고 한다 — 어긋나지 않는다

**같은 시기에 정반대로 읽히는 실측이 하나 더 있다.** 자연어 인식 테스트 글(원문 161190216, 2026-02-01)의 결론은 이것이다.

> **생성 해상도는 `1024x1024` 가 적정이며 `1536x1536` 은 찐빠가 심하다.
> 업스케일이 필요하면 Klein-4B 로 하는 것을 추천한다.**

**두 글을 다 읽으면 축이 다르다는 것이 드러난다.**

| | 768 쪽 (원문 163201876, 2026-02-24) | 1024 쪽 (원문 161190216, 2026-02-01) |
|---|---|---|
| 무엇을 잰 값인가 | **ANIMA+IL 2단 워크플로우에서 ANIMA 가 스케치를 맡는 단계**의 잠재 크기 | **ANIMA 단독 단일 패스로 최종 결과물**을 뽑을 때의 크기 |
| 뒤에 무엇이 오나 | Illustrious 가 고해상도로 마무리한다 | 없다. 그게 결과물이다 |
| 함께 쓴 것 | 고속(CFG distilled) 로라 · CFG 4 · shift 8 · `er_sde` | 없음 (샘플 워크플로우 그대로) |
| 그래서 이 값은 | **하한** — 여기서 시작해 올린다 | **상한** — 여기를 넘기면 깨진다 |
| 1536 을 재 봤나 | 안 잼 | **쟀다. 심하게 깨졌다** |
| 768 을 재 봤나 | **쟀다** | 안 잼 |

**즉 어느 쪽도 상대 값을 실제로 재 보고 부정한 것이 아니다.**
768 쪽은 1024 를 쓰지 말라는 것이 아니라 *2단 구성이면 앞단을 768 로 내려도 되고 그게 2배 빠르다*는 말이고,
1024 쪽은 768 이 나쁘다는 것이 아니라 *1024 를 넘기지 말라*는 말이다.
**둘을 합치면 ANIMA 의 실용 구간은 `768 ~ 1024` 다.**

```text
2단 구성(ANIMA → IL/업스케일)  →  ANIMA 단계는  768 근처   (빠르고 학습 비중이 몰린 곳)
ANIMA 단독 한 방                →  1024 급        (832x1216 · 1024x1024)
그보다 크게                     →  깡으로 올리지 말고 highres · 업스케일 · Klein-4B
```

### 그럼 1536 은 뭔가 — 시점이 다르다

**`1536x1536` 이 깨진다는 것은 2026-02-01 `preview` 시절 실측이다.** 그 뒤 값이 바뀌었다.

| | 값 | 시점 · 출처 |
|---|---|---|
| **공식 지원 버킷** | `512x512`(NAI1) ~ `1024x1024`(SDXL) ~ `1536x1536`(ILXL1) | 정보글 개정판 (2026-05) |
| **공식 안내상 무난한 값** | SDXL 해상도. 세로는 `832x1216` | 정보글 개정판 · 찍먹 입문글 |
| **실전 기본값(2단 구성 앞단)** | **`768` 근처** — 품질·속도 모두 유리 | VER.2 작성자 댓글 (2026-02) |
| **preview 실측 상한** | `1024x1024` 적정 / `1536x1536` 찐빠 심함 | 자연어 인식 테스트 (2026-02-01) |
| **정식판 실측 상한** | DyPE 없이도 **`2112x2112`** 까지 준수 | 해상도 임계 실험 (2026-07) |

**preview 의 `1536` 붕괴는 정식판 실측으로 대체됐다.** 지금 ANIMA 는 그보다 훨씬 위까지 버틴다.
어디까지 깡으로 버티는지는 아래 "해상도 임계점" 절에 실측이 있다.

> **정리** — **2단 구성이면 앞단을 `768` 근처에서 시작하고, ANIMA 하나로 끝낼 거면 `1024` 급을 쓴다.**
> 큰 그림이 필요하면 그 해상도로 직접 뽑지 말고 highres·업스케일(Klein-4B 등)로 올린다.
> `512` 대는 저해상도로 빠르게 뽑고 hires fix 하는 용도가 아니면 생으로 쓰지 않는다.
> 큰 해상도를 깡으로 뽑는 것은 [업스케일과 화질](upscale.md) 쪽 문제다.

### 2026-08-18 로컬 실검증 — **832는 기본값, 1024x1536은 최종 저장값**

이 PC(RTX 5070 Ti)에서 같은 시드·같은 자연어 프롬프트·같은 `er_sde`/`simple` 로 다시 비교했다.

| 해상도 | 시간 | 관찰 |
|---|---:|---|
| `832x1216` | **23.2초** | 이미 깔끔하고, 탐색용 기본값으로 충분하다 |
| `1024x1536` | **35.5초** | 머리카락 결, 배경 보케, 광원 분위기가 더 정리돼 **한 장 완성도**는 분명히 오른다 |

이 비교는 "1024가 무조건 더 낫다"는 뜻이 아니다.
다만 **ANIMA 하나로 한 장을 저장할 때**는 `1024x1536` 정도까지 올리는 실익이 실제로 있었다.
반대로 프롬프트를 갈아 보거나 여러 장을 탐색할 때는 `832x1216` 쪽이 훨씬 덜 답답했다.

- **탐색 기본값**: `832x1216`
- **최종 한 장**: `1024x1536`
- **그 이상**: 깡 생성보다 highres / 업스케일 단계로 넘기는 편이 낫다

### 2026-08-18 로컬 실검증 — **bare 설치의 latent hires 는 '되긴 되지만 안전한 기본값은 아니다'**

외부 업스케일 모델이 하나도 없는 현재 설치에서는, 바로 검증 가능한 다음 단계가
**latent upscale + 2차 KSampler** 뿐이었다. 같은 시드로 이렇게 맞붙였다.

| 경로 | 시간 | 관찰 |
|---|---:|---|
| **직출 `1024x1536`** | **36.8초** | 구도와 얼굴 방향이 비교적 안정적이었다 |
| **`832x1216 → latent upscale → 1024x1536 → 2차 KSampler 12스텝, denoise 0.5`** | **37.8초** | 돌긴 돌지만, **같은 시드라도 얼굴 방향과 구도가 크게 흔들렸다** |

즉 지금 설치 상태에서의 결론은 이렇다.

- **bare ANIMA 설치만으로도 latent hires 는 실행 가능하다**
- 하지만 **안전한 기본값**으로 둘 만큼 안정적이지는 않았다
- 그래서 **최종 한 장의 기본값은 여전히 직출 `1024x1536`**
- latent hires 는 **'다음에 실험할 수 있는 단계'** 까지로 보고,
  **정식 업그레이드 루트는 전용 업스케일 모델 / PiD / ResShift / USDU** 같은 별도 경로를 갖춘 뒤로 미루는 편이 낫다

### 2026-08-18 로컬 실검증 — **전용 업스케일 모델은 latent hires 보다 훨씬 보수적이고 안전했다**

같은 설치에서 `2x-AnimeSharpV4_RCAN.safetensors` 를 `models/upscale_models` 에 넣고,
`Load Upscale Model → Upscale Image (using Model)` 만 붙여 `1024x1536` 결과물에 태워 봤다.

| 경로 | 결과 |
|---|---|
| **직출 `1024x1536`** | 기준 이미지 |
| **`2x-AnimeSharpV4_RCAN` 업스케일** | **`2048x3072` 로 정확히 2배** 커졌고, 구도·얼굴 방향은 거의 그대로였다 |
| **bare latent hires** | 같은 시드여도 얼굴 방향과 구도가 흔들렸다 |

즉 현 시점 bare 설치의 결론은 더 선명하다.

- **직출 `1024x1536`**: 여전히 가장 안전한 기본값
- **latent hires**: 되긴 되지만, bare 상태에서는 실험용
- **전용 업스케일 모델**: **다음 단계로 실제 채택 가능한 경로**

shared models 방식이면 `extra_model_paths.yaml` 에 `upscale_models: upscale_models` 도 넣어야
ComfyUI 가 그 폴더를 본다. 이번 로컬 검증에서도 그 키가 빠져 있으면
파일이 있어도 `Load Upscale Model` 목록이 비어 있었다.

*768 권장의 근거는 원문 163201876 **한 글의 작성자 댓글**이다. 다만 근거가 취향이 아니라
'학습 해상도'와 '픽셀 수'라는 구조적인 것이고, 512 학습 비중은 정보글 개정판의 버킷 설명과도 어긋나지 않는다.*


<small>근거 — [응애도 할 수 있는 ComfyUI Anima 로컬 아니메 이… 26.02](https://arca.live/b/aiart/163553760) · [로컬 아니메 모델 Anima에 대한 잡다한 정보 개정판 26.05](https://arca.live/b/aiart/170924904) · [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [초보자용 아니마+IL 워크플로우 VER.2 26.02](https://arca.live/b/aiart/163201876)</small>

??? note "근거 6건 전부 보기"
    [응애도 할 수 있는 ComfyUI Anima 로컬 아니메 이… 26.02](https://arca.live/b/aiart/163553760) · [로컬 아니메 모델 Anima에 대한 잡다한 정보 개정판 26.05](https://arca.live/b/aiart/170924904) · [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [초보자용 아니마+IL 워크플로우 VER.2 26.02](https://arca.live/b/aiart/163201876) · [(anima) DyPE를 쓰면 깡으로 초고해상도 이미지를 뽑… 26.07](https://arca.live/b/aiart/176872950) · [Anima 모델 자연어 인식 테스트 26.02](https://arca.live/b/aiart/161190216)

## 텍스트 인코더는 CLIP 이 아니라 Qwen3 다
<small>2026-05 기준 · 근거 3건 · 자료 엇갈림</small>

ANIMA 의 텍스트 인코더는 **CLIP 이 아니다.** `Qwen3-0.6B-base` 라는 **LLM** 이다.

```text
ComfyUI/models/text_encoders/qwen_3_06b_base.safetensors
```

**`CLIP` 은 SD1.5·SDXL 시절 인코더를 가리키는 말**이라 ANIMA 에 쓰면 혼동을 부른다.
ComfyUI 의 노드 이름이 여전히 *CLIP 로드* 인 탓에 더 헷갈리는데, 그 노드가 읽는 것은 Qwen3 다.

> ⚠️ **이 설명은 틀렸다** — ANIMA 텍스트 인코더 상향 실험을 소개한 글(원문 170079773)이 본문 말미에서
> *"CLIP 모델을 상위의 것으로 바꿔보니"* 라고 요약했다. **실제로 바꾼 것은 Qwen3 계열 LLM 텍스트 인코더**다.
> 같은 글 댓글도 *"3과 3.5의 차이보다 qwen3 6b, 8b 같은 걸 써 보면 어떨지 궁금하다"* 며 LLM 인코더로 이해하고 있다.

### 반드시 순정을 써라

**튜닝되지 않은 순정 `Qwen3-0.6B-base` 를 써야 한다.** 아니면 토큰이 어긋나 타율이 떨어진다.

| 구성 요소 | 실체 |
|---|---|
| 본체 | **2B DiT + LLM 어댑터** |
| 텍스트 인코더 | **`Qwen3-0.6B-base`** (순정) |
| VAE | **Qwen-Image VAE (16채널)** |

이 구조가 앞 절들의 이유이기도 하다 — **작가·캐릭터 지식 상당 부분이 DiT 가 아니라 LLM 어댑터에 저장**돼 있어서
인코더를 갈아 끼우면 그 지식을 처음부터 다시 학습해야 한다. 실제로 개발자가
`Qwen3.5-2B-Base` 로 올리는 실험을 돌려 **기존 품질의 약 95%** 까지 갔지만 채택하지 않았다.
그 전말은 [모델 고르기](models.md) 의 "ANIMA 는 무엇 기반이고 왜 가벼운가" 항목에 있다.

용어 자체가 헷갈리면 [용어집](glossary.md) 을 보라.


<small>근거 — [응애도 할 수 있는 ComfyUI Anima 로컬 아니메 이… 26.02](https://arca.live/b/aiart/163553760) · [로컬 아니메 모델 Anima에 대한 잡다한 정보 개정판 26.05](https://arca.live/b/aiart/170924904) · [아니마와 Qwen3.5 26.05](https://arca.live/b/aiart/170079773)</small>

## VAE 고르기 — 링크 정정과 Qwen2D-VAE 의 진짜 의의
<small>2026-07 기준 · 근거 1건 · 자료 엇갈림</small>

VAE 는 잠재 이미지를 실제 픽셀로 되돌리는 부분이라 바꾸면 **색감과 미세 디테일**이 달라진다.
ANIMA 의 기본 VAE 는 `qwen_image_vae.safetensors` 다.

### 결론부터 — 차이는 사실상 밝기다

4종을 같은 조건에서 비교한 글(2026-07)의 결론이다.

| VAE | 성격 |
|---|---|
| **`qwen_image_vae`** | 기본 아니마 VAE |
| `Qwen2D-Anime-VAE` (Anzhc) | 애니 튜닝본. 커스텀 노드 `Anzhc/anzhc-qwen2d-comfyui` 설치 필수 |
| `qwenimagevae_v7` (Civitai, Liquidn2) | 프리뷰 시절엔 기본보다 맑고 깔끔했지만 **정출 이후로는 굳이 싶다** |
| `qwenjmVae_x1` (Civitai, DjM_) | 다른 VAE 대비 **어둑해 보이게** 튜닝됨 |

소매 끝단이나 옷깃 같은 사소한 디테일에서 차이가 나기도 하지만 **나란히 대보지 않으면 알 수 없는 수준**이다.

### ⚠️ 링크가 틀렸었다 — `Qwen2D-VAE` 가 아니라 `Qwen2D-Anime-VAE`

> **이 설명은 틀렸다.** 원문(178177432)은 처음에 Anzhc 의 애니 튜닝 VAE 로 **`Anzhc/Qwen2D-VAE` 를 걸었다.**
> 그것은 **영상 관련 기능만 제거한 판**이고, 진짜 애니 튜닝본은 아래쪽이다. **원글 작성자가 본문을 수정해 수용했다.**

```text
✗  https://huggingface.co/Anzhc/Qwen2D-VAE          # 영상 기능 제거판
✓  https://huggingface.co/Anzhc/Qwen2D-Anime-VAE    # 애니 튜닝본
```

### `Qwen2D-VAE` 의 진짜 의의는 화질이 아니다

그렇다고 영상 기능 제거판이 쓸모없는 것은 아니다. **쓰는 자리가 다르다.**

| | 무엇에 쓰나 |
|---|---|
| **그림 품질용** | `Qwen2D-Anime-VAE` 등 애니 튜닝본 |
| **학습 효율용** | **`Qwen2D-VAE`** — 학습 시 **latent 캐싱 속도 2배**, **VRAM 사용량 절반** |

**화질 개선이 아니라 학습 비용을 줄이는 물건**이라는 것이 댓글의 지적이다.
로라를 굽는 쪽이라면 이쪽이 훨씬 값어치가 크다 → [로라 쓰는 법](lora-usage.md)

*4종 비교와 두 정정 모두 원문 178177432 **한 글**에서 나왔다. 다만 링크 정정은 원글 작성자가 본문을 고쳐 수용한 건이다.*


<small>근거 — [아니마 VAE 4종 비교 26.07](https://arca.live/b/aiart/178177432)</small>

## highres 가 뭉개질 때 — 세팅이 아니라 로라를 의심하라
<small>2026-05 기준 · 근거 3건</small>

highres 를 걸었더니 결과가 **자글자글해지거나 뭉개진다면, 세팅을 만지기 전에 로라부터 꺼 봐라.**

원문 170922099 댓글에서 실제로 잡힌 범인은 **'아니마 디테일 트위커' 로라**였다. 그 로라를 끄니 해결됐다.

| 의심 순서 | 확인할 것 |
|---|---|
| **1** | **적용 중인 로라를 하나씩 끈다** — 특히 디테일러·디테일 트위커 계열 |
| 2 | highres 목표 해상도가 **모델 지원 해상도를 넘지 않는지** — `2048` 을 넘는 길이는 **USDU(타일 분할)** 로 처리한다 |
| 3 | highres 해상도가 **32 배수**인지 (All in One V5 제약) |

> **고해상도가 안 뽑히는 흔한 원인이 로라다.** 스타일 로라가 아닌데도 그림체에 영향을 주거나
> 의도치 않은 것이 튀어나오는 ANIMA 로라가 많다는 것은 별개의 글에서도 지적된 바다.

디테일러 자체를 언제 쓰는지는 이 문서의 "디테일러 — 방침이 뒤집혔다" 절을,
업스케일 쪽 처리는 [업스케일과 화질](upscale.md) 을 보라.

*범인 특정은 원문 170922099 **한 글의 댓글**에서만 나온 사례다. 다만 해결이 확인된 건이다.*


<small>근거 — [ANIMA All in One 워크플로우 v5: i2i와 인… 26.05](https://arca.live/b/aiart/171941799) · [Anima 로라 블럭필터 개조 26.05](https://arca.live/b/aiart/171479837) · [ANIMA All in One 워크플로우 v4.1핫픽스 26.05](https://arca.live/b/aiart/170922099)</small>

## 초보자용 아니마+IL VER.2 — 값의 근거와 오류 셋
<small>2026-02 기준 · 근거 2건</small>

입문자가 가장 많이 집어 드는 배포판이 **초보자용 아니마+IL 워크플로우 VER.2** (2026-02) 다.
이미지를 새 창에서 원본으로 받아 ComfyUI 에 드래그앤드롭하면 열린다. **VRAM 12GB 이상용과 8GB 용**이 따로 있다.

### 왜 그 값인가 (작성자 댓글)

| 항목 | 이 워크플로우 | 고속 로라 개발자 권장 |
|---|---|---|
| **CFG** | **`4`** | `1.5` |
| **shift** | **`8`** | `3` |
| 샘플러 | `er_sde` | |

**`CFG 1.5` 에서는 프롬프트를 무시하는 일이 잦았다.** `4` 까지 올리니 지시 이행 확률이 크게 늘었고 시프트도 `8` 로 올렸다.
`shift` 의 일반론은 이 문서의 "shift — 기본값 3, 0 은 검은 화면" 절에 있다.

> 감각 하나 더 *(댓글)* — `shift 3` + `euler cfg++` 20스텝(고속 로라 미사용) 과
> `shift 8` + 고속 로라 + `er_sde` 는 **우열이 아니라 아예 다른 구도의 그림**이 나온다.

### 8GB 판의 정체 — Tiled VAE

```text
VAE 디코드 순간 점유    13.4GB  →  7.9GB
```

**결과가 가끔 검은 이미지로 나오는 것은 VAE 디코딩 중 VRAM 이 넘친 것**이다.
12GB 판 대신 **8GB 판(Tiled VAE)** 을 쓰면 된다. VRAM 이 넉넉해도 이 증상이 나면 8GB 판으로 내려라.

### 자주 나는 오류 셋 (전부 댓글에서 해결됨)

**1. `animaPreviewRdbt.4bB9.safetensors 로라가 없다`**

**같은 파일이다.** 제작자가 이름을 바꿔 재업로드했다.

```text
animaPreviewRdbt.4bB9.safetensors
  = anima_preview_rdbt_finetuned_cfg_distilled_v0.12.safetensors
```

파일명을 워크플로우가 찾는 이름으로 바꾸거나, 노드에서 새 이름을 직접 고르면 된다.

**2. CLIP 로드 노드의 `Llama2` 텐서 크기 불일치**

```text
size mismatch for model.embed_tokens.weight: copying a param with shape
torch.Size([151936, 1024]) ... current model is torch.Size([128256, 4096])
```

**ComfyUI 를 업데이트하면 해결된다.** 구버전이 Qwen 계열 텍스트 인코더를 Llama2 로 잘못 잡던 문제다
(ANIMA 의 인코더가 CLIP 이 아니라는 앞 절과 같은 이야기다).

**3. 캐릭터 로라를 못 넣겠다** → 로라 로더 노드를 하나 더 달면 적용된다. → [로라 쓰는 법](lora-usage.md)

> ⚠️ **해상도는 이 워크플로우가 `0.75` 배로 떨어뜨린다.** 그 이유는 위 "해상도 — 1024가 아니라 768" 절에 있다.

*VER.2 는 [VER.3(아니마3 + 고속 로라 교체)](https://arca.live/b/aiart/167585299) 로 이어진다.
지금 기준판은 All in One V5 쪽이므로 "워크플로우와 버전" 절도 함께 보라.*


---

**VER.1 (2026-02) 을 먼저 만났다면** — 글 첫 줄에 작성자가 *"VER.2 가 더 좋다"* 고 직접 적어 뒀으므로
`https://arca.live/b/aiart/163201876` 쪽을 본다. VER.1 의 특징은 ComfyCore **기본 노드로만 구성해
커스텀 노드를 따로 설치하지 않아도 된다**는 것과, 모델 로드 노드 옆에 다운로드 링크와 넣을 폴더가 적혀 있다는 것이다.
Anima 기본 설정 대비 4~5배 빠르게 뽑히도록 스텝과 해상도를 최적화했다.

**노드가 빨갛게 뜰 때** — 대개 그 노드가 참조하는 파일이 없어서다.

| 빨간 노드 | 해결 |
|---|---|
| `4step 고속 로라 로드` | 그 노드에서 `dmd2_sdxl_4step_lora.safetensors` 를 **직접 선택**한다 |
| 업스케일 모델 | `2x-AnimeSharpV4` 계열 파일을 받아 `models/upscale_models` 에 넣고 **F5 새로고침 또는 ComfyUI 재시작**. 로컬 실검증은 `2x-AnimeSharpV4_RCAN.safetensors` 로 확인했다. shared models 방식이면 `extra_model_paths.yaml` 에 **`upscale_models: upscale_models`** 도 있어야 한다 |

LoRA 를 추가하려면 LoRA 로더 노드를 붙이면 된다 → [로라 쓰는 법](lora-usage.md)

<small>근거 — [초보자용 아니마 + IL 5배 초고속 워크 플로우 26.02](https://arca.live/b/aiart/162909120) · [초보자용 아니마+IL 워크플로우 VER.2 26.02](https://arca.live/b/aiart/163201876)</small>

## mod guidance — 퀄리티 태그를 어디에 넣나
<small>2026-06 기준 · 근거 1건 · 자료 엇갈림</small>

`Anima Mod Guidance` 는 **(퀄리티태그 - 퀄리티부정태그)** 방향으로 생성을 보조하는 기능이다.
어디에 무엇을 넣는지를 **정반대로 이해하는 사람이 실제로 나왔고**, 원글 작성자가 *"정확히 반대"* 라고 정정했다.

| | 넣는 것 |
|---|---|
| **mod guidance 쪽** | **퀄리티 태그만.** 컨텐츠 태그를 넣는 게 아니다 |
| 샘플러로 가는 일반 부정 | 퀄리티 태그를 **빼고**, '그림에 들어가면 안 되는 내용' 만 |

```text
positive_quality   highres, best quality, score_7
negative_quality   score_1, score_2, score_3, worst quality, lowres, old, bad hands, bad anatomy
일반 negative       (위 퀄리티 태그 제외) 그림에 들어가면 안 되는 내용만
```

> ⚠️ **"기본 긍정칸에 퀄리티 태그, mod guidance 에 상세 프롬프트" 는 틀렸다.**
> 어떤 독자가 그렇게 이해했고 작성자가 **정확히 반대**라고 직접 정정했다. **퀄리티 태그가 mod guidance 쪽이다.**

왜 이렇게 나뉘었나 — 이미지 생성은 `(긍정태그 - 부정태그)` 벡터로 진행되는데,
지금까지 **부정 태그 전부를 한꺼번에 밀어 넣다 보니 보조 역할이 흐려졌다.**
`ComfyUI-Spectrum-KSampler` v2.7.0 에서 생성부와 guidance 부를 분리하면서 **'부정 퀄리티 태그' 입력칸이 하나 더 생겼다.**

### ⚠️ batch size 2 이상에서는 안 먹는다

> **`Anima Mod Guidance` 의 model patch 버전은 batch size 2 이상에서 적용되지 않는다.**
> Civitai 에서도 같은 보고가 있다. **배치를 키웠는데 효과가 사라졌다면 이것 때문이다.**

### 잔팁 (댓글)

- 검은 막대·글자 제거는 **일반 부정에 `bar censor`, guidance 부정에 `censored`** 로 나눠 넣는 게 좋다
- 긍정에 `masterpiece` 를 안 쓰는 이유는 **결과가 'AI 그림처럼' 되기 때문**이라고 작성자가 답했다
- 태그에서 추상적인 표현을 덜어내고 퀄리티 태그 쪽으로 몰수록 프롬프트 이행력이 좋아진다는 것이 작성자 관찰이다

연결 방향(어느 소켓에 무엇을 꽂는지)은 이 문서의 "화질 보정 노드 넷 — 겹쳐 쓰면 탄다" 절에 있다.
튜링(RTX20·GTX16) 세대는 `KSampler(spectrum)` 대신 이 노드를 써야 한다.

*원문 174673655 **한 글**에서 나온 정리다. batch size 제약만 Civitai 쪽 보고가 겹친다.*


<small>근거 — [comfyui anima 고속 + mod guidance 노… 26.06](https://arca.live/b/aiart/174673655)</small>

## ANIMA 가 무엇인가 — 2B · Cosmos 기반 · 비상업용 라이선스
<small>2026-01 기준 · 근거 1건</small>

ANIMA 를 받기 전에 알아 둘 것 두 가지다 — **무엇으로 만들어졌는가**와 **어디까지 써도 되는가**.

| 항목 | 값 |
|---|---|
| 만든 곳 | **CircleStone Labs + Comfy Org** |
| 크기 | **2B** (20억 파라미터) |
| 기술 기반 | NVIDIA Cosmos — `Cosmos-Predict2-2B` |
| 학습 데이터 | 애니메 이미지 수백만 장 + 비애니메 예술 이미지 약 80만 장. **합성 데이터를 쓰지 않고 실제 이미지만** |
| 라이선스 | ⚠️ **CircleStone Labs Non-Commercial License — 비상업용만 허용** |

**실사는 일부러 못 만들게 설계됐다.** 애니메이션 컨셉·캐릭터·스타일에 특화시키느라 그 방향을 잘라 냈다.
그리고 **Danbooru 스타일 태그와 자연어 캡션을 둘 다 지원**한다 — 이게 ANIMA 를 SDXL 계열과 가르는 지점이다.

> 첫 소개 글의 체감 평가는 *"자연어를 상당히 잘 알아듣고 속도가 SDXL 만큼 빠르다. 다만 인체 찐빠가 생각보다 좀 많다"* 였다.
> 인체 찐빠는 이후 판에서 개선됐지만, **가볍고 빠른데 자연어가 되고 단부루 태그도 다 알아듣는다**는 장점 요약은 지금도 유효하다.

⚠️ **라이선스가 비상업용이라는 점은 커미션·판매 목적이면 반드시 확인해야 한다.**
모델 파일을 어디서 받아 어느 폴더에 넣는지는 위 "시작하기" 절에 있다.


<small>근거 — [NSFW 애니메이션 신모델 Anima 26.01](https://arca.live/b/aiart/161150715)</small>

## `score` 태그 — 왜 `score_7` 인가, 그리고 아예 빼자는 쪽
<small>2026-03 기준 · 근거 3건 · 자료 엇갈림</small>

ANIMA 프롬프트에 흔히 붙는 `score_7` 이 어디서 왔고 왜 `score_9` 가 아닌지에 대한 답이 있다.
그리고 **아예 빼자는 쪽도 있어 갈린다.**

### `score_7` 을 쓰는 쪽 (2026-02-04)

고품질 아티스트 태그 목록의 선행 퀄리티 태그가 이렇게 생겼다.

```text
newest, year2024, (masterpiece, best quality, score_7), highres, absurdres, safe
```

"Pony 계열 score 태그는 `score_9` 까지 있는데 왜 7 이냐" 는 질문에서 시작한 댓글 토론의 답이 명쾌하다.

> **점수별로 작품을 쪼개면 `best quality` 가 50장을 학습할 때 각 점수 태그는 10장씩만 학습하게 된다.**
> 특히 **9점짜리는 학습량이 매우 부족해서** 거의 없거나 그림체가 한쪽으로 쏠린다.
> 그래서 **낮지도 않으면서 다양한 그림이 가능한 7 정도**를 쓰는 것이다.

score 가 높아질수록 그 태그로 선별된 이미지가 줄어들어 일관적인 그림만 나온다는 관찰도 같은 말이다.
Pony 제작자가 이 한계를 개선하려고 score 를 여러 개 썼다가 AI 가 태그 세트로 통째 인식해 버려 더 실패했다는 이야기도 나왔다.

### ⚠️ 빼는 쪽 (2026-02-12) — 양쪽을 병기한다

로라 학습 재시도 글은 **'`score` 태그가 오히려 성능을 저하시킨다'는 말을 보고 다시 해 봤다**고 밝히며
긍정 프롬프트에서 `score_8` 을 빼고 `highres,` 로 시작했다.

| | 긍정 프롬프트 | 네거티브 |
|---|---|---|
| **넣는 쪽** (2026-02-04) | `(masterpiece, best quality, score_7)` | `worst quality, low quality, score_1, score_2, score_3, ...` |
| **빼는 쪽** (2026-02-12) | `highres,` 로 시작 — **score 태그 없음** | `worst quality, low quality, score_1, score_2, score_3, ...` **그대로 유지** |

**두 쪽이 일치하는 것이 하나 있다 — 네거티브의 `score_1, score_2, score_3` 은 양쪽 다 남긴다.**
낮은 점수를 밀어내는 용도로는 이견이 없다. 갈리는 것은 **긍정 프롬프트에 score 를 넣느냐**뿐이다.

> 결론이 나지 않았다. 둘 다 한 글씩이고 서로를 실측으로 부정하지 않았다.
> ANIMA 의 퀄리티 태그가 두 계통(사람 기준 `masterpiece~worst quality` / PonyV7 판정 AI 기준 `score_1~score_9`)이고
> **둘 다 써도 되고 하나만 쓰거나 안 써도 동작한다**는 것이 공식 설명이므로, 넣고 빼 보고 판단하면 된다.

### 그 `score_` 는 어디서 왔나 (2026-03)

이 논쟁의 배경이 되는 출처가 따로 밝혀져 있다. `score_9`~`score_1` 은 **Pony V7 개발 과정에서 쓰인 미적 점수 분류 AI**
(https://huggingface.co/purplesmartai/aesthetic-classifier)에서 온 것이고, 이 분류기는 사람이 직접 매긴 소수 이미지로 학습했는데
**Pony V7 개발자가 퍼리라서 퍼리 기준의 미적 판단이 섞여 있다**고 본다. 그래서 남용하면 전형적인 'AI 그림체' 가 된다.
**대신 `masterpiece` 계열보다 NSFW 로 쏠리는 현상은 확실히 덜하다**는 장점이 있다 — 위 '품질 태그가 NSFW 쪽으로 끌고 간다' 항목 참조.

<small>근거 — [로컬 Anima모델의 품질 태그와 세이프티 태그에 대해서 (… 26.03](https://arca.live/b/aiart/163666946) · [스압) 아니마 프리뷰 고품질 아티스트 태그 batch 1 26.02](https://arca.live/b/aiart/161430824) · [anima 로라 재시도 26.02](https://arca.live/b/aiart/162256686)</small>

## 한글로 프롬프트 쓰기 — gemma4 번역 워크플로우
<small>2026-05 기준 · 근거 1건</small>

ANIMA 는 한국어를 이해하지 못한다(위 "프롬프트 쓰는 법" 참조). 그런데 **한글로 써도 되게 만든 초보자용 워크플로우**가 있다 —
`gemma4` 모델이 한글 프롬프트를 영어로 자동 번역해 ANIMA 에 넣어 주는 구조다 (2026-05).

| 항목 | 값 |
|---|---|
| ⚠️ **필수 버전** | **ComfyUI 포터블 `0210` 이상** — `gemma4` 모델이 이 버전부터 지원된다 |
| SageAttention 을 쓸 때 | **KJNodes** 커스텀 노드가 추가로 필요 |
| 제작 환경 | VRAM 16GB / RAM 64GB |
| 구성 | 초보자용이라 **최대한 기본 노드만**으로 만들었고 기본 한국어 프롬프트가 미리 들어 있다 |
| 받는 법 | 본문 이미지를 클릭 → 우클릭 다운로드 → ComfyUI 창에 드래그 앤 드롭 |

### 오류 셋 (전부 댓글에서 해결됐다)

| 증상 | 해결 |
|---|---|
| `ValueError: invalid tokenizer` | **ComfyUI 를 최신 버전으로 설치**하면 해결된다 |
| GGUF 젬마(26b·31b)를 쓰고 싶다 | **city96 의 GGUF 노드**를 설치한 뒤 **GGUF CLIP Loader** 를 쓴다. ⚠️ 다만 **`Prompt Translator` 노드는 GGUF 젬마를 인식하지 못하며 ComfyUI 방식으로 변환된 GGUF 모델만 쓸 수 있다** |
| `RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!` | **모델 로드 장치가 CPU 로 설정돼 있는지** 확인한다 |

> 번역 노드를 끼우는 방식 자체는 이 워크플로우만의 것이 아니다 — EasyUseAnima 는 0.2.5 부터 `%{내용}` 형태로
> 구글번역을 타는 베타 기능을 넣었다(위 "EasyUseAnima" 절). **번역기가 무엇이든 ANIMA 에 들어가는 것은 결국 영어다.**

→ [ComfyUI 쓰는 법](comfyui.md) · [오류 해결](troubleshooting.md)


<small>근거 — [Anima 초보자 자연어(한국어) 프롬프트 워크플로우 26.05](https://arca.live/b/aiart/171167219)</small>

## 전용 모델 없이 인페인팅 — 그리고 나서 마스크를 칠한다
<small>2026-04 기준 · 근거 1건</small>

ANIMA 는 공식적으로 인페인팅을 지원하지 않는다. **그래도 된다** — 전용 모델보다 결과가 못할 뿐이다 (2026-04).
손가락이 4개로 나온 찐빠를 고치는 과정으로 설명된 방법이다.

### 순서 — 마스크를 먼저 칠하지 않는다

이 글의 핵심은 작업 순서다. 우클릭 → `Open in MaskEditor` 로 들어가서

```text
1. 브러시를 고르고 스포이드로 "고치려는 손가락의 색" 을 뽑는다   ← 먼저 할 일은 이것
2. 붓 굵기를 조절해 수정할 부위를 직접 그린다  (허접해 보여도 된다)
3. 그제서야 마스크 탭에서 방금 그린 손가락 위에 마스크를 칠한다
4. 낮은 denoise 로 생성
5. 마무리는 디테일러에게 맡긴다
```

**허접해도 되는 이유는 이것이 '낙서를 고퀄 그림으로 만드는 i2i' 의 응용이기 때문**이다.

### 값

| 항목 | 값 |
|---|---|
| 샘플러 `denoise` | **`0.1~0.3`** — 조금만 높여도 시키지 않은 짓을 한다. **여기서는 기초 공사만 한다** |
| `Mask Blur` | **`5~40`, 대부분 `10`** — `Set Latent Noise Mask` 에 연결하기 **전에** 걸어 주변과 섞는다 |
| `Grow Mask` | 필요할 때만 적당히 |
| Image Blend 의 `mask invert` | `False` = 마스크 **안쪽**을 다시 그림 / `True` = **바깥쪽**을 다시 그림 |
| 마무리 | **Ultimate SD Upscaler** 로 전체를 다듬고 → **손 디테일러**로 세부 |

> 워크플로우의 노드 이름이 전부 '페이스 디테일러' 인 것은 이름만 그럴 뿐 각기 다른 Ultralytics 모델을 물고 있어 동작에는 문제가 없다.

⚠️ **워크플로우가 안 불러와진다면** *(댓글)* — 이미지를 '다른 이름으로 저장' 하면 EXIF 가 날아간다.
**클릭해서 새 탭으로 연 상태 그대로 ComfyUI 로 끌어와야** 하고, 이미지가 커서 완전히 로딩될 때까지 기다린 뒤 시도해야 한다.

→ [인페인팅·아웃페인팅](inpainting.md) · [디테일러](detailer.md)


<small>근거 — [(anima) 최신 모델로 고전적인 인페인팅 하기. 26.04](https://arca.live/b/aiart/168764579)</small>

## ⚠ 와일드카드 팩 — 호출 문서명이 본문과 다르다
<small>2026-07 기준 · 근거 1건 · 자료 엇갈림</small>

ANIMA 전용 와일드카드 팩(2026-07, 작성자 Cloudy)은 의상 34종을 비롯해 캐릭터·외형·배경·표정까지 갖췄다.
**전제: 이 팩은 ANIMA 의 자연어 처리 능력에 크게 의존하므로 다른 모델에서는 테스트되지 않았다.**

설치 경로는 **`ComfyUI/custom_nodes/impact-pack/wildcards`** 다 *(댓글)*.
*(EasyUseAnima 올인원 노드를 쓰면 경로가 다르다 → 위 "EasyUseAnima" 절)*

### ⚠ 본문의 호출 문서명이 틀렸다

| | |
|---|---|
| 본문의 표기 | `Call_Clothes_Place_Pose` ← **틀렸다. 실제 파일명과 달라 호출되지 않는다** |
| 실제 파일명 | **`Call_Clothes_Pose_Place`** |

댓글 지적으로 작성자가 수정했다. **`Place` 와 `Pose` 의 순서가 뒤바뀌어 있었다.**

| 호출 문서 | 무엇이 랜덤으로 나오나 |
|---|---|
| `Call_Clothes` | 의상만 |
| `Call_Clothes_Place` | 의상 + 장소 |
| `Call_Clothes_Pose` | 의상 + 포즈 |
| **`Call_Clothes_Pose_Place`** | 전체 |

의상별로 어울리는 Pose·Place 와일드카드가 따로 만들어져 있어 함께 쓰기를 권한다.
(Casual, Nudity 처럼 맥락을 안 타는 것은 단독으로도 무방하다.)

### 함께 쓰는 보조 프롬프트

**의상 노출 사고(Exposure_Accident) 강화**

```text
unbuttoned, unzipped, unleashed, untied, slipped, loose, stretched, detached
```

**라텍스 이음새 줄이기** — 네거티브에 아래를 넣고, `Latex_Bodysuit` 대신 `Latex_Seamless` 문서를 쓴다.

```text
seams, stitch lines, panel lines, piping, harness, straps, belts, buckles, zipper,
corset, boning, garter straps, thigh straps, chest straps, segmented suit, armor panels, trim lines
```

**부분 누드**

```text
minimal coverage clothing, revealing clothes, scanty attire, erotic clothes, seductive clothes,
transparent, nipple outline on clothes, prominent cameltoe, unbuttoned, unzipped, unleashed,
untied, slipped, loose, stretched, detached, bare shoulder, exposed collarbone,
fully exposed, bare lower body exposed
```

### 쓰면서 걸리는 것

- 동물·몬스터 **의인화 캐릭터 문서는 피부색·머리색(과 헤어스타일) 문서를 꺼 두고** 쓴다.
- **마스크(`Accessory_Mask`)는 앞머리·이마 노출을 설정하는 헤어스타일 프롬프트와 충돌**할 수 있다. 필요하면 헤어스타일을 끈다.
- 표정 문서는 감정별로 갈려 있고 **`Expr_Call` 이 NSFW 를 제외하고 무작위 호출하는 상위 문서**다.
- 압축파일 안의 `old` 문서는 예전 파일이니 무시해도 된다.
- AI 로 생성한 프롬프트라서 **가짓수는 많지만 비슷한 의상·표정이 왕왕 나오고**, 모델이 의도와 다른 복장을 그릴 수 있다고 작성자가 미리 밝혔다.

→ 와일드카드 문법 자체(순차 사이클 함정)는 [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [Anima용 와일드카드 공유 26.07](https://arca.live/b/aiart/177489520)</small>

## 캐릭터 LoRA 배포글 읽는 법 — `anima-base-v1.0` 은 받는 모델이 아니다
<small>2026-06 기준 · 근거 5건</small>

채널의 ANIMA 캐릭터 LoRA 배포글은 글머리에 두 줄이 똑같이 붙어 있다. **이 두 줄이 뉴비를 가장 많이 헷갈리게 한다.**

```text
LoRA Base Model : anima-base-v1.0
Checkpoint Model: waiANIMA_v10Base10
```

| 줄 | 정체 | 받아야 하나 |
|---|---|---|
| `anima-base-v1.0` | **제작자가 LoRA 를 학습시킬 때 쓴 베이스 모델** | **아니다.** 그림을 만드는 모델이 아니다 |
| `waiANIMA_v10Base10` | **실제로 그림을 뽑는 체크포인트** | 그렇다. 여기에 캐릭터 LoRA 를 얹는다 |

**댓글에서 다른 사용자와 작성자가 함께 확인해 준 부분이다.**

### 배포자가 미리 밝히는 공통 한계

> **캐릭터의 의상·장식·특이한 눈동자·문신은 제대로 구현되지 않을 가능성이 높다.**
> 구현이 안 된 일부 의상은 아예 올리지 않았다.

프롬프트는 본문이 아니라 **Civitai 각 모델 페이지**에 있고, 예시 이미지에 EXIF 가 살아 있어 워크플로우를 노드로 불러올 수 있다.

### 개별 LoRA 의 함정 (해당 배포글에서만 언급됨)

| 로라 | 증상 | 대처 |
|---|---|---|
| '모비딕' 계열 | **입이 아예 안 그려진다** | **입·표정 관련 태그가 필수**다 |
| '동아리' 이예린 | 분리된 소매가 계속 나온다 | 네거티브에 `detached sleeves` |

### 링크가 예전 것과 같아 보일 때

**같은 Civitai 모델 페이지 안에 IL 판과 ANIMA 판이 함께 들어 있다.**
"전에 받은 것과 주소가 같은데?" 싶으면, 페이지에 들어가 **모델 버전에서 ANIMA 판을 골라** 받아야 한다.

### 그림체 로라 묶음 (2026-07)

메인 로라 2 + 디테일 로라 2 를 **따로 넣어 조정하는 구성**과, 넷을 **하나로 합친 딸깍 구성** 두 가지로 배포된다.
가중치는 기본 **1** 권장이고, 배포자 본인은 4개를 따로 넣어 조정하는 쪽을 추천한다.
댓글의 실제 예시: `mixed 1` / 다른 로라 `1` / detail 계열 `0.25 ~ 0.4`.
번거로우면 합본(mixed2) 하나만 넣으면 된다.

*(학습 도구는 kohya script 라고 댓글에서 밝혀졌다. → [로라 쓰는 법](lora-usage.md))*

<small>근거 — [Anima 웹툰 캐릭터 Lora 공유) 뷰티풀 군바리 26.06](https://arca.live/b/aiart/173589934) · [아니마 그림체 로라 공유 26.07](https://arca.live/b/aiart/176886634) · [Anima 웹툰 캐릭터 Lora 공유) 동아리 26.06](https://arca.live/b/aiart/173973554) · [Anima 애니메이션 캐릭터 Lora 공유) Fate sta… 26.06](https://arca.live/b/aiart/173275160)</small>

??? note "근거 5건 전부 보기"
    [Anima 웹툰 캐릭터 Lora 공유) 뷰티풀 군바리 26.06](https://arca.live/b/aiart/173589934) · [아니마 그림체 로라 공유 26.07](https://arca.live/b/aiart/176886634) · [Anima 웹툰 캐릭터 Lora 공유) 동아리 26.06](https://arca.live/b/aiart/173973554) · [Anima 애니메이션 캐릭터 Lora 공유) Fate sta… 26.06](https://arca.live/b/aiart/173275160) · [Anima 웹툰 캐릭터 Lora 공유) 모비딕 26.06](https://arca.live/b/aiart/174511949)

## ANIMA→IL 2단에서 실제로 부딪히는 것
<small>2026-08 기준 · 근거 2건</small>

위 "2단 구성" 절이 왜 그렇게 짜였는지는 설명했으니, 여기서는 **실제로 돌렸을 때 부딪히는 것들**만 적는다(2026-05 개조 실험).

| 증상 | 원인 | 대처 |
|---|---|---|
| **IL 구간부터 그림 속 글자가 깨진다** | IL 단계의 디노이즈 | Denoise 를 낮추면 글자는 보존되지만 **IL 특유의 색채가 약해진다** — 맞교환이다 |
| **IL 단계에서 눈이 변한다** | IL 쪽 긍정 프롬프트를 **비워 뒀다** | 아니마 쪽 프롬프트를 IL 쪽에도 적어 준다 |
| IL 쪽에 자연어를 적었더니 안 먹는다 | **아니마는 자연어를, Illustrious 는 danbooru 태그를 먹는다** | IL 칸에는 태그로 적는다 |
| 같은 하사쿠인데 XL 로 넘어가면 **여성기 형태가 뭉개진다** | 모델 간 차이 | 중간 단계를 생략하고 **깡해상도로 뽑은 뒤 디테일러만** 돌리는 편이 낫다 |

**그래서 그룹 단위 스위치 노드(`Fast Group Bypasser`, rgthree)를 반드시 넣어 두라**고 권한다 —
중간 단계를 통째로 껐다 켰다 할 수 있어야 위의 마지막 행 같은 대처가 가능하다.
*(글쓴이는 그 준비를 깜빡했다고 밝혔다.)*

시작 해상도를 896x1152 에서 1024x1536 으로 올려도 IL 이후 단계가 모델·VAE 를 IL 에서 받아 쓰는 데 이상은 없었다.

### 저사양에서도 도는가

각 단계마다 가속 노드를 붙여 두면 **RTX 2070 SUPER 에서도 매끄럽게 돌아갔다**는 보고가 있다 *(한 글의 사례)*.
→ 가속 조합은 위 "가속 — 무엇이 얼마나" 절

### 2026-08 시점의 전환 장벽

**"IL 에서 쓰던 그림체를 ANIMA 에서 쓸 수 없다"** 가 아니마를 안 쓰는 결정적 이유로 꼽히는 증언이 있다(RTX 4060 Laptop 사용자).
같은 글에서 **Anima Easy Use 는 디테일러를 쓰면 ComfyUI 서버가 메모리 오류를 내며 꺼졌고,
자작 아니마 워크플로우는 디테일러(SEGS)에서 100초 이상 잡아먹어 1024x1024 한 장에 200초가 넘었다**고 보고했다.
같은 사람의 WAI17(IL) 워크플로우는 디테일러 포함 약 40초다.

곁다리 하나 — **ANIMA 는 불필요한 공백이나 줄바꿈을 허용하지 않는다.** 프롬프트를 노드로 조립할 때 걸리는 지점이다.

<small>근거 — [Anima+IL 연속 스펙트럼 워크플로우. 26.05](https://arca.live/b/aiart/171529357) · [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179637421)</small>

## ⚠ Pixelate x4 VAE — 픽셀화냐 다운샘플링이냐 (결론 없음)
<small>2026-06 기준 · 근거 1건 · **근거 약함** · 자료 엇갈림</small>

`Pixelate x4 VAE`(2026-06)는 **VAE 자체를 도트 전용으로 훈련해** 픽셀화를 하겠다는 접근이다.

**본문의 주장** — 픽셀화는 보통 `pixel art` 프롬프트나 LoRA 로 하는데, 프롬프트는 모델이 그만큼 학습돼 있어야 하고
LoRA 는 그림체 자체에 영향을 준다. 이 VAE 는 **"생성 결과를 출력하는 프린터를 도트 전용으로 바꾼 것"** 이라
그림체와 구도를 그대로 두고 픽셀화만 적용할 수 있다는 것이다.
ANIMA 는 SDXL 보다 VAE 해상도가 높아 뭉개짐 없이 더 선명하게 나온다고 덧붙였다.

> ⚠️ **댓글에서 이 핵심 주장이 정면으로 반박됐다.**
> 여러 사람이 **"이건 픽셀화가 아니라 다운샘플링에 가깝다. 픽셀 경계가 명확하지 않고 블러가 심해서
> 의도한 픽셀 아트가 아니라 그냥 화질이 떨어진 이미지처럼 보인다"** 고 지적했다.

작성자는 "아카라이브 게시물 안에서 블러가 생기니 원본을 보라" 고 반박했지만, 반박자는 원본으로 봐도 마찬가지라며
아래 프롬프트로 뽑아 비교하라고 제안했고 실제 비교 글까지 올렸다. 다른 댓글도 반박 쪽에 동의했다.

```text
(pixel art:3), (dithering), (oekaki:2)
```

**결론이 나지 않은 채로 끝났다. 직접 비교해 보고 판단하는 것이 안전하다.**

→ i2i 로 화풍을 바꾸는 일반적인 요령은 [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [아니마 완벽한 픽셀 그림 만들기 26.06](https://arca.live/b/aiart/173819166)</small>

## 쓸 만한 작가 태그 모으기 — 역추출 도구
<small>2026-02 기준 · 근거 1건</small>

ANIMA 는 작가 태그(`@`)를 강하게 지원한다. 그런데 **쓸 만한 태그를 모으는 일**이 따로 남는다.

와일드카드로 대량 생성한 이미지가 폴더에 쌓여 있고 **각 이미지에 ANIMA 작가 태그가 하나씩 들어 있는 상황**을 전제로 만든 도구가 있다.

```
ANIMA_comfy_artist_extractor.zip
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/Beta/
```

| 기능 | 하는 일 |
|---|---|
| Extracted Tags | 선택한 이미지의 **ComfyUI 워크플로우 안에서 `@` 로 시작하는 작가 태그를 역추출** (Ctrl+C 로 복사) |
| Favorite 폴더 | 테스트를 마친 태그를 관리 영역으로 (우클릭으로 특정 그룹에 바로 보내기도 가능) |
| 클립보드 붙여넣기 | 만족스러운 이미지를 Ctrl+C → Ctrl+V 하면 **해당 아티스트 페이지 썸네일에 자동 등록** |
| 순차 와일드카드 생성 | 정리한 태그로 와일드카드를 만들어 한 번에 여러 장 뽑고 선별 |

실행은 `run_ComfyUI_Workflow_Viewer.bat` 더블클릭. **⚠ EXE 가 아니라 Python 이 설치돼 있어야 한다** *(댓글)*.

> ⚠ **혼동 주의** *(댓글)*: 이것은 `artist_thumbnail_anima.json` 같은 파일을 읽는 **썸네일 뷰어가 아니다.**
> **이미 생성된 이미지에서 작가 태그를 역추출**하는 용도다. 썸네일 뷰어가 필요하면 따로 찾아야 한다.

### 도구 제작자가 남긴 관찰

> **ANIMA 작가 태그는 성능은 좋지만 NAI 처럼 재현을 잘하는 것은 아니다.**

동봉된 `CLAUDE.md` 에 프로그램 구조가 들어 있어서 **Gemini·Claude 에 던져 주면 직접 고쳐 쓸 수 있다**고 안내한다.

→ 작가 태그 표기 규칙(`@`)은 위 "작가 태그는 `@`" 절

<small>근거 — [ANIMA용 간이 아티스트 태그 관리 도구 (추가1) 26.02](https://arca.live/b/aiart/161369658)</small>

## ⚠ 공식 퀄리티 로라 `anima-highresaesthetic-boost` — 노이즈 보고와 0.7 권장이 갈린다
<small>2026-07 기준 · 근거 2건 · **근거 약함** · 자료 엇갈림</small>

같은 로라를 두고 **정반대에 가까운 두 보고**가 있다. 한쪽을 지우지 않고 둘 다 적는다.

| | 시점 | 체크포인트 | 내용 |
|---|---|---|---|
| **노이즈가 낀다** | 2026-06-09 | anima **BASE** 모델 기준 | "ANIMA 에서 제공하는 공식 퀄리티 로라인데 **PREVIEW 시절에 나왔던 거라 현재 BASE 모델 기준으로는 노이즈 낀다는 말이 있네요**" — 이 사람은 공식 로라 대신 `aesthetic-quality-modifiers-masterpiece` 만 **0.2~0.5** 로 쓴다 |
| **0.7 로 쓴다** | 2026-07-11 | **WAI-ANIMA** (파인튜닝 체크포인트) | 그림체 공유 세팅에 `anima-highresaesthetic-boost` **0.7** + `anima-detail-tweaker` 의 `rendering_detailer_base10` **0.7** 이 그대로 들어가 있다 |

### 판정 — 진짜 충돌이라기보다 조건이 다르다

세 가지가 어긋난다.

1. **체크포인트가 다르다.** 노이즈 보고는 `anima-base` 계열 **BASE** 이야기이고, 0.7 쪽은 커뮤니티 파인튜닝판 **WAI-ANIMA** 다. ANIMA 계열은 로라 배포글의 `LoRA Base Model: anima-base-v1.0` 이 학습 베이스일 뿐 실제로 그림을 뽑는 체크포인트는 따로라는 점이 이미 정리돼 있다 (아래 'LoRA 배포글 읽는 법' 항목).
2. **근거의 무게가 다르다.** 노이즈 쪽은 댓글에서 전해 들은 말(`~라는 말이 있네요`)이고, 0.7 쪽은 한 달 뒤 본인이 직접 쓴 세팅 전문이다.
3. **BASE 모델에 0.7 을 직접 걸어 본 보고는 아직 없다.** 그래서 "BASE 에서는 안 된다" 도 "0.7 이 맞다" 도 단정할 수 없다.

### 그래서 어떻게 쓰나

| 상황 | |
|---|---|
| 파인튜닝 체크포인트(WAI-ANIMA 등) | 0.7 이 실사용된 값이다. 그대로 시작해도 된다 |
| `anima-base-v1.0` 계열 순정 BASE | **강도를 0.2~0.5 로 낮춰서 시작하고, 자글자글한 노이즈가 보이면 이 로라를 먼저 의심한다.** 고해상도가 뭉개지는 원인이 세팅이 아니라 로라였던 사례가 따로 있다(아래 'highres 가 뭉개질 때') |
| 어느 쪽이든 | **로라를 써도 `masterpiece`/`best quality` 같은 기본 긍정·부정 프롬프트는 그대로 쓴다.** "긍정이나 네거는 기본으로 써야 되는 거죠" 가 원문 작성자의 답이다 |

→ [로라 쓰는 법](lora-usage.md) · [업스케일과 화질](upscale.md)

<small>근거 — [어제 작업한 아니마 그림체 공유 26.07](https://arca.live/b/aiart/176515020) · [아니마 퀄리티 높이기 26.06](https://arca.live/b/aiart/173299334)</small>

## 퀄리티는 프롬프트가 아니라 로라로 — 슬라이더 계열
<small>2026-06 기준 · 근거 1건</small>

ANIMA 베이스 모델의 품질을 프롬프트로 잡는 데는 한계가 명확하다는 것이 이 글의 출발점이다 (1건, 2026-06).

> 글쓴이가 쓰는 퀄리티 프롬프트도 `(masterpiece, best quality:2)` 아니면 `(masterpiece, best quality:2), score_7` **둘뿐**이고,
> `score_7` 은 원작 그림체를 크게 침범해서 거의 안 쓴다. **네거티브를 3까지 올려 봐도 아니마에서는 별 효과가 없었다.**
> 작가 프롬프트는 효과가 있지만 특정 그림체로 모델을 강제로 끌고 가고 불순물이 많아 여기저기 튄다.

남는 답은 셋이다 — **파인튜닝하거나, 퀄리티 로라를 쓰거나, 자기 그림체를 직접 로라로 굽거나.**

### 실사용 배합

```text
anima-quality-enhance-slider   1.5      https://civitai.red/models/2612570/anima-quality-enhance-slider
anima-detail-tweaker           0.5      https://civitai.red/models/2620171/anima-detail-tweaker
```

효과는 **아니마 최대 약점인 배경이 강화되고, 단순화돼 있던 명암이 세밀해지면서도 그림체는 최소한으로만 건드리는** 것이다.
이것이 **슬라이더 로라의 강점**이다 — 일반 퀄리티 로라는 원본 그림체가 '누구세요?' 가 되는 경우가 많다.
같은 제작자의 dlss 로라·빛 로라도 함께 쓴다.

### 곁다리로 나온 교훈 — 데이터셋 구성이 품질에 직결된다

캐릭터 로라를 얹었을 뿐인데 전체 퀄리티가 덩달아 오르는 경우가 있다.

| 데이터셋 | 결과 |
|---|---|
| 원작 스샷이 **화면을 꽉 채운 그래픽** (예: 스텔라블레이드2 이비 로라, 30장 학습) | 30장뿐인데도 **전체 퀄리티가 난데없이 상승**한다 |
| **얼굴 위주로만** 채운 로라 | 결과가 **휑해진다** |

> 글쓴이는 ilxl 과 아니마의 차이를 '480i 폴더폰 카메라가 1080p 스마트폰 카메라가 된 것' 에 비유한다.
> 댓글에서 본문 서술이 하나 보정됐다 — **`score`(포니) 태그를 넣으면 품질이 저하되는 게 아니라 오히려 오르지만, AI 티가 많이 묻어 호불호가 갈린다.**

→ [로라 쓰는 법](lora-usage.md)

<small>근거 — [아니마 퀄리티 높이기 26.06](https://arca.live/b/aiart/173299334)</small>

## 품질 태그가 NSFW 쪽으로 끌고 간다 — 세이프티 태그 4단계
<small>2026-03 기준 · 근거 1건</small>

"NSFW 를 하나도 안 적었는데 야한 그림이 나온다" 의 원리가 설명된 글이다 (1건, 2026-03).

### 왜 그런가

ANIMA 의 품질 태그 두 계통 중 **Human score 계열**(`masterpiece, best quality, good quality, normal quality, low quality, worst quality`)은
**단부루 같은 사이트에서 사람들이 좋아요를 많이 누른 순서**로 매긴 것이다. NAI1 유출 시절 `masterpiece` 부터 이어진 전통적 방식이다.

> 문제는 **사람들이 SFW 보다 NSFW 이미지에 좋아요를 훨씬 많이 누른다**는 점이다.
> 그래서 `masterpiece, best quality` 만 넣어도 **NSFW 선언이 없는데 그림이 NSFW 쪽으로 끌려간다.**
> **Anima-Preview 는 이 문제가 특히 심하다.**

일부 모델은 이를 고치려고 NSFW 이미지의 좋아요 가중치를 낮추고 SFW 는 높이는 방식을 썼다.

### 대처 — 세이프티 태그를 쓴다

| 태그 | 등급 |
|---|---|
| `safe` | 전체 이용가 |
| `sensitive` | 청소년 이용가 |
| `nsfw` | 청소년 이용불가 |
| `explicit` | 성인물 |

**NSFW 로 쏠리는 게 싫으면 `safe` 를 명시적으로 넣는다.** 반대로 야한 것을 뽑을 때도 이 네 단계로 수위를 조절한다.

### `score_` 계열은 왜 다른가

`score_9`~`score_1` 은 Pony V7 개발 과정에서 쓰인 **미적 점수 분류 AI**(https://huggingface.co/purplesmartai/aesthetic-classifier)에서 온 것이다.
이 분류기는 사람이 직접 매긴 소수 이미지로 학습했는데 **Pony V7 개발자가 퍼리라서 퍼리 기준의 미적 판단이 섞여 있다**고 본다.
그 결과 서양 아티스트 스타일과 과한 미적 보정이 걸려 **남용하면 전형적인 'AI 그림체'** 가 된다.

**대신 Human score 계열보다 NSFW 로 쏠리는 현상은 확실히 덜하다.** 그래서 글쓴이는 `score_` 를 필수요소처럼 넣지 말고 **취향에 따른 선택지**로 쓰라고 권한다.

> 댓글 보충 — 네거티브에 넣는다면 `score_1, score_2` 정도가 좋고, 긍정에는 score 를 아예 안 넣는 사람들이 있다.
> **특히 `score_9` 가 들어가는 순간 AI 특유의 번들거리는 광택 느낌이 난다**는 증언이 여러 건이며, `watercolor`/`pastelcolor` 를 섞어 눌러 왔다는 사람도 있다.

이 설명은 **로컬 Anima 와 Pony 계열 모델에만** 해당한다. → 아래 '`score` 태그 — 왜 `score_7` 인가' 항목과 함께 볼 것.

<small>근거 — [로컬 Anima모델의 품질 태그와 세이프티 태그에 대해서 (… 26.03](https://arca.live/b/aiart/163666946)</small>

## 퀄리티 태그 뭉치에 가중치를 통째로 거는 법
<small>2026-05 기준 · 근거 1건</small>

ANIMA 는 태그 가중치를 2부터 시작해도 된다는 성질을 퀄리티 태그에 그대로 써먹은 실험이다 (1건, 2026-05, 같은 시드 비교).

```text
원래         : year2025, newest, (masterpiece, best quality, score_9, score_8), highres, absurdres
통째로 묶기  : (year2025, newest, masterpiece, best quality, score_9, score_8, highres, absurdres:2)
```

시드를 포함해 나머지 설정이 전부 같은데도 **품질이 눈에 띄게 달라졌다** — 색감이 진해지고 얼굴형이 샤프해지며 눈 색이 선명해지는 방향이다.
다만 **AI 티가 강해졌고**, 그 원인이 포니 스코어 태그라는 제보를 받아 다시 시험했다.

| 형태 | 결과 |
|---|---|
| `(... score_9, score_8, ...:2)` — 포니 태그를 **가중치 안에** | 품질은 오르지만 **AI 느낌이 강하다** |
| `(year2025, newest, masterpiece, best quality, highres, absurdres:2), score_9, score_8` — 포니 태그를 **가중치 밖으로** | 그 중간 |
| 포니 태그를 **아예 제외** | **AI 느낌이 사라지면서도 원본보다 나아졌다** ← 글쓴이 결론 |

> **Illustrious(ilxl) 까지만 해도 퀄리티 태그 한두 개로 이만한 차이가 나지 않았고 가중치를 줘도 변화가 작았는데 ANIMA 는 다르다**는 것이 요지다.
> 작성자는 아니마가 아직 베이스 모델이라 품질이 들쑥날쑥해서 생기는 현상이고 **튜닝된 파생 모델이 나오면 사라질 것**으로 본다.

**작가 프롬프트를 쓰기 부담스러울 때**(작가 태그 영향력이 너무 강해서)의 대안으로 쓸 만하다.
댓글에서 공개된 실제 프롬프트는 가중치를 **3** 까지 올린 예시도 있다.

```text
1girl, (year2025, newest, masterpiece, best quality, highres, absurdres:3), score_9, score_8, ...
(delicate colored lineart, highly aesthetic Pixiv style illustration, clean composition,
 low contrast shading, high-quality digital art.:0.7)
<lora:KinniStyle:0.5>
```

→ [프롬프트 쓰는 법](prompting.md) 의 가중치 항목

<small>근거 — [아니마 이거 의외로 먹히나? 싶은거 26.05](https://arca.live/b/aiart/170963618)</small>

## 이미지 편집(에디트) — 공식 모델이 없어서 우회 셋이 쓰인다
<small>2026-05 기준 · 근거 1건</small>

ANIMA 에는 공식 이미지 편집 모델이 없다. 이를 간접적으로 구현하는 세 방법을 각각 떼어 비교한 기록이다 (1건, 2026-05, RTX 2070 SUPER).

### ★ 먼저 — 필수 사전 조건

앞의 두 LoRA 는 이 커스텀 노드가 없으면 **성능이 제대로 나오지 않는다. 반드시 설치한다.**

```text
https://github.com/Mirumo0u0/ComfyUI-Cosmos-Reference
# 관련 노드 https://github.com/Anzhc/Anzhc-ComfyUI-Cosmos-Reference 도 같이 쓸 수 있다
```

### 셋의 성격이 정반대다

| | 잘 되는 것 | 조건·한계 |
|---|---|---|
| ① **AnimaEdit-experimental v0.1** (LoRA) | **외부에서 가져온 이미지**(게임 CG 등) 개조 | AI 로 생성한 이미지를 편집하려면 **원본과 같은 조건**(같은 품질/작가 태그, 같은 스타일 LoRA)을 맞춰 줘야 동작한다. 스타일 LoRA 를 끄니 스쿠미즈 입히기도 누드화도 실패했고 켜니 정상 작동했다. **매우 까다롭다** |
| ② **Anima Edit [Nude Filter + Clothes Change + More] v1.0** (LyCORIS) | **AI 로 만든 이미지** 개조 — 의상 변경·완전 누드 모두 단독으로 성공 | **다른 LoRA 와 같이 쓸 수 없고**, CLIP 수치 없이 **오직 모델 수치로만** 작동한다. **품질 프롬프트가 없으면 전혀 작동하지 않았다.** 주문하지 않은 표정까지 같이 바뀐다 |
| ③ **Anima-LLLite** (kohya-ss) | — | 그림 전체에 마스크를 칠해 버려 **사실상 그냥 i2i** 다. 스타킹 색만 바꾸려 해도 전혀 다른 그림이 나오고 시드에 따라 텅 빈 그림이 나오기도 한다. denoise 를 줄이면 아예 아무것도 안 바뀐다. **단순 복장 변경 용도로는 사용 불가** |

**①②는 둘 다 배경 변경이 불가능하고, 서로 호환되지 않아 장점을 합칠 수 없다**는 것이 댓글의 결론이다.
②에서 샘플러를 아니마 공식 추천(ER SDE 포함)으로 바꿔 봤지만 원인은 샘플러가 아니라 **LoRA 성능 자체**였다.

> **글쓴이와 댓글의 공통 권고** — 캐릭터 LoRA 가 없다면 차라리 **마스크 에디터로 몸만 마스킹해 평범하게 인페인트**하거나
> **SAM3 로 특정 부위를 감지**하는 방식이 더 효율적일 수 있다.

→ [인페인팅](inpainting.md)

<small>근거 — [(스압) 실험용 아니마 에디트 워크플로우 3종 26.05](https://arca.live/b/aiart/172022855)</small>

## NAI 에서 넘어올 때 — 문법 세 가지가 다르다
<small>2026-07 기준 · 근거 1건</small>

NAI 만 쓰다가 RTX 5080 을 사고 로컬 ANIMA 로 옮긴 사람의 *"그림체가 시원찮다"* 는 글에서
**NAI 사용자가 부딪히는 차이가 거의 다 정리됐다** (2026-07).

### 문법 — 셋이 다르다

| | NAI | **ANIMA** |
|---|---|---|
| 작가 | `artist:name` | **`@아티스트`** |
| 가중치 | `from side::2` | **`(from side:2)`** |
| 캐릭터명 괄호 | 그대로 | **`kaga_\(kancolle\)` — 역슬래시 이스케이프 필수.** 안 하면 인식하지 못한다 |
| 언더바 | 빼는 것이 정석 | **`_` 대신 스페이스로 써도 된다** |

### 기대치 — 작가 태그는 NAI 만큼 안 먹는다

> **ANIMA 는 작가 태그가 NAI 만큼 먹지 않는다. NAI 쓰던 습관대로 작가 태그를 잔뜩 넣으면 오히려 어색해진다.**

**그림체 자체를 따지는 사람에게는 NAI 가 여전히 대체하기 어렵다**는 평이 댓글에서 다수였다.
작가 태그를 왜 가중치만으로 못 섞는지(qwen3 인코더가 프롬프트를 통째로 인코딩해 임베딩이 평균으로 뭉개진다)는
이 문서의 "작가 태그는 `@`" 항목에 있다. 화풍은 [프롬프트 쓰는 법](prompting.md) 의 2단 구성 쪽이 정공법이다.

반대로 **Illustrious 에서 넘어온 사람 기준 ANIMA 의 장점**은 둘로 정리됐다.

- 자연어를 어느 정도 알아듣는다
- **디테일러를 따로 안 써도 눈이나 손이 덜 망가진다**

### 실제로 부딪힌 것들

| 증상 | 답 |
|---|---|
| 수위 있는 그림이 잘 안 나옴 | 퀄리티 태그 자리에 **`nsfw`**, 부정 프롬프트에 **`safe`** 를 넣어 본다 |
| 화면이 과하게 확대돼 나옴 (넣지도 않은 `feet out of frame` 이 들어감) | **부정 프롬프트로 하나씩 잡아 커스텀**해야 한다 |
| `cum on penis` 가 잘 안 그려짐 / `bikini_bottom_aside` 가 3장 중 2장 실패 | 로컬에서 겪은 구체적 실패로 남아 있다 |
| 자연어로 써 봤더니 태그보다 타율이 낮았다 | ANIMA 가 자연어를 받는다고 해서 **태그를 버릴 이유는 아니다** |

시작 워크플로우는 Civitai 의 `Anima (Preview) Workflow - V7.0` 베이직을 그대로 썼다.

→ [NovelAI](nai.md) · [프롬프트 쓰는 법](prompting.md) · [모델 고르기](models.md)

<small>근거 — [nai만 쓰다가 로컬 아니마로 넘어가봤는데 먼가 그림체가 시… 26.07](https://arca.live/b/aiart/175904931)</small>

## 와일드카드 팩 — 이미지를 `.zip` 으로 바꿔 받고, 문장 안에 끼워 넣는다
<small>2026-06 기준 · 근거 3건</small>

ANIMA 용 와일드카드 배포글은 **배포 방식과 문법이 둘 다 특이하다.**

### 배포 — 첨부 이미지의 확장자를 `.zip` 으로 바꾼다

```text
글에 올라온 이미지 원본 다운로드  →  확장자를 .zip 으로 변경  →  압축 해제
윈도우 기본 압축 기능으로 안 열리면  →  반디집 또는 7-Zip
```

그 이미지 자체에 **워크플로우 EXIF 도 살아 있어** 캔버스에 드래그하면 노드가 그대로 불러와진다.
*"안 열린다"* 는 문의가 실제로 있었지만 답은 **본문을 다시 읽으라**는 것이었다 — 방법은 위 그대로가 맞다.

### 문법 — 태그 나열이 아니라 **자연어 문장 안에** 끼워 넣는다

ANIMA 가 자연어 문장 조합을 이해한다는 점을 이용한 구조다. 제작자의 설명은 *"주어 is v-ing 솰라솰라"* 식으로
**`is` 로 계속 이어 붙이는 것**이다.

```text
1인 예시
(The first girl with __anima_2girls/anima_character3_hair_style__
 __anima_2girls/anima_character4_eye_color__
 { __anima_2girls/anima_character5_special_trait__ is|is}
 {__anima_2girls/anima_outfit_nsfw__|completely nude}
 and is __anima_2girls/anima_pose_1girl_tenta2__)

2인 구조
태그, 1번 캐릭터 [외모] 행동.  [??]  2번 캐릭터 [외모] 행동
   ↑ 대괄호 자리에 다른 와일드카드를 끼워 넣는다
   ↑ 또는 와일드카드 하나를 뽑아 반으로 나눠 각 주어 자리에 넣는다
```

### ⚠️ 완성도 — 제작자 본인의 평가가 갈린다

| 계열 | 타율 |
|---|---|
| 촉수 / 산란 / 슬라임 · 1girl 촉수 | **양호** |
| **2인 백합 체위 · 3P** | **결과가 심하게 무너져 하나씩 수동 테스트해야 했다.** 남자가 끼는 3P 는 시도조차 안 했다 |

제작자는 프롬프트를 제미나이로 뽑아 만들었고, *"1girl 촉수 외에는 퀄리티가 많이 허접하니
재미로만 굴리거나 직접 개조해 쓰라"* 고 스스로 밝혔다.

### 다인 캐릭터를 와일드카드로 굴릴 때의 이름 문제

이른바 **'오크의 가슴잡기' 프롬 작성법**(`https://arca.live/b/aiart/171855587`)은 다인에서 타율이 매우 좋은데,
**행동 프롬프트 안에도 캐릭터 이름을 다 넣어야 타율이 나온다.**
그래서 와일드카드로 캐릭터를 무작위 조합하면 이름이 어긋나 쓸 수 없다.

이 문제를 푸는 ComfyUI 커스텀 노드가 있다 — **캐릭터 프롬에 적힌 이름을 읽어
행동 프롬프트의 `Left girl` / `Right girl` / `Center girl` 을 실제 이름으로 치환**해 준다(3인까지).

```text
캐릭터 프롬 형식 (어기면 오류)
[위치 girl is 이름 \(외형 등등\).]

예) Left girl is tpp \( Deep skin, blund bangs, black hair, green eyes, O-ring top, ... \).
    Right girl is bbc \( blue twintails, short hair, purple eyes, large breasts, ... \).

행동 프롬
Left girl is kneeling on the Left boy and having sex in cowgirl position on the left.
Left boy is lying on his back. ...

설치   ComfyUI 의 custom_nodes 폴더에 파일을 그냥 넣는다
```

> ⚠️ 배포 링크는 **kio.ac** (본문에 base64 로 가려져 있었다). **보관 기간이 있는 임시 공유라 지금은 만료됐을 수 있다.**
> 작성자는 코딩을 전혀 모르고 AI 가 만들어 준 것이라 수정 요청은 받기 어렵다고 미리 밝혔다.

→ [프롬프트 쓰는 법](prompting.md) · [ComfyUI 쓰는 법](comfyui.md) · [자원](resources.md)

<small>근거 — [이상성욕)아니마용 촉수, 백합용 와일드카드 26.05](https://arca.live/b/aiart/169392958) · [아니마 Lefr girl, Right girl 이름 대체 커… 26.06](https://arca.live/b/aiart/173945456) · [대충만든 아니마 촉수, 2girls 보빔 or 3P or 촉… 26.04](https://arca.live/b/aiart/169192403)</small>

## 프롬프트 가중치의 실제 상한 — `4` 와 `15.3` 은 조건이 다르다
<small>2026-06 기준 · 근거 4건 · 자료 엇갈림</small>

앞의 "작가 태그는 `@`" 절은 **`4` 이상을 남발하면 연산이 깨져 검은 화면**이라고 적었다.
그런데 `15.3` 까지 올라간 실측이 따로 있다. **둘은 조건이 다르다. 덮어쓰지 않고 조건을 구분해 적는다.**

| | 조건 | 값 |
|---|---|---|
| 기존 (앞 절) | **일반 t2i**, 프롬프트 전체에 높은 가중치를 뿌리는 경우 | **`4` 이상 남발 → 검은 화면** |
| 2026-06 실측 | **lllite 인페인팅으로 구도를 고정**하고 **단일 태그 하나에만** 가중치를 준 경우 | **`15.3` 근처가 실질 최대** |

### 실측 (lllite 인페인팅 · 단일 태그)

구도가 튀면 비교가 안 되므로 예시 이미지에서 Sam 3 으로 대상만 따서 인페인팅으로 고정하고,
`(very small tiny microbikini:N)` 의 `N` 만 바꿔 가며 관찰했다.

| N | 결과 |
|---|---|
| `1.0` · `2.0` | 변화가 미미하다 |
| **`3.0`** | 여기서부터 확실히 체감된다 |
| `6.0` | 눈에 띄게 강해진다 |
| `13.0` | 형태가 겨우 남는다 |
| **`15.3`** | **실질적 최대치** (시드에 따라 형태가 거의 사라진다) |
| **`16.0` 이상** | ⚠️ **역전.** 오히려 되돌아가는 오버플로우가 나고, 그 뒤로는 **VAE 디코드에서 그림이 타 버린다** |

```text
같은 실험자 기준 SDXL 은 2.5 만 넘어도 그림이 타기 시작한다
```

### 왜 이렇게 높은 값이 필요한가 — 개발자 답변

`huggingface.co/circlestone-labs/Anima` 디스커션 **#135** 에 개발자 답변이 있다.

> 프롬프트 가중치는 적어도 ComfyUI 에서는 작동하며 문법은 SDXL 과 같다 —
> `you can (emphasize:2) certain words or phrases`.
> 구현은 확산 모델에 입력되는 **텍스트 인코더 벡터를 스케일링**하는 것이고,
> 확산 모델이 컨디셔닝에 대해 **크로스 어텐션**을 하는 방식 때문에 **SDXL 에서 쓰던 것보다 훨씬 높은 가중치가 필요**하다.

**실천 지침** — SDXL 습관대로 1.1, 1.2 로 찔끔 올리는 것은 사실상 무효다. `2` 부터 시작한다.
실제 배포글에서도 세부 묘사가 안 나올 때 `(long labia:2), (dark labia:2)` 처럼 2 를 주는 예가 나온다.
다만 댓글에는 **실사용 감각으로는 1.0 정도가 제일 낫다**는 반대 의견도 있었다.

*(2026-05 · 2026-06 두 글. 판은 BASE v1.0 시기다.)*

### 세 번째 증언 — "10 을 줘도 문제없다" *(2026-06-24)*

같은 글의 댓글 둘이 정면으로 어긋난다. **어느 쪽도 지우지 않고 병기한다.**

| 증언 | 내용 |
|---|---|
| A | *"NAI 가중치와 로컬 가중치는 차이가 커서 **IL 이든 ANIMA 든 1.5 를 넘기는 일은 사실상 없다**"* |
| B | *"**ANIMA 는 가중치 10 을 줘도 문제없고** 그만큼 더 강조된다"* |

조건(단일 태그인지 프롬프트 전체인지, 어느 판인지)이 명시되지 않아 판정할 수 없다.
위 표의 두 조건과 함께 **세 조건을 나란히 두고 자기 세팅에서 직접 재는 수밖에 없다.**

```text
조건 1  일반 t2i · 프롬프트 전체에 높은 값        →  4 이상 남발하면 검은 화면
조건 2  lllite 인페인팅 고정 · 단일 태그 하나에만  →  15.3 근처가 실질 최대, 16 이상은 역전
조건 3  (조건 불명, 2026-06 댓글)                →  1.5 를 넘길 일이 없다  vs  10 도 문제없다
```

> ⚠️ **여기서 말하는 '검은 화면' 과 헷갈리면 안 되는 별개 현상이 있다.**
> **ComfyUI 를 업데이트한 뒤 fp16 환경에서 SDXL 계열로 생성하면 검은 화면이 나오는** 보고가 있다(2026-07-29).
> 이쪽은 가중치와 무관한 **ComfyUI 버전 + fp16 조합 문제**이고, 이 때문에 IP-Adapter 를 못 쓰고 있다는 사례가 붙어 있다.
> 가중치를 낮췄는데도 검은 화면이면 fp16 쪽을 의심하라. → [오류 해결](troubleshooting.md)

<small>근거 — [Anima로 NAI 느낌 짤털 26.07](https://arca.live/b/aiart/178404708) · [마이크로 비키니 크기로 anima lllite 가중치 강도 … 26.06](https://arca.live/b/aiart/174717928) · [이미 공식에서 아니마는 프롬프트 가중치를 높게 줘야 한다고 … 26.05](https://arca.live/b/aiart/169840426) · [wai illustious SDXL은 아니마 프롬프트가 안먹… 26.06](https://arca.live/b/aiart/174739881)</small>

## 같은 시드로 반복하면 얼룩이 생긴다 — DiT 특유의 문제
<small>2026-05 기준 · 근거 1건</small>

**증상** — T2I → Hires → FaceDetailer 로 뽑았는데 디테일러를 거칠 때마다 이미지가 **더 쨍해지고 얼룩덜룩**해진다.
해상도·시드 등 조건은 전부 같은데 그렇다.

**원인은 시드다.** 같은 시드로 여러 번 I2I 를 돌리면 미세한 노이즈와 특징이 **증폭**된다.

```text
해결  →  Hires · FaceDetailer 등 I2I 단계마다 시드를 바꾼다 (예: 각각 +10)
```

시드를 바꾸자 디테일은 훨씬 살아나면서 얼룩이 사라졌다.

| 시도 | 결과 |
|---|---|
| 단계마다 시드 변경 | ✅ **해결** |
| Hires 를 **Ultimate SD Upscale**(타일 분할)로 교체 | ✅ 증상이 사라진다 |
| Hires 전 · FaceDetailer 전에 **VAE Decode → Encode** 삽입 | ❌ **증상 그대로** — latent 를 갈아 끼우는 것으로는 해결되지 않는다 |

> **SDXL 에서는 같은 시드를 써도 이 문제가 없었다**는 것이 글쓴이의 기억이고,
> Anima 가 DiT 기반이라 달라진 것으로 추정했다. 댓글도 SD 계열보다 Anima 가 이 현상에 민감하다는 쪽이다.
> Ultimate SD Upscale 이 잘 됐던 이유도 타일 분할 방식이기 때문으로 보인다.

*(2026-05-16, BASE v1.0 정출 직후. 한 글의 추적이지만 재현 절차와 실패한 우회까지 남아 있다.)*

→ [업스케일과 화질](upscale.md) · [디테일러](detailer.md)

<small>근거 — [아니마 I2I or 디테일러 과정에서 노이즈가 발생하는 현상… 26.05](https://arca.live/b/aiart/170831609)</small>

## int8 양자화를 기본값으로 돌리면 — 무엇이 어긋나고 어디를 남기나
<small>2026-07 기준 · 근거 5건 · 자료 엇갈림</small>

"경량화되고 빠르다니 그냥 돌리면 되겠지" 를 실제로 검증한 글이 있다. **결론은 '안 괜찮다'** 다.

### 기본 설정 그대로 양자화하면

파인튜닝판 `anima_aestheticV11` 을 원본으로 두고 **ComfyUI 공식 스크립트(comfyui-model-tools) · StarNodes 모델 컨버터 · INT8(W8A8)**
세 가지로 각각 **블록 제외 없이 기본값 그대로** 양자화한 뒤 8종의 프롬프트로 비교했다.

> 큰 구도는 무너지지 않지만 **모든 양자화판에서 일관되게 디테일이 어긋났다** —
> 우산 디테일, 배경 사당, 전봇대, 보도블럭과 철문, 그림자, 원근감, 치마 주름, 리본.
> 한 장은 아예 **앉은 각도와 그에 따른 배경 각도까지** 틀어졌다. 배경만이 아니라 인물 디테일이 변한 사례도 나왔다.

> ⚠️ **[모델 고르기](models.md) 의 "양자화 파일 고르기" 항목은 반대에 가까운 수치를 싣고 있다** —
> 공식 툴로 *"아무 옵션 없이 양자화해도 상대 오차 2% 미만, 코사인 유사도 최저 0.999936"* 이라는 것이다.
> **수치상의 오차가 작은 것과 그림이 같게 나오는 것은 다르다**는 것이 이 글의 요지다. 양쪽을 병기한다.

### 어느 레이어를 남길 것인가 *(댓글 지침 — 이 글의 가장 값진 부분)*

| 지침 | 내용 |
|---|---|
| `qkv` · `o` projection | ⚠️ **하나라도 bf16 이면 어차피 bf16 속도를 따라간다.** Anima 를 양자화하는 이유는 VRAM 이 아니라 속도이므로 이 점만 주의하면 된다 |
| `adaln` · `mlp` | **양자화에 민감해 보였다** |
| `layer 0` · `layer 1` | **통짜로 bf16 유지**를 추천 — 결과를 bf16 과 비슷하게 하려면 |
| relerr | comfyui-model-tools 기준을 **엄격히** 잡아 몇 블록을 더 제외하면 변화가 확 준다 |

### 판별 실측 — 형식별로 얼마나 빨라지나

| 판 | 형식 | 실측 |
|---|---|---|
| PREVIEW (2026-02) | **FP8** | 30스텝 BF16 3.99it/s·8.63초 → FP8 4.61it/s·7.14초. sage attention 을 더하면 4.39 → 5.16it/s. **약 20% 에 그치고 품질은 떨어진다** → 당시 결론은 *"그냥 BF16 을 쓰는 게 맞다"*. WebUI 계열에서는 아예 동작하지 않는다 |
| PREVIEW (2026-02) | **INT8 tensorwise** | 832x1216·CFG 4.0·30스텝 기준 BF16 대비 **RTX3090 +53.3%**(1.70→2.58it/s) · **RTX3060 +25.7%** · **RTX5090 +18.8%**. **구형 카드일수록 이득이 크다.** 그래도 같은 조건 SDXL 보다는 **35~53% 느리다** |
| PREVIEW (2026-02) | **INT8 rowwise** | tensorwise 는 레이어 하나가 FP32 스케일 하나를 공유하지만 **rowwise 는 row 마다 스케일을 따로 가져 손실이 훨씬 적다** |
| **BASE v1.0** | `anima-base-v1.0-int8rowwise` | 30스텝 BF16 6.35it/s·5.63초 → 8.54it/s·4.57초. 0번뿐 아니라 **27번(마지막) 블록도 bf16 으로 남겼다** |

### `dynamic_lora` 스위치 — BASE v1.0 int8rowwise 를 쓸 때 가장 중요한 것

| | 결과 |
|---|---|
| **켬** | BF16 과 유사한 결과. 대신 속도 향상 폭이 작아진다 |
| **끔** | 빠르다. 대신 **LoRA 가 잘 안 먹혀 강도를 `1.5~1.7` 까지 올려야 한다** |

```text
필수 옵션   sage attention + torch.compile + --disable-dynamic-vram
로더        Load Diffusion Model (INT8)   ← 체크포인트 로더에 넣으면 안 된다
Forge Neo   BufferError: Failed to load diffusion model  (ComfyUI 전용)
```

⚠️ **INT8 은 LoRA 반응이 약하고 작가 태그 결과물이 꽤 달라진다.** 속도가 꼭 필요한 사람만 쓰는 것이 맞다.

*(2026-02 PREVIEW ~ 2026-07 aesthetic v1.1. 최적화를 한꺼번에 붙였을 때의 실측 한 벌은 위 "int8 양자화로 SDXL 만큼" 절에 있다.)*

<small>근거 — [anima-base-v1.0-int8rowwise 26.05](https://arca.live/b/aiart/170720836) · [Anima FP8 양자화 모델 26.02](https://arca.live/b/aiart/161167531) · [Anima-INT8Rowwise 모델 26.02](https://arca.live/b/aiart/163367034) · [Anima를 INT8 양자화 해보았다. 26.02](https://arca.live/b/aiart/162298399)</small>

??? note "근거 5건 전부 보기"
    [anima-base-v1.0-int8rowwise 26.05](https://arca.live/b/aiart/170720836) · [Anima FP8 양자화 모델 26.02](https://arca.live/b/aiart/161167531) · [Anima-INT8Rowwise 모델 26.02](https://arca.live/b/aiart/163367034) · [Anima를 INT8 양자화 해보았다. 26.02](https://arca.live/b/aiart/162298399) · [(anima) 무지성으로 int8 양자화를 시도해도 괜찮을까? 26.07](https://arca.live/b/aiart/178163658)

## 병합·파인튜닝의 한계 — 'BASE 성능이 전부' 라는 관측
<small>2026-07 기준 · 근거 5건</small>

채널에서 Anima 병합·파인튜닝을 여러 번 돌려 본 사람들이 남긴 관측이다. **방향이 한쪽으로 모인다.**

### 최신 부품이 병합에서 더 나은 결과를 주지 않는다

고속 LoRA 병합 모델을 더 최신 `anima_turbo` 로 갱신해 보라는 제안에 대한 제작자의 답이다.

> 실제로 해 봤지만 **CFG 부스팅으로 색감이 너무 진해지고 미적 성능이 저하돼** 조합식을 여러 번 바꿔도 극복하지 못하고 포기했다.
> **단독 사용으로는 최신 버전이 더 좋지만, 병합은 돌연변이 모델을 만드는 과정이기도 해서** 최신 부품이 항상 더 나은 결과를 주지는 않는다.

### 소형 DiT 에서는 BASE 성능이 전부다

> 병합이나 소규모 튜닝 모델은 점점 의미가 사라지고 있다. **소형 DiT 아니메 모델에 Aesthetic 튜닝을 하면
> BASE 모델이 가진 아니메 지식을 잃어버리기 시작**한다는 것이 점점 확실해지는 분위기이고,
> 여러 DiT 모델을 병합·튜닝해 본 소감으로는 **Unet 시절의 모델 튜닝 공식이 DiT 에서는 깨진 지 오래**라
> 오직 **BASE 모델의 성능만이 모든 것을 결정**하게 될 것이다.

같은 방향의 관찰이 셋 더 있다.

| 관찰 | 내용 |
|---|---|
| Anzhc `AAAAnima` | 이전 판은 **베이스보다 살짝 미묘했고 일부 지식 망각**(원래 알던 캐릭터·개념을 잊는 현상)이 있었다. 파인튜닝 Anima 를 고를 때 확인할 지점이 바로 이 지식 망각이다 |
| `Anitional` 제작 동기 | 기존 Anima 파인튜닝들을 테스트해 보니 **베이스 대비 한쪽이 좋아지면 다른 쪽이 무너지거나**, 기본 그림체를 밀어 넣으면서 Anima 의 장점이 희석되는 경우가 많았다 |
| 고속 병합 모델 제작자 | 스스로 *"사실상 혼자 쓰려고 만든 잡탕 모델이며 고속 모델답게 타율은 나쁜 편"* 이라고 밝힌다 |

> **실천으로 옮기면** — 파인튜닝판을 찾아 헤매기보다 공식 BASE / Aesthetic 을 쓰고,
> 필요한 것은 로라로 얹는 편이 낫다는 시각이다. *(단정이 아니라 제작자들의 관측이다. 반대 방향의 자료는 아직 없다.)*

### 그래도 고속 병합 모델을 쓴다면

| 항목 | 값 |
|---|---|
| 샘플러 | `er_sde` |
| CFG | **`1.0`** — 터보/증류 로라가 이미 병합돼 네거티브 경로를 쓰지 않기 때문이다 |
| 스텝 | **`7` 이상** |
| 해상도 | 512x512(0.25MP) ~ 1280x1280(1.50MP) |

병합 모델 `Anitional-v1.0-int8c` 처럼 다른 값을 권하는 것도 있다 —
`euler a cfg pp` / `AYS`(ComfyUI-ppm 필요) / CFG `2~3.5` / 스텝 `16~28` / shift 는 기본 3 에서 **`3.5`**.
**다른 로라를 섞을 때는 로라 강도를 적당히 줄이는 게 낫다**는 조언이 붙어 있다.

→ [모델 고르기](models.md) · [자원](resources.md)

<small>근거 — [(모델공유) Anitional-v1.0-int8c (병합모델) 26.07](https://arca.live/b/aiart/178360790) · [Anzhc/AAAAnima not so early 26.07](https://arca.live/b/aiart/176018707) · [그냥 또 만든 고속 LoRA 병합 Anima 모델 (INT8… 26.07](https://arca.live/b/aiart/177115790) · [그냥 만든 고속 LoRA 병합 Anima 모델 (INT8 버… 26.07](https://arca.live/b/aiart/176416762)</small>

??? note "근거 5건 전부 보기"
    [(모델공유) Anitional-v1.0-int8c (병합모델) 26.07](https://arca.live/b/aiart/178360790) · [Anzhc/AAAAnima not so early 26.07](https://arca.live/b/aiart/176018707) · [그냥 또 만든 고속 LoRA 병합 Anima 모델 (INT8… 26.07](https://arca.live/b/aiart/177115790) · [그냥 만든 고속 LoRA 병합 Anima 모델 (INT8 버… 26.07](https://arca.live/b/aiart/176416762) · [간단한 고속 LoRA 병합 Anima 모델 26.06](https://arca.live/b/aiart/172494759)

## 고속화 — cfg_pp 로 스텝 반 토막, 그리고 4스텝 로라
<small>2026-07 기준 · 근거 3건</small>

위 "터보(고속) 로라 3종 실측" 이 로라별 비교라면, 여기는 **로라 없이 스텝을 줄이는 길**과 **4스텝 로라**다.

### 고속화 로라 없이 스텝을 반 토막 — cfg_pp 계열 샘플러

Anima 권장 스텝은 보통 30~50, 못해도 24~28 인데 스텝 수가 생성 시간의 대부분을 차지한다.
샘플러를 **cfg_pp 계열**로 바꾸고 CFG 를 낮추면 스텝을 크게 줄일 수 있다.
*(cfg_pp = CFG 적용 방식을 바꿔 낮은 CFG·적은 스텝에서도 붕괴가 덜하게 만든 변형이라, CFG 를 기본값보다 낮게 잡는 것이 정상이다.)*

```text
샘플러  euler_ancestral_cfg_pp     스케줄러  normal
CFG     3.5  (권장 범위 2~4)        스텝      12
```

| 스텝 | 시간 |
|---|---|
| 12 | **15.51초** |
| 24 | 30.08초 |

정확히 절반이다. 그림이 달라지긴 하지만 12스텝 쪽이 못 볼 수준은 아니라는 평가.
이 방식에서 원래 가장 좋은 스케줄러는 **AYS** 인데 기본 ComfyUI 에서는 SD 계열에만 쓸 수 있고,
`https://github.com/pamparamm/ComfyUI-ppm` 을 넣으면 쓸 수 있다.
기본 제공 중에는 `ddim_uniform` · `sgm_uniform` · `simple` 이 문제없이 동작한다.
**cfg_pp 는 고속화 로라와 섞어 써도 괜찮다**는 반응이 댓글에 있다.

> ⚠️ **다만 cfg_pp 샘플러는 KJNodes 의 `Scheduled CFG Guidance` 와 충돌해 그림이 탄다.**
> 위 "같이 쓰면 안 되는 조합" 절 참조.

### 4스텝 터보 로라

`huggingface.co/sorryhyun/anima-turbo-4step` 의 `anima_turbo_4tep.safetensors`.

```text
샘플러 er_sde   step 4   cfg 1
```

| 환경 | 속도 |
|---|---|
| M1 Pro (맥) · 512x512 | 11~13초 — **맥에서도 돌아간다는 것을 확인해 준 드문 자료다** |
| RTX 5070 Ti · 1024x1024 | **1.2초** |

⚠️ **대가** — Anima 가 원래 약한 **텍스트 렌더링이 특히 더 취약**해지고,
**시드를 바꿔도 비슷한 이미지가 나온다**(다양성 감소는 증류·가속 로라의 전형적 부작용이다).

*(2026-02 PREVIEW · 2026-07. 앞의 "가속 — 무엇이 얼마나" 표와 함께 볼 것.)*

<small>근거 — [(모델공유) Anitional-v1.0-int8c (병합모델) 26.07](https://arca.live/b/aiart/178360790) · [아니마 챈에 올리는 고속화로라없이 스탭줄이는 날먹셋팅팁 26.02](https://arca.live/b/aiart/161175343) · [하지만 빨랐죠? 자작 4스텝 로라 정식버전 업데이트 26.07](https://arca.live/b/aiart/177065984)</small>

## 이 캐릭터를 아는가 — 학습 커트라인은 찔러 봐야 안다
<small>2026-05 기준 · 근거 1건</small>

학습 데이터가 공개되지 않은 모델이라 **어떤 캐릭터를 아는지 알아내려면 프롬프트로 직접 찔러 보는 수밖에 없다.**
캐릭터 로라를 구울지 말지 정하기 전에 이 테스트를 먼저 하면 시간을 아낀다.

로라 없이 캐릭터 태그(이름만, 외형 묘사 없이)로만 찔러 본 결과다 *(BASE v1.0)*.

| | 태그 |
|---|---|
| ✅ 성공 | `the herta \(honkai: star rail\)` |
| ❌ 실패 | `nefer \(genshin impact\)` · `aemeath \(wuthering waves\)` · `lynae \(wuthering waves\)` |

**댓글에서 정리된 추정 커트라인**

| 작품 | 어디까지 |
|---|---|
| 명조 | '라하이로이' 이전까지 |
| 붕괴 스타레일 | 3버전까지 대체로 |
| 원신 | 라우마가 나오는 것으로 보아 공월노 극초반까지 |

그보다 뒤에 나온 캐릭터는 로라를 직접 구워야 한다.

> **표기 주의** — `the_herta_(honkai:_star_rail)` 처럼 언더바로 이어 쓰면 인식이 달라진다.
> 단부루 원본 표기는 언더바지만 **Anima 쪽은 공백 표기가 안전**하다. 괄호는 `\(` `\)` 로 이스케이프한다.

*(한 글의 테스트다. 커트라인은 추정이므로 쓰려는 캐릭터는 직접 찔러 볼 것.)*

→ [자원](resources.md) · [로라 쓰는 법](lora-usage.md)

<small>근거 — [anima base 캐릭터 테스트 26.05](https://arca.live/b/aiart/171041987)</small>

## 파생 체크포인트 고르기 — 4종 비교, 그리고 다수는 그냥 aesthetic 1.1 을 쓴다
<small>2026-08 기준 · 근거 3건 · 자료 엇갈림</small>

ANIMA 파생 체크포인트를 자작 로라로 실제 비교한 자료다 *(2026-08-04)*.

| 판 | 강점 | 약점 |
|---|---|---|
| **wai** | **원작 그림체·스타일·색감 재현 1위** | |
| **nova** | **프롬프트 추종 1위** (최신 버전으로 자주 업데이트된다). 스타일도 두 번째로 잘 따라온다 | |
| **yume** | 무난 | ⚠️ 동일 세팅에서 **저화질 이미지처럼 뽑히는** 사례가 따로 보고됐다 (아래) |
| **miao** | 넷 중 **순수 퀄리티 1위** | **스타일과 그림체를 다 죽여 버려** AI 특유의 느낌이 강하다 |

그 밖에 언급된 파생판 — `reanimate v2` · `nyaIrisAnima` · `reedAnimaXXX`.

### 그런데 댓글의 다수 의견은 "그냥 베이스"

| 근거 | |
|---|---|
| 자작 로라를 쓸 정도면 | **파생 체크포인트보다 베이스 모델이 찐빠가 가장 적다** |
| 실제로 가장 많은 답 | **`anima-aesthetic-v1.1`.** *"1.0 쓰다가 1.1 로 넘어왔는데 1.1 이 저점이 더 높다(최악의 결과가 덜 나쁘다)"* |
| 로라 재현도 실측 *(2026-08-04, 별개 글)* | 동일 로라·동일 프롬프트에서 **base v1.0 및 다른 체크포인트보다 aesthetic 1.1 이 원본 레퍼런스와 가장 유사**했다. 이유는 *"체크포인트를 쓰면 그 체크포인트가 가진 고유한 특성을 너무 강하게 따라가는 것 같다"* |

> 그래서 **캐릭터 로라의 재현도를 말할 때는 어느 판에서 뽑았는지를 반드시 함께 적어야 한다.**

### ⚠ 영상(Wan I2V)용이면 판단이 뒤집힌다

Wan 으로 영상을 자주 뽑는 사용자는 **`miao`** 를 쓴다.
**피부 묘사가 현실감 있어 Wan 이 굉장히 잘 인지하고**, 로라를 학습했을 때 뿌옇게 나오는 특유의 배경 톤도 줄어든다.

```text
스틸 그림체 재현  →  wai  또는  베이스 aesthetic 1.1
영상(Wan I2V)용   →  miao
```

### ⚠ YumeAnima 만 저화질처럼 나오는 사례 *(2026-06-28, 한 글)*

챈 배포 '심플 ANIMA 워크플로우' 로 **모든 세팅을 똑같이 맞췄는데** 하샤쿠 계열과 waiAnima 는 괜찮고
**YumeAnima 만 그림체나 퀄리티 문제가 아니라 아예 저화질 이미지처럼 뽑혔다.**
같은 워크플로우라도 파생 체크포인트마다 요구하는 세팅이 다를 수 있다는 뜻이다.
(같은 글에서 `@fujimoto tatsuki` 를 넣어도 그 작가의 '그림 대충 그리던 시절' 화풍만 나오고 `year` 태그로도
조절되지 않았다는 관찰이 함께 나왔다 — 학습 데이터 분포가 쏠려 있으면 태그만으로 전성기 화풍을 끌어올 수 없다.)

→ 판 이름과 계보는 위 '판 계보' 절, 받는 곳은 [자원](resources.md)

<small>근거 — [GPT로 아니마 캐릭터 만들기 중간결과 26.08](https://arca.live/b/aiart/178985085) · [다들 아니마 체크포인트 뭐 씀 26.08](https://arca.live/b/aiart/178971620) · [혐주의) 아니마 만져보는데 이건 뭐가 문제일까 26.06](https://arca.live/b/aiart/175249876)</small>

## 판을 올리면 과거 그림체가 사라진다 — 연작은 판을 고정하라
<small>2026-08 기준 · 근거 2건</small>

연작이나 시리즈를 이어 갈 계획이라면 이것부터 알아 둬야 한다.

> **"로컬 모델을 모두 업그레이드한 상황이라 그때 그 그림체가 더 이상 나오지 않는다"**
> — 장편 만화 제작자가 과거 시리즈를 리메이크하지 않는 가장 큰 이유로 든 것이다 *(2026-08-07)*.

| 대처 | |
|---|---|
| 판 고정 | 연작을 시작할 때 쓴 체크포인트 파일을 그대로 보관한다 |
| 데이터셋 확보 | 그 그림체로 뽑은 결과를 모아 로라로 구워 둔다 (제작자 본인의 계획도 이쪽이었다) |

### ⚠ 디노이즈를 낮춰도 그림체는 보존되지 않는다

기존 Illustrious 그림체를 지키면서 ANIMA 성능만 빌리려는 절충 워크플로우가 쓰인다 *(2026-08-05)*.

```text
밑그림 · 초안        →  기존(IL) 모델
디테일러 · 업스케일  →  ANIMA
그 뒤 인페인트 여러 번으로 홍조 · 의상 손보기
```

왜 이렇게 하느냐 — **ANIMA 로만 생성하면 기존 작가 프롬프트와 ANIMA 용 작가 스타일 로라를 함께 써도
원하는 그림체가 재현되지 않았기 때문**이다. 구체적 증상은 색감 변화에 더해
*"히나의 미간이 골프장 사이즈로 자꾸 나오는"* 얼굴 비례 붕괴였다.

> ⚠️ **함정** — 마무리를 ANIMA 로 돌릴 때 **디노이즈 값을 조절해도 기존 그림체가 싹 증발한다.**
> 기존 느낌이 남을 때까지 무한 수정을 반복해야 했다는 것이 글쓴이의 기록이다.
> 디노이즈를 낮추는 것만으로는 그림체가 보존되지 않는다.

비슷한 분업 사례로 **GPT 가 기본 캐릭터·장소·상황을 만들고 GPT 가 못 만드는 NSFW 만 ANIMA 인페인터로 고치는**
방식도 있는데, 퀄리티에는 만족했으나 1편 완성에 상상을 초월할 만큼 시간이 걸렸다고 한다.

→ 로라로 그림체를 붙잡는 쪽은 [로라 쓰는 법](lora-usage.md), 판 이야기는 위 '판 계보' 절.

<small>근거 — [<장래를 약속한 소꿉친구 그녀의 NTR 추억> 1편 26.08](https://arca.live/b/aiart/179279560) · [내가 이겼다 아니마 26.08](https://arca.live/b/aiart/179030080)</small>

## 속도 — 실행 인자 `--fast --gpu-only`, 그리고 VRAM 6GB 는 고장이 아니다
<small>2026-05 기준 · 근거 1건</small>

*"아니마가 제 성능을 내지 못하는 것 같다"* 는 질문에서 정리된 것 *(2026-05)*.

| 관찰 | 답 |
|---|---|
| **VRAM 을 6GB 밖에 안 쓴다** | **고장이 아니다.** 모델 자체가 작아서 그런 것이고 윈도우 자체 점유까지 생각하면 **6~7GB 언저리가 정상**이다 |
| **느리다** | ANIMA 는 파일 용량과 상관없이 모델이 무거워 **SDXL 대비 약 2배 느리다** |
| **자연어가 안 먹는다** | 한 문장만 덧붙이면 안 된다. **공식도 최소 2문장 이상 서술을 권한다.** 적당히 길게, 객관적으로 묘사할 것 |

### 실행 인자 하나로 180초 → 120초

```text
ComfyUI 실행 인자에   --fast --gpu-only
```

4060Ti 16GB + DDR5 32GB · **1344x1344 + 1.6x 업스케일** 기준으로 180초(3분)가 **120초대로 안정**됐다.

참고 비교값 — 프리뷰3 판 · 4070 Super · **832x1216 한 장에 30초 남짓**(해상도가 다르니 직접 비교는 불가).
VRAM 로드가 꼬여 시간이 늘어나는 경우가 있으니 **SageAttention / Triton 을 빼고 한 번 돌려 보라**는 제안도 나왔다.

→ 가속 노드를 붙이는 순서는 위 '가속을 붙이는 순서' 절, [VRAM·속도 최적화](vram.md)

<small>근거 — [후타주의) 아니마가 제 성능을 내지 못하는 것 같아요 26.05](https://arca.live/b/aiart/171021817)</small>

## 터보(고속) 로라의 대가 — CFG 1 이면 네거티브가 죽는다
<small>2026-08 기준 · 근거 1건</small>

터보 로라는 `steps 8 / cfg 1` 로 돌린다. 여기서 놓치기 쉬운 결과가 하나 있다.

> **CFG 가 1 이라 네거티브 프롬프트가 아예 먹지 않는다.**

네거티브에 아무리 적어도 반영되지 않으므로, 빼고 싶은 요소는 **NegPiP** — 개별 토큰에 음수 가중치를 먹이는
확장/노드(설명: `https://arca.live/b/respectai/135469379`) — 로 눌러야 한다.
`3hands` 같은 것을 NegPiP 쪽에 넣어 보라는 조언이 함께 나왔다.
'터보 로라를 쓰면 품질이 떨어진다' 는 지적도 붙어 있다.

### 곁가지 — 찐빠 원인을 가리는 절차

같은 글에서 나온 진단 순서가 실용적이다. 손이 분열된다는 질문에 **다른 사람이 같은 프롬프트를 그대로 넣어
돌려 봤더니 찐빠가 나지 않았다.**

```text
남이 같은 프롬프트로 돌려서 멀쩡하다
        ↓
프롬프트 문제가 아니다  →  체크포인트 또는 로라를 의심한다
        ↓
로라를 하나씩 꺼 가며 범인을 찾는다
과적합이 의심되면 로라 가중치를 낮춘다
```

손 자세는 태그를 나열하는 대신 *"한 손은 펠라 제스처, 다른 손은 무릎 위"* 식으로
**자연어로 풀어 쓰면 타율이 오른다.**

→ 터보 로라 실측값은 위 '터보(고속) 로라 3종 실측' 절, 절차 일반론은 [오류 해결](troubleshooting.md)

<small>근거 — [아니마 원래 손찐빠가 좀 심한가용 26.08](https://arca.live/b/aiart/179393628)</small>

## ANIMA 가 약한 것 — 국소 부위 묘사, 그리고 웹 버전(WebGPU)
<small>2026-06 기준 · 근거 4건</small>

### 국소 부위(여성기·음핵) 묘사 품질이 낮다 — 판의 알려진 약점

세 글이 같은 증상을 말한다 *(2026-06)*.

- 그림체(작가 태그·스타일 로라)에 따라 **편차가 크다.** 어떤 그림체는 아무것도 안 넣어도 잘 나오고 어떤 그림체는 무엇을 해도 안 나온다
- `erect clitoris` 는 **가중치를 높게 줘도 결과가 거의 달라지지 않거나 갑자기 후타나리를 그려 버리는 급발진**이 일어난다
- 옆구리에 주름이 너무 많이 지고 가슴 묘사도 약하다는 지적이 붙었다
- *"이런 마이너한 부위 묘사는 `ilxl`(Illustrious) 계열이 더 나아 보인다"* 는 체감

| 완화책 | |
|---|---|
| 업스케일을 붙인다 | 눈에 띄게 나아진다 (하이레스만 쓰고 있었다면 특히) |
| 태그 | `clitoris`, `clitoris hood` 를 함께 넣는다 |
| 작가 태그 | `cosine` · `nezunezu` · `shungikuten` |

> **다만 "조금 나아지는 수준이지 해결책은 아니다" 라고 못을 박았다.** 근본 해법은 직접 로라 학습이라는 것이 중론이다.
> 전용 로라가 올라온 적이 없다는 지적도 함께 나왔다. → [로라 쓰는 법](lora-usage.md)

### 웹 버전(브라우저 WebGPU)의 한계 *(2026-06-20)*

| 제약 | |
|---|---|
| 모델 재로드 | **한 모델을 로드한 뒤 다른 모델을 로드하면 뻗는다** — 모델 간 비교가 어렵다 |
| 시드 고정 | 시드를 고정한 채 모델만 바꿔 테스트하는 방법을 찾지 못했다 |
| 원인 | **WebGPU 는 원래 VRAM 이 질질 새는 구조이고 플랫폼 자체 문제**라 고치기 어렵다 |
| 해결 | **모든 문제는 설치형(로컬 ComfyUI 등)으로 가면 해결된다** |

*(웹 버전 질문에는 '배포처 권장 프롬프트를 못 봤다' 는 사례도 있는데, 그 깡모델도 어딘가에서 받은 것이니
제작자가 적어 둔 적정 태그를 참고하라는 답이 달렸다.)*

<small>근거 — [아니마web 모델별 질문 26.06](https://arca.live/b/aiart/174417723) · [anima 쓰는 사람들 클리 잘 나오나 26.06](https://arca.live/b/aiart/175044736) · [뷰지랑 꼭지 쫀득하게 하는 로라추천 문질 26.06](https://arca.live/b/aiart/174452999) · [아니마 뷰지가 너무 이상한데 잘나오게 하는 방법 있음?ㅠ 26.06](https://arca.live/b/aiart/173469736)</small>

## IL·Pony 프롬프트를 그대로 가져올 때 — 되풀이되는 실수 넷
<small>2026-06 기준 · 근거 4건</small>

ANIMA 로 넘어와 *"프롬프트가 안 먹는다"* 는 질문의 원인은 대체로 하나다 —
**Illustrious · Pony · SD1.5 시절 프롬프트를 그대로 들고 온 것.**

| 실수 | 무엇이 문제인가 |
|---|---|
| **화풍 형용구 남발** | `refined anime illustration, clean polished 2D anime rendering, soft flat cel shading, low dynamic range lighting …` 를 수십 개 늘어놓는 것. *"SD1.5 시절 고봉밥 프롬프트"* 라는 지적이 붙었다. **danbooru 태그 위주로 다이어트할 것** |
| **빈 쉼표와 줄바꿈** | `,,,,` 와 줄바꿈이 난무하는 프롬프트. ANIMA 는 서식에 이례적으로 민감하다 |
| **과한 가중치 남발** | `(buttjob:2), (deep skin:2), (looking back:1.7), (skinny:1.5)` 처럼 마구 올린 것 — 전부 걷어내고 **가중치 없는 평범한 태그 나열 + 자연어 설명**이 정답에 가깝다 |
| **같은 내용을 두 번 붙이기** | 반영률만 떨어진다 |

### 없는 태그를 지어 쓰지 말 것

`Tooking down` 처럼 **존재하지 않는 태그**를 쓰면 그냥 자리만 차지한다.
자연어로 쓰고 싶으면 제대로 된 문장형으로 쓰고, 아니면 정확한 danbooru 태그를 찾아 쓴다.
*(채널에서 확인된 없는 태그·오타 태그 사례는 [프롬프트 쓰는 법](prompting.md) 의 '태그를 고르는 법' 절에 모여 있다.)*

### 물리적으로 모순되는 태그를 함께 쓰지 말 것

| 하지 말 것 | 할 것 |
|---|---|
| `spread legs` + 팬티를 허벅지에 걸치기 | 팬티가 늘어나야 하므로 성립하지 않는다 → `spread legs` 를 빼거나 **`panties around one leg`** |
| 앉아서 앞으로 숙인 자세에 `bent over` | **`leaning forward`** |
| `spread legs` + `knees together feet apart` | 서로 모순 |
| `covering crotch` / `covering privates` | 목적과 반대이므로 뺀다 |
| 스스로 벗는 동작 | `undressing`. 그래도 다른 옷을 벗으면 편법으로 `adjusting panties` 추가 |

### 출발점은 배포처 프롬프트

> *"다 지우고 CivitAI 샘플 사진의 프롬프트를 그대로 따라 하면 엄청 잘 나온다"* — 질문자 본인의 말이다.

모델을 받은 곳에 권장 긍정 프롬프트가 적혀 있으면 그것을, 없으면 **CivitAI 예시 이미지를 눌러 어떤 프롬프트를
썼는지 보는 것**이 가장 안전하다. 태그는 복붙하지 말고 하나씩 danbooru 에서 검색해 뜻을 이해하고 쓴다.

*(전신이 잘려 나올 때는 해상도 비율 문제일 가능성이 커서 `wide shot` 을 넣어 보고, 세로로 긴 캔버스를 쓴다.)*

→ 표기 규칙은 위 '작가 태그는 `@`' 절. ANIMA 는 **reForge Neo 에서도 구동된다**(2026-05·06 두 글에서 확인).

<small>근거 — [로컬 anima로 팬티 내리기 태그 하는데 26.06](https://arca.live/b/aiart/173497043) · [포지네오 아니마 프롬프트 질문좀 26.06](https://arca.live/b/aiart/174213477) · [anima wep 전신이미지 안나옴 26.06](https://arca.live/b/aiart/174211583) · [anima 쓸려고 리포지 네오로 바꿧는데 26.05](https://arca.live/b/aiart/172355759)</small>

## 자세·구도가 안 잡힐 때 — 가중치를 올리지 말고 충돌하는 것을 지운다
<small>2026-08 기준 · 근거 3건</small>

### `head_back` 이 가중치 3.0 에도 안 먹은 진짜 이유 *(wai anima base1.0, 2026-06-05)*

질문자 프롬프트에는 눈 묘사 태그가 잔뜩 들어 있었다 —
`(gradient eyes:1.3), detailed iris, long eyelashes, (red eyes:2.0), beautiful detailed eyes, perfect eyes, simple eyes, (clear eyes:1.5)`.

> **눈을 이렇게 강하게 강조해 두면 모델이 눈을 포함한 얼굴을 계속 정면으로 그리려 하기 때문에
> 고개를 젖히는 태그가 이길 수 없다.** 눈 관련 태그를 싹 지우자 `head_back` 이 즉시 작동했다.

**자세 태그가 안 먹을 때는 가중치를 더 올릴 것이 아니라, 그 자세와 충돌하는 부위 강조 태그를 먼저 지운다.**

곁가지 실측 — `head back` · `turning head` · `head down` 처럼 고개를 돌리는 태그는 원래 가중치를 좀 줘야 하는데,
**같은 태그도 판에 따라 필요한 값이 다르다.**

```text
ANIMA  →  2
ILXL   →  1.5
```

### 인물이 화면에서 거꾸로 뒤집힐 때 *(2026-06-14)*

`lying` 이나 `on back` 둘 중 하나만 들어가도 같은 시드에서 꾸준히 머리가 아래로 뒤집힌 구도가 나오는데,
**danbooru 에는 이 구도를 지정하는 태그가 따로 없다.**

| 시도 | 결과 |
|---|---|
| 네거티브에 `upside_down` | ❌ 효과 없음 — **구도를 네거티브로 고치는 것 자체가 잘 안 된다** |
| 포지티브에 `head at the top`, `from above head` | 중간 단계 조언 |
| **최종 해결** | `(head positioned near the top of the frame^head at the top^upper body at the top:3)` — **같은 뜻의 표현 셋을 `^` 로 묶어 가중치 3** 을 주자 정상화됐다(글쓴이 확인) |

### 배제형 자연어는 반영되지 않는다 *(2026-08-06)*

`Only the taller man's hands and his penis are visible in the image, no other part of the taller man is shown.`
처럼 **"X 만 보이고 나머지는 보이지 않는다" 는 배제형 서술은 ANIMA 자연어에서도 잘 먹지 않는다.**

그 구도에 해당하는 danbooru 태그를 쓰는 편이 확실하다 —
`disembodied hand` · `disembodied penis` · `out of frame` · `faceless male`.

<small>근거 — [head_back 태그가 안 먹음 (wai anima bas… 26.06](https://arca.live/b/aiart/172856945) · [보추주의) 상대방 손하고 자지만 보이는 그런 투시? 형태는 … 26.08](https://arca.live/b/aiart/179089265) · [이런 구도 안 나오게 하는 네거같은거 없을까 26.06](https://arca.live/b/aiart/173775104)</small>

## 파인튜닝·병합판을 쓸 때 — `NAI_ANIMA_2dac_v0.3` 배합과 챈산 판 주의
<small>2026-08 기준 · 근거 2건</small>

### `NAI_ANIMA_2dac_v0.3` — 로라가 아니라 순수 병합 모델 *(2026-08-09)*

받는 곳: `https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAI_ANIMA_2dac_v0.3.safetensors`

```text
베이스        anima-aesthetic-v1.1
그 위에       (preview3 + anima v1.0 + nai anima v0.2) 병합본을 MBW 로 섞음
마지막에      깎여나간 배경·질감을 메꾸려고 다시 anima-aesthetic-v1.1 로 덮어씌움
```

**제작자가 댓글에서 분명히 한 점 — 로라가 아니라 순수 병합 모델이며 추가 학습은 하지 않았다.**

왜 이렇게 섞었나 —
> *"aesthetic 판이 ANIMA 특유의 **칙칙하고 어두운 그림**을 내놓는 경향이 심해서 그것을 덜어내고 자기 취향 쪽으로 덮어씌운 것"*

즉 **aesthetic 계열의 어두운 색감은 알려진 성질**이고, preview3 / v1.0 / nai anima 계열을 섞어 완화할 수 있다는 실사용 사례다.

> ⚠️ **배포 파일명과 EXIF 내부 모델명이 다르다.** EXIF 의 모델명이 `b0625_aes085` 로 적혀 있으면 동일 모델이다.
> 출력이 달라 보인다는 지적에는 *"최적화 노드가 껴 있어 완전히 같지는 않겠지만 프롬프트·네거티브·파라미터가 같으면 재현되어야 한다"* 고 답했다.

### ⚠ 챈 배포 파인튜닝판의 증상은 순정 ANIMA 의 것이 아니다

챈에서 배포된 파인튜닝판('농농이 아니마')에서 `1girl, loli, white hair` 조합의 **피부가 탄 것처럼 익어서 나오는**
현상이 **5할 넘게 재현**됐다는 보고가 있다 *(2026-05-31)*.
임시 대처는 네거티브에 `tan` 계열 태그를 넣는 것이고 그러면 개선되지만 **근본 원인은 확인되지 않았다**(댓글 없음).

**순정 ANIMA 가 아니라 챈 자체 파인튜닝판 이야기라는 점에 주의할 것.**
파인튜닝판에서 나는 증상을 ANIMA 일반의 성질로 옮겨 적으면 안 된다.

→ 병합 일반론은 [모델 고르기](models.md), 받는 곳은 [자원](resources.md)

<small>근거 — [페) 말랑이 26.08](https://arca.live/b/aiart/179394381) · [exif 첨부해서 다시 질문해봄 26.05](https://arca.live/b/aiart/172357596)</small>

## 다른 모델과의 체감 비교 (2026-08) — Krea · Illustrious
<small>2026-08 기준 · 근거 4건 · 자료 엇갈림</small>

### Krea 대 ANIMA — NSFW 에서는 격차가 크다 *(2026-08-11, 한 글)*

| | |
|---|---|
| 순수 퀄리티 | **Krea** 우위 |
| NSFW 지시 추종·세부 묘사 | **ANIMA** 우위 — 가중치만 주면 원하는 세부 묘사가 바로 나온다 |
| Krea 의 문제 | 검열을 통과한 것이 실력인지 우연인지 헷갈리고, **NSFW 튜닝판은 지시를 제대로 듣지 않고 제멋대로 행위부터 시작**한다 |

**부수 실측 하나** — `peeing` 계열 태그의 **가중치를 0.5 로 낮추면 소변이 아니라 분수(사정) 형태로 바뀐다.**
가중치를 낮추는 것이 단순히 '약하게' 가 아니라 **다른 표현으로 넘어가게 만드는** 사례다.

### Illustrious 에 남는 쪽 — 같은 글에서 정확히 둘로 갈렸다 *(2026-08-03)*

| 남는 쪽 | 넘어간 쪽 |
|---|---|
| *"ANIMA 를 테스트해 봤는데 영 아니라서 IL 이면 충분하다. 일단 빠르고 편하다"* | *"나도 ANIMA 는 아직 아니다 싶었는데 **괜찮은 워크플로우를 쓰니까 속도도 빠르고 신세계**였다"* |
| *"순수 야짤 뽑기에서는 ANIMA 가 ILXL 을 완전히 눌렀다고 하기 애매하다"* | *"ILXL 로라가 수십 기가 있는데도 ILXL 을 안 쓰는 중"* |

읽어 낼 수 있는 것 — **ANIMA 의 체감 우열은 (가) 어떤 워크플로우를 쓰느냐와 (나) 단순 구도인가 복잡한 다인물인가에 따라 갈린다.**
단순 구도 위주면 reForge + Illustrious 로 충분하고, 복잡한 구도·다인물이면 ANIMA 의 이점이 커진다.

*(ANIMA 는 **reForge Neo** 에서도 구동된다 — 2026-05·06 두 글에서 확인됐다.)*

→ 모델 지형 전체는 [모델 고르기](models.md)

<small>근거 — [페) 아직도 리포지에 ILXL 잡고 있는 내가 레전드 26.08](https://arca.live/b/aiart/178845352) · [크레아는 야짤 완성도 높아지기 전에 퇴물되겠지? (오줌짤) 26.08](https://arca.live/b/aiart/179568421) · [포지네오 아니마 프롬프트 질문좀 26.06](https://arca.live/b/aiart/174213477) · [anima 쓸려고 리포지 네오로 바꿧는데 26.05](https://arca.live/b/aiart/172355759)</small>

## 그림체가 시드마다 갈릴 때, 그리고 LLM 에 장면을 맡기는 실험
<small>2026-07 기준 · 근거 2건 · **근거 약함**</small>

### 로라·프롬프트가 같은데 그림체가 두 갈래로 갈린다 *(2026-05-26, 한 글)*

시드만 다른데 그림체가 갈리고, **프롬프트가 복잡해질수록 그 빈도가 는다.**
글쓴이의 원인 추정은 **학습 이미지가 1장뿐인 로라라 그림체를 붙잡는 힘이 약하다**는 것이다
(학습에 쓸 그림이 부족한 캐릭터에서 흔한 상황).

| 시도 | 결과 |
|---|---|
| ChatGPT 조언대로 `full color, balanced colors, natural lighting` 추가 | 이미 넣은 상태라 효과 없음 |
| **highres(2단 생성)를 돌린다** | 댓글의 실효 조언 |
| **CFG 와 스텝 수를 늘린다** | 〃 |

요지는 **프롬프트를 더 붙이는 대신 샘플링 예산을 늘려 로라가 충분히 반영되게 하라**는 것이다.
NAI 시절에도 이 정도 편차는 있었으나, **ANIMA 는 로라로 그림체를 잡고 NAI 는 작가명 나열로 잡는다**는 차이가 있다.
('1장이면 캐릭터 로라를 만들기 충분하다' 는 말이 사실과 다르다는 별개 실측도 있다 → [로라 쓰는 법](lora-usage.md))

### LLM 에 스토리를 맡겨 연작을 자동 생성 *(2026-07-24, 한 글)*

```text
Qwen3.6 으로 작성한 자동화 프로그램  →  흐름 제어
Gemma 4                              →  장면 설명 · 프롬프트 생성
ANIMA                                →  출력
```

*"학원 선도부장이 만일 숨덕인 경우"* 라는 한 줄 설정만 주면 **LLM 이 시간 흐름과 상황 변화를 스스로 배치**해
기승전결 네 장면이 나왔다는 것이 확인된 내용이다.

> ⚠️ **프롬프트 전문·학습/샘플링 설정·프로그램 코드가 공개되지 않아 그대로 재현할 수는 없다.**

<small>근거 — [(아니마) '학원 선도부장이 만일 숨덕인 경우'를 gemma… 26.07](https://arca.live/b/aiart/177862681) · [아니마에서 이정도 그림체 차이는 받아들여야하겠죠? 26.05](https://arca.live/b/aiart/171815293)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 275개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 캐릭터·작가·매체 태그 안의 괄호는 역슬래시로 이스케이프해 nagisa \(blue archive\), star \(sky\), graphite \(medium\) 처럼 적는다 | 7 | 0 | 2025-08~2026-07 |
| ANIMA 는 Euler A + automatic/normal 조합에서 그림이 기괴해지므로 Euler 또는 ER SDE 샘플러에 simple 또는 SGM uniform 스케줄러를 써야 한다 | 7 | 0 | 2026-04~2026-08 |
| 와일드카드는 언더바 두 개로 감싼 __파일명__ 형태로 호출하고, 하위 폴더에 있으면 __폴더/파일명__ 으로 적는다 | 6 | 0 | 2024-03~2026-07 |
| ANIMA 의 작가 태그는 반드시 `@` 로 시작한다 — 작가 태그가 `abcd efg` 이면 `@abcd efg` 로 쓰고 (단부루 표기가 `aaaaa_bbb` 이면 `@aaaaa bbb`), `@` 를 안 붙이면 태그 효과가 미미하다 | 6 | 0 | 2026-02~2026-05 |
| 2026년 Illustrious·SDXL·ANIMA 계열의 퀄리티 태그 관례는 masterpiece, best quality, highres, absurdres 를 프롬프트 앞머리에 두는 것이다 | 6 | 0 | 2026-02~2026-07 |
| ANIMA 계열 LoRA 배포글 머리의 `LoRA Base Model: anima-base-v1.0` 은 학습에 쓴 베이스일 뿐 그림을 만드는 모델이 아니다. 실제로 그림을 뽑는 체크포인트는 `waiANIMA_v10Base10` 이고 그 위에 캐릭터 LoRA 를 얹는다. | 6 | 0 | 2026-05~2026-06 |
| 포니 계열에서 유래한 스코어 태그는 score_9 부터 score_1 까지 아홉 단계이며, 긍정에 score_9/score_8/score_7 중 1~3개를, 네거티브에 score_1/score_2/score_3 을 넣는 것이 관례다 | 6 | 0 | 2026-02~2026-06 |
| ANIMA 캐릭터 LoRA 는 의상·장식·특이한 눈동자·문신이 제대로 구현되지 않을 가능성이 높다고 제작자가 미리 고지한다. | 5 | 0 | 2026-05~2026-06 |
| ANIMA 의 공식 지원 해상도는 512x512(NAI1) ~ 1024x1024(SDXL) ~ 1536x1536(ILXL1) 버킷이고, 공식·입문 자료는 SDXL 해상도(1024급, 세로 832x1216)를 무난한 기본값으로 권한다 | 5 | 0 | 2026-01~2026-05 |
| ANIMA 는 safe/sensitive/nsfw/explicit 안전등급 태그, year 2025 같은 연도 태그, newest·recent·mid·early·old 시대 태그를 받으며 안 야한 것을 뽑으려면 safe 를 넣어야 한다 | 5 | 0 | 2026-02~2026-05 |
| ANIMA 는 qwen3 기반 LLM 인코더가 프롬프트를 통째로 인코딩해 작가 태그 임베딩이 평균으로 뭉개지므로, SDXL 처럼 가중치만으로 화풍을 섞을 수 없다 | 5 | 0 | 2026-04~2026-05 |
| A1111 계열 가중치 문법은 (태그:1.2) 이고 괄호를 겹치는 표기는 한 겹당 1.1배라서 (((검은머리))) 세 겹은 1.1^3 = 1.331배다 | 5 | 0 | 2022-10~2026-07 |
| ANIMA 작가 태그는 반드시 @ 로 시작하며, 단부루 등록명이 aaaaa_bbb 이면 @aaaaa bbb 로 적는다 | 5 | 0 | 2026-02~2026-07 |
| ComfyUI-EasyUseAnima 는 릴리스보다 main 브랜치에 수정이 먼저 올라가므로 git 으로 설치해야 인풋 소켓 누락 같은 버그가 고쳐진 판을 받는다 | 4 | 0 | 2026-06~2026-07 |
| ANIMA 는 다국어를 지원하지 않아 프롬프트를 영어로 써야 하며, 한국어로 쓰려면 워크플로우에 번역 노드를 끼워 넣는다 | 4 | 0 | 2026-02~2026-08 |
| ANIMA 의 가중치 문법은 ComfyUI 에서 SDXL 과 같은 `(tag:weight)` 이지만 cross attention 구조상 SDXL 보다 훨씬 높은 값이 필요해 `(chibi:2)` 처럼 :2 정도에서 시작하며, 4 이상을 남발하면 연산이 깨져 검은 화면이 나올 수 있다 | 4 | 0 | 2026-05~2026-07 |
| SDXL 시대에 DPM++ 권장이 뒤집혔다 — Illustrious·NoobAI 는 `Euler`·`Euler A`, ANIMA 는 `er_sde` 계열을 쓴다. | 4 | 0 | 2023-02~2026-05 |
| ANIMA All in One 워크플로우는 V5/V5.1(2026-06) 이 기준판이고 그 이전 preview3 시절 판들은 작성자 스스로 낡았다고 철회했다 | 4 | 0 | 2026-04~2026-06 |
| ANIMA 는 자연어 이해력은 좋지만 화풍과 미학적 구도가 약해, ANIMA 로 구도를 잡고 Illustrious/SDXL 로 hires fix 해 화풍을 덮는 2단 구성이 쓰인다 | 4 | 0 | 2026-02~2026-04 |
| ANIMA 용 LLLite 컨트롤넷 모델은 ComfyUI\models\controlnet 에 넣고 Apply Anima ControlNet-LLLite 노드로 연결한다 | 4 | 0 | 2026-05~2026-05 |
| 이미지 생성(ANIMA)에서는 dynamic vram 을 끄는 쪽이 빠르며, torch.compile 을 쓸 때는 --disable-dynamic-vram 이 사실상 필수다 | 4 | 0 | 2026-05~2026-08 |
| ANIMA 전용으로 학습된 LoRA 는 정상 동작한다 — 캐릭터 LoRA(강도 1), 터보 로라, 디테일러 로라가 실제로 쓰인다. 호환되지 않는 것은 SDXL(Illustrious·NoobAI)용 LoRA·임베딩·컨트롤넷이다 | 4 | 0 | 2026-05~2026-07 |
| ComfyUI 인페인팅은 `VAE Encode (for Inpainting)` 대신 `VAE Encode` + `Set Latent Noise Mask` 를 써야 한다 — 전자는 마스킹 주변부가 깨진다 | 3 | 0 | 2026-04~2026-05 |
| 챈의 Anima LoRA 배포는 kio.ac·mega·구글 드라이브 같은 임시 공유가 많아 만료가 잦다 — `165231841`(kio.ac, 2026-03-21 만료) · `164800666`(구글 드라이브, 공유 기간 종료) · `178293143`(kio.ac, 공개 직후 닫힌 것으로 보임)은 만료가 확인됐고, 링크를 base64 로 인코딩해 올리는 것은 저작권 시비를 피하려는 챈의 관행이다 | 3 | 0 | 2026-03~2026-07 |
| ComfyUI 와일드카드 파일은 ComfyUI\custom_nodes\comfyui-impact-pack\wildcards 에 txt 든 yaml 이든 넣으면 되고, 다른 커스텀 노드들도 이 Impact Pack 폴더를 공유한다 | 3 | 0 | 2025-01~2026-05 |
| ANIMA 의 텍스트 인코더는 CLIP 이 아니라 Qwen3-0.6B-base LLM 이며(CLIP 은 SD1.5/SDXL 시절 인코더를 가리키는 말), 반드시 튜닝되지 않은 순정 `qwen_3_06b_base.safetensors` 를 써야 토큰이 어긋나지 않는다 | 3 | 0 | 2026-02~2026-05 |
| ANIMA 2.9B 는 기존 Transformer 28블록 사이사이에 신규 12블록을 삽입해 총 40블록으로 확장한 구조라 기존 ANIMA 로라를 쓰려면 블록 인덱스를 `0,1,3,4,6,7,9,10,12,13,15,16,18,19,20,22,23,25,26,28,29,31,32,34,35,37,38,39` 로 재매핑해야 하고(삽입 블록은 `2,5,8,11,14,17,21,24,27,30,33,36` 이며 여기에는 로라 delta 를 넣지 않는다), 인덱스를 그대로 쓰거나 뒤에 12개를 padding 하는 변환은 틀렸으며, 재매핑해도 앞쪽 삽입 블록이 hidden state 를 먼저 바꾸므로 원본 ANIMA 와 동일한 시각적 효과는 보장되지 않는다 | 3 | 0 | 2026-08 |
| ANIMA 의 판 계보는 `PREVIEW1` → `PREVIEW2` → `PREVIEW3` → `anima-base-v1.0`(2026-05-14 정출) → `anima-aesthetic-v1.0` / `v1.0b` / `v1.1` · `Anima Turbo`(2026-07) 순이며, BASE 는 공식 설명 그대로 '정제되지 않은 사전학습 원본(The pretrained, unrefined base model)' 이고 Aesthetic 계열은 그 위에 미적 튜닝을 얹은 판이다 | 3 | 0 | 2026-05~2026-07 |
| ANIMA 의 기본 shift 값은 3 이고(ComfyUI supported_models.py 에서 3.0 확인) shift 0 은 CFG·스텝 조합과 무관하게 공통적으로 검은 화면이 나오므로 쓰면 안 된다 | 3 | 0 | 2026-02~2026-06 |
| ANIMA 로 넘어와 '프롬프트가 안 먹는다' 는 질문의 되풀이되는 원인은 IL·Pony·SD1.5 시절 프롬프트를 그대로 가져온 것이다 — 화풍 형용구 남발('SD1.5 시절 고봉밥 프롬프트'), 빈 쉼표와 줄바꿈, 과도한 가중치, 같은 문장 중복을 전부 걷어내고 정확한 danbooru 태그 나열 + 자연어 설명으로 다시 쓰는 것이 답이며, 배포처 권장 프롬프트나 CivitAI 예시 이미지의 프롬프트가 가장 안전한 출발점이다 | 3 | 0 | 2026-05~2026-06 |
| ANIMA 는 여성기·음핵 등 국소 부위 묘사 품질이 낮은 것이 판의 알려진 약점이다 — 그림체(작가 태그·스타일 로라)에 따라 편차가 크고 `erect clitoris` 는 가중치를 올려도 반응이 없거나 후타나리로 급발진한다. 완화책은 업스케일 추가, `clitoris`·`clitoris hood` 병기, 해당 부위를 잘 그리는 작가 태그(cosine · nezunezu · shungikuten)이지만 '조금 나아지는 수준이지 해결책은 아니다' 가 중론이고 근본 해법은 직접 로라 학습이다 | 3 | 0 | 2026-06~2026-06 |
| ANIMA 생성에서 sage attention 은 약 9~11% 속도 향상이며 품질 손상이 거의 없다 | 3 | 0 | 2026-02~2026-05 |
| ComfyUI 네이티브 PiD 구현은 gemma 를 불필요하게 받게 하고 정중앙이 찢어지는 결함이 있어, 재구현 노드(ComfyUI-Anima-PiD)로 옮겨가는 편이 낫다 | 3 | 0 | 2026-06~2026-06 |
| 터보(고속) 로라를 쓸 때는 Spectrum·Layer Replay 계열이 부적합하고 Anima NAG 를 쓰며, 터보 로라를 안 쓰면 정반대로 Spectrum 을 쓰고 NAG 를 뺀다 | 3 | 0 | 2026-05~2026-05 |
| Spectrum 계열 가속은 ANIMA 단일 최적화 중 효과가 가장 커서 속도를 2배 이상(+116~124%) 올린다 | 3 | 0 | 2026-05~2026-05 |
| ANIMA 자연어 프롬프트는 최소 2문장 이상 쓰고 품질·아티스트 태그를 앞부분에 두며, 여러 캐릭터를 넣을 때는 이름만 나열하지 말고 외형을 설명해야 한다 | 3 | 0 | 2026-04~2026-07 |
| ANIMA 는 SDXL(Illustrious, NoobAI)과 구조가 달라 기존 로라·임베딩·컨트롤넷이 전혀 호환되지 않는다 | 3 | 0 | 2025-09~2026-07 |
| 태그는 쉼표+공백 ", " 으로 잇고, 2명 이상이면 2girls 같은 인원수 태그를 선두에 두며 solo·1girl 과 병용하지 않는다 | 3 | 0 | 2026-04~2026-07 |
| 전체 torch.compile 보다 블록 컴파일(Anima Block Compile / compile_transformer_blocks_only)이 컴파일 시간이 짧아 실용적이다 | 3 | 0 | 2026-05~2026-06 |
| ComfyUI-EasyUseAnima (https://github.com/n0va39/ComfyUI-EasyUseAnima)는 릴리스가 아니라 GIT 으로 받아야 하며, 0.4.0 이후 버그가 다수 수정된 0.5.2(와일드카드 수정본 0.5.3) 이상을 쓰라는 것이 제작자의 최종 안내다 | 3 | 0 | 2026-07~2026-07 |

## 이 문서와 이어진 곳

**이 개체를 다루는 다른 문서**

- [업스케일과 화질](upscale.md) (가이드)
- [VRAM·속도 최적화](vram.md) (가이드)
- [모델 고르기](models.md) (가이드)
- [ComfyUI 쓰는 법](comfyui.md) (튜토리얼)
- [국룰 — 채널이 합의한 기본값](kukroul.md) (국룰)
- [오류 해결](troubleshooting.md) (문제해결)

**함께 등장하는 것들** — 숫자는 같은 글에 함께 나온 횟수

ComfyUI 8 · negpip 3 · KJNodes 3 · SageAttention 3 · WAI-illustrious-SDXL 3 · Triton 3 · Autocomplete Plus 3 · rgthree 3 · ComfyUi_NakoNode 3 · Illustrious 3 · ComfyUI Manager 3 · Easy-Models-Linker 2

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [마참내! anima-base-v1.0 떳다](https://arca.live/b/aiart/170688430) — 2026-05, 추천 72
- [워크플로) SDXL만큼 빠른 Anima T2I](https://arca.live/b/aiart/167246595) — 2026-04, 추천 63
- [Anima 웹툰 캐릭터 Lora 공유) 뷰티풀 군바리](https://arca.live/b/aiart/173589934) — 2026-06, 추천 59
- [Anima용 와일드카드 공유](https://arca.live/b/aiart/177489520) — 2026-07, 추천 59
- [아니마 심플하면서 제대로쓰기](https://arca.live/b/aiart/171770463) — 2026-05, 추천 56
- [응애도 할 수 있는 ComfyUI Anima 로컬 아니메 이미지 생성 간단 사용 입문하기](https://arca.live/b/aiart/163553760) — 2026-02, 추천 49
- [웹 아니마](https://arca.live/b/aiart/173582055) — 2026-06, 추천 49
- [anima preview 3 떳다](https://arca.live/b/aiart/167051252) — 2026-04, 추천 47
- [Anima용 디테일 개선 노드 만들어왔습니다. (Comfy UI 확장)](https://arca.live/b/aiart/175940996) — 2026-07, 추천 47
- [로컬 아니메 모델 Anima에 대한 잡다한 정보 개정판](https://arca.live/b/aiart/170924904) — 2026-05, 추천 46
- [아니마 그림체 로라 공유](https://arca.live/b/aiart/176886634) — 2026-07, 추천 46
- [초보자용 아니마 + IL 5배 초고속 워크 플로우](https://arca.live/b/aiart/162909120) — 2026-02, 추천 45
- [Anima 찍먹해보기 - 이미지생성](https://arca.live/b/aiart/171031030) — 2026-05, 추천 44
- [Comfy ANIMA 정보글 모음](https://arca.live/b/aiart/175397651) — 2026-06, 추천 43
- [바보멍청이를 위한 아니마 워크플로우](https://arca.live/b/aiart/174818684) — 2026-06, 추천 42
- [아니마 완벽한 픽셀 그림 만들기](https://arca.live/b/aiart/173819166) — 2026-06, 추천 40
- [ANIMA Easy Use workflow v1: 복잡한 워크플로우 없이 딸깍하기](https://arca.live/b/aiart/175755179) — 2026-07, 추천 40
- [anima2.9b 출시](https://arca.live/b/aiart/179710466) — 2026-08, 추천 40
- [초보자용 아니마+IL 워크플로우 VER.2](https://arca.live/b/aiart/163201876) — 2026-02, 추천 39
- [최근 AI 그림 자주 묻는 질문 (26년 5월 기준)](https://arca.live/b/aiart/170655900) — 2026-05, 추천 38
- [[모델공유] Anitional-v1.0-int8c (병합모델)](https://arca.live/b/aiart/178360790) — 2026-07, 추천 37
- [NSFW 애니메이션 신모델 Anima](https://arca.live/b/aiart/161150715) — 2026-01, 추천 36
- [Anima 찍먹해보기 - 최적화](https://arca.live/b/aiart/171129670) — 2026-05, 추천 36
- [아니마 쉽게 뽑는툴](https://arca.live/b/aiart/179069358) — 2026-08, 추천 35
- [초보자를 위한 초보자의 ANIMA 워크플로우](https://arca.live/b/aiart/168821026) — 2026-04, 추천 34
- [ANIMA All in One 워크플로우 v5: i2i와 인페인트 정상화](https://arca.live/b/aiart/171941799) — 2026-05, 추천 34
- [Anima 웹툰 캐릭터 Lora 공유) 동아리](https://arca.live/b/aiart/173973554) — 2026-06, 추천 34
- [Anima 초보자 자연어(한국어) 프롬프트 워크플로우](https://arca.live/b/aiart/171167219) — 2026-05, 추천 33
- [Anima 찍먹해보기 - 인페인팅](https://arca.live/b/aiart/171376566) — 2026-05, 추천 33
- [어제 작업한 아니마 그림체 공유](https://arca.live/b/aiart/176515020) — 2026-07, 추천 33
- [아니마 1.1 대충 찍먹](https://arca.live/b/aiart/176800461) — 2026-07, 추천 33
- [Anima to XL 워크플로 공유](https://arca.live/b/aiart/161453678) — 2026-02, 추천 31
- [comfyui) Anima 찍먹용 - anima+ill 워크플로우 (t2i , i2i, ollama 필요)](https://arca.live/b/aiart/162677789) — 2026-02, 추천 31
- [아니마 퀄리티 높이기](https://arca.live/b/aiart/173299334) — 2026-06, 추천 31
- [아니마 모델의 시프트 값에 대해 알아보자](https://arca.live/b/aiart/163123039) — 2026-02, 추천 30
- [오크의 가슴잡기로 알아보는 태그형에 가까운 아니마의 하이브리드 프롬프트 작성법.](https://arca.live/b/aiart/171855587) — 2026-05, 추천 30
- [anima용 슈퍼울트라작가믹스](https://arca.live/b/aiart/177376366) — 2026-07, 추천 30
- [Anima 생성을 빨리 해보자!](https://arca.live/b/aiart/161452759) — 2026-02, 추천 29
- [로컬 comfyui 찍먹해보기 - 리저널 프롬프트](https://arca.live/b/aiart/161686015) — 2026-02, 추천 29
- [대충 만든 Anima용 인페인팅 LLLite 컨트롤넷](https://arca.live/b/aiart/169549288) — 2026-05, 추천 28
- [아니마 디테일 트위커 로라 나왔음.](https://arca.live/b/aiart/170584706) — 2026-05, 추천 28
- [로컬 아니메 모델 Anima에 대한 잡다한 정보](https://arca.live/b/aiart/161337087) — 2026-02, 추천 26
- [Anima preview2 / preview3 / base 비교](https://arca.live/b/aiart/170773343) — 2026-05, 추천 26
- [아니마 이거 의외로 먹히나? 싶은거](https://arca.live/b/aiart/170963618) — 2026-05, 추천 26
- [오늘의 한요일은 여자다 "Anima" 올인원(거의)로라 공유](https://arca.live/b/aiart/171042669) — 2026-05, 추천 26
- [Anima 찍먹해보기 - LLLite Controlnet](https://arca.live/b/aiart/171458536) — 2026-05, 추천 26
- [Anima 애니메이션 캐릭터 Lora 공유) Fate stay night](https://arca.live/b/aiart/173275160) — 2026-06, 추천 26
- [PeroPixfy) ComfyUI에서 워크플로우 없이 아니마 쓰기](https://arca.live/b/aiart/174926997) — 2026-06, 추천 26
- [초보자를 위한 ANIMA All in One 워크플로우 v2](https://arca.live/b/aiart/169548769) — 2026-05, 추천 25
- [아니마 자연어 프롬프트 공식 팁](https://arca.live/b/aiart/171082011) — 2026-05, 추천 25
- [Anima에서 작가 태그 혼합을 도와주는 커스텀 노드 제작함 (Anima Artist Mixer)](https://arca.live/b/aiart/171947113) — 2026-05, 추천 25
- [kohya가 만든 Anima용 인페인팅 LLLite 컨트롤넷](https://arca.live/b/aiart/170374198) — 2026-05, 추천 24
- [로컬 comfyui 찍먹해보기 - Spectrum 가속](https://arca.live/b/aiart/171935194) — 2026-05, 추천 24
- [anima PID 업스케일링 원클릭 노드 배포](https://arca.live/b/aiart/172741115) — 2026-06, 추천 24
- [아니마 Aesthetic V1.0쓰는 삣삐들스탑](https://arca.live/b/aiart/176406993) — 2026-07, 추천 24
- [블아 작가로라 2개](https://arca.live/b/aiart/167677263) — 2026-04, 추천 23
- [조금 더 좋은 Anima용 인페인팅 LLLite 컨트롤넷 만든거 공유](https://arca.live/b/aiart/169700812) — 2026-05, 추천 23
- [아티스트 태그를 섞는 Anima Artist Mixer 노드](https://arca.live/b/aiart/172080673) — 2026-05, 추천 23
- [ANIMA All in One 워크플로우 v5.1: 오류 수정, 간단한 기능 추가](https://arca.live/b/aiart/172676286) — 2026-06, 추천 23
- [<장래를 약속한 소꿉친구 그녀의 NTR 추억> 1편](https://arca.live/b/aiart/179279560) — 2026-08, 추천 23
- [Anima FP8 양자화 모델](https://arca.live/b/aiart/161167531) — 2026-02, 추천 22
- [anima-base-v1.0-int8rowwise](https://arca.live/b/aiart/170720836) — 2026-05, 추천 22
- [anima-aesthetic-v1.0, turbo 모델 출시](https://arca.live/b/aiart/176286183) — 2026-07, 추천 22
- [[anima] DyPE를 쓰면 깡으로 초고해상도 이미지를 뽑을 수 있을까?](https://arca.live/b/aiart/176872950) — 2026-07, 추천 22
- [XL to Anima 워크플로 공유](https://arca.live/b/aiart/161442385) — 2026-02, 추천 21
- [(중급자를 위한) 개조 아니마-IL 워크플로우](https://arca.live/b/aiart/168234596) — 2026-04, 추천 20
- [ANIMA All in One 워크플로우 v4: 인페이팅 추가](https://arca.live/b/aiart/170572804) — 2026-05, 추천 20
- [comfyui anima 고속 + mod guidance 노드 mod 개편](https://arca.live/b/aiart/174673655) — 2026-06, 추천 20
- [스압) 아니마 프리뷰 고품질 아티스트 태그 batch 1](https://arca.live/b/aiart/161430824) — 2026-02, 추천 19
- [comfy에서 리저널+SAM3로 여러캐릭 한번에 뽑기](https://arca.live/b/aiart/162598061) — 2026-02, 추천 19
- [로컬 Anima모델의 품질 태그와 세이프티 태그에 대해서 (미니 정보)](https://arca.live/b/aiart/163666946) — 2026-03, 추천 19
- [브더2 느낌의 amima 로라](https://arca.live/b/aiart/165231841) — 2026-03, 추천 19
- [Anzhc/AAAAnima not so early](https://arca.live/b/aiart/176018707) — 2026-07, 추천 19
- [Anima 모델 자연어 인식 테스트](https://arca.live/b/aiart/161190216) — 2026-02, 추천 18
- [kohya 제작 Anima용 인페인팅 LLLite 컨트롤넷 V2](https://arca.live/b/aiart/170867594) — 2026-05, 추천 18
- [EasyUseAnima 0.5.5: 해상도와 자동완성 편의성 패치, 버그수정](https://arca.live/b/aiart/177930483) — 2026-07, 추천 18
- [comfyUI ANIMA 그림체 및 워크플로우 공유](https://arca.live/b/aiart/168777426) — 2026-04, 추천 17
- [ANIMA All in One 워크플로우 v3: NAIA 추가](https://arca.live/b/aiart/169978553) — 2026-05, 추천 17
- [저처럼 forge neo쓰다가 여러 문제를 겪으시는분들 혹시라도 도움되길](https://arca.live/b/aiart/174448928) — 2026-06, 추천 17
- [Anima 웹툰 캐릭터 Lora 공유) 모비딕](https://arca.live/b/aiart/174511949) — 2026-06, 추천 17
- [개인용 아니마 워크플로우 공유](https://arca.live/b/aiart/174806461) — 2026-06, 추천 17
- [아니마 디테일러 로라 5종 간단 비교](https://arca.live/b/aiart/175333518) — 2026-06, 추천 17
- [ANIMA용 잼민이 gems v5](https://arca.live/b/aiart/177929816) — 2026-07, 추천 17
- [Anima 로라 블럭필터 개조](https://arca.live/b/aiart/171479837) — 2026-05, 추천 16
- [[스압] 실험용 아니마 에디트 워크플로우 3종](https://arca.live/b/aiart/172022855) — 2026-05, 추천 16
- [초보자의 초보자를 위한 ANIMA all in one 워크플로우 업데이트](https://arca.live/b/aiart/169127262) — 2026-04, 추천 15
- [이상성욕)아니마용 촉수, 백합용 와일드카드](https://arca.live/b/aiart/169392958) — 2026-05, 추천 15
- [아니마 I2I or 디테일러 과정에서 노이즈가 발생하는 현상 고치기](https://arca.live/b/aiart/170831609) — 2026-05, 추천 15
- [뉴비의 아니마 워크플로우 공유](https://arca.live/b/aiart/170889404) — 2026-05, 추천 15
- [ANIMA All in One 워크플로우 v4.1핫픽스](https://arca.live/b/aiart/170922099) — 2026-05, 추천 15
- [Anima 샘플링 속도 개선 SPEED 커스텀 노드](https://arca.live/b/aiart/171255449) — 2026-05, 추천 15
- [아니마만을 위한 아니마를 위한 아니마 전용 노드들](https://arca.live/b/aiart/171378660) — 2026-05, 추천 15
- [EasyUseAnima 0.2.3: 기능 총정리](https://arca.live/b/aiart/175754499) — 2026-07, 추천 15
- [그냥 또 만든 고속 LoRA 병합 Anima 모델 (INT8 버전 포함)](https://arca.live/b/aiart/177115790) — 2026-07, 추천 15
- [EasyUseAnima 0.5.2: 디테일러 설정, 와카 시드, 모델 선택 버그 수정](https://arca.live/b/aiart/177337756) — 2026-07, 추천 15
- [Anima로 NAI 느낌 짤털](https://arca.live/b/aiart/178404708) — 2026-07, 추천 15
- [페) 말랑이](https://arca.live/b/aiart/179394381) — 2026-08, 추천 15
- [초간단 급조 2.9b 호환 로라 로더 만들어옴](https://arca.live/b/aiart/179726548) — 2026-08, 추천 15
- [[개쩌는대회] 사자왕의 봄](https://arca.live/b/aiart/163475234) — 2026-02, 추천 14
- [뉴비의 아니마 워크플로우 공유 (2)](https://arca.live/b/aiart/172332889) — 2026-05, 추천 14
- [아니마 프리뷰v3 / 베이스v1 동일 데이터셋으로 학습한 로라 함 비교](https://arca.live/b/aiart/170810380) — 2026-05, 추천 13
- [Anima+IL 연속 스펙트럼 워크플로우.](https://arca.live/b/aiart/171529357) — 2026-05, 추천 13
- [아니마 VAE 4종 비교](https://arca.live/b/aiart/178177432) — 2026-07, 추천 13
- [아니마 모델시프트0~9까지 3번비교](https://arca.live/b/aiart/163239744) — 2026-02, 추천 12
- [허접한 AnimaYumeV02 용 LoRA 공유함](https://arca.live/b/aiart/164800666) — 2026-03, 추천 12
- [Anima 최적화 속도테스트](https://arca.live/b/aiart/171106264) — 2026-05, 추천 12
- [EasyUseAnima 0.2.0: 다양한 편의성 노드와 리저널 프롬프트 노드 추가](https://arca.live/b/aiart/175458978) — 2026-06, 추천 12
- [ANIMA 터보 로라 3종 테스트.](https://arca.live/b/aiart/175962147) — 2026-07, 추천 12
- [EasyUseAnima 0.4.0: AiO 생성기 프리셋 기능, UI 버그수정](https://arca.live/b/aiart/176677452) — 2026-07, 추천 12
- [[anima, 스압] 해상도 임계점 실험, DyPE 추가 실험](https://arca.live/b/aiart/177102053) — 2026-07, 추천 12
- [아니마 챈에 올리는 고속화로라없이 스탭줄이는 날먹셋팅팁](https://arca.live/b/aiart/161175343) — 2026-02, 추천 11
- [EasyUseAnima 0.2.1: Artist Mix와 spectrum 가속, 기타등등](https://arca.live/b/aiart/175613721) — 2026-07, 추천 11
- [EasyUseAnima 1.1.0: Webui(A1111) 방식 로라 지원, Hook 추가 기능](https://arca.live/b/aiart/179713666) — 2026-08, 추천 10
- [Anima-INT8Rowwise 모델](https://arca.live/b/aiart/163367034) — 2026-02, 추천 9
- [[anima] 최신 모델로 고전적인 인페인팅 하기.](https://arca.live/b/aiart/168764579) — 2026-04, 추천 9
- [kohya의 ComfyUI-Anima-LLLite 커스텀 노드](https://arca.live/b/aiart/169455470) — 2026-05, 추천 9
- [아니마 Lefr girl, Right girl 이름 대체 커스텀노드](https://arca.live/b/aiart/173945456) — 2026-06, 추천 9
- [하지만 빨랐죠? 자작 4스텝 로라 정식버전 업데이트](https://arca.live/b/aiart/177065984) — 2026-07, 추천 9
- [Anima를 INT8 양자화 해보았다.](https://arca.live/b/aiart/162298399) — 2026-02, 추천 8
- [EasyUseAnima 1.1.1: ANIMA 2.9B 지원 추가 + 챈산 모드 가이드넌스 포크버전](https://arca.live/b/aiart/179735645) — 2026-08, 추천 8
- [ANIMA용 간이 아티스트 태그 관리 도구 (추가1)](https://arca.live/b/aiart/161369658) — 2026-02, 추천 7
- [아니마용 @Conditioning쓰까쓰까 노드](https://arca.live/b/aiart/167592729) — 2026-04, 추천 7
- [대충만든 아니마 촉수, 2girls 보빔 or 3P or 촉수용 와일드카드](https://arca.live/b/aiart/169192403) — 2026-04, 추천 7
- [아니마와 Qwen3.5](https://arca.live/b/aiart/170079773) — 2026-05, 추천 7
- [[anima, 페, 할] 연령 조절 슬라이더 로라](https://arca.live/b/aiart/174677230) — 2026-06, 추천 7
- [마이크로 비키니 크기로 anima lllite 가중치 강도 최대치 알아보기](https://arca.live/b/aiart/174717928) — 2026-06, 추천 7
- [아이폰용 아니마 돌린 간단 후기](https://arca.live/b/aiart/177129172) — 2026-07, 추천 7
- [[anima] 무지성으로 int8 양자화를 시도해도 괜찮을까?](https://arca.live/b/aiart/178163658) — 2026-07, 추천 7
- [채신기법으로 anima lora 학습시켜봄 (2)](https://arca.live/b/aiart/165954535) — 2026-03, 추천 6
- [Anima용 작가 태그 섞기 커스텀 노드](https://arca.live/b/aiart/171467099) — 2026-05, 추천 6
- [ANIMA 야매 레퍼런스 인페인팅(?) 워크플로우.](https://arca.live/b/aiart/171682435) — 2026-05, 추천 6
- [ANIMA 로라 적용시 스타일이 불안정할 때 팁](https://arca.live/b/aiart/171818770) — 2026-05, 추천 6
- [이미 공식에서 아니마는 프롬프트 가중치를 높게 줘야 한다고 말했구나.](https://arca.live/b/aiart/169840426) — 2026-05, 추천 5
- [아니마 연령 조절 로라](https://arca.live/b/aiart/170858259) — 2026-05, 추천 5
- [아니마 5070 ti 1024x1280 기준 약 10초 내외로 걸리는 워크플로우 (미완성) 공유](https://arca.live/b/aiart/171745858) — 2026-05, 추천 5
- [그냥 만든 고속 LoRA 병합 Anima 모델 (INT8 버전 포함)](https://arca.live/b/aiart/176416762) — 2026-07, 추천 5
- [Anima로 이미지 선명화와 GLSL 셰이더](https://arca.live/b/aiart/178612795) — 2026-07, 추천 5
- [GPT로 아니마 캐릭터 만들기 중간결과](https://arca.live/b/aiart/178985085) — 2026-08, 추천 5
- [[anima] DyPE 노드 업데이트 (+SEGA 노드 추가)](https://arca.live/b/aiart/179097719) — 2026-08, 추천 5
- [anima 로라 재시도](https://arca.live/b/aiart/162256686) — 2026-02, 추천 4
- [intel portable 벤?치마크](https://arca.live/b/aiart/168411491) — 2026-04, 추천 4
- [torch.compile 캐시 저장으로 최초로딩속도 줄이기](https://arca.live/b/aiart/171503442) — 2026-05, 추천 4
- [EasyUseAnima 0.1.9 와카 추가](https://arca.live/b/aiart/175389876) — 2026-06, 추천 4
- [anima base 캐릭터 테스트](https://arca.live/b/aiart/171041987) — 2026-05, 추천 3
- [간단한 고속 LoRA 병합 Anima 모델](https://arca.live/b/aiart/172494759) — 2026-06, 추천 3
- [내가 이겼다 아니마](https://arca.live/b/aiart/179030080) — 2026-08, 추천 3
- [[아니마] '학원 선도부장이 만일 숨덕인 경우'를 gemma에게 물어보면 LLM은 무슨 짓을 하는가.](https://arca.live/b/aiart/177862681) — 2026-07, 추천 2
- [ANIMA 자연어 프롬 오염 어쩌구... 이걸 원한거임?](https://arca.live/b/aiart/178231780) — 2026-07, 추천 2
- [페) 아직도 리포지에 ILXL 잡고 있는 내가 레전드](https://arca.live/b/aiart/178845352) — 2026-08, 추천 2
- [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유](https://arca.live/b/aiart/179637421) — 2026-08, 추천 2
- [크레아는 야짤 완성도 높아지기 전에 퇴물되겠지? (오줌짤)](https://arca.live/b/aiart/179568421) — 2026-08, 추천 1
- [후타주의) 아니마가 제 성능을 내지 못하는 것 같아요](https://arca.live/b/aiart/171021817) — 2026-05, 추천 0
- [아니마에서 이정도 그림체 차이는 받아들여야하겠죠?](https://arca.live/b/aiart/171815293) — 2026-05, 추천 0
- [anima 쓸려고 리포지 네오로 바꿧는데](https://arca.live/b/aiart/172355759) — 2026-05, 추천 0
- [exif 첨부해서 다시 질문해봄](https://arca.live/b/aiart/172357596) — 2026-05, 추천 0
- [head_back 태그가 안 먹음 (wai anima base1.0)](https://arca.live/b/aiart/172856945) — 2026-06, 추천 0
- [아니마 뷰지가 너무 이상한데 잘나오게 하는 방법 있음?ㅠ](https://arca.live/b/aiart/173469736) — 2026-06, 추천 0
- [로컬 anima로 팬티 내리기 태그 하는데](https://arca.live/b/aiart/173497043) — 2026-06, 추천 0
- [이런 구도 안 나오게 하는 네거같은거 없을까](https://arca.live/b/aiart/173775104) — 2026-06, 추천 0
- [anima wep 전신이미지 안나옴](https://arca.live/b/aiart/174211583) — 2026-06, 추천 0
- [포지네오 아니마 프롬프트 질문좀](https://arca.live/b/aiart/174213477) — 2026-06, 추천 0
- [아니마web 모델별 질문](https://arca.live/b/aiart/174417723) — 2026-06, 추천 0
- [뷰지랑 꼭지 쫀득하게 하는 로라추천 문질](https://arca.live/b/aiart/174452999) — 2026-06, 추천 0
- [wai illustious SDXL은 아니마 프롬프트가 안먹나?](https://arca.live/b/aiart/174739881) — 2026-06, 추천 0
- [anima 쓰는 사람들 클리 잘 나오나](https://arca.live/b/aiart/175044736) — 2026-06, 추천 0
- [혐주의) 아니마 만져보는데 이건 뭐가 문제일까](https://arca.live/b/aiart/175249876) — 2026-06, 추천 0
- [nai만 쓰다가 로컬 아니마로 넘어가봤는데 먼가 그림체가 시원찮음](https://arca.live/b/aiart/175904931) — 2026-07, 추천 0
- [첸럼발 아니마 디테일 개선 노드 후기](https://arca.live/b/aiart/175950158) — 2026-07, 추천 0
- [ANIMA 자연어 프롬 오염](https://arca.live/b/aiart/178230466) — 2026-07, 추천 0
- [다들 아니마 체크포인트 뭐 씀](https://arca.live/b/aiart/178971620) — 2026-08, 추천 0
- [보추주의) 상대방 손하고 자지만 보이는 그런 투시? 형태는 자연어로 어떻게 프롬프트 해야함?](https://arca.live/b/aiart/179089265) — 2026-08, 추천 0
- [아니마 원래 손찐빠가 좀 심한가용](https://arca.live/b/aiart/179393628) — 2026-08, 추천 0
