# 오류 해결

> **원문 174건 → 이 문서 하나** · 주장 495개 · 정리 2026-08-14

증상으로 찾는 문서다. **여기 있는 것의 절반 이상은 원문 본문이 아니라 댓글에서 나왔다.** 글만 읽고 따라 하다 막히는 이유가 대개 그것이다.

## 먼저 — 증상별 빠른 찾기
<small>2026-08 기준 · 근거 105건</small>

| 증상 | 원인 | 어디로 |
|---|---|---|
| `time_shift_slope` 오류 | ComfyUI 버전 × MiniMaxH3-Cache | ↓ 버전 충돌 |
| 영상이 **검은 화면** | int8convrot VAE 환경 | ↓ 버전 충돌 |
| ADetailer 후 **검은 사각형** → 전체 검게 | Forge Neo 확장 호환 | ↓ 결과물 이상 |
| 안 시켰는데 **비키니**가 나옴 | 퀄리티 태그 부작용 | ↓ 결과물 이상 |
| 인페인팅이 **Pause 0%** 에서 멈춤 | 대기 상태 (오류 아님) | ↓ 멈춘 것처럼 보임 |
| 커스텀 노드가 **매니저에서 안 나옴** | 매니저 등록 안 됨 | ↓ 설치 |
| 업데이트했는데 **반영이 안 됨** | 매니저 ≠ 코어 | ↓ 설치 |
| 노드 이름이 **엔크립트/어노말리**로 뜸 | 오인식 (실제로는 KJNodes) | ↓ 설치 |
| **공유받은 워크플로우가 그냥 터짐** | **sage-attention (범인 1위)** | ↓ ComfyUI · 포터블 계열 표 |
| 커스텀 노드 clone 이 `Filename too long` | 윈도우 260자 경로 제한 | ↓ ComfyUI · 포터블 계열 표 |
| 라데온에서 `hipErrorInvalidValue` | gfx1200·gfx1100 장치 패키지 미설치 | ↓ ComfyUI · 포터블 계열 표 |
| `Couldn't install torch` 가 반복됨 | venv 밖에 설치했다 | ↓ PyTorch 가 안 깔린다 |
| **검은 이미지 · NaN** | U-Net / VAE 어느 쪽인지부터 | ↓ 검은 이미지 · NaN |
| VAE 를 걸었는데 그림체가 이상하다 | **VAE 는 그림체를 바꾸지 않는다** | ↓ VAE 오해 둘 |
| A1111 이 아예 실행되지 않음 (2026) | 파이썬에 `pkg_resources` 가 빠졌다 | [설치와 환경 구성](install.md) |
| `git clone` 후 폴더에 **`.git` 만 남고 파일이 없음** | 파일명의 **콜론(:)** — 윈도우가 못 만든다 | ↓ 새로 깔면 만나는 오류 (설치·clone) |
| `Couldn't install clip` / `Failed to build ... CLIP ... zip` | 최신 setuptools 가 구형 CLIP 빌드를 깨뜨림 | ↓ 새로 깔면 만나는 오류 (설치·clone) |
| `Stability-AI/stablediffusion.git not found` | 원본 저장소가 사라졌다 | ↓ 새로 깔면 만나는 오류 (설치·clone) |
| 노드 교체 후 **'필수 리소스 로드에 실패했습니다'** | 기존 폴더를 `_old` 로 이름만 바꿔 중복 로드 | ↓ 새로 깔면 만나는 오류 (설치·clone) |
| 번역이 안 됨 / `requires googletrans-py ...` | `googletrans-py` **4.0.2** 를 깔았다 (요구는 4.0.0) | ↓ 새로 깔면 만나는 오류 (돌려 본 뒤) |
| `mat1 and mat2 shapes cannot be multiplied` | **로라의 베이스 계열 ≠ 체크포인트 계열** | ↓ 새로 깔면 만나는 오류 (돌려 본 뒤) |
| 폰트를 깔았는데도 **아이콘이 깨짐** | **폰트가 아니라 브라우저** (Brave 깨짐 / Chrome 정상) | ↓ 새로 깔면 만나는 오류 (돌려 본 뒤) |
| sage 가 **어제까지 되다가 갑자기** 실패 | ComfyUI Manager 가 sageattention 을 교체함 | [ComfyUI 쓰는 법](comfyui.md) |
| 모델 '경량화' 했더니 **그림이 달라짐** | fp32→fp16 변환이라 결과가 달라진다 | ↓ 모델 '경량화' |
| **큐를 여러 개 쌓으면** GPU 대신 CPU 로 연산 | kohya GUI 설치기가 CUDA 를 덮어씀 | ↓ 학습 도구를 깔았더니 |
| 배경에 **얼굴이 덕지덕지 복제**됨 | 작가 태그 **조합** | ↓ 배경에 얼굴이 복제된다 |
| KSampler **프리뷰가 갑자기 나빠짐** | comfyui-frontend-package 1.10.17 이후 | [ComfyUI 쓰는 법](comfyui.md) |
| **앱 빌더를 쓴 뒤** 워크플로우가 깨져 보임 | Nodes 2.0 이 강제로 켜짐 | [ComfyUI 쓰는 법](comfyui.md) |
| CLIP 이 **설치돼 있는데 없다고** 함 | venv 상태가 꼬임 | ↓ 새로 깔면 만나는 오류 (설치·clone) |
| `Input type (c10::Half) and bias type (float)` | live preview 의 `approx NN` | ↓ 오류 문구 표 (A1111 계열) |
| `Expected all tensors to be on the same device` | `--medvram` 과 임베딩 충돌 | ↓ 오류 문구 표 (A1111 계열) |
| **파워쉘이 켜자마자 꺼짐** | 실행 정책 / 시스템 로캘 | ↓ 오류 문구 표 (A1111 계열) |
| llama-cpp-python 이 안 깔림 (VLM·TIPO) | 빌드 도구 설치 순서 | ↓ ComfyUI · 포터블 계열 표 |
| `CUDA error: the launch timed out and was terminated` | **미해결** | ↓ 아직 답이 없는 것 |
| 배경에 **사각형 노이즈** / 신체에 **세로줄 노이즈** / **도화지·유화 질감** | 여러 태그를 한 가중치 블록에 묶었다 (`3::a, b, c::`) | ↓ NAI 노이즈 |
| 네거티브가 **통째로 안 먹는다** | `cfg` 가 1.0 이다 (고속 로라·터보 모델) | [프롬프트 쓰는 법](prompting.md) |
| `uncensored` 를 넣어도 **김딱지 · 막대 얼룩** | **작가 태그**가 검열된 그림만 학습했다 | ↓ 검열이 안 풀린다 |
| 로라를 폴더에 넣었는데 **목록에 안 뜸** | 로드된 체크포인트가 **SDXL 계열이 아니다** | ↓ 로라가 목록에 안 뜬다 |
| ANIMA CLIPLoader `size mismatch ... embed_tokens.weight` | 구버전 ComfyUI 가 Qwen 인코더를 오인식 | [ANIMA](anima.md) |
| ANIMA 번역 워크플로우 `ValueError: invalid tokenizer` | ComfyUI 가 구버전 (gemma4 는 포터블 0210+) | [ANIMA](anima.md) |
| 받은 워크플로우가 **바로 오류**, 노드가 **핑크색** | 원작자의 **모델 파일**이 박혀 있다 | [ComfyUI 쓰는 법](comfyui.md) |
| 그림 대신 **노이즈만** 나온다 | v-pred 아닌 모델에 **`v_prediction` 이 켜져 있다** | [ComfyUI 쓰는 법](comfyui.md) |
| `Failed to get input node 0 for group node child` | ComfyUI 의 **그룹 노드** 처리 변경 (issue 8887) | ↓ ComfyUI · 포터블 계열 표 |
| `The size of tensor a (16) must match ... b (36)` | **Easy Cache 가 켜져 있다** (AUTO-WAN 계열) | [비디오 생성](video-generation.md) |
| `join() argument must be str ... not 'tuple'` | **Execution Order Controller 를 MMAudio 로더에 물렸다** | [비디오 생성](video-generation.md) |
| 텍스트 인코더가 **크기 불일치**로 안 돈다 (WAN) | `umt5_xxl_fp8_e4m3fn_scaled` 를 썼다 | [비디오 생성](video-generation.md) — **BF16 판을 쓴다** |
| **와일드카드가 같은 조합만** 반복된다 | `{ A \| B }` 는 랜덤이 아니라 **순차 사이클** | [ComfyUI 쓰는 법](comfyui.md) |
| 그림체 칸을 **9번 이상** 썼더니 워크플로우가 뻗음 | 배포본의 **상한이 0~8** 이다 | [ComfyUI 쓰는 법](comfyui.md) |
| `r` 을 누른 뒤 **드롭다운이 먹통** | ComfyUI 자체 버그 | **브라우저 새로고침** |
| 매니저가 **미싱 노드를 못 잡는다** | **데스크톱 버전**을 쓰고 있다 | **포터블 버전**으로 |
| **피부·얼굴이 도자기처럼** 뭉개진다 | 디테일러가 아니라 **업스케일 단계의 i2i** | [인페인팅](inpainting.md) |
| **세로 구도만 찐빠**가 잦다 (특정 로라) | **학습 데이터가 가로**(애니 캡처)다 | ↓ 낡았지만 살아 있는 규칙 |
| lineart adjuster 를 써도 **선 굵기가 안 바뀐다** | 원래 **굵기 조절이 아니다** | ↓ 낡았지만 살아 있는 규칙 |
| `git switch master` 가 `fatal: invalid reference` | **기본 브랜치가 `main`** 이다 | ↓ 오류 문구 표 (A1111 계열) |
| `CLIP 로드 유형에 krea2 가 없다` | 최신 모델이다 | **ComfyUI 업데이트** |
| TiledVAE 를 켰더니 **화질이 떨어진다** | **디코더 타일 크기**가 작다 | ↓ TiledVAE |
| `No module named mmdet.core` (ddetailer 계열) | mmdet **버전**이 안 맞는다 (torch 를 내릴 필요 없다) | ↓ 오류 문구 표 (A1111 계열) |
| triton·SageAttention 이 **몇 주째 안 깔린다** (Wan) | triton **최신판**을 깔았다 | ↓ ComfyUI · 포터블 계열 표 |
| 업데이트 후 깨져서 **소스를 되돌렸는데 그대로**다 | 문제가 소스가 아니라 **`venv` 안에** 있다 | ↓ 소스 롤백 ≠ venv 재생성 |
| LTX 2.3 워크플로우가 **로라를 못 찾는다** | 배포글 본문의 폴더명이 틀렸다 (`loras/LTX` → **`loras/ltx23`**) | [비디오 생성](video-generation.md) |
| Anima 로 i2i 를 돌렸더니 **캐릭터 인상이 딴판**이 됐다 | `denoise 0.5` — **거의 금기다** | [ComfyUI 쓰는 법](comfyui.md) |
| NAIA 에서 **그림체 없는 랜덤 태그 짤**만 나온다 | 자동 생성이 **빈 프롬프트 엔지니어링으로 메인을 덮어썼다** | [NovelAI](nai.md) |
| NAI 에서 **야짤이 안 나온다** | **`c` 로 시작하는 모델**(Curated)은 NSFW 가 안 나온다 | [NovelAI](nai.md) — 모델을 바꾸고 `nsfw, uncensored` |
| 작가 태그를 썼는데 **흑백만** 나온다 | 그 작가가 **흑백 만화만** 그린다 | [프롬프트 쓰는 법](prompting.md) — 긍정에 `cover image` |
| 네거티브에 `large breasts` 를 넣었더니 **인물이 어려졌다** | 크기 대신 **나이 축이 끌려간다** | [프롬프트 쓰는 법](prompting.md) — negpip 으로 `(large breasts:-1.5)` |
| 와일드카드 세트를 풀었는데 **아무것도 안 뽑힌다** | 폴더째 풀어 `__폴더명/RANDOM__` 이 됐다 | [프롬프트 쓰는 법](prompting.md) — 루트에 평평하게 |
| 베니스 `Grok Imagine 1.5 Private blocked this content.` | **2026-06-03 부터 NSFW 검열**이 걸렸다 | [비디오 생성](video-generation.md) — 우회 없음 |
| 어느 날부터 **선이 지저분하게 뭉개져** 나온다 | **UNET weight dtype 이 `fp8_e4m3fn`** 이다 | ↓ 결과물이 이상할 때 |
| 그림 전체가 **희뿌옇게** 변하며 그림체가 무너진다 (WAI·naiXL vpred) | 학습이 얕은 태그에 **가중치를 높게** 줬다 | ↓ 결과물이 이상할 때 |
| ANIMA 에서 **crotch 에 겹선**이 계속 나온다 | **베이스 모델 특성** — 프롬프트로 해결 불가 | ↓ 결과물이 이상할 때 |
| `Value not in list` | 워크플로우에 박힌 **로라·업스케일·디텍터 이름**이 내 폴더에 없다 | ↓ ComfyUI · 포터블 계열 표 |
| `float object cannot be interpreted as an integer` | **`Random Number` 노드** (굿나잇 랜덤 v1.5) | ↓ ComfyUI · 포터블 계열 표 |
| `prompt_outputs_failed_validation` (NAIA → ComfyUI) | API 로 넘긴 워크플로의 **커스텀 노드 필수 입력이 비었다** | ↓ ComfyUI · 포터블 계열 표 |
| 누락 노드를 다 깔았는데 **`workflowgroup` 이 없다** | 설치 전 상태의 워크플로가 남아 있다 | ↓ ComfyUI · 포터블 계열 표 |
| 디테일러가 **"부정 프롬을 연결하라"** 고 뜬다 | 워크플로우에서 **부정 프롬이 긍정에 연결**돼 있다 | [ComfyUI 쓰는 법](comfyui.md) |
| **디테일러를 걸면 로라가 빠져** 눈·얼굴이 바뀐다 | 체크포인트가 **로라를 거치지 않고 디테일러로 직결**돼 있다 | [ComfyUI 쓰는 법](comfyui.md) |
| ddetailer 2차에서 **와일드카드·LoRA 가 씹힌다** | 처리 순서 문제 — **미해결** | ↓ 오류 문구 표 (A1111 계열) |
| `OMP: Error #15: ... libiomp5md.dll already initialized` | OpenMP 런타임 **중복 링크** | ↓ 오류 문구 표 (A1111 계열) |
| DirectML(AMD·인텔)에서 **창이 바로 꺼진다** | 실행 인자에 **`--xformers`** 가 있다 | ↓ 오류 문구 표 (A1111 계열) |
| Negpip 이 **아예 안 먹는다** | 문법 — **콜론 앞 쉼표**가 빠졌다 (`(black,:-1.7)`) | [ComfyUI 쓰는 법](comfyui.md) |
| 첨부 이미지에서 **워크플로가 안 불러와진다** | 업로드·저장 과정에서 **EXIF 소실** | [ComfyUI 쓰는 법](comfyui.md) |
| Wan2.2 연속 생성이 **시작조차 안 된다** | **긍정 프롬프트가 비어 있다** (본문 설명이 틀렸다) | [비디오 생성](video-generation.md) |
| Impact `SAMLoader` 가 **모델을 못 찾는다** | 경로가 `Models/sams` 인데 기본 폴더는 `models/sam` | [비디오 생성](video-generation.md) — 폴더를 직접 만든다 |
| I2V 결과가 **갑자기 3D 렌더**처럼 나온다 | SmoothMix 의 **`t2v` 모델을 i2v 자리**에 넣었다 | [비디오 생성](video-generation.md) |
| Bernini I2V 의 **첫 프레임이 바뀐다** | 버그가 아니라 **Semantic Planner 의 재해석** | [비디오 생성](video-generation.md) |
| MiniMax H3 에서 **최적화 노드가 하나도 안 먹고** 계속 실패 | 여러 모델을 쓰다 **커스텀 노드가 꼬였다** | ↓ H3 에서 최적화가 통째로 안 먹을 때 |
| 터보 LoRA 를 얹으면 **오류 메시지가 잔뜩** 뜬다 (H3) | **pruned 모델**이라 참조할 키가 일부 없다 | [비디오 생성](video-generation.md) — **무시해도 되고 로라는 작동한다** |
| H3 **비디오 레퍼런스**를 넣었더니 4시간이 걸린다 | MP 설정이 아니라 **레퍼런스 영상의 실해상도** | [비디오 생성](video-generation.md) — **720 이하로 줄여 넣는다** |
| H3 R2V 에서 **이미지 속 캐릭터를 안 가져온다** | `<Subject 1>` 토큰만 적었다 | [비디오 생성](video-generation.md) — **외형 설명을 함께** 적는다 |
| H3 R2V 결과가 **원본 영상 그림체**를 따라간다 | 레퍼런스의 **역할 선언**이 없다 | [비디오 생성](video-generation.md) — `<Picture 1>` = character / `<Video 1>` = scene |
| MMAudio 오디오가 **1초 짧게** 잘린다 | 영상을 **24fps** 로 맞췄다 | [비디오 생성](video-generation.md) — **25fps 다** |
| MMAudio 싱크가 안 맞는다 (force_rate 를 줬는데도) | `video info` 의 **source fps 를 연결**했다 | [비디오 생성](video-generation.md) — **출력 fps 에 25 를 직접 입력** |
| deno 커스텀 노드가 **빨간 불만 뜨고 즉시 끝난다** (LTX) | **로라 매니저에 미보유 로라**가 있다 (off 여도 중단) | ↓ ComfyUI · 포터블 계열 표 — **Remove 로 뺀다** |
| LTX 워크플로우의 **프롬프트 미리보기가 안 바뀐다** | **메뉴얼 프롬프트 칸에 글자가 있다** | [비디오 생성](video-generation.md) — LLM 을 쓰려면 **비운다** |
| SVI 워크플로우 `[GetNode] ✗ Variable 'model_low' not found!` | 모델이 안 들어갔거나 Get/Set 노드가 꼬였다 | ↓ ComfyUI · 포터블 계열 표 |
| WAN 다단 워크플로 결과가 **뭉개진다** | 실행 순서를 `시작 → wan-hires → 1차` 로 했다 | [비디오 생성](video-generation.md) — **`시작 → 1차 → wan-hires`** |
| I2I 일관성 워크플로 결과에 **녹색 마스크가 침범** | 빈 이미지 노드의 기본색이 `6796102`(녹색) | [비디오 생성](video-generation.md) — 안 겹치는 색으로 교체 |
| `1280x720` 을 넣었는데 **`1280x704`** 가 된다 | WAN 계열은 **16·32의 배수 해상도만** 처리한다 | [비디오 생성](video-generation.md) |
| Smooth Mix WAN 이 **아날로그 TV 노이즈**처럼 나온다 | GGUF 가 아닌데 **`unet` 폴더**에 넣었다 | [비디오 생성](video-generation.md) — `diffusion_models` + 확산 모델 로드 |
| ANIMA 양자화 모델의 **배경·소품 디테일이 어긋난다** | **레이어 선별 없이 기본 설정으로** 양자화했다 | [ComfyUI 쓰는 법](comfyui.md) |
| AMD 에서 **flash-attn 이 아예 동작하지 않는다** | `FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE` 미설정 | [ComfyUI 쓰는 법](comfyui.md) |
| AMD 에서 **VAE decode 중 VRAM 이 19GB 까지** 치솟는다 | ROCm 할당자 설정 | [ComfyUI 쓰는 법](comfyui.md) — `expandable_segments:True` 등 |
| 스펙트럼·SPEED 를 켰더니 **업스케일에서 노이즈**가 남는다 | 업스케일은 스텝이 적어 **스킵이 과해진다** | [ComfyUI 쓰는 법](comfyui.md) — 업스케일엔 미적용 모델 |
| 램이 남는데 **램 오프로딩이 안 돌고 OOM** (3090Ti·4090) | **NVIDIA 제어판의 ECC 가 켜져 있다** | ↓ ECC 를 켜 두면 램 오프로딩이 안 돈다 |
| 콘솔의 `Total VRAM` 이 같은 GPU 보다 **1.5GB 적게** 찍힌다 | 같은 원인 — ECC 가 VRAM 을 점유한다 | ↓ ECC 를 켜 두면 램 오프로딩이 안 돈다 |
| 같은 모델·같은 세팅인데 **외곽선이 흐리고 색감이 다르다** | **이름만 같고 해시가 다른 VAE** | ↓ 재현이 안 될 때는 파일명이 아니라 해시로 |
| `Required input is missing: model_patch` | `Apply Anima ControlNet-LLLite` 가 **커스텀 → 내장 노드로 바뀌었다** | ↓ 노드가 내장으로 바뀌었을 때 |
| 위를 고쳤더니 strength 가 **NaN** / `Failed to convert an input value to a FLOAT value` | 구버전 워크플로우의 **위젯 배치가 밀렸다** | ↓ 노드가 내장으로 바뀌었을 때 — **값을 고치지 말고 노드를 새로 불러온다** |
| `[DCW] Warning: correction skipped at this step` | 디테일러 구간 · **8의 배수인데 2로 나누면 홀수인 해상도**(1208 등) | [ComfyUI 쓰는 법](comfyui.md) — 노드 업데이트 |
| SAM3 노드가 `'NoneType' object has no attribute 'data'` | 커스텀 노드 최신 커밋이 깨졌다 | ↓ SAM3 커스텀 노드 되살리기 |
| SAM3 가 `InvalidHeaderDeserialization` | **모델 파일이 깨졌다** (위와 **별개 오류**) | ↓ SAM3 커스텀 노드 되살리기 |
| `MaskDetailerPipe` 에서 `'Tensor' object has no attribute 'copy'` | **SAM3 노드 연결 실수** | [디테일러](detailer.md) |
| 원클릭 코랩이 **rife49.pth 를 못 받아** 멈춘다 | `vfi_utils.py` 의 다운로드 URL 세 개가 전부 죽었다 | ↓ ComfyUI · 포터블 계열 표 |
| Qwen-Image-Edit 결과가 **새까맣게** 나온다 | Sage 충돌 / fp8 가속 충돌 / **RTX 20 시리즈** | [ComfyUI 쓰는 법](comfyui.md) |
| `ReferenceLatent` · `CFGNorm` · `TextEncodeQwenImageEditPlus` 가 **없다**고 뜬다 | 커스텀 노드가 아니라 **ComfyUI 본체가 낡았다** | **본체 업데이트** |
| `JWImageSaturation` 이 없다 (Optical Realism) | 제작자가 곁들인 **남의 노드**일 뿐이다 | [인페인팅](inpainting.md) — **지우고 써도 된다** |
| 업스케일했더니 **없던 유두·복근 줄**이 생긴다 | **USDU 의 타일 분할** — denoise 를 낮춰도 안 된다 | [업스케일과 화질](upscale.md) |
| 인페인트했더니 **아예 새 그림**이 그려진다 | **여러 곳을 한꺼번에 마스킹**했다 | [인페인팅](inpainting.md) — 한 번에 한 군데씩 |
| 인페인트한 자리만 **피부톤이 어긋난다** | latent 를 만드는 노드가 인페인팅용이 아니다 | [인페인팅](inpainting.md) |
| `mat1 and mat2 shapes cannot be multiplied (308x2048 and 768x320)` | **SD1.5 용 컨트롤넷을 SDXL·포니에** 물렸다 | [컨트롤넷](controlnet.md) |
| 디테일러가 **마스크 밖 엉뚱한 영역**을 그린다 | **컨트롤넷이 크롭 전 좌표를 밀어 넣는다** | [디테일러](detailer.md) — 연결을 끊는다 |
| 인텔 내장에서 `text encoder model load` 에서 **멈춘다** | **애로우레이크-S 데스크톱 내장** — 지원 목록을 믿을 수 없다 | [설치와 환경 구성](install.md) |
| `--fast cublas_ops` 를 붙였는데 **아무 변화가 없다** | 그 인자는 **별도 패키지가 있어야만** 동작한다 | [설치와 환경 구성](install.md) — `pip show cublas_ops` |
| `No detections found for prompt: ...` → `[MaskToQuad] 윤곽선을 찾지 못했습니다` | ComfyUI-SAM3 가 대상을 못 잡는다 | **`comfyui-easy-sam3` 로 교체**해 성공한 사례 |


<small>근거 — [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865) · [WAN2.2 I2I 일관성 통일 워크플로우 26.01](https://arca.live/b/aiart/160425811) · [ComfyUI 뉴 원클릭 로컬 리터칭 V4A 워크플로우 26.01](https://arca.live/b/aiart/159742122) · [Ultimate SNS generator 만들어서 공유해봄 26.05](https://arca.live/b/aiart/170679152)</small>

??? note "근거 105건 전부 보기"
    [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!… 24.07](https://arca.live/b/aiart/111903865) · [WAN2.2 I2I 일관성 통일 워크플로우 26.01](https://arca.live/b/aiart/160425811) · [ComfyUI 뉴 원클릭 로컬 리터칭 V4A 워크플로우 26.01](https://arca.live/b/aiart/159742122) · [Ultimate SNS generator 만들어서 공유해봄 26.05](https://arca.live/b/aiart/170679152) · [Ie 아티스트 로라 v2 만듬 + 쓸만한 툴 로라 추천 25.01](https://arca.live/b/aiart/127368119) · [nai 가이드 팁&자주 묻는 질문 (완) 25.10](https://arca.live/b/aiart/151423873) · [ILXL) 말랑이 선생님의 랜덤 와일드카드 모음집 공유 25.01](https://arca.live/b/aiart/125265456) · [NAIA를 처음 접하는 사람에게 - NAIA의 첫걸음 ~ 프… 25.11](https://arca.live/b/aiart/154179363) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [NAI) 이런 노이즈는 「 3::???, ???:: 」 가중… 25.07](https://arca.live/b/aiart/143845479) · [ComfyUI에서 이미지 누끼 따고, 그 안에 다른 이미지를… 26.03](https://arca.live/b/aiart/165751166) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [NSFW 애니메이션 신모델 Anima 26.01](https://arca.live/b/aiart/161150715) · [(가이드) 뉴비 자주 묻는 질문 (FAQ) 23.01](https://arca.live/b/aiart/68598675) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [Anima 초보자 자연어(한국어) 프롬프트 워크플로우 26.05](https://arca.live/b/aiart/171167219) · [원하는 위치, 원하는 로라 23.05](https://arca.live/b/aiart/76318653) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [Krea2 edit LoRA 간단 후기 26.07](https://arca.live/b/aiart/177257973) · [UncannyValley V-pred v1 출시 25.06](https://arca.live/b/aiart/140017939) · [베니스 결제 및 사용법이었는데 검열먹었다함 26.06](https://arca.live/b/aiart/172694842) · [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜… 25.05](https://arca.live/b/aiart/137508828) · [로컬의 희망 Smooth Mix Wan 2.2 모델 공유 25.10](https://arca.live/b/aiart/149889518) · [커스텀노드) ComfyUI-LLM-Helper 26.06](https://arca.live/b/aiart/174631586) · [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780) · [Wan2.2 연속 영상 생성 + 병합 워크플로우 공유 (We… 25.08](https://arca.live/b/aiart/146168826) · [딸깍 AUTO-WAN+디테일러+사운드(MMAudio) 워크플… 25.11](https://arca.live/b/aiart/153525536) · [ComfyUI 뉴비의 초간단 regional 분리 방법(영역… 25.08](https://arca.live/b/aiart/145827191) · [ComfyUI 초보자를 위한 워크플로우 사용 가이드 25.07](https://arca.live/b/aiart/141704804) · [SAM3 해결했다.. 26.03](https://arca.live/b/aiart/166035589) · [LTX 2.3 워크플로우 V2 공유 및 팁 정리 26.06](https://arca.live/b/aiart/172671768) · [DDSD Postprocessing 업데이트 23.04](https://arca.live/b/aiart/74887800) · [초보자용 LTX2.3 워크플로우 26.06](https://arca.live/b/aiart/172768105) · [Wan2.2 노트북 4070 8g 짜리 돌리는 워크 공유 25.08](https://arca.live/b/aiart/145496771) · [LTX2.3 워크플로우 공유 26.07](https://arca.live/b/aiart/177971843) · [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림… 25.12](https://arca.live/b/aiart/157410060) · [기초) 모델들 용량 줄이는 방법 (병합 활용 7GB->4GB) 23.02](https://arca.live/b/aiart/68966157) · [(-) DirectML을 사용해 윈도우 환경에서 AMD 라데… 23.03](https://arca.live/b/aiart/72113936) · [ComfyUI-DCW 노드업뎃 26.05](https://arca.live/b/aiart/169518554) · [WAN 2.2 SVI PRO 15초+올라마 자동 프롬프트+컬… 26.01](https://arca.live/b/aiart/159309952) · [스팩트럼기반 최적화 노드 26.03](https://arca.live/b/aiart/165070655) · [(워크플로우 공모전) 라면보단 어렵더라! 3트째 간편 워크플… 25.07](https://arca.live/b/aiart/141180724) · [저처럼 forge neo쓰다가 여러 문제를 겪으시는분들 혹시… 26.06](https://arca.live/b/aiart/174448928) · [순정webui에서 v-pred모델쓰기 25.02](https://arca.live/b/aiart/128472488) · [WAN 2.2 SVI 올라마 자동프롬프트 15초 워크플로우 … 26.01](https://arca.live/b/aiart/160056290) · [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 … 26.08](https://arca.live/b/aiart/179176367) · [NaN 오류 체크리스트 23.01](https://arca.live/b/aiart/68478526) · [페) ILXL) TiledVAE 관련 미세? 실험 24.10](https://arca.live/b/aiart/119251783) · [EasyUseAnima 0.3.1: 버그픽스, 업스케일, P… 26.07](https://arca.live/b/aiart/176029127) · [Anima+IL 아님. IL+Anima임. 26.05](https://arca.live/b/aiart/171656386) · [미니맥스 r2v로 만든것 26.08](https://arca.live/b/aiart/179207537) · [물리 기반 이미지 후처리 노드 이거 좋다 26.03](https://arca.live/b/aiart/164468269) · [AI그림 채널 오류 해결책 모음 23.02](https://arca.live/b/aiart/70417374) · [ComfyUI 램 오프로딩(RAM Offloading) EC… 26.01](https://arca.live/b/aiart/161052343) · [딸깍 AUTO-WAN 워크플로우 업데이트함 (순서 제어) 25.11](https://arca.live/b/aiart/154065928) · [(ComfyUI) Latent Hires Fix 사용시 그림… 23.09](https://arca.live/b/aiart/86901822) · [특정 작가태그(주로 NSFW 관련)에서 흑백이 자주 나올때 … 25.06](https://arca.live/b/aiart/141015266) · [모르고 쓰면 해골물인 ComfyUI 옵션 26.07](https://arca.live/b/aiart/177447677) · [ComfyUI 워크플로우 - SAM3, 마스크 디테일러로 활… 25.12](https://arca.live/b/aiart/157473218) · [인텔 Arc GPU용 ComfyUI windows-porta… 26.04](https://arca.live/b/aiart/168348535) · [AMD R9700 attention 별 생성속도 26.06](https://arca.live/b/aiart/173409804) · [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172) · [(워크플로우 공모전) 라면 어쩌고 저쩌고 실전압축 워크플로우… 25.07](https://arca.live/b/aiart/141718826) · [SAM3 컨트롤넷 인페인팅 워크플로우 일부 개선 (컨트롤넷과… 26.04](https://arca.live/b/aiart/168604584) · [미니맥스 4스텝 터보로라 돌려봄 26.08](https://arca.live/b/aiart/179108697) · [내가 쓰고있는 ComfyUI 워크플로우 공유 (SDXL, A… 26.08](https://arca.live/b/aiart/179640921) · [AnimateDiff 때 돌려본 래퍼런스 영상을 R2V 해보… 26.08](https://arca.live/b/aiart/179265081) · [comfyui Starnodes 양자화 노드 26.07](https://arca.live/b/aiart/176070719) · [로컬 성인여성 작은가슴 만들기 쉬움 25.12](https://arca.live/b/aiart/156681380) · [(후타주의) Bernini 모델 I2V의 첫프레임이 변하는 … 26.06](https://arca.live/b/aiart/173025640) · [뭣같은 wan2.1 triton + sageattention… 25.04](https://arca.live/b/aiart/133924449) · [ddetailer 프롬 입력+ cfg스케일 조정 버전 23.03](https://arca.live/b/aiart/72119679) · [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 v1.5 25.07](https://arca.live/b/aiart/142088366) · [rife49.pth 버그제보 - 원클릭 코랩 실행 안되는 사… 26.02](https://arca.live/b/aiart/162972850) · [(pony) 원피스 애니 와노쿠니 스타일 로라 공유 24.07](https://arca.live/b/aiart/112312429) · [z-tipo-extension 설치 및 tipo 파일 수정 26.02](https://arca.live/b/aiart/162039111) · [MMaudio 싱크 맞추는법 25.10](https://arca.live/b/aiart/151497792) · [MMaudio 싱크 관련 추가정보 25.11](https://arca.live/b/aiart/152614659) · [comfyui 앱모드 사용법 26.05](https://arca.live/b/aiart/171528258) · [어제 있었던 개같은 얼굴 복제 현상 해결 후기 25.03](https://arca.live/b/aiart/131650885) · [EreNodes 자동완성 한국어 입력버그 수정본 26.01](https://arca.live/b/aiart/161031716) · [ComfyUI - 검열이나 가리는게 있다면 사용하는 단부루 … 25.12](https://arca.live/b/aiart/158273723) · [webui fail 뜨면서 실행안되는 오류 해결법 26.02](https://arca.live/b/aiart/162800946) · [아 미맥 비디오 레퍼 모르겠다 26.08](https://arca.live/b/aiart/179453440) · [오늘 업뎃해서 오류나는 챈럼들을 위한 이전버전 링크 23.03](https://arca.live/b/aiart/72586603) · [ComfyUI 에서 bjornulf_custom_nodes … 26.02](https://arca.live/b/aiart/163272564) · [reforge 설치시 오류 해결법 중 꽤 유용한거 있어서 갖… 26.03](https://arca.live/b/aiart/164173886) · ['갑자기' comfy 에서 sage-attension 실패하… 26.03](https://arca.live/b/aiart/163926460) · [KSampler 프리뷰 해상도 수정해주는 커스텀 노드 Com… 26.02](https://arca.live/b/aiart/161467109) · [와 comfyui 다시 깔고 H3 돌리니깐 최적화 전부 먹히… 26.08](https://arca.live/b/aiart/179172801) · [정보탭의 kohya gui 설치후 발생한 문제해결 26.07](https://arca.live/b/aiart/176818115) · [선 지저분하게 나오는 문제 해결! 26.07](https://arca.live/b/aiart/178281311) · [파이토치 설치 안되는사람 보셈 23.02](https://arca.live/b/aiart/69972082) · [comfyui 인페인트 질문 26.05](https://arca.live/b/aiart/171032438) · [뉴비 특정 lora만 안 돌아가는 문제가 있슴 23.01](https://arca.live/b/aiart/68448644) · [comfyui inpaint turbo 워크플로우 관련 질문 26.07](https://arca.live/b/aiart/177370189) · [comfy에서 anima로 돌리는데 계속 crotch 쪽 찐… 26.07](https://arca.live/b/aiart/176433146) · [ComfyUI - 와일드카드 복습 25.11](https://arca.live/b/aiart/155383963) · [ComfyUI 최신버전에서 MiniMaxH3-Cache 버그… 26.08](https://arca.live/b/aiart/179251955) · [외곽선이 명확하게 그려지지 않는 이유 26.05](https://arca.live/b/aiart/171512796) · [comfyui 업스케일러 이 미친놈 대체 왜이러는걸까 26.05](https://arca.live/b/aiart/172185043) · [페?)왜 갑자기 3D로 넘어가는 것일까요 26.06](https://arca.live/b/aiart/172447183) · [NAIA로 Comfy + 아니마를 써보려는데 사용법을 잘 모… 26.06](https://arca.live/b/aiart/173906125) · [WAI로 그림 뽑다 보면 종종 마주치는 문제 26.06](https://arca.live/b/aiart/173511292) · [nai로 뽑은걸 컴피로 수정하고 싶어요 26.06](https://arca.live/b/aiart/173477606)

## 그다음 — 오류 메시지 읽는 법 (마지막 문장이 해결책이다)
<small>⚠️ 2023-05 기준 · 근거 2건</small>

채널에서 가장 자주 나오는 조언이 이것이다. **영어라고 겁먹고 스크롤을 내리지 말고, 오류 메시지의 마지막 부분을 읽어라.** 대개 거기에 해결책이 그대로 적혀 있다 (75960531, 2023-05).

**실례** — 아래 오류를 통째로 보자.

```
modules.devices.NansException: A tensor with all NaNs was produced in Unet.
This could be either because there's not enough precision to represent the picture,
or because your video card does not support half type.
Try setting the "Upcast cross attention layer to float32" option in Settings > Stable Diffusion
or using the --no-half commandline argument to fix this.
Use --disable-nan-check commandline argument to disable this check.
```

앞 두 줄은 증상과 원인이고, **뒤 두 줄이 곧 해결책**이다.

1. `설정 > Stable Diffusion` 에서 **`Upcast cross attention layer to float32`** 를 체크하거나
2. `webui-user.bat` 에 **`--no-half`** 를 추가한다

마찬가지로 `OutOfMemoryError` 같은 이름은 **그 자체가 검색 키워드**다.

**오류가 주르륵 뜰 때** — 답이 없어 보이지만 대개 연쇄 반응이다. **목록 맨 위에 있는 최초 오류부터** 풀면 얼마 안 가 해결된다 (63591884, 2022-11).

**그래도 모르겠으면 물어보기 전에 이것부터** — 원문이 정리한 체크리스트다.

| | 확인 |
|---|---|
| 1 | 문제의 키워드를 공지와 정보 탭에서 **검색**해 봤는가 |
| 2 | 검색해도 모르겠다면 **명료한 정보**를 제공했는가 |
| 3 | 오류가 났다면 **마지막 부분의 문장**을 확인했는가 |
| 4 | 말머리를 `[질문]` 으로 설정했는가 |

**'명료한 정보'는 육하원칙 중 셋이면 된다.**

| | 무엇을 적나 |
|---|---|
| **어디서** | 코랩·런팟·로컬·원클릭·통합팩 등 어떤 환경인지 |
| **무엇을** | 로라를 썼는지, 고해상도 보정을 했는지, 디테일러를 썼는지 |
| **어떻게** | 그 값들을 얼마로 줬는지, Torch+cuda+cudnn+xformers 버전 |

> 더 간단히 말하면 **'EXIF 제공'** 이다. 브라우저 화면을 캡처하고 **CMD(검은 창) 내용을 복사해 붙이면** 대부분 해결책을 받을 수 있다. 이미지를 첨부할 때는 반드시 **EXIF 보존을 체크**하고 올린다.

**댓글의 마지막 수단** — 스크립트 오류 대부분은 **오류 문구를 그대로 GPT 에 붙여 넣으면** 해결 방법을 알려 준다.

→ [국룰](kukroul.md) · [처음이라면](overview.md)


<small>근거 — [질문에 답변이 안달린다구? 답변 잘 받는 꿀팁 대공개 (6/… 23.05](https://arca.live/b/aiart/75960531) · [Web UI 통합팩 설치 오류 드디어 해결했습니다. (방법 … 22.11](https://arca.live/b/aiart/63591884)</small>

## 오류 문구 → 원인 → 해결 표 (A1111 계열)
<small>2026-08 기준 · 근거 17건 · 자료 엇갈림</small>

2022~2023년에 정리된 대응표들이지만, **오류 문구와 대응 인자의 짝은 지금도 상당수 그대로 통한다.** 도구(A1111·kohya_ss)는 대체됐어도 문구는 남아 있으니 검색용으로 쓴다.

| 오류 문구 | 원인 | 해결 |
|---|---|---|
| `Torch is not able to use GPU` | GPU 인식 실패 | `--skip-torch-cuda-test` → 그래도 같으면 `--precision full --no-half`. **다만 이 인자를 두고 채널 안에서 말이 갈린다 → 아래 별도 항목** |
| `RuntimeError: CUDA error: no kernel image is available for execution on the device` | **RTX 50(블랙웰)에 A1111 master 브랜치** | dev 브랜치로: `git switch dev` → `git pull` → [설치와 환경 구성](install.md) |
| 같은 문구인데 `... at line 167 ... bitsandbytes\csrc\ops.cu` | **kohya_ss 학습에서 `Use 8bit adam`** | `Use 8bit adam` 체크 해제 (파스칼·Titan XP 는 xformers 도 함께 끔) → [로라 쓰는 법](lora-usage.md) |
| `python launch unsuccessful` / `Couldn't launch python` / `exit code: 9009` | 파이썬 설치 시 **`Add python to PATH` 미체크** | `webui-user.bat` 의 `set python=` 뒤에 `python.exe` 전체 경로를 넣는다 |
| `ModuleNotFoundError` | 모듈 없음 | `pip install 모듈명` → 안 되면 `pip list` / `pip show 모듈명` 으로 위치를 찾아 그 폴더를 `stable-diffusion-webui` 로 복사 |
| `ImportError` 계열 | 파일이 정상적으로 받아지지 않음 | 문제가 된 폴더(예: `venv`)를 **지우고 재설치** |
| 피클 악성코드 감지 에러 | safe unpickle 검사 | `--disable-safe-unpickle` |
| `zipfile.BadZipFile: File is not a zip file` | 받다 만 huggingface 캐시와 충돌 | `C:\Users\사용자명\.cache` 의 **huggingface 폴더 삭제** 후 재실행 |
| `OSError: Unable to load weights from pytorch checkpoint file` | 같은 원인 | `C:\Users\사용자명\.cache` 삭제 |
| `RuntimeError: DefaultCPUAllocator: not enough memory` | **시스템 RAM** 부족 | 다른 프로그램을 전부 내리거나 **pruned/fp16 경량 모델** 사용 |
| `MemoryError` / `you tried to allocate xxxx bytes` | 시스템 RAM 부족 | **가상 메모리를 늘린다** → 아래 메모리 항목 |
| `OSError: [WinError 1455] 이 작업을 완료하기 위한 페이징 파일이 너무 작습니다` | 페이징 파일 부족 | 가상 메모리를 늘린다 (사용자 지정보다 **시스템 관리**가 나은 경우가 있다) |
| `CUDA out of memory` | **VRAM** 부족 | `--medvram` / `--lowvram`. 그래도 안 되면 배치·해상도를 줄인다 |
| `OSError: [WinError 126] Error loading c10.dll` / `Microsoft Visual C++ Redistributable is not installed` | VC++ 재배포 패키지 없음 | `https://aka.ms/vs/16/release/vc_redist.x64.exe` 설치 |
| `Restoring base VAE` (로그) | VAE 가 안 걸림 | 아래 VAE 항목 |
| `RuntimeError: Cannot add middleware after an application has started` | fastapi 신규 버전과의 비호환 | **지금은 WebUI 를 업데이트하면 해결된다**(2023-03-14 갱신). 옛 처방은 `cache/virtualenv/Scripts` 에서 `./Activate.ps1` 후 `pip install --upgrade fastapi==0.90.1`(또는 0.90.0). ⚠ **파워쉘이 켜자마자 꺼져 그 명령조차 못 치는** 사례가 있었고, 그때는 fastapi 0.89.1 폴더와 `fastapi-0.89.1.dist-info` 를 `stable-diffusion-webui\venv\Lib\site-packages` 에 덮어쓰는 우회를 썼다 — 다만 **site-packages 에 fastapi 폴더 자체가 없던 케이스는 해결되지 않았고**, 덮어쓴 뒤 `AttributeError: 'App' object has no attribute 'debug'` 가 뜬 사례도 있다 |
| `.ckpt` 파일이 없다 | **실행기·통합팩은 모델을 포함하지 않는다** | 모델을 따로 구해 `models\Stable-diffusion` 에 넣는다. '실행기와 모델은 별개'라는 구분은 ComfyUI 에서도 같다 |
| `RuntimeError: Input type (c10::Half) and bias type (float) should be the same` | **live preview 옵션의 `approx NN`** | 미리보기 방식을 **`full` 또는 `cheap`** 으로 바꾼다 |
| `RuntimeError: Expected all tensors to be on the same device` | **`--medvram` / `--lowvram` 이 임베딩과 충돌**하는 이슈 | `webui-user.bat` 에서 **`--medvram` 을 지운다** |
| `styles.csv` utf-8 오류 | 파일 인코딩 | 메모장에서 **'다른 이름으로 저장'** → 인코딩을 **utf-8** 로 지정해 저장 |
| `AssertionError: extension access disabled because of command line flags` | 확장 설치를 막는 인자 | `webui-user.bat` 에 **`--enable-insecure-extension-access`** 추가 (또는 git 으로 수동 설치해 우회) |
| **파워쉘이 켜자마자 그냥 꺼진다** | 실행 정책 | 관리자 파워쉘에서 `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`. 그래도 꺼지면 **윈도우 언어 설정의 '유니코드를 지원하지 않는 프로그램용 언어'가 한국어인지** 확인(댓글) |
| 이미지 브라우저에서 **`move to i2i` 시 Error** | 널 처리 누락 | `modules/generation_parameters_copypaste.py` 의 `def image_from_url_text(filedata)` **첫 줄에** `if filedata == None: return None` 추가 |
| `Can't run without a checkpoint` | 모델 파일이 없다 | `models` 폴더에 `.ckpt` / `.safetensors` 를 넣는다 |
| kohya_ss 가 파이썬 버전(3.10.9 ↔ 3.10.6)이 안 맞는다 | tcl/tk 누락 | 제어판 > 프로그램 및 기능 > **Python 우클릭 > 변경 > Modify > tcl/tk 체크 > 적용**(댓글) |
| `fatal: invalid reference: master` (dev 브랜치에서 되돌릴 때) | **그 저장소의 기본 브랜치가 `master` 가 아니라 `main`** 이다 | `git switch main` → `git pull`. **되돌릴 때는 원래 브랜치명을 먼저 확인한다** → [설치와 환경 구성](install.md) |
| v-pred 모델을 골랐더니 **새까맣게 나온다** | 순정 A1111 이 v-pred 를 지원하지 않는다 | `git switch dev` → `git pull`. **Forge/reForge 는 이미 지원해 이 작업이 필요 없다** |
| `AssertionError: Extension directory already exists` | 확장 폴더가 남아 있다 | webui 를 끄고 `extensions` 폴더에서 **수동 삭제** 후 zip 수동 설치 |
| `ModuleNotFoundError: No module named segment_anything` / `groundingdino` | **CUDA 보다 확장을 먼저 깔았다** | `venv/lib/site-packages` 의 `groundingdino`·`segment_anything` 을 지우고 **CUDA → cuDNN → 확장** 순으로 다시 → [인페인팅](inpainting.md) |
| `No module named mmdet.core` (ddetailer·DDSD 계열) | **torch 를 1.7 로 내리라는 소문은 틀렸다.** torch 2.0 에서도 **mmdet 버전만** 맞추면 된다 | `pip install -U openmim==0.3.7` → `pip install mmcv-full==1.7.1` → `pip install mmdet==2.28.2`. 그래도 안 되면 ↓ '`mmdet.core` 한 줄 교체' |
| mmcv 컴파일이 **계속 실패**한다 | 빌드 환경 | **ddetailer 판을 붙들지 말고 adetailer 판을 쓴다** — bbox 크기가 조금 다를 뿐 기능은 같다는 것이 여러 댓글의 권고다 |
| DDSD 업데이트 후 **GUI 가 깨져 보인다** | `ui_config.json` 에 옛 초기값이 남았다 | webui 폴더의 **`ui_config.json` 에서 ddsd 관련 초기값을 지우고** webui 를 **완전히** 재시작 |
| DDSD 에서 생성을 **중단했더니 그 뒤로 꼬인다** | 내부적으로 모델 복구가 안 된다 | **WebUI 재실행**, 또는 **DDSD 를 끈 상태로 이미지를 한 번 생성**하면 복구된다 |
| `OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized` | **OpenMP 런타임이 중복 링크**됐다 | 환경변수 **`KMP_DUPLICATE_LIB_OK=TRUE`** (임시 회피책) |
| DirectML(AMD·인텔 GPU)에서 실행하면 **창이 바로 꺼진다** | 실행 인자에 **`--xformers`** 가 들어 있다 | **DirectML 에서는 xformers 를 쓸 수 없다.** `--xformers` 를 뺀다 |
| DirectML 인데 **`Invoke-Expression Command 매개 변수가 빈 문자열`** | AMD 인데 **CUDA 관련 의존성이 설치**됐다 | 환경을 다시 만든다 → [설치와 환경 구성](install.md) |
| **ddetailer 2차 처리에서 와일드카드(Dynamic Prompts)·LoRA 가 씹힌다** | **처리 순서** — webui 의 프롬프트 원문이 그대로 ddetailer 프롬프트로 들어간 **뒤에야** Dynamic Prompts 변환이 일어난다. 그래서 1차 얼굴에는 LoRA 가 반영되고 **2차로 다시 그린 얼굴은 LoRA 가 빠져 형태가 바뀐다** | **미해결.** 작성자도 방법을 찾지 못했다 (72119679, 2023-03) |
| 버전 강제 .bat 을 돌렸는데 **하단 버전 표시가 그대로다** | 설치가 안 된 것이다 | 설치가 오래 걸리니 **창이 저절로 닫힐 때까지 끄지 않는다.** 중간에 끄면 `지정된 모듈을 찾을 수 없습니다` 가 난다 |

> **인자를 넣는 곳** — `webui-user.bat` 을 메모장으로 열어 `set COMMANDLINE_ARGS=` 줄 뒤에 붙인다.

```bat
set COMMANDLINE_ARGS=--skip-torch-cuda-test --no-half --precision=full --listen --lowvram
```

(GTX 16xx 에서 `Torch is not able to use GPU` 가 났을 때 쓴 실제 조합이다.)

**에러 해결에는 운도 작용한다** — 원문의 조언이다. 오늘 안 되면 내일 다시 시도하고, 특히 **메모리를 할당하는 설치 단계에서는 다른 작업을 동시에 하지 말 것.**

→ ComfyUI 쪽 오류는 아래 '버전 충돌'·'노드 충돌' 항목


<small>근거 — [DDSD GUI 대폭 개선 및 기능 변경 23.04](https://arca.live/b/aiart/74470925) · [DDSD 대 업데이트 23.04](https://arca.live/b/aiart/74205817) · [kohya_ss 드림부스 기반 LoRA GUI 학습 사용법 23.01](https://arca.live/b/aiart/68205055) · [(구)원클릭 윈도우 실행기 23.01](https://arca.live/b/aiart/67307479)</small>

??? note "근거 17건 전부 보기"
    [DDSD GUI 대폭 개선 및 기능 변경 23.04](https://arca.live/b/aiart/74470925) · [DDSD 대 업데이트 23.04](https://arca.live/b/aiart/74205817) · [kohya_ss 드림부스 기반 LoRA GUI 학습 사용법 23.01](https://arca.live/b/aiart/68205055) · [(구)원클릭 윈도우 실행기 23.01](https://arca.live/b/aiart/67307479) · [원하는 위치, 원하는 로라 23.05](https://arca.live/b/aiart/76318653) · [파워셀 설정해도 자꾸 꺼져서 서버 연결 문제 해결 못한 사람… 23.02](https://arca.live/b/aiart/69516260) · [webui 자동좌가 직접 만든 실행기 23.01](https://arca.live/b/aiart/68257234) · [(구)torch2.1.2 xformers0.0.23 원클릭자… 23.05](https://arca.live/b/aiart/76553767) · [WebUI 에러 모음 22.12](https://arca.live/b/aiart/65362592) · [DDSD 추가 업데이트 23.04](https://arca.live/b/aiart/75057131) · [Web UI 통합팩 설치 오류 드디어 해결했습니다. (방법 … 22.11](https://arca.live/b/aiart/63591884) · [(-) DirectML을 사용해 윈도우 환경에서 AMD 라데… 23.03](https://arca.live/b/aiart/72113936) · [!!! 블랙웰 (RTX 50) 유저들 설치시 필독 !!! 25.05](https://arca.live/b/aiart/135962161) · [순정webui에서 v-pred모델쓰기 25.02](https://arca.live/b/aiart/128472488) · [AI그림 채널 오류 해결책 모음 23.02](https://arca.live/b/aiart/70417374) · [LoRA 설치시 Error 및 해결방법 정리 23.02](https://arca.live/b/aiart/70243793) · [ddetailer 프롬 입력+ cfg스케일 조정 버전 23.03](https://arca.live/b/aiart/72119679)

## 메모리가 모자란다 — 가상 메모리로 되는 것과 안 되는 것
<small>⚠️ 2023-02 기준 · 근거 7건</small>

**RAM 부족과 VRAM 부족은 다른 문제이고, 해결책도 다르다.** 이 구분을 못 해서 헛짓을 하는 경우가 많다.

| 무엇이 모자란가 | 대표 문구 | 되는 해결 |
|---|---|---|
| **시스템 RAM** | `MemoryError`, `you tried to allocate xxxx bytes`, `[WinError 1455] 페이징 파일이 너무 작습니다`, `DefaultCPUAllocator: not enough memory` | **가상 메모리(페이징 파일)를 늘린다.** 다른 프로그램을 내린다. pruned/fp16 모델을 쓴다 |
| **VRAM** | `CUDA out of memory` | `--medvram` / `--lowvram`, 배치·해상도 축소 |

> ⚠ **본문과 댓글이 갈리는 지점 — 댓글 쪽이 맞다.**
>
> 2022년 에러 모음글은 메모리 오류 전반에 "가상 메모리를 늘려라"라고 적었다. 그러나 댓글의 정정이 정확하다 — **`--medvram` 이나 `--lowvram` 을 쓰지 않는다면 가상 메모리를 아무리 올려도 VRAM 부족은 해결되지 않는다.** 가상 메모리는 **시스템 RAM 부족만 메우고 VRAM 부족은 메우지 못한다.** 결국 VRAM 이 큰 카드가 필요하다 (65362592 댓글, 2022-12).

**가상 메모리를 늘리는 곳** — 내 컴퓨터 우클릭 → 속성 → 고급 시스템 설정 → 고급 탭 성능 설정 → 고급 탭 → 가상 메모리 변경. 용량이 넉넉한 드라이브를 골라 사용자 지정 크기로 잡는다. 2023년 로라 학습글이 제시한 값은 **최소 100000MB / 최대 150000MB** 였다 (69186437). 다만 `[WinError 1455]` 계열에서는 **사용자 지정 대신 '시스템 관리'** 로 두는 편이 나은 경우가 있다는 보고도 있다 (70243793).

> SSD 수명 걱정에는 채널 답이 **"수명 괴담이니 그냥 켜라"** 였다.

**`--lowvram` / `--medvram` 이 하는 일**

- `--lowvram` 은 모델을 모듈로 쪼개 GPU 메모리에 하나씩만 올린다. 4GB 카드에서도 512x512 가 가능하지만 **RTX 3090 기준 일반 대비 약 10배 느리다.**
- `--medvram` 은 같은 배치에서 조건부/무조건부 노이즈 제거를 분리해 VRAM 을 크게 줄인다.

**껐는데도 VRAM 이 안 비워질 때** — WebUI·ComfyUI 를 종료했는데도 작업 관리자의 **'전용 GPU 메모리'** 가 꽉 찬 채 남아 `CUDA out of memory` 가 계속 나는 경우가 있다. CUDA 캐시를 비운다 (70658672, 2023-02).

```
pip install torch
python -c "import torch; torch.cuda.empty_cache()"
```

매번 치기 귀찮으면 `purge.bat` 으로 만들어 둔다.

```bat
@echo off
python -c "import torch; torch.cuda.empty_cache()"
```

> **한계도 분명하다** — 자기 GPU 사양을 넘는 작업의 OOM 은 이것으로 해결되지 않으며, 명령을 써도 전용 메모리가 안 줄었다는 제보도 있다. 확인은 작업 관리자에서 VRAM 수치가 떨어지는지 보는 것이다.

→ [VRAM·속도 최적화](vram.md)


### `CUDA out of memory` — 인자를 붙이기 전에 순서대로

VRAM 부족은 인자만이 답이 아니다. 2023년 채널 공식 '오류 해결책 모음' 이 제시한 순서가 지금도 유효하다.

| | 무엇을 |
|---|---|
| 1 | 설정 > **live previews** 의 `show live~` **체크 해제** |
| 2 | **batch size 1** |
| 3 | **hires fix 의 `Upscale by` 배수를 낮추거나 끈다** |
| 4 | 이미지 크기 축소 |
| 5 | **뒤에서 GPU 를 점유하는 프로그램** 확인 |

### 페이징 파일은 '얼마나' 만이 아니라 '어디에' 가 문제다

프리징 · 심한 렉 · `not enough memory` 가 나는데 램은 남아 도는 것 같다면,
**가상 메모리(페이징 파일)가 느린 HDD 에 잡혀 있는 것**이 원인일 수 있다.

```
내 컴퓨터 우클릭 → 속성 → 고급 시스템 설정 → 고급 → 성능 설정 → 고급 → 가상 메모리 변경
  '모든 드라이브에 대한 페이징 파일 크기 자동 관리'  해제
  HDD  →  '페이징 파일 없음'
  SSD  →  '시스템이 관리하는 크기'
  재부팅
```

⚠ **전부 해제하면 메모리 부족으로 실행 자체가 안 되니 주의.**

<small>근거 — [Lora 학습 실패로 자살하고 싶은 ㅈ밥 뉴비들만 이리와라 23.02](https://arca.live/b/aiart/69186437) · [CUDA out of memory. 전용 메모리 가비지 컬랙팅 23.02](https://arca.live/b/aiart/70658672) · [WebUI 쓸때 메모리 유출문제 해결방법 23.02](https://arca.live/b/aiart/69230678) · [WebUI 에러 모음 22.12](https://arca.live/b/aiart/65362592)</small>

??? note "근거 7건 전부 보기"
    [Lora 학습 실패로 자살하고 싶은 ㅈ밥 뉴비들만 이리와라 23.02](https://arca.live/b/aiart/69186437) · [CUDA out of memory. 전용 메모리 가비지 컬랙팅 23.02](https://arca.live/b/aiart/70658672) · [WebUI 쓸때 메모리 유출문제 해결방법 23.02](https://arca.live/b/aiart/69230678) · [WebUI 에러 모음 22.12](https://arca.live/b/aiart/65362592) · [Web UI 통합팩 설치 오류 드디어 해결했습니다. (방법 … 22.11](https://arca.live/b/aiart/63591884) · [AI그림 채널 오류 해결책 모음 23.02](https://arca.live/b/aiart/70417374) · [LoRA 설치시 Error 및 해결방법 정리 23.02](https://arca.live/b/aiart/70243793)

## 오류 문구 → 원인 → 해결 표 (ComfyUI · 포터블 계열)
<small>2026-08 기준 · 근거 47건</small>

위 표가 A1111 계열이라면, 이쪽은 **ComfyUI·포터블·커스텀 노드**에서 나오는 문구다.

| 오류 문구 / 증상 | 원인 | 해결 |
|---|---|---|
| `error: unable to create file ...: Filename too long` + `fatal: unable to checkout working tree` | **윈도우 260자 경로 제한.** 저장소에 지나치게 긴 파일명이 들어 있다 | 아래 '긴 경로 켜기' |
| `hipErrorInvalidValue` 를 뿜고 ComfyUI 가 죽음 (라데온) | gfx1200(RX 9000)·gfx1100(RX 7000) **장치 패키지 미설치** | `amd_torch_device_gfx12_0` 또는 `amd_torch_device_gfx110x` 를 추가 설치 → [설치와 환경 구성](install.md) |
| **공유받은 워크플로우가 그냥 터진다** | **sage-attention** — 뉴비 오류의 **범인 1위** | 아래 'sage-attention' |
| `import failed` — `soundfile` / `pyaudioop` 없음 | `pyaudioop` 은 파이썬에서 **삭제된** 라이브러리 | `soundfile` 과 대체 패키지 `audioop-lts` 를 포터블 파이썬으로 설치 |
| `... is not a supported wheel on this platform` (`cp312` whl) | 휠의 **파이썬 버전이 다름** | 파일명의 `cp312` 는 파이썬 **3.12 전용**이라는 뜻이다. 3.14 등에서는 설치되지 않는다 |
| `.\python_embeded\python.exe` 를 인식하지 못한다 | 이미 `python_embeded` 안에서 명령을 실행하면서 경로에 다시 `python_embeded` 를 붙여 **이중 경로**가 됐다 | 명령은 **포터블 최상위 폴더** 기준이다 |
| pip 로 깔았는데 ComfyUI 가 못 찾는다 | **시스템 파이썬**에 깔았다 | 아래 '포터블에서는 임베디드 파이썬' |
| `ERROR: Could not find a version that satisfies the requirement comfy-attn` | `requirements.txt` 에 배포되지 않는 패키지가 적혀 있다 | 해당 줄을 지운다 → 아래 '설치 — 안 찾아지거나 반영이 안 될 때' |
| ComfyUI 가 **큐를 여러 개 쌓으면 GPU 대신 CPU 로** 연산한다 | **kohya GUI 설치기가 전역 PATH·CUDA_PATH 를 CUDA 13.2 로 덮어씀** | 실행 옵션에 **`--disable-cuda-malloc`** 추가 → 아래 '학습 도구를 깔았더니' |
| `llama-cpp-python` 설치가 실패한다 (VLM 노드 · z-tipo-extension) | 빌드 도구가 없거나 순서가 틀렸다 | `python_embeded` 를 백업하고 그 폴더 cmd 에서 **`pip install --upgrade pip` → `scikit-build-core` → `build setuptools wheel` → `cmake` → `llama-cpp-python`** 순으로 |
| TIPO 를 `device=cuda` 로 놨는데 **CPU 가 돈다** | `TIPO-500m-ft-F16.gguf` 는 **GGUF 라 CPU 로 돈다** | GPU 판 `model.safetensor` 를 `ComfyUI\models\kgen` 에 넣고 `custom_nodes\z-tipo-extension\nodes\tipo.py` 의 270~280행·430~460행을 고친다. **CPU 로도 잘 돌아가긴 한다** |
| `Failed to load mtmd context from: ...gguf` (VLM 노드) | **mmproj 파일을 안 받았다** | mmproj 를 함께 받는다 → [ComfyUI 쓰는 법](comfyui.md) |
| `Failed to get input node 0 for group node child ... with slot 0` | ComfyUI 업데이트로 **그룹 노드 처리가 바뀌었다** ([issue 8887](https://github.com/comfyanonymous/ComfyUI/issues/8887)) | **그룹 노드를 해제**한 뒤 **서브그래프로 변환** |
| 미싱 노드가 **아무리 해도 설치되지 않는다** | **ComfyUI 데스크톱 버전** | **포터블 버전**으로 옮긴다 |
| 매니저에서 다 깔았는데 특정 노드팩만 안 돈다 | 워크플로우가 직접 안 써서 **`In workflow` 목록에서 빠졌다** | 예: `efficiency-nodes-ED` 에는 **`efficiency-nodes-comfyui`** 가 필요 — 수동 설치 |
| 노드팩을 업데이트했는데 **UI 가 그대로** | 커스텀 노드가 **`user.css` 등 UI 파일을 덮어쓰는** 구조 | 매니저에서 **disable → 재시작 → enable → 재시작** |
| `Node '무작위 정수' has no class_type` (Bjornulf_RandomIntNode) | 그 노드 자체가 문제가 많다 | **지우고 아무 랜덤 정수 노드로 교체** |
| `SDPromptReader` / `SDPromptSaver` 업데이트·설치 실패 | 매니저 경로 문제 | 지우고 `git clone --recursive .../comfyui-prompt-reader-node.git` → `pip install -r requirements.txt` |
| `JWIntegerMul` / `Integer Multiply` 가 **IMPORT FAILED** | `comfyui-various` 미설치 | 매니저에서 `Various ComfyUI Nodes by Type` 설치. 안 되면 **`soundfile` 을 먼저** |
| `RIFEInterpolation` 노드가 없다 | 보간 노드팩 미설치 | 매니저에서 **`ComfyUI-VFI`** |
| `SamplerCustomAdvanced - CalledProcessError ... triton\runtime\tcc\tcc.exe` | triton 빌드 환경 | `python_3.13.2_include_libs.zip` 을 `python_embeded` 에 풀거나 **Torch Compile·SageAttention 을 전부 끈다** |
| 로우노이즈 단계에서 `torch._dynamo` **재컴파일 오류** | Torch Compile | **Torch Compile 노드를 끈다** (실제 해결) |
| `UltralyticsDetectorProvider: UnpicklingError: Weights only load failed` | 파이토치 버전 | 커스텀 노드 업데이트 |
| FaceDetailer 계열이 **업데이트 후 죽음** | `UltralyticsDetectorProvider` 가 **서브팩으로 분리** | **`ComfyUI-Impact-Subpack`** 설치 |
| `r`(노드 정의 새로고침) 뒤 **드롭다운·choice 가 먹통** | ComfyUI 자체 버그 | **브라우저 새로고침** |
| Deep Translator 노드가 **빈 문자열**을 뱉는다 | `from_translate` 가 `auto` | `english` 로 변경. 그래도 안 되면 ComfyUI **2단계 이상 다운그레이드** |
| TIPO 가 **NVIDIA 없는 환경에서 `import failed`** | 설치기가 CUDA 를 전제한다 | ↓ 빌드 도구 절 |
| triton·SageAttention 이 **몇 주째 안 깔린다** (Wan 2.1, 2025-04) | **triton 최신판**을 깔았고 SageAttention 을 pip 로 깔았다 | ↓ 'triton 은 낮춰서 whl, sage 는 깃 소스로' |
| `SD Prompt Reader` 노드에서 **마스크를 뽑으면 오류** | 그 노드가 마스크 출력을 지원하지 않는다 | **Load Image 노드에 같은 이미지를 한 번 더** 올려 그쪽에서 우클릭 → `OPEN IN MASKEDITOR` → [ComfyUI 쓰는 법](comfyui.md) |
| 디테일러 `.pt` 에서 **보안 경고** | 화이트리스트 미등록 | `ComfyUI\user\default\ComfyUI-Impact-Subpack\model-whitelist.txt` 에 **파일 이름**을 적는다 |
| 그림이 **흐리멍텅**하게 나온다 (배포 워크플로우) | **Eps 모델에 v-pred 스위치가 켜져 있다** | **V-PRED 그룹을 바이패스**한다 |
| `[CNS] Warning: coloring skipped ... Padding size 4 is not supported for 5D input tensor.` | 컬러 노이즈 패치 + 특이 해상도(1104x1472 등) | **제작자가 수정했다** — 노드팩 업데이트 |
| 컬러 노이즈 패치를 `euler_ancestral` 에 걸면 오류 | 샘플러 이름 | **`euler_ancestral_RF`** 로 바꾼다 |
| ANIMA 워크플로우에서 **SAM 노드가 초록불인데 실행이 멈춘다** | 노드만 깔리고 **SAM 모델 파일이 없다** | 모델 파일을 직접 받아 넣는다 → [ANIMA](anima.md) |
| `Value not in list` | 워크플로우에 박힌 **로라·업스케일·디텍터 모델 이름**이 내 폴더에 없다 | **접힌 노드를 펼쳐** 내 파일로 바꾸거나 `None` 으로 둔다 → [ComfyUI 쓰는 법](comfyui.md) |
| `float object cannot be interpreted as an integer` | **`Random Number` 노드** (굿나잇 랜덤 워크플로우 v1.5). 클린 설치해도 재현된다 | **`Random Integer` 노드로 교체.** 제작자가 v1.8 에서 반영했다 → `https://arca.live/b/aiart/142849197` |
| 누락 노드를 다 설치했는데 **`workflowgroup` 이 없다** | 노드 설치 **전** 상태의 워크플로가 남아 있다 | **커스텀 노드 설치 후 워크플로우를 다시 넣는다** |
| NAIA 에서 넘기면 `prompt_outputs_failed_validation` | API 형식으로 넘긴 워크플로의 **커스텀 노드 필수 입력이 안 채워졌다** (`KeyError: 'mode'`, `Required input is missing: default_active / text / file / volume / mode`) | LoraManager·Impact Pack·pysssss 계열을 빼거나 **Bridge 노드 방식**으로 → [ComfyUI 쓰는 법](comfyui.md) |
| 업스케일에 **RCAN 모델**을 넣으면 실패 | `spandrel` 미설치 | ComfyUI 설치 폴더에서 `python -m pip install spandrel --upgrade` |
| 배포 워크플로우 로딩이 **유난히 느리다** | `efficiency-nodes` 의 **`LoRA Stacker`** | Easy-Use 의 **`EasyLoraStacker`** 로 교체(토글을 `enable` 로) |
| 업스케일 때 **비프음**이 난다 | 워크플로우에 `playsound` 노드가 들어 있다 | **미리보기 노드 아래의 `playsound` 노드를 제거** |
| **deno 커스텀 노드**로 돌리면 로라 매니저에 빨간 불이 잠깐 뜨고 **즉시 끝난다** | **로라 매니저 목록에 내가 갖고 있지 않은 로라가 있으면, 사용이 `off` 여도 중단된다.** 노드 버전 문제가 아니다(nightly·0.7.27·0.7.22 전부 재현) | **안 쓰는 로라를 `Remove` 로 뺀다.** 또는 `Power Lora Loader (rgthree)` 로 교체 |
| `The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 0` | MiniMax H3 터보 전용 확장 | `https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo/issues/9` 참고 |
| 터보 LoRA 로드 시 **오류 메시지가 수십 줄** 쏟아진다 (H3) | **`pruned` 모델**이라 로라가 참조할 키 일부가 없다 | **무시한다.** 4·6·8스텝 모두 영상이 정상 생성된다 → [비디오 생성](video-generation.md) |
| `[GetNode] ✗ Variable 'model_low' not found!` (WAN SVI) | Get/Set 노드가 모델을 못 찾는다 | 모델을 제대로 넣었는지 확인하고, 그래도 안 되면 **`get model low` / `set model low` 노드를 다 지우고 직접 잇는다** |
| Ollama 자동 프롬프트에서 **'모델이 없다'** 고 나온다 (Huihui-Qwen3) | 모델 태그가 다르다 | PowerShell 에서 `ollama run huihui_ai/qwen3-vl-abliterated:4b-instruct-q4_K_M` |
| Ollama 프롬프트 생성까지는 되는데 **전체 시퀀스가 6초 만에 완료**로 끝난다 | ComfyUI 최신 업데이트와 **호환되지 않는 노드** (보통 번역 관련) | 해당 노드를 제거해 본다 |
| `WanVideo Torch Compile Settings` 에서 **inductor·cudagraphs 가 전부 에러** | 최적화용 노드다 | **노드를 비활성화해도 된다** — 결과물에는 영향이 없고 속도만 조금 느려진다 |
| `local variable 'clip_vision_output' referenced before assignment` (WAN FLF2V) | 클립비전을 비워 둔 채로 노드가 남아 있다 | **`CLIP Vision Encode` 노드 자체를 삭제**한다 (공식 워크플로에도 클립비전이 없다) |
| `Anima Prompt Studio Advanced` 에서 `Required input is missing: ...` 무더기 | 제작자가 잘못 올린 커밋 | **0.1.2 이상 또는 최신 커밋으로 업데이트** |
| SpectrumSDXL 노드를 쓰면 **ComfyUI 가 닫힌다** (AMD ROCm) | 노드 충돌 | **노드 교체로 해결**됐다 |
| 원클릭 코랩에서 **rife49.pth 가 받아지지 않는다** (ComfyUI-Frame-Interpolation) | `vfi_utils.py` 의 `BASE_MODEL_DOWNLOAD_URLS` 세 곳(styler00dollar · Fannovel16 · dajes)이 **전부 먹통**이 됐다 | 그 값을 아래 한 줄로 바꾼다 — 커밋 해시가 URL 에 박혀 있어 그 시점 파일이 고정으로 내려온다<br>`["https://huggingface.co/hfmaster/models-moved/resolve/cab6dcee2fbb05e190dbb8f536fbdaa489031a14/rife/"]` |
| `Model Loader Node doesn't work - 'NoneType' object has no attribute 'data'` (ComfyUI-SAM3) | 커스텀 노드의 모델 로더가 깨졌다 | 이슈 [#106](https://github.com/PozzettiAndrea/ComfyUI-SAM3/issues/106) 의 수정안을 `ComfyUI\custom_nodes\comfyui-sam3\nodes\sam3\model.py` 에 반영 → ↓ 'SAM3 커스텀 노드 되살리기' |
| `safetensors_rust.SafetensorError: Error while deserializing header: InvalidHeaderDeserialization` | **위와 무관한 별개 오류** — 받아진 모델 파일이 깨졌거나 다운로드가 막혔다 | `sam3.safetensors` 를 직접 받아 `ComfyUI/models/sam3` 에 넣는다. 그래도 안 되면 **ComfyUI 재설치**로 해결된 사례가 있다 |
| `Required input is missing: model_patch` | `Apply Anima ControlNet-LLLite` 가 **커스텀 노드에서 내장 노드로 바뀌며 입력이 새로 생겼다** | LLLite 파일을 `ComfyUI/models/model_patches/` 로 옮기고 **'모델 패치 로더'** 를 그 입력에 연결 → ↓ '노드가 내장으로 바뀌었을 때' |
| `Failed to convert an input value to a FLOAT value` + strength 자리에 **파일명이 들어가 NaN** | 구버전 워크플로우의 위젯 배치가 새 노드 정의와 어긋나 값이 밀렸다 | **값을 고치지 말고** 그 노드를 **삭제 후 새로 불러와 재연결** |
| `[DCW] Warning: correction skipped at this step – Padding size 4 is not supported for 5D input tensor.` | 디테일러 구간과 **8의 배수이지만 2로 나누면 홀수인 해상도**(1208 등)에서 보정이 **조용히 스킵**되던 버그 | ComfyUI-DCW 를 업데이트(`dcw_node.py` 만 덮어써도 된다) → [ComfyUI 쓰는 법](comfyui.md) |
| `'Tensor' object has no attribute 'copy'` (MaskDetailerPipe) | **SAM3 노드 연결 실수** | 연결을 다시 본다 |
| SAM3 노드가 미싱으로 남거나 마스크가 깨진다 | 노드팩이 여러 개 겹쳤다 | **sam3 관련 노드를 전부 지우고 ComfyUI-RMBG 만** 다시 깐 뒤 `ComfyUI\models\sam3\sam3.pt` 를 넣어 RMBG 가 그 모델을 쓰게 한다. 함께 미싱으로 뜨는 `set basic`·`get basic` 은 **UI 용이라 직결해도 된다** |
| `--fast cublas_ops` 를 붙였는데 아무 변화가 없다 | `cublas_ops` 는 CUBLAS 가 아니라 **별도 파이썬 확장**이다 | `pip show cublas_ops` → `Package(s) not found` 면 그 인자는 무효 → [설치와 환경 구성](install.md) |

### triton 은 낮춰서 whl, sage 는 깃 소스로 (2025-04, Wan 2.1 · 포터블)

**원클릭 설치본 · 최신 pip 설치 · `__init__.py` 와 `core.py` 직접 수정 · 전체 재설치 — 전부 실패한 끝에 찾은 절차다.**
환경은 RTX 4070 Ti Super / 파이썬 3.11.8 / CUDA 12.8.

```powershell
# 1) triton 과 SageAttention 을 모두 완전히 제거한 뒤,
#    3.1.0 whl 을 받아 python_embeded\Lib\site-packages 에 넣고 그 폴더에서
#    https://github.com/woct0rdho/triton-windows/releases/tag/v3.1.0-windows.post9
python -m pip install triton-3.1.0-cp311-cp311-win_amd64.whl
#    ↑ 파일명의 cp311 은 파이썬 3.11 전용이라는 뜻. 자기 버전에 맞는 것을 고른다

# 2) SageAttention 은 pip install sageattention 으로는 되지 않았다. 깃 소스에서 깐다
python -m pip install git+https://github.com/thu-ml/SageAttention.git
```

> **핵심은 'triton 은 버전을 낮춰 whl 로, SageAttention 은 깃 소스로'** 다.
> 댓글에서 `https://github.com/woct0rdho/SageAttention/releases` 의 빌드본을 권했지만 글쓴이는 그것도 안 됐다고 답했다(triton 문제였을 수도 있다고).
> ⚠️ **2026년 기준 최신 절차는 위 [ComfyUI 쓰는 법](comfyui.md) 의 SageAttention 항목이다.** 이 처방은 그쪽이 안 될 때 시도해 볼 옛 경로다.
> 참고 성능 — 4070 Ti Super, 업스케일·보간 없이 로라 2개, 480p 6초(97프레임) 영상에 약 11분.

### 소스 롤백 ≠ venv 재생성 (2023-03, 지금도 유효)

WebUI 가 업데이트 후 깨졌을 때 **처방이 둘인데 서로 다른 것을 고친다.**

| 증상의 뿌리 | 처방 |
|---|---|
| **WebUI 소스 코드** | 이전 커밋의 소스 zip 으로 되돌린다 |
| **Gradio 같은 파이썬 라이브러리** | **소스를 덮어써도 소용없다 — 문제는 `venv`(가상환경) 안에 있다.** venv 를 지우고 다시 만든다 |

> 모델과 아웃풋만 남기고 나머지를 싹 지우는 것도 방법이지만, 그러면 **torch 처럼 venv 에 따로 `pip install` 했던 것을 전부 다시 설치**해야 한다.
> **"되돌렸는데 그대로다" 의 대부분이 이 구분을 몰라서 생긴다.**

### 긴 경로 켜기 — `Filename too long`

커스텀 노드가 매니저에서 설치되지 않을 때는 **매니저 로그에 남는 명령을 cmd·파워셸에서 직접 실행**해 보면 진짜 원인이 드러난다.

```
error: unable to create file civitai/sd_1.5/Life_Like_Diffusion__Ethnicities_supported_-_...._1923023.jpeg: Filename too long
fatal: unable to checkout working tree
```

**관리자 파워셸**에서:

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```

**반드시 재부팅**한 뒤:

```
git config --global core.longpaths true
```

그리고 다시 `git clone` 하면 성공한다. **이 조합은 다른 커스텀 노드에서 파일명이 길어 clone 이 실패할 때 그대로 쓸 수 있는 처방이다.**
같은 제한이 로라 학습(comfyui-instant-lora)에서 "깊은 폴더의 파일을 못 찾는" 에러로도 나타난다 — 레지스트리를 바꾸고 재부팅하면 3만 자 수준까지 인식한다.

### 포터블에서는 임베디드 파이썬으로 깐다

**포터블 환경에서 파이썬 패키지는 시스템 파이썬이 아니라 `python_embeded` 안의 `python.exe` 로 깔아야 한다.**
네 편 이상의 글이 같은 말을 한다(커스텀 노드 의존성, ROCm, 라데온 SageAttention whl, triton 인스톨러).

```powershell
# python_embeded 폴더에서
.\python.exe -m pip install soundfile
.\python.exe -m pip install audioop-lts

# 포터블 최상위 폴더에서
.\python_embeded\python.exe -s -m pip install --no-cache-dir <URL 또는 whl>
```

설치 후 **ComfyUI 를 재시작**한다.

### sage-attention — 뉴비 오류의 범인 1위

> **"많은 뉴비가 공유받은 워크플로우에서 오류가 터지는 범인은 세이지(sage-attention)"** (175397651, 2026-06)

남이 만든 워크플로우가 이유 없이 터진다면 **모델·노드보다 sage 를 먼저 의심한다.** 확인 순서:

| | 확인 |
|---|---|
| 1 | **sage 를 끄고 돌려 본다.** 통합팩이면 `run_nvidia_gpu_fast_fp16_accumulation.bat` 대신 **`run_nvidia_gpu.bat`** / 직접 구성이면 실행 인자에서 `--use-sage-attention` 을 뺀다 |
| 2 | Forge Neo 계열에서 검은 화면 + `Encountered NaN in Latent; Try --disable-sage` 로그가 뜨면 그것이 신호다 |
| 3 | **RTX 2000번대(튜링)** 는 통합팩에서 sage 를 켜면 터진다. RTX 2060 Super 8GB 에서 **sage 만 끄면 정상 동작**이 확인됐다 |
| 4 | 그래도 sage 를 쓰겠다면 **튜링용 wheel 은 따로 받아야 한다** ↓ |

```
# ComfyUI 공식 wheels — 튜링(RTX 20 시리즈) 미대응
https://comfy-org.github.io/wheels
# 튜링은 이쪽 Windows fork
https://github.com/woct0rdho/SageAttention
```

sage 를 켜면 **생성 속도가 10~15% 오르지만 손가락 찐빠가 늘어난다는 보고**도 함께 있다. 그림만 뽑을 거면 꺼도 된다.

### 빌드 도구가 없으면 안 깔린다 — `llama-cpp-python` 계열

**`llama-cpp-python` 은 C++ 로 된 라이브러리를 직접 빌드하는 패키지다.
윈도우에 C++ 빌드 환경이 없으면 설치 자체가 실패한다.** 그래서 pip 명령을 몇 번 반복해도 결과가 같다.

**먼저 깔아야 하는 것 둘** (2025-03 기록, 지금도 통용된다):

| | 받는 곳 | ⚠ 체크할 것 |
|---|---|---|
| **CMake** | `https://cmake.org/download/` | 설치 중 **`Add CMake to system PATH`** 가 체크됐는지 반드시 확인 |
| **VS Build Tools** | `https://visualstudio.microsoft.com/ko/visual-cpp-build-tools/` | **`Desktop development with C++`**, **`MSVC v142 - VS 2019 C++ x64/x86 build tools`**, **`Windows 10 SDK`**(또는 11) 체크 |

그 다음에 ComfyUI 폴더에서 설치한다.

```bash
pip install llama-cpp-python
```

**이 처방은 TIPO 에만 해당하는 것이 아니라, C++ 컴파일이 필요한 파이썬 패키지 설치가 막힐 때 공통으로 쓴다.**

### NVIDIA 가 없는 환경에서 TIPO 쓰기 (인텔 내장 등)

`z-tipo-extension` 은 기본값이 CUDA 라 NVIDIA 가 없으면 `import failed` 가 뜬다.
`custom_nodes\z-tipo-extension\tipo_installer.py` 를 메모장으로 열어 `has_cuda = torch.cuda.is_available()` **아래 두 줄**을 아래로 바꾼다.

```python
cuda_version = torch.version.cuda.replace(".", "") if torch.version.cuda else None
arch = f"cu{cuda_version}" if has_cuda and cuda_version else "cpu"
```

저장하고 ComfyUI 를 재시작하면 `import failed` 는 사라진다.
마지막으로 **TIPO 노드를 펼쳐 맨 아래의 `cuda` 를 `cpu` 로** 바꾸면 정상 동작한다.

→ [ComfyUI 쓰는 법](comfyui.md) · [설치와 환경 구성](install.md)

<small>근거 — [WAN2.2 I2I 일관성 통일 워크플로우 26.01](https://arca.live/b/aiart/160425811) · [딸깍충을 위한 완전 자동 AUTO-WAN (워크플로우) (+… 25.10](https://arca.live/b/aiart/152101017) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780)</small>

??? note "근거 47건 전부 보기"
    [WAN2.2 I2I 일관성 통일 워크플로우 26.01](https://arca.live/b/aiart/160425811) · [딸깍충을 위한 완전 자동 AUTO-WAN (워크플로우) (+… 25.10](https://arca.live/b/aiart/152101017) · [Comfy ANIMA 정보글 모음 26.06](https://arca.live/b/aiart/175397651) · [라면보다 쉽다! 간편 종합 워크플로우 v1.5 25.07](https://arca.live/b/aiart/143249780) · [뉴비 친화적 Smooth 워크플로우 개조판 (+업데이트) 25.10](https://arca.live/b/aiart/151277424) · [딸깍 AUTO-WAN+디테일러+사운드(MMAudio) 워크플… 25.11](https://arca.live/b/aiart/153525536) · [SAM3 해결했다.. 26.03](https://arca.live/b/aiart/166035589) · [LTX 2.3 워크플로우 V2 공유 및 팁 정리 26.06](https://arca.live/b/aiart/172671768) · [미니맥스 H3 R2V 오디오 레퍼런스 시연 26.08](https://arca.live/b/aiart/179459020) · [Wan2.2 FLF2V 간단 테스트 25.08](https://arca.live/b/aiart/145952453) · [EasyUse Anima: ANIMA 프롬프트 보조 노드 베… 26.06](https://arca.live/b/aiart/174369324) · [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림… 25.12](https://arca.live/b/aiart/157410060) · [Wan 쓰시는 분들을 위해 워크플로우 공유 26.06](https://arca.live/b/aiart/172865906) · [ComfyUI-DCW 노드업뎃 26.05](https://arca.live/b/aiart/169518554) · [(워크플로우 공모전) 라면보단 어렵더라! 3트째 간편 워크플… 25.07](https://arca.live/b/aiart/141180724) · [쉽고 빠른 ComfyUI V6 마이너 업데이트 24.12](https://arca.live/b/aiart/122761449) · [WAN 2.2 SVI 올라마 자동프롬프트 15초 워크플로우 … 26.01](https://arca.live/b/aiart/160056290) · [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 … 26.08](https://arca.live/b/aiart/179176367) · [뉴비의 아니마 워크플로우 공유 26.05](https://arca.live/b/aiart/170889404) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [comfyui-cns_sampler_patch 26.05](https://arca.live/b/aiart/172367736) · [ComfyUI 워크플로우 - SAM3, 마스크 디테일러로 활… 25.12](https://arca.live/b/aiart/157473218) · [AMD R9700 attention 별 생성속도 26.06](https://arca.live/b/aiart/173409804) · [모르고 쓰면 해골물인 ComfyUI 옵션 26.07](https://arca.live/b/aiart/177447677) · [미니맥스 4스텝 터보로라 돌려봄 26.08](https://arca.live/b/aiart/179108697) · [anima 1장 Lora 학습 comfyui 포터블 설치기 26.04](https://arca.live/b/aiart/168909715) · [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 v1.8 25.07](https://arca.live/b/aiart/142849197) · [2주차 뉴비의 comfyUI 워크플로우 공유 25.08](https://arca.live/b/aiart/145850172) · [4.5 챈에 쓰는 ComfyUI 빡통 워크플로우 4.0 25.06](https://arca.live/b/aiart/139311613) · [빡통워크 5.1 자동 랜덤그림체 + 업스케일 25.08](https://arca.live/b/aiart/146574747) · [내가 쓰고있는 ComfyUI 워크플로우 공유 (SDXL, A… 26.08](https://arca.live/b/aiart/179640921) · [z-tipo-extension 설치 및 tipo 파일 수정 26.02](https://arca.live/b/aiart/162039111) · [(워크플로우 공모전) 굿나잇 랜덤 워크플로우 v1.5 25.07](https://arca.live/b/aiart/142088366) · [rife49.pth 버그제보 - 원클릭 코랩 실행 안되는 사… 26.02](https://arca.live/b/aiart/162972850) · [SAM3 디테일러 커스텀 노드가 작동되게 수정한 파일이야. 26.03](https://arca.live/b/aiart/164808456) · [(워크플로우 공모전) 라면보다 쉽다! 간편 종합 워크플로우 … 25.07](https://arca.live/b/aiart/141991828) · [뭣같은 wan2.1 triton + sageattention… 25.04](https://arca.live/b/aiart/133924449) · [인텔 내장으로 comfyui를 돌릴때 tipo를 사용하는 방… 25.03](https://arca.live/b/aiart/132353208) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848) · [오늘 업뎃해서 오류나는 챈럼들을 위한 이전버전 링크 23.03](https://arca.live/b/aiart/72586603) · [(워크플로우 공모전) T2I특화 모듈형 프롬프트 워크플로우 25.07](https://arca.live/b/aiart/142197182) · [ComfyUI 에서 bjornulf_custom_nodes … 26.02](https://arca.live/b/aiart/163272564) · [라데온용 컴피 rocm 업데이트 방법 다시 알아옴 26.01](https://arca.live/b/aiart/160654263) · [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179637421) · [정보탭의 kohya gui 설치후 발생한 문제해결 26.07](https://arca.live/b/aiart/176818115) · [NAIA로 Comfy + 아니마를 써보려는데 사용법을 잘 모… 26.06](https://arca.live/b/aiart/173906125) · [comfyui inpaint turbo 워크플로우 관련 질문 26.07](https://arca.live/b/aiart/177370189)

## PyTorch 가 안 깔린다 — venv 밖에서 깔면 몇 번을 해도 같다
<small>⚠️ 2023-02 기준 · 근거 1건 · 자료 엇갈림</small>

`RuntimeError: Couldn't install torch` 로 WebUI 설치가 멈출 때다. **이 글은 본문 처방으로는 해결되지 않고 실제 해결책이 전부 댓글에 있다** (69972082, 2023-02).

**본문 처방** — 전역 파이썬에서 다음을 실행하라고 한다.

```
python -m pip install torch --extra-index-url https://download.pytorch.org/whl/cu117 --upgrade
python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117 --upgrade
```

> ❌ **이 처방만으로는 대개 해결되지 않는다.**
>
> 댓글 19번의 정정 — **pip 설치는 WebUI 의 가상환경(venv) 안에서 이뤄져야 한다.**
> **전역 파이썬에 아무리 설치해도 venv 안이 비어 있으면 같은 오류가 반복된다.**

**맞는 절차**

```bat
:: 윈도우 — WebUI 설치 폴더에서
venv\Scripts\activate.bat
python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130 --upgrade
deactivate
```

```sh
# 맥·리눅스
source venv/bin/activate
```

빠져나온 뒤 webui 를 실행한다.
(위 `cu117` 은 2023년 값이다. **자기 CUDA 에 맞는 index-url 은 `https://pytorch.kr/` 에서 확인한다** — 대체로 RTX 5000번대는 `cu130`, 4000번대는 `cu128`.)

### SSL 인증서 오류라면 버전 문제가 아니다

로그에 이런 조합이 보이면 **버전이 아니라 인증서 문제**다 (댓글 18번).

```
SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate'))
ERROR: Could not find a version that satisfies the requirement torch==1.13.1+cu117
```

호스트를 신뢰 목록에 넣어 설치한다.

```
python -m pip --trusted-host download.pytorch.org install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117 --upgrade
```

### 설치가 됐는지 판별하는 법

> pip 출력 **마지막 줄에 error 나 빨간 글씨가 없으면**, `Requirement already satisfied` 만 잔뜩 떠도 **설치가 된 것이다** (댓글 4번).

**그 밖에** — 본문은 외장하드·USB 의 파일시스템이 NTFS 가 아니면 이 오류가 난다는 말을 덧붙이는데, **작성자 스스로 확인하지 못했다고 단서를 달았다**(한 글에서만 언급된 미확인 정보). 끝내 해결되지 않은 사례는 파이썬만 밀고 재설치 → 그래도 안 되면 포맷으로 해결됐다.

→ [설치와 환경 구성](install.md)

<small>근거 — [파이토치 설치 안되는사람 보셈 23.02](https://arca.live/b/aiart/69972082)</small>

## 검은 이미지 · NaN — 어디서 터졌는지부터 가른다
<small>2026-05 기준 · 근거 2건</small>

검은 이미지가 나오거나 `NaN` 오류가 뜰 때의 원인 후보를 **순서대로** 좁히는 체크리스트다. SD1.5·2.x 시절 자료지만 **진단 논리는 지금도 유효하다** (68478526, 2023-01).

**배경** — A1111 은 살아 있는 텐서가 하나라도 있으면 사용 가능한 모델로 판단한다(`tensor.all`). 검은 이미지가 나오는 것은 **NaN(계산이 숫자가 아닌 값으로 터진 것)** 이 반환됐을 가능성이 높다.

### 0. 먼저 — 어디서 터졌나

`half` 는 fp16 반정밀도 연산이다. **끄는 위치로 원인을 가른다.**

| 인자 | 무엇을 끄나 | 이걸로 해결되면 |
|---|---|---|
| `--no-half` | U-Net 전체의 fp16 | **U-Net** 에서 터진 것 |
| `--no-half-vae` | VAE 의 fp16 | **VAE** 에서 터진 것 |
| `--opt-sub-quad-attention` | 크로스 어텐션 최적화를 다른 것으로 | **크로스 어텐션 최적화 버그** |

손상된 CLIP / OpenCLIP 임베딩이 의심되면 레포지토리를 이 커밋으로 체크아웃해 본다.

```
ef75c980536471c0729a2319440e3083cd57a4f0
```

### 1~4. 그다음 순서

| | 원인 후보 | 확인 방법 |
|---|---|---|
| 1 | **고학습률 파인튜닝** | 하이퍼네트워크·임베딩·LoRA 를 **전부 빼고** 같은 오류가 나는지 본다. 학습을 다시 한다면 BF16 또는 FP32 로 |
| 2 | **병합으로 망가진 레이어** | SD·Waifu Diffusion 같은 **원본 계열 모델**에서도 같은 오류가 나는지 대조한다 |
| 3 | **xformers 버그** | 다른 xformers 버전으로 교체. SD 2.X 모델에 한해 `--xformers-flash-attention` 을 켜 본다 |
| 4 | **ROCm / DirectML 버그 (AMD)** | 댓글 — DirectML 의 NaN 은 **계속 돌리다 보면 사라지는** 경우가 많다 |

### 최신 계열의 다른 원인 두 가지

같은 '검은 화면' 이라도 2026년 환경에서는 원인이 다를 수 있다.

- **Forge Neo** 에서 `Encountered NaN in Latent; Try --disable-sage` 가 뜬다면 **sage-attention** 또는 **ADetailer** 쪽이다 → 위 'sage-attention' 절과 아래 '결과물이 이상할 때'
- ComfyUI 의 검은 영상은 int8convrot VAE 환경 문제다 → 아래 '버전 충돌'

→ [모델 고르기](models.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [NaN 오류 체크리스트 23.01](https://arca.live/b/aiart/68478526)</small>

## VAE 를 둘러싼 오해 둘 — 바로잡는다
<small>⚠️ 2023-02 기준 · 근거 4건 · 자료 엇갈림</small>

VAE 는 입문자가 가장 많이 헷갈리는 파일이고, **채널의 대표 가이드 두 편에 각각 오해가 하나씩 박혀 있다.** 둘 다 지금도 재생산되고 있어서 따로 적는다.

### 오해 1. "`Ignore selected VAE ...` 를 **체크**하라" — 틀렸다

**본문 주장** — 「뉴비 자주 묻는 질문(FAQ)」의 VAE 설정 3번 항목은 설정에서
`Ignore selected VAE for stable diffusion checkpoints with loaded VAE weights` 를 **체크**하라고 적었다 (68598675, 2023-01).

> ❌ **이 설명은 틀렸다. 체크 해제가 맞다.**
>
> **댓글 6·7번이 지적해 '체크 해제' 로 정정됐다.**
> 다만 **대회 출품글이라 본문 수정이 막혀 취소선으로만 표시돼 있다** — 그래서 본문만 훑고 지나가면 틀린 쪽을 그대로 따라 하게 된다.

이름 그대로 **"모델에 VAE 가 내장돼 있으면 내가 고른 VAE 를 무시한다"** 는 옵션이다. 체크하면 **직접 고른 VAE 가 안 걸린다.**

### 오해 2. "anime VAE 를 썼더니 극실사체가 나온다" — VAE 탓이 아니다

**질문자 주장** — 「프롬대장경 제1권」 댓글 3번에서 "anime vae 를 적용했더니 극실사체만 나온다"고 물었다 (68917133, 2023-02, 조회 53만).

> ❌ **VAE 탓이 아니다.**
>
> **댓글 4번의 정정 — "VAE 는 그림체에 아무런 영향도 주지 않습니다. 모델을 다시 확인하세요."**

**VAE 가 하는 일과 하지 않는 일**

| VAE 가 하는 것 | VAE 가 하지 않는 것 |
|---|---|
| 잠재공간의 latent 를 **실제 픽셀 이미지로 되돌리는 디코더** | **그림체(화풍)를 바꾸는 것** |
| **색감**을 좌우한다 — 안 걸리면 뿌옇고·물 빠진 색·채도 저하·푸른 멍/보라색이 낀다 | 구도·캐릭터·인체를 바꾸는 것 |
| 흐린 이미지를 **선명하게** 만든다 | |

**즉 실사체가 나오면 봐야 할 것은 VAE 가 아니라 체크포인트(모델)다.**
그림체는 모델과 로라·프롬프트가 정한다 → [모델 고르기](models.md) · [프롬프트 쓰는 법](prompting.md)

### 오해 3. "실사 태그를 더 세게 누르면 AI 티가 빠진다" — 그보다 모델을 먼저 바꾼다

반실사·실사에서 AI 티가 심할 때 자주 하는 실수가 `photorealistic`, `realistic` 같은 태그를
계속 더하고 빼며 버티는 것이다.

| 먼저 볼 것 | 이유 |
|---|---|
| **체크포인트** | 실사/반실사 성향은 모델이 먼저 정한다. ANIMA 와 2dac·RoseMIX·Uncanny 는 출발점이 다르다 |
| **작가 태그 개수** | 작가를 많이 쌓을수록 배경 오염·색 흔들림·액자/포스터 끼어듦이 커진다 |
| **실사 태그 자체** | 카드 실사용에서는 `4::photorealistic, realistic::` 같은 실사 태그를 **음수로 누르기보다 아예 빼는 편이 낫다**는 쪽으로 수렴했다 |

**빠른 처방**

1. 실사·반실사 목표면 [모델 고르기](models.md)의 `RoseMIX` / `2dac` / `Uncanny` 계열로 먼저 옮긴다.
2. 작가 태그를 5명 이하로 줄인다.
3. `photorealistic`, `realistic` 를 억지로 마이너스로 누르기 전에 **긍정에서 먼저 제거**해 본다.
4. 한 장에서 끝내려 하지 말고 hires / detailer / upscale 로 후반 정리를 탄다.

### 덤 — VAE 파일을 어디에 넣나

| | |
|---|---|
| A1111 계열 | `models\VAE` 든 `models\Stable-diffusion` 이든 **어느 쪽이든 인식된다**(댓글에서 재확인). `models\VAE` 에 'Put VAE here' 안내가 있으니 거기 넣으면 된다 |
| 용량으로 판별 | VAE 는 보통 **300~400MB**. 확장자만으로는 임베딩·하이퍼·모델·VAE·LoRA 를 구분할 수 없다 |
| 적용 확인 | 콘솔에 `VAE weights loaded.` 가 뜨면 정상, `Restoring base VAE` 면 미적용 → 아래 '색이 뿌옇다' 항목 |

→ [용어집](glossary.md) · [설치와 환경 구성](install.md)

<small>근거 — [(가이드) 프롬대장경 제 1권 『설치부터 t2i까지』 23.02](https://arca.live/b/aiart/68917133) · [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법 23.01](https://arca.live/b/aiart/66582124) · [흐릿, 흐리멍텅, 흐리게, 뿌옇게,해상도 ,뿌옅게 ,뿌해 ,… 23.02](https://arca.live/b/aiart/68904629) · [(가이드) 뉴비 자주 묻는 질문 (FAQ) 23.01](https://arca.live/b/aiart/68598675)</small>

## 지금 새로 깔면 만나는 오류 — 설치 · clone 단계 (2026 갱신)
<small>2026-06 기준 · 근거 4건</small>

2026년에 **새로** 깔면 그대로 만나는 것들이다. 위쪽 대응표는 대부분 2022~2023년 자료라 여기 있는 문구가 없다.

| 오류 문구 / 증상 | 원인 | 해결 |
|---|---|---|
| `error: invalid path 'subgraphs/LLM:ChatCompletions Simple.json'` + `fatal: unable to checkout working tree` | 파일명의 **콜론(:)** 을 윈도우가 만들지 못한다 | ↓ '콜론 파일명' |
| `RuntimeError: Couldn't install clip` + `ERROR: Failed to build 'https://github.com/openai/CLIP/archive/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip' when getting requirements to build wheel` | **최신 setuptools 가 구형 CLIP 빌드를 깨뜨린다** | ↓ 'setuptools 69.5.1' |
| `remote: Repository not found.` + `fatal: repository 'https://github.com/Stability-AI/stablediffusion.git/' not found` | 원본 저장소가 **깃허브에서 사라졌다** | ↓ '사라진 저장소' |
| 커스텀 노드를 새 포크로 바꿨더니 **'필수 리소스 로드에 실패했습니다'** | 기존 폴더를 `_old` 로 **이름만 바꿔** 중복 로드 | ↓ 'EreNodes `_old`' |

### 콜론 파일명 — clone 하면 `.git` 만 남는다

`git clone` 이 끝난 것처럼 보이는데 폴더에 **파일이 하나도 없고 `.git` 만 남아 있다면** 이것이다 (174631586, 2026-06).

```
error: invalid path 'subgraphs/LLM:ChatCompletions Simple.json'
fatal: unable to checkout working tree
```

원인은 **파일명에 콜론(`:`)이 들어가 윈도우가 그 파일을 만들 수 없기 때문**이다. 체크아웃이 통째로 중단되므로 파일이 하나도 안 받아진다.
`ComfyUI-LLM-Helper` 는 **제작자가 1.0.5 에서 파일명을 고쳐 해결**했다 — 같은 증상이면 **1.0.5 이상**을 받으면 된다.

> 같은 자리에서 나오는 `error: unable to create file ...: Filename too long` 은 **다른 문제**(윈도우 260자 경로 제한)다. 그쪽은 위 'ComfyUI · 포터블 계열' 표의 '긴 경로 켜기' 를 본다. **문구가 `invalid path` 인지 `Filename too long` 인지로 갈린다.**

### setuptools 69.5.1 — A1111 계열 CLIP 빌드 실패

A1111 WebUI·reForge 를 **지금 새로** 깔면 `webui-user.bat` 실행 중에 그대로 만난다 (164173886, 2026-03. 원 출처는 https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/17284 댓글).

전제 — Python **3.10.6** 을 `Add Python to PATH` 체크로 설치하고, git 을 설치하고, `c:/ai` 같은 영어 폴더에서 clone 한다.

```
cd c:/ai/stable-diffusion-webui/
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install --force-reinstall --no-cache-dir "setuptools==69.5.1" wheel
.\venv\Scripts\python.exe -m pip install --no-build-isolation https://github.com/openai/CLIP/archive/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip
```

둘째 줄에서 `packaging-26.0 setuptools-69.5.1 wheel-0.46.3` 같은 줄이 나오면 정상이다.
요점은 **setuptools 를 69.5.1 로 내리고 빌드 격리(`--no-build-isolation`)를 끄는 것** 두 가지다.

### 사라진 저장소 — 미러 + 커밋 해시로 대체

위를 넘기면 바로 다음에 이게 뜬다.

```
remote: Repository not found.
fatal: repository 'https://github.com/Stability-AI/stablediffusion.git/' not found
```

**원본 저장소가 깃허브에서 사라졌다.** `webui-user.bat` 의 `call webui.bat` 줄 **앞에** 두 줄을 넣어 미러와 커밋 해시를 지정한다.

```bat
set STABLE_DIFFUSION_REPO=https://github.com/joypaul162/Stability-AI-stablediffusion.git
set STABLE_DIFFUSION_COMMIT_HASH=f16630a927e00098b524d687640719e4eb469b76
```

제보자는 이 두 오류를 넘긴 뒤로는 순탄했다고 적었다.

### EreNodes `_old` — 폴더는 이름만 바꾸면 안 된다

커스텀 노드를 새 포크로 교체할 때 **기존 폴더를 지우지 않고 `_old` 로 이름만 바꿔 두면** '필수 리소스 로드에 실패했습니다' 오류가 난다. **같은 확장으로 판정돼 중복 로드되기 때문**이다 (161031716, 2026-01 댓글).

> **백업하려고 `_old` 를 붙이는 습관이 그대로 사고가 된다.** 백업하려면 `custom_nodes` **바깥**으로 옮기고, 안에 두려면 **지운다.**

같은 글의 설치법 참고 — 보안 레벨을 조절할 수 있으면 ComfyUI Manager 의 `Install via Git URL`, 아니면 실행 bat 이 있는 곳에서:

```
cd ComfyUI/custom_nodes
git clone https://github.com/craftingmod/ComfyUI-EreNodes.git
```

→ [설치와 환경 구성](install.md) · [ComfyUI 쓰는 법](comfyui.md)

### 'CLIP 이 설치돼 있는데 없다고 한다' — venv 재생성 (2026-02)

위 'setuptools 69.5.1' 과 **문구는 같은데 상황이 다른** 경우가 있다.

```
https://github.com/openai/CLIP/archive/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip
가 설치되지 않았다는 fail 메시지
```

**그런데 venv 를 열어 보면 CLIP 은 멀쩡히 설치되어 있다.** 깃에 올라온 것이 업데이트되면서 뭔가 깨진 것으로 보인다.
해결은 **venv 를 통째로 지우고 다시 만들어 경로를 새로 잡아 주는 것**이다.

```powershell
# WebUI 설치 폴더에서 venv 폴더를 지운 뒤
python -m venv venv
venv\Scripts\python.exe launch.py
```

설치가 완료되었다고 뜰 때까지 **중간에 끊지 말고 기다린다.** 다 되면 알아서 WebUI 창이 열린다.

> **둘을 가르는 기준** — **빌드가 실패하면**(`Failed to build ...`) setuptools 를 69.5.1 로 내리는 쪽이고,
> **이미 설치돼 있는데 없다고 하면** venv 재생성 쪽이다.
> 짧은 글이지만 **'설치는 되어 있는데 없다고 한다' 유형에서 venv 재생성이 표준 처방**이라는 점을 보여 준다.

<small>근거 — [커스텀노드) ComfyUI-LLM-Helper 26.06](https://arca.live/b/aiart/174631586) · [webui fail 뜨면서 실행안되는 오류 해결법 26.02](https://arca.live/b/aiart/162800946) · [EreNodes 자동완성 한국어 입력버그 수정본 26.01](https://arca.live/b/aiart/161031716) · [reforge 설치시 오류 해결법 중 꽤 유용한거 있어서 갖… 26.03](https://arca.live/b/aiart/164173886)</small>

## 지금 새로 깔면 만나는 오류 — 돌려 본 뒤 (2023~2026)
<small>2026-07 기준 · 근거 3건 · 자료 엇갈림</small>

설치는 넘겼는데 **돌려 보니 안 되는** 것들이다.

| 증상 | 원인 | 해결 |
|---|---|---|
| 번역이 안 되고 `Google prompt translation requires googletrans-py or GOOGLE_TRANSLATION_API_KEY` | `googletrans-py` **4.0.2** 를 깔았다. 요구는 **4.0.0** 이고 **둘은 다른 패키지다** | ↓ 'googletrans-py' |
| `RuntimeError: mat1 and mat2 shapes cannot be multiplied (154x1024 and 768x256)` | 로라 파일 문제가 아니라 **로라의 베이스 계열 ≠ 체크포인트 계열** | ↓ 'mat1 and mat2' |
| 폰트를 다 깔았는데도 **아이콘이 깨진다** | ⚠ **폰트가 아니라 브라우저다** | ↓ '아이콘 깨짐' |

### googletrans-py — 4.0.2 와 4.0.0 은 다른 패키지다

EasyUseAnima 의 구글 번역이 동작하지 않을 때 나오는 문구다 (176029127, 2026-07 댓글).

```
Google prompt translation requires googletrans-py or GOOGLE_TRANSLATION_API_KEY
```

**원인은 `googletrans-py` 4.0.2 를 깐 것이다.** 요구 버전은 `googletrans-py==4.0.0` 이고 **4.0.2 는 이름만 비슷한 다른 패키지라 충돌한다.**

1. 4.0.2 를 지운다
2. 커스텀 노드의 `pyproject.toml`(또는 `requirements.txt`) 의존성을 `googletrans-py==4.0.0` 으로 맞춘다
3. ComfyUI 재실행

toml 만 고쳐서 안 되면 **해당 커스텀 노드를 지우고 재설치**하니 해결됐다.

> **같은 글에 '고장이 아닌' 사례도 함께 있다.** `%{소녀가 햄버거를 먹고있다.}` 처럼 번역 문법을 써도 그대로 나온다는 보고의 답은 — **그 버전부터 번역 기본값이 OFF 로 바뀌었으니 설정창에서 구글 번역을 다시 켜라**였다. 기능 고장이 아니라 기본값 변경이다. **업데이트 뒤 갑자기 안 되는 기능은 설정 기본값부터 확인한다.**

### `mat1 and mat2` — 로라가 아니라 계열이 안 맞는 것이다

```
RuntimeError: mat1 and mat2 shapes cannot be multiplied (154x1024 and 768x256)
```

특정 로라들만 이 오류를 내며 아예 동작하지 않는다. **로라 파일이 깨진 게 아니다** (68448644, 2023-01 댓글).

> 숫자 **768 과 1024 는 서로 다른 텍스트 인코더 차원**을 가리킨다 — **SD 1.x 계열은 768, SD 2.x 계열은 1024** 다. 즉 SD 2.x 기반으로 학습된 로라를 SD 1.5 계열 체크포인트에 물리면 이 오류가 난다.

**해결은 로라와 같은 계열의 체크포인트를 쓰는 것**이다.
2023년 사례지만 **형태가 그대로 살아 있다** — 오늘날로 옮기면 SD1.5 용 로라를 SDXL/Illustrious 에, 또는 ILXL 로라를 ANIMA 에 물렸을 때 같은 종류의 충돌이 난다.
**일반화하면 — 행렬 곱 shape 불일치 오류가 뜨면 로라 파일이 아니라 '로라의 베이스 계열 ≠ 체크포인트 계열' 을 의심한다.**
→ [로라 쓰는 법](lora-usage.md) · [모델 고르기](models.md)

### 아이콘 깨짐 — ⚠ 폰트가 아니라 브라우저다

챈 도구(Ultimate SNS generator)에서 아이콘이 깨질 때의 안내가 본문과 댓글에서 갈린다 (170679152, 2026-05).

**본문 주장** — 아이콘이 깨지면 구글 폰트 **Material Icons** 와 **Material Icons Outlined** 두 개를 시스템에 설치하면 된다.

> ❌ **이 설명만으로는 틀렸다.**
>
> 댓글의 정정 — **폰트를 둘 다 깐 상태에서도** 트위터 말풍선의 리트윗·하트 아이콘이 깨진다는 보고가 있었고, **원인은 브라우저였다. Brave 에서는 깨지고 Chrome 에서는 정상 동작한다.**

**폰트를 깔았는데도 아이콘이 깨지면 크롬으로 연다.** 폰트 설치 자체는 여전히 선행 조건이므로, 순서는 **① 폰트 두 개 설치 → ② 그래도 깨지면 Chrome** 이다.

→ [자원](resources.md)

<small>근거 — [Ultimate SNS generator 만들어서 공유해봄 26.05](https://arca.live/b/aiart/170679152) · [EasyUseAnima 0.3.1: 버그픽스, 업스케일, P… 26.07](https://arca.live/b/aiart/176029127) · [뉴비 특정 lora만 안 돌아가는 문제가 있슴 23.01](https://arca.live/b/aiart/68448644)</small>

## ⚠ TiledVAE 타일 크기 — 본문과 댓글이 갈린다 (2024-10)
<small>⚠️ 2024-10 기준 · 근거 1건 · **근거 약함** · 자료 엇갈림</small>

**2024-10 A1111 + Illustrious XL 시절 실험이다.** TiledVAE 는 이미지를 여러 타일로 쪼개 처리해 메모리 부담을 줄이고 다시 붙이는 확장이다.
쓰는 사람에게는 여전히 유효한데, **본문과 댓글의 이해가 갈린다.**

### 본문(실험자)의 가설

> **생성될 이미지 크기 ÷ 타일 크기가 자연수로 딱 나눠떨어져야 타일이 쪼개지고 합쳐질 때 빈틈이 안 생긴다.**

| 값 | 잡는 법 |
|---|---|
| Encoder Tile Size | 이미지 **높이** 그대로, 또는 그것의 1/2 · 1/3 · 1/4 · 1/6 |
| Decoder Tile Size | Encoder 의 **1/8** 또는 1/16 |

실측(1024x1536, illustriousXL + sdxlVAE, Heun / SGM Uniform / 27스텝 / CFG 4.5 / RTX 2070S):

| 조합 | 결과 |
|---|---|
| **Encoder 768 / Decoder 96** (1536÷2, 1:8) | **저점이 확실히 올라가고 작가 프롬도 일관되게 먹었다** |
| Encoder 784 / Decoder 80 (나눠떨어지지 않음) | 업스케일러를 켰는데도 전체 품질이 떨어졌다 |
| Encoder 768 / Decoder 48 (1:16) | 저점은 1:8 과 비슷, 고점은 1:8 이 더 좋았다 |

본문 정리로는 **인코딩 값이 안 맞으면 나눠 생성할 때 데이터를 잃고, 디코딩 값이 안 맞으면 결합할 때 노이즈가 생긴다.**

### ⚠ 댓글에서 이 이해가 상당 부분 뒤집힌다

> **인코더 사이즈는 img2img 에서만 쓰여서 txt2img 에는 별 상관이 없고, 정작 중요한 것은 디코더 사이즈다.**

| 댓글 쪽 정리 |
|---|
| 디코더는 **최대 변을 8로 나눈 값 이상**으로 쓰지 않으면 무조건 화질 손상이 온다 (**64의 배수**로 맞추는 게 좋다) |
| SDXL 계열은 덜 티가 나지만 **Pony 계열은 디코더 타일 크기를 작게 잡으면 화질 저하가 심하게 눈에 띈다** |
| 다만 8로 나눈 값만 쓰면 VRAM 은 덜 먹어도 **원본 생성과 시간 차이가 거의 없어**, 그 이하에서 핫스팟을 찾는 편이 낫다 |

**양쪽을 다 적어 둔다. 확정되지 않았다.**
그 밖에 "일반 생성에서는 끄고 hires 돌릴 때만 켠다", "그냥 1536/96 으로 쓴다" 는 사용례도 함께 나왔다.

→ [업스케일과 화질](upscale.md) · [VRAM·속도 최적화](vram.md)

<small>근거 — [페) ILXL) TiledVAE 관련 미세? 실험 24.10](https://arca.live/b/aiart/119251783)</small>

## ⚠ ECC 를 켜 두면 램 오프로딩이 아예 안 돈다 — 엉뚱한 데를 고치고 있었다 (2026-01)
<small>2026-01 기준 · 근거 1건</small>

**증상만 보면 램 오프로딩 기능 자체가 고장난 것처럼 보이지만, 범인은 GPU 설정이다.**
2026-01, RTX 3090 Ti · RTX 4090 처럼 **ECC 를 지원하는 소비자용 카드**에서 나온 사례다.

| | |
|---|---|
| 증상 | ComfyUI 의 **pinned-memory 램 오프로딩이 동작하지 않고**, 램이 넉넉한데도 `OOM` 이 난다 |
| 배경 | ComfyUI 가 자체 램 오프로딩을 넣으면서 기존 **블록 스왑 커스텀 노드를 비활성화**했고, "새 오프로딩이 내 환경에선 안 돈다"·"블록 스왑이 죽으면서 OOM 이 난다" 는 항의가 레딧·깃헙에 이어졌다 |
| **채널·해외에서 유행한 대처** | 추가된 **`nodes_nop.py` 를 지워** 옛 블록 스왑 노드를 되살린다 — **대증요법이지 근본 해결이 아니다** |

### 진짜 단서는 콘솔 첫 줄에 있다

문제를 겪는 사용자의 콘솔에 이렇게 찍혀 있었다.

```
Total VRAM 23028 MB
```

**같은 GPU 를 쓰는 정상 환경과 약 1.5GB 차이가 났다.**
이것은 **하드웨어 수준에서 무언가가 VRAM 을 점유하고 있다**는 뜻이고, 곧 **ECC 가 켜져 있다는 신호**다.
(ECC = 메모리 오류 정정. 켜면 VRAM 일부를 패리티에 쓴다.)

### 해결 — NVIDIA 제어판에서 ECC 해제

체크 하나를 풀면 **점유되던 1.5GB VRAM 을 되찾을 뿐 아니라 램 오프로딩 이슈도 완전히 사라졌다.**
글쓴이 환경에서는 **램 96GB 로 40GB 모델까지 안정적으로 돌아갔다.**

> **켜 둘 이유도 없다(댓글)** — 4090 의 ECC 는 전용 ECC 램이 아니라 **소프트웨어로 흉내 낸 수준**이라
> 켜면 **눈에 띄게 느려지기만 한다.** 진짜 ECC 가 필요하면 쿼드로/프로 계열을 써야 한다.

**확인 순서** — ① 콘솔의 `Total VRAM` 값을 같은 GPU 사양과 비교한다 → ② 1~2GB 적게 뜨면 NVIDIA 제어판에서 ECC 를 본다 → ③ 끄고 재실행한다.

*(한 글에서 규명된 것이지만 콘솔 값이라는 검증 가능한 단서가 있고, `nodes_nop.py` 삭제라는 기존 대처와 어느 쪽이 근본인지가 분명하다.)*

→ [VRAM·속도 최적화](vram.md) · [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [ComfyUI 램 오프로딩(RAM Offloading) EC… 26.01](https://arca.live/b/aiart/161052343)</small>

## 낡았지만 살아 있는 규칙 둘 — 종횡비, 그리고 잘못 알려진 lineart adjuster
<small>⚠️ 2025-01 기준 · 근거 2건 · 자료 엇갈림</small>

낡은 글에서 건진 것 중, **지금도 그대로 통하는데 요즘 글에서는 잘 안 다뤄지는 규칙 둘**이다.

### ① 학습 데이터의 종횡비가 결과 종횡비의 타율을 결정한다 (2024-07)

어떤 그림체 로라가 **세로 구도에서만 유난히 찐빠가 잦다면**, 세팅 문제가 아닐 수 있다.

> 그림체 로라를 만든 사람이 댓글에서 이유를 밝혔다 —
> **애니 캡처를 그대로 떠다 태깅하고 학습했기 때문에(원본이 가로 화면) 세로는 찐빠가 잦다.**

**즉 학습 데이터의 종횡비가 결과물의 종횡비 타율을 결정한다.**
받아 쓰는 쪽에서는 **"이 로라는 가로가 잘 나온다" 를 버그가 아니라 성질로 이해**하면 된다.
만드는 쪽에서는 데이터셋 종횡비를 목표 출력에 맞춰야 한다.

*(같은 글에서 나온 또 하나 — **비슷한 외형의 캐릭터를 한 데이터셋에 넣으면 개념이 섞인다.**
루피가 이상하게 나온 원인이 키드를 같은 데이터셋에 넣은 것이었다. → [로라 쓰는 법](lora-usage.md))*

**2024-07 Pony(SDXL) 시절 사례이지만 원리는 지금도 유효하다.**

### ② `lineart adjuster` 는 선 굵기를 조절하지 않는다 (2025-01 정정)

소개글 **본문은 "무테에 가깝게 만드는 것부터 실제 붓질 느낌까지 선을 조절할 수 있다"** 고 적었다.

> **댓글의 정정: 선을 굵게~얇게 조절해 주는 것이 아니라 '덩어리진 느낌' 으로 바뀌는 쪽이라 기대와 다를 수 있다.**

**"선을 얇게 만들고 싶다" 는 목적으로 이 로라를 받으면 원하는 결과가 안 나온다.**
같은 댓글에서 **SD1.5 시절 잘 되던 슬라이더 LoRA 들이 XL 에서는 대체로 애매했다**는 언급도 함께 나왔다.

→ [로라 쓰는 법](lora-usage.md) · [모델 고르기](models.md)

<small>근거 — [Ie 아티스트 로라 v2 만듬 + 쓸만한 툴 로라 추천 25.01](https://arca.live/b/aiart/127368119) · [(pony) 원피스 애니 와노쿠니 스타일 로라 공유 24.07](https://arca.live/b/aiart/112312429)</small>

## 본문이 틀린 것 — 모델 '경량화 7GB→4GB' 는 fp32→fp16 일 뿐이다 (2023-02)
<small>⚠️ 2023-02 기준 · 근거 1건 · 자료 엇갈림</small>

바로 아래 '채널에 도는 틀린 설명 셋' 과 같은 계열이다. **원문(본문)이 틀렸고 댓글이 맞은** 사례라 따로 적는다.

**본문 주장** — Anything V3.0 의 7GB 파일을 4GB 로 **'경량화'** 할 수 있다. WebUI 의 체크포인트 병합(Checkpoint Merger) 탭에서 주 모델에 줄이고 싶은 모델만 넣고, `Multiplier` 는 병합이 아니므로 **0**, 보간 방법은 **None**, 그리고 옆의 **`Save as float16` 을 반드시 체크**한 뒤 Merge 를 누르면 4GB 모델이 나온다 (68966157, 2023-02).

> ❌ **'경량화' 라는 설명은 틀렸다.**
>
> 댓글의 정정 — 이건 경량화라기보다 **fp32 를 fp16 으로 낮춘 것**이고 **EMA 가중치는 그대로 남아 있다.** 게다가 **Anything V3 기준으로는 결과물 그림도 조금 달라진다.** 즉 "용량만 줄고 그림은 같다"가 아니다.

**제대로 줄이려면** — `sd-webui-model-converter` 확장을 쓴다.

```
https://github.com/Akegarasu/sd-webui-model-converter.git
```

| 방법 | 결과 |
|---|---|
| 병합 탭 `Save as float16` (본문) | 7GB → **4GB** (fp32→fp16만, **EMA 잔존**, 그림이 조금 달라짐) |
| model-converter 로 **fp16 + no-ema** | **2GB** |
| 그림이 바뀌는 게 싫어 **fp32 유지 + no-ema 만** | **3GB 가량 절감** |

이 확장은 체크할 항목이 `fp16` · `no-ema` · `ckpt/safetensors` 세 개뿐이라 오히려 더 직관적이고, 지금은 확장기능 목록에 등록돼 있어 `Install from URL` 없이도 설치된다.

**이 정정이 중요한 이유** — 아래 '채널에 도는 틀린 설명 셋' 의 두 번째 항목(`safetensors` 는 컨테이너 형식일 뿐이며 **용량을 좌우하는 것은 fp16 여부와 EMA 포함 여부**)과 정확히 같은 이야기다. 같은 모델이 7.2GB / 4GB / 2GB 로 나뉘는 것이 바로 이 두 축 때문이다.

> 덧 — 당시 "코랩이 Anything V3 를 못 견딘다"는 이야기는 확장자를 `safetensors` 로 바꾸면 해결되는 문제이기도 했다.

→ [용어집](glossary.md) · [모델 고르기](models.md)

<small>근거 — [기초) 모델들 용량 줄이는 방법 (병합 활용 7GB->4GB) 23.02](https://arca.live/b/aiart/68966157)</small>

## 채널에 도는 틀린 설명 셋 — 바로잡는다
<small>⚠️ 2023-02 기준 · 근거 4건 · **근거 약함** · 자료 엇갈림</small>

원문(본문)이 틀렸고 **댓글이 맞은** 사례들이다. 셋 다 지금도 채널에서 재생산되고 있어서 따로 적는다. 양쪽을 다 적되, **어느 쪽이 틀렸는지 분명히 밝힌다.**

### 1. "WebUI 가 Standby 메모리를 누수한다"

**본문 주장** — 모델을 계속 바꿔 끼우거나 병합을 반복하면 작업 관리자 메모리 탭의 **흰색(Standby, 대기) 영역**이 비정상적으로 커지고 WebUI 를 종료해도 그대로 남는다. 이것이 '메모리 유출'이므로 RamMap 의 `Empty > Empty Standby List` 로 비워야 한다 (69230678, 2023-02).

> ❌ **'누수'라는 진단은 틀렸다.**
>
> 댓글의 정정 — **Standby 는 누수가 아니라 윈도우가 종료된 프로세스의 메모리를 바로 버리지 않고 다음 실행 때 즉시 재할당하려고 남겨 두는 정상 캐시다.** (프로그램을 껐다 바로 켜면 더 빨리 뜨는 이유가 이것이다.) **메모리가 부족해지면 윈도우가 알아서 이 영역을 회수하므로 대개 손댈 필요가 없다.**

**그래도 남는 사실 두 가지** —

- **WebUI 가 가상 메모리까지 잔뜩 먹는 것 자체는 WebUI 쪽 문제가 맞다**는 데는 댓글도 동의한다. 심하면 XYZ 그리드를 돌리다 C 드라이브가 꽉 차는 일이 실제로 생긴다.
- `RamMap` 의 `Empty > Empty Standby List` 는 **즉시 비우는 응급 수단으로는 유효하다.** 주기적 자동 정리 도구로 `memreduct` 도 언급된다.

즉 **"누수라서 반드시 비워야 한다"가 아니라 "정상 캐시지만 급하면 비울 수 있다"** 가 맞다.

### 2. "safetensors = 학습 데이터를 포함한 대용량 형식"

**본문 주장** — 모델 병합 출력 형식을 설명하며 `half = 저용량 파일(fp16)`, `safetensors = 학습용 데이터 포함 대용량` 이라고 적었다 (70241791, 2023-02).

> ❌ **이 설명은 틀렸다.**
>
> **`safetensors` 는 파일 컨테이너 형식일 뿐이라 용량과 무관하다.** 모델 파일 용량을 좌우하는 것은 **fp16 여부와 EMA 포함 여부**다.

같은 모델이 7.2GB(원본) / 4GB(학습용 부분 제거) / 2GB(F16 변환) 로 나뉘는 것이 그 증거다. `safetensors` 를 받는 이유는 용량이 아니라 **`.ckpt` 에 숨어 있을 수 있는 악성코드 위험을 없앤 포맷이기 때문**이다.

> 덧붙여 — **확장자만으로는 임베딩·하이퍼네트워크·모델·VAE·로라를 구분할 수 없다.** `.pt` · `.safetensors` · `.bin` 은 전부 학습 결과를 담은 저장 포맷일 뿐이라 **용량으로 판별**해야 한다 → [설치와 환경 구성](install.md)

### 3. "SD 의 탐색 공간은 3x512x512 다"

**본문 주장** — 512x512 컬러 이미지의 경우의 수를 `256^(512*512*3) ≈ 10^1887436` 으로 계산하며, AI 는 이 거대한 공간에서 그림을 찾아내는 것이라고 설명했다 (70488954, 2023-02).

> ❌ **탐색 공간 계산이 틀렸다.**
>
> 댓글의 정정 — **실제 Stable Diffusion 의 확산은 픽셀 공간이 아니라 VAE 로 8배 압축한 `4x64x64` 잠재 공간(latent space)에서 일어난다.** VAE 인코더가 이미지를 64x64 로 압축하고 거기서 확산을 돌린 뒤 다시 VAE 로 512x512 로 복원한다. 이렇게 만든 이유는 **개인용 그래픽카드에서도 돌아가게 하기 위해서**다.

**이 정정이 실용적으로 중요한 이유** —

| 왜 궁금했나 | 답 |
|---|---|
| 왜 **해상도를 8의 배수**로 맞춰야 하나 | **잠재 1픽셀 = 실제 8픽셀** 이기 때문이다 |
| 왜 **`latent` 업스케일러**라는 게 따로 있나 | 픽셀이 아니라 잠재 공간에서 키우는 방식이 따로 있기 때문이다 |

(큰 그림 자체 — '이미 존재하는 그림을 찾아내는 것'이라는 비유와 우주 원자 수 `10^82`, 바둑 `10^768` 과의 비교 — 는 그대로 유효하다.)

→ [용어집](glossary.md) · [업스케일과 화질](upscale.md)


<small>근거 — [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법 23.01](https://arca.live/b/aiart/66582124) · [WebUI 쓸때 메모리 유출문제 해결방법 23.02](https://arca.live/b/aiart/69230678) · [AI는 고차원 공간에 이미 존재하는 그림을 찾아내는 것일 뿐 23.02](https://arca.live/b/aiart/70488954) · [병합하는 방법은 공지 없음?? 23.02](https://arca.live/b/aiart/70241791)</small>

## `--skip-torch-cuda-test` 는 도움이 되나 — 채널 안에서 갈린다
<small>⚠️ 2023-02 기준 · 근거 4건 · **근거 약함** · 자료 엇갈림</small>

같은 시기(2022~2023) 자료인데 **정반대로 말한다.** 어느 한쪽으로 정리하지 않고 양쪽을 그대로 적는다.

| 입장 | 근거 글 |
|---|---|
| **쓰라** — `Torch is not able to use GPU` 에는 `--skip-torch-cuda-test` 를 붙이고, 그래도 같은 에러면 `--precision full --no-half` 를 함께 쓴다 | 65362592 (2022-12, 에러 모음), 70243793 (2023-02, GTX 16xx 사례) |
| **쓰지 마라** — **이 인자는 문제 해결에 도움이 되지 않는다.** 해당 오류의 원인은 **xformers 와 torch 버전 불일치**이므로 버전을 맞춰야 한다 | 60216616 (2022-10, 통합팩), 67307479 (2023-01, 원클릭 실행기) |

**읽는 법** — `--skip-torch-cuda-test` 는 이름 그대로 **CUDA 사용 가능 여부 검사를 건너뛰는** 인자다. 즉 **원인을 고치는 것이 아니라 검사만 넘기는 것**이라, 진짜로 GPU 를 못 쓰는 상태라면 뒤에서 다시 터진다. 그래서:

- **일단 뜨게 만들어 원인을 좁히는 용도**로는 쓸 만하다 (그래서 저사양 배치파일 예시에 `--no-half --precision=full --lowvram` 과 함께 들어간다)
- **근본 해결은 버전을 맞추는 것**이다

두 입장 모두 한쪽 편에 각각 두 글씩이라 어느 쪽도 압도적이지 않다. 그리고 **넷 다 2022~2023년 A1111 기준**이라, xformers 자체를 쓰지 않는 지금 ComfyUI 환경에는 그대로 적용되지 않는다.


<small>근거 — [(구)WEB UI설치가 어려운 사람을 위한 통합팩 (0.66… 22.10](https://arca.live/b/aiart/60216616) · [(구)원클릭 윈도우 실행기 23.01](https://arca.live/b/aiart/67307479) · [WebUI 에러 모음 22.12](https://arca.live/b/aiart/65362592) · [LoRA 설치시 Error 및 해결방법 정리 23.02](https://arca.live/b/aiart/70243793)</small>

## 색이 뿌옇다 — VAE 가 안 걸린 것이다
<small>⚠️ 2023-01 기준 · 근거 4건</small>

**'색이 뿌옇게 나온다' = VAE 미적용**이 가장 흔한 원인이다. 로그로 바로 확인할 수 있다 (66138624, 2022-12).

**확인** — WebUI 를 실행하면 뜨는 **명령 프롬프트(검은 창)** 를 본다.

```
# 정상
Loading VAE weights from: C:\...\models\Stable-diffusion\01_NaiFull.vae.pt
Applying xformers cross attention optimization.
VAE Weights loaded.

# 어떤 VAE 도 적용되지 않은 상태
Restoring base VAE
```

**해결 — 상단에 고정 드롭다운을 만든다.** 설정(Settings)의 **빠른 설정 리스트(Quicksettings list)** 에 아래를 붙여 넣고 적용한 뒤, **WebUI 와 명령 프롬프트를 둘 다 껐다 켠다.**

```
sd_model_checkpoint, sd_hypernetwork, sd_hypernetwork_strength, CLIP_stop_at_last_layers, sd_vae
```

그러면 화면 최상단에 **체크포인트 · VAE · Clip skip** 드롭다운이 나타나 바꾸는 즉시 적용된다. 설정 창에 들어갈 일이 거의 없어진다.

> 이 기능 자체를 몰랐다는 반응이 많았던 것으로 보아, **상단 고정 드롭다운을 만드는 것**이 이 글의 핵심 수확이다. 자주 쓰는 것을 더 넣은 댓글 버전에는 `eta_noise_seed_delta` 도 들어간다.

**VAE 파일을 어디에 넣나** — `models\VAE` 든 `models\Stable-diffusion` 이든 **어느 쪽이든 동일하게 인식된다** (댓글에서 재확인). `models\VAE` 폴더에 'Put VAE here' 안내가 있으니 거기 넣어도 된다.

이래도 안 되면 재설치를 권한다. **ComfyUI 계열에서 결과가 탁하거나 흰 점이 찍히는 경우**는 원인이 달라 아래 '결과물이 이상할 때' 항목을 본다.

> ⚠ 설정의 `Ignore selected VAE for stable diffusion checkpoints with loaded VAE weights` 는 **체크 해제**여야 한다.
> 채널의 뉴비 FAQ 본문이 '체크' 라고 적어 두어 반대로 따라 하는 사람이 많다 → 위 **'VAE 를 둘러싼 오해 둘'**
>
> 그리고 **VAE 는 그림체를 바꾸지 않는다.** 색감·선명도만 좌우한다.

→ [설치와 환경 구성](install.md) · [모델 고르기](models.md)


<small>근거 — [(가이드) 프롬대장경 제 1권 『설치부터 t2i까지』 23.02](https://arca.live/b/aiart/68917133) · [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법 23.01](https://arca.live/b/aiart/66582124) · [(가이드) 뉴비 자주 묻는 질문 (FAQ) 23.01](https://arca.live/b/aiart/68598675) · [VAE 적용 확인 하는 법 22.12](https://arca.live/b/aiart/66138624)</small>

## 같은 시드인데 다르게 나온다 — 재현성 체크리스트
<small>⚠️ 2023-02 기준 · 근거 3건</small>

프롬프트·네거티브·샘플러·CFG·CLIP skip 을 전부 똑같이 맞췄는데 다른 이미지가 나올 때 확인할 것들이다. A1111 공식 위키의 `Seed-breaking-changes` 를 옮긴 것 (70485768, 2023-02).

**먼저 — 절대 못 맞추는 것 두 가지**

| 원인 | 설명 |
|---|---|
| **하드웨어 차이** | CPU·GPU 아키텍처(파스칼·튜링·에이다 등)마다 무작위 값을 만드는 방식이 다르다. 차이는 **20xx 이하에서 크고 30xx·40xx 에서는 거의 없다.** 완전히 동일한 연산 하드웨어를 써야만 해결된다 |
| **xformers 사용 유무** | **속도를 얻고 재현성을 버린다**고 생각하면 된다. SD 2.x 모델에 한해 `--xformers-flash-attention` 으로 개선 가능 |

**시대별 호환 옵션** — 옛날 시드를 재현하려면 `설정 > Compatibility` 에서 켠다.

| 그 시드가 만들어진 시점 | 무엇이 바뀌었나 | 되돌리는 옵션 |
|---|---|---|
| 2022-09-29 이전 | 강조 문법 구조 변경 | `Use old emphasis implementation` |
| 2023-01-01 이전 | Karras(k-diffusion) 샘플러의 sigma max/min 대응 | `Use old karras scheduler sigmas` |
| 2023-01-03 이전 | **Hires. fix 방식 변경** | 아래 변환표 |
| 2023-01-23 이전 | 대체 단어 문법 버그 수정 | 강조 프롬프트를 지우고 첫 괄호 문자로 대체 |
| 2023-02-19 이전 | `DPM++ SDE` 가 배치 크기에 따라 달라지던 버그 | `Do not make DPM++ SDE deterministic across different batch sizes` |

**Hires. fix 변환표** — 과거에는 폭·높이를 고정했지만 지금은 첫 생성(first pass) 크기를 잡고 배율이나 목표 크기를 지정한다.

```
과거)  Size: 1024x1024 / First pass size: 640x512
지금)  Size: 640x512 + Hires upscale: 2.0
       또는 Size: 640x512 + Hires resize: 1280x1024
```

과거 설정이 적힌 프롬프트를 붙여넣고 버튼을 누르면 **자동으로 계산해 준다.**

**대체 단어 문법 버그** — `[cat|(dog:1.1)]` 이 과거에는 `cat → ( → cat → (` 로 인식됐고 지금은 `cat → (dog:1.1) → cat → (dog:1.1)` 로 정상 인식된다.

출처: `https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Seed-breaking-changes`

> 로라를 쓴 남의 그림이 재현되지 않는 경우는 원인이 또 다르다 → [로라 쓰는 법](lora-usage.md)

### 그래픽카드가 다르면 결과도 다르다

체크리스트를 다 맞췄는데도 남의 샘플과 다르다면 여기까지 온 것이다 (1건, 2023-02, 댓글).

> 병합모델 배포자가 댓글에 남긴 단서 — **예시 그림은 GTX 1060 으로 뽑은 것이고,
> 더 좋은 그래픽카드를 쓰면 동일 시드·동일 프롬프트여도 샘플과 다른 결과가 나올 수 있다.**

**같은 시드는 '같은 난수' 를 보장하는 것이지 '같은 그림' 을 보장하지 않는다.**
배포글의 예시 이미지와 1:1 로 맞추려는 시도는 여기서 접는 것이 맞다.

> 같은 글에는 또 하나의 함정이 있었다 — **예시 그림 자체가 본문의 권장 설정으로 뽑힌 것이 아니었다**
> (hires.fix 를 끄고 아무 보정 없이 뽑은 것). **배포글의 '권장 설정' 과 '예시 이미지의 설정' 은 다를 수 있다.**

같은 계열의 다른 사례 — **돌리는 서버(모델·VAE 구성)가 바뀌면 그림체가 달라진다**
(2022-12, 챈섭을 중간에 바꿔 그림체가 바뀐 기록) → [프롬프트 쓰는 법](prompting.md) 「왜 그렇게 되는가」.


<small>근거 — [완전히 같은 이미지를 만들 수 없다면? - 재현성 체크리스트 23.02](https://arca.live/b/aiart/70485768) · [(병합대회) Sita7taker 23.02](https://arca.live/b/aiart/70499026) · [(꼴림찾아) 세일러 교복과 가터벨트 22.12](https://arca.live/b/aiart/65677286)</small>

## 버전 충돌
<small>2026-08 기준 · 근거 5건</small>

### `time_shift_slope` 오류 — MiniMaxH3-Cache

**경계 버전이 특정돼 있다:**

```
정상   ComfyUI v0.30.0-1-g14b05228c   (2026-08-02)
오류   v0.30.0-19-g88fec4b6 이후
```

**해결 세 가지** — 위로 갈수록 권장:

1. 원 저장소에 **PR이 올라와 있다.** 먼저 최신을 확인한다
2. 직접 고친다 — `__init__.py` 에서 `time_shift_slope` 로 구한 `slope_a` 를 오디오 출력에 곱하는
   부분을 지우고 `-audio_out` 을 그대로 반환한다 *(같은 내용의 업스트림 PR이 이유 없이 닫힌 적 있음)*
3. 업데이트를 미루거나 다운그레이드한다

### 영상이 검은 화면 (int8convrot Video VAE)

**해결 조건 네 가지를 모두 만족해야 한다:**
ComfyUI 최신 + torch `+cu130` 이후 + comfy-aimdo 최신 + comfy-kitchen 최신

> ⚠️ **미해결 사례가 있다.** PyTorch 2.11.0+cu130 신규 설치 환경에서도 검은 화면이 났다는
> 보고가 댓글에 남아 있다.

### 라데온: 0.31.0 에서 sage가 안 된다

ROCm on Windows 11 기준으로 **ComfyUI portable 0.30.0에서만 동작**하고 0.31.0은 버그로 안 됐다.
9070XT에서 스텝당 약 11.5초.

<small>근거 — [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [H3 캐시 고치는 법 26.08](https://arca.live/b/aiart/179254934) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848) · [ComfyUI Nightly용 Minimax H3 Cache… 26.08](https://arca.live/b/aiart/179215559)</small>

??? note "근거 5건 전부 보기"
    [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [H3 캐시 고치는 법 26.08](https://arca.live/b/aiart/179254934) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848) · [ComfyUI Nightly용 Minimax H3 Cache… 26.08](https://arca.live/b/aiart/179215559) · [ComfyUI 최신버전에서 MiniMaxH3-Cache 버그… 26.08](https://arca.live/b/aiart/179251955)

## 노드 충돌 — 같이 쓰면 안 되는 조합
<small>2026-08 기준 · 근거 3건</small>

| A | B | 결과 |
|---|---|---|
| MiniMaxH3 Cache | Spectrum Apply | **Error** |
| MiniMaxH3 Cache | EasyCache | 같이 못 씀 |
| MiniMaxH3 Cache | **터보 LoRA** | **결과물 박살남** — Cache는 계산 재사용, Turbo는 스텝 자체를 생략해 원리가 겹침 |
| NoobAI·V-pred 체크포인트 | Kohya Deep Shrink / DCW / Spectrum | 상성 나쁨 — **하나씩 바이패스**해서 범인을 찾는다 |

**최속 조합** (에러 없이 되는 것): `Cache + Mem Eff Sage Attention Patch + Patch Sage Attention KJ`
→ 309.58초가 94.73초로. 여기에 Spectrum을 더하면 에러다.

**Easy-Use 썸네일 충돌**: 설정 → easyuse → `모델 미리보기 썸네일 활성화`, `컨텍스트 메뉴에서
자동으로 하위 디렉토리를 중첩` 을 끈다.

<small>근거 — [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [MiniMax H3 가속 노드 별 속도 후기 26.08](https://arca.live/b/aiart/179038650) · [1시간전에 올라온 H3 고속 로라 테스트 26.08](https://arca.live/b/aiart/179280493)</small>

## 설치 — 안 찾아지거나 반영이 안 될 때
<small>2026-08 기준 · 근거 5건</small>

**매니저에서 검색이 안 되는 노드가 있다.** `SimpleMathInt+`, `CacheDiT`, `MiniMaxH3Cache` 등.
깃허브 zip을 받아 `custom_nodes` 에 풀거나 나이틀리로 설치한다.

**매니저 업데이트는 코어를 갱신하지 않는다.** 내장 노드 변경은 반영되지 않으므로
본체는 git 또는 `update_comfyui.bat` 로 올린다.

**릴리스가 아니라 main 브랜치여야 하는 경우도 있다.** EasyUseAnima는 리저널 노드의 인풋 소켓
누락 버그 때문에 git(main)으로 설치해야 수정본을 받는다.

**노드 이름이 이상하게 뜬다면 오인식이다.** `MiniMax H3 Mem Eff Sage Attention Patch` 와
`Patch Sage Attention KJ` 는 원래 **KJNodes 노드**인데, '엔크립트'·'어노말리' 계열로 표시되는 건
ComfyUI의 오인식 오류다. 그 이름의 노드를 따로 설치할 필요 없다.

**미싱 노드**는 ComfyUI Manager의 `Custom nodes in workflow` 로 한번에 설치한다.

**노드가 깨진 커밋으로 배포된 경우도 있다 — comfyui-sam3 사례.** SAM3 가 마스크를 제대로 잡지 못하고
**흩뿌려진 파티클처럼** 나오면 최신 커밋이 깨진 것이다. `2026-02-22` 이전 커밋으로 되돌린다 (165353584, 2026-03).

먼저 `ComfyUI\custom_nodes\comfyui-sam3\requirements.txt` 에서 **`comfy-attn` 줄을 통째로 지운다.**
남아 있으면 아래에서 설치가 중단된다.

```
ERROR: Could not find a version that satisfies the requirement comfy-attn (from versions: none)
ERROR: No matching distribution found for comfy-attn
```

그다음 그 폴더에서 순서대로 실행한다.

```
git checkout $(git rev-list -n 1 --before="2026-02-22" main)
git switch -c sam3-fixed
python -m pip install --upgrade pip
pip install -r requirements.txt
```

확인된 정상 커밋은 `607a21da2ec5ae7916d8e3cbbb80854ee0044992` (2026-02-21) 이다. 댓글은 `comfy-env==0.2.10` 줄도
함께 지우기를 권한다.

<small>근거 — [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.… 26.01](https://arca.live/b/aiart/160657113) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [EasyUseAnima 0.2.0: 다양한 편의성 노드와 리… 26.06](https://arca.live/b/aiart/175458978)</small>

??? note "근거 5건 전부 보기"
    [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.… 26.01](https://arca.live/b/aiart/160657113) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [EasyUseAnima 0.2.0: 다양한 편의성 노드와 리… 26.06](https://arca.live/b/aiart/175458978) · [뉴비기준 sam3 노드 문제해결방법 26.03](https://arca.live/b/aiart/165353584)

## 결과물이 이상할 때
<small>2026-07 기준 · 근거 9건</small>

### 안 시켰는데 비키니가 나온다

원인은 **퀄리티 태그**다. `masterpiece`, `best quality`, `score_7` 같은 태그가 사실상
"고평점 = 야짤"을 부른다.

> **네거티브에 `bikini` 를 넣어도 안 된다.** 프롬프트에 **`safe` 태그**를 넣어야 해결된다.

### ADetailer 후 검은 사각형 → 이미지 전체가 검게 (Forge Neo)

`COMMANDLINE_ARGS` 를 아무리 바꿔도 소용없다(`--sage --uv`, 빈 값, `--uv` 만 등 전부 실패).
`Haoming02/ADetailer-Neo` 로도 재발한다.

**해결**: extensions 에서 기존 adetailer 체크를 해제하고 `abzaloff/aadetailer-neoforge` 로 교체.
*(작성자도 5시간 이상 검증하지는 못했다고 밝힘)*

### ANIMA 그림이 기괴해진다

**Euler A / automatic 조합에서 발생한다.** `Euler` 또는 `ER SDE` + `simple` 또는 `SGM uniform` 을 쓴다.

### LTX LoRA에서 중국어 음성이 나온다

중국어로 훈련된 LoRA다. **LoRA Audio 강도를 0으로** 둔다. 그리고
`ltx-2.3-22b-distilled-1.1_transformer_only_fp8_scaled.safetensors` 로만 써야 강도를 올려도 화면이 안 깨진다.

### SDXL/Illustrious 결과가 탁하거나 흰 점

**VAE Select = 2** (`fixFP16ErrorsSDXLLowerMemoryUse_v10`)

### 어느 날부터 선이 지저분하게 뭉개진다 — `fp8_e4m3fn`

같은 프롬프트와 세팅으로 다시 뽑아도 재현되고, 예전에는 깨끗하게 나오던 그림이다 (178281311, 2026-07).

> **원인은 ComfyUI 의 UNET weight dtype 이 `fp8_e4m3fn` 으로 되어 있는 것이다. `default` 로 되돌리면 정상으로 돌아온다.**

`Load Diffusion Model` / `UNET Loader` 계열 노드의 **`weight_dtype`** 을 확인한다.
fp8 계열은 VRAM 사용량을 줄이려고 **정밀도를 낮추는** 옵션이라 속도·메모리에는 이득이지만 **선이나 디테일 품질이 눈에 띄게 떨어질 수 있다.**
로컬을 처음 시작할 때 그림체를 다듬으면서 한 번 켜 보고 잊는 경우가 많다.

### 그림 전체가 희뿌옇게 변하며 그림체가 무너진다 (WAI · naiXL vpred)

증상의 특징이 구체적이다 (173511292, 2026-06).

- 가중치를 낮추거나 태그를 지워 나가면 **망가진 그림체는 돌아오지만 희뿌연 색은 좀처럼 되돌아오지 않는다**
- "아까는 이보다 더 많이 쓰고도 잘 나왔는데" 싶을 만큼 **왕창 줄여야 비로소 정상화**된다
- 즉 **임계점을 한 번 넘으면 원래 잘 되던 수준으로 되돌려도 회복되지 않는다**

| 관찰 | |
|---|---|
| 방아쇠 | **태그 하나만 더 추가하면 발생하고 그 태그를 빼면 정상화**되는 사례. `cum` 계열 가중치가 높을 때 잦았다는 경험 |
| 가중치 | **최대 1.2 밖에 안 줬는데도** 발생 |
| 모델 | naiXL vpred 에서도 발생(심하면 점묘화처럼 일그러짐). **ANIMA 에서는 목격 사례가 없다는 증언이 둘** |

**유력한 가설** — 프롬프트 실수가 아니라 illustrious/vpred 계열 구형 모델 쪽 특성으로, **학습 데이터가 부족해 현재 그림체로 재현하기 어려운 태그에 가중치를 높게 주면 모델이 무너진다**는 것이다.

**대처** — 특정 태그 하나가 방아쇠일 수 있으니 **마지막에 추가한 태그부터 의심해 빼 보고, 가중치를 습관적으로 올리지 않는다.**

### ANIMA 에서 crotch 에 겹선이 계속 나온다 — 모델 특성이다

사타구니 부근에 허벅지 살이 접힌 듯한 표현이 **이중으로 겹쳐** 계속 나오는 문제다 (176433146, 2026-07).

> **결론: ANIMA 베이스 모델 자체의 특성이다.** 프롬프트나 설정으로 해결할 문제가 아니므로 **옷을 입히거나 인페인트로 지우는 식으로 우회**한다.

이 글의 진짜 쓸모는 결론보다 **그 결론에 도달한 절차**다 — 아래 '원인을 가리는 절차' 참조.

### 손 찐빠 보정이 한쪽 손만 된다

검출 + 인페인팅 노드로 손을 고치는데 **한쪽 손만 잡아 고치고 다른 손은 건드리지 않는** 문제다 (175325170, 2026-06).

> **해결 — `bbox`(바운딩 박스) 검출 임계치(threshold)를 낮추면 두 손을 모두 인식한다.**
> 검출 모델이 **확신도가 낮은 손을 버리고 있었던** 것이다.

**'수정이 일부 부위에만 적용된다' 면 프롬프트가 아니라 검출 임계치를 먼저 의심한다.**
곁가지로, **SDXL 시절의 검출/인페인팅 노드 구성은 체크포인트만 ANIMA 로 바꾸면 그대로 쓸 만하다**는 것도 확인됐다.

### 자세 태그가 가중치를 아무리 줘도 안 먹는다

`head_back` 에 가중치 3.0 을 줘도 안 먹는다는 질문에서 원인이 밝혀졌다 (172856945, 2026-06).

> **범인은 그 자세와 충돌하는 부위 강조 태그다.** 프롬프트에 `(red eyes:2.0)` · `(clear eyes:1.5)` ·
> `beautiful detailed eyes` 처럼 눈 묘사가 잔뜩 들어 있으면, 모델이 **눈을 포함한 얼굴을 계속 정면으로 그리려 해서**
> 고개를 젖히는 태그가 이길 수 없다. **눈 태그를 지우자 즉시 작동했다.**

**가중치를 더 올리지 말고 충돌하는 태그를 먼저 지운다.** 자세히는 → [ANIMA](anima.md)

<small>근거 — [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [미니맥스 H3 Edit 모델로 써 본 간단 후기 26.08](https://arca.live/b/aiart/178880588) · [LTX 2.3 테스트중인 로라 하나 추천 26.06](https://arca.live/b/aiart/173213921) · [저처럼 forge neo쓰다가 여러 문제를 겪으시는분들 혹시… 26.06](https://arca.live/b/aiart/174448928)</small>

??? note "근거 9건 전부 보기"
    [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [미니맥스 H3 Edit 모델로 써 본 간단 후기 26.08](https://arca.live/b/aiart/178880588) · [LTX 2.3 테스트중인 로라 하나 추천 26.06](https://arca.live/b/aiart/173213921) · [저처럼 forge neo쓰다가 여러 문제를 겪으시는분들 혹시… 26.06](https://arca.live/b/aiart/174448928) · [선 지저분하게 나오는 문제 해결! 26.07](https://arca.live/b/aiart/178281311) · [head_back 태그가 안 먹음 (wai anima bas… 26.06](https://arca.live/b/aiart/172856945) · [WAI로 그림 뽑다 보면 종종 마주치는 문제 26.06](https://arca.live/b/aiart/173511292) · [comfy에서 anima로 돌리는데 계속 crotch 쪽 찐… 26.07](https://arca.live/b/aiart/176433146) · [손찐빠 보정할때 한쪽손만 수정하는 문제 해결방법 아시는분..? 26.06](https://arca.live/b/aiart/175325170)

## 멈춘 것처럼 보일 때
<small>2026-06 기준 · 근거 3건</small>

**인페인팅이 `Pause 0%` 에서 멈춘다** — 오류가 아니다. 워크플로우 안에서 **파랗게 깜빡이는
`Continue` 버튼**을 누르면 진행된다.

> 이 질문에 제미나이는 "하드웨어 병목"이라고 답했다. **오답이다.**

**`Validate Prompt` 서브그래프 오류** — 검사 실패 시 에러를 내도록 만든 것인데 오류가 잦다.
비활성화하거나 지우고 직접 연결해도 된다 *(작성자도 없애겠다고 함)*.

**`FALLBACK` 로그**는 오류가 아니다. "이번 스텝은 불안정하니 정상 계산했다"는 뜻이다.

**Grok 워크플로우**는 프롬프트를 비우면 오류가 난다. **마침표 하나라도** 넣는다.
인증 파일은 `c:\사용자\.grok\auth.json`.

<small>근거 — [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179083162) · [GPT PRO가 맨든 미니맥스 고속노드 26.08](https://arca.live/b/aiart/179254885)</small>

## 환경별 — AMD / Intel
<small>2026-08 기준 · 근거 3건</small>

**Intel B580 은 구동 실패**했다. 세 시간 씨름 끝에:
- int8convrot — 1회는 13분, 2회차에 `UR_LOST` 에러
- fp8 — **BSOD**
- dynamic vram 불안정

**AMD는 되기는 한다.** 다만 느리다:

| GPU | MiniMax H3 I2VA (544x800, 20스텝) |
|---|---|
| RTX 5090 | 1분 04초 |
| RTX 3090 | 2분 41초 |
| **R9700** | 3분 27초 |
| **RX 7900XT** | 6분 53초 |
| RTX 3060 | 8분 59초 |

R9700은 sage attention이, RX 7900XT는 flash attention이 빨랐다.
AI Max 395 + rocm 7.2에서 Wan 2.2는 960x640 81프레임에 거의 1시간이 걸렸고,
우분투로 옮겨도 향상이 미미해 윈도우가 권장됐다.

<small>근거 — [GPU 5종 MiniMax H3 I2VA 생성속도 테스트 26.08](https://arca.live/b/aiart/179069083) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848) · [Ubuntu,윈도우 ai max 395 wan2.2 후기 26.01](https://arca.live/b/aiart/160894544)</small>

## NovelAI 비공식 클라이언트는 현재 로그인 자체가 불가능하다 (2026)
<small>2026-04 기준 · 근거 1건</small>

NAI 를 자동 생성 앱·비공식 클라이언트로 쓰던 사람이 갑자기 못 쓰게 되는 문제다. **버그가 아니라 서비스 쪽 변경이다.**

> **2026년 중반 NovelAI 가 로그인에 reCAPTCHA 를 도입하면서, NAIApp 을 포함한 비공식 클라이언트의 로그인이 불가능해졌다.** `please refresh novelai.net` 이 뜨며 재로그인이 실패한다는 제보가 다수다 (168830995 댓글, 2026-04. 관련 글 `https://arca.live/b/aiart/176933271`).

따라서 그 계열 앱은 **지금은 그대로 쓸 수 없다고 봐야 한다.** 앱 자체의 설정을 아무리 만져도 해결되지 않는다.

참고로 같은 앱의 모델별 레퍼런스 제약도 정리돼 있다 — `Vibe Transfer` 는 **v4 이상**, `Character Reference` 는 **v4.5 이상** 모델에서만 쓸 수 있고, UI 에서 비활성화된 레퍼런스 기능이 실제 요청 payload 에 남아 **400 오류**를 만들던 버그가 있었다.

→ [NovelAI](nai.md)


<small>근거 — [NAI 자동생성 앱 (NAIApp) v1.4.0 26.04](https://arca.live/b/aiart/168830995)</small>

## 아직 답이 없는 것
<small>2026-08 기준 · 근거 6건 · **근거 약함** · 자료 엇갈림</small>

정직하게 — 채널에서 해결되지 않은 것들이다.

- **int8convrot 검은 화면** — 권장 조건을 다 맞춘 환경(PyTorch 2.11.0+cu130 신규 설치)에서도 재현 보고
- **DaSiWa 워크플로우** — MiniMax H3 Director 노드 업데이트 이후 작동하지 않는다는 보고
- **묵직·둔탁한 효과음** — MiniMax H3 I2V에서 "무슨 짓을 해도 제거 안 됨"
- ~~**로라 확장자가 `.safetensors` 로 안 나옴** (2023년 LoRA 학습)~~ — **답이 나왔다.**
  `LoRA` 탭이 아니라 **`Dreambooth` 탭으로 학습한 것**이다 → [로라 쓰는 법](lora-usage.md)
- **`RuntimeError: CUDA error: the launch timed out and was terminated`** — 2023년 오류 모음글 댓글에서
  **여러 명이 겪었는데 끝내 풀리지 않았다.** 나온 답은 *"모델 호환 문제이니 다른 체크포인트를 쓰라"* 뿐이었다.
- **VLM 프리뷰가 PreviewMonitor 에 안 뜬다** — ComfyUI 0.21.1 리눅스에서 **KSampler 미리보기는 되는데
  `PreviewMonitor` 노드에는 안 보인다**는 보고(`--front-end-version` 켜진 상태)가 미해결로 남아 있다.


**오류 로그를 그록에 붙여넣으면 대부분 해결된다**는 조언이 반복해서 나온다. 채널에 답이 없을 때
쓸 만한 마지막 수단이다.

<small>근거 — [Lora 학습 실패로 자살하고 싶은 ㅈ밥 뉴비들만 이리와라 23.02](https://arca.live/b/aiart/69186437) · [스압주의) 미맥H3 i2v NSFW프롬프트 팁 공유. 26.08](https://arca.live/b/aiart/179445963) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797)</small>

??? note "근거 6건 전부 보기"
    [Lora 학습 실패로 자살하고 싶은 ㅈ밥 뉴비들만 이리와라 23.02](https://arca.live/b/aiart/69186437) · [스압주의) 미맥H3 i2v NSFW프롬프트 팁 공유. 26.08](https://arca.live/b/aiart/179445963) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [(커스텀노드) ComfyUI-PreviewMonitor: 프… 26.05](https://arca.live/b/aiart/171041315) · [AI그림 채널 오류 해결책 모음 23.02](https://arca.live/b/aiart/70417374)

## 배경에 얼굴이 덕지덕지 복제된다 — 범인은 작가 태그 '조합' 이다
<small>⚠️ 2025-03 기준 · 근거 1건</small>

"칠판 낙서에서 얼굴이 나온다" 로 시작해 **인형·뱃지·티셔츠·벽지·액자·키링** 형태로 일그러진 얼굴이
배경에 덕지덕지 복제되는 현상이다. 매개체(예: `chalkboard`)를 지워도 다른 물건으로 옮겨 다닌다.
2025년 3월, 하루를 통째로 써서 파고든 기록이 있다 (131650885).

### 먼저 — 실패한 시도들

**이걸 아는 것이 절반이다.** 아래는 전부 효과가 없었다.

| 시도 | 결과 |
|---|---|
| `solo` , `1girl` 을 맨 앞에 박기 | ❌ |
| 네거티브에 `multiple others` | ❌ |
| `blank chalkboard` 같은 자연어로 매개체 비우기 | ❌ |
| 퀄리티 태그 **전부** 지우기 | ❌ |
| 퀄리티 태그 · 작가 태그 · `1girl` 의 **순서 바꾸기** | ❌ |

### 효과가 있었던 네거티브

```
extra faces, multiple faces, photo (object), drawing (object), painting (object)
```

이걸 넣고 나서야 복제가 **'잦아들었다'.**
⚠ **완전히 없어진 것은 아니다** — 칠판을 깨끗이 지우는 데는 여전히 실패했지만,
**사람 얼굴이 나오는 빈도는 크게 줄었고** `chalkboard` 태그를 뺀 뒤에도 배경에 얼굴이 붙는 현상이 사라졌다.

**댓글이 더한 대책들**

| 상황 | |
|---|---|
| 뒤에 나오는 얼굴이 **작다** | 네거티브에 `chibi` , `deformed` |
| **고해상도에서 얼굴이 두 개** | 네거티브에 `water effect` |
| 배경 자체를 단순화 | `simple background` |
| 조합 | 긍정 `1girl, solo, simple background, blurry background, depth of field` + 네거티브 `people` |

### ⚠ 진짜 원인 — 작가 한 명이 아니라 '조합' 이다

> 작가를 **한 명씩 넣었다 빼고, 순서를 바꾸고, 가중치를 없애 봐도**
> **3~4명 이상을 삭제하지 않으면 얼굴 제거에 실패했다.**
> 즉 **특정 작가 한 명의 문제가 아니라 조합이 만들어 내는 문제다.**

문제를 일으킨 실제 작가 조합도 댓글에 공개돼 있다.

```
{{{{artist: wanke, artist: tokkyu, artist: ciloranko, artist: qiandaiyiyu}}}},
{artist: anmi, artist: freng, artist: mignon, artist: ningen_mame, artist: Mika Pikazo},
artist: shal.e, artist: kim eb
```

**부수 관찰** — `Euler A` 에서 이 현상이 발생할 확률이 조금 더 높다.

### 진단 요령 — 증상이 잘 나오는 조건을 일부러 유지하라

이 글이 남긴 방법론이 가장 값지다.

> 작성자는 문제를 부르는 `chalkboard` 태그를 **일부러 유지한 채** 하나씩 바꿔 가며 테스트했다.
> **증상이 잘 나오는 조건을 만들어 놓고 고쳐야 확인이 빠르기 때문이다.**

증상이 가끔 나오는 상태에서 이것저것 바꾸면 나아졌는지 아닌지를 알 수 없다. **변인 통제가 먼저다.**

**한 글에서만 검증된 처방이다** (2025-03, 추천 5). 다만 실패 기록과 댓글 확인이 함께 붙어 있어 재현 가능성이 높다.

→ [프롬프트 쓰는 법](prompting.md) · [모델 고르기](models.md)

<small>근거 — [어제 있었던 개같은 얼굴 복제 현상 해결 후기 25.03](https://arca.live/b/aiart/131650885)</small>

## 학습 도구를 깔았더니 생성이 CPU 로 넘어간다 — CUDA 전역 변수 충돌
<small>2026-07 기준 · 근거 1건</small>

**증상이 특이해서 표에 한 줄로 넣으면 못 알아본다.** 원인 설명이 있어야 응용이 되는 사례다 (176818115, 2026-07).

### 증상

kohya GUI(LoRA 학습기)를 깐 뒤부터, **ComfyUI 가 한 장씩 뽑을 때는 멀쩡한데
생성 큐를 좀 쌓으면(예: 20개 연속) GPU 연산을 멈추고 CPU 로 넘어가 버린다.**

> **"한 장씩 뽑을 때는 멀쩡한데 큐를 몰아 넣으면 먹통이 된다"** 는 것이 이 문제의 지문이다.

### 해결

```
--disable-cuda-malloc
```

ComfyUI 실행 옵션에 추가한다. 윈도우 포터블이면 `run_nvidia_gpu.bat` 안의 `python main.py` 뒤에 붙이면 된다.

### 왜 그런가 — 알아 두면 다른 데도 쓴다

| | |
|---|---|
| 1 | **kohya GUI 를 자동 설치하면 최신 CUDA(13.2)가 함께 깔린다** |
| 2 | 설치기가 **윈도우 전역 환경 변수 `PATH` 와 `CUDA_PATH` 를 CUDA 13.2 로 덮어쓴다** |
| 3 | ComfyUI 내장 PyTorch 는 **`2.10.0+cu128`** 이라, 내장 cu128 DLL 과 시스템의 cu132 DLL 사이에 **경로 섀도잉(Path Shadowing)** 충돌이 생긴다 |
| 4 | ComfyUI 는 VRAM 할당에 **`cudaMallocAsync`** 를 쓰는데, 1회 생성일 때는 가비지 컬렉터가 간신히 정리하지만 **연속 큐로 메모리를 빠르게 쪼개고 합치면 반환 지연과 단편화가 누적되어 GPU 가 병목에 걸린다** |
| → | `--disable-cuda-malloc` 은 **이 비동기 할당기를 꺼서 기본 할당 방식으로 되돌리는** 옵션이다 |

### 일반화

> **학습 도구와 생성 도구를 같은 PC 에 깔 때는 CUDA 전역 환경 변수 충돌을 항상 의심해야 한다.**

같은 계열의 사고가 이미 여럿 기록돼 있다 — ComfyUI Manager 가 커스텀 노드 의존성을 설치하며
**sageattention 을 다른 버전으로 갈아치우는 것**(→ [ComfyUI 쓰는 법](comfyui.md)),
라데온에서 **커스텀 노드를 깔다 ROCm 용 torch 가 날아가는 것**(→ [설치와 환경 구성](install.md)).
**"내가 건드리지 않은 것이 바뀌어 있다" 가 이 부류의 공통 지문이다.**

**한 글에서만 제시된 진단이다** (2026-07, 추천 2). 다만 원인 분석이 구체적이고 처방이 실행 인자 한 줄이라 시도 비용이 낮다.

→ [설치와 환경 구성](install.md) · [로라 쓰는 법](lora-usage.md) · [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [정보탭의 kohya gui 설치후 발생한 문제해결 26.07](https://arca.live/b/aiart/176818115)</small>

## NAI 노이즈(사각형 · 세로줄 · 도화지 질감) — `3::a, b, c::` 가중치 묶기가 범인이다
<small>⚠️ 2025-07 기준 · 근거 1건</small>

**증상 세 가지가 전부 같은 원인이다** (2025-07, NAI V4 실험 글).

| 증상 | 어디에서 |
|---|---|
| 배경에 **사각형 노이즈** | |
| 신체 부위에 **세로줄 노이즈** | |
| **도화지에 그린 듯한 유화·수채화 질감** | 캐릭터 프롬프트에 몰아 줬을 때 |
| 뒤틀리고 열화된 느낌 | 베이스 프롬프트에 몰아 줬을 때 |

> **원인은 여러 태그를 하나의 가중치 블록에 묶어서 넣는 것이다.**

```text
잘못  :  3::sitting, knee up, feet::
맞음  :  3::sitting::, 3::knee up::, 3::feet::
```

**태그마다 따로 가중치를 주면 사라진다.** 네거티브와 캐릭터 네거티브에서도 같은 현상이 난다.

### 임계값 — 가중치와 개수가 함께 작용한다

| 가중치 | 한 블록에 묶을 수 있는 항목 수 |
|---|---|
| **`2`** | **100개까지 대부분 멀쩡**, 130개쯤부터 문제 |
| **`3`** | **적게는 4개, 많아야 10개부터 깨진다** |
| `4.5` | 더 심하다 |

반대로 `3::x1::, 3::x2::, ... 3::x100::` 처럼 **가중치 3 을 100개 태그에 개별로** 주는 것은 거의 문제가 없었다
(확대하면 하늘에 아주 약한 노이즈만). `2::{{{tag, tag}}}, tag::` 처럼 **중괄호와 섞은 형태도 문제**가 생긴다.

```text
가중치를 항상 2 이하로만 쓴다        →  신경 쓸 필요 없다
2.3 이상을 자주 쓰는데 노이즈가 낀다  →  가중치를 태그마다 분할한다
```

### ⚠️ 로컬도 똑같다. 그리고 4.5 는 더 심하다

- 이 문제는 **NAI 만이 아니라 로컬에서도 동일하게 발생한다** *(댓글)*
- **NAI 4.5 는 오히려 더 심하다** — 4.5 부터 가중치를 `7`, `10` 처럼 높게 주기 시작해서다 *(댓글)*

### 공식 문법과 어긋나는 것 아닌가 — 아니다

NovelAI 공식 문법 설명은 `1girl, 1.5::rain, night ::, 0.5::coat ::` 처럼 **묶어 쓰는 것을 정식으로 제시**한다.
이걸 근거로 혼란을 표한 댓글이 있었는데, 이어진 답이 정확하다.

> **공식 예시에는 가중치 `3` 을 넘는 경우가 없다.**

즉 **묶어 쓰는 문법 자체가 틀린 것이 아니라, 높은 가중치와 묶기가 겹칠 때 깨지는 것**이다.
문법 자체는 [NovelAI](nai.md) 와 [프롬프트 쓰는 법](prompting.md) 의 가중치 절을 보라.

> 이 노이즈를 없애려고 `scan artifacts` 를 음수 가중치로 넣고 있었다며 **원인을 잘못 짚고 있었음을 인정한 댓글**이 있고,
> 가중치를 나눠 주니 퀄리티가 확 올랐다는 후기도 있다.


<small>근거 — [NAI) 이런 노이즈는 「 3::???, ???:: 」 가중… 25.07](https://arca.live/b/aiart/143845479)</small>

## 검열(모자이크 · 김딱지)이 안 풀린다 — 순서와 진짜 범인
<small>2025-12 기준 · 근거 1건</small>

뽑은 그림에 자꾸 검열(모자이크·김딱지)이 끼거나 뭔가로 가려질 때의 순서다 (2025-12).

```text
1. 모델 자체의 검열 · 프롬프트 · 출력 비율에 찐빠가 날 요소가 없는지 본다
2. 긍정 프롬프트에  uncensored,   ← 대체로 여기서 해결된다
3. 등급(rating) 태그를 필요에 맞게 넣는다
4. 네거티브에  mosaic censoring
5. 그래도 안 되면 포즈 LoRA · 컨트롤넷 · 편집 모델
```

### 등급 태그는 `rating:` 을 붙이는 편이 좋다

`general, sensitive, nsfw, explicit` 는 **일반 태그가 아니라서** `artist:` 와 같은 방식으로 접두사를 붙이는 게 좋을 수 있다 *(댓글)*.

```text
rating:general    rating:sensitive    rating:nsfw    rating:explicit
```

> 다만 경험상 퀄리티에 큰 차이는 없다고 같은 댓글이 덧붙였다. 등급 태그가 필수가 아니라는 점은 [NovelAI](nai.md) 의 `rating:` 항목에도 있다.

### ⚠️ `uncensored` 를 넣어도 안 풀린다면 — 진짜 범인은 작가 태그다

댓글이 본문보다 더 중요한 해법을 준다.

> **`uncensored` 를 넣어도 계속 김딱지가 붙거나 막대 모양 얼룩이 생긴다면 그건 작가(artist) 태그 문제다.**
> 단부루에서 그 작가 태그를 `uncensored` 와 함께 검색했을 때 **남는 그림이 거의 없다면**
> 그 작가는 원래 검열된 그림만 그린다는 뜻이므로 **빼거나 비중을 낮춰야 한다.**

```text
danbooru 에서 검색 :   <작가 태그>  uncensored
결과가 거의 없다     →  그 작가를 빼거나 가중치를 낮춘다
```

**이 판별법이 이 절의 핵심이다.** 프롬프트를 아무리 만져도 안 되던 것이 작가 하나 빼면 풀린다.
작가 태그가 결과를 지배하는 다른 사례는 [프롬프트 쓰는 법](prompting.md) 의 "작가 태그를 어떤 순서로 늘어놓나" 절과
아래 "배경에 얼굴이 덕지덕지 복제된다" 절에 있다.

> 수증기로 가리거나 포즈로 가리는 등 특수한 검열이 계속되면, 단부루가 명시하는 **검열 태그 그룹**을 참고해
> 적절히 긍정 또는 부정 프롬프트에 넣는다.
> 마음에 드는 결과가 나오면 EXIF 나 와일드카드 형식으로 쟁여 두라는 것이 본문 말미의 조언이다.


<small>근거 — [ComfyUI - 검열이나 가리는게 있다면 사용하는 단부루 … 25.12](https://arca.live/b/aiart/158273723)</small>

## 로라가 목록에 안 뜬다 — 체크포인트가 SDXL 이 아니다
<small>⚠️ 2025-05 기준 · 근거 1건</small>

**LoRA 폴더에 분명히 넣었는데 WebUI 의 로라 목록에 안 뜬다** — 입문자가 자주 막히는 곳이고 답은 파일이 아니라 체크포인트에 있다.

> **현재 로드된 체크포인트가 SDXL 계열이 아니어서다.**
> **WebUI 는 로드된 체크포인트와 아키텍처가 다른 LoRA 를 목록에서 숨긴다.**

```text
증상  :  SDXL(Illustrious·NoobAI) 로라를 넣었는데 목록에 없다
확인  :  지금 로드된 체크포인트가 SDXL 계열인가?
해결  :  체크포인트를 SDXL 계열로 바꾼다  →  바로 나타난다
```

실제로 질문자가 **체크포인트만 SDXL 로 바꾸니 LoRA 가 떴다**고 확인했다 (2025-05, 조회 22만 로라 배포글 댓글).
파일이 깨진 것도 폴더가 틀린 것도 아니니 **파일부터 뒤지지 마라.**

> 계열이 다른 로라를 **강제로 물렸을 때** 나는 오류는 따로 있다 —
> `RuntimeError: mat1 and mat2 shapes cannot be multiplied` 는 로라 파일이 망가진 것이 아니라 계열 불일치다(위 표 참조).
> **목록에 안 뜨는 것**과 **물렸는데 터지는 것**은 같은 원인의 두 얼굴이다. → [로라 쓰는 법](lora-usage.md)

### 곁들여 — 같은 글이 준 해상도 실전값

로라 배포자가 댓글에서 밝힌 실사용 해상도다. **특별한 이유가 있는 값은 아니고 SDXL 규격에 맞으면 자유롭게 쓰면 된다**는 것이 본인 답이다.

| 용도 | 값 |
|---|---|
| 기본 | **`1024x1344`** |
| 사양이 낮으면 | **`832x1216`** |
| 정사각형 | **`1024x1024`** |

> **결과가 예시와 다르다**는 질문에는 체크포인트를 illustriousXL 원본이 아니라 **`wainsfw140v` 로 바꾸고
> 그 모델 배포처에 적힌 세팅을 그대로 쓰라**고 답했다. 로라 배포글의 예시는 대개 특정 체크포인트에서 뽑은 것이다.


<small>근거 — [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜… 25.05](https://arca.live/b/aiart/137508828)</small>

## 원인을 가리는 절차 — 워크플로 → 프롬프트 → 모델 순으로 변인을 뺀다
<small>2026-07 기준 · 근거 4건</small>

"이게 워크플로 탓인가 프롬프트 탓인가 모델 탓인가" 를 가리지 못해 며칠을 태우는 것이 입문자의 가장 흔한 시간 낭비다.
채널에 그 절차를 그대로 밟은 기록이 있다 (176433146, 2026-07). **결론보다 절차가 재사용 가치가 있다.**

| 순서 | 무엇을 뺀다 | 그래도 재현되면 |
|---|---|---|
| **1** | **워크플로** — ComfyUI 를 아예 새로 설치하고 **남이 배포한 다른 워크플로**로 같은 것을 돌려 본다 | 워크플로 탓이 아니다 |
| **2** | **프롬프트** — 네거티브와 퀄리티 태그를 **전부 빼고 메인 프롬프트만** 남긴다 | 프롬프트 탓이 아니다 |
| **3** | 여기까지 왔으면 **베이스 모델 특성**이다 | 프롬프트·설정으로는 해결되지 않는다. **다른 모델로 가거나 인페인트로 우회**한다 |

실제 사례에서는 3단계까지 가서 "ANIMA 가 원래 그렇게 그린다" 는 결론이 나왔고, 그 뒤로는 **착의나 인페인트로 우회**하는 쪽으로 방향을 틀었다.

### 비슷한 절차가 통한 다른 사례

| 문제 | 어떤 변인을 뺐나 | 답 |
|---|---|---|
| 어느 날부터 선이 지저분해짐 | 프롬프트·모델을 그대로 뒀는데 재현 → **설정이 바뀐 것** | UNET weight dtype 이 `fp8_e4m3fn` → 위 '결과물이 이상할 때' |
| WAI 에서 그림체가 무너짐 | 태그를 하나씩 빼며 **방아쇠 태그**를 찾음 | 학습이 얕은 태그의 높은 가중치 → 위 '결과물이 이상할 때' |
| 영상이 3D 로 나옴 | 파일 출처를 의심했으나 **파일명을 확인**하니 `t2vHigh` | i2v 자리에 t2v 모델 → [비디오 생성](video-generation.md) |

> **요령 하나** — 변인을 뺄 때는 **한 번에 하나씩** 뺀다. 새 설치 + 새 워크플로 + 새 프롬프트를 동시에 바꾸면 뭐가 고쳤는지 알 수 없어 같은 문제를 또 만난다.

→ 위 '0. 오류 메시지 읽는 법' · [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [선 지저분하게 나오는 문제 해결! 26.07](https://arca.live/b/aiart/178281311) · [WAI로 그림 뽑다 보면 종종 마주치는 문제 26.06](https://arca.live/b/aiart/173511292) · [comfy에서 anima로 돌리는데 계속 crotch 쪽 찐… 26.07](https://arca.live/b/aiart/176433146) · [페?)왜 갑자기 3D로 넘어가는 것일까요 26.06](https://arca.live/b/aiart/172447183)</small>

## H3 에서 최적화가 통째로 안 먹을 때 — 세팅이 아니라 ComfyUI 를 의심한다
<small>2026-08 기준 · 근거 1건</small>

MiniMax H3 를 돌리는데 **torch compile · SageAttention 같은 최적화가 하나도 먹지 않고 생성이 계속 실패**한다면,
세팅을 붙잡고 있기보다 **ComfyUI 를 완전히 밀고 다시 까는 편이 빠를 수 있다** (179172801, 2026-08).

> 전날까지 최적화가 전혀 먹지 않아 계속 실패하던 사람이 **ComfyUI 를 새로 설치했더니 최적화가 전부 먹기 시작했다.**
> **원인은 LTX·WAN 등 여러 모델을 쓰면서 커스텀 노드가 꼬인 것**으로 추정된다.
> 댓글에서도 *"minimax 를 써 보니 노드가 꼬이는 것이 보여 전부 밀고 재설치 중"* 이라는 동일 사례가 나왔다.

**재설치 후 실측** — 아래는 **전날에는 전부 실패하던 조건**들이다(GPU 미기재).

| 조건 | 시간 |
|---|---|
| 1.2MP · 5초 | 4분 |
| 0.7MP · 5초 | 2분 |
| 0.6MP · 9초 | 5분 |

### 밀기 전에 확인할 것

전부 미는 것은 마지막 수단이다. 그 전에 아래 순서를 밟는다.

1. **`sage-attention` 을 먼저 끄고 돌려 본다** — 뉴비 오류의 범인 1위다 (위 'sage-attention' 절)
2. **고속화 노드끼리 겹치지 않는지** 본다 — 터보 LoRA + EasyCache 처럼 **둘 다 스텝을 줄이는 것**은 같이 쓰면 안 된다
3. **H3 Cache 노드**는 ComfyUI 업데이트 이후 **노드의 존재 자체가 샘플러 구동을 막는** 사례가 보고됐다 → 지워 본다
4. `--disable-dynamic-vram` · `--lowvram` · `--highvram` · `--gpu-only` **를 쓰고 있지 않은지** 본다 (H3 에서는 쓰지 않는다)

**여러 영상 모델을 번갈아 쓰는 환경이라면 버전별 인스턴스를 나눠 두는 편이 근본 처방이다**
→ [ComfyUI 쓰는 법](comfyui.md) 의 '버전별 인스턴스로 나눠 쓰기' 절 · [비디오 생성](video-generation.md)

<small>근거 — [와 comfyui 다시 깔고 H3 돌리니깐 최적화 전부 먹히… 26.08](https://arca.live/b/aiart/179172801)</small>

## 재현이 안 될 때는 파일명이 아니라 해시로 대조한다 — 'ComfyUI vs WebUI 차이' 가 아니었다
<small>2026-05 기준 · 근거 1건</small>

**"같은 모델·같은 세팅인데 내 ComfyUI 결과물만 외곽선이 흐리고 색감이 이상하다" 는 질문의 답이 나온 사례다** (2026-05).

질문자는 WebUI 로 뽑힌 남의 이미지 EXIF 를 그대로 따라갔다.

```
DPM++ 2M / Karras / 30 steps / CFG 7 / 1024x1360 / Clip skip 2
체크포인트 rinAnim8drawIllustrious_v40B
네거티브·퀄리티 프롬프트·퀄리티 로라(NOOB_vp1_detailer_by_volnovik_v1:0.3) 까지 동일
```

캐릭터 로라 가중치를 1.0 → 0.6 까지 바꿔 봐도 마찬가지였다. **원인은 VAE 였다.**

> 한 댓글이 *"색이 깨지는 것까지 보면 VAE 문제로 보인다. **파일 이름은 얼마든지 바꿀 수 있으니 이름만 같고 실제로는 다른 파일 아니냐**"* 고 짚었고,
> 실제로 **원본 EXIF 의 VAE hash `235745af8d`(`sdxl.vae.safetensors`) 와 질문자가 쓰던 파일의 해시가 아예 달랐다.** 교체하니 크게 해결됐다.

### 교훈 — 재현할 때는 파일명이 아니라 해시로 대조한다

| | |
|---|---|
| 대조 기준 | **모델·VAE 는 파일 이름이 아니라 hash 로 맞춘다.** 같은 이름의 다른 파일이 흔하다 |
| 오해 주의 | **ComfyUI 와 WebUI 의 차이만으로 이 정도 색감·외곽선 차이는 나지 않는다.** "툴이 달라서" 로 넘기면 원인을 못 찾는다 |
| 곁들여 확인 | 노드 연결이 끊긴 곳이 없는지, 외곽선만 문제라면 디테일러(인페인트)로 얼굴 외곽선만 다시 그리는 우회도 있다 |

VAE 가 좌우하는 것은 **색감과 선명도**이고 그림체가 아니라는 것은 이 문서의 'VAE 를 둘러싼 오해 둘' 항목에 있다.

→ [ComfyUI 쓰는 법](comfyui.md) · [업스케일과 화질](upscale.md)

<small>근거 — [외곽선이 명확하게 그려지지 않는 이유 26.05](https://arca.live/b/aiart/171512796)</small>

## 노드가 커스텀에서 내장으로 바뀌었을 때 — 값을 고치지 말고 노드를 새로 불러온다
<small>2026-07 기준 · 근거 1건</small>

ComfyUI 업데이트 뒤 **잘 쓰던 워크플로우가 갑자기 죽는** 유형 중, 원인이 '내 설정' 이 아니라 **노드의 소속이 바뀐 것**인 경우다 (2026-07).

```
Required input is missing: model_patch
```

| | |
|---|---|
| 원인 | **`Apply Anima ControlNet-LLLite` 가 커스텀 노드에서 ComfyUI 내장 노드로 바뀌면서 `model_patch` 입력이 새로 생겼다.** 예전 워크플로우에는 그 입력이 아예 없다 |
| 1차 조치 | LLLite 컨트롤넷 파일들을 **`ComfyUI/models/model_patches/`** 로 옮기고, `model_patch` 입력에 **'모델 패치 로더(model patch loader)'** 노드를 연결한다 |

### ⚠ 여기서 한 번 더 걸린다 — 값을 고치지 마라

파일을 옮겨 연결했더니 이번엔 노드의 **strength 값 자리에 파일명(`anima-lllite-inpainting-v2.safetensors`)이 들어간 채 NaN** 으로 표시되고 이 오류가 났다.

```
Failed to convert an input value to a FLOAT value
```

임의로 `1.0` 같은 숫자를 넣으면 **에러는 사라지지만 결과가 어색하거나 레퍼런스와 무관한 이미지**가 나온다.

> **진짜 해결은 값을 고치는 것이 아니라 `Apply Anima ControlNet-LLLite` 노드를 삭제하고 새로 불러와 다시 연결하는 것이다.**
> 구버전 워크플로우에 남아 있던 **위젯 배치가 새 노드 정의와 어긋나 값이 한 칸씩 밀려 들어간 것**이기 때문이다. 질문자가 그렇게 해서 해결을 확인했다.

**일반화** — 커스텀 노드가 본체에 편입되면 입력 개수·순서가 바뀐다. 그때 나오는 `Required input is missing: ...` 과 밀린 위젯 값은
**노드를 지우고 새로 꺼내 연결하는 것이 정석**이고, 값을 손으로 맞추는 것은 증상만 가린다.

→ [컨트롤넷](controlnet.md) · [ANIMA](anima.md)

<small>근거 — [comfyui inpaint turbo 워크플로우 관련 질문 26.07](https://arca.live/b/aiart/177370189)</small>

## SAM3 커스텀 노드 되살리기 — 커밋 고정 + requirements 두 줄 삭제 + model.py 패치
<small>2026-03 기준 · 근거 2건</small>

SAM3 는 **ComfyUI 본체 버전과 커스텀 노드 커밋이 어긋나면서** 채널에서 가장 자주 깨진 노드다.
2026-03, ComfyUI **v0.18.2** 기준으로 정리된 완전 복구 절차다.

**증상은 두 단계로 나타난다.**

| | |
|---|---|
| 1 | 최신 SAM3 를 쓰면 모델 로드 자체가 안 되고 `'NoneType' object has no attribute 'data'` 류 오류 |
| 2 | 깃헙 이슈의 수정 코드를 넣으면 로드는 되지만 **이번엔 마스크가 깨져서 나온다** |

**그래서 해법이 '노드는 되돌리고 `model.py` 만 최신 + 패치' 라는 조합이 된다.**

```bash
# 1) custom_nodes 에서
git clone https://github.com/PozzettiAndrea/ComfyUI-SAM3
cd ComfyUI-SAM3
# 2) 2026-02-21 커밋으로 고정
git checkout -b sam3-fixed 607a21da2ec5ae7916d8e3cbbb80854ee0044992
```

**3) `requirements.txt` 에서 두 줄을 지운다** — `comfy-env==0.2.0` 과 `comfy-attn`.
⚠ 그 아래 `comfy-3d-viewers==0.2.27` 은 **남긴다**(댓글 확인).

```bash
# 4) 포터블 임베디드 파이썬으로 설치
..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
```

**5)** `https://github.com/PozzettiAndrea/ComfyUI-SAM3/blob/main/nodes/sam3/model.py` 에서 **최신 `model.py`** 를 받는다(구버전은 에러가 남는다).
**6)** 받은 파일에 **이슈 [#106](https://github.com/PozzettiAndrea/ComfyUI-SAM3/issues/106)** 의 패치를 넣는다 —
`if box_refine:` 블록에서 `last_layer = self.bbox_embed.layers[-1]` 을 잡아 **weight/bias 가 None 이 아닐 때만** `nn.init.constant_(...)` 를 하도록 감싸고,
`self.reference_points = operations.Embedding(num_queries, 4, dtype=dtype, device=device)` 와 instance_query 일 때의 `self.instance_reference_points` 를 둔다. **들여쓰기 위치가 중요하다.**
**7)** 수정한 `model.py` 를 `custom_nodes/comfyui-sam3/nodes/sam3` 에 덮어쓴다(원본은 백업).

> 파이썬을 몰라도 되는 지름길 — 이슈 #106 을 이미 반영한 `model.py` 를 통째로 공유한 글이 있다(구글 드라이브 개인 공유라 만료될 수 있고, 죽었으면 이슈를 보고 직접 패치한다).
> 모델 파일 경로는 `ComfyUI/models/sam3/sam3.safetensors` 다.

### ⚠ 이 절차와 무관한 별개 오류

```
safetensors_rust.SafetensorError: Error while deserializing header: InvalidHeaderDeserialization
```

**댓글에서 갈라져 나온 다른 문제다.** 절차를 아무리 정확히 밟아도 이건 안 고쳐진다 — **받아진 모델 파일이 깨졌거나 다운로드가 막힌 것**이다.
`https://huggingface.co/AEmotionStudio/sam3/blob/main/sam3.safetensors` 를 직접 받아 `ComfyUI/models/sam3` 에 넣어 보고,
그래도 안 되면 ComfyUI 설치 자체가 문제일 수 있다 — 실제로 그 사용자는 **ComfyUI 를 통째로 지우고 재설치한 뒤 본문 절차대로 해서 해결**됐다.

→ [디테일러](detailer.md) · [ComfyUI 쓰는 법](comfyui.md)

<small>근거 — [SAM3 해결했다.. 26.03](https://arca.live/b/aiart/166035589) · [SAM3 디테일러 커스텀 노드가 작동되게 수정한 파일이야. 26.03](https://arca.live/b/aiart/164808456)</small>

## ANIMA 계열에서 새로 나온 오류 둘 — PiD 로더와 fp16 검은 화면 (2026 중반)
<small>2026-07 기준 · 근거 2건 · 자료 엇갈림</small>

### `AnimaPiDLoader` 가 `_pickle.UnpicklingError` 로 죽는다 *(2026-06-14)*

```text
Node ID        58
Node Type      AnimaPiDLoader
Exception      _pickle.UnpicklingError: invalid load key, \xc7
```

| | |
|---|---|
| ❌ 효과 없었던 것 | **`comfyui-unsafe-torch` 커스텀 노드 설치.** 비슷한 UnpicklingError 에 쓰인다는 말을 듣고 설치 후 재부팅까지 했지만 소용없었다 |
| ✅ **원인과 해결** | **`ckpt_name` 에 따로 다운로드한 PiD 모델 파일을 직접 지정하면 안 된다. 그냥 `autodownload` 로 두면** 노드가 알아서 필요한 모델을 받아 실행한다. 잘못된(혹은 형식이 다른) 파일을 pickle 로 읽으려다 난 오류였다 |

PiD 는 ANIMA 계열 워크플로우에서 쓰이는 보조 모델 로더다.
**문제가 있을 때는 PiD 부분만 건너뛴 워크플로우로 돌려 원인을 좁힐 수 있다.** → [업스케일과 화질](upscale.md)

### ComfyUI 업데이트 후 SDXL 생성이 검은 화면 (fp16) *(2026-07-29)*

> **ComfyUI 를 업데이트한 뒤 SDXL 관련으로 뽑으면 검은 화면이 나온다. fp16 에서 주로 보이는 현상**이고,
> 이 때문에 **IP-Adapter 를 못 쓰고 있다**는 보고다.

> ⚠️ **[ANIMA](anima.md) 의 '가중치 4 이상에서 검은 화면' 과 원인이 다른 별개 현상이다.**
> 이쪽은 가중치와 무관한 **ComfyUI 버전 + fp16 조합** 문제이므로 섞어서 진단하면 안 된다.
> 가중치를 낮췄는데도 검은 화면이면 이쪽을 의심한다.

같은 글의 곁가지 실측 — 포터블 ComfyUI 를 **fp16 → bf16** 으로 바꾸자 장당 20초 이하로 나오던 것이
**30초 이상으로 느려졌다.** 구도·자세가 색다르게 나오는 느낌이라는 체감은 글쓴이 스스로 *"해골물인가 싶기도 하다"* 고 덧붙였다.
그리고 **NAI 용 로라를 ANIMA 에 쓰면 손가락 찐빠와 얼굴 돌출이 심해** 결국 안 쓰는 것과 큰 차이가 없다.

*검은 화면의 다른 원인들(sage-attention, shift 0, Tiled VAE, 시그마 그래프 시작값)은 이 문서의 다른 절과
[ComfyUI 쓰는 법](comfyui.md) · [ANIMA](anima.md) 에 흩어져 있다. **검은 화면은 원인이 여럿이므로 하나로 묶지 말 것.***

<small>근거 — [Anima로 NAI 느낌 짤털 26.07](https://arca.live/b/aiart/178404708) · [AnimaPiDLoader 오류 발생 26.06](https://arca.live/b/aiart/173758822)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 455개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 이 시리즈의 예시 이미지는 ComfyUI 로 뽑았으므로 이미지를 ComfyUI 캔버스에 끌어다 놓으면 노드(워크플로우)가 그대로 불러와진다 | 44 | 0 | 2025-04~2026-07 |
| 배포글에 적힌 'LoRA Base Model' 은 그 로라를 만들 때 쓴 학습용 베이스 모델일 뿐이고, 그림을 실제로 뽑는 것은 별도의 'Checkpoint Model' 이다 — 제작자가 뉴비 혼동을 막으려고 본문에 못 박아 둔 문구다 | 31 | 0 | 2025-02~2026-07 |
| 같은 제작자의 웹툰·애니 캐릭터 LoRA 배포 목록 (전부 LoRA Base illustriousXL_v1.1 / 체크포인트 WaiNSFWillustrious V140) — 퀘스트지상주의 6종 `baek chaerin, elisa, kim dahyeon, lee jihyeon, yang soha, yeon seohui` · 초인의 게임 6종 `higpr(대사제), baek hayeon, lee nayeon, qun1(여왕), saniya ahmetova, shuran` · 일진담당일진 5종 · 수요웹툰의 나강림 13종 · 사시미 한 자루로 아카데미를 씹어먹음 6종 · 전지적 독자 시점 14종 · 현실퀘스트 7종 `choi minhye` 외 · 이세계 밀프 헌터 10종 · 광마회귀 공손월 · 동아리 11종. 짝 글 관계 — 전독시 https://arca.live/b/aiart/139326347 ↔ https://arca.live/b/aiart/139333927 , 밀프헌터 https://arca.live/b/aiart/140473932 ↔ https://arca.live/b/aiart/140480040 | 26 | 0 | 2025-05~2025-12 |
| 채널의 웹툰·애니 캐릭터 LoRA 배포 시리즈는 동봉된 Metadata(json) 파일의 파일명을 LoRA(.safetensors) 파일명과 똑같이 맞춰 같은 폴더에 넣으면 WebUI 에서 트리거워드·프롬프트가 자동으로 뜬다. 이 json 은 ComfyUI 전용이 아니라 WebUI(Stable Diffusion) 사용자도 로라 폴더에 같이 넣으면 된다 | 25 | 0 | 2025-04~2025-08 |
| 워크플로우는 EXIF 가 든 이미지·영상 파일을 다운로드해 ComfyUI 창에 드래그앤드롭해 불러온다 | 11 | 0 | 2024-06~2026-08 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| ANIMA 는 Euler A + automatic/normal 조합에서 그림이 기괴해지므로 Euler 또는 ER SDE 샘플러에 simple 또는 SGM uniform 스케줄러를 써야 한다 | 7 | 0 | 2026-04~2026-08 |
| 포니 계열에서 유래한 스코어 태그는 score_9 부터 score_1 까지 아홉 단계이며, 긍정에 score_9/score_8/score_7 중 1~3개를, 네거티브에 score_1/score_2/score_3 을 넣는 것이 관례다 | 6 | 0 | 2026-02~2026-06 |
| 긴 영상은 통짜로 만들면 타이밍과 두 번째 상황을 제대로 못 그리므로, 프롬프트를 나눠 이어붙이는 편이 낫다 | 6 | 0 | 2026-02~2026-08 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| 이 웹툰 캐릭터 LoRA 시리즈의 다운로드처는 '키오스크(kio.ac)' 서버 장애로 civitai 로 옮겨졌고, 이후 일부 제작자는 civitai 서버·정책에 회의를 느껴 아카라이브로 다시 옮겼다 — 링크가 죽었으면 civitai 에서 작품명으로 검색하는 편이 빠르다(https://civitai.com/search/models?query=작품명) | 6 | 0 | 2025-05~2025-06 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| ANIMA 의 공식 지원 해상도는 512x512(NAI1) ~ 1024x1024(SDXL) ~ 1536x1536(ILXL1) 버킷이고, 공식·입문 자료는 SDXL 해상도(1024급, 세로 832x1216)를 무난한 기본값으로 권한다 | 5 | 0 | 2026-01~2026-05 |
| 배포 워크플로우의 v-pred 스위치는 v-pred 모델이 아니면 반드시 꺼야 한다 — Eps 모델에 v-pred 를 켜 두면 정상 동작하지 않고, 결과가 흐리멍텅하면 V-PRED 모델이 맞는지부터 확인해 아니면 그 그룹을 바이패스한다 | 5 | 0 | 2025-06~2025-08 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| WAN 2.2 계열 워크플로우는 High/Low 모델을 나눠 쓰고 lightx2v(라이트닝) 로라를 별도로 물리는 것이 표준 구성이다 | 5 | 0 | 2026-01~2026-04 |
| MiniMax H3 프롬프트는 [Shot 1] 에 타임스탬프를 붙이지 않고 이후 샷만 'At 00:SS.mmm' 형식으로 시간이 증가하게 적으며 기본 길이는 10.00초다 | 5 | 0 | 2026-08~2026-08 |
| `MemoryError`, `you tried to allocate xxxx bytes`, `OSError: [WinError 1455] 이 작업을 완료하기 위한 페이징 파일이 너무 작습니다` 는 가상 메모리(페이징 파일)를 늘려 대처한다 | 5 | 0 | 2022-12~2023-02 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |
| 2023-02 SD1.5 병합 대회 배포글들은 U-Net 블록 단위 병합을 썼다 — 25개 블록 각각에 소수 가중치를 주거나(multicolor.v2) 0/1 만 주어 특정 층을 통째로 한쪽 모델에서 가져오거나(Unico Bergamotto: `1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1` / Base alpha 0), LoRA 를 SuperMerger 로 뒤쪽 블록에만 얹는(Sita7taker: `헬테이커:0.1:(0,…,0,1,1,1,1,1)`) 방식이다. 지금 기준으로는 낡았고 시대 확인용이다 | 5 | 0 | 2023-02~2023-02 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| 채널의 2023년 로라 학습글 다수가 작성자 스스로 철회했거나 낡음 단서를 붙였다 — 71341748 은 '오래된 글이니 읽지 말고 최신 정보를 찾으라', 69186437 은 '원글 68205055 을 따라가라', 68205055 는 2023-06-01 AS 중단, 84182288 은 2024-10-29 '참고용으로만 보라', 81325841 은 본문 블로그 링크 사망 | 5 | 0 | 2023-01~2023-08 |
| CFG 가 1 이면 네거티브 프롬프트가 사실상 작동하지 않으므로, 고속 로라·Hyper·Lightning 이 박혀 CFG 1 로 쓰는 모델에서는 네거티브를 쓸 의미가 없고 그만큼 품질도 다소 떨어진다 | 4 | 0 | 2025-06~2026-03 |
| 아카라이브에 그림을 올릴 때 그냥 드래그하거나 붙여넣으면 아카 쪽에서 메타데이터가 날아가므로, 글쓰기 편집기 위쪽의 이미지 버튼을 눌러 **'EXIF 저장'(EXIF 보존) 체크박스를 켜고 그 창에서 업로드**해야 프롬프트·워크플로우가 보존된다 — 이미 EXIF 없이 올렸고 글 수정이 막혔다면 원본을 압축해 catbox 등에 올려 댓글로 링크하거나 EXIF 를 체크해 다시 올린 별도 글을 링크한다 | 4 | 0 | 2024-08~2025-08 |
| 이미지 생성(ANIMA)에서는 dynamic vram 을 끄는 쪽이 빠르며, torch.compile 을 쓸 때는 --disable-dynamic-vram 이 사실상 필수다 | 4 | 0 | 2026-05~2026-08 |
| '체크포인트만 같으면 같은 그림이 나온다' 는 생각은 틀렸다 — WebUI 는 확장 프로그램·고해상도 보정(hires) 설정·모델 차이 때문에 예시와 다르게 나올 수 있고, 제작자가 ComfyUI 로 만든 예시는 WebUI 와 결과가 다르다. 업스케일 단계 설정까지 맞춰야 한다 | 4 | 0 | 2025-03~2025-06 |
| 설정 > Comfy > Nodes 2.0 > 모던 노드 디자인을 켜면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다 | 4 | 0 | 2026-05~2026-08 |
| ComfyUI-EasyUseAnima 는 릴리스보다 main 브랜치에 수정이 먼저 올라가므로 git 으로 설치해야 인풋 소켓 누락 같은 버그가 고쳐진 판을 받는다 | 4 | 0 | 2026-06~2026-07 |
| ComfyUI 포터블에서 파이썬 패키지를 깔 때는 시스템 파이썬이 아니라 `python_embeded\python.exe -m pip` 로 설치해야 한다 | 4 | 0 | 2026-01~2026-08 |
| MiniMax H3 터보 LoRA 는 H3-Cache 와 원리가 겹쳐 함께 쓰면 결과물이 망가지며, 품질은 Cache 쪽이 낫다 | 4 | 0 | 2026-08~2026-08 |
| `.ckpt` 와 `.safetensors` 는 담긴 내용이 같고 **safetensors 는 악성코드가 실행될 수 없는 더 안전한 컨테이너 형식일 뿐**이라 용량·성능과는 무관하다. 체크포인트 용량을 좌우하는 것은 **fp16 여부와 EMA 가중치 포함 여부**다 — 7GB 짜리는 EMA 약 3GB + fp32 가중치 약 4GB 구성이고, fp32→fp16 으로 바꾸면 4~5GB, 거기서 EMA 까지 떼면 2GB 가 된다(EMA 를 뗀 모델을 pruned 라 부른다). 그림 생성·병합·LoRA 사용에 EMA 는 필요 없다 | 4 | 0 | 2023-01~2023-03 |
| int8convrot 양자화는 fp8 tensorwise 보다 품질이 좋고(Q8_0 급) 조금 빠르며, 캘리브레이션이 필요 없어 대세가 된다 | 4 | 0 | 2026-07~2026-08 |
| 모델이 diffusion model 단독으로 배포되면 models/checkpoints 가 아니라 models/diffusion_models 에 넣고 Load Diffusion Model 계열 노드로 불러야 하며, 텍스트 인코더와 VAE 도 각각 models/text_encoders, models/vae 에 따로 넣어 연결해야 한다 | 4 | 0 | 2026-05~2026-08 |
| ANIMA 는 다국어를 지원하지 않아 프롬프트를 영어로 써야 하며, 한국어로 쓰려면 워크플로우에 번역 노드를 끼워 넣는다 | 4 | 0 | 2026-02~2026-08 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [(구)WEB UI설치가 어려운 사람을 위한 통합팩 [0.66.2v]](https://arca.live/b/aiart/60216616) — 2022-10, 추천 189
- [Lora 학습 실패로 자살하고 싶은 ㅈ밥 뉴비들만 이리와라](https://arca.live/b/aiart/69186437) — 2023-02, 추천 130
- [[가이드] 프롬대장경 제 1권 『설치부터 t2i까지』](https://arca.live/b/aiart/68917133) — 2023-02, 추천 106
- [AI그림 뉴비가 차근차근 설치하는 webui의 A부터Z까지!!!](https://arca.live/b/aiart/111903865) — 2024-07, 추천 71
- [DDSD GUI 대폭 개선 및 기능 변경](https://arca.live/b/aiart/74470925) — 2023-04, 추천 66
- [WAN2.2 I2I 일관성 통일 워크플로우](https://arca.live/b/aiart/160425811) — 2026-01, 추천 65
- [ComfyUI 뉴 원클릭 로컬 리터칭 V4A 워크플로우](https://arca.live/b/aiart/159742122) — 2026-01, 추천 59
- [DDSD 대 업데이트](https://arca.live/b/aiart/74205817) — 2023-04, 추천 58
- [Ultimate SNS generator 만들어서 공유해봄](https://arca.live/b/aiart/170679152) — 2026-05, 추천 57
- [Ie 아티스트 로라 v2 만듬 + 쓸만한 툴 로라 추천](https://arca.live/b/aiart/127368119) — 2025-01, 추천 56
- [kohya_ss 드림부스 기반 LoRA GUI 학습 사용법](https://arca.live/b/aiart/68205055) — 2023-01, 추천 53
- [nai 가이드 팁&자주 묻는 질문 (완)](https://arca.live/b/aiart/151423873) — 2025-10, 추천 51
- [딸깍충을 위한 완전 자동 AUTO-WAN (워크플로우) (+ 추가 내용)](https://arca.live/b/aiart/152101017) — 2025-10, 추천 51
- [ILXL) 말랑이 선생님의 랜덤 와일드카드 모음집 공유](https://arca.live/b/aiart/125265456) — 2025-01, 추천 46
- [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.2 워크플로우](https://arca.live/b/aiart/160657113) — 2026-01, 추천 46
- [NAIA를 처음 접하는 사람에게 - NAIA의 첫걸음 ~ 프롬프트 엔지니어링/자동화/프리셋을 활용해보자](https://arca.live/b/aiart/154179363) — 2025-11, 추천 45
- [Comfy ANIMA 정보글 모음](https://arca.live/b/aiart/175397651) — 2026-06, 추천 43
- [임베딩 하이퍼 모델 VAE yaml 구분 및 적용법](https://arca.live/b/aiart/66582124) — 2023-01, 추천 42
- [NAI) 이런 노이즈는 「 3::???, ???:: 」 가중치 문제](https://arca.live/b/aiart/143845479) — 2025-07, 추천 41
- [스압주의] 미맥H3 i2v NSFW프롬프트 팁 공유.](https://arca.live/b/aiart/179445963) — 2026-08, 추천 41
- [(구)원클릭 윈도우 실행기](https://arca.live/b/aiart/67307479) — 2023-01, 추천 40
- [완전히 같은 이미지를 만들 수 없다면? - 재현성 체크리스트](https://arca.live/b/aiart/70485768) — 2023-02, 추천 38
- [ComfyUI에서 이미지 누끼 따고, 그 안에 다른 이미지를 리사이징해서 합성하는 워크플로우 공유](https://arca.live/b/aiart/165751166) — 2026-03, 추천 38
- [Comfyui portable v0.31.0 + sage 외 여러가지.](https://arca.live/b/aiart/179342860) — 2026-08, 추천 38
- [흐릿, 흐리멍텅, 흐리게, 뿌옇게,해상도 ,뿌옅게 ,뿌해 ,채도,푸른멍,보라색,선명,피멍](https://arca.live/b/aiart/68904629) — 2023-02, 추천 37
- [NSFW 애니메이션 신모델 Anima](https://arca.live/b/aiart/161150715) — 2026-01, 추천 36
- [[가이드] 뉴비 자주 묻는 질문 (FAQ)](https://arca.live/b/aiart/68598675) — 2023-01, 추천 35
- [MiniMax H3 가속 노드 별 속도 후기](https://arca.live/b/aiart/179038650) — 2026-08, 추천 35
- [MiniMax H3 int8convrot Video VAE 올라옴](https://arca.live/b/aiart/179114541) — 2026-08, 추천 34
- [파워셀 설정해도 자꾸 꺼져서 서버 연결 문제 해결 못한 사람 보셈.](https://arca.live/b/aiart/69516260) — 2023-02, 추천 33
- [원하는 위치, 원하는 로라](https://arca.live/b/aiart/76318653) — 2023-05, 추천 33
- [Anima 초보자 자연어(한국어) 프롬프트 워크플로우](https://arca.live/b/aiart/171167219) — 2026-05, 추천 33
- [CUDA out of memory. 전용 메모리 가비지 컬랙팅](https://arca.live/b/aiart/70658672) — 2023-02, 추천 32
- [Comfyui portable v0.26.0 + sage 외 여러가지](https://arca.live/b/aiart/175163102) — 2026-06, 추천 32
- [Krea2 edit LoRA 간단 후기](https://arca.live/b/aiart/177257973) — 2026-07, 추천 32
- [WebUI 쓸때 메모리 유출문제 해결방법](https://arca.live/b/aiart/69230678) — 2023-02, 추천 31
- [UncannyValley V-pred v1 출시](https://arca.live/b/aiart/140017939) — 2025-06, 추천 29
- [베니스 결제 및 사용법이었는데 검열먹었다함](https://arca.live/b/aiart/172694842) — 2026-06, 추천 29
- [[병합대회] Sita7taker](https://arca.live/b/aiart/70499026) — 2023-02, 추천 28
- [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜송연우｜유은희](https://arca.live/b/aiart/137508828) — 2025-05, 추천 28
- [라면보다 쉽다! 간편 종합 워크플로우 v1.5](https://arca.live/b/aiart/143249780) — 2025-07, 추천 28
- [로컬의 희망 Smooth Mix Wan 2.2 모델 공유](https://arca.live/b/aiart/149889518) — 2025-10, 추천 28
- [뉴비 친화적 Smooth 워크플로우 개조판 (+업데이트)](https://arca.live/b/aiart/151277424) — 2025-10, 추천 28
- [커스텀노드) ComfyUI-LLM-Helper](https://arca.live/b/aiart/174631586) — 2026-06, 추천 28
- [webui 자동좌가 직접 만든 실행기](https://arca.live/b/aiart/68257234) — 2023-01, 추천 27
- [질문에 답변이 안달린다구? 답변 잘 받는 꿀팁 대공개 (6/16 수정)](https://arca.live/b/aiart/75960531) — 2023-05, 추천 26
- [Wan2.2 연속 영상 생성 + 병합 워크플로우 공유 (WebUI Style)](https://arca.live/b/aiart/146168826) — 2025-08, 추천 26
- [딸깍 AUTO-WAN+디테일러+사운드(MMAudio) 워크플로우](https://arca.live/b/aiart/153525536) — 2025-11, 추천 26
- [NAIA 및 아니마 사용을 위한 Webui Forge Neo 포지네오 설치 가이드 (수정)](https://arca.live/b/aiart/170554328) — 2026-05, 추천 26
- [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯](https://arca.live/b/aiart/178949797) — 2026-08, 추천 26
- [AI는 고차원 공간에 이미 존재하는 그림을 찾아내는 것일 뿐](https://arca.live/b/aiart/70488954) — 2023-02, 추천 25
- [ComfyUI 뉴비의 초간단 regional 분리 방법(영역분리, 영역지정, Regional Prompt)](https://arca.live/b/aiart/145827191) — 2025-08, 추천 25
- [(구)torch2.1.2 xformers0.0.23 원클릭자동설치파일 5000번대4000번대3000번대2000번대1000번대 최적화](https://arca.live/b/aiart/76553767) — 2023-05, 추천 24
- [ComfyUI 초보자를 위한 워크플로우 사용 가이드](https://arca.live/b/aiart/141704804) — 2025-07, 추천 24
- [SAM3 해결했다..](https://arca.live/b/aiart/166035589) — 2026-03, 추천 24
- [LTX 2.3 워크플로우 V2 공유 및 팁 정리](https://arca.live/b/aiart/172671768) — 2026-06, 추천 23
- [미니맥스 H3 R2V 오디오 레퍼런스 시연](https://arca.live/b/aiart/179459020) — 2026-08, 추천 23
- [WebUI 에러 모음](https://arca.live/b/aiart/65362592) — 2022-12, 추천 22
- [DDSD Postprocessing 업데이트](https://arca.live/b/aiart/74887800) — 2023-04, 추천 22
- [Wan2.2 FLF2V 간단 테스트](https://arca.live/b/aiart/145952453) — 2025-08, 추천 22
- [초보자용 LTX2.3 워크플로우](https://arca.live/b/aiart/172768105) — 2026-06, 추천 22
- [LTX 2.3 테스트중인 로라 하나 추천](https://arca.live/b/aiart/173213921) — 2026-06, 추천 22
- [미니맥스 H3 Edit 모델로 써 본 간단 후기](https://arca.live/b/aiart/178880588) — 2026-08, 추천 22
- [Wan2.2 노트북 4070 8g 짜리 돌리는 워크 공유](https://arca.live/b/aiart/145496771) — 2025-08, 추천 21
- [EasyUse Anima: ANIMA 프롬프트 보조 노드 베타테스트 버전](https://arca.live/b/aiart/174369324) — 2026-06, 추천 21
- [LTX2.3 워크플로우 공유](https://arca.live/b/aiart/177971843) — 2026-07, 추천 21
- [DDSD 추가 업데이트](https://arca.live/b/aiart/75057131) — 2023-04, 추천 20
- [빡통 워크 6.0 - 랜덤 이미지 자동 프롬프트 생성, 그림체 랜덤 전환, SAM3 디테일러](https://arca.live/b/aiart/157410060) — 2025-12, 추천 20
- [GPU 5종 MiniMax H3 I2VA 생성속도 테스트](https://arca.live/b/aiart/179069083) — 2026-08, 추천 20
- [Web UI 통합팩 설치 오류 드디어 해결했습니다. (방법 공유)](https://arca.live/b/aiart/63591884) — 2022-11, 추천 19
- [기초) 모델들 용량 줄이는 방법 (병합 활용 7GB->4GB)](https://arca.live/b/aiart/68966157) — 2023-02, 추천 19
- [[-] DirectML을 사용해 윈도우 환경에서 AMD 라데온 그래픽카드로 ComfyUI 돌리기](https://arca.live/b/aiart/72113936) — 2023-03, 추천 19
- [ComfyUI-DCW 노드업뎃](https://arca.live/b/aiart/169518554) — 2026-05, 추천 19
- [Wan 쓰시는 분들을 위해 워크플로우 공유](https://arca.live/b/aiart/172865906) — 2026-06, 추천 19
- [!!! 블랙웰 (RTX 50) 유저들 설치시 필독 !!!](https://arca.live/b/aiart/135962161) — 2025-05, 추천 18
- [WAN 2.2 SVI PRO 15초+올라마 자동 프롬프트+컬러매치](https://arca.live/b/aiart/159309952) — 2026-01, 추천 18
- [NAI 자동생성 앱 (NAIApp) v1.4.0](https://arca.live/b/aiart/168830995) — 2026-04, 추천 18
- [VAE 적용 확인 하는 법](https://arca.live/b/aiart/66138624) — 2022-12, 추천 17
- [쉽고 빠른 ComfyUI V6 마이너 업데이트](https://arca.live/b/aiart/122761449) — 2024-12, 추천 17
- [[워크플로우 공모전] 라면보단 어렵더라! 3트째 간편 워크플로우! (로라, 노드 수정 버전) (최종최종진최종 (1)) + 가이드](https://arca.live/b/aiart/141180724) — 2025-07, 추천 17
- [스팩트럼기반 최적화 노드](https://arca.live/b/aiart/165070655) — 2026-03, 추천 17
- [[커스텀노드] ComfyUI-PreviewMonitor: 프리뷰 몰아보기 노드](https://arca.live/b/aiart/171041315) — 2026-05, 추천 17
- [저처럼 forge neo쓰다가 여러 문제를 겪으시는분들 혹시라도 도움되길](https://arca.live/b/aiart/174448928) — 2026-06, 추천 17
- [NaN 오류 체크리스트](https://arca.live/b/aiart/68478526) — 2023-01, 추천 16
- [페) ILXL) TiledVAE 관련 미세? 실험](https://arca.live/b/aiart/119251783) — 2024-10, 추천 16
- [순정webui에서 v-pred모델쓰기](https://arca.live/b/aiart/128472488) — 2025-02, 추천 16
- [WAN 2.2 SVI 올라마 자동프롬프트 15초 워크플로우 업데이트 + 빡통워크 업데이트](https://arca.live/b/aiart/160056290) — 2026-01, 추천 16
- [(Linux + ROCm 10.1) 내가 쓰는 라데온 환경 세팅 방법](https://arca.live/b/aiart/179176367) — 2026-08, 추천 16
- [뉴비의 아니마 워크플로우 공유](https://arca.live/b/aiart/170889404) — 2026-05, 추천 15
- [Anima+IL 아님. IL+Anima임.](https://arca.live/b/aiart/171656386) — 2026-05, 추천 15
- [EasyUseAnima 0.3.1: 버그픽스, 업스케일, PAG 추가](https://arca.live/b/aiart/176029127) — 2026-07, 추천 15
- [Anima로 NAI 느낌 짤털](https://arca.live/b/aiart/178404708) — 2026-07, 추천 15
- [미니맥스 r2v로 만든것](https://arca.live/b/aiart/179207537) — 2026-08, 추천 15
- [물리 기반 이미지 후처리 노드 이거 좋다](https://arca.live/b/aiart/164468269) — 2026-03, 추천 14
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [AI그림 채널 오류 해결책 모음](https://arca.live/b/aiart/70417374) — 2023-02, 추천 13
- [(ComfyUI) Latent Hires Fix 사용시 그림 변형 줄이기](https://arca.live/b/aiart/86901822) — 2023-09, 추천 13
- [딸깍 AUTO-WAN 워크플로우 업데이트함 (순서 제어)](https://arca.live/b/aiart/154065928) — 2025-11, 추천 13
- [ComfyUI 램 오프로딩(RAM Offloading) ECC 이슈](https://arca.live/b/aiart/161052343) — 2026-01, 추천 13
- [comfyui-cns_sampler_patch](https://arca.live/b/aiart/172367736) — 2026-05, 추천 12
- [EasyUseAnima 0.2.0: 다양한 편의성 노드와 리저널 프롬프트 노드 추가](https://arca.live/b/aiart/175458978) — 2026-06, 추천 12
- [특정 작가태그(주로 NSFW 관련)에서 흑백이 자주 나올때 꿀팁](https://arca.live/b/aiart/141015266) — 2025-06, 추천 11
- [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유](https://arca.live/b/aiart/179083162) — 2026-08, 추천 10
- [LoRA 설치시 Error 및 해결방법 정리](https://arca.live/b/aiart/70243793) — 2023-02, 추천 9
- [ComfyUI 워크플로우 - SAM3, 마스크 디테일러로 활용하기.](https://arca.live/b/aiart/157473218) — 2025-12, 추천 9
- [인텔 Arc GPU용 ComfyUI windows-portable 등장](https://arca.live/b/aiart/168348535) — 2026-04, 추천 9
- [AMD R9700 attention 별 생성속도](https://arca.live/b/aiart/173409804) — 2026-06, 추천 9
- [모르고 쓰면 해골물인 ComfyUI 옵션](https://arca.live/b/aiart/177447677) — 2026-07, 추천 9
- [4.5 챈에 쓰는 ComfyUI 빡통 워크플로우 4.0](https://arca.live/b/aiart/139311613) — 2025-06, 추천 8
- [[워크플로우 공모전] 라면 어쩌고 저쩌고 실전압축 워크플로우 (完)](https://arca.live/b/aiart/141718826) — 2025-07, 추천 8
- [[워크플로우 공모전] 굿나잇 랜덤 워크플로우 v1.8](https://arca.live/b/aiart/142849197) — 2025-07, 추천 8
- [2주차 뉴비의 comfyUI 워크플로우 공유](https://arca.live/b/aiart/145850172) — 2025-08, 추천 8
- [빡통워크 5.1 자동 랜덤그림체 + 업스케일](https://arca.live/b/aiart/146574747) — 2025-08, 추천 8
- [SAM3 컨트롤넷 인페인팅 워크플로우 일부 개선 (컨트롤넷과 디테일러의 간섭 제거)](https://arca.live/b/aiart/168604584) — 2026-04, 추천 8
- [anima 1장 Lora 학습 comfyui 포터블 설치기](https://arca.live/b/aiart/168909715) — 2026-04, 추천 8
- [미니맥스 4스텝 터보로라 돌려봄](https://arca.live/b/aiart/179108697) — 2026-08, 추천 8
- [comfyui Starnodes 양자화 노드](https://arca.live/b/aiart/176070719) — 2026-07, 추천 7
- [AnimateDiff 때 돌려본 래퍼런스 영상을 R2V 해보았다.](https://arca.live/b/aiart/179265081) — 2026-08, 추천 7
- [내가 쓰고있는 ComfyUI 워크플로우 공유 (SDXL, Anima)](https://arca.live/b/aiart/179640921) — 2026-08, 추천 7
- [ddetailer 프롬 입력+ cfg스케일 조정 버전](https://arca.live/b/aiart/72119679) — 2023-03, 추천 6
- [(pony) 원피스 애니 와노쿠니 스타일 로라 공유](https://arca.live/b/aiart/112312429) — 2024-07, 추천 6
- [뭣같은 wan2.1 triton + sageattention 문제 해결법](https://arca.live/b/aiart/133924449) — 2025-04, 추천 6
- [[워크플로우 공모전] 라면보다 쉽다! 간편 종합 워크플로우 - 종합 개선 업데이트 1.4 버전](https://arca.live/b/aiart/141991828) — 2025-07, 추천 6
- [[워크플로우 공모전] 굿나잇 랜덤 워크플로우 v1.5](https://arca.live/b/aiart/142088366) — 2025-07, 추천 6
- [MMaudio 싱크 맞추는법](https://arca.live/b/aiart/151497792) — 2025-10, 추천 6
- [로컬 성인여성 작은가슴 만들기 쉬움](https://arca.live/b/aiart/156681380) — 2025-12, 추천 6
- [z-tipo-extension 설치 및 tipo 파일 수정](https://arca.live/b/aiart/162039111) — 2026-02, 추천 6
- [rife49.pth 버그제보 - 원클릭 코랩 실행 안되는 사람 봐](https://arca.live/b/aiart/162972850) — 2026-02, 추천 6
- [SAM3 디테일러 커스텀 노드가 작동되게 수정한 파일이야.](https://arca.live/b/aiart/164808456) — 2026-03, 추천 6
- [뉴비기준 sam3 노드 문제해결방법](https://arca.live/b/aiart/165353584) — 2026-03, 추천 6
- [(후타주의) Bernini 모델 I2V의 첫프레임이 변하는 원인을 찾았습니다.](https://arca.live/b/aiart/173025640) — 2026-06, 추천 6
- [1시간전에 올라온 H3 고속 로라 테스트](https://arca.live/b/aiart/179280493) — 2026-08, 추천 6
- [[꼴림찾아] 세일러 교복과 가터벨트](https://arca.live/b/aiart/65677286) — 2022-12, 추천 5
- [어제 있었던 개같은 얼굴 복제 현상 해결 후기](https://arca.live/b/aiart/131650885) — 2025-03, 추천 5
- [인텔 내장으로 comfyui를 돌릴때 tipo를 사용하는 방법?](https://arca.live/b/aiart/132353208) — 2025-03, 추천 5
- [MMaudio 싱크 관련 추가정보](https://arca.live/b/aiart/152614659) — 2025-11, 추천 5
- [comfyui 앱모드 사용법](https://arca.live/b/aiart/171528258) — 2026-05, 추천 5
- [H3 캐시 고치는 법](https://arca.live/b/aiart/179254934) — 2026-08, 추천 5
- [라데온 sageattention whl로 만들어왔어](https://arca.live/b/aiart/179413848) — 2026-08, 추천 5
- [오늘 업뎃해서 오류나는 챈럼들을 위한 이전버전 링크](https://arca.live/b/aiart/72586603) — 2023-03, 추천 4
- [[워크플로우 공모전] T2I특화 모듈형 프롬프트 워크플로우](https://arca.live/b/aiart/142197182) — 2025-07, 추천 4
- [ComfyUI - 검열이나 가리는게 있다면 사용하는 단부루 태그](https://arca.live/b/aiart/158273723) — 2025-12, 추천 4
- [EreNodes 자동완성 한국어 입력버그 수정본](https://arca.live/b/aiart/161031716) — 2026-01, 추천 4
- [webui fail 뜨면서 실행안되는 오류 해결법](https://arca.live/b/aiart/162800946) — 2026-02, 추천 4
- [GPT PRO가 맨든 미니맥스 고속노드](https://arca.live/b/aiart/179254885) — 2026-08, 추천 4
- [아 미맥 비디오 레퍼 모르겠다](https://arca.live/b/aiart/179453440) — 2026-08, 추천 4
- [라데온용 컴피 rocm 업데이트 방법 다시 알아옴](https://arca.live/b/aiart/160654263) — 2026-01, 추천 3
- [KSampler 프리뷰 해상도 수정해주는 커스텀 노드 ComfyUI-bleh](https://arca.live/b/aiart/161467109) — 2026-02, 추천 3
- [ComfyUI 에서 bjornulf_custom_nodes 가 설치되지 않는 문제 해결](https://arca.live/b/aiart/163272564) — 2026-02, 추천 3
- ['갑자기' comfy 에서 sage-attension 실패하는 이슈 해결 (자동 업데이트)](https://arca.live/b/aiart/163926460) — 2026-03, 추천 3
- [reforge 설치시 오류 해결법 중 꽤 유용한거 있어서 갖고옴](https://arca.live/b/aiart/164173886) — 2026-03, 추천 3
- [Ubuntu,윈도우 ai max 395 wan2.2 후기](https://arca.live/b/aiart/160894544) — 2026-01, 추천 2
- [정보탭의 kohya gui 설치후 발생한 문제해결](https://arca.live/b/aiart/176818115) — 2026-07, 추천 2
- [와 comfyui 다시 깔고 H3 돌리니깐 최적화 전부 먹히네요](https://arca.live/b/aiart/179172801) — 2026-08, 추천 2
- [ComfyUI Nightly용 Minimax H3 Cache 수정버전](https://arca.live/b/aiart/179215559) — 2026-08, 추천 2
- [WAI17(일러스트리어스) T2I 이미지 생성 워크플로우 공유](https://arca.live/b/aiart/179637421) — 2026-08, 추천 2
- [파이토치 설치 안되는사람 보셈](https://arca.live/b/aiart/69972082) — 2023-02, 추천 1
- [선 지저분하게 나오는 문제 해결!](https://arca.live/b/aiart/178281311) — 2026-07, 추천 1
- [뉴비 특정 lora만 안 돌아가는 문제가 있슴](https://arca.live/b/aiart/68448644) — 2023-01, 추천 0
- [병합하는 방법은 공지 없음??](https://arca.live/b/aiart/70241791) — 2023-02, 추천 0
- [ComfyUI - 와일드카드 복습](https://arca.live/b/aiart/155383963) — 2025-11, 추천 0
- [comfyui 인페인트 질문](https://arca.live/b/aiart/171032438) — 2026-05, 추천 0
- [외곽선이 명확하게 그려지지 않는 이유](https://arca.live/b/aiart/171512796) — 2026-05, 추천 0
- [comfyui 업스케일러 이 미친놈 대체 왜이러는걸까](https://arca.live/b/aiart/172185043) — 2026-05, 추천 0
- [페?)왜 갑자기 3D로 넘어가는 것일까요](https://arca.live/b/aiart/172447183) — 2026-06, 추천 0
- [head_back 태그가 안 먹음 (wai anima base1.0)](https://arca.live/b/aiart/172856945) — 2026-06, 추천 0
- [nai로 뽑은걸 컴피로 수정하고 싶어요](https://arca.live/b/aiart/173477606) — 2026-06, 추천 0
- [WAI로 그림 뽑다 보면 종종 마주치는 문제](https://arca.live/b/aiart/173511292) — 2026-06, 추천 0
- [AnimaPiDLoader 오류 발생](https://arca.live/b/aiart/173758822) — 2026-06, 추천 0
- [NAIA로 Comfy + 아니마를 써보려는데 사용법을 잘 모르겠음 ㅜㅜ](https://arca.live/b/aiart/173906125) — 2026-06, 추천 0
- [손찐빠 보정할때 한쪽손만 수정하는 문제 해결방법 아시는분..?](https://arca.live/b/aiart/175325170) — 2026-06, 추천 0
- [comfy에서 anima로 돌리는데 계속 crotch 쪽 찐빠가 나옴](https://arca.live/b/aiart/176433146) — 2026-07, 추천 0
- [comfyui inpaint turbo 워크플로우 관련 질문](https://arca.live/b/aiart/177370189) — 2026-07, 추천 0
- [ComfyUI 최신버전에서 MiniMaxH3-Cache 버그있는듯](https://arca.live/b/aiart/179251955) — 2026-08, 추천 0
