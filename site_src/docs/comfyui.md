# ComfyUI 쓰는 법

> **원문 160건 → 이 문서 하나** · 주장 362개 · 정리 2026-08-14

[설치와 환경 구성](install.md) 까지 끝냈다면 브라우저에 노드가 잔뜩 깔린 화면이 떠 있을 것이다.
이 문서는 그 다음, **"그래서 뭘 눌러야 하나"** 에 답한다.

ComfyUI 는 그림을 그리는 프로그램이 아니라 **워크플로우를 실행하는 판**이다.
그래서 처음 할 일은 노드를 짜는 것이 아니라 **남이 만든 워크플로우를 불러오는 것**이고,
그 다음 부딪히는 벽은 대부분 *미싱 노드*·*업데이트*·*설정* 세 가지다. 순서대로 다룬다.

노드 방식 자체는 ComfyUI 가 발명한 게 아니다. 후디니·Softimage XSI 에 있던 노드 에디터를
블렌더가 무료로 대중화한 흐름에서 왔다는 정리가 채널에 올라와 있다(한 글에서만 언급됨).
그래서 3D 툴을 만져본 사람은 화면이 낯익을 것이고, 아니어도 **상자를 선으로 잇는다**는 것만 알면 된다.

## 처음이라면 이 순서대로 — 완전 초보 7단계
<small>2026-06 기준 · 근거 6건</small>

아무것도 모르는 사람이 **로컬로 그림을 뽑는 데까지** 올라오는 길은 채널에 이미 정리돼 있다.
175397651 「Comfy ANIMA 정보글 모음」(2026-06, 추천 43)이 **완전 초보자용 시작 순서를 일곱 단계로 못박아** 두었다.
**지금 시점 입문자에게 가장 먼저 건네야 할 지도다.**

| | 단계 | 이 위키에서 |
|---|---|---|
| 1 | **로컬 comfyui 찍먹해보기 — 설치** | [설치와 환경 구성](install.md) 의 'A0. 가장 짧은 길' |
| 2 | **커스텀 노드 설치** | 아래 '미싱 노드' |
| 3 | **컴피 공홈에서 포터블 버전 받는 방법** | [설치와 환경 구성](install.md) 의 '⚠ 먼저 읽기' — 노란 버튼은 포터블이 아니다 |
| 4 | **챈에 올라오는 포터블 직접 검색해보기** | [설치와 환경 구성](install.md) 의 'B. ComfyUI 포터블 통합팩' |
| 5 | **Anima 찍먹해보기 — 이미지생성** | [ANIMA](anima.md) |
| 6 | **진짜 초보자용 워크플로우** | 아래 '워크플로우 불러오기' · '노드 여섯 개면 그림이 나온다' |
| 7 | **ANIMA All in One 워크플로우** | [ANIMA](anima.md) |

**순서에서 읽어야 할 것 두 가지.**

- **1~4단계가 전부 '설치' 다.** 노드를 배우는 것은 5단계 이후다. 처음 막히는 지점은 노드가 아니라 **어느 ComfyUI 를 깔았는가**이며, 그래서 3·4단계가 따로 서 있다.
- **6단계와 7단계가 나뉘어 있다.** 초보자용 워크플로우로 한 장 뽑아 본 다음에 올인원(AiO)으로 간다. 처음부터 AiO 를 열면 노드가 수십 개라 어디를 눌러야 할지 모른다.

**5·6단계에서 참고할 것** — 초보자용 아니마 워크플로우 다섯 종을 비교한 글이 있다. 기본 28스텝은 21초, 고속 LoRA 는 8초이며, **기본 생성 + 고속 LoRA 업스케일(31초)** 조합이 미적 다양성과 손가락 안정성을 함께 챙겨 추천된다 (170932870, 2026-05).

**색인 글 자체의 구성** — 175397651 은 아래처럼 나뉜다. 지금 뭘 찾는지 알 때 여기부터 뒤지면 된다.

| 갈래 | 들어 있는 것 |
|---|---|
| ComfyUI 설치·관리 | 기초 / 심화 |
| 기본 ANIMA 생성 | 설정값·시그마·CFG / 모델·로라·VAE / 커스텀 노드 / 워크플로우 |
| 기타 | 개념 · 프롬프트 · 환경 구축 · 팁과 외부툴 |

→ [처음이라면](overview.md) · [설치와 환경 구성](install.md) · [ANIMA](anima.md)

<small>근거 — [초보자용 아니마 워크플로우 다섯종류 26.05](https://arca.live/b/aiart/170932870) · [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [ComfyUI - 산지직송 뉴비가 작성한, 하루만에 설치하고… 26.02](https://arca.live/b/aiart/163532702)</small>

??? note "근거 6건 전부 보기"
    [초보자용 아니마 워크플로우 다섯종류 26.05](https://arca.live/b/aiart/170932870) · [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [ComfyUI - 산지직송 뉴비가 작성한, 하루만에 설치하고… 26.02](https://arca.live/b/aiart/163532702) · [ANIMA All in One 워크플로우 v6.0: Easy… 26.06](https://arca.live/b/aiart/175299629) · [컴피 공홈에서 포터블 버전 받는 방법. 26.05](https://arca.live/b/aiart/170235453)

## ⚠ 남의 워크플로우가 터지면 sage-attention 부터 의심한다
<small>2026-08 기준 · 근거 6건</small>

6·7단계에서 남의 워크플로우를 불러오면 반드시 한 번은 오류를 만난다. **범인은 대개 정해져 있다.**

> **"많은 뉴비가 공유받은 워크플로우에서 오류가 터지는 범인은 세이지(sage-attention)"** (175397651, 2026-06)

sage-attention 은 어텐션 연산을 빠르게 하는 가속 라이브러리다. **워크플로우에 관련 노드가 보이지 않아도 실행 인자나 전역 설정으로 켜져 있는 경우가 많아서**, 노드를 아무리 뒤져도 원인이 안 보인다.

**확인 순서**

| | 확인 | 어떻게 |
|---|---|---|
| 1 | **sage 를 끄고 돌려 본다** | 통합팩이면 `run_nvidia_gpu_fast_fp16_accumulation.bat` 대신 **`run_nvidia_gpu.bat`** / 직접 구성이면 실행 인자에서 `--use-sage-attention` 을 뺀다 |
| 2 | 내 GPU 가 **RTX 2000번대(튜링)** 인가 | 통합팩에서 sage 를 켜면 터진다. **RTX 2060 Super 8GB 에서 sage 만 끄면 정상 동작**이 확인돼 배포글 본문에도 반영됐다 |
| 3 | Forge Neo 에서 **검은 화면** + 로그에 `Encountered NaN in Latent; Try --disable-sage` | 같은 신호다 |
| 4 | 그래도 쓰겠다면 | **튜링용 wheel 을 따로 받는다** ↓ |

```
# ComfyUI 공식 wheels — 튜링(RTX 20 시리즈)은 대응하지 않는다
https://comfy-org.github.io/wheels

# 튜링은 이쪽 Windows fork
https://github.com/woct0rdho/SageAttention
```

이 경고는 색인글 댓글 1번의 제보로 **본문에 경고문이 추가된** 내용이다. 같은 시기 튜링용 `flash-attention` 도 존재하지만(`https://github.com/ssiu/flash-attention-turing`) **whl 이 제공되지 않아 직접 빌드해야 하므로**, 작성자는 꼭 필요한 게 아니면 굳이 설치하지 말라고 권한다.

**켜서 얻는 것과 잃는 것**

| | |
|---|---|
| 얻는 것 | 생성 속도 **10~15% 향상** |
| 잃는 것 | **손가락 찐빠가 늘어난다는 보고**가 통합팩 배포글 여러 편에 붙어 있다 |
| 결론 | 2D 짤만 뽑을 거면 **꺼도 무방하다.** 오류가 나는데 원인을 모르겠으면 끄는 쪽이 먼저다 |

> comfy-cli 로 직접 구성한 환경에서는 튜링도 sage-attention 을 쓸 수 있다는 댓글이 있다 — 위 woct0rdho fork 의 wheel 을 지정해 깔기 때문이다.

증상별 대응은 [오류 해결](troubleshooting.md) 의 'ComfyUI · 포터블 계열' 표에 더 있다.

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328)</small>

??? note "근거 6건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [Comfy CLI 설치 방법 정리 26.05](https://arca.live/b/aiart/169751935) · [튜링용 flash-attention 26.07](https://arca.live/b/aiart/176657130)

## SageAttention — 입문의 '통곡의 벽' 을 세 줄로 넘기
<small>2026-02 기준 · 근거 4건</small>

바로 위 항목이 "터지면 sage 부터 끄라"였다면, 이 항목은 **왜 다들 이걸 기어이 깔려고 하는가**와 **어떻게 까는가**다.
Easy-Install 배포글은 이걸 두고 **"보통은 이걸 까는 게 ComfyUI 입문의 '통곡의 벽'"** 이라고 적었다 (161826600, 2026-02).

### 무엇인가

> SageAttention 은 **어텐션 연산을 양자화해 생성 속도를 올려 주는 구현**이다. Illustrious 짤뽑에서도 빨라지지만 **어텐션 시퀀스가 긴 최신 모델(비디오·ANIMA 등)에서 효과가 더 크다.** (162993309, 2026-02)

### 설치 — 포터블 기준 세 줄

포터블 루트(`ComfyUI` 폴더와 `python_embeded` 가 **같이 있는** 경로)에서 빈 공간을 클릭하고 주소창에 `cmd` 를 입력해 그 경로의 터미널을 연 다음:

```
.\python_embeded\python.exe -m pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post4/sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl

curl -O -L https://github.com/woct0rdho/triton-windows/releases/download/v3.0.0-windows.post1/python_3.13.2_include_libs.zip
tar -xf python_3.13.2_include_libs.zip -C python_embeded

.\python_embeded\python.exe -m pip install triton-windows
```

- **가운데 줄이 왜 필요한가** — 포터블에는 **파이썬 dev(include/libs) 파일이 빠져 있어서**, 이 zip 을 `python_embeded` 에 풀어 넣지 않으면 triton 이 동작하지 않는다.
- **시스템 파이썬이 아니라 `python_embeded` 에 깐다.** 명령은 포터블 **최상위** 폴더 기준이다.
- 설치형(포터블이 아닌 것)은 파이썬 바이너리가 보통 `내 문서\ComfyUI\.venv` 아래에 있다.
- 딸깍으로 끝내고 싶으면 → [설치와 환경 구성](install.md) 의 'ComfyUI-Easy-Install' (`Add-Ons` 의 SageAttention 을 더블클릭하면 Triton 까지 함께 깔린다)

### 켜는 법 두 가지

| 방법 | 어떻게 | 성질 |
|---|---|---|
| 실행 인자 | 실행 bat 의 실행 줄에 `--use-sage-attention` 추가 | 전역. **워크플로우에 관련 노드가 없어도 걸린다** |
| 노드 | ComfyUI-KJNodes 의 `Patch Sage Attention KJ` 를 모델 선에 통과시킨다 (`sage_attention=auto`, `allow_compile=true`) | **켜고 끄기가 쉽다** — 원문 작성자가 선호하는 쪽 |

> `allow_compile` 항목이 안 보이는 버전이 있는데 **없어도 기본보다는 빠르다.** `auto` 로 두면 triton 이 안 도는 줄 아는 오해가 있으나, CUDA 백엔드도 이 노드가 triton 을 요구해서 같이 깔리는 것이고 이론상 CUDA 백엔드가 트리톤 백엔드보다 빠르다. 편한 대로 쓰면 된다. (162993309 댓글)

### 노드 순서 — 여기서 많이 틀린다

```
모델 로드 → 로라(Power LoRA Loader) → Patch Sage Attention → KSampler
```

**로라가 sage 앞이다.** (162993309 댓글) ED 노드를 쓴다면 로더와 샘플러 사이에 `Context(rgthree)` 를 넣어 로더에서 모델을 뽑아 적용하고 덮어쓰면 되고, qwen-image-edit 이나 ANIMA 처럼 모델이 나오는 자리에도 똑같이 붙인다.

### fp16 누산도 같이 켜면 더 빠르다

실행 인자 `--fast` 대신 KJNodes 의 `Model Patch Torch Settings` 노드를 연결하고 `enable_fp16_accumulation` 을 켜도 된다.
실행 인자로 쓸 때의 전체 값 목록(`--fast fp16_accumulation fp8_matrix_mult cublas_ops`)은 → [설치와 환경 구성](install.md) 의 'RTX 5000번대'

### 끄는 법 · 안 되는 경우

| 상황 | |
|---|---|
| 그냥 끄고 싶다 | 통합팩이면 `run_nvidia_gpu_fast_fp16_accumulation.bat` 대신 **`run_nvidia_gpu.bat`** / 직접 구성이면 실행 인자에서 `--use-sage-attention` 제거 / 노드 방식이면 그 노드를 **Ctrl+B** 로 바이패스 |
| 모델에 따라 안 된다 | **아주 가끔 화질이 나빠지거나 아예 동작하지 않는다.** 음악 생성 모델 **Ace-step 은 sage 로 실행하면 소리가 안 난다.** z-image 충돌 사례도 댓글에 있다 (161826600) |
| RTX 20 시리즈(튜링) | Triton 버전 함정이 따로 있다 — **반드시 3.2** → [설치와 환경 구성](install.md) |
| 어제까지 잘 되던 게 갑자기 깨졌다 | ↓ 바로 아래 항목 |

→ [설치와 환경 구성](install.md) · [VRAM·속도 최적화](vram.md) · [오류 해결](troubleshooting.md)

<small>근거 — [ComfyUI Portable 설치 쉽게 하는 툴 하나 소개함 26.02](https://arca.live/b/aiart/161826600) · [로컬 comfyui 찍먹해보기 - sage-attention… 26.02](https://arca.live/b/aiart/162993309) · [RTX 20 시리즈를 사용하는데 아니마는 써보고 싶은 사람들… 26.05](https://arca.live/b/aiart/170741530) · [pytorch 2.10 +  python 3.13 + RTX… 26.01](https://arca.live/b/aiart/160668279)</small>

## ⚠ 잘 돌던 sage 가 '갑자기' 깨진다 — 당신이 뭘 잘못한 게 아니다 (2026-03)
<small>2026-03 기준 · 근거 2건</small>

### 증상

어제까지 멀쩡했는데 갑자기 이 두 줄이 쏟아진다. 그림이 나오기는 하지만 **pytorch attention 으로 폴백되어 느려지고** 에러 로그가 어마어마하게 뜬다. RTX 50번대(sm120) 사용자가 특히 겪는다.

```
Error running sage attention: CUDA error: no kernel image is available for execution on the device
cudaErrorNoKernelImageForDevice
```

### 원인 — 사용자가 뭘 잘못한 게 아니다

> 설치해 둔 sageattention 이 `2.2.0+cu130torch2.9.0andhigher.post4` 였는데 **어느 순간 `2.2.0+cu130torch210` 으로 바뀌어 있었다.** 이 버전이 50번대(sm120)를 지원하지 않아 생긴 일이다.
> **범인은 ComfyUI Manager 다** — 커스텀 노드의 의존성을 자동으로 설치·갱신하면서 sageattention 까지 갈아치운다. 대표적으로 **SAM3** 커스텀 노드가 그렇다(원문 작성자 본인 케이스도 SAM3). (163926460, 2026-03)

**설정을 건드린 적도, 업데이트 버튼을 누른 적도 없이 깨질 수 있다.** 커스텀 노드를 하나 깐 것이 방아쇠다. 최근에 SAM3 를 깔았다면 그것부터 의심한다.

| sageattention 버전 | sm120(RTX 50) |
|---|---|
| `2.2.0+cu130torch2.9.0andhigher.post4` | 정상 |
| `2.2.0+cu130torch210` | **미지원 — 이 오류가 난다** |

### 1. 즉시 되돌리기

원래 받았던 포터블 압축을 다른 곳에 다시 풀어 두고 **sageattention 만 갈아 끼운다.**

```powershell
# (1) 문제 환경에서 제거
& $badPy -m pip uninstall -y sageattention

# (2) python_embeded\Lib\site-packages 에 남아 있을 수 있는
#     sageattention 폴더와 sageattention-*.dist-info 를 강제 삭제

# (3) 정상 환경의 같은 폴더 두 개를 복사해 넣는다

# (4) 확인
& $badPy -m pip show sageattention
```

### 2. 재발 방지 — 이 글의 진짜 수확

ComfyUI Manager 에는 **의존성을 강제로 치환하는 수단**이 있다. wheel 을 프로젝트 안에 넣고 고정한다.

1. `pip cache dir` 에서 지금 쓰는 sageattention wheel 을 찾아 `ComfyUI\user\__manager\wheels\` 로 복사한다
2. `ComfyUI\user\__manager\pip_overrides.json` 에 적는다

```json
{
  "sageattention==2.2.0+cu130torch210": "sageattention @ ./ComfyUI/user/__manager/wheels/<wheel 파일명>",
  "sageattention": "sageattention @ ./ComfyUI/user/__manager/wheels/<wheel 파일명>"
}
```

3. `ComfyUI\user\__manager\pip_auto_fix.list` 에도 같은 항목을 넣는다

그러면 **매니저가 sageattention 을 요구해도 지정한 로컬 wheel 로 치환된다.**
`pip_overrides.json` / `pip_auto_fix.list` 는 sage 뿐 아니라 **매니저가 멋대로 바꾸면 곤란한 모든 패키지**에 쓸 수 있는 수단이다 — 이걸 알아 두는 것이 이 글에서 건질 가장 큰 것이다.

> **한 글에서만 제시된 방법이다** (163926460, 2026-03, 추천 3). 다만 댓글에서 "챈럼이 만들어 둔 sage 휠로 설치하니 문제가 없었다", "SAM3 를 최근에 깔았다면 그걸 의심하라"는 확인이 붙었고, 결론은 **"안정화될 때까지 새 버전은 안 쓰는 게 맞다"** 였다.

### 비슷한 버전 어긋남

`ImportError: DLL load failed while importing _fused: 지정된 프로시저를 찾을 수 없습니다` 도 같은 계열이다. torch/python/sageattention/cuda 버전이 어긋난 것이므로 **파이썬 버전 무관 빌드(`cp39-abi3`)** 로 바꾸면 해결된다 (160668279 댓글) → [설치와 환경 구성](install.md)

→ [오류 해결](troubleshooting.md) · [설치와 환경 구성](install.md)

<small>근거 — [pytorch 2.10 +  python 3.13 + RTX… 26.01](https://arca.live/b/aiart/160668279) · ['갑자기' comfy 에서 sage-attension 실패하… 26.03](https://arca.live/b/aiart/163926460)</small>

## 버전별 인스턴스로 나눠 쓰기 — 업데이트하다 터지는 사고를 원천 차단 (2026-06)
<small>2026-06 기준 · 근거 3건</small>

통합팩 배포글들이 하나같이 **"본체 업데이트는 절대 하지 말고 새 버전이 나오면 처음부터 새로 받으라"** 고 못박는 이유는, ComfyUI 를 올렸다가 커스텀 노드가 무더기로 깨지는 사고가 흔하기 때문이다. 이 문제를 **구조로** 푸는 방법이 있다 (172936836, 2026-06).

### 발상

본체만 버전별로 나누고 **모델 폴더·결과물 폴더·user 폴더는 공유한다.**

```
D:\ComfyUI\ComfyUI_main\
  instances\   ComfyUI_v0.24.0\ , ComfyUI_v0.26.0\ ...   ← 본체만 여러 개
  models\      ← 공유
  outputs\     ← 공유
  user\        ← 공유 (버전을 완전히 독립시키려면 여기도 버전별로 나눈다)
  scripts\     ← 실행 bat
```

경로가 너무 길면 안 되고 **중간에 한글·특수문자가 들어가면 일부 커스텀 노드에서 문제가 생긴다.**

### 핵심은 인자 하나

```powershell
comfy --skip-prompt --workspace "$INSTANCE_ROOT" install --nvidia --version 0.24.0 --skip-torch-or-directml
```

`--skip-torch-or-directml` 이 핵심이다 — PyTorch 는 나중에 **원하는 CUDA 판으로 직접** 깔려고 여기서 건너뛴다.
uv·comfy-cli 설치와 torch·triton·sage 명령 전문은 → [설치와 환경 구성](install.md)

### 운용 규칙 셋

| | |
|---|---|
| **모델 공유** | 인스턴스 루트마다 `extra_model_paths.yaml` 을 넣고 `base_path` 를 공통 폴더로 잡는다. **인스턴스를 새로 만들 때마다 이 파일을 복사**해야 하고, 로라 매니저의 추가 폴더 경로도 중복되지 않게 설정한다 |
| **동시 실행** | 포트를 `--port 8188` / `8189` 처럼 다르게 준다. (포터블도 폴더만 다르면 여러 개 깔 수 있지만, 동시에 켜려면 마찬가지로 포트를 나눠야 한다) |
| **업데이트** | **중요한 작업 환경이면 업데이트하지 말고 새 인스턴스를 하나 더 만든다.** 굳이 하려면 `comfy --workspace "<경로>" update` |

인스턴스를 지울 때는 **해당 폴더만 삭제**하면 되고 uv 쪽에 따로 할 일은 없다(댓글).

### 자주 나는 문제

| 증상 | 원인 |
|---|---|
| `comfy` 명령을 인식하지 못함 | PowerShell 재실행 / PATH |
| `torch.cuda.is_available()` 가 False | CPU 판 torch 가 깔렸거나 드라이버·CUDA wheel 불일치 |
| SageAttention import 오류 | wheel 과 torch/CUDA 조합 불일치 |
| `cl is not found` | torch.compile 계열이 윈도우 C++ 컴파일러를 못 찾는 것 — Visual Studio Build Tools 의 C++ 도구를 깔거나 compile 을 끈다 |
| `extra_model_paths.yaml` 을 넣었는데 모델이 안 보임 | 파일 위치 · YAML 들여쓰기 · 키 중복 확인. **특히 폴더 종류별 키(`loras`, `vae`, `upscale_models` 등)가 빠져 있으면 그 종류만 통째로 안 보인다** |

> **한 글에서만 제시된 구성이다** (172936836, 2026-06, 추천 8). 다만 "포터블 구버전이 무조건 나쁜 것은 아니고, 최신에서 말썽부리는 노드가 있으면 구버전에서 작업하는 편이 낫다"는 판단은 통합팩 배포글들이 공유한다.

→ [설치와 환경 구성](install.md) · [오류 해결](troubleshooting.md)

<small>근거 — [ComfyUI Portable 설치 쉽게 하는 툴 하나 소개함 26.02](https://arca.live/b/aiart/161826600) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [ComfyUI 버전 여러개 쓰기: UV와 ComfyCLI 기… 26.06](https://arca.live/b/aiart/172936836)</small>

## ⚠ 남의 워크플로우가 안 돌아가는 진짜 이유 — 모델 파일이 박혀 있다
<small>2026-08 기준 · 근거 5건</small>

받은 워크플로우를 열자마자 Run 을 눌렀는데 아무것도 안 나온다면, 십중팔구 당신 잘못이 아니라 **파일 경로** 문제다.

> **"남의 워크플로우에는 그 사람이 쓰던 파일이 할당돼 있고, 당신이 같은 파일을 쓸 확률은 1% 도 안 된다."**
> — 141704804 (2025-07)

워크플로우는 "어떤 모델 파일을 쓸지" 를 **파일명 그대로** 저장한다.
원작자가 쓰던 그 체크포인트·로라·VAE 파일이 **내 폴더에 같은 이름으로 없으면** ComfyUI 는 없는 파일을 찾다 멈춘다.
**해결책은 하나뿐이다 — 각 로더 노드에서 파일명을 눌러 자기 폴더의 파일로 바꾼다.**

### 증상 → 대처 표

| 증상 | 진짜 원인 | 대처 |
|---|---|---|
| Run 을 눌렀는데 **바로 오류**, 노드 하나가 **핑크색**으로 칠해짐 | 그 노드가 요구하는 **파일이 없다** | 로더 노드의 파일명 드롭다운을 열어 **내 파일로 교체** |
| 핑크 노드가 **안 보인다** | 시각적 정리를 위해 **로더 노드를 다른 노드 뒤에 숨겨** 뒀다 | 좌측 상단 동그라미로 노드를 **접어 가며** 뒤를 확인 |
| 로더를 눌렀는데 **목록이 비어 있다** | 파일을 **엉뚱한 폴더**에 넣었다 | [설치와 환경 구성](install.md) 의 폴더 경로 표 |
| 그림 대신 **노이즈만** 나온다 | `ModelSamplingDiscrete` 등에 **`v_prediction` 이 켜져 있는데 내 모델은 v-pred 가 아니다** | 그 노드를 **바이패스하거나 지운다** |
| 로라를 끼웠더니 결과가 무너진다 | **체크포인트와 로라의 기반 계열이 다르다** | 체크포인트와 **같은 기반**의 로라를 쓴다 |
| 노드가 **빨갛게** 뜨거나 자리가 비어 있다 | 파일이 아니라 **커스텀 노드**가 없다 | ↓ "미싱 노드" 절 |
| 오류는 없는데 **원글만큼 안 나온다** | 다른 체크포인트를 끼웠으면 **수치를 다시 조정**해야 한다 | ↑ "워크플로우 불러오기" 절 |
| 배포본의 **장수·격자 수가 이상하다** | 원작자가 자기 값을 **수정하지 않고 올렸다** | `end-index`(총 장수) · `max-columns`(X축 개수) 를 직접 고친다 |

### 왜 폴더를 알아야 하는가

`ComfyUI/models/` 아래 폴더는 각각 역할이 있고, **워크플로우의 로더 노드는 그 폴더만 본다.**

| 폴더 | 무엇이 들어가나 |
|---|---|
| `checkpoints` | **모델 본체.** SDXL · Flux · Pony · Illustrious · NoobAI 등 |
| `controlnet` | 레퍼런스를 잡아 주는 모델. 필수는 아니지만 많은 워크플로우에 기본 탑재 |
| `loras` | 추가 학습. **체크포인트와 같은 기반의 로라를 써야 한다** |
| `ultralytics` | 디테일러가 쓰는 **검출(인식) 모델.** '그리는 모델' 이 아니다 |
| `upscale_models` | 업스케일용 |
| `vae` | latent 를 그림으로 해독. ILXL 계열은 대부분 내장이라 잘 안 쓰이지만, 아닌 모델은 여전히 필요하다 |

### v-pred 노드 — 노이즈만 나오는 대표 원인

원작자가 v-pred 모델을 썼다면 워크플로우에 **v-pred / CFG 리스케일 노드**가 들어 있을 확률이 높다.
**v-pred 가 아닌 모델에 `v_prediction` 을 적용하면 이미지가 노이즈만 나온다.**
자기 모델이 지원하지 않으면 그 노드들을 비활성화하거나 지워야 한다.
(순정 A1111 에서 v-pred 모델을 쓰는 방법은 → [설치와 환경 구성](install.md))

### 오류를 읽는 법

ComfyUI 는 **오류가 난 노드를 핑크색으로 하이라이트**해 준다. 거기만 다시 확인하면 기초 문제는 대부분 풀린다.
AI 에게 물을 때 요령도 하나 있다 — **Show Report 의 장문 로그를 통째로 넣지 말고 에러와 관련된 문단만 추려서** 넣어야 정확한 답이 나온다.

### 곁들여 알아 두면 화면이 읽힌다

- **데이터는 무조건 왼쪽 → 오른쪽으로 흐른다.** 노드 왼쪽 위 ○ 이 입력, 오른쪽 위 ○ 이 출력이다.
- 노드를 클릭하면 **연결된 그래프가 하얗게** 하이라이트된다. 색을 따라가면 무엇이 어디로 가는지 보인다.
  단 **연결선 색은 테마에 따라 달라지므로 절대 기준으로 삼지 마라.**
- 그룹을 한꺼번에 켜고 끄는 스위치 노드는 우클릭 → Properties → `matchTitle` 에 `A|B|C|D` 형식으로
  키워드를 넣으면 제목에 그 키워드가 든 그룹이 자동으로 잡힌다.

→ 노드가 없어서 나는 문제는 아래 "미싱 노드", 그 밖의 오류 문구는 [오류 해결](troubleshooting.md)

<small>근거 — [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780) · [ComfyUI 초보자를 위한 워크플로우 사용 가이드 25.07](https://arca.live/b/aiart/141704804) · [내가 쓰고있는 ComfyUI 워크플로우 공유 (SDXL, A… 26.08](https://arca.live/b/aiart/179640921) · [NoobAI-ILXL 병합 플롯 25.04](https://arca.live/b/aiart/134064704)</small>

??? note "근거 5건 전부 보기"
    [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780) · [ComfyUI 초보자를 위한 워크플로우 사용 가이드 25.07](https://arca.live/b/aiart/141704804) · [내가 쓰고있는 ComfyUI 워크플로우 공유 (SDXL, A… 26.08](https://arca.live/b/aiart/179640921) · [NoobAI-ILXL 병합 플롯 25.04](https://arca.live/b/aiart/134064704) · [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179637421)

## 파일을 다 맞췄는데도 터진다 — 배포 워크플로우의 고장 지점 넷
<small>2025-12 기준 · 근거 5건</small>

파일을 다 맞췄는데도 터진다면 아래 넷 중 하나인 경우가 많다. **전부 배포글 댓글에서 확인된 것들이다.**

| 증상 | 원인 | 해결 |
|---|---|---|
| `Failed to get input node 0 for group node child ... with slot 0` | ComfyUI 업데이트로 **그룹 노드 처리 방식이 바뀌었다** (issue 8887) | **그룹 노드를 먼저 해제**한 뒤 **서브그래프로 변환** |
| 매니저가 **미싱 노드를 못 잡는다** | **데스크톱 버전**을 쓰고 있다 | **포터블 버전**으로 옮긴다 |
| 매니저에서 다 깔았는데 특정 노드팩이 **안 돈다** | 워크플로우에서 직접 안 쓰여 **`In workflow` 목록에서 빠졌다** | 예: `efficiency-nodes-ED` 는 **`efficiency-nodes-comfyui` 가 있어야** 동작한다 — 수동 설치 |
| 노드팩을 업데이트했는데 **UI 가 그대로다** | 커스텀 노드가 **`user.css` 등 UI 파일을 덮어쓰는** 구조라 갱신이 안 먹는다 | 매니저에서 **disable → 재시작 → enable → 재시작** |

```
# ComfyUI 그룹 노드 오류 원문
https://github.com/comfyanonymous/ComfyUI/issues/8887
```

### 배포자가 쓰는 요령 하나 — 없는 노드를 일부러 넣어 둔다

**ComfyUI Manager 의 missing nodes 는 워크플로우가 실제로 쓰는 노드만 잡는다.**
그래서 KJ Nodes 처럼 그룹 노드 안에 숨어 있는 의존성은 감지되지 않는다.
한 배포자는 **KJ Nodes 의 `Dummy out` 노드를 일부러 워크플로우에 넣어** missing nodes 에 잡히게 만들었다.
**받는 쪽에서 빨간 줄이 뜨는 `Dummy out` 은 설치를 유도하려고 넣은 기능 없는 노드이므로, 설치가 끝났으면 지워도 된다.**

### 손으로 깔아야 하는 것들

`SDPromptReader` / `SDPromptSaver` 는 매니저에서 자주 실패한다. 그때는 지우고 수동으로 깐다.

```bash
# ComfyUI/custom_nodes 폴더에서
git clone --recursive https://github.com/receyuki/comfyui-prompt-reader-node.git
cd comfyui-prompt-reader-node
pip install -r requirements.txt
```

`Impact Pack` 업데이트 후 FaceDetailer 계열이 죽는 것은 **`UltralyticsDetectorProvider` 가 서브팩으로 분리**됐기 때문이다.
**`ComfyUI-Impact-Subpack` 을 설치하면 해결된다.** 기존 워크플로우는 `Load Image ED` 노드를 **우클릭 → Fix node (recreate)** 해 줘야 한다.

### ⚠ 배포 워크플로우에는 '넘으면 터지는 상한' 이 있다

빡통워크 계열은 **그림체 칸을 0~8번(최대 8개)까지만** 쓸 수 있다.
**9번 이상을 쓰면 오류가 나며 워크플로우가 통째로 뻗는다.** *(이 제약은 본문에 없고 댓글에서만 밝혀졌다.)*

와일드카드 노드를 **서브그래프로 묶으면 오류가 났다는 보고**도 있다 — 결국 풀어서 쓰고 있다고 한다.

### 만료된 배포 링크

`kio.ac` · `mega.nz` · 구글드라이브로 배포된 워크플로우는 **보관 기간이 짧거나 링크가 죽는다.**
빡통워크 5.0(2025-07)의 `kio.ac` 링크는 댓글에도 재공유 요청이 달려 있다. **본문 링크가 죽었으면 후속판 글을 찾는 편이 빠르다.**

→ 미설치 노드를 채우는 네 가지 경로는 아래 "미싱 노드" 절, 오류 문구별 대응은 [오류 해결](troubleshooting.md)

<small>근거 — [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780) · [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림… 25.12](https://arca.live/b/aiart/157410060) · [쉽고 빠른 ComfyUI V6 마이너 업데이트 24.12](https://arca.live/b/aiart/122761449) · [빡통워크 5.0 : 배치 로더 자동화 랜덤그림체 짤뽑 25.07](https://arca.live/b/aiart/143059270)</small>

??? note "근거 5건 전부 보기"
    [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780) · [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림… 25.12](https://arca.live/b/aiart/157410060) · [쉽고 빠른 ComfyUI V6 마이너 업데이트 24.12](https://arca.live/b/aiart/122761449) · [빡통워크 5.0 : 배치 로더 자동화 랜덤그림체 짤뽑 25.07](https://arca.live/b/aiart/143059270) · [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179637421)

## ⚠ 와일드카드가 같은 조합만 뱉는다 — `{ A | B }` 는 랜덤이 아니다
<small>2025-11 기준 · 근거 3건</small>

와일드카드를 걸어 두고 100장을 돌렸는데 **같은 조합만 반복해서 나온다면** 버그가 아니라 문법 문제다.

### ⚠ `{ A | B | C }` 는 랜덤이 아니다

**Dynamic Prompts 의 `{ A | B | C }` 는 모든 가짓수를 `A → B → C` 순으로 도는 사이클이다.**
게다가 WAS Node 의 분기(Input Switch)는 **노드를 정지시키는 것이 아니라 플로우 라인만 전환**하므로,
선택되지 않은 쪽 노드도 **계속 사이클을 돈다.**

```text
1girl, { outdoor | indoor }
실외 의상: { 바니걸 | 라텍스 슈츠 }
실내 의상: { 비키니 | 고양이 란제리 }

→ outdoor+바니걸 → indoor+고양이 란제리 → outdoor+바니걸 → …
   특정 조합만 반복되고 나머지는 영영 안 나온다
```

**해결책: 여는 중괄호 옆에 물결표를 붙인다.**

```text
{~outdoor | indoor }
```

이러면 완전 랜덤으로 돌아서, 시도 횟수만 충분하면 모든 조합이 나온다.

### 조건 분기(if 문) 만들기

| 필요한 것 | 링크 |
|---|---|
| Dynamic Prompts | `https://github.com/adieyal/sd-dynamic-prompts` |
| WAS Node Suite | `https://github.com/WASasquatch/was-node-suite-comfyui` |

**`Text Contains` + `Input Switch`** 를 조합하면 입력 텍스트에 특정 키워드가 있느냐로 `text_a` / `text_b` 를 갈라 낼 수 있다.
같은 방식을 `Lora Input Switch` 에 물리면 **프롬프트에 그 키워드가 있을 때만 해당 로라로 선로를 잇는다.**
100~200장을 걸어 두면 로라와 의상을 알아서 맞춰 뽑아 준다.

**단점도 분명하다** — PNG info 에는 모든 로라가 적용된 것처럼 표시되고(실제로 다 적용되지는 않는 듯하다), 배선이 복잡해져 나중에 손보기가 힘들다.

### 와일드카드 운용 원칙

- **고정시킬 태그는 직접 적고, 변화시킬 태그만 와일드카드로 돌린다.** 순서대로 뽑고 싶으면 텍스트 멀티라인을 쓴다.
- 와일드카드 노드는 **Impact-Pack** 안의 텍스트 출력형 노드를 쓴다 *(댓글)*.
- 프롬프트를 자리별로 나눠 두면 관리가 쉽다:
  `품질,검열 / 카운팅,캐릭터,작품명,작가 / 구도,배경 / 외형,의상 / 행동,기타`
- 공식 그림체를 강하게 붙잡고 싶으면 공식 작가 태그에 `anime coloring, anime screenshot, official art` 를 함께 쓴다.
- 리저널 프롬프트를 쓸 게 아니라면 **여캐 중심 구도에서는 여캐에만 로라를 투자**하고, 남캐는 인페인팅이나 리저널로 넘기는 편이 낫다 *(한 글에서만 언급됨)*.
- ⚠ **와일드카드 노드를 서브그래프로 묶으면 오류가 난 사례가 있다.**

→ [프롬프트 쓰는 법](prompting.md) · [로라 쓰는 법](lora-usage.md)

<small>근거 — [ComfyUI If문 적용 Prompt 25.11](https://arca.live/b/aiart/153389527) · [ComfyUI - 와일드카드 25.11](https://arca.live/b/aiart/153827221) · [ComfyUI - 와일드카드 복습 25.11](https://arca.live/b/aiart/155383963)</small>

## 캐시 규칙 — seed 입력이 없는 노드는 다시 돌지 않는다 (2023-03, 지금도 유효)
<small>⚠️ 2023-03 기준 · 근거 1건</small>

**2023-03 에 정리된 규칙이지만 지금도 그대로 유효하다.** 알아 두면 "왜 이 노드는 값이 안 바뀌지" 를 안 헤맨다.

> **seed 입력값이 있는 노드 이후는 실행할 때마다 재계산되지만,
> seed 가 없는 노드는 입력값이 바뀌지 않는 한 재계산되지 않는다.**

그래서 이런 일이 벌어진다.

| 현상 | 이유 |
|---|---|
| 두 번째 생성부터 훨씬 빠르다 | 체크포인트·VAE 로드, Latent 생성이 **캐시에서 재사용**된다 |
| '현재 시각을 문자열로 만드는' 노드가 **한 번만 동작**한다 | seed 입력이 없어서 재계산되지 않는다 → 그런 노드에는 **seed 입력을 붙여야** 한다 |
| 시드를 고정하면 샘플러까지 건너뛴다 | 같은 이유다 |

모든 노드를 무조건 재계산하게 만들면 **모델 로드·샘플러 로드까지 다시 도는 낭비**가 생긴다.
캐시는 고장이 아니라 설계다.

### 같은 시절의 함정 하나 (2023-03)

**ComfyUI 의 '저장할 때 이미지 미리보기' 는 기본 `output` 폴더로 고정돼 있다.**
저장 경로를 바꾼 커스텀 노드에서는 이미지가 뜨지 않으므로, 그때는 **기본 preview 노드**를 따로 붙여야 한다.

<small>근거 — [Comfy UI 노드 추가중 23.03](https://arca.live/b/aiart/72115884)</small>

## 폴더의 짤을 태깅해 다시 뽑기 — 배치 자동화 워크플로우
<small>2025-12 기준 · 근거 2건</small>

태그를 짜기 귀찮을 때 쓰는 구조다. **이미 있는 그림을 자동으로 태깅해서 그 태그로 다시 뽑는다.**

```text
폴더의 짤 무작위 로드 → WD14Tagger 로 태깅 → 그 태그를 프롬프트로 → 생성
                                        (+ 그림체 랜덤 스위치)
```

큐를 100개 걸어 두고 설거지하고 오면 짤이 쌓여 있다는 것이 이 계열('빡통워크')의 취지다.

| 항목 | 값 |
|---|---|
| 이미지를 넣는 곳 | `(ComfyUI 설치 폴더)\input\batch load` — 없으면 그 이름으로 만든다 |
| 특정 태그 금지 | `WD14Tagger` 노드의 **`exclude_tags`** 칸에 적는다 |
| 그림체 칸 | **0~8번만.** 9번 이상은 워크플로우가 뻗는다 *(댓글)* |
| 순차로 돌리기 | 인덱스 위젯의 **'생성 후 제어' 를 `INCREMENT`** 로 |
| 수동 지정 | 수동 로드 노드에 이미지를 올리고 스위치를 2로 |

**태거가 모르는 캐릭터**(예: 마이너 캐릭터)는 태깅되지 않는다.
그래서 그 캐릭터 짤만 따로 모아 두고 프롬프트 칸에 `yoshimi \(blue archive\),` 처럼 직접 적어 보완한다.
프롬프트 입력칸을 1·2 로 나눠 두는 배포본이 많은 것은 이 때문이다.

배포자 기본 세팅(2025-07, NAI_XL V-pred 2dac colorized 기준):

| | |
|---|---|
| CFG | `0.6` |
| 스텝 | `50` |
| 샘플러 / 스케줄러 | `euler_a_cfg_pp` / `sgm_uniform` |

6.0 판(2025-12)에는 SAM3 디테일러(눈·손)와 레퍼런스 컨트롤넷이 붙었다.
**컨트롤넷을 강하게 걸면 생성 시간이 2배가 되고 찐빠가 잦으므로** 워크플로우의 노트를 보고 강도를 조절한다.
업스케일은 `2X ANIME SHARP` 에 0.75 배율이 기본값이다.

→ [프롬프트 쓰는 법](prompting.md) · [디테일러](detailer.md) · [업스케일과 화질](upscale.md)

<small>근거 — [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림… 25.12](https://arca.live/b/aiart/157410060) · [빡통워크 5.0 : 배치 로더 자동화 랜덤그림체 짤뽑 25.07](https://arca.live/b/aiart/143059270)</small>

## 워크플로우 불러오기 — 파일을 ComfyUI 창에 끌어다 놓는다
<small>2026-08 기준 · 근거 7건</small>

채널에서 워크플로우를 공유하는 방식은 거의 예외 없이 **결과물 파일에 EXIF 로 워크플로우를 심어 올리는 것**이다.
따라서 `.json` 을 찾을 게 아니라 **본문의 이미지나 영상을 다운로드해 ComfyUI 창에 드래그앤드롭**하면 된다.
다섯 개 이상의 배포글이 같은 방식을 안내한다.

| 배포 형태 | 하는 법 |
|---|---|
| PNG 짤 | 짤을 다운로드해 ComfyUI 창에 드래그 |
| 결과 영상 mp4 | **확장자를 바꾸지 말고** mp4 그대로 드래그드롭 |
| 커스텀 노드 동봉형 | `nodes_dully.py` 를 `custom_nodes` 폴더에 넣고 ComfyUI 재시작 → `WAN22_Universal_Dully.png` 를 드래그 |
| 구글드라이브 `.json` | 받아서 드래그 (동일) |

주의할 점 두 가지.

- **스샷에는 EXIF 가 없는 경우가 많다.** 워크플로우 스샷이 아니라 *결과물 파일* 을 받아야 한다.
  MiniMax H3 레퍼런스 I2V 배포글은 스샷에 EXIF 가 없고 결과 mp4 에만 들어 있었다.
- **아카라이브에 올릴 때는 업로드 전에 `exif 데이터 보존` 을 체크**해야 워크플로우가 살아남는다.
  드래그앤드롭으로 그냥 올리면 날아간다(댓글 제보). 실제로 EXIF 가 날아가 워크플로우 복사가 안 된다는
  제보가 붙은 배포글이 여럿이다.

불러온 뒤 체크포인트 로드 노드에서 **파일을 다시 선택**해야 하는 경우가 흔하다. 경로가 다르면 목록이 비어 있다.

**불러온 뒤에 손봐야 하는 것 하나 더** — 워크플로우에 적힌 **그대로의 모델**을 쓰면 괜찮지만,
**다른 체크포인트를 끼우면 수치를 다시 조정해야 한다.** 눈 디테일러를 그대로 돌렸는데 뭉개진다는 제보에
"워크플로우에 있는 그대로의 모델이면 괜찮은데 다른 체크포인트를 끼면 수치를 조정해야 한다"는 답이 달렸다(댓글).
**"받은 워크플로우가 원글만큼 안 나온다" 의 절반은 이것이다.**

<small>근거 — [간단한 MinimaxH3 레퍼런스 I2V 워크플로우 공유 26.08](https://arca.live/b/aiart/179460713) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [뉴비용) 나는 진짜 업스케일만 하고 싶어요 26.03](https://arca.live/b/aiart/163774464) · [SCAIL-2 RV2V 편의성 패치 워크플로우 26.06](https://arca.live/b/aiart/173906280)</small>

??? note "근거 7건 전부 보기"
    [간단한 MinimaxH3 레퍼런스 I2V 워크플로우 공유 26.08](https://arca.live/b/aiart/179460713) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [뉴비용) 나는 진짜 업스케일만 하고 싶어요 26.03](https://arca.live/b/aiart/163774464) · [SCAIL-2 RV2V 편의성 패치 워크플로우 26.06](https://arca.live/b/aiart/173906280) · [WAN2.2 SVI 결과에 음성 추가용 WAN2.2 (SVI… 26.06](https://arca.live/b/aiart/173733176) · [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179083162) · [뉴비의 간단한 워크 플로우 26.02](https://arca.live/b/aiart/161471075)

## 노드 여섯 개면 그림이 나온다 — 최소 워크플로우
<small>⚠️ 2023-09 기준 · 근거 1건</small>

불러온 워크플로우가 노드 40개짜리라도 **그림이 나오는 뼈대는 여섯 개뿐**이다.
나머지는 전부 그 뼈대에 붙은 장식(업스케일·디테일러·와일드카드)이라, 이 줄기만 눈에 익으면 화면이 갑자기 읽힌다.

```text
Load Checkpoint  →  CLIP Set Last Layer  →  CLIP Text Encode (긍정)
                                        →  CLIP Text Encode (부정)
                         Empty Latent Image  ┐
                                             ├→  KSampler  →  VAE Decode  →  Save Image
```

**2023년에 정리된 이 줄기가 지금까지 이름도 연결 방식도 바뀌지 않았다.** 그래서 오래된 입문글이 아직 유효하다.

| 노드 | 하는 일 | 헷갈리는 점 |
|---|---|---|
| `Load Checkpoint` | 모델을 읽는다 | 워크플로우를 불러오면 **파일을 다시 골라야** 하는 경우가 흔하다 |
| `CLIP Set Last Layer` | **이게 Clip Skip 이다** | WebUI 와 달리 **음수 값**을 입력한다 (`-2` 등) |
| `CLIP Text Encode` | 긍정·부정 프롬프트 | 두 개가 각각 KSampler 의 positive / negative 로 들어간다 |
| `Empty Latent Image` | 빈 캔버스 = 해상도 | |
| `KSampler` | 실제로 그리는 곳 | 빈 Latent 에서 시작하는 t2i 는 참조할 이미지가 없으므로 **디노이즈를 반드시 1** 로 둔다 |
| `VAE Decode` → `Save Image` | latent 를 그림으로 되돌려 저장 | |

**Queue Prompt 를 눌러야 비로소 돈다.** 값을 바꿔도 알아서 다시 그리지 않는다.
그리고 **두 번째 생성부터는 같은 작업을 건너뛴다** — 체크포인트·VAE 로드, Latent 생성이 재사용되고
**시드를 고정하면 샘플러까지 건너뛴다.** 두 번째가 훨씬 빠른 것은 고장이 아니다.

> 노드를 켜고 끄는 것이 조작의 전부라는 이야기는 아래 "노드를 다루는 최소 조작" 절에 있다.

<small>근거 — [(ComfyUI) 가장 기본적인 이미지 생성 워크플로우 가이드 23.09](https://arca.live/b/aiart/86110809)</small>

## 워크플로우를 어디서 구하나 — 직접 짜지 말고 골라 쓴다
<small>2026-08 기준 · 근거 3건</small>

채널의 방법론은 일관되게 **"노드를 이해해서 직접 짜기보다 남의 워크플로우를 골라 쓰는 편이 낫다"** 쪽이다.
이것저것 받다가 ComfyUI 가 망가지는 일이 적고 Q&A 도 빠르다는 이유다.

고르는 기준:

- Civitai 에서 **최근 1달~1년으로 필터**한 뒤 사용량이 가장 많은 것, 또는 기존에 쓰던 것의 최신 버전
- **체크포인트·베이스 모델을 직접 만드는 제작자**의 워크플로우를 우선
- 한 작성자 기준 선호: I2V 는 Dasiwa 제작자, 그 외는 Smooth 제작자
- 검색어가 안 먹는 경우가 있다. DaSiWa 의 MiniMax H3 워크플로우는 Civitai 에서 `minimax` 로 검색하면 나오지 않는다

기대치는 미리 낮춰 두는 게 좋다. **유명한 워크플로우도 10번에 5~7회 정도만 타율이 나오니 최소 2~3트는 해보라**는
조언이 있다(한 글에서만 언급됨).

받은 뒤 정리하는 요령으로는 한글화한 다음 `Get`/`Set` 노드로 묶고 서브그래프로 접는 방식이 제시된다.
다만 **서브그래프와 메인그래프 사이에서는 `Get`/`Set` 이 동작하지 않는다**는 제약이 있다(댓글 보충).

받는 곳 목록은 [자원 — 받는 곳 모음](resources.md) 에 따로 정리돼 있다.

<small>근거 — [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [ComfyUI - 맘에 드는 워크플로우 찾기 26.01](https://arca.live/b/aiart/160610621) · [ComfyUI - 다양한 워크플로우를 써 본 소감과 활용방법. 26.01](https://arca.live/b/aiart/160605007)</small>

## 미싱 노드 — 빨갛게 뜨는 것을 채우는 네 가지 경로
<small>2026-08 기준 · 근거 7건</small>

워크플로우를 불러왔는데 노드가 빨갛게 뜨거나 아예 자리가 비어 있으면 그 노드를 제공하는 확장이 없는 것이다.
채널에 나온 해결 경로는 네 가지이고, **위에서부터 시도**하면 된다.

| 순서 | 방법 | 언제 |
|---|---|---|
| 1 | ComfyUI Manager → **`Custom nodes in workflow`** | 대부분의 경우. 워크플로우가 요구하는 노드를 자동으로 찾아 설치 |
| 2 | 매니저에서 해당 노드팩을 **Nightly 로 지정** | 매니저에 있는데도 노드가 안 보일 때 |
| 3 | **`Install via git`** 또는 `custom_nodes` 에서 `git clone` | 매니저 목록에 아예 없을 때 |
| 4 | 깃허브 zip 을 받아 `custom_nodes` 에 압축 해제 | 검색이 안 잡히는 노드 |

실제 사례:

- `MiniMaxH3MemoryEfficientSageAttentionPatch` 는 **KJNodes 를 Nightly 로 지정해야 나타난다.**
  일반 `Patch Sage Attention` 노드로 대체할 수도 있다.
- `MiniMaxH3ImageToVideo`·`MiniMaxH3ReferenceToVideo`·`MiniMaxH3SigmaShift` 등 `MiniMaxH3*` 노드는
  **ComfyUI 0.30.0 이상에 내장**돼 있다. 즉 없다면 노드를 설치할 게 아니라 **본체를 올려야** 한다.
  반대로 `MiniMaxH3Cache` 만은 매니저에 없고 `https://github.com/lihaoyun6/ComfyUI-MiniMaxH3-Cache` 를
  `Install via git` 으로 넣어야 한다.
- `SimpleMathInt+` 는 매니저 검색에 안 잡혀 깃허브 zip 수동 설치 또는 Nightly 설치가 필요하다.
- Spectrum 계열은 `cd ComfyUI/custom_nodes && git clone https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3.git`

노드 이름이 이상하게 보이는 경우도 있다. `MiniMax H3 Mem Eff Sage Attention Patch` 와 `Patch Sage Attention KJ` 가
'엔크립트'·'어노말리' 계열 노드로 표시되는 것은 **오인식 오류**이며 원래 KJNodes 소속 노드다(댓글 정정).

증상별 대응은 [오류 해결](troubleshooting.md) 에 더 있다.

### 매니저로 다 되지 않는 이유 (알아 두면 덜 헤맨다)

*"워크플로우를 새 포터블에 넣고 `Install Missing Custom Nodes` 로 다 깔면 되지 않냐"* 는 질문에 나온 답이 정확하다.

> 커스텀 노드는 보통 **PyPI 에서 라이브러리를 받는데 특정 라이브러리는 특정 버전에서 설치가 안 되고,
> 제작자가 `requirements` 에 의존성을 빼먹기도 한다.** 그러면 `no module named ~` 로 `import failed` 가 계속 뜬다.
> 그럴 때는 **직접 빌드하거나 남이 미리 빌드한 wheel 을 깔아야 하는데 매니저는 그걸 지원하지 않는다.**

즉 위 표의 1~2번이 실패하는 것은 흔한 일이고, 그때는 손으로 깔아야 한다.
**의존성이 깨지는 대표적 계기는 PyTorch 버전업과 Python 버전업이다.**
이 수동 부분을 스크립트로 자동화한 것이 → [설치와 환경 구성](install.md) 의 '포터블 이사'

### 손으로 깔 때의 두 가지 요령

| | |
|---|---|
| **ZIP 수동 설치** | 저장소를 ZIP 으로 받아 압축을 풀고 **`ComfyUI/custom_nodes` 에 폴더째로** 넣은 뒤 **ComfyUI 재시작**. 매니저에 없는 노드는 대개 이 방법이다 |
| **의존성은 필요한 것만** | 전부 깔 필요 없이 **로드 시 작동 불가가 나는 것만** `python.exe -m pip install --no-deps 패키지명` 으로 추가한다. `--no-deps` 라서 기존 환경을 덜 건드린다 |

> ⚠ **커스텀 노드 폴더에 `requirements.txt` 가 있으면 ComfyUI 가 확장을 로딩할 때 자동으로 설치한다.**
> 그 자동 pip/git 설치가 환경을 망가뜨릴 위험이 커서, **`requirements.txt` 를 일부러 빈 파일로 두고**
> 필요한 것만 수동으로 깔게 만든 커스텀 노드도 있다. "왜 requirements 가 비어 있지" 싶으면 의도된 것이다.

포터블에서는 **시스템 파이썬이 아니라 `python_embeded` 의 파이썬**으로 깔아야 한다 → [오류 해결](troubleshooting.md)

<small>근거 — [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.… 26.01](https://arca.live/b/aiart/160657113) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [comfyui 개인제작노드(깃링크. P30.0기동확인) 26.02](https://arca.live/b/aiart/161492328) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965)</small>

??? note "근거 7건 전부 보기"
    [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.… 26.01](https://arca.live/b/aiart/160657113) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [comfyui 개인제작노드(깃링크. P30.0기동확인) 26.02](https://arca.live/b/aiart/161492328) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179083162) · [간단한 미니맥스(MiniMax) 워크플로우 공유 26.08](https://arca.live/b/aiart/178942263) · [comfyui 포터블 이사가는거 도와주는 스크립트 26.02](https://arca.live/b/aiart/162198611)

## ⚠️ 업데이트 — 매니저로 본체를 올리면 코어가 반영되지 않는다 (원칙이 갈린다)
<small>2026-08 기준 · 근거 3건 · **근거 약함** · 자료 엇갈림</small>

여기서 두 가지 상반된 원칙이 채널에 공존한다. **어느 쪽을 쓰는지에 따라 행동이 완전히 달라지므로 둘 다 적는다.**

**(가) 본체는 git 또는 `update_comfyui.bat` 으로 올려라** — 직접 설치·최신 기능 추종파

> ComfyUI Manager 로 업데이트하면 **코어(내장 노드) 변경이 반영되지 않는다.**
> ComfyUI 가 SAM3 를 자체 지원하기 시작했는데도 매니저로만 업데이트한 사람에게는
> SAM3 detect 노드가 보이지 않았다는 사례가 있다.
>
> - 최신 git 으로 pull, 또는 포터블 폴더 안의 `update_comfyui.bat` 실행
> - 릴리스에서 최신 엔비디아 버전을 받아 압축을 풀고 기존 **커스텀 노드 폴더 · 모델 폴더 · 워크플로우 폴더 · 유저 폴더**만 덮어쓰는 방법도 쓰인다

**(나) 본체 업데이트는 절대 하지 말고, 새 버전은 처음부터 새로 받아라** — 통합팩 배포자

> 통합팩 배포글들은 본체 업데이트를 금지한다. 커스텀 노드 호환성이 깨지기 때문이며,
> 실제로 0.15.1 판은 배포자 스스로 "커스텀 노드 찐빠가 심하다"며 이전 0.11.1 을 병행 배포했다.
> 2D 짤만 뽑을 거면 최신 버전을 쓸 필요가 없다는 것이 이쪽 논리다.

**정리하면** — 통합팩을 쓰는 중이면 (나), 최신 모델(MiniMax H3 등)을 따라가야 하면 (가).
(가) 를 택했다면 업데이트 전에 위 네 폴더를 백업하고, 새 노드가 안 보이면
`--disable-all-custom-nodes` 로 템플릿 워크플로를 두 번 돌려 본체만의 동작을 먼저 확인한다.

통합팩 버전 이력과 '업데이트하지 말 것' 원칙의 자세한 내용은 [설치와 환경 구성](install.md) 에 있다.

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [ComfyUI SAM3 / RIFE 자체 지원 노드 추가 26.04](https://arca.live/b/aiart/168617494) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965)</small>

## 노드를 다루는 최소 조작 — 바이패스 · 뮤트 · 그룹
<small>2026-06 기준 · 근거 5건</small>

워크플로우 하나에 기능이 여러 개 들어 있는 경우가 많고, **쓰지 않는 부분을 끄는 것**이 사실상 조작의 전부다.

| 조작 | 단축키·경로 | 효과 |
|---|---|---|
| 바이패스 | `Ctrl+B` | 노드를 통과시킴(보라색). 워크플로우 모드 전환에 주로 쓰임 |
| 뮤트 | `Ctrl+M` | 노드를 실행에서 제외 |
| 실행 건너뛰기 | 노드 우클릭 → 건너뛰기(보라색) | 중간 저장 노드 등을 끌 때 |
| 그룹 단위 온오프 | `Fast Groups Bypasser` (rgthree-comfy) | 그룹째로 껐다 켜기 |
| 마스크 그리기 | 이미지 노드 우클릭 → `open in maskeditor` | 인페인팅용. **칠한 뒤 작업을 취소하고 다시 실행해야 마스크가 적용된다** |
| 노드 복구 | 노드 우클릭 → `Fix node (recreate)` | 로더가 깨졌을 때 |

기능 조합의 실제 예 — WAN2.2 통합 워크플로우는 프레임 조건 네 개를 `Ctrl+B` 로 켜고 끄는 것만으로 모드가 바뀐다.

> 1=시작 이미지, 2=시작 비디오, 3=끝 이미지, 4=끝 비디오.
> 전부 끄면 T2V / 시작 이미지만 = FF2V / 끝 이미지만 = LF2V / 둘 다 = FLF2V /
> 시작 비디오만 = 뒷부분 연장 / 끝 비디오만 = 앞부분 연장.
> 이미지와 비디오가 동시에 켜지면 이미지는 무시된다.

**함정 두 가지.**

- **뮤트로는 안 꺼지는 노드가 있다.** Anima+ill 워크플로우에서 페이스 디테일러를 안 쓸 거면
  보라색 뮤트만 걸어서는 워크플로우가 돌지 않고 **노드를 아예 제거해야** 한다(한 글에서만 언급됨).
- **멈춘 것처럼 보이는 것이 정상 동작인 경우가 있다.** 인페인팅이 `노드:Pause 0%` 에서 멈춘 것처럼 보이면
  워크플로우 안에서 **파랗게 깜빡이는 `Continue` 버튼**을 누르면 진행된다. 하드웨어 병목이 아니다(작성자 정정).

<small>근거 — [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [comfyui) Anima 찍먹용 - anima+ill 워크… 26.02](https://arca.live/b/aiart/162677789)</small>

??? note "근거 5건 전부 보기"
    [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [comfyui) Anima 찍먹용 - anima+ill 워크… 26.02](https://arca.live/b/aiart/162677789) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430)

## 화면과 설정 손보기
<small>2026-08 기준 · 근거 6건</small>

생성 자체와는 무관하지만 계속 거슬리는 것들을 고치는 방법이 각각 한 글씩 올라와 있다.

| 하고 싶은 것 | 방법 | 근거 |
|---|---|---|
| KSampler 진행 상황을 눈으로 보기 | 설정 → Comfy → **라이브 미리보기 방식**을 `latent2rgb` | 통합팩 배포글 |
| 사이드바 `Template` 버튼 제거 | `ComfyUI/user/default/` 에 `user.css` 를 넣고 `button.templates-tab-button { display: none; }` → 재시작 후 브라우저 열기 | 한 글에서만 언급됨 |
| 프롬프트 칸 글씨 키우기 | `ComfyUI/web/user.css` 의 `comfy-multiline-input font-size: 16px` 수정 | 한 글에서만 언급됨 (2024-09 기준, 경로가 바뀌었을 수 있음) |
| 소수점을 6자리까지 보기 | 설정에서 `float` 검색 → `Disable default float widget rounding`, `Float widget rounding decimal places [0 = auto]` 조절 | 시그마 편집 글 |

**반대로 켜면 안 되는 설정이 하나 있다.**
`설정 → Comfy → Nodes 2.0 → 모던 노드 디자인` 을 켜면 **워크플로우 배열이 깨지고 일부 커스텀 노드가 작동하지 않는다.**
통합팩 배포글 세 편이 반복해서 경고한다.

user.css 커스터마이즈의 공식 문서는 `https://docs.comfy.org/interface/appearance#advanced-customization-with-user-css` 다.

**표에 더할 것 두 개** *(각각 한 글에서만 언급됨)*

| 하고 싶은 것 | 방법 |
|---|---|
| png 를 다른 프로그램 없이 **바로 jpg 로 저장** | 우클릭 메뉴에 `open as jpg` · `save as jpg` 를 추가하는 커스텀 노드가 있다. `custom_nodes` 에 압축을 풀면 끝이고 **파이썬 의존성이 없다.** Load image · image preview · save image 등 기본 이미지 노드에 모두 적용된다. ⚠ **blob URL 방식이라 VSCode 의 integrated browser 같은 일부 환경에서는 표시되지 않는다** |
| ComfyUI Manager 의 **Legacy UI 를 끈 채로** Git URL 설치·본체 업데이트·git pull 을 쓰고 싶다 | 검색창에 **`ControlPanel`** 로 검색해 설치한다(ComfyRegistry 등록됨). Snapshot 과 별개로 **python 의존성 없이 설치된 custom_node 만 백업·복원**하는 기능도 있다. 보통은 Legacy UI 를 그냥 쓰면 되므로 자주 필요한 노드는 아니다 |

> Legacy UI 자체를 되살리는 쪽은 실행 인자 `--enable-manager-legacy-ui` 다. 위 노드는 **반대로 Legacy UI 를 끈 상태**에서
> 그 기능만 되살려 화면을 깔끔하게 쓰려는 선택지다.

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750) · [미세팁) ComfyUI 사이드바에서 Template 버튼 제… 26.03](https://arca.live/b/aiart/164602009)</small>

??? note "근거 6건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750) · [미세팁) ComfyUI 사이드바에서 Template 버튼 제… 26.03](https://arca.live/b/aiart/164602009) · [Comfy의 기본 메뉴에 jpg를 추가하는 커스텀 노드. 26.05](https://arca.live/b/aiart/171262767) · [ComfyUI 매니저 Legacy UI 대체 커스텀 노드 26.08](https://arca.live/b/aiart/179523894)

## 본체에 들어온 기능과, 교체하면 빨라지는 노드
<small>2026-05 기준 · 근거 5건 · 자료 엇갈림</small>

커스텀 노드를 깔기 전에, **이미 본체에 들어와 있는지** 확인할 가치가 있다.

**ComfyUI 가 자체 지원하기 시작한 것 (최신 git 필요, Kijai 기여)**

- **SAM3** — 별도 SAM 커스텀 노드 없이 쓸 수 있다. 태그 뒤에 `face:10` 처럼 최대 숫자를 적으면 여러 명을 감지한다.
- **RIFE** (프레임 보간) — 모델은 `https://huggingface.co/Comfy-Org/frame_interpolation`

⚠️ **모델을 넣는 폴더에 대해 두 글이 다르게 적는다. 둘 다 적어 둔다.**

| 모델 | 글 A (2026-04-24, 자체 지원 소식) | 글 B (2026-05-23, 통합팩 배포) |
|---|---|---|
| SAM3.1 | `checkpoint` 폴더 → `Load Checkpoint` 로 로드 | `설치폴더\ComfyUI\models\sam3` |

한쪽이 최신 경로일 수도, 통합팩이 별도 경로를 쓰는 것일 수도 있다. 인식이 안 되면 반대쪽을 시도하라.

**RIFE(VFI) 모델 경로는 이견이 없다.** `ComfyUI/models/frame_interpolation` 이며,
`vfi`·`interpolation`·`rife` 폴더가 아니다(세 글이 일치). 파일은 `rife_v4.26_heavy.safetensors`,
배율은 2배 정도가 적당하다.

**바꾸면 이득이 큰 노드**

| 기존 | 대체 | 차이 |
|---|---|---|
| `ComfyUI-WD14-Tagger` | `ComfyUI-WD-Timm-Tagger` | 291장 태깅 **226.99초 → 9.34초**. 121프레임 영상은 92.96초 → 3.01초(batch_size 4). onnxruntime 대신 timm 사용, 같은 이미지를 두 번 분류하지 않음 (RTX 5090, eva02 모델 기준 / 한 글에서만 언급됨) |
| 기본 업스케일 | `SeedVR2` | 기본은 5090 기준 0.4초로 매우 빠르지만 평면적. SeedVR2 는 약 5초지만 DiT 라 피사체에 샤픈·배경에 블러를 넣는 식으로 동작. **이미지 업스케일에는 3b Q4/Q8 gguf 로 충분하고 7b fp16 은 불필요** |

**SUPIR 업스케일은 SDXL 전용**이다. FLUX·포니 결과물은 호환성이 나쁘므로 별도 SDXL 모델로 다시 돌려야 한다
(2024-09 기준, 한 글에서만 언급됨).

<small>근거 — [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [뉴비용) 나는 진짜 업스케일만 하고 싶어요 26.03](https://arca.live/b/aiart/163774464) · [ComfyUI SAM3 / RIFE 자체 지원 노드 추가 26.04](https://arca.live/b/aiart/168617494)</small>

??? note "근거 5건 전부 보기"
    [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [뉴비용) 나는 진짜 업스케일만 하고 싶어요 26.03](https://arca.live/b/aiart/163774464) · [ComfyUI SAM3 / RIFE 자체 지원 노드 추가 26.04](https://arca.live/b/aiart/168617494) · [ComfyUI-WD-Timm-Tagger 커스텀 노드 26.05](https://arca.live/b/aiart/169517277)

## 딸깍 올인원 워크플로우 계열 — '쉽고 빠른 ComfyUI'
<small>2026-04 기준 · 근거 3건</small>

노드를 최대한 안 만지고 싶다면 `efficiency-nodes-ED` 기반 **'쉽고 빠른 ComfyUI'** 계열이 채널의 대표적인 선택지다.
V6(2024-09, FLUX 대응) → V9(2026-04, ANIMA 추가)로 이어졌다.

**V6 (2024-09 기준)**

- 로더 `ckpt_name` 에서 `model_opt_input` 을 고르면 FLUX 모드: cfg 1, 클립스킵 제거, 유넷/클립 로더와 플럭스 가이던스 활성,
  이름에 `flux` 가 든 VAE 자동 선택, 로라·임베딩 스태커 바이패스
- 일반 체크포인트를 고르면 SDXL 모드: 유넷/클립 로더·플럭스 가이던스가 뮤트된다(`Ctrl+M` 으로 해제)
- **설치 순서가 있다.** `Efficiency Nodes for ComfyUI Version 2.0+` 를 **먼저**,
  `Efficiency Nodes ExtendeD` 를 **나중에** 설치
- 함께 설치되는 노드 11개: ComfyUI Impact Pack, pythongosssss/ComfyUI-Custom-Scripts, UltimateSDUpscale,
  rgthree's ComfyUI Nodes, Efficiency Nodes for ComfyUI Version 2.0+, ComfyUI-SUPIR, ComfyUI-Miaoshouai-Tagger,
  ComfyUI_BiRefNet_ll, Efficiency Nodes ExtendeD, ComfyUI ImageGallery ExtendeD, KJNodes for ComfyUI
- 알려진 오류: LoRA/Embedding Stacker 의 `Value not in list` 는 `View model info → Use as preview` 클릭 시
  자동 리프레시로 모델이 안 잡히는 버그다. **리프레시 후 다시 선택하면 정상**

**V9 (2026-04)**

- 메인/리저널/Flux 워크플로우를 EXIF 에 담아 제공. V7.7 대비 TIPO 노드(랜덤 프롬 생성),
  순차적 와일드카드 인코딩(`#DSC숫자` / `#ASC숫자`), 리파이너 스크립트 추가
- **워크플로우를 다시 불러올 때마다 FaceDetailer 의 `cycle` 값이 20 으로 되돌아가 노드가 강제로 패스되는 버그**가 있었다.
  ComfyUI 프론트엔드 자체 버그로 확인됐고 배포자가 0.9.5 로 수정 배포했다.
  임시 대처는 `cycle` 값을 별도 int 노드로 빼서 입력을 고정하는 것
- Qwen i2i 인페인트 오류는 배포자가 Qwen 모델을 전부 지웠다며 당분간 업데이트하지 않겠다고 답했다

---

**다른 계열 — '딸깍플로우'** *(V1.1, 2025-02 / 이후 V2 로 대체됨)*

- **대량 업스케일이 이미지 EXIF 의 모델명을 인식해 해당 모델로 처리**한다. 여러 모델로 뽑은 이미지가 섞여 있어도 된다
- 순차 프롬프트 값을 `**job1**` ~ `**job4**` 형태로 **프롬프트 아무 위치에나** 끼워 넣을 수 있다
- ⚠️ 이 시점의 순차 프롬프트는 **배치 방식이라 도중에 꺼지면 결과가 전부 날아간다**
- 샘플러·스케줄러는 EXIF 에 **한 문장으로 합쳐져** 들어가 자동 입력이 불가능하다
- `Show Any` 에 `__example__` 같은 와일드카드 문구가 그대로 보이는 것은 증상일 뿐 **EXIF 상으로는 정상 변환**된다

<small>근거 — [쉽고 빠른 ComfyUI V9(ANIMA추가). 26.04](https://arca.live/b/aiart/166559591) · [쉽고 빠른 ComfyUI V6 (FLUX 대응) 24.09](https://arca.live/b/aiart/116551406) · [ComfyUI 딸깍플로우 V1.1로 업데이트 했음 25.02](https://arca.live/b/aiart/127946352)</small>

## 영역 분할 프롬프트 — 세 세대가 겹쳐 있다
<small>2026-02 기준 · 근거 7건</small>

화면을 나눠 캐릭터마다 다른 프롬프트를 주는 기능이다. **채널에는 세 세대가 겹쳐 남아 있어** 옛 글을 그대로 따라 하면 막힌다.

**1세대 — Attention Couple** *(2023-09)*

픽셀 좌표 대신 **인페인트처럼 마스크를 칠해** 영역을 나눈다. 워크플로우를 한 번 실행하면 영역 지정용 노드에 이미지가 뜨고,
`#1`·`#2` Mask 노드를 우클릭 → `Open in MaskEditor` 로 칠한다.
Base 영역은 `전체 − (#1 + #2)` 로 자동 지정된다 — 프롬프트가 적힌 영역에 마스크가 없으면 에러가 나기 때문이다.

| 모드 | 성격 |
|---|---|
| **Attention** | 하나의 Unet 안에서 한 번에 처리해 **빠르지만 영역 간 간섭이 많다.** 로라 없이 랜덤짤 뽑을 때 |
| **Latent** | Latent 영역을 직접 나눠 각각 샘플링해 **느리지만 간섭이 덜하다.** 로라를 쓸 때 |

간섭이 남기 때문에 각 영역에 `1girl` 대신 **`2girls` 를 쓴다**(`1girl` 을 쓰면 전체 그림에 영향).
`512x512` / `512x768` / `768x512` 처럼 **일반적인 비율**을 쓸 것 — 작성자가 다른 크기에서 에러를 많이 겪었다.

> ⚠️ **이후 Attention Couple 노드가 사라져 "누락되었다" 오류가 여럿 보고됐다.**
> 다른 노드로 대체한 워크플로우가 `https://arca.live/b/aiart/118857835` 에 올라와 있다.

**2세대 — Impact Pack 의 Latent 완전 분리** *(2023-09)*

영역에 프롬프트뿐 아니라 **모델까지** 할당해 간섭을 완전히 없앤다.
핵심 노드는 `KSamplerAdvancedProvider` → `RegionalPrompt` → `CombineRegionalPrompts` → `RegionalSampler`
(영역이 2개뿐이면 `TwoSamplerForMask`).

⚠️ **시간 계산을 틀리기 쉽다.** `RegionalSampler` 는 기본 영역과 각 영역을 **1스텝씩 번갈아** 디노이징한다.

```text
20스텝 설정 + 영역 3개  →  실제로는 총 60스텝이 진행된다
```

영역이 완전 독립이라 **AI 가 알아서 배치해 주지 않는다.** 컨트롤넷 openpose 를 반드시 함께 써서 캐릭터를 영역 안에 잡아 둬야 한다.
품질 프롬프트는 `Text Concatenate` 의 `text_a` 에 한 번만 써서 각 영역 텍스트와 합치면 반복해 적지 않아도 된다.

> 작성자가 댓글에서 직접 인정했다 — *"꽤 오래전 글이라 ComfyUI 와 확장 노드가 업데이트되면서 본문 워크플로우는 작동하지 않을 수 있다."*

**3세대 — 지금** *(2026)*

- ANIMA 리저널에서는 A8R8 판보다 **`ComfyUI-ppm` 의 Attention Couple** 이 프롬프트 길이·복잡성과 무관하게 타율이 좋다
- ILXL 리저널은 **베이스 프롬프트에 `2girls`, 각 area 에는 `1girl`** 을 넣는다 (area 에 `2girls` 를 적으면 네 명이 나온다)
- 강제 영역 분리 `attention_bootstrap` 모드는 `euler_ancestral` 에서 그림이 망가지고, `bootstrap_steps` 는 **2 까지 낮춰야** 자연스럽다

즉 **1·2세대의 "각 영역에 2girls" 규칙이 3세대에서 뒤집혔다.** 연도를 보고 따라갈 것.
프롬프트 작성 자체는 [프롬프트 쓰는 법](prompting.md) 을 보라.

### 3세대 실전 — 마스킹은 'Preview Bridge 가 한 번 받아야' 열린다 (2026-02)

노드 업데이트로 옛 Attention Couple 워크플로우들이 돌지 않게 되면서 나온 **2인 리저널 수정본**의 절차다.
**여기서 막히는 사람이 많은데, 요령 하나만 알면 된다.**

| | |
|---|---|
| 1 | `Ref Image` 에 컨트롤넷을 쓸 거면 관련 이미지를, **안 쓸 거면 공백 이미지**를 넣는다 (아무 이미지나 되지만 **만들 이미지와 같은 해상도**가 편하다) |
| 2 | **한 번 실행한다.** 넣은 공백 이미지가 나타난다 |
| 3 | **그때 실행을 취소한다** |
| 4 | `Preview Bridge` 를 **우클릭 → `Open in MaskEditor`** 로 원하는 부분을 칠한다 |

**핵심은 `Preview Bridge` 노드가 이미지를 한 번 받아야 MaskEditor 를 열 수 있다는 것이다.**
같은 성질이 인페인팅에도 있다 — 칠한 뒤 작업을 취소하고 다시 실행해야 마스크가 적용된다.

### 영역마다 로라를 따로 걸기

| 환경 | 방법 |
|---|---|
| ED 노드 | **로라 스태커**를 쓸 수 있다 |
| **바닐라 ComfyUI** | 기본 노드의 **`후크 LoRA 생성`** 을 각 리저널 프롬프트에 연결한다 |
| 슬라이더류 로라 | **`후크 LoRa 생성 (모델 전용)`** 에서 모델 강도로 조절 |

적용 후 사용법은 평소와 같아서 트리거 단어를 **해당 영역 프롬프트**에 넣으면 된다.
예시에서는 왼쪽 인물에 가슴 크기 로라, 오른쪽에 태닝 로라를 강도 2.0 으로 걸어 좌우가 바뀌는 것까지 확인했다.
로라를 여러 개 쓰면 노드가 계속 길어지는 것은 감수해야 한다.

> ⚠ **리저널에 로라를 달면 VRAM 을 극단적으로 많이 먹고 시간도 오래 걸린다**(버그인지는 불명).

**영역별 부정 프롬프트**가 꼭 필요하면 `조건 쌍 (속성 설정)` 노드를 쓴다 — 영역마다 긍정·부정을 모두 가질 수 있지만
`CLIP 텍스트 인코딩` 노드가 커서 워크플로우가 길쭉해진다. 원문 작성자는 **글로벌 부정 프롬프트 하나만** 가져간다.

### ⚠ 영역별 디테일러 — 마스크 배율을 안 맞추면 조용히 실패한다

한쪽 인물의 얼굴만 디테일러를 걸고 싶을 때다. SAM3 로 전체에서 `face` 를 감지한 뒤 **리저널 마스크와 AND 로 걸러낸다.**

```text
'마스크 합성' 노드  연산 = and
   대상 ← 리저널 마스크 (배율을 맞춘 것)
   원본 ← SAM3 감지 마스크
→ 한쪽 인물의 얼굴만 남는다 → SEGS 로 변환 → 디테일러(SEGS)
```

**여기서 틀리기 쉬운 지점** — 디테일러는 highresfix **뒤에** 오고 highresfix 가 해상도를 바꾸므로,
**원래 씌운 리저널 마스크도 같은 배율로 확대해야 AND 가 성립한다.**
마스크를 직접 확대하는 노드가 없다면 이렇게 우회한다.

```text
마스크를 이미지로 변환 → 이미지 확대 비율 (highresfix 와 같은 배율) → 이미지를 마스크로 변환
예) 832x1216 → 1248x1824    ('마스크 미리보기' 로 확인)
```

디테일러의 **긍정 조건에는 해당 영역의 리저널 프롬프트를 연결**한다.

### 후처리 순서와 연결

```text
highresfix(x1.5)  →  디테일러  →  업스케일(x2.0)
832x1216          →  1248x1824  →  2496x3648
```

⚠ **이미지 입력은 순차적으로 이어져야 진행 상황이 날아가지 않는다** — `highresfix 출력 → 디테일러1 → 디테일러2` 로
**직렬 연결**한다(디테일러끼리의 순서는 바뀌어도 무방). 워크플로우가 스파게티가 되는 것은 나중에 **서브그래프와 그룹화**로 정리하면 된다.

→ [디테일러](detailer.md) · [업스케일과 화질](upscale.md)

<small>근거 — [(ComfyUI) Latent 영역 지정으로 프롬프트를 완전… 23.09](https://arca.live/b/aiart/86519619) · [(ConfyUI) Attention Couple (Regio… 23.09](https://arca.live/b/aiart/86441475) · [ilxl 자작 리저널+오픈포즈 노드 26.05](https://arca.live/b/aiart/171224457) · [챈산 리저널 노드를 활용한 ilxl용 워크플로우. 26.05](https://arca.live/b/aiart/171276717)</small>

??? note "근거 7건 전부 보기"
    [(ComfyUI) Latent 영역 지정으로 프롬프트를 완전… 23.09](https://arca.live/b/aiart/86519619) · [(ConfyUI) Attention Couple (Regio… 23.09](https://arca.live/b/aiart/86441475) · [ilxl 자작 리저널+오픈포즈 노드 26.05](https://arca.live/b/aiart/171224457) · [챈산 리저널 노드를 활용한 ilxl용 워크플로우. 26.05](https://arca.live/b/aiart/171276717) · [로컬 comfyui 찍먹해보기 - 리저널 프롬프트 응용 26.02](https://arca.live/b/aiart/161706938) · [(ComfyUI) Attention Couple 리저널 2인… 26.02](https://arca.live/b/aiart/163287880) · [(anima) Attention Couple 리저널 워크플로… 26.04](https://arca.live/b/aiart/169319019)

## 시그마(노이즈 스케줄) 직접 편집 — 되긴 하지만 품질이 극적으로 좋아지진 않는다
<small>2026-03 기준 · 근거 4건</small>

샘플러 뒤편의 노이즈 스케줄(시그마)을 **그래프로 직접 그려** 조절하는 방법이 여러 편에 걸쳐 정리돼 있다.
기존 `ModelSampling` 노드는 1~8 구간에서만 활발히 변하고 `linear_quadratic` 같은 스케줄러에서는 값이 아예 안 변하기 때문이다.

> **입문자는 건너뛰어도 된다.** 아래는 "샘플러를 다 만져 봤는데도 아쉬울 때" 여는 서랍이다.

**필요한 노드**

- `https://github.com/JoeNavark/comfyui_custom_sigma_editor` (Custom Graph Sigma)
- `https://github.com/Extraltodeus/sigmas_tools_and_the_golden_scheduler` (Join Sigma Values)
- `https://github.com/crom8505/ComfyUI-Dynamic-Sigmas` (Dynamic Sigma Scheduler, 매니저 검색 가능)

**구성 (WAN 계열 SVI 예제)**

| 항목 | 값 |
|---|---|
| 그래프 1 | `start_y` 1 → `end_y` **0.99** (0-2 구간, 강한 노이즈로 2스텝) |
| 그래프 2 | 0.99 → 0 (2-4 구간, 완만히 감소) |
| `start_y` 기준 | wan 계열은 1 고정, SDXL 은 15 (최대 20) |
| `steps` | **-1 만큼 들어간다.** 2스텝을 원하면 3 을 입력 |
| 샘플러 | High/Low 용 `SamplerCustom`, 첫 샘플러 `add_noise` 활성 / 두 번째 비활성, cfg 1.0 고정 |
| 네거티브 | 트리플 샘플러·NAG 미사용 시 `ConditioningZeroOut` 으로 제거 |

⚠️ **그래프 1 의 시작값을 1 로 두면 안 된다.** High 에서 Low 로 넘길 때 인식하지 못해 **검은 화면**이 나온다.
반드시 0.99 를 쓴다.

**그래프 편집 조작** — 왼클릭으로 점 추가, 드래그로 이동, `Shift+클릭` 으로 삭제.
점이 안 놓이면 `Ctrl` 을 누른 채 캔버스를 드래그한다.

**`ComfyUI-Dynamic-Sigmas` 의 파라미터** *(2026-03)*

| 파라미터 | 뜻 | 함정 |
|---|---|---|
| `sigma_start` | 노이즈의 양 | **노드 기본값이 1.0(대부분의 모델 값)이라 SDXL 을 쓴다면 반드시 15 로 고쳐야 한다.** `BasicScheduler` 로 모델 기본값을 확인할 수 있다 |
| `sigma_end` | 끝나는 지점 | 여러 노드를 Concat 으로 이을 때 쓰고 **최종 결과물은 반드시 0 으로 끝나야 한다** |
| `curve_factor` | 양수는 위로, 음수는 아래로 꺾음 | |
| `curve_smooth` | 끄면 딱딱한 직선으로 꺾임 | |
| `show_steps` | 모든 스텝 표시(정교한 수치 기입) | 각 스텝은 소수점 15자리 이상 지원 |

실전 예 (WAI-illustrious-SDXL v16.0 + LUXsumildo style 로라):
`시드 1234 / cfg 1 고정 / 1024x1024 / SamplerEulerAncestralCFG++ 의 s_noise 를 1 → 1.05~1.1`.
총 35스텝을 `0~2 / 2~5 / 5~35` 세 구간으로 Concat 했다 — 시그마 15 에서 2스텝 머물다가 2~5 구간에서 15→2 로 급락시키고
(초반 몰빵), 5~35 에서 2→0 으로 천천히 내린다.

**어디에 쓰면 이득인가** *(작성자 댓글)* — 단순히 노이즈 양을 컨트롤하는 것이라 고속 로라는 물론
**과적합 로라 보정에 특히 효과적**이다. 반대로 **과소적합 로라는 학습 데이터 자체가 부족한 것**이라 보정 정도의 효과만 기대할 수 있다.
커스텀 시그마를 쓰는 중이면 자체 디테일러 노드보다 **SAM3 등으로 대상을 추출해 샘플러를 하나 더 돌리라**고 권한다.

**LTX-2.3 쪽 응용** — 8스텝 기준 시그마를 High/Low **5:3** 으로 나누고 y값은 0.95~0.99 에서 조절한다.
소리가 울리고 기계음이면 High 를 올리고 Low 를 내리며, 먹먹하면 반대로 한다. 비디오 품질이 낮으면 y값과 곡률을 만진다.

**결론은 유보적이다.** 작성자 스스로 `euler+simple` 대비 `euler+custom` 이 **훨씬 역동적**이긴 했으나
결과물 품질이 극적으로 좋아지는 건 아니고 **문제 진단·범용성·편의성** 쪽 장점이 크다고 정리했다.
다른 글에서는 정해진 시그마를 그대로 쓰라는 주장과, 수동 시그마와 `linear_quadratic` 이 2스텝에서
0.001 차이뿐이라는 반박이 오갔다. 수동 시그마 대신 `linear_quadratic` 또는 `Beta75(a: 0.7, b: 0.5)` 가
시그마 값이 가장 비슷하다는 대안도 제시됐다.

<small>근거 — [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750) · [(ComfyUI) 커스텀 시그마 마무리 (SDXL), 커스텀… 26.03](https://arca.live/b/aiart/166267341) · [(ComfyUI) LTX-2.3 커스텀 시그마로 영상과 음질… 26.03](https://arca.live/b/aiart/165196910) · [(워크플로) LTX2.3 Distilled Simple + … 26.03](https://arca.live/b/aiart/164232718)</small>

## 실험용 자작 노드 — 이름을 봤을 때를 위해
<small>2026-05 기준 · 근거 2건 · **근거 약함**</small>

채널에는 **작성자 스스로 "실험용" 이라 못박은** 자작 노드도 올라온다.
쓰라고 권하는 것이 아니라, 워크플로우에서 이름을 봤을 때 정체를 알 수 있도록 적어 둔다.

**LatentSpectralExpand** — `https://github.com/n0va39/ComfyUI-LatentSpectralExpand` *(2026-05)*

ANIMA SPEED 노드의 잠재이미지 업스케일 방식을 논문 기반으로 부분 재현한 것이다.
Highres 시 잠재이미지 크기를 키워 1차 생성에서는 디테일을 만들지 않고 2차 샘플러로 넘겨 효율을 높이는 발상이며,
구현은 **시그마 곡선을 중간에 잘라 2차 샘플러로 넘기는** 방식이다.
노드 출력으로 나오는 float 시그마 값으로 스케쥴러를 다시 부를 수도 있다.

> 작성자가 스스로 **논문 방식이 더 잘 되는지 확신이 없다**고 적었다 —
> 손 찐빠·디테일이 살아나는 것 같다가도 뭉개지는 느낌이라며 **초보보다 실험하고 싶은 사람용**이라고 못박는다.

**임베딩 커스텀 노드 묶음** *(2026-03, ComfyUI P30 까지 호환)*

임베딩(텍스트 몇 토큰을 한 단어로 압축해 둔 파일)을 **직접 만들고 검사하고 변환하는** 도구 모음이다.
구글 번역 호출 + 텍스트 임베딩 생성 노드, 말풍선 위에 글자를 얹는 텍스트 박스 노드,
`pt`/`bin` → `safetensors` 변환 노드, 각종 텐서 체커로 구성된다.

| 항목 | 값 |
|---|---|
| ⚠️ 저장 위치 | 전부 **`MODEL/proj_embedding` 폴더**(설치 시 자동 생성)로 가므로 **변환 직후 임베딩 폴더로 옮겨야 한다** |
| 네거티브 임베딩 | **'부정 조건 감소 강도'** 를 적용하는 게 좋다. 값이 낮으면 **부정 키워드가 일러스트를 덮어 버린다.** 한도를 20 → 50 으로 올렸다 |
| 한글 폰트 | 텍스트 박스 노드 첫 실행 시 생기는 `fonts` 폴더에 **한글 호환 폰트**를 넣어야 한다 (윈도우 기본 arial 은 한글이 깨진다) |
| 포터블 추가 설치 | 에러가 날 때만 `python -m pip install --no-deps torchvision` / `... deep-translator beautifulsoup4` |
| 샘플러 시드 | **0 일 때만 랜덤**, 값을 넣으면 고정 |

노드마다 한글로 주의사항이 적혀 있다. 임베딩 자체가 무엇인지는 [용어집](glossary.md) 을 보라.

<small>근거 — [임베딩 노드 버전업(P30까지 호환) 26.03](https://arca.live/b/aiart/163973039) · [LatentSpectralExpand 노드 (아니마 Spee… 26.05](https://arca.live/b/aiart/171519242)</small>

## PC 밖에서 돌리기 — 휴대폰 브라우저와 클라우드 GPU
<small>2026-05 기준 · 근거 2건</small>

둘 다 **한 글에서만 언급된** 방법이다. 검증된 표준이 아니라 선택지로만 봐라.

**휴대폰 브라우저에서 — ComfyBridge**

PC 에서 ComfyUI 를 띄워두고 같은 Wi-Fi/LAN 의 휴대폰으로 t2i·i2v 를 돌리는 로컬 웹앱이다.

- 설치: `git clone https://github.com/ddol2ya/ComfyBridge.git` → `install_node_and_deps.bat` → `start_bridge.bat`
- ComfyUI 폴더 또는 `ComfyUI\main.py` 경로 지정 (예: `F:\ComfyUI_windows_portable\ComfyUI`)
- 접속: PC `http://127.0.0.1:8189/` , 모바일 `http://<PC의 IPv4>:8189/`
- **외부 접속은 포트포워딩을 권하지 않고 Tailscale 을 권장**한다
- 출력은 `bridge_output` 폴더. Monitor 탭에서 ComfyUI 를 실행한 뒤 **브라우저를 새로고침해야** 모델·LoRA 목록이 로드된다
- SEGS Detection 은 얼굴 마스크 파이프라인이라 이미지에 얼굴이 없으면 체크를 해제해야 오류가 안 난다
- i2v 는 RTX 4090 / 96GB RAM 에서 테스트됐다

**클라우드 GPU 로 — comfyui-modal**

On-demand GPU 플랫폼 Modal 을 커스텀 노드로 연결한다.

- `https://github.com/JunnnnyWon/comfyui-modal` 을 `custom_nodes` 에 넣기만 하면 동작
- 사이드바에 Modal 토큰을 붙여넣으면 키가 자동 분리 입력됨 → `Connect & Deploy`.
  `Modal On` 버튼이 켜져야 Modal GPU 를 쓰고, 꺼지면 로컬로 돌아간다
- 모델·로라·VAE 등 **모든 모델 파일을 Modal 볼륨에 올려야** 하고 로컬에는 `modal-이름` 형태의 더미 파일이 생긴다
- 콜드 스타트 약 20~30초, 큐 완료 2초 뒤 컨테이너 자동 종료
- 카드 등록 시 30달러 무료 크레딧. 작성자는 A10-24GB 로 Wan2.2 를 약 100시간 돌릴 수 있다고 했으나,
  **댓글에 1시간 30분에 1달러 넘게 썼다는 반례**가 있다(작성자는 논스탑 구동 기준이며 콜드스타트·스토리지 비용은 별도라고 답)
- 제약: 현재 `comfyui-manager` 하나만 지원하며 다른 커스텀 노드는 매번 이미지 재빌드가 필요해 제외된다

<small>근거 — [A10 GPU 쌀먹하는 방법 26.04](https://arca.live/b/aiart/169220758) · [모바일 Comfy 구동 프론트 Web App 26.05](https://arca.live/b/aiart/170363616)</small>

## 앱 모드 — 노드가 무서우면 화면을 접어 버려도 된다
<small>2026-05 기준 · 근거 2건</small>

노드 그래프가 무서우면 **접어 버리면 된다.** ComfyUI 에는 복잡한 워크플로우를 프롬프트·시드·해상도 같은
입력칸 몇 개짜리 화면으로 바꿔 주는 **앱 모드(App Builder)** 가 공식 기능으로 들어 있다. **따로 설치할 것은 없다.**
반응형이라 폰·태블릿에서도 쓸 만하고, 그래프를 보면 현기증 나는 사람은 PC 에서도 쓸 수 있다 (앱↔그래프 전환은 자유다).

### 만드는 법

| | |
|---|---|
| 1 | 워크플로우를 열고 **좌측 상단 그래프 > 앱 빌더** 로 들어간다 |
| 2 | 앱에서 조작할 요소를 골라 담는다 (원문 작성자는 **긍정 프롬프트·부정 프롬프트·시드·해상도** 넷만 골랐다) |
| 3 | 다음 → 결과창에 띄울 **출력 노드**를 고른다 (보통 이미지 저장 노드) |
| 4 | **다른 이름으로 저장** → 이름을 넣고 **'기본적으로 앱으로 열기'** 체크 |
| 5 | 앱 보기를 누르면 고른 요소와 오른쪽 아래 **실행 버튼**만 있는 화면이 뜬다 |

여러 번 실행하면 하단바 오른쪽에 결과 기록, 왼쪽에 대기 큐가 보인다.
만든 앱은 **좌측 사이드바의 앱 모드 아이콘**에서 다시 열고, 모바일도 같은 경로로 열어 '편집 및 실행'을 누른다.

> **앱 빌더가 아예 안 뜬다면** ComfyUI 가 아주 오래된 버전이라는 뜻이다. 본체를 올려야 한다.

### ⚠ 함정 — 앱 빌더에 들어가면 Nodes 2.0 이 강제로 켜진다

**이걸 모르면 앱을 한 번 만들어 보고 나서 "워크플로우가 깨졌다"고 착각하게 된다.**

> 앱 빌더에 들어가는 **순간** UI 가 **Nodes 2.0 으로 강제 전환된다.**
> 커스텀 노드를 많이 깐 사람은 여기서 충돌이 나 **워크플로우 파라미터가 전부 깨져 보일 수 있다.**
> 앱 빌더를 쓰고 나면 **좌측 상단 ComfyUI 아이콘에서 Nodes 2.0 을 반드시 다시 꺼라** — 그러면 워크플로우가 정상으로 돌아온다.

이것은 위 '화면과 설정 손보기' 에서 "켜면 안 되는 설정" 으로 적어 둔 그 `모던 노드 디자인` 과 같은 것이다.
차이는 **사용자가 켠 적이 없는데 켜진다**는 점이다.

### ⚠ 폰에서 쓰려면 서버를 열어야 하고, 그건 안전하지 않다

모바일에서 쓰려면 내부망이든 외부망이든 서버를 개방해야 한다 (`https://arca.live/b/aiart/162190790`).

> **ComfyUI 는 불특정 다수에게 서빙하라고 만든 프로그램이 아니라 보안이 사실상 없다.** 외부 개방은 특히 주의할 것.

같은 이유로 **API-KEY 를 워크플로에 그대로 저장하면 안 된다** — 워크플로우는 EXIF 로 통째로 공유되기 때문에
키가 그대로 새어 나간다. `.env` 로 관리하는 노드를 쓴다
(`https://github.com/tankenyuen-ola/comfyui-env-variable-reader` / `https://github.com/bedovyy/ComfyUI-LLM-Helper`).

→ [설치와 환경 구성](install.md) 의 '휴대폰·다른 방에서 쓰기'

<small>근거 — [ComfyUI 추천 VLM 노드, 프롬프트, 모델 (장문) 26.01](https://arca.live/b/aiart/160879401) · [comfyui 앱모드 사용법 26.05](https://arca.live/b/aiart/171528258)</small>

## 생성 중 화면 — 프리뷰가 나빠졌거나 안 보일 때
<small>2026-05 기준 · 근거 2건</small>

"돌고는 있는 것 같은데 화면에 아무것도 안 보인다" 는 입문자 질문이 많다. **대개 고장이 아니라 설정이거나 버전 문제다.**

| 하고 싶은 것 | 어떻게 |
|---|---|
| KSampler 진행 상황을 눈으로 보기 | 설정 → Comfy → **라이브 미리보기 방식**을 `latent2rgb` |
| 프리뷰가 여기저기 흩어져 못 보겠다 | **ComfyUI-PreviewMonitor** (`https://github.com/bedovyy/ComfyUI-PreviewMonitor`) — 프리뷰만 한곳에 몰아 보여 주고 실행 중인 노드도 표시한다 |
| 프리뷰 화질이 갑자기 나빠졌다 | ↓ 아래 |
| 생성이 끝나도 이미지가 안 뜬다 | ↓ 아래 |

### ⚠ 프리뷰가 갑자기 나빠졌다면 당신 탓이 아니다 (2026-02)

> `comfyui-frontend-package` 가 특정 버전을 넘어가면서(**1.10.17 까지는 정상**) **프리뷰 성능이 반토막 나고 관련 옵션도 사라졌다.**

**해결** — `ComfyUI-bleh` (`https://github.com/blepping/ComfyUI-bleh`) 를 설치하고 **그 폴더에서 파일 이름을 바꾼 뒤 재시작**한다.

```
blehconfig.example.json  →  blehconfig.json
blehconfig.example.yaml  →  blehconfig.yaml
```

그러면 프리뷰 해상도를 조절할 수 있다. 당연히 해상도가 높을수록 성능은 조금 떨어진다.

### 같이 사라진 기능 — '생성 후 이미지 새로고침'

원래는 생성이 끝나면 이미지가 새로고침되며 결과물을 보여 줬는데 그 기능도 없어졌다.

| 대안 | 되는 것 / 안 되는 것 |
|---|---|
| **ComfyUI-Easy-Use 의 `EasyKSampler`** (`https://github.com/yolain/ComfyUI-Easy-Use`) | KSampler 계열 커스텀 노드를 다 실험한 끝에 **유일하게 정상 동작**했다 |
| was-node-suite-comfyui 의 `KSampler Cycle` (`https://github.com/ltdrdata/was-node-suite-comfyui`) | 한 노드에서 **업스케일까지 프리뷰를 전부** 보여 주는 것은 이것뿐이지만, 새로고침을 안 해 줘 **중간 결과물을 못 보고 `image compare` 노드도 못 쓴다** |

> PreviewMonitor 는 `ComfyUI/temp` 폴더를 감시하는 것이 아니라 **웹소켓으로 넘어오는 프리뷰를 그대로 표시**하는
> 프론트엔드 전용 노드라 별도 의존성이 없다. 다만 **ComfyUI 0.21.1 리눅스에서 KSampler 프리뷰는 되는데
> PreviewMonitor 에는 안 보인다는 미해결 보고**가 있다.

각각 **한 글에서만 언급된** 도구다.

→ [오류 해결](troubleshooting.md)

<small>근거 — [(커스텀노드) ComfyUI-PreviewMonitor: 프… 26.05](https://arca.live/b/aiart/171041315) · [KSampler 프리뷰 해상도 수정해주는 커스텀 노드 Com… 26.02](https://arca.live/b/aiart/161467109)</small>

## 프롬프트를 편하게 다루는 노드들 — 뼈대를 안 건드리고 붙이는 것부터
<small>2026-08 기준 · 근거 7건</small>

노드를 무서워하지 않게 되는 가장 빠른 길은 **"프롬프트를 편하게 만들어 주는 노드" 부터 붙여 보는 것**이다.
그림이 나오는 뼈대(위 '노드 여섯 개면 그림이 나온다')를 건드리지 않고 **프롬프트 칸 앞에만 끼우면 되기 때문에** 망가뜨릴 위험이 적다.

| 하고 싶은 것 | 노드 | 한 줄 |
|---|---|---|
| **WebUI 처럼 `<로라:1>` 로 로라 부르기** | ComfyUI-TIL | 로라 로더를 안 만져도 된다 ↓ |
| 태그가 나오면 다른 태그도 자동으로 붙이기 | Conditional Prompt Append | 와일드카드용 ↓ |
| 이미지에서 프롬프트를 꺼내 재사용 | 프롬프트 매니저 | ↓ |
| 자연어 스타일을 골라 덧씌우기 | ComfyUI-ZImagePowerNodes | ↓ |
| 이미지를 보고 프롬프트를 AI 가 써 주기 | VLM 노드 | ↓ |
| 값 계산·조건 분기·순차 실행 | ComfyUI-basic_data_handling | ↓ |

### `<로라이름:가중치>` — ComfyUI-TIL

ComfyUI 는 원래 로라를 로더 노드로 **모델 선에 연결**해야 하는데, WebUI 처럼 프롬프트 안에 적고 싶을 때 쓴다.
`https://github.com/namemechan/ComfyUI-TIL-Text-Inline-LoRA-`

```
<이름:가중치>                 기본. 프롬프트 어디에 넣어도 되고, 여러 개면 앞에서부터 로드
<이름:가중치:클립가중치>       클립까지 통과시키는 로라에서 모델/클립 가중치를 따로
<lora:이름:가중치>            lora: 접두사는 붙여도 되고 없어도 된다
```

'이름' 은 **로라 파일명**이다. **텍스트 출력에서는 `<...>` 가 자동으로 제거된다** — `1girl, solo <로라A:1>` 을 넣으면
로라A 가 적용되고 문자열은 `1girl, solo` 만 나가므로 **메타데이터나 다음 노드로 넘겨도 깨끗하다.**

| `mode` | 언제 |
|---|---|
| `auto` | clip 사용 여부 자동 감지. **대부분 이걸로 둔다** |
| `clip` | XL 계열처럼 clip 까지 학습한 로라 |
| `no-clip` | **ANIMA 같은 DiT 모델** |

노드는 `TIL - Base`(올인원) 와 Sender/Receiver 유선·무선이 있는데, **무선은 노드에서 작동 흐름을 제어하지 않아
복잡한 워크플로우에서 동작을 보장하지 않는다. 유선을 권한다.** 이 노드는 conditioning 을 출력하지 않으며(텍스트 인코딩 노드가 아니다)
노드 매니저에 등록 신청을 하지 않았다.

### 조건부로 태그 덧붙이기 — Conditional Prompt Append

와일드카드로 랜덤 프롬프트를 돌릴 때 **"이 태그가 나오면 이 보조 태그도 같이 넣어라"** 를 자동화한다.

```
cd ComfyUI/custom_nodes
git clone https://github.com/COkedat/comfyui-prompt-append
```

재시작하고 `utils/prompt` 카테고리에서 찾는다. `base_prompt` 안에서 `search_prompt` 태그를 `search_logic`(AND/OR)로 검사해
`condition`(`Always` / `If Detected` / `If Not Detected`)에 맞으면 `append_prompt` 를 `position`(front/back)에 붙인다.
`skip_duplicate` 로 중복 추가를 막고, 가중치를 1.2 로 주면 추가분이 `(wow nice boba, damn:1.2)` 로 감싸져 붙는다.
출력은 `prompt` 와 **`is_detected`(BOOLEAN)** 인데, 이걸 스위치 노드에 연결하면 **"이 태그가 나왔을 때만 특정 경로를 타게"** 같은 분기도 만들 수 있다.

### 이미지에서 프롬프트를 꺼내 두기 — 프롬프트 매니저

이미지를 드래그앤드롭해 두면 그 이미지의 프롬프트를 **항목별로 나눠 저장**하고 '현재 워크플로우에 적용' 으로 되돌려 넣는다.

| 판 | 특징 |
|---|---|
| 1판 (2026-05) | **EXIF 워크플로우의 '노드 이름' 을 기준으로** 프롬프트를 구분한다 → **노드 이름이 바뀌면 동작하지 않는다** |
| 2판 (2026-05-31) | 프롬프트를 **6칸**까지 분리, 퀄리티·네거티브 퀄리티 태그 접기, 검색, **`// ` 주석**(그 줄 제외 / `/* */` 블록 주석은 **미지원**) |

⚠ **2판은 노드를 새로 만들었기 때문에 1판과 호환되지 않는다.**
두 판 모두 **퀄리티 태그와 네거티브 퀄리티 태그는 저장 대상에서 일부러 제외한다** — 한 번 정하면 잘 안 바꾸는 값이라
같이 저장하면 목록이 지저분해지기 때문이다.

### 자연어 스타일 프리셋 — ComfyUI-ZImagePowerNodes

`https://github.com/martin-rizzo/ComfyUI-ZImagePowerNodes`
제작자는 Z-Image 용이라고 하지만 **프롬프터 부분은 SDXL 기반 모델만 빼면 어디에 갖다 써도 쓸 만하다**는 것이 소개자의 평가다.
상단에서 카테고리와 세부 스타일을 고르면 아래처럼 **역할 지정 문장을 앞에 자동으로 덧씌운다.**

```
YOUR CONTEXT: You are an illustrator of dark and disturbing themes.
Your illustration includes stippling textures, dramatic raking side lighting...
YOUR DRAWING: [내 프롬프트]
```

Z-Image 같은 최신 모델은 **단부루 태그가 아니라 자연어 문장**을 받기 때문에 쓰는 방식이다.
댓글이 세대 변화를 정확히 짚었다 — *"태그가 좋았는데 이제 자연어를 태그처럼 저장해 두고 써야 한다."*

### 이미지를 보고 AI 가 프롬프트를 쓰게 하기 — VLM 노드

| 누구에게 | 노드 | 성질 |
|---|---|---|
| **초보자** | `https://github.com/bedovyy/ComfyUI-LLM-VLM-Node` | 노드 하나로 끝나고 **쓸 때만 VRAM 에 올렸다 닫아** VRAM 걱정이 없다. 같은 시드·같은 입력이면 같은 결과. 대신 체크포인트를 바꿀 때마다 `clip_name` 에 **mmproj** 를 맞춰 올려야 하고 gemma·qwen2-vl·qwen3-vl 만 지원 |
| LLM 을 다뤄 본 사람 | `https://github.com/hekmon/comfyui-openai-api` | openai-api 를 지원하는 모든 LLM/VLM 에서 동작. **다른 PC 에서 LLM 을 돌리면 VRAM 에 올려 둔 채** 쓸 수 있다. 단점은 서버를 따로 세팅해야 하는 것 |

```
# gguf 를 넣는 곳
ComfyUI/models/LLavacheckpoints/

# i-quant 는 동작하지 않는 노드가 있다 → Q4_K_M 정도를 쓴다
# ollama 로 받은 모델은 파일명을 해시로 바꿔 저장하므로 그대로 가져다 쓰기 어렵다
```

**두 개의 함정이 실제로 보고됐다.**

| 증상 | 원인·해결 |
|---|---|
| `Failed to load mtmd context from: ...Qwen3-VL-8B-NSFW-Caption-V4.Q4_K_M.gguf` | **mmproj 파일을 안 받은 것.** mmproj 를 함께 받으면 해결된다 |
| llama-cpp-python 이 안 깔린다 | 원작자가 **5개월째 업데이트를 안 했다.** `https://github.com/JamePeng/llama-cpp-python` 릴리즈에서 whl 링크를 복사해 `pip install <whl URL>` 로 깐다 → 포터블에서의 설치 순서는 [오류 해결](troubleshooting.md) |

ComfyUI 가 이미지 생성으로 잡아 둔 VRAM 은 **직접 빼 줘야 하므로** 프롬프트 쪽과 이미지 쪽에
**KJNodes 의 `VRAM Debug`** 노드를 붙이는 것이 권장된다.

> **모델마다 권장 프롬프트 길이가 다르다** — FLUX.2 Klein 은 **4~6문장의 짧은** 프롬프트, Z-Image 는 긴 프롬프트도 잘 받고,
> 영상 쪽은 **Wan2.2 가 짧게 · LTX 가 길게**다.

### 값 계산과 분기 — ComfyUI-basic_data_handling

`https://github.com/StableLlama/ComfyUI-basic_data_handling`
비슷한 기능이 ComfyUI 기본 노드·KJNodes·Impact Pack 에도 있으므로 **반드시 이걸 깔 필요는 없다**고 제작자가 밝힌다.
다만 여기서 나온 **개념 하나는 알아 둘 값이 있다.**

| | 무엇 | WebUI 로 치면 |
|---|---|---|
| **BATCH** | `Empty Latent` 의 `batch_size` 처럼 **한 번에 처리** | batch size |
| **DATA LIST** | 개수만큼 **순차 실행** | **batch count** |

`range` 노드로 39~43 을 지정해 `steps` 에 넣으면 **39·40·41·42 네 장**이 생성되고, 프롬프트 등 다른 값은 마지막 것을 쓴다.
LoRA 가중치를 0.0~1.0 사이 0.2 간격으로 6개 뽑아 비교표를 만들 때는 **이미지를 붙이는 KJNode 가 batch 를 받으므로
중간에 `Image List to Image Batch` 노드를 넣어야 한다.** float 계산에서 0.6 이 `0.60000...1` 로 나오는 것은 `round` 노드로 반올림한다.

⚠ **알려진 버그** — `create DICT` 노드는 **이미지에서 워크플로를 불러오면 key 값이 사라진다.** **서브그래프로 감싸면** 지워지지 않는다.

> 참고로 **대부분의 확산 모델은 64 배수 해상도를 요구한다.** 원본 비율에 맞춰 1024x1024 에 가장 가까운 64 배수를 계산해 넣으면 안전하다.

→ [프롬프트 쓰는 법](prompting.md) · [로라 쓰는 법](lora-usage.md)

<small>근거 — [프롬프트 매니저 26.05](https://arca.live/b/aiart/172333335) · [프롬프팅을 편하게 해주는 ComfyUI-ZImagePower… 26.01](https://arca.live/b/aiart/160992548) · [조건부 프롬프트 추가 커스텀 노드 만듦 26.03](https://arca.live/b/aiart/165692820) · [ComfyUI 추천 VLM 노드, 프롬프트, 모델 (장문) 26.01](https://arca.live/b/aiart/160879401)</small>

??? note "근거 7건 전부 보기"
    [프롬프트 매니저 26.05](https://arca.live/b/aiart/172333335) · [프롬프팅을 편하게 해주는 ComfyUI-ZImagePower… 26.01](https://arca.live/b/aiart/160992548) · [조건부 프롬프트 추가 커스텀 노드 만듦 26.03](https://arca.live/b/aiart/165692820) · [ComfyUI 추천 VLM 노드, 프롬프트, 모델 (장문) 26.01](https://arca.live/b/aiart/160879401) · [ComfyUI-basic_data_handling 커스텀노드… 26.02](https://arca.live/b/aiart/162937578) · [comfyui 프롬에서<로라:1>로 불러오는 노드 TIL 26.08](https://arca.live/b/aiart/179076765) · [로라매니저식 프롬프트 매니저-fix 26.05](https://arca.live/b/aiart/171714325)

## ⚠ 와일드카드를 순서대로 돌리기 — 되는 것과, 본문이 틀린 것
<small>2026-06 기준 · 근거 2건 · 자료 엇갈림</small>

와일드카드는 기본이 **랜덤**이라 "목록을 처음부터 끝까지 한 번씩" 돌리고 싶을 때 답이 없다.
채널에서 Impact Pack 의 **'와일드카드 처리기(Impact)'** 노드를 직접 고쳐 순차 모드를 붙인 **비공식 패치**가 두 번 배포됐다.

| 모드 | 동작 |
|---|---|
| `sequential` | 와일드카드 파일의 항목을 **첫 줄부터 차례대로** 뽑고, 중단했다 다시 실행하면 **이어서** 다음 항목을 낸다 |
| `sequential_reset` | 재시작하면 처음으로 돌아간다 |

2026-06-28 판은 여기에 **다음·이전·리셋 버튼**과 **주석 문법**을 더했다.

> 와일드카드 파일 안에서 **`==` 사이에 적은 항목은 주석 처리되어 출력되지 않는다.**
> (와일드카드 **파일**을 사용하는 경우에만 적용된다.)

### 적용법 — 파일 네 개를 덮어쓴다

```
impact_pack.py  wildcards.py  impact_server.py
  → ComfyUI\custom_nodes\comfyui-impact-pack\modules\impact

impact-pack.js
  → ComfyUI\custom_nodes\comfyui-impact-pack\js
```

⚠ **원본 파일은 반드시 백업할 것.** 배포자 본인이 *"전부 Claude 가 만든 것이라 어떤 오류가 날지 모른다"* 고 못박았다.
Impact Pack 은 **최신으로 업데이트해 둬야 한다**(댓글).

### ❌ 본문이 틀린 부분 — '배치 수만큼 순차 출력' 은 되지 않는다

**이것이 이 글에서 가장 중요한 대목이다.**

**본문 주장** — 작성자는 순환(끝까지 가면 처음으로) 기능을 추가했다며 *"테스트는 안 해봤는데 아마 잘 될 거임"* 이라고 적었다.

> ❌ **이 설명은 틀렸다. 그 기능은 원리상 불가능하다.**
>
> 요청된 동작은 '배치 7로 뽑으면 1~7번 항목, 다시 배치 5로 뽑으면 1~5번' 이었는데
> **실제로는 1번 항목만 배치 수만큼 반복 생성됐다.**
> 작성자도 나중에 **"배치 1로 큐를 다섯 번 누른 것인지 배치 5로 한 번 누른 것인지 노드가 구분할 방법이 없어 불가능하다"** 고 인정했다.

**결국 이 패치의 실제 기능은 순차 출력과 리셋까지다.** 배치 수만큼 다른 항목을 뽑고 싶다면
**큐를 그 횟수만큼 누르는 것**밖에 방법이 없다.

### ⚠ 배포 링크는 대개 죽어 있다

채널에서 이런 파일을 배포할 때의 관행이 정해져 있다.

| | |
|---|---|
| 링크 | 본문에 **base64 로 가려** 올린다 (예: `aHR0cHM6Ly9raW8uYWMvYy9iTUJfMUhMSmtLTU1MWnduM1hkejhi` → `https://kio.ac/c/bMB_1HLJkKMMLZwn3Xdz8b`) |
| 압축 비밀번호 | **`ai`** |
| 보관 기한 | **한 달** |

즉 **글이 올라온 지 한 달이 지났으면 링크는 죽었다고 봐야 한다.** 2026-06·2026-06-28 판 모두 지금은 만료됐을 가능성이 높다.

→ [프롬프트 쓰는 법](prompting.md) · [자원](resources.md)

<small>근거 — [컴피 와일드카드 노드 순차모드 추가. 업데이트 26.06](https://arca.live/b/aiart/174214832) · [컴피 와일드카드 노드 업데이트 26.06](https://arca.live/b/aiart/175224738)</small>

## 뽑은 그림에 프롬프트를 남기는 법 — 추적하지 말고 심어라
<small>2026-05 기준 · 근거 10건 · 자료 엇갈림</small>

**뽑고 나서 "이 그림 어떻게 뽑았더라" 를 되찾지 못하는 것이 입문자가 가장 크게 후회하는 지점이다.**
채널의 결론은 명확하다 — **나중에 추적하려 하지 말고, 처음부터 심어서 저장하라.**

### 근본 해법 — ComfyUI-Image-Saver

```
https://github.com/alexopus/ComfyUI-Image-Saver
```

프롬프트·모델·설정을 **Civitai 규격 메타데이터로 이미지에 직접 심어** 저장한다.
**EXIF 뷰어를 만든 제작자 본인이 두 번에 걸쳐 같은 결론을 냈다.**

> *"애초에 ComfyUI-Image-Saver 를 써서 저장하면 프롬프트 추적기 같은 '예측기' 가 필요 없다."* (2026-06)
> *"복잡하게 추적하지 말고 그냥 image saver 를 쓰자."* (2026-07)

프롬프트만 텍스트로 남기고 싶다면 **KJNodes 의 `SaveImageKJ`** 를 쓰면 **이미지와 같은 이름의 `.txt`** 로 저장된다.
채널의 워크플로우 배포글들도 **KSampler 와 이미지 출력 노드를 바로 옆에 붙이고, EXIF 가 자동 저장되는 출력 노드로 바꿔 두는** 구성을 쓴다.

### 이미 저장해 버린 파일을 열어볼 때 — ComfyUI-EXIF-viewer

```
https://github.com/n0va39/ComfyUI-EXIF-viewer
# v0.1.3 (2026-07, 프롬프트 추적 개선)
https://github.com/n0va39/ComfyUI-EXIF-viewer/releases/tag/v0.1.3
```

**exe 로 실행하면 끝이라 설치가 필요 없다.**

| 기능 | 한계 |
|---|---|
| **프롬프트 추적기** — 워크플로우에서 **가장 처음 들어가는 샘플러**를 기준으로 프롬프트를 역추적 | 기본 노드와 context 류 커스텀 노드 구조에 대응하지만 **모든 워크플로우에서 되지는 않는다** |
| **리소스 뷰어** — Civitai 규격 메타데이터가 있으면 해당 모델·로라의 Civitai 페이지로 자동 연결 | 그 메타데이터를 **Image-Saver 가 넣어 줘야** 동작한다 |

즉 이 뷰어는 **이미 있는 파일을 가볍게 열어볼 때 쓰는 도구**이고, 근본은 여전히 Image-Saver 다.

> 이미지의 EXIF 프롬프트를 읽는 다른 뷰어들도 **NovelAI 형식은 잘 읽지만 ComfyUI 의 복잡한 워크플로우나
> 자연어 범벅은 못 읽는 경우가 있다.** 워크플로우를 한 번 열어 프롬프트가 같은지 확인하고 쓰는 편이 좋다.

### 아카라이브에 올릴 때

워크플로우가 담긴 png 는 **EXIF 를 유지한 채 올려야** 상대가 드래그앤드롭으로 열 수 있다.
**업로드 전에 `exif 데이터 보존` 을 체크**하지 않으면 메타데이터가 날아간다 — 실제로 워크플로우가 안 열려
다시 올려 해결한 사례가 있다. 자세한 것은 위 '워크플로우 불러오기' 를 보라.

### ⚠ 자작 메모 노드보다 `image saver` 가 낫다 — 작성자가 수긍한 정정

ComfyUI **밖에서** 프롬프트를 받아오면(외부 LLM·번역기 등) 워크플로우에 프롬프트가 남지 않는다.
그래서 저장할 때 임의 문자열을 EXIF 에 함께 심는 자작 노드(`SaveImageEX`)가 만들어졌는데,
**댓글에서 "`image saver` 노드가 이미 AI 짤 메타데이터 양식에 맞춰 저장하고 webp·jpeg 도 지원하며
Civitai 등에서 자주 쓰여 호환성이 좋다" 는 지적이 나왔고 작성자도 이를 인정했다.**

> 작성자가 결론 삼아 남긴 교훈: **"복잡한 건 결국 나중에 후환이 온다.
> 규격이 확실한 NAI·WebUI 쪽이 낫고, 워크플로우도 가능하면 기본 노드나 단순한 것만 쓰게 됐다."**

`image saver` 로 저장하면 메타데이터가 **WebUI 형식**으로 남아 **Civitai 업로드 시 사용한 로라가 자동 인식**된다.

### ⚠ ComfyUI 로 뽑은 이미지의 EXIF 는 직전 프롬프트에 오염된다

**ComfyUI 로 뽑으면 EXIF 안에 '직전에 생성한 이미지의 프롬프트' 가 먼저 남는다.**
와일드카드 A B C D E 로 돌렸다면 EXIF 순서가 `AAB BBC CCD DDE` 처럼 되어, 프롬프트로 분류하면 결과가 어긋난다.

> **대처: 검색 키워드에 `A`, 제외 키워드에 `B|C|D|E` 를 넣어 A 로 생성한 것만 걸러낸다.**

같은 이유로 **ComfyUI 이미지는 워크플로우마다 내부 정보 형식이 달라** 프롬프트만 뽑아내기가 어렵다.
뷰어들이 쓰는 우회는 **자주 쓰는 문자열이 든 가장 긴 덩어리를 프롬프트로 간주**하는 것이다 —
프롬프트는 `newest` · `year 2024` · `masterpiece` 같은 퀄리티 프롬,
네거티브는 `worst` · `low quality` 또는 낮은 score 태그를 기준으로 찾는다.
**webp 는 인코딩 형식 자체가 제각각이라 WebUI 산이 아니면 키 분류가 안 되는 경우가 많다.**

### Image-Saver 를 쓸 때 실제로 걸리는 것들

| | |
|---|---|
| 자동으로 들어가는 것 | **체크포인트 · 시드 · 프롬프트** (워크플로우에서 끌어온다) |
| **손으로 넣어야 하는 것** | **샘플러 · 스케줄러** |
| ⚠ 함정 | 이 노드는 **워크플로우를 분석해 주지 않는다.** '넣어 준 값' 을 그대로 기록할 뿐이라 **연결을 잘못하면 실제 생성에 쓰인 값과 다른 값이 저장된다** |
| 출력 분기 | input 은 하나만 연결되지만 output 은 여러 개로 갈 수 있다. **하이레즈 유무를 스위치로 번갈아 뽑아 하나로 저장하려면** 저장부를 복사해 Image Saver 를 두 개 만들거나 switch 로 하나를 고르게 한다 |
| 미해결 | 어떤 윈도우 환경에서는 **역슬래시가 중복 출력되는 버그**가 있어 못 쓰고 기본 노드를 쓰는 사람이 있다 |

**함께 보이는 Get/Set 노드는 기능이 아니라 UI 편의용이다.** Set 에서 지정한 값을 Get 이 받아 오는 것뿐이고 **직접 연결한 것과 동작이 같다**(선이 길어지는 것을 막으려고 쓴다).
⚠ **Set 하나를 Get 여럿이 받을 수는 있지만 Set 둘을 Get 하나로 받을 수는 없고**(두 번째 Set 에 자동으로 `_0` 이 붙는다), **Get 노드가 스스로 정보를 찾아내지도 못한다.**

### 왜 역추적이 그렇게 어려운가 — 실제로 뜯어본 기록

이론상 경로는 `KSampler` → 그 `positive`/`negative` 입력 노드 → 보통 `CLIPTextEncode` 의 `text` 다. 실제로는 두 군데서 막힌다.

| 막히는 곳 | |
|---|---|
| **KSampler 가 아닌 샘플러**를 쓰면 | 시작부터 추적이 안 된다 |
| `text` 자리에 **문자열 조립 커스텀 노드**가 있으면 | 예: `"class_type": "Merge Strings v2 [RvTools]"` — **그 노드의 동작을 해석해 실행까지 해 봐야** 최종 문자열을 알 수 있다 |

**우회** — 최종 텍스트를 `"class_type": "PreviewAny"` 로 한 번 흘려 두면 **`preview_markdown` 항목에 완성된 문자열이 남아** 그 노드 번호로 복원할 수 있다.
⚠ 단 **PreviewAny 의 출력이 워크플로우에서 다른 노드로 연결돼 있지 않으면 EXIF 에 아예 남지 않는다.**
댓글은 **`PreviewAny` 보다 `Show Text` 노드**를 권한다. LLM 으로 프롬프트를 만드는 워크플로우에서는 이것을 빠뜨리면 프롬프트가 통째로 사라진다.

→ [자원](resources.md) · [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [comfy EXIF 뷰어 + 리소스 뷰어 + 자동 프롬프트 … 26.06](https://arca.live/b/aiart/173672742) · [exif잇음)늒네식 워크플로우 공유 26.07](https://arca.live/b/aiart/175642035) · [태그뷰어+분류기+컴피이미지메모추가노드 종합 업뎃 26.05](https://arca.live/b/aiart/169783666) · [ComfyUI에서 EXIF에 NAI처럼 프롬프트 남기는 방법 26.05](https://arca.live/b/aiart/169763428)</small>

??? note "근거 10건 전부 보기"
    [comfy EXIF 뷰어 + 리소스 뷰어 + 자동 프롬프트 … 26.06](https://arca.live/b/aiart/173672742) · [exif잇음)늒네식 워크플로우 공유 26.07](https://arca.live/b/aiart/175642035) · [태그뷰어+분류기+컴피이미지메모추가노드 종합 업뎃 26.05](https://arca.live/b/aiart/169783666) · [ComfyUI에서 EXIF에 NAI처럼 프롬프트 남기는 방법 26.05](https://arca.live/b/aiart/169763428) · [ComfyUI 추천 VLM 노드, 프롬프트, 모델 (장문) 26.01](https://arca.live/b/aiart/160879401) · [또 업뎃한 프롬프트 분류기 25.11](https://arca.live/b/aiart/154827249) · [comfy-EXIF 뷰어 v0.1.3: 프롬프트 추적기능 향상 26.07](https://arca.live/b/aiart/176893071) · [ComfyUI exif에서 프롬프트 정보 찾아 뜯어보다 알게… 26.05](https://arca.live/b/aiart/169744100) · [nai+로컬 태그뷰어 업뎃 26.05](https://arca.live/b/aiart/170775337) · [뉴비의 간단한 워크 플로우 26.02](https://arca.live/b/aiart/161471075)

## 가속·노이즈 노드 — 이름을 봤을 때를 위해
<small>2026-07 기준 · 근거 2건</small>

샘플러 자체를 갈아 끼워 **속도를 올리는** 노드와, 초기 노이즈를 만져 **그림맛을 바꾸는** 노드가 각각 있다.
**입문자는 굳이 안 붙여도 된다.** 다만 남의 워크플로우에서 이름을 보면 정체를 알아야 하고, 값 하나만 만지면 되는 것들이 있다.

### Spectrum-KSampler — `refresh_ratio` 하나로 속도-퀄리티

```
https://github.com/sorryhyun/ComfyUI-Spectrum-KSampler
```

이미지 생성 속도를 높이면서 네거티브·퀄리티 태그에 더 잘 순응하게 만드는 커스텀 KSampler 다.
**v2.6.0 의 SEA(Spectrum Evolution Aware) filter 가 이 노드를 쓰기 쉽게 만든 지점이다.**

> 예전에는 속도를 조절하려면 `window size` · `flex window` · `lambda` · `w` · `m` · `warmup` 을 일일이 미세 튜닝해야 했는데,
> **SEA filter 는 `refresh_ratio` 하나로 속도-퀄리티 균형을 잡는다.**

| `refresh_ratio` | 실제 스텝(실측) | |
|---|---|---|
| `0.0` | — | SEA 가 자동으로 스펙트럼을 보정. **기존 스펙트럼과 같은 속도** |
| `0.20` | **14** | 0 에 가까울수록 빠르지만 퀄리티가 떨어진다 |
| `0.35` | **16** | |
| `0.5` | **20** | |
| `0.7` | **24** | |
| `1.0` | 전부 | 모든 스텝에서 모든 블록을 연산 |

⚠ **처음 한 장은 SEA 가 안 걸린다.**
SEA filter 는 해당 **(해상도, 스텝, 스케줄러, refresh_ratio) 조합의 이미지를 한 번 미리 생성한 뒤에** 적용된다.
**해상도나 스텝을 바꾸면 첫 생성 한 번은 일반 스펙트럼으로 돌아가고 그다음부터 걸린다.** 고장이 아니다.
기존에 달려 있던 `mod guidance` 와 `smc_cfg` 는 그대로 함께 쓸 수 있다.

> **RTX 20 시리즈(튜링)는 이 노드를 쓸 수 없다** — 제작자 공인 **bf16 필수**다 → [설치와 환경 구성](install.md)

### FrequencyCorrectedNoise — 효과는 미미하다

```
https://github.com/oron1208/ComfyUI-FrequencyCorrectedNoise
```

초기 노이즈에 푸리에 변환을 적용해 저주파 성분을 조금 깎아 편향을 제어하는 노드다.

| | |
|---|---|
| ⚠ 쓰는 법이 다르다 | **출력이 '노이즈' 라서 일반 KSampler 계열에는 못 쓴다.** `고급 사용자 정의 샘플러(SamplerCustomAdvanced)` 와 함께 써야 한다 |
| ⚠ Spectrum 과 시드를 공유할 때 | 정수 노드로 양쪽에 연결하되, **speed 쪽은 음수 시드에서 에러가 나므로 수학식 노드로 절대값을 취해** 연결한다 |
| 모드 | `off` / `dc` / `fft` |

**효과에 대한 평가는 유보적이다.** 소개자 본인도 dc 의 변화가 가장 컸지만 **그게 긍정적인지는 애매하고 오히려 찐빠가 난 것도 있었다**고 적었고,
**댓글도 변화가 거의 없다는 반응이 다수**였다. (fft 에서 수치를 올리니 디테일이 더 사는 것 같다는 후기는 있었다.)
**한 글에서만 언급된** 도구이며, 소개자도 본인이 만든 것이 아니라 X 에서 발견해 옮긴 것이다.

→ [VRAM·속도 최적화](vram.md) · [설치와 환경 구성](install.md)

<small>근거 — [comfyui anima 고속 + mod guidance 노… 26.06](https://arca.live/b/aiart/174577922) · [ComfyUI-FrequencyCorrectedNoise 노드 26.07](https://arca.live/b/aiart/178611005)</small>

## 끼우기만 하면 되는 노드들 — Skimmed CFG · NAG · 말풍선 OCR
<small>2026-08 기준 · 근거 5건</small>

워크플로우 뼈대를 건드리지 않고 **모델 선 사이에 끼우기만 하면 되는** 노드들이다. 이름을 봤을 때를 위해 적어 둔다.

### Skimmed CFG — 높은 CFG 를 견디게 한다

```
https://github.com/Extraltodeus/Skimmed_CFG
```

연결은 `모델 → Skimmed_CFG → KSampler` 가 전부다.
프롬프트와 네거티브에서 **상충되는 부분을 제거**해, 높은 CFG 에서 나타나는 과채도·경직(속칭 '타는 현상')을 줄인다.
높은 CFG 를 견딜수록 원하는 이미지 구현도가 올라간다는 것이 쓰는 이유다.

| 값 | 근거 |
|---|---|
| **3** | 제작자가 밝힌 정상 작동 상정값 |
| 7 | 깃허브 샘플 이미지 (샘플러 CFG 6/8/12/16/24/32 와 조합) |
| 1.5~2 | 소개글 작성자가 실제로 쓰는 값 |

> ⚠️ **부작용 — CFG 나 스텝이 너무 낮으면 손가락이 융합된다.**
> 깃허브 side effects 에 `sometimes fused fingers with too low skimming CFG scale and too low amount of steps` 라고 적혀 있다.
> 이 노드는 **CFG 를 높게 쓰는 것을 상정하고** 만들어졌다. CFG 리스케일 노드(보통 0.5~0.7)와는 작동 방식이 다르다.

사용기(댓글): ANIMA 를 CFG 5 로 돌리던 사람이 **CFG 7 로 올리고 이 노드를 쓰니 색감이 훨씬 자연스러워졌다.**
ANIMA 에서 이 노드를 다른 보정 노드와 겹쳐 쓰면 안 되는 문제는 → [ANIMA](anima.md)

### Krea 2 Turbo 에서 네거티브 쓰기 (NAG)

```
https://github.com/iljung1106/ComfyUI-Krea2-NAG   # ComfyUI Manager 로도 설치 가능
```

**Krea 2 Turbo 는 CFG 1 이 권장인데, CFG 1 에서는 네거티브가 아예 작동하지 않는다.**
CFG 를 억지로 올리면 모델이 학습한 것과 다른 환경에서 돌고 속도도 느려진다.
이 노드는 NAG(Normalized Attention Guidance)로 **CFG 를 건드리지 않고** 네거티브를 먹인다.

| | |
|---|---|
| 속도 저하 | 프롬프트를 바꿨을 때 약 **30%**, 고정 상태에서 약 **10%** |
| CFG 를 올리는 방식 대비 | 약 **80% 빠름** |
| ⚠ 최소 버전 | **ComfyUI 0.29.0**. 그보다 낮으면 지원하지 않는다 |

### 말풍선 글자 갈아 끼우기 (OCR)

```bash
cd custom_nodes
git clone https://github.com/Toraong/ComfyUI-OCR-Bubble
cd ComfyUI-OCR-Bubble
pip install requirements.txt
```

의존성은 `easyocr>=1.7`, `opencv-python>=4.8.0`, `Pillow>=9.0.0` 셋뿐이다.
**생성 모델을 돌리지 않고 OCR + 이미지 편집만 하므로 VRAM 1GB, 처리 0.2~0.5초**면 끝난다.
`bg_padding` 은 말풍선을 덮는 흰 영역 크기(픽셀 단위, 미리보기의 초록 네모),
`height_fill_ratio`·`width_fill_ratio` 는 그 영역 대비 글자 크기 비율이다(1 = 영역 크기, 2 = 2배).

### 프롬프트 프리셋 노드 (2025-01 기준)

프리셋 노드를 찾아 헤맨 기록의 결론은 **`https://github.com/noembryo/ComfyUI-noEmbryo`** 였다.
*(pythongosss 프리셋 노드와 Impact Pack 의 builder 는 "둘 다 나사가 하나씩 빠져 있어 계륵" 이라는 평.)*
preset 폴더의 txt 를 메모장으로 고친 뒤 **노드를 선택하고 `R`** 을 누르면 리로드된다.

### 자작 노드를 만들려는 사람에게

노드는 **파이썬 파일(본체) + 자바스크립트 파일(외형)** 로 이루어지고, 파이썬 10줄 정도면 노드 하나는 만들어진다.
공식 문서는 `https://docs.comfy.org/custom-nodes/custom_node_walkthrough` 다.
**ComfyUI 자체가 `https://github.com/jagenjo/litegraph.js` 를 가져다 만든 것이라,
LLM 이 헛소리를 하면 litegraph 쪽 자료를 함께 주면 정답이 나올 때가 있다.**

### 근거가 약하다고 스스로 밝힌 것 (DCW 노드의 RDC)

작성자 본인이 **'해골물'**(플라시보일 수 있는 근거 약한 기법)이라 부르는 실험 기능이다.
권장값은 `tau 0.15`(0 이면 끔, 0.25 초과 비권장), `alpha_ll 0.05`(0.1 초과 비권장), `alpha_hh 0 고정`.
효과는 "좀 더 부드럽고 디테일해지거나 대비가 풀리는 느낌인데 확실하지 않다" 고 한다.
**비교 이미지에 다른 설정이 전부 들어가 있어 동일한 경험을 보장하지 않는다고 작성자가 못 박았다.**

<small>근거 — [Krea 2 Turbo/Edit용 네거티브 프롬프트 노드를 … 26.08](https://arca.live/b/aiart/179598126) · [말풍선 노드 2.0버전 26.07](https://arca.live/b/aiart/176155066) · [DCW노드 새로운해골물 RDC추가 26.07](https://arca.live/b/aiart/178277612) · [comfyui Skimmed_CFG 노드 (스압) 26.05](https://arca.live/b/aiart/171375569)</small>

??? note "근거 5건 전부 보기"
    [Krea 2 Turbo/Edit용 네거티브 프롬프트 노드를 … 26.08](https://arca.live/b/aiart/179598126) · [말풍선 노드 2.0버전 26.07](https://arca.live/b/aiart/176155066) · [DCW노드 새로운해골물 RDC추가 26.07](https://arca.live/b/aiart/178277612) · [comfyui Skimmed_CFG 노드 (스압) 26.05](https://arca.live/b/aiart/171375569) · [comfyui 쓸만한 프리셋 노드 25.01](https://arca.live/b/aiart/126197785)

## i2i 로 화풍 바꾸기 — 작가 태그를 빼야 한다
<small>2026-08 기준 · 근거 1건</small>

i2i 로 **그림체만 바꾸는** 작업(픽셀 아트화 등)에서 사람들이 가장 많이 놓치는 것이 하나 있다.

> **T2I 때 쓰던 작가 태그를 그대로 두고 돌리면 결과가 이상해진다. 작가 태그를 전부 빼야 그나마 잘 나온다.**
> 화풍을 바꾸는 작업에서는 **원래의 화풍 태그가 방해**가 된다.

조절할 것은 프롬프트와 KSampler 의 **denoise** 뿐이고, 적정값은 이미지마다 다르다.

| 대상 | denoise | 비고 |
|---|---|---|
| 인물 그림 | **0.4 전후** | |
| 풍경 | 0.4 는 과함 — 더 낮춘다 | 너무 낮추면 원본 해상도를 무시하고 제멋대로 그린다 |
| LLM(Gemini 등)이 만든 이미지 | **0.25** | 1408x768 을 1344x768 로 크롭해 넣은 실사용값 |

**원본 해상도가 어느 정도 높아야 잘 나오기 때문에**, 해상도가 들쭉날쭉한 실사 이미지보다 AI 로 생성한 그림을 넣는 편이 낫다.

→ [인페인팅](inpainting.md) · [업스케일과 화질](upscale.md)

<small>근거 — [WAI17(일러스트리어스) I2I 픽셀 아트화 워크플로우 공유 26.08](https://arca.live/b/aiart/179639075)</small>

## ⚠ `denoise 0.5` 로 i2i 를 도는 것은 거의 금기다 — 본문이 틀렸고 글쓴이가 수긍했다
<small>2026-05 기준 · 근거 2건 · 자료 엇갈림</small>

'Anima+IL 이 아니라 IL+Anima' 라며 순서를 뒤집은 워크플로우 검증글인데, **본문 평가를 댓글이 뒤집었고 글쓴이가 받아들였다** (1건, 2026-05).

### 본문의 주장

구조는 단순하다 — **IL 로 t2i 생성 → Anima 로 i2i 다듬기 → 업스케일.**
테스트 모델은 하사쿠 XL(IL)과 하사쿠 아니마이고 두 프롬프트 노드에 같은 프롬프트를 넣었다.
이 방식이 나온 이유는 **Anima 쪽 로라가 부족**해서, IL 전용 캐릭터·스타일 로라를 그대로 쓰면서 Anima 의 렌더링 품질을 얻으려는 것이다.

> 본문 결론 — Anima 쪽 **Denoise 0.5** 에서도 IL 전용 로라의 특징이 의외로 잘 유지됐다.

### ⚠ 댓글의 반박 — 이쪽이 맞다

| | |
|---|---|
| **(1)** | Anima 를 쓰는 이유는 **초반 구도·형태를 잘 잡기 때문**인데 이 워크플로우는 **그 능력을 봉인한다** |
| **(2)** | 두 번째 결과가 좋아 보이는 건 단순히 **i2i 로 전체 디테일링을 한 번 더 돌렸기 때문**이며 **ILXL 로 똑같이 해도 비슷하거나 더 낫다** |
| **(3)** | **실제로 좌우 캐릭터의 인상이 완전히 달라졌다** — 장난기 많은 캐릭이 수줍은 캐릭이 됐다. **`denoise 0.5` 로 i2i 를 도는 것은 거의 금기다** |

**글쓴이도 '제작자 세팅 그대로 썼다' 며 수긍했다.**

### 그래서 어떻게 쓰나

**원본을 지키려면 `denoise` 를 `0.2` 정도로 낮춘다.** 0.2 에서는 원본이 거의 그대로 유지된다.
이 워크플로우는 'Anima 로라 부족' 이라는 **과도기 상황의 우회책**이고, 품질 향상처럼 보이는 부분의 상당 부분은 **i2i 디테일링 자체의 효과**라는 것을 알고 써야 한다.

> ⚠️ **이 문서 안에서 값이 어긋나는 지점이 있다.** 다른 항목은 'Anima 로 뽑은 짤을 i2i 한 번 더 돌리면 좋아지며 **디노이즈 0.5 정도가 권장**' 이라고 적는다.
> **같은 0.5 를 두고 평가가 갈린다** — 캐릭터 인상 유지가 중요하면 0.2, 디테일 보강이 목적이면 0.5 로 나눠 생각하는 것이 지금으로선 최선이다.
> 다른 댓글은 VAE 차이를 근거로 **반대 방향(Anima→IL)이 오히려 세부 디테일(악세사리·눈알)을 뭉갠다**며 이쪽이 낫다고 본다.

→ [ANIMA](anima.md) · [인페인팅](inpainting.md)

### 덧 — "i2i 를 한 번 더 돌리면 좋아진다" 자체가 반쯤 착각이다

같은 지적이 훨씬 앞선 글의 댓글에도 있었다 (112476411, 2024-07).

> **i2i 를 한 번 더 돌린다고 이론적으로 퀄리티가 올라가는 것은 아니고, 뭉개졌던 부분이 어쩌다 풀리는 것에 가깝다.
> 실제로 배꼽이 하나 더 생기는 역찐빠가 나는 것이 그 증거다. 디테일이 목적이라면 Detailer(SEGS) 를 쓰는 편이 맞다.**

**작성자의 반박도 함께 적어 둔다** — 체감 7할 타율로 목걸이·귀걸이·꽃 같은 디테일이 살아난다는 것이다.
정리하면 **i2i 재실행은 '디테일 추가' 가 아니라 '재추첨'** 이고, 확실한 디테일이 목적이면 디테일러가 맞다.
그래서 그 글의 실전 운용은 이렇다 — 반복 생성에는 denoise **0.4**, 배꼽이 두 개가 되는 찐빠가 나면 Hires 단계 이미지를 꺼내 독립 i2i 워크플로에서 **0.3** 으로 다시 돌린다.

덧붙여, 그 글에서 나온 노드 하나 — **ComfyUI 에서 Detail Daemon 처럼 노이즈 스케줄(Sigmas)을 다루려면 `KSampler` 가 아니라 `SamplerCustom`** 을 써야 한다(KSampler 를 더 잘게 분해한 노드이며, 더 내려가면 `SamplerCustomAdvanced` 가 있다).
그리고 **ComfyUI 기본 저장 방식으로는 나중에 결과물을 찾기 힘들어지므로** `https://github.com/thedyze/save-image-extended-comfyui` 로 폴더를 나눠 저장하기를 권한다.

<small>근거 — [(ComfyUI 대회) 뉴비의 ComfyUI 후기 (약후방) 24.07](https://arca.live/b/aiart/112476411) · [Anima+IL 아님. IL+Anima임. 26.05](https://arca.live/b/aiart/171656386)</small>

## 배포 워크플로우에서 반복되는 두 함정 — v-pred 스위치와 `.pt` 보안 경고
<small>2025-08 기준 · 근거 2건</small>

채널에 도는 '빡통 워크플로우' 계열 배포글 둘이 같은 지점을 짚는다 (2025-06 · 2025-08).

### (1) v-pred 스위치 — 모델과 안 맞으면 반드시 끈다

바이패스 스위치로 기능을 켜고 끄는 워크플로우에서 **v-pred 모델이 아니면 v-pred 스위치를 반드시 꺼야 한다.**
**Eps 모델에 v-pred 를 켜 두면 정상 동작하지 않는다.**

> 증상으로는 **그림이 흐리멍텅하게** 나온다. 그럴 때 **V-PRED 모델이 맞는지부터 확인하고 아니면 V-PRED 그룹을 바이패스**한다.

### (2) 디테일러 `.pt` 파일 — 받는 곳과 보안 경고

가장 자주 나온 질문의 답이다.

```text
받는 곳 : 파일명을 그대로 구글에 검색하면 허깅페이스 링크가 나온다
넣는 곳 : ComfyUI\models\ultralytics\segm
보안 예외 : ComfyUI\user\default\ComfyUI-Impact-Subpack\model-whitelist.txt 를 열고 그 파일 이름을 적는다
```

### (3) 그 밖에 이 계열 워크플로우를 받을 때

| | |
|---|---|
| 베이스 세팅 | `Euler a cfg++ / CFG 0.6 / 50 steps` 처럼 **궁합이 안 맞는 체크포인트가 많은 값**으로 배포돼 있으니 쓰려는 체크포인트의 권장 설정을 반드시 확인하고 바꾼다 (cfg++ 계열 샘플러는 CFG 를 1 미만으로 쓰는 방식이라 일반 샘플러 기준으로 보면 안 된다) |
| 업스케일 스텝 | **스텝이 많으면 찐빠가 나서 15 로 고정**해 쓰거나 **베이스의 절반**(28→14)으로 둔다 |
| 디테일러 스텝 | 원래 스텝의 절반 |
| 컨트롤넷 | 레퍼런스 이미지 하나만 올리면 되고 **출력 시간이 약 두 배**가 된다 |
| `SD Prompt Reader` 수동 설치 | `git clone --recursive https://github.com/receyuki/comfyui-prompt-reader-node.git` → `cd comfyui-prompt-reader-node && pip install -r requirements.txt` |
| `Bjornulf_RandomIntNode` 가 없다 | 그냥 지우고 **아무 랜덤 정수 노드로 갈아 끼워도 된다** |

### (4) EXIF 를 살리면서 인페인트하기 — 이미지를 두 번 올리는 이유

**`SD Prompt Reader` 노드에서 마스크를 뽑으면 오류가 난다.** 그래서 EXIF 를 살려 저장하면서 인페인트하려면
**SD Prompt Reader 노드와 Load Image 노드 양쪽에 같은 이미지를 올리고, Load Image 쪽에서 우클릭 → `OPEN IN MASKEDITOR`** 로 마스킹한다.

→ [오류 해결](troubleshooting.md)

<small>근거 — [빡통워크 5.1 자동 랜덤그림체 + 업스케일 25.08](https://arca.live/b/aiart/146574747) · [4.5 챈에 쓰는 ComfyUI 빡통 워크플로우 4.0 25.06](https://arca.live/b/aiart/139311613)</small>

## 와일드카드 개조 둘 — 순차(`#ASC`)와 폴더 호출(`__*폴더__`)
<small>⚠️ 2025-07 기준 · 근거 2건</small>

### (1) `efficiency-nodes-ED` 계열의 순차 와일드카드

'쉽고 빠른 ComfyUI' 워크플로우가 제공하는 기능이다 (1건, 2025-02).
보통 와일드카드는 매번 무작위로 뽑는데, 이 기능은 **목록을 순서대로 하나씩 훑게 해서 전수 비교를 가능하게** 한다.

`Get Booru Tag ED` 노드의 **`text_b` 칸**에 적는다.

| 문법 | 동작 |
|---|---|
| `__와일드카드__#ASC0` | 그 숫자에서부터 **하나씩 올라가며** 순회. 최대치에 도달하면 멈춘다 |
| `__와일드카드__#DSC1000` | 그 숫자에서부터 **내려오며** 순회. 0 에 도달하면 멈춘다 — **개수를 모를 때 크게 적으면 된다** |
| `#FIX숫자` | 특정 항목으로 **고정** |
| (키워드 없음) | 기존처럼 랜덤 |

숫자는 와일드카드 파일 내 **줄 카운트**이고 배치 사이즈에서도 정상 동작한다.
HiresFix 를 걸 때는 cmd 창에서 와일드카드가 무엇으로 변환됐는지 확인하고 `#FIX숫자` 로 바꿔 주면 된다.

> ⚠️ **제약이 셋이다** — `Get Booru Tag ED` 와 `Efficient Loader ED` 가 있을 때만, **`text_b` 칸에 적었을 때만**,
> 그리고 **`Get Booru Tag ED` 가 워크플로에 하나만 있을 때만** 정상 동작한다.
> ⚠️ **2025-02-07 자로 키워드가 `#INC`/`#DEC` 에서 `#ASC`/`#DSC` 로 바뀌었다.** 옛 글의 표기는 더 이상 맞지 않는다.
> 업데이트는 `update all` 후 `ComfyUI\custom_nodes\efficiency-nodes-ED\start.bat` 실행.

### (2) 폴더 이름으로 호출하기 — Impact Pack 개조

Impact Pack 의 와일드카드 노드에 '폴더명으로 호출' 을 추가하는 파일 교체 개조다 (1건, 2025-07).

```text
1. impactPack 커스텀 노드가 이미 설치돼 있을 것
2. ComfyUI\custom_nodes\comfyui-impact-pack\modules\impact 로 이동
3. 받은 wildcards.py 로 교체
4. ComfyUI 재시작
```

```text
기존 :  __채소__      __고기__          ← 파일 단위 호출만 된다
추가 :  __*식량__                        ← 식량 폴더 안의 파일 중 하나를 무작위로
        __*모든것__                      ← 더 위 계층까지 통째로
```

폴더 구조만 잘 정리하면 `__*시간__`, `__*장소__`, `__*캐릭터__` 처럼 **개념 단위로 뽑을 수** 있고,
`__*nsfw__` 를 여러 번 나열해 그 폴더 전체를 대상으로 가챠를 돌리는 것도 가능하다.

> ⚠️ **WebUI 쪽 dynamic prompts 에서는 쓸 수 없고**(작성자가 WebUI 를 안 써서 미확인),
> **파일 인코딩은 UTF-8 이어야 한글이 깨지지 않는다.**

<small>근거 — [계층적 와일드카드 만들었음. 25.07](https://arca.live/b/aiart/142805267) · [쉽고 빠른 ComfyUI V7 - 순차적 와일드 카드 업뎃 25.02](https://arca.live/b/aiart/128282786)</small>

## 그림체가 쓸 만한지 판정하는 워크플로우 — 다섯 기준
<small>2025-12 기준 · 근거 1건</small>

작가 조합(그림체)이 쓸 만한지 **판정하는 기준**을 워크플로우로 굳힌 글이다 (1건, 2025-12). 실행에 `was-node-suite-comfyui` 가 필요하다.

워크플로우는 **SFW 2장 + NSFW 3장을 한 번에** 뽑도록 짜여 있다. 맨 윗줄에 작가 리스트를, 왼쪽에 프롬프트 리스트를 넣고
오른쪽 메모장 노드에 잘 나온 조합을 적어 두는 구조다. 칸을 늘리려면 shift 로 여러 개 선택한 뒤 `ctrl+c` / `ctrl+shift+v` 로 복제한다.

### 판정 기준 — 이 글의 핵심

| 장 | 무엇을 보는가 |
|---|---|
| 1 (SFW) | 다른 이미지들과 **얼굴 특징·비율(이마 비율, 눈 크기, 눈매)이 일관되는가** |
| 2 (SFW) | **얼굴과 몸의 묘사 밀도가 균일한가** |
| 3 | **손과 성기 묘사가 무너지지 않는가** |
| 4 | 인체와 프롬프트가 제대로 먹히는가 — **유두를 꼬집고 있어야 하고 티셔츠가 뚫리면 안 된다** |
| 5 | **남자아이 형태도 나오는가** |

**나쁜 예를 일부러 같이 준다** — `Artist Set D` 는 얼굴과 몸이 따로 놀고 손이 망가지며 옷이 뚫린다.
좋은 예/나쁜 예를 나란히 주는 구성이라 **판정 감각을 익히기 좋다.**

여러 번 돌려 봤을 때 프롬프트가 가장 잘 먹은 것은 `Set C` 와 `Set F` 였다 (체크포인트 WAI NSFW v15).

```text
Set C : (artist:kakure eria:0.85), (artist:ie \(raarami\):0.9), (artist:blue gk:0.95),
        (artist:beitemian:0.45), (artist:healthyman:0.7), (artist:2n5:0.5),
        (artist:iwano kenta:0.95), (artist:yomu \(sgt epper\):0.6), (artist:c.cu:0.75),
        (artist:aster crowley:0.6),
```

워크플로우는 EXIF 가 살아 있는 첨부 이미지를 ComfyUI 에 끌어다 놓으면 불러올 수 있다.

→ [프롬프트 쓰는 법](prompting.md) 의 '그림체 깎기'

<small>근거 — [(ComfyUI) 그림체 테스트 워크플로우 + 그림체 공유 … 25.12](https://arca.live/b/aiart/157943050)</small>

## 이름을 봤을 때를 위해 — 컬러 노이즈 패치 · Ollama 자동 프롬프트 · 픽셀아트
<small>2026-08 기준 · 근거 3건</small>

### 컬러 노이즈 샘플러 패치 (`comfyui-cns_sampler_patch`, 2026-05)

노이즈를 주입하는 샘플러에 '컬러 노이즈(colored noise)' 를 적용하는 패치다.
근거 논문 `https://arxiv.org/abs/2605.30332`, 공식 구현 `https://github.com/hadardavidson/colored-noise-sampling`.
이 배포판(`https://github.com/namemechan/comfyui-cns_sampler_patch`)은 `SamplerCustomAdvanced` 에
샘플러·스케줄러·노이즈를 따로 붙여 쓰는 사람, 특히 별도 SPEED 노드를 쓰는 사람용이다.

> ★ **작동 조건 — `ancestral` 또는 `sde` 가 붙은 샘플러에서만 동작한다.**
> 노이즈를 다시 주입하지 않는 샘플러에서는 **아예 효과가 없다.**

**효과는 미묘하다.** 글쓴이 본인도 '솔직히 잘 모르겠다' 며 A/B 비교 이미지를 놓고 직접 판단하라고 했다.
댓글 관찰로는 다크라인 처리가 부드러워지고 AI 특유의 면처리가 덜 느껴지며 하이라이트는 오히려 날카로워진다는 평이 있다.

| 실사용 문제 (댓글) | |
|---|---|
| `euler_ancestral` 에서 오류 | **`euler_ancestral_RF`** 로 하면 된다 |
| `[CNS] Warning: coloring skipped at this step – Padding size 4 is not supported for 5D input tensor.` | 1104x1472 같은 특이 해상도의 버그로, **제작자가 수정했다** |

> 곁다리 — **WebP 로 뽑아도 `ImageSaver` 를 쓰면 프롬프트 메타데이터가 저장되고** 윈도우 기본 메타정보 뷰어로도 프롬프트가 보인다.

### Ollama 로 프롬프트를 자동 작성하기 (2026-05)

ComfyUI 에 Ollama 로컬 LLM 을 붙여 **거칠게 쓴 묘사를 프롬프트로 정리**하게 하는 구성이다. 쓰는 법은 둘이다.

| | |
|---|---|
| **이미지 + 사용자 프롬프트** | 이미지를 넣고 프롬프트에는 **캐릭터 이름 정도만** 적으면 나머지는 LLM 이 만든다 |
| **텍스트만** | 이미지 로드 노드를 바이패스하고 원하는 장면을 묘사한다. **아주 거칠게 써도 된다** |

```text
캐릭터: 무츠키(블루 아카이브) / 복장: 마젠타 색 드레스, 검은 머리띠, 망사 스타킹 /
상황: 다리를 꼬고 앉아 있다. smile, one eye closed
→ 한글과 영어 태그를 섞어 대충 써도 LLM 이 정리해 준다
```

모델은 `Huihui_ai/qwen3-vl-abliterated:8b-instruct` 를 썼다.

> ⚠️ **한계 — LLM 이 이미지 속 캐릭터가 누구인지는 알아보지 못해 캐릭터 이름은 수동으로 적어야 한다.**
> WD 태거를 붙이는 것도 고려했지만 태거도 완벽하지 않아 그냥 수동으로 쓴다고 밝혔다.
> 잘 안 되면 **auto prompt 그룹만 떼어다 자기 워크플로우에 붙여** 써도 된다.

### 픽셀 아트는 스텝을 줄여도 된다 (2026-08)

**픽셀 아트는 디테일이 떨어져도 어색해 보이지 않는 특성**이 있어서
**디테일러가 필요 없고 스텝이 적어도 찐빠가 잘 나지 않는다.** 그래서 WAI17 기반 픽셀 아트 워크플로우는 **20스텝만** 쓰고 그만큼 빠르다.

→ [프롬프트 쓰는 법](prompting.md) 의 'LLM 에 프롬프트를 맡기기'

<small>근거 — [(수정) 아니마 b1 ollama 자동 프롬프트 테스트 26.05](https://arca.live/b/aiart/171660784) · [comfyui-cns_sampler_patch 26.05](https://arca.live/b/aiart/172367736) · [WAI17(일러스트리어스) T2I 픽셀 아트 생성 워크플로우… 26.08](https://arca.live/b/aiart/179639518)</small>

## 크게 키웠다 줄이는 구조 — 체크포인트를 탄다
<small>⚠️ 2025-05 기준 · 근거 1건</small>

'아주 선명한' 결과를 내는 워크플로우의 구조인데, **아무 모델에나 옮겨 쓰면 안 되는 대표적인 예**다 (1건, 2025-05).

```text
ComradeshipXL v14KC  →  1K t2i  →  2.70배 hi-res i2i  →  0.25배 다운스케일  →  2x-AnimeSharpV4 업스케일
```

즉 **크게 키웠다가 줄인 뒤 전용 업스케일러로 마무리**하는 방식이다.

> ⚠️ **이 구조는 `v14KC` 가 고해상도 관련 튜닝이 되어 있기에 가능한 것이고, 일반 ILXL 기반 모델에서는 제대로 작동하지 않는다**고 배포자가 못 박았다.

| | |
|---|---|
| 속도 | 4080 Super 16GB, fp16 fast 모드에서 **장당 35초** |
| VRAM | 12GB 정도면 충분 |
| 워크플로우 | `https://huggingface.co/hanzogak/comradeshipXL/blob/main/superclear.zip` (샘플 이미지의 ComfyUI EXIF 를 그대로 써도 된다) |

**남에게 받은 워크플로우를 다른 체크포인트에 끼우면 그대로는 잘 안 나온다**는 일반 규칙의 구체적 사례다.

→ [업스케일과 화질](upscale.md)

<small>근거 — [아주 선명한 ComradeshipXL v14KC용 Comfy… 25.05](https://arca.live/b/aiart/136415303)</small>

## 컴피 첫날 Q&A — 버튼 위치부터 태그 자동완성까지 (2024-07)
<small>⚠️ 2024-07 기준 · 근거 1건</small>

입문 3일 차가 구글링하며 막혔던 것을 Q&A 로 모은 글이 하나 있는데, **컴피 첫날의 막힘 대부분이 여기서 덮인다** (112644586, 2024-07). 아래는 그 목록이다.

| 막히는 곳 | 답 |
|---|---|
| 시작 버튼이 어디 | 화면 **우하단 메뉴의 `Queue Prompt`** |
| 생성 중지 | 우하단 **`View Queue`** → 진행 중인 항목의 `Cancel` |
| 원하는 노드를 못 찾겠다 | **빈 공간을 더블클릭**하면 노드 검색창이 뜬다 |
| 확장(커스텀 노드) 설치 | `custom_nodes` 폴더에서 빈 공간 우클릭 → `Open Git Bash here` → `git clone <깃허브 주소>` |
| 그룹·노드 제목과 색 바꾸기 | 우클릭 → `Edit Group` (예: `CLIP Text Encode (Prompt)` 를 `Positive`/`Negative` 로) |
| 노드 위치가 자꾸 움직인다 | 우클릭 → `Lock`. 그룹은 `Edit Group` → `Lock` |
| 노드가 너무 많다 | **`Ctrl`+클릭** 다중선택 → 우클릭 → `Convert to Group Node`. `Manage Group Node` 에서 매개변수 순서를 바꾸거나 숨긴다 |
| 선만 이어진 작은 노드의 정체 | **`Reroute`** — 선 정리를 위한 중간다리일 뿐 기능이 없다 |
| 로라 트리거 워드를 매번 찾기 귀찮다 | `https://github.com/jitcoder/lora-info` 를 깔면 LoRA 정보 노드가 생긴다 |

### ⚠ Bypass 와 '그룹 비활성화' 는 같은 것이 아니다

남의 워크플로우를 통째로 복붙했더니 안 쓰는 부분까지 다 돌아 시간이 폭발할 때 끄는 방법이 둘인데, **동작이 다르다.**

| | 하는 법 | 노드의 상태 | 중간에 낀 것에 쓰면 |
|---|---|---|---|
| **Bypass** | 노드 우클릭 → `Bypass` (단축키 **`Ctrl+B`**, 보라색이 됨) | **노드는 존재하되 그 작업만 건너뛴다** | 정상. 컨트롤넷을 반드시 거치게 짠 워크플로우도 그 부분만 Bypass 하면 평범한 t2i 처럼 돈다 |
| **그룹 비활성화** | 그룹 우클릭 → `Set Group Nodes to Never` (되살리기는 `Always`) | 그 노드들이 **'존재하지 않는 것'** 이 된다 | **워크플로 중간의 그룹을 끄면 에러가 나며 멈춘다** |

즉 **'있어야 하지만 이번엔 쓰기 싫은' 중간 노드(LoRA·컨트롤넷)는 그룹 비활성화가 아니라 Bypass** 다.
그룹을 우클릭 없이 스위치 하나로 끄고 켜려면 `https://github.com/rgthree/rgthree-comfy` 의 **Fast Groups Bypasser / Fast Groups Muter** 를 쓴다.

### WebUI 처럼 태그 자동완성 쓰기 — Load 다음에 **Save 를 눌러야 한다**

```
https://github.com/pythongosssss/ComfyUI-Custom-Scripts
```

설치한 뒤 우하단 톱니바퀴 → 설정 → `Tag Autocomplete` → `Manage Custom Words` → **우상단 `Load`** 를 누르면 단부루 태그를 전부 가져온다.
**`Load` 후 반드시 `Save` 를 눌러야 적용된다** — 여기서 안 눌러 "안 된다" 는 사람이 많다.

같은 확장으로 빈 공간 우클릭 메뉴에서 **워크플로를 이미지 파일로 추출**해 공유할 수도 있다.

→ [설치와 환경 구성](install.md) · [프롬프트 쓰는 법](prompting.md)

<small>근거 — [(ComfyUI 대회) 뉴비입장에서 적어보는 찐뉴비용 Com… 24.07](https://arca.live/b/aiart/112644586)</small>

## 배포 워크플로우를 처음 열었을 때 — 로더 넷 · 폴더 · 배율 · 접힌 노드
<small>⚠️ 2025-07 기준 · 근거 4건</small>

워크플로우 공모전 출품작들의 가이드가 같은 곳을 반복해서 짚는다 (141180724 · 141718826 · 141991828, 2025-07).
'남의 워크플로우가 안 돈다' 의 대부분은 아래 넷을 확인하면 끝난다.

### 1. 반드시 확인할 로더 넷

| | 무엇 | 폴더 |
|---|---|---|
| 1 | **체크포인트** — 그림을 생성하는 모델 | `comfyui/models/checkpoints` |
| 2 | **VAE** — 잠재 상태의 그림을 눈에 보이는 이미지로 바꾸는 해독기 | `models/vae` |
| 3 | **LoRA** — 스타일·캐릭터·포즈를 강제하는 보조제 | `models/loras` |
| 4 | **업스케일 모델** — 해상도를 높이는 파일 | `models/upscale_models` |

받은 워크플로우에는 **그 사람의 파일명이 그대로 박혀 있고 내 폴더엔 그 파일이 99% 없다.**
각 로더에서 흰 글씨의 파일명을 눌러 **내 파일로 바꾸면** 된다. → 위 '남의 워크플로우가 안 돌아가는 진짜 이유'

> **`Value not in list` 오류**도 같은 원인이다. 워크플로우에 박힌 **로라·업스케일·디텍터 모델 이름이 내 폴더에 없어서** 나는 것이므로, 접힌 노드를 펼쳐 내 파일로 바꾸거나 `None` 으로 둔다.

**ILXL(Illustrious XL) 계열 모델은 대부분 VAE 를 내장**하므로 별도 VAE 로더를 안 써도 된다. 내 모델이 무슨 계열인지는 Civitai 페이지에 적혀 있다.

### 2. 노드가 접혀 있다 — 회색 동그라미

노드 **왼쪽 위의 회색 동그라미**를 누르면 접기/펼치기가 토글된다.
배포 워크플로우는 화면을 정리하려고 로더나 Negpip 같은 노드를 **접어 둔 채로 올리는 경우가 많아서**, 접힌 것을 펼치지 않으면 고쳐야 할 노드가 아예 눈에 안 띈다.

### 3. 업스케일 배율은 고정돼 있다 — 2x 모델로 1.25배는 `scale_by 0.625`

업스케일 모델은 배율이 제각각으로 **고정**돼 있다. 2x 모델을 쓰면서 **1.25배만** 확대하려면

```
scale_by = 원하는 배율 ÷ 모델 배율 = 1.25 ÷ 2 = 0.625
```

ComfyUI 표시상 **`0.63` 으로 반올림**된다. 세 편의 워크플로우가 모두 `2x-AnimeSharpV4` 계열 + `0.63` 을 쓴다.
같은 계산으로 4x 모델에서 2배를 원하면 `0.5` 다. → [업스케일과 화질](upscale.md)

### 4. 그룹 스위치 — `matchTitle` 로 자동 등록

스위치 노드(붉은 노드)로 그룹을 통째로 켜고 끌 수 있고, 우클릭 → `Properties` → **`matchTitle`** 에 `A|B|C|D` 형식으로 키워드를 넣으면 **제목에 그 키워드가 들어간 그룹이 자동으로 스위치에 뜬다.**

### 5. v-pred 가 아니면 두 노드를 지운다

`CFG Rescale` 과 `Model Sampling(이산)` 은 **v-pred 모델용**이다. v-pred 가 아닌 체크포인트로 바꿨는데 **회색 화면만 나오면** 이 두 노드를 지우거나 그 그룹을 비활성화한다.
회색 이미지의 원인은 세 가지다 — ① 체크포인트에 VAE 가 내장돼 있는지 ② v-pred 모델이 아닌데 그 그룹이 켜져 있는지 ③ 프롬프트 가중치를 과하게 주지 않았는지.

> ⚠ 한 배포글은 **v-pred 를 쓰지 않는 모델 자리는 바이패스로 두지 말고 노드를 아예 삭제해야 문제가 안 생긴다**고 밝혔다 (141848057, 한 글에서만 언급됨).

<small>근거 — [(워크플로우 공모전) 라면보단 어렵더라! 3트째 간편 워크플… 25.07](https://arca.live/b/aiart/141180724) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826) · [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 25.07](https://arca.live/b/aiart/141848057) · [(워크플로우 공모전) 라면보다 쉽다! 간편 종합 워크플로우 … 25.07](https://arca.live/b/aiart/141991828)</small>

## ⚠ 후처리 순서는 '업스케일 → 디테일러' 다 — 본문이 틀렸고 대회 주최자가 잡았다
<small>⚠️ 2025-07 기준 · 근거 4건 · 자료 엇갈림</small>

워크플로우 공모전 출품작 하나가 **'생성 → 디테일러 → 업스케일'** 순서로 짜여 올라왔다 (141180724, 2025-07-01).
**이 순서는 틀렸다.** 대회 주최자가 댓글로 지적했고 **작성자가 수긍해 다음 버전에서 고쳤다.**

> **"후처리 순서는 업스케일 → 디테일러가 맞다.
> 디테일러 → 업스케일로 하면 해상도가 낮아 디테일러가 제대로 일하기 어렵고,
> 업스케일이 자체적으로 디테일러보다 낮은 수준의 보정을 가하므로 디테일러의 의미가 퇴색된다."**
> — 141180724 댓글 (대회 주최자)

바로 다음 버전(141718826, 2025-07-07)의 흐름이 이렇게 바뀌었다.

```text
0 모델·로라 로더 → 1.0 프롬프트 → 1.1 리저널
  → 2.0 생성 → 2.1 업스케일 → 2.2.1 얼굴 디테일러 → 2.2.2 손 디테일러 → 3.0 최종
```

최우수상 수상작(141991828 v1.4)도 같은 순서다 — `2.0 생성 → 2.1 업스케일 → 2.2 디테일러`.

**왜 그런가** — 디테일러는 얼굴·손 영역을 잘라내 확대한 뒤 다시 그려 붙이는 도구다.
업스케일 전의 저해상도 상태에서는 잘라낸 조각이 너무 작아 **다시 그릴 정보 자체가 없다.**

> **예외적으로 세 번을 도는 구성도 있다** — `생성 → 디테일러 → SD 업스케일 → 업스케일 후 디테일러` 처럼 앞뒤로 한 번씩 거는 워크플로우가 있고, 각 단계를 스킵할 수 있게 만들어 뒀다 (142197182). 다만 **하나만 고른다면 업스케일 뒤가 맞다.**

→ [업스케일과 화질](upscale.md) · [디테일러](detailer.md)

<small>근거 — [(워크플로우 공모전) 라면보단 어렵더라! 3트째 간편 워크플… 25.07](https://arca.live/b/aiart/141180724) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826) · [(워크플로우 공모전) 라면보다 쉽다! 간편 종합 워크플로우 … 25.07](https://arca.live/b/aiart/141991828) · [(워크플로우 공모전) T2I특화 모듈형 프롬프트 워크플로우 25.07](https://arca.live/b/aiart/142197182)</small>

## ⚠ Negpip — 콜론 **앞**에 쉼표가 없으면 안 먹는다 (본문은 '작동 안 해서 지웠다'고 적었다)
<small>⚠️ 2025-07 기준 · 근거 2건 · 자료 엇갈림</small>

Negpip 은 NAI 처럼 **긍정 프롬프트 안에서 마이너스 가중치**를 쓸 수 있게 해 주는 노드다.
한 출품작 본문은 **"작동하지 않아서 지웠다"** 고 적었는데, 댓글에서 **문법을 몰랐던 것**임이 드러났다 (141180724, 2025-07-01).

### 문법 — 태그와 콜론 사이에 쉼표를 하나 넣는다

```text
(black,:-1.7)      ← 먹힌다
(black:-1.7)       ← 먹히지 않는다

..., furry,:-2, ...   ← 프롬프트 안에서는 이런 모양
```

**콜론 바로 앞의 쉼표가 필수다.** 이것 하나 때문에 "노드가 고장났다"고 판단하고 지운 것이었다.
다음 버전(141718826)에서 작성자가 다시 넣었다.

### 노드 배치

`comfyui-ppm` 의 **`Positive Prompt (CLIPNegPip)`** 노드를 **Load Checkpoint 뒤**에 두고 `CLIP Text Encode` 로 잇는다.

### 태그마다 반응하는 강도가 다르다

| 태그 | 반응 시작 |
|---|---|
| `blonde hair` | **-0.4** 부터 |
| `gothic dress` | **-1.7** 은 되어야 |

고딕 드레스는 학습값이 거의 검정이라 **네거티브에 `(black:1.8)` 을 넣어도 색이 안 바뀌는데**, Negpip 으로 긍정 쪽에 음수를 주면 바뀐다. 이것이 이 노드를 쓰는 이유다.

→ [프롬프트 쓰는 법](prompting.md)

<small>근거 — [(워크플로우 공모전) 라면보단 어렵더라! 3트째 간편 워크플… 25.07](https://arca.live/b/aiart/141180724) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826)</small>

## 굿나잇 랜덤 워크플로우 — `Random Number` 오류와 굳어진 실전값
<small>⚠️ 2025-07 기준 · 근거 3건</small>

돌려 놓고 자는 동안 **체크포인트·로라·해상도를 매번 무작위로** 골라 주는 워크플로우 계열이다 (141848057 v1.0 → 142088366 v1.5 → 142849197 v1.8, 2025-07).

### ⚠ v1.5 를 받았다면 v1.8 로 간다

```
float object cannot be interpreted as an integer
```

**v1.5 는 실행하면 `Random Number` 노드에서 위 오류가 난다.**
댓글에서 여러 사용자가 ComfyUI 를 클린 설치해도 재현했고, 결국 **제작자가 `Random Number` 를 `Random Integer` 노드로 교체**해 v1.8 로 다시 올렸다.
(v1.0 기준으로는 random 노드를 float 로 강제하면 돌아가기도 했지만 v1.5 는 그 방법도 통하지 않았다.)

**v1.8** — `https://arca.live/b/aiart/142849197`

### 입력 형식 — 여기서 자주 막힌다

| 칸 | 형식 | 함정 |
|---|---|---|
| 선택 범위 | **`n~n`** | **물결표가 없으면 인식하지 못한다.** 하나만 쓰려면 `1~1` |
| 해상도 프리셋 | **`가로,세로`** | **콤마 외의 구분자는 인식하지 못한다** |
| 로라 스태커 | 카테고리를 통일 | 캐릭터끼리 / 의상끼리 / 포즈끼리. 이름이 '캐릭터 랜덤 로라' 일 뿐 무엇이든 된다 |

### 굳어진 수치

| 항목 | 값 |
|---|---|
| 해상도 배율 | **1.25배까지 안정적.** 1.5배는 1:1 비율이 아니면 인체가 무너진다. 작은 소수점은 쓰지 않는다 |
| 업스케일 | 배율과 무관하게 **항상 1024x2 크기**로 고정 |
| 디테일러(얼굴·눈·손) | `guide/max size` 가 높게 잡혀 있다. **VRAM 이 부족하면 512 / 1024 로** |
| 손 디테일러·업스케일 | **CFG 1 / 12스텝** (크게 변형될 필요가 없다) |
| Ultimate SD Upscale | 단순 업스케일만 원하면 `Mode = None` |

### 절대 하면 안 되는 것

- **디테일러·컨트롤넷·SAM 로더를 `Anything Everywhere` 로 모아 둔 그룹은 바이패스 금지.**
- v-pred 를 쓰지 않는 체크포인트 자리는 **바이패스가 아니라 노드를 삭제**한다.

### 로딩이 느리면

`efficiency-nodes` 의 **`LoRA Stacker`** 노드를 **Easy-Use 의 `EasyLoraStacker`** 로 교체한다. 토글을 `enable` 로 두는 것 외엔 사용법 차이가 없다.

<small>근거 — [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 v1.8 25.07](https://arca.live/b/aiart/142849197) · [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 25.07](https://arca.live/b/aiart/141848057) · [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 v1.5 25.07](https://arca.live/b/aiart/142088366)</small>

## ⚠ 배포 워크플로우의 긍정/부정 '색 표기' 는 믿지 마라 — 세 번 반복된 사고다
<small>2025-08 기준 · 근거 3건 · 자료 엇갈림</small>

노드 색으로 긍정(초록)·부정(빨강)을 표시해 둔 워크플로우에서 **표기와 실제 연결이 반대인 사고가 반복해서 보고됐다.**
색만 보고 고치다가 시간을 버리는 지점이라 따로 적는다.

| 워크플로우 | 무엇이 어긋났나 | 결말 |
|---|---|---|
| **141718826** (2025-07) | 긍정=초록·부정=빨강으로 표시했는데 **실제 조건 연결이 정반대**였고, 특히 **아웃페인팅 쪽은 긍정 프롬프트를 묶은 노드가 부정 영역으로 연결**돼 있었다 | 댓글 지적 → **작성자 인정**, 다음 버전에서 수정 |
| **141991828 v1.4** (2025-07) | 컨트롤넷의 긍정/부정 **노드 색만** 반대(부정이 녹색·긍정이 적색) | **연결 자체는 정상**이었고 색만 고쳤다 |
| **145850172** (2025-08) | 부정 프롬이 긍정 프롬으로 잘못 연결돼 **디테일러가 "부정 프롬을 연결하라"는 오류**를 냈다 | 가장 마지막 긍정조건/부정조건인 `controlnet by adjusting` 노드에서 디테일러로 이으면 해결 |

**요령** — 노드 색은 작성자가 손으로 칠한 라벨일 뿐 연결과 아무 관계가 없다.
ComfyUI 에서 **노드를 클릭하면 연결된 그래프가 하얗게 하이라이트**되므로, 색이 아니라 그 선을 따라가 확인한다.

### 같은 워크플로우에서 나온 다른 연결 실수

**디테일러를 걸면 로라가 적용되지 않아 캐릭터 눈이 바뀌는 문제** — 체크포인트 모델이 **로라를 거치지 않고 디테일러로 직결**돼 있던 것이 원인이다.
**마지막 LoRA 노드의 `model` 출력을 디테일러에 연결**하면 해결된다 (145850172).

> 덧붙여, 같은 글에서 나왔다 취소된 지적도 있다 — **"퀄리티 태그를 최상단으로 올려야 한다"** 는 조언은 **지적자 본인이 철회**했다. "대부분의 모델이 최상단이든 최하단이든 **중간만 아니면** 괜찮다고 설명한다" 는 것이다 (141718826 댓글).

<small>근거 — [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826) · [(워크플로우 공모전) 라면보다 쉽다! 간편 종합 워크플로우 … 25.07](https://arca.live/b/aiart/141991828)</small>

## ⚠ 워크플로우 EXIF 가 날아가는 네 경우 — 그림은 보이는데 노드가 안 뜬다
<small>2026-05 기준 · 근거 5건 · 자료 엇갈림</small>

채널의 워크플로우 배포는 대부분 **결과 이미지의 EXIF 에 워크플로를 심어** 올리는 방식이다.
그런데 **EXIF 가 날아가 못 불러오는 사고가 네 가지 경로로 반복해서 일어난다.**

| 경우 | 무슨 일 | 대처 |
|---|---|---|
| **아카라이브에 그냥 드래그해 올림** | 아카 쪽에서 메타데이터가 날아간다 | 글쓰기 편집기 위쪽의 **이미지 버튼 → `EXIF 저장`(EXIF 보존) 체크** 후 **그 창에서** 업로드 |
| **브라우저에서 '새 탭 열기' · '다른 이름으로 저장'** 으로 받음 | 저장 과정에서 EXIF 소실 | **글의 원본 파일**을 받거나, 새 창에서 **로드가 끝난 뒤** ComfyUI 캔버스에 드래그 앤 드롭 |
| **외부 편집기(클립스튜디오·포토샵)로 손댐** | 편집 저장 시 EXIF 가 남지 않는다 | 원본을 따로 보관한다 |
| **Civitai 자체 생성 서버로 뽑은 이미지** | LoRA 적용 정보 등이 **워크플로 형태로 보존되지 않는다** | 드래그해 나온 노드 구성은 **실제 파이프라인이 아니다.** 프롬프트 참고용으로만 쓴다 |

### ⚠ 본문이 틀렸던 사례

145827191 본문은 **"첨부 이미지에서 워크플로를 불러올 수 있다"** 고 적었지만, **최초 판본에서는 사실이 아니었다.**
EXIF 가 날아가 여러 사람이 워크플로를 못 찾았고 **글쓴이가 재업로드 → 다시 해체해 재재업로드까지 두 번** 고쳤다.
같은 일이 142197182 에서도 있었다 — 본문 첫 줄의 catbox 링크는 접속 불가가 됐고 **글의 이미지도 EXIF 가 날아가** 있어서, 작동이 확인된 것은 Kiosk 링크뿐이었다.

### 이미 EXIF 없이 올렸다면

대회 탭 등으로 **글 수정이 막힌 경우**의 우회법이 채널에 정리돼 있다 (114468193).

- 원본 파일을 **압축해 catbox 같은 곳에 올려 댓글로 링크**
- **EXIF 를 체크해 다시 올린 별도 글**을 만들어 링크

> 채널에서 "이 그림 프롬 좀" 이라는 요청이 잦은 것도, 남의 그림에서 프롬을 받아 오는 문화가 성립하는 것도 **전부 이 EXIF 보존이 전제**다.

→ 위 '뽑은 그림에 프롬프트를 남기는 법 — 추적하지 말고 심어라'

<small>근거 — [ComfyUI 뉴비의 초간단 regional 분리 방법(영역… 25.08](https://arca.live/b/aiart/145827191) · [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172) · [(미쿠미쿠 대회) 미쿠짤 뽑으려고 ai그림 시작했던 뉴비 24.08](https://arca.live/b/aiart/114468193) · [(워크플로우 공모전) T2I특화 모듈형 프롬프트 워크플로우 25.07](https://arca.live/b/aiart/142197182)</small>

??? note "근거 5건 전부 보기"
    [ComfyUI 뉴비의 초간단 regional 분리 방법(영역… 25.08](https://arca.live/b/aiart/145827191) · [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172) · [(미쿠미쿠 대회) 미쿠짤 뽑으려고 ai그림 시작했던 뉴비 24.08](https://arca.live/b/aiart/114468193) · [(워크플로우 공모전) T2I특화 모듈형 프롬프트 워크플로우 25.07](https://arca.live/b/aiart/142197182) · [컴피 질문이 있습니다 26.05](https://arca.live/b/aiart/170967423)

## 리저널을 실제로 채우는 법 — 칸 나누기 · 좌표 · 개별 로라의 한계
<small>2025-08 기준 · 근거 5건</small>

위 '영역 분할 프롬프트 — 세 세대가 겹쳐 있다' 가 **무엇을 쓰는가**였다면, 이 항목은 **칸을 어떻게 채우는가**다.
2025년 공모전 출품작들이 같은 규칙을 반복해서 안내한다.

### 1. '인물' 칸에는 인원 수만 적는다

| 칸 | 넣는 것 |
|---|---|
| **인물(person)** | **`1girl`, `1boy`, `2girls`, `3girls` — 인원 수만** |
| **캐릭터(character)** | 캐릭터명 · **의상 · 외형 · 포즈 전부** |

모델이 **인원 수를 맨 앞에 두기를 권하기 때문에** 칸을 나눠 놓은 것이다. 여기에 의상을 적으면 순서가 흐트러진다.

### 2. 리저널은 메인 프롬에 합쳐지지 않는다

리저널 프롬은 메인 프롬에 **합쳐져 들어가는 구조가 아니다.**
그래서 의상 같은 요소는

1. 먼저 메인 `Character` 프롬에 **"이런 의상이 존재한다"는 전제**를 깔아 두고
2. 리저널에는 **그것을 누가 입고 있는지**를 적는다

이 순서를 지키지 않으면 리저널 쪽 의상이 통째로 무시된다 (140945356).

### 3. 마스크는 좌표계다

화면을 좌우 절반으로 나눌 때 (145850172):

| 위치 | 값 |
|---|---|
| 왼쪽 캐릭터 | `x=0`, `width=50` |
| 오른쪽 캐릭터 | `x=50` |

**`x` 에 음수를 넣을 수 없다.** 그래서 왼쪽 바깥으로 영역을 빼는 식의 배치는 안 된다.
3등분 마스킹으로 최소 2인·최대 3인을 지정하는 구성이 표준이고, 2인만 쓰면 세 번째는 비워 둔다.

### 4. ⚠ 캐릭터별 개별 로라는 그 워크플로우에서 작동하지 않았다

최우수상 수상작 v1.4 는 **리저널 프롬프트의 캐릭터별 개별 로라 노드가 구조상 작동하지 않는 노드였음을 확인하고 제거**했다 (141991828).
대신 권하는 것은 **로라 트리거 단어를 각 리저널 프롬프트 입력창에 직접 적는 것**이다.

> 다만 이것이 "ComfyUI 에서 영역별 로라가 불가능하다"는 뜻은 아니다.
> 바닐라 기본 노드의 **'후크 LoRA 생성'** 노드나 **`LoRA Hook`** 노드를 각 리저널 프롬프트에 연결하면 된다는 보고가 따로 있다 (145827191 댓글).
> **VRAM 을 극단적으로 많이 먹고 시간도 오래 걸린다**는 대가가 있다.

### 5. 로라 로더에 `None` 이 없을 때

ComfyUI 에 기본으로 딸려 오는 리저널 쪽 로라 로더 노드에는 **`None` 옵션이 없다.**
로라를 안 쓰려면 **아무 로라나 넣고 강도를 0** 으로 두거나, **`Blank.safetensors` 라는 이름의 빈 파일**을 만들어 할당한다 (140945356).

### 6. 값은 얼마나 비싼가

리저널 버전은 영역 구분이 없는 통짜 대비 **약 2배의 생성 시간**이 든다 (145850172).

### 가장 단순한 자작 구성

고인물 워크플로는 노드가 너무 많고 업데이트가 끊긴 노드도 섞여 있어 뉴비가 고쳐 쓰기 어렵다는 판단에서 나온 **최소 구성**이 있다 (145827191).
원리는 **마스크 좌표로 영역을 지정하고 그 영역에 대응하는 프롬프트 입력란을 두는 것**이 전부이고, 영역을 늘리려면 **조건(conditioning) 노드와 프롬프트 노드를 같은 방식으로 복제**해 붙이면 된다.
필요한 커스텀 노드 팩은 **`was-ns`(WAS Node Suite)** 와 **`comfyui-inspire-pack`** 둘이다.

<small>근거 — [ComfyUI 뉴비의 초간단 regional 분리 방법(영역… 25.08](https://arca.live/b/aiart/145827191) · [(워크플로우 공모전) 라면보다 쉽다! 생활 간단 워크플로우!… 25.06](https://arca.live/b/aiart/140945356) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826) · [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172)</small>

??? note "근거 5건 전부 보기"
    [ComfyUI 뉴비의 초간단 regional 분리 방법(영역… 25.08](https://arca.live/b/aiart/145827191) · [(워크플로우 공모전) 라면보다 쉽다! 생활 간단 워크플로우!… 25.06](https://arca.live/b/aiart/140945356) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826) · [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172) · [(워크플로우 공모전) 라면보다 쉽다! 간편 종합 워크플로우 … 25.07](https://arca.live/b/aiart/141991828)

## 워크플로우를 파이썬 코드로 — 코랩·헤드리스에서 돌리기 (2025-08)
<small>2025-08 기준 · 근거 1건</small>

ComfyUI 워크플로우를 **파이썬 스크립트로 변환**해 코랩 같은 저사양·헤드리스 환경에서 돌리는 경로다 (146658219, 2025-08).
`ComfyUI` 로 그대로 돌렸다면 RAM·VRAM 이 터졌을 워크플로우를 코랩에서 굴린 실제 사례가 있다.

**사전 준비** — ComfyUI 설치, 그 워크플로우가 쓰는 **모든 커스텀 노드 설치**, 변환 도구 `pydn/ComfyUI-to-Python-Extension` 설치.

### 1. 확장 자체의 버그부터 고친다

현재 이 확장은 UI 에서 **`To Python` 버튼이 사라지는 문제**가 있다.

```
js/save-as-script.js 를 Pull Request #132 ('Fix To Python button') 대로 수정
```

이걸 해야 코드 추출이 된다.

### 2. 추출된 코드 고치기

**(a) 커스텀 노드 로딩** — ComfyUI 의 비동기(async) 환경에서 커스텀 노드를 안정적으로 불러오려면 필수다.

```python
# init_extra_nodes()            ← 이렇게 되어 있는 것을
loop.run_until_complete(init_extra_nodes())   # 이렇게 바꾼다
```

**(b) 메모리 관리 함수 추가** — import 구문 아래에 넣고, 작업이 끝나는 지점(예: 이미지 저장 후)에서 호출한다.

```python
import torch
import gc

def clear_memory():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
    gc.collect()
```

**(c) 불필요한 변수 제거** — 더 이상 쓰지 않는 무거운 변수를 직접 지운 뒤 `clear_memory()` 를 부르면 효과가 크다.

```python
del model, clip, vae
clear_memory()
```

### ⚠ 호환성 함정 — 다중 LoRA Stack 노드

이 확장은 **모든 커스텀 노드와 100% 호환되지 않는다.**
특히 **여러 LoRA 를 한 번에 불러오는 Stack 방식 노드**를 쓰면 코드로 변환이 안 되거나, 변환돼도 실행 시 메모리가 정리되지 않아 오류가 난다.

> **해결책은 복잡한 다중 LoRA 노드 대신 기본 LoRA 로더를 여러 개 직렬로 연결하는 것이다.**

**검증** — `wan2.2 q4_k_m` 모델로 832x480 / 81프레임 생성에 문제가 없었다.

→ [VRAM·속도 최적화](vram.md) · [비디오 생성](video-generation.md)

<small>근거 — [코랩에서 원하는 워크플로우를 파이썬 코드로 변환해보자 (WA… 25.08](https://arca.live/b/aiart/146658219)</small>

## NAIA 와 로컬 ComfyUI 를 잇는 두 갈래 — 위계가 다르다
<small>2026-06 기준 · 근거 1건</small>

NAIA(NovelAI 보조 클라이언트)와 로컬 ComfyUI 를 연동하는 방식은 **두 가지이고 누가 주인이냐가 다르다** (173906125, 2026-06).

| | 방식 | 누가 실행하나 |
|---|---|---|
| **① Bridge 노드** *(권장)* | ComfyUI 안에 Bridge 노드를 만들어 연결해 둔다 | **ComfyUI 가 실행과 통제를 한다.** NAIA 는 프롬프트 생성기 역할만 하고 값만 보낸다. **EXIF 관리 등이 되어 이쪽이 편하다**는 것이 답변자의 권고 |
| **② 워크플로 API 등록** | NAIA 에 워크플로 API 를 등록한다 | **NAIA 가 ComfyUI 를 원격으로 통솔한다.** 등록은 커스텀 노드가 아니라 **NAIA 쪽에서** 한다 |

### ⚠ ②에서 자주 나는 실패

워크플로를 **API 형식으로 넘길 때 일부 커스텀 노드의 필수 입력이 채워지지 않아** 검증에서 떨어진다.

```
[ERROR] [Impact Pack] ComfyUI-Impact-Pack: Error on prompt ... KeyError: 'mode'
[ERROR] * TriggerWord Toggle (LoraManager): Required input is missing: default_active / allow_strength_adjustment / group_mode
[ERROR] * Lora Loader (LoraManager): Required input is missing: text
[ERROR] * PlaySound|pysssss: Required input is missing: file / volume / mode
→ prompt_outputs_failed_validation
```

즉 **LoraManager · Impact Pack · pysssss 계열 노드가 든 워크플로우는 그대로 API 로 넘기면 떨어진다.**
GPU 인식이 끝났고 파라미터를 맞췄어도 이 단계에서 막히므로, 노드 구성을 단순화하거나 ①로 가는 편이 빠르다.

→ [NovelAI](nai.md) · [ANIMA](anima.md)

<small>근거 — [NAIA로 Comfy + 아니마를 써보려는데 사용법을 잘 모… 26.06](https://arca.live/b/aiart/173906125)</small>

## 양자화 — FP8 · MXFP8 · INT8 · convrot, 그리고 공식 지원 (2026 상반기)
<small>2026-07 기준 · 근거 5건</small>

모델 파일 이름에 붙는 `fp8` · `int8` · `mxfp8` · `nvfp4` 는 **가중치를 몇 비트로 줄였는지**를 뜻한다.
2026 상반기에 ComfyUI 본체가 이것들을 차례로 흡수했다.

### 형식별 성격

| 형식 | 스케일을 어떻게 두는가 | 성격 |
|---|---|---|
| **FP8** | **FP32 스칼라 1개로 레이어 전체**를 스케일링 | 가장 거칠다 |
| **MXFP8** | **`FP8E8M0` 스케일을 32블록마다 하나** | FP8 보다 오차가 적을 수 있다 |
| **GGUF Q8_0** | INT8 가중치 + FP16 32블록 스케일 (8.5bpw) | FP8 보다 품질이 좋다 |
| **INT8 rowwise** | 행 단위 스케일 | 빠르다 |
| **INT8 convrot** | 하다마르 변환 계열 **회전으로 outlier 를 뭉갠 뒤** int8 로 자른다 | 단순 clipping 보다 손실이 적어 **품질이 BF16 급**, 대신 rowwise 보다 느리다 |

### 공식 지원 — 언제 무엇이 들어왔나

| 시점 | 내용 |
|---|---|
| **2026-03-15** | **MXFP8 정식 지원** (PR `Comfy-Org/ComfyUI#12907`). 요구 사양은 **RTX 5000 시리즈 이상 + Python 3.10 이상** |
| **2026-06-25** | **INT8 정식 지원** (PR `Comfy-Org/ComfyUI#14636`) — 기본 `Load Diffusion Model` 노드가 int8 모델을 읽는다. **커스텀 노드 없이 쓰려면 `comfy-kitchen` 을 최신으로** 올려야 한다 |
| **2026-07-05** | 공식 모델 컨버터에 **int8convrot 양자화 코드**가 올라왔다 → `https://github.com/Comfy-Org/comfy-model-tools` |

> ✔ **본문이 하루 만에 뒤집힌 사례가 있다.** INT8 공식 지원 글은 *"공식 노드로는 BF16 수준으로 느려서 속도를 원하면 여전히 커스텀 노드를 써야 한다"* 고 적었는데,
> **글쓴이 본인이 댓글에서 철회했다** — *"글 올리고 보니 comfy-kitchen 이 업데이트돼서 테스트해 봤더니 이제 커스텀 노드만큼 빨라졌다."*
> **`comfy-kitchen` 을 최신으로 두면 공식 노드로 충분하다.**

### 실측 (Anima 기준)

**MXFP8 · 30스텝**

| 형식 | 속도 |
|---|---|
| bf16 | 6.26 it/s |
| **mxfp8** | **6.75 it/s** |
| fp8 | 7.03 it/s |
| nvfp4 | 7.38 it/s |

즉 **MXFP8 은 BF16 과 FP8 의 중간이고, FP8 보다 느리다**(글쓴이가 댓글에서 명시). 레이스나 장식 같은 세부 표현은 FP8 보다 조금 나은 느낌이 있다.

**INT8 · 34스텝 · 기본 `Load Diffusion Model` + sage + torch.compile**

| 형식 | 속도 | 1장 |
|---|---|---|
| bf16 | 6.18 it/s | 5.67초 |
| **int8rowwise** | **8.52 it/s** | **4.16초** |
| int8convrot | 7.61 it/s | 4.62초 |

**FP8 을 못 쓰는 RTX 3090 사용자에게 특히 의미 있는 변화**라는 반응이 나왔다.

### 직접 양자화하기

| 도구 | |
|---|---|
| **공식** | `https://github.com/Comfy-Org/comfy-model-tools` — 앞으로 int8 양자화는 여기로 |
| 이전부터 쓰이던 것 | `https://github.com/silveroxides/convert_to_quant` |
| **GUI** | `https://github.com/Starnodes2024/comfyui-starnodes-modelconverter` — NVFP4 / FP8 / MXFP8 / INT8 / INT8 ConvRot 지원 |

**어느 레이어를 양자화할지 고를 때는 HuggingFace 모델 파일 페이지에 들어가면 레이어 정보가 나오므로 그걸 참고한다.**

> ⚠ **StarNodes 컨버터를 포함해 기본 설정 그대로 양자화하면 배경과 소품 디테일이 눈에 띄게 어긋난다**는 후속 검증(2026-07-27)이 있다.
> **레이어 선별 없이 돌리는 것은 권하기 어렵다.**
> NVFP4 는 nVidia 전용이고 실제로는 **RTX 5000 시리즈 이상**에서만 동작하며, 일부 형식은 `comfy-kitchen` 이 필요하다.

### 작은 모델은 양자화할 이유가 없다

**MXFP8 을 소개한 글쓴이 본인의 결론이 냉정하다 — "anima 급(작은) 모델에서 굳이 양자화 모델을 쓸 일은 없을 것."**
MXFP8 이 의미 있는 쪽은 큰 모델이다(Kijai 가 LTX2.3 distilled 를 `mxfp8_block32` 로 만들어 뒀다).
공식 방향도 같아 보인다 — **아니마는 비교적 가벼워서 int8 을 따로 주기보다 터보 LoRA 사용을 권장하는 쪽**이다.

→ [VRAM·속도 최적화](vram.md) · [모델 고르기](models.md)

<small>근거 — [ComfyUI mxfp8 지원 (RTX5000시리즈) 26.03](https://arca.live/b/aiart/164899356) · [ComfyUI 공식 int8convrot 양자화 도구 26.07](https://arca.live/b/aiart/175935647) · [ComfyUI INT8 공식 지원+가속 지원 26.06](https://arca.live/b/aiart/174942443) · [comfyui Starnodes 양자화 노드 26.07](https://arca.live/b/aiart/176070719)</small>

??? note "근거 5건 전부 보기"
    [ComfyUI mxfp8 지원 (RTX5000시리즈) 26.03](https://arca.live/b/aiart/164899356) · [ComfyUI 공식 int8convrot 양자화 도구 26.07](https://arca.live/b/aiart/175935647) · [ComfyUI INT8 공식 지원+가속 지원 26.06](https://arca.live/b/aiart/174942443) · [comfyui Starnodes 양자화 노드 26.07](https://arca.live/b/aiart/176070719) · [ComfyUI 아니마 공식 워크플로우 템플릿 갱신 26.07](https://arca.live/b/aiart/178127727)

## 스텝을 건너뛰는 가속 노드 — 원리가 겹치면 같이 쓰면 안 된다
<small>2026-07 기준 · 근거 2건 · 자료 엇갈림</small>

`TeaCache` · `EasyCache` · `CacheDiT` · 스펙트럼 계열은 **전부 '스텝을 덜 계산하는' 방법**이다.
그래서 **원리가 겹치는 것끼리 겹쳐 쓰면 하나가 동작하지 않거나 결과가 망가진다.**

### 스펙트럼 기반 최적화 (2026-03)

```
https://github.com/ruwwww/comfyui-spectrum-sdxl      # 노드
https://arxiv.org/pdf/2603.01623                      # 논문
```

**원리** — 매 스텝마다 무거운 denoiser 를 전부 실행하는 대신, **이전 스텝들의 feature 를 체비쇼프 다항식으로 피팅해서 중간 스텝은 예측값으로 때운다.**
**스텝 수는 그대로인데 실제 계산량이 절반 이하로 준다.** 이름은 `sdxl` 이지만 Anima 와 일부 DiT 모델도 지원하고, Sage attention 같은 다른 최적화와 병용된다.

| 실측 | |
|---|---|
| SDXL | 6.5초 → **3.6초** |
| Anima | 23.67초 → **13.01초** |

> ⚠ **평가가 크게 갈린다.** 호평은 *"증류 LoRA 가 필요 없을 정도로 빠르다"*, *"스텝이나 스케줄러는 쓰던 걸 그대로 쓰면 된다"*.
> 혹평은 *"25% 정도 빨라진 대신 **디노이즈가 덜 된 자국**이 남는다"*, *"anima 기준 15초→9초인데 **품질도 많이 떨어진다**"*,
> *"2배 빨라져도 타율이 50% 안 나오면 그게 그거다"*, *"anima 는 아예 안 된다"*.

### ⚠ 실전 주의 셋

| | |
|---|---|
| ① | **TeaCache / EasyCache 같은 캐싱 방식과 같이 쓰면 안 된다.** 둘 다 스텝을 스킵하는 방식이라 하나가 동작을 안 하거나 결과가 이상해진다 |
| ② | **이미 고속화 세팅(증류 LoRA 등)을 쓰는 상태에 덧붙이면 열화가 심해진다** |
| ③ | **업스케일 단계에서 디노이즈가 특히 심해진다** — 업스케일은 원래 스텝 수가 적어 **예측에 쓸 스텝이 모자라거나 스킵이 과해지기** 때문이다. 업스케일 때는 **이 노드를 적용하지 않은 모델을 다시 불러오거나** 생성 때와 다른 설정을 쓴다 |

같은 원칙이 영상 쪽에도 그대로 적용된다 — **고속(터보) LoRA 를 쓸 때 EasyCache 를 같이 붙이면 안 된다**
→ [비디오 생성](video-generation.md)

RTX 30 계열은 **SageAttention 을 FP16 으로 컴파일**하라는 팁이 함께 나왔다.

### SPEED 노드 (2026-07 업데이트)

```
https://github.com/ruwwww/ComfyUI-SPEED
```

*Spectral Progressive Diffusion for Efficient Image and Video Generation* 의 비공식 구현(Anima 대상)이다.

| | |
|---|---|
| 변경 | **프리셋 방식으로 전환**됐다. 세팅을 다시 잡아야 하지만 적응하면 기존 SPEED 샘플러보다 편하다는 평. **알고리즘 자체는 그대로**다 |
| 추가 | 기존 DCT 외에 **DWT, FFT 변환** 지원 |
| ⚠ 설치 | **매니저에 등록되지 않아 수동 `git clone`** 이 필요하다 |
| 해당 없음 | **스펙트럼 샘플러(`SpectrumKSampler` 계열)로 기능을 쓰는 사람은 이 업데이트와 무관하다** |

→ [VRAM·속도 최적화](vram.md)

<small>근거 — [스팩트럼기반 최적화 노드 26.03](https://arca.live/b/aiart/165070655) · [SPEED 노드 업데이트 됐음. 26.07](https://arca.live/b/aiart/175612838)</small>

## AMD 에서 attention 고르기 — R9700 실측 (2026-06)
<small>2026-06 기준 · 근거 1건</small>

**AMD 로 Anima 를 돌리려는 사람에게 사실상 유일한 실측 자료다.** RX 9070XT 도 비슷할 것이라고 밝혀져 있다.

```text
환경: AMD 5700X3D / DDR4-3200 128GB / R9700 (PCIe 4.0x8, 260W)
      Ubuntu 26.04 / Python 3.14 / Torch 2.13.0a0+rocm7.13
      Anima 기본 워크플로 5회 생성, 아래는 2~5회 평균
```

| attention | torch.compile 없음 | 있음 |
|---|---|---|
| pytorch | 18.70초 | 14.70초 |
| **xformers** | **26.71초** | 22.34초 |
| sage attn | 16.74초 | 13.65초 |
| **flash attn** | 17.53초 | **13.36초** |

**xformers 가 최약체이고 flash attention 이 가장 빠르다.**
기본 워크플로 1장에 13초면 **RTX 3090 의 BF16 + sage + torch.compile 보다 조금 빠른 수준**이다.

### AMD 에서 정밀도 고르기

- **BF16 보다 FP16 이 빠르고 `--fast` 옵션이 효과가 있다** (nVidia 와 같다)
- ⚠ **FP8 은 BF16 보다 느렸고, INT8ROWWISE 는 10% 정도밖에 안 빨라졌다** —
  **AMD 에서는 양자화 모델의 실익이 nVidia 보다 훨씬 작다**

### 실행 옵션

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

--enable-triton-backend --use-flash-attention --supports-fp8-compute \
--fast fp16_accumulation fp8_matrix_mult
```

⚠ **`FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE` 가 없으면 flash-attn 은 아예 동작하지 않는다.**
윈도우에서는 `set FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE` 로 준다.

### VAE decode 에서 VRAM 이 치솟을 때

`1024x1536` 에서 **19GB 까지 올라 공유 메모리로 넘어가던 것이 위 두 환경변수를 설정하니 12.5GB 로 줄었다** *(댓글 확인)*.

### 설치 난이도

| | |
|---|---|
| **flash-attn** | whl 이 있어 간편. **다만 윈도우+ROCm 에서는 사실상 리눅스 전용이라 sage 백엔드를 쓰게 된다** |
| sage | `MAX_JOBS=8` 로 약 **10분** |
| **xformers** | **3시간 이상** (그러고도 가장 느리다) |

⚠ SpectrumSDXL 노드와의 충돌로 ComfyUI 가 닫히는 문제가 있었고 **노드 교체로 해결**됐다.

→ [설치와 환경 구성](install.md) · [오류 해결](troubleshooting.md)

<small>근거 — [AMD R9700 attention 별 생성속도 26.06](https://arca.live/b/aiart/173409804)</small>

## 영상 소스를 자동으로 만들기 — 반복문과 이미지 자동 리사이즈
<small>2025-11 기준 · 근거 2건</small>

### EasyUse 의 For / While 로 이미지를 누적시킨다

`ComfyUI-EasyUse` 의 **`For Loop Start` 와 `For Loop End` 사이에서 값을 누적**시키는 구조다.

```text
For Loop Start (initial_value1 = 빈 값)
  └ Batch Any (any_1 = 누적분, any_2 = 이번 사이클 이미지)
       └ I2V 가 이미지를 생성해 전달
  └ For Loop End (initial_value1 을 덮어씀) ──▶ 다시 For Loop Start
```

첫 사이클에서는 `any_1` 이 비어 있고, 다음 사이클부터는 **0번째 사이클 이미지가 `any_1` 에 저장돼 있다.**
**프롬프트 리스트 길이만큼 반복하면 마지막 사이클의 `value1` 이 이미지가 누적된 batch** 가 되고, 이것을 저장하거나 I2V 입력으로 쓴다.
While 도 동일하되 **bool 값을 잘 조절해야 한다.**

용도는 **start frame 과 end frame 을 뽑는 것**이고, 자가 발전하며 영상을 길게 이어 가는 응용도 고려됐다(보완책으로 고정 시드와 디노이징 검토).

> **이어 붙인 구간의 색감 틀어짐은 `color match` 커스텀 노드로 대응하는데 설정값에 이견이 있다** *(댓글)*.
>
> | 쪽 | 값 |
> |---|---|
> | A | `hm-mvgd-hm` · strength **1.0** — 그래도 문제가 남는다고 했다 |
> | B | `mkl` · strength **0.4** — **end frame 이 있는 상황에서는 굳이 strength 를 1까지 줄 필요가 없다** |
>
> 영상 접합 자체는 `WAN VACE Clip Joiner` 쪽이 더 낫다는 후속 보고가 있다 → [비디오 생성](video-generation.md)

K샘플러의 스텝은 I2V 서브 노드 **안에** 있다.

### 입력 이미지를 최대 픽셀 수로 자동 리사이즈 — `ResizeImageForWan`

**만든 이유가 원리를 설명해 준다.**

> **영상은 VRAM 사용량이 `이미지 너비 × 높이 × 프레임 수` 로 정해지기 때문에** 가로·세로를 따로 지정하는 방식이 불편하고,
> 각자 VRAM·모델 크기·블록스왑 유무에 따라 한계치가 다 다르다.

| | |
|---|---|
| 입력 | **`max_pixels` 하나뿐** (기본 `850000`) |
| 동작 | 원본 픽셀 수가 그보다 크면 **1%씩 줄여가며** 조건을 만족하는 배율을 찾고(못 찾으면 `√(max/original)`), **LANCZOS** 로 리사이즈한다 |
| **특징** | **`max_pixels` 이하면 아무것도 하지 않고 그대로 반환한다** — 기존 리사이즈 노드 중에는 **배율 1배로 리사이즈가 불필요한데도 변형이 일어나 품질이 떨어지는 것**이 있어서 이렇게 만들었다 |

설치는 `custom_nodes` 아래 폴더를 만들고 `ImageResizeForWan.py` 와 `__init__.py`(`NODE_CLASS_MAPPINGS` / `NODE_DISPLAY_NAME_MAPPINGS` 에 `ResizeImageForWan` 등록) 두 파일을 넣는다.
⚠ **GitHub 이 아니라 본문 복붙 배포라 이상한 문자가 섞일 수 있다.**

**실측 기준값** — VRAM 16GB, GGUF Q8 모델 + 블록스왑 40개로 **145프레임(16×9+1)을 돌릴 때 약 845,000 픽셀이면 OOM 이 나지 않는다.**
프레임 수를 고정해 쓰는 것이 보통이므로 **대충 값을 넣고 OOM 이 뜨면 줄이는 식**으로 잡으면 된다.
높은 해상도를 원하면 **블록스왑 40개를 무조건 권장**한다 *(댓글)* — 그래야 프레임과 이미지를 최대한 크게 가져간다.

→ [비디오 생성](video-generation.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [comfyUI, EasyUse의 반복문(for, while)… 25.11](https://arca.live/b/aiart/154218788) · [i2v 사용시 이미지 크기 자동조절기 25.10](https://arca.live/b/aiart/150416705)</small>

## 공식 템플릿과 새 모델을 붙일 때 — Anima 템플릿 갱신 · Krea2 reference
<small>2026-07 기준 · 근거 6건</small>

### ComfyUI 아니마 공식 템플릿 갱신 (2026-07-27)

| 변경 | 내용 |
|---|---|
| ① | **새 BASE 워크플로우에 터보 LoRA 가 기본 포함**되고 ComfyUI 기본 스위치 노드로 **온/오프**한다. 템플릿 하나로 일반 생성과 고속 생성을 오간다 |
| ② | **아니마 lllite**(경량 컨트롤넷 계열)가 정식 편입되며 **Canny · 인페인팅 · Depth** 체험용 템플릿이 추가됐다. Depth 템플릿은 공식 `DepthAnythingV3` 노드를 쓴다 |

이 컨트롤 워크플로우들도 BASE 와 마찬가지로 터보 온/오프가 된다.

> ⚠ **공식 템플릿은 자기네 공식 노드 위주로 짜여 있고, 그중 일부는 노드 2.0(신 노드 시스템)을 써야만 한다.
> 구버전 UI 를 쓰고 있다면 열리지 않을 수 있다.**

**속도가 필요하면 공식이 미는 길은 양자화가 아니라 터보 LoRA 다** — 무거운 모델에는 int8 convrot 사양을 주면서
아니마처럼 가벼운 모델에는 터보 LoRA 를 권장하는 방향으로 보인다. → 위 "양자화" 절

### 새 모델에 reference 를 붙이는 야매 — Krea2 (2026-06)

**Krea2 가 텍스트 인코더로 `qwen3VL`(비전 언어모델)을 쓴다는 점을 이용해,
이미지를 컨디셔닝에 직접 집어넣는 방식으로 reference 기능을 임시 구현한 것**이다(제작자 스스로 AI 에게 시켜 만든 야매라고 밝혔다).

```
https://drive.google.com/drive/folders/1JEOPf8dOEB6veeu98QFxZKbDUHdj1LWw
```

| | |
|---|---|
| 판 | **PCA** 와 **Direct** 두 개 — **PCA 쪽이 더 안정적** |
| 레퍼런스 이미지 | **최대 10장.** 더 넣으면 어떤 에러가 날지 모른다 |
| ⚠ 성질 | **style 만 가져오고 형태(생김새)는 가져오지 않는다** — 그림체 용도로 contents 를 일부러 배제했다 |
| 오해 주의 | **VLM 이 외형을 분석해 프롬프트를 만드는 게 아니라, vLLM 을 텍스트 인코더로 쓰면서 이미지 요소를 컨디셔닝에 직접 넣는 개념**이다 |

### Anima 와 Krea2 — 용도가 갈린다

| | Anima | Krea2 |
|---|---|---|
| 야짤의 하드코어·마이너 개념 | **여기서만 된다** | **개념 자체가 학습돼 있지 않다** |
| 서브컬처 작가 그림체 | **여기서만 된다** | 안 된다 |
| 복잡한 요구·명령 수행 | | **훨씬 위다** |
| 학습 난이도 | | **아주 낮다** — 증류 모델이면서 비증류 모델도 공개돼 있어 대충 학습해도 잘 나온다 |
| 사양 | **매우 가볍다** | 더 무겁다 (RTX 2070 으로 Anima 를 겨우 돌리는 수준이면 어렵다) |

두 모델을 이어 쓰는 **'Anima → Krea2' 워크플로우**도 공유돼 있다 — Anima 로 1차 생성하고 Krea2 로 마무리한다.
⚠ **프롬프트 입력란이 '아니마 전용' 과 '공용' 둘로 갈라져 있는 것이 특징**인데,
**Anima 는 `@작가` 골뱅이 표기와 퀄리티 태그 계통이 Krea2 와 달라 모델별 프롬프트를 분리해 둔 것**이다.
글쓴이 스스로 *'단순한 아이디어를 실행해 본 것'* 이라고 밝혔으므로 **정제된 국룰이 아니라 아이디어 참고용**으로 본다.
구체적인 스텝/CFG/디노이즈는 본문에 없고 워크플로우 파일 안에만 있으며, **이미지 호스팅이 만료되면 워크플로우도 같이 사라진다.**

### 곁가지 — ANIMA 관련 노드 둘

- **`ComfyUI-EasyUseAnima`** (`https://github.com/n0va39/ComfyUI-EasyUseAnima`) — LoRA 프리셋·스타일 프로필 저장/불러오기,
  프롬프트 작성기, **오타 수정과 ANIMA 문법(골뱅이 작가 태그) 자동 수정**. NAIA 에서 프롬프트를 바로 받아올 수도 있다.
  ⚠ 설치 직후 `Anima Prompt Studio Advanced` 노드에서 `Required input is missing: ...` 가 무더기로 뜨는 것은
  **제작자가 실수로 잘못 건드린 것이며 0.1.2 이상 또는 최신 커밋으로 업데이트하면 해결된다.**
  예시 워크플로우는 `docs/example_workflows` 에 있다
- **Anima Edit LoRA 원클릭 워크플로우** — 고속 LoRA 병합 모델 덕에 프롬프트를 바꾸지 않으면
  **두 번째 작업부터 리눅스 + RTX 4080 Super 16GB 에서 약 2초**. 권장 사양은 **VRAM 8GB / DRAM 16GB / 고속 SSD**.
  복잡한 포즈나 복잡한 의상에서는 잘 안 된다.
  > ⚠ **`abliterated` 처럼 '검열을 해제했다' 는 LLM 을 텍스트 인코더로 쓰면 문제가 생길 수 있다.**
  > **Anima 는 멀티모달 LLM 이 아니라 DiT 모델이라, LLM 의 검열 해제와 DiT 의 텍스트 인코더 사용은 성격이 다르다** — 채널에서 흔한 오해다

→ [ANIMA](anima.md) · [모델 고르기](models.md)

<small>근거 — [아니마 to Krea2 워크플로우 26.06](https://arca.live/b/aiart/175436884) · [초고속 원클릭 벗기기 아니마 워크플로우 26.05](https://arca.live/b/aiart/172310666) · [EasyUse Anima: ANIMA 프롬프트 보조 노드 베… 26.06](https://arca.live/b/aiart/174369324) · [Krea2 reference 노드(임시) + 테스트 lora 26.06](https://arca.live/b/aiart/174785012)</small>

??? note "근거 6건 전부 보기"
    [아니마 to Krea2 워크플로우 26.06](https://arca.live/b/aiart/175436884) · [초고속 원클릭 벗기기 아니마 워크플로우 26.05](https://arca.live/b/aiart/172310666) · [EasyUse Anima: ANIMA 프롬프트 보조 노드 베… 26.06](https://arca.live/b/aiart/174369324) · [Krea2 reference 노드(임시) + 테스트 lora 26.06](https://arca.live/b/aiart/174785012) · [ComfyUI 아니마 공식 워크플로우 템플릿 갱신 26.07](https://arca.live/b/aiart/178127727) · [Anima 기본워크플로 26.06](https://arca.live/b/aiart/173797432)

## 저장 파일명 포맷팅 — 날짜·해상도를 파일명에 자동으로 넣기
<small>2026-05 기준 · 근거 1건</small>

저장 노드의 **'파일명 접두사'** 칸은 그냥 이름이 아니라 **포맷팅 문법을 받는다.**
접두사를 그대로 두면 `ComfyUI_00001_`, `ComfyUI_00002_` 로 쌓이고 저장 위치는 `ComfyUI/output` 이다(접두사를 바꾸면 번호가 다시 1부터 시작한다).

| 하고 싶은 것 | 쓰는 법 |
|---|---|
| **하위 폴더** | 접두사에 `/` 를 넣으면 그 이름으로 폴더를 만들어 저장한다 |
| **날짜·시간** | `%date:FORMAT%` |
| **워크플로우의 값** | `%NODE.PARAMETER%` |

### 날짜 — `%date:FORMAT%`

지정자는 `yy`/`yyyy`(년) · `M`/`MM`(월) · `d`/`dd`(일) · `h`/`hh`(시) · `m`/`mm`(분) · `s`/`ss`(초) 이고,
한 글자와 두 글자의 차이는 **zero-padding 뿐**이다. 지정자 사이에 구분자를 넣어도 된다.

```text
%date:yyyyMMdd%     →  20260526
%date:yyyy_MM_dd%   →  2026_05_26
%date:yyyy-MM-dd%   →  2026-05-26
```

폴더명 자리에 쓰면 **날짜별로 자동 정리**된다.

### 노드 값 끌어오기 — `%NODE.PARAMETER%`

```text
ComfyUI_%EmptyLatentImage.width%x%EmptyLatentImage.height%
→ 해상도를 832x1216 으로 바꾸면 파일명도 따라 바뀐다
```

체크포인트명, KSampler 의 시드값 등 **워크플로우에 있는 값이면 무엇이든** 끌어올 수 있다.

### ⚠ 여기서 다들 걸린다 — 한국어로 번역된 노드는 영문 원문명을 써야 한다

**ComfyUI 의 기본 노드 이름은 한국어로 번역돼 표시된다.** 화면에 보이는 '빈 잠재 이미지' 를 그대로 적으면 인식되지 않는다.

| 화면에 보이는 이름 | 실제로 적어야 하는 것 |
|---|---|
| 빈 잠재 이미지 | `%EmptyLatentImage.width%` · `%EmptyLatentImage.height%` |
| 확산모델로드 | `%UNETLoader.unet_name%` |

**파라미터 이름도 마찬가지**로 영문 원문을 쓴다. 커스텀 노드는 보통 영어라 화면에 보이는 대로 써도 인식된다.

| 원문명 확인법 | |
|---|---|
| **노드 이름** | 노드를 클릭 → 우측 상단 아이콘 → **정보 탭** |
| **파라미터 이름** | 워크플로우 빈 공간을 더블클릭해 **노드 검색창**을 열고 노드명을 입력하면 파라미터 원문명이 보인다 |

⚠ **노드 이름을 직접 바꿨다면(노드 이름 더블클릭) 바꾼 이름으로 참조해야 한다** — `%UNETLoader.unet_name%` 도 이름을 `aaa` 로 바꾸면 `%aaa.unet_name%` 이 된다.

프롬프트 자체를 메타데이터로 남기는 것은 이 문서의 '뽑은 그림에 프롬프트를 남기는 법' 항목이다.

<small>근거 — [comfyui 이미지 저장노드 포맷팅 사용법 26.05](https://arca.live/b/aiart/171825322)</small>

## Qwen-Image-Edit 를 붙일 때 — 비율이 틀어지는 것부터 막는다
<small>2026-01 기준 · 근거 3건</small>

Qwen-Image-Edit 계열은 **말로 시켜서 고치는** 편집 모델이고, ComfyUI 에서 붙일 때 걸리는 지점이 정해져 있다.

### ⚠ 편집했더니 원본 비율이 틀어진다 (언줌) — 노드 연결 문제다

| | |
|---|---|
| 증상 | Qwen-Image-Edit-2511 이 편집하면서 **가로세로 비율을 멋대로 바꿔 버린다** |
| 원인 | **`TextEncodeQwenImageEditPlus` 가 내부에서 이미지를 리사이즈한다.** ComfyUI 소스 `comfy_extras/nodes_qwen.py` 를 보면 **384x384 기준**으로 맞추는 것으로 보인다 |
| **해결** | **`TextEncodeQwenImageEditPlus` 에는 VAE 를 연결하지 말고 비워 두고, latent 는 `ReferenceLatent` 노드로 따로 공급한다** |

(출처는 reddit `r/StableDiffusion` 의 `totally_fixed_the_qwenimageedit2509_unzooming` 글이다.)

### 없다고 뜨는 노드 셋 — 커스텀이 아니라 본체가 낡은 것이다

`ReferenceLatent` · `CFGNorm` · `TextEncodeQwenImageEditPlus` 가 빨갛게 뜨면 **매니저를 뒤질 것이 아니라 ComfyUI 본체를 최신으로 올린다.** 셋 다 **네이티브 노드**다.

### 실사용에서 나온 것들

| | |
|---|---|
| 프롬프트 언어 | **영어보다 한국어·중국어가 더 좋은 결과를 낼 때가 있다** |
| 결과가 **새까맣게** 나온다 | **SageAttention 충돌 / fp8 가속 충돌 / RTX 20 시리즈** 셋 중 하나 |
| 사양 | 최소 **VRAM 8GB / DRAM 32GB** + 가상메모리용 고속 SSD, 권장 **24GB / 64GB**. 4080 Super 16GB + 64GB 에서 두 번째 실행 이후 약 20초 |
| ⚠ 텍스트 인코더 | **`abliterated` 처럼 '검열을 풀었다' 는 LLM 을 텍스트 인코더로 쓰면 문제가 생길 수 있다.** 이건 멀티모달 LLM 이 아니라 **DiT** 라서 LLM 쪽 검열 해제와는 다른 얘기다 |
| 잘 하는 것 | 워터마크·UI·텍스트 제거, 물체 제거, 포즈 변경, 화질 개선, 캔버스 늘리기 |
| 못 하는 것 | 하드코어 NSFW, 이미지 안에 한국어 쓰기, 고해상도의 작은 글씨 |

### 시점(카메라 각도) 돌리기 — 명령문은 아주 단순하다

```text
Change it to the front view.
Rotate the camera <각도> degrees to the <방향>.
Change it to the back view.
```

**흐름** — `T2I → Qwen Image Edit(여러 각도로 계속 뽑기) → 스티치 → 디테일러`.
⚠ **마지막 디테일러를 T2I 와 같은 모델·같은 프롬프트로 돌리는 것이 요점**으로, Qwen Edit 이 만든 컷들의 화풍을 원래 그림 쪽으로 되돌려 준다.
삼면도·캐릭터 시트를 만들 때 응용할 수 있으나 일관성이 떨어질 수 있으니 여러 장 뽑아 고르는 편이 낫다.

### 곁들여 — 64배수로 자르기

`ImageScaleToTotalPixels` 에 `resolution_steps` 가 생겼지만 **크롭이 아니라 리사이즈로 처리해 이미지가 길어지거나 납작해진다.**
KJNodes 의 `Resize Image v2` 는 crop 은 되지만 픽셀 크기 맞춤이 없다.
넘치는 부분을 crop 하는 서브그래프를 직접 만들어 쓴다면 **megapixel 지정값을 0.01 정도 더 준다** — 해상도를 맞춘 뒤 자르기 때문에 **최악의 경우 63픽셀이 깎여 나간다.**

→ [인페인팅](inpainting.md) · [모델 고르기](models.md)

<small>근거 — [ComfyUI 뉴 원클릭 로컬 리터칭 V4A 워크플로우 26.01](https://arca.live/b/aiart/159742122) · [ComfyUI - Qwen Edit 25.11](https://arca.live/b/aiart/154401699) · [Qwen-Image-Edit-2511 원본 비율 유지하는 법 26.01](https://arca.live/b/aiart/160703142)</small>

## ⚠ DCW · CWM · SMC — 조용히 스킵되고 있던 조건들 (2026-05)
<small>2026-05 기준 · 근거 3건</small>

DCW 노드팩(`https://github.com/namemechan/ComfyUI-DCW`)은 **DCW · CWM · SMC 세 기능을 한 노드에 통합**해 두고 각각 켜고 끄는 구조다
(노드 검색에 `CWM`·`SMC` 가 따로 안 보이는 것이 정상이다).
2026년 5월, **이 셋이 특정 조건에서 아무 말 없이 스킵되고 있었다는 것이 밝혀져 연달아 고쳐졌다.**

### ⚠ 조용히 스킵되던 두 조건

| 언제 | 무엇이 | 고쳐진 날 |
|---|---|---|
| **디테일러 구간**, 그리고 **8의 배수이지만 2로 나누면 홀수가 되는 해상도**(예: **1208**) | **DCW** 보정이 적용되지 않았다 | 2026-05-02 |
| **스텝마다 해상도가 바뀌는 구성**(SPEED 노드 등) | **CWM · SMC** 보정이 적용되지 않았다 | 2026-05-22 |

첫 번째는 실행 중 이런 경고가 뜨는 것이 신호였다.

```
[DCW] Warning: correction skipped at this step – Padding size 4 is not supported for 5D input tensor.
```

**즉 그 전까지 디테일러 구간에서는 DCW 가 사실상 적용되지 않고 있었다**(댓글 표현으로 '디테일러 해골물').
수정 후 댓글에서 *"디테일러 돌려도 오류 안 뜨고 퀄이 확실히 좋아졌다"* 는 확인이 나왔다.
업데이트는 git 으로 하거나 **`dcw_node.py` 만 다시 받아 덮어써도** 된다.

> **KSampler 를 아예 분리해** 저해상도로 몇 스텝 돌리고 latent·이미지를 확대한 뒤 다음 KSampler 로 넘기는 방식은
> 모델 연결이 따로따로라 **원래 이 문제가 없었다.** DCW 기능 자체도 두 번째 버그와는 무관하다.

### 값 범위 — 음수가 열렸다

| 시점 | |
|---|---|
| 2026-05-02 | 제작자 답변: **"이 구현에서는 최소값이 0 으로 막혀 있다"** — 음수를 넣을 수 없었다 |
| **2026-05-03 (하루 뒤)** | **음수 허용.** `L`(저주파) **±0.5**, `H`(고주파) **±0.3** 까지 |

코드에서 숫자만 바꾸면 범위를 더 늘릴 수 있지만 **그 정도만 올려도 그림이 박살나므로 의미가 없다.**
무난한 기본값은 **L 0.01 / H 0.015** 이고, 제작자는 비교표(L ±0.1 을 0.05 단위 × H ±0.02 를 0.01 단위)에서 대충 고른 뒤 거기서 더 조절하라고 권한다.
**`ll lambda` 의 최적값은 이미지에 따라 다르고 CFG 에 따라서도 달라진다.**

원리는 **pixel space 가 아니라 wavelet domain correction 두 가지를 함께 쓰는 것**이다(논문 `arxiv.org/abs/2604.16044`, 원 구현 `github.com/AMAP-ML/DCW`. 범용성을 위해 일부는 유사 구현).

→ [디테일러](detailer.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [ComfyUI-DCW 노드업뎃 26.05](https://arca.live/b/aiart/169518554) · [ComfyUI-DCW 노드 음수지원업뎃 및 비교표 26.05](https://arca.live/b/aiart/169612897) · [dcw&cwm&smc 가변해상도버그수정 26.05](https://arca.live/b/aiart/171469275)</small>

## 이름을 봤을 때를 위해 — 2026 상반기에 더해진 자잘한 노드들
<small>2026-07 기준 · 근거 11건</small>

남의 워크플로우에서 **이름만 보고 정체를 알아야 하는** 것들이다. 대부분 한 글에서 소개된 도구이므로 필수는 아니다.

| 노드 · 도구 | 무엇 | 알아 둘 것 |
|---|---|---|
| `ComfyUI-WD-Timm-Tagger` | 이미지에서 단부루 태그를 뽑는 태거 | **dtype 을 `bf16`/`fp16` 으로 지정**하면 `vit-large`·`eva02`(1.1GB) 가 **VRAM 절반 · 속도 2배**가 되고 성능 저하는 크지 않다(기본 `auto`). exclude tags 는 **`white*` · `* shirt` 같은 glob** 을 받는다 |
| 태거 모델별 threshold | | `검열-tagger-v0.9` 는 최신 캐릭터가 되지만 오탐이 많아 **0.5 이상**(rating 태그 미지원), `Grio43/OppaiOracle` 은 기준 자체가 달라 **0.7 이상** |
| `Mask Fourier Smoothing` | 마스크 경계를 부드럽게 | 마스크를 **주파수 영역으로 옮겨 저역통과 필터**를 걸었다 되돌리는 Fourier Descriptor 방식. **SAM 계열 마스크가 지저분할 때** 인페인팅·합성 앞에 끼운다 (`github.com/bemoregt/ComfyUI_MaskSmoothing`) |
| `controlnet deep shrink patch` | Deep Shrink 와 컨트롤넷을 함께 | **기본적으로 둘은 호환되지 않는다.** 선행 노드 `ComfyUI_GradientDeepShrink` 의 **advanced 노드 전용**이라 일반 버전과 병용 금지 → [컨트롤넷](controlnet.md) |
| `Mask to Quad` + `Affine Transform` | 마스크 사각형에 다른 이미지를 **투시 변형해 합성** | SAM3 마스크 → 네 꼭짓점 좌표 → `warpPerspective`. ⚠ 폴더명을 **언더바(`ComfyUI_Affine_Transform`)** 로 바꿔야 인식되고 `affine_transform.py` 에 **`background` 입력 추가 · `rect_*` 를 FLOAT 로 · 출력 크기를 배경 크기로** 고쳐야 연결된다 |
| `ComfyUI-Cosmos-Reference` | 레퍼런스 이미지 참조 | ⚠ **강도 조절이 불가능하다.** 코드를 확인한 사용자에 따르면 **레퍼런스를 latent 에 concat 해 버리는 단순 구현**이라 그대로 박힌다 |
| `civitai_comfy_nodes` | CivitAI 공식 노드팩 | 모델 페이지의 **AIR 식별자**를 넣으면 그 모델을 찾아 준다(워크플로우 재현용). ⚠ **API 키를 노드에 그대로 박아 넣게 돼 있어** 공유 시 위험하고, 소개자 평가는 "이보다 나은 노드가 이미 많다" 였다 |
| `comfyui-custom-node-sig` | WebUI 의 prompt-all-in-one 을 옮긴 **태그 목록·자동완성** | 태그 데이터는 **`web/ko_KR.yaml`** 을 직접 고치고 **F5** 로 즉시 반영. ⚠ **작은 그룹 안에 같은 요소가 둘 이상이면 오류**가 나고, 특수문자 태그는 `"> o": '> o 표정'` 처럼 **따옴표로 감싼다**. 수정한 yaml 은 백업할 것 |
| `ImpactValueSender` / `ImpactValueReceiver` | **방금 뽑은 그림의 시드를 화면에 남긴다** | `link_id` 를 같은 값으로 맞춘다. `control_after_generate=fixed` 는 **'앞으로 뽑을'** 시드를 고정하는 것이고 이건 **'이미 지나간'** 시드를 보존하는 것이라 서로 다르다 (2023-09 기법이지만 지금도 통한다) |
| `GroundingDinoSAMSegment` | 2024년의 누끼 | prompt 칸에 대상 영어 단어(`human`·`bookshelf`·`sky`)를 적어 마스크를 뽑았다. 간단히 끝내려면 `ComfyUI-BRIA_AI-RMBG`. **지금은 SAM3·RMBG 계열이 대체했다** |
| `comfyui-mobile-frontend` | 폰용 UI | `http://<PC IP>:8188/mobile` → [설치와 환경 구성](install.md) |

### 워크플로우 하나 — 앞 2스텝만 CFG 를 주는 고속 구성 (2025-06)

와일드카드 → TIPO → T2I 로 끝나는 초고속 랜덤 짤 워크플로우에서 나온 세팅인데, 발상만 떼어 쓸 수 있다.

```text
6스텝 중 앞 2스텝만 CFG 2.5 / 나머지 4스텝은 CFG 1   (Scheduled CFG Guidance, KJNodes)
```

⚠ **스케줄러는 `sgm_uniform` 이나 `simple` 처럼 초반에 디노이즈를 많이 하는 것을 반드시 써야 한다** — 초반에만 CFG 를 주는 구조이기 때문이다.
속도는 RTX 5090 약 1초, RTX 3060 은 TIPO 포함 6초 / TIPO 없이 4초였다.

> ⚠ **저장 경로에 작가명을 넣는다면** — `2 \(Endou\)` 처럼 **괄호·백슬래시가 든 작가 태그에서 경로가 깨져 고장난다.**
> replace regex 류로 문제되는 문자를 전부 `_` 로 치환해야 한다(기본 세팅이 작가명에 백슬래시를 포함해 저장하게 돼 있었다).

→ [자원](resources.md) · [프롬프트 쓰는 법](prompting.md)

<small>근거 — [ComfyUI에서 이미지 누끼 따고, 그 안에 다른 이미지를… 26.03](https://arca.live/b/aiart/165751166) · [ComfyUI에서 누끼를 따보자 24.07](https://arca.live/b/aiart/111339977) · [커스텀노드) ComfyUI-WD-Timm-Tagger 업데이트 26.05](https://arca.live/b/aiart/170377879) · [(워크플로우 공모전) 겁나빠른 투닥뽑 25.06](https://arca.live/b/aiart/140754696)</small>

??? note "근거 11건 전부 보기"
    [ComfyUI에서 이미지 누끼 따고, 그 안에 다른 이미지를… 26.03](https://arca.live/b/aiart/165751166) · [ComfyUI에서 누끼를 따보자 24.07](https://arca.live/b/aiart/111339977) · [커스텀노드) ComfyUI-WD-Timm-Tagger 업데이트 26.05](https://arca.live/b/aiart/170377879) · [(워크플로우 공모전) 겁나빠른 투닥뽑 25.06](https://arca.live/b/aiart/140754696) · [(ComfyUI) 간단히 이전 그림 시드 보존하기 23.09](https://arca.live/b/aiart/87528398) · [(ComfyUI Custom Node) Mask Fourie… 26.02](https://arca.live/b/aiart/162468361) · [comfy 모바일 ui 확장 괜찮은거 하나 있네 26.02](https://arca.live/b/aiart/162164907) · [comfyui-cosmos-reference 26.06](https://arca.live/b/aiart/173603389) · [자작 컴피용 태그 가독성 커스텀노드 26.07](https://arca.live/b/aiart/177365104) · [civitAI에서 커스텀노드를 공개 26.06](https://arca.live/b/aiart/174070490) · [deep shrink 에 컨트롤넷이 호환되게 해주는 커스텀노드 26.02](https://arca.live/b/aiart/163330579)

## 프롬프트 입력 노드를 유형별로 쪼개기 — 그리고 해상도 노드를 갈아 끼울 때
<small>⚠️ 2025-06 기준 · 근거 1건</small>

2025-06 워크플로우 공모전 출품작(ILXL 계열 올인원)의 설계에서 **노드 배치보다 값어치 있는 발상**이 나왔다 (1건, 2025-06).

### 프롬프트 입력 노드를 유형별로 쪼갠다

한 칸에 다 넣지 않고 칸을 나눈 뒤 `Text Concatenation` 노드로 합쳐 KSampler 긍정 프롬에 넣는다.

```text
인물 수  /  그림체·스타일  /  배경  /  캐릭터·의상·포즈  /  앵글·효과  /  퀄리티 태그
                    → Text Concatenation → KSampler(positive)
```

**이 분리의 실익은 재조합이다** — 아웃페인팅에는 **인물 프롬만 빼고** 스타일·배경·앵글·퀄리티만 골라 넣을 수 있다.
멀티 캐릭터는 3인까지 지원하고 캐릭터별 LoRA 로드 노드를 따로 붙였다.

### ⚠ 해상도 노드를 갈아 끼울 때 걸리는 것

**SDXL 해상도 프리셋 노드는 기본값이 낮아 ILXL 의 '쌩으로 고해상도' 장점을 못 살린다.**
그런데 수동 해상도 노드로 바꾸면 **멀티 캐릭터 마스크 노드가 String 을 요구하는데 기존 노드는 Latent 만 출력해** 안 맞는다.

```text
해결  단순 텍스트 입력 노드  →  Latent 생성 노드의 해상도 값에 직접 연결
      마스크 노드가 요구하는 int 는  Math Expression 노드로 String → int 변환해 붙인다
```

### 나머지 구성

흐름은 체크포인트 로드 → 로라 스태커 → KSampler → aDetailer(얼굴·손) → HiresFix → **생성 날짜 폴더에 생성 시각 파일명으로 저장**이다.

- 모델은 `NAI-XL vpred1.0 2d accelerated - colorized`. **ILXL 모델은 대부분 VAE 내장이라 VAE 로더는 예비용.**
- aDetailer 모델은 `ultralytics/bbox` · `ultralytics/segm` 아래에 넣는다 → [디테일러](detailer.md).
- 컨트롤넷은 사진 기반과 포즈 직접 설정 두 개를 조건 결합 노드로 이어 두되 **스위치로 하나만 켜는 것을 권장**한다.
- HiresFix 는 그룹 노드로 병합했고, 왼쪽 구석 스위치와 북마크(1번 프롬·모델 설정, 2번 첫 생성 확인, z키 그룹 스위치)를 뒀다.

> ⚠ **본문의 워크플로우 공유 링크(kio.ac)는 이미 만료됐다고 댓글이 달려 있다.**
> **개선판이 `https://arca.live/b/aiart/141180724` 에 있으므로 그쪽을 받는다** → [자원](resources.md).


<small>근거 — [(워크플로우 공모전) 라면보다 쉽다! 생활 간단 워크플로우! 25.06](https://arca.live/b/aiart/140743677)</small>

## 로컬 LLM 프롬프트 노드 — Danbooru CSV를 직접 읽게 해서 가짜 태그를 막는다
<small>2026-08 기준 · 근거 1건</small>

로컬 LLM 자동프롬프트의 가장 큰 문제는 **존재하지 않는 태그를 그럴싸하게 꾸며내는 것**이다.

이걸 막는 우회가 있었다. LLM이 **Danbooru 태그 CSV를 직접 읽고 그 안의 태그만 쓰게 강제**하는 커스텀 노드다.

### 장점

- `aged`, `animation artstyle` 같은 **없는 태그 생성 억제**
- 와일드카드와 함께 사용 가능
- 사람이 `artist`·`quality` 같은 핵심 태그만 따로 적고, 나머지를 LLM에게 맡길 수 있다

### 전제

- 로컬 LLM(예: qwen 3.6 27b 계열) 필요
- CSV 데이터가 최신이어야 한다
- 자동 생성이라도 **최종 프롬프트를 사람이 한 번 훑는 습관**은 남겨 둬야 한다

핵심은 'LLM에게 자유롭게 쓰게 하는 것'이 아니라 **허용된 태그 목록 안에서만 조합하게 하는 것**이다.

<small>근거 — [로컬 llm으로 ILXL 뽑는 커스텀노드 + 이미지 워크플로우 26.08](https://arca.live/b/aiart/179817083)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 322개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 워크플로우는 EXIF 가 든 이미지·영상 파일을 다운로드해 ComfyUI 창에 드래그앤드롭해 불러온다 | 11 | 0 | 2024-06~2026-08 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| 긴 영상은 통짜로 만들면 타이밍과 두 번째 상황을 제대로 못 그리므로, 프롬프트를 나눠 이어붙이는 편이 낫다 | 6 | 0 | 2026-02~2026-08 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| 와일드카드는 언더바 두 개로 감싼 __파일명__ 형태로 호출하고, 하위 폴더에 있으면 __폴더/파일명__ 으로 적는다 | 6 | 0 | 2024-03~2026-07 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| WAN 2.2 계열 워크플로우는 High/Low 모델을 나눠 쓰고 lightx2v(라이트닝) 로라를 별도로 물리는 것이 표준 구성이다 | 5 | 0 | 2026-01~2026-04 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| 배포 워크플로우의 v-pred 스위치는 v-pred 모델이 아니면 반드시 꺼야 한다 — Eps 모델에 v-pred 를 켜 두면 정상 동작하지 않고, 결과가 흐리멍텅하면 V-PRED 모델이 맞는지부터 확인해 아니면 그 그룹을 바이패스한다 | 5 | 0 | 2025-06~2025-08 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |
| 모델이 diffusion model 단독으로 배포되면 models/checkpoints 가 아니라 models/diffusion_models 에 넣고 Load Diffusion Model 계열 노드로 불러야 하며, 텍스트 인코더와 VAE 도 각각 models/text_encoders, models/vae 에 따로 넣어 연결해야 한다 | 4 | 0 | 2026-05~2026-08 |
| ANIMA 는 자연어 이해력은 좋지만 화풍과 미학적 구도가 약해, ANIMA 로 구도를 잡고 Illustrious/SDXL 로 hires fix 해 화풍을 덮는 2단 구성이 쓰인다 | 4 | 0 | 2026-02~2026-04 |
| SDXL/Illustrious 결과물이 탁하거나 흰 점이 찍히면 VAE Select 값을 2로 두어 별도 VAE(fixFP16ErrorsSDXLLowerMemoryUse_v10)를 적용한다 | 4 | 0 | 2026-06~2026-08 |
| 아카라이브에 그림을 올릴 때 그냥 드래그하거나 붙여넣으면 아카 쪽에서 메타데이터가 날아가므로, 글쓰기 편집기 위쪽의 이미지 버튼을 눌러 **'EXIF 저장'(EXIF 보존) 체크박스를 켜고 그 창에서 업로드**해야 프롬프트·워크플로우가 보존된다 — 이미 EXIF 없이 올렸고 글 수정이 막혔다면 원본을 압축해 catbox 등에 올려 댓글로 링크하거나 EXIF 를 체크해 다시 올린 별도 글을 링크한다 | 4 | 0 | 2024-08~2025-08 |
| ComfyUI-EasyUseAnima 는 릴리스보다 main 브랜치에 수정이 먼저 올라가므로 git 으로 설치해야 인풋 소켓 누락 같은 버그가 고쳐진 판을 받는다 | 4 | 0 | 2026-06~2026-07 |
| MiniMax H3 가속은 MiniMaxH3 Cache(TeaCache 계열, 스텝 스킵이 아니라 계산 결과 재사용)가 EasyCache·Spectrum 보다 품질 손실이 적어 사실상 표준이다 | 4 | 0 | 2026-08~2026-08 |
| 설정 > Comfy > Nodes 2.0 > 모던 노드 디자인을 켜면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다 | 4 | 0 | 2026-05~2026-08 |
| ComfyUI 포터블에서 파이썬 패키지를 깔 때는 시스템 파이썬이 아니라 `python_embeded\python.exe -m pip` 로 설치해야 한다 | 4 | 0 | 2026-01~2026-08 |
| 통합팩은 ComfyUI 본체를 업데이트하지 말고 새 버전이 나오면 처음부터 새로 받아야 한다 | 4 | 0 | 2026-05~2026-08 |
| ANIMA 의 기본 shift 값은 3 이고(ComfyUI supported_models.py 에서 3.0 확인) shift 0 은 CFG·스텝 조합과 무관하게 공통적으로 검은 화면이 나오므로 쓰면 안 된다 | 3 | 0 | 2026-02~2026-06 |
| ComfyUI 통합팩은 한글이 없는 경로에 압축을 풀어야 한다 | 3 | 0 | 2026-02~2026-08 |
| 배포 워크플로우의 '인물' 칸은 1girl·1boy·2girls 처럼 **인원 수만** 적는 칸이고, 캐릭터·의상·외형·포즈는 전부 '캐릭터' 칸에 넣는다(모델이 인원 수를 맨 앞에 두기를 권해서 나눈 것) | 3 | 0 | 2025-06~2025-07 |
| 프롬프트 역추적은 어차피 추정이므로 근본 해법은 ComfyUI-Image-Saver(https://github.com/alexopus/ComfyUI-Image-Saver)로 프롬프트·모델·설정을 메타데이터에 제대로 심어 저장하는 것이다 — 뷰어 제작자 본인이 '복잡하게 추적하지 말고 그냥 image saver 를 쓰자' 고 결론지었다 | 3 | 0 | 2026-05~2026-07 |
| 디테일러·SAM 로더·컨트롤넷 모델을 Anything Everywhere 로 모아 연결해 둔 그룹은 절대 바이패스하면 안 된다 | 3 | 0 | 2025-07~2025-07 |
| 디테일러의 guide/max size 가 높게 잡혀 있어 VRAM 이 부족하면 각각 512 / 1024 로 낮추고, 손 디테일러와 업스케일은 이미지가 크게 달라질 필요가 없으므로 CFG 1 에 스텝 절반(12스텝)만 준다 | 3 | 0 | 2025-07~2025-07 |
| 포터블 구버전이 무조건 나쁜 것은 아니어서, 최신 버전에서 말썽을 부리는 노드가 있으면 구버전에서 작업하는 편이 나은 경우도 있다 | 3 | 0 | 2026-02~2026-08 |
| 커스텀 시그마(그래프 편집)로 노이즈 스케줄을 직접 조절하면 결과가 훨씬 역동적이 되지만 품질이 극적으로 좋아지지는 않는다 | 3 | 0 | 2026-03~2026-03 |
| VFI(프레임 보간) rife 모델은 ComfyUI/models/frame_interpolation 폴더에 넣어야 인식된다 | 3 | 0 | 2026-04~2026-08 |
| ComfyUI-EXIF-viewer(https://github.com/n0va39/ComfyUI-EXIF-viewer)는 설치 없이 exe 로 실행하는 png 메타데이터 뷰어로, 워크플로우에서 가장 처음 들어가는 샘플러를 기준으로 프롬프트를 역추적하고 Civitai 규격 메타데이터가 있으면 해당 모델·로라의 Civitai 페이지로 자동 연결해 주지만 모든 워크플로우에서 되지는 않는다 | 3 | 0 | 2026-06~2026-07 |
| SageAttention 을 켜는 방법은 두 가지다 — 실행 bat 에 `--use-sage-attention` 을 추가하거나, ComfyUI-KJNodes 의 'Patch Sage Attention KJ' 노드(sage_attention=auto, allow_compile=true)를 모델 선에 통과시킨다. 노드 방식은 켜고 끄기가 쉽다 | 3 | 0 | 2026-02~2026-05 |
| LTX2.3 distilled 8스텝은 cfg 1.0 으로 고정하고 시그마·스케줄러(linear_quadratic)로 품질을 조절한다 | 3 | 0 | 2026-03~2026-04 |
| ComfyUI 는 불특정 다수에게 서빙하라고 만든 프로그램이 아니라 보안이 사실상 없으므로 외부망 개방은 특히 주의해야 한다 | 3 | 0 | 2026-02~2026-05 |
| Spectrum Apply MiniMax H3 노드는 MiniMaxH3 Cache·EasyCache 와 함께 쓸 수 없다 | 3 | 0 | 2026-08~2026-08 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [쉽고 빠른 ComfyUI V9(ANIMA추가).](https://arca.live/b/aiart/166559591) — 2026-04, 추천 61
- [ComfyUI 뉴 원클릭 로컬 리터칭 V4A 워크플로우](https://arca.live/b/aiart/159742122) — 2026-01, 추천 59
- [초보자용 아니마 워크플로우 다섯종류](https://arca.live/b/aiart/170932870) — 2026-05, 추천 50
- [Comfyui portable v0.30.0 + sage 외 여러가지.](https://arca.live/b/aiart/178800540) — 2026-08, 추천 47
- [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.2 워크플로우](https://arca.live/b/aiart/160657113) — 2026-01, 추천 46
- [쉽고 빠른 ComfyUI V6 (FLUX 대응)](https://arca.live/b/aiart/116551406) — 2024-09, 추천 43
- [Comfy ANIMA 정보글 모음](https://arca.live/b/aiart/175397651) — 2026-06, 추천 43
- [ComfyUI - 산지직송 뉴비가 작성한, 하루만에 설치하고 짤뽑까지.](https://arca.live/b/aiart/163532702) — 2026-02, 추천 42
- [Comfyui portable v0.22.0 + sage + triton.](https://arca.live/b/aiart/171586136) — 2026-05, 추천 41
- [ComfyUI Portable 설치 쉽게 하는 툴 하나 소개함](https://arca.live/b/aiart/161826600) — 2026-02, 추천 40
- [ComfyUI에서 이미지 누끼 따고, 그 안에 다른 이미지를 리사이징해서 합성하는 워크플로우 공유](https://arca.live/b/aiart/165751166) — 2026-03, 추천 38
- [Comfyui portable v0.31.0 + sage 외 여러가지.](https://arca.live/b/aiart/179342860) — 2026-08, 추천 38
- [간단한 MinimaxH3 레퍼런스 I2V 워크플로우 공유](https://arca.live/b/aiart/179460713) — 2026-08, 추천 38
- [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법](https://arca.live/b/aiart/167528900) — 2026-04, 추천 35
- [comfy EXIF 뷰어 + 리소스 뷰어 + 자동 프롬프트 추적기](https://arca.live/b/aiart/173672742) — 2026-06, 추천 33
- [Comfyui portable v0.26.0 + sage 외 여러가지](https://arca.live/b/aiart/175163102) — 2026-06, 추천 32
- [Comfy UI 노드 추가중](https://arca.live/b/aiart/72115884) — 2023-03, 추천 31
- [comfyui) Anima 찍먹용 - anima+ill 워크플로우 (t2i , i2i, ollama 필요)](https://arca.live/b/aiart/162677789) — 2026-02, 추천 31
- [ANIMA All in One 워크플로우 v6.0: EasyUseAnima 안정버전, Anima-DAVE 추가, 디테일러 정상화](https://arca.live/b/aiart/175299629) — 2026-06, 추천 31
- [아니마 to Krea2 워크플로우](https://arca.live/b/aiart/175436884) — 2026-06, 추천 31
- [[ComfyUI] 복잡한 시그마를 초보자도 쉽게 요리해 보자.](https://arca.live/b/aiart/165103750) — 2026-03, 추천 30
- [초고속 원클릭 벗기기 아니마 워크플로우](https://arca.live/b/aiart/172310666) — 2026-05, 추천 29
- [(ComfyUI) Latent 영역 지정으로 프롬프트를 완전히 분리시켜 적용해보자](https://arca.live/b/aiart/86519619) — 2023-09, 추천 28
- [라면보다 쉽다! 간편 종합 워크플로우 v1.5](https://arca.live/b/aiart/143249780) — 2025-07, 추천 28
- [A10 GPU 쌀먹하는 방법](https://arca.live/b/aiart/169220758) — 2026-04, 추천 27
- [NAIA 및 아니마 사용을 위한 Webui Forge Neo 포지네오 설치 가이드 (수정)](https://arca.live/b/aiart/170554328) — 2026-05, 추천 26
- [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯](https://arca.live/b/aiart/178949797) — 2026-08, 추천 26
- [ComfyUI 뉴비의 초간단 regional 분리 방법(영역분리, 영역지정, Regional Prompt)](https://arca.live/b/aiart/145827191) — 2025-08, 추천 25
- [(수정) 아니마 b1 ollama 자동 프롬프트 테스트](https://arca.live/b/aiart/171660784) — 2026-05, 추천 25
- [ComfyUI 초보자를 위한 워크플로우 사용 가이드](https://arca.live/b/aiart/141704804) — 2025-07, 추천 24
- [Krea 2 Turbo/Edit용 네거티브 프롬프트 노드를 만들었습니다.](https://arca.live/b/aiart/179598126) — 2026-08, 추천 24
- [뉴비용) 나는 진짜 업스케일만 하고 싶어요](https://arca.live/b/aiart/163774464) — 2026-03, 추천 23
- [exif잇음)늒네식 워크플로우 공유](https://arca.live/b/aiart/175642035) — 2026-07, 추천 23
- [SCAIL-2 RV2V 편의성 패치 워크플로우](https://arca.live/b/aiart/173906280) — 2026-06, 추천 22
- [ComfyUI에서 누끼를 따보자](https://arca.live/b/aiart/111339977) — 2024-07, 추천 21
- [comfyui 개인제작노드(깃링크. P30.0기동확인)](https://arca.live/b/aiart/161492328) — 2026-02, 추천 21
- [로컬 comfyui 찍먹해보기 - sage-attention 설치](https://arca.live/b/aiart/162993309) — 2026-02, 추천 21
- [ComfyUI mxfp8 지원 (RTX5000시리즈)](https://arca.live/b/aiart/164899356) — 2026-03, 추천 21
- [EasyUse Anima: ANIMA 프롬프트 보조 노드 베타테스트 버전](https://arca.live/b/aiart/174369324) — 2026-06, 추천 21
- [(ComfyUI) 가장 기본적인 이미지 생성 워크플로우 가이드](https://arca.live/b/aiart/86110809) — 2023-09, 추천 20
- [(ConfyUI) Attention Couple (Regional Prompt) 영역 지정으로 프롬프트를 따로 적용해보자](https://arca.live/b/aiart/86441475) — 2023-09, 추천 20
- [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림체 랜덤 전환, SAM3 디테일러](https://arca.live/b/aiart/157410060) — 2025-12, 추천 20
- [[ComfyUI] 커스텀 시그마 마무리 (SDXL), 커스텀 노드 배포](https://arca.live/b/aiart/166267341) — 2026-03, 추천 20
- [ComfyUI 공식 int8convrot 양자화 도구](https://arca.live/b/aiart/175935647) — 2026-07, 추천 20
- [말풍선 노드 2.0버전](https://arca.live/b/aiart/176155066) — 2026-07, 추천 20
- [comfyUI, EasyUse의 반복문(for, while)을 써보자](https://arca.live/b/aiart/154218788) — 2025-11, 추천 19
- [ComfyUI-DCW 노드업뎃](https://arca.live/b/aiart/169518554) — 2026-05, 추천 19
- [ilxl 자작 리저널+오픈포즈 노드](https://arca.live/b/aiart/171224457) — 2026-05, 추천 19
- [프롬프트 매니저](https://arca.live/b/aiart/172333335) — 2026-05, 추천 19
- [comfyui anima 고속 + mod guidance 노드 SEA 업데이트](https://arca.live/b/aiart/174577922) — 2026-06, 추천 19
- [ComfyUI INT8 공식 지원+가속 지원](https://arca.live/b/aiart/174942443) — 2026-06, 추천 19
- [ComfyUI 딸깍플로우 V1.1로 업데이트 했음](https://arca.live/b/aiart/127946352) — 2025-02, 추천 18
- [comfyui portable v0.11.1 + sage + triton.](https://arca.live/b/aiart/161206430) — 2026-02, 추천 18
- [[ComfyUI] LTX-2.3 커스텀 시그마로 영상과 음질을 개선해 보자.](https://arca.live/b/aiart/165196910) — 2026-03, 추천 18
- [ComfyUI SAM3 / RIFE 자체 지원 노드 추가](https://arca.live/b/aiart/168617494) — 2026-04, 추천 18
- [[ComfyUI 대회] 뉴비의 ComfyUI 후기 (약후방)](https://arca.live/b/aiart/112476411) — 2024-07, 추천 17
- [쉽고 빠른 ComfyUI V6 마이너 업데이트](https://arca.live/b/aiart/122761449) — 2024-12, 추천 17
- [[워크플로우 공모전] 라면보단 어렵더라! 3트째 간편 워크플로우! (로라, 노드 수정 버전) (최종최종진최종 (1)) + 가이드](https://arca.live/b/aiart/141180724) — 2025-07, 추천 17
- [계층적 와일드카드 만들었음.](https://arca.live/b/aiart/142805267) — 2025-07, 추천 17
- [프롬프팅을 편하게 해주는 ComfyUI-ZImagePowerNodes](https://arca.live/b/aiart/160992548) — 2026-01, 추천 17
- [스팩트럼기반 최적화 노드](https://arca.live/b/aiart/165070655) — 2026-03, 추천 17
- [[커스텀노드] ComfyUI-PreviewMonitor: 프리뷰 몰아보기 노드](https://arca.live/b/aiart/171041315) — 2026-05, 추천 17
- [comfyui 이미지 저장노드 포맷팅 사용법](https://arca.live/b/aiart/171825322) — 2026-05, 추천 17
- [태그뷰어+분류기+컴피이미지메모추가노드 종합 업뎃](https://arca.live/b/aiart/169783666) — 2026-05, 추천 16
- [컴피 공홈에서 포터블 버전 받는 방법.](https://arca.live/b/aiart/170235453) — 2026-05, 추천 16
- [빡통워크 5.0 : 배치 로더 자동화 랜덤그림체 짤뽑](https://arca.live/b/aiart/143059270) — 2025-07, 추천 15
- [[ComfyUI] 그림체 테스트 워크플로우 + 그림체 공유 (260103 Update)](https://arca.live/b/aiart/157943050) — 2025-12, 추천 15
- [조건부 프롬프트 추가 커스텀 노드 만듦](https://arca.live/b/aiart/165692820) — 2026-03, 추천 15
- [Anima+IL 아님. IL+Anima임.](https://arca.live/b/aiart/171656386) — 2026-05, 추천 15
- [DCW노드 새로운해골물 RDC추가](https://arca.live/b/aiart/178277612) — 2026-07, 추천 15
- [ComfyUI에서 EXIF에 NAI처럼 프롬프트 남기는 방법](https://arca.live/b/aiart/169763428) — 2026-05, 추천 14
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [[워크플로우 공모전] 겁나빠른 투닥뽑](https://arca.live/b/aiart/140754696) — 2025-06, 추천 13
- [ComfyUI-WD-Timm-Tagger 커스텀 노드](https://arca.live/b/aiart/169517277) — 2026-05, 추천 13
- [커스텀노드) ComfyUI-WD-Timm-Tagger 업데이트](https://arca.live/b/aiart/170377879) — 2026-05, 추천 13
- [WAN2.2 SVI 결과에 음성 추가용 WAN2.2 (SVI) + LTX Worfkflow](https://arca.live/b/aiart/173733176) — 2026-06, 추천 13
- [(ComfyUI) 간단히 이전 그림 시드 보존하기](https://arca.live/b/aiart/87528398) — 2023-09, 추천 12
- [[워크플로우 공모전] 라면보다 쉽다! 생활 간단 워크플로우!](https://arca.live/b/aiart/140743677) — 2025-06, 추천 12
- [[워크플로] LTX2.3 Distilled Simple + 생성속도 간단 테스트](https://arca.live/b/aiart/164232718) — 2026-03, 추천 12
- [ComfyUI-DCW 노드 음수지원업뎃 및 비교표](https://arca.live/b/aiart/169612897) — 2026-05, 추천 12
- [모바일 Comfy 구동 프론트 Web App](https://arca.live/b/aiart/170363616) — 2026-05, 추천 12
- [RTX 20 시리즈를 사용하는데 아니마는 써보고 싶은 사람들을 위한 작은 ComfyUI 팁.](https://arca.live/b/aiart/170741530) — 2026-05, 추천 12
- [comfyui Skimmed_CFG 노드 (스압)](https://arca.live/b/aiart/171375569) — 2026-05, 추천 12
- [comfyui-cns_sampler_patch](https://arca.live/b/aiart/172367736) — 2026-05, 추천 12
- [쉽고 빠른 ComfyUI V7 - 순차적 와일드 카드 업뎃](https://arca.live/b/aiart/128282786) — 2025-02, 추천 10
- [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유](https://arca.live/b/aiart/179083162) — 2026-08, 추천 10
- [[워크플로우 공모전] 라면보다 쉽다! 생활 간단 워크플로우! (노드 배치 개선 버전)](https://arca.live/b/aiart/140945356) — 2025-06, 추천 9
- [ComfyUI 추천 VLM 노드, 프롬프트, 모델 (장문)](https://arca.live/b/aiart/160879401) — 2026-01, 추천 9
- [로컬 comfyui 찍먹해보기 - 리저널 프롬프트 응용](https://arca.live/b/aiart/161706938) — 2026-02, 추천 9
- [챈산 리저널 노드를 활용한 ilxl용 워크플로우.](https://arca.live/b/aiart/171276717) — 2026-05, 추천 9
- [AMD R9700 attention 별 생성속도](https://arca.live/b/aiart/173409804) — 2026-06, 추천 9
- [Krea2 reference 노드(임시) + 테스트 lora](https://arca.live/b/aiart/174785012) — 2026-06, 추천 9
- [간단한 미니맥스(MiniMax) 워크플로우 공유](https://arca.live/b/aiart/178942263) — 2026-08, 추천 9
- [4.5 챈에 쓰는 ComfyUI 빡통 워크플로우 4.0](https://arca.live/b/aiart/139311613) — 2025-06, 추천 8
- [[워크플로우 공모전] 라면 어쩌고 저쩌고 실전압축 워크플로우 (完)](https://arca.live/b/aiart/141718826) — 2025-07, 추천 8
- [[워크플로우 공모전] 굿나잇 랜덤 워크플로우 v1.8](https://arca.live/b/aiart/142849197) — 2025-07, 추천 8
- [2주차 뉴비의 comfyUI 워크플로우 공유](https://arca.live/b/aiart/145850172) — 2025-08, 추천 8
- [빡통워크 5.1 자동 랜덤그림체 + 업스케일](https://arca.live/b/aiart/146574747) — 2025-08, 추천 8
- [[ComfyUI Custom Node] Mask Fourier Smoothing](https://arca.live/b/aiart/162468361) — 2026-02, 추천 8
- [ComfyUI-basic_data_handling 커스텀노드 소개](https://arca.live/b/aiart/162937578) — 2026-02, 추천 8
- [ComfyUI 버전 여러개 쓰기: UV와 ComfyCLI 기반, 포터블도 가능](https://arca.live/b/aiart/172936836) — 2026-06, 추천 8
- [로컬 llm으로 ILXL 뽑는 커스텀노드 + 이미지 워크플로우](https://arca.live/b/aiart/179817083) — 2026-08, 추천 8
- [아주 선명한 ComradeshipXL v14KC용 ComfyUI 워크플로우](https://arca.live/b/aiart/136415303) — 2025-05, 추천 7
- [ComfyUI - Qwen Edit](https://arca.live/b/aiart/154401699) — 2025-11, 추천 7
- [또 업뎃한 프롬프트 분류기](https://arca.live/b/aiart/154827249) — 2025-11, 추천 7
- [Qwen-Image-Edit-2511 원본 비율 유지하는 법](https://arca.live/b/aiart/160703142) — 2026-01, 추천 7
- [comfy 모바일 ui 확장 괜찮은거 하나 있네](https://arca.live/b/aiart/162164907) — 2026-02, 추천 7
- [임베딩 노드 버전업(P30까지 호환)](https://arca.live/b/aiart/163973039) — 2026-03, 추천 7
- [ComfyUI exif에서 프롬프트 정보 찾아 뜯어보다 알게된거](https://arca.live/b/aiart/169744100) — 2026-05, 추천 7
- [comfyui Starnodes 양자화 노드](https://arca.live/b/aiart/176070719) — 2026-07, 추천 7
- [comfy-EXIF 뷰어 v0.1.3: 프롬프트 추적기능 향상](https://arca.live/b/aiart/176893071) — 2026-07, 추천 7
- [comfyui 프롬에서<로라:1>로 불러오는 노드 TIL](https://arca.live/b/aiart/179076765) — 2026-08, 추천 7
- [내가 쓰고있는 ComfyUI 워크플로우 공유 (SDXL, Anima)](https://arca.live/b/aiart/179640921) — 2026-08, 추천 7
- [[ComfyUI 대회] 뉴비입장에서 적어보는 찐뉴비용 Comfy 팁 (약스압)](https://arca.live/b/aiart/112644586) — 2024-07, 추천 6
- [[워크플로우 공모전] 굿나잇 랜덤 워크플로우](https://arca.live/b/aiart/141848057) — 2025-07, 추천 6
- [[워크플로우 공모전] 라면보다 쉽다! 간편 종합 워크플로우 - 종합 개선 업데이트 1.4 버전](https://arca.live/b/aiart/141991828) — 2025-07, 추천 6
- [[워크플로우 공모전] 굿나잇 랜덤 워크플로우 v1.5](https://arca.live/b/aiart/142088366) — 2025-07, 추천 6
- [코랩에서 원하는 워크플로우를 파이썬 코드로 변환해보자 (WAN 2.2, FLUX)](https://arca.live/b/aiart/146658219) — 2025-08, 추천 6
- [i2v 사용시 이미지 크기 자동조절기](https://arca.live/b/aiart/150416705) — 2025-10, 추천 6
- [ComfyUI - 맘에 드는 워크플로우 찾기](https://arca.live/b/aiart/160610621) — 2026-01, 추천 6
- [[ComfyUI] Attention Couple 리저널 2인 수정본](https://arca.live/b/aiart/163287880) — 2026-02, 추천 6
- [Comfy CLI 설치 방법 정리](https://arca.live/b/aiart/169751935) — 2026-05, 추천 6
- [nai+로컬 태그뷰어 업뎃](https://arca.live/b/aiart/170775337) — 2026-05, 추천 6
- [comfyui-cosmos-reference](https://arca.live/b/aiart/173603389) — 2026-06, 추천 6
- [Anima 기본워크플로](https://arca.live/b/aiart/173797432) — 2026-06, 추천 6
- [컴피 와일드카드 노드 순차모드 추가. 업데이트](https://arca.live/b/aiart/174214832) — 2026-06, 추천 6
- [ComfyUI 아니마 공식 워크플로우 템플릿 갱신](https://arca.live/b/aiart/178127727) — 2026-07, 추천 6
- [ComfyUI-FrequencyCorrectedNoise 노드](https://arca.live/b/aiart/178611005) — 2026-07, 추천 6
- [comfyui 쓸만한 프리셋 노드](https://arca.live/b/aiart/126197785) — 2025-01, 추천 5
- [NoobAI-ILXL 병합 플롯](https://arca.live/b/aiart/134064704) — 2025-04, 추천 5
- [ComfyUI If문 적용 Prompt](https://arca.live/b/aiart/153389527) — 2025-11, 추천 5
- [pytorch 2.10 +  python 3.13 + RTX5000대 기준 패키지 설치법](https://arca.live/b/aiart/160668279) — 2026-01, 추천 5
- [[anima] Attention Couple 리저널 워크플로우 2종.](https://arca.live/b/aiart/169319019) — 2026-04, 추천 5
- [dcw&cwm&smc 가변해상도버그수정](https://arca.live/b/aiart/171469275) — 2026-05, 추천 5
- [LatentSpectralExpand 노드 (아니마 Speed 노드 실험용)](https://arca.live/b/aiart/171519242) — 2026-05, 추천 5
- [comfyui 앱모드 사용법](https://arca.live/b/aiart/171528258) — 2026-05, 추천 5
- [SPEED 노드 업데이트 됐음.](https://arca.live/b/aiart/175612838) — 2026-07, 추천 5
- [[미쿠미쿠 대회] 미쿠짤 뽑으려고 ai그림 시작했던 뉴비](https://arca.live/b/aiart/114468193) — 2024-08, 추천 4
- [[워크플로우 공모전] T2I특화 모듈형 프롬프트 워크플로우](https://arca.live/b/aiart/142197182) — 2025-07, 추천 4
- [ComfyUI - 와일드카드](https://arca.live/b/aiart/153827221) — 2025-11, 추천 4
- [미세팁) ComfyUI 사이드바에서 Template 버튼 제거하기](https://arca.live/b/aiart/164602009) — 2026-03, 추천 4
- [튜링용 flash-attention](https://arca.live/b/aiart/176657130) — 2026-07, 추천 4
- [자작 컴피용 태그 가독성 커스텀노드](https://arca.live/b/aiart/177365104) — 2026-07, 추천 4
- [WAI17(일러스트리어스) T2I 픽셀 아트 생성 워크플로우 공유](https://arca.live/b/aiart/179639518) — 2026-08, 추천 4
- [KSampler 프리뷰 해상도 수정해주는 커스텀 노드 ComfyUI-bleh](https://arca.live/b/aiart/161467109) — 2026-02, 추천 3
- [comfyui 포터블 이사가는거 도와주는 스크립트](https://arca.live/b/aiart/162198611) — 2026-02, 추천 3
- ['갑자기' comfy 에서 sage-attension 실패하는 이슈 해결 (자동 업데이트)](https://arca.live/b/aiart/163926460) — 2026-03, 추천 3
- [로라매니저식 프롬프트 매니저-fix](https://arca.live/b/aiart/171714325) — 2026-05, 추천 3
- [컴피 와일드카드 노드 업데이트](https://arca.live/b/aiart/175224738) — 2026-06, 추천 3
- [WAI17(일러스트리어스) I2I 픽셀 아트화 워크플로우 공유](https://arca.live/b/aiart/179639075) — 2026-08, 추천 3
- [ComfyUI - 다양한 워크플로우를 써 본 소감과 활용방법.](https://arca.live/b/aiart/160605007) — 2026-01, 추천 2
- [deep shrink 에 컨트롤넷이 호환되게 해주는 커스텀노드](https://arca.live/b/aiart/163330579) — 2026-02, 추천 2
- [Comfy의 기본 메뉴에 jpg를 추가하는 커스텀 노드.](https://arca.live/b/aiart/171262767) — 2026-05, 추천 2
- [civitAI에서 커스텀노드를 공개](https://arca.live/b/aiart/174070490) — 2026-06, 추천 2
- [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유](https://arca.live/b/aiart/179637421) — 2026-08, 추천 2
- [ComfyUI 매니저 Legacy UI 대체 커스텀 노드](https://arca.live/b/aiart/179523894) — 2026-08, 추천 1
- [ComfyUI - 와일드카드 복습](https://arca.live/b/aiart/155383963) — 2025-11, 추천 0
- [뉴비의 간단한 워크 플로우](https://arca.live/b/aiart/161471075) — 2026-02, 추천 0
- [컴피 질문이 있습니다](https://arca.live/b/aiart/170967423) — 2026-05, 추천 0
- [NAIA로 Comfy + 아니마를 써보려는데 사용법을 잘 모르겠음 ㅜㅜ](https://arca.live/b/aiart/173906125) — 2026-06, 추천 0
