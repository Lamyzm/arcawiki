# VRAM·속도 최적화

> **원문 24건 → 이 문서 하나** · 주장 52개 · 정리 2026-08-14

ANIMA 가 SDXL 보다 느리다는 문제의식에서 채널의 최적화 논의가 시작됐다.
2026-02 부터 2026-08 사이에 sage attention · torch.compile · 블록 컴파일 · Spectrum · int8 양자화 ·
dynamic vram 제어가 차례로 검증됐고, 5070 Ti 기준 bf16 15.60초짜리 생성이 전부 적용 시 4.95초까지 내려갔다
(832x1216, 30스텝).

적용 순서는 '귀찮은 순'으로 **dynamic-vram 비활성화 → sage attention → 블록 컴파일 → Spectrum → int8-fast** 이며,
앞의 셋은 품질 손상이 거의 없는 등가 연산 대체이고 뒤의 둘은 정확도를 속도와 맞바꾼다.
노드 연결 순서는 확산모델로드 → lora loader → sage attention → block compile → KSampler 다.
전부 쓸 때는 Load Diffusion Model INT8 (W8A8) → INT8 Grouped LoRA → (DCW) → sage attention → block compile →
KSampler (Spectrum + SPD / SPEED).

## 누적 적용 실측표 (5070 Ti · 4060)
<small>2026-05 기준 · 근거 3건</small>

832x1216, 30스텝, cfg 5.0, er_sde, simple 스케줄러, 시드 3개(155788488~90) 고정.
랜덤 시드로 최초 로딩 오버헤드를 털어낸 뒤 측정했다. **로라 미적용** 기준.

| 조합 | 5070 Ti | 4060 |
|---|---|---|
| bf16 (기준) | 15.60s | 44.76s |
| +sage | 14.11s (+11%) | 41.19s (+9%) |
| +torch.compile | 11.14s (+41%) | 34.25s (+33%) |
| +spectrum | 7.14s (+124%) | 21.63s (+116%) |
| int8rowwise | 10.68s (+47%) | 30.45s (+43%) |
| int8 +sage | 9.19s (+72%) | 27.28s (+61%) |
| int8 +torch.compile | 7.60s (+110%) | 25.02s (+74%) |
| int8 +spectrum | **4.95s (+230%)** | **15.64s (+183%)** |

**로라를 적용하면 int8 계열의 이득이 절반 가까이 줄어든다** — 5070 Ti +47% → +28%, 4060 +43% → +21%.
bf16 계열은 로라 유무 차이가 거의 없다(15.60s → 15.57s). 터보 로라는 품질 손상이 너무 커서 비교에서 제외됐다.

다른 환경의 실측:

- RTX 5090, 832x1216, 28스텝, cfg 4.0 — 무최적화 6.84초(4.34 it/s) → sage 5.48초 → torch.compile 5.99초 →
  EasyCache 0.15 적용 4.22초(28스텝 중 7스텝 스킵, 1.33x) → 전부 적용 **4.17초** (약 64% 단축)
- AMD 9070xt (torch 2.10.0+rocm7.13.0a20260511, bf16+sage(triton 우회)+spectrum) 8.5초 /
  9060xt (bf16+sage+torch.compile+spectrum) 832x1216 약 22초 (댓글)

이 최적화들은 ANIMA 전용이 아니라 SDXL 계열에도 그대로 적용된다.

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264)</small>

## dynamic vram — 이미지는 끄고, 영상은 켠다
<small>2026-08 기준 · 근거 5건 · **근거 약함** · 자료 엇갈림</small>

**이미지 생성(ANIMA)에서는 끄는 쪽이 빠르다.** 램 오프로드로 인한 속도 저하를 막기 위해서이고,
이미지 품질에는 영향이 없다. VRAM 8GB 기준으로도 ANIMA 에는 문제없다.

`run_nvidia_gpu.bat` 를 복사해 이렇게 고친다.

```
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --fast --disable-dynamic-vram
```

**torch.compile 을 쓸 때는 사실상 필수다.** ANIMA All in One 워크플로우에서 반복 보고되던
`RuntimeError: Fault failed: 2` 의 원인이 제작자가 `--disable-dynamic-vram` 으로 실행하고 있었기 때문이었고,
v5.1(2026-06-03)은 워크플로우의 `disable_dynamic_vram` 옵션을 기본 on 으로 바꿔 배포했다.
v5 문서도 "torch_compile: disable_dynamic_vram 꼭 켜기"라고 못박는다. 실행 명령 예시:

```
comfy launch -- --port 8188 --windows-standalone-build --enable-manager --disable-dynamic-vram --auto-launch
```

**충돌 — 영상과 대형 GPU 에서는 반대다.**

- MiniMax H3 영상 생성(2026-08-05): 모델이 VRAM 에 다 올라가는 RTX 5090 에서도 **켜는 쪽이 총 시간이 짧았다**.
  On 2.78 s/it · total 1분 04.0초 vs Off 2.75 s/it · total 1분 16.1초. R9700 댓글에서도
  `--vram-headroom 6.0` 을 줘도 속도가 비슷할 만큼 dynamic vram 최적화가 좋아 VRAM 크기 차이가 잘 안 드러난다고 한다.
- H200 x4 환경(2026-08-08): dynamic vram 같은 **개인용 GPU 기준으로 튜닝된 최적화가 VRAM 이 충분한 환경에서는
  오히려 offloading 오버헤드**가 된다.

정리하면 이미지 생성 + torch.compile 이면 끄고, 영상 생성이면 켠다. 영상 쪽 사정은
[비디오 생성](video-generation.md) 을 보라.

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [ANIMA All in One 워크플로우 v5: i2i와 인… 26.05](https://arca.live/b/aiart/171941799) · [ANIMA All in One 워크플로우 v5.1: 오류 수… 26.06](https://arca.live/b/aiart/172676286) · [GPU 5종 MiniMax H3 I2VA 생성속도 테스트 26.08](https://arca.live/b/aiart/179069083)</small>

??? note "근거 5건 전부 보기"
    [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [ANIMA All in One 워크플로우 v5: i2i와 인… 26.05](https://arca.live/b/aiart/171941799) · [ANIMA All in One 워크플로우 v5.1: 오류 수… 26.06](https://arca.live/b/aiart/172676286) · [GPU 5종 MiniMax H3 I2VA 생성속도 테스트 26.08](https://arca.live/b/aiart/179069083) · [초고속 아니마 (초당 10장) + 간단한 최적화 후기 26.08](https://arca.live/b/aiart/179371306)

## sage attention — +9~11%, 품질 논쟁은 남아 있다
<small>2026-05 기준 · 근거 4건 · **근거 약함** · 자료 엇갈림</small>

ANIMA 생성에서 **약 9~11% 향상**이며 품질 손상이 거의 없는 등가 연산 대체로 분류된다.
RTX 3000 시리즈 이상이 필요하다.

적용 방법은 두 가지 중 하나만 쓰면 된다.

| 방법 | 비고 |
|---|---|
| KJNodes 의 `Patch Sage Attention KJ` 노드 | 워크플로우에 노드로 붙인다 |
| 실행 인자 `--use-sage-attention` | bat 에 인자가 있으면 노드는 불필요 |

실측: 5070 Ti 15.60 → 14.11초(+11%), 4060 44.76 → 41.19초(+9%), RTX 5090 6.84 → 5.48초.
워크플로우 구성에 따라 개선폭이 10% 이하로 떨어지기도 한다(2026-05-03).

**충돌.** [설치](install.md) 문서에 정리한 통합팩 배포글들은 10~15% 로 적고, 2026-06-27 판부터
"손가락 찐빠가 늘어난다는 이야기가 있다"를 본문에 덧붙였다. 반면 여기 최적화 글들은 품질 손상이 거의 없다고 본다.
어느 쪽도 품질을 정량 비교하지 않았으므로 양쪽을 그대로 둔다.

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [초보자를 위한 ANIMA All in One 워크플로우 v2 26.05](https://arca.live/b/aiart/169548769) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264)</small>

## torch.compile 은 GPU 편차가 크다 — 블록 컴파일이 더 실용적
<small>2026-06 기준 · 근거 5건</small>

**전체 torch.compile 의 향상폭은 14~41% 로 편차가 크다.** SM count 가 많은 GPU(3090·5090)에서 효과가 크고,
일부 환경에서는 오히려 느려지거나 아예 동작하지 않는다. 첫 로딩도 느려진다.
적용은 `TorchCompileModel` 노드 연결.

| 환경 | 결과 |
|---|---|
| 5070 Ti | +41% (15.60 → 11.14s) |
| 4060 | +33% (44.76 → 34.25s) |
| RTX 5090 | 약 14% (6.84 → 5.99s) |
| 라데온 16GB (댓글) | 13.4 → 9.7초 |
| 2080Ti (댓글) | fp16가속 + ScheduledCFG + torch.compile 로 1024x1024 35초 → 20초 |

**블록 컴파일이 더 낫다.** `Anima Block Compile` 노드(= `compile_transformer_blocks_only`)는 **+25%** 이면서
품질 손상이 거의 없고, 해상도를 바꾸지 않는 한 최초 1회 이후 오버헤드가 없다.
전체 컴파일이 45초 걸리던 환경에서 이 노드는 **컴파일이 8초**에 끝났다는 보고가 있다.
PiD 업스케일 노드는 자체 블록 컴파일을 구현해 해상도가 바뀔 때마다 5초 이내로 컴파일하면서 실행 속도가 약 1.3배 빨라진다
(설치: ComfyUI 매니저 → install via git URL → `https://github.com/sorryhyun/ComfyUI-Anima-PiD.git`).

**그래도 전체 torch.compile 을 쓴다면 캐시를 디스크에 남긴다** (한 글에서만 언급됨, 2026-05-23).

| 환경변수 | 값 |
|---|---|
| `TORCHINDUCTOR_CACHE_DIR` | `D:\Data\Packages\ComfyUI\torch_cache` (자기 설치 경로에 맞출 것) |
| `TORCHINDUCTOR_FX_GRAPH_CACHE` | `1` |

- 포터블: `run_nvidia_gpu.bat` 의 `python main.py` 실행 줄 **바로 위**에 `set` 으로 두 줄 추가
- Stability Matrix: 설정 → Environment Variables → Edit → `+` 로 두 값 추가 (Packages 안의 ComfyUI 설정이 아니다)
- 효과(4070Ti Super, 30스텝 1MP): 캐시 전 첫 실행 60초 / torch.compile 만 45초 → 캐시 후 첫 실행 20초, 이후 10초
- 미리 자주 쓰는 해상도를 한 장씩 뽑아 캐시를 채워 둔다
- 초기화 조건: NVIDIA 드라이버 업데이트, PyTorch 업데이트, inductor 값 변경.
  컨트롤넷·IP-Adapter 를 바꾸면 재컴파일되고 로라는 무관하다

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [anima PID 업스케일링 원클릭 노드 배포 26.06](https://arca.live/b/aiart/172741115) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264)</small>

??? note "근거 5건 전부 보기"
    [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [anima PID 업스케일링 원클릭 노드 배포 26.06](https://arca.live/b/aiart/172741115) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264) · [torch.compile 캐시 저장으로 최초로딩속도 줄이기 26.05](https://arca.live/b/aiart/171503442)

## Spectrum — 단일 최적화 중 가장 큰 폭(2배 이상)
<small>2026-05 기준 · 근거 3건</small>

일부 스텝을 실제 연산 대신 아주 가벼운 예측 연산으로 대체한다. **+116~124%** 로 ANIMA 단일 최적화 중 효과가 가장 크다.
다만 정확도를 속도와 맞바꾸는 방식이라 앞의 세 기법과 달리 **품질 손상이 불가피**하다.

두 갈래가 있다.

| 노드 | 쓰는 법 |
|---|---|
| `KSampler (spectrum)` (ComfyUI-Spectrum-KSampler) | KSampler 를 통째로 교체 |
| `Spectrum Adaptive Forecaster (SDXL)` (ruwwww/ComfyUI-Spectrum-sdxl) | 체크포인트 로드[모델] → 이 노드[model] → KSampler[모델] 로 사이에 끼움 |

실측: 25스텝 832x1216 기준 5070 Ti 4.5 → 2.7초, 4060 13.7 → 8.6초.
누적 벤치마크에서는 5070 Ti 7.14초(+124%), 4060 21.63초(+116%).

**Spectrum Adaptive Forecaster 파라미터**

| 파라미터 | 기본 / 권장 | 의미 |
|---|---|---|
| `steps` | KSampler 의 스텝 수 그대로 | |
| `window_size` | 2 | 실제연산:예측 비율. 클수록 빠르고 품질 저하 |
| `warmup_steps` | 5 | spectrum 미적용 초반 스텝 |
| `stop_caching_step` | -1 (= 마지막 20% 구간), 또는 전체스텝-3 (30스텝이면 27) | spectrum 미적용 후반 스텝 |
| `m` | 3 | 흐름 곡선 복잡도. 너무 높으면 노이즈까지 추종 |
| `w` | 0.3 | 체비셰프/테일러 예측 블렌딩 비율 (1에 가까울수록 체비셰프) |
| `lam` | 0.1 | 릿지 회귀 정규화 강도(λ). FP8/FP16 저정밀도에서 이미지가 깨지면 올린다 |
| `flex_window` | 0 (공격적 가속은 0.25) | window_size 에 스텝당 누적 가산 |

`warmup_steps` 와 `stop_caching_step` 이 고정 스텝을 먹기 때문에 **스텝 수가 적으면 효과가 떨어진다.**

**SPEED 합본 노드**(`KSampler (Spectrum + SPD / SPEED)`): `split_mode=single`(옵션이 하나뿐),
`spd_scale=0.5`(목표 해상도의 절반부터 시작, 기본값 유지 무방), `spd_sigma=0.7`(노이즈 100 → 70% 까지 저해상도로
디노이즈한 뒤 목표 해상도로 확장). 스텝이 아니라 시그마 잔여량 기준이라 스케줄러에 따라 확장 후 남은 스텝 수가 달라지고,
남은 스텝이 부족하면 품질이 크게 손상된다. 작성자 스스로 "나라면 SPEED 는 빼고 쓸 듯"이라고 적었다.

SDXL 용 구현이라 DiT 모델인 ANIMA 에서는 성능이 아쉽다는 지적도 댓글에 있다.

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [로컬 comfyui 찍먹해보기 - Spectrum 가속 26.05](https://arca.live/b/aiart/171935194) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264)</small>

## Spectrum 을 쓸 때 피해야 하는 조합
<small>2026-05 기준 · 근거 3건</small>

**샘플러** — ancestral(euler a)·sde 계열은 매 스텝 랜덤 노이즈를 주입해 예측이 어긋나므로 피한다.
`euler a` 와 같이 쓰면 퀄리티가 확 나빠지고, `dpmpp_2m_sde` 는 "노래방 조명 같은 노이즈"가 남는다.
작성자는 `er_sde` 로 문제가 없었다고 한다.

**스케줄러** — karras 계열 비호환. 같은 제약이 EasyCache 에도 있어 `simple`·`sgm_uniform` 이 권장된다.

**디테일러** — Spectrum 을 통과한 모델을 face detailer 에 물리면 성능이 떨어진다.
t2i 에만 쓰고 **디테일러에는 패치 전 모델을 연결**한다 (한 글에서만 언급됨, 2026-05-27).

**그 밖의 궁합** — Scheduled CFG Guidance 와 cfg++ 계열 샘플러는 궁합이 나쁘다(댓글).
터보 로라를 쓰면 Layer Replay·Spectrum 이 부적합하고, 반대로 터보 로라를 안 쓰면 NAG 가 비추천된다는 정리도 있다.

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 생성을 빨리 해보자! 26.02](https://arca.live/b/aiart/161452759) · [로컬 comfyui 찍먹해보기 - Spectrum 가속 26.05](https://arca.live/b/aiart/171935194)</small>

## int8 양자화 — 로라를 쓰면 이득이 절반으로 줄어든다
<small>2026-05 기준 · 근거 2건</small>

int8rowwise 양자화 모델은 bf16 대비 **+43~47%** 빠르지만, **로라를 적용하면 +21~28% 로 절반 가까이 줄어든다**
(5070 Ti +47% → +28%, 4060 +43% → +21%). bf16 런타임 양자화는 그보다 조금 낮다.

- 모델: `https://huggingface.co/Bedovyy/Anima-INT8/resolve/main/anima-base-v1.0-int8rowwise.safetensors`
  → `models\diffusion_models`
- 노드: ComfyUI-INT8-Fast 의 `Load Diffusion Model INT8 (W8A8)` 로 확산모델로드를 교체

**노드 파라미터**

| 파라미터 | 값 |
|---|---|
| `weight_dtype` | default |
| `model_type` | anima |
| `on_the_fly_quantization` | false (이미 양자화된 int8rowwise 모델) / true (civitai 의 bf16 모델) |
| `enable_convrot` | true |
| `lora_mode` | 로라 미사용 시 None. 사용 시 Dynamic 권장(bf16 과 비슷하게 먹지만 느림) 또는 Stochastic(중간) |

로라는 `pre_lora` 소켓보다 뒤쪽에 `INT8 Grouped LoRA` 노드를 붙이는 편이 잘 된다.

**addmm 오류 패치** (한 글에서만 언급됨). `on_the_fly_quantization` 이 마지막 레이어까지 양자화해 spectrum 과 충돌한다.
제외 목록에 `'final_layer'` 를 추가하면 사라진다. 포터블 경로 터미널에서:

```powershell
Copy-Item "ComfyUI\custom_nodes\ComfyUI-INT8-Fast\int8_unet_loader.py" "...loader.py.bak"
(Get-Content "...int8_unet_loader.py" -Raw) -replace "'embed', 'llm', 'adaln',", "'embed', 'llm', 'adaln', 'final_layer'," | Set-Content "...int8_unet_loader.py" -NoNewline
```

이후 ComfyUI 재시작.

Windows portable Python 3.13 에서 Triton CUDA 커널 컴파일 실패
(`Failed to find Python libs`, `utils.cp313-winamd64.pyd`) 사례가 다수 보고됐다.
NumPy 를 2.3.x 로 낮추고 `python313.lib` 존재를 확인하며 C++ Build Tools 설치를 점검하라고 한다
([오류 해결](troubleshooting.md)).

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [Anima 최적화 속도테스트 26.05](https://arca.live/b/aiart/171106264)</small>

## 튜링(RTX 20 · GTX 16) 세대 우회
<small>2026-05 기준 · 근거 3건</small>

최적화 가이드가 RTX 3000 이상을 요구하는 이유는 **bf16 가속**이다. 튜링 세대는 bf16 을 못 써서
`KSampler (spectrum)` 을 쓸 수 없고, sage attention 도 2000번대에서는 힘들다.

대안 구성:

| 항목 | 내용 |
|---|---|
| spectrum 대체 | `ruwwww/ComfyUI-Spectrum-sdxl` 를 `ComfyUI\custom_nodes` 에 git clone |
| 품질 보완 | `Anzhc/Anima-Mod-Guidance-ComfyUI-Node` (매니저 또는 git clone) |
| 전용 CLIP | `Anzhc Noobai11 CLIP L Anime.safetensors` (Anzhc/Noobai11-CLIP-L-and-BigG-Anime-Text-Encoders) |

Anima Mod Guidance 는 속도에는 영향이 없지만 최적화 과정에서 생기는 품질 저하를 DCW 와 함께 보완해 주므로
사실상 반필수로 본다. 연결이 지저분한 이유는 **모드 가이던스에 들어가는 CLIP 과 KSampler 에 들어가는 CLIP 이
서로 달라야 하기** 때문이다.

프롬프트 칸은 1 = 베이스(품질 태그), 2 = 긍정, 3 = 부정.
베이스 프롬을 긍정에도 넣는 것이 안즈크 방식이고, 글쓴이는 StringConcatenate 로 이어 붙여 중복 입력을 피했다.
로라는 노드 선택 후 Ctrl+B(또는 우클릭 '실행 건너뛰기')로 바이패스를 풀고 Add LoRA / Remove LoRA 로 개수를 조절한다.

<small>근거 — [Anima 찍먹해보기 - 최적화 26.05](https://arca.live/b/aiart/171129670) · [아니마만을 위한 아니마를 위한 아니마 전용 노드들 26.05](https://arca.live/b/aiart/171378660) · [튜링용 아니마 최적화 워크플로우 26.05](https://arca.live/b/aiart/171232354)</small>

## 영상 모델(MiniMax H3) 쪽의 VRAM·RAM 옵션
<small>2026-08 기준 · 근거 3건 · **근거 약함** · 자료 엇갈림</small>

**GPU 격차** — 동일 조건(544x800 = 0.4MPixel, duration 5.0, 20스텝, seed 42, 커스텀 노드 최적화 없음, 2회차 생성):

| GPU | s/it | total |
|---|---|---|
| RTX 5090 (400W) | 2.78 | 1분 04.0초 |
| RTX 3090 (350W) | 7.13 | 2분 40.9초 |
| R9700 (300W) | 10.06 | 3분 27.2초 |
| RX 7900XT (285W) | 16.54 | 6분 52.8초 |
| RTX 3060 (170W) | 24.12 | 8분 59.4초 |
| Intel B580 | — | 구동 실패 (int8convrot 2회차 UR_LOST, fp8 은 BSOD, dynamic vram 불안정) |

**어텐션 선택이 벤더마다 다르다.** R9700 은 sage-attn(PR-368) 10.06 s/it > flash-attn 13.44 s/it,
RX 7900XT 는 flash-attn(CK) 16.54 > sage-attn(PR-381) 17.57 > pytorch-attn 28.06 s/it.

**`--disable-pinned-memory` 로 RAM 을 줄인다** (한 글에서만 언급됨, 2026-08-05).
Windows 14~16GB, Linux 6GB 수준으로 내려간다. MiniMax H3 는 모델 크기만 40GB 라 RAM 40GB 점유가 정상이며,
이 옵션으로 줄일 수 있으나 느려질 수 있다. `--fast fp16_accumulation` 의 이득은 미미했다
(5090 On 2.78 s/it · 1분 04.0초 vs Off 2.88 s/it · 1분 07.4초).

**w4a8_int 양자화 — 본문과 댓글이 엇갈렸다가 정정됐다.**
2026-08-10 글 본문은 w4a8 이 int8 대비 약 1.09배 **빠르다**고 썼으나, 댓글이 같은 영상 기준
w4a8 2.10 s/it(52초) vs int8convrot 2.01 s/it(50초)로 오히려 **1.09배 느리다**고 정정했고 작성자도 수긍했다.
독립 측정(2026-08-07)도 int8convrot 64.99초(2.77 s/it) vs w4a8 69.90초(2.81 s/it)로 같은 방향이다.
다만 VRAM 이 작은 환경이나 큰 해상도·긴 길이에서는 cpu offload 가 줄어 유리할 수 있다.
요구사항은 ComfyUI git 최신 + comfy-kitchen v0.2.27 이상이며 AMD 도 day 0 지원이다.
자세한 내용은 [MiniMax H3](minimax-h3.md) 를 보라.

<small>근거 — [GPU 5종 MiniMax H3 I2VA 생성속도 테스트 26.08](https://arca.live/b/aiart/179069083) · [미니맥스 w4a8 int8 최적화 / 새로운 sol-attn… 26.08](https://arca.live/b/aiart/179541542) · [ComfyUI w4a8_int 양자화 모델 지원 26.08](https://arca.live/b/aiart/179270173)</small>

## 한 글에서만 나온 기법들
<small>2026-04 기준 · 근거 3건 · **근거 약함** · 자료 엇갈림</small>

**Anzhc Qwen2D-VAE (2026-04-18, 한 글)** — Qwen Image VAE 에서 영상이 아닌 경우 낭비되는 부분을 쳐낸 VAE.
노드(`Anzhc/anzhc-qwen2d-comfyui`)를 깔고 해당 VAE 를 선택하면 된다.
**본문 주장과 실사용이 엇갈린다** — 본문은 "VAE 작업에서 VRAM 약 3배 절감, 속도 2.5배"라고 하지만,
댓글의 실사용자는 **속도 차이는 별로 없고 VRAM staged 가 242MB → 85MB 로 줄었다**고 보고했다.
해상도를 더 키우면 체감이 클 것이라는 단서가 붙었다.

**NVFP4 (2026-03 기준, 한 글)** — NVIDIA 가 GDC 2026 에서 발표한 내용으로, GeForce RTX 50 시리즈에서
영상 생성 최대 2.5배·VRAM 60% 감소, FP8 은 1.7배·40% 감소를 내세웠다.
FLUX.1 은 BF16 23GB → 신규 포맷 9GB 로 RTX 5070 Ti·5080 같은 16GB 카드에서도 로컬 실행이 가능해진다고 한다.
그러나 댓글 반응은 **LoRA·커스텀 노드 호환을 계속 신경 써야 해서 실사용에서는 안 쓴다**는 쪽이 주였다.

**WAN2.2 Wrapper 의 VAE 인코딩 타일링 (2026-03 기준, 한 글)** — Wrapper 기본 정책이 입력 크기와 무관하게
무조건 가로세로 4분할이라 캐릭터 얼굴 중앙이 쪼개질 확률이 높고 타일이 작아 오버헤드도 크다.
`custom_nodes\ComfyUI-WanVideoWrapper\wanvideo\wan_video_vae.py` 의 1399~1412 라인을 고쳐 픽셀 수로 분기시킨다.

| 입력 크기 | 타일링 |
|---|---|
| 210만 화소(1920x1080) 이하 | 없음 |
| 210만 초과 | 짧은 축 100%, 긴 축 80% |
| 250만 초과 | 긴 축 60% |
| 그 이상 | 40% (40+40+20 3분할) |

VRAM 별 배포본이 셋이다 — 16GB 이하(720p급까지 노 타일링), 24GB(180만 픽셀까지), RTX 5090 이상(1080p까지).
**디코딩 VAE 가 아니라 인코딩 VAE**(CLIP 처리 전 첫 단계)라는 점에 주의한다.
VAE 인코딩 시 VRAM·가상 메모리를 거의 만땅 쓰며 전보다 느려지면 타일링 정책이 실패한 것이니 수치를 낮춘다.

<small>근거 — [anima용 더빠르고 가벼운 qwen vae 26.04](https://arca.live/b/aiart/168018256) · [NVIDIA RTX로 ComfyUI 가속, FP4 양자화 기… 26.03](https://arca.live/b/aiart/164756981) · [WAN2.2 COMFYUI용 TILING VAE 인코딩 화질… 26.03](https://arca.live/b/aiart/164043399)</small>

## 그래픽카드 고르기 — 2026년 7월 기준
<small>2026-07 기준 · 근거 2건 · 자료 엇갈림</small>

**먼저 원칙** — `GPU 속도 = 그림 뽑는 속도`, `VRAM 크기 = 그림 크기와 추가 기능 가능 여부`. 이 둘은 따로 논다. VRAM 이 커도 느릴 수 있고, 빨라도 VRAM 이 작으면 ControlNet·업스케일에서 막힌다.

성능 순서는 `xx90 > xx80ti > xx80 > xx70ti > xx70 > xx60ti > xx60 > xx50ti > xx50 > xx30` 이고, `super` 는 `ti` 처럼 조금 더 좋은 것, 앞자리는 세대다.

### 가격대별 (SDXL 이미지 생성속도, RTX 5070 Ti = 1.0)

| 카드 | 가격 | 배수 | VRAM | 메모 |
|---|---|---|---|---|
| **RTX 5070 Ti** | 150~160만 | **1.0** | 16GB | **원픽 추천** |
| RTX 5060 Ti 16GB | 90~100만 | 0.5 | 16GB | 180W. FP8/FP4 가속 지원. **16GB 최저가** |
| RTX 5070 | 100~110만 | 0.75 | 12GB | VRAM 12GB 라 **비추천** |
| RTX 3090 (중고) | 110~120만 | 0.75 | **24GB** | ~400W. NVLink 로 VRAM 병합이 되는 마지막 세대라 인기 |
| RTX 3080 / 3080 Ti 12GB (중고) | 40~50만 | 0.7 | 12GB | 350W 이상, 발열 심함. FP8/FP4 미지원. 서멀 재도포 필요 |
| RTX 3060 12GB (중고) | 20만 후반 | 0.3 | 12GB | bf16 지원, 6핀 1개. FP8/FP4 미지원 |
| RTX 3060 **8GB** | — | — | 8GB | **사면 안 된다** |
| 지포스 10(파스칼) 이하 | — | — | — | **사용 불가. 중고가 헐값이라도 금지** |

4000번대는 매물이 없어 다루지 않았다고 작성자가 밝혔다.

**⚠️ 충돌 — 5060 Ti 와 5070 Ti 의 차이** : 본문은 **2배**라고 하고 근거 글을 든다. 그런데 **둘 다 쓰는 댓글러가 실제로는 0.7배 수준 차이**라고 반박했다. 작성자는 본문을 유지했다. 실사용 체감은 두 배까지는 아닐 가능성이 있다.
(참고로 5090 vs 5070 Ti 는 실사용 2.0~2.2배, LLM 에서는 4.6배 차이라는 댓글이 있다.)

**3090 의 함정** — VRAM 24GB 는 매력적이지만, **Wan 2.2 처럼 오프로딩하는 신형 모델에서는 5060 Ti 도 못 잡는 벤치**가 있다.

**AMD·인텔·맥** — 가능은 하지만 엔비디아가 100이면 잘 쳐야 **10~20 수준**이라 새로 살 거면 비추다. 생성만 하면 라데온도 되지만 **로라 학습 툴이 마땅치 않고 개조가 필요**하다(댓글). → [설치와 환경 구성](install.md)

### 최소선

```
최소   VRAM 6GB 이상 NVIDIA, 가능하면 RTX 2000번대 이상
권장   3000번대 이상 VRAM 8GB  (SDXL·ANIMA 를 1024x1024 정도로 쓰는 데는 충분)
```

ControlNet 같은 추가 기능까지 쓰려면 더 필요하다. → [컨트롤넷](controlnet.md)

<small>근거 — [로컬 AI 입문자를 위한 장비 고르기 (그래픽카드) (26년… 26.07](https://arca.live/b/aiart/176516327) · [(26.07.10수정)안보면 뒤져도 할말없는 AI그림챈 압축… 24.12](https://arca.live/b/aiart/123263240)</small>

## 나머지 부품 — 견적 짜기
<small>2025-09 기준 · 근거 1건</small>

그래픽카드만 좋으면 되는 것이 아니다. **우선순위는 `그래픽카드 > DRAM 용량 > SSD > CPU > 메인보드 > DRAM 스피드`** 다.

| 부품 | 기준 |
|---|---|
| **DRAM** | 최소 **32GB**, 본격 **64GB**, Wan 2.2 같은 건 **96GB 이상**도 고려. 16GB 는 SDXL 정도, 8GB 이하는 비권장 |
| **SSD** | **1TB 이상 PCIe 4.0 NVMe** 권장 — 가상 메모리 역할을 한다 |
| CPU | 라이젠 5600 / 인텔 12400F 급이면 충분. 단 **GGUF + RTX 4070~5080 조합이면 싱글코어가 빠른 CPU**(라이젠 9600X)가 필요하고 **인텔은 E코어를 꺼야** 한다 |
| DDR5 | 4개 구성은 클럭 저하가 극단적이다 — **2개 구성** 권장 |
| PCIe | `3.0 8x`(= `4.0 4x`) 까지는 성능 하락이 극단적이지 않다 |

**공짜로 VRAM 0.5~1GB 버는 법** — 내장그래픽을 메인 GPU 로 두고 **외장 그래픽카드에는 모니터를 연결하지 않으면** 화면 출력에 쓰이던 VRAM 이 돌아온다.

**이미 가진 카드 기준**

```
RTX 3000 이상            도전할 만하다
RTX 2000                 SDXL 정도
Arc B580 · RX 7000 · A770  세팅은 어렵지만 SDXL 은 된다
RX 6000 이하 · GTX · MX    포기
```

> 게임 겸용이면 CPU 병목이 생길 수 있으니 SSD·DRAM 용량·그래픽카드만 참고하라고 작성자가 전제를 달았다.

<small>근거 — [로컬 그림 AI용 컴퓨터 견적 짜는 방법 25.09](https://arca.live/b/aiart/147541161)</small>

## 온도와 전기 — 전력제한과 언더볼팅
<small>⚠️ 2023-05 기준 · 근거 1건</small>

AI 그림은 글카를 하루 종일 혹사시킨다. **온도·전력 관리가 실질적인 문제**이고, 이 항목은 세대가 바뀌어도 그대로 쓸 수 있다.

```
설정이 귀찮고 안정성이 최우선이면  →  전력제한
성능과 온도의 스윗스팟을 찾겠다면   →  언더볼팅
```

준비물: MSI Afterburner, 3D Mark Demo(Time Spy, 가능하면 Port Royal), 최신 NVIDIA 드라이버(최신에 버그가 있으면 바로 이전 버전), 선택으로 HWiNFO64.

**⚠️ Afterburner 함정** — 설정 창을 닫을 때 **`_`(최소화)를 눌러야 세팅이 유지되고 `X` 를 누르면 순정으로 돌아간다.** 일반 탭에서 '윈도우 시작 시 자동 실행' 과 '최소화 모드로 시작' 을 체크해야 부팅 후에도 적용된다. 그리고 세팅 후 반드시 **'설정 적용'** 버튼을 눌러야 반영된다.

### 전력제한 — 슬라이더 하나

RTX 4090 실측 (실내 25도, 512x768 / 40스텝 / 배치 12):

| 설정 | 핫스팟 | 전력 |
|---|---|---|
| 순정 | 71.1℃ (1.05V) | 346W |
| 80% 제한 | 70.3℃ | 344W |
| 70% 제한 | 69.3℃ | 334W |

**순정 상태에서도 그림 뽑을 때 이미 80% 수준만 쓰고 있어서 80% 제한은 사실상 변화가 없다.** 작성자 표현으로 *'80% 전력제한한 사람은 해골물을 마시고 있었을 수도'*. 유의미한 것은 70% 부터다.

### 언더볼팅 — 실측 효과가 크다

RTX 4090: 순정 71.6℃ / 1.05V / **346W** → `0.95V 2745MHz` 언더볼팅 **62.8℃ / 276W**.
**성능 감소폭보다 소비전력·온도 감소폭이 훨씬 크다.**

절차 — 커브에디터를 열고 3D Mark Time Spy(또는 Port Royal)를 돌려(도중에 아무것도 클릭하면 처음부터) 결과 화면의 GPU 코어클럭(분홍 그래프) 값을 확인한다.
- **4000번대**: 코어클럭 슬라이더를 왼쪽 끝까지 내리고 적용 → `950mV` 지점의 점을 아까 확인한 코어클럭 바로 위 값에 놓고 다시 적용
- **3000번대**: 코어클럭을 `-150~-240` 으로 두고, `900mV` 점을 옮긴 뒤 그 오른쪽을 `Shift`+드래그로 끝까지 끌어 평평하게

**참고값** (수율에 따라 다르다)

```
4090     0.90V 2595 / 0.95V 2745 / 1.00V 2850 MHz
4080     0.90V 2580 / 0.95V 2700
4070 Ti  0.90V 2610
4070     0.925V 2715 / 0.95V 2745 / 0.975V 2790 / 1.00V 2850
3090     0.85V 1850 / 0.875V 1865 / 0.887V 1900 / 0.931V 1950
3080     0.85V 1850 / 0.887V 1900 / 0.931V 1950
3080Ti · 3060Ti   0.75V 1650 / 0.80V 1755 / 0.85V 1875 / 0.90V 1965
3070 Ti  0.80V 1785 / 0.85V 1890 / 0.90V 1980
3060     0.80V 1740 / 0.85V 1875 / 0.993V 1995
```

안정화 — 튕기면 전압을 `+25mV` 씩 올리거나 코어클럭을 `-15~-45MHz` 씩 내린다(클럭이 15 단위라서). 더 쥐어짜려면 `+15MHz` 씩 올리거나 `-25mV` 씩 낮추며 테스트하고, **마지막으로 통과한 값에서 -15~-30 한 값을 실사용으로 쓴다.** 한 번 통과했다고 바로 쓰지 말고 3회 이상 크로스체크하거나 Port Royal 스트레스 테스트(20주기 약 40분)를 돌린다.

**갑작스러운 재부팅 진단법** — 99% 커널 파워 에러다. `시작 > 검색 > event viewer` → 위험 → 커널 파워 → 자세히 탭에서 버그체크코드를 확인하고 16진수로 바꾼다. 예: `281` → `0x119` = `VIDEO_SCHEDULER_INTERNAL_ERROR`, 파라미터1 `0xA000` 은 '메모리 손상 또는 불량 하드웨어' — **무리한 메모리 오버클럭이 원인**이다.

> 댓글에는 **'값 찾는 게 어려우면 전력제한만 하라, 언더볼팅은 오버클럭 이상으로 위험하다'** 는 반론도 있다. 라데온 쪽 언더볼팅 값(RX 7900 XTX)은 [설치와 환경 구성](install.md)에 있다.

<small>근거 — [뜨거운 그래픽카드를 달래보자: 전력제한 및 언더볼팅 세팅 (… 23.05](https://arca.live/b/aiart/77471456)</small>

## 옛 글을 만났을 때 — 무엇이 속도를 정하고 무엇이 한계를 정하나 (2023)
<small>⚠️ 2023-02 기준 · 근거 1건</small>

2023년 2월, **'3천번대 미만이면 코랩 써라'** 라는 채널 통설을 실제 벤치마크로 검증한 글이다. **코랩은 지금 사실상 막혔고 세대도 바뀌었지만, 지표 설명은 그대로 통한다.**

| 지표 | 무엇을 정하나 |
|---|---|
| **CUDA 성능** | 같은 조건에서 이미지 한 장을 뽑는 **시간** |
| **VRAM 용량** | 할 수 있는 작업의 **한계** — ControlNet, Hires.fix 처럼 메모리를 더 쓰는 작업을 얹을 수 있는지. 한계를 넘으면 `CUDA out of memory` |

이 구분이 2026년의 `GPU 속도 = 속도 / VRAM = 가능 여부` 원칙의 원형이다.

당시 결론 — 코랩이 할당하던 Tesla T4 는 CUDA 성능이 RTX 2060 보다 약간 처지지만 **VRAM 이 16GB 로 여유로워, 같은 급 카드가 `medvram` 을 강요받는 상황에서도 성능 하락 없이 생성**할 수 있었다. 반대로 RTX 2060 보다 상급 카드는 `medvram` 을 켜도 코랩보다 빠르거나 비슷했다.

**댓글의 중요한 정정(작성자가 수용)** — GTX 1000번대는 **fp16 성능이 매우 나빠 fp32 로 돌아가므로 벤치 점수를 절반으로 깎아 봐야 한다.** 지금도 GTX 계열이 '사용 불가' 로 분류되는 근거가 이것이다.

실사용 수치 감각(2023년): 1660S 가 512x768 에 50초 걸리던 것이 3060 에서 10초 초중반. 3060 랩탑은 데스크톱 3060 과 10% 차이.

<small>근거 — [WebUI 그래픽 카드 가이드 (1) : 입문 - '3천번대… 23.02](https://arca.live/b/aiart/70611187)</small>

## ANIMA 전용 TeaCache — 빠르지만 품질은 EasyCache 가 위
<small>2026-07 기준 · 근거 1건 · **근거 약함**</small>

`ComfyUI-Anima-TeaCache` — EasyCache 처럼 **이미 만들어진 부분을 다시 연산할 때 건너뛰도록 캐시를 써서** 샘플링 속도를 올리는 노드다.

```
저장소  https://github.com/CocyNoric/ComfyUI-Anima-TeaCache
기본값  rel_l1_thresh = 0.050   ← euler 샘플러 기준으로 보수적으로 잡힌 값
```

주로 쓰는 ANIMA 샘플러별 설정은 GitHub 페이지를 봐야 한다.

**검증 환경** — RTX 2070 SUPER 8GB, ANIMA int8/mxfp8(Aesthetic v1.1), SageAttention + Torch Compile, 실행 인자 `--enable-triton-backend --lowvram --disable-dynamic-vram --async-offload 2 --fast cublas_ops`. 이 환경에서 기존 EasyCache 대비 확실한 속도 차이가 났다.

**⚠️ 다만 글쓴이 스스로 인정한 것** — 실험 세팅 기준 **품질은 EasyCache 가 더 위**다. `rel_l1_thresh` 를 `0.15` 로 낮추면 디테일이 EasyCache 보다 올라가지만 **속도가 몇 초 늘어난다.**

정리하면 이 노드의 자리는 *'EasyCache 보단 소폭 빠르고, 품질은 임계값을 낮춰야 따라잡는다'* 정도다. **한 글에서만 나온 실측이고 다른 사람의 재현 보고는 없다.**

`--disable-dynamic-vram` 을 함께 쓴 것에 주의할 것 — 이 문서 앞쪽의 'dynamic vram' 항목과 이어진다.

<small>근거 — [아니마 전용 티캐시 노드 26.07](https://arca.live/b/aiart/178238402)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 12개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| ANIMA 는 Euler A + automatic/normal 조합에서 그림이 기괴해지므로 Euler 또는 ER SDE 샘플러에 simple 또는 SGM uniform 스케줄러를 써야 한다 | 7 | 0 | 2026-04~2026-08 |
| 캐릭터·작가·매체 태그 안의 괄호는 역슬래시로 이스케이프해 nagisa \(blue archive\), star \(sky\), graphite \(medium\) 처럼 적는다 | 7 | 0 | 2025-08~2026-07 |
| 와일드카드는 언더바 두 개로 감싼 __파일명__ 형태로 호출하고, 하위 폴더에 있으면 __폴더/파일명__ 으로 적는다 | 6 | 0 | 2024-03~2026-07 |
| 2026년 Illustrious·SDXL·ANIMA 계열의 퀄리티 태그 관례는 masterpiece, best quality, highres, absurdres 를 프롬프트 앞머리에 두는 것이다 | 6 | 0 | 2026-02~2026-07 |
| 포니 계열에서 유래한 스코어 태그는 score_9 부터 score_1 까지 아홉 단계이며, 긍정에 score_9/score_8/score_7 중 1~3개를, 네거티브에 score_1/score_2/score_3 을 넣는 것이 관례다 | 6 | 0 | 2026-02~2026-06 |
| ANIMA 는 safe/sensitive/nsfw/explicit 안전등급 태그, year 2025 같은 연도 태그, newest·recent·mid·early·old 시대 태그를 받으며 안 야한 것을 뽑으려면 safe 를 넣어야 한다 | 5 | 0 | 2026-02~2026-05 |
| 이미지 생성(ANIMA)에서는 dynamic vram 을 끄는 쪽이 빠르며, torch.compile 을 쓸 때는 --disable-dynamic-vram 이 사실상 필수다 | 4 | 0 | 2026-05~2026-08 |
| ANIMA All in One 워크플로우는 V5/V5.1(2026-06) 이 기준판이고 그 이전 preview3 시절 판들은 작성자 스스로 낡았다고 철회했다 | 4 | 0 | 2026-04~2026-06 |
| 초보자용 ANIMA All in One 워크플로우 v2 는 생성 → SeedVR2 1차 업스케일 → SAM3 디텍터 디테일러 → USDU 2차 업스케일 구조다 | 3 | 0 | 2026-04~2026-05 |
| 터보(고속) 로라를 쓸 때는 Spectrum·Layer Replay 계열이 부적합하고 Anima NAG 를 쓰며, 터보 로라를 안 쓰면 정반대로 Spectrum 을 쓰고 NAG 를 뺀다 | 3 | 0 | 2026-05~2026-05 |
| 2026년 ANIMA·Illustrious 네거티브도 lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits 처럼 2022년 국룰의 뼈대를 그대로 이어 쓰되 worst quality, low quality 와 score_1~score_3 을 앞에 붙인다 | 3 | 0 | 2026-02~2026-05 |
| ANIMA 에는 디테일러 자체가 맞는 방법이 아니라 Highres 를 먼저 하고 눈 정도만 디테일러를 돌리는 것이 낫다 | 3 | 0 | 2026-04~2026-06 |
| ANIMA 의 기본 shift 값은 3 이고(ComfyUI supported_models.py 에서 3.0 확인) shift 0 은 CFG·스텝 조합과 무관하게 공통적으로 검은 화면이 나오므로 쓰면 안 된다 | 3 | 0 | 2026-02~2026-06 |
| ComfyUI 네이티브 PiD 구현은 gemma 를 불필요하게 받게 하고 정중앙이 찢어지는 결함이 있어, 재구현 노드(ComfyUI-Anima-PiD)로 옮겨가는 편이 낫다 | 3 | 0 | 2026-06~2026-06 |
| Nvidia PiD 업스케일은 SeedVR2 보다 최소 10배 빠르지만 배율이 4배로 고정되고 입력 긴 변을 512 또는 1024 에 정확히 맞춰야 일렁임이 없다 | 3 | 0 | 2026-06~2026-06 |
| Spectrum 계열 가속은 ANIMA 단일 최적화 중 효과가 가장 커서 속도를 2배 이상(+116~124%) 올린다 | 3 | 0 | 2026-05~2026-05 |
| ANIMA 생성에서 sage attention 은 약 9~11% 속도 향상이며 품질 손상이 거의 없다 | 3 | 0 | 2026-02~2026-05 |
| 전체 torch.compile 보다 블록 컴파일(Anima Block Compile / compile_transformer_blocks_only)이 컴파일 시간이 짧아 실용적이다 | 3 | 0 | 2026-05~2026-06 |
| 영상 생성에는 엔비디아 RTX 16GB 이상이 필요하고 AMD/Intel GPU는 사실상 부적합하다 | 3 | 0 | 2025-05~2026-01 |
| ComfyUI 와일드카드 파일은 ComfyUI\custom_nodes\comfyui-impact-pack\wildcards 에 txt 든 yaml 이든 넣으면 되고, 다른 커스텀 노드들도 이 Impact Pack 폴더를 공유한다 | 3 | 0 | 2025-01~2026-05 |
| bf16 을 못 쓰는 튜링(RTX20·GTX16) 세대는 KSampler(spectrum) 대신 ruwwww/ComfyUI-Spectrum-sdxl 와 Anzhc 의 Anima Mod Guidance 로 우회한다 | 2 | 0 | 2026-05~2026-05 |
| torch.compile 의 ANIMA 가속 효과는 GPU 에 따라 14~41% 로 편차가 크고 일부 환경에서는 오히려 느려지거나 동작하지 않는다 | 2 | 0 | 2026-02~2026-05 |
| Spectrum 가속 노드는 ancestral(euler a)·sde 계열 샘플러 및 karras 스케줄러와 호환되지 않는다 | 2 | 0 | 2026-02~2026-05 |
| int8rowwise 양자화 모델은 bf16 대비 +43~47% 빠르지만 로라를 적용하면 이득이 +21~28% 로 절반 가까이 줄어든다 | 2 | 0 | 2026-05 |
| ANIMA 의 highres 는 모델 지원 해상도를 넘지 않는 것이 좋고 2048 을 넘는 길이는 USDU(타일 분할)로 처리해야 한다 | 2 | 0 | 2026-05~2026-06 |
| 로컬에서 문제가 생기면 원인은 99% cmd 창에 영어로 적혀 있고 error 바로 옆이나 다음 줄에 해결법이 있는 경우가 많다. 긴 로그는 통째로 메모장에 붙여 Ctrl+F 로 `error` 를 찾으면 된다. 검색이 안 될 때는 대개 문장으로 검색해서 그런 것이므로 단어로·다른 키워드로·영문으로 바꿔 본다. 에러 메시지는 번역기라도 돌려 보고 질문하라는 것이 채널의 오래된 답이다 | 2 | 0 | 2023-02~2026-07 |
| MiniMax H3 의 w4a8_int 양자화는 int8convrot 보다 약 1.09배 느리며(69.90초 vs 64.99초), VRAM 이 작거나 큰 해상도에서만 cpu offload 감소로 유리할 수 있다 | 2 | 0 | 2026-08~2026-08 |
| RuntimeError: Fault failed: 2 는 torch compile 과 dynamic vram 이 함께 켜져 있을 때 발생하므로 --disable-dynamic-vram 으로 실행하거나 토치컴파일을 끈다 | 2 | 0 | 2026-06~2026-06 |
| ANIMA All in One v5 는 ComfyUI 포터블 0.20.1 을 권장하며 0.20.0 미만은 sam3 노드 미지원, 0.21.0 이상은 node2.0 문제로 UI 가 깨질 수 있다 | 2 | 0 | 2026-06~2026-06 |
| torch.compile 캐시는 TORCHINDUCTOR_CACHE_DIR 와 TORCHINDUCTOR_FX_GRAPH_CACHE=1 로 디스크에 남겨 첫 로딩을 60초에서 10~20초로 줄일 수 있고, 드라이버·PyTorch 업데이트 시 초기화된다 | 1 | 0 | 2026-05 |
| Anzhc 의 CLIP 사용 Anima Mod Guidance 는 기존 Anima Mod Guidance 와 노드 이름이 겹쳐 목록에 안 뜰 수 있어 custom_nodes 를 직접 수정해야 한다 | 1 | 0 | 2026-05~2026-05 |
| NVFP4 는 RTX 50 시리즈에서 영상 생성 최대 2.5배·VRAM 60% 감소를 내세우지만, LoRA·커스텀 노드 호환을 계속 신경 써야 해서 실사용에서는 기피된다 | 1 | 0 | 2026-03 |
| INT8-Fast 의 on_the_fly_quantization 이 마지막 레이어까지 양자화해 spectrum 과 충돌하므로, int8_unet_loader.py 의 제외 목록에 'final_layer' 를 추가해야 addmm 오류가 사라진다 | 1 | 0 | 2026-05 |
| GTX 1000번대는 fp16 성능이 매우 나빠 fp32 로 돌아가므로 CUDA 벤치 점수를 절반으로 깎아 봐야 한다 (댓글 지적을 작성자가 수용해 본문을 수정) | 1 | 0 | 2023-02 |
| PiD 업스케일의 degrade_sigma 는 0(+null embedding)이 가장 낫고 0.05 이상은 할루시네이션만 늘린다 | 1 | 1 | 2026-06~2026-06 |
| --disable-pinned-memory 는 MiniMax H3 의 RAM 사용량을 크게 줄여 준다(Windows 14~16GB, Linux 6GB) 다만 느려질 수 있다 | 1 | 0 | 2026-08 |
| AMD·Intel GPU 는 MiniMax H3 구동에서 NVIDIA 대비 크게 밀리며(R9700 3분27초 vs RTX3090 2분41초), Intel B580 은 구동 자체가 실패했다 | 1 | 0 | 2026-08 |
| MASK to SEGS 의 `crop_factor` 는 다시 그릴 때 참조할 영역의 크기이며, 크게 잡을수록 주변과 어우러지지만 디테일이 떨어진다 | 1 | 0 | 2026-02~2026-05 |
| 채널 규정 — 질문글은 반드시 질문탭에, 19금이면 19금 질문탭에 써야 하며 어기면 삭제 + 1일 차단이고 이것이 채널 차단 사유 1위다. 정보 없이 '안 켜져요 / 그림 이상해요 / 에러 떴어요' 만 쓴 질문도 삭제 + 1일(최대 3일) 차단이며, 질문할 때는 생성 환경(세팅) · 쓰는 모델 · 생성된 그림(EXIF 포함) · 에러 메시지 · 로컬이면 사양을 함께 적어야 한다. NAI·그록 등 외부 사이트의 결제·구독·환불 문의는 무통보 삭제 대상이다 | 1 | 0 | 2026-07 |
| ANIMA 전용 TeaCache 노드(`https://github.com/CocyNoric/ComfyUI-Anima-TeaCache`)는 EasyCache 처럼 이미 만들어진 부분을 다시 연산할 때 건너뛰도록 캐시를 써서 샘플링 속도를 올린다. 기본값 `rel_l1_thresh` 는 `0.050` 인데 이는 euler 샘플러 기준으로 보수적으로 잡힌 값이고 샘플러별 설정은 GitHub 를 봐야 한다. RTX 2070 SUPER 8GB + int8/mxfp8 환경에서 EasyCache 대비 확실한 속도 차이가 났으나, 글쓴이 실험 세팅 기준 품질은 EasyCache 가 더 위였고 `rel_l1_thresh` 를 0.15 로 낮추면 디테일이 EasyCache 를 넘지만 속도가 몇 초 늘어난다 | 1 | 0 | 2026-07 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [WebUI 그래픽 카드 가이드 (1) : 입문 - '3천번대 미만 코랩 써라'?](https://arca.live/b/aiart/70611187) — 2023-02, 추천 36
- [Anima 찍먹해보기 - 최적화](https://arca.live/b/aiart/171129670) — 2026-05, 추천 36
- [anima용 더빠르고 가벼운 qwen vae](https://arca.live/b/aiart/168018256) — 2026-04, 추천 34
- [ANIMA All in One 워크플로우 v5: i2i와 인페인트 정상화](https://arca.live/b/aiart/171941799) — 2026-05, 추천 34
- [로컬 그림 AI용 컴퓨터 견적 짜는 방법](https://arca.live/b/aiart/147541161) — 2025-09, 추천 29
- [Anima 생성을 빨리 해보자!](https://arca.live/b/aiart/161452759) — 2026-02, 추천 29
- [뜨거운 그래픽카드를 달래보자: 전력제한 및 언더볼팅 세팅 (6/3 수정)](https://arca.live/b/aiart/77471456) — 2023-05, 추천 28
- [초보자를 위한 ANIMA All in One 워크플로우 v2](https://arca.live/b/aiart/169548769) — 2026-05, 추천 25
- [로컬 comfyui 찍먹해보기 - Spectrum 가속](https://arca.live/b/aiart/171935194) — 2026-05, 추천 24
- [anima PID 업스케일링 원클릭 노드 배포](https://arca.live/b/aiart/172741115) — 2026-06, 추천 24
- [ANIMA All in One 워크플로우 v5.1: 오류 수정, 간단한 기능 추가](https://arca.live/b/aiart/172676286) — 2026-06, 추천 23
- [로컬 AI 입문자를 위한 장비 고르기 (그래픽카드) (26년7월)](https://arca.live/b/aiart/176516327) — 2026-07, 추천 23
- [아니마 전용 티캐시 노드](https://arca.live/b/aiart/178238402) — 2026-07, 추천 20
- [GPU 5종 MiniMax H3 I2VA 생성속도 테스트](https://arca.live/b/aiart/179069083) — 2026-08, 추천 20
- [NVIDIA RTX로 ComfyUI 가속, FP4 양자화 기술로 AI 영상 생성 속도 2.5배 향상](https://arca.live/b/aiart/164756981) — 2026-03, 추천 17
- [미니맥스 w4a8 int8 최적화 / 새로운 sol-attn 속도개선 소개](https://arca.live/b/aiart/179541542) — 2026-08, 추천 17
- [아니마만을 위한 아니마를 위한 아니마 전용 노드들](https://arca.live/b/aiart/171378660) — 2026-05, 추천 15
- [WAN2.2 COMFYUI용 TILING VAE 인코딩 화질/속도 직접 개선한 노드(추가)](https://arca.live/b/aiart/164043399) — 2026-03, 추천 13
- [Anima 최적화 속도테스트](https://arca.live/b/aiart/171106264) — 2026-05, 추천 12
- [초고속 아니마 (초당 10장) + 간단한 최적화 후기](https://arca.live/b/aiart/179371306) — 2026-08, 추천 8
- [튜링용 아니마 최적화 워크플로우](https://arca.live/b/aiart/171232354) — 2026-05, 추천 5
- [ComfyUI w4a8_int 양자화 모델 지원](https://arca.live/b/aiart/179270173) — 2026-08, 추천 5
- [torch.compile 캐시 저장으로 최초로딩속도 줄이기](https://arca.live/b/aiart/171503442) — 2026-05, 추천 4
- [[26.07.10수정]안보면 뒤져도 할말없는 AI그림챈 압축공지](https://arca.live/b/aiart/123263240) — 2024-12, 추천 0