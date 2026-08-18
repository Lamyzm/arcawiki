# 처음이라면 — 전체 지도

> **원문 28건 → 이 문서 하나** · 주장 124개 · 정리 2026-08-14

아무것도 모르는 상태에서 **내 손으로 그림 한 장을 뽑는 데까지** 가는 지도다.
읽는 순서는 정해져 있다 — 먼저 **길이 두 갈래**라는 것을 알고(웹서비스 / 내 컴퓨터), 다음에 **내 그래픽카드로 되는지**를 확인하고, 그 다음에 [설치와 환경 구성](install.md)으로 간다.
모르는 낱말이 나오면 [용어집](glossary.md)을 옆에 띄워 두면 된다.

## ① 길은 두 갈래다 — 웹서비스로 뽑기 vs 내 컴퓨터에 깔기
<small>2026-07 기준 · 근거 5건</small>

AI 그림을 뽑는 방법은 크게 둘이다. **어느 쪽이 맞는지는 그래픽카드가 정한다.**

| | **웹서비스로 뽑기** (NovelAI 등) | **내 컴퓨터에 깔기** (로컬) |
|---|---|---|
| 필요한 것 | 인터넷과 결제 수단 | NVIDIA 그래픽카드, 디스크 여유, 설치 시간 |
| 돈 | NAI Opus 구독 **월 3만원대** (기본 해상도 무제한) | 전기값 + 그래픽카드 값 |
| 시작까지 | 결제하고 바로 | 파이썬·git 설치 → 클론 → 모델 다운로드 |
| 뭘 못 하나 | 모델·로라·확장을 내 마음대로 못 바꾼다 | 없음 (대신 전부 직접 해야 한다) |
| 막혔을 때 | 서비스가 정해 준 대로 | 채널에 물어볼 수 있다 (단 [국룰](kukroul.md) 먼저) |

**웹서비스를 권하는 경우가 분명히 있다.** 원문 109424774 는 이렇게 못박는다 —
AMD Radeon·Intel Arc 에 대해 2024-06 자료는 **"사용자가 적어 문제가 생겨도 답을 못 얻으니 NAI Opus 를 쓰라"** 고 했다. 지금은 길이 생겼지만(③번 표) **여전히 손이 많이 가고 막혔을 때 물어볼 곳이 적다.**
GTX 1060 3GB 나 RTX 2050 노트북도 되기는 하지만 그 고생과 전기값을 생각하면 Opus 가 낫고, RTX 4090 이면 그냥 로컬을 설치하면 된다.

VRAM 이 부족하면 생성 도중 메모리 부족으로 프로그램이 그냥 꺼진다(원문 68686905). 그래서 다음 항목의 표를 먼저 봐야 한다.

**그래서 나는 어느 쪽인가** — 채널의 뉴비 순서도(원문 177192496, 2026-07)를 그대로 옮긴 것이다.

| 내 상황 | 가는 곳 |
|---|---|
| 월 25달러를 낼 의사가 있다 | **NAI Opus** — 일반 옵션은 사실상 무제한 |
| 지포스 **RTX 30 시리즈 이상** | 로컬 (권장 구간) |
| 지포스 **RTX 20 시리즈** | 로컬은 되지만 일부 모델이 안 된다. INT8 이면 쓸 만하다 |
| **GTX 16 시리즈** | 포기 권장. 다만 INT8 에서 쓸 만하다는 보고가 있다 |
| **GTX 10 시리즈 이하** | 포기 |
| **RX 7000 이상** / 노트북 RDNA 3 이상 / **Arc A 시리즈 이상** | [Comfy-Org 윈도우 포터블](https://github.com/Comfy-Org/ComfyUI#windows-portable) |
| 애플 M4 등 NPU 가 넉넉한 기기 | 마지막 선택지로 열려 있다 |

**여기서 놓치면 안 되는 것** — 이 순서도가 NAI 를 앞에 둔 이유는 **성능이 아니라 입문 난이도**다.
작성자는 댓글에서 *PC 사양이 충분해도 로컬이 NAI 보다 어렵다*고 못박는다.
RTX 5090 을 가진 사람들조차 **그래픽카드 수명·집안 온도·생성 중 게임 불가·설치 번거로움** 때문에 NAI 를 좋은 선택지로 본다.
즉 위 표는 "되느냐" 를 가르는 것이지 "무엇이 편하냐" 를 가르는 것이 아니다.

Opus 는 월 25달러이고, **과다 생성·계정 공유·노골적 자동화는 403 영구 제한 사유**다.

→ 웹서비스 쪽은 [NovelAI](nai.md), 로컬 쪽은 [설치와 환경 구성](install.md).

<small>근거 — [~무지성부터 활용까지~ NAI 사용법을 떠먹어보자 23.11](https://arca.live/b/aiart/92677065) · [야한 그림을 뽑고 싶은 뉴비를 위한 초간단 가이드 26.07](https://arca.live/b/aiart/177192496) · [(가이드)아무것도 몰라도 10분내로 이해하는 기초 단어 가이드 23.01](https://arca.live/b/aiart/68686905) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774)</small>

??? note "근거 5건 전부 보기"
    [~무지성부터 활용까지~ NAI 사용법을 떠먹어보자 23.11](https://arca.live/b/aiart/92677065) · [야한 그림을 뽑고 싶은 뉴비를 위한 초간단 가이드 26.07](https://arca.live/b/aiart/177192496) · [(가이드)아무것도 몰라도 10분내로 이해하는 기초 단어 가이드 23.01](https://arca.live/b/aiart/68686905) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774) · [크퀘스타일 도트 로라 공유 26.04](https://arca.live/b/aiart/167362821)

## ② 플랫폼 비교표 — 뭘 골라야 하나
<small>2026-08 기준 · 근거 12건</small>

지금 채널에서 실제로 쓰이는 다섯 갈래다.

| | 돈 | 사양 | 잘하는 것 | 입문 난이도 |
|---|---|---|---|---|
| **NovelAI (NAI)** | Opus 월 3만원대 / 비구독은 10,000 Anlas 13.99$ (장당 약 30 Anlas) | 없음 (웹) | 설치 없이 바로. 그래픽카드가 없는 사람의 답이고, 라데온·Arc 는 되지만 손이 많이 간다(③번 표) | 가장 쉬움 |
| **WebUI Forge Neo** | 무료 | NVIDIA. VRAM 은 ComfyUI 보다 약간 덜 먹는다는 체감 보고(7.8GB 수준) | ANIMA 를 칸에 값 넣는 방식으로 돌리기. 뉴비에게 권장되는 로컬 | 중 (명령어 몇 줄) |
| **ComfyUI** (포터블 통합팩) | 무료 | 지포스 3000~5000번대 권장, sage attention 을 끄면 2000번대도 동작 | 워크플로우로 못 하는 게 없음. 영상·업스케일·인페인팅 전부 | 어려움 — 단 **App Mode** 로 위젯만 보이게 하면 WebUI 처럼 쓸 수 있다 |
| **ANIMA** (모델) | 무료 | INT8 판은 모델+텍스트인코더+VAE 합쳐 4GB 미만이라 VRAM 8GB 급도 무난 | 2026년 채널의 기본 아니메 모델. 자연어를 알아듣는다 | Forge Neo·ComfyUI 위에 얹어 씀 |
| **MiniMax H3** (영상) | 로컬 무료 / API 는 출력 1초당 $0.13 | RTX 3060 12GB + RAM 32GB 급에서도 구동 (832x480 124프레임 10분 미만) | 영상. 오픈웨이트 중 최상위권(아레나 1185점) | 어려움 — ComfyUI 필수 |

**고르는 기준 한 줄.**
- 그래픽카드가 없다 → **NAI**
- 라데온·Arc → **NAI 가 편하다.** 로컬을 고집한다면 ③번 표의 조건을 먼저 확인한다
- NVIDIA 가 있고 그림만 뽑고 싶다 → **Forge Neo + ANIMA**
- 영상·업스케일·인페인팅까지 하고 싶다 → **ComfyUI 통합팩**

원문 176802949 는 "뉴비들은 webui neo 쓰자" 를 제목으로 걸고, 생성 속도는 ComfyUI 와 별 차이 없으면서 확장 하나로 태그 추가·가중치 조절·자동번역을 딸깍으로 쓸 수 있다고 한다. 설치가 어려우면 StabilityMatrix 로 딸깍하라고도 적혀 있다.
2024년 10월판 reForge 도 같은 A1111 계열이지만, 작성자 본인이 모델을 바꿀 때마다 렉이 심해 결국 자기는 안 쓴다고 밝혔다.

→ [ComfyUI 쓰는 법](comfyui.md) · [ANIMA](anima.md) · [MiniMax H3](minimax-h3.md) · [모델 고르기](models.md)

<small>근거 — [~무지성부터 활용까지~ NAI 사용법을 떠먹어보자 23.11](https://arca.live/b/aiart/92677065) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774)</small>

??? note "근거 12건 전부 보기"
    [~무지성부터 활용까지~ NAI 사용법을 떠먹어보자 23.11](https://arca.live/b/aiart/92677065) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774) · [ComfyUI App mode가 나왔길래 써봤다. 26.03](https://arca.live/b/aiart/164519826) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089) · [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능) 24.10](https://arca.live/b/aiart/119210516) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부… 26.08](https://arca.live/b/aiart/178717529) · [Gemini Omni Flash vs Minimax-H3 26.08](https://arca.live/b/aiart/178630221)

## ③ 내 그래픽카드로 되나 — 실측표
<small>2026-08 기준 · 근거 12건</small>

채널에 실제로 올라온 숫자만 모은 것이다. **조건이 제각각이니 절대값이 아니라 등급으로 읽어야 한다.**

| 그래픽카드 | 결과 | 조건 |
|---|---|---|
| GTX 1060 | 되기는 하나 느리다 | SDXL/Illustrious 계열 생성 |
| RTX 2000번대 (2060 Super 8GB 등) | ComfyUI 통합팩 동작. **단 sage attention 을 끄고 써야 한다** | sage 를 켜면 터진다 |
| RTX 3060 12GB | "할 만하다" 급. MiniMax H3 영상도 RAM 32GB + NVMe 조합으로 832x480 124프레임 10분 미만 | |
| RTX 3090 | ANIMA 1024x1024 · euler simple · CFG 5 · 40스텝에 **20.73초** (BF16, sage, torch.compile) | 2장이면 14.11초 (49.9% 향상) |
| RTX 4080 SUPER | 장당 **6초** | SDXL/Illustrious 계열 |
| RTX 5070 Ti | ANIMA 4스텝 터보 로라로 장당 **1.2~1.31초** | er_sde / step 4 / cfg 1 |
| RTX 5090 | 장당 **4초** | SDXL/Illustrious 계열 |
| Intel Arc B580 | ANIMA 1장 28.96초 → 2장 15.53초. sage·torch.compile·int8 을 못 쓴다 | MiniMax H3 는 **구동 자체 실패** |
| AMD Radeon | MiniMax H3 에서 NVIDIA 에 크게 밀림 (R9700 3분27초 vs RTX3090 2분41초) | |

**정리하면**
- **지포스 3000~5000번대**가 ComfyUI 통합팩의 공식 권장선이다. 라데온은 미확인이라고 배포자가 적어 두었다.
- 2000번대는 sage attention 만 끄면 돌아간다.
- **라데온·Arc 는 사정이 바뀌었다.** 2024-06 자료는 "사용자가 적어 문제가 생겨도 답을 못 얻으니 NAI 를 쓰라" 였고
  그 말은 지금도 절반은 맞다 — 막혔을 때 물어볼 곳이 적다. 다만 **길이 생겼다**:
  **RX 7000 이상 / 노트북 RDNA 3 이상 / Arc A 시리즈 이상**이면 [Comfy-Org 윈도우 포터블](https://github.com/Comfy-Org/ComfyUI#windows-portable)로 가고,
  리눅스 + ROCm 이면 **RX 9060 XT 가 ANIMA 1024 를 22초**에 뽑는다. 절차는 [설치와 환경 구성](install.md)에 명령어째로 있다.
  **여전히 엔비디아보다 손이 많이 가고 안 되는 기능이 있다**(Arc 는 sage·torch.compile·int8 불가, MiniMax H3 구동 실패).
- VRAM 이 모자라면 ANIMA **INT8** 판을 쓴다. 모델+텍스트인코더+VAE 합쳐 4GB 미만이라 8GB 급에서도 무난하고 1.3배 이상 빠르다.

GPU 2장을 쓰는 MultiGPU CFG Split 은 CFG 가 1인 터보 로라 환경에서는 적용되지 않고 VRAM 이득도 없다는 점을 함께 알아 둬야 한다.

→ 더 파고들려면 [VRAM·속도 최적화](vram.md)

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [야한 그림을 뽑고 싶은 뉴비를 위한 초간단 가이드 26.07](https://arca.live/b/aiart/177192496) · [(가이드)아무것도 몰라도 10분내로 이해하는 기초 단어 가이드 23.01](https://arca.live/b/aiart/68686905)</small>

??? note "근거 12건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [야한 그림을 뽑고 싶은 뉴비를 위한 초간단 가이드 26.07](https://arca.live/b/aiart/177192496) · [(가이드)아무것도 몰라도 10분내로 이해하는 기초 단어 가이드 23.01](https://arca.live/b/aiart/68686905) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774) · [크퀘스타일 도트 로라 공유 26.04](https://arca.live/b/aiart/167362821) · [GPU 5종 MiniMax H3 I2VA 생성속도 테스트 26.08](https://arca.live/b/aiart/179069083) · [MultiGPU CFG Split이 ComfyUI maste… 26.05](https://arca.live/b/aiart/171831134) · [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 … 26.08](https://arca.live/b/aiart/179176367) · [하지만 빨랐죠? 자작 아니마 4스텝 로라 업데이트 26.07](https://arca.live/b/aiart/176518628) · [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부… 26.08](https://arca.live/b/aiart/178717529)

## ④ 처음 온 사람의 순서 — 1번부터
<small>2026-08 기준 · 근거 12건</small>

**1. 낱말부터 맞춘다.** 체크포인트·VAE·CFG·스텝·시드·샘플러·디노이즈·배치가 뭔지 10분이면 된다.
→ [용어집](glossary.md) (뿌리 원문: 68686905)

**2. 내 그래픽카드를 확인한다.** 위 ③번 표. **GPU 가 없으면** 여기서 [NovelAI](nai.md) 로 간다.
라데온·Arc 는 되기는 하지만 조건이 붙으니 ③번 표를 보고 정한다.

**3. 설치한다.** 둘 중 하나만 고른다.
- 그림만 뽑을 것이다 → **Forge Neo** (python 3.13.12 → `git clone ... --branch neo` → `webui-user.bat` 편집)
- 영상·인페인팅까지 할 것이다 → **ComfyUI 포터블 통합팩 0.31.0** (압축 풀고 컨트롤넷·체크포인트만 따로 받으면 끝)
→ [설치와 환경 구성](install.md)

**4. 모델을 받는다.**
- ANIMA: `anima-base-v1.0.safetensors` + `qwen_3_06b_base.safetensors` + `qwen_image_vae.safetensors`
- SDXL 계열이면 `WAI-illustrious-SDXL`
- 2026-08 기준으로 **SDXL/Pony 는 쓸 이유가 없고 Illustrious 나 ANIMA 를 쓰라**고 배포자가 명시했다.
- **처음 실제 검증은 ANIMA 로 하는 편이 쉽다.** 세 파일이 공식 Hugging Face 직링크라 바로 받아지고, Civitai 로그인·필터에 덜 막힌다.
- **애니가 아니라 인스타 감성의 예쁜 여자 사진 같은 실사 / 반실사**를 노리면, 처음부터 ANIMA 에 매달리기보다
  [모델 고르기](models.md) 의 **반실사·2.5D 계열**을 먼저 본다. 현재 문서에 묶여 있는 시작점은
  `RoseMIX_XL_V1.1`, `Uncanny Valley noob 3d v1 DMD`, `communitymodel / 2dac` 계열이다.
- 파일을 넣은 뒤에는 **ComfyUI 를 재시작하고** 드롭다운에 모델명이 뜨는지 본다.
- 첫 실행에서 기본 워크플로우가 **깨진 상태로 열려도 정상**이다. 이 경우 기본 예제를 고치지 말고 **`템플릿` → `Anima` 검색 → `Anima Base v1: 텍스트 기반 이미지 생성`** 으로 들어간다.
- 여기서 `anima-turbo-lora-v0.2.safetensors` 누락이 뜨면 실패가 아니라 **추가 로라 1개가 더 필요한 것**이다. `models\\loras` 에 넣고 오류 패널의 **`새로고침`** 을 누르면 바로 풀린다.
→ [자원 — 받는 곳 모음](resources.md) · [모델 고르기](models.md)

**5. 첫 장을 뽑는다.** 모르겠으면 이 값으로 시작한다.

| 쓰는 모델 | 샘플러 | 스케쥴러 | 스텝 | CFG | 해상도 |
|---|---|---|---|---|---|
| **ANIMA** (Forge Neo) | `ER SDE` | `Simple` | 27~30 | 4.5~5.5 | **1024x1024** |
| **Illustrious / NoobAI** | `Euler a` 또는 `Euler` | `SGM Uniform` | 28 | 4.5~5 | 1024x1024 |
| **반실사 / 실사 지향 SDXL·NoobAI 계열** | `Euler a` 또는 `Euler` | `SGM Uniform` 또는 `KL Optimal` | 24~35 | 계열에 따라 다름 (`CFG++` 계열은 1 근처, 일반 Euler 는 4.5~6) | 1024x1024 부근부터 |

이 표는 **처음 한 장을 뽑아 보라고 주는 시작값**이지 유일한 정답이 아니다.
ANIMA 줄은 Forge Neo 설치 가이드의 값이고, **공식 권장은 스텝 `30~50` · CFG `4.0~6.0` 으로 더 넓다**.
Illustrious 줄도 배포자마다 달라서, 계열별 공식·배포자 값은 [국룰](kukroul.md)의 표를 봐야 한다.
자기가 받은 모델의 배포글에 값이 적혀 있으면 **그게 가장 정확하다.**

실사 쪽은 **애니보다 프롬프트와 체크포인트 성향 차이가 더 크다.**
그래서 시작값만 보고 밀기보다 [모델 고르기](models.md) 의 **반실사 지향 모델 표**를 먼저 보고,
해당 모델이 `Euler a + SGM Uniform` 계열인지, `CFG++ + KL Optimal` 계열인지부터 맞추는 편이 낫다.

ANIMA 해상도는 **어떻게 쓰느냐에 따라 갈린다** — 한 방에 뽑으면 `1024` 급(`1024x1024` · `832x1216`), ANIMA 로 스케치를 잡고 Illustrious·업스케일로 마무리하는 2단 구성이면 **앞단은 `768` 근처**가 빠르다. 그보다 크게는 깡으로 올리지 말고 하이레즈나 업스케일로 키운다. 자세한 것은 [ANIMA](anima.md).

→ [프롬프트 쓰는 법](prompting.md)

**6. 안 되면 찾아본다.** 파란 깨짐·로라 안 보임·검은 화면·`exit code 9009` 는 이미 답이 나와 있다.
→ [오류 해결](troubleshooting.md) · [국룰](kukroul.md)

**7. 그 다음.** 한 장을 뽑았으면 여기서부터가 진짜다. 막힌 것부터 하나씩 고르면 된다.

| 이런 게 아쉽다 | 볼 곳 |
|---|---|
| 얼굴·손이 뭉개진다 | [디테일러 — 얼굴·손 고치기](detailer.md) |
| 일부만 고쳐 그리고 싶다 | [인페인팅·아웃페인팅](inpainting.md) |
| 원하는 포즈·구도가 안 나온다 | [컨트롤넷 — 구도·포즈 잡기](controlnet.md) |
| 특정 캐릭터·그림체를 쓰고 싶다 | [로라 쓰는 법](lora-usage.md) |
| 같은 캐릭터로 계속 뽑고 싶다 | [같은 캐릭터 계속 뽑기](consistency.md) |
| 해상도·화질을 올리고 싶다 | [업스케일과 화질](upscale.md) |
| 움직이게 하고 싶다 | [비디오 생성](video-generation.md) |

**결과물은 어디에 생기나.**
- ComfyUI 기본 출력: `설치폴더\\ComfyUI\\output`
- 지금 로컬 검증 환경: `F:\\AI\\ComfyUI\\ComfyUI\\output`
- 입력 이미지를 다시 넣을 곳: `설치폴더\\ComfyUI\\input`

**다음 목표가 "특정 작품 그림체를 흉내내기" 라면** 처음부터 이 네 갈래를 탄다.

| 목표 | 먼저 볼 것 | 시작점 |
|---|---|---|
| **카구야님은 고백받고 싶어 / 초 가구야 공주** 같은 또렷한 2D 러브코미디·극장판 작화 | [프롬프트 쓰는 법](prompting.md) 의 **작품 태그 / 작가 태그 / 그림체 깎기** | 작가를 여러 명 억지로 섞기보다 **작품 태그 1개 + 작가 태그 소수 + 작품 스크린샷 계열 보조 태그** |
| **장송의 프리렌** 같은 원작 고증형 애니풍 | [프롬프트 쓰는 법](prompting.md) 의 **캐릭터 태그가 작가 태그를 씹어먹을 때** | 인기 캐릭터 태그가 그림체를 눌러버릴 수 있으니 **캐릭터 / 작품 / 작가 순서**를 따로 본다 |
| **페르소나풍** 같은 강한 스타일 모사 | [모델 고르기](models.md) 의 **페르소나 스타일 체크포인트** | 프롬프트로 억지로 깎기보다 **전용 체크포인트**부터 쓰는 편이 빠르다 |
| **원신·붕괴 / 3D 게임풍** | [자원 — 받는 곳 모음](resources.md) 의 **ANIMA — 원신 · 붕괴 스타레일 인게임 느낌 조합** | 2D 모델 하나로 해결하려 하지 말고 **게임풍 전용 로라/조합**부터 본다 |

이 문서 기준 현재 판단은 이렇다 — **그림체 모사는 프롬프트만으로 끝나지 않는다.**
체크포인트 성향, 작품 태그, 작가 태그, 스타일 로라가 같이 움직인다.
즉 "어떤 애니 느낌"을 목표로 잡았으면 **그 작품에 맞는 시작 모델부터 고르는 것**이 절반이다.

**지금 DB 기준으로 특히 바로 써먹을 수 있는 5개 카드**

| 목표 | 바로 따라 할 핵심 |
|---|---|
| **카구야님 / 초 가구야 공주** | 작품 태그를 먼저 두고, 필요하면 `anime screencap` 류 보조 태그를 붙인다. 캐릭터명은 최소화한다 |
| **프리렌** | 캐릭터 이름이 너무 강하면 이름을 빼고 **레퍼런스 이미지 + 일반 태그**(`old man`, `bald` 같은 식)로 다시 조립한다 |
| **원작 애니풍 전반** | 작품 태그는 **`0.5::작품명::`** 처럼 낮게 시작한다. 1.0부터는 작풍이 과하게 튈 수 있다 |
| **반실사 / 인스타 감성** | `RoseMIX_XL_V1.1`, `2dac`, `Uncanny Valley` 같은 계열로 먼저 옮기고, ANIMA 에서 억지로 실사 태그를 누르지 않는다 |
| **작가 조합 실험** | 처음부터 8~10명을 쌓지 말고 **5명 안팎**에서 시작한다. 실제 카드 실험값은 5명 근처에서 가장 안정적이었다 |

더 읽을 것을 찾으면 **2026년 4월 입문자용 정보글 모음집**(https://arca.live/b/aiart/167283401)이 설치·워크플로우·ComfyUI 설명서·학습 네 갈래로 추린 최신 색인이다.

<small>근거 — [2026년 4월 입문자용 정보글 모음집 26.04](https://arca.live/b/aiart/167283401) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [NlxlMix - Noob 1.1 eps + Illustri… 25.03](https://arca.live/b/aiart/130197990) · [챈에서 nai 짤 프롬 확인하는법 23.12](https://arca.live/b/aiart/94872564)</small>

??? note "근거 12건 전부 보기"
    [2026년 4월 입문자용 정보글 모음집 26.04](https://arca.live/b/aiart/167283401) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [NlxlMix - Noob 1.1 eps + Illustri… 25.03](https://arca.live/b/aiart/130197990) · [챈에서 nai 짤 프롬 확인하는법 23.12](https://arca.live/b/aiart/94872564) · [초보자용 아니마+IL 워크플로우 VER.2 26.02](https://arca.live/b/aiart/163201876) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [(가이드)아무것도 몰라도 10분내로 이해하는 기초 단어 가이드 23.01](https://arca.live/b/aiart/68686905) · [NAI-XL 2dac / 2.5dac 색감 개선모델 (권장 … 25.06](https://arca.live/b/aiart/140191370) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [NAIA 기능 가이드 모음 (260217) 24.06](https://arca.live/b/aiart/108288949) · [Anima 모델 자연어 인식 테스트 26.02](https://arca.live/b/aiart/161190216)

## ⑤ 지금 어떤 모델을 쓰나 — 지형 한 장
<small>2026-05 기준 · 근거 3건</small>

2026년 5월 기준 채널의 티어 정리다. **깡성능 기준이며 무검열 아니메 능력 기준이 아니다** — 작성자 본인이 아니메 무검열로 보면 ANIMA 는 2~3티어급이라고 보충했다.

| 티어 | 모델 |
|---|---|
| 1티어 | GPT-Image 2, Nano-Banana 2 Pro |
| 2티어 | Z-Image-Turbo / Base, Qwen-Image-Edit-2511 |
| 3티어 | Flux.2 Kevin 9B, Chroma1-HD |
| 4티어 | **ANIMA 시리즈**, NAI 4.5 |
| 5티어 | NoobAI · Illustrious XL 기반 SDXL 모델 |

**계열 이름이 헷갈릴 때** (2024-10 기준 정리, 지금도 골격은 유효):
- **Pony** — SDXL 기반이나 독자 태깅이라 문법이 많이 다르고 NSFW 에 강하다
- **Illustrious XL (ILXL)** — 범용 태깅이라 보편적 프롬프트와 작가 태그가 잘 먹는다
- **AnimagineXL 3.1** — 애니 특화지만 사용 빈도가 낮다
- **FLUX** — 별개 오픈소스 모델. 고사양

2026-08 기준 배포자 권고는 한 줄이다 — **SDXL/Pony 는 쓸 이유가 없고 Illustrious 나 ANIMA 를 쓰라.**

다만 이 문서의 실제 목표를 **애니 한 장**에서 **실사/반실사까지** 넓히면 읽는 법이 달라진다.

- **애니 / 2D 기본 루트**: ANIMA → 필요하면 업스케일
- **인스타 감성 실사 / 반실사 루트**: [모델 고르기](models.md) 의 **RoseMIX_XL_V1.1 / Uncanny Valley / 2dac / communitymodel** 같은 계열부터

즉 **"요즘 대세가 ANIMA"** 와 **"내가 원하는 결과가 실사"** 는 다른 문제다.
실사를 목표로 잡았으면 처음부터 그쪽 체크포인트를 골라야 한다.

→ [모델 고르기](models.md) · [ANIMA](anima.md)

<small>근거 — [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774) · [(미니 정보) 26년 5월 기준 간단하게 소개하는 그림 AI… 26.05](https://arca.live/b/aiart/169601993)</small>

## ⑥ 채널에서 지켜야 할 최소한
<small>⚠️ 2024-06 기준 · 근거 2건</small>

**질문하기 전에 EXIF 부터 본다.** 그림의 작가·모델을 묻는 질문은 EXIF(메타데이터)가 없으면 아무도 알 수 없다. 반대로 있으면 스스로 다 볼 수 있다.

프롬프트를 확인하는 방법은 셋이다.
1. 크롬에 **템퍼몽키(Tampermonkey)** 를 깔고 `https://greasyfork.org/ko/scripts/464214` 의 EXIF 뷰어를 설치한다 — 클릭하는 즉시 프롬프트가 뜬다
2. 이미지를 저장해 **NovelAI 화면에 끌어다 놓는다** — NAI 로 만든 그림이면 EXIF 보존을 안 하고 올린 짤도 정보가 남아 있다
3. EXIF 가 보존된 원본을 **메모장으로 연다**

뷰어가 아무것도 못 읽는 경우의 99% 는 업로더가 EXIF 보존 체크를 해제하고 올린 것이다.

**이미 답이 나와 있는 질문들** — 파란 깨짐 / 로라 안 보임 / 모델 바꾸니 망가짐 / 눈·얼굴 뭉개짐 / 손 찐빠는 전부 [국룰](kukroul.md)과 [오류 해결](troubleshooting.md)에 있다.

<small>근거 — [챈에서 nai 짤 프롬 확인하는법 23.12](https://arca.live/b/aiart/94872564) · [(24.10.13 수정)질문하기 전에 한번만 보고 가면 24.06](https://arca.live/b/aiart/109424774)</small>

## ⑦ 문서 지도
<small>2026-04 기준 · 근거 2건</small>

| 하려는 것 | 문서 |
|---|---|
| 낱말이 안 통한다 | [용어집](glossary.md) |
| 깔아야 한다 | [설치와 환경 구성](install.md) |
| 파일을 어디서 받나 | [자원 — 받는 곳 모음](resources.md) |
| 웹서비스로 뽑겠다 | [NovelAI](nai.md) |
| 어떤 모델을 쓰나 | [모델 고르기](models.md) · [ANIMA](anima.md) |
| 프롬프트를 어떻게 쓰나 | [프롬프트 쓰는 법](prompting.md) |
| 노드가 무섭다 | [ComfyUI 쓰는 법](comfyui.md) |
| 느리다 / VRAM 이 모자란다 | [VRAM·속도 최적화](vram.md) |
| 화질을 올리고 싶다 | [업스케일과 화질](upscale.md) |
| 움직이게 하고 싶다 | [비디오 생성](video-generation.md) · [MiniMax H3](minimax-h3.md) |
| 오류가 난다 | [오류 해결](troubleshooting.md) |
| 포즈·구도를 잡고 싶다 | [컨트롤넷](controlnet.md) |
| 일부만 고쳐 그리고 싶다 | [인페인팅·아웃페인팅](inpainting.md) |
| 얼굴·손이 뭉개진다 | [디테일러](detailer.md) |
| 로라를 쓰고 싶다 / 굽고 싶다 | [로라 쓰는 법](lora-usage.md) |
| 같은 캐릭터로 계속 뽑고 싶다 | [같은 캐릭터 계속 뽑기](consistency.md) |
| 채널 예절 | [국룰](kukroul.md) |

채널 바깥 색인 — **입문자용 정보글 모음집**(2026-04, arca.live/b/aiart/167283401), **NAIA 가이드 색인**(arca.live/b/aiart/108288949).

<small>근거 — [2026년 4월 입문자용 정보글 모음집 26.04](https://arca.live/b/aiart/167283401) · [NAIA 기능 가이드 모음 (260217) 24.06](https://arca.live/b/aiart/108288949)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 84개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 채널에는 배포 링크를 base64 로 인코딩해 올리는 관행이 있어, 뜻 없는 영문+숫자 덩어리가 보이면 base64 디코더에 넣으면 실제 주소(kio.ac · mega.nz 가 많다)가 나온다 | 12 | 0 | 2023-03~2026-06 |
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |
| ANIMA 의 공식 지원 해상도는 512x512(NAI1) ~ 1024x1024(SDXL) ~ 1536x1536(ILXL1) 버킷이고, 공식·입문 자료는 SDXL 해상도(1024급, 세로 832x1216)를 무난한 기본값으로 권한다 | 5 | 0 | 2026-01~2026-05 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| 채널에 올라오는 신규 모델 소식의 상당수는 제작사 주장·유출·LLM 요약이라 실사용 검증이 없다 | 5 | 0 | 2026-02~2026-07 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| 설정 > Comfy > Nodes 2.0 > 모던 노드 디자인을 켜면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다 | 4 | 0 | 2026-05~2026-08 |
| ANIMA 는 다국어를 지원하지 않아 프롬프트를 영어로 써야 하며, 한국어로 쓰려면 워크플로우에 번역 노드를 끼워 넣는다 | 4 | 0 | 2026-02~2026-08 |
| int8convrot 양자화는 fp8 tensorwise 보다 품질이 좋고(Q8_0 급) 조금 빠르며, 캘리브레이션이 필요 없어 대세가 된다 | 4 | 0 | 2026-07~2026-08 |
| MiniMax H3 는 RTX 3060 12GB + RAM 32GB 급 환경에서도 구동된다 | 4 | 0 | 2026-07~2026-08 |
| 통합팩은 ComfyUI 본체를 업데이트하지 말고 새 버전이 나오면 처음부터 새로 받아야 한다 | 4 | 0 | 2026-05~2026-08 |
| 모델이 diffusion model 단독으로 배포되면 models/checkpoints 가 아니라 models/diffusion_models 에 넣고 Load Diffusion Model 계열 노드로 불러야 하며, 텍스트 인코더와 VAE 도 각각 models/text_encoders, models/vae 에 따로 넣어 연결해야 한다 | 4 | 0 | 2026-05~2026-08 |
| SDXL/Illustrious 결과물이 탁하거나 흰 점이 찍히면 VAE Select 값을 2로 두어 별도 VAE(fixFP16ErrorsSDXLLowerMemoryUse_v10)를 적용한다 | 4 | 0 | 2026-06~2026-08 |
| ComfyUI 포터블에서 파이썬 패키지를 깔 때는 시스템 파이썬이 아니라 `python_embeded\python.exe -m pip` 로 설치해야 한다 | 4 | 0 | 2026-01~2026-08 |
| 이미지 생성(ANIMA)에서는 dynamic vram 을 끄는 쪽이 빠르며, torch.compile 을 쓸 때는 --disable-dynamic-vram 이 사실상 필수다 | 4 | 0 | 2026-05~2026-08 |
| EXIF(메타데이터)는 이미지 파일 안에 텍스트로 박히는 생성 정보(프롬프트·시드·스텝·모델 해시)이며, 아카라이브는 업로드 시 EXIF 보존 옵션을 제공하고 채널은 EXIF 공유를 권장한다 | 3 | 0 | 2023-01~2023-12 |
| ComfyUI 포터블에서 가속 패키지는 시스템 파이썬이 아니라 동봉된 `python_embeded` 파이썬에 깔아야 한다 | 3 | 0 | 2026-01~2026-08 |
| 그림의 작가·모델을 묻는 질문은 EXIF(메타데이터)가 없으면 아무도 알 수 없다 | 3 | 0 | 2023-12~2026-06 |
| 뉴비가 공유받은 워크플로우에서 오류가 터지는 범인 1위는 sage-attention 이다 | 3 | 0 | 2026-05~2026-08 |
| ANIMA 는 기존 ILXL 로라를 쓸 수 없고, 로라는 ANIMA 계열(프리뷰1~3 · 정발 Base 1.0)로 학습된 것을 베이스 버전에 맞춰 골라야 한다 | 3 | 0 | 2026-04~2026-06 |
| ComfyUI 통합팩은 한글이 없는 경로에 압축을 풀어야 한다 | 3 | 0 | 2026-02~2026-08 |
| sage attention을 켜면 손가락 찐빠(손 왜곡)가 늘어난다는 보고가 있다 | 3 | 0 | 2026-06~2026-08 |
| VAE 는 이미지를 더 작은 잠재 공간으로 인코딩·디코딩하는 신경망 부분으로 색감과 선명도를 결정하며, 결과물이 물 빠진 듯 흐리면 VAE 를 적용하지 않은 것이다. 모델에 내장돼 있어 필수는 아니다 | 2 | 0 | 2023-01~2023-01 |
| i2i(img2img)는 기존 이미지를 재료로 새 이미지를 만드는 방식이고, 인페인팅은 그중 특정 부분만 다시 그리는 기능이다 | 2 | 0 | 2023-01~2023-11 |
| AI 그림 EXIF 뷰어는 greasyfork.org 에 올라온 유저스크립트를 Tampermonkey/Violentmonkey 에 설치해 쓰며(https://greasyfork.org/ko/scripts/464214), NovelAI·Stable Diffusion WebUI·InvokeAI 로 만든 png/jpeg/webp 를 AI그림채널·픽시브에서 클릭만으로 읽어 준다 | 2 | 0 | 2023-03~2023-12 |
| ANIMA 용 CLIP 로드 노드에서 나는 `size mismatch for model.embed_tokens.weight: copying a param with shape torch.Size([151936, 1024]) ... current model is torch.Size([128256, 4096])` (Llama2 텐서 크기 불일치) 오류는 ComfyUI 를 업데이트하면 해결된다 — 구버전이 Qwen 계열 텍스트 인코더를 Llama2 로 잘못 잡던 문제다 | 2 | 0 | 2026-01~2026-02 |
| 체크포인트(모델)는 이미지를 학습한 결과 파일(.ckpt/.safetensors)로 그림을 뽑는 본체이며, Stable Diffusion 을 붕어빵 기계라 하면 체크포인트가 형틀에 해당한다 | 2 | 0 | 2023-01~2023-01 |
| sage attention을 끄면 지포스 2000번대에서도 ComfyUI 통합팩이 동작한다 | 2 | 0 | 2026-08~2026-08 |
| 2023년 2월의 채널 정보글 모음 공지는 작성자 본인이 댓글에서 대부분 outdated 라고 인정했고 삭제된 글과 죽은 링크가 섞여 있어, 최신 정보는 정보탭에서 직접 검색하는 편이 낫다 | 2 | 0 | 2023-02~2026-04 |
| 검은 이미지·NaN 오류는 U-Net 에서 터졌으면 `--no-half`, VAE 에서 터졌으면 `--no-half-vae` 를 붙여 어디서 터졌는지부터 가르고, 크로스 어텐션 최적화 버그가 의심되면 `--opt-sub-quad-attention` 도 시도한다 | 2 | 0 | 2023-01~2026-05 |
| Illustrious/NoobAI 계열 병합 모델의 권장 기본값은 대체로 Euler 계열 샘플러 · CFG 4.5~5 · **28스텝** · **1024x1024** 다 — NlxlMix 는 `Euler a` / CFG 5 / 28 / 1024x1024, NAI-XL 2dac 는 `Euler + SGM Uniform` / CFG 4.5 / 28 / CFG Rescale 0.6 (reForge 기준) | 2 | 0 | 2025-03~2025-06 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [~무지성부터 활용까지~ NAI 사용법을 떠먹어보자](https://arca.live/b/aiart/92677065) — 2023-11, 추천 51
- [Comfyui portable v0.30.0 + sage 외 여러가지.](https://arca.live/b/aiart/178800540) — 2026-08, 추천 47
- [2026년 4월 입문자용 정보글 모음집](https://arca.live/b/aiart/167283401) — 2026-04, 추천 45
- [뉴비들은 webui neo 쓰자](https://arca.live/b/aiart/176802949) — 2026-07, 추천 44
- [야한 그림을 뽑고 싶은 뉴비를 위한 초간단 가이드](https://arca.live/b/aiart/177192496) — 2026-07, 추천 44
- [NlxlMix - Noob 1.1 eps + Illustrious 1.0 기반 병합 모델](https://arca.live/b/aiart/130197990) — 2025-03, 추천 43
- [챈에서 nai 짤 프롬 확인하는법](https://arca.live/b/aiart/94872564) — 2023-12, 추천 42
- [초보자용 아니마+IL 워크플로우 VER.2](https://arca.live/b/aiart/163201876) — 2026-02, 추천 39
- [[가이드]아무것도 몰라도 10분내로 이해하는 기초 단어 가이드](https://arca.live/b/aiart/68686905) — 2023-01, 추천 38
- [Comfyui portable v0.31.0 + sage 외 여러가지.](https://arca.live/b/aiart/179342860) — 2026-08, 추천 38
- [NAI-XL 2dac / 2.5dac 색감 개선모델 (권장 세팅 추가)](https://arca.live/b/aiart/140191370) — 2025-06, 추천 33
- [(24.10.13 수정)질문하기 전에 한번만 보고 가면](https://arca.live/b/aiart/109424774) — 2024-06, 추천 32
- [[미니 정보] 26년 5월 기준 간단하게 소개하는 그림 AI 모델들](https://arca.live/b/aiart/169601993) — 2026-05, 추천 31
- [ComfyUI App mode가 나왔길래 써봤다.](https://arca.live/b/aiart/164519826) — 2026-03, 추천 27
- [NAIA 및 아니마 사용을 위한 Webui Forge Neo 포지네오 설치 가이드 (수정)](https://arca.live/b/aiart/170554328) — 2026-05, 추천 26
- [크퀘스타일 도트 로라 공유](https://arca.live/b/aiart/167362821) — 2026-04, 추천 24
- [NAIA 기능 가이드 모음 (260217)](https://arca.live/b/aiart/108288949) — 2024-06, 추천 23
- [GPU 5종 MiniMax H3 I2VA 생성속도 테스트](https://arca.live/b/aiart/179069083) — 2026-08, 추천 20
- [Comfy로 anima 실행 및 최적화하기](https://arca.live/b/aiart/175408089) — 2026-06, 추천 19
- [reForge 간단 소개 및 클린설치 매뉴얼 (초보자도 가능)](https://arca.live/b/aiart/119210516) — 2024-10, 추천 18
- [Anima 모델 자연어 인식 테스트](https://arca.live/b/aiart/161190216) — 2026-02, 추천 18
- [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minimax H3)](https://arca.live/b/aiart/178537097) — 2026-07, 추천 18
- [MultiGPU CFG Split이 ComfyUI master에 커밋됨](https://arca.live/b/aiart/171831134) — 2026-05, 추천 16
- [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 세팅 방법](https://arca.live/b/aiart/179176367) — 2026-08, 추천 16
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [하지만 빨랐죠? 자작 아니마 4스텝 로라 업데이트](https://arca.live/b/aiart/176518628) — 2026-07, 추천 13
- [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부 공개](https://arca.live/b/aiart/178717529) — 2026-08, 추천 9
- [Gemini Omni Flash vs Minimax-H3](https://arca.live/b/aiart/178630221) — 2026-08, 추천 7
