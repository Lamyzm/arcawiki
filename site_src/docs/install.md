# 설치와 환경 구성

> **원문 87건 → 이 문서 하나** · 주장 270개 · 정리 2026-08-14

**명령어와 경로를 그대로 실은 문서다.** 위에서부터가 지금(2026-08) 방식이고, 아래로 갈수록 옛 방식이며 시점을 밝혀 두었다.
어느 갈래를 고를지는 [처음이라면](overview.md) 의 그래픽카드 표를 먼저 보고 정한다.
설치 중 막히면 이 문서의 '흔한 실패' 표와 [오류 해결](troubleshooting.md) 을 본다.

## ⚠ 먼저 읽기 — 공식 홈의 노란 버튼은 '데스크탑 앱'이고, 채널은 '포터블' 기준이다
<small>2026-05 기준 · 근거 2건</small>

**입문자와 조언자 사이에 말이 안 통하는 가장 흔한 원인이 이것이다.**

채널 사람들은 대부분 ComfyUI **포터블(독립 실행형)** 기준으로 설명하는데, 공식 홈페이지를 통해 들어온 사람은 **데스크탑 앱**을 쓰고 있다. 둘은 화면과 폴더 구조가 서로 달라서, 같은 말을 해도 서로 다른 것을 보고 있게 된다 (170235453, 2026-05).

| | 데스크탑 앱 | 포터블 |
|---|---|---|
| 받는 곳 | 공식 홈 `Download Local` 의 **큼직한 노란 버튼** | 그 **옆 버튼** → ComfyUI 깃허브 → **Releases 목록** → 사양에 맞는 **7z** |
| 형태 | 설치형 | 압축 해제형, 한 폴더에 전부 |
| 채널 조언 | 화면·경로가 달라 잘 안 맞는다 | **그대로 통한다** |
| 업데이트 | 안정 위주 | 베타 위주라 최신 반영이 빠르다 |

> **함정 1** — 노란 버튼을 누르면 포터블이 아니라 **설치형 데스크탑 앱**이 깔린다.
> **함정 2** — 깃허브 첫 화면에 보이는 AMD·Intel·RTX 20 시리즈용 링크는 **최신 버전이 아니다.** 스크롤을 올려 **릴리스 목록**으로 들어가 아래로 내려야 최신 7z 이 있다.
> **함정 3** — 공식 포터블은 완전한 **바닐라**라 `Sage-Attention` 과 그 짝인 `triton` 을 직접 깔아야 하는데, 버전을 미리 맞춰 보지 않고 깔면 말썽이 난다. **채널 사람들이 배포하는 통합본**을 받는 편이 낫다 → 아래 'B. ComfyUI 포터블 통합팩'

원문 작성자의 평가: 앱 버전은 가볍게 그림을 뽑기엔 나쁘지 않지만 **확장성이 떨어지고, 어설픈 한글화 때문에 중요한 항목을 지나치기 쉬워** 한국인 사용자에겐 오히려 혼란스럽다. (한 글에서만 언급된 견해다.)

**구버전이 무조건 나쁜 것도 아니다.** 최신 판에서 말썽을 부리는 노드가 있으면 구버전에서 작업하는 편이 나은 경우가 있다 — 실제로 0.15.1 판은 배포자 스스로 "커스텀 노드 충돌이 크니 0.11.1 도 함께 쓰라"고 병행 배포했다.

→ 어느 갈래를 고를지는 바로 아래 표에서


<small>근거 — [컴피 공홈에서 포터블 버전 받는 방법. 26.05](https://arca.live/b/aiart/170235453) · [comfyui portable v0.15.1 + sage +… 26.02](https://arca.live/b/aiart/163592169)</small>

## 0. 세 갈래 중 하나만 고른다
<small>2026-08 기준 · 근거 4건</small>

| 갈래 | 누구에게 | 한 줄 |
|---|---|---|
| **A. Forge Neo + ANIMA** | 그림만 뽑을 사람, 노드가 싫은 사람 | python 3.13.12 → `git clone --branch neo` → `webui-user.bat` 두 줄 편집 |
| **B. ComfyUI 포터블 통합팩** | 영상·업스케일·인페인팅까지 할 사람 | 압축을 풀고 컨트롤넷·체크포인트만 따로 받으면 끝 |
| **C. comfy-cli 직접 구성** | 컴파일·cuda 경로가 꼬였을 때 스스로 해결할 사람 | `uv` 로 cuda 13.2 / python 3.13 / torch 2.12 를 직접 맞춘다 |

뉴비 권고는 A 다 — 원문 176802949 는 "뉴비들은 webui neo 쓰자" 를 제목으로 걸고, 설치가 어려우면 **StabilityMatrix** 로 딸깍하라고 덧붙인다.

<small>근거 — [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089)</small>

## A0. 가장 짧은 길 — ComfyUI-Easy-Install 로 첫 그림까지 (2026-02)
<small>2026-02 기준 · 근거 2건</small>

입문 10일차가 쓴 **설치부터 첫 그림까지의 최단 경로**다. 아무것도 모르는 사람이 하루 만에 '일단 되게' 만드는 것이 목적이라, 지금 채널에 있는 것 중 **가장 완결된 입문 경로**다 (163532702, 2026-02, 추천 42).

**1) 설치** — zip 을 받아 **C: 또는 D: 드라이브 바로 아래**에 푼다 (경로에 한글 금지).

```
https://github.com/Tavris1/ComfyUI-Easy-Install/releases/download/2.02.5/ComfyUI-Easy-Install.zip
```

안에 있는 설치 배치 파일을 실행하면 도스창이 뜨고 알아서 설치된다. 끝나면 폴더에 실행 파일이 생기고 **바탕화면에 바로가기 3개**가 만들어진다. 그중 실행 버튼을 누르면 도스창과 함께 ComfyUI 웹 화면이 열린다.

**2) 워크플로 불러오기** — 채널에 `(EXIF)` 라고 표기된 이미지는 **그 이미지 자체가 워크플로 정보를 품고 있다**는 뜻이다.

1. 이미지를 **새 탭에서 열고** 우클릭 → 다른 이름으로 저장
2. 받은 파일을 **ComfyUI 화면에 드래그&드롭** → 워크플로가 열린다
3. **'누락된 노드' 경고창**이 뜨면 닫는다
4. 오른쪽 위 **매니저** → `Install Missing Custom Nodes` → **전체 체크** → `Install`
5. 끝나면 `Restart`, 도스창이 진정되면 **F5**

남의 워크플로를 쓸 때마다 이 절차를 그대로 반복하면 된다.

**아직 받아 둔 워크플로 이미지가 없다면** — ComfyUI 는 처음 켜면 기본 워크플로가 이미 떠 있다.
그것만으로도 3)·4) 를 그대로 진행할 수 있으니, 남의 워크플로는 첫 장을 뽑아 본 뒤에 가져와도 늦지 않다.
채널에서 고를 때는 제목에 `(EXIF)` 가 붙고 **추천이 붙은 최근 글**부터 보는 것이 안전하다 —
오래된 워크플로는 지금 없는 노드를 쓰는 경우가 많다.

**3) 모델 넣기**

```
# 체크포인트
D:\ComfyUI-Easy-Install\ComfyUI\models\checkpoints
# 로라
D:\ComfyUI-Easy-Install\ComfyUI\models\loras
```

**모델은 어디서 받나** — 이 글은 파일을 이미 갖고 있다고 보고 넘어가지만, 처음이면 여기서 막힌다.
받는 곳과 무엇을 고를지는 [자원 — 받는 곳 모음](resources.md)과 [모델 고르기](models.md)에 있다.
2026-08 기준으로 처음 받을 것은 둘 중 하나다.

| 쓰려는 것 | 받을 파일 |
|---|---|
| **ANIMA** (2026년 채널 기본) | `anima-base-v1.0.safetensors` + `qwen_3_06b_base.safetensors` + `qwen_image_vae.safetensors` |
| **Illustrious 계열** | `WAI-illustrious-SDXL` |

**실제로 처음 검증할 때는 ANIMA 쪽이 더 쉽다.** 이유는 간단하다 — 세 파일이 모두 **공식 Hugging Face 직링크**로 바로 받아지고, Civitai 쪽처럼 로그인·연령·필터에 막힐 가능성이 적다.
즉 **"설치가 됐는지 지금 당장 확인"** 하는 목적이면 먼저 ANIMA 3파일로 한 장을 뽑아 보고, 그 다음에 Illustrious 나 다른 체크포인트로 넓히는 편이 덜 막힌다.

**세 파일짜리(ANIMA)는 넣는 폴더가 서로 다르다.** 체크포인트 폴더에 전부 넣으면 안 된다 —
어느 것을 어디에 넣는지는 이 문서의 **'폴더 경로 표'** 와 [ANIMA](anima.md)를 보라.

**검증용 배치만 먼저 적으면 이렇게다.**

| 파일 | 넣는 폴더 |
|---|---|
| `anima-base-v1.0.safetensors` | `설치폴더\ComfyUI\models\diffusion_models` |
| `qwen_3_06b_base.safetensors` | `설치폴더\ComfyUI\models\text_encoders` |
| `qwen_image_vae.safetensors` | `설치폴더\ComfyUI\models\vae` |

**4) 실행** — 모델 파일을 넣었으면 먼저 ComfyUI 를 다시 열고, **첫 화면에 뜨는 기본 워크플로우가 깨져 있어도 당황하지 말라.**
실검증에서는 기본 예제 대신 **`템플릿` → 검색창에 `Anima` → `Anima Base v1: 텍스트 기반 이미지 생성`** 으로 들어가는 쪽이 더 곧다.

**지금 버전에서는 여기서 한 번 더 막힌다.** 템플릿을 열면 `anima-turbo-lora-v0.2.safetensors` 누락 오류가 뜰 수 있다.
이 경우는 실패가 아니라 **템플릿이 추가 로라 1개를 더 요구한다는 뜻**이다.

| 추가 파일 | 넣는 폴더 |
|---|---|
| `anima-turbo-lora-v0.2.safetensors` | `설치폴더\ComfyUI\models\loras` |

오류 패널의 **다운로드** 버튼이나 아래 링크로 받아 넣으면 된다.

`https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors`

파일을 넣은 뒤에는 **오류 패널의 `새로고침`** 을 눌러라. 이번 실검증에서는 **재시작 없이 `새로고침` 만으로 오류가 사라지고 바로 실행**됐다.

**여기서 진짜로 설치 성공 여부를 가르는 확인은 네 가지다.**

1. `diffusion_models` 드롭다운에 `anima-base-v1.0` 이 뜬다
2. `text_encoders` 드롭다운에 `qwen_3_06b_base` 가 뜬다
3. `vae` 드롭다운에 `qwen_image_vae` 가 뜬다
4. `템플릿 → Anima Base v1` 로 연 뒤 **`실행`** 을 눌렀을 때 에러 없이 한 장이 저장된다

셋 중 하나라도 안 뜨면 **파일이 없는 것**이 아니라 **잘못된 폴더에 넣었거나, 복사 후 재시작을 안 했을 가능성**부터 먼저 의심한다.
템플릿에서만 `anima-turbo-lora-v0.2` 누락이 뜨면 체크포인트 3파일 문제는 아니고, **로라 폴더에 그 파일 하나가 더 없는 것**이다.

**5) 로라가 뭔지 눈으로 확인하는 법** — 자동 프롬프트를 끄고 방금 쓰인 프롬프트를 수동 칸에 복사한 뒤 **시드를 고정**하고 실행하면 같은 그림만 반복해서 나온다. 그 상태에서 **로라 스위치만 켜고** 다시 실행하면 그림체가 바뀌는 것이 보인다.

> **같은 모델 + 같은 프롬프트 + 같은 시드 = 같은 결과.** 이 원리를 눈으로 확인시키는 방식이다. (다만 하드웨어가 다르면 완전히 같지는 않다 → [오류 해결](troubleshooting.md))

**6) 첫 결과가 너무 밋밋하면** — 설치 검증용 최소 프롬프트는 "돌아간다" 확인에는 좋지만, 그림은 심심하게 나오기 쉽다.
실검증에서 아래 프롬프트로 바꾸자마자 **더 그럴듯한 아니메 상반신**이 나왔다.

```text
1girl, solo, upper body, long black hair, red eyes, sailor uniform,
night city bokeh, anime illustration, detailed eyes, delicate face,
clean lineart, soft rim light, subtle blush, polished shading
```

네거티브는 이 정도면 충분했다.

```text
worst quality, low quality, blurry, jpeg artifacts, sepia,
realistic, photo, 3d, extra fingers, bad hands
```

같은 시드·같은 프롬프트·같은 설정으로 이 **짧은 네거티브**와,
여기에 `score_1~3`, `artist name`, `chromatic aberration`, `bad anatomy`, `bad proportions` 등을 더한
**길어진 공식형**을 맞붙여 봤는데, **차이는 아주 작고 결과를 뒤집을 정도는 아니었다.**
그래서 **처음 한 장은 이 짧은 네거티브로 시작**하고, 문제가 생길 때만 공식형으로 늘리는 편이 낫다.

실검증 기준으로는 **`832x1216` + `steps 30` + `cfg 4` + `er_sde` + `simple`** 조합이,
최소 프롬프트보다 훨씬 덜 밋밋하고 입문용 예시로 쓰기 좋았다.

**6-1) 태그로 시작할지, 자연어 2문장으로 시작할지** — 입문자가 여기서 바로 헤맨다.
채널 자료는 갈리지만, **이번 로컬 실검증에서는 "정확한 외형 보존" 쪽은 자연어 2문장이 더 낫게 나왔다.**
같은 모델·비슷한 해상도에서 아래 둘을 비교했더니, 짧은 태그 나열은 `long black hair` 를 넣었는데도
머리가 **짧은 보브컷 쪽으로 기울었고**, 자연어 2문장은 **긴 검은 머리**를 더 안정적으로 유지했다.

| 목적 | 먼저 쓸 형식 |
|---|---|
| **캐릭터 외형을 정확히 잡고 싶다** | **자연어 2문장** — 머리 길이·복장·배경 관계를 문장으로 적기 |
| **단부루 태그에 익숙하고 빠르게 바꿔 보고 싶다** | **태그 나열** |

처음 한 장은 아래처럼 **2문장 자연어**로 시작하는 편이 덜 흔들렸다.

```text
Masterpiece, best quality, safe. An anime schoolgirl with long black hair and red eyes is standing in front of blurred city lights at night. She is shown from the upper body with delicate facial features, clean lineart, soft rim lighting, and a subtle blush.
```

반대로 태그 나열은 **짧고 빠르지만 속성을 일부 뭉개 먹을 수 있다.**
즉 **외형 고정이 먼저면 자연어 2문장, 빠른 변주가 먼저면 태그**로 시작하라.

**7) 속도와 품질을 갈라 쓴다** — 같은 프롬프트로 실측해 보니
`anima-base-v1.0` 은 **약 23.7초**, 공식 `anima-turbo-lora-v0.2` 는 **약 4.6초**였다
(`832x1216`, RTX 5070 Ti, ComfyUI 로컬 실행).

정리하면 이렇게 쓰면 된다.

| 목적 | 권장 |
|---|---|
| 프롬프트를 빠르게 바꿔 가며 방향만 잡기 | **터보 로라** — `steps 8`, `cfg 1`, `euler` |
| 한 장을 더 예쁘게 뽑아 저장하기 | **베이스 모델** — `steps 30`, `cfg 4`, **`er_sde` 우선** · `euler` 는 대안 |

터보는 빠른 대신 **디테일이 조금 단순해지고 네거티브가 사실상 죽는다.**
그래서 **빠른 시안 확인은 터보, 최종 저장은 베이스**로 가는 흐름이 입문자에게 가장 덜 헷갈린다.

같은 자연어 프롬프트로 다시 맞붙여 본 실검증(2026-08-18)에서는,
`er_sde` 가 **선이 더 또렷하고 얼굴·옷 주름이 더 중립적이며 안정적**이었다.
`euler` 는 시간 차이는 거의 없었지만 **조금 더 말랑하고 귀여운 쪽으로 기울고 2.5D 느낌이 더 섞였다.**
그래서 **첫 기본값은 `er_sde`**, 얼굴을 좀 더 부드럽고 귀엽게 틀고 싶을 때만 `euler` 로 바꾸는 편이 낫다.

**7-1) 해상도는 어디서 멈추나** — 같은 시드·같은 프롬프트·같은 샘플러(`er_sde`)로
`832x1216` 과 `1024x1536` 을 다시 맞붙여 보니, 큰 쪽이 **확실히 더 예쁘긴 했지만**
시간이 함께 오른다.

| 해상도 | 시간 | 관찰 |
|---|---:|---|
| `832x1216` | **23.2초** | 이미 충분히 깔끔하다. 입문 기본값으로 쓰기 좋다 |
| `1024x1536` | **35.5초** | 머리카락 결·배경 보케·광원 분위기가 더 정리돼 **한 장 완성도**는 올라간다 |

즉 이 PC 기준으로 `1024x1536` 은 **약 1.5배 느린 대신 더 예쁜 한 장**을 주고,
`832x1216` 은 **속도와 품질 균형점**이다.

- **처음 검증 / 프롬프트 탐색**: `832x1216`
- **마음에 든 프롬프트로 최종 한 장 저장**: `1024x1536`

무작정 크게 올리는 것은 권하지 않는다. `1024x1536` 까지는 실익이 있었지만,
그보다 더 큰 해상도는 [ANIMA](anima.md)의 해상도 절처럼 **highres / 업스케일 단계 문제**로 넘어간다.

**다만 여기서 바로 latent hires 로 넘어가면 된다고 생각하면 또 막힌다.**
이번 로컬 실검증에서 **bare ANIMA 설치만으로 가능한 최소 highres**도 한 번 돌려 봤다:

- 1차: `832x1216`
- latent upscale: `1024x1536`
- 2차 KSampler: `12 steps`, `denoise 0.5`

시간은 **직출 1024x1536 = 36.8초**, **latent hires = 37.8초**로 거의 비슷했다.
문제는 **그림이 더 예뻐지는 대신 같은 시드라도 구도와 얼굴 방향이 크게 흔들렸다**는 점이다.
즉 **'지금 가진 기본 설치만으로 바로 쓸 수 있는 next step' 은 맞지만, 안전한 기본값은 아니다.**

정리:

- **안전한 최종 한 장**: 직출 `1024x1536`
- **실험적 다음 단계**: latent hires
- **안정적인 업그레이드 루트**: 전용 업스케일 모델 / PiD / ResShift / USDU 같은 별도 경로를 갖춘 뒤

2026-08-18 로컬 재검증으로 이 마지막 줄도 한 단계 더 구체화됐다.
`2x-AnimeSharpV4_RCAN.safetensors` 를 `models/upscale_models` 에 두고
ComfyUI 의 `Load Upscale Model → Upscale Image (using Model)` 만 붙여 보니,
**구도와 얼굴 방향은 그대로 둔 채 1024x1536 → 2048x3072 로 안전하게 커졌다.**
같은 날 bare latent hires 는 같은 시드에서도 얼굴 방향이 흔들렸으므로,
**지금 이 문서 기준의 다음 단계는 latent hires 보다 전용 업스케일 모델 쪽이 더 안전하다.**

주의:

- shared models 방식이면 `extra_model_paths.yaml` 에 **`upscale_models: upscale_models`** 항목도 있어야 한다
- 파일을 넣은 뒤 목록이 안 보이면 **F5 새로고침 또는 ComfyUI 재시작**

→ [자원 — 받는 곳 모음](resources.md) · [모델 고르기](models.md) · [ComfyUI 쓰는 법](comfyui.md) · [로라 쓰는 법](lora-usage.md)


<small>근거 — [ComfyUI - 산지직송 뉴비가 작성한, 하루만에 설치하고… 26.02](https://arca.live/b/aiart/163532702) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430)</small>

## A0-2. ComfyUI-Easy-Install 을 조금 더 — 302초 · SageAttention Add-on · Torch-Pack 복구 (2026-02)
<small>2026-02 기준 · 근거 1건</small>

바로 위 A0 이 "받아서 풀고 실행하라"까지라면, 이 항목은 **그 툴에 뭐가 더 들어 있는가**다. 특히 **SageAttention 을 더블클릭으로 해결한다**는 점이 크다 (161826600, 2026-02, 추천 40).

```
https://github.com/Tavris1/ComfyUI-Easy-Install/releases
# 직링 예
https://github.com/Tavris1/ComfyUI-Easy-Install/releases/download/3.12.2/ComfyUI-Easy-Install.zip
```

압축을 풀고 설치 실행 파일을 더블클릭하면 **git 과 파이썬까지 알아서 깐다.** 함께 들어 있는 `Helper-CEI.zip` 은 설치에 필요한 파일 모음이라 건드릴 필요 없다.

| | |
|---|---|
| 설치 시간 | 작성자 환경 **302초**. 댓글에 320초 · 490초 사례 |
| 같이 깔리는 것 | 대중적으로 쓰이는 커스텀 노드들이 처음부터 함께 |
| 바탕화면 아이콘 | `ComfyUI-EZi`(기본 실행) · `ComfyUI-SA`(**SageAttention 적용 실행**) |
| 모델 폴더 연결 | 툴에서 폴더만 지정하면 자동으로 잡아 준다 |

### SageAttention — '통곡의 벽' 을 더블클릭으로

> **"보통은 이걸 까는 게 ComfyUI 입문의 '통곡의 벽'이다."**

`Add-Ons` 폴더의 **SageAttention 을 더블클릭**하면 알아서 깔린다. **ComfyUI 를 켜기 전에 먼저 실행**할 것을 권한다. Triton 은 이 배치 파일에 포함돼 함께 깔린다(댓글).
직접 명령으로 까는 절차는 → [ComfyUI 쓰는 법](comfyui.md) 의 'SageAttention'

### Torch/CUDA 가 깨졌을 때 — 원클릭 복구

커스텀 노드를 이것저것 깔다 Torch/CUDA 버전이 어긋나 오류가 나면:

```
ComfyUI-Easy-Install\Add-Ons\Torch-Pack
```

에서 원클릭으로 되돌린다. 업데이트 후 오류가 나면 `Add-Ons\Tools` 의 **버전 스위처**를 쓴다(기본은 바로 아랫버전으로만 내려간다).

**`Add-Ons` 안의 파일들은 단독 실행형이라 다른 ComfyUI 설치본에도 쓸 수 있다** (댓글). 기존 ComfyUI 에 sage 를 넣고 싶으면 거기서 `Torch 2.9.1+cu130 (default).bat` 으로 파이토치 버전을 맞춘 뒤 `SageAttention.bat` 을 실행하면 sage 와 triton 이 같이 깔린다.

### 주의

- **자동 업데이트는 없다.** 문제가 없으면 그냥 쓰고, 새 기능이 필요할 때만 업데이트한다.
- **노드까지 업데이트하면 Torch 버전이 달라질 수 있다.**
- 포터블이라 다른 폴더에 여러 개 깔아도 되지만 **동시에 실행하려면 포트 번호를 다르게** 줘야 한다 → [ComfyUI 쓰는 법](comfyui.md) 의 '버전별 인스턴스'
- SageAttention 을 적용하면 아주 가끔 화질이 나빠지거나 아예 안 되는 모델이 있다(Ace-step 은 소리가 안 남).

→ [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [ComfyUI Portable 설치 쉽게 하는 툴 하나 소개함 26.02](https://arca.live/b/aiart/161826600)</small>

## A. Forge Neo + ANIMA 설치 (2026-05 기준, 지금 방식)
<small>2026-05 기준 · 근거 1건</small>

**1) 파이썬 3.13.12 설치**

```
https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe
```

> **주의** — NAIA 를 함께 쓸 사람은 이 3.13.12 설치 시 `Add python.exe to PATH` 를 **체크하면 안 된다**. 기존 파이썬과 충돌을 막기 위해서다.

**2) git 설치** (미리 깔아 둔다)

**3) ANIMA 파일 3개 다운로드**

```
https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors
https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors
https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors
```

**4) 클론** — 설치할 폴더를 만들고 탐색기 주소창을 지운 뒤 `cmd` 를 쳐 명령 프롬프트를 연다.

```
git clone https://github.com/Haoming02/sd-webui-forge-classic sd-webui-forge-neo --branch neo
```

**5) `webui-user.bat` 편집** — 메모장으로 열어 아래 두 줄을 만들고, 파이썬 줄 앞의 `:: `(주석 표시)를 지운 뒤 `Ctrl+S`.

```bat
set PYTHON=py -3.13
set COMMANDLINE_ARGS=--api
```

**6) 파일 배치** — 3)에서 받은 세 파일을 각각 stable diffusion(체크포인트) 폴더 / text encoder 폴더 / VAE 폴더에 넣는다.

**7) 실행** — `webui-user.bat` 을 더블클릭하면 의존성이 자동 설치되고 WebUI 가 열린다. UI 프리셋을 ANIMA 로 바꾸고 Checkpoint 를 로드한 뒤 VAE / Text Encoder 를 지정한다.

**8) 첫 생성값** — 모르겠으면 이렇게 둔다.

| 항목 | 값 |
|---|---|
| 샘플러 | `ER SDE` |
| 스케쥴러 | `Simple` |
| 스텝 | `27~30` |
| CFG | `4.5~5.5` |

성능 관련 인자(`--cuda-malloc`, `--use-sage-attention`)는 원문이 "따로 알아보라"고만 적어 두었다.
NAIA 를 쓸 경우 `--api` 를 넣었다는 전제로 NAIA 의 API 메뉴 → WEBUI 탭에서 확인 후 저장하면 바로 연결된다 → [NovelAI](nai.md)

<small>근거 — [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328)</small>

## B. ComfyUI 포터블 통합팩 (2026-08 기준 0.31.0)
<small>2026-08 기준 · 근거 9건</small>

SageAttention·Triton·커스텀 노드·워크플로우를 미리 넣어 배포하는 '딸깍' 패키지다. 배포 링크는 base64 로 가려 올라오고 **비번은 `ai`, 기한은 한 달**이라 지난 판은 대개 만료돼 있다 → [자원](resources.md)

**규칙 다섯 가지 (판이 바뀌어도 그대로다)**

1. **한글이 없는 경로**에 압축을 푼다.
2. **본체를 업데이트하지 않는다.** 새 버전이 나오면 처음부터 새로 받는다.
3. 실행은 `run_nvidia_gpu.bat`, **sage attention 을 쓰려면** `run_nvidia_gpu_fast_fp16_accumulation.bat` (속도 10~15% 향상, 손가락 찐빠가 늘어난다는 보고 있음).
4. 지원 GPU 는 **지포스 3000~5000번대**. 라데온은 미확인. **sage 를 끄면 2000번대도 동작**한다 (RTX 2060 Super 8GB 확인).
5. `설정 → Comfy → Nodes 2.0 → 모던 노드 디자인` 이 켜져 있으면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다. **끈다.**

**따로 받아 넣어야 하는 파일**

```
# 체크포인트 → 설치폴더\ComfyUI\models\checkpoints
https://civitai.red/models/827184/wai-illustrious-sdxl

# ANIMA → 설치폴더\ComfyUI\models\diffusion_models  (Base v1.0 또는 Aesthetic v1.1)
https://civitai.red/models/2458426

# 컨트롤넷 → 설치폴더\ComfyUI\models\controlnet
https://huggingface.co/xinsir/controlnet-union-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors
https://civitai.com/models/1376234/noobai-inpainting-controlnet
https://civitai.red/models/962537/noobai-xl-controlnet-openpose
https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/OpenPoseXL2.safetensors
https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
https://huggingface.co/kohya-ss/Anima-LLLite/resolve/main/anima-lllite-inpainting-v2.safetensors

# SAM3 → 설치폴더\ComfyUI\models\sam3
https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors
```

> 기본으로 들어 있는 `OpenPoseXL2` 가 잘 안 들으면 `noobai-xl-controlnet-openpose`(civitai 962537) 로 교체하라는 작성자 정정이 있다.

**triton·sageattention 을 직접 깔 때**

```
git clone https://github.com/DazzleML/comfyui-triton-and-sageattention-installer.git
# 포터블 내부 파이썬으로:
python comfyui_triton_sageattention.py --install
```

→ 워크플로우 다루는 법은 [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039)</small>

??? note "근거 9건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [comfyui portable v0.15.1 + sage +… 26.02](https://arca.live/b/aiart/163592169)

## B-2. 첫 영상까지 — Wan I2V 를 맨땅에서 돌리기 (2025-09)
<small>2025-09 기준 · 근거 1건</small>

설치를 마쳤으면 **첫 영상까지 가는 데 필요한 것은 파일 세 개와 bat 하나뿐이다.**
아래는 "아무것도 모르는 사람" 기준으로 쓰인 절차다(2025-09).

| 준비물 | |
|---|---|
| 권장 VRAM | **16GB 이상** (NVIDIA RTX + 윈도우) |
| 실사용 가능 | **12GB** 도 잘 작동한다 |
| 빠듯함 | 8GB — 돌아가긴 하지만 힘들다 |

### 1. ComfyUI 포터블

`ComfyUI_windows_portable_nvidia.7z` 를 받아 압축을 푼다. **포터블이라 python·git 을 따로 안 깔아도 된다.**

> ⚠ **압축 푸는 위치는 한글이 들어가지 않은 짧은 경로**여야 하고, 가능하면 고속 SSD 가 좋다(HDD 도 작동은 한다).

이미 쓰고 있다면 새로 깔지 말고 **`update` 폴더의 `update_comfyui.bat` 을 반드시 한 번 실행**한다.

### 2. 모델 — 여기서 뉴비가 가장 잘 빼먹는 것

```
# WAN 확산 모델 (i2v)
https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/tree/main/v10
# ⚠ 보조 모델 CLIP VISION — 이걸 빼먹으면 안 된다
https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/clip_vision
```

i2v 모델이 둘인데 `nsfw` 가 붙은 것은 야한 영상용, 아닌 것은 일반용이며 용량이 되면 둘 다 받는 게 좋다.

| 파일 | 넣는 곳 |
|---|---|
| WAN2.2-14B-Rapid-AllInOne | `ComfyUI_windows_portable > ComfyUI > models > checkpoints` |
| **`clip_vision_h.safetensors`** | `... > models > clip_vision` |

### 3. 실행

| bat | |
|---|---|
| **`run_nvidia_gpu_fast_fp16_accumulation.bat`** | 기본으로 이걸 쓴다 |
| `run_nvidia_gpu.bat` | 느린 대신 품질이 아주 조금 좋다 |

**뜨는 검은 창이 ComfyUI 본체다. 그 창을 닫으면 프로그램이 꺼진다.**
브라우저는 자동으로 열리고, 실수로 닫았으면 아래로 다시 들어간다 — **단 ComfyUI 가 돌고 있는 그 컴퓨터에서만.**

```
http://127.0.0.1:8188
```

### 4. 워크플로우와 경로

배포된 워크플로우 파일을 창에 드래그앤드롭하거나 `C 버튼 > 파일 > 열기` 로 연다.
*(⚠ 이 글의 워크플로우는 mega.nz 로 배포됐다. **mega.nz 링크는 시간이 지나면 만료될 수 있다.**)*

| 경로 | 무엇 |
|---|---|
| `ComfyUI/input` | 업로드한 이미지가 저장되는 곳 |
| `ComfyUI/output/video` | **결과 영상이 저장되는 곳** |

프롬프트는 **영어가 가장 좋지만 중국어를 공식 지원하고 한국어도 어느 정도 알아듣는다.**
결과는 **입력 이미지와 프롬프트에 크게 좌우된다** — 마음에 안 들면 시드를 바꿔 다시 뽑는다.

→ 실전 설정값은 [비디오 생성](video-generation.md), 워크플로우가 안 돌아갈 때는 [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [응애도 할 수 있는 ComfyUI Wan I2V 영상 AI … 25.09](https://arca.live/b/aiart/147203387)</small>

## C. comfy-cli 로 직접 구성 (2026-06 기준)
<small>2026-06 기준 · 근거 1건</small>

포터블이 아니라 환경을 직접 잡는 방식이다. **전제는 NVIDIA 3000번대 이상 + 윈도우**이며 WSL·linux·mac 은 다루지 않는다고 원문이 못박는다(ANIMA 가 bf16 이라 20 시리즈는 양자화나 fp32 캐스팅이 필요해 제외).

강제 환경: **cuda 13.2 / python 3.13 / uv / torch 2.12**

```powershell
# uv 설치
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```
uv venv --python 3.13
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu132
uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.9.25/flash_attn-2.8.3+cu132torch2.12-cp313-cp313-win_amd64.whl
uv pip install -U "triton-windows<3.8"
uv pip install comfy-cli torchaudio comfy-aimdo simpleeval blake3 torchsde spandrel aiohttp kornia alembic comfy-kitchen httpx==0.28.1 comfyui-manager
```

```
comfy install
comfy launch
# → http://localhost:8188/
```

재실행할 때는 설치 위치에서 터미널을 열고 가상환경을 켠 뒤 `comfy launch`.

```
.venv\scripts\activate.ps1
```

모델은 huggingface 에서 받아 `comfy/ComfyUI/models` 아래 같은 이름 폴더(diffusion_models · vae · text_encoders)에 넣고, 노드는 매니저에서 `SpectrumKSampler` · `Anima Block Compile` · `Anima PiD Decode` 를 최신판(nightly 제외)으로 설치한다.
포터블 대비 장점은 컴파일이나 cuda 경로가 꼬였을 때 해결이 수월하다는 점이다.

<small>근거 — [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089)</small>

## C-2. comfy-cli + uv 로 직접 설치 — 명령어 전문 (2026-05)
<small>2026-05 기준 · 근거 1건</small>

위 'C. comfy-cli 로 직접 구성' 과 같은 방식이되, **ANIMA 전용이 아닌 일반 구성**의 명령어 전문이다 (169751935, 2026-05).

> ⚠ **원문의 경고를 먼저 옮긴다.** 터미널 경험이 없고 프로그래밍 경험이 전무하며 GPT 로 명령어를 다루는 데 익숙하지 않으면 오류 대처가 매우 어려우니 **따라 하지 말 것.** 권장은 **RTX 4000번대 이상 + VRAM 16GB**.

```powershell
# (0) 최신 PowerShell 이 필요하면
winget install --id Microsoft.PowerShell --source winget

# (1) uv 설치
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**(2) 작업 폴더를 만든다.** 예: `D:\ComfyUI\ComfyUI_base` — **경로가 길면 안 되고 한국어가 들어가면 안 된다.** 그 폴더로 이동해서:

```
uv venv -p 3.12
uv pip install --upgrade pip
```

**(3) comfy-cli 와 torch** — torch 를 따로 까는 이유는 **원하는 CUDA 버전을 쓰기 위해서**다.

```
uv pip install comfy-cli
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
uv run comfy-cli --workspace ComfyUI --skip-prompt install --nvidia --skip-torch-or-directml
```

| GPU | index-url |
|---|---|
| RTX 5000번대 | `.../whl/cu130` |
| RTX 4000번대 | `.../whl/cu128` 이 나을 수 있음 |

`--skip-prompt` 는 예/아니오 질문 건너뛰기, `--skip-torch-or-directml` 은 이미 원하는 버전으로 torch 를 깔았으니 건너뛰기다.

**(4) 실행**

```
uv run comfy launch -- --windows-standalone-build --enable-manager --auto-launch
```

배치 파일로 만들려면 아래를 `.bat` 으로 저장해 **작업 디렉터리**(`D:\ComfyUI\ComfyUI_base` — 그 아래 `ComfyUI` 가 **아니다**)에 넣는다.

```bat
@echo off
cd /d "%~dp0"
uv run comfy launch -- --windows-standalone-build --enable-manager --auto-launch
pause
```

**(5) 업데이트**

```
uv run comfy update
uv pip install -U comfyui-manager
```

> CLI 설치는 **최신 매니저 UI 가 자동으로 딸려 오므로** ComfyUI-Manager 를 커스텀 노드로 따로 설치할 필요가 없다. 다만 매니저 갱신은 `uv run comfy node update ComfyUI-Manager` 로는 **안 되고** 위의 `uv pip install -U comfyui-manager` 를 써야 한다.

**(6) 추가 가속**

```
uv pip install -U "triton-windows==3.6.0.post26"     # 또는 "triton-windows<3.7"
uv pip install "https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post4/sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl"
```

실행 인자에 `--use-sage-attention` 을 넣으면 별도 노드 없이 적용되고, `--fast` 는 fp16 가속을 쓴다. 튜링(RTX 20 시리즈)도 지원하므로 구형 카드도 sage-attention 을 쓸 수 있다(댓글).

**포터블과 뭐가 다른가** — 거의 같지만, `comfy` 명령 하나로 커스텀 노드와 모델의 다운로드·업데이트를 일괄 관리할 수 있다.

→ [VRAM·속도 최적화](vram.md)


<small>근거 — [Comfy CLI 설치 방법 정리 26.05](https://arca.live/b/aiart/169751935)</small>

## '체크포인트 폴더에 넣었는데 안 돼요' — 체크포인트라는 말이 두 가지다
<small>2026-05 기준 · 근거 4건</small>

반복해서 나오는 입문자 사고인데, 원인은 **용어**다 (170230261, 2026-05).

| | 뜻 |
|---|---|
| **넓은 의미의 체크포인트** | 게임의 임시 세이브처럼 **특정 시점의 모델 상태를 저장한 것 전부.** 이 정의로는 LoRA 도 체크포인트다 |
| **좁은 의미의 체크포인트** | WebUI·ComfyUI 가 말하는 것. **디퓨전 모델 + CLIP(텍스트 인코더) + VAE 를 한 파일로 병합한 것** |

SD1 부터 SDXL 까지는 이 셋을 한 파일로 묶어 배포하는 것이 관행이었고 그게 곧 '체크포인트'였다. 그런데 모델이 커지고 복잡해지면서 **각 구성 요소를 병합하지 않고 따로 배포**하기 시작했는데(ANIMA 같은 최신 모델), **아무도 기존 기능의 이름을 바꾸지 않아** 용어가 어긋난 채로 남았다.

그래서 ComfyUI 기본 워크플로의 `Load Checkpoint` 노드에 ANIMA 를 물리면 **에러가 난다.** 그 노드는 병합본만 읽기 때문이다.

**모델 종류별로 어디에 넣고 무엇으로 부르나**

| 배포 형태 | 넣을 폴더 | 부르는 노드 |
|---|---|---|
| 병합본 (SD1.5 · SDXL · Illustrious · Pony) | `models\checkpoints` | `Load Checkpoint` |
| **디퓨전 모델 단독** (ANIMA 등) | **`models\diffusion_models`** | `Load Diffusion Model` 계열 |
| 텍스트 인코더 | `models\text_encoders` | 별도 로더 |
| VAE | `models\vae` | 별도 로더 |
| 로라 | `models\loras` | 로라 로더 노드 |

> 병합이 미숙하던 시절 VAE 가 제대로 작동하지 않는 일이 잦아서 **VAE 를 따로 불러와 연결하는 기능은 예전부터 있었다.** 지금 분리 배포 모델을 다루는 방식은 그 기능을 그대로 쓰는 것이다.

**왜 이렇게 됐나 (댓글)** — ckpt 가 그런 묶음 형태를 갖게 된 것은 SD1/SDXL 시절 Stability AI 가 그렇게 배포했기 때문이고, 그러지 않으려면 **Diffusers 규격**으로 배포해야 하는데 그건 파일이 너무 잘게 나뉘어 있어 그것대로 불편했다.

→ 자세한 폴더 표는 바로 아래 항목 · [ANIMA](anima.md) · [모델 고르기](models.md) · [용어집](glossary.md)


<small>근거 — [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089) · [넓은 의미의 체크포인트와 좁은 의미의 체크포인트 26.05](https://arca.live/b/aiart/170230261)</small>

## 모델 파일 받기 — Hugging Face 에서 무엇을 누르나
<small>⚠️ 2023-01 기준 · 근거 1건</small>

모델 파일을 어디서 받는지부터 막히는 경우가 있다. **Hugging Face** 는 절차가 정해져 있다.

| 순서 | |
|---|---|
| 1 | `https://huggingface.co/` 왼쪽 위 검색창에 모델 키워드를 넣는다 |
| 2 | 모델 페이지에서 **`Files and versions`** 탭을 연다 |
| 3 | 목록에서 **`.ckpt` · `.safetensors`** 확장자가 곧 모델 파일이다. 이것만 알면 무엇이 모델인지 바로 구분된다 |
| 4 | ⚠ **파일명을 누르면 다운로드가 아니라 안내 페이지가 열리는 경우가 있다.** 본문의 download 링크나 **용량 옆의 아래 화살표(↓) 버튼**을 누르는 편이 확실하다(댓글 지적 → 본문 반영) |

**클라우드(코랩·런팟 등)에서 쓸 때는** 파일을 로컬로 받아 다시 올리지 말고, 다운로드 링크를 우클릭해 주소를 복사한 뒤 컨테이너에서 직접 받는다.

```
https://huggingface.co/<user>/<repo>/resolve/main/<파일명>
```

받은 파일을 어느 폴더에 넣는지는 아래 '폴더 경로 표' 항목에 있다.

*(2023-01 자료지만 Hugging Face 화면 구성과 `resolve` 직링크 형식은 그대로다.)*

<small>근거 — [허깅페이스에서 모델 다운받는 방법 23.01](https://arca.live/b/aiart/66720059)</small>

## 폴더 경로 표 — 받은 파일을 어디에 넣나
<small>2026-08 기준 · 근거 10건</small>

**A1111 계열 (WebUI / Forge Neo / reForge)** — 용량과 확장자로 종류를 판별한다.

| 종류 | 용량 | 확장자 | 경로 |
|---|---|---|---|
| 임베딩 | **1MB 이하** (1토큰당 4KB, 75토큰을 못 넘는다) | `.pt` | `\stable-diffusion-webui\embeddings` |
| 하이퍼네트워크 | 21MB~1GB | `.pt` | `\models\hypernetworks` |
| 체크포인트(모델) | 7.2GB(원본) / 4GB / 2GB(F16) | `.ckpt` `.safetensors` | `\models\Stable-diffusion` |
| VAE | 300~400MB | `.vae.pt` | `\models\VAE` (또는 `\models\Stable-diffusion` — 어느 쪽이든 동일) |
| yaml | 1~10KB | `.yaml` | 모델과 같은 이름으로 `\models\Stable-diffusion` |

> **`.safetensors` 를 받는다.** `.ckpt` 에 숨어 있을 수 있는 악성코드 위험을 없앤 포맷이다.
> 확장자만으로는 임베딩·하이퍼·모델·VAE·LoRA 를 구분할 수 없다. **용량으로 판별**해야 한다.

**ComfyUI**

| 종류 | 경로 |
|---|---|
| 체크포인트 (SDXL/Illustrious) | `설치폴더\ComfyUI\models\checkpoints` |
| ANIMA 본체 | `설치폴더\ComfyUI\models\diffusion_models` |
| 텍스트 인코더 | `설치폴더\ComfyUI\models\text_encoders` (`qwen_3_06b_base.safetensors` 로 개명 권장) |
| VAE | `설치폴더\ComfyUI\models\vae` |
| 로라 | `설치폴더\ComfyUI\models\loras` (하위 폴더 분류 가능) |
| 컨트롤넷 | `설치폴더\ComfyUI\models\controlnet` |
| SAM3 | `설치폴더\ComfyUI\models\sam3` |
| 업스케일러 | `설치폴더\ComfyUI\models\upscale_models` |
| 프레임 보간(rife) | `설치폴더\ComfyUI\models\frame_interpolation` |
| **출력물** | `설치폴더\ComfyUI\output\날짜\` (중간 과정은 그 아래 `WIP`) |

**해상도 프리셋을 고치는 파일**

```
Illustrious/SDXL : custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py
ANIMA            : custom_nodes\comfyui-kjnodes\custom_dimensions.json
```

**WebUI(A1111 계열)의 출력 경로**

```
자동 저장  : output/txt2img-images   (그리드는 output/txt2img-grids)
저장 버튼  : (webui루트)/log/images  — log.csv 에 프롬프트·시드가 누적된다
```

**ComfyUI-Lora-Manager 로 ANIMA 를 받았을 때** — 매니저는 체크포인트를 `models/checkpoints` 에 저장하지만 ANIMA 는 `models/diffusion_models` 에 있어야 한다. 정션으로 우회한다(심링크는 관리자 권한이 필요하고 `.lnk` 바로가기는 동작하지 않는다).

```
mklink /J ComfyUI\models\checkpoints\Anima ComfyUI\models\diffusion_models
```

### A1111 계열 저장 설정 — 켜 두지 않으면 나중에 되찾을 수 없다

폴더만 정해 놓고 **저장 설정을 안 만지면 프롬프트가 남지 않는다.**

| 설정 | |
|---|---|
| **'이미지 생성 설정값을 PNG 청크에 텍스트로 저장'** (= EXIF 저장) | ⚠ **반드시 켠다.** 꺼 두면 **나중에 자기 그림의 프롬프트를 되찾을 수 없다** |
| '생성된 이미지마다 생성 설정값을 담은 텍스트 파일 생성하기' | 같은 정보가 `.txt` 로도 저장된다 |
| 저장 jpeg 품질 | **85 가 표준** |
| 그리드 파일 형식 | **png 로 하면 용량이 폭발한다** |
| '(자동 감지 사용시) 그리드에 빈칸이 생기는 것 방지하기' | 8장 생성 시 3x3 에 한 칸 비우는 대신 **4x2** 로 만들어 준다 |

> ⚠ **부가기능(extras) 탭에서 업스케일하면 기존 EXIF 가 제거된다.**

### 저장 경로에도 파일명 패턴을 쓸 수 있다 — 폴더 자동 정리

```
[date]\[model_name]
  → 2023-03-05 에 AOM3.safetensors 로 생성한 결과가  \2023-03-05\AOM3  에 저장된다
```

경로 맨 앞에 `C:` `D:` 처럼 **드라이브를 붙이면 설치 폴더 밖으로도** 저장할 수 있고,
하위 디렉토리 기능의 '디렉토리명 패턴' 을 비워 두면 **프롬프트로 폴더가 만들어진다.**

**쓸 수 있는 키워드**

```
[seed] [steps] [cfg] [sampler] [model_name] [model_hash] [width] [height] [styles]
[date]                          2022-10-24
[datetime]                      20221025013106
[datetime<Format>]              [datetime<%Y%m%d_%H%M%S_%f>]  → 20221025_014350_733877
[datetime<Format><TimeZone>]    [datetime<%Y%m%d_%H%M%S_%f><Asia/Tokyo>]
[prompt] [prompt_no_styles] [prompt_spaces] [prompt_words] [prompt_hash]
```

(2023-03 자료지만 **WebUI 계열(Forge · reForge · Forge Neo)에는 지금도 같은 설정이 있다.**)

<small>근거 — [WebUI 기본 사용법 정리 22.10](https://arca.live/b/aiart/61366565) · [나는 심심하면 정보글을 쓰고 있어... 이미지 저장편 23.03](https://arca.live/b/aiart/71264253) · [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법 23.01](https://arca.live/b/aiart/66582124) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136)</small>

??? note "근거 10건 전부 보기"
    [WebUI 기본 사용법 정리 22.10](https://arca.live/b/aiart/61366565) · [나는 심심하면 정보글을 쓰고 있어... 이미지 저장편 23.03](https://arca.live/b/aiart/71264253) · [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법 23.01](https://arca.live/b/aiart/66582124) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [Anima 찍먹해보기 - 아니마 체크포인트, 로라 다운로드 26.05](https://arca.live/b/aiart/171506089) · [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089) · [ComfyUI SAM3 / RIFE 자체 지원 노드 추가 26.04](https://arca.live/b/aiart/168617494) · [(ComfyUI) Hires Fix 워크플로우 가이드 23.09](https://arca.live/b/aiart/86112135)

## 모델 폴더를 이미 갖고 있다면 — 공유 설정
<small>2026-08 기준 · 근거 6건</small>

같은 모델을 두 번 받지 않아도 된다.

**A1111 계열** — `webui-user.bat` 의 `set COMMANDLINE_ARGS=` 줄에 붙인다.

```bat
set COMMANDLINE_ARGS=--ckpt-dir "C:\경로" --lora-dir "C:\경로" --vae-dir "C:\경로" --embeddings-dir "C:\경로" --theme dark
```

경로 인식이 안 되면 역슬래시를 두 번(`\\`) 쓰거나 `/` 로 바꾼다. 기존 순정 WebUI 폴더를 그대로 지정하면 공유된다.

**ComfyUI 통합팩** — `Add-Ons\Easy-Models-Linker.bat` 를 실행해 기존 ComfyUI models 폴더를 지정하면 `extra_model_paths.yaml` 이 만들어진다. 기존 `extra_model_paths.yaml` 을 복사해도 된다.

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102)</small>

??? note "근거 6건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능) 24.10](https://arca.live/b/aiart/119210516) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430)

## 설치 중 흔한 실패와 해결
<small>2026-08 기준 · 근거 18건</small>

| 증상 | 원인 | 해결 |
|---|---|---|
| `Couldn't launch python` / `exit code: 9009` | 파이썬이 **PATH 에 없다** | 파이썬을 `Add Python to PATH` 체크로 다시 설치하거나, `set PYTHON=py -3.13` 처럼 명시 |
| `PyTorch is not able to access GPU` 로 설치가 멈춤 | NVIDIA 카드가 없거나 비활성 상태 | 장치 관리자에서 그래픽카드 장착·활성 여부 확인 |
| **검은 화면**, 로그에 `Encountered NaN in Latent; Try --disable-sage` | ADetailer 가 원인이었던 사례 | `Haoming02/ADetailer-Neo` 대신 `https://github.com/abzaloff/aadetailer-neoforge` 로 교체 (포지네오 이슈 #1072 에서도 권장) |
| 그림이 **파랗게 깨짐** | SDXL 모델에 **SD1.5 용 VAE** 를 물림 | VAE 를 SDXL 용으로 교체 |
| 결과가 **탁하거나 흰 점**이 찍힘 | 내장 VAE 문제 | 통합팩이면 `VAE Select` 값을 **2** 로 (`fixFP16ErrorsSDXLLowerMemoryUse_v10`) |
| **로라 목록에 안 보임** | 로드된 체크포인트와 로라의 **버전이 다름** | SD1.5 모델엔 SD1.5 로라, SDXL 모델엔 SDXL 로라만 보인다. 포니용과 ILXL 용도 서로 호환되지 않는 경우가 대부분 |
| 모델을 바꿨더니 그림이 망가짐 | 그 계열 권장 해상도가 아님 | SDXL 은 **1024 기준** |
| sage attention 을 켜니 터짐 (RTX 2000번대) | 2000번대 미지원 | **sage 를 끄고 쓴다** (`run_nvidia_gpu.bat`) |
| NoobAI·V-pred 결과가 이상함 | 가속 노드와 상성 | `Kohya Deep Shrink` · `DCW` · `Spectrum` 을 **하나씩 바이패스**해 원인을 찾는다 |
| 워크플로우 배열이 깨지고 커스텀 노드가 오작동 | 모던 노드 디자인 | `설정 → Comfy → Nodes 2.0 → 모던 노드 디자인` 끄기 |
| 압축을 풀었는데 커스텀 노드가 안 뜸 | 한글 경로 | 한글이 없는 경로에 다시 푼다 |
| 외장하드에 설치하니 에러 | — | C드라이브 설치에서는 문제가 없었다는 보고 |
| `--skip-torch-cuda-test` 를 넣어도 안 됨 | 이 인자는 도움이 안 된다 | 원인은 **xformers 와 torch 버전 불일치** (2022 기준) |
| **CUDA out of memory** | VRAM 부족 | `webui-user.bat` 의 COMMANDLINE_ARGS 에 `--lowvram` 또는 `--medvram` 추가 |
| **A1111 이 초기 구동조차 안 됨 (2026)** | 파이썬에서 `pkg_resources` 가 빠졌다 | 아래 **'⚠ 아래 낡은 방식을 따라 하기 전에'** — 제작자 이슈 17201 의 4번 항목 |
| 커스텀 노드 clone 이 `Filename too long` 으로 실패 | 윈도우 260자 경로 제한 | `LongPathsEnabled` 레지스트리 + 재부팅 + `git config --global core.longpaths true` → [오류 해결](troubleshooting.md) |
| 라데온에서 `hipErrorInvalidValue` 로 죽음 | gfx1200·gfx1100 **장치 패키지** 미설치 | `amd_torch_device_gfx12_0` / `amd_torch_device_gfx110x` 추가 설치 → 아래 '라데온(AMD)' |
| **hires 만 켜면 OOM** (VRAM 8GB) | tiled vae 가 없다 | 아래 **'VRAM 8GB 로도 SDXL 은 된다'** |
| `RuntimeError: Couldn't install torch` 가 몇 번을 해도 같음 | 전역 파이썬에 깔고 **venv 안이 비어 있다** | `venv\Scripts\activate.bat` 후 설치 → [오류 해결](troubleshooting.md) |
| `INCOMPATIBLE PYTHON VERSION` 이 뜨며 설치가 멈춤 | A1111 에 **파이썬 3.11 이상**을 깔았다 | **3.10.11**(3.10.6 이상) 로 다시 설치 → 아래 'A1111 계열 재설치' |
| ComfyUI 가 **큐를 여러 개 쌓으면 GPU 대신 CPU 로** 연산 | **kohya GUI 설치기가 CUDA 13.2 로 전역 PATH·CUDA_PATH 를 덮어씀** (내장 PyTorch 2.10.0+cu128 과 충돌) | 실행 옵션에 **`--disable-cuda-malloc`** 추가 → [오류 해결](troubleshooting.md) |
| 라데온 ROCm 업데이트 스크립트가 조용히 멈춤 | 스크립트가 **CPython 3.12 를 강제**한다 | 3.13 포터블이면 안 된다 → 아래 '라데온(AMD)' |
| `... is not a supported wheel on this platform` | whl 파일명의 `cp312` 는 **파이썬 3.12 전용**이라는 뜻 | 자기 파이썬 버전에 맞는 whl 또는 `cp39-abi3` 무관 빌드를 받는다 |

**`--lowvram` / `--medvram` 이 하는 일**
- `--lowvram` 은 모델을 모듈로 쪼개 GPU 메모리에 하나씩만 올린다. 4GB 카드에서도 512x512 가 가능하지만 **RTX 3090 기준 일반 대비 약 10배 느리다.**
- `--medvram` 은 같은 배치에서 조건부/무조건부 노이즈 제거를 분리해 VRAM 을 크게 줄인다.

저사양 배치파일 예 (2022 기준):

```bat
set COMMANDLINE_ARGS=--skip-torch-cuda-test --no-half --precision=full --listen --lowvram --deepdanbooru --autolaunch
```

→ 더 많은 사례는 [오류 해결](troubleshooting.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [(구)WEB UI설치가 어려운 사람을 위한 통합팩 (0.66… 22.10](https://arca.live/b/aiart/60216616) · [WebUI 기본 사용법 정리 22.10](https://arca.live/b/aiart/61366565) · [누구나 따라할 수 있는 로컬 자동좌 WebUI 클린 설치 (… 23.06](https://arca.live/b/aiart/79413719) · [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865)</small>

??? note "근거 18건 전부 보기"
    [(구)WEB UI설치가 어려운 사람을 위한 통합팩 (0.66… 22.10](https://arca.live/b/aiart/60216616) · [WebUI 기본 사용법 정리 22.10](https://arca.live/b/aiart/61366565) · [누구나 따라할 수 있는 로컬 자동좌 WebUI 클린 설치 (… 23.06](https://arca.live/b/aiart/79413719) · [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865) · [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [vram8기가라도 쫄지말고 그림뽑아 24.10](https://arca.live/b/aiart/119326123) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능) 24.10](https://arca.live/b/aiart/119210516) · [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 … 26.08](https://arca.live/b/aiart/179176367) · [RX 9000용 torch+rocm 업데이트 + sage 빌… 26.07](https://arca.live/b/aiart/176063226) · [ComfyUI 에서 bjornulf_custom_nodes … 26.02](https://arca.live/b/aiart/163272564) · [정보탭의 kohya gui 설치후 발생한 문제해결 26.07](https://arca.live/b/aiart/176818115) · [파이토치 설치 안되는사람 보셈 23.02](https://arca.live/b/aiart/69972082)

## VRAM 8GB 로도 SDXL 은 된다 — 실측 처방 (2024-10)
<small>⚠️ 2024-10 기준 · 근거 3건 · 자료 엇갈림</small>

"8GB 로는 안 된다"는 말이 돌지만, **RTX 3060 으로 여덟 조합을 실측한 글**이 반대를 증명했다.
결론부터 — **SDXL 은 8GB VRAM 으로 1024x1024 에 hires 2배까지 되고, ComfyUI 나 forge 로 옮기지 않아도 된다** (119326123, 2024-10, 유용도 9).

**처방 세 줄**

| | 무엇을 | 무엇이 줄어드나 |
|---|---|---|
| 1 | `--medvram` | **기본 생성** VRAM 을 깎는다. 속도가 조금 느려지고 그림 변화는 거의 없다 |
| 2 | **tiled vae** (확장 설치) | **hires** VRAM 을 깎는다. OOM 이 나면 타일 크기를 더 줄인다 |
| 3 | 엔비디아 제어판 → **CUDA - 시스템 메모리 대체 정책** ON | 마지막 합치기 단계의 피크를 넘긴다 |

```
# tiled vae 확장
https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111
```

**실측 조건과 결과** — RTX 3060 12GB / SDXL / 1024x1024 / `Euler a` + `SGM Uniform` / 25스텝 / hires 2배 20스텝.
무설정 · fp8 · tiled vae · tiled vae+fp8 · medvram · medvram+fp8 · medvram+tiled vae · 전부, 여덟 조합(A~H)을 돌렸다.

> **hires 2배에서는 `tiled vae` 를 쓴 조합만 살아남고 나머지는 전부 OOM 이 났다.**
> 즉 8GB 에서 hires 를 살리는 것은 사실상 tiled vae 하나다.

**각 옵션이 하는 일**

| 옵션 | VRAM | 속도 | 그림 변화 | 비고 |
|---|---|---|---|---|
| `--medvram` | 적당히 감소 | 조금 느려짐 | 거의 없음 | `--lowvram` 은 대동소이하며 같이 써도 티가 안 난다 |
| fp8 (WebUI 설정) | 꽤 감소 | 조금 빨라짐 | **꽤 있음** | 모델을 바꿀 때마다 fp8 변환 시간이 든다. WebUI 1.8.0 이상 + torch 2.1.0 이상 |
| **tiled vae** (확장) | **획기적으로 감소** | 조금 느려짐 | 없음 | VAE 작업을 분할 처리. 원글 표현으로 '신' |
| hypertile (1.7.0 내장) | 변화 없음 | hires 개선 | — | 예전에는 hires 결과가 타일별로 디테일·색감이 달라지는 문제가 있었다 |
| deepcache (확장) | — | 향상 | 설정에 따라 심함 | PAG 처럼 U-Net 을 만지는 기능과 충돌할 수 있다 |
| LoRA | 조금 증가 | — | — | |
| **ControlNet** | **평소의 1.5~2배** | — | — | |

### ⚠ '시스템 메모리 대체' 를 끄라는 말은 틀렸다

채널에는 **"초보자 속도 문제의 99% 범인은 엔비디아 제어판의 시스템 메모리 대체이니 꺼라"** 는 말이 돌았다.
실측글이 이것을 정면으로 정정한다. **양쪽을 다 적되, 어느 쪽이 맞는지 밝힌다.**

> ❌ **"끄라"는 진단은 틀렸다.**
>
> 표의 VRAM 값은 **'생성 도중'** 사용량이고, 마지막에 그림을 다시 합칠 때 **한 번은 8GB 를 넘는 피크**가 온다.
> 지금까지 느리다던 사람들은 최적화가 없어서 **생성 도중에도** 시스템 메모리를 썼던 것이다.
> 최적화를 해서 생성 중에는 VRAM 안에서 끝난다면, 마지막에 잠깐 끌어다 쓰는 정도는 시간을 크게 잡아먹지 않는다.
> **VRAM 8GB 면 켜 두는 것이 맞다.**

### 그리고 — 처음부터 hires 를 켠 채로 뽑지 마라

이 글에서 가장 실용적인 한 줄이다.

> 기본 해상도로 뽑아 **마음에 드는 것만 골라** `PNG 정보` 탭에 넣고 **t2i 로 보낸 다음**, 그때 hires 를 걸어 다시 뽑는다.

**댓글 보충**

- 노트북 3060 6GB 로도 본문의 H 세팅이면 1024x1536 에서 2x hires 가 된다.
- ComfyUI 공식 SDXL 추론 권장 VRAM 은 **6GB** 다.
- **`--medvram` 만 넣었는데** `RuntimeError: bad allocation` · `0x00000000` 참조 오류 · 글카 드라이버 이탈이 나는 사례가 있다. 권한이 꼬인 것으로 보이며 **DDU 로 드라이버를 밀고 재설치**하거나 윈도우 재설치 외에 답이 없었다.

**VRAM 이 더 적다면** — 4GB 는 SD1.5 면 가능하고 XL 도 3GB 로 굴린 사례가 있으나 속도·퀄리티는 보장되지 않는다. VRAM 이 낮을수록 WebUI 보다 **ComfyUI** 가 권장된다. ANIMA 라면 **int8 판이 모델+텍스트인코더+VAE 를 합쳐도 4GB 미만**이라 8GB 급에서 무난하다.

→ [VRAM·속도 최적화](vram.md) · [업스케일과 화질](upscale.md) · [오류 해결](troubleshooting.md)

<small>근거 — [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [vram8기가라도 쫄지말고 그림뽑아 24.10](https://arca.live/b/aiart/119326123)</small>

## RTX 5000번대 — CUDA 13.0 / torch 2.10 / python 3.13 전체 조합 (2026-01)
<small>2026-07 기준 · 근거 2건 · 자료 엇갈림</small>

RTX 5000번대는 **CUDA 13.0 이 최신**이라 13.0 으로 맞춘다. **포터블은 시스템 파이썬이 아니라 동봉 파이썬에 깔아야 한다** — cmd 에서 `python_embeded` 폴더로 이동한 뒤 `python -m pip install ...` 형태로 실행한다 (160668279, 2026-01).

**1) torch**

```
pip install torch==2.10.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```

torchvision·torchaudio 도 버전에 맞게 함께 깔린다.

**2) Flash Attention · SageAttention 2.2 · Nunchaku** — https://github.com/wildminder/AI-windows-whl 의 whl 을 `pip install (링크)` 로 깐다.

```
flash_attn-2.8.3+cu130torch2.10.0cxx11abiTRUE-cp313-cp313-win_amd64.whl
sageattention-2.2.0.post3+cu130torch2.10.0-cp313-cp313-win_amd64.whl
nunchaku-1.0.2+torch2.10-cp313-cp313-win_amd64.whl
```

(nunchaku 는 https://github.com/nunchaku-tech/nunchaku/releases 에서)

**3) Triton** — PyTorch 2.10 에는 **Triton 3.6** 이 대응한다.

```
pip install "triton-windows<3.7"
```

그리고 `python_3.13.2_include_libs.zip` 을 `python_embeded` 폴더에 풀어 넣는다.

**4)** `ComfyUI_windows_portable\update\update_comfyui_and_python_dependencies.bat` 을 한 번 실행한다.
⚠ **이 과정에서 pytorch 버전이 멋대로 지워지고 다시 깔릴 수 있다.** 그러면 다시 맞는 버전을 찾아 설치한다.

**5)** `ComfyUI_windows_portable\run_nvidia_gpu_fast_fp16_accumulation.bat` 을 메모장으로 열어 실행 줄에 옵션을 추가한다.

### 실행 옵션 — 본문만 따라 하면 fp8 가속이 안 걸린다

| | |
|---|---|
| 본문 | `--fast fp16_accumulation --use-sage-attention` |
| **댓글 보강** | `--fast fp16_accumulation fp8_matrix_mult cublas_ops` |

`--fast` 의 유효한 값은 **`fp16_accumulation` · `fp8_matrix_mult` · `cublas_ops` · `autotune`** 이며 **이어 써야** 각각 걸린다. 즉 **본문의 옵션만으로는 fp8 가속이 걸리지 않는다.**
`--fast` 뒤에 **아무것도 붙이지 않으면 하위 옵션 네 가지가 전부 켜지고**, 한 칸 띄우고 항목을 적으면 **적은 것만** 켜진다.

### ⚠ 그런데 `cublas_ops` 는 해골물이다 — 그냥 붙이면 아무 일도 일어나지 않는다 (2026-07)

**위 줄의 마지막 인자 `cublas_ops` 는 대부분의 사람에게 아무 효과도 내지 않고 있었다.** 지우지 말고 조건을 알고 쓴다.

| | |
|---|---|
| 오해 | 이름 때문에 **NVIDIA 의 CUBLAS**(CUDA Basic Linear Algebra Subprograms) 가속 라이브러리를 켜는 옵션으로 읽힌다 |
| 실제 | CUBLAS 가 아니라 **`CublasOps` 라는 별도의 파이썬 확장 라이브러리**(`aredden/torch-cublas-hgemm`)를 가리킨다. PyTorch 가 CUBLAS 를 쓰는 방식의 중간 오버헤드를 줄이려고 개발자가 CUDA/C++ 로 CUBLAS·CUBLASLt API 를 직접 호출하게 만든 것이다 (`hgemm` = Half-precision GEMM, 즉 FP16 행렬 곱셈) |
| **확인** | ComfyUI 내장 콘솔에서 아래 한 줄 |

```
pip show cublas_ops
```

```
WARNING: Package(s) not found: cublas_ops
```

**이렇게 뜨면 그 인자는 아무 일도 하지 않는다.** 기본 포터블에는 이 패키지가 들어 있지 않다.
**따로 설치(댓글 확인 — 직접 컴파일해야 한다)하지 않은 채 인자만 붙여 온 사람은 처음부터 아무 이득도 못 보고 있었다.**
ComfyUI 가 이에 대한 설명을 하지 않아 채널 안에서 널리 오해돼 왔다.

> **덤** — 누산(accumulation) 단계에서는 FP16 보다 FP32 가 안전하므로, FP16 GEMM 을 강제로 빠르게 만드는 `cublas_ops` 와
> `fp16_accumulation` 을 함께 켤 때의 관계는 따져 볼 필요가 있다는 지적이 댓글에 있다.

**정리** — `pip show cublas_ops` 가 정상 출력되면 그대로 두고, `Package(s) not found` 가 뜨면 그 인자는 **있으나 마나**다.
남는 세 인자(`fp16_accumulation` · `fp8_matrix_mult` · `autotune`)는 별도 설치 없이 동작한다.

### 흔한 실패 (댓글에서 해결됨)

```
ImportError: DLL load failed while importing _fused: 지정된 프로시저를 찾을 수 없습니다
```

torch / python / sageattention / cuda 버전이 어긋난 것이다. `pip show <패키지>` 로 버전을 확인하고, **cp313 전용 whl 대신 파이썬 버전 무관 빌드(`cp39-abi3`)** 로 바꾸면 해결된다.

| GPU | 쓸 whl |
|---|---|
| 5000번대 (CUDA 13.0) | `sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl` |
| 4000번대 (CUDA 12.8) | `sageattention-2.2.0+cu128torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl` — wildminder 저장소에는 이 조합이 없다 |

둘 다 https://github.com/woct0rdho/SageAttention/releases 에 있다.

### 덧

- **(취향)** `ComfyUI_windows_portable\ComfyUI\comfy\quant_ops.py` 에서 `ck.registry.disable("triton")` 을 찾아 앞에 `#` 을 붙여 주석 처리하면 triton 이 활성화된다.
- Flash Attention 이 어디 쓰이냐면 — **Florence-2 이미지→태그 제네레이터**(ComfyUI 에서는 Miaoshouai-Tagger 커스텀 노드)다.

→ [ComfyUI 쓰는 법](comfyui.md) · [VRAM·속도 최적화](vram.md) · [오류 해결](troubleshooting.md)

<small>근거 — [모르고 쓰면 해골물인 ComfyUI 옵션 26.07](https://arca.live/b/aiart/177447677) · [pytorch 2.10 +  python 3.13 + RTX… 26.01](https://arca.live/b/aiart/160668279)</small>

## RTX 20 시리즈(튜링) 생존 가이드 — Triton 은 반드시 3.2 (2026-05)
<small>2026-05 기준 · 근거 4건</small>

RTX 20 시리즈(튜링, sm75)는 **fp8 도 nvfp4 도 bf16 도 지원하지 않고 fp16 만 쓸 수 있다.** 사실상 ANIMA 를 돌릴 수 있는 최소 사양이다 (170741530, 2026-05).

| 항목 | 튜링에서는 |
|---|---|
| **Sage-Attention** | **필수.** 2.2 를 https://github.com/woct0rdho/SageAttention/releases 에서 받는다. ComfyUI 공식 wheels(https://comfy-org.github.io/wheels)는 튜링에 대응하지 않는다 |
| **Triton** | ⚠ **반드시 3.2.** Triton 은 **3.3 버전부터 튜링 지원을 뺐다** — 최신을 받으면 콘솔에 에러 로그만 잔뜩 뜬다 (https://github.com/triton-lang/triton-windows) |
| Xformers | 선택. Sage-Attention 이 있으면 거의 의미가 없고 효과도 미미하다 |
| fp16 accumulation | 따로 설치할 것 없는 **ComfyUI 기본 옵션**. `--fast` 또는 `run_nvidia_gpu_fast_fp16_accumulation.bat` 또는 KJNodes 의 `Model Patch Torch Settings` |
| Torch Compile | 오래 안 됐으나 원문 말미에 **최신 버전에서는 되는 걸 확인했다고 정정**했다. 단 ComfyUI 공식 노드가 아니라 **KJNodes 사양**을 써야 한다 |
| **Spectrum-KSampler** | **불가.** 제작자 공인 **bf16 필수**다. 다만 거기 내장된 **DCW 기능은 별도 DCW 노드로** 쓸 수 있어 품질 관리 자체는 가능하다 |
| Flash-Attention | 튜링용이 있기는 하다 (https://github.com/ssiu/flash-attention-turing). 다만 Sage·Triton 과 달리 **whl 이 제공되지 않아 직접 빌드**해야 한다 (176657130, 2026-07) |

### sage·triton 이 도저히 안 걸리면 — 옛 조합까지 내려간다

162993309 댓글의 마지막 수단이다. 대신 최신 기능은 포기하게 된다.

```
pip install torch==2.6.0+cu126 torchvision==0.21.0+cu126 torchaudio==2.6.0+cu126 --index-url https://download.pytorch.org/whl/cu126
pip install "triton-windows<3.3"
pip install sageattention==1.0.6
```

### 실측과 병목

- **속도(댓글, 고속 로라 미사용)**: 896x1152 약 **40초** / 1216x1856 약 **95초**. 디테일러까지 돌리는 시간을 생각하면 상위 글카 기준으로는 매우 느리다.
- **남은 병목은 VAE 인코드/디코드다.** 크게 생성하고 업스케일까지 하면 마지막에 여기서 걸리므로 **타일 인코드/디코드**를 찾아 쓰는 것이 답이다.
- 체감 — ANIMA 는 이렇게라도 돌아가지만 **Z-Image 는 뭘 해도 거북이 속도이고 Qwen·FLUX 는 꿈도 못 꾼다.**
- 댓글 선택지: 튜링(T4)에서 **INT8 양자화 모델**이 제법 속도 향상이 있었다는 제보가 있다. 다만 **결과물이 달라지는 대가**가 있다. 1660 Super 도 튜링이라 되긴 하겠지만 VRAM 6GB 라 주의.

> **더 간단한 길** — 통합팩을 쓴다면 **RTX 2060 Super 8GB 에서 sage 만 끄면 정상 동작**이 확인돼 배포글 본문에 반영됐다. 굳이 sage 를 붙이지 않아도 2D 짤은 뽑힌다 → [ComfyUI 쓰는 법](comfyui.md)

→ [ComfyUI 쓰는 법](comfyui.md) · [ANIMA](anima.md) · [오류 해결](troubleshooting.md)

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [로컬 comfyui 찍먹해보기 - sage-attention… 26.02](https://arca.live/b/aiart/162993309) · [RTX 20 시리즈를 사용하는데 아니마는 써보고 싶은 사람들… 26.05](https://arca.live/b/aiart/170741530) · [튜링용 flash-attention 26.07](https://arca.live/b/aiart/176657130)</small>

## RTX 50 시리즈(블랙웰) — A1111 은 dev 브랜치가 필수다 (2025-05)
<small>⚠️ 2025-05 기준 · 근거 1건</small>

PyTorch 2.7 이 정식으로 나왔다고 그냥 깔면 안 된다. **A1111 WebUI 정식(master) 브랜치가 아직 블랙웰을 지원하지 않는다** (135962161, 2025-05).

**이 오류가 뜬다면 그것이다.**

```
RuntimeError: CUDA error: no kernel image is available for execution on the device
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

**해결 1 — zip 배포판을 쓰는 경우**

1. zip 을 받아 `Update.bat` 실행
2. `switch-branch-tool.bat` 실행 → **3** 을 눌러 dev 브랜치로
3. `run.bat` 으로 실행

**해결 2 — 직접 clone**

```
git clone --filter=blob:none -b dev https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

원래 안내 명령에 `-b dev` 가 붙은 것이 전부다. **이미 설치한 사람**은 폴더에서:

```
git switch dev
git pull
```

**그 밖에 알아야 할 것 (댓글)**

| 항목 | 블랙웰에서 |
|---|---|
| xformers | 미지원 |
| Forge | 애초에 지원 안 함 |
| **ComfyUI** | **별도 조치 없이 그냥 동작** |

즉 2025년 상반기 기준으로 RTX 50 시리즈는 **ComfyUI 쪽이 훨씬 수월했다.**

> ⚠ 같은 `no kernel image is available` 문구라도 **kohya_ss 로 로라를 학습하는 중**이라면 원인이 다르다 — `Use 8bit adam` / bitsandbytes 다 → [로라 쓰는 법](lora-usage.md)

참조: `https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/16818`


<small>근거 — [!!! 블랙웰 (RTX 50) 유저들 설치시 필독 !!! 25.05](https://arca.live/b/aiart/135962161)</small>

## 순정 A1111 에서 v-pred 모델 쓰기 — dev 브랜치 (되돌릴 때의 함정 포함)
<small>⚠️ 2025-02 기준 · 근거 1건 · 자료 엇갈림</small>

v-pred(v-prediction)는 노이즈 예측 방식이 기존 epsilon 과 다른 모델 형식이다.
**지원하지 않는 버전에서 돌리면 그림이 새까맣게 나오거나 망가진다.** NoobAI vpred 계열이 나오면서 필요해진 설정이다.

### 순정 A1111 은 dev 브랜치로 갈아타는 것 말고 방법이 없다

```bash
# webui 설치 폴더의 파일탐색기 주소창에 cmd 를 치고 엔터
git switch dev
git pull
```

끝이다. 실행하면 화면 아래 버전 표기가 dev 커밋으로 바뀌어 있고, 그 뒤로는 평소처럼 v-pred 모델을 골라 돌리면 된다.

> ⚠ **Forge / reForge 는 v-pred 를 이미 지원하므로 이 작업이 필요 없다** *(댓글)*.
> 실제로 Forge 를 쓰면서 이 글대로 따라 하다 브랜치가 꼬인 사용자가 나왔다.

### ⚠ 되돌릴 때 — 본문의 `git switch master` 가 실패한다

원문은 복구 명령을 `git switch master` 로 안내했지만, **저장소의 기본 브랜치가 `main` 인 경우 이렇게 실패한다.**

```text
fatal: invalid reference: master
```

**저장소마다 기본 브랜치 이름이 다르다. 되돌릴 때는 원래 브랜치명을 확인해야 한다.**

```bash
git switch main      # 기본 브랜치가 main 인 경우 (댓글에서 이렇게 복구됨)
git pull
```

dev 로 옮기면 옵션 구성이 달라져 당황할 수 있는데, 기존 버전이 최신이 아니었다면 업데이트되면서 바뀐 부분일 수 있다.

### 곁들여 알아 둘 것

| | |
|---|---|
| **ztsnr** (Zero Terminal SNR) | 설정의 `[Noise schedule for sampling]` 에서 켠다. **v-pred 모델은 그냥 뽑아도 적용돼 있어 차이가 없고**, epsilon 모델에는 적용되어 그림이 바뀐다 |
| **CFG Rescale** | `https://github.com/Seshelle/CFG_Rescale_webui` — **수치를 세게 줄수록 색이 망가지므로 과하게 주지 마라** |
| Auto Color Fix | 채도·대비를 올려 한 장을 더 만들어 주는 딸림 기능. 어두운 그림에서는 티가 안 난다 |
| SD1.5 | **v-pred 모델이 없다** |

*(ComfyUI 쪽에서 v-pred 노드 때문에 노이즈만 나오는 문제는 → [ComfyUI 쓰는 법](comfyui.md))*

<small>근거 — [순정webui에서 v-pred모델쓰기 25.02](https://arca.live/b/aiart/128472488)</small>

## 라데온(AMD) — '로컬 비권장' 이 뒤집혔다 (Linux + ROCm 10.1, 2026-08)
<small>2026-08 기준 · 근거 7건</small>

**옛 서술은 "라데온은 로컬 비권장" 이었고, 2022~2023년 기준으로는 맞는 말이었다.**
윈도우에 ROCm 드라이버가 없고 DirectML 용 PyTorch 는 WebUI 가 요구하는 버전보다 낮았기 때문이다 (60447786, 2022-10).

### 먼저 — 가장 쉬운 길은 AMD 전용 포터블이다 (2026-03)

아래의 리눅스 ROCm 구성은 성능을 짜내는 길이고, **"되긴 되나" 만 확인하고 싶으면 이쪽이 훨씬 짧다.**
RX 7900 XTX + **아드레날린 26.2.2 일반 게임 드라이버**(별도 프로 드라이버 불필요)로 확인됐다.

```
# ComfyUI 릴리스의 'Experimental portable for AMD GPUs'
https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_amd.7z
```

C 드라이브에 압축을 풀고 **`run_amd_gpu.bat`** 을 더블클릭하면 cmd 가 뜨면서 `http://127.0.0.1:8188/` 이 열린다.
그 뒤 사용법은 일반 ComfyUI 와 같다.

**여기서 ROCm 나이틀리로 torch 만 올리고 싶다면**(댓글이 제시한, 초심자에게 가장 빠르고 안정적이었던 방법)
`python_embeded` 에서:

```
python -m pip install --index-url https://rocm.nightlies.amd.com/whl-multi-arch/ "torch[device-gfx1201]" "torchvision[device-gfx1201]" torchaudio
```

또는 `update` 폴더의 `update_comfyui_and_python_dependencies(multi arch).bat` 을 그 문구로 고쳐 실행한다.

**자기 카드의 gfx 코드** (`https://github.com/ROCm/TheRock/blob/main/RELEASES.md`)

| GPU | gfx | GPU | gfx |
|---|---|---|---|
| RX 9070 / XT | `gfx1201` | RX 6900 / 6800 XT | `gfx1030` |
| RX 9060 / XT | `gfx1200` | RX 6750 / 6700 XT | `gfx1031` |
| RX 7900 XTX / XT | `gfx1100` | RX 6600 XT / 6600 | `gfx1032` |
| RX 7800 / 7700 XT | `gfx1101` | RX 6500 XT | `gfx1034` |
| RX 7600 | `gfx1102` | RX 5700 / XT | `gfx1010` |
| Ryzen AI Max+ 395 | `gfx1151` | | |

ROCm 미지원 카드도 gfx 버전만 맞추면 동작은 하지만 **'그냥 동작만 하는 수준'** 이다.

**SageAttention 은 RDNA4 만 생각한다** — **RDNA3 이하에는 fp8 연산 유닛이 없어 SageAttention 2.2.0 이 작동하지 않을 가능성이 높다.**
그래서 배포된 빌드 스크립트도 RDNA3 이하에서는 sage 를 건너뛰고 torch 업데이트만 하도록 수정됐다.
sage 까지 빌드돼야 성공 판정인 것은 **RDNA4(gfx1200/1201)** 사용자다.

> ⚠ **그 ROCm 업데이트 PowerShell 스크립트에는 본문에 안 적힌 조건이 있다.**
> 내부적으로 **CPython 3.12 를 강제**하므로(`if sys.version_info[:2] != (3, 12): raise SystemExit`)
> **3.13 포터블을 쓰고 있다면 여기서 멈춘다.**

**ROCm 이 안 맞으면 ZLUDA 라는 갈래가 있다(댓글)** — ROCm 이 나아지긴 했어도 안 되는 것이 꽤 있고,
**Qwen 같은 모델은 오히려 ZLUDA 가 더 잘 먹고 메모리도 덜 쓴다.** RX 6700 XT 기준으로는 **ROCm 7 보다 ZLUDA 가 더 안정적이고
속도 차이는 거의 없었다.**

⚠ **ComfyUI 에서 커스텀 노드를 깔다가 ROCm 용 torch 가 날아가는 사고가 잦으니 늘 신경 써야 한다.**

**라데온 실측(댓글)** — RX 9070 XT 는 832x1216 한 장이 잘 나오면 **약 7초**, 7900 XTX 는 **6900 XT 대비 약 2.5배**.
라데온으로도 **SDXL · ANIMA · ZIT 정도는 충분**하고, **영상 툴도 되긴 하나 동급 지포스보다 느리다.**

**AMD 설치 가이드 총정리**
```
https://github.com/CS1o/Stable-Diffusion-Info/wiki/Webui-Installation-Guides#amd-install-guides
https://github.com/CS1o/Stable-Diffusion-Info/wiki/Lora-Trainer-Setup-Guides#amd-install-guides   (로라 학습)
```

---

**2026년 8월 기준으로는 조건이 붙은 '된다' 다.** 조건을 그대로 옮긴다.

| 조건 | 값 |
|---|---|
| OS | **리눅스** (윈도우도 길이 있으나 아래 별도) |
| GPU | 라데온 + 최신 amdgpu 드라이버 |
| 파이썬 | **3.12** |
| 그 밖 | CMake 와 C/C++ 빌드 환경, Git |
| 실측 | **RX 9060 XT (gfx1200) 로 anima 1024x1024 한 장 약 22초** (ROCm 7.14 대비 3초 단축) |

**1) ROCm 설치** — ROCm 7.14부터 **TheRock** 을 통해 배포되어 시스템 전역 설치 없이 pip 로 깐다.

```
pip install --index-url https://rocm.nightlies.amd.com/whl-multi-arch/ "rocm[libraries,devel,device-gfx1200]"
```

`device-{id}` 의 `{id}` 는 자기 GPU 의 gfx id 로 바꾼다 (RX 9060 이면 `gfx1200`).
공식 가이드: `https://github.com/ROCm/TheRock/blob/main/RELEASES.md`

> ⚠ **함정 1 — torch 를 나중에 깔면 ROCm 이 내려간다.**
> ROCm 만 단독 설치하면 문제없지만 **pytorch 를 따로 설치하면 ROCm 이 7.15 로 다운그레이드된다.**
> 그래서 `torch` · `torchvision` 과 **각각의 장치 패키지** whl URL 을 직접 나열해 **한 번에** 설치해야 한다
> (`torch-2.14.0a0+rocm10.1.0a20260806-cp312`, `torchvision-0.29.0a0+rocm10.1.0a20260806-cp312`, `amd_torch_device_{id}`, `amd_torchvision_device_{id}`).
> `triton` 과 `torchaudio` 는 그냥 설치하면 된다.

> ⚠ **함정 2 — 장치 패키지를 안 깔면 죽는다. 이게 제일 크다.**
> **gfx1200 계열(RX 9000번대)과 gfx1100 계열(RX 7000번대)** 은 추가 장치 패키지까지 깔아야 한다.
>
> ```
> amd_torch_device_gfx12_0    # RX 9000번대
> amd_torch_device_gfx110x    # RX 7000번대
> ```
>
> 안 깔면 ComfyUI 가 **`hipErrorInvalidValue`** 를 뿜고 죽는다. 댓글 6번이 4시간을 헤매다 이슈까지 올렸던 바로 그 증상이다.

**2) 초기화·검증**

```
rocm-sdk init
rocm-sdk test
```

**3) 실행 환경변수** — launch.sh 에 몰아넣는다.

```sh
TORCH_BLAS_PREFER_HIPBLASLT=0
USE_ROCM_AITER_ROPE_BACKEND=0
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE
TORCHINDUCTOR_FX_GRAPH_CACHE=1      # torch.compile 시간을 크게 줄여 준다 (강력 권장)
```

```
python main.py --use-flash-attention
```

라데온은 **dynamic-vram 이 기본 비활성**이라 필요하면 `--enable-dynamic-vram --fast-disk` 를 붙인다.

**4) flash attention 빌드** — 설치되면서 **기존 triton 을 강제로 갈아치우므로 빌드 뒤 AMD 저장소에서 triton 을 한 번 더 설치**한다 (댓글 5번은 `--no-deps` 를 줘도 triton 버전이 바뀌더라며 확인을 권한다).

```
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" pip install --no-deps --no-build-isolation .
```

**대안 설치법 (댓글 4번)**

```
uv pip install --pre -U --index-url https://rocm.nightlies.amd.com/whl-multi-arch/ \
  "torch[device-gfx1100]==2.14.0a0+rocm10.1.0a20260806" "torchvision[device-gfx1100]" torchaudio
```

### 성능은 어디까지 왔나

| 환경 | Anima 1024x1024 |
|---|---|
| RX 9060 XT + ROCm 10.1 + flash-attn(triton) | 약 **22초** |
| **R9700** + comfy-kitchen HIP + flash-attn(CK) | **12.51초 (2.43 it/s)** — RTX 3090 에 거의 근접 |
| R9700 + sage-attn | 14.56초 (2.10 it/s) |

R9700 쪽 실측글의 환경변수 네 개가 성능에 직결된다 (178367683, 2026-07).

```
COMFYUI_ENABLE_MIOPEN=1
MIOPEN_FIND_MODE=6                       # 3(HYBRID) 또는 6(TRUST_VERIFY) 이어야 캐싱된다
MIOPEN_USER_DB_PATH="/ai/.cache/miopen"
PYTORCH_HIP_ALLOC_CONF="expandable_segments:True"
```

> `MIOPEN_FIND_MODE` 를 **2(FAST)** 로 두면 ComfyUI 재시작 때마다 **최초 VAE 디코드가 10초 넘게** 걸린다.
> flash-attn 을 **CK 백엔드**로 빌드하면 가장 빠르지만 `MAX_JOBS=8 BUILD_TARGET="rocm" python setup.py bdist_wheel` 이 **하루 종일** 걸린다.

### 윈도우에서 쓰려면

윈도우 길도 있다. 다만 **포터블의 임베디드 파이썬(`python_embeded`)에 깔아야 한다**는 것이 핵심이다 (160654263, 2026-01).

1. 그래픽 드라이버를 **아드레날린 26.1.1** 로 업데이트
2. `https://github.com/Comfy-Org/ComfyUI/releases` 에서 `ComfyUI_windows_portable_amd.7z` 다운로드
3. `ComfyUI_windows_portable\python_embeded` 로 이동해 터미널을 연다
4. ROCm SDK 4개 + torch 계열 3개를 설치

```
.\python_embeded\python.exe -s -m pip install --no-cache-dir <URL>
```

> ⚠ 파일명에 `cp312` 가 박혀 있듯 **파이썬 3.12 전용 휠**이다. 3.14 에서는 이렇게 막힌다.
> ```
> ERROR: torch-2.9.1+rocmsdk20260116-cp312-cp312-win_amd64.whl is not a supported wheel on this platform
> ```

SageAttention 도 라데온용 whl 을 직접 빌드해 공유한 사례가 있다(9070XT 기준 스텝당 약 11.5초). 다만 **ComfyUI portable 0.30.0 에서만 동작하고 0.31.0 은 버그로 안 됐다** (179413848, 2026-08).

→ [ComfyUI 쓰는 법](comfyui.md) · [오류 해결](troubleshooting.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [라데온 stable-diffusion-webui 세팅 가이드 22.10](https://arca.live/b/aiart/60447786) · [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 … 26.08](https://arca.live/b/aiart/179176367) · [AMD R9700 comfy-kitchen HIP PR + … 26.07](https://arca.live/b/aiart/178367683) · [라데온 7900xtx 찍먹 입문 정보 26.03](https://arca.live/b/aiart/165090900)</small>

??? note "근거 7건 전부 보기"
    [라데온 stable-diffusion-webui 세팅 가이드 22.10](https://arca.live/b/aiart/60447786) · [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 … 26.08](https://arca.live/b/aiart/179176367) · [AMD R9700 comfy-kitchen HIP PR + … 26.07](https://arca.live/b/aiart/178367683) · [라데온 7900xtx 찍먹 입문 정보 26.03](https://arca.live/b/aiart/165090900) · [RX 9000용 torch+rocm 업데이트 + sage 빌… 26.07](https://arca.live/b/aiart/176063226) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848) · [라데온용 컴피 rocm 업데이트 방법 다시 알아옴 26.01](https://arca.live/b/aiart/160654263)

## 라데온 RDNA4(RX 9000) — sage 가 들어간 포터블 배포본 (2026-08)
<small>2026-08 기준 · 근거 1건</small>

RDNA4(라데온 **9000번대**)를 쓴다면 위의 리눅스·ROCm 경로를 밟기 전에 **윈도우용 포터블 배포본**이 먼저다.

```
https://huggingface.co/datasets/qweqweewqe7/ComfyUI_windows_portable_sage_Rdna4
```

| | |
|---|---|
| 들어 있는 것 | **ComfyUI 0.30.1 + SageAttention**, ROCm 은 **7.14 정식 버전**으로 교체 |
| 대상 | **RDNA4 (RX 9000 시리즈)**. 기존 0.26.0 판은 내려갔다 |
| RDNA3 | 아마 될 것 같지만 **테스트되지 않았고**, 그 경우 **sage 는 작동하지 않을 가능성이 높다** |

### ⚠ 내장 GPU 를 잡아 버리는 경우

댓글에서 **RX 9060 · RX 9060XT 16GB 구동 성공**이 확인됐는데, 그 전에 `run_amd_gpu.bat` 에 두 줄을 넣어야 했다.

```bat
set "TORCHINDUCTOR_BUNDLE_TRITON_INTO_FX_GRAPH_CACHE=1"
set "HIP_VISIBLE_DEVICES=1"
```

노드 업데이트까지 전부 마치면 잘 돌아간다는 보고다.

| 실측 (832x1216) | |
|---|---|
| int8 양자화 모델 | 11.7초 |
| + ANIMA 고속 로라 | **10초 미만** |
| 재실행 | **2.5초** (첫 생성만 느린 것이 정상) |

*(한 글 + 그 댓글의 보고다. RDNA3 이하는 위의 ROCm 절을 본다.)*

→ [ComfyUI 쓰는 법](comfyui.md) · [오류 해결](troubleshooting.md)

<small>근거 — [rdna4용 comfyui 0.30.1 + sage 26.08](https://arca.live/b/aiart/178869944)</small>

## 인텔 아크(Arc) — 되지만 하위호환이 나쁘다 (B580 실측, 2026-06)
<small>2026-06 기준 · 근거 2건 · 자료 엇갈림</small>

엔비디아도 라데온도 아닌 세 번째 갈래다. **되긴 되지만 NVIDIA 처럼 그냥 돌아가지는 않는다.**
2026년 6월, **인텔 아크 B580(40만원대)** 으로 ComfyUI + ANIMA 를 굴려 최적화까지 마친 실측 보고가 근거다.

**테스트 환경** — AMD 5700X3D / DDR4 3200 128GB / **B580(PCIe 4.0x8, 200W)** / **Ubuntu 26.04** / **Python 3.14** /
`wheels-pytorch-py3.14-20260611`. ANIMA 기본 워크플로 **1024x1024 / 30 steps** 로 5회 생성해 측정했다.

| 구성 | First Run | 2~5회 평균 | it/s | 배수 |
|---|---|---|---|---|
| 최적화 없음 | 22.79초 | **19.62초** | 1.55 | 1.00x |
| **Triton** | 20.51초 | **16.66초** | 1.83 | 1.18x |
| **Triton + torch.compile** | 29.43초 | **15.02초** | 2.03 | **1.31x** |

**torch.compile 은 첫 실행이 오히려 느려진다**(컴파일 시간). 그다음부터가 빠르다.

**다른 GPU 와 비교** (같은 기준, 2~5회 평균)

| GPU | 시간 | it/s |
|---|---|---|
| Intel Arc **B580** | 15.02초 | 2.03 |
| AMD **R9700** | 12.85초 | 2.41 (1.17x) |
| **RTX 3090** | **11.66초** | 2.63 (1.29x) |

> ⚠ **이전 R9700 글의 수치가 정정됐다.**
> "R9700 이 RTX3090 보다 소폭 빠르다" 고 했던 것은 **RTX3090 에 전력 제한을 걸어 둔 것을 잊은 탓**이고,
> **전력 제한을 풀면 RTX3090 이 가장 빨랐다.** 벤치 글을 읽을 때 전력 제한 여부를 확인해야 하는 이유다.

### 적용법 (Ubuntu 기준)

**Triton 은 실행 인자 하나면 끝이다.**

```
--use-triton-backend
```

**torch.compile 은 손이 많이 간다.**

1. `https://dgpu-docs.intel.com/installation-guides/installing-packages-from-the-intel-ppa.html` 에서 요구하는 패키지를 전부 설치하고 **oneAPI Toolkit** 설치
2. 기존 `torch` · `torchvision` · `torchaudio` · `triton-xpu` 제거
3. `intel-xpu-backend-for-triton` 의 Action(`https://github.com/intel/intel-xpu-backend-for-triton/actions/workflows/nightly-wheels.yml`)에서 휠을 받아 압축을 풀고

```
uv pip install *.whl
source /opt/intel/oneapi/setvars.sh     # 실행 전 환경변수
```

4. **`TorchCompileModel` 노드를 모델 사이에 연결**한다 (위치는 무관)

### 인텔에서만 다른 것들

| | |
|---|---|
| **dtype** | `fp16` 으로 두면 **`bf16` 보다 오히려 느리다** (역전) |
| **attention** | AMD 와 달리 **SDPA 말고 돌아가는 것이 없다.** `flex attention` 커스텀 노드는 오히려 느렸다 — **사실상 fa4 백엔드라 CUDA 가 아니면 의미가 없다**(댓글) |
| 전성비 | 약 **170W** 근처 (8% 성능 저하로 30W 절감) |

### ⚠ 공식 포터블은 나왔지만, 지원 GPU 목록을 그대로 믿으면 안 된다 (2026-04)

인텔 Arc 용 **ComfyUI windows-portable** 이 공식으로 등장했다 (`https://github.com/Comfy-Org/ComfyUI#windows-portable`).
본문이 옮긴 **PyTorch 기준 지원 GPU 목록**은 아래와 같다.

| 분류 | 예 |
|---|---|
| Arc A 시리즈 외장 | A770, A750 |
| Arc B 시리즈 외장 | B580, B570 |
| Core Ultra 1세대 **메테오레이크-H** 내장 | Core Ultra 5 125H |
| Core Ultra 2세대 **애로우레이크-H** 내장 | Core Ultra 5 225H |
| Core Ultra 2세대 **루나레이크** 내장 | Core Ultra 5 226V |
| Core Ultra 3세대 **팬서레이크** 내장 | Core Ultra 5 322 |

> ⚠ **댓글 정정 — 이 목록을 그대로 믿으면 안 된다.**
> 목록의 애로우레이크-H 와 **같은 세대인 데스크톱용 애로우레이크-S 내장 그래픽**은
> **`text encoder model load` 단계에서 멈추고 진행되지 않는다**는 보고가 있다.
> **인텔은 아키텍처가 동시대라도 지원 모델 목록에 없으면 안 되는 경우가 흔하다** — 아래 '총평' 의 하위호환 문제와 같은 이야기다.

또 다른 댓글의 두 가지: **VRAM 이 많다고 GPU 여러 장을 묶어 합산해 쓸 수는 없다**(엔비디아끼리도 마찬가지이며, `multigpu` 계열은 CFG 1 을 넘는 모델만 두 장에 나눠 돌린다).
Arc **B70** 은 VRAM 32GB 에 연산 성능이 4070 Ti 소폭 아래 수준이고 출시 초기 가격은 180만원대였다.

### 총평

> **Anima 같은 작은 모델을 돌리기에는 가성비가 매우 좋지만, NVIDIA 처럼 바로 돌아가지 않고 버전별 하위호환이 심각하게 나쁘다.**

⚠ **영상 쪽은 이야기가 다르다.** MiniMax H3 영상 생성에서는 Intel B580 이 세 시간 씨름 끝에 **구동 실패**로 보고됐다
(int8convrot 1회 13분 → 2회차 `UR_LOST`, fp8 은 **BSOD**) → [오류 해결](troubleshooting.md).
**정지 이미지는 되고 영상은 아직 아니다**로 읽는 것이 맞다.

→ [ANIMA](anima.md) · [VRAM·속도 최적화](vram.md) · [오류 해결](troubleshooting.md)

<small>근거 — [B580 생성속도 최적화 (Anima) 26.06](https://arca.live/b/aiart/173585515) · [인텔 Arc GPU용 ComfyUI windows-porta… 26.04](https://arca.live/b/aiart/168348535)</small>

## 글카가 없거나 ROCm 이 안 될 때 — stable-diffusion.cpp 로 우회
<small>2026-07 기준 · 근거 2건</small>

**"글카가 없으면 못 한다" 는 완전히 맞는 말은 아니다.** ComfyUI 는 못 쓰지만
**stable-diffusion.cpp**(llama.cpp 의 이미지 생성판)를 **Vulkan** 백엔드로 빌드하면 ANIMA 가 돌아간다.
**결론부터 — 되긴 되는데 매우 느리다.** 그래도 ROCm 미지원 하드웨어나 내장그래픽에서 유일한 길이다.

두 편의 실사용 기록이 근거다 — 노트북 **내장그래픽(Ryzen 4600H, GCN 5.0, 램 16GB 듀얼채널)** 과
채굴용으로 풀린 **AMD BC-250**(ROCm 미지원이라 ROCm 시도는 실패).

### 1) 빌드

**윈도우** — 파워쉘에서 준비물부터 깔고 **재부팅**한다.

```powershell
winget install --id Kitware.CMake -e
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudio.2022.BuildTools --override "--passive --wait --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
winget install --id KhronosGroup.VulkanSDK -e
```

```
git clone --recursive https://github.com/leejet/stable-diffusion.cpp
cd stable-diffusion.cpp && mkdir build && cd build
cmake .. -G "Visual Studio 17 2022" -A x64 -DSD_VULKAN=ON -DCMAKE_CXX_FLAGS="/bigobj" -DCMAKE_C_FLAGS="/bigobj"
cmake --build . --config Release --parallel
```

⚠ **이 환경에서는 `/bigobj` 를 넣어야 컴파일이 됐다.** `ERROR` 글자 없이 끝나면 성공이고 실행 파일은
`stable-diffusion.cpp\build\bin\Release\sd-cli.exe` 다.

**리눅스(Arch 계열)**

```sh
sudo pacman -S --needed base-devel git cmake ninja vulkan-headers vulkan-icd-loader vulkan-tools shaderc spirv-tools
git clone https://github.com/leejet/stable-diffusion.cpp && cd stable-diffusion.cpp
cmake -B build -DSD_VULKAN=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
```

> **빌드가 귀찮으면 안 해도 된다(댓글).** 릴리즈 페이지에 **Vulkan 빌드를 포함한 prebuilt 바이너리**가 있다.
> `https://github.com/leejet/stable-diffusion.cpp/releases`

### 2) 모델 — 여기서 많이 막힌다

| | |
|---|---|
| 형식 | safetensors · gguf 둘 다 되지만 **BF16 은 안 돌아간다.** **fp8 또는 Q8 GGUF 이상**이어야 한다 |
| 구성 | **vae 와 텍스트 인코더를 따로 받아** `--vae` `--llm` 으로 지정한다 (ANIMA 면 `qwen_image_vae` + `qwen_3_06b_base`) |
| ⚠ 필수 인자 | **`--vae-tiling` 이 없으면 RAM 부족 에러**가 난다 |

### 3) 실행

```
sd-cli.exe --diffusion-model <모델> --vae <qwen-image-vae> --llm <qwen 3 0.6B> \
  --lora-model-dir <로라 폴더> --prompt "... <lora:로라파일명(확장자제외):1>" --negative-prompt "..." \
  --width 512 --height 512 --steps 8 --cfg-scale 1 --seed -1 \
  --vae-tiling --sampling-method euler -o <출력경로>
```

`--steps 8` 은 **터보가 아니면 느려서 못 돌리기 때문**이다.
매번 긴 명령을 치기 싫으면 `sd-server` 로 띄운다.

```
./build/bin/sd-server --diffusion-model <gguf> --vae <vae> --llm <text encoder> \
  --diffusion-fa --vae-tiling --listen-ip 0.0.0.0 --listen-port 7860 --verbose
```

⚠ **`--listen-ip` 를 127.0.0.1 로 두면 같은 네트워크의 다른 컴퓨터에서 접속할 수 없다.** `0.0.0.0` 으로 둔다.

> **기본 웹 UI 는 매우 빈약하다** — **반복 생성도 자동 저장도 없다.** 두 글이 같은 불만을 적었다.

### 4) NAIA 에 붙이기 — `/sdapi/v1/progress` 가 없다

**이 절이 이 경로의 진짜 알맹이다.**

> stable-diffusion.cpp 는 A1111 WebUI **API 호환을 지원하지만 잘 안 쓰는 엔드포인트 구현을 생략했고,
> 하필 NAIA 가 연결 확인에 쓰는 `/sdapi/v1/progress` 가 빠져 있다.** 그래서 그냥 연결하면 실패한다.

해결은 **얇은 wrapper 하나를 앞에 두는 것**이다. (200 코드와 `"progress"` 키가 든 JSON 을 돌려주면 된다.)

```
https://pastebin.com/1r3a5kwP     →  naia_wrapper.py 로 저장 후  python naia_wrapper.py
실행 순서 : sd-server(7861)  →  naia_wrapper(7860)  →  NAIA
NAIA 의 webui 설정에 127.0.0.1:7860 을 넣는다
```

**NAIA 2.0.30 에서 함께 고치면 좋은 것** — NAIA 는 5분 안에 그림이 안 나오면 에러로 보고 재시도하는데
내장그래픽은 큰 해상도에서 5분을 넘기기 일쑤다.

```
NAIA-Portable\resources\naia-backend\core\api_service.py
  session.post(api_endpoint, headers=headers, json=payload, timeout=300)   →   timeout=3600
```

### 실측 — 각오할 속도

| 환경 | 조건 | 시간 |
|---|---|---|
| 내장그래픽 + ANIMA turbo Q8 GGUF | 512x512 | 약 **100초** |
| 〃 | 1024x1024 | 약 **500초** |
| 〃 | 1532x1532 | **램 부족 에러** |
| AMD BC-250 (Vulkan) | 768x1024 / 35스텝 / cfg 4 / `er_sde` + `simple` | **227초** |

> 저사양에서는 **스펙트럼 같은 캐싱 테크닉의 속도 향상이 거의 없었고 flash attention 은 오히려 느려져 껐다.**
> 램 8GB 라면 Q3 GGUF 에 텍스트 인코더도 세게 양자화하면 될 수도 있다(**미검증**).

→ [ANIMA](anima.md) · [NovelAI](nai.md) · [모델 고르기](models.md)

<small>근거 — [오래된 노트북 내장그래픽으로 ANIMA 돌려보기 26.07](https://arca.live/b/aiart/176691794) · [bc250으로 짤뽑아보기 26.07](https://arca.live/b/aiart/176880815)</small>

## 글카 없이 — 지금도 살아 있는 무료 경로 (Comfy Cloud)
<small>2026-03 기준 · 근거 4건</small>

위 '낡은 방식 — 무료 클라우드로 돌리던 시절' 의 선택지는 대부분 죽었지만, **지금 살아 있는 무료 경로가 하나 있다.**
**로컬 글카 없이 ANIMA 를 찍먹해 보고 싶을 때** 쓸 만하다 (2026-03).

| | |
|---|---|
| 무료 티어 | **매달 400 크레딧** ($2 상당) |
| 환경 | **RTX PRO 6000**. **KJNodes · VideoHelperSuite(VHS) 같은 필수 커스텀 노드가 이미 설치**돼 있고 **ANIMA 모델도 올라와 있다** |
| 실측 | ANIMA **30스텝 한 장에 7~8초, 크레딧 2개** |
| 즉 | **매달 200장 정도**를 무료로 뽑을 수 있다 |

> (댓글: 7~8초면 거의 5090급인데 PRO 6000 치고는 느린 편이라 전력 제한이나 max-q 버전일 수 있다.)

### ⚠ 제약 두 가지

| | |
|---|---|
| **로라를 못 올린다** | 로라 임포트는 **월 $35 플랜에서만** 가능하다 |
| **nsfw 는 하지 마라** | **브라우저를 닫았다 다시 들어가도 생성한 이미지가 남아 있다** = 서버에 보관된다는 뜻이다 |

**한 글에서만 언급된** 정보다 (163815149, 2026-03).

→ [ANIMA](anima.md) · [자원](resources.md)

### 옛 무설치 경로 — 지금은 정책이 달라졌을 것을 전제로 본다

| 경로 | 무엇 | 시점 주의 |
|---|---|---|
| **PixAI** (`https://pixai.art`) | **설치도 그래픽카드도 필요 없는 무료 온라인 생성 서비스.** PC 사양이 낮아 WebUI 를 못 돌리고 NovelAI 구독료도 부담스러운 사람이 실제로 만족스러운 결과를 얻은 기록이 있다 (92064917) | **2023-11 기준** — 현재 무료 정책과 모델 목록은 달라졌을 수 있다 |
| **RunPod 서버리스 API** | Anything 모델을 무료 오픈베타로 공개했던 시절. **네거티브 프롬프트를 넣을 수 없고 서버 쪽 NSFW 필터**가 걸려 있어 필터에 걸리면 결과가 비어 나왔다 (66830656) | **2023-01, 무료 오픈베타** — 지금은 그대로 쓸 수 없다. 역사적 기록 |
| **코랩 Diffusers 노트북** | OneFlow-Diffusers 로 1장을 7초에 뽑던 '하이퍼코랩'. **프롬프트 가중치 문법이 동작하지 않고 t2i 만 지원**했다 (69335887) | **2023-02, Diffusers 0.x + Python 3.8** — 지금 경로는 위 '무료 클라우드' 절과 Comfy Cloud |

> 이 시절 코랩 자료에서 아직 쓸모 있는 조각 둘 —
> **NSFW 안전 필터로 검은 이미지만 나올 때**(`Potential NSFW content was detected in one or more images. A black image will be returned instead.`)는
> `pipe.safety_checker = lambda **kwargs: (kwargs["images"], False)` 로 우회하고,
> 허깅페이스 로그인은 토큰 붙여넣기 대신 `from huggingface_hub import login` 후 `login()` 으로도 된다.
> 모델 로딩 시 `OSError: <repo> does not appear to have a file named scheduler_config.json` / 404 가 나면 **그 저장소에 Diffusers 형식의 `scheduler` 폴더가 없기 때문**이며, scheduler 폴더가 있는 저장소만 쓸 수 있다.

<small>근거 — [하이퍼코랩 - 초고속 이미지 생성 코랩 노트북 (7초만에 생… 23.02](https://arca.live/b/aiart/69335887) · [(월페이퍼 대회) 악마에게 몸을 빼앗긴 소녀 23.11](https://arca.live/b/aiart/92064917) · [Comfy Cloud Free tier 시작 (매달 400크… 26.03](https://arca.live/b/aiart/163815149) · [런팟 서버리스 api Anything 무료 오픈베타와 사용 … 23.01](https://arca.live/b/aiart/66830656)</small>

## 클라우드 GPU 를 빌려 돌리기 — RunPod · Vast.ai (불량 인스턴스 버리는 기준)
<small>2025-12 기준 · 근거 2건</small>

집 컴퓨터가 못 버티면 시간당 몇백 원에 GPU 를 빌린다. **두 서비스의 실사용 기록이 채널에 있다.**
공통 교훈이 하나 있다 — **불량 인스턴스를 빨리 버리는 것이 돈을 아끼는 길이다.**

### 버려야 할 신호

| 신호 | 판단 |
|---|---|
| `CUDA initialization failed. Exiting...` 이 뜨며 모델 다운로드가 멈춘다 | **그 서버의 GPU 가 고장난 것이다. 포드를 빨리 버리고 새로 만든다** |
| 허깅페이스·civitai 다운로드가 **10MB/s 이하** | 그 인스턴스는 버리고 새로 빌린다 (한 시간 돌려도 안 끝난다) |
| 로그에 `comfyui startup paused until instance provisioning has completed (/.provisioning present)` 만 **15분 이상** | 인스턴스가 맛이 갔다. 재실행하거나 다른 서버로 |

### RunPod — 도커 이미지로 밀키트처럼 (2025-10)

**런팟은 상태가 저장되는 게 아니라 초기화된 PC 를 매번 빌리는 개념**이라 세팅 반복이 문제인데, 그것을 도커 이미지로 없앤 배포가 있다.

| 항목 | 값 |
|---|---|
| 템플릿 | `rhplus-comfyui-video` (`template=9lkpdziphh`) — **템플릿 검색으로는 안 뜰 수 있다** |
| ⚠ CUDA | **12.9 기준으로 빌드했으므로 CUDA 버전 제한을 12.9 이상으로 수동 설정**해야 한다 |
| 볼륨 | 모델 전부 약 90GB (모델 2개면 46GB), 결과물 10GB |
| 모델 링크 | **세미콜론으로 구분**(`A;B;C`)해 넣으면 켜질 때 `diffusion_models` 로 자동 다운로드 |
| 접속 | `Download Done!` 과 `0.0.0.0:8188` 이 뜨면 Connect → ComfyUI. 2분 넘게 로딩이면 **Ctrl+F5** |
| 서버 타입 | Secure(비싸지만 다운로드 안정) / Community(저렴) / **Spot 은 인스턴스를 뺏길 수 있다** |

실측(720p 급, 2번째 생성부터, 업스케일 + 보간 포함): 기본 샘플러 약 **160초**, 스케줄드 샘플러 약 **200~240초**.
**끝나면 반드시 포드를 정리해 크레딧이 새지 않게 한다.**

### Vast.ai — 30분 세팅, 2회차부터 5분 (2025-12)

준비물은 Syncthing(파일 실시간 동기화), GitHub 계정, Vast.ai 계정, **civitai API 토큰**(로그인 없이 모델을 받으려면 필수),
허깅페이스 토큰(SAM3 처럼 접근 권한이 필요한 모델일 때만).

| 항목 | 값 |
|---|---|
| 가격 | RTX 5090 이 디스크 40GB 기준 **시간당 0.31~0.40 USD** |
| 최소 충전 | 본문 10 USD / **댓글 정정: 실제로는 5 USD** |
| 데이터 전송 요금 *(댓글)* | 별도로 붙는다. 실측 34.9GB 에 약 **0.003 USD/GB**, 합계 −0.09 USD 수준 |
| 버전 | **`cuda-12.9-auto`** (5090 속도 저하 방지) |
| 디스크 | 설정한 모델 총합 **+20GB**. 체크포인트 2개 + 로라 몇 개면 40GB, Wan 을 쓰면 65GB |
| 정지 보관비 | 40GB 기준 하루 약 0.53 USD |

`ai-dock/comfyui` 를 포크해 `config/provisioning/default.sh` 를 고치는 방식인데, **함정이 둘이다.**

> ⚠ ① **`ESRGAN_MODELS` 를 `UPSCALE_MODELS` 로 전체 치환**해야 한다. 현 ComfyUI 와 경로가 다르다.
> ⚠ ② **포크 저장소는 반드시 Private** — 아니면 스크립트에 넣은 API 토큰이 다 털린다.

링크는 큰따옴표 안에, 앞에 탭 공백을 넣고, **`#` 를 붙이면 주석 처리되어 그 파일만 건너뛴다.**
Key 에 `CIVITAI_TOKEN` 을 넣을 때는 **옆의 `+` 버튼을 반드시 눌러야** 추가된다.

**결과물 회수는 Syncthing 으로 한다** — 로컬은 폴더 유형 '수신 전용' + 파일 수신 순서 '오랜 파일 순',
원격은 `/workspace/ComfyUI/output` 을 '송신 전용'.
⚠ **공유 설정에서 자물쇠는 절대 누르지 마라(파일이 다 깨진다).** 양쪽 다 압축은 '하지 않음' 으로 두면 EXIF 가 보존되고 업로드도 빨라진다.

서버를 고를 때는 정렬을 Price(inc.) 로 두고, 카드의 숫자를 본다 —
업로드 속도(↑)는 Syncthing 속도, 다운로드 속도(↓)와 포트 수는 초기 구성 시간,
**디스크 대역폭은 최소 2000 MB/s 이상.** 파키스탄·인도·독일은 실제 다운로드가 박살나는 경우가 있어 피한다.

→ [비디오 생성](video-generation.md)

<small>근거 — [30분내로 끝내는 Vast.ai 사용법 (시간당 0.3$로 … 25.12](https://arca.live/b/aiart/158013422) · [런팟 RTX 5090용 WAN 2.2 딸깍 도커 이미지 25.10](https://arca.live/b/aiart/151440980)</small>

## 저사양·영상용 — Wan2GP (2025-05)
<small>⚠️ 2025-05 기준 · 근거 2건</small>

저사양 GPU 용 영상 생성 프론트다. 최적화와 업스케일이 내장된 것이 장점이고 확장성은 ComfyUI 보다 떨어진다.

```
git clone https://github.com/deepbeepmeep/Wan2GP.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install torch==2.6.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cu124   # 50시리즈는 2.7.0
pip install sageattention-2.1.1+cu126torch2.6.0-cp310-cp310-win_amd64.whl                                 # 파이썬 3.10
python wgp.py
```

- configuration 에서 **sage2** 를 켜면 720x720 이 **20분 → 10분**으로 줄었다 (RTX 4060 Ti 16GB 기준).
- 파이썬 3.11 이면 wheel 파일명을 `cp311-cp311-win_amd64.whl` 로 바꾼다.
- 댓글: `pip uninstall torch torchvision torchaudio` 단계를 **건너뛰니** 정상 기동했다는 보고가 있다.

→ [비디오 생성](video-generation.md)

<small>근거 — [저사양, 작은뇌를 위해 간단히 적는 Wan2.1 사용법 25.05](https://arca.live/b/aiart/137466035) · [Wan2GP 미니맥스 H3 나왔네 26.08](https://arca.live/b/aiart/179281753)</small>

## 포터블 이사 — 커스텀 노드와 의존성을 통째로 옮기기 (2026-02)
<small>2026-02 기준 · 근거 1건</small>

ComfyUI 를 새 버전으로 갈아탈 때 가장 아까운 것은 **커스텀 노드와 그 의존성을 다시 맞추는 시간**이다.
그 반복 작업을 자동화한 스크립트가 있다 (2026-02). **완전 자동은 아니고, 사람마다 다른 부분만 미리 적어 두면 두고두고 쓴다.**

```
https://file.baepoyong.com/share/CgMioCkk
```

### 왜 매니저로는 안 되나

이 스크립트의 존재 이유가 곧 답이다 (→ [ComfyUI 쓰는 법](comfyui.md) 의 '미싱 노드' 에도 적어 두었다).

> 커스텀 노드는 보통 PyPI 에서 라이브러리를 받는데 **특정 라이브러리는 특정 버전에서 설치가 안 되고,
> 제작자가 `requirements` 에 의존성을 빼먹기도 한다.** 그러면 `no module named ~` 로 `import failed` 가 계속 뜬다.
> 그럴 때는 **직접 빌드하거나 남이 미리 빌드한 wheel 을 깔아야 하는데 매니저는 그걸 지원하지 않는다.**

**의존성이 깨지는 대표적 계기는 PyTorch 버전업과 Python 버전업이다.** 그때 아래 txt 3개만 갱신하면 된다.

### 미리 채워 두는 파일 셋

| 파일 | 무엇을 적나 | 작성자 예시 |
|---|---|---|
| `wheel.txt` | 따로 설치한 **휠 파일 주소** | `insightface-0.7.3-cp313-cp313-win_amd64.whl` , `sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl` |
| `replace.txt` | **지우고 다시 깔** 라이브러리 이름 | `onnxruntime-gpu` |
| `requirements.txt` | **따로 설치할** 라이브러리 | `onnxruntime-gpu --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-13/pypi/simple/` , `argostranslate` , `triton-windows` |

> **정석은 라이브러리로 먼저 시도하고 안 되면 wheel 을 찾는 것이다.**

### 파일 배치와 실행

```
[기존 포터블 경로]  (python_embeded 가 있는 곳)
  git_address_checker.py , exporter.bat        ← 이 둘만

[새 포터블 경로]
  나머지 전부  +  생성된 git_address.txt
```

| | |
|---|---|
| 1 | **기존** 쪽에서 `exporter.bat` 실행 → **`git_address.txt`** 가 생긴다 (쓰던 커스텀 노드들의 깃 주소. ComfyUI 본체는 제외된다) |
| 2 | 직접 만들어 쓰던 커스텀 노드는 **`manual_install.txt`** 에 폴더 이름으로 남는다 |
| 3 | `git_address.txt` 를 **새** 포터블 경로로 옮기고 **`installer.bat`** 실행 |
| 4 | 스크립트가 wheel 설치 → 라이브러리 교체 → 추가 라이브러리 설치 → 커스텀 노드 `git clone` · 의존성 · `install.py` 까지 돌린다 |

**결과 확인**

| 파일 | 뜻 |
|---|---|
| `install_warning.txt` | `install.py` 를 못 돌린 것. **문제없을 수도 있고**, 첫 실행 때 ComfyUI-Manager 스캔이 한 번씩 다시 돌려 주기도 한다 |
| `install_failed.txt` | `git clone` 이나 의존성 설치에서 **실패한 것** |

(없으면 파일이 생기지 않는다.)

### ⚠ 이 스크립트로도 안 옮겨지는 것

- **외부에서 받아야 하는 모델 파일** (ipadapter 모델 등)
- **커스텀 노드 폴더 안의 사용자 설정 파일** (자동완성 데이터 등)

둘 다 따로 옮겨야 한다. 모델 폴더 자체를 공유하는 방법은 위 **'모델 폴더를 이미 갖고 있다면'** 을 본다.

> **한 글에서만 제시된 스크립트다** (162198611, 2026-02). 다만 '업데이트하지 말고 새로 받으라' 는 통합팩 원칙과
> **버전별 인스턴스로 나눠 쓰기**(→ [ComfyUI 쓰는 법](comfyui.md))는 같은 문제를 다루는 다른 해법이므로 함께 읽으면 좋다.

→ [ComfyUI 쓰는 법](comfyui.md) · [오류 해결](troubleshooting.md)

<small>근거 — [comfyui 포터블 이사가는거 도와주는 스크립트 26.02](https://arca.live/b/aiart/162198611)</small>

## A1111 계열 재설치 — 지우는 것과 남기는 것
<small>⚠️ 2024-03 기준 · 근거 2건</small>

A1111 계열이 꼬였을 때 **폴더를 통째로 지우고 다시 받는 것은 최악의 선택**이다. 지울 것과 남길 것이 정해져 있다.

### 지우는 것 / 남기는 것

```
지운다   :  venv        (필요하면 repositories 까지)
그다음   :  webui-user.bat 을 다시 실행하면 알아서 다시 받는다
```

새 폴더로 옮겨 살려야 하는 것 — **이걸 안 옮기면 설정과 모델을 전부 잃는다.**

```
embeddings/  extensions/  extensions-builtin/  log/  models/  outputs/
config.json  ui-config.json  쓰던 webui-user.bat
```

### 파이썬 버전 — 여기서 반이 막힌다

| | |
|---|---|
| 필요한 것 | **Python 3.10.X** (3.10.6 이상, **3.10.11 권장**) |
| 설치할 때 | **`Add python.exe to PATH` 체크는 필수** |
| ⚠ 3.11 / 3.12 / 3.13 | **`INCOMPATIBLE PYTHON VERSION` 이 뜨며 설치가 멈춘다** |

**윈도우 계정명이나 설치 경로 폴더 이름에 한글·공백이 있으면 정상 설치·실행이 안 된다.**
계정명이 한글이라 못 바꾸면 **C 드라이브 최상위에 영문 폴더를 만들어 거기에 설치**한다.

> **실행하면 함께 뜨는 검은 CMD 창이 본체다.** 브라우저는 접속기일 뿐이라 **CMD 를 닫으면 안 된다** —
> 진행도·속도·오류가 전부 거기 찍힌다. `Connection errored out` 의 흔한 원인이 이것이다.

### 시대에 따라 바뀐 값 하나

⚠ **옛 글을 그대로 따라 하면 그림이 이상하게 나온다.**

| WebUI 버전 | 시그마 노이즈(sigma noise) |
|---|---|
| ~ 1.5.2 | `0.2` |
| **1.6.0 ~** | **`1`** |

### 어텐션 인자

```bat
:: 기본 (xformers 가 sdp 보다 VRAM 을 덜 먹는다)
set COMMANDLINE_ARGS= --xformers --xformers-flash-attention --opt-channelslast --enable-insecure-extension-access

:: sdp 를 쓰겠다면
set COMMANDLINE_ARGS= --opt-sdp-no-mem-attention --opt-channelslast --enable-insecure-extension-access
```

### cuDNN 덮어쓰기

받은 zip 의 `bin` 폴더 내용물을 아래에 덮어쓴다.

```
stable-diffusion-webui\venv\Lib\site-packages\torch\lib
```

⚠ **1.8.0 부터 CUDA 12.1 로 바뀌어 'cuDNN 8.X for CUDA 12.X' 를 받아야 하고 cuDNN 9.0 은 적용할 수 없다**
(`https://developer.nvidia.com/rdp/cudnn-archive`).

### 버전별 기본 스택 (참고용)

| WebUI | torch | CUDA | xformers |
|---|---|---|---|
| 1.3.2 | 2.0.1 | 11.8 | 0.0.17 |
| 1.4.0 | 2.0.1 | 11.8 | 0.0.20 (자동 설치) |
| 1.8.0 | 2.1.2 | 12.1 | 0.0.23 |

> ⚠ **이 절차는 2026년 지금 그대로는 막힌다.** 위 **'⚠ 아래 낡은 방식을 따라 하기 전에'** 의
> `pkg_resources` · `setuptools 69.5.1` · **사라진 저장소** 세 관문을 먼저 넘겨야 한다
> → [오류 해결](troubleshooting.md). 원글 상단에도 '더 이상 유지·관리되지 않는다'는 안내가 붙어 있다.
> 다만 **절차 자체는 2026년까지도 그대로 동작한다는 후기가 계속 달렸다.**

→ [오류 해결](troubleshooting.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [누구나 따라할 수 있는 로컬 자동좌 WebUI 클린 설치 (… 23.06](https://arca.live/b/aiart/79413719) · [AI그림 채널 오류 해결책 모음 23.02](https://arca.live/b/aiart/70417374)</small>

## 휴대폰·다른 방에서 쓰기
<small>2026-02 기준 · 근거 6건 · 자료 엇갈림</small>

ComfyUI 를 `--listen` 옵션으로 실행하면 **같은 공유기 안의 휴대폰 브라우저**에서 쓸 수 있다.

```
http://<PC의 IP>:8188      예: http://192.168.0.7:8188
```

정확한 인자는 **`--listen 0.0.0.0`** 이고, 포터블이면 `run_nvidia_gpu.bat` 의 실행 줄
(`.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build ...`) 뒤에 붙인다.
내부망 IP 는 cmd 에서 `ipconfig` 를 쳐 **IPv4 주소(192.168.x.x)** 를 본다.

같은 Wi-Fi/LAN 이면 **ComfyBridge** 를 띄워 폰에서 t2i·i2v 를 돌리는 방법도 있다.

### 폰 화면에 맞춘 UI — comfyui-mobile-frontend (2026-02)

```
https://github.com/cosmicbuffalo/comfyui-mobile-frontend
접속: http://<PC 내부 IP>:8188/mobile
```

노드를 **세로로 정렬**해 보여 주고 워크플로우 패널·출력 미리보기·북마크·대기열 패널·이미지 뷰어·메타데이터 모달을 준다.
⚠ **본가는 아직 LoRA Manager 를 지원하지 않는다**(풀리퀘스트만 올라와 있다). 로라 매니저를 쓰려면 포크 쪽이다.

```
https://github.com/pccr10001/comfyui-mobile-frontend/tree/main
```

### 집 밖에서 — Cloudflare 퀵터널 (2026-02)

포트포워딩 없이 **임시로** 여는 가장 짧은 길이다. 아웃바운드로 Cloudflare 에 연결하고 Cloudflare 가 리버스 프록시를 맡는다.

```powershell
# cmd 가 아니라 PowerShell 에서
winget install --id Cloudflare.cloudflared
# 터미널을 껐다 켜고, --listen 0.0.0.0 을 붙인 실행 bat 을 먼저 띄운 뒤
cloudflared tunnel --url http://localhost:8188
```

실행하면 접속 주소가 표시된다. **터미널을 나가면 터널도 닫힌다.**
단점은 **주소가 지저분하고 실행할 때마다 바뀐다**는 것.

> ⚠ **ComfyUI 는 인증이 없다.** 외부망으로 열었으면 **쓰고 바로 닫는다.**
> 계속 쓸 거면 퀵터널이 아니라 **Tailscale·WireGuard 같은 VPN** 이 맞다.
> **iptime 공유기라면 내장 WireGuard 기능이 세팅도 쉽고 속도도 잘 나온다**(이중 공유기만 아니라면 — 댓글).

노드 화면이 폰에서 버겁다면 **App Mode** 를 쓴다 — 제작자가 고른 위젯(프롬프트·해상도·CFG·스텝·시드)만 보이는 화면으로 워크플로우를 돌릴 수 있다.

### 남에게 열어 주기 — Gradio 와 ngrok (A1111 계열, 2023)

'챈섭' 은 자기 PC 의 그림 생성기를 외부에 공개해 남들이 쓰게 해 주는 것이다.
**지금은 ComfyUI 가 주류라 그대로는 안 맞지만 원리는 그대로 쓸 수 있다.**

| | Gradio | ngrok |
|---|---|---|
| 여는 법 | `webui-user.bat` 의 `set COMMANDLINE_ARGS=` 줄에 `--share --gradio-auth ID:PW` 추가 | WebUI 를 그냥 켜고 포트(보통 7860)를 확인한 뒤 `ngrok http 7860` |
| 비번 | `--gradio-auth user:pw1234` | `ngrok http 7860 --basic-auth="user:pw123456"` (6자 이상) |
| 주소 | 실행하면 `Running on public URL: https://xxxx.gradio.live` | Forwarding 에 뜨는 주소 |
| ⚠ 제한 | **무료 계정은 3시간** — 3시간마다 다시 열어야 한다 | **시간 제한 없음** |
| 접속자 확인 | 없음 | **`http://127.0.0.1:4040`** 에서 IP 까지 보인다 |

즉 **장시간·불특정 다수에게 열 거면 ngrok** 쪽이다.
ngrok 토큰은 `https://dashboard.ngrok.com/get-started/your-authtoken` 의 값을 넣는다
(**Tunnel Agent Authtokens 페이지가 아니다** — 여기서 많이 틀린다).
ngrok 으로 연결했는데 로컬 주소만 보이면 출력창에서 **`ngrok connected to`** 를 검색하면 위쪽에 실제 주소가 있다.

**남이 못 하게 막을 기능 제한하기** — ⚠ **파일을 뜯어고치는 본문 방식보다 실행 인자가 낫다.**

| 방법 | |
|---|---|
| ✅ **실행 인자** | `--hide-ui-dir-config` (폴더 버튼 · i2i 배치 대체) , `--freeze-settings` (설정 탭 잠금) |
| ✅ 값 제한 | `ui-config.json` 에서 `txt2img/Batch count/maximum` , `txt2img/Sampling steps/maximum` , `txt2img/Width/maximum` 등을 낮춘다 |
| ❌ **하지 말 것** | **`modules/ui.py` 에서 settings 인터페이스를 주석 처리하면 모델·VAE 변경 시 에러가 나고 생성 결과가 콘솔에 찍히지 않는다** (댓글 지적, 근거: AUTOMATIC1111 issue #11769). 본문이 권한 방식이지만 부작용이 있다 |

**IP 밴은 ngrok Enterprise 유료 기능**이다 (Security > IP Policies > New IP Policy, Action: Deny, IPv4 는 `주소/32` · IPv6 는 `주소/128`).
⚠ **정책을 하나라도 만들면 기본이 전부 차단**이라 허용할 국내 IP 대역을 따로 추가해야 하고,
**'Use my I.P' 를 누르거나 Agent/API/Dashboard 를 건드리면 본인이 잠겨 ngrok 에 이메일로 문의해야 한다.**

> ⚠ **ComfyUI 는 불특정 다수에게 서빙하라고 만든 프로그램이 아니라 보안이 사실상 없다** → [ComfyUI 쓰는 법](comfyui.md) 의 '앱 모드'

<small>근거 — [ComfyUI App mode가 나왔길래 써봤다. 26.03](https://arca.live/b/aiart/164519826) · [(정보글) 챈섭 여는 법 ABC (gradio / ngrok… 23.05](https://arca.live/b/aiart/76388840) · [모바일 Comfy 구동 프론트 Web App 26.05](https://arca.live/b/aiart/170363616) · [comfy 모바일 ui 확장 괜찮은거 하나 있네 26.02](https://arca.live/b/aiart/162164907)</small>

??? note "근거 6건 전부 보기"
    [ComfyUI App mode가 나왔길래 써봤다. 26.03](https://arca.live/b/aiart/164519826) · [(정보글) 챈섭 여는 법 ABC (gradio / ngrok… 23.05](https://arca.live/b/aiart/76388840) · [모바일 Comfy 구동 프론트 Web App 26.05](https://arca.live/b/aiart/170363616) · [comfy 모바일 ui 확장 괜찮은거 하나 있네 26.02](https://arca.live/b/aiart/162164907) · [comfyui 원격접속하는법 26.02](https://arca.live/b/aiart/162190790) · [comfyui 앱모드 사용법 26.05](https://arca.live/b/aiart/171528258)

## A1111 계열 인페인트 옵션 (지금도 그대로)
<small>⚠️ 2022-10 기준 · 근거 1건</small>

2022년 글이지만 WebUI 계열의 인페인트 화면은 지금도 같다.

| 옵션 | 뜻 | 기본값 |
|---|---|---|
| 마스크 블러 | 마스크를 몇 픽셀 블러 처리할지 | **4** |
| 마스크된 부분 처리 옵션 | 마스크 안쪽을 어떻게 시작할지 | **원본 유지(Original)** |
| 전체 해상도로 인페인트하기 | 마스크 영역만 크기를 조정해 처리한 뒤 원래 사진에 되붙인다 | 끄기 |

- 마스크는 UI 에서 직접 그리거나 **외부 툴로 만든 마스크 이미지를 업로드**할 수 있다. 업로드하면 **흰색 부분이 인페인트 대상**이며 조금이라도 희면 포함된다.
- **'전체 해상도로 인페인트하기'** 를 켜면 큰 그림에서도 인페인트 대상만 훨씬 높은 해상도로 렌더링된다. 얼굴이 작아 뭉개질 때 쓰는 방법이다.

i2i 리사이징 3종: `리사이징`(종횡비가 안 맞을 수 있음) / `잘라낸 후 리사이징`(종횡비 유지, 튀어나온 부분 자름) / `리사이징 후 채우기`(종횡비 유지, 빈 공간 채움).

**i2i 배치** — 인풋 이미지 경로에 폴더를 넣으면 1:1 로 반복 처리한다. 저장 경로를 비우면 `outputs/img2img-images` 에 저장되고, 별도 지정 시 그 폴더를 **직접 만들어 둬야 한다**(자동 생성 안 됨). 완료돼도 결과창에는 안 뜬다.

**CLIP 분석 / DeepBooru 분석** — 업로드한 이미지에서 프롬프트를 역추출한다. CLIP 은 자연어 문장, DeepBooru 는 단부루 태그를 뱉는다.

<small>근거 — [WebUI 기본 사용법 정리 22.10](https://arca.live/b/aiart/61366565)</small>

## ⚠ 아래 '낡은 방식' 을 따라 하기 전에 — A1111·reForge 는 지금 그대로는 막힌다
<small>2026-08 기준 · 근거 7건 · 자료 엇갈림</small>

채널에서 가장 널리 도는 입문 설치글이 111903865 「AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지」(2024-07, 추천 71)다.
**본문만 읽고 그대로 따라 하면 2026년 지금은 막힌다.** 댓글에 본문을 뒤집는 정정이 두 개 있다.

| | 본문이 말하는 것 | 댓글이 말하는 것 |
|---|---|---|
| 어느 WebUI 를 쓰나 | "**처음 하는 사람은 그냥 리포지(reForge)를 쓰라**" 며 `git clone .../stable-diffusion-webui-reForge` 를 **가장 먼저** 제시 | **댓글 20번 — "절대 리포지를 쓰지 마"** (본문과 정반대) |
| 순정 A1111 은 도나 | `git clone` 뒤 `git switch dev` → `git pull` 하면 설치가 진행된다 | **댓글 21번 — 2026년부터 파이썬에 `pkg_resources` 가 빠져 초기 구동조차 안 된다** |

### 1. `pkg_resources` — A1111 이 아예 뜨지 않는다

> **2026년부터 파이썬을 설치해도 `pkg_resources` API 가 함께 설치되지 않는다.**
> A1111 은 이것을 쓰기 때문에 **초기 구동 자체가 실패한다.**

제작자가 올린 해결법을 댓글 22번이 링크했다. **그 이슈의 4번 항목**이 해당 처방이다.

```
https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/17201#issuecomment-3882017097
```

같은 계열 증상은 옛 구름IDE 판 댓글에도 그대로 남아 있다(작성자도 관리 중단을 알렸다).

```
ImportError: cannot import name 'packaging' from 'pkg_resources'
```

즉 **이 글대로 따라 하려면 위 이슈를 먼저 봐야 한다.** 아래 '낡은 방식' 절의 절차들도 같은 전제에서 읽어야 한다.

### 2. reForge — 본문과 댓글이 정반대다. 양쪽을 다 적는다

| 입장 | 근거 |
|---|---|
| **쓰라** | 111903865 **본문** (2024-07). "리포지는 이런 최적화가 미리 되어 있으니 건들지 말 것" 이라고까지 적었다 |
| **쓰지 마라** | 111903865 **댓글 20번** — "절대 리포지를 쓰지 마" / 119210516 **작성자 본인** — "모델을 바꿀 때마다 시간이 오래 걸리고 렉이 심해(모델 로딩 때 시스템 RAM 을 풀로드하고 VRAM 은 남는다) **결국 나는 현행 Forge 를 쓴다**", 댓글에도 "얘만큼 모델·로라 가져올 때 렉 걸리는 걸 못 봤다"는 동일 증상 보고 |

**정리** — reForge 를 **초보 기본값으로 권하는 본문 쪽이 지금은 소수설**이다. 실사용 보고와 댓글이 반대편에 있다.

### 그래서 지금은 무엇을 쓰나

위쪽 **'0. 세 갈래 중 하나만 고른다'** 로 돌아간다. 2026년 채널의 권고는 A1111·reForge 가 아니라 **Forge Neo** 또는 **ComfyUI 포터블**이다.

> 다만 111903865 의 **본문 지식 자체가 무가치한 것은 아니다.** SD1.5 계열과 SDXL 계열의 구분, VAE·LoRA 의 버전을 모델에 맞춰야 한다는 것, `python -m xformers.info` 의 `build.torch_version` 으로 필요한 torch 버전을 확인하는 진단법, `ui-config.json` 으로 기본값을 고정하는 방법은 지금도 통한다. 댓글 14·15·16번도 "사양 맞춰 최적화만 하면 여전히 쓸 만하다"고 답한다.
> **막히는 것은 '설치 절차' 뿐이다.**

→ [오류 해결](troubleshooting.md) · [ComfyUI 쓰는 법](comfyui.md)

### 그 시절 자료 중 아직 쓸 데가 있는 것

| 자료 | 지금 상태 |
|---|---|
| **확장기능(Extensions) 탭 사용법** | 지금도 그대로다 — `Installed`(체크된 것만 적용, **Apply and restart UI**. 일부는 완전 종료 후 재실행해야 반영) / `Available`(**체크되어 있는 카테고리의 확장은 목록에 안 나오므로 한국어 패치 같은 것을 받으려면 그 체크를 풀고 다시 `Load from`**) / `Install from URL`(**실패의 70%는 주소 오타**). 어느 쪽으로 깔았든 `Installed` 탭에서 실제로 들어갔는지 확인하는 습관을 권한다 |
| **ddetailer 설치가 안 된다** | ☠ **따라 하지 마라.** 원래는 빌드에 C++ 컴파일러가 필요해 Visual Studio 의 'C++를 사용한 데스크톱 개발' 워크로드를 깔아야 했지만, **원 제작자가 업데이트를 중단해 Visual Studio 가 필요 없는 대체판(`https://arca.live/b/aiart/75017759`)으로 갈아타라**고 원글에 갱신이 붙었다. **이것 하나 때문에 VS 를 8GB 씩 깔 이유는 없다** |
| **RTX 4000번대 이하용 구형 패키지** | 최신 WebUI 가 신형 GPU·파이썬 기준으로 옮겨 가며 구형에서 설치가 깨지는 것을 피하려고 **아주 오래된 마지막 버전 기준으로 만들고 ControlNet 오류까지 잡아 둔** A1111 계열 배포본이 있다. 동봉된 설치 방법을 그대로 따르고 **파이썬 버전을 반드시 맞추고 폴더명·경로를 영문으로** 해야 한다. 다만 **최신 ComfyUI 를 쓸 수 있는 환경이면 이 경로를 택할 이유가 없다** (한 글에서만 언급됨) |
| **stable-diffusion-webui-codex** | A1111 의 포크가 **아니라** WebUI 의 디자인·기능을 표방해 새로 만드는 **별개 프론트엔드**(백엔드 FastAPI). SD1.5·SDXL·FLUX.1·Z-Image·**WAN 2.2**·ANIMA 를 지원해 WebUI 계열에서 영상이 되는 것이 특징이지만, **아직 개발 중이고 GGUF 미지원·속도가 느리다는 평**이 있어 **지금 갈아탈 이유는 없다.** '이런 게 나오고 있다' 수준으로 알아 두면 된다 (`https://github.com/sangoi-exe/stable-diffusion-webui-codex`) |

> Forge Neo 는 WebUI 에서 갈라져 나온 **파생·변조 계열**이고 codex 는 **겉모습만 WebUI 처럼 만든 완전히 다른 물건**이라는
> 구분이 댓글에서 정리됐다.

<small>근거 — [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865) · [( ddetailer / 감지-디테일 향상 ) 설치 방법 모… 23.02](https://arca.live/b/aiart/70364209) · [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능) 24.10](https://arca.live/b/aiart/119210516) · [원클릭 노트북 구름IDE 버전 (원클릭Colab 기반, 24… 23.01](https://arca.live/b/aiart/66555000)</small>

??? note "근거 7건 전부 보기"
    [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865) · [( ddetailer / 감지-디테일 향상 ) 설치 방법 모… 23.02](https://arca.live/b/aiart/70364209) · [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능) 24.10](https://arca.live/b/aiart/119210516) · [원클릭 노트북 구름IDE 버전 (원클릭Colab 기반, 24… 23.01](https://arca.live/b/aiart/66555000) · [새로운 프론트엔드 webui codex 26.03](https://arca.live/b/aiart/163821917) · [(WebUI 기본) 확장기능(Extensions/익스텐션) … 23.02](https://arca.live/b/aiart/70348389) · [Webui 4000번대 이하 그래픽 카드용 설치버전 26.04](https://arca.live/b/aiart/167175204)

## 낡은 방식 — 무료 클라우드로 돌리던 시절 (죽은 것과 남은 것)
<small>⚠️ 2024-01 기준 · 근거 7건</small>

그래픽카드 없이 남의 GPU 를 빌려 돌리던 경로가 여럿 있었다. **지금은 대부분 죽었지만 비교표 자체는 감각을 잡는 데 쓸모가 있다.**

| 선택지 | 상태 | 조건 (당시) |
|---|---|---|
| **Google Colab** (무료) | ☠ **사실상 막힘** — 여러 사용자가 실행 자체가 진행되지 않는다고 보고. 구글의 무료 코랩 AI 사용 차단이 원인으로 추정 | 무료, 접근성 높음, 원본 코드라 **업데이트가 가장 빠름**. GPU 할당 이슈, 유료 플랜이 비쌈 |
| **구름IDE** | ☠ **죽음** — `ImportError: cannot import name 'packaging' from 'pkg_resources'` 로 실행 불가. 작성자도 관리 중단 | 무료 **주 30시간**, 하드 **40GB** (매우 큼), 무제한 유료는 NAI 급 가격. GPU 는 Tesla T4 를 반드시 선택 |
| **Amazon SageMaker Studio Lab** | ☠ **죽음** — 서비스 종료·변경 | 하루 8시간 무료, 세션 4시간마다 자동 중지, 계정 승인제. 저장 용량이 적어 모델 2개 정도 |
| **RunPod.io** | ○ **살아 있음** (유료) | 성능이 가장 높음. **최소 충전 $10**, RTX 3090 시간당 $0.35 / RTX 3080 $0.23 (2022~2023 시세) |

> 위 세 개가 죽었다고 해서 **로컬이 어려워진 것은 아니다.** 지금 채널의 기본 경로는 클라우드가 아니라 로컬이며, 위쪽 'A. Forge Neo' 또는 'B. ComfyUI 포터블 통합팩' 을 본다.

### 지금도 유효한 RunPod 주의사항

RunPod 자체는 살아 있지만 **UI 와 템플릿이 여러 번 바뀌어 옛 절차는 그대로 따라 할 수 없다**(작성자 스스로 "이게 4번째 수정" 이라 했고, 댓글에도 메뉴가 사라져 진행이 안 된다는 보고가 있다). 개념만 남긴다.

| 항목 | 내용 |
|---|---|
| **과금 기준** | GPU 사용량이 아니라 **포드가 켜져 있는 시간** — 안 쓸 때는 정지 |
| **완전 종료** | `Stop` 만 누르면 **스토리지 대기 과금이 계속된다.** `Stop` 뒤 생기는 **휴지통(terminate)** 까지 눌러야 하고, 그러면 데이터도 다 날아가니 **미리 백업** |
| 볼륨 | 컨트롤넷·모델을 여러 개 쓰면 **최소 30GB** (나중에 늘리는 것만 가능) |
| 파이썬 | 기본 PyTorch 템플릿은 **3.9** 라 WebUI 용은 **3.10 이상 템플릿** |
| 출력물 회수 | `apt install zip` → `zip -r /workspace/outputs.zip /workspace/outputs` |
| 스팟 인스턴스 | 실시간 경매라 싸지만(예: 시간당 $0.29 → $0.118) **남이 더 높이 부르면 인스턴스가 꺼진다** |

→ [자원](resources.md) · [처음이라면](overview.md)

### RunPod 템플릿 — 'SD 1.5' 와 'RunPod Pytorch' 는 다른 물건이다

댓글이 남긴 구분이 지금도 유효하다.

| 템플릿 | 비유 | |
|---|---|---|
| **SD 1.5** | 윈도우가 깔려 나온 PC | Stable Diffusion 이 이미 깔린 상태로 시작하지만 **RunPod 이 정해 둔 버전으로 고정**돼 dynamic-thresholding 같은 확장이 안 먹을 수 있다 |
| **RunPod Pytorch** | 윈도우를 직접 깔아야 하는 PC | 주피터만 있는 깡통이라 **원하는 버전만 골라 설치**할 수 있다 |

서버를 고를 때는 **서버 기준 '업로드 속도' 가 곧 내 컴퓨터로의 다운로드 속도**이므로 업로드 속도 순으로 정렬해 고르고,
vCPU 4개 이상 · **TCP 연결 제공**(나중 SFTP 접속에 필요)을 확인한다.
SFTP 는 `ssh-keygen -t ed25519` → `cat ~/.ssh/id_ed25519.pub` 로 공개키를 만들어
`https://www.runpod.io/console/user/settings` 의 SSH Public Key 에 등록한다.

> ⚠ **비용** — 사용이 끝나면 Pod 를 **'중지' 만 하지 말고 '삭제' 까지** 해야 한다.
> 중지 후 삭제하지 않으면 **디스크 유지 비용이 시간당 계속 청구된다.**

### 코랩 — 생성 이미지는 기본으로는 드라이브에 안 남는다

코랩에서 뽑은 이미지는 **기본 설정으로는 구글 드라이브에 저장되지 않는다.**
WebUI 설정의 **'paths for saving'** 을 아래처럼 바꿔야 한다.

```
/content/sd-webui/[작업 디렉터리]/outputs
/content/drive/MyDrive/[작업 디렉터리]/outputs
```

> ⚠ **구글 드라이브에 저장하면 구글이 내용을 스캔할 수 있다**(댓글의 경고).

당시 쓰이던 'SD Web UI 런처' 는 **작업 디렉터리 이름을 기존 원클릭 코랩과 같게(예: `SD`) 맞추면
모델 · LoRA · VAE 와 `config.json` · `ui-config.json` 을 그대로 재사용**할 수 있었지만,
**일부 확장이 구글 드라이브 경로 문제로 실행되지 않아 확장은 일부러 지원 대상에서 제외**됐다
(따라서 preset utility 같은 확장의 프리셋은 유지되지 않았다).

<small>근거 — [(구)원클릭(3트) 코랩 22.10](https://arca.live/b/aiart/60472214) · [SD Web UI 런처 소개 및 사용법(코랩) 23.03](https://arca.live/b/aiart/72664098) · [(2023-02-08 수정) 런팟(런포드)로 코랩보다 빠른 … 22.12](https://arca.live/b/aiart/65122299) · [원클릭 노트북을 이용한 Runpod.io 설정 가이드 22.10](https://arca.live/b/aiart/60867273)</small>

??? note "근거 7건 전부 보기"
    [(구)원클릭(3트) 코랩 22.10](https://arca.live/b/aiart/60472214) · [SD Web UI 런처 소개 및 사용법(코랩) 23.03](https://arca.live/b/aiart/72664098) · [(2023-02-08 수정) 런팟(런포드)로 코랩보다 빠른 … 22.12](https://arca.live/b/aiart/65122299) · [원클릭 노트북을 이용한 Runpod.io 설정 가이드 22.10](https://arca.live/b/aiart/60867273) · [원클릭 노트북 구름IDE 버전 (원클릭Colab 기반, 24… 23.01](https://arca.live/b/aiart/66555000) · [무료 클라우드 아마존 SageMaker Studio Lab … 23.02](https://arca.live/b/aiart/70072652) · [SD Web UI 런처 사용법(런팟) 23.03](https://arca.live/b/aiart/72686601)

## 낡은 방식 — reForge 코랩 (2025-01, 지금은 막혔다)
<small>⚠️ 2025-01 기준 · 근거 1건 · **근거 약함**</small>

**2025년 1월에 돌던 reForge 코랩 코드다. 지금 그대로 동작하리라 기대하기는 어렵다** —
이후 Google Colab 은 무료 등급에서 Stable Diffusion WebUI 계열 실행을 차단해 왔다.
**구조만 참고용으로 남긴다.**

당시 forge 대신 reForge 를 쓴 이유는 명확했다 — **forge 로 하면 NAIA 에서 업스케일이 안 되는데 reForge 는 됐다.**

```bash
git clone https://github.com/Panchovix/stable-diffusion-webui-reForge.git
git checkout main
git clone https://github.com/Bing-su/adetailer.git extensions/adetailer
```

**핵심 구조: 코랩은 세션이 끝나면 파일이 사라지므로, 모델과 결과물을 구글드라이브에 두고 심볼릭 링크로 붙인다.**

```bash
# MyDrive/Stable Diffusion/{outputs, model, lora} 를 reForge 쪽에 ln -s 로 연결
ln -s "/content/drive/MyDrive/Stable Diffusion/model"  .../models/Stable-diffusion
ln -s "/content/drive/MyDrive/Stable Diffusion/lora"   .../models/Lora
```

모델 다운로드는 `aria2c -x 8 -s 8` 로 8연결 병렬을 걸었다.
⚠ **Civitai 의 서명된 다운로드 URL(`X-Amz-Expires` 등이 붙은 주소)은 만료 시간이 있어 본문에 적힌 주소는 이미 죽었다.**

```bash
python launch.py --api --theme dark --share --always-high-vram \
  --enable-insecure-extension-access --disable-safe-unpickle
```

`--share` 는 외부에서 접속할 gradio 링크를 만들고, `--always-high-vram` 은 코랩 GPU 를 최대한 쓰는 설정이다.

<small>근거 — [reforge 코랩 코드입니다 25.01](https://arca.live/b/aiart/127339783)</small>

## 낡은 방식 — 리눅스 클라우드에 손으로 올리던 시절 (2022-10, 본문에 sudo 가 빠져 있다)
<small>⚠️ 2022-10 기준 · 근거 1건 · 자료 엇갈림</small>

2022년 구름IDE(goorm) 컨테이너에 A1111 WebUI 를 **손으로** 올리던 절차다. 본문 맨 앞에 작성자가 직접 "원클릭 나왔으니 개발할 거 아니면 그거 써라"라고 적어 둘 만큼 **지금 따라 할 경로가 아니다.** 그래도 리눅스에 올릴 때 걸리는 전형적인 함정이 그대로 남아 있어 적어 둔다 (60817266, 2022-10).

### ⚠ 본문이 여러 명령에서 `sudo` 를 빠뜨렸다

> 본문의 `apt install` · `add-apt-repository` 계열 명령 여럿에 `sudo` 가 없다. 그대로 치면 **`are you root?` 와 dpkg lock 허가 거부**가 난다.
> **댓글의 정정 — 명령 앞에 `sudo` 를 붙인다.** 본문을 그대로 따라 하면 여기서 막힌다.

### ⚠ venv 가 구버전 파이썬으로 만들어진다

증상: `python -V` 는 3.10 인데 **실제 실행은 3.6/3.8 로 잡히고** `RuntimeError: Couldn't install torch` 가 난다.

```bash
rm -rf venv
python -m venv venv
```

로 다시 만들면 3.10 으로 잡혀 해결된다. 본문에도 같은 처방이 적혀 있지만 **댓글에서 실제로 이 순서로 풀렸다.**
같은 함정의 윈도우판(전역 파이썬에 깔고 venv 안이 비어 있는 경우)은 → [오류 해결](troubleshooting.md)

### 파이썬 3.8 → 3.10 올리기 (당시 컨테이너 기본이 3.8)

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
sudo update-alternatives --config python     # 목록에서 3.10 번호 선택
sudo apt install python3.10-venv
sudo apt-get install libgl1
```

권한은 `chown -R 사용자이름 stable-diffusion-webui/` 와 `chmod -R 777 stable-diffusion-webui/` 로 잡고, `nano /etc/sudoers` 에서 `root ALL=(ALL:ALL) ALL` 아래에 `사용자이름 ALL=(ALL:ALL) ALL` 을 추가한다.

### 시간을 아끼는 버그 하나

**자동 로그인 상태에서는 GPU 컨테이너 생성 버튼을 눌러도 생성되지 않는다.** 로그아웃 후 다시 로그인하면 생성 알림이 뜬다 — 모르면 몇 시간을 기다리게 된다.

무료 클라우드 경로가 지금 어떤 상태인지는 위 '낡은 방식 — 무료 클라우드로 돌리던 시절' 을 본다.

<small>근거 — [구름IDE 에서 webui 돌리기 22.10](https://arca.live/b/aiart/60817266)</small>

## 낡은 방식 — reForge (2024-10)
<small>⚠️ 2024-10 기준 · 근거 1건</small>

지금은 Forge Neo 등 후속 프로젝트가 더 많이 쓰이지만, **A1111 계열 WebUI 를 처음 까는 절차 자체**는 이 글이 가장 친절해 그대로 응용할 수 있다.

1. 파이썬 **3.10.6** 을 받아 설치. `Add Python 3.10 to PATH` 를 **반드시 체크** (3.11 이상 비권장)
   `https://www.python.org/downloads/release/python-3106/`
2. `https://git-scm.com/downloads` 에서 git 을 받아 기본 설정으로 설치
3. 설치할 폴더를 **영어 이름**으로 만들고 우클릭 → `Git Bash Here`

```
git clone https://github.com/Panchovix/stable-diffusion-webui-reForge.git
```
   (git bash 는 `Ctrl+C/V` 가 안 되니 마우스로 붙여넣는다)
4. `stable-diffusion-webui-reForge/models/Stable-diffusion` 에 모델을 넣는다
5. `webui-user.bat` 더블클릭 → 첫 실행에 필요한 파일을 자동으로 받고 브라우저가 열린다
6. 업데이트는 설치 폴더에서 우클릭 → Git bash here → `git pull`

**작성자 본인의 단서** — reForge 는 모델을 바꿀 때마다 오래 걸리고 렉이 심해(모델 로딩 때 시스템 RAM 을 풀로드하고 VRAM 은 남는다) 결국 자기는 현행 Forge 를 쓴다고 밝혔다. 댓글에도 같은 증상 보고가 있다.

cfg++ 실측(동일 프롬·동일 시드): `euler a (normal) 28스텝 CFG 5` = **24.2초**, `euler a cfg++ (SGM Uniform) 18스텝 CFG 2.5` = **15.8초**. 단 `ddim cfg++` 는 지원하지 않아 검은 이미지가 나온다.

<small>근거 — [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능) 24.10](https://arca.live/b/aiart/119210516)</small>

## 낡은 방식 — 2022년 WebUI 통합팩·코랩·Runpod (따라하지 말 것)
<small>⚠️ 2022-10 기준 · 근거 3건</small>

2022년 10월의 (구)WebUI 통합팩·원클릭 코랩·Runpod 가이드는 **작성자 본인이 글 첫머리에서 "따라하지 말라"고 철회**한 상태다. 남은 것 중 지금도 쓸모 있는 것만 옮긴다.

- 당시 최소 사양은 **GTX 1050ti 4GB VRAM + 디스크 30GB 이상**이었고 접속 주소는 `http://127.0.0.1:7860/` 이었다. 이 주소는 지금도 A1111 계열의 기본값이다.
- `--skip-torch-cuda-test` 인자는 문제 해결에 도움이 되지 않으며, 해당 오류의 원인은 **xformers 와 torch 버전 불일치**다.
- 코랩은 여러 사용자가 실행 자체가 진행되지 않는다고 보고했고, 구글이 무료 코랩의 AI 사용을 막은 것으로 추정된다.
- Runpod 요금은 GPU 사용량이 아니라 **포드가 켜져 있는 시간** 기준이라 안 쓸 때는 정지해야 한다.

<small>근거 — [(구)WEB UI설치가 어려운 사람을 위한 통합팩 (0.66… 22.10](https://arca.live/b/aiart/60216616) · [(구)원클릭(3트) 코랩 22.10](https://arca.live/b/aiart/60472214) · [원클릭 노트북을 이용한 Runpod.io 설정 가이드 22.10](https://arca.live/b/aiart/60867273)</small>

## 부록 — A1111 WebUI + 포토샵 연동 (2023-01)
<small>⚠️ 2023-01 기준 · 근거 1건</small>

A1111 시대 글이라 지금 환경과는 거리가 크지만, `--api` 를 켜서 외부 프로그램이 WebUI 를 조종하는 구조 자체는 지금 NAIA 연동과 같다.

준비물: 로컬 A1111 WebUI, 포토샵 v24 이상, git, python.

```bat
set COMMANDLINE_ARGS=--api
```

```
https://github.com/AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin
```

실행 순서는 `webui-user.bat` → `start_server.bat` → 포토샵 → Adobe UXP Developer Tool 에서 `manifest.json` 로드다. 포토샵은 `편집 → 환경설정 → 플러그인 → 개발자 모드`를 켜야 한다. t2i·i2i·인페인팅·아웃페인팅을 포토샵 안에서 쓸 수 있다.

<small>근거 — [무료 포토샵 플러그인 설치 및 사용방법 23.01](https://arca.live/b/aiart/67261156)</small>

## 라데온 RX 7900XTX — Windows 11 + WSL2 + ROCm 6.4.2 + SageAttention 전 과정 (2025-08)
<small>2025-08 기준 · 근거 1건</small>

위 '라데온(AMD)' 항목이 **2026-08 기준 리눅스 + ROCm 10.1** 경로라면, 이쪽은 **윈도우를 유지한 채 WSL2 안에서 돌리는** 경로다 (146695792, 2025-08).
일본어 원문 가이드(kemari)를 참고해 전 과정을 옮긴 기록이고, **명령이 전부 적혀 있어 그대로 따라갈 수 있다.**

| 항목 | 값 |
|---|---|
| GPU | **AMD RX 7900XTX** |
| OS | **Windows 11 + WSL2 (Ubuntu 24.04 Noble)** |
| ROCm | **6.4.2** |
| PyTorch | **2.6.0+rocm6.4.2** (cp312 휠) |
| 가속 | **FlashAttention(`main_perf` 브랜치) + SageAttention** |
| 실측 | Sage attention 활성화 상태에서 **960x1440 60fps 7초 영상(480x720 을 2배 업스케일) = 492.5초** |

ComfyUI 전용 우분투라 **root 권한(`sudo su`)** 으로 진행한다.

### 1. 시스템 준비

```bash
apt-get update
apt-get -y dist-upgrade
apt install python3.12-venv
python3 -m venv myvenv          # myvenv 는 임의 이름
source myvenv/bin/activate
python -m pip install --upgrade pip
```

### 2. AMD 드라이버 · ROCm

```bash
wget https://repo.radeon.com/amdgpu-install/6.4.2.1/ubuntu/noble/amdgpu-install_6.4.60402-1_all.deb
sudo apt install ./amdgpu-install_6.4.60402-1_all.deb
amdgpu-install -y --usecase=wsl,rocm --no-dkms
rocminfo                        # 인식 확인
```

### 3. PyTorch ROCm 판

기존 것을 먼저 지운다.

```bash
pip3 uninstall torch torchaudio torchvision pytorch-triton-rocm -y
```

그다음 `repo.radeon.com/rocm/manylinux/rocm-rel-6.4.2/` 에서 **cp312 휠**을 받아 설치한다 —
`pytorch_triton_rocm-3.2.0+rocm6.4.2`, `torch-2.6.0+rocm6.4.2`, `torchaudio-2.6.0+rocm6.4.2`, `torchvision-0.21.0+rocm6.4.2`.

### 4. ⚠ 라이브러리 충돌 해결 — 이 단계를 빼면 안 된다

```bash
location=$(pip show torch | grep Location | awk -F ": " '{print $2}')
cd ${location}/torch/lib/
rm libhsa-runtime64.so*
```

이전 사용 이력이 있으면 트리톤 캐시도 지운다.

```bash
rm -rf /home/user/.triton/cache
```

### 5. FlashAttention + SageAttention

```bash
git clone https://github.com/ROCm/flash-attention.git
cd flash-attention
git checkout main_perf
pip install packaging
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" python setup.py install
pip install sageattention
```

**파일 교체** — 원문 첨부 파일을 쓴다. 먼저 `chmod -R 777 /home/계정이름` 으로 권한을 준 뒤
`flash_attn/utils` 의 `distributed.py` 를 덮어쓰고, `sageattention` 폴더의
`attn_qk_int8_per_block.py` · `attn_qk_int8_per_block_causal.py` · `quant_per_block.py` 를 덮어쓴다.

### 6. 실행 스크립트 `comfyui.sh`

```bash
export FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"
export MIOPEN_FIND_MODE=2
export MIOPEN_LOG_LEVEL=3
export TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
export PYTORCH_TUNABLEOP_ENABLED=1

python3 main.py --reserve-vram 0.1 --preview-method auto --use-sage-attention --bf16-vae --disable-xformers
```

`chmod +x` 후 `~/.bashrc` 에 alias 를 등록하면 `comfyui` 한 단어로 실행된다.

> 댓글 반응 — **WSL 이 네이티브 리눅스만큼은 아니어도 쓸 만하고, ROCm 호환성이 예전보다 많이 좋아졌다**는 평이다.
> 지금 새로 시작한다면 위 '라데온(AMD) — 로컬 비권장이 뒤집혔다' 의 2026-08 경로부터 보고, 그쪽이 막힐 때 이 문서를 연다.

<small>근거 — [라데온 RX 7900XTX + Win11 + WSL + Fl… 25.08](https://arca.live/b/aiart/146695792)</small>

## 낡은 방식 — DirectML 포크와 torch/xformers 강제 되돌리기 (2023)
<small>⚠️ 2023-05 기준 · 근거 2건</small>

### ComfyUI DirectML 포크 — 유지보수가 끝났다

NVIDIA 가 아닌 GPU 로 윈도우에서 ComfyUI 를 돌리려고 만들어졌던 DirectML 포크와 파워셸 자동 설치 스크립트가 있다 (72113936, 2023-03).
**글 첫머리에 중단 공지가 붙어 있다.**

> **"이제 ComfyUI 자체가 DirectML 을 지원하게 되어 이 프로젝트는 더 이상 유지보수되지 않는다."**

즉 **지금은 이 배포판이 아니라 ComfyUI 본체를 쓰면 된다.** 제작자도 2023년 중반 이후 "수요가 적고 손 놓은 지 오래라 업데이트 계획이 없다" 고 답했고, 그래서 **Detailer 같은 최신 노드는 쓸 수 없다.**
정상 작동이 확인된 기능은 `VAELoader` + `CLIPText` + `KSampler(euler)` 를 쓴 **일반 이미지 생성뿐**이었다.

**다만 여기서 나온 오류 둘은 지금도 검색에 걸린다.**

| 오류 | 원인 | 해결 |
|---|---|---|
| 실행하면 **창이 바로 꺼진다** | `run.ps1` 에 **`--xformers`** 가 들어 있다 | **DirectML 에서는 xformers 를 쓸 수 없다.** `--xformers` 를 뺀다(제작자 답변) |
| `OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized` | **OpenMP 런타임 중복 링크** | 환경변수 **`KMP_DUPLICATE_LIB_OK=TRUE`** (임시 회피책) |

DirectML 은 윈도우가 제공하는 범용 GPU 연산 API 로, CUDA 가 없는 AMD·인텔 GPU 에서도 딥러닝을 돌릴 수 있게 해 주지만 **속도와 메모리 효율은 CUDA 보다 나쁘다.**
지금 라데온을 쓴다면 위 'ROCm' 경로 두 편이 먼저다.

### A1111 의 torch / xformers 버전 강제 되돌리기

**정상 설치했다면 따라 하지 말라고 작성자가 못 박은 방법이다** (76553767, 2023-05).
지금 webui 를 새로 설치하면 그 시점에 맞는 최신 torch/xformers 가 깔리므로, **버전을 강제로 되돌려야 할 때만** 쓴다.

webui 폴더에 아래 내용의 `.bat` 을 넣고 실행한다.

```bat
@echo off
set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--reinstall-xformers --reinstall-torch --xformers --exit
set XFORMERS_PACKAGE=xformers==0.0.23.post1
set TORCH_COMMAND=pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html
call webui.bat
```

`--reinstall-xformers`·`--reinstall-torch` 는 기존 것을 지우고 다시 깔라는 뜻이고 **`--exit` 는 설치만 하고 종료하라는 뜻**이라 **창이 저절로 닫힐 때까지 기다려야 한다.**

| 주의 | |
|---|---|
| 실행 후 **webui 하단 버전 표시가 그대로**면 | 설치가 안 된 것이다 |
| 설치 중 창을 임의로 끄면 | `지정된 모듈을 찾을 수 없습니다` 오류가 난다 |
| `torchaudio` **dependency conflict 경고** | webui 가 정상 실행되고 하단 버전이 의도한 값이면 **무시해도 된다**는 사례가 있다 |

엔비디아 그래픽카드면 1000~5000번대 어느 세대든 동일하게 동작하고, **버전 문자열만 고치면 다른 CUDA/xformers 조합으로도 쓸 수 있다.**

→ [오류 해결](troubleshooting.md)

<small>근거 — [(구)torch2.1.2 xformers0.0.23 원클릭자… 23.05](https://arca.live/b/aiart/76553767) · [(-) DirectML을 사용해 윈도우 환경에서 AMD 라데… 23.03](https://arca.live/b/aiart/72113936)</small>

## 글카 없이 ANIMA 찍먹 — 무료 코랩 원클릭 노트북 (2026-04)
<small>2026-04 기준 · 근거 1건</small>

글카가 없어도 **무료 코랩(T4)** 에서 ANIMA 를 찍먹해 볼 수 있는 원클릭 노트북이 있다.
판은 `anima-preview3-base-int8rowwise` 이고 **여러 최적화가 들어간 워크플로우라 원본 BF16 대비 품질 저하가 있음을 감안**해야 한다.

| 단계 | |
|---|---|
| 출력 | 구글 드라이브를 연결하면 `ONECLICK/outputs/ComfyUI` 에 복사된다 |
| 접속 | 실행 후 **약 3분** 뒤 터널링 주소가 뜬다. 아무거나 접속하면 되고 **로딩 완료 전에 접속하면 아무것도 안 뜬다** |
| 403 | 원인 불명. **시크릿 모드나 다른 브라우저**로 열면 된다 |
| 워크플로우 | 좌측 워크플로우 탭에서 `anima_fast_sage_torch_cach` 를 불러온다. 앱 모드가 불편하면 좌측 상단의 노드 그래프 진입 |
| 자동완성 | 좌측 하단 설정에서 `pysssss` 항목을 켠 뒤 커스텀 워드 관리에 `huggingface.co/arcacolab/foranima/raw/main/for_anima_danbooru_2025-09-01_pt20-ia-dd.csv` 내용을 붙여 넣는다 (작가 태그 앞에 `@` 가 붙도록 손본 ANIMA 전용 CSV) |

```text
속도   최초 생성 2분 이상 (로딩·패치·컴파일)   →   이후 30~40초대
       코랩 특성상 일정하지 않아 40초 이상 걸릴 수도 있다
```

로라는 노드를 연결하면 쓸 수 있다고 작성자가 답했다.

*(2026-04, 한 글이다. 코랩 정책은 자주 바뀌므로 안 되면 위 "글카 없이" 절들을 볼 것.)*
→ [ANIMA](anima.md)

<small>근거 — [무료 코랩용 anima pr3 int8 찍먹 노트북 26.04](https://arca.live/b/aiart/167342462)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 230개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| `MemoryError`, `you tried to allocate xxxx bytes`, `OSError: [WinError 1455] 이 작업을 완료하기 위한 페이징 파일이 너무 작습니다` 는 가상 메모리(페이징 파일)를 늘려 대처한다 | 5 | 0 | 2022-12~2023-02 |
| int8convrot 양자화는 fp8 tensorwise 보다 품질이 좋고(Q8_0 급) 조금 빠르며, 캘리브레이션이 필요 없어 대세가 된다 | 4 | 0 | 2026-07~2026-08 |
| SDXL/Illustrious 결과물이 탁하거나 흰 점이 찍히면 VAE Select 값을 2로 두어 별도 VAE(fixFP16ErrorsSDXLLowerMemoryUse_v10)를 적용한다 | 4 | 0 | 2026-06~2026-08 |
| 모델이 diffusion model 단독으로 배포되면 models/checkpoints 가 아니라 models/diffusion_models 에 넣고 Load Diffusion Model 계열 노드로 불러야 하며, 텍스트 인코더와 VAE 도 각각 models/text_encoders, models/vae 에 따로 넣어 연결해야 한다 | 4 | 0 | 2026-05~2026-08 |
| 통합팩은 ComfyUI 본체를 업데이트하지 말고 새 버전이 나오면 처음부터 새로 받아야 한다 | 4 | 0 | 2026-05~2026-08 |
| 설정 > Comfy > Nodes 2.0 > 모던 노드 디자인을 켜면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다 | 4 | 0 | 2026-05~2026-08 |
| ComfyUI 포터블에서 파이썬 패키지를 깔 때는 시스템 파이썬이 아니라 `python_embeded\python.exe -m pip` 로 설치해야 한다 | 4 | 0 | 2026-01~2026-08 |
| ComfyUI 는 불특정 다수에게 서빙하라고 만든 프로그램이 아니라 보안이 사실상 없으므로 외부망 개방은 특히 주의해야 한다 | 3 | 0 | 2026-02~2026-05 |
| `RuntimeError: Cannot add middleware after an application has started` 는 설치 폴더의 cache/virtualenv/Scripts 에서 파워셸을 열고 `./Activate.ps1` 후 `pip install --upgrade fastapi==0.90.0` 을 실행하면 해결된다 | 3 | 0 | 2023-01~2023-02 |
| 2022~2023년 WebUI 통합팩·코랩·Runpod 설치 안내글은 작성자 스스로 '따라하지 말라'고 철회한 상태다 | 3 | 0 | 2022-10~2022-10 |
| 뉴비가 공유받은 워크플로우에서 오류가 터지는 범인 1위는 sage-attention 이다 | 3 | 0 | 2026-05~2026-08 |
| `Torch is not able to use GPU` 에는 `--skip-torch-cuda-test` 를 붙이고 그래도 같은 오류면 `--precision full --no-half` 를 함께 쓰며, GTX 16xx 는 `set COMMANDLINE_ARGS=--skip-torch-cuda-test --no-half --precision=full --listen --lowvram` 로 쓴 사례가 있다 | 3 | 0 | 2022-12~2023-02 |
| 윈도우 계정명이나 설치 경로 폴더 이름에 한글·공백이 있으면 정상 설치·실행이 되지 않으며, 계정명이 한글이라 못 바꾸면 C 드라이브 최상위에 영문 폴더를 만들어 거기에 설치한다 | 3 | 0 | 2023-02~2026-04 |
| Autocomplete Plus의 autocomplete tag source를 danbooru로 지정하면 e621 태그가 빠진다 | 3 | 0 | 2026-02~2026-05 |
| --skip-torch-cuda-test 인자는 문제 해결에 도움이 되지 않으며 해당 오류의 원인은 xformers 와 torch 버전 불일치다 | 3 | 0 | 2022-10~2023-01 |
| `zipfile.BadZipFile: File is not a zip file` 이나 `OSError: Unable to load weights from pytorch checkpoint file` 은 받다 만 huggingface 캐시와 충돌한 것이므로 `C:\Users\사용자명\.cache` 의 huggingface 폴더를 삭제하고 다시 실행한다 | 3 | 0 | 2022-11~2023-02 |
| 무료 클라우드로 A1111 을 돌리던 경로는 지금 대부분 죽었다 — 구름IDE 판은 `ImportError: cannot import name 'packaging' from 'pkg_resources'` 로 실행되지 않고 작성자도 관리를 중단했으며, Amazon SageMaker Studio Lab 은 서비스가 종료·변경됐고, 무료 코랩은 실행 자체가 진행되지 않는다는 보고가 다수다 | 3 | 0 | 2022-10~2023-02 |
| VFI(프레임 보간) rife 모델은 ComfyUI/models/frame_interpolation 폴더에 넣어야 인식된다 | 3 | 0 | 2026-04~2026-08 |
| 그림의 작가·모델을 묻는 질문은 EXIF(메타데이터)가 없으면 아무도 알 수 없다 | 3 | 0 | 2023-12~2026-06 |
| VAE 는 그림체에 아무런 영향도 주지 않는다 — 극실사체가 나오면 모델을 다시 확인해야 한다. VAE 가 좌우하는 것은 색감과 선명도뿐이다 | 3 | 0 | 2023-01~2023-02 |
| ComfyUI 포터블에서 가속 패키지는 시스템 파이썬이 아니라 동봉된 `python_embeded` 파이썬에 깔아야 한다 | 3 | 0 | 2026-01~2026-08 |
| ComfyUI 통합팩은 한글이 없는 경로에 압축을 풀어야 한다 | 3 | 0 | 2026-02~2026-08 |
| SageAttention 을 켜는 방법은 두 가지다 — 실행 bat 에 `--use-sage-attention` 을 추가하거나, ComfyUI-KJNodes 의 'Patch Sage Attention KJ' 노드(sage_attention=auto, allow_compile=true)를 모델 선에 통과시킨다. 노드 방식은 켜고 끄기가 쉽다 | 3 | 0 | 2026-02~2026-05 |
| 포터블 구버전이 무조건 나쁜 것은 아니어서, 최신 버전에서 말썽을 부리는 노드가 있으면 구버전에서 작업하는 편이 나은 경우도 있다 | 3 | 0 | 2026-02~2026-08 |
| sage attention을 켜면 손가락 찐빠(손 왜곡)가 늘어난다는 보고가 있다 | 3 | 0 | 2026-06~2026-08 |
| NaN 원인은 ① WebUI 설정(half 연산·크로스 어텐션·손상된 CLIP) ② 고학습률 파인튜닝(하이퍼네트워크·임베딩·LoRA 를 전부 빼고 재현 확인) ③ 병합으로 망가진 레이어(원본 계열 모델과 대조) ④ xformers 버그 ⑤ ROCm·DirectML 버그 순으로 좁힌다 | 2 | 0 | 2023-01~2023-02 |
| 체크포인트(모델)는 이미지를 학습한 결과 파일(.ckpt/.safetensors)로 그림을 뽑는 본체이며, Stable Diffusion 을 붕어빵 기계라 하면 체크포인트가 형틀에 해당한다 | 2 | 0 | 2023-01~2023-01 |
| `ImportError: DLL load failed while importing _fused: 지정된 프로시저를 찾을 수 없습니다` 는 torch/python/sageattention/cuda 버전이 어긋난 것이므로 cp313 전용 whl 대신 파이썬 버전 무관 빌드(cp39-abi3)인 `sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl`(4000번대는 cu128 판)로 바꾸면 해결된다 | 2 | 0 | 2026-01~2026-08 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [(구)WEB UI설치가 어려운 사람을 위한 통합팩 [0.66.2v]](https://arca.live/b/aiart/60216616) — 2022-10, 추천 189
- [WebUI 기본 사용법 정리](https://arca.live/b/aiart/61366565) — 2022-10, 추천 87
- [누구나 따라할 수 있는 로컬 자동좌 WebUI 클린 설치 (v1.6.0 기준 수정)](https://arca.live/b/aiart/79413719) — 2023-06, 추천 81
- [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!!!](https://arca.live/b/aiart/111903865) — 2024-07, 추천 71
- [[ ddetailer / 감지-디테일 향상 ] 설치 방법 모를때 초보용 설치방법](https://arca.live/b/aiart/70364209) — 2023-02, 추천 69
- [저사양, 작은뇌를 위해 간단히 적는 Wan2.1 사용법](https://arca.live/b/aiart/137466035) — 2025-05, 추천 56
- [응애도 할 수 있는 ComfyUI Wan I2V 영상 AI 모델 간단 사용 방법](https://arca.live/b/aiart/147203387) — 2025-09, 추천 56
- [(구)원클릭(3트) 코랩](https://arca.live/b/aiart/60472214) — 2022-10, 추천 52
- [Comfyui portable v0.30.0 + sage 외 여러가지.](https://arca.live/b/aiart/178800540) — 2026-08, 추천 47
- [나는 심심하면 정보글을 쓰고 있어... 이미지 저장편](https://arca.live/b/aiart/71264253) — 2023-03, 추천 45
- [뉴비들은 webui neo 쓰자](https://arca.live/b/aiart/176802949) — 2026-07, 추천 44
- [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법](https://arca.live/b/aiart/66582124) — 2023-01, 추천 42
- [ComfyUI - 산지직송 뉴비가 작성한, 하루만에 설치하고 짤뽑까지.](https://arca.live/b/aiart/163532702) — 2026-02, 추천 42
- [vram8기가라도 쫄지말고 그림뽑아](https://arca.live/b/aiart/119326123) — 2024-10, 추천 41
- [Comfyui portable v0.22.0 + sage + triton.](https://arca.live/b/aiart/171586136) — 2026-05, 추천 41
- [ComfyUI Portable 설치 쉽게 하는 툴 하나 소개함](https://arca.live/b/aiart/161826600) — 2026-02, 추천 40
- [Comfyui portable v0.31.0 + sage 외 여러가지.](https://arca.live/b/aiart/179342860) — 2026-08, 추천 38
- [comfyui portable v0.20.1 + sage + triton.](https://arca.live/b/aiart/169293039) — 2026-04, 추천 36
- [하이퍼코랩 - 초고속 이미지 생성 코랩 노트북 (7초만에 생성)](https://arca.live/b/aiart/69335887) — 2023-02, 추천 32
- [SD Web UI 런처 소개 및 사용법(코랩)](https://arca.live/b/aiart/72664098) — 2023-03, 추천 32
- [(24.10.13 수정)질문하기 전에 한번만 보고 가면](https://arca.live/b/aiart/109424774) — 2024-06, 추천 32
- [30분내로 끝내는 Vast.ai 사용법 (시간당 0.3$로 로컬굴리기)](https://arca.live/b/aiart/158013422) — 2025-12, 추천 32
- [Comfyui portable v0.26.0 + sage 외 여러가지](https://arca.live/b/aiart/175163102) — 2026-06, 추천 32
- [ComfyUI App mode가 나왔길래 써봤다.](https://arca.live/b/aiart/164519826) — 2026-03, 추천 27
- [(2023-02-08 수정) 런팟(런포드)로 코랩보다 빠른 웹ui 구성, 모델 설치 가이드](https://arca.live/b/aiart/65122299) — 2022-12, 추천 26
- [NAIA 및 아니마 사용을 위한 Webui Forge Neo 포지네오 설치 가이드 (수정)](https://arca.live/b/aiart/170554328) — 2026-05, 추천 26
- [라데온 stable-diffusion-webui 세팅 가이드](https://arca.live/b/aiart/60447786) — 2022-10, 추천 25
- [원클릭 노트북을 이용한 Runpod.io 설정 가이드](https://arca.live/b/aiart/60867273) — 2022-10, 추천 25
- [Comfyui portable v0.23.0 + sage + grok i2v 외 여러가지](https://arca.live/b/aiart/172596107) — 2026-06, 추천 25
- [[정보글] 챈섭 여는 법 ABC (gradio / ngrok / 기능 제한 방법)](https://arca.live/b/aiart/76388840) — 2023-05, 추천 24
- [(구)torch2.1.2 xformers0.0.23 원클릭자동설치파일 5000번대4000번대3000번대2000번대1000번대 최적화](https://arca.live/b/aiart/76553767) — 2023-05, 추천 24
- [무료 포토샵 플러그인 설치 및 사용방법](https://arca.live/b/aiart/67261156) — 2023-01, 추천 21
- [로컬 comfyui 찍먹해보기 - sage-attention 설치](https://arca.live/b/aiart/162993309) — 2026-02, 추천 21
- [Anima 찍먹해보기 - 아니마 체크포인트, 로라 다운로드](https://arca.live/b/aiart/171506089) — 2026-05, 추천 21
- [허깅페이스에서 모델 다운받는 방법](https://arca.live/b/aiart/66720059) — 2023-01, 추천 19
- [[-] DirectML을 사용해 윈도우 환경에서 AMD 라데온 그래픽카드로 ComfyUI 돌리기](https://arca.live/b/aiart/72113936) — 2023-03, 추천 19
- [Comfy로 anima 실행 및 최적화하기](https://arca.live/b/aiart/175408089) — 2026-06, 추천 19
- [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능)](https://arca.live/b/aiart/119210516) — 2024-10, 추천 18
- [!!! 블랙웰 (RTX 50) 유저들 설치시 필독 !!!](https://arca.live/b/aiart/135962161) — 2025-05, 추천 18
- [comfyui portable v0.11.1 + sage + triton.](https://arca.live/b/aiart/161206430) — 2026-02, 추천 18
- [ComfyUI SAM3 / RIFE 자체 지원 노드 추가](https://arca.live/b/aiart/168617494) — 2026-04, 추천 18
- [순정webui에서 v-pred모델쓰기](https://arca.live/b/aiart/128472488) — 2025-02, 추천 16
- [컴피 공홈에서 포터블 버전 받는 방법.](https://arca.live/b/aiart/170235453) — 2026-05, 추천 16
- [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 세팅 방법](https://arca.live/b/aiart/179176367) — 2026-08, 추천 16
- [원클릭 노트북 구름IDE 버전 (원클릭Colab 기반, 24/01/20 수정)](https://arca.live/b/aiart/66555000) — 2023-01, 추천 15
- [(ComfyUI) Hires Fix 워크플로우 가이드](https://arca.live/b/aiart/86112135) — 2023-09, 추천 14
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [AI그림 채널 오류 해결책 모음](https://arca.live/b/aiart/70417374) — 2023-02, 추천 13
- [[월페이퍼 대회] 악마에게 몸을 빼앗긴 소녀](https://arca.live/b/aiart/92064917) — 2023-11, 추천 13
- [Comfy Cloud Free tier 시작 (매달 400크레딧)](https://arca.live/b/aiart/163815149) — 2026-03, 추천 13
- [B580 생성속도 최적화 (Anima)](https://arca.live/b/aiart/173585515) — 2026-06, 추천 13
- [comfyui portable v0.15.1 + sage + triton.](https://arca.live/b/aiart/163592169) — 2026-02, 추천 12
- [모바일 Comfy 구동 프론트 Web App](https://arca.live/b/aiart/170363616) — 2026-05, 추천 12
- [RTX 20 시리즈를 사용하는데 아니마는 써보고 싶은 사람들을 위한 작은 ComfyUI 팁.](https://arca.live/b/aiart/170741530) — 2026-05, 추천 12
- [오래된 노트북 내장그래픽으로 ANIMA 돌려보기](https://arca.live/b/aiart/176691794) — 2026-07, 추천 11
- [구름IDE 에서 webui 돌리기](https://arca.live/b/aiart/60817266) — 2022-10, 추천 10
- [[WebUI 기본] 확장기능(Extensions/익스텐션) 탭 사용 방법, 설치, 적용](https://arca.live/b/aiart/70348389) — 2023-02, 추천 10
- [새로운 프론트엔드 webui codex](https://arca.live/b/aiart/163821917) — 2026-03, 추천 10
- [인텔 Arc GPU용 ComfyUI windows-portable 등장](https://arca.live/b/aiart/168348535) — 2026-04, 추천 9
- [넓은 의미의 체크포인트와 좁은 의미의 체크포인트](https://arca.live/b/aiart/170230261) — 2026-05, 추천 9
- [모르고 쓰면 해골물인 ComfyUI 옵션](https://arca.live/b/aiart/177447677) — 2026-07, 추천 9
- [rdna4용 comfyui 0.30.1 + sage](https://arca.live/b/aiart/178869944) — 2026-08, 추천 9
- [라데온 RX 7900XTX + Win11 + WSL + FlashAttention + SageAttention 설치](https://arca.live/b/aiart/146695792) — 2025-08, 추천 8
- [런팟 RTX 5090용 WAN 2.2 딸깍 도커 이미지](https://arca.live/b/aiart/151440980) — 2025-10, 추천 8
- [무료 코랩용 anima pr3 int8 찍먹 노트북](https://arca.live/b/aiart/167342462) — 2026-04, 추천 8
- [comfy 모바일 ui 확장 괜찮은거 하나 있네](https://arca.live/b/aiart/162164907) — 2026-02, 추천 7
- [무료 클라우드 아마존 SageMaker Studio Lab 사용 가이드](https://arca.live/b/aiart/70072652) — 2023-02, 추천 6
- [comfyui 원격접속하는법](https://arca.live/b/aiart/162190790) — 2026-02, 추천 6
- [Webui 4000번대 이하 그래픽 카드용 설치버전](https://arca.live/b/aiart/167175204) — 2026-04, 추천 6
- [Comfy CLI 설치 방법 정리](https://arca.live/b/aiart/169751935) — 2026-05, 추천 6
- [pytorch 2.10 +  python 3.13 + RTX5000대 기준 패키지 설치법](https://arca.live/b/aiart/160668279) — 2026-01, 추천 5
- [라데온 7900xtx 찍먹 입문 정보](https://arca.live/b/aiart/165090900) — 2026-03, 추천 5
- [comfyui 앱모드 사용법](https://arca.live/b/aiart/171528258) — 2026-05, 추천 5
- [RX 9000용 torch+rocm 업데이트 + sage 빌드 하는 법 (RX 7000 이하도 torch+rocm 업데이트 가능하게 수정)](https://arca.live/b/aiart/176063226) — 2026-07, 추천 5
- [AMD R9700 comfy-kitchen HIP PR + flash-attn CK backend 테스트](https://arca.live/b/aiart/178367683) — 2026-07, 추천 5
- [Wan2GP 미니맥스 H3 나왔네](https://arca.live/b/aiart/179281753) — 2026-08, 추천 5
- [라데온 sageattention whl로 만들어왔어](https://arca.live/b/aiart/179413848) — 2026-08, 추천 5
- [SD Web UI 런처 사용법(런팟)](https://arca.live/b/aiart/72686601) — 2023-03, 추천 4
- [튜링용 flash-attention](https://arca.live/b/aiart/176657130) — 2026-07, 추천 4
- [런팟 서버리스 api Anything 무료 오픈베타와 사용 방법](https://arca.live/b/aiart/66830656) — 2023-01, 추천 3
- [라데온용 컴피 rocm 업데이트 방법 다시 알아옴](https://arca.live/b/aiart/160654263) — 2026-01, 추천 3
- [comfyui 포터블 이사가는거 도와주는 스크립트](https://arca.live/b/aiart/162198611) — 2026-02, 추천 3
- [ComfyUI 에서 bjornulf_custom_nodes 가 설치되지 않는 문제 해결](https://arca.live/b/aiart/163272564) — 2026-02, 추천 3
- [bc250으로 짤뽑아보기](https://arca.live/b/aiart/176880815) — 2026-07, 추천 3
- [reforge 코랩 코드입니다](https://arca.live/b/aiart/127339783) — 2025-01, 추천 2
- [정보탭의 kohya gui 설치후 발생한 문제해결](https://arca.live/b/aiart/176818115) — 2026-07, 추천 2
- [파이토치 설치 안되는사람 보셈](https://arca.live/b/aiart/69972082) — 2023-02, 추천 1
