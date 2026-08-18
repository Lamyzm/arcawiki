# 모델 고르기

> **원문 177건 → 이 문서 하나** · 주장 291개 · 정리 2026-08-14

실행기를 깔았다면 다음 질문은 **"그래서 무슨 파일을 받아야 하나"** 다.
`.safetensors` 하나가 수 GB 라서 아무거나 받아보고 결정할 수가 없다.

이 문서는 채널에 올라온 모델 소개·비교글에서 **고르는 데 필요한 것만** 추린다.
개별 모델의 설정값은 [ANIMA](anima.md), [MiniMax H3](minimax-h3.md), [비디오 생성](video-generation.md) 에,
받는 곳은 [자원 — 받는 곳 모음](resources.md) 에 따로 있다.

먼저 알아 둘 것 하나 — **채널에 올라오는 모델 소식의 상당수는 아직 검증되지 않은 것이다.**
제작사 주장, 유출 정보, LLM 요약본이 섞여 있고 며칠 뒤 철회되는 경우도 있다.
그 판별법은 마지막 항목에 정리해 두었다.

## 체크포인트란 정확히 무엇인가 — 병합본과 분리 배포
<small>2026-05 기준 · 근거 1건</small>

받을 파일을 고르기 전에 낱말부터 맞춰야 한다.
**"체크포인트 파일이라길래 checkpoints 폴더에 넣었는데 작동을 안 한다"** 는 반복되는 사고의 원인이 여기 있다.

| | 무엇을 가리키나 |
|---|---|
| **넓은 의미** | 특정 시점의 모델 상태를 저장한 것 **전부**. 게임의 임시 세이브 지점 같은 것이라, 이 정의로는 LoRA 도 체크포인트다 |
| **좁은 의미** (WebUI·ComfyUI 가 쓰는 뜻) | **디퓨전 모델 + CLIP(텍스트 인코더) + VAE 세 가지를 하나로 병합한 파일** |

SD1 부터 SDXL 까지는 셋을 한 파일로 묶어 배포하는 것이 관행이었고 그게 곧 '체크포인트' 였다.
(병합이 미숙하던 시절 VAE 가 제대로 작동하지 않는 일이 잦아서, VAE 를 따로 불러와 연결하는 기능이 예전부터 있었다.)

**그런데 모델이 커지고 복잡해지면서 구성 요소를 병합하지 않고 따로 배포하기 시작했다** — ANIMA 가 그렇다.
그러면서도 **아무도 기존 기능의 이름을 바꾸지 않아** `Load Checkpoint` 노드는 여전히 병합본만 읽는다.
소문을 듣고 기본 워크플로의 `Load Checkpoint` 에 ANIMA 를 물리면 그래서 에러가 난다.

| 배포 형태 | 넣는 곳 | 부르는 노드 |
|---|---|---|
| **병합본** — SD1.5 · SDXL · Illustrious · NoobAI · WAI 등 | `models/checkpoints` | `Load Checkpoint` |
| **분리 배포** — diffusion model | `models/diffusion_models` | `Load Diffusion Model` 계열 |
| **분리 배포** — 텍스트 인코더 | `models/text_encoders` | 별도 로더 |
| **분리 배포** — VAE | `models/vae` | `Load VAE` |

댓글 보충 — ckpt 가 그런 묶음 형태를 갖게 된 것은 **SD1/SDXL 시절 Stability AI 가 그렇게 배포했기 때문**이고,
그러지 않으려면 Diffusers 규격으로 배포해야 하는데 그건 파일이 너무 잘게 나뉘어 그것대로 불편했다.

한 글에서만 다룬 정리이지만, 이 채널에서 가장 자주 반복되는 입문자 사고의 원인을 짚은 것이라 그대로 옮긴다 (2026-05).

→ 파일 이름 뒤의 `fp16` · `EMA` · `pruned` 표기는 [용어집](glossary.md) 의 파일 형식 항목을,
`Q8_0` · `int8convrot` 같은 양자화 표기는 아래 "양자화 파일 고르기" 를 보라.

<small>근거 — [넓은 의미의 체크포인트와 좁은 의미의 체크포인트 26.05](https://arca.live/b/aiart/170230261)</small>

## 베이스 · 파인튜닝 · 병합 — "이 로라가 왜 내 모델에서 안 먹히지" 의 답
<small>⚠️ 2024-10 기준 · 근거 1건 · 자료 엇갈림</small>

**"PONY 로 만든 로라를 Illustrious 에 물렸는데 이상한 그림이 나온다"** — 채널에서 가장 자주 반복되는 질문이고,
답은 모델의 **계보**에 있다. 2024-10 의 정보글 한 편(`https://arca.live/b/aiart/119613811`)이 이것을 통으로
설명해 뒀다. **한 글에서만 다룬 정리**이지만 원리를 다루기 때문에 세대가 바뀐 지금도 그대로 통한다.

### 모델은 셋으로 나뉜다

| 갈래 | 무엇인가 |
|---|---|
| **베이스 모델** | 다른 모델들이 참조할 수 있는 기본 모델 |
| **파인튜닝 모델** | 베이스 모델에 추가 학습(때로는 기술적 조정까지)을 시킨 모델. 베이스와 **부모자식** 관계다 |
| **병합 모델** | 두 모델의 일부를 떼어 와 섞어 만든 모델 |

### '베이스 모델' 이 두 가지 뜻으로 쓰인다 — 여기서 다 헷갈린다

원문의 **가구 설계도 비유**가 가장 잘 통한다.

| | 가구로 치면 | AI 로 치면 | 원문의 이름 |
|---|---|---|---|
| **첫째 뜻** | 어떤 회사가 가구를 만들고 **설계도까지 공개**한 것 | 구조·학습 방식·사용법을 집약해 공개한 원 설계 — `SD1.5` · `SDXL` · `SD3.5` · `FLUX` | **태생적** |
| **둘째 뜻** | 그 설계도를 보고 따라 만들되 **재료(데이터셋)를 전부 직접 준비**해 만든 가구 | 그 구조로 자기 데이터셋을 학습시켜 만든 모델 — `kohaku-xl-beta5` 같은 것 | **파생적** |

> 두 가구는 **디자인과 구조는 같지만 재료의 물성이 달라** 쓰는 사람의 경험이 달라진다.
> "챈에서 ILXL 을 베이스 모델이라고 부르던데?" 는 둘째 뜻이다 — 파생 모델들이 **'베이스로 삼은 모델'** 이라는 뜻.

`SD1.5` · `SDXL` · `SD3.5` 의 숫자는 스테이블디퓨전의 **버전**이고, 버전이 달라지면 구조가 크게 바뀌어
**그 모델에 맞게 만든 LoRA·임베딩이 호환되지 않고 사용법까지 바뀐다.**
모델을 돌리는 프로그램도 그 모델을 지원해야 한다(WebUI 가 1.5.x 부터 SDXL 을 지원하기 시작한 것이 그 예다).

### 계보 — 3대로 보면 정리된다

```text
kohaku-xl-beta5        1대 · 조부모    ← 파생적 베이스
        ↓ 추가 학습
Illustrious XL (ILXL)  2대 · 부모      ← 파인튜닝 모델
        ↓ 추가 학습
ILXL 기반 파생 모델들    3대 · 자식
```

**부모의 베이스 모델은 kohaku 이고, 자식의 베이스 모델은 ILXL 이다.** 같은 낱말이 대(代)마다 다른 것을 가리킨다.

### ⚠️ PONY 와 ILXL 은 둘 다 SDXL 인데 왜 로라가 호환되지 않는가

**LoRA 와 임베딩은 같은 파생적 베이스에서 학습한 자식들끼리만 공유된다.**

| | PONY | Illustrious XL |
|---|---|---|
| **태생적** 베이스 | SDXL | SDXL |
| **파생적** 베이스(부모) | 서로 다르다 | 서로 다르다 |
| 서로의 LoRA | **작동은 하지만 정상적인 결과물이 안 나온다 → 그래서 못 쓴다** | |

태생적 베이스가 같으니 파일은 물리고 에러도 안 나는데 결과만 망가진다 — 그래서 원인을 못 찾고 헤맨다.
Civitai 에 "SDXL 1.0" 이라고만 적혀 있어도 **어느 파생 베이스에서 학습한 로라인지**를 봐야 하는 이유가 이것이다.

같은 원리가 지금도 그대로 반복되고 있다.

| 사례 | 왜 |
|---|---|
| **ANIMA 에 ILXL 로라를 못 쓴다** | 태생적 베이스부터 다르다 (ANIMA 는 NVIDIA Cosmos-Predict2 2B 기반) |
| ANIMA 로라도 **베이스 버전(프리뷰1~3 · 정발 Base 1.0)에 맞춰** 골라야 한다 | 같은 이름의 모델도 파생 지점이 다르면 어긋난다 |
| SD1.5 로라를 SDXL 에 못 쓴다 | 태생적 베이스의 버전 자체가 다르다 |

→ [로라 쓰는 법](lora-usage.md) · 받는 곳은 [자원](resources.md)

### 병합 — 태생적 베이스가 같아야 하고, 같아도 잘 안 섞인다

WebUI 가 지원하는 기본 병합식은 이것 하나다.

```text
A*(1-m) + B*m          m 은 0 ~ 1
```

`m` 이 A 와 B 의 비율을 정한다. 규칙은 셋이다.

- **태생적 베이스가 같은 것끼리만** 병합된다 — 1.5 는 1.5 끼리, XL 은 XL 끼리. SD1.5 와 SDXL 은 아예 안 된다
- 태생적 베이스가 같아도 **부모가 다르면 잘 안 섞인다** — 아니마진·ILXL·PONY 는 **물과 기름**이라는 것이 원문의 표현
- 1 + 1 이 2 가 되지 않는다. 위 단순 비율식에는 한계가 있고, 모델별 장점만 골라 섞으려면
  **U-Net 레이어를 하나하나 신경 써서 병합**해야 하는데 알려진 정보가 많지 않다

LoRA 를 모델에 병합해 넣는 것도 가능하다. 블록별 병합의 발상은 아래 "옛 SD1.5 자료를 읽을 때" 항목을 보라.

### ⚠️ 본문의 오기 하나 — Illustrious 의 베이스는 **kohaku beta5** 다

이 글의 **초판 본문은 Illustrious 의 베이스를 'kohaku 제타(zeta)'** 라고 적었다. **이 표기는 틀렸다.**

> **댓글 8번의 정정** — "illustrious 는 kohaku **beta5** 를 베이스로 만들었더라구요.
> zeta 가 나온 시점에 왜 beta5 를 썼는지 모르겠습니다만, 암튼 그렇습니다"
> 근거로 `https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0` 를 달았다.
>
> **원글쓴이도 "아 제타가 아니라 베타였구나" 라며 수용해 본문을 고쳤다**(현재 본문은 `kohaku-xl-beta`).

정정 쪽에 제작자 저장소 링크와 원글쓴이의 수용이 함께 있으므로 **kohaku beta5 가 맞다.**
옛 캡처본이나 재배포본에서 '제타' 표기를 보게 되면 그것이 초판이다.

### 곁다리로 정리된 두 낱말

| 질문 | 답 |
|---|---|
| **NAI(3) 는 뭔가** | NovelAI 사 이미지 모델의 3번째 버전. **베이스는 SDXL** 이고 클라우드 방식이라 사양과 무관하게 쓸 수 있는 대신 인터넷이 필수이고 **LoRA 를 쓸 수 없으며 모델에 손댈 수 없다** → [NovelAI](nai.md) |
| **FLUX 는 뭔가** | 베이스 모델 중 하나. StabilityAI 가 아니라 거기서 나온 사람들이 모인 **Black Forest Labs** 가 만들었다. 성능만큼 사양이 무겁고 **증류(distilled) 모델이라는 특징 때문에 파생 모델이 많지 않다** |

> **시점 주의 (2024-10)** — 위의 *원리*(태생적/파생적 베이스, 계보, 병합식, 로라 호환 규칙)는 지금도 그대로다.
> 다만 *예시로 든 모델과 프로그램 지원 현황*은 낡았다. 지금 채널의 기본값은 위의 "체감 대세" 항목을 보라.


<small>근거 — [응애 뉴비가 설명하는 AI모델의 개념 24.10](https://arca.live/b/aiart/119613811)</small>

## 먼저 나누기 — 이미지 모델과 영상 모델은 다른 물건이다
<small>2026-05 기준 · 근거 2건</small>

받아야 할 파일도, 필요한 장비도, 난이도도 완전히 다르다. **둘을 동시에 시작하지 마라.**

| | 이미지 모델 | 영상 모델 |
|---|---|---|
| 하는 일 | T2I(글 → 그림), I2I(그림 → 그림 수정) | T2V(글 → 영상), I2V(그림 → 영상), FLF2V(첫·끝 프레임) |
| 파일 크기 | 2~7GB 급 (ANIMA INT8 은 4GB 미만) | 수십 GB 급, High/Low 로 두 벌인 경우도 있음 |
| 입문 난이도 | 통합팩으로 바로 시작 가능 | **입문 비추천** |

> **로컬 영상 AI 는 입문에 비추천이며, 고사양 + ComfyUI 고인물이면 그때 보라**는 것이
> 채널 FAQ 의 답이다 (2026-05 기준).

한 작성자는 셋의 역할을 이렇게 단순화해 둔다 — **T2I 는 이미지 생성, I2I 는 이미지 찐빠 수정, I2V 는 이미지 영상화.**
그리고 이것을 복합적으로 쓴다. 원하는 중간 자세가 있으면 T2I 배치를 늘리기보다 나노바나나나 Qwen 에
I2I 로 던져 각을 바꾸고, 그림체가 뒤틀리면 T2I 결과의 EXIF 를 I2I 에 적용해 수정하며,
레퍼런스가 더 필요하면 I2V 로 뽑아 프레임 단위로 분리해 고른다(한 글에서만 언급됨).

장비 기준은 [처음이라면](overview.md) 과 [VRAM·속도 최적화](vram.md) 를 보라.
참고로 **애플 맥은 AI 연산이 느려 비추천**이고, RTX 5060 8GB 가 M4 맥미니보다 대략 8배 이상 빠르다는
정리가 있다 (2026-05 기준).

<small>근거 — [최근 AI 그림 자주 묻는 질문 (26년 5월 기준) 26.05](https://arca.live/b/aiart/170655900) · [ComfyUI - 다양한 워크플로우를 써 본 소감과 활용방법. 26.01](https://arca.live/b/aiart/160605007)</small>

## 이미지 모델 지형도 — 티어 정리 (2026-05 기준)
<small>2026-05 기준 · 근거 1건</small>

**한 글에서만 언급된 정리**지만 이 주제를 통으로 다룬 유일한 글이라 그대로 옮긴다.
**티어는 무검열 아니메 능력이 아니라 '깡성능' 기준**이라는 단서가 붙어 있다.

| 티어 | 모델 | 성격 |
|---|---|---|
| 1티어 | GPT-Image 2 / Nano-Banana 2 Pro | 웹 서비스 전용 |
| 2티어 | Z-Image-Turbo · Z-Image-Base / Qwen-Image-Edit-2511 | Qwen 쪽은 20B 라 **최적화 필수** |
| 3티어 | Flux.2 Kevin 9B / Chroma1-HD | Chroma1-HD 는 **무검열 최고 성능이나 매우 느림** |
| 4티어 | ANIMA 시리즈 / NAI 4.5 | |
| 5티어 | NoobAI · Illustrious XL 기반 SDXL 모델 | 채널 입문 기본값 |

작성자가 댓글에서 보충하기를, **아니메 무검열 기준으로 보면 ANIMA 는 2~3티어급**이다.
즉 위 표는 "그림 잘 그리는 순서" 이지 "이 채널에서 쓸모 있는 순서" 가 아니다.

링크:
- ANIMA `https://huggingface.co/circlestone-labs/Anima`
- NoobAI `https://huggingface.co/Laxhar/noobai-XL-1.1`
- Z-Image-Turbo `https://huggingface.co/Tongyi-MAI/Z-Image-Turbo`
- Qwen-Image-Edit-2511 `https://huggingface.co/Qwen/Qwen-Image-Edit-2511`
- Chroma1-HD `https://huggingface.co/lodestones/Chroma1-HD`
- NAI `https://novelai.net/`

**파운데이션 모델도 하나 더 있다.** Ideogram 4.0 이 가중치를 공개했고(9.3B — Z-Image 6B 보다 무겁고
Qwen·Flux 보다는 월등히 가볍다), 네이티브 2K 생성과 폐쇄 모델급 텍스트 렌더링이 강점이다.
다만 **라이선스가 빡빡하고 모델 내부 안전 필터 때문에 `Image blocked by safety filter` 출력이 잦다**는
실사용 제약이 댓글에서 지적됐다 (2026-06 기준).

<small>근거 — [(미니 정보) 26년 5월 기준 간단하게 소개하는 그림 AI… 26.05](https://arca.live/b/aiart/169601993)</small>

## 체감 대세 — 웹은 NAI 4.5 Full, 로컬은 ANIMA. 다만 입문 기본값은 아직 Illustrious
<small>2026-08 기준 · 근거 5건</small>

티어표와 실제로 채널에서 굴리는 것은 다르다. 두 층으로 나뉘어 있다.

**(가) 대세 — 2026-05 기준 FAQ**

> 체감 대세는 **NAI 4.5 Full(웹) / ANIMA(로컬)**.
> NAI5 는 아키텍처 설계 마무리 단계로 학습도 시작 안 했고 빨라야 3개월 뒤 소식.
> ANIMA 는 **2026-05-15 정식 출시**.

**(나) 입문 기본값 — 통합팩 배포글 세 편이 일관되게 추천하는 체크포인트**

> `설치폴더\ComfyUI\models\checkpoints` 에 **WAI-illustrious-SDXL**
> (`https://civitai.red/models/827184/wai-illustrious-sdxl`).
> `WAI NSFW` 는 이름만 다른 동일 모델이다.

둘이 모순은 아니다. **(나) 는 "지금 바로 딸깍해서 그림이 나오는 조합"** 이고
**(가) 는 "품질을 더 올리고 싶을 때 갈아탈 곳"** 이다.
통합팩의 기본 워크플로우와 노드 자체가 SDXL/Illustrious 기반 2D 그림용으로 짜여 있어,
wan 이나 z-image 를 쓰려면 워크플로우를 따로 마련해야 한다.

ANIMA 로 넘어갈 때 필요한 파일 세트는 다음과 같다.

| 파일 | 위치 |
|---|---|
| `anima-base-v1.0.safetensors` (또는 Aesthetic v1.1) | `설치폴더\ComfyUI\models\diffusion_models` |
| Text Encoder | `설치폴더\ComfyUI\models\text_encoders` (`qwen_3_06b_base.safetensors` 로 개명 권장) |
| VAE | `설치폴더\ComfyUI\models\vae` |

세부 설정은 [ANIMA](anima.md) 를 보라.

### ⚠️ "야짤은 pony 가 낫다던데요" — 2026-08 기준 아니다

입문 2일 차가 `noobaiXLNAIXL` 로 잘 뽑다가 *"pony 가 야짤을 더 잘 만든다"* 는 말을 듣고
`score_9` 같은 태그를 붙여 옮겼더니 오히려 결과가 깨졌다는 질문에 대한 답이다 (2026-08).

> **pony 는 3년쯤 전 세대의 모델이고, `score_9` · `score_8` 품질 태그 관행도 그 시절 가이드의 흔적이다.**
> 옛날 가이드를 보고 있는 것이라는 지적이 여러 번 나왔다.

| | 지금 |
|---|---|
| 로컬 이미지 생성 | **ANIMA 가 사실상 평정했다** (`krea2` 가 함께 언급된다). 둘 다 채널에 정보글이 있고 Civitai 에서 받는다 |
| 구시대 모델 | 그 모델 특유의 그림체를 **일부러** 원하는 경우가 아니면 쓸 일이 없다 |
| 그래도 pony 를 고려한다면 | **`illustrious` 가 낫다.** ANIMA 가 전반적으로 우수하지만 illustrious 계열은 **LoRA 생태계가 넓어** 디테일과 LoRA 활용에서 이득이 있다 |

결론은 **모델을 바꾸는 대신 쓰던 모델을 유지하고 인페인트 연습으로 넘어가는 편이 낫다**는 방향이었다.
스코어 태그 자체의 성격은 [ANIMA](anima.md) 의 `score` 태그 항목에 있다.


<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [최근 AI 그림 자주 묻는 질문 (26년 5월 기준) 26.05](https://arca.live/b/aiart/170655900) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430)</small>

??? note "근거 5건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [최근 AI 그림 자주 묻는 질문 (26년 5월 기준) 26.05](https://arca.live/b/aiart/170655900) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430) · [뉴비 꼭 pony할 필욘 없지? 26.08](https://arca.live/b/aiart/179433132)

## 실사용 3자 비교 — Krea 2 · ANIMA · ILXL 은 무엇이 다른가
<small>2026-07 기준 · 근거 1건</small>

티어표가 *"어느 쪽이 잘 그리나"* 라면, 이건 **같은 프롬프트를 세 모델에 그대로 넣고 비교한 실사용 후기**다.
**한 글에서만 다룬 비교**이지만 세 모델의 성격이 갈리는 지점을 정확히 짚어 그대로 옮긴다 (2026-07).

```text
테스트 프롬프트 (ANIMA 는 Aesthetic 1.0 사용)
masterpiece, best quality, newest, highres, absurdres, very aesthetic, anime screencap,
flat color, cel shading, sensitive, yanineko, 1girl, solo, cat girl, animal ears,
messy pale green hair, brown eyes, casual clothes,
sitting by a cafe window with a cup of coffee, warm afternoon light,
relaxed, soft smile, looking out the window, upper body
```

| | 강점 | 약점 |
|---|---|---|
| **Krea 2** | 질감·색감이 훨씬 자연스럽고 **체급이 있어 묘사가 매우 정확**하다. 유리창 얼룩과 반사, 전신주·전선·벽돌까지 배경을 정확하고 다양하게 배치한다. **같은 로라를 쓴다면 ANIMA 보다 훨씬 낫다** | **NSFW 지식이 사실상 전무.** ANIMA 보다도 훨씬 무거운 구동, 로라 용량도 기본 수백 MB (큰 것은 900MB) |
| **ANIMA** | score 태그가 없고 기본 로라가 괜찮아 자연스럽게 나온다. **로라 없이 프롬프트만으로 즉각 탈의**한다 | **노이즈를 너무 제거해 채색이 단순해지고 보더(윤곽선)가 강조돼 'AI 티'가 두드러진다.** 원 모델의 지향성이 너무 강해 상쇄가 힘들다 |
| **Illustrious XL** | **압도적인 로라 물량과 네거티브 임베딩**으로 AI 티를 뺄 수 있고 색·질감 표현 범위가 넓다. 색감은 ANIMA 보다 나아 로라 색감용 재료로 쓸 만하다 | **VAE 해상도가 낮아 손가락 찐빠가 심하고 눈·무늬가 조금만 작아지면 뭉개진다 → Hires fix 와 디테일러가 필수.** 자연어를 못 알아들어 상호작용·다인 구도에서 못 비빈다 |

### ⚠️ Krea 2 의 NSFW 는 '약하다' 가 아니라 '없다'

`pussy`, `stained sheet` 같은 태그를 넣어도 **싸그리 무시하고 심지어 뿔이나 피부색 지정까지 버린다.**
겉옷 안에 누드·spread leg 를 넣어도 전부 무시하고 '하의 실종' 을 넣으면 알아서 바지를 입힌다.
몸비틀기를 하면 뜬금없이 실사가 튀어나오거나 인간 신체가 아닌 것이 나온다. danbooru 태그도 적용될 때와
안 될 때가 갈린다. 결국 **로라를 찾거나 만들어야 한다.**

> **댓글의 보강이 중요하다** — 우회 필터를 쓰면 프롬프트가 어느 정도 통하는데,
> 이 필터가 **성적 표현만 막는 것이 아니다.** *"주인공이 울면서 눈물을 흘린다"* 같은 태그까지 걸려서,
> **폭력·고통·슬픔 등 부정적 요소 전반**이 필터에 잡혀 있는 것으로 보인다.
> 완화 로라 `https://civitai.com/models/2775340/krea2-textfusion-refusal-reduction-lora` 가
> 레딧에서 좋은 반응을 얻었다고 소개된다.

### 곁다리 — 그림체를 자연어로 바꾸는 실전 팁

Krea 2 와 ANIMA 는 자연어를 알아들으므로, 아래 같은 **서술문**을 넣으면 그림체가 극적으로 바뀐다
(Illustrious 에서는 통하지 않는다).

```text
Edges transition organically—sharp and refined in focal areas such as the face, while gradually
dissolving into loose, unfinished sketch marks and partially erased lines toward the outer regions.
Hair and clothing are depicted with flowing, expressive, and incomplete strokes. The upper and lower
sections fade into abstraction, blending into negative space and raw construction marks. Background
features a warm brown, textured cardboard-like paper with visible fibrous matte grain and subtle
vignette (darker edges, lighter center), merged with a faint studio-like atmospheric depth.
No text elements.
```

### 결론 (작성자)

> 사양이 되고 NSFW 문제가 해결되면 **Krea 2 가 의심의 여지 없이 원탑**,
> 그렇지 않으면 **ANIMA**(강력한 기본 NSFW + 지속 개선 기대),
> **ILXL 은 아직 압도적 로라 물량 덕에 그럭저럭 쓸 만하다.**

ILXL 의 Hires·디테일러 부담은 [업스케일과 화질](upscale.md) 과 [디테일러](detailer.md) 를,
ANIMA 설정은 [ANIMA](anima.md) 를 보라.


<small>근거 — [스압) krea2, 아니마, ilxl 비교 26.07](https://arca.live/b/aiart/176897194)</small>

## 로컬에서는 못 쓰는 것 — 가중치를 공개하지 않은 모델
<small>2026-05 기준 · 근거 4건</small>

**상위권 영상·이미지 모델 상당수는 가중치가 공개되지 않아 로컬 실행이 아예 불가능하다.**
세 편 이상의 글이 각각 이를 확인한다. 성능 순위표를 보고 "이걸 받아야지" 했다가 시간을 버리는 일이 잦아
먼저 걸러 둔다.

| 모델 | 상태 | 쓸 수 있는 경로 |
|---|---|---|
| Happy Horse 1.0 (알리바바, 2026-04-27) | **가중치 미공개** | 공식 데모(happyhorse.cn / happyhorse-ai.com) · fal.ai API · 알리바바 클라우드. 초당 6크레딧, 월 19.99달러에 400크레딧 |
| HappyHorse (출시 전 정보) | 제목이 **'(오픈소스 아님 확정)'** 으로 정정됨. 사이트·트위터 게시물이 삭제돼 페이크 모델 얘기까지 붙음 | — |
| Gemini Omni Flash (구글) | 웹·앱 전용 | 제미나이 앱, Google Flow (AI Plus/Pro/Ultra 구독자), YouTube 쇼츠·YouTube Create 는 무료. 모든 출력에 **SynthID 워터마크** |
| Seedance 2.0 (시댄스) | 웹 서비스 | — |
| ChatGPT Images 2.0 (OpenAI) | 웹 서비스 | 2K 해상도, 한 요청으로 다중 이미지 동시 생성 |

Happy Horse 1.0 을 소개한 글은 **본문 대부분이 제미나이 요약본**이고, 작성자 스스로
'조만간 가중치가 풀리면 ComfyUI 노드로 나올 것' 부분은 제미나이의 오류라고 표시해 두었다.
참조로 걸린 GitHub 저장소도 공식이 아니라 커뮤니티 유출 정보를 모으는 개인 저장소다.

**ChatGPT Images 2.0 의 한국어 한계** — 이미지 안에 다국어 텍스트를 배치하는 것이 강점으로 홍보됐지만,
댓글에서 한국어 생성 결과의 자모 오류가 다수 관찰됐다('생'성, 렌더'렁', '톡'히, 벵'굴'어, '게'선, 느'껴'지는).

<small>근거 — [알리바바에서 딸내미 하나 샀음 (happy horse 1.0… 26.04](https://arca.live/b/aiart/169030124) · [Gemini Omni를 소개합니다. 26.05](https://arca.live/b/aiart/171183268) · [(오픈소스 아님 확정) 새로운 SOTA급 T2V/I2V 모델… 26.04](https://arca.live/b/aiart/167106042) · [ChatGPT Images 2.0을 소개합니다! 26.04](https://arca.live/b/aiart/168399124)</small>

## 로컬로 돌릴 수 있는 영상 모델
<small>2026-08 기준 · 근거 9건</small>

가중치가 공개돼 ComfyUI 에서 돌릴 수 있는 쪽만 모았다.

| 모델 | 성격 | 실행 조건 |
|---|---|---|
| **MiniMax H3** (2026-08-03 오픈웨이트) | 옴니모달 — 텍스트·이미지·오디오·비디오 입력 → 비디오 출력. 2K 출력, 스테레오 오디오 | RTX 3060 12GB + RAM 32GB 로도 구동 확인. AMD 5600G + DDR4 3200 32GB + RTX3060 에서 8분 53초 실측 |
| **Wan 2.2** | I2V·T2V. High/Low 두 모델 분리 구조 | VRAM 12GB 이상 권장 |
| **LTX 2.3** | Audio-to-Video, 20초 영상, 4K 50FPS, 네이티브 세로(1080×1920) | 5090 기준 512x768/8스텝/121프레임 12초 |
| **Bernini** (ByteDance) | Wan 2.2 파인튜닝 옴니 모델. **편집(edit) 성능이 강점**, i2v 등은 예시가 적어 판단 어려움 | ComfyUI PR #14216 (Kijai) |
| **Cosmos3** (NVIDIA) | Super 64B / Nano 16B, OpenMDW-1.1 | **목적이 다르다** — 미적 기준·연출이 아니라 **로보틱스 현장 시각 데이터 증강**용 |
| **Lance** (ByteDance) | 이미지·비디오 이해/생성/편집 통합 | **최소 40GB VRAM 권장**. 댓글 평은 "개별 기능은 전용 모델이 더 낫다" |
| **lingbot-video-moe-30b-a3b** | MoE, ANIMA(cosmos2) 계열 DiT. T2V·I2V·TI2V | 전체 30B / 활성 3B, 쌩모델 약 90GB |

**아레나 점수 (2026-07-31 기준)** — 씨댄스 2.0 **1196** / MiniMax H3 **1185** / 그록 **1114**.
1위인 씨댄스는 웹 전용이므로, **MiniMax H3 가 로컬로 돌릴 수 있는 것 중 사실상 최상위**다.

**MiniMax H3 를 쓸 때 알아 둘 구조적 특성 두 가지** (개발팀 AMA):

- 기본 해상도가 **768p** 이고 2K 업스케일링도 원본이 768p 여야 한다. 그 이하는 저해상도 취급이다
- 시드가 같아도 **해상도가 바뀌면 다른 영상이 나온다.** 따라서 저해상도로 미리보기를 뽑고
  마음에 들면 고해상도로 다시 뽑는 방식이 잘 통하지 않는다
- 5+17 프레임 고정 구조를 쓰며, 이는 토큰의 시공간 분포를 고르게 하기 위함이다

자세한 운용은 [MiniMax H3](minimax-h3.md) 와 [비디오 생성](video-generation.md) 을 보라.

<small>근거 — [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [MiniMax-H3 오픈웨이트 모델의 출시일이 공개 26.07](https://arca.live/b/aiart/178585330) · [LTX-2.3 영상모델 출시 26.03](https://arca.live/b/aiart/164020977)</small>

??? note "근거 9건 전부 보기"
    [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [MiniMax-H3 오픈웨이트 모델의 출시일이 공개 26.07](https://arca.live/b/aiart/178585330) · [LTX-2.3 영상모델 출시 26.03](https://arca.live/b/aiart/164020977) · [nvidia에서 cosmos3 출시했네. 26.06](https://arca.live/b/aiart/172423630) · [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부… 26.08](https://arca.live/b/aiart/178717529) · [Bernini (비디오 omni 모델) Comfy에 곧 PR… 26.06](https://arca.live/b/aiart/172591568) · [재밌는 비디오 제네레이션 모델 나왔네. 26.07](https://arca.live/b/aiart/176717035) · [Lance: ByteDance의 통합 다중 모드 모델 (생성… 26.05](https://arca.live/b/aiart/171096415)

## ANIMA 는 무엇 기반이고 왜 가벼운가
<small>2026-07 기준 · 근거 9건 · 자료 엇갈림</small>

로컬 이미지 모델 중 채널이 가장 많이 다루는 것이 ANIMA 다. 고르기 전에 알아 둘 것.

**기반** — **NVIDIA Cosmos-Predict2 2B** 이다. 세 편의 글이 이를 확인한다.
Cosmos-Predict2 시리즈는 원래 로봇팔·자율주행 학습 데이터 생성이 주목적인 i2v 모델이고,
2.0 2B 와 2.5 2B 의 구조가 사실상 동일해서 NVIDIA 쪽 증류 모델을 가져와 DMD2 LoRA 로 추출하는 것도 가능했다.
cosmos2 는 2B 와 14B 의 벤치 성능이 비슷했다는 언급도 있다.

**용량** — 2B 급이라 가볍다. **ANIMA INT8 은 모델 + 텍스트 인코더 + VAE 를 합쳐도 4GB 미만이라
VRAM 8GB 급에서도 무난**하고, int8 모델을 쓰면 원본 대비 **1.3배 이상 빠르다**.

| 배포본 | 크기 | 비고 |
|---|---|---|
| `Bedovyy/Anima-INT8` int8convrot | 2.46GB | 0번·끝번 레이어를 bf16 으로 유지해 정확도가 더 높음 |
| `Bedovyy/Anima-INT8` int8rowwise | — | 품질이 약간 낮고 더 빠름 |
| Civitai `Anima int8 / mxfp8 - Aesthetic v1.1` | 2.09GB | |
| comfy-model-tools 로 자작 | 2.20GB | 아래 항목 참조 |

**대가** — 체급이 작아 **양자화에 취약하다.** GGUF 는 `Q8_0` 이 마지노선이고 그 아래(q3 등)는 유화처럼 뭉개진다는
평이 여럿이다. RTX4000 시리즈 이상이면 BF16 이 가장 빠르다.

**파생 모델이 많다.** `novaAnimeAM`, `waiANIMA`, `Z-Anime` 등. 다만 파생 모델이 화풍을 심하게 바꿔
특정 화풍을 못 살린다는 비교글이 있는데, **비교 방법 자체가 편향됐다는 반론이 강하게 제기됐고
작성자도 인정했다**(베이스에서 학습한 LoRA 로 파생 모델을 비교했기 때문). 그대로 믿지 마라.

Z-Anime(알리바바 Z-Image Base 6B 전체 파인튜닝)은 8GB VRAM 에서 돌아가도록 설계됐지만,
**데이터셋이 AI 생성 이미지로 학습된 정황**이 지적돼 "아직은 ANIMA 가 낫다" 는 평이 지배적이다 (2026-04 기준).

**텍스트 인코더를 더 큰 것으로 바꾸면 좋아지나 — 실험은 무산됐다.**
개발자가 텍스트 인코더를 `Qwen3 0.6B` → `Qwen3.5-2B-Base` 로 올리는 실험을 돌려 **기존 품질의 약 95%** 까지
갔지만 **채택하지 않았다**(허깅페이스 디스커션 #67, 2026-05).

| 왜 접었나 |
|---|
| 작가·캐릭터 지식이 미미하게나마 **눈에 띄게 뒤처졌고** 완전 복구에 **약 2주 연속 학습**이 더 필요했다 |
| 손실 곡선 감소율에 뚜렷한 개선이 없었고, 수동 테스트에서도 프롬프트 이해도 향상이 관찰되지 않았다 |
| 실험 모델 공개 요청도 거절됐다 — 성능이 낮고, 중간 해상도로 학습돼 **1024 에서 제대로 동작하지 않으며**, 공개되지 않은 커스텀 코드가 필요하다 |

여기서 나오는 일반 규칙 하나 — **인코더를 갈아 끼운다고 그림이 좋아지지 않는다.**
스타일·작가·캐릭터 지식 상당 부분이 DiT 가 아니라 **LLM 어댑터에 저장돼 있어**, 인코더를 바꾸면
전체 데이터셋을 다시 학습해야 하기 때문이다.

> ⚠️ **낱말 주의** — 이 실험을 소개한 글은 본문 말미에서 *"CLIP 모델을 상위의 것으로 바꿔보니"* 라고 요약했는데
> **이 표현은 틀렸다.** ANIMA 의 텍스트 인코더는 CLIP 이 아니라 **Qwen3 계열 LLM** 이다.
> CLIP 은 SD1.5·SDXL 시절 인코더를 가리키는 말이다.

설정값은 [ANIMA](anima.md) 로.

### 파생 판이 하나 더 늘었다 — Anima 2.9B (2026-08-12)

공식이 아니라 **제3자가 튜닝 + 레이어 확장**한 판이다. `2.9B` 는 파라미터 29억 개라는 뜻이지 버전 번호가 아니다.
**Transformer 블록이 28 → 40 으로 늘어(기존 블록 사이에 12개 삽입) 기존 로라를 그대로 물릴 수 없고**,
VRAM 은 약 8GB → 9.5GB, 모델 파일은 약 +1.6GB 다. 지식 컷오프는 **2026년 7월**.
블록 대응표와 전용 로더는 [ANIMA](anima.md) 의 'ANIMA 2.9B' 절에 있다.

파생 체크포인트(`wai` · `nova` · `yume` · `miao`)의 실사용 비교와
**'자작 로라를 쓸 거면 파생판보다 베이스(aesthetic v1.1)가 낫다'** 는 다수 의견도 같은 문서에 정리해 두었다.

<small>근거 — [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [anima2.9b 출시 26.08](https://arca.live/b/aiart/179710466) · [Anima에서 사용할 수 있는 DMD2 LoRA 26.03](https://arca.live/b/aiart/164898297) · [Anima Base / novaAnime / wai 화풍 비교 26.06](https://arca.live/b/aiart/172910863)</small>

??? note "근거 9건 전부 보기"
    [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [anima2.9b 출시 26.08](https://arca.live/b/aiart/179710466) · [Anima에서 사용할 수 있는 DMD2 LoRA 26.03](https://arca.live/b/aiart/164898297) · [Anima Base / novaAnime / wai 화풍 비교 26.06](https://arca.live/b/aiart/172910863) · [ComfyOrg 공식모델들에 int8convrot 추가됨 26.07](https://arca.live/b/aiart/175519662) · [nvidia에서 cosmos3 출시했네. 26.06](https://arca.live/b/aiart/172423630) · [재밌는 비디오 제네레이션 모델 나왔네. 26.07](https://arca.live/b/aiart/176717035) · [아니마와 Qwen3.5 26.05](https://arca.live/b/aiart/170079773) · [다들 아니마 체크포인트 뭐 씀 26.08](https://arca.live/b/aiart/178971620)

## ⚠️ 병합의 함정 — 병합하면 내장 VAE 가 소실된다
<small>2025-10 기준 · 근거 3건</small>

자작 병합본을 받았는데 **색이 물 빠진 듯 채도가 낮거나, 뿌옇거나, 결과에 흰 점이 찍힌다면**
모델 탓도 세팅 탓도 아니다. 거의 언제나 **VAE** 다.

> **체크포인트를 병합하면 원본에 내장(baked)돼 있던 VAE 가 소실된다.**
> 배포자가 저장할 때 VAE 를 다시 굽지 않으면 그 모델에는 VAE 가 없는 상태로 나간다.

**한 글이면 우연이지만 세 글에서 같은 일이 벌어졌다.** 전부 배포자 본인이 원인을 인정하고 재업로드했다.

| 시점 | 모델 | 어떻게 드러났나 | 배포자의 조치 |
|---|---|---|---|
| **2025-02-04** | communitymodel v2 (`n001`~`n005`) | *"n002 에서 n004 로 바꿨더니 같은 조합인데 **채도가 빠져 보인다**"* 는 제보 | *"VAE 굽는 걸 깜빡했다"* 고 인정하고 **2월 4일 23시** 이후 VAE 포함본으로 재업로드 |
| **2025-02-25** | Addillustri v10 v-pred | 처음에는 *"아무 SDXL VAE 나 쓰라"* 고 안내했는데 댓글에서 **baked VAE 상태가 이상하다**는 지적 | **2025-02-25 22시** 에 SDXL VAE 포함본으로 재업로드 |
| **2025-10-06** | 개인 병합본 (supermerger) | *"결과물에 **하얀 점이 찍히고 뿌옇게** 나온다"* | 배포자가 *"VAE 를 안 쓴 것 아니냐"* 고 되물었고 **SDXL VAE 를 걸자 해결** |

### 진단 — 증상으로 거꾸로 짚는다

| 증상 | 원인 |
|---|---|
| 채도가 빠져 물 빠진 색 | 병합으로 VAE 가 소실된 모델을 VAE 없이 돌렸다 |
| **흰 점이 찍히고 전체가 뿌옇다** | **SDXL VAE 미지정** — 2025-10 사례에서 이렇게 특정됐다 |
| 같은 프롬프트인데 버전만 바꿨더니 색이 다르다 | 한쪽에만 VAE 가 구워져 있다 |

```text
대처 — SDXL 계열이면 이것 하나면 된다
  sdxl_vae.safetensors  를  models/vae  (A1111 계열은 models/VAE) 에 넣고
  UI 에서 VAE 를 명시적으로 지정한다
```

### ⚠️ 헷갈리기 쉬운 지점

- **NoobAI v-pred 는 "VAE 를 따로 안 써도 된다"고 알려져 있다.** 그래서 그 파생 병합본에서 채도가 빠져도
  VAE 를 의심하지 않게 된다. 병합되는 순간 그 전제가 깨진다는 것이 요점이다.
- 배포글 본문에 *"VAE 내장(baked)"* 이라고 적혀 있어도 **초판이 그랬을 뿐 재업로드분과 다를 수 있다.**
  세 사례 모두 **본문이 아니라 댓글에서** 문제가 드러났다 — 병합본을 받을 때 댓글을 끝까지 읽어야 하는 이유다.
- 반대로 **노이즈 낀 이상한 그림**은 VAE 문제가 아닐 확률이 높다. v-pred 모델이라면 `ZeroSNR` 과 실행 환경을
  먼저 본다 → 이 문서의 "9-b" 3D-Stock 항목.

VAE 자체가 무엇인지는 [용어집](glossary.md) 을, SD1.5 시절 VAE 파일과 넣는 위치는 이 문서의
"옛 SD1.5 자료를 읽을 때 — 계보 · VAE · 병합" 항목을 보라. 색이 아니라 화질이 문제라면
[업스케일과 화질](upscale.md).


<small>근거 — [(모델공유) Addillustri v10 v-pred(ILX… 25.02](https://arca.live/b/aiart/129841057) · [(v2) 2d 이미지 생성을 위한 noob v-pred 단순… 25.02](https://arca.live/b/aiart/128005836) · [개인병합 모델 세팅 공유 25.10](https://arca.live/b/aiart/149889901)</small>

## 직접 병합해 보기 — supermerger MBW 레시피와 Add Difference
<small>2025-10 기준 · 근거 3건</small>

위 항목이 *"병합본을 받을 때 무엇을 조심하나"* 라면, 여기는 **직접 섞어 보는 쪽**이다.
채널에 레시피가 통째로 공개된 글 두 편이 있고, 접근법이 서로 다르다.

### (가) supermerger MBW — 모델 두 개를 블록별 비율로 섞는다 (2025-10)

도구는 `sd-webui-supermerger` 확장이고, 재료는 **WAI-NSFW-illustrious-SDXL_v15 · Kakarot 2.8D 2025 ·
MelonMIX_XL_V1** 세 개다. `use MBW` 를 체크한 뒤 **Merge Block Weights 탭에서 `XL` 을 선택**하고
`Weights for alpha` 에 숫자 20개를 넣는다.

```text
1단계   모델A = WAI-NSFW-illustrious-SDXL_v15      모델B = Kakarot 2.8D 2025
alpha   0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.3,0.5,0.4,0.65,0.65,0.65,0.65,0.4,0.4,0.4,0.4,0.4,0
        → 병합·저장 (temp1)

2단계   모델A = MelonMIX_XL_V1                      모델B = temp1
alpha   0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.3,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.4,0.4,0.4,0.4,0
        → 병합·저장 (완성)
```

두 벌 모두 **뒤쪽 값이 낮다.** U-Net 앞쪽 블록이 구도·형태에, 뒤쪽 블록이 화풍·디테일에 주로 관여하므로
뒤를 낮춰 특정 모델의 그림체만 가져오는 것이다(블록별 병합의 발상은 아래 "옛 SD1.5 자료를 읽을 때" 항목).

| 생성 세팅 | 값 |
|---|---|
| Sampling Method | `DPM++ 2M` |
| Schedule type | `Karras` *(본문 표기 `Kerras` 는 오타)* |
| Sampling steps | **14** |
| CFG Scale | **4** |

> SDXL 계열답게 steps 와 CFG 가 SD1.5 시절(steps 20~30 / CFG 7~10)보다 훨씬 낮다.
>
> **알려진 한계(댓글)** — 앞머리(`blunt bangs`)가 거의 고정으로 나와 네거티브를 세게 줘도 잘 안 빠진다.
> MelonMIX 특유의 몸매 라인을 빼는 방법을 묻자 배포자는 *"supermerger 에서 관련 블록 값을 찾아
> 바뀔 때까지 시도하는 수밖에 없다"* 고 답했다.
> **그리고 이 모델에는 VAE 가 안 들어 있다 — 위 항목을 반드시 보라.**

### (나) Add Difference — 베이스에 로라를 물타기 한다 (2025-02)

이쪽 글의 값어치는 결과물이 아니라 **방법론**이다. 배포자 스스로 하고 싶은 말은 이것이 거의 전부라고 적었다.

> **마음에 드는 모델이 없으면 그냥 `Noob v-pred` 에 LoRA 를 섞어 써라.**
> 이때 가중치를 `0.7~1` 처럼 과하게 주지 말고 **`0.1~0.6`** 정도로 주면서 **작가명 태그로 최종 출력을 조절**한다.

기본 모델은 나오는 이미지의 미학적 범위가 너무 넓으니, 로라로 물타기 해서 원하는 방향만 나오도록 좁힌다는 발상이다.
**작가명 태그를 쓰지 않는 사람에게는 맞지 않는 방법**이라는 단서가 본문에 붙어 있다.

```text
병합식 (Add Difference)
  NoobAI-XL V-Pred 1.0 * 0.5  +  (Model D − NoobAI-XL V-Pred 1.0) * 0.5

  Model D = Model C 에 LoRA 병합
  Model C = Model A * 0.55 + Model B * 0.45   (Weight Sum)
  Model A, B = 각각 NoobAI V-Pred 1.0 에 작가 LoRA 여러 개를 병합
```

Model B 단계에 들어간 로라와 가중치가 전부 공개돼 있다. **음수 가중치가 실제로 쓰인 드문 사례다.**

```text
null1040:0.3   customUdonXL:0.14   Cutesexyrobutts_IL:0.45   cactusman:0.1
kanzarinXL:0.11   Nekoblow_Style:0.14   kedamaaXL:0.08   deal360acv:0.3
nyalia:0.2   arcain-2411:0.11
nekojiraXL:-0.15        ← 음수. 그 화풍의 성향을 빼는 방향으로 작용한다
```

중간 산출물까지 `communitymodel_n001` ~ `n005` 로 공개돼 있어
(`https://huggingface.co/baqu2213/PoemForSmallFThings`) **어느 단계에서 무엇이 달라졌는지 되짚어 볼 수 있다.**
이것이 왜 중요한지는 반대 사례가 보여 준다 — PodoMIX_XL 배포자는 어깨가 넓어 보이는 문제를 지적받고
*"너무 오래전에 병합한 것이라 그림체만 남은 중간 산출물이 없어 수정해 줄 수 없다"* 고 답했다.
**병합 중간 결과를 남기지 않으면 나중에 부작용만 빼는 수정이 불가능하다.**

| 권장 생성 세팅 | 값 |
|---|---|
| 스케줄러 | `KL Optimal` 또는 `SGM Uniform` |
| 샘플러 | `Euler Ancestral CFG++` |
| CFG | **1.1~1.25** (CFG++ 기준) · 일반 `Euler` 라면 **4.5** |
| Steps | **28~35** (댓글) |

> 결과가 과하면 Add difference 로 가중치를 줄인다 — `A: Noob, B: 병합모델, C: Noob, M: 전달할 가중치`.
> CFG++ 계열 샘플러의 CFG 가 왜 1 근처인지는 이 문서의 "저스텝 증류(DMD)·CFG++ 모델" 항목을 보라.

### 부분 병합 — 블록 하나만 가져오기

U-Net 을 통째로 섞지 않고 **`middle block` 만** 병합해 구조·구도 성향만 옮겨 오는 방법도 쓰인다.
PodoMIX_XL(`https://civitai.com/models/1249442?modelVersionId=1408471`)은 반실사 자작 모델에
Illustrious XL 1.0 의 middle block 만 병합했는데, 배포자 스스로 **ILXL 1.0 의 특징이 온전히 나오지는 않았다**고 밝혔다.

*(2025-02 ~ 2025-10. Illustrious·NoobAI 세대의 자료다. 병합의 일반 규칙 — 태생적 베이스가 같아야 한다,
부모가 다르면 안 섞인다 — 은 이 문서의 "베이스 · 파인튜닝 · 병합" 항목에 있다.)*


<small>근거 — [(v2) 2d 이미지 생성을 위한 noob v-pred 단순… 25.02](https://arca.live/b/aiart/128005836) · [PodoMIX_XL 공유 25.02](https://arca.live/b/aiart/128806467) · [개인병합 모델 세팅 공유 25.10](https://arca.live/b/aiart/149889901)</small>

## 채널 자작 병합 체크포인트 — 계열을 알면 권장값이 정해진다
<small>⚠️ 2025-03 기준 · 근거 7건</small>

채널에는 자작 병합·파인튜닝 체크포인트가 꾸준히 올라온다. **어느 계열에서 갈라져 나왔는지를 보면 권장값이 정해진다** — 계열이 같으면 샘플러·CFG·스텝이 거의 같기 때문이다.

### Illustrious / NoobAI 계열 병합본 (2024-12 ~ 2025-03)

| 모델 | 계열 · 성격 | 권장값 | 받는 곳 |
|---|---|---|---|
| **OBNMix_V1** (2024-12) | NoobAI 1.1 + NAI 학습 LoCon + 748cmSDXL LoRA + Obsession. 퀄리티가 아니라 **기본 그림체·색감**을 취향대로 맞춘 것 | `steps 23` · `CFG 4.4` · `euler_a` + `sgm_uniform` | 최신판은 `https://tensor.art/models/830701663783315316` *(본문 링크는 V1)* |
| **CherryMIX_XL_V2** (2025-01) | V1 의 스타일 LoRA 가 디테일을 뭉개던 문제를 개선. **손 타율과 배경 묘사**가 좋아졌다 | `steps 28` · `CFG 5~7` · `dpmpp_2m` + `sgm_uniform` (또는 `ddim` + `ddim_uniform`) | `https://civitai.com/models/1079112?modelVersionId=1273212` |
| **RoseMIX_XL_V1.1** (2025-01) | CherryMIX_XL_V2 에 실사 모델을 강하게 병합한 **반실사 지향**. 머리가 작아져 전신에 유리 | 위와 동일 | `https://civitai.com/models/1132549/rosemixxl` |
| **communitymodel_n001 / n002 / n003** (2025-01) | NoobAI-XL **V-Pred** 1.0 + 스타일 LoRA 단순병합, 2D 화풍. n002 는 외곽선이 굵고 플랫, n003 은 중간 | 스케줄러 `KL Optimal` · `Euler Ancestral CFG++` 계열 `CFG 1.15` (없으면 `Euler` `CFG 5.5`) | `https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/communitymodel_n001.safetensors` |
| **communitymodel_n007c (v3)** (2025-02) | 같은 계열 후속. AI 특유의 매끈한 피부를 줄이고 **거친 드로잉·스케치 질감** | 스케줄러 `KL Optimal` · `Euler A DY CFG++` · `CFG 1.35~2` | `.../communitymodel_n007c.safetensors` |
| **NAI-XL vpred1.0 2dac - BluemintObsession v6** (2025-03) | 같은 계열의 최신판. 목표는 **로컬에서 작가명 태그로 NAI v2~v3 급을 뽑는 것**. ilxl 1.0 비중이 5% 미만이라 e621 태그도 그대로 쓸 수 있다 | `KL Optimal` 판과 `SGM Uniform` + `CFG Rescale` 판 두 가지 | Civitai 검색 |
| **FuzzyEclipse** (2025-02) | Illustrious-XL 1.0 파인튜닝. 이전 모델의 **외곽선이 흐리던 문제**를 데이터셋을 바꿔 잡음 | `steps 24` · `CFG 6` · `Euler a` · VAE `sdxl_vae.safetensors` 를 **따로 물릴 것** | `https://huggingface.co/Lucetepolis/FuzzyHazel/blob/main/FuzzyEclipse.safetensors` |

**communitymodel 계열은 모델을 안 받아도 된다.** 같은 LoRA 를 같은 가중치로 얹으면 같은 결과가 난다 —
`cactusman 0.2` / `customUdonXL_il_lokr_V5311P 0.3` / `Cutesexyrobutts_IL 0.45` / `kanzarinXL 0.25` /
`kedamaaXL 0.2` / `Nekoblow_Style 0.4` / `null1040 0.55`.

**n007c 의 고정 프롬프트**는 모델 자체가 아니라 프롬프트로 화풍을 만든다.

```text
(sketch, traditional media, watercolor \(medium\), graphite \(medium\):1.1), (no lineart:1.1),
very awa, masterpiece, best quality, amazing quality, absurd res, hi res, highres
```

결과가 마음에 안 들면 이 가중치를 `1.3` 으로 올리고, 살색이 누렇게 뜨면 네거티브의 `(bb \(baalbuddy\):1.3)` 을 `bkub` 등으로 바꾼다.

### DMD 내장 계열 — UncannyValley 와 그 파생

| 모델 | 성격 | 받는 곳 |
|---|---|---|
| **Uncanny Valley noob 3d v1 DMD** (2025-01) | 3D 지향이되 프롬프트에 따라 2.5D, 작가 태그를 박으면 2D 로도 나오는 **반실사 겸용**. NSFW 특화라 프롬프트를 안 넣으면 알아서 수위가 올라간다 | `https://civitai.com/models/507472/uncanny-valley?modelVersionId=1303338` |
| **UncannyValley ilxl1.0+noob** (2025-02) | 위의 ILXL 1.0 혼합판. 목적은 **더 큰 해상도** 하나 — 1280x1600 에 hires 2.5배로 3200x4000 (직전판은 2240x2880) | `https://civitai.com/models/507472?modelVersionId=1413921` |
| **페르소나 스타일 체크포인트** (2025-01 / 2025-02 ILXL판) | UncannyValley 기반. **`persona` 를 적어야 페르소나 화풍**이 나오고 안 적으면 기반의 반실사·3D 가 나온다 (초기판은 `persona, soejima shigenori, anime coloring`) | `https://civitai.com/models/31771/persona-style-checkpoint` |

이 계열의 권장값은 전부 같고 **일반 모델과 완전히 다르다** — 아래 "저스텝 증류 모델" 절을 반드시 읽어라.

### ILXL 1.X 고해상도 계열 — ComradeshipXL

| 판 | 무엇이 다른가 | 권장 CFG |
|---|---|---|
| **v14K** | ComradeshipX v14 를 ILXL 1.0 기반으로 갈아끼운 것. **1536x1536 특화** | `3.0` |
| **v14K2** | v14K + (Arasaka Test 3 − ilxl 0.1) 차이분을 0.5 '더하기'. 혼합이 아니라 더하기라 **뭉개짐과 색감 약화** 부작용이 있다 (작성자도 무리한 병합이었다고 인정) | `2` |
| **v14K3** | 서브 모델을 noobai-XL **EPS 1.1** 로 바꾸고 가중치를 조정해 v14K2 의 부작용을 해결 | `3` |
| **v14K1A** (ILXL 1.1) | 병합식은 v14K 와 비슷하나 **1796x1796 권장 / 2048x2048 최대** | `5~6` |
| **v14K1AX** | 2.5K 해상도로 직접 학습한 LoRA 를 병합해 **1.5K 이상에서 스케치처럼 변하는 ILXL 의 약점**을 완화 | `2.5~3` |

전부 `Euler a` + `SGM Uniform`(없으면 `Simple`/`Uniform`), 20~30 스텝(v14K1AX 는 최소 11)이고
`https://huggingface.co/hanzogak/comradeshipXL/` 에서 받는다.

```text
퀄리티  masterpiece, best quality, very aesthetic, absurdres, amazing quality, beautiful color
네거    polydactyly, extra digits, sketch, text, 2koma, 3koma, 4koma, monochrome, greyscale,
        photo, paper, watermark, logo
```

> `polydactyly` 는 손가락이 여러 개 달리는 **다지증**을 가리키는 의학 용어로, 손가락 개수 오류를 줄이려고 넣는다.

**v14K1AX 만의 함정 하나** — 이 모델의 Hi-res 에서는 `Denoising strength` 를 **`1.0`** 으로 둔다.
보통 hires 에서 `0.4~0.6` 을 쓰는 것과 정반대다.

## 반실사·실사에서 AI 티를 줄이는 첫 선택 — 모델부터 바꾼다
<small>2026-08 기준 · 근거 6건</small>

**"프롬프트를 더 깎으면 실사처럼 보이겠지"** 보다 먼저 해야 할 일이 있다.
현재 카드들을 묶어 보면, **AI 티 감소는 프롬프트보다 체크포인트 선택의 영향이 더 크다.**

| 시작 모델 | 왜 여기서 시작하나 | 바로 쓰는 값 |
|---|---|---|
| **RoseMIX_XL_V1.1** | 실사 모델 병합 비중이 커서 **반실사 인물 비율**이 안정적이고 전신에 유리 | `steps 28` · `CFG 5~7` · `dpmpp_2m` + `sgm_uniform` |
| **NAI-XL 2dac / 2.5dac** | AI 티를 줄이려는 목적이 분명하고, **2D와 반실사 사이를 가장 다루기 쉬운 축**이다 | `Euler` + `SGM Uniform` · `steps 28` · `CFG 4.5` · `CFG Rescale 0.6` |
| **Uncanny Valley noob 3d v1 DMD** | 3D 출발이지만 프롬프트와 작가 태그로 **2.5D~2D까지 왕복**된다 | 저스텝 계열. 본문 아래 "저스텝 증류 모델" 절 우선 |
| **communitymodel / n007c** | 매끈한 피부와 플라스틱 질감을 줄이고 **거친 드로잉·질감**을 얻기 좋다 | `KL Optimal` 계열, `Euler A DY CFG++`, `CFG 1.35~2` |

**카드에서 반복된 공통 원칙**

- ANIMA 는 빠르고 편하지만 **AI 티가 남기 쉬운 계열**로 여러 카드가 수렴했다.
- 실사/반실사 목표라면 **ANIMA 에 실사 태그를 억지로 누르기보다** 위 계열로 출발하는 편이 낫다.
- `2dac` 계열은 고정 네거티브와 샘플러 조합이 이미 공개돼 있어 **입문 재현성**이 높다.
- `Uncanny` 계열은 `persona` 같은 **작품/스타일 단어 하나**로도 방향이 크게 꺾이므로, 체크포인트 성향을 먼저 읽어야 한다.

**즉 "애니 기본 루트" 와 "인스타 감성 반실사 루트" 는 시작 모델이 다르다.**
체크포인트를 잘못 고른 상태에서 프롬프트만 만지면 AI 티를 줄이기 어렵다.

### ⚠️ 두 가지 주의

- **RoseMIX_XL 은 V1 이 아니라 V1.1 을 받아라.** 처음 올린 V1 에 색감·디테일 문제가 있어 작성자가 *"충분히 테스트하지 않고 배포했다"* 며 핫픽스를 다시 올렸다
- **이것들은 전부 체크포인트이지 LoRA 가 아니다.** 배포글 댓글에 실제로 나온 질문이다 — 체크포인트는 그림을 만드는 본체이고 LoRA 는 그 위에 얹는 보조 파일이다. `models/checkpoints` 에 넣는다 → [로라 쓰는 법](lora-usage.md)

원작 모델 라이선스 때문에 CherryMIX·RoseMIX 계열과 그 재병합 모델은 **상업적 이용이 금지**된다.

*⚠️ **시점 주의 (2024-12 ~ 2025-03)** — 이 표는 Illustrious·NoobAI 세대의 자료다. 2026년 기준 채널의
체감 대세는 위 "체감 대세" 항목에 있고, 여기 실린 값은 **그 계열을 쓸 때만** 유효하다.
받는 곳 전반은 [자원](resources.md).*

<small>근거 — [(병합모델공유) OBNMix_V1 24.12](https://arca.live/b/aiart/125081627) · [(v6) 작가명 태그 재현을 목적으로 하는 Noob v-pr… 25.03](https://arca.live/b/aiart/131849412) · [(v3) 2d 이미지 생성을 위한 noob v-pred 단순… 25.02](https://arca.live/b/aiart/128832358) · [병합모델 RoseMIX_XL_V1 공유 25.01](https://arca.live/b/aiart/126129697)</small>

??? note "근거 7건 전부 보기"
    [(병합모델공유) OBNMix_V1 24.12](https://arca.live/b/aiart/125081627) · [(v6) 작가명 태그 재현을 목적으로 하는 Noob v-pr… 25.03](https://arca.live/b/aiart/131849412) · [(v3) 2d 이미지 생성을 위한 noob v-pred 단순… 25.02](https://arca.live/b/aiart/128832358) · [병합모델 RoseMIX_XL_V1 공유 25.01](https://arca.live/b/aiart/126129697) · [병합모델 CherryMIX_XL_V2 공유 25.01](https://arca.live/b/aiart/126129327) · [(모델공유) FuzzyEclipse 25.02](https://arca.live/b/aiart/129333797) · [noob v-pred 모델의 2d 위주 이미지 생성을 위한 … 25.01](https://arca.live/b/aiart/127549205)

## 9-b. 채널 자작 병합본 (2024-11 ~ 2025-07) — 본문보다 댓글이 정확했던 것들
<small>⚠️ 2025-07 기준 · 근거 4건 · 자료 엇갈림</small>

위 "채널 자작 병합 체크포인트" 의 뒷 세대다. **이 네 모델은 공통점이 하나 있다 — 배포글 본문만 읽으면 막히고,
답이 댓글에 있다.** 자작 병합본을 받을 때 댓글을 끝까지 읽어야 하는 이유를 그대로 보여 준다.

### FuzzyLune (2025-04) — 본문에 **베이스 모델이 없다**

```text
https://huggingface.co/Lucetepolis/FuzzyHazel/blob/main/FuzzyLune.safetensors
Sampler Euler / CFG 7 / Steps 24 / VAE sdxl_vae.safetensors 를 따로 물린다
긍정 masterpiece, best quality,
```

원글쓴이가 *"이것저것 섞다가 만든 거라 병합식을 까먹었다"* 고 해서 **본문에는 베이스가 적혀 있지 않다.**

> **댓글이 채웠다** — *"일러스트리어스 기반인가 noob 기반인가"* 를 물은 댓글 4에,
> 원글쓴이가 **"아마 noob 기반이었던 것 같다"** 고 답했다(댓글 5). **NoobAI 계열로 보는 것이 맞다.**
>
> **⚠️ 그리고 hires 없이 고해상도로 직출력하면 깨진다.** 큰 해상도로 바로 뽑으면 그림이 이상하게 나올 것이라고
> 원글쓴이가 밝혔으므로 **기본 SDXL 해상도로 뽑고 업스케일하는 것이 안전하다.**
> **이 두 가지는 본문에 없고 댓글에만 있다.** → [업스케일과 화질](upscale.md)

### LimeMIX_XL (2025-04) — 프롬프트 중복은 **오타가 아니라 의도**다

```text
https://civitai.com/models/1463920?modelVersionId=1655617
steps 28 / cfg 5 / (dpmpp_2m 또는 euler a) + sgm_uniform, 혹은 ddim + ddim_uniform
추천 작가 태그  ciloranko, ningen mame, ask \(askzy\), (eonsang:0.7), atie1225, (wanke:0.9)
```

NoobAI eps 1.1 + Illustrious XL 1.1 병합으로 **고해상도 안정 출력**을 노렸고,
제작자의 로라(특히 몸매 로라)가 함께 병합돼 **캐릭터가 전반적으로 성숙한 체형으로 나온다**고 본문이 미리 경고한다.

본문은 퀄리티 프롬 `masterpiece, best quality, amazing quality, highres, absurdres, very aesthetic, newest,`
를 **앞뒤로 두 번** 감싸 쓰는데, 댓글 9가 *"중복 아니냐"* 고 지적했다.

> **원글쓴이의 정정(댓글 10)** — **의도한 것**이며 경험상 두 번 쓰는 게 더 좋고,
> **한 번만 쓸 거면 맨 뒤에 두라**고 답했다. 지적한 쪽이 틀렸다.

댓글에만 있는 것이 둘 더 있다.

| | 내용 |
|---|---|
| **어깨 수정판** | 어깨가 너무 넓게 나온다는 지적을 받고 **어깨에 영향을 주는 로라를 뺀 버전**을 따로 올렸다 — `https://civitai.com/models/1463920?modelVersionId=1666432` |
| **버전 차이** | **1.1 은 캐릭터가 더 어려 보이고, 1.0 은 더 성숙해 보인다**(댓글 12) |

### 3D-Stock (2025-07) — **노이즈 낀 그림의 범인은 VAE 가 아니다**

```text
https://civitai.com/models/1773389/3d-stock?modelVersionId=2007089        ← vpred 모델이다
Euler a 또는 DPM++ 2M SDE / SGM Uniform / CFG 3~5 / 24~30 스텝
Hires  Denoising 0.3~0.4, 10~15 스텝
해상도 960x1280 / 1280x960 / 1128x1128 / 832x1216 / 1216x832 / 1024x1024
긍정   masterpiece, best quality, very awa, absurdres, highres,
       + cel shading, anime coloring, anime anime screenshot, shiny skin, humid skin  + 3D
```

*"이 모델로 뽑으면 노이즈 낀 이상한 그림이 나온다"* 는 보고에 **VAE 를 의심하는 진단이 먼저 나왔는데,
댓글 6~8 이 이를 바로잡았다.**

> **VAE 문제가 아니라 vpred 관련 문제일 확률이 높다.**
> **ZeroSNR(z snr) 옵션을 건드려야 하고, A1111 WebUI 는 특정 버전이 아니면 v-pred 를 지원하지 않는다.**
> **vpred 모델을 처음 받은 사람이 가장 자주 겪는 증상이다.**

v-pred 모델 전반의 기본 세팅과 실행 환경 제약은 위 "병합의 금기 — eps 와 v-pred 는 섞이지 않는다" 를 보라.

**3D 아바타처럼 나올 때의 대처도 본문에 이유와 함께 적혀 있다** — 네거티브에 **`lips`** 를 넣으면 크게 줄고,
그래도 너무 현실적이면 **`realistic`** 을 추가한다.

### N40NAillousV2-xl (2024-11) — **평가가 정반대로 갈렸다**

vPred 와 epsPred 를 섞는 방법을 설명해 병합에 관심 있는 사람에게 값이 있다.
재료는 NoobAI-XL V-Pred 0.6 · NoobAI-XL 1.0 · NTRMIX 4.0 LoRA · arcain-2411 LoRA · NTR MIX 2.1 퀄리티 LoRA 이고,
**블록웨이트로 vPred 모델의 TE(텍스트 인코더)만 살린 중간 모델**을 만들어 우회했다.

| 댓글에서 나온 것 | 내용 |
|---|---|
| 이게 vPred 모델인가 | **"TE 만 vPred 라 vPred 로 보긴 어렵다"** 고 원글쓴이가 답했다 (댓글 2·3) |
| A1111 에서 안 돈다 | 정식 버전은 vPred 를 그냥 못 돌린다. RTX 2060 에서 CUDA 메모리 오류가 나자 **`fp8` 옵션을 켜니 정상 출력**됐다 (댓글 3·12) |
| NTRMIX 4.0 로라를 또 얹어야 하나 | **병합 초반 과정에 이미 들어가 있으므로 따로 얹을 필요가 없다** (댓글 12) |

> ### ⚠️ 작가 태그 반응성 — 두 사용자의 평가가 정면으로 엇갈린다. 양쪽을 그대로 싣는다
>
> | | 평가 |
> |---|---|
> | **댓글 13** | **"작가 프롬을 잘 못 먹는 느낌"** |
> | **댓글 16** | **"작가 태그를 안 써도 캐릭터 프롬만으로 원작 고증이 잘 나온다"** 며 만족 |
>
> **어느 쪽도 원글쓴이의 확인을 받지 못했다.** 작가 태그 반응성이 약한 대신 캐릭터 재현이 강한 모델로
> 이해하면 두 후기가 모순 없이 읽히지만, 그것은 해석이지 확인된 사실이 아니다. **직접 돌려 봐야 안다.**

*(2024-11 ~ 2025-07. Illustrious·NoobAI 세대의 자료이므로 이 계열을 쓸 때만 유효하다. 받는 곳은 [자원](resources.md))*


<small>근거 — [애니메 3D 스타일 병합모델 공유 25.07](https://arca.live/b/aiart/142309559) · [LimeMIX_XL 공유 25.04](https://arca.live/b/aiart/133867786) · [(모델공유) FuzzyLune 25.04](https://arca.live/b/aiart/133525011) · [병합모델공유 N40NAillousV2-xl 24.11](https://arca.live/b/aiart/121889356)</small>

## 9-c. 작가 태그 재현 특화 계열 — NAI-XL vpred 2dac
<small>⚠️ 2025-06 기준 · 근거 2건</small>

`baqu2213` 의 **NAI-XL vpred1.0 2d accelerated(2dac)** 시리즈다. 위 "채널 자작 병합 체크포인트" 의
communitymodel 계열에서 갈라져 나왔고, **목표가 하나로 뚜렷하다.**

> **NoobAI v-pred 1.0 을 기반으로 '작가명 태그' 재현에 특화시켜, 로컬에서 NAI v2~v3 수준의 그림을 뽑는 것.**
>
> 그래서 두 배포글이 모두 같은 경고를 본문에 박아 두었다 —
> **작가 태그를 쓰지 않는 사람은 이 모델을 쓸 이유가 없다.**

### 판별

| 판 | 시점 | 무엇이 다른가 | 받는 곳 |
|---|---|---|---|
| **v5 (standard)** | 2025-02 | 2D 포커싱 탓에 부자연스럽던 **빛과 살색을 개선**하고 과한 색감을 안정화. 외곽선을 크게 줄이고 realistic 비중을 늘려 rough 한 2D 비율을 낮췄다. **`watercolor, no lineart, realistic` 같은 추가 고정 프롬프트나 네거티브 없이도 균형이 잡히도록** 조정했다 | `https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAI-XL_vpred1.0_2dac_standard.safetensors` |
| **v7 (2.5dac)** | 2025-06 | 2D 기반에 **2.5D 스타일을 일부 섞어 피부·스타킹 질감**을 개선하고 BluemintObsession 과 병합해 2D 포커싱을 유지 | `https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAI-XL_vpred1.0_2.5dac.safetensors` · 미러 `https://tensor.art/models/733388528173472100` |

시리즈 설명 원글 `https://arca.live/b/aiart/128899435`.
v7 에서 원글쓴이는 *"Noob v-pred 에서는 더 파먹을 게 없어 보인다"* 며 **사실상 마지막 버전임을 시사**했다.

### ⚠️ 버전이 올라간다고 상위 호환이 아니다

기존 final 50 과 native 90 을 갖고 있는데 지우고 새 것만 받아도 되냐는 질문에 원글쓴이가 답했다.

> **native 90 은 버려도 되지만 나머지는 다 조금씩 다르니 남겨 두라.**
> 즉 `final` / `standard` / `native` 는 **상위 호환 관계가 아니라 성격이 다른 갈래**다 (v5 댓글 5~7).

### 쓰는 법 — 프롬프트로 2D↔2.5D 를 직접 조절한다

```text
v5 퀄리티  (모델이 균형을 잡아 주므로 추가 고정 프롬프트가 필요 없다)
v7 퀄리티  very awa, very aesthetic, masterpiece, best quality, amazing quality, absurdres
v7 네거    worst quality, blurry, old, early, low quality, lowres, signature, username, logo,
           bad hands, mutated hands, ambiguous form, colored skin, censored genitalia,
           censorship, unfinished, anthro, furry
```

| 하고 싶은 것 | 어떻게 |
|---|---|
| 2.5D 쪽으로 | `(realistic)` 을 **퀄리티 프롬에** 넣는다 |
| 2D 쪽으로 | `(realistic)` 을 **네거티브에** 넣는다 |

> **작가 태그의 위치가 결과를 바꾼다** — **캐릭터 태그 뒤에 아티스트 태그가 오면 캐릭터 태그에 담긴 스타일이
> 아티스트 스타일에 영향을 준다.** 태그 위치와 가중치를 조절할 줄 알아야 한다.
> → [프롬프트 쓰는 법](prompting.md)

> **'사용 가능한 작가 목록' 은 없다** — **3만 명이 넘어서 목록이 있어도 의미가 없다**는 것이 원글쓴이의 답이다
> (v5 댓글 8~9). 취향 작가를 좁히는 절차는 [자원](resources.md) 의 NAIA 랜덤작가 관리 항목에 있다.

### ⚠️ 기대치 — 원글쓴이가 직접 낮춰 두었다

> **`artist collaboration` 태그는 안 먹히고, 성능은 딱 'NAI3 Smea off' 수준이지 그 이상을 바라면 처참하다**
> (v7 댓글 20).
>
> 결국 NAI 와 달리 로컬은 **로라를 넣어 모델을 자기 입맛대로 변형해야 한다**는 것이 원글쓴이의 결론이다.

### v-pred 모델에 로라를 학습시킬 때 — 옵션 두 개가 필수다

```text
v_parameterization     반드시 켠다
zero_terminal_snr      반드시 켠다
```

> **civitai 의 온라인 training 기능은 이 파라미터를 설정할 수 없어서 제대로 안 되고,
> 그렇다고 noob eps 모델로 학습하면 결과가 약해진다** (v7 댓글 14).
> 이 글 최대의 수확이며, v-pred 계열 로라를 만들려는 사람이 가장 자주 걸리는 지점이다.
> → [로라 쓰는 법](lora-usage.md)


<small>근거 — [(v7) 작가명 태그 재현을 목적으로 하는 Noob v-pr… 25.06](https://arca.live/b/aiart/138768269) · [(v5) 작가명 태그 재현을 목적으로 하는 Noob v-pr… 25.02](https://arca.live/b/aiart/129843355)</small>

## 저스텝 증류(DMD)·CFG++ 모델 — CFG 를 낮추지 않으면 탄다
<small>⚠️ 2025-02 기준 · 근거 6건</small>

모델 이름 뒤에 `DMD` 가 붙어 있거나 배포글이 `CFG 1.5~3` 을 권하고 있으면, **그 모델은 일반 모델과 다른 규칙으로 도는 것**이다. 여기를 모르면 "권장값대로 했는데 그림이 탄다" 가 된다.

### DMD — 증류가 체크포인트에 박혀 있는 경우

DMD(Distribution Matching Distillation)는 **적은 스텝으로 뽑게 만드는 증류 기법**이다.
UncannyValley 계열은 이것이 체크포인트 안에 병합돼 있어 **무조건 저스텝 고속 생성만 가능하다.**

| 항목 | 값 |
|---|---|
| Sampling Steps | **10~20** |
| CFG scale | **1.5~3** |
| 샘플러 / 스케줄러 | `Euler a` / `SGM Uniform` |

> **CFG 가 유난히 낮은 이유가 DMD 다. 일반 모델 감각으로 CFG 7 을 넣으면 타버린다.**

네 편의 배포글(Uncanny Valley noob 3d v1 DMD · 페르소나 스타일 · UncannyValley ilxl1.0+noob ·
페르소나 스타일 ilxl1.0+noob)이 **모두 같은 값을 적었다.**

**비DMD 일반 버전은 존재하지 않는다** — 재료 모델들에 이미 DMD 가 박혀 있어서 아예 만들지 않았다고 작성자가 밝혔다.

```text
긍정  masterpiece, very awa, best quality, amazing quality, very aesthetic, absurdres,
      newest, intricate details
```

### CFG++ 계열 샘플러 — 여기도 CFG 를 1 근처로 쓴다

`Euler Ancestral CFG++` · `Euler DY CFG++` · `Euler A DY CFG++` · `Euler SMEA DY CFG++` 는
**원래 CFG 를 1 근처로 쓰는 샘플러**다.

| 모델 | 값 |
|---|---|
| communitymodel_n001~n003 | `CFG 1.15` |
| communitymodel_n007c | `CFG 1.35~2` |
| 이 샘플러들이 없을 때 | 평소대로 `Euler` + `CFG 5.5` |

`Euler SMEA DY CFG++` 에서 이미지가 뿌옇게 퍼지면 `cactusman` LoRA 를 0.1 씩 올려 보정한다.
이 샘플러들이 **reForge 에서만 된다**는 댓글이 있었으나, 다른 댓글이 **포지(Forge)에 샘플러를 설치해 잘 돌렸다고 반박**했다.

### ⚠️ 네거티브로 지워지지 않는 것은 모델의 학습 편향이다

페르소나 스타일(UncannyValley 기반) 사용자가 **네거티브에 `pink lip, lipstick` 을 아무리 강조해도
립스틱이 사라지지 않는다**고 질문했고, 작성자의 답이 중요하다.

> 그건 립스틱이 아니라 **'입술 표현' 자체**이며, 이 모델이 UncannyValley 기반이라 **근본이 3D 라서** 그렇다.
> 해결책은 네거티브를 더 세게 거는 것이 아니라 **입술을 묘사하지 않는 작가 태그를 쓰는 것**이다.

여기서 일반 규칙이 나온다 — **네거티브 프롬프트로 못 지우는 것은 모델의 학습 편향이고, 화풍 태그로 우회해야 한다.**
네거티브 태그의 작동 원리 전반은 [프롬프트 쓰는 법](prompting.md) 의 네거티브 항목을 보라.

*(2025-01 ~ 2025-02. 저스텝·저CFG 라는 성질 자체는 지금의 터보·증류 로라에도 그대로 이어진다 →
[ANIMA](anima.md) 의 터보 로라 절, [국룰](kukroul.md))*

<small>근거 — [Uncanny valley noob 3d v1 DMD 출시 25.01](https://arca.live/b/aiart/126726445) · [(v3) 2d 이미지 생성을 위한 noob v-pred 단순… 25.02](https://arca.live/b/aiart/128832358) · [UncannyValley ilxl1.0+noob 출시 25.02](https://arca.live/b/aiart/128930860) · [페르소나 스타일 Noob xl모델 출시 25.01](https://arca.live/b/aiart/127345203)</small>

??? note "근거 6건 전부 보기"
    [Uncanny valley noob 3d v1 DMD 출시 25.01](https://arca.live/b/aiart/126726445) · [(v3) 2d 이미지 생성을 위한 noob v-pred 단순… 25.02](https://arca.live/b/aiart/128832358) · [UncannyValley ilxl1.0+noob 출시 25.02](https://arca.live/b/aiart/128930860) · [페르소나 스타일 Noob xl모델 출시 25.01](https://arca.live/b/aiart/127345203) · [페르소나 스타일 ilxl1.0+noob 출시 25.02](https://arca.live/b/aiart/129087107) · [noob v-pred 모델의 2d 위주 이미지 생성을 위한 … 25.01](https://arca.live/b/aiart/127549205)

## 10-b. 고속화의 대가 — 3초 모델과 Hyper·Lightning 병합판
<small>⚠️ 2025-06 기준 · 근거 3건</small>

위 "저스텝 증류(DMD)·CFG++ 모델" 의 뒷 세대다. **속도를 목표로 삼은 모델들이 공통으로 치르는 대가**가 여기서 분명해진다.

### UncannyValley V-pred v1 (2025-06) — 한 장 **약 3초**

사양이 약하거나 대량 가챠를 돌리는 사람에게 쓸모가 크다.

```text
https://civitai.com/models/507472?modelVersionId=1916865      (내부 버전은 v1.5 였지만 이제부터 이것이 v1)

(A)  Sampling Step 10  / CFG 1      / Euler a 또는 Euler Ancestral CFG++ / 스케줄러 beta
(B)  Sampling Step 10~20 / CFG 1.5~3 / Euler a                          / SGM Uniform, beta

긍정  masterpiece, best quality, amazing quality, very aesthetic, absurdres
```

WebUI 에서 v-pred 모델을 쓰는 방법은 `https://arca.live/b/aiart/128472488` (순정 dev) 을 참고하라고 안내했다.

> **얼굴 뭉개짐을 손봤지만 여전히 ADetailer 가 필요하다**고 원글쓴이가 밝혔다. → [디테일러](detailer.md)

### Comradeship XL v14VW3H (2025-06) — Hyper + Lightning 병합 고속판

```text
https://huggingface.co/hanzogak/comradeshipXL/blob/main/comradeshipXL-v14VW3H.safetensors
reForge 기준  Euler a / SGM Uniform / CFG 1.0 / 7스텝 / 832x1216 / Rescale CFG 0.5 / ZeroSNR
```

기존 V-Pred 병합모델에 **Hyper SD LoRA 와 Lightning SD LoRA 를 병합**한 것이다.
V-Pred 이므로 **reForge / Forge / ComfyUI** 를 써야 하고 **ZeroSNR 과 RescaleCFG 를 함께 쓰면 좋다**
(참고 `https://arca.live/b/aiart/128421439`).

### ⚠️ 저CFG 고속 모델의 공통 대가 — **네거티브가 작동하지 않는다**

> **CFG 가 1 이면 네거티브 프롬프트는 사실상 작동하지 않는다.**
> 고속 로라가 박혀 항상 낮은 CFG 로 쓰게 되는 모델에서는 **네거티브를 쓸 의미가 없고, 그만큼 품질도 다소 떨어진다.**
> 두 배포글이 각각 같은 말을 했다 — 한쪽은 *"굳이 쓴다면"* 이라며 목록을 남겼고,
> 다른 쪽은 *"네거티브를 쓸 수 없어 품질이 좀 떨어진다"* 고 인정하며 `textless version` 을 넣으면
> 조금 도움이 될지도 모른다고 덧붙였다.

이것이 [국룰](kukroul.md) 의 CFG 기본값이 이 계열에 통하지 않는 이유다.

### Persona Style noob v1.5 (2025-06) — 트리거는 그대로 `Persona`

```text
https://civitai.com/models/31771
긍정  masterpiece, best quality, amazing quality, very aesthetic, absurdres
```

v1.5 에서 **광원(빛 표현)을 개선하고 모델 자체의 개성을 줄여 아티스트 프롬프트와 LoRA 호환성을 높였다** —
콧구멍이 없는 그림체인데 모델이 구멍을 하나씩 찍어 넣던 문제도 이전 버전보다 줄었다.
트리거를 빼면 기본 그림체로도 쓸 수 있다.
`persona` 트리거의 원래 동작과 이 계열의 CFG 규칙은 위 "저스텝 증류(DMD)·CFG++ 모델" 을 보라.

*(2025-06)*


<small>근거 — [UncannyValley V-pred v1 출시 25.06](https://arca.live/b/aiart/140017939) · [Persona Style noob v1.5 출시 25.06](https://arca.live/b/aiart/139354250) · [여러가지 Comradeship 병합모델 3개 공유 25.06](https://arca.live/b/aiart/140944045)</small>

## 이 모델은 몇 픽셀까지 뽑히나 — 해상도 상한
<small>⚠️ 2025-03 기준 · 근거 5건</small>

"1536 으로 뽑으니 팔다리가 여러 개 나온다" 는 세팅 문제가 아니라 **모델이 감당하는 범위를 넘긴 것**이다.
이 값은 체크포인트마다 다르고, **병합모델일수록 원본보다 낮게 잡아야 한다.**

| 계열 | 안전한 상한 |
|---|---|
| **NoobAI-XL 계열** | **1280x1280** 까지 |
| **ILXL 1.X 공식 지원** | **1536x1536** (1.5K) |
| ComradeshipXL **v14K** | 1536x1536 특화 |
| ComradeshipXL **v14K1A / v14K1AX** (ILXL 1.1) | 권장 **1796x1796** · 최대 **2048x2048**. 가로세로 한쪽이 2048 을 넘어도 괜찮아 보인다는 관찰 |
| v14K1AX + 전용 Hi-res 세팅 | 권장 `1024x1024 x2.25` · 최대 `x2.5` (**이때 denoise 1.0**) |
| 병합모델에서 1536 이 이상하면 | **1408x1408 로 낮춘다** |

> **1280x1280 이하로 뽑거나 Hi-res 로 키우는 방식이라면** 고해상도 특화 ILXL 병합모델이 아니라
> **NoobAI-XL 기반 모델을 쓰는 편이 낫다.** 세 편의 ComradeshipXL 배포글이 모두 같은 안내를 붙였다.

### ILXL 1.X 의 고유한 약점 — 1.5K 이상에서 스케치가 된다

인체가 무너지는 것과는 다른 증상이다. **ILXL 1.X 계열은 1536 이상에서 그림이 스케치 스타일로 변해 버린다.**
v14K1AX 는 **2.5K 해상도로 직접 학습한 LoRA 를 병합해** 이 증상을 완화했다.

### 왜 병합하면 해상도가 줄어드는가

병합글 하나가 원리를 명확히 적어 뒀다.

> A 모델의 성격 100 과 B 모델의 성격 100 을 1:1 로 섞으면 **각각 50 씩 남는다**(아니메+실사 = 반실사).
> **1536x1536 출력 능력이 A 만의 성격이라면 병합 후 50% 로 줄어 그 해상도를 감당하지 못하게 된다.**

- **더하기(Add) 병합은 할수록 원본 성격을 잃는다**
- **블록 병합도 마찬가지다** — 성질이 여러 블록에 분산돼 있어 결국 같은 문제가 생긴다
- **추가 학습으로 만든 변종 모델**도 기존 학습 데이터를 담보로 하므로 고해상도 출력을 잃을 수 있다

### 고해상도 붕괴를 LoRA 로 막아 보려 한 실험

`1152x2016` 에서 팔다리가 여러 개 나오는 문제를 두고, **'ILXL 1.0 과 ILXL 0.1 의 차이값'** 을
LoRA 로 뽑아 NoobAI 에 얹는 실험이 있었다 *(step 40 · CFG 4.0 · `euler_ancestral` · `normal`)*.

| 대상 | 결과 |
|---|---|
| ilxl 0.1 순정 | 당연히 망가짐 |
| **ilxl 1.0 순정** | **매우 멀쩡함** |
| noob vpred 1.0 순정 | 의외로 살짝만 망가짐 |
| noob vpred 1.0 + **ilxl 차이값 LoRA 0.6** | vpred 계열 중 **가장 안정적** (원래 덜 망가져 체감은 작다) |
| noob eps 1.1 | 전형적인 고해상도 증상. 차이값 LoRA 0.6 을 얹어도 팔다리 문제가 남음 |
| **noob eps 1.1 + ilxl 1.0 을 50:50 단순병합** | **다른 방식보다 훨씬 나았다** |

결론 — **vpred 모델이면 차이값을 LoRA 로 만들어 얹고, eps 모델이면 병합이 쉽고 효과적이다.**
(이 실험에서 나온 병합 금기는 다음 절을 보라.)

ANIMA 쪽 해상도 임계점은 [ANIMA](anima.md) 에, 큰 그림을 만드는 방법 자체는
[업스케일과 화질](upscale.md) 에 따로 있다.

*(2025-02 ~ 2025-03)*

<small>근거 — [고해상도 생성용 ilxl 1.1 병합모델 Comradeshi… 25.03](https://arca.live/b/aiart/132177025) · [ilxl 1.0 병합모델 ComradeshipXL v14K … 25.02](https://arca.live/b/aiart/129171018) · [ILXL 1.0 병합모델 ComradeshipXL v14K3… 25.02](https://arca.live/b/aiart/129497774) · [고해상도 생성용 병합모델 ComradeshipXL v14K1… 25.03](https://arca.live/b/aiart/132553722)</small>

??? note "근거 5건 전부 보기"
    [고해상도 생성용 ilxl 1.1 병합모델 Comradeshi… 25.03](https://arca.live/b/aiart/132177025) · [ilxl 1.0 병합모델 ComradeshipXL v14K … 25.02](https://arca.live/b/aiart/129171018) · [ILXL 1.0 병합모델 ComradeshipXL v14K3… 25.02](https://arca.live/b/aiart/129497774) · [고해상도 생성용 병합모델 ComradeshipXL v14K1… 25.03](https://arca.live/b/aiart/132553722) · [(ILXL 1.0과 ILXL 0.1의 차이값 + noob모델… 25.02](https://arca.live/b/aiart/128849512)

## 병합의 금기 — eps 와 v-pred 는 섞이지 않는다
<small>⚠️ 2025-02 기준 · 근거 3건</small>

위의 "베이스 · 파인튜닝 · 병합" 항목이 *태생적 베이스가 같아야 한다* 는 규칙이라면, 여기는 그것을 만족해도 걸리는 함정이다.

### ⚠️ eps 모델과 v-prediction 모델은 섞으면 안 된다

같은 SDXL 계열이고 같은 NoobAI 계열이어도, **노이즈 예측 방식이 다르면 병합이 성립하지 않는다.**
실험 기록에 실패 사례가 그대로 남아 있다.

| 시도 | 결과 |
|---|---|
| noob **vpred** 1.0 + ilxl 1.0 **50:50 단순병합** | **아무것도 안 나온다** |
| 차이값을 '모델'로 만들어 clip 과 Model 의 **MergeAdd** 로 더하기 | **노이즈 덩어리만 나온다** (vpred·eps 양쪽 모두) |
| noob **eps** 1.1 + ilxl 1.0 50:50 단순병합 | 정상 동작하고 결과도 좋다 |

> **예측 방식(eps vs v-prediction)이 다른 체크포인트끼리는 그냥 섞으면 안 된다.**
> vpred 모델에 ILXL 1.0 을 섞으려면 **차이값을 LoRA 화해서 0.6 정도로 얹는다.**

### v-pred 모델을 쓸 때 알아 둘 두 가지

```text
기본 세팅   rescale 0.7  +  sampling v_prediction  +  zsnr true
```

**돌아가는 프로그램이 제한된다** — v-pred 모델은 **A1111 dev 브랜치 · reForge · ComfyUI 에서만** 돌아가고
**구버전 A1111 정식판에서는 못 쓴다.**

### 더하기(Add) 병합의 대가 — 실제 사례

ComradeshipXL v14K2 는 v14K 에 다른 모델의 차이분을 0.5 만큼 **'더한'** 모델인데,
**혼합이 아니라 더하기라서 뭉개짐과 색감 약화 부작용**이 생겼고 작성자 본인이 *"무리한 병합이었다"* 고 인정했다.
다음 판인 v14K3 는 **서브 모델을 noobai-XL EPS 1.1 로 바꾸고 가중치를 조정**해 이를 해결했다.

병합 비율식 자체와 태생적/파생적 베이스 구분은 위 "베이스 · 파인튜닝 · 병합" 항목에,
옛 SD1.5 시절의 블록 병합 표기법은 아래 "옛 SD1.5 자료를 읽을 때" 항목에 있다.

*(2025-02. 실패 사례는 원문 128849512 한 글의 실험이고, 더하기 병합의 부작용은 129171018 · 129497774 두 글이 뒷받침한다.)*

<small>근거 — [ILXL 1.0 병합모델 ComradeshipXL v14K3… 25.02](https://arca.live/b/aiart/129497774) · [ilxl 1.0 병합모델 ComradeshipXL v14K … 25.02](https://arca.live/b/aiart/129171018) · [(ILXL 1.0과 ILXL 0.1의 차이값 + noob모델… 25.02](https://arca.live/b/aiart/128849512)</small>

## Z-Image · Nanosaur · DreamLite — 대세 바깥의 로컬 모델
<small>2026-01 기준 · 근거 4건</small>

대세 모델 바깥에도 로컬에서 만져 볼 수 있는 것들이 있다. **전부 한 글씩만 있는 소개**라 참고로만 봐라.

### Z-Image — 파일을 어떻게 물리는지가 전부다

Z-Image 는 위 티어표의 2티어에 있는 모델인데, **ComfyUI 에 물리는 방식이 SDXL 과 달라서 대부분 여기서 막힌다.**

| 항목 | 어떻게 |
|---|---|
| 본체 | **확산 모델 로더** 로 로드 (`models/unet` 폴더). `Load Checkpoint` 가 아니다 |
| 텍스트 인코더 | **qwen 계열**을 따로 로드 |
| VAE | baked 가 안 먹어서 **`ae.safetensor` 를 따로 받아** 넣는다 |
| shift | **'모델 샘플링 (AuraFlow)' 노드로 3 정도** — 안 주면 제대로 나오지 않는다 |

```text
공식 문서   https://docs.comfy.org/tutorials/image/z-image/z-image-turbo
최초 배포처 https://comfyanonymous.github.io/ComfyUI_examples/z_image/
```

> **위 네 가지가 공식 문서에 전부 적혀 있다** *(댓글)*. 남의 워크플로우를 복붙하기 싫어 직접 빌드하다 헤맨 사례이므로,
> 새 모델을 만질 때는 공식 문서를 먼저 확인하는 편이 빠르다.

**다 합쳐 놓은 체크포인트 버전도 있지만 나눠 쓰는 편이 낫다** — qwen 텍스트 인코더를
여러 커스텀 모델이 공유할 수 있어 용량을 아낀다.

기존 워크플로우에 끼워 넣다 나온 오류 셋은 [ComfyUI 쓰는 법](comfyui.md) 쪽 이야기이지만 기록해 둔다 —
`ComfyUI-Easy-Use` 의 EasyLoader 에 qwen 인코더를 `Clip_override` 로 물리면 `KeyError: 'l'` 가 나고,
HiresFix 에 프롬프트 정보가 전달되지 않는 것은 **EasyLoader 단계에서 Clip 을 물리지 말고
먼저 pipe 를 만든 뒤 `pipe in` 노드로 Clip 정보를 추가**하면 해결된다.

### Z-Image 는 **태그도 알아듣는다** — 실측으로 확인됐다 *(2026-01)*

자연어 전용 모델처럼 보이지만 그렇지 않다.

> **Z-Image 는 학습 시 태그(단부루는 아님) / 짧은 캡션 / 긴 캡션 세 가지 방식으로 캡셔닝했다.** 그래서 태그가 먹힌다.
> 출처는 논문 `https://arxiv.org/pdf/2511.22699` 와
> `https://www.reddit.com/r/StableDiffusion/comments/1qolwcz/a_reminder_of_the_three_official_captioning/`.

실측에 쓴 도구는 VLM `Qwen3-VL-NSFW-Captioning-V4`(4.5 는 학습이 잘못됐는지 지시를 못 따라온다),
태거는 `wd-eva02-large-tagger-v3` 다.

```text
퀄리티 태그  best quality, highres, very aesthetic, muted color, clear outline, anime
기본 세팅    832x1216 / cfg 5.0→1.0 (scheduled 0-0.4) / euler_ancestral / simple
```

| 결론 | |
|---|---|
| 문장이 어려우면 | 기존처럼 **태그로 써도 된다** |
| 태그만 쓰면 | 더 단부루틱해지고 **왠지 더 벗으려 한다** — 태그에 `breasts` 가 들어가서인 듯 |
| 이해도 | **문장 프롬프트가 태그보다 높다** |
| **가장 원본에 가까운 것** | **태그와 캡션을 모두 넣은 경우** — VLM 이 놓친 부분을 wd14tagger 가 보완해 주기 때문으로 보인다 |

**한국어 프롬프트도 통한다.** 퀄리티 태그 뒤에 한국어 서술을 그대로 쓰고
`1girl, solo, white shoes, white hoodie, black shorts, skyscraper, from below, foreshortening,`
같은 태그를 함께 붙이면 더 그럴듯해진다는 예시가 실려 있다.

**양자화** — 여러 방식을 시도했지만 퀄리티가 불만족스럽거나 하드웨어 가속이 안 됐고,
**가속을 포기하고 VRAM 만 줄이려면 GGUF 가 가장 낫다.**
워크플로우는 첨부 이미지를 ComfyUI 에 끌어다 놓으면 뜨며 **webp 파일에도 워크플로우가 들어 있다**(댓글 4~6).

### 소형 모델 둘

| 모델 | 무엇인가 | 제약 |
|---|---|---|
| **Nanosaur-1.2B-Preview** | 개인이 **밑바닥부터** 만든 1.2B 이미지 모델. H100 1장으로 17일(256x256 6일 → 1024x1024, batch 16), VAE 는 DINOv3 기반 8시간, 텍스트 인코더는 `gemma3 270m`. 커스텀 ComfyUI 노드가 함께 제공되고 **`(character:2)` 처럼 높은 강조도 잘 동작**한다. 속도는 SDXL 급인데 크기 대비 결과가 좋다는 평 | ⚠️ **bf16 미지원 GPU(코랩 T4, RTX 20 시리즈 등)에서는 그냥 실패한다** |
| **DreamLite** | **0.39B** 크기의 온디바이스 통합 확산 모델. 생성과 **텍스트 지시 편집**을 한 네트워크에서 지원하고, 점진적 스텝 증류로 4스텝 추론을 달성해 iPhone 17 Pro(4비트 Qwen-VL + fp16 VAE·UNet)에서 1024x1024 를 **약 3초**에 처리 | 채널 반응은 *"0.39B 짜리 편집 모델은 귀한 편"* |

```text
https://huggingface.co/well9472/Nanosaur-1.2B-Preview/tree/main
https://github.com/ByteVisionLab/DreamLite   ·   https://carlofkl.github.io/dreamlite/
```

> DreamLite 소개글의 본문은 **Gemini 번역본**이다. 위 "모델 소식을 읽는 법" 의 체크리스트를 적용해 읽어라.

*(2026-01 ~ 2026-05. 셋 다 한 글에서만 언급됐다.)*

<small>근거 — [Z Image 는 태그도 인식함 26.01](https://arca.live/b/aiart/160874039) · [Nanosaur-1.2B-Preview 26.04](https://arca.live/b/aiart/166944946) · [와씨 쓰던 워크플로우 개조해서 Z-Image 모델용으로 개조… 26.01](https://arca.live/b/aiart/160774868) · [핸드폰에서도 3초만에 이미지 편집을? 0.39B 크기를 자랑… 26.05](https://arca.live/b/aiart/171398852)</small>

## 13-b. Lumina · Chroma — SDXL 바깥의 DiT 계열
<small>⚠️ 2025-07 기준 · 근거 6건</small>

지금까지의 모델은 전부 SDXL 계열이었다. **여기서부터는 아예 다른 물건**이라 파일 구성도 프롬프트 문법도 바뀐다.
채널에서는 `hanzogak` 의 **Comradeship LU(Lumina) / CR(Chroma)** 시리즈로 접하게 된다.

### 두 계열의 체급이 정반대다

| | **Lumina 계열** (Comradeship **LU**) | **Chroma 계열** (Comradeship **CR**) |
|---|---|---|
| 뿌리 | Lumina-Image-2.0 → Neta Lumina | FLUX.1-schnell → Chroma v40 |
| 구성 | **2.6B DiT + 2B `gemma-2-2b` TE + FLUX.1 의 16채널 VAE** | **8.9B DiT + 4.7B T5-XXL TE + 16채널 VAE** |
| 성격 | 소형. *"가난한 자의 NAI4"* | 대형. 깡성능은 **NAI4 이상** |
| 작가 태그 | 된다 (`@` 접두사) | **전혀 안 먹힌다** |
| 아니메 캐릭터 | 되는 편 | 동양 아니메 지식이 얕아 **블루 아카이브 정도의 인기 캐릭터만 겨우** |
| 자연어 | 된다 | **자연어는 이쪽을 권장** |

> **병합자 본인의 판단(댓글 5)** — *"루미나는 잘해 봐야 NAI4 대체품인 반면,
> 크로마는 대형 DiT 의 깡성능이 있어 대체 불가능한 영역"* 이다.
> 다만 **두 계열 모두 FLUX 기반이라 일반 사용자 하드웨어로는 구동이 아슬아슬하다**는 지적이 붙었다(댓글 11~12).

### ⚠️ Chroma 의 하드웨어 조건

> **Chroma 는 FP8 모드에서 성능 저하가 있으므로 VRAM 24GB 이상이 아니면 `Q8 GGUF` 버전을 써라.**

```text
Q8 GGUF (DiT만)  https://huggingface.co/hanzogak/comradeshipCR/blob/main/comradeshipCR-v1T14-40KM-Q8_0.gguf
FP16             https://huggingface.co/hanzogak/comradeshipCR/blob/main/comradeshipCR-v1T14-40KM.safetensors
샘플             ComfyUI / euler / beta / CFG 6.0 / 30스텝 / 864x1152
권장 프롬        best quality, aesthetic, highres, high quality, newest animated illustrations.
```

양자화 표기 자체는 위 "양자화 파일 고르기" 를 보라.

### Lumina 계열은 **프롬프트 문법부터 다르다**

텍스트 인코더에 **소형 언어모델(gemma-2-2b)을 그대로** 넣었기 때문에, 프롬프트를 **언어모델 지시문으로 시작**해야 한다.

```text
긍정   You are an assistant designed to generate anime images based on textual prompts. <Prompt Start>
       … 내용 … , masterpiece, best quality, very aesthetic, absurdres, amazing quality, beautiful color,
네거   You are an assistant designed to generate low-quality images with lowest degree of aesthetics
       based on user prompts. <Prompt Start> …
```

| 규칙 | 내용 |
|---|---|
| **작가명** | 앞에 **`@`** 를 붙인다 — `as109` → **`@as109`** |
| **캐릭터** | 작품명을 함께 넣는 게 좋다 — `mifune shioriko, love live!, love live! nijigasaki high school idol club` |
| **언어** | 다국어 지원. 중국어·일본어가 되고 **한국어도 어느 정도** 된다(영어만큼은 아니다) |
| **길이** | 입력 토큰이 **8192** 로 추정될 만큼 넉넉해 길게 써도 된다 |
| **네거티브의 외국어** | 권장 네거티브에 `难看, 醜い, 不細工, 格好悪い, 못생기다, 추하다, 볼품없다, Уродливый` 처럼 여러 언어의 '못생김' 이 나열돼 있는데 **오타가 아니라 다국어 TE 라서 의도된 것**이다 |

> **gemma 검열은 상관없다** — 구글 AI 스튜디오에서 gemma 2b 에 NSFW 를 넣으면 거부하는데 이 모델은 왜 검열이
> 없느냐는 질문이 나왔다. 답은 **gemma 2b 가 여기서는 텍스트 인코딩에만 쓰이고 추론·답변을 하는 게 아니므로
> 언어모델의 검열과는 상관이 없다**는 것이다(댓글 11~13).

### ⚠️ 실행 환경과 알려진 증상

> **Comradeship LU v2 계열은 reForge·Forge 에서 안 되고 ComfyUI 에서만 돌아간다**(원글쓴이 확인, 댓글 5~6).
> Neta Lumina 를 WebUI 로 돌리는 것이 구조적으로 불가능하지는 않으나 **직접 구현해야 해서 쉽지 않다.**
>
> 그리고 **소형인데도 생성이 생각보다 느리고, 일부 FP16 환경에서 그림이 새까맣게만 나올 수 있다.**
> (FP16 검은 화면과 RTX 2000번대의 관계를 물은 댓글에는 답이 달리지 않았다 — 직접 돌려 봐야 안다.)

### 판별 — **권장 설정이 버전마다 다르다**

| 판 | 무엇이 다른가 | 샘플러 / 스케줄러 / CFG / 스텝 |
|---|---|---|
| **LU v1T2** (2025-04) | `Illustrious-Lumina-v0.03 + ((LeX-Lumina − Lumina-Image-2.0) × 0.6)`. Lumina 는 인프라가 덜 갖춰져 복잡한 병합이 불가능해 식이 단순하다 | `Euler` / `Simple` / **CFG 7** / **shift 6** / 25 |
| **LU v2T6 · v2T12 · v2T14** | v2T12 는 퀄리티 로라 **6개**를 직접 만들어 병합해 aesthetic 성격으로 개조, v2T14 는 그것을 **9개**로 늘렸다 | `res_multistep` / `linear_quadratic` / **CFG 5.5** / 20~29 |
| **LU v2T22** (2025-07) | 베이스를 **Neta Lumina 1.0** 으로 교체해 지식이 늘었고 로라 병합식을 재조정 | **`euler_ancestral` / `simple` / CFG 4~6 / 20~30** |
| **LU v2T25** (2025-07) | Neta Lumina **Experimental 2종 + Karcher-merge**. **추가 aesthetic 튜닝을 하지 않아 base 에 가깝다** | 위와 같음 (샘플 CFG 5.5 / 28스텝) |

```text
v1T2   https://huggingface.co/hanzogak/comradeshipLU/blob/main/comradeshipLU-v1T2.safetensors
v2 계열 https://huggingface.co/hanzogak/comradeshipLUv2/          (v2T6 / v2T12 / v2T14 / v2T22 / v2T25)
```

> **버전을 바꾸면 설정도 같이 바꿔야 한다.** v2T12·v2T14 의 값을 v2T22 에 그대로 쓰면 안 된다.

`Illustrious-Lumina-v0.03`(`https://huggingface.co/OnomaAIResearch/Illustrious-Lumina-v0.03`)은
Illustrious 측이 Lumina-Image-2.0 을 테스트 목적으로 **DiT 만 파인튜닝한** 아니메 모델이고,
**TE 는 튜닝하지 않아 베이스의 기본 TE 를 그대로 쓴다.**

### ⚠️ 한계 — 병합자 본인이 낮춰 둔 기대치

> **Neta Lumina 베이스는 손가락·발가락 타율이 나쁘다.** v2T22 는 부작용을 감수하고 로라를 여러 번 병합해
> 쓸 수 있게 만든 것이며, **극한으로 튜닝된 아니메 SDXL 모델보다는 밀릴 수 있다**고 솔직히 밝혔다.
>
> 공개된 Neta Lumina 모델들의 **지식 폭이 예상보다 깊지 않아, 대규모 추가 학습이 없다면
> 당분간 '가난한 자의 NAI4' 에 머무를 가능성이 높다.**

**이 계열로 로라를 학습하는 제대로 된 가이드는 아직 없다.**
`https://huggingface.co/hanzogak/comradeshipLUv2/tree/main/assy-animeLU-LoRA` 의 파일들을 읽어 보라는 것이
병합자의 안내다(v2T22 댓글 1~2).

*(2025-04 ~ 2025-07)*


<small>근거 — [Neta-Lumina 기반 병합모델 Comradeship L… 25.07](https://arca.live/b/aiart/141311244) · [Neta Lumina 1.0 기반 병합모델 Comradesh… 25.07](https://arca.live/b/aiart/143116958) · [Illustrious-Lumina-v0.03 병합모델 Com… 25.04](https://arca.live/b/aiart/134430978) · [Neta-Lumina 기반 병합모델 Comradeship L… 25.07](https://arca.live/b/aiart/141472508)</small>

??? note "근거 6건 전부 보기"
    [Neta-Lumina 기반 병합모델 Comradeship L… 25.07](https://arca.live/b/aiart/141311244) · [Neta Lumina 1.0 기반 병합모델 Comradesh… 25.07](https://arca.live/b/aiart/143116958) · [Illustrious-Lumina-v0.03 병합모델 Com… 25.04](https://arca.live/b/aiart/134430978) · [Neta-Lumina 기반 병합모델 Comradeship L… 25.07](https://arca.live/b/aiart/141472508) · [Neta Lumina 기반 병합모델 Comradeship L… 25.07](https://arca.live/b/aiart/143596900) · [여러가지 Comradeship 병합모델 3개 공유 25.06](https://arca.live/b/aiart/140944045)

## 양자화 파일 고르기 — fp16 / fp8 / GGUF / int8convrot
<small>2026-08 기준 · 근거 5건</small>

같은 모델도 파일이 여러 개다. 이름 뒤에 붙는 것이 **양자화 방식**이고, 용량·속도·품질이 여기서 갈린다.

| 형식 | 원리 | 품질 | 속도 |
|---|---|---|---|
| BF16 / FP16 | 원본 | 기준 | RTX4000 시리즈 이상은 이게 가장 빠른 경우가 많음 |
| **fp8 tensorwise** (ComfyUI 기본 fp8) | 원본을 -448~448 범위 FP8 로 표현, **레이어 전체에 FP32 스케일 하나** | 아래 것들보다 열위 | FP8 행렬곱 지원 GPU 에서 이론상 2배, 실제 1.5~1.8배 |
| **GGUF Q8_0** | **32×32 블록마다 스케일**(blockwise) | fp8 tensorwise 보다 우위 | — |
| int8rowwise | 2D 값에 1D 스케일 | fp8 수준까지 올라옴 | 속도 저하 적음 |
| **int8convrot** | int8rowwise + **아다마르 변환(quarot 계열)** 으로 INT8 의 이상치 취약점 보완 | **Q8_0 급** | fp8 보다 조금 빠름 (변환 시간 때문에 int8rowwise 보다는 조금 느림) |
| w4a8 | 4비트 | nvfp4 이상 (Kijai 준비 중) | int8convrot 대비 10% 느림 |
| Nunchaku 4bit | — | **캘리브레이션이 필요**해 Wan 2.1/2.2 는 양자화 시 품질이 무너짐 | 빠름 |

**결론은 int8convrot 쪽이다.** ComfyUI **v0.27.0 부터 convrot 을 공식 지원**하면서
Comfy-Org 의 Ideogram-4, Bernini, Krea-2 등에 int8convrot 판이 올라왔다.
병합·추가학습 모델이 많은 이 바닥에서는 **캘리브레이션이 필요 없는 쪽이 대세가 될 것**이라는 것이 근거다.
INT8 행렬곱은 RTX 2000 시리즈·AMD·인텔 GPU 에서도 지원된다(구현 필요)는 것도 이점이다.

실측 — MiniMax H3 의 Video VAE 를 int8convrot 으로 바꾸자 RTX5090 400W 기준
**1MPixel 디코드 16.65초 → 11.85초**, 0.4MPixel 은 5.83초 → 3.31초로 줄었고
blend image 노드로 diff 를 떠봐도 결과물 차이가 없었다. 단, **검은 화면 보고**가 있으므로
ComfyUI 최신 + torch `+cu130` 이후 + comfy-aimdo 최신 + comfy-kitchen 최신 조건을 맞춰야 한다
(그래도 발생했다는 미해결 사례가 댓글에 남아 있다).

**양자화판이 없는 튜닝 모델은 직접 만들 수 있다.**
공식 툴 `https://github.com/Comfy-Org/comfy-model-tools` 를 쓰며,
`--verify-report` 옵션으로 input 대비 output delta 를 받아볼 수 있다.
아무 옵션 없이 양자화해도 상대 오차 2% 미만, 코사인 유사도 최저 0.999936 이 나온다.

**GGUF 로 ANIMA 를 쓸 때의 함정** — `anina_fp16_patch_gguf.py` 를 `custom_nodes` 에 둔 채
양자화하지 않은 **원본** 모델을 쓰면 KSampler 시작과 동시에
`mat1 and mat2 must have the same dtype, but got Float and BFloat16` 가 난다.
파일을 폴더 밖으로 빼거나 삭제해야 한다. 대안으로 실행 옵션 `--fast fp16_accumulation fp8_matrix_mult` 또는
모델 뒤에 `ModelComputeDtype` 노드를 두고 fp16 을 지정하는 방법이 있다.

<small>근거 — [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [Anima GGUF 양자화 모델 26.02](https://arca.live/b/aiart/161385741) · [ComfyOrg 공식모델들에 int8convrot 추가됨 26.07](https://arca.live/b/aiart/175519662)</small>

??? note "근거 5건 전부 보기"
    [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [Anima GGUF 양자화 모델 26.02](https://arca.live/b/aiart/161385741) · [ComfyOrg 공식모델들에 int8convrot 추가됨 26.07](https://arca.live/b/aiart/175519662) · [(anima) 원본+int8 convrot 모델 3종 비교 26.07](https://arca.live/b/aiart/177372687)

## 웹 서비스끼리의 선택 — 용도가 갈린다
<small>2026-08 기준 · 근거 5건</small>

로컬을 안 쓰거나 병행할 때의 이야기다. 모두 **한 글씩만 있는 비교**라 참고로만 봐라.

**그록 vs 시댄스 2.0** (2026-06 기준, 동일 재료컷 + 동일 한국어 프롬프트)

> 결론은 **떡씬(NSFW)은 그록, 그 외 연출은 시댄스 2.0**.
> 시댄스는 '여자 뒷춤에서 검을 뽑아' 의 주체를 장군으로 오인했지만 자동 생성된 **배경음·액션·캐릭터 일관성이 훌륭**했고
> 화질이 좋아 채널 용량 제한을 넘길 정도였다.
> 그록은 10개를 뽑아도 장군 외형이 거의 동일하고 **얼굴 일관성이 유지되지 않으며 배경음이 어색**했다.

⚠️ **다만 그록 영상 서비스는 이후 종료됐다**(통합팩 배포글의 후기). 위 비교는 기록으로만 유효하다.

**Gemini Omni Flash vs MiniMax H3 (API 가격, 2026-08-01)**

| | Gemini Omni Flash | MiniMax H3 |
|---|---|---|
| 출력 1초당 | **$0.1** | **$0.13** |
| 10초 영상 | $1.0 | $1.3 |
| 해상도 기준 | 720×1280 (HD) | 1440×2560 (QHD) |

가격 차는 크지 않은데 해상도 기준이 다르므로, **저해상도 옵션이 생기면 오히려 H3 가 더 쌀 수 있다**는 것이 작성자 판단이다.
체감 평은 갈린다 — 옴니는 안정적이지만 밋밋하고 H3 는 카메라워킹·연출 이해가 낫다는 의견과,
옴니가 더 부드럽고 앵글·구도가 낫다는 반대 의견이 함께 있다.

**Gemini Omni** 자체는 이미지·오디오·비디오·텍스트를 조합해 입력받고 **대화형으로 누적 편집**
(캐릭터·물리·장면 기억 유지)이 되는 것이 특징이며, 모든 출력에 SynthID 워터마크가 들어간다.
댓글에서는 SeedDream-2.0 에는 못 미친다는 의견과, **동영상 생성 한도에 도달하면 언어모델로서의
제미나이 프로까지 잠긴다**는 실사용 주의가 나왔다.

<small>근거 — [그록 빌드 검열없을때 퍼먹으시오 26.06](https://arca.live/b/aiart/172435010) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [ChatGPT Images 2.0을 소개합니다! 26.04](https://arca.live/b/aiart/168399124) · [그록과 시댄스2.0 영상 비교 26.06](https://arca.live/b/aiart/172854969)</small>

??? note "근거 5건 전부 보기"
    [그록 빌드 검열없을때 퍼먹으시오 26.06](https://arca.live/b/aiart/172435010) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [ChatGPT Images 2.0을 소개합니다! 26.04](https://arca.live/b/aiart/168399124) · [그록과 시댄스2.0 영상 비교 26.06](https://arca.live/b/aiart/172854969) · [Gemini Omni Flash vs Minimax-H3 26.08](https://arca.live/b/aiart/178630221)

## ⚠️ 모델 소식을 읽는 법 — 절반은 아직 검증되지 않았다
<small>2026-07 기준 · 근거 6건 · 자료 엇갈림</small>

다섯 편 이상의 글에서 반복 확인된다. **채널에 올라오는 신규 모델 소식의 상당수는
제작사 주장·유출 정보·LLM 요약이라 실사용 검증이 없다.** 실제 사례:

| 사례 | 무엇이 문제였나 |
|---|---|
| Veo 3.2 유출 (2026-02) | 공식 발표가 아니라 **유출 정보**를 Gemini 3 Pro 가 외부 블로그 3건(supermaker.ai / glbgpt.com / netcontentseo.net)을 참고해 정리한 글 |
| Helios (2026-03) | 1분 영상·WAN2.2 급 품질이 **전부 제작사 '주장'**. 작성자가 이를 반복 표시했고 실사용 검증은 본문에도 댓글에도 없음 |
| HappyHorse (2026-04) | 오픈소스 예정 정보가 **철회**되고 제목이 '(오픈소스 아님 확정)' 으로 바뀜. 사이트·트위터 게시물 삭제 |
| Happy Horse 1.0 (2026-04) | 본문 대부분이 **제미나이 요약본**. 작성자가 오류 부분을 직접 표시 |
| MiniMax H3 (2026-07) | "**미니맥스는 벤치맥싱이 심하니 걸러서 볼 것**" 이라는 경계가 댓글에 붙음 |

**읽을 때의 체크리스트 — 아래 넷 중 하나라도 걸리면 판단을 보류하라.**

1. **가중치 링크가 있는가.** 허깅페이스/ModelScope 주소 없이 "곧 공개 예정" 이면 로컬에서 못 쓴다
2. **글에 실사용 결과물이 있는가.** 공식 샘플 영상만 있으면 제작사 주장이다
3. **본문이 LLM 요약본인가.** "제미나이 3.1 Pro 로 번역/요약" 같은 표기가 있으면 세부 수치를 그대로 믿지 마라
4. **댓글을 끝까지 읽었는가.** 본문 정보가 댓글에서 정정되는 일이 매우 잦다
   (예: MiniMaxH3 Cache 는 매니저가 아니라 git 설치, HappyHorse 는 페이크 논란)

가중치가 공개된 모델 소식이라도 **ComfyUI PR 이 머지됐는지**를 함께 확인하는 것이 안전하다.
Bernini·lingbot 처럼 PR 만 올라온 상태인 경우가 있다.

### 검증 수단 하나 — 모델 유사도 비교(속칭 '친자검사')

*"이 모델은 밑바닥부터 학습했다"*, *"NAI 기반이 아니다"* 같은 **배포자의 주장은 실제로 검증할 수 있다.**
2023-04 의 HD-22 소개글이 그 전형이다.

| | 내용 |
|---|---|
| **본문의 최초 주장** | HD-22 는 *"NAI 병합 기반이 아닌 몇 안 되는 모델"* |
| **댓글의 검증** | base 를 `animefull-final-pruned.safetensors`(2022년 유출된 NovelAI 모델)로 놓고 유사도를 재니 `HD-22.ckpt` 가 **95.63%** |
| **결론** | **본문이 틀렸다.** 밑바닥부터 학습한 것이 아니라 NAI 를 파인튜닝한 것이며, 학습 비용 후원을 받고 그렇게 했다는 비판이 이어졌다. **원글쓴이도 본문을 정정했다** |

```text
친자검사(모델 유사도 비교) 방법   https://arca.live/b/aiart/68239023
```

> 여기서 남는 것은 HD-22 라는 모델이 아니라 **주장을 수치로 반증할 수 있다**는 사실과 그 방법이다.
> 2023년 무렵 국내외 애니 계열 모델 대부분이 유출 NAI 를 조상으로 두고 있어, *"NAI 기반이 아니다"* 는
> 당시 흔한 홍보 문구였다.


<small>근거 — [1분 넘는 영상을 고속으로 뽑는 Helios 모델 출시 26.03](https://arca.live/b/aiart/163968817) · [알리바바에서 딸내미 하나 샀음 (happy horse 1.0… 26.04](https://arca.live/b/aiart/169030124) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [(오픈소스 아님 확정) 새로운 SOTA급 T2V/I2V 모델… 26.04](https://arca.live/b/aiart/167106042)</small>

??? note "근거 6건 전부 보기"
    [1분 넘는 영상을 고속으로 뽑는 Helios 모델 출시 26.03](https://arca.live/b/aiart/163968817) · [알리바바에서 딸내미 하나 샀음 (happy horse 1.0… 26.04](https://arca.live/b/aiart/169030124) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [(오픈소스 아님 확정) 새로운 SOTA급 T2V/I2V 모델… 26.04](https://arca.live/b/aiart/167106042) · [HD-22 23.04](https://arca.live/b/aiart/74124808) · [Google의 Veo 3.2 유출 26.02](https://arca.live/b/aiart/163312367)

## 16-b. 공식 소개글을 뜯어 읽는 법 — Illustrious XL 3.6 사례
<small>⚠️ 2025-07 기준 · 근거 1건</small>

위 항목이 *"검증되지 않은 소식을 걸러라"* 라면, 여기는 **검증된 공식 발표문을 어떻게 읽는가**의 실례다.
Illustrious XL 3.6 공식 소개글을 한 줄씩 뜯은 분석(2025-07)이며 **한 글에서만 다뤄졌지만** 방법 자체가 값이 있다.

```text
원문  https://www.illustrious-xl.ai/updates/29    ·    https://www.illustrious-xl.ai/blog/16
```

| 홍보 문구 | 어떻게 읽었나 |
|---|---|
| "최신 고해상도 데이터셋으로 훈련" | 넓은 **Full** 인지 좁은 **Curated** 인지에 따라 뜻이 다르다. '인기 인터넷 문화 재현 가능' 이라는 표현으로 보아 Full 에 준하는 것으로 **추정** |
| "푸리에 특징 손실로 고주파 타겟팅, 흐릿함 방지" | 쉽게 말해 **포토샵 샤프니스 필터를 거는 느낌**이다 |
| "감소된 zTSNR 과대평가" | V-pred 와 ZeroSNR 은 색이 진해지는 현상이 있고 원래 CFG 리스케일로 해결했는데, 이제 그것 없이도 해결했다는 주장으로 보인다 |
| "적응형 드롭아웃으로 캐릭터 제어 향상" | 드롭아웃은 일부를 일부러 날려 학습을 새롭게 유도하는 기법. **이론적 서술이라 직접 써 봐야 안다** |
| "요가 포즈 등 바디 컨트롤 발전" | 자연어 처리 향상이라기보다 **특이 포즈를 집중 학습한 결과**로 보이며, 마이너 아니메 지식이 대신 빠졌을 가능성이 있는 트레이드오프. 샘플의 `Butterfly sitting pose` 에 실제 나비가 나타나는 데서 **CLIP 의 한계**가 드러난다 |

### ⚠️ 가장 날카로운 지적 — 예시 프롬프트에 **눈 색상이 빠져 있다**

'두 인물 구도 성능 향상' 의 공식 예시는 *'왼쪽은 갈색 단발, 오른쪽은 빨간 포니테일'* 이다.

> **잘 보면 눈 색상 지정이 빠져 있다.** 즉 실사용 성능이 아니라 **기술 시연 성격**이다.
>
> 원글쓴이가 직접 병합한 ComradeshipXL v14VW3 로 같은 프롬프트를 돌리면 약 **1/3 확률**로 준수하는데,
> **눈 색상을 추가해 변수가 하나 늘면 사실상 프롬프트를 못 따라간다.**

**공식 예시 프롬프트에서 무엇이 빠졌는지를 보라** — 이것이 이 글이 남긴 가장 재사용 가능한 읽기 방법이다.

### 함께 정리된 것

| | 내용 |
|---|---|
| **4채널 VAE 의 물리적 한계** | SDXL 계열의 4채널 VAE 는 **고주파(선명함)를 담기에 물리적 한계**가 있어, 이미 저해상도로 압축된 이미지를 선명하게 튜닝한다고 해결될 문제인지는 **미지수**다 |
| **라이선스** | ILXL 은 **SDXL 기반이라 SDXL 의 Open RAIL++-M 라이선스를 벗어날 수 없고**, 어그로를 끌면 라이선스로 조치가 들어올 수 있다 (댓글 6, 참고 `https://arca.live/b/aiart/142159932`) |
| **자연어 능력** | **ILXL 1/2 의 자연어 인식 능력은 NoobAI V-pred 보다 한 수 아래**라는 평가 (댓글 19). 아니메 분야는 **태그 입력이 기본이고 자연어는 보조**다 |
| **차세대 유망주** | Neta Lumina 와 Chroma 가 꼽혔다 — 위 "Lumina · Chroma" 항목 |

총평은 **기술적 개선은 맞지만 실사용 개선보다는 투자자에게 잘 보이려는 성격이 강해 보인다**는 것이다.

*(2025-07. 한 글에서만 언급된 분석이다.)*


<small>근거 — [Illustrious XL 3.6 소개글에 대해서 분석해보는… 25.07](https://arca.live/b/aiart/142556834)</small>

## 옛 SD1.5 자료를 읽을 때 — 계보 · VAE · 병합
<small>2026-05 기준 · 근거 11건</small>

채널에는 2022~2023년 SD1.5 시절 모델 자료가 많이 남아 있다. **지금 그대로 쓸 것과 배경 지식으로만 볼 것을 갈라 둔다.**

**(1) 모델 계보 — 옛 이름의 출처를 확인할 때만**
2023-01 시점 국내 채널에서 쓰이던 애니메 체크포인트는 **대다수가 Anything v3 의 병합 파생**이었다.
12종을 같은 프롬프트·시드로 비교한 카탈로그(`https://arca.live/b/aiart/68725324`)가 그 계보를 남겼다 —
7th Layer, a+f-s, AbyssOrangeMix2, Anything v4.5, BlossomMix, Counterfeit v2.0, DefMix, NO133_104,
treebark, ProjectTurn8 luna, ultracolor, YuzuLemonTea.
지금은 Illustrious/NoobAI/ANIMA 로 세대가 완전히 바뀌었으므로 **실용 목적으로 받을 이유는 없다.**

**(2) VAE — 개념은 그대로, 파일은 낡았다**
VAE 는 모델에 탈부착하는 애드온으로 색감·선명도를 마무리하며 단독으로는 작동하지 않는다.
**VAE 는 체크포인트와 달리 `models/Stable-diffusion` 이 아니라 별도의 VAE 폴더에 넣는다.**

```
# SD1.5 시절 표준 (지금 Illustrious·ANIMA 계열에는 그대로 쓰지 않는다)
애니메 : kl-f8-anime2          https://huggingface.co/Kaeya/aichan_blend/tree/main/vae
실사   : vae-ft-mse-840000-ema-pruned
        https://huggingface.co/stabilityai/sd-vae-ft-mse-original
```

요즘은 대부분의 체크포인트에 VAE 가 내장(baked)돼 있어 따로 안 넣어도 되지만,
**병합 모델 중에는 VAE 를 안 넣은 것이 있다** — 예를 들어 개인 병합 모델 JINMODEL_v7.5 는
"별도 VAE 를 연결해야 색이 정상으로 나온다"고 명시한다(권장값 1024x1024 / 832x1216 / 1024x1360,
`Euler a` + `karras`, CFG 5~7, Step 30~40, Forge 기준). 색이 물 빠진 듯하면 VAE 부터 의심한다.
**왜 VAE 가 빠져 있는지는 이 문서의 "⚠️ 병합의 함정 — 병합하면 내장 VAE 가 소실된다" 항목에 있다.**

**(3) 병합 — 블록별로 섞는다는 발상**
WebUI 자체 병합 기능은 모델 전체에 **단일 비율만** 적용할 수 있다.
U-Net 의 계층(블록)별로 세부 조절하려면 Merge Block Weighted 확장을 쓴다.

```
https://github.com/bbc-mc/sdweb-merge-block-weighted-gui
```

**옛 글의 병합 표기법도 읽을 줄 알아야 한다.** 2022~2023년 병합 비교글은 이렇게 적었다.

```text
모델A + 모델B - 모델C - M계수      =  Add difference :  A + (1-M) * (B-C)
예) Anything+f222-SD1.4-M0.3
```

> 병합을 **한두 번만 할 거면 M 이 커도 되지만, 계속 이어 붙이는 식으로 병합할 때는 M 을 점점 줄여 나가야 한다**
> (댓글 보충, 2022-12). 당시 유명 병합인 berrymix·blossommix 는 모두 M=1 을 썼다.

블록별로 나누는 이유가 핵심이다 — **U-Net 앞쪽(입력) 블록은 구도·형태에, 뒤쪽(출력) 블록은 화풍·디테일에 주로 관여**해서
"구도는 A 모델, 그림체는 B 모델" 같은 조합이 가능하기 때문이다. 이 발상은 지금의 LoRA Block Weight 로 이어진다
([자원](resources.md) 의 로라 관리 항목).

**(4) 2023년 봄 배포글의 공통 규격 — 옛 글을 읽을 때의 기준선**

2023년 봄 채널의 SD1.5·A1111 병합모델 배포글(ExpMix_Extra · ZemiHR · ZemiHR_V2 등)은 **권장값이 거의 같다.**
옛 글에서 이 값들을 보면 *"이 시절 기본값"* 이라고 읽으면 된다.

| 항목 | 당시 값 |
|---|---|
| 샘플러 | `DPM++ SDE Karras` 또는 `DPM++ 2M Karras` |
| Clip skip | **2** (ExpMix 는 1~2) |
| CFG Scale | **7~10** |
| Hires steps | **13** |
| Hires 업스케일러 | `R-ESRGAN 4x+Anime6B` 또는 `R-ESRGAN General WDN 4xV3` |

```text
긍정   (masterpiece:1.2), best quality
부정   (worst quality, low quality:1.4), EasyNegative, badhandv4
       ↑ EasyNegative 와 badhandv4 는 프롬프트가 아니라 Textual Inversion 임베딩이라
         따로 받아 embeddings 폴더에 넣어야 동작한다
```

그리고 이 시절 병합은 **체크포인트에 LoRA 를 직접 구워 넣는(merge) 방식**이었고,
배포글이 병합 순서와 비율을 그대로 공개하는 관행이 있었다(supermerger 같은 확장으로 했다).
지금의 "채널 자작 병합 체크포인트" 배포글이 레시피를 공개하는 문화가 여기서 이어진 것이다.

> **얼굴 블록만 바꾸는 요령**도 이때 나왔다 — 병합 시 **얼굴에 해당하는 U-Net 블록만 2D 모델로 교체**하면
> 배경과 질감을 살린 채 **손 타율이 올라간다**(henmix_2.5D 배포글 댓글).

> 위 넷 모두 **SD1.5 기준 자료**다. 원리(VAE 의 역할, 블록별 기여, 병합의 뜻, 블록별 성격)는 지금도 통하지만
> **모델 이름·파일·수치는 그대로 쓰지 마라.** 지금 세대의 권장값은 이 문서의 "채널 자작 병합 체크포인트" 항목에 있다.

<small>근거 — [모델공유) 반실사 병합모델 ZemiHR 23.04](https://arca.live/b/aiart/74030139) · [모델공유) ExpMix_Extra 23.04](https://arca.live/b/aiart/73792400) · [코랩 AI그림 실전압축 레퍼런스 23.03](https://arca.live/b/aiart/72672264) · [Anything + Stable Diffusion + f22… 22.12](https://arca.live/b/aiart/64965428)</small>

??? note "근거 11건 전부 보기"
    [모델공유) 반실사 병합모델 ZemiHR 23.04](https://arca.live/b/aiart/74030139) · [모델공유) ExpMix_Extra 23.04](https://arca.live/b/aiart/73792400) · [코랩 AI그림 실전압축 레퍼런스 23.03](https://arca.live/b/aiart/72672264) · [Anything + Stable Diffusion + f22… 22.12](https://arca.live/b/aiart/64965428) · [#개인 병합 모델 공유 - JINMODEL_v7.5 26.05](https://arca.live/b/aiart/170224006) · [그래서 vae는 뭐 쓰면 돼요? 23.01](https://arca.live/b/aiart/68299849) · [henmix_2.5d v2 업데이트 23.04](https://arca.live/b/aiart/75260114) · [ZemiHR_V2 모델 업데이트 23.04](https://arca.live/b/aiart/75017141) · [체크포인트 카탈로그(12개 모델 비교) 23.01](https://arca.live/b/aiart/68725324) · [VAE별 이미지 차이 22.11](https://arca.live/b/aiart/62060325) · [병합하는 방법은 공지 없음?? 23.02](https://arca.live/b/aiart/70241791)

## 이미지 편집 모델 — Qwen-Image-Edit 와 그 파인튜닝판
<small>2026-02 기준 · 근거 1건</small>

그림을 새로 그리는 것이 아니라 **기존 이미지에 '왼팔에 용 문신을 새겨라' 같은 지시를 줘서 고치는** 모델이다.
위 티어표의 2티어 `Qwen-Image-Edit-2511` 이 이 갈래이고, 그 파인튜닝판이 하나 더 있다 (**한 글에서만 언급됨**, 2026-02).

```text
# FireRed-Image-Edit-1.0 — Qwen-Image-Edit-2511 을 SFT + DPO 로 미세조정한 것
https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0
https://huggingface.co/cocorang/FireRed-Image-Edit-1.0-FP8_And_BF16    # BF16 / FP8 / FP8_comfy 변환판
```

구조를 갈아엎지 않고 **미세조정만 했는데도** 벤치마크에서 원본 Qwen-Image-Edit-2511 을 모든 영역에서 상회하고
Nano-Banana-Pro 까지 상회했다는 것이 원문의 주장이다. 작성자 본인도 처음에는 아키텍처가 같아 차이를 못 느꼈고,
**전역적인 프롬프트가 아니라 세부적인 프롬프트로 들어가니** 품질 차이가 났다고 적었다.

**실사용 요령이 정반대라는 것이 핵심이다.**

| 모델 | 지시문을 어떻게 쓰나 |
|---|---|
| Qwen-Image-Edit-2511 (원본) | 설명이 구구절절하면 **오히려 못 알아먹는다** |
| FireRed-Image-Edit | 지시문이 복잡해지더라도 **상세하고 길게 쓸수록** 진가가 나온다 |

워크플로우는 따로 없고 **기존 qwen-image-edit 워크플로우에서 모델만 바꾸면 된다**(댓글 2).
검증에 쓴 지시문은 편집 정밀도(`왼쪽에 있는 원판만 2개로 줄여라`), 생성 오브젝트 품질(`왼팔에 용 문신을 새겨라`),
텍스트 렌더링(`상의를 하얀 면티로 바꾸고 "…" 라는 글자를 넣어라`) 세 가지이고 원문 프롬프트는 영어로 썼다.

> ⚠️ **여기서 나온 규칙 하나는 이 모델에 국한되지 않는다 — 증류 LoRA 는 갈아탄 모델에서 제 성능이 안 난다.**
> 기존 `Qwen-Image-Edit-2511-4step` 고속 LoRA 를 FireRed 에 얹으면 지시 이행률은 원본보다 높지만
> **20 step · cfg 2.5 원본 수준의 품질은 안 나온다.** LoRA 는 베이스 모델 가중치에 덮어씌우는 것이라,
> **이전 모델에서 증류한 LoRA 를 그 모델의 파인튜닝판에 얹으면 품질 하락이 필연적**이기 때문이다.
> 품질 하락 없이 4step 을 쓰고 싶으면 개발팀의 공식 증류 모델을 기다리는 편이 낫다.
> 로라 호환 규칙 전반은 위 "베이스 · 파인튜닝 · 병합" 항목을 보라.


<small>근거 — [Qwen-Image-Edit-2511 vs FireRed-I… 26.02](https://arca.live/b/aiart/162479433)</small>

## 모델 용량 줄이기 — '경량화 7GB→4GB' 는 틀린 설명이다
<small>⚠️ 2023-02 기준 · 근거 3건 · 자료 엇갈림</small>

"모델 용량이 커서 줄이고 싶다" 는 요구는 코랩 시절부터 있었고, 채널에 **서로 어긋나는 두 설명**이 남아 있다.
**둘 중 하나는 틀렸다.**

### ⚠️ "체크포인트 병합 탭으로 7GB → 4GB 경량화" 는 틀린 설명이다

원문 68966157 은 WebUI **체크포인트 병합(Checkpoint Merger)** 탭에서
주 모델만 지정하고 `Multiplier 0` · 보간 `None` · **`Save as float16` 체크** 후 Merge 하면
7GB 가 4GB 로 **'경량화'** 된다고 적었다.

> **이 설명은 틀렸다** *(댓글 정정)*. 그것은 경량화가 아니라 **`fp32` 를 `fp16` 으로 낮춘 것일 뿐**이고
> **EMA 가중치는 그대로 남아 있다.** 게다가 **Anything V3 기준으로는 결과물 그림도 조금 달라진다.**

절반만 줄이고 결과물까지 바꾼 셈이다.

### 실제 구조 — 7GB 는 무엇으로 되어 있나

```text
7GB   =  EMA 약 3GB  +  fp32 가중치 약 4GB
  ↓  fp32 → fp16
4~5GB
  ↓  EMA 제거 (no-ema / pruned)
2GB
```

**EMA 는 본격적인 학습에만 쓰인다.** 병합·LoRA 사용·그림 생성에는 **전혀 필요 없는 데이터 덩어리**라
떼어내도 결과가 사실상 같다. 그렇게 EMA 를 제거한 모델을 **`pruned`** 라 부른다.
표기 자체는 [용어집](glossary.md) 의 "파일 형식 — `.ckpt` / `.safetensors` / fp16 / EMA" 항목에 정리돼 있다.

### 제대로 줄이는 법 — Model Converter

```text
https://github.com/Akegarasu/sd-webui-model-converter.git
```

체크할 항목이 **`fp16` · `no-ema` · `ckpt/safetensors`** 세 개뿐이라 병합 탭보다 오히려 직관적이고,
지금은 확장기능 목록에 등록돼 있어 `install from URL` 없이도 설치된다.

| 목표 | 설정 | 결과 |
|---|---|---|
| 최대한 줄이기 | `fp16` + `no-ema` | **2GB** |
| **그림이 바뀌는 게 싫을 때** | `fp32` 유지 + `no-ema` 만 | 약 **3GB 절감** |

**그림이 달라지는 것은 fp16 쪽이지 no-ema 쪽이 아니다.** 결과를 지키고 싶으면 EMA 만 떼면 된다.

> **fp16 변환의 차이는 대개 미세하다** — 시드 고정 상태에서 머리 꽃장식 유무 정도였고,
> 원문 69024846 작성자는 "안심하고 쓰라"고 결론지었다. **단 AnythingV3 계열은 예외**라고 단서를 달았고,
> 68966157 댓글의 "결과물이 달라진다" 는 지적도 Anything V3 기준이다. **두 글이 같은 예외를 가리킨다.**

### 변환 후에는 반드시 그림을 뽑아 확인한다

- 로그창의 진행 숫자가 **안 올라가고 멈춘 것처럼 보이는 게 정상**이다
- 로그가 **아예 안 뜨면** 원본 모델 자체에 문제가 있을 수 있으니 그 모델이 정상 동작하는지 먼저 확인한다
- ⚠️ **`xformers` 를 켜면 시드를 고정해도 결과가 완전히 재현되지 않는다** *(댓글)*. 업스케일 시 더 심하다.
  변환 전후를 비교할 때 이걸 모르면 없는 차이를 만들어 낸다

### 덤 — "safetensors 는 대용량" 도 틀린 설명이다

원문 70241791 은 출력 형식을 *"`half` = 저용량 파일(fp16), `safetensors` = 학습용 데이터 포함 대용량"* 이라고 적었다.

> **틀렸다.** `.safetensors` 는 **파일 컨테이너 형식일 뿐**이고 담긴 내용은 `.ckpt` 와 같다.
> **용량을 좌우하는 것은 `fp16` 여부와 EMA 포함 여부다.** 같은 정정이 [용어집](glossary.md) 에도 들어 있다.

---

*⚠️ **낡음 주의** — 위 세 원문은 전부 **2023년 SD1.5·A1111 시절** 자료다. 지금 주력인 Illustrious·ANIMA
계열에는 그대로 적용되지 않고, 특히 **ANIMA 처럼 디퓨전 모델·텍스트 인코더·VAE 가 분리 배포되는 모델**에는
'7GB 체크포인트' 라는 전제 자체가 없다. 요즘 용량을 줄이는 수단은 EMA 제거가 아니라 **양자화**다
— 이 문서의 "양자화 파일 고르기 — fp16 / fp8 / GGUF / int8convrot" 항목을 보라.
살아남는 것은 **`fp16` 여부와 EMA 포함 여부가 용량을 결정한다**, **EMA 는 생성에 필요 없다**,
**용량을 줄일 때 결과가 바뀌는 쪽은 정밀도(fp) 변경이다** 세 가지다.*


<small>근거 — [모델 컨버터 사용법(모델 용량 줄이는 법) 23.02](https://arca.live/b/aiart/69024846) · [기초) 모델들 용량 줄이는 방법 (병합 활용 7GB->4GB) 23.02](https://arca.live/b/aiart/68966157) · [병합하는 방법은 공지 없음?? 23.02](https://arca.live/b/aiart/70241791)</small>

## 18-b. v-pred 모델을 어디서 어떻게 돌리나
<small>2025-09 기준 · 근거 3건</small>

`v-prediction`(v-pred) 모델은 **아무 실행기에서나 돌지 않는다.** 받아 놓고 안 나온다면 여기부터 확인한다.

| 실행기 | 되나 | 무엇을 해야 하나 |
|---|---|---|
| **ComfyUI** | ○ | `ModelSamplingDiscrete` 노드를 **`v_prediction`** 으로 두고 **`zsnr` 을 `true`** 로 하면 더 좋다 |
| **reForge** | ○ | **알아서 처리한다** |
| **Forge** | ○ | **ZeroSNR 관련 설정을 직접** 해야 한다 |
| **A1111 WebUI** | △ | **`dev` 버전이 아니면 v-pred 미지원** |

v-pred 모델에는 **RescaleCFG** 도 함께 쓰면 좋다 (설정 참고 `https://arca.live/b/aiart/128421439`).
Rectified Flow 계열은 `ModelSamplingDiscrete` 가 아니라 `ModelSamplingSD3` 를 쓴다(아래 18-c).

### EPS 모델을 V-pred 로 바꾸는 병합 기법

EPS 모델과 V-pred 모델을 그냥 섞으면 품질이 떨어지고 노이즈가 낀다. 그런데 **같은 모델의 vpred 판과 eps 판의
차이를 더하면** 전환이 된다.

```text
EPS 모델  +  ( rouwei_07_vpred  −  rouwei_07_epsilon )   →  V-pred
```

ComradeshipXL v14VWW 가 이 방식으로 만들어졌다 (RouWei-0.7 `https://huggingface.co/Minthy/RouWei-0.7`).

> 이것은 위 "병합의 금기 — eps 와 v-pred 는 섞이지 않는다" 를 뒤집는 것이 아니라 **조건을 붙이는 것**이다.
> **서로 다른 모델**(noob vpred 1.0 ↔ ilxl 1.0)의 차이값을 더하면 여전히 노이즈 덩어리가 되고,
> **같은 모델의 예측방식 쌍**을 쓸 때만 통한다.


<small>근거 — [V-Pred 병합모델 ComradeshipXL v14VW2 … 25.05](https://arca.live/b/aiart/138326689) · [WAI 15 기반 V-pred 병합모델 Comradeship… 25.09](https://arca.live/b/aiart/146874458) · [고해상도 생성용 병합모델 ComradeshipXL v14VX… 25.04](https://arca.live/b/aiart/132946028)</small>

## 18-c. Rectified Flow(RF)와 EQ-VAE — 세 번째 예측 방식
<small>2025-10 기준 · 근거 1건</small>

`eps` · `v-pred` 와 나란히 놓이는 **세 번째 예측 방식**이 Rectified Flow 다.
데이터와 노이즈를 **직선으로 이어** 샘플링을 단순화한다.

```text
RF 모델을 V-Pred 로 설정해 돌리면  →  돌아가긴 해도 결과가 많이 이상해진다
RF 에는 스케줄러 외에 'shift' 라는 옵션이 따로 있다
```

**ComradeshipXL v14F** (NoobAI RectifiedFlow 실험판 + v14VZ 단순병합) 가 그 사례다.

| 항목 | 값 |
|---|---|
| 다운로드 | `https://huggingface.co/hanzogak/comradeshipXL/blob/main/comradeshipXL-v14F.safetensors` |
| **필수 1** | ComfyUI 에서 **`ModelSamplingSD3` 를 `2.5`** 로 세팅 |
| **필수 2** | **모델에 내장된 VAE** 를 쓸 것 |
| 샘플 | `Euler a` / `Simple` / **CFG 2.5** / **10 스텝** / `1024x1536` |

**둘 중 하나만 어겨도 결과가 망가진다.**
순정 WebUI 에서는 정상 작동하는 샘플러가 **4개 정도뿐이고 스케줄러는 아예 먹히지 않았다**는 보고가 있다
(제작자는 RF 가 원래 일부 샘플러에서만 도는 게 맞지만 이 모델이 좀 이상한 것이라고 답했다).
ComfyUI 에서는 샘플러·스케줄러를 바꿔도 이미지는 얼추 나온다.

### EQ-VAE 가 들어간 모델의 로라 제약

일부 LoRA 가 `conv` 영역에 영향을 줘서, **EQ 모델로 학습된 LoRA 만 쓰거나 마지막에 EQ 호환용 LoRA 를
덧씌워야 하는** 불편이 있다. 프롬프트 작성법 자체는 기존과 비슷하다는 것이 테스트한 사람의 결론이다.


<small>근거 — [NoobAI 기반 병합모델 ComradeshipXL v14F… 25.10](https://arca.live/b/aiart/151922549)</small>

## 19-b. `wai anima` 는 SDXL 이 아니다 — 이름이 비슷해서 생기는 사고
<small>2026-06 기준 · 근거 3건</small>

받기 전에 **계열부터 확인해야 하는 대표적인 함정**이다.

| 이름 | 계보 | 로라·VAE·워크플로우 |
|---|---|---|
| **WAI Illustrious** (`wai-illustrious-sdxl`) | SDXL → Illustrious | SDXL 용이 그대로 통한다 |
| **WAI ANIMA** (`https://civitai.red/models/2544636/wai-anima`) | **Cosmos-Predict2 기반 ANIMA** | **SDXL 용이 그대로 통하지 않는다** |

배포자가 본문에서 **굵게 강조한 대목**이다 — 이름이 비슷해 헷갈리기 쉽지만 **ANIMA 는 SDXL 이 아니다.**
같은 이유로 ANIMA 계열은 기존 ILXL 로라를 쓸 수 없고, 로라는 ANIMA 계열(프리뷰 1~3 · 정발 Base 1.0)로
학습된 것을 베이스 버전에 맞춰 골라야 한다.

### 튜닝 색이 강한 모델일수록 작가 태그가 안 먹는다

작가 조합으로 그림체를 만드는 사람이라면 모델을 고르기 전에 확인해야 한다.

```text
Cat · Cotton · AnimaYume   →  작가 태그의 존재감이 많이 희석된다
NTRMIX 3.5 이상            →  품질·광원 로라를 병합해 넣으면서 작가 태그 영향력이 줄었다
```

### 작가 로라의 세기는 가중치 숫자로 정해지지 않는다

작가 로라를 **5개나 넣었는데도 `melowh` 그림체가 다 뚫고 나왔고, 가중치 `0.5` 의 melowh 가
`1.3` 의 `oda non` 을 눌러 버렸다.** 특정 작가는 훨씬 강하게 박힌다.

→ ANIMA 자체는 [ANIMA](anima.md), 짝이 되는 튜닝 모델 목록은 [자원](resources.md)


<small>근거 — [개인적인 Anima+IL 워크플로우 세트 구성품 추천 26.05](https://arca.live/b/aiart/169680210) · [(anima) 아사나기 그림체 로라 2종+작가 태그 테스트 26.05](https://arca.live/b/aiart/172194583) · [첸돚거 그림체 커스텀+기타 개인 설정세팅값 자료 26.06](https://arca.live/b/aiart/174789689)</small>

## 10-c. ANIMA 고속화 병합판 — 한 모델에 모드가 세 개
<small>2026-03 기준 · 근거 2건</small>

`Anima-Comradeship` 계열은 Anima-Preview 에 고속 LoRA 를 병합한 것으로,
**한 파일을 모드별로 다르게 세팅해 쓴다.** 모드마다 샘플러·스케줄러·CFG·스텝이 전부 다르다.

### v1T7 (2026-02) — 세 모드

| 모드 | 샘플러 / 스케줄러 | CFG | 스텝 | 배속 |
|---|---|---|---|---|
| 일반 | `er_sde` / `simple` | 3.0 | 20~30 | 1× |
| 고속 | `euler_ancestral` / `simple` | 2.5 | 8~12 | 2~3× (일부 프롬프트가 안 먹을 수 있다) |
| 초고속 | `dpmpp_2m` / `simple` | **1.0** | 7 | 6~8× — **비권장** |

### v1T8 (2026-03) — 고속/초고속 전용

고속 LoRA 블록 병합을 더 적극적으로 넣은 대가로 **일반 모드의 적절한 세팅을 제작자 본인도 모르겠다고 밝혔다.**

| 모드 | 샘플러 / 스케줄러 | CFG | 스텝 | 배속 |
|---|---|---|---|---|
| 고속 | `dpmpp_2m_sde_gpu` / `simple` | 2.5 | 14 | 2× |
| 초고속 | `dpmpp_2m_sde_gpu` / `simple` | **1.0** | 14 | 4× — 채도가 낮게 나와 워크플로우에 **채도 보정이 포함**돼 있다 |

> **CFG 1.0 은 조건/무조건 예측을 분리하지 않는 지점이라 네거티브 프롬프트가 무의미해진다.**
> 초고속 모드에서 네거티브를 쓸 수 없고 성능 하락이 상당한 이유가 이것이다.

```text
모델   https://huggingface.co/hanzogak/Anima-Comradeship/
VAE·TE https://huggingface.co/circlestone-labs/Anima/tree/main/split_files   ← 따로 받는다
워크플로우  같은 저장소 workflow/ 폴더에 모드별 json (v1T7-normal / -fast / -veryfast, v1T8_fast / _veryfast)
샘플   832x1216, ComfyUI EXIF 포함
```


<small>근거 — [Anima-Preview 고속화 병합모델 Anima-Comr… 26.02](https://arca.live/b/aiart/163306203) · [Anima-Preview 고속화 병합모델 Anima-Comr… 26.03](https://arca.live/b/aiart/163971242)</small>

## 17-b. Illustrious-XL 2.0 은 1.0 대비 퇴보했다 — 2025-04 현장 평가
<small>⚠️ 2025-04 기준 · 근거 3건</small>

ILXL 2.0 이 공개되자마자 그것을 베이스로 병합한 사람들이 남긴 기록이다.
**버전 숫자가 올랐다고 나아진 것이 아니다.**

| 증상 | 내용 |
|---|---|
| 고해상도 붕괴 | 인물이 기형으로 **3명이 나오는** 등 `solo` 조차 제대로 안 된다 |
| 프롬프트 인식률 | 엉망이 되어 **오히려 SDXL 기본 해상도가 '그나마' 낫다** |
| 병합 회귀 | ILXL 1.0 병합 베이스에서 잘 나오던 것이 2.0 에서 무너졌다 |
| 로라 | 이전 모델들보다 일관성이 떨어진다 |
| **고속화 상실** | ILXL 2.0 을 섞으면 ComradeshipXL v14 시리즈의 고속화 특성이 망가져 **최소 25스텝 이상**이 필요해졌다 |

`NNGMIXv4.1-XL` 은 제작자 스스로 '그림이 불안정하니 여러 테스트가 필요하다' 고 미리 경고했고,
`NNGMIXv4.2-XL` 에서 고해상도 안정도를 보강했지만 **ILXL 2.0 원본보다는 낫되 완벽하지 않고
특히 가로로 긴 이미지에서 약하다**고 밝혔다.

### NNGMIXv4.2-XL 제작자 세팅 (참고값)

```text
샘플링   Euler a
스케줄   Automatic  (ComfyUI 는 Normal)
Steps    28        CFG 5
해상도   832~1216  또는 1152~2016(고해상도)
Hires    Upscaler 4x-UltraSharp / Steps 10 / Denoising 0.35 / Upscale by 1.25~1.5
ADetailer  얼굴만
프롬프트 순서   Quality tags, Rating → 인물·옷·행동·배경·사물·광원 → 작가·로라
```

> **함정 하나** — 이미지가 흐리멍텅하게 나온다는 사람의 원인이 프롬프트의 **`shabby`** 태그였다.
> '허름한 집' 을 파파고로 옮긴 것인데, 제작자는 **단부루 태그인 `abandoned`** 를 쓰라고 답했다.
> **사전적 번역어가 아니라 실제 단부루 태그를 써야 한다.**


<small>근거 — [병합모델공유 NNGMIXv4.2-XL 25.04](https://arca.live/b/aiart/134980776) · [고해상도용 병합모델 ComradeshipXL v14KC 모델… 25.04](https://arca.live/b/aiart/134594033) · [병합모델공유 NNGMIXv4.1-XL 25.04](https://arca.live/b/aiart/134463563)</small>

## 17-c. 고해상도 특화 ComradeshipXL 계열 — 버전별 스펙표
<small>2025-09 기준 · 근거 4건</small>

'몇 픽셀까지 뽑히나' 를 따질 때 가장 자주 언급되는 계열이다. **전부 V-pred 라 reForge·Forge·ComfyUI 가 필요하다.**

| 버전 | 기반 | 해상도 | 샘플 세팅 |
|---|---|---|---|
| **v14VX** | NoobAI-XL-Vpred-1.0 | 권장 `1536x1536` · 최대 `1796x1796` · **landscape 미지원** | `Euler a` / `SGM Uniform` / CFG **2.0** / 20스텝 / RescaleCFG Normal 0.7 |
| **v14KC** | ILXL 2.0 병합본 + NoobAI EPS 1.1 을 **1:1** | 권장 `1536x1536` · 최대 `1796x1796` | `Euler a` / `SGM Uniform` / CFG **3.5** / **최소 25스텝** / `1536x2048` |
| **v14VW2** | NoobAI 1.0 V-Pred + Rouwei 0.8 EPS (Karcher-merge) | `832x1216` | `Euler a` / `SGM Uniform` / CFG **2.0** / 20스텝 / RescaleCFG 0.7 / **ZeroSNR** |
| **v14VWW** | **WAI 15** 기반 | `1024x1536` | `Euler a` / **`Beta`** / CFG **3.5** / 20~28스텝 / RescaleCFG **OFF** / ZeroSNR ON |

```text
전부  https://huggingface.co/hanzogak/comradeshipXL/blob/main/comradeshipXL-<버전>.safetensors
```

### 무리한 고해상도는 대가가 있다

- **v14VX** — 해상도를 무리하게 끌어올린 탓에 복잡한 상황에서 타율이 나쁘고 병합 오남용 부작용이 상당하다.
  **`1280x1280` 이하로 쓰거나 일반 Hi-res 를 쓸 거라면 다른 NoobAI-XL 기반 모델이 낫다.**
- **v14KC** — 고해상도로 테스트하면 여전히 인체가 한 번씩 망가지고, 제작자도 1:1 병합인 데다
  원본 모델들이 완전한 고해상도 지원을 하는 것은 아니라 **리스크 있는 행위**로 본다고 인정했다.
- **v14VWW** — WAI 15 의 NSFW 튜닝을 얻은 대신 **v14VW3 이 갖고 있던 고속화 특성을 잃었다.**

### 자연어 이해 — 병합이 없던 능력을 만들지는 못한다

**병합 모델이 자연어를 이해하는 것은 기반 모델들이 이미 자연어 프롬프트로 학습됐기 때문이다.**

```text
자연어 이해력이 있는 Illustrious 계열   NoobAI 1  /  ILXL 2  /  Rouwei 0.8
기대치                                  아니메 SDXL 기준으로 나아진 것이지,
                                        T5 급 텍스트 인코더를 쓰는 NAI 4 와 비교하면 처참한 수준
```

문장형 프롬프트의 동작성은 확실히 좋아져 다른 모델은 알아듣지 못하던
'햇살 드는 도심 광장이나 조용한 공원 산책로' 같은 배경 서술을 반영했지만, **생소한 개념은 나아진 것이 없다.**

> ⚠️ **v14VW2 에서 RescaleCFG 를 0.7 아래로 내리면 블루아카이브 헤일로가 튀어나오는 비중이 크게 올라간다** —
> 프롬프트가 복잡해질수록 10장 중 8장꼴이며, 제작자는 v14 계열에서 캐릭터 지정이 없으면
> 발생할 수 있는 현상이라고 답했다.


<small>근거 — [고해상도용 병합모델 ComradeshipXL v14KC 모델… 25.04](https://arca.live/b/aiart/134594033) · [V-Pred 병합모델 ComradeshipXL v14VW2 … 25.05](https://arca.live/b/aiart/138326689) · [WAI 15 기반 V-pred 병합모델 Comradeship… 25.09](https://arca.live/b/aiart/146874458) · [고해상도 생성용 병합모델 ComradeshipXL v14VX… 25.04](https://arca.live/b/aiart/132946028)</small>

## 13-c. 풀사이즈 LoRA 와 NewBie — Lumina 계열 주변에서 알아 둘 것
<small>2025-11 기준 · 근거 3건</small>

### ⚠️ 10GB 짜리 파일인데 체크포인트가 아니다 — '풀사이즈 LoRA'

`Comradeship LU v2T1KIT` 는 용량이 **10GB** 나 되지만 **체크포인트가 아니라 LoRA 이므로 반드시 LoRA 로
로드해야 한다.** 체크포인트로 로드하면 안 된다.

```text
풀사이즈 LoRA   네트워크 랭크와 무관하게 존재하는 형태
                학습으로는 만들 수 없고, 모델 추출 작업으로만 뽑을 수 있다
왜 이 형태인가   Neta Lumina Alpha 가 2차 배포를 허용하지 않아 가중치를 포함할 수 없었다
다운로드        https://huggingface.co/hanzogak/comradeshipLU/blob/main/comradeshipLU-v2T1KIT.safetensors
병합식          (LeX-Lumina − Lumina-Image-2.0) × 0.2
```

성능은 글쓴이 스스로 '범용 프롬프트 지시 이행 능력이 예상보다 좋지 않다', 댓글에서도
'그냥 타율이 소폭 상승하는 용도' 라고 낮춰 평가했다.

### NewBie image v0.1-exp — SDXL 바깥으로 가려는 다음 시도 (2025-11 예고)

| 항목 | 값 |
|---|---|
| 저장소 | `https://huggingface.co/NewBie-AI/NewBie-image-v0.1-exp-model-repo` |
| 계열 | SDXL 이 아니라 **Lumina-image 2.0 계열 DiT** |
| 텍스트 인코더 | `Google/Gemma3-4b-it` + `Jina AI/Jina Clip v2` |
| 네트워크 | `Next-DiT 3.5b` (26레이어 → **36레이어**로 확장) |
| VAE | `Flux.1 Dev VAE` |
| 학습 데이터 | danbooru 전체 + e621 100만 장 (텍스트를 XML 형식으로 재구성) |
| 학습 자원 | H200 **8장으로 4개월**, 총 **2만 3천 H200 시간** |
| 진행도 | 글 작성 시점 학습 60% · 전체 개발 80%. **공개 예정일 2025-12-31** |

NoobAI 개발진이 다수 참여한 것으로 보인다. **이 글 하나로는 쓸 수 있는 모델이 아니고**,
'로컬 아니메 모델이 SDXL 에서 DiT 로 넘어가려는 흐름' 을 파악하는 용도로 본다.
공개 예정일이 지났으므로 **실제 배포 상태는 직접 확인해야 한다.**

> 댓글의 속도 감각 — Lumina-image 2.0 은 **VRAM 요구는 낮은 대신 속도가 SDXL 의 1/4 수준**이고,
> RTX 4080 Super 에서 `1024x1024 · 30스텝` 이 약 20초다. NewBie 는 모델을 더 키웠으니 더 느릴 것이라는 예상이다.


<small>근거 — [앞으로 출시될 로컬 이미지 모델 NewBie-AI 25.11](https://arca.live/b/aiart/154900388) · [Neta-Lumina 기반 병합모델 Comradeship L… 25.07](https://arca.live/b/aiart/141964528) · [Neta Lumina Alpha용 Comradeship LU… 25.06](https://arca.live/b/aiart/140558851)</small>

## 25-b. 2023년 SD1.5 병합모델 배포글의 권장값을 읽는 법
<small>⚠️ 2023-04 기준 · 근거 9건</small>

채널 초기(2022-11 ~ 2023-04) 병합모델 배포글에는 권장값이 친절하게 적혀 있는데,
**그 수치를 지금 SDXL·Illustrious 계열에 그대로 옮기면 안 된다.** 감각 자체가 다르다.

| 모델 | 권장값 |
|---|---|
| `idkwiMIX` | **CFG 5** — 10 근처면 색이 쨍하게 탄다 |
| `ExpMix_Line_V2` | `DPM++ SDE Karras` / Clip skip **1~2** / **CFG 6~10** / Denoise 0.4~0.65 / Hires `R-ESRGAN 4x+Anime6B` |
| `Xtracolor.v18` | `DPM++ 2M Karras` / Steps 30 / **CFG 8** / **512x768** / upscaler `latent(nearest)` / Denoise 0.6 / Clip skip 2 |
| `C-Moon SD` (2~3등신 치비) | 긍정 `(best quality), (masterpiece), (Chibi)` / 부정 `(worst quality:1.4), (low quality:1.4)` |

```text
2023 SD1.5   CFG 6~10, 512x768, Clip skip 2
2026 SDXL계  CFG 2~7,  1024 이상
```

### 얼굴이 뭉개지면 ddetailer 로 덮는 것이 당시 표준이었다

`GradationWhite` 배포글은 **'배경을 잘 넣어 주는 대신 얼굴이 뭉개지는데, 싫으면 ddetailer 로 해결하라'**
고 아예 적어 두었다. `Xtracolor.v18` · `C-Moon SD` 도 같이 권했다.
`ddetailer` 는 지금 [디테일러](detailer.md) 문서의 ADetailer 이전 세대다.

### 스타일 로라는 파일만으로 완성되지 않는다

| 로라 / 모델 | 반드시 함께 넣을 것 |
|---|---|
| 낙서 스타일 `rkgk` (`https://huggingface.co/4sho/rkgk`) | `monochrome, manga, ink, sketch` |
| 치비 특화 `C-Moon SD` | `Chibi` — 안 넣으면 일반 체형으로 나온다 |
| 한복 `Hanbok_LoRA_V2` (가중치 0.8) | 네거티브에 `animal_ears, japanese_clothes, kimono, chinese_clothes` — **한복이 기모노·치파오로 새는 것을 막는다** |

낙서 로라는 실사용자가 **'완전히 러프하게 쓰기보다 다른 로라와 병합해서 쓰면 훨씬 좋다'** 고 덧붙였다.


### 병합 배포글의 예시 설정에서 읽을 것 둘 (2023-02)

| 모델 | 예시 설정에서 건질 것 |
|---|---|
| **BACLA-MIX** (69704838) | Steps 20 / `DPM++ 2M Karras` / CFG 8 / Clip skip 2 / hires.fix denoise 0.6 / **`hires steps 0`** / 업스케일러 `ERGAN_4x` / 2배. **`hires steps 0` 은 A1111 에서 '본체 스텝과 같게 쓰라' 는 뜻이다** — 옛 EXIF 에서 0 을 보고 당황하지 않으면 된다. 댓글에서 **`half` 버전은 fp32 대비 fp16 저용량 버전**이라고 확인됐다 |
| **MIX-Pro-V4 Beta** (70413762) | 예시는 전부 **`4x-UltraSharp` 로 업스케일**했고 **ddetailer 는 쓰지 않고 Hires.fix 만** 썼다. VAE 는 댓글에서 **`kl-f8-anime2.ckpt`**. **Clip skip 1 과 2 의 색감 차이가 유난히 커서 양쪽 다 쓸 만하니 스왑해 가며 뽑으라**고 권한다 |

**MIX-Pro-V4 는 이 문서를 읽는 법 자체의 예시이기도 하다** — 본문의 다운로드 링크가 이후 무효화됐고
**정정은 댓글에** 있다(`MIX-Pro-V3.5+Lignes`, `civitai.com/models/14206`). 게다가 **글쓴이 본인이 "테스트하다 V3 보다 못한 부분이 있었다" 고 인정**했다.
→ [자원](resources.md) 의 '3-e. ⚠️ 배포글 본문이 틀렸던 것들'

<small>근거 — [한복 로라 다시 만들어왔음 23.02](https://arca.live/b/aiart/69505242) · [(병합대회) MIX-Pro-V4_Beta 23.02](https://arca.live/b/aiart/70413762) · [낙서 스타일 LoRA 23.04](https://arca.live/b/aiart/73263468) · [ExpMix_Line_V2 모델 업데이트 23.02](https://arca.live/b/aiart/70802971)</small>

??? note "근거 9건 전부 보기"
    [한복 로라 다시 만들어왔음 23.02](https://arca.live/b/aiart/69505242) · [(병합대회) MIX-Pro-V4_Beta 23.02](https://arca.live/b/aiart/70413762) · [낙서 스타일 LoRA 23.04](https://arca.live/b/aiart/73263468) · [ExpMix_Line_V2 모델 업데이트 23.02](https://arca.live/b/aiart/70802971) · [(병합모델) C-Moon SD 공유 23.04](https://arca.live/b/aiart/73744147) · [병합모델 Xtracolor.v18 배포 23.02](https://arca.live/b/aiart/70825950) · [개인 병합 모델 공유 idkwiMIX 23.02](https://arca.live/b/aiart/69875937) · [(병합대회) BACLA-MIX 23.02](https://arca.live/b/aiart/69704838) · [개인병합 모델, 로라모음 공유함 23.03](https://arca.live/b/aiart/72576924)

## 12-b. 개별 배포 체크포인트·로라 추가분 (2025-01 ~ 2026-07)
<small>2026-07 기준 · 근거 6건</small>

계열 설명에는 안 들어가지만 **받아서 쓸 때 알아야 할 개별 모델**들이다.

### `OBNMix_V1.5` (NoobAI 계열, 2025-01)

```text
다운로드  https://drive.google.com/file/d/15-lqctDKDN4xnTqJiBwyK7kz7yAbIAc-/view
세팅      스텝 26~30  /  CFG 4.4  /  euler_a + sgm_uniform
퀄리티    masterpiece, best quality, amazing quality, volumetric lighting
```

**v1 과 권장 스텝·퀄리티 프롬프트가 다르므로 v1 세팅을 그대로 쓰면 안 된다.**
26스텝이 하한인 것은 **25스텝에서 깨짐이 심했기 때문**이고, 이후 25스텝에서도 덜 깨지게 보정한
별도 버전이 텐서아트(`https://tensor.art/models/830701663783315316`)에 올라갔다 — 로라 학습을 다시 해서
느낌이 조금 다를 수 있다.

### `CuteLucidMerge` (2025-10) — `https://civitai.com/models/2054164`

시비타이 단속으로 사라진 `zuki cute` 모델을 병합해 살려 낸 체크포인트다.

| | |
|---|---|
| **최대 장점** | 작가 태그나 LoRA 를 **전혀 넣지 않은 순정 상태에서도 선화와 색감이 매력적**이다 |
| **최대 단점** | 웬만해서는 **인물이 어린 쪽으로 나온다** — 취향이 아니면 LoRA·작가 태그로 중화해서 써야 한다 |

### ANIMA 용 2D VAE — `Qwen2D-Anime-VAE`

```text
VAE        https://huggingface.co/Anzhc/Qwen2D-Anime-VAE
필수 노드  https://github.com/Anzhc/anzhc-qwen2d-comfyui     ← 없으면 못 쓴다
```

'2D VAE' 는 Qwen VAE 에서 **이미지 생성에 쓰지 않는(영상용) 차원을 제거해 VRAM 과 속도를 아낀 것**이고,
이번 것은 거기에 **아니메 튜닝까지 들어간 판**이다. ANIMA 뿐 아니라 일반 Qwen VAE 를 쓰는 곳이나 Krea 2 에서도 쓴다.

> **차이는 아주 미미하다.** 제작자도 원본 크기로 봐도 차이가 미미하다고 적었고, 그나마 눈에 띄는 것은
> 머리카락이 떡지는 부분이나 속눈썹처럼 조밀한 영역이 조금 자연스러워지는 정도다.
> **설치 함정** — 커스텀 노드만 깔고 VAE 옵션이 안 생긴다는 사람이 있었는데, **VAE 파일은 따로 받아
> VAE 폴더에 넣어야** 목록에 나타난다. Forge 계열에서는 확장을 직접 만들지 않으면 쓸 수 없다.

### ANIMA 용 flat 그림체 로라 `flackstyle`

```text
Anima 판  https://civitai.red/models/2737018/flackstyle?modelVersionId=3077672
원본      https://civitai.red/models/2100786/k0mugik0-2000-or-shiiros-styles
트리거    flackstyle           권장 강도 0.9~1.0 (댓글)
긍정      (masterpiece, best quality, year 2025, newest, highres:1.5), score_8
부정      worst quality, low quality, score_1, score_2, score_3, text, detailed nose
실패율    손 찐빠 30~40%  /  인체 찐빠 5~10%   ← 제작자가 직접 공개
```

### 웹툰 그림체 로라를 쓸 때 — 퀄리티 태그를 빼라

`waiNSFWIllustrious v16` 으로 학습한 한예나('종말이 찾아왔다') 로라는 **긍정 프롬에 퀄리티 태그를 넣으면
애니 화풍으로 변해 버린다.** 모델마다 다르지만 웹툰 그림체 로라의 공통 특성이다.

### 작가 태그 vs 그림체 로라 — 아사나기 3자 비교 (2026-05)

| 방법 | 결과 |
|---|---|
| 프리뷰3 기반 로라 | 정출 로라보다 못하다 |
| **정출(Base 1.0) 기반 로라** | **가장 낫다.** 기본 ANIMA 이상으로 '프롬프트에 없는 것은 안 그리는' 경향이 생긴다 |
| 로라 없이 **작가 태그만** | 유명 작가는 모델이 이미 알고 있어 **위 둘의 중간쯤** 결과가 나온다 |

> **작가 태그는 로라와 달리 품질 프롬프트의 영향을 크게 받는다.**
> 실험용 최소 프롬프트에서 평시용으로 바꾸자 같은 작가 태그의 결과가 훨씬 나아졌다.
>
> ```text
> 실험용  masterpiece, best quality, score_7
> 평시용  highres, hi res, masterpiece, very aesthetics, best quality,
>         score_9, score_8, score_7, score_6, (anime coloring, anime screencap:1.1)
> ```


<small>근거 — [Anima) flat 그림체 로라 공유 26.06](https://arca.live/b/aiart/175209258) · [(병합모델공유) OBNMix_V1.5 25.01](https://arca.live/b/aiart/125277703) · [웹툰로라) 한예나 26.03](https://arca.live/b/aiart/164851217) · [로컬 농사꾼을 위한 체크포인트 추천 25.10](https://arca.live/b/aiart/151588509)</small>

??? note "근거 6건 전부 보기"
    [Anima) flat 그림체 로라 공유 26.06](https://arca.live/b/aiart/175209258) · [(병합모델공유) OBNMix_V1.5 25.01](https://arca.live/b/aiart/125277703) · [웹툰로라) 한예나 26.03](https://arca.live/b/aiart/164851217) · [로컬 농사꾼을 위한 체크포인트 추천 25.10](https://arca.live/b/aiart/151588509) · [아니마튜닝된 2d vae 26.07](https://arca.live/b/aiart/175945729) · [(anima) 아사나기 그림체 로라 2종+작가 태그 테스트 26.05](https://arca.live/b/aiart/172194583)

## 목적별로 딱 잘라 고르기 — 2025-05 입문 가이드 (지금과의 차이 포함)
<small>⚠️ 2025-05 기준 · 근거 1건</small>

아무것도 모르는 입문자가 **첫 갈래를 잡는 데 가장 직접적인 글**이다 (2025-05 기준, 한 글에서만 언급됨).
'무엇이 제일 좋은가' 가 아니라 **'무엇을 하려는가'** 로 나눈 것이 이 글의 방식이다.

| 하려는 것 | 답 | 단서 |
|---|---|---|
| 야한 애니 일러스트를 **편하게** | **NovelAI Diffusion V4 Full** — `https://novelai.net/` | 16채널 VAE 로 흐릿하지 않고 T5 인코더로 자연어 이해가 개선됐다. **월 25달러 Opus 가 사실상 강제.** 비슷한 것으로 NAI V4.5 · V4 Curated(나체·성교 기능을 뺀 판본) |
| 반드시 **로컬**이거나 NVIDIA RTX 를 쓰고 싶다 | **`WAI-NSFW-illustrious-SDXL`** — `https://civitai.com/models/827184` | Illustrious 1 기반 튜닝. NAI V4 Full 보다는 떨어지지만 쓸 만하다. 비슷한 것 NoobAI EPS 1.1 · NoobAI V-pred 1.0 · Animagine XL 4.0 Opt · RouWei 0.7 |
| **건전한** 이미지를 가볍게 | **구글 Imagen 3** — `https://labs.google/fx/en/tools/image-fx` | 무료인데 성능이 좋지만 **검열이 매우 강하다** |
| 요즘 일반인이 많이 쓰는 것 | **OpenAI GPT-image-1** (ChatGPT 에 '이거 그려줘') | 프롬프트 이해력은 최고지만 **고점이 높은 건 아니고** 결과가 노란색으로 치우치며 느리다. 수영복 정도는 통과 |
| 영상용 이미지를 **로컬로** | **FLUX.1-dev** | 로컬 중 고점이 가장 높으나 일부 프롬프트에서 고집을 부리고 **야한 건 이해하지 못한다.** 대안 HiDream-I1-Fast · SD 3.5 Large Turbo · FLUX.1-schnell |

> **Civitai 같은 무료 온라인 생성 서비스는 검열이 있어 야한 용도로는 비추천**, 건전한 그림이면 나쁘지 않다.
> NAI 결제는 **페이팔을 권한다** — 본문에 이유가 없어 댓글에서 물었더니 *"카드 직결제는 결제 에러가 잘 나서"* 라는 답이 달렸다.

**⚠️ 지금과 달라진 것** — 이 글은 2025년 5월 기준이다.
로컬 항목의 `WAI-NSFW-illustrious-SDXL` 은 여전히 통합팩의 입문 기본값이지만,
**2026년에는 로컬 이미지 생성을 ANIMA 가 사실상 평정했다.** 이 문서의 "체감 대세" 항목을 함께 보라.

→ [처음이라면](overview.md) · [NovelAI](nai.md) · [ANIMA](anima.md) · [자원](resources.md)

<small>근거 — [응애를 위한 AI 그림 모델 선택 가이드 (2025/05) 25.05](https://arca.live/b/aiart/136531062)</small>

## 25-c. 2023년 병합 배포글에서 실제로 건질 것 — 재현 가능성 · 비교 프로토콜 · 상황별 처방
<small>⚠️ 2023-05 기준 · 근거 28건</small>

채널 초기 병합 배포글은 스무 편 넘게 남아 있지만 **모델 파일 자체는 거의 쓸모가 없다.**
그런데도 읽을 값이 있는 것은 **방법론**이 남아 있어서다. 무엇이 남고 무엇이 안 남는지부터 가른다.

### ⚠️ 절반은 애초에 재현이 불가능하다

**제작자가 병합 비율을 기록해 두지 않은 배포글이 아주 많다.** 네 편에서 같은 말이 나온다.

| 모델 | 본문에 적힌 말 |
|---|---|
| `mixedmixedmixed v2` | *"첫 버전은 5개, v2 는 8개 정도인데 정확히는 기억나지 않는다"* |
| `ExpMix` | *"괜찮은 게 나올 때까지 마구잡이로 넣어서 정확히는 기억나지 않는다"* |
| `NGMix` | 병합 **순서만** 기록. 배율은 없음. `G` 이후로는 같은 이름에 계속 덧씌워 그 뒤 순서도 부정확 |
| `JamminMK6` / `INFP` | 비율·권장 세팅·프롬프트가 아예 없음 |

**레시피가 없는 배포글에서 얻을 것은 파일뿐이고, 그 파일의 링크는 대부분 죽었다.**

### 레시피를 남긴 쪽 — 블록 병합(MBW)을 숫자 열로 적는 관행

반대쪽에는 **25개 레이어 가중치를 통째로 공개한** 글들이 있다.

```text
ExpMix_Line_V3 병합 순서 (2023-05)
  ExpMix_Line_V2 + NabiMix   = 0,0,0,0.15,0.3,0.1,0.1,0.2,0,0,0,0.2,0.3,0.2,0,0,0,0.25,0.2,0.3,0,0,0,0,0        → A
  A + Counterfeit V3         = 0.25,0.5,0.15,0.3,0.1,0.2,0.2,0.15,0.3,0.2,0.4,0,0.3,0.1,0.1,0,0.2,0,0,0,0,0,0,0.2,0.2  → B
  B + 0.2 × Mochizuki Kei Art Style LoRA                                                                        → C
  C + Treebark               = 0,0,0.1,0.1,0,0,0,0.05,0.1,0.1,0.1,0.1,0.1,0,0,0,0,0,0,0,0,0,0,0,0               → V3
```

**그 숫자를 어떻게 정했는지**를 적어 둔 글이 하나 있다 (MareColoris, 2023-03). 지금 봐도 방법이 통한다.

```text
1. 25개 레이어를 10개 파트로 쪼갠다
2. Supermerger 로 나머지 파트는 0.5 로 고정하고, 해당 파트만 0 / 1 로 두 장을 뽑는다
3. 둘 중 어느 쪽이 취향인지 따져 가산점을 매긴다
4. 가산점에 따라 파트별 가중치를 정하고 0.05 단위로 반올림한다
```

LoRA 를 체크포인트에 구워 넣을 때의 요령도 여기서 나왔다 — **로라를 직접 병합하면 XY plot 을 못 쓰므로,
베이스 모델에 로라를 강도 1로 통째로 병합한 판을 따로 만들어 두고 그것과 베이스 사이를 블록 가중치로 섞으며 비교한다.**

### 모델을 공정하게 비교하는 프로토콜

레퍼런스걸 공모 규칙(2023-03)이 사실상 비교 프로토콜이었다. **지금 모델을 고를 때도 그대로 쓸 수 있다.**

| 규칙 | 왜 |
|---|---|
| **시드를 포함해 모든 값을 고정** (WebUI 는 XY 플롯) | 값이 하나라도 다르면 비교가 아니다 |
| **LoRA·임베딩(EasyNegative 포함) 전부 금지** | **모델 자체의 성격**을 보려면 외부 보조물을 빼야 한다 |
| 배경은 `white background` 로 통일, 네거티브는 최대한 단순하게 | 캐릭터를 강조하고 변수를 줄인다 |
| **전신이 아니라 `(close up upper:1.4)` 상반신** | 무릎 위까지 담으면 거리가 멀어져 디테일이 죽는다. **사람이 모델을 고르는 기준은 그림 전체가 아니라 그림체·아웃라인** 이라 증명 사진처럼 상체를 찍어야 차이가 드러난다 |
| **전체 EXIF 공개** | 없으면 아무도 재현할 수 없다 |

부수적으로 얻은 관찰 — **`black eyes` 는 인식률이 의외로 높지 않다.**
`smirk` 는 1.2 로 주면 2.5D 계열에서 약하고 1.3 은 줘야 하지만 더 올리면 붕괴하는 모델도 있다.

### 배포글의 '권장값' 을 읽는 법

| 짚을 것 | 실제 |
|---|---|
| 예시 EXIF 를 복사해도 결과가 다르다 | **`medvram` · `xformers` · SD upscale 이 켜진 상태에서 뽑은 것**이라고 다섯 편의 배포글이 모두 명시해 뒀다. 그림체가 재현되지 않으면 **예시 EXIF 를 그대로 한 번 돌려 보고 그것을 기준으로 프롬프트를 고치는 것**이 제작자들의 표준 답이었다 |
| 권장 `Denoise 0.3~0.4` | **절대 규칙이 아니다.** CamelliaMix_2.5D 제작자는 댓글에서 *"체감상 0.3~0.4 정도가 얼굴이 예쁘게 나오더라, 잘만 나온다면 올려도 상관없다"* 고 답했다 — 얼굴 붕괴를 피하려는 경험값이다 |
| 권장 `Clip skip 2` | **clip skip 1 과 2 는 그림체 차이가 크고 특히 화풍 프롬프트를 강조할 때 두드러진다.** 같은 비교에서 **스텝 수도 결과에 꽤 영향을 준다**는 지적이 나왔다 |
| 그림이 흐리고 회색빛 | **VAE 를 안 건 것이다** (입문자가 가장 자주 겪는 증상) — 이 문서의 "옛 SD1.5 자료를 읽을 때" 항목 |

### 뉴비가 자주 하는 오해 셋 — 당시 댓글에서 정정된 것

- **병합 모델은 받아서 그냥 쓰는 것이며 다시 병합할 필요가 없다.**
- A1111 체크포인트 병합 탭의 **C 슬롯은 Add Difference 계열이라 빼기처럼 작동한다.**
- **코랩에서 7GB 짜리 무압축 원본을 병합에 물리면 터진다.** 배포도 fp16/pruned 로 줄여 올리는 것이 관행이 됐다.

그리고 **이름의 숫자가 버전 업그레이드를 뜻하지 않는 경우가 많았다** — 무믹스 시리즈는 숫자가 높을수록 개선된 것이 아니라
매번 다른 방향을 노린 별개 결과물이라, 지적을 받고 그 뒤부터 `stupid` 처럼 이름을 붙이기 시작했다.
파일 형식도 확인하라 — **`.ckpt` 는 악성코드를 심어 배포할 수 있어 지금은 대부분 `.safetensors` 를 쓴다**(병합 시 저장 형식으로 지정 가능).

### 상황별 처방을 함께 배포한 사례

배경 특화 `HighRiseMixV1`(`https://civitai.com/models/7443/highrisemix`)은 증상별 대처를 표로 붙여 배포했다.
**모델 배포글이 어디까지 친절할 수 있는지의 본보기다.**

| 증상 | 처방 |
|---|---|
| 마천루 창문틀이 지저분 | 부정에 `spider web` (*"이유는 모르나 가끔 잘 먹힌다"*) |
| 캐릭터가 너무 멀리 생김 | 긍정에 `(focus upper body)` 또는 `(focus whole body)` |
| 흰/검은 테두리가 두껍게 생김 | 부정의 `border, outside border, white border` 를 강조 |
| 너무 직각적이라 곡선미가 필요 | `curves` **만으로는 안 되고** `railroad tracks, bridges` 같은 구조물을 함께 |
| 포스트 아포칼립스로 | 부정에서 `moss` 를 빼고 긍정에 `post apocalypse, collapsed skyscrapers, broken cars, broken trees` |

같은 계열로 **판본별 성격 차이를 명시한** 사례도 있다 — `CreamLike` 는 의상을 지정하지 않고 뽑으면
**A 는 판타지풍 옷, B 는 현대 의상**이 자주 나오고 B 쪽이 배경이 잘 나온다고 적었다.
`dual_personality` 계열은 **`upper body` 태그가 사실상 필수**이고 전신 등 더 넓은 구도로 가면 타율이 급락한다.

→ 이 문서의 "옛 SD1.5 자료를 읽을 때" · "25-b. 2023년 SD1.5 병합모델 배포글의 권장값을 읽는 법" · [자원](resources.md)

### 병합식 자체를 어떻게 적었나 — 2023-02 대회 출품작 다섯

이 시절 배포글은 **병합식을 그대로 공개하는 것이 관례**였다. 지금 재현할 값어치는 없지만
**어떤 단위로 섞었는지**를 보면 2023년의 병합 문화가 그대로 읽힌다.

| 모델 | 병합 단위 |
|---|---|
| **multicolor.v2** | `Anything.v3 + (OpenNiji + dalcefoBm9V2)` 를 **U-Net 25블록 각각에 소수 가중치**로. `0.23,0.2,0.2,0.16,0.63,0.7,…` |
| **Unico Bergamotto** | `Unico Arancia + OpenNiji` 를 **블록마다 0 아니면 1** 로 — `1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1` / Base alpha 0. **특정 층을 통째로 한쪽 모델에서 가져오는** 방식이다 |
| **Sita7taker** | 오렌지 병합식으로 합친 뒤 **LoRA 를 SuperMerger 로** — `(sita_mix + 7th anime v3) + 헬테이커:0.1:(0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1)`. 뒤쪽 블록에만 1을 주어 **LoRA 영향을 특정 층에 한정**했다 |
| **Kawaii 2D** | 모델을 순차로 섞은 뒤 스타일 LoRA 둘을 0.3씩 — `a=2*0.5+3*0.5`, `b=1*0.3+a*0.7`, `c=b*0.7+4*0.3`, `d=c+(A*0.3)+(B*0.3)` |
| **WhiteSpace Prism** | **3개 모델을 0.25/0.5/0.25 로 묶는 단계를 반복** — `pastelmix×0.25 + anything-v4.5×0.5 + Counterfeit-V2.5×0.25 = WS1` → `WS1×0.5 + qwerty_v2×0.5 = WS2` → … → WS4 |

**배포자가 밝힌 특성 중 지금도 의미가 있는 것**

- **WhiteSpace Prism 은 프롬프트에 `Prism` 을 넣으면 퀄리티가 눈에 띄게 오른다**고 배포자가 안내했다 — 병합 결과에 특정 단어가 붙는 사례.
- **Kawaii 2D 는 제작자도 이유를 모른다고 했으나 손·발 타율이 좋다는 반응이 댓글에서 여러 번 나왔다** (SD1.5 시절엔 드문 장점).
- Sita7taker 는 **로리/비로리 캐릭터의 화폭이 서로 달랐고** 배포자가 원인을 7th anime 의 영향으로 추정했다.
- Sita7taker 예시에서 `Sharp Focus` · `(female focus)` 두 개를 빼고 화사한 배경을 넣으니 바로 귀여워졌다는 관찰이 있다.

### colormixed 가 남긴 실측 셋 (2023-02)

병합 자체보다 **비교 실험** 쪽이 남는다.

| 축 | 결론 |
|---|---|
| **clip skip** | **인물만 뽑을 거면 1, 배경까지 같이 뽑을 거면 2.** clip skip 1 로 전신을 뽑으면 얼굴이 망가지는 경우가 적지 않다 |
| **steps** | **10과 20 사이에서만 큰 차이가 있고 20~90 은 차이가 거의 없다** |
| **CFG** | 높아질수록 **그림이 밝아진다** |
| **업스케일러** | `Latent (nearest-exact)` 는 장식·문양 디테일 / `R-ESRGAN 4x+ Anime6B` 는 **배경+인물 동시 생성 시 얼굴 붕괴 방어** → [업스케일과 화질](upscale.md) |

> **가장 크게 걸린 한계** — **배경 프롬이 들어가거나 인물이 멀리 있는 전신샷에서는 얼굴이 거의 무조건 붕괴했다.**
> 전신은 t2i 만으로 안 되고 **i2i 를 반드시 거쳐야** 했다. 150장 기준 손가락이 키메라처럼 꼬이는 건 드물었지만 6손·7손은 흔했다.

> ⚠ 이 시절 배포글의 권장 프롬프트에는 **`extremly`(→`extremely`) 오타**와
> **`best ratio four finger and one thumb` 같은 미신 관용구**, **`fingers(missing, fused, …)` 함수형 중첩 괄호**가 그대로 들어 있다
> → [프롬프트 쓰는 법](prompting.md) 「⚠ 폐기·오작동 태그와 즉석 조합」.
> 값을 채워 넣을 자리를 C 주석 `/*place tags*/` 로 표시한 **빈칸 채우기 템플릿**을 배포한 글도 있다.


<small>근거 — [도시 배경 특화 U-Net 기반 자작 병합 모델 HighRi… 23.02](https://arca.live/b/aiart/69302021) · [CamelliaMIx_V2 모델 업데이트 23.03](https://arca.live/b/aiart/71600989) · [모델공유) 병합모델 CamelliaMix_2.5D 23.03](https://arca.live/b/aiart/71331822) · [모델공유) 병합모델 CamelliaMix_Line 23.03](https://arca.live/b/aiart/71144590)</small>

??? note "근거 28건 전부 보기"
    [도시 배경 특화 U-Net 기반 자작 병합 모델 HighRi… 23.02](https://arca.live/b/aiart/69302021) · [CamelliaMIx_V2 모델 업데이트 23.03](https://arca.live/b/aiart/71600989) · [모델공유) 병합모델 CamelliaMix_2.5D 23.03](https://arca.live/b/aiart/71331822) · [모델공유) 병합모델 CamelliaMix_Line 23.03](https://arca.live/b/aiart/71144590) · [(레퍼런스걸) 싸이버거 걸고 대회 한번 열어봄 23.03](https://arca.live/b/aiart/71483615) · [모델공유) ExpMix_Line 23.02](https://arca.live/b/aiart/70608629) · [(병합 대회) colormixed 23.02](https://arca.live/b/aiart/69730929) · [약속대로 병합모델 공유: moomix4 23.05](https://arca.live/b/aiart/76635524) · [(레퍼런스걸) 핑핑이 (약 장문 주의) 23.03](https://arca.live/b/aiart/71521039) · [모델공유) 병합모델 CamelliaMix 23.03](https://arca.live/b/aiart/70982910) · [ExpMix_LIne_V3 모델 업데이트 23.05](https://arca.live/b/aiart/76462452) · [처음으로 만든 병합모델입니다. 23.03](https://arca.live/b/aiart/72369910) · [모델공유) 병합모델 ExpMix 입니다. 23.02](https://arca.live/b/aiart/70434894) · [(병합대회) Kawaii 2D 23.02](https://arca.live/b/aiart/70627117) · [(병합대회) Sita7taker 23.02](https://arca.live/b/aiart/70499026) · [모델공유)Lora 병합모델 빅토리안 믹스 개선?버전 23.03](https://arca.live/b/aiart/71147882) · [Treebark 경량화 허깅페이스 링크 23.01](https://arca.live/b/aiart/67648642) · [(병합대회)CreamLike_A,B 23.02](https://arca.live/b/aiart/69662750) · [병합 mixedmixedmixed v2 라능... 23.02](https://arca.live/b/aiart/69423609) · [(병합대회) 오랜지 0%, 파스텔 0% multicolor.… 23.02](https://arca.live/b/aiart/69573598) · [(병합대회) Unico Bergamotto 23.02](https://arca.live/b/aiart/69648477) · [자작) 병합모델 MareColoris 23.03](https://arca.live/b/aiart/70994766) · [(병합대회)WhiteSpace Prism 병합모델 23.02](https://arca.live/b/aiart/70623701) · [병합모델 ( RoyaleEngine-V0.98 ) 공유. 경… 23.03](https://arca.live/b/aiart/72714918) · [28일 시작 뉴비 모델병합해봄 23.03](https://arca.live/b/aiart/71208752) · [저번에 올렸던 모델 수정버젼과 두번째 모델 공유! 23.03](https://arca.live/b/aiart/71308838) · [(공유 종료) moomix20 : stupid 23.05](https://arca.live/b/aiart/77392210) · [dual_personality 모델 업데이트 23.03](https://arca.live/b/aiart/71611067)

## ANIMA 의 제원 — 2.6B 의 내역과 'SDXL 3.5B' 의 정체
<small>2026-02 기준 · 근거 1건 · 자료 엇갈림</small>

ANIMA 가 왜 작은데 잘 나오는가를 SDXL·Z-Image 와 나란히 놓고 따진 글이다.

| | 확산 모델 | 텍스트 인코더 | 합 | 아키텍처 |
|---|---|---|---|---|
| **ANIMA** | **2B** | `qwen3-0.6b` | **약 2.6B** | **DiT** (기반: NVIDIA `Cosmos-Predict2` Text2Image) |
| SDXL 1.0 | Unet 2.6B | CLIP_L 120m + CLIP_G 0.7b | 약 3.5B | Unet |
| Z-Image | 6B | `qwen3-4B` | — | S3-DiT |

> ⚠️ **'SDXL 3.5B' 를 확산 모델 크기로 읽으면 안 된다.** 글쓴이가 처음에 그렇게 적었다가
> 댓글에서 **"확산 모델이 아니라 체크포인트(Unet+CLIP) 기준 3.5B"** 라고 **스스로 정정했다.**
> 확산 모델끼리 비교하면 ANIMA 2B 대 SDXL Unet 2.6B 다.

### 왜 작은데 앞서는가 — 그리고 반론

**본문의 논지** — Unet 은 파라미터를 늘려도 성능이 선형으로만 오르지만,
**DiT**(이미지를 패치 단위로 쪼개 시퀀스로 처리하는 트랜스포머 구조)는 스케일링 법칙이 잘 먹혀 체급에 따라 성능이 기하급수적으로 오른다.

> ⚠️ **댓글의 반론** — **소형 DiT 는 오히려 효율이 나빠서 Neta-Lumina · PD7 · SD3 Medium · NAI4 처럼
> 처참하게 깨진 사례가 많다.** 따라서 'DiT 가 무조건 우월하다' 는 말은 성립하지 않고,
> **ANIMA 의 선방이 오히려 의외의 사건**이라는 것이다.
>
> **재반론** — 그건 아키텍처 문제가 아니라 학습 성숙도·데이터 편향 문제이며 DiT 는 충분한 체급에서 고점이 훨씬 높다.
>
> **결론은 나지 않았다. 양쪽을 적어 둔다.**

같은 방향의 후속 관측이 있다 — 소형 DiT 에 Aesthetic 튜닝을 하면 BASE 의 아니메 지식을 잃기 시작하고,
Unet 시절의 병합 공식은 DiT 에서 깨진 지 오래라 **BASE 성능이 전부**라는 것 → [ANIMA](anima.md)

*(2026-02-01, 한 글과 그 댓글이다.)*

<small>근거 — [Anima의 사례가 Z-Image를 더욱 기대하게 만드는 이유 26.02](https://arca.live/b/aiart/161187637)</small>

## Krea2 아니메 파인튜닝 — CEO 가 말한 조건부 예고 (2026-07)
<small>2026-07 기준 · 근거 1건</small>

Krea CEO(Victor)가 **ComfyUI 공식 유튜브 라이브**(`youtube.com/watch?v=31jiUhCEjJ4`)에서 직접 말한 것이다.

| 발언 | 내용 |
|---|---|
| Krea2 의 현재 | **오픈 웨이트 모델 중 일러스트·애니메이션 생성이 가장 뛰어나다**고 본다. 다만 입력을 더 구체적으로 줘야 해서 기본값으로 프롬프트 인핸서를 붙여 놨는데, 아주 기본적인 수준이니 **애니메이션용 시스템 프롬프트를 직접 만들어 쓰라**고 권한다 |
| 아니메 파인튜닝 | 리드 연구원 **Sangu(한국인)** 에게 Krea2 의 애니메이션 버전을 학습시키도록 허락하는 **핸드셰이크 계약**을 맺어 뒀다 |
| 공개 여부 | 연구원이 하고 싶어 하고 **커뮤니티가 원한다면** 학습 후 공개할 생각이 있다 |
| 그 밖 | RAW/Turbo 외에 **5B 같은 더 압축된 버전**이 내부에 있고 공개를 고려 중이며, 일회성 출시로 끝내지 않고 몇 주~몇 달마다 새 걸 추가하겠다고 했다 |

> ⚠️ **확정이 아니다.** 연구원 의사와 커뮤니티 반응에 달린 조건부 이야기다.

**전망** — Sangu 는 직접 단부루 데이터셋을 만든 경험이 있는 쪽이라 실현 가능성은 있어 보이지만,
나오더라도 **단부루 기반 작가 태그를 쓰는 NAI/ANIMA 방식보다는 니지저니에 가까운 성격**일 것 같다는 관측이 붙어 있다
(로라 학습은 잘 되니 ANIMA 쓰듯 쓰면 될 것이라는 단서 포함).

*(2026-07-01, 한 글이다.)*

<small>근거 — [Krea에서 직접 Krea2 아니메 파인튜닝을 진행할 가능성… 26.07](https://arca.live/b/aiart/175561117)</small>

## 작가 태그 접두사와 재현 범위 — 계열마다 공식 안내가 다르다
<small>⚠️ 2025-02 기준 · 근거 1건</small>

작가 태그로 화풍을 부르는 것은 계열마다 **공식 안내 자체가 다르다.** 표기를 그대로 옮기면 안 먹는다.

| 계열 | 표기 | 근거 |
|---|---|---|
| **NAI** | `artist:이름` | NAI 공식 홈페이지가 이 형식을 안내한다 |
| **Illustrious (ILXL)** | `artist:이름` | ILXL 공식 문법. 빼면 태그 오염이 생긴다(`yd_(orange_maru)` 가 배경에 오렌지를 끌고 오는 식) |
| **NoobAI** | **접두사 없이 작가명만** | NoobAI 는 공식적으로 접두사를 붙이지 말라고 안내돼 있다 (1건, 2025-02) |

### 작가 재현 특화 병합 모델의 설정값 — 샘플러가 CFG 를 정한다

`NAI-XL_vpred1.0_2dac_final50` 처럼 **대부분의 작가명 태그 재현을 노린 NoobAI v-pred 병합**은
CFG 를 샘플러 종류에 맞춰야 작가 스타일이 제대로 나온다 (1건, 2025-02).

| 항목 | 값 |
|---|---|
| **CFG (일반 샘플러)** | **3.0 ~ 4.0** |
| **CFG (CFG++ 계열 샘플러)** | **1.15 ~ 1.35** |
| 스케줄러 | **`SGM Uniform`** 또는 **`KL Optimal`** |
| 샘플러 | `Euler Ancestral CFG++` 또는 `Euler` |
| 해상도 | Noob 과 같은 **1024x1024** |

CFG++ 샘플러를 쓰려면 **reForge 계열 WebUI** 가 필요하다.
Noob v-pred 원본 비율이 더 높은 변형본(`..._naive90.safetensors`)도 함께 배포되며 취향에 따라 후자가 나을 수 있다.

### 어디까지 재현되나 — 단부루 작품 수 70건

> 재현 가능한 범위는 **Danbooru 작품 수 70건 정도까지**이며,
> **캐릭터 태그를 넣으면 작가 스타일이 묻히므로 작가명 쪽 가중치를 더 올려야 한다.**

작가 이름 옆의 단부루 포스트 카운트를 **태그가 먹힐 확률의 지표**로 쓰는 방법은
[자원](resources.md) 의 작가명 썸네일 뷰어 항목에 있다.
NAI 쪽에서도 같은 원칙이 나온다 — **레퍼런스(작품 수)가 적은 작가는 태그로 불러도 재현이 불안정하므로 LoRA 쪽이 낫다.**

→ 프롬프트 쪽 계열 차이는 [프롬프트 쓰는 법](prompting.md) 의 '계열이 갈린다' 절

<small>근거 — [(추가) 대부분의 작가명 태그 재현이 가능한 Noob v-p… 25.02](https://arca.live/b/aiart/128899435)</small>

## krea2 + `Kroma` — 자연어 모델을 태그 모델로 바꾸는 로라
<small>2026-08 기준 · 근거 2건</small>

krea2 는 **원래 자연어로 작문해야 하는 모델**인데, 로라 하나로 그 전제가 뒤집힌다 (1건, 2026-07).

Chroma 제작자(lodestones)가 krea2 용으로 낸 대형 단부루 학습 LoRA **`Kroma`** 다.

```text
https://huggingface.co/lodestones/Kroma
규격 : 256 rank / 1.9GB   (로라치고 매우 크다)
학습 : Danbooru 지식 + e621 지식
```

> **이 로라를 얹으면 자연어를 전혀 쓰지 않고 Danbooru 태그 프롬프트만으로 그림이 나온다.**
> 후기 작성자는 실제로 **모든 그림을 단부루 프롬프트만으로** 뽑았다.

생성 조건은 **1M 픽셀 8스텝에 장당 약 11초**였고, Krea2 Turbo int8 로라 사용/미사용을 비교했다.
첫 버전임을 감안하면 결과가 훌륭하고 개선 여지도 있어, **초대형 파인튜닝 모델이 나오기 전까지의 대안**으로 평가된다.
댓글에서는 사실상 검열 해제 로라로 극찬받았고 실사와 애니 양쪽 다 좋다는 반응, 베이스 모델을 위한 테스트 로라라는 언급이 있었다.

→ 계열별 프롬프트 작성 방식은 [프롬프트 쓰는 법](prompting.md)

### Kroma 0.2 간단 실측 (2026-08)

| 항목 | 값 |
|---|---|
| 배포 | `https://huggingface.co/lodestones/Kroma` |
| 테스트 조건 | 2M 픽셀 해상도 · **8스텝** · 장당 **23초** |
| 실행 | 모델이 너무 커서 **`int8_convrot` 으로 변환**해 돌렸다 |
| 비교 방식 | **같은 태그·같은 시드**로 모델만 Krea2 순정 int8 ↔ Kroma 0.2 int8 로 바꿔 대조 |

**가장 중요한 결론은 프롬프트 쪽이다.**

> 그림 뽑는 데 **단부루 태그만** 사용했고 **확실히 잘 먹힌다.**
> **기존 krea2 에서는 잘 안 먹히던 태그도 Kroma 에서는 먹힌다.**

즉 krea2 계열은 태그 입력에 약하고 Kroma 파인튜닝이 그 약점을 메운다는 뜻이라,
**같은 태그 프롬프트를 계열 간에 그대로 옮기면 안 되는 이유가 하나 더 늘었다**
→ [프롬프트 쓰는 법](prompting.md) 「계열이 갈린다」.

그 외 평가는 주관이다 — 0.1 에서도 만족했는데 0.2 는 더 깔끔해진 느낌이 있고,
순정 모델에 비해 야한 그림이 월등히 잘 뽑히지만 미적인 상승은 잘 모르겠다고 했다.
**표본이 작고 주관 평가라 수치로 받아들일 것은 해상도·스텝·소요시간 정도다.**


<small>근거 — [Krea2 대형 단부루 학습 로라 사용 후기 26.07](https://arca.live/b/aiart/178556661) · [Kroma 0.2 간단 사용 후기 26.08](https://arca.live/b/aiart/179438130)</small>

## 편집 모델에서 되풀이되는 두 함정 — 텍스트 인코더와 다리 길이
<small>2026-01 기준 · 근거 3건</small>

이미지 편집 모델을 처음 물릴 때 **거의 항상 같은 두 곳에서 막힌다.**

### 1. 텍스트 인코더가 따로다

| 모델 | 함정 |
|---|---|
| **FLUX.1-Kontext-dev** | **텍스트 인코더가 동봉돼 있지 않다.** FLUX.1-dev 에서 쓰던 **T5 XXL** 을 따로 물려야 한다 (1건, 2025-06) |
| **Qwen Image Edit** | **텍스트 인코더는 GGUF 판을 쓰면 안 된다.** Edit 모델은 비전 인코더가 필요한데 GGUF 판은 보통 비전 인코더가 제거돼 있다 — Qwen-Image 용 **일반 텍스트 인코더**를 쓴다 (1건, 2025-08) |

Qwen Image Edit 를 **fp8 로 돌릴 때 결과에 노이즈가 잔뜩 끼는 것은 모델 샘플링 노드가 없어서**다.

```text
모델 로드 → (선택) 로라 로드 → 모델 샘플링(AuraFlow) shift 3.0 → KSampler
```

### 2. 다리가 짧아진다

FLUX.1-Kontext-dev 와 Qwen Image Edit 에서 **공통으로** 나타나며, 입력 이미지가 전신이 아닐 때 잘 생긴다.
프롬프트에 이 문장을 추가하면 완화된다.

```text
The figure's lower body are very long. The figure's thighs are very thin.
The figure is very long and very tall.
```

### 성능 위치 (실사용 체감, 시점 주의)

| 비교 | 결론 |
|---|---|
| Qwen Image Edit vs FLUX.1-Kontext-dev | Qwen 쪽이 낫다 (2025-08) |
| Qwen Image Edit vs 나노바나나 | 나노바나나에는 못 미친다 (2025-08) |
| **여럿이 얽힌 편집** | **Qwen Image Edit 쪽이 FLUX.2 Klein 보다 낫다** (2026-01) |
| t2i 용도 | Kontext 는 그쪽으로 튜닝된 모델이 아니라 성능 저하가 있다 — **t2i 는 FLUX.1-dev** |

<small>근거 — [FLUX.1-Kontext-dev 가중치 공개 및 간단한 C… 25.06](https://arca.live/b/aiart/140754531) · [ComfyUI용 Qwen Image Edit 초기 지원 시작 25.08](https://arca.live/b/aiart/145582528) · [Flux.2-Klein-4B 사용기 (뭘 할 수 있는가) 26.01](https://arca.live/b/aiart/160707593)</small>

## 2026 상반기 소형·고속 모델 실측 묶음 — Klein · Mage Flow · ERNIE · int4convrot · Zeta-Chroma
<small>2026-07 기준 · 근거 6건 · 자료 엇갈림</small>

2026년 상반기에 올라온 소형·고속 모델 소식들인데, **속도와 품질의 맞바꿈이 공통 주제**다.
값은 전부 개인 실측이므로 장비가 다르면 달라진다.

### FLUX.2-Klein-4B — T2I 와 편집이 한 모델에 (2026-01)

Black Forest Labs 의 소형 모델로 **T2I 와 Edit 이 통합**돼 있는 것이 특징이다(Z-Image 는 Edit 모델이 따로 있다).

| 항목 | 값 |
|---|---|
| 해상도 | 1MPixel(1024x1024) 기본, 2.25MPixel(1536x1536) 도 문제없음 |
| **T2I** | **Scheduled CFG (첫 스텝만 2.0, 나머지 1.0) + 8 steps** |
| **I2I** | **CFG 1.0 + 4 steps** (변경량이 많으면 I2I 도 Scheduled CFG) |
| 양자화 | fp8 은 bf16 과 거의 같은 품질. **nvfp4 는 4B 에서 품질이 많이 떨어진다**(9B 는 괜찮았다) |
| INT8 자작판 | FP8 대비 RTX3090 +35% · RTX3060 +27%, 품질 비슷. `torch 2.9.0+cu130` + triton + 전용 커스텀 노드 필요 |

편집 지시 끝에 **`Upscale and refine image while keeping all others as original image.`** 를 붙이는 패턴이 반복 사용됐고,
**SDXL 로 뽑았을 때 생기는 제멋대로 뻗는 선과 흐릿한 색 경계를 리파인으로 정리**하는 용도가 특히 좋다.
낙서나 openpose 를 넣고 `change scribbles or openpose to professional anime-style illustration.` 로 완성 일러스트를 만드는 것도 된다.
한계는 **손발 찐빠가 잦고 여러 인물이 나오면 무너지는 것**, 그리고 검열이 많은 편이라는 것이다.

### Mage Flow — 가치는 품질이 아니라 속도다 (2026-07)

마이크로소프트가 만든 약 4B 이미지 생성/편집 모델. **본문의 평가와 댓글의 온도가 다르다.**

| 쪽 | 말 |
|---|---|
| 본문 | 성능이 flux 를 **상회하고도 남는다** |
| **댓글** | **'엄청 빠르긴 한데 품질이 좋지 않다'**, '외국 커뮤에서 klein 4b 와 비교한 걸 봤는데 딱 그 급' |

속도는 확실하다 — **1M 이미지 기준 Krea2 Edit LoRA 28초 vs Mage Flow Edit int8 7초**,
int8 + turbo 로 RTX 3090 에서 1248x832 편집 1장에 약 2초.
int8 과 bf16 은 속도 차이만 크고 품질 차이는 크지 않아 **int8 권장**이다.
한계는 시점 전환 같은 추상적·데이터 집약 작업이고, **검열이 세게 들어가 있으며 Edit 이 아닌 일반 생성 모델은 깡성능이 처참**하다.

### ERNIE-Image — 8B DiT + 3B 프롬프트 인핸서 (2026-04)

바이두가 공개한 8B DiT. 특이한 점은 **3B 크기의 프롬프트 인핸서(PE)를 따로 두어 프롬프트에 따른 성능 편차를 줄인 것**이다.
공식은 VRAM 24GB 라고 적었지만 **8B 치고 과한 수치이고 양자화하면 훨씬 적다** — 실측으로 **RTX 3060 에서 int8rowwise 터보 기준 14초**.
2D 애니 스타일 지원 여부는 확인되지 않았다.

### int4convrot — 가속 지원이 세대별로 뒤집혀 있다 (2026-07)

ComfyUI 가 지원하기 시작한 양자화 방식으로, **순수 int4 가 아니라 int4 · int8 matmul · 16bit 를 섞은 것**이다
(convrot = 가중치에 회전 변환을 걸어 극단값을 흩뜨려 저비트 손실을 줄이는 기법 계열).

> **RTX 3000/4000 은 int4 가속을 지원하지만 5000 시리즈는 int4 가속이 없어 int8 로 연산한다.**
> NVIDIA 가 int4 는 표현 범위가 너무 좁다고 보고 마이크로 스케일링에서 **FP4 E2M1 에 올인**했기 때문이다.

### Zeta-Chroma — 지금도 받아 볼 수 있지만 아니메 모델이 아니다 (2026-04)

chroma 를 만든 lodestones 가 **Z-Image 를 베이스로** 진행 중인 미세조정이다.
`https://huggingface.co/lodestones/Zeta-Chroma` 에 모델과 학습 그래프가 **1시간마다 자동 갱신**돼 지금 당장 받아서 체험할 수 있다.

> ⚠️ **2D(단부루) 전용 모델이 아니다.** 2D 를 일부 포함하면서 NSFW 를 지원하는 성격이라
> 아니메 쪽으로 큰 기대는 하지 말라는 것이 채널 반응이다. 완성 시점 추산은 **학습 그래프에서 역산한 추정**이다.

*⚠️ 위 소식들은 대부분 **글쓴이 한 명의 실측**이다. 아래 「⚠️ 모델 소식을 읽는 법」 절과 함께 읽을 것.*

<small>근거 — [Flux.2-Klein-4B 사용기 (뭘 할 수 있는가) 26.01](https://arca.live/b/aiart/160707593) · [ComfyUI int4convrot 지원 26.07](https://arca.live/b/aiart/176403272) · [바이두산 8b모델 ERNIE-Image 26.04](https://arca.live/b/aiart/167779972) · [ComfyUI에서 Mage Flow 공식 지원 시작했네. 26.07](https://arca.live/b/aiart/178320979)</small>

??? note "근거 6건 전부 보기"
    [Flux.2-Klein-4B 사용기 (뭘 할 수 있는가) 26.01](https://arca.live/b/aiart/160707593) · [ComfyUI int4convrot 지원 26.07](https://arca.live/b/aiart/176403272) · [바이두산 8b모델 ERNIE-Image 26.04](https://arca.live/b/aiart/167779972) · [ComfyUI에서 Mage Flow 공식 지원 시작했네. 26.07](https://arca.live/b/aiart/178320979) · [Zeta-Chroma 올해 중반쯤에는 나올 듯? 26.04](https://arca.live/b/aiart/167731791) · [Mage Flow Edit 간단 후기 26.07](https://arca.live/b/aiart/178550271)

## Chroma·Lumina 계열을 쓸 때 — 캐릭터 호출법과 고속화 병합, 그리고 NSFW 화풍
<small>2025-11 기준 · 근거 6건</small>

Chroma 계열 병합모델(Comradeship CR 시리즈)은 **캐릭터를 부르는 방식이 아니메 SDXL 과 다르다** (4건, 2025-06 ~ 2025-08).

```text
arona \(blue archive\), blue archive, blue hair
   캐릭터명        +      작품명      +   캐릭터 특성
```

**셋을 다 적어야 겨우 작동**하고, **작가 태그는 작동하지 않는 것으로 보인다.**
캐릭터가 작품명과 묶여 학습된 것으로 추정된다.

| 항목 | 내용 |
|---|---|
| 성격 | 아니메 지식은 부족(Chroma 의 선별된 5M 데이터셋 때문으로 추정)하지만 **대형 DiT 로서 범용 지식이 풍부**하다 — '고성능 범용 모델의 검열이 완전히 풀리면 어떤 느낌일까' 용도 |
| 텍스트 인코더 | Chroma 도 구글의 **T5 XXL** 을 쓴다 |
| **양자화** | **FP8 로 로드하면 품질 저하가 있다 — VRAM 16GB 는 GGUF Q8_0 권장.** VRAM 10GB 는 속도 면에서 많이 타협해야 한다 |
| 댓글 온도 | Chroma 는 **Pony V6 처럼 퍼리 타겟 모델에 가까워서** 누군가 따로 튜닝하지 않으면 아니메 쪽 결과는 미지수. 다만 NoobAI/Illustrious 특유의 피부 질감이 없다는 점은 기대 요소 |

### 고속화 로라는 통짜로 병합하면 안 된다

Neta Lumina 기반 `Comradeship LU v2 FINAL FAST` 의 설계 이유다 (1건, 2025-11).

> 고속 추론 튜닝 모델(`lu2_lightning_test`)을 **그대로 통짜 병합하면 가뜩이나 부족한 아니메 지식을 크게 말아먹어 쓸모가 없다.**
> 그래서 **블록 병합**을 택했고, 25~30스텝이 필요하던 모델을 **아니메 지식 손실 없이 약 12스텝**으로 줄였다.
> 샘플 세팅 — `res_multistep / simple / CFG 3.5 / 12스텝 / 832x1216`

### NSFW 로 넘어갈 때 그림체 — Curated 와 Full, 그리고 역발상

NAI V4 의 **CURATED 는 상의만 벗은 남성 캐릭터를 그리려 해도 그림체가 약간 무너지고 채색법 자체가 달라지는** 반면,
**FULL(정출판)은 NSFW 를 학습했을 리 없는 작가만 넣은 조합에서도 그림체가 무너지지 않았다**는 체감 보고가 있다 (1건, 2025-03).

> **댓글의 역발상** — 이 글을 보고 반대로 **프롬에 `nsfw` 를 넣고 수위는 `rating:general` 로 통제**했더니
> 그림체가 잘 안 무너지더라는 보고가 붙었다. **본인도 해골물일 수 있다고 단서를 달았다.**

같은 문제를 Vibe 로 교정하는 방법과 '애초에 NSFW 를 안 그리는 작가로 조합을 짜면 안 생긴다' 는 반례는
[NovelAI](nai.md) 의 Vibe 항목에 있다.

<small>근거 — [Neta Lumina 기반 고속화 병합모델 Comradesh… 25.11](https://arca.live/b/aiart/155089645) · [Chroma 병합모델 Comradeship CR v1T21 … 25.08](https://arca.live/b/aiart/145366717) · [Chroma 병합모델 Comradeship CR v1T4-3… 25.06](https://arca.live/b/aiart/138501441) · [Chroma 병합모델 Comradeship CR v1T7-3… 25.06](https://arca.live/b/aiart/138969996)</small>

??? note "근거 6건 전부 보기"
    [Neta Lumina 기반 고속화 병합모델 Comradesh… 25.11](https://arca.live/b/aiart/155089645) · [Chroma 병합모델 Comradeship CR v1T21 … 25.08](https://arca.live/b/aiart/145366717) · [Chroma 병합모델 Comradeship CR v1T4-3… 25.06](https://arca.live/b/aiart/138501441) · [Chroma 병합모델 Comradeship CR v1T7-3… 25.06](https://arca.live/b/aiart/138969996) · [V4 정출판은 NSFW에서 그림체 안 무너지는듯 25.03](https://arca.live/b/aiart/130237851) · [Chroma 병합모델 Comradeship CR v1T7-3… 25.06](https://arca.live/b/aiart/138621473)

## ⚠ '로컬 모델은 전부 NAI1 유출본 기반' — 틀린 전제다
<small>2026-05 기준 · 근거 1건</small>

채널에 오래 도는 편견인데, 2026-05 의 한 질문글 댓글이 조목조목 정정했다.
본문의 전제(*"로컬 모델은 NAI1 유출 버전을 토대로 만들어졌고 단부루 태그 학습이 덜 됐다"*)는 **틀렸다.**

| 세대 | 실제 |
|---|---|
| **SD1.5 계열** | 여기까지는 **NAI1 유출 기반이라 부를 수 있다** |
| **SDXL 세대** (`Illustrious` · `NoobXL`) | **아예 족보가 다르고 모델 유출 자체가 없었다** |

`NoobXL` 은 NAI3 막바지인 **2024년 10월**에 나왔고 **danbooru 전체 + e621** 학습으로 NSFW 와 지식 범위를 넓혔다.

### 곁가지 — ANIMA 와 NAI 의 자연어 차이

> *"NAI 도 자연어를 어느 정도 알아듣지만 ANIMA 와는 비교가 안 된다. **ANIMA 는 태그 자체를 전부 자연어로 서술할 수 있다.**"*

ANIMA 의 학습 데이터 커트라인은 **2025년 9월**까지이며 태깅도 최신 양식에 맞춰 돼 있다(댓글에서 두 명이 같은 값을 말했다).
따라서 단부루에서 이름이 바뀐 최신 태그도 대체로 반영돼 있다.
다만 아주 마이너한 태그(`under another's clothes` 등)까지 되는지는 확인되지 않았다.

*(커트라인을 실제로 찔러 보는 방법은 [ANIMA](anima.md) 의 '이 캐릭터를 아는가' 절.)*

<small>근거 — [아니마 지금 많이 괜찮은 편인가요? 26.05](https://arca.live/b/aiart/171581384)</small>

## 25-d. 2023년 '레퍼런스걸' 대회 — 모델 비교에 시드까지 고정한 사례
<small>⚠️ 2023-03 기준 · 근거 4건</small>

**2023-03 시점 자료다. 값 자체는 낡았지만 방법론은 그대로 유효하다.**

두 편의 대회 출품글이 SD1.5 계열 애니 모델을 **같은 프롬프트·같은 시드**로 5종씩 나란히 돌렸다.

| 글 | 비교 대상 |
|---|---|
| `71547451` | `lightningcounter7:3ver` · `OctaFuzz` · `expmixLine_v10` · `Counterfeit-V2.5_fp16` · `mechanicmix_v2` |
| `71543229` | `7PA` · `7PAG` · `7th_anime_v3_C` · `AOM3 A3` · `mouseymix` |

> **요지는 "모델을 비교하려면 프롬프트뿐 아니라 시드도 고정해야 한다" 는 것이다.**
> 지금도 파생 체크포인트를 비교할 때 같은 통제가 필요하다.

```text
설정 통제  DPM++ 2M Karras / 512x768 / Denoising 0.5
           Hires fix — R-ESRGAN 4x+ Anime6B, Upscale 1.5
           (글에 따라 CFG 9·Steps 30·Clip skip 1  또는  CFG 7·Steps 20·Clip skip 2·ENSD 1·Hires steps 10)
```

곁가지로 건질 것 — 네거티브에 **`cape` · `hat` · `hair ornament` · `coat` · `animal ears` · `twintails` 처럼
'원치 않는 요소' 를 직접 나열해 캐릭터 디자인을 고정**하는 방식이 쓰였다.
또 하나, 색 태그 사이에 `*//*` 구분자를 넣는 **당시 관행**이 보이는데 이는 지금 문법이 아니다.

→ 2023년 병합 배포글을 읽는 법은 위 '25-c' 절, 파생 체크포인트 비교는 [ANIMA](anima.md)


### ⚠ 같은 대회의 다른 글은 통제가 깨져 있었다 — VAE

**71970382** 도 같은 '레퍼런스걸' 출품작으로 모델 5종을 비교했다
(`anyhentai_18` · `abysshellmaple_v10` · `MIX-HIRES-V3` · `sparklingmix_v10` · `yarrrlmix_`, 각 모델마다 1000장씩 뽑아 선별).
공통 설정은 384x512 / Steps 20 / `DPM++ SDE Karras` / CFG 7 / Denoising 0.6 / Hires 2배 `R-ESRGAN 4x+ Anime6B` 로 잘 통제돼 있다.

**그런데 댓글이 문제를 짚었다.** 비교 이미지들의 색감이 약간씩 흐린 것 같다는 지적에 이어 —

> **"당신의 VAE 는 안녕하십니까?"**

**본문에 VAE 언급이 전혀 없고 EXIF 에도 VAE 필드 자체가 없다.** 색이 흐리고 채도가 낮은 것은
모델 차이가 아니라 **VAE 를 안 물려서** 생긴 현상일 가능성이 높고, 그렇다면 **이 비교는 통제가 깨진 것**이다.

**교훈은 시드 고정과 같은 무게다 — 모델을 비교할 때는 VAE 도 고정해야 하고, 남의 비교글을 읽을 때는 통제부터 확인해야 한다.**
(위 프로토콜 표에 한 줄을 더 붙인다: **VAE 고정 및 명시**.) → 이 문서의 'SDXL 아니메 VAE 가 hires 결과를 가른다' 항목

같은 대회의 **71687350**(에순이)은 `MIX-Pro-V4` · `abyssmaple_ver3` · `camelliamixLine_v10` · `7th_anime_v3_A` · `AOM3` 를
384x576 / Steps 25 / CFG 5 / Denoising 0.6 / Hires 2배 · Hires steps 10 · `4x-AnimeSharp` 로 통제해 돌렸다.
곁다리로 남은 관찰 — **눈 색을 검은색이 아니라 파란색으로 고른 이유는 당시 모델들이 `black eyes` 태그를 잘 못 잡았기 때문**이라고 밝혔다(위 항목의 관찰과 일치한다).

<small>근거 — [(레퍼런스걸) 설화 23.03](https://arca.live/b/aiart/71547451) · [(레퍼런스걸) 에순이 23.03](https://arca.live/b/aiart/71687350) · [(레퍼런스걸) 은적이 23.03](https://arca.live/b/aiart/71543229) · [(레퍼런스걸) 호박이 23.03](https://arca.live/b/aiart/71970382)</small>

## SDXL 아니메 VAE 가 hires 결과를 가른다 — Dpipe · B3 · XL_VAE_C · Andromeda
<small>2025-12 기준 · 근거 2건</small>

VAE 는 색감만 바꾸는 부품이 아니다. **hires 를 돌렸을 때 무엇이 달라지는지가 VAE 마다 다르다.**
같은 사람이 두 번(2025-08 · 2025-12) 같은 방법으로 비교한 자료가 있다 — **포토샵으로 두 이미지의 '차이' 를 뽑고, 보기 힘드니 '반전' 시키고, RGB 값을 더해 '흑백' 으로도** 뽑는 방식이다.

| VAE | 기본 해상도에서 | **hires 를 돌리면** |
|---|---|---|
| **Dpipe** (Anzhc Anime SDXL VAE DPipe Prototype) | 기준. 무난하다 | **색감을 최대한 유지한 채 디테일이 오르고 부드러움을 지킨다** — 글쓴이의 최종 선택 |
| **B3** (Anzhc Anime B3 VAE) | 채도가 진해지고 대비가 오르며 작은 부분의 선명도도 오른다 | **배경의 빈 영역이 파란색으로 약간 뜨고**, 색감까지 변하며 **흐려야 좋았을 부분까지 선명해진다** |
| **XL_VAE_C** (G10.2, 시빗) | 채도·대비가 올라 포토샵으로 샤픈을 먹인 느낌 | **좀 타 버린 느낌**이 들 정도 |
| **Andromeda** | Dpipe 와 비슷하나 색조가 약간 변하고 대비가 오른다 | 전체적으로 선명해져 **얼룩·무늬 같은 사소한 디테일이 변하고 머릿결이 더 선명**해지지만 **Dpipe 특유의 부드러움이 사라진다** |
| SDXL 기본 VAE | (비교에서 아예 제외했다) | |

```text
받는 곳  https://huggingface.co/Anzhc/Anzhcs-VAEs
파일     Anime SDXL VAE DPipe Prototype.safetensors
         MS DPipe fp32 112k Anime VAE SDXL.safetensors   (2025-08 글에서 특정된 이름)
```

- **B1/B3 는 채도 수준이 아니라 색 계열 자체가 조금 바뀌어 버려서** Dpipe 로 갈아탄 사용자가 여럿이다.
- 댓글의 절충안 하나 — **B3 같은 강한 VAE 는 쓰더라도 i2i 막단에만 넣겠다**는 활용법.
- 글쓴이 스스로 **그림체마다 차이 정도가 달라질 수 있으니 참고용**이라고 단서를 달았다.

### 곁가지 — 텍스트 인코더를 섞어 끼우기

155729515 본문 말미에 붙은 이야기다. **챈킨의 TE + 개선된 클립L 을 섞은 '짬뽕 TE'** 로 바꿔 다시 뽑으니
**디테일·인식능력·손가락이 전반적으로 좋아졌다**고 한다. 조합식은 댓글에서 밝혔다.

```text
챈킨 TE(L,G)  +  Anzhc L  +  시빗에서 주운 비교적 최신 캐릭이 나오는 모델의 TE(L,G)
→ 세 개를 동일 비율로 (본인도 정확히는 기억 안 난다는 단서 포함)
```

- **WebUI 기반에서도 되냐**는 질문에는 **ComfyUI 로 섞어서 모델째로 저장하면 다른 곳에서도 쓸 수 있다**고 답했다 → [ComfyUI 쓰는 법](comfyui.md)
- 한 사용자는 **Anzhc 허깅페이스의 CLIP L/G 를 이식했을 때는 깨졌고**(G 까지 병합해서일 수도) **챈킨 TE 를 이식하니 기본 TE 보다 낫게 나왔다**고 후기를 남겼다.

→ hires 자체는 [업스케일과 화질](upscale.md), 병합 시 VAE 소실은 이 문서의 '⚠️ 병합의 함정' 항목

<small>근거 — [Dpipe 랑 B3 vae 비교 25.08](https://arca.live/b/aiart/145608893) · [xl용 vae 2개비교 25.12](https://arca.live/b/aiart/155729515)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 251개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 채널의 모델·로라 배포글은 한 달 기한 링크나 만료된 클라우드 주소가 많아, 오래된 배포글은 링크가 죽어 있을 것을 전제하고 댓글의 대체 링크를 먼저 확인해야 한다 | 24 | 0 | 2022-12~2026-06 |
| 채널에 실제로 배포·공유된 프롬프트에서 걷어낸 오타 — `deep epentration` · `droped head` · `opend condom wrapper` · `large grithy veiny penis` · `hot temperutre` · `unsensored` · `engage ring` · `look at viewer` · `medium breast` · `stick out tongue` · `sconstricted pupils` · `hang electircguitar` · `ansurdly` · `glown` · `perfect feets` · `multiple view` · `gif rtifacts` · `extremly` · `intricated details` · `trannsexual` · `gradiant eyes` · `sterpiece` · `stlye` · `fusedears` · `auqa` · `baeball` · `aqua hairs` · `back graound` · `out doors` — 존재하지 않는 문자열은 조용히 무시될 뿐 비슷하게 해석해 주지 않는다 | 18 | 0 | 2022-11~2026-07 |
| 픽셀 업스케일러(`R-ESRGAN 4x+ Anime6B` · `4x-UltraSharp` · `4x-AnimeSharp`)의 hires denoise 는 0.35~0.7 로 넓게 쓰였고 하한이 없다 — 반면 2단 구성에서 2차로 도는 SD Upscale 단계는 0.1~0.4 로 낮게 잡는다 | 17 | 0 | 2023-01~2023-10 |
| 채널에는 배포 링크를 base64 로 인코딩해 올리는 관행이 있어, 뜻 없는 영문+숫자 덩어리가 보이면 base64 디코더에 넣으면 실제 주소(kio.ac · mega.nz 가 많다)가 나온다 | 12 | 0 | 2023-03~2026-06 |
| 2023년 A1111 에서는 Hires steps 를 본체 스텝의 절반 이하로 낮춰 시간을 아끼는 것이 관행이었다 — 본체 20~45 스텝에 hires 10~20 스텝을 준 사례가 아홉이다 | 9 | 0 | 2023-03~2023-10 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| Lumina-Image-2.0 계열(Illustrious-Lumina, Neta Lumina, Comradeship LU)은 2.6B DiT + 2B `gemma-2-2b` 텍스트 인코더 + FLUX.1 의 16채널 VAE 로 구성된 소형 DiT 아니메 모델로, 로컬 SDXL 모델과는 아예 다른 물건이다 | 8 | 0 | 2025-04~2025-07 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| Lumina 계열 모델은 텍스트 인코더에 소형 언어모델을 그대로 넣었기 때문에 프롬프트를 언어모델 지시문으로 시작해야 한다 — `You are an assistant designed to generate anime images based on textual prompts. <Prompt Start>` 형식이며, 네거티브도 `... low-quality images with lowest degree of aesthetics ... <Prompt Start>` 로 시작한다 | 6 | 0 | 2025-04~2025-07 |
| `more than two arm per body`·`more than five fingers on one hand`·`best ratio four finger and one thumb`·`5 fingers, hyper detailed fingers`·`clear boundaries of the arms` 처럼 팔·다리·손가락 개수를 영어 문장으로 비는 것은 2022~2023년의 대표적 미신 관용구이고 학습된 표현이 아니다 | 6 | 0 | 2022-12~2023-11 |
| Lumina 계열에서는 작가명 앞에 `@` 를 붙이고(예: `@as109`), 캐릭터는 작품명을 함께 넣는 것이 좋다(예: `mifune shioriko, love live!, love live! nijigasaki high school idol club`) | 6 | 0 | 2025-06~2025-07 |
| Lumina 계열은 소형인데도 생성 속도가 생각보다 느리고, 일부 FP16 환경에서 그림이 새까맣게만 나올 수 있다 | 6 | 0 | 2025-07~2025-11 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| 체크포인트마다 감당하는 최대 해상도가 다르다 — ILXL 1.X 공식 지원은 1536x1536, ComradeshipXL v14K 는 1536x1536 특화, v14K1A/v14K1AX 는 권장 1796x1796·최대 2048x2048, NoobAI 계열은 1280x1280 까지가 안전하며, 병합모델에서 1536x1536 이 이상하면 1408x1408 로 낮춘다 | 6 | 0 | 2025-02~2025-04 |
| UncannyValley·페르소나 스타일 계열처럼 DMD(Distribution Matching Distillation)가 체크포인트에 내장된 모델은 Sampling Steps 10~20, CFG scale 1.5~3, 샘플러 Euler a, 스케줄러 SGM Uniform 으로만 써야 하며 일반 모델 감각으로 CFG 7 을 넣으면 그림이 탄다 | 5 | 0 | 2025-01~2025-06 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| 2023-02 SD1.5 병합 대회 배포글들은 U-Net 블록 단위 병합을 썼다 — 25개 블록 각각에 소수 가중치를 주거나(multicolor.v2) 0/1 만 주어 특정 층을 통째로 한쪽 모델에서 가져오거나(Unico Bergamotto: `1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1` / Base alpha 0), LoRA 를 SuperMerger 로 뒤쪽 블록에만 얹는(Sita7taker: `헬테이커:0.1:(0,…,0,1,1,1,1,1)`) 방식이다. 지금 기준으로는 낡았고 시대 확인용이다 | 5 | 0 | 2023-02~2023-02 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |
| 채널에 올라오는 신규 모델 소식의 상당수는 제작사 주장·유출·LLM 요약이라 실사용 검증이 없다 | 5 | 0 | 2026-02~2026-07 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| SD1.5 병합 모델 배포글의 예시 EXIF 는 `medvram`·`xformers`·SD upscale 이 켜진 상태에서 뽑은 것이라 그대로 복사해도 결과가 다를 수 있다고 제작자들이 명시했다 — 그림체가 재현되지 않으면 예시 EXIF 를 그대로 한 번 돌려 보고 그것을 기준으로 프롬프트를 고치는 것이 당시 제작자의 표준 답이었다 | 5 | 0 | 2023-02~2023-03 |
| Lumina 계열은 다국어를 지원해 중국어·일본어가 되고 한국어도 어느 정도 되며(영어만큼은 아니다), 입력 토큰이 8192 로 추정될 만큼 넉넉해 프롬프트를 길게 써도 된다 | 5 | 0 | 2025-07~2025-07 |
| Comradeship LU(Neta Lumina) 계열의 권장 샘플러·CFG 는 버전마다 다르다 — v2T6·v2T12·v2T14 는 `res_multistep` / `linear_quadratic` / CFG 5.5 (20~29스텝)이고, v2T22·v2T25 는 `euler_ancestral` / `simple` / CFG 4~6 (20~30스텝)이다. 버전을 바꾸면 설정도 같이 바꿔야 한다 | 5 | 0 | 2025-06~2025-07 |
| 고해상도 특화 ComradeshipXL 계열의 버전별 스펙 — v14VX(NoobAI-XL-Vpred-1.0 기반, 권장 1536x1536 · 최대 1796x1796 · landscape 미지원, `Euler a / SGM Uniform / CFG 2.0 / 20스텝 / RescaleCFG Normal 0.7`), v14KC(ILXL 2.0 병합본 + NoobAI EPS 1.1 을 1:1 병합, 최소 25스텝 이상 · `CFG 3.5 / 1536x2048`), v14VW2(NoobAI 1.0 V-Pred + Rouwei 0.8 을 Karcher-merge 로 병합, `Euler a / SGM Uniform / CFG 2.0 / 20스텝 / 832x1216 / RescaleCFG 0.7 / ZeroSNR`), v14VWW(WAI 15 기반, 고속화 특성을 잃어 20~28스텝 · `Euler a / Beta / CFG 3.5 / 1024x1536 / RescaleCFG OFF / ZeroSNR ON`). 전부 V-pred 라 reForge·Forge·ComfyUI 가 필요하다 | 4 | 0 | 2025-04~2025-09 |
| v-pred(v-prediction) 모델은 A1111 dev 브랜치·reForge·ComfyUI 에서만 돌아가고 구버전 A1111 정식판에서는 쓸 수 없다 | 4 | 0 | 2025-02~2025-09 |
| `.ckpt` 와 `.safetensors` 는 담긴 내용이 같고 **safetensors 는 악성코드가 실행될 수 없는 더 안전한 컨테이너 형식일 뿐**이라 용량·성능과는 무관하다. 체크포인트 용량을 좌우하는 것은 **fp16 여부와 EMA 가중치 포함 여부**다 — 7GB 짜리는 EMA 약 3GB + fp32 가중치 약 4GB 구성이고, fp32→fp16 으로 바꾸면 4~5GB, 거기서 EMA 까지 떼면 2GB 가 된다(EMA 를 뗀 모델을 pruned 라 부른다). 그림 생성·병합·LoRA 사용에 EMA 는 필요 없다 | 4 | 0 | 2023-01~2023-03 |
| 설정 > Comfy > Nodes 2.0 > 모던 노드 디자인을 켜면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다 | 4 | 0 | 2026-05~2026-08 |
| 그림체 LoRA 는 베이스 모델을 바꿔 가며 평가해야 한다 — Unstable 로라 제작자는 NTR xiii 한 모델에서만 테스트해 결과가 목표에 못 미친 원인을 확정하지 못했다 | 4 | 0 | 2023-02~2026-07 |
| 모델이 diffusion model 단독으로 배포되면 models/checkpoints 가 아니라 models/diffusion_models 에 넣고 Load Diffusion Model 계열 노드로 불러야 하며, 텍스트 인코더와 VAE 도 각각 models/text_encoders, models/vae 에 따로 넣어 연결해야 한다 | 4 | 0 | 2026-05~2026-08 |
| MiniMax H3 는 RTX 3060 12GB + RAM 32GB 급 환경에서도 구동된다 | 4 | 0 | 2026-07~2026-08 |
| 2023년 채널 자작 병합 모델의 상당수는 제작자가 병합 비율을 기록해 두지 않아 재현이 불가능하다 — `mixedmixedmixed v2`·`ExpMix`·`NGMix`·`JamminMK6` 배포글이 모두 '마구잡이로 넣어서 정확히 기억나지 않는다'고 적었다. 레시피가 남지 않은 배포글은 파일을 받아 쓰는 것 말고는 할 수 있는 것이 없다 | 4 | 0 | 2023-02~2023-03 |
| Neta Lumina 계열은 베이스 모델의 손가락·발가락 타율이 나쁘고 공개된 모델들의 지식 폭이 예상보다 깊지 않아, 대규모 추가 학습이 없다면 당분간 '가난한 자의 NAI4' 에 머무를 가능성이 높다고 병합자 본인이 평했다 — 극한으로 튜닝된 아니메 SDXL 모델보다 밀릴 수 있다 | 4 | 0 | 2025-06~2025-07 |
| SDXL/Illustrious 결과물이 탁하거나 흰 점이 찍히면 VAE Select 값을 2로 두어 별도 VAE(fixFP16ErrorsSDXLLowerMemoryUse_v10)를 적용한다 | 4 | 0 | 2026-06~2026-08 |
| int8convrot 양자화는 fp8 tensorwise 보다 품질이 좋고(Q8_0 급) 조금 빠르며, 캘리브레이션이 필요 없어 대세가 된다 | 4 | 0 | 2026-07~2026-08 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [그록 빌드 검열없을때 퍼먹으시오](https://arca.live/b/aiart/172435010) — 2026-06, 추천 175
- [도시 배경 특화 U-Net 기반 자작 병합 모델 HighRiseMixV1 공유](https://arca.live/b/aiart/69302021) — 2023-02, 추천 83
- [한복 로라 다시 만들어왔음](https://arca.live/b/aiart/69505242) — 2023-02, 추천 64
- [모델공유) 반실사 병합모델 ZemiHR](https://arca.live/b/aiart/74030139) — 2023-04, 추천 58
- [[병합대회] MIX-Pro-V4_Beta](https://arca.live/b/aiart/70413762) — 2023-02, 추천 57
- [CamelliaMIx_V2 모델 업데이트](https://arca.live/b/aiart/71600989) — 2023-03, 추천 52
- [모델공유) 병합모델 CamelliaMix_2.5D](https://arca.live/b/aiart/71331822) — 2023-03, 추천 50
- [낙서 스타일 LoRA](https://arca.live/b/aiart/73263468) — 2023-04, 추천 49
- [모델공유) ExpMix_Extra](https://arca.live/b/aiart/73792400) — 2023-04, 추천 48
- [모델공유) 병합모델 CamelliaMix_Line](https://arca.live/b/aiart/71144590) — 2023-03, 추천 47
- [[레퍼런스걸] 싸이버거 걸고 대회 한번 열어봄](https://arca.live/b/aiart/71483615) — 2023-03, 추천 47
- [Comfyui portable v0.30.0 + sage 외 여러가지.](https://arca.live/b/aiart/178800540) — 2026-08, 추천 47
- [응애 뉴비가 설명하는 AI모델의 개념](https://arca.live/b/aiart/119613811) — 2024-10, 추천 46
- [Uncanny valley noob 3d v1 DMD 출시](https://arca.live/b/aiart/126726445) — 2025-01, 추천 45
- [뉴비들은 webui neo 쓰자](https://arca.live/b/aiart/176802949) — 2026-07, 추천 44
- [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들](https://arca.live/b/aiart/179458112) — 2026-08, 추천 44
- [모델공유) ExpMix_Line](https://arca.live/b/aiart/70608629) — 2023-02, 추천 43
- [[병합모델공유] OBNMix_V1](https://arca.live/b/aiart/125081627) — 2024-12, 추천 43
- [ExpMix_Line_V2 모델 업데이트](https://arca.live/b/aiart/70802971) — 2023-02, 추천 42
- [[v7] 작가명 태그 재현을 목적으로 하는 Noob v-pred 1.0 2d기반 모델](https://arca.live/b/aiart/138768269) — 2025-06, 추천 42
- [[v6] 작가명 태그 재현을 목적으로 하는 Noob v-pred 1.0 2d기반 모델](https://arca.live/b/aiart/131849412) — 2025-03, 추천 40
- [anima2.9b 출시](https://arca.live/b/aiart/179710466) — 2026-08, 추천 40
- [코랩 AI그림 실전압축 레퍼런스](https://arca.live/b/aiart/72672264) — 2023-03, 추천 39
- [[병합 대회] colormixed](https://arca.live/b/aiart/69730929) — 2023-02, 추천 38
- [앞으로 출시될 로컬 이미지 모델 NewBie-AI](https://arca.live/b/aiart/154900388) — 2025-11, 추천 38
- [최근 AI 그림 자주 묻는 질문 (26년 5월 기준)](https://arca.live/b/aiart/170655900) — 2026-05, 추천 38
- [약속대로 병합모델 공유: moomix4](https://arca.live/b/aiart/76635524) — 2023-05, 추천 37
- [[레퍼런스걸] 핑핑이 (약 장문 주의)](https://arca.live/b/aiart/71521039) — 2023-03, 추천 36
- [[병합모델] C-Moon SD 공유](https://arca.live/b/aiart/73744147) — 2023-04, 추천 36
- [[v3] 2d 이미지 생성을 위한 noob v-pred 단순병합모델](https://arca.live/b/aiart/128832358) — 2025-02, 추천 36
- [comfyui portable v0.20.1 + sage + triton.](https://arca.live/b/aiart/169293039) — 2026-04, 추천 36
- [애니메 3D 스타일 병합모델 공유](https://arca.live/b/aiart/142309559) — 2025-07, 추천 35
- [모델공유) 병합모델 CamelliaMix](https://arca.live/b/aiart/70982910) — 2023-03, 추천 34
- [UncannyValley ilxl1.0+noob 출시](https://arca.live/b/aiart/128930860) — 2025-02, 추천 34
- [[모델공유] Addillustri v10 v-pred(ILXL병합모델)](https://arca.live/b/aiart/129841057) — 2025-02, 추천 34
- [Qwen-Image-Edit-2511 vs FireRed-Image-Edit](https://arca.live/b/aiart/162479433) — 2026-02, 추천 34
- [MiniMax H3 int8convrot Video VAE 올라옴](https://arca.live/b/aiart/179114541) — 2026-08, 추천 34
- [ExpMix_LIne_V3 모델 업데이트](https://arca.live/b/aiart/76462452) — 2023-05, 추천 33
- [(추가) 대부분의 작가명 태그 재현이 가능한 Noob v-pred 기반 모델](https://arca.live/b/aiart/128899435) — 2025-02, 추천 33
- [Anything + Stable Diffusion + f222(twam) 병합 모델 비교](https://arca.live/b/aiart/64965428) — 2022-12, 추천 32
- [#개인 병합 모델 공유 - JINMODEL_v7.5](https://arca.live/b/aiart/170224006) — 2026-05, 추천 32
- [모델공유) 병합모델 ExpMix 입니다.](https://arca.live/b/aiart/70434894) — 2023-02, 추천 31
- [처음으로 만든 병합모델입니다.](https://arca.live/b/aiart/72369910) — 2023-03, 추천 31
- [[미니 정보] 26년 5월 기준 간단하게 소개하는 그림 AI 모델들](https://arca.live/b/aiart/169601993) — 2026-05, 추천 31
- [[병합대회] Kawaii 2D](https://arca.live/b/aiart/70627117) — 2023-02, 추천 30
- [병합모델 Xtracolor.v18 배포](https://arca.live/b/aiart/70825950) — 2023-02, 추천 30
- [[v2] 2d 이미지 생성을 위한 noob v-pred 단순병합모델](https://arca.live/b/aiart/128005836) — 2025-02, 추천 30
- [응애를 위한 AI 그림 모델 선택 가이드 (2025/05)](https://arca.live/b/aiart/136531062) — 2025-05, 추천 30
- [PodoMIX_XL 공유](https://arca.live/b/aiart/128806467) — 2025-02, 추천 29
- [UncannyValley V-pred v1 출시](https://arca.live/b/aiart/140017939) — 2025-06, 추천 29
- [그래서 vae는 뭐 쓰면 돼요?](https://arca.live/b/aiart/68299849) — 2023-01, 추천 28
- [[병합대회] Sita7taker](https://arca.live/b/aiart/70499026) — 2023-02, 추천 28
- [병합모델 RoseMIX_XL_V1 공유](https://arca.live/b/aiart/126129697) — 2025-01, 추천 28
- [페르소나 스타일 Noob xl모델 출시](https://arca.live/b/aiart/127345203) — 2025-01, 추천 28
- [LimeMIX_XL 공유](https://arca.live/b/aiart/133867786) — 2025-04, 추천 28
- [Anima) flat 그림체 로라 공유](https://arca.live/b/aiart/175209258) — 2026-06, 추천 28
- [ZemiHR_V2 모델 업데이트](https://arca.live/b/aiart/75017141) — 2023-04, 추천 27
- [henmix_2.5d v2 업데이트](https://arca.live/b/aiart/75260114) — 2023-04, 추천 27
- [Treebark 경량화 허깅페이스 링크](https://arca.live/b/aiart/67648642) — 2023-01, 추천 26
- [개인 병합 모델 공유 idkwiMIX](https://arca.live/b/aiart/69875937) — 2023-02, 추천 26
- [모델공유)Lora 병합모델 빅토리안 믹스 개선?버전](https://arca.live/b/aiart/71147882) — 2023-03, 추천 26
- [[병합모델공유] OBNMix_V1.5](https://arca.live/b/aiart/125277703) — 2025-01, 추천 26
- [병합모델 CherryMIX_XL_V2 공유](https://arca.live/b/aiart/126129327) — 2025-01, 추천 26
- [[v5] 작가명 태그 재현을 목적으로 하는 Noob v-pred 1.0 2d기반 모델](https://arca.live/b/aiart/129843355) — 2025-02, 추천 26
- [[모델공유] FuzzyLune](https://arca.live/b/aiart/133525011) — 2025-04, 추천 26
- [개인병합 모델 세팅 공유](https://arca.live/b/aiart/149889901) — 2025-10, 추천 26
- [Krea에서 직접 Krea2 아니메 파인튜닝을 진행할 가능성이 있습니다](https://arca.live/b/aiart/175561117) — 2026-07, 추천 26
- [[병합대회]CreamLike_A,B](https://arca.live/b/aiart/69662750) — 2023-02, 추천 25
- [병합모델공유 N40NAillousV2-xl](https://arca.live/b/aiart/121889356) — 2024-11, 추천 25
- [페르소나 스타일 ilxl1.0+noob 출시](https://arca.live/b/aiart/129087107) — 2025-02, 추천 25
- [Persona Style noob v1.5 출시](https://arca.live/b/aiart/139354250) — 2025-06, 추천 25
- [Anima의 사례가 Z-Image를 더욱 기대하게 만드는 이유](https://arca.live/b/aiart/161187637) — 2026-02, 추천 25
- [Anima-Preview 고속화 병합모델 Anima-Comradeship v1T7 공유](https://arca.live/b/aiart/163306203) — 2026-02, 추천 25
- [Comfyui portable v0.23.0 + sage + grok i2v 외 여러가지](https://arca.live/b/aiart/172596107) — 2026-06, 추천 25
- [체크포인트 카탈로그(12개 모델 비교)](https://arca.live/b/aiart/68725324) — 2023-01, 추천 24
- [병합 mixedmixedmixed v2 라능...](https://arca.live/b/aiart/69423609) — 2023-02, 추천 24
- [[모델공유] FuzzyEclipse](https://arca.live/b/aiart/129333797) — 2025-02, 추천 24
- [Anima-Preview 고속화 병합모델 Anima-Comradeship v1T8 공유](https://arca.live/b/aiart/163971242) — 2026-03, 추천 24
- [개인적인 Anima+IL 워크플로우 세트 구성품 추천](https://arca.live/b/aiart/169680210) — 2026-05, 추천 24
- [[병합대회] BACLA-MIX](https://arca.live/b/aiart/69704838) — 2023-02, 추천 23
- [개인병합 모델, 로라모음 공유함](https://arca.live/b/aiart/72576924) — 2023-03, 추천 23
- [병합모델공유 NNGMIXv4.2-XL](https://arca.live/b/aiart/134980776) — 2025-04, 추천 23
- [Anima에서 사용할 수 있는 DMD2 LoRA](https://arca.live/b/aiart/164898297) — 2026-03, 추천 23
- [Krea2 대형 단부루 학습 로라 사용 후기](https://arca.live/b/aiart/178556661) — 2026-07, 추천 23
- [Neta-Lumina 기반 병합모델 Comradeship LU v2T12 공유](https://arca.live/b/aiart/141311244) — 2025-07, 추천 22
- [Anima GGUF 양자화 모델](https://arca.live/b/aiart/161385741) — 2026-02, 추천 22
- [1분 넘는 영상을 고속으로 뽑는 Helios 모델 출시](https://arca.live/b/aiart/163968817) — 2026-03, 추천 22
- [모델 컨버터 사용법(모델 용량 줄이는 법)](https://arca.live/b/aiart/69024846) — 2023-02, 추천 21
- [[병합대회] 오랜지 0%, 파스텔 0% multicolor.v2](https://arca.live/b/aiart/69573598) — 2023-02, 추천 21
- [[병합대회] Unico Bergamotto](https://arca.live/b/aiart/69648477) — 2023-02, 추천 21
- [[레퍼런스걸] 설화](https://arca.live/b/aiart/71547451) — 2023-03, 추천 21
- [Illustrious XL 3.6 소개글에 대해서 분석해보는 시간?](https://arca.live/b/aiart/142556834) — 2025-07, 추천 21
- [고해상도 생성용 ilxl 1.1 병합모델 ComradeshipXL v14K1A 모델 공유](https://arca.live/b/aiart/132177025) — 2025-03, 추천 20
- [Dpipe 랑 B3 vae 비교](https://arca.live/b/aiart/145608893) — 2025-08, 추천 20
- [알리바바에서 딸내미 하나 샀음 (happy horse 1.0 출시)](https://arca.live/b/aiart/169030124) — 2026-04, 추천 20
- [기초) 모델들 용량 줄이는 방법 (병합 활용 7GB->4GB)](https://arca.live/b/aiart/68966157) — 2023-02, 추천 19
- [noob v-pred 모델의 2d 위주 이미지 생성을 위한 단순 병합 모델](https://arca.live/b/aiart/127549205) — 2025-01, 추천 19
- [FLUX.1-Kontext-dev 가중치 공개 및 간단한 ComfyUI 테스트](https://arca.live/b/aiart/140754531) — 2025-06, 추천 19
- [Anima Base / novaAnime / wai 화풍 비교](https://arca.live/b/aiart/172910863) — 2026-06, 추천 19
- [고해상도용 병합모델 ComradeshipXL v14KC 모델 공유](https://arca.live/b/aiart/134594033) — 2025-04, 추천 18
- [V-Pred 병합모델 ComradeshipXL v14VW2 모델 공유](https://arca.live/b/aiart/138326689) — 2025-05, 추천 18
- [로컬 농사꾼을 위한 체크포인트 추천](https://arca.live/b/aiart/151588509) — 2025-10, 추천 18
- [comfyui portable v0.11.1 + sage + triton.](https://arca.live/b/aiart/161206430) — 2026-02, 추천 18
- [웹툰로라) 한예나](https://arca.live/b/aiart/164851217) — 2026-03, 추천 18
- [아니마튜닝된 2d vae](https://arca.live/b/aiart/175945729) — 2026-07, 추천 18
- [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minimax H3)](https://arca.live/b/aiart/178537097) — 2026-07, 추천 18
- [[병합대회]WhiteSpace Prism 병합모델](https://arca.live/b/aiart/70623701) — 2023-02, 추천 17
- [자작) 병합모델 MareColoris](https://arca.live/b/aiart/70994766) — 2023-03, 추천 17
- [ilxl 1.0 병합모델 ComradeshipXL v14K / v14K2 모델 공유](https://arca.live/b/aiart/129171018) — 2025-02, 추천 17
- [ILXL 1.0 병합모델 ComradeshipXL v14K3 모델 공유](https://arca.live/b/aiart/129497774) — 2025-02, 추천 17
- [병합모델공유 NNGMIXv4.1-XL](https://arca.live/b/aiart/134463563) — 2025-04, 추천 17
- [WAI 15 기반 V-pred 병합모델 ComradeshipXL v14VWW 모델 공유](https://arca.live/b/aiart/146874458) — 2025-09, 추천 17
- [Gemini Omni를 소개합니다.](https://arca.live/b/aiart/171183268) — 2026-05, 추천 17
- [ComfyOrg 공식모델들에 int8convrot 추가됨](https://arca.live/b/aiart/175519662) — 2026-07, 추천 17
- [병합모델 [ RoyaleEngine-V0.98 ] 공유. 경량화 모델도 추가.](https://arca.live/b/aiart/72714918) — 2023-03, 추천 16
- [고해상도 생성용 병합모델 ComradeshipXL v14K1AX 모델 공유](https://arca.live/b/aiart/132553722) — 2025-03, 추천 16
- [ComfyUI용 Qwen Image Edit 초기 지원 시작](https://arca.live/b/aiart/145582528) — 2025-08, 추천 16
- [28일 시작 뉴비 모델병합해봄](https://arca.live/b/aiart/71208752) — 2023-03, 추천 15
- [[레퍼런스걸] 은적이](https://arca.live/b/aiart/71543229) — 2023-03, 추천 15
- [[레퍼런스걸] 에순이](https://arca.live/b/aiart/71687350) — 2023-03, 추천 15
- [Illustrious-Lumina-v0.03 병합모델 Comradeship LU v1T2 모델 공유](https://arca.live/b/aiart/134430978) — 2025-04, 추천 15
- [Neta Lumina Alpha용 Comradeship LU v2T1KIT LoRA 공유](https://arca.live/b/aiart/140558851) — 2025-06, 추천 15
- [Neta-Lumina 기반 병합모델 Comradeship LU v2T18 공유](https://arca.live/b/aiart/141964528) — 2025-07, 추천 15
- [Neta Lumina 1.0 기반 병합모델 Comradeship LU v2T22 공유](https://arca.live/b/aiart/143116958) — 2025-07, 추천 15
- [NoobAI 기반 병합모델 ComradeshipXL v14F 모델 공유](https://arca.live/b/aiart/151922549) — 2025-10, 추천 15
- [MiniMax-H3 오픈웨이트 모델의 출시일이 공개](https://arca.live/b/aiart/178585330) — 2026-07, 추천 15
- [Neta-Lumina 기반 병합모델 Comradeship LU v2T14 공유](https://arca.live/b/aiart/141472508) — 2025-07, 추천 14
- [Flux.2-Klein-4B 사용기 (뭘 할 수 있는가)](https://arca.live/b/aiart/160707593) — 2026-01, 추천 14
- [Z Image 는 태그도 인식함](https://arca.live/b/aiart/160874039) — 2026-01, 추천 14
- [LTX-2.3 영상모델 출시](https://arca.live/b/aiart/164020977) — 2026-03, 추천 14
- [Nanosaur-1.2B-Preview](https://arca.live/b/aiart/166944946) — 2026-04, 추천 14
- [Neta Lumina 기반 병합모델 Comradeship LU v2T25 공유](https://arca.live/b/aiart/143596900) — 2025-07, 추천 13
- [(오픈소스 아님 확정) 새로운 SOTA급 T2V/I2V 모델 HappyHorse 출시예정](https://arca.live/b/aiart/167106042) — 2026-04, 추천 13
- [ChatGPT Images 2.0을 소개합니다!](https://arca.live/b/aiart/168399124) — 2026-04, 추천 13
- [스압) krea2, 아니마, ilxl 비교](https://arca.live/b/aiart/176897194) — 2026-07, 추천 13
- [Neta Lumina 기반 고속화 병합모델 Comradeship LU v2 FINAL FAST 공유](https://arca.live/b/aiart/155089645) — 2025-11, 추천 12
- [xl용 vae 2개비교](https://arca.live/b/aiart/155729515) — 2025-12, 추천 12
- [HD-22](https://arca.live/b/aiart/74124808) — 2023-04, 추천 11
- [여러가지 Comradeship 병합모델 3개 공유](https://arca.live/b/aiart/140944045) — 2025-06, 추천 9
- [넓은 의미의 체크포인트와 좁은 의미의 체크포인트](https://arca.live/b/aiart/170230261) — 2026-05, 추천 9
- [nvidia에서 cosmos3 출시했네.](https://arca.live/b/aiart/172423630) — 2026-06, 추천 9
- [그록과 시댄스2.0 영상 비교](https://arca.live/b/aiart/172854969) — 2026-06, 추천 9
- [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부 공개](https://arca.live/b/aiart/178717529) — 2026-08, 추천 9
- [저번에 올렸던 모델 수정버젼과 두번째 모델 공유!](https://arca.live/b/aiart/71308838) — 2023-03, 추천 8
- [Bernini (비디오 omni 모델) Comfy에 곧 PR될 것으로 보임](https://arca.live/b/aiart/172591568) — 2026-06, 추천 8
- [[anima] 원본+int8 convrot 모델 3종 비교](https://arca.live/b/aiart/177372687) — 2026-07, 추천 8
- [VAE별 이미지 차이](https://arca.live/b/aiart/62060325) — 2022-11, 추천 7
- [(ILXL 1.0과 ILXL 0.1의 차이값 + noob모델) 로 1152*2016 해상도 테스트](https://arca.live/b/aiart/128849512) — 2025-02, 추천 7
- [Chroma 병합모델 Comradeship CR v1T4-33 모델 공유](https://arca.live/b/aiart/138501441) — 2025-06, 추천 7
- [Chroma 병합모델 Comradeship CR v1T21 모델 공유](https://arca.live/b/aiart/145366717) — 2025-08, 추천 7
- [바이두산 8b모델 ERNIE-Image](https://arca.live/b/aiart/167779972) — 2026-04, 추천 7
- [아니마와 Qwen3.5](https://arca.live/b/aiart/170079773) — 2026-05, 추천 7
- [ComfyUI int4convrot 지원](https://arca.live/b/aiart/176403272) — 2026-07, 추천 7
- [재밌는 비디오 제네레이션 모델 나왔네.](https://arca.live/b/aiart/176717035) — 2026-07, 추천 7
- [Gemini Omni Flash vs Minimax-H3](https://arca.live/b/aiart/178630221) — 2026-08, 추천 7
- [Chroma 병합모델 Comradeship CR v1T7-35DC 모델 공유](https://arca.live/b/aiart/138969996) — 2025-06, 추천 6
- [[anima] 아사나기 그림체 로라 2종+작가 태그 테스트](https://arca.live/b/aiart/172194583) — 2026-05, 추천 6
- [ComfyUI에서 Mage Flow 공식 지원 시작했네.](https://arca.live/b/aiart/178320979) — 2026-07, 추천 6
- [Kroma 0.2 간단 사용 후기](https://arca.live/b/aiart/179438130) — 2026-08, 추천 6
- [V4 정출판은 NSFW에서 그림체 안 무너지는듯](https://arca.live/b/aiart/130237851) — 2025-03, 추천 5
- [고해상도 생성용 병합모델 ComradeshipXL v14VX 모델 공유](https://arca.live/b/aiart/132946028) — 2025-04, 추천 5
- [와씨 쓰던 워크플로우 개조해서 Z-Image 모델용으로 개조하는데 성공했다 ㅅㅂ](https://arca.live/b/aiart/160774868) — 2026-01, 추천 5
- [Google의 Veo 3.2 유출](https://arca.live/b/aiart/163312367) — 2026-02, 추천 5
- [Zeta-Chroma 올해 중반쯤에는 나올 듯?](https://arca.live/b/aiart/167731791) — 2026-04, 추천 5
- [[레퍼런스걸] 호박이](https://arca.live/b/aiart/71970382) — 2023-03, 추천 4
- [[공유 종료] moomix20 : stupid](https://arca.live/b/aiart/77392210) — 2023-05, 추천 4
- [Chroma 병합모델 Comradeship CR v1T7-34DC 모델 공유](https://arca.live/b/aiart/138621473) — 2025-06, 추천 4
- [핸드폰에서도 3초만에 이미지 편집을? 0.39B 크기를 자랑하는 DreamLite를 소개합니다.](https://arca.live/b/aiart/171398852) — 2026-05, 추천 4
- [dual_personality 모델 업데이트](https://arca.live/b/aiart/71611067) — 2023-03, 추천 3
- [Lance: ByteDance의 통합 다중 모드 모델 (생성·편집·영상)](https://arca.live/b/aiart/171096415) — 2026-05, 추천 3
- [첸돚거 그림체 커스텀+기타 개인 설정세팅값 자료](https://arca.live/b/aiart/174789689) — 2026-06, 추천 3
- [Mage Flow Edit 간단 후기](https://arca.live/b/aiart/178550271) — 2026-07, 추천 3
- [ComfyUI - 다양한 워크플로우를 써 본 소감과 활용방법.](https://arca.live/b/aiart/160605007) — 2026-01, 추천 2
- [병합하는 방법은 공지 없음??](https://arca.live/b/aiart/70241791) — 2023-02, 추천 0
- [아니마 지금 많이 괜찮은 편인가요?](https://arca.live/b/aiart/171581384) — 2026-05, 추천 0
- [다들 아니마 체크포인트 뭐 씀](https://arca.live/b/aiart/178971620) — 2026-08, 추천 0
- [뉴비 꼭 pony할 필욘 없지?](https://arca.live/b/aiart/179433132) — 2026-08, 추천 0
