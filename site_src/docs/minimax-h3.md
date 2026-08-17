# MiniMax H3

> **원문 14건 → 이 문서 하나** · 주장 29개 · 정리 2026-08-14

바이트댄스 계열 오픈웨이트 영상 생성 모델. 2026년 8월 현재 채널의 주력이다. **자료가 전부 최근 1~2주 안에 나왔고 하루 단위로 뒤집히고 있으니** 날짜를 보고 읽을 것.

## 가속 — 노드 조합이 3배를 가른다
<small>2026-08 기준 · 근거 2건</small>

i7-13700F + RTX5090 + 64GB, 1MPixel 5초 기준 실측이다.

| 조합 | 시간 |
|---|---|
| 기본 (가속 없음) | 309.58s |
| MiniMaxH3 Cache 단독 | 153.80s |
| **Cache + Mem Eff Sage + Patch Sage KJ** | **94.73s** ← 최상 |
| Cache + Patch Sage KJ | 100.39s |
| Cache + Mem Eff Sage | 105.33s |
| Cache + Spectrum | **Error** |

**연결 순서**가 중요하다 *(댓글)*:
`Load Diffusion Model → MiniMaxH3 Cache → MiniMax H3 Mem Eff Sage Attention Patch → Patch Sage Attention KJ → Basic Guider`

> **VRAM에 따라 결과가 다르다.** 4080 Super 16GB에서는 Mem Eff Sage Attention Patch 효과가 없었다는 반례가 있다(다이나믹 VRAM 오프로드 탓으로 추정). 5080 + 64GB에서는 0.4MP 15초 영상이 180초.

`Spectrum Apply MiniMax H3`는 Cache와 **같이 쓰면 에러**다. 단독으로는 약 30% 단축.

<small>근거 — [MiniMax H3 가속 노드 별 속도 후기 26.08](https://arca.live/b/aiart/179038650) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965)</small>

## VRAM 옵션 — 건드리지 않는 게 기본
<small>2026-08 기준 · 근거 1건</small>

RAM 32GB로 충분하다. 실측 **AMD 5600G + DDR4 3200 32GB + RTX3060에서 8분 53초**.

**쓰지 말 것** — VRAM 80GB 이하면 손대지 않는다:
`--disable-dynamic-vram`, `--lowvram`, `--highvram`, `--gpu-only`

특히 `--disable-dynamic-vram`은 smart memory로 동작해 offload 모델을 전부 RAM에 올려 **최소 40GB 가까이** 쓴다.

**상황에 따라 쓸 것**:
- `--disable-pinned-memory` — RAM 32GB 이하. **댓글 확인: MiniMax는 이걸 줘야 정상 생성된다**
- `--reserve-vram 1.0`, `--vram-headroom`, NVMe면 `--fast-disk`

옵션은 `run_nvidia_gpu.bat`의 `--windows-standalone-build` 뒤에 이어 적는다. torch는 `+cu130` 이상이라야 int8convrot 속도 향상이 있다.

<small>근거 — [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112)</small>

## 양자화 — int8convrot / w4a8
<small>2026-08 기준 · 근거 2건</small>

**int8convrot Video VAE** (ComfyUI PR #15334 머지, git pull로 적용)

| 디코드 | fp16 | int8convrot |
|---|---|---|
| 1 MPixel | 16.65s | **11.85s** |
| 0.4 MPixel | 5.83s | **3.31s** |

RTX5090 400W 기준. blend image로 diff를 떠도 결과물 차이가 없었다.

> **검은 화면 이슈** — 본문은 "ComfyUI 최신 + torch +cu130 이후 + comfy-aimdo 최신 + comfy-kitchen 최신"으로 해결된다고 정정했으나, **댓글에 PyTorch 2.11.0+cu130 신규 설치 환경에서도 재현된다는 미해결 보고**가 남아 있다.

**w4a8 (가중치 4비트 / 활성화 8비트)** — ComfyUI git 최신 + comfy-kitchen v0.2.27 이상. AMD day 0 지원.

속도는 int8convrot 64.99초 vs w4a8 69.90초로 **오히려 소폭 느리다.** 다만 VRAM이 작거나 큰 해상도·긴 길이에서는 cpu offload가 줄어 유리할 수 있다.

<small>근거 — [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [ComfyUI w4a8_int 양자화 모델 지원 26.08](https://arca.live/b/aiart/179270173)</small>

## 터보 LoRA — Cache와 같이 쓰면 안 된다
<small>2026-08 기준 · 근거 3건 · **근거 약함** · 자료 엇갈림</small>

4스텝으로 줄여 **25스텝 30분 → 4스텝 4분**까지 떨어진 사례가 있다(sage 병용).

**그런데 자료가 정면으로 엇갈린다:**

| 주장 | 출처 |
|---|---|
| 움직임은 따라오나 소리가 먹먹하고, 같은 시드에서도 그림체가 바뀐다 | 본문 |
| **Cache와 중첩하면 결과물이 박살난다** — Cache는 이전 계산 재활용, Turbo는 스텝 자체를 생략해 원리가 겹침 | 댓글 |
| 퀄리티는 그냥 **cache 쪽이 압살**한다 | 다른 글 댓글 |
| 제작자는 8스텝을 권한다 / 반론: Cache가 이미 20스텝 중 11~12를 건너뛰므로 4스텝 아니면 무의미 | 댓글 |
| civitai의 다른 turbo LoRA가 더 낫다 — 실사 ema 500, 애니 850 | 댓글 |

**정리되지 않은 상태다.** Cache를 이미 쓰고 있다면 터보 LoRA는 보류하는 편이 안전하다.

쓸 경우 `ComfyUI-MiniMax-H3-Turbo` 노드를 반드시 함께 쓴다(퀄 차이 큼). 사운드 깨짐은 Kijai 노드 업데이트로 해결된다 *(댓글)*.

<small>근거 — [lightx2v minimax fl2v 터보로라 공개 (v0… 26.08](https://arca.live/b/aiart/179258094) · [미니맥스 H3 터보로라 나온듯? 26.08](https://arca.live/b/aiart/179094410) · [1시간전에 올라온 H3 고속 로라 테스트 26.08](https://arca.live/b/aiart/179280493)</small>

## 알려진 문제 — ComfyUI 버전 충돌
<small>2026-08 기준 · 근거 2건</small>

**증상**: MiniMaxH3-Cache 노드에서 `time_shift_slope` 오류

**경계 버전이 특정됐다:**
- 정상: `v0.30.0-1-g14b05228c` (2026-08-02)
- 발생: `v0.30.0-19-g88fec4b6` 이후

**회피**: ComfyUI 업데이트를 미루거나 다운그레이드한다.

임시 포크가 배포됐다가, **댓글에서 원 저장소에 PR이 이미 올라와 있다고 정정**되어 작성자가 포크를 내려도 되겠다고 답했다. 지금은 원 저장소를 확인하는 게 맞다.

같은 시기 ComfyUI의 dynamic VRAM에서 스파이크로 OOM이 나는 **별개 문제**도 보고됐다.

<small>근거 — [ComfyUI Nightly용 Minimax H3 Cache… 26.08](https://arca.live/b/aiart/179215559) · [ComfyUI 최신버전에서 MiniMaxH3-Cache 버그… 26.08](https://arca.live/b/aiart/179251955)</small>

## 프롬프트 — Ollama 자동 생성
<small>2026-08 기준 · 근거 2건</small>

H3는 프롬프트 형식이 까다로워서, 로컬 LLM으로 자동 생성하는 방식이 자리잡았다.

**형식 규칙**
- 기본 길이 `10.00 seconds`, 보통 3~4비트 (setup → action onset → development → result)
- `[Shot 1]`에는 타임스탬프를 붙이지 않는다. 이후는 `[Shot N] At 00:SS.mmm, the camera cuts to...`
- 대사는 `<d>[Korean] 원문</d>`로 원문 보존, 화자는 `(S1)` 고정 ID
- 라벨 정규화: `사진1` → `<Picture 1>`, `영상1` → `<Video 1>`, `오디오1` → `<Audio 1>`
- 모드는 레퍼런스에 따라 자동 판정: 없으면 T2VA / 이미지 1장이면 I2VA / 마지막 프레임이면 L2VA / 첫·끝 둘 다면 FL2VA

**Full-reference 모드**는 6개 섹션을 이 순서로 강제한다:
`subject_definitions / summary / retention_analysis / detailed_description / overall_soundscape / non_diegetic_music`

**LLM**: Qwen heretic 8B로 10초 이내 생성. Qwen3.6 27B Q5는 230초 이상. 커스텀 노드는 `stavsap/comfyui-ollama`.

> ⚠️ **본문 복사 주의** — 한 글은 아카라이브 접기 코드가 꼬여 본문에서 `<Picture 0>`, `<Subject N>` 태그가 **통째로 누락**됐다. 작성자가 인정했고 첨부 이미지 쪽이 정본이다.

<small>근거 — [MinimaxH3 I2V 전용 Ollama 자동 프롬프트 26.08](https://arca.live/b/aiart/179447493) · [MinimaxH3 용 Ollama 자동 프롬프트를 위한 시스… 26.08](https://arca.live/b/aiart/178949046)</small>

## 모델 자체에 대해 — 개발팀 AMA
<small>2026-08 기준 · 근거 1건</small>

레딧 AMA 요약.

- **H3-Regenerate-2K**는 H3를 한 번 더 돌리는 게 아니라 **latent 수준 업스케일 전용 DiT 모델**. 가정용 GPU 대응 작업 중, 출시일 미정
- **5+17 프레임 고정 구조**는 토큰의 시공간 분포를 고르게 하려는 것
- **시드가 같아도 해상도가 바뀌면 다른 영상**이 나온다. 저해상도 미리보기 방식이 잘 안 통하는 이유
- 기본 해상도는 **768p**이며 2K 업스케일도 원본이 768p여야 한다 *(댓글)*
- sparse attention은 MSA가 아니라 **MoBA 스타일 블록**
- few-step 증류 LoRA와 h3-context-ir는 **공식 배포 계획 없음**
- 번짐·노이즈·작은 물체 디테일 붕괴는 VAE 단독 문제가 아니라 훈련 파이프라인 전반 문제로 최우선 작업 중

<small>근거 — [미니맥스 AMA한 것 내용 정리 26.08](https://arca.live/b/aiart/179268944)</small>

## 라이선스
<small>2026-08 기준 · 근거 1건</small>

서면 허가 신청 폼이 있다. 제출하면 즉시 허가 메일이 온다.

오픈웨이트지만 초상권·저작권 소송 대비로 라이선스를 그렇게 잡았다는 설명이다. **댓글에서는 안 해도 대체로 문제없고 예방 차원**이라고 답했다.

<small>근거 — [Minimax H3 서면 허가 신청 폼 26.08](https://arca.live/b/aiart/178825020)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| MiniMax H3 프롬프트는 [Shot 1] 에 타임스탬프를 붙이지 않고 이후 샷만 'At 00:SS.mmm' 형식으로 시간이 증가하게 적으며 기본 길이는 10.00초다 | 5 | 0 | 2026-08~2026-08 |
| ComfyUI 포터블에서 파이썬 패키지를 깔 때는 시스템 파이썬이 아니라 `python_embeded\python.exe -m pip` 로 설치해야 한다 | 4 | 0 | 2026-01~2026-08 |
| int8convrot 양자화는 fp8 tensorwise 보다 품질이 좋고(Q8_0 급) 조금 빠르며, 캘리브레이션이 필요 없어 대세가 된다 | 4 | 0 | 2026-07~2026-08 |
| 통합팩은 ComfyUI 본체를 업데이트하지 말고 새 버전이 나오면 처음부터 새로 받아야 한다 | 4 | 0 | 2026-05~2026-08 |
| MiniMax H3 터보 LoRA 는 H3-Cache 와 원리가 겹쳐 함께 쓰면 결과물이 망가지며, 품질은 Cache 쪽이 낫다 | 4 | 0 | 2026-08~2026-08 |
| MiniMax H3 가속은 MiniMaxH3 Cache(TeaCache 계열, 스텝 스킵이 아니라 계산 결과 재사용)가 EasyCache·Spectrum 보다 품질 손실이 적어 사실상 표준이다 | 4 | 0 | 2026-08~2026-08 |
| MiniMax H3 는 RTX 3060 12GB + RAM 32GB 급 환경에서도 구동된다 | 4 | 0 | 2026-07~2026-08 |
| 프롬프트 생성용 로컬 LLM 은 27B/35B 급이 VRAM 26~28GB 를 먹고 응답도 느려, 8~9B 급이 현실적인 상용 구간이다 | 3 | 0 | 2026-03~2026-08 |
| Spectrum Apply MiniMax H3 노드는 MiniMaxH3 Cache·EasyCache 와 함께 쓸 수 없다 | 3 | 0 | 2026-08~2026-08 |
| ComfyUI v0.30.0-19-g88fec4b6 이후 버전에서 ComfyUI-MiniMaxH3-Cache 노드가 time_shift_slope 오류를 낸다 | 3 | 0 | 2026-08 |
| ComfyUI 포터블에서 가속 패키지는 시스템 파이썬이 아니라 동봉된 `python_embeded` 파이썬에 깔아야 한다 | 3 | 0 | 2026-01~2026-08 |
| MiniMax H3·NSFW 프롬프트 자동생성은 검열 때문에 GPT·제미나이가 아니라 Grok 또는 Ollama 로컬 모델(Qwen 계열)에 물려야 한다 | 3 | 0 | 2026-08~2026-08 |
| 포터블 구버전이 무조건 나쁜 것은 아니어서, 최신 버전에서 말썽을 부리는 노드가 있으면 구버전에서 작업하는 편이 나은 경우도 있다 | 3 | 0 | 2026-02~2026-08 |
| LTX2.3 영상 생성에서 dynamic_vram 을 켜면 RAM 사용이 약 80GB 에서 10~15GB 로 줄어들므로 반드시 켜야 한다(이미지 생성에서는 끄는 편이 낫다) | 2 | 0 | 2026-03~2026-08 |
| ComfyUI Manager 로 업데이트하면 코어(내장 노드) 변경이 반영되지 않으므로 본체는 git 또는 update_comfyui.bat 으로 업데이트해야 한다 | 2 | 0 | 2026-04~2026-08 |
| `ImportError: DLL load failed while importing _fused: 지정된 프로시저를 찾을 수 없습니다` 는 torch/python/sageattention/cuda 버전이 어긋난 것이므로 cp313 전용 whl 대신 파이썬 버전 무관 빌드(cp39-abi3)인 `sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl`(4000번대는 cu128 판)로 바꾸면 해결된다 | 2 | 0 | 2026-01~2026-08 |
| MiniMax H3 의 w4a8_int 양자화는 int8convrot 보다 약 1.09배 느리며(69.90초 vs 64.99초), VRAM 이 작거나 큰 해상도에서만 cpu offload 감소로 유리할 수 있다 | 2 | 0 | 2026-08~2026-08 |
| MiniMaxH3-Cache 의 오류는 __init__.py 에서 slope_a 곱을 빼고 return [-video_out, -audio_out] 로 두 줄 고치면 해결되며 업스트림 PR 은 닫혀 있다 | 2 | 0 | 2026-08 |
| MiniMax H3 터보(고속) LoRA 4스텝으로 25스텝 30분 걸리던 생성을 4분까지 줄일 수 있다 | 2 | 0 | 2026-08~2026-08 |
| MiniMax H3 최속 조합은 MiniMaxH3 Cache + MiniMax H3 Mem Eff Sage Attention Patch + Patch Sage Attention KJ 3종이며 기본 309.58초를 94.73초로 약 3배 줄인다 | 2 | 0 | 2026-08~2026-08 |
| MiniMax H3 Mem Eff Sage Attention Patch·Patch Sage Attention KJ 는 KJNodes 소속 노드이며 Nightly 버전을 지정해야 나타난다 | 2 | 0 | 2026-08~2026-08 |
| MiniMax H3 에 Spectrum Apply 노드를 붙이면 생성 시간이 약 30% 줄어든다 | 2 | 0 | 2026-08~2026-08 |
| MiniMax H3 의 기본 해상도는 768p 이며 그 이하는 저해상도 취급이라 저해상도 미리보기 방식이 통하지 않는다 | 1 | 0 | 2026-08~2026-08 |
| MiniMax H3 구동에 RAM 32GB면 충분하며, VRAM 관련 옵션을 수동으로 통제하면 오히려 해롭다 | 1 | 0 | 2026-08 |
| MiniMax H3 는 5+17 프레임 고정 구조를 쓰며 이는 토큰의 시공간 분포를 고르게 하기 위함이다 | 1 | 0 | 2026-08 |
| triton·sageattention 은 DazzleML 인스톨러를 포터블 내부 파이썬으로 --install 해서 까는 것이 간편하다 | 1 | 0 | 2026-02~2026-08 |
| MiniMax H3는 --disable-pinned-memory 옵션을 줘야 정상 생성된다 | 1 | 0 | 2026-08 |
| MiniMax H3 는 오픈웨이트지만 초상권·저작권 소송 대비로 서면 허가 라이선스를 두었고, feishu 신청 폼을 제출하면 즉시 허가 메일이 온다 — 안 하고 써도 대체로 문제는 없고 예방 차원이라는 것이 채널의 답이다 | 1 | 0 | 2026-08 |
| MiniMax H3 용 int8convrot Video VAE 는 fp16 대비 디코드가 약 30~40% 빠르면서 결과물 차이가 없다 | 0 | 0 | 2026-08 |

## 이 문서와 이어진 곳

**이 개체를 다루는 다른 문서**

- [오류 해결](troubleshooting.md) (문제해결)
- [ComfyUI 쓰는 법](comfyui.md) (튜토리얼)
- [모델 고르기](models.md) (가이드)
- [국룰 — 채널이 합의한 기본값](kukroul.md) (국룰)
- [VRAM·속도 최적화](vram.md) (가이드)
- [업스케일과 화질](upscale.md) (가이드)
- [비디오 생성](video-generation.md) (가이드)

**함께 등장하는 것들** — 숫자는 같은 글에 함께 나온 횟수

ComfyUI 19 · KJNodes 6 · SageAttention 6 · MiniMaxH3-Cache 6 · comfy-kitchen 3 · Qwen Image 3 · Ollama 2 · MiniMax-H3-Turbo-Lora 2 · comfyui-ollama 2

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들](https://arca.live/b/aiart/179458112) — 2026-08, 추천 44
- [MiniMax H3 가속 노드 별 속도 후기](https://arca.live/b/aiart/179038650) — 2026-08, 추천 35
- [MiniMax H3 int8convrot Video VAE 올라옴](https://arca.live/b/aiart/179114541) — 2026-08, 추천 34
- [미니맥스 AMA한 것 내용 정리](https://arca.live/b/aiart/179268944) — 2026-08, 추천 27
- [MinimaxH3 I2V 전용 Ollama 자동 프롬프트](https://arca.live/b/aiart/179447493) — 2026-08, 추천 23
- [MinimaxH3 용 Ollama 자동 프롬프트를 위한 시스템 프롬프트](https://arca.live/b/aiart/178949046) — 2026-08, 추천 22
- [Minimax H3 서면 허가 신청 폼](https://arca.live/b/aiart/178825020) — 2026-08, 추천 17
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [lightx2v minimax fl2v 터보로라 공개 (v0.1 프리뷰)](https://arca.live/b/aiart/179258094) — 2026-08, 추천 12
- [미니맥스 H3 터보로라 나온듯?](https://arca.live/b/aiart/179094410) — 2026-08, 추천 6
- [1시간전에 올라온 H3 고속 로라 테스트](https://arca.live/b/aiart/179280493) — 2026-08, 추천 6
- [ComfyUI w4a8_int 양자화 모델 지원](https://arca.live/b/aiart/179270173) — 2026-08, 추천 5
- [ComfyUI Nightly용 Minimax H3 Cache 수정버전](https://arca.live/b/aiart/179215559) — 2026-08, 추천 2
- [ComfyUI 최신버전에서 MiniMaxH3-Cache 버그있는듯](https://arca.live/b/aiart/179251955) — 2026-08, 추천 0