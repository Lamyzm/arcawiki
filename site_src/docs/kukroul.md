# 국룰 — 채널이 합의한 기본값

> **원문 79건 → 이 문서 하나** · 주장 152개 · 정리 2026-08-14

여러 글이 **독립적으로 같은 말을 한 것**만 모았다. 어느 한 글에도 이렇게 정리돼 있지 않다. 괄호 안 숫자는 그렇게 말한 글의 수이며, 클수록 채널의 합의에 가깝다.

한 절만 예외다 — **"샘플러·스케쥴러·스텝·CFG"** 는 다수결이 아니라 **모델별 공식·배포자 권장값**을 계열별로 옮긴 것이고, 반론이 붙은 칸은 ⚠ 로 표시했다.

## ComfyUI 통합팩 — 딸깍 규약
<small>2026-08 기준 · 근거 9건</small>

채널에는 같은 사람이 만든 딸깍 통합팩 계보가 있다
(`0.11.1 → 0.15.1 → 0.20.1 → 0.22.0 → 0.23.0 → 0.26.0 → 0.30.0 → 0.31.0`, 여덟 판).
같은 규칙이 여덟 판에 걸쳐 반복돼서, 사실상 **성문화된 국룰**이다.

| 규칙 | 근거 |
|---|---|
| sage attention을 쓰려면 `run_nvidia_gpu.bat` 이 아니라 **`run_nvidia_gpu_fast_fp16_accumulation.bat`** 으로 실행 | 8건 |
| negpip 덕에 일반 프롬프트 칸에서 **`(tag:-1),`** 음수 가중치를 쓸 수 있다 | 6건 |
| 지원 GPU는 **지포스 3000~5000번대**, 라데온은 미확인 | 6건 |
| 출력물은 `output/날짜`, 중간 과정은 그 아래 `WIP` | 6건 |
| **한글이 없는 경로**에 압축을 푼다 | 3건 |
| 기존 모델 폴더는 `Add-Ons/Easy-Models-Linker.bat` 또는 `extra_model_paths.yaml` 복사로 공유 | 5건 |
| **본체를 업데이트하지 말고**, 새 판이 나오면 처음부터 새로 받는다 | 4건 |
| 설정 > Comfy > Nodes 2.0 > **모던 노드 디자인을 켜면** 워크플로우 배열이 깨지고 일부 노드가 오작동 | 4건 |

> **조건 하나** — sage attention을 끄면 **지포스 2000번대에서도** 동작한다 (2건).

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039)</small>

??? note "근거 9건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [comfyui portable v0.15.1 + sage +… 26.02](https://arca.live/b/aiart/163592169)

## SDXL / Illustrious 기본값
<small>2026-08 기준 · 근거 7건</small>

| 항목 | 값 | 근거 |
|---|---|---|
| 체크포인트 | **WAI-illustrious-SDXL** (`models/checkpoints`) | 5건 |
| 결과물이 탁하거나 흰 점이 찍히면 | **VAE Select = 2** (`fixFP16ErrorsSDXLLowerMemoryUse_v10`) | 4건 |
| Controlnet Mode Select | **1=일반, 2=오픈포즈, 3=리저널** (ANIMA 워크플로우는 1=일반, 2=컨트롤넷) | 5건 |
| 해상도 프리셋 수정 위치 | Illustrious·SDXL은 `ComfyUi_NakoNode/py/aspect_ratio.py`, ANIMA는 `comfyui-kjnodes/custom_dimensions.json` | 5건 |
| 태그 자동완성 | `autocomplete tag source` 를 **danbooru** 로 두면 e621 태그가 빠진다 | 3건 |
| NoobAI·V-pred 계열 | Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘다. **하나씩 바이패스**해 원인을 찾는다 | 5건 |

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039)</small>

??? note "근거 7건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430)

## ANIMA 배치
<small>2026-08 기준 · 근거 10건</small>

파일 세 개를 각각 다른 폴더에 넣어야 한다 (5건).

```
Base v1.0        →  models/diffusion_models
텍스트 인코더     →  models/text_encoders   (qwen_3_06b_base.safetensors 로 개명)
VAE              →  models/vae
```

- ANIMA는 **NVIDIA Cosmos-Predict2 2B** 기반이다 (3건)
- **INT8 판은 모델+텍스트인코더+VAE 합쳐 4GB 미만**이라 VRAM 8GB급에서도 무난하다 (2건)

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860)</small>

??? note "근거 10건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [Anima에서 사용할 수 있는 DMD2 LoRA 26.03](https://arca.live/b/aiart/164898297) · [ComfyOrg 공식모델들에 int8convrot 추가됨 26.07](https://arca.live/b/aiart/175519662) · [nvidia에서 cosmos3 출시했네. 26.06](https://arca.live/b/aiart/172423630) · [재밌는 비디오 제네레이션 모델 나왔네. 26.07](https://arca.live/b/aiart/176717035)

## 샘플러·스케쥴러·스텝·CFG — 모델 계열별 권장값
<small>2026-05 기준 · 근거 6건 · **근거 약함** · 자료 엇갈림</small>

**여기만은 "채널 다수결" 이 아니라 모델별 공식·배포자 권장값이다.**
계열이 다르면 값이 통째로 다르므로 **자기 모델 줄만 보면 된다.**
반론이 붙은 칸은 ⚠ 로 표시하고 아래에 양쪽을 다 적었다.

| 모델 계열 | 샘플러 | 스케쥴러 | 스텝 | CFG | 근거 |
|---|---|---|---|---|---|
| **ANIMA** | `er_sde` (기본) / `euler_a` / `dpmpp_2m_sde_gpu` | `simple` 또는 `beta` ⚠ | **30~50** | **4.0~6.0** | 공식, 2026-05 |
| **NoobAI-XL eps** (전 버전) | `Euler A` | — | **28~35** | **5~7** | 공식 매뉴얼, 2024-12 |
| **NoobAI-XL V-pred 1.0** | `Euler` | — | **32~40** | **3.5~5.5** | 공식 매뉴얼, 2024-12 |
| **NoobAI-XL V-pred 1.0** (대안) | `Euler A` | — | **28~40** | **3~5** | 공식 매뉴얼, 2024-12 |
| **Illustrious XL** | `Euler` ⚠ | `normal` | — | **5.0** (또는 7.0) | ILXL 가이드, 2024-10 |
| **Illustrious XL** (저CFG) | `euler_cfg_pp` (Euler CFG++) | `sgm_uniform` | — | **1.5** (또는 2.5) | ILXL 가이드, 2024-10 |
| **NoobAI 기반 2D 개선판** | `Euler` | `SGM Uniform` | **28** | **4.5** (+ CFG Rescale 0.6) | 배포자, 2025-06 |
| **Noob + ILXL 병합판** | `Euler a` | — | **28** | **5** | 배포자, 2025-03 |
| **NAI 4.5 full** | `k_euler_ancestral` | `karras` | — | **3.8~5.5** (가이던스) ⚠ | 실사용, 2025-06 |

> **NAI 용어 주의** — **가이던스가 곧 CFG** 다.
> NAI 공홈은 CFG 를 '가이던스' 로 표기하고 NAIA 는 가이던스를 'CFG' 로 표기해서 헷갈리는 사람이 많다.
> 리스케일은 '가이던스 리스케일' 이다.

### V-pred 을 쓸 때 하나 더

NoobAI V-pred 계열은 그냥 돌리면 과포화·과노출이 난다. 공식 매뉴얼의 처방은 둘 중 하나다.

```text
Rescale CFG  ≈ 0.7                                  ⚠ 반론 있음
Euler Ancestral CFG++ 샘플러 + CFG Scale 1 ~ 1.8
```

이유로 든 것은 (i) 색상·조명·디테일 최적화 (ii) 과포화·과노출 제거 (iii) 의미론적 이해력 향상이다.
**일부 UI 는 미지원**이고, Forge 는 CFG Rescale 이 설정이 아니라 **스크립트 형태**라 찾기 어렵다는 보고가 있다
(reForge 에는 설정으로 있다).

CLIP skip 은 **SDXL 아키텍처 전체에 적용되지 않으므로 설정할 필요가 없다.**
SD1.5 시절의 `Clip skip 2` 습관을 그대로 들고 오면 안 된다.

### ⚠ 반론이 붙은 칸

**1) ANIMA 의 스케쥴러 — `simple` 인가 `beta` 인가**

| 쪽 | 내용 |
|---|---|
| 공식 | `simple` **또는** `beta` 둘 다 제시 |
| 반례 (댓글) | `er_sde` + **30스텝** + **CFG 6** 에서는 **`beta` 가 더 낫다** |

글쓴이도 **"권장값을 꼭 따라갈 필요 없다"** 고 답했다. 조건이 달라 둘 다 맞는 경우로 본다.

**2) Illustrious 의 DPM 계열 — 정말 안 먹히나**

| 쪽 | 내용 |
|---|---|
| 본문 | SDXL, 특히 ILXL 은 **DPM/Karras 계열이 잘 안 먹힌다.** `Euler` 또는 `euler_cfg_pp` 를 쓰라 |
| 반론 (댓글 **다수**) | **dpm 시리즈를 안 쓰면 원래 작가 그림체 느낌이 안 난다** |

글쓴이도 **Euler 쪽이 깔끔하지만 거친 그림체 작가와는 잘 안 맞는다**고 인정했다.
→ **목적에 따라 갈린다.** 깔끔함이 목표면 Euler, **작가 화풍 재현이 목표면 DPM 계열**을 시험해 볼 것.

**3) NoobAI 의 Rescale CFG 0.7**

reForge 기준으로 **"0.7 을 줘도 기존이랑 똑같다"** 는 보고가 **둘** 있다.
공식 권장이지만 실행기에 따라 체감이 없을 수 있다.

**4) NAI 가이던스 3.8~5.5**

원글의 주장은 **가이던스 6~8(특히 7~8)이 과용이고 인체 찐빠의 주범**이며,
**2.7 아래로는 v3 시절처럼 덜 그린 결과**가 나온다는 것이다. 1:다수 nsfw 구도 이야기다.

| 쪽 | 내용 |
|---|---|
| 주장 | 최종 사용 범위 **3.8~5.5**. 가이던스를 낮추니 인체 찐빠·과한 색감·`official art` 부작용이 해결됐다 |
| 반론 (댓글 **다수**) | **동일 시드로 CFG 를 1/3/5/7/9 로 바꾼 비교 예시가 없어 변인통제가 안 됐다** |
| 자기정정 | 글쓴이가 처음엔 "5~6 도 문제" 라고 썼다가 **"7~8 만 문제"** 로 번복했다 |

실사용 후기로는 '찐빠가 확실히 줄었다', '구도가 좀 정적으로 바뀌었지만 손발몸 찐빠가 줄었다' 는 보고가 있었다.
같은 글이 **`dpm` 류는 여전히 안정성이 안 좋다**고 적었고,
`k_dpmpp_2m_sde + karras` 는 **그림체 재현을 가장 잘하지만** 찐빠가 여전해 포기했다고 밝혔다 —
위 2번 반론과 방향이 같다.

### ⚠ 뒤집힌 것 — DPM++ 2M Karras

**2023년 SD1.5 시절의 국룰은 `DPM++ 2M Karras` 였다.** 지금 옛 글을 보면 이게 나온다.

| 지금 | ← 예전 | 언제 |
|---|---|---|
| Illustrious·NoobAI 는 **`Euler`·`Euler A`**, ANIMA 는 **`er_sde`** | **`DPM++ 2M Karras`** ("Euler 는 DPM 과 비교조차 안 될 만큼 안 좋다") | 2023-02 → 2024~2026 |

당시 근거는 **연산 속도**였다. 원문 댓글이 확정한 '성능' 의 뜻은
**"최대한 적은 스텝으로 1000번 돌렸을 때의 결과물에 근접하는 것"** 이지 '그림이 예쁘다' 가 아니다.
샘플러마다 결과가 다른 것은 근사 과정의 **부수 효과**에 가깝다.

`beta57` 스케쥴러의 정체도 적어 둔다 (1건, 2026-06) —

```text
beta57 = comfy.samplers.beta_scheduler(model_sampling, steps, alpha=0.5, beta=0.7)
         이름의 '57' 이 alpha 0.5 와 beta 0.7 에서 왔다
```


<small>근거 — [NoobAI-XL user Manual(24.12.25 버전) 24.12](https://arca.live/b/aiart/124830494) · [ILXL 프롬프트 가이드 24.10](https://arca.live/b/aiart/118111192) · [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [NlxlMix - Noob 1.1 eps + Illustri… 25.03](https://arca.live/b/aiart/130197990)</small>

??? note "근거 6건 전부 보기"
    [NoobAI-XL user Manual(24.12.25 버전) 24.12](https://arca.live/b/aiart/124830494) · [ILXL 프롬프트 가이드 24.10](https://arca.live/b/aiart/118111192) · [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [NlxlMix - Noob 1.1 eps + Illustri… 25.03](https://arca.live/b/aiart/130197990) · [내용 추가2/잘못된 내용 수정)4.5f) 추가적으로 알아낸 … 25.06](https://arca.live/b/aiart/138557595) · [NAI-XL 2dac / 2.5dac 색감 개선모델 (권장 … 25.06](https://arca.live/b/aiart/140191370)

## 샘플러 이름 읽는 법 — 2 / S / M / a / SDE / Karras
<small>2026-05 기준 · 근거 3건</small>

**추천 결론은 뒤집혔지만 이름 읽는 법은 지금도 그대로 쓴다.**
`dpmpp_2m_sde_gpu` 같은 ComfyUI 샘플러 이름을 해석할 때 필요하다 (1건, 2023-02).

| 글자 | 뜻 |
|---|---|
| **`2`** | **2차** 샘플러 |
| **`S`** | **Singlestep** (대표적으로 DPM solver). 스텝마다 모델을 **2번 추론**해서 각 스텝이 Multistep 보다 **2배 느리다.** 고차 Singlestep 은 불안정성 문제가 있다 |
| **`M`** | **Multistep** (대표적으로 DEIS). Singlestep 의 불안정성을 해결한 것 |
| **`a`** / `ancestral` | **Ancestral sampling.** 스텝마다 노이즈를 더 추가할 수 있어 **변화가 큰** 출력이 나온다. 성능 차이는 없고 **결과의 성격만** 다르다 |
| **`SDE`** | Multistep 보다 적은 스텝으로 생성하지만 각 스텝이 모델을 2번 추론해 **2배 느리다.** 같은 시간이면 Multistep 이 낫다 |
| **`Karras`** | **Karras 노이즈 스케줄.** 같은 스텝에서 더 높은 품질(~50스텝 구간에서 사실) |
| `gpu` | 노이즈를 GPU 에서 생성 (CPU 노이즈와 시드 결과가 달라진다) |
| `cfg_pp` | **CFG++**. CFG 를 1~2.5 같은 **낮은 값**으로 쓰는 게 정상이다 |

읽기 연습 —

```text
dpmpp_2m_sde_gpu   =  DPM++ / 2차 / Multistep / SDE / GPU 노이즈
                      → ANIMA 공식이 "er_sde 와 비슷하지만 더 창의적" 이라고 소개하는 샘플러

euler_ancestral    =  Euler / Ancestral   (= A1111 의 "Euler a")
euler_cfg_pp       =  Euler / CFG++       (CFG 1.5~2.5 로 쓴다)
```

> `Karras` 가 붙은 것은 **손 타율이 안 좋다**는 체감 보고가 2023년에 있었다.
> 원글쓴이는 Karras 가 노이즈 스케줄링을 건드리니 영향이 있을 수는 있지만
> **어지간하면 기분 탓**이라고 답했다.

샘플러가 왜 여러 개인지도 한 줄로 —
디퓨전(DDPM)은 원래 **1000번을 반복**해야 이미지가 나오는데,
DDIM 이 x번씩 건너뛰어 `1000/x` 번 만에 **근사**한다.
**그 근사 방법의 차이가 곧 샘플러의 차이**다.


<small>근거 — [Anima 찍먹해보기 - 이미지생성 26.05](https://arca.live/b/aiart/171031030) · [샘플러에 대해 알아보자. 23.02](https://arca.live/b/aiart/69343204) · [DPM++ 종류 23.02](https://arca.live/b/aiart/69388839)</small>

## WAN 2.2 — High/Low 분리가 표준
<small>2026-04 기준 · 근거 6건</small>

**High/Low 모델을 나눠 쓰고 lightx2v(라이트닝) 로라를 별도로 물리는 것**이 표준 구성이다 (5건).
그냥 쓰면 느리고 품질도 나쁘다.

라이트닝·디스틸 로라가 **이미 병합된** 모델이라면 **cfg 1, 4~6스텝**으로 돌린다 (3건).

실측값은 [비디오 생성](video-generation.md) 참조.

<small>근거 — [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.… 26.01](https://arca.live/b/aiart/160657113) · [개빠른데 품질도 좋은 WAN 2.2 워크플로우 (VRAM 1… 26.01](https://arca.live/b/aiart/160633807) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750)</small>

??? note "근거 6건 전부 보기"
    [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.… 26.01](https://arca.live/b/aiart/160657113) · [개빠른데 품질도 좋은 WAN 2.2 워크플로우 (VRAM 1… 26.01](https://arca.live/b/aiart/160633807) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750) · ["버니니 다시왔네" 제작법 및 초간단 후기 (역양자화 파이선… 26.07](https://arca.live/b/aiart/175630790) · [어쩌다 찾은 svi 워크플로우 26.03](https://arca.live/b/aiart/164696140)

## MiniMax H3 가속 — 2026년 8월 기준
<small>2026-08 기준 · 근거 16건</small>

**이 절은 유효기간이 짧다.** 아래 합의가 만들어지는 데 며칠밖에 안 걸렸다.

| 합의 | 근거 |
|---|---|
| 가속은 **MiniMaxH3 Cache** 가 사실상 표준. TeaCache 계열로 스텝을 건너뛰는 게 아니라 계산 결과를 재사용해서 EasyCache·Spectrum보다 품질 손실이 적다 | 4건 |
| **int8convrot** 양자화가 fp8 tensorwise보다 품질이 좋고(Q8_0급) 조금 빠르며 캘리브레이션이 필요 없어 대세 | 4건 |
| **RTX 3060 12GB + RAM 32GB** 급에서도 구동된다 | 4건 |
| 최속은 **Cache + Mem Eff Sage Attention Patch + Patch Sage Attention KJ** 3종. 309.58초 → 94.73초 | 2건 |
| `MiniMaxH3*` 노드는 ComfyUI **0.30.0 이상에 내장**, `MiniMaxH3Cache` 만 git으로 별도 설치 | 3건 |
| Mem Eff Sage Patch·Patch Sage KJ는 **KJNodes 소속**이며 **Nightly** 를 지정해야 나타난다 | 2건 |
| **Spectrum Apply는 Cache·EasyCache와 같이 쓸 수 없다** | 3건 |
| 터보 LoRA는 Cache와 **원리가 겹쳐 병용 불가**. 품질은 Cache 쪽이 낫다 | 4건 |

자세한 것은 [MiniMax H3](minimax-h3.md) 참조.

<small>근거 — [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112) · [MiniMax H3 가속 노드 별 속도 후기 26.08](https://arca.live/b/aiart/179038650) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541)</small>

??? note "근거 16건 전부 보기"
    [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112) · [MiniMax H3 가속 노드 별 속도 후기 26.08](https://arca.live/b/aiart/179038650) · [MiniMax H3 int8convrot Video VAE … 26.08](https://arca.live/b/aiart/179114541) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [ComfyOrg 공식모델들에 int8convrot 추가됨 26.07](https://arca.live/b/aiart/175519662) · [MiniMax-H3 오픈웨이트 모델의 출시일이 공개 26.07](https://arca.live/b/aiart/178585330) · [ComfyUI-MiniMaxH3-Cache 노드 진짜 보배네. 26.08](https://arca.live/b/aiart/179044166) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [lightx2v minimax fl2v 터보로라 공개 (v0… 26.08](https://arca.live/b/aiart/179258094) · [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179083162) · [간단한 미니맥스(MiniMax) 워크플로우 공유 26.08](https://arca.live/b/aiart/178942263) · [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부… 26.08](https://arca.live/b/aiart/178717529) · [MiniMax H3 스펙트럼 노드 적용 방법 26.08](https://arca.live/b/aiart/178930365) · [GPT PRO가 맨든 미니맥스 고속노드 26.08](https://arca.live/b/aiart/179254885)

## LTX 2.3
<small>2026-06 기준 · 근거 10건</small>

- **2D·애니메이션이 약하다.** 아니메 LoRA를 물리거나 프롬프트에 스타일을 명시해야 한다 (3건)
- distilled 8스텝은 **cfg 1.0 고정**, 품질은 시그마·스케줄러(`linear_quadratic`)로 조절 (3건)
- 비디오용·오디오용 **VAE 두 개**와 듀얼 클립(`gemma3-12B-it` + `ltx-2.3_text_projection`)이 필요 (2건)
- **`dynamic_vram` 은 영상에서 반드시 켠다.** RAM 사용이 약 80GB → 10~15GB로 준다.
  반대로 **이미지 생성에서는 끄는 편이 낫다** (2건)

<small>근거 — [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112) · [LTX 2.3 워크플로우 공유 26.06](https://arca.live/b/aiart/172797485) · [오픈소스 무검열 비디오 생성 모델 Sulphur 2 배포!!… 26.05](https://arca.live/b/aiart/169565904) · [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750)</small>

??? note "근거 10건 전부 보기"
    [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들 26.08](https://arca.live/b/aiart/179458112) · [LTX 2.3 워크플로우 공유 26.06](https://arca.live/b/aiart/172797485) · [오픈소스 무검열 비디오 생성 모델 Sulphur 2 배포!!… 26.05](https://arca.live/b/aiart/169565904) · [(ComfyUI) 복잡한 시그마를 초보자도 쉽게 요리해 보자. 26.03](https://arca.live/b/aiart/165103750) · [오픈소스 무검열 비디오 생성 모델 Sulphur 2 발표 26.05](https://arca.live/b/aiart/169384763) · [(ComfyUI) LTX-2.3 커스텀 시그마로 영상과 음질… 26.03](https://arca.live/b/aiart/165196910) · [LTX I2V + FLF2V 추가 테스트 26.03](https://arca.live/b/aiart/164076209) · [LTX2.3 멀티모달 옵션 설명 26.04](https://arca.live/b/aiart/166755710) · [(워크플로) LTX2.3 Distilled Simple + … 26.03](https://arca.live/b/aiart/164232718) · [LTX2.3 아니메 미세팁 26.03](https://arca.live/b/aiart/164305753)

## 여러 곳에서 반복되는 것
<small>2026-08 기준 · 근거 16건</small>

| | 근거 |
|---|---|
| 워크플로우는 **EXIF가 든 이미지·영상**을 받아 ComfyUI 창에 드래그앤드롭해서 불러온다 | 5건 |
| VFI(프레임 보간) rife 모델은 **`models/frame_interpolation`** 폴더에 넣어야 인식된다 (`vfi`·`rife` 폴더 아님) | 3건 |
| **ComfyUI Manager로 업데이트하면 코어(내장 노드) 변경이 반영되지 않는다.** 본체는 git 또는 `update_comfyui.bat` | 2건 |
| 긴 영상은 통짜로 만들면 타이밍과 두 번째 상황을 제대로 못 그린다. **프롬프트를 나눠 이어붙인다** | 4건 |
| 채널에 올라오는 **신규 모델 소식의 상당수는 제작사 주장·유출·LLM 요약**이라 실사용 검증이 없다 | 5건 |

<small>근거 — [간단한 MinimaxH3 레퍼런스 I2V 워크플로우 공유 26.08](https://arca.live/b/aiart/179460713) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [1분 넘는 영상을 고속으로 뽑는 Helios 모델 출시 26.03](https://arca.live/b/aiart/163968817)</small>

??? note "근거 16건 전부 보기"
    [간단한 MinimaxH3 레퍼런스 I2V 워크플로우 공유 26.08](https://arca.live/b/aiart/179460713) · [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법 26.04](https://arca.live/b/aiart/167528900) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [1분 넘는 영상을 고속으로 뽑는 Helios 모델 출시 26.03](https://arca.live/b/aiart/163968817) · [SCAIL-2 RV2V 편의성 패치 워크플로우 26.06](https://arca.live/b/aiart/173906280) · [알리바바에서 딸내미 하나 샀음 (happy horse 1.0… 26.04](https://arca.live/b/aiart/169030124) · [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minima… 26.07](https://arca.live/b/aiart/178537097) · [ComfyUI SAM3 / RIFE 자체 지원 노드 추가 26.04](https://arca.live/b/aiart/168617494) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [Comfy 자동프롬프트 + 영상연결 딸깍 워크 플로우 - 가… 26.02](https://arca.live/b/aiart/163169341) · [WAN2.2 SVI 결과에 음성 추가용 WAN2.2 (SVI… 26.06](https://arca.live/b/aiart/173733176) · [(오픈소스 아님 확정) 새로운 SOTA급 T2V/I2V 모델… 26.04](https://arca.live/b/aiart/167106042) · [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179083162) · [간단한 미니맥스(MiniMax) 워크플로우 공유 26.08](https://arca.live/b/aiart/178942263) · [wan 2.2 프롬프트 릴레이 (kijai 아재가 작업 중) 26.04](https://arca.live/b/aiart/168139926) · [Google의 Veo 3.2 유출 26.02](https://arca.live/b/aiart/163312367)

## ⚠️ 뒤집힌 것들
<small>2026-08 기준 · 근거 10건 · 자료 엇갈림</small>

**국룰은 고정된 게 아니다.** 실제로 뒤집힌 사례들이다. 옛 글을 읽을 때 주의할 것.

| 지금 | ← 예전 | 언제 |
|---|---|---|
| 통합팩은 **0.31.0 판** | 0.11.1 권장 / 0.15.1은 충돌 잦아 비권장 | 2026-02 → 2026-08 |
| easycache는 **PR #12231로 수정됨** (nightly 필요) | easycache는 LTX2에서 동작하지 않는다 | — |
| **MiniMaxH3 Cache가 표준**, Spectrum은 충돌 대상 | Spectrum Apply로 30% 단축 | **2026-08-04 → 08-05** |
| Seedance는 **dreamina.capcut.com** | 2/24 글로벌 출시 예정, 중국 계정 필요 | 2026-02 |

세 번째를 보라. **하루 만에 뒤집혔다.** 8월 4일에 "Spectrum으로 30% 단축"이 올라왔고,
8월 5일에 더 나은 Cache가 등장하면서 Spectrum은 권장이 아니라 **충돌 대상**이 됐다.
이 분야의 정보 수명이 이 정도다.

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Seedance 2.0 26.02](https://arca.live/b/aiart/162007977) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [MiniMax H3 가속 노드 별 속도 후기 26.08](https://arca.live/b/aiart/179038650)</small>

??? note "근거 10건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Seedance 2.0 26.02](https://arca.live/b/aiart/162007977) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [MiniMax H3 가속 노드 별 속도 후기 26.08](https://arca.live/b/aiart/179038650) · [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯 26.08](https://arca.live/b/aiart/178949797) · [Seedance 2.0 프리미엄 맴버십 효율 26.02](https://arca.live/b/aiart/162514113) · [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유 26.08](https://arca.live/b/aiart/179083162) · [I2V CacheDit 테스트 - LTX 2 (Qwen, W… 26.02](https://arca.live/b/aiart/161698458) · [MiniMax H3 스펙트럼 노드 적용 방법 26.08](https://arca.live/b/aiart/178930365) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848)

## 아직 갈리는 것
<small>2026-08 기준 · 근거 13건 · **근거 약함** · 자료 엇갈림</small>

**sage attention이 10~15% 빠르다** — 찬성 8 / 반대 1
반대 근거: LTX2.3에서는 it/s만 11% 오를 뿐 실제 생성시간 차이는 크지 않다.
→ SDXL·t2i에서는 합의, **비디오 distilled 모델에서는 이견**.

**부작용**: sage를 켜면 **손가락 찐빠(손 왜곡)가 늘어난다**는 보고가 있다 (3건).

**터보 LoRA** — 찬성 2 / 반대 4
"25스텝 30분 → 4스텝 4분"은 속도만 보면 사실이다. 그러나 Cache와 병용이 안 되고
품질이 떨어져서, Cache를 이미 쓰고 있다면 **실사용에서는 Cache가 우세**하다는 게 다수 의견이다.

**portable 0.31.0** — 찬성 1 / 반대 1
라데온 ROCm sage 빌드 쪽에서는 "0.31.0은 버그로 안 되고 0.30.0에서만 동작"이라는 반례가 있다.

<small>근거 — [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039)</small>

??? note "근거 13건 전부 보기"
    [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [comfyui portable v0.11.1 + sage +… 26.02](https://arca.live/b/aiart/161206430) · [(워크플로) LTX2.3 Distilled Simple + … 26.03](https://arca.live/b/aiart/164232718) · [lightx2v minimax fl2v 터보로라 공개 (v0… 26.08](https://arca.live/b/aiart/179258094) · [comfyui portable v0.15.1 + sage +… 26.02](https://arca.live/b/aiart/163592169) · [미니맥스 H3 터보로라 나온듯? 26.08](https://arca.live/b/aiart/179094410) · [1시간전에 올라온 H3 고속 로라 테스트 26.08](https://arca.live/b/aiart/179280493) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848)

## 남의 그림 설정 알아내기 — 채널의 표준 3법
<small>2026-04 기준 · 근거 4건</small>

*'이 그림 어떻게 뽑아요'* 에 대한 채널의 답은 4년째 같다. **묻기 전에 EXIF 부터 열어 본다.**

### ① 브라우저에서 바로 — EXIF 뷰어 유저스크립트

아카라이브·픽시브에 올라온 AI 그림을 **클릭만 하면** 생성 정보를 팝업으로 보여 준다. greasyfork 에서 받아 Tampermonkey/Violentmonkey 에 설치한다.

| | |
|---|---|
| 지원 생성기 | NovelAI, Stable Diffusion web UI, InvokeAI |
| 지원 확장자 | png / jpeg / webp (**로딩 속도는 png=jpeg ≫ webp**) |
| 동작 사이트 | AI그림채널·AI그림학습채널·AI반실사그림채널·AI실사채널·픽시브 |
| 부가 기능 | CIVITAI 모델 해시 검색 버튼, `Infer`(쓴 기술을 추론 — T2I/I2I/Hires.fix/LoRa/Hypernet/ControlNet/…), WD 1.4 Tagger·DeepDanbooru 연동, 오프라인 이미지 드래그앤드롭 |

**픽시브는 png 만** 확인된다 — jpg 로 올라간 것은 메타데이터가 지워진다.

### ② 로컬 파일이면 — EXIF-II 프로그램

Windows 10/11 전용 자작 프로그램. 로컬 이미지와 웹 URL 둘 다 드래그앤드롭으로 조회한다. 모델·해시 추적 검색, `.TXT` 추출, **PNG→JPG 변환 시 메타데이터 복제 보존**, EXIF 전체 삭제, **NAI 숨겨진 정보(PNG·WebP 스텔스) 탐색**을 지원한다.

**탐지 불가 조건** — 원본 메타데이터 삭제, 개인 암호화, 규칙 직접 수정, RGBA 의 A 채널 삭제, JPG/JPEG 로 변환.
**백신 오탐** — `Trojan:Script/Wacatac.B!ml` 로 잡히므로 폴더와 파일을 화이트리스트에 넣어야 한다. 관리자 권한으로 설치하면 드래그앤드롭이 안 되니 무설치 파일을 쓴다.

### ③ 이미 로컬 도구가 있으면 — `PNG Info` 탭

WebUI·Forge 계열에 기본으로 있다. 남이 올린 png 를 떨어뜨리면 프롬프트·시드·모델이 나온다.

### 메타데이터가 아예 없다면 — `Tagger`

여기서부터는 '알아내기' 가 아니라 '추측' 이다. 이미지를 보고 태그를 뽑아 주는 것이므로 실제 값이 아니다. 둘의 차이는 [용어집](glossary.md)에 있다.

---

### 반대쪽 국룰 — 올릴 때 EXIF 를 살려라

**ComfyUI 워크플로우가 담긴 png 는 메타데이터를 유지한 채 올려야** 상대방이 드래그앤드롭으로 열 수 있다. 아카라이브에 그냥 올리면 업로드 과정에서 날아가므로 **EXIF 보존 옵션(또는 EXIF 보존 유저스크립트)을 켜고** 올린다. 워크플로우가 안 열린다는 신고의 첫 번째 원인이 이것이다.

질문할 때 **생성된 그림을 EXIF 포함해서** 올리라는 채널 규정도 같은 이유다.

<small>근거 — [최근 연달아 업데이트 한 EXIF 뷰어 기능 소개함 23.03](https://arca.live/b/aiart/70916246) · [(제작) Exif AI 프롬 확인 프로그램 :: v2.3.4… 23.08](https://arca.live/b/aiart/83667711) · [Forge neo 에서 돌아가는 tagger 찾음 26.04](https://arca.live/b/aiart/168352863) · [뉴비의 간단한 워크 플로우 26.02](https://arca.live/b/aiart/161471075)</small>

## ⚠️ LLM(GPT·제미나이)에게 물으면 안 되는 이유
<small>2026-08 기준 · 근거 3건 · 자료 엇갈림</small>

**이 채널에서 LLM 이 틀리는 방식은 일정하다 — 문법·수치·모델 이름을 자신 있게 답하는데, 그 답이 몇 세대 전 것이다.**
세 건의 질문글에서 같은 패턴이 그대로 반복됐고, **세 번 모두 댓글이 바로잡았으며 원글쓴이가 수긍했다.**

| 물어본 것 | LLM 의 답 | 실제 | 결말 |
|---|---|---|---|
| 캐릭터 LoRA 에 몇 장이 필요한가 (GPT, 2026-08) | *"최소 30장, 평균 50장"* | 단순한 디자인이면 **1장**으로도 되고, 데이터가 더 필요한 **ILXL 계열도 깔끔한 자료면 20장이면 끝난다** | 원글쓴이가 **"할루시네이션에 또 당했다"** 며 수긍 |
| 그림을 움짤로 만들려면 (제미나이, 2026-08) | AnimateDiff 모션 모델 `v3_sd15_mm.ckpt` / `mm_sd_v15_v2.ckpt` | AnimateDiff 는 **아주 초기 영상 모델이라 지금은 아무도 쓰지 않는다.** I2V 는 **MiniMax H3**(그 전이 WAN 2.2 · LTX 2.3) | 댓글이 정정, ComfyUI 템플릿의 `minimax h3 i2v` 로 안내 |
| WebUI 가중치 문법 (제미나이, 2026-06) | `3::excessive cum::` — 즉 `가중치::태그::` | 그건 **NAI 전용 문법이고 WebUI 에서는 통째로 안 먹는다.** 20개 가까운 태그의 가중치가 전부 무효였다 | 댓글이 WebUI 문법을 다시 알려 줌 |

**WebUI(A1111·Forge·reForge) 가중치 문법 — 위 사례에서 다시 정리된 것**

```text
(태그)        = 1.1 배
[태그]        = 1.1 배 감소
((태그))      = 1.1 × 1.1 = 1.21 배
(태그:1.4)    = 1.4 배
상한          아무리 높게 줘도 1.5 정도까지가 최선
퀄리티 태그   masterpiece 같은 것에는 가중치를 주지 말 것
```

### 왜 이렇게 되나

**이 분야는 반년이면 세대가 바뀌는데 LLM 의 지식은 학습 시점에 얼어 있다.**
이 문서의 "⚠️ 뒤집힌 것들" 항목을 보라 — 채널 안에서도 **하루 만에** 권장이 충돌 대상으로 바뀐 사례가 있다.
게다가 LLM 은 모델별 문법(NAI 의 `::` 와 WebUI 의 `()`)을 뒤섞어 그럴듯한 한 덩어리로 만들어 낸다.
채널 압축공지도 같은 말을 한다 — *"GPT 같은 챗봇에게 물어보는 것도 방법이지만 **검증된 정보를 기대하지 말고**
그걸 사실인 양 채널에 옮기지도 말라."*

### 대신 무엇을 보나

| 순서 | 어디를 | 왜 |
|---|---|---|
| 1 | **채널 공지·압축공지** | 규정과 기본값이 갱신된 채로 있다 |
| 2 | **그림 탭 추천글의 EXIF** | 실제로 나온 그림에 붙어 있는 값이라 검증이 끝나 있다. 여는 방법은 이 문서의 "남의 그림 설정 알아내기" 항목 |
| 3 | **모델·워크플로우 배포글** | 제작자가 직접 적은 수치. 단 [모델 고르기](models.md)의 "모델 소식을 읽는 법" 을 함께 볼 것 |
| 4 | **이 위키** | 위 셋을 항목별로 정리해 둔 것 |

> **꼭 LLM 을 써야 한다면** — 제미나이에게 물을 때 *"최신 정보를 검색해서 응답하라"* 를 명시하면 그나마 낫다는
> 요령이 같은 글의 댓글에 있다. 그래도 **나온 답은 반드시 EXIF 나 배포글로 대조하라.**
> LLM 이 실제로 잘하는 일은 '문법을 알려 주는 것' 이 아니라 **이미 형식이 정해진 프롬프트를 살 붙여 확장하는 것**이다
> ([프롬프트 쓰는 법](prompting.md) 의 "LLM 에 프롬프트를 맡기기" 항목).

→ [프롬프트 쓰는 법](prompting.md) · [모델 고르기](models.md) · [비디오 생성](video-generation.md) · [로라 쓰는 법](lora-usage.md)

<small>근거 — [GPT를 이용해 아니마 캐릭터 로라 만드는건 처음인데 잘 되… 26.08](https://arca.live/b/aiart/178963807) · [로컬 ai 입문 3일차 뉴비 움짤을 만들고 싶은데.... 26.08](https://arca.live/b/aiart/179060623) · [4일차 뉴비 로컬 야짤 정액량 관련 질문 드립니다. 26.06](https://arca.live/b/aiart/173111055)</small>

## 프롬프트에서 하지 말 것 — 반복 확인된 표기 사고
<small>2026-06 기준 · 근거 7건</small>

실제 그림이 안 나온 원인이 **프롬프트 표기 자체**였던 사례가 반복된다. 뽑기 전에 이것부터 확인한다.

| 하지 말 것 | 왜 | 근거 |
|---|---|---|
| **`no ~` 형 부정 태그를 긍정 프롬에 넣기** | 부정의 의미는 사라지고 핵심 단어만 남아 **오히려 그 현상을 부른다.** `no heterochromia` 는 단부루에 있는데도 SDXL·ANIMA 어느 쪽도 학습이 안 돼 `heterochromia` 의 유의어처럼 작동했다 | 2026-05 |
| **계열이 다른 품질 태그 옮겨 쓰기** | `score_9_up` · `score_8_up` · `score_7_up` 은 **Pony 전용**이라 WAI Illustrious 에서는 무효 토큰이고 자리만 먹는다 | 2026-05 |
| **괄호 없이 가중치 쓰기** | `blurry:1.5` · `fellatio:1.3` 은 **가중치로 작동하지 않고** 콜론과 숫자가 텍스트로 들어간다. NAI 쪽은 `::내용::` 처럼 **앞 숫자를 빠뜨리면** 강조가 안 걸린다 | 2026-05 · 2026-06 |
| **수식어를 붙여 태그를 만들어 내기** | 학습된 태그가 아니라 **수식이 버려지고 원 태그만 남는다.** 같은 뜻을 여러 번 쌓으면 실제 태그의 비중만 희석된다 | 2026-05 · 2026-06 |
| **안 된다고 가중치만 올리기** | **올려도 아무 일이 일어나지 않는 태그가 있다.** `submerged` 는 6·8·10 까지 올려도 변화가 없었다 | 2026-05 |

```text
막혔을 때의 순서
  ① 그 태그가 단부루/e621 에 실제로 있는지, 게시물 수가 몇인지 본다
  ② 없으면 그 상태를 가리키는 전용 태그를 찾는다  (condom belt · super highleg · reverse fellatio)
  ③ 그래도 없으면 태그를 더 쌓지 말고 빼거나 앵글을 바꾼다
```

전체 목록은 [프롬프트 쓰는 법](prompting.md) 의 **「⚠ 폐기·오작동 태그와 즉석 조합」** 절에 있다.

<small>근거 — [계속 오드아이만 나오는데 해결 방법 있나 26.05](https://arca.live/b/aiart/172340770) · [이 사진처럼 뿌연 처리가 잘 안나오는데 도움 26.05](https://arca.live/b/aiart/171363238) · [콘돔 관련 몇가지 질문 드립니다. 26.05](https://arca.live/b/aiart/171151416) · [가슴 때리는 태그 어떻게 짬? 26.05](https://arca.live/b/aiart/172118644)</small>

??? note "근거 7건 전부 보기"
    [계속 오드아이만 나오는데 해결 방법 있나 26.05](https://arca.live/b/aiart/172340770) · [이 사진처럼 뿌연 처리가 잘 안나오는데 도움 26.05](https://arca.live/b/aiart/171363238) · [콘돔 관련 몇가지 질문 드립니다. 26.05](https://arca.live/b/aiart/171151416) · [가슴 때리는 태그 어떻게 짬? 26.05](https://arca.live/b/aiart/172118644) · [늘어난 유두 프롬프트 질문 26.06](https://arca.live/b/aiart/172547260) · [(보추주의) Nai 바닥딸 태그 없숨? 26.06](https://arca.live/b/aiart/172731925) · [NAI)혹시 물 속에 있는 느낌 어떻게 냄? 26.05](https://arca.live/b/aiart/172077937)

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 112개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 워크플로우는 EXIF 가 든 이미지·영상 파일을 다운로드해 ComfyUI 창에 드래그앤드롭해 불러온다 | 11 | 0 | 2024-06~2026-08 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| 수식어를 앞에 붙여 만든 즉석 조합 태그는 학습된 태그가 아니어서 수식이 버려지고 원 태그만 남는다 — 같은 뜻의 어구를 여러 개 쌓아도 효과는 더해지지 않고 실제로 작동하는 태그의 비중만 희석된다 | 7 | 0 | 2026-02~2026-06 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| LTX 계열은 2D·애니메이션이 약해 아니메 LoRA 를 물리거나 프롬프트에 스타일을 명시해야 한다 | 6 | 0 | 2026-03~2026-08 |
| ANIMA 의 작가 태그는 반드시 `@` 로 시작한다 — 작가 태그가 `abcd efg` 이면 `@abcd efg` 로 쓰고 (단부루 표기가 `aaaaa_bbb` 이면 `@aaaaa bbb`), `@` 를 안 붙이면 태그 효과가 미미하다 | 6 | 0 | 2026-02~2026-05 |
| 긴 영상은 통짜로 만들면 타이밍과 두 번째 상황을 제대로 못 그리므로, 프롬프트를 나눠 이어붙이는 편이 낫다 | 6 | 0 | 2026-02~2026-08 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| WAN 2.2 계열 워크플로우는 High/Low 모델을 나눠 쓰고 lightx2v(라이트닝) 로라를 별도로 물리는 것이 표준 구성이다 | 5 | 0 | 2026-01~2026-04 |
| 채널에 올라오는 신규 모델 소식의 상당수는 제작사 주장·유출·LLM 요약이라 실사용 검증이 없다 | 5 | 0 | 2026-02~2026-07 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| NAI 에서만 되는 음수 가중치 활용법 — 제거는 `-1::hat ::`, 색상 반전·추가는 `-1::monochrome ::`, 디테일 추가는 `-3::simple illustration ::` 이다 | 5 | 0 | 2025-06~2026-08 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| ANIMA 의 공식 지원 해상도는 512x512(NAI1) ~ 1024x1024(SDXL) ~ 1536x1536(ILXL1) 버킷이고, 공식·입문 자료는 SDXL 해상도(1024급, 세로 832x1216)를 무난한 기본값으로 권한다 | 5 | 0 | 2026-01~2026-05 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| ANIMA 전용으로 학습된 LoRA 는 정상 동작한다 — 캐릭터 LoRA(강도 1), 터보 로라, 디테일러 로라가 실제로 쓰인다. 호환되지 않는 것은 SDXL(Illustrious·NoobAI)용 LoRA·임베딩·컨트롤넷이다 | 4 | 0 | 2026-05~2026-07 |
| SDXL/Illustrious 결과물이 탁하거나 흰 점이 찍히면 VAE Select 값을 2로 두어 별도 VAE(fixFP16ErrorsSDXLLowerMemoryUse_v10)를 적용한다 | 4 | 0 | 2026-06~2026-08 |
| ComfyUI 포터블에서 파이썬 패키지를 깔 때는 시스템 파이썬이 아니라 `python_embeded\python.exe -m pip` 로 설치해야 한다 | 4 | 0 | 2026-01~2026-08 |
| int8convrot 양자화는 fp8 tensorwise 보다 품질이 좋고(Q8_0 급) 조금 빠르며, 캘리브레이션이 필요 없어 대세가 된다 | 4 | 0 | 2026-07~2026-08 |
| 통합팩은 ComfyUI 본체를 업데이트하지 말고 새 버전이 나오면 처음부터 새로 받아야 한다 | 4 | 0 | 2026-05~2026-08 |
| SDXL 시대에 DPM++ 권장이 뒤집혔다 — Illustrious·NoobAI 는 `Euler`·`Euler A`, ANIMA 는 `er_sde` 계열을 쓴다. | 4 | 0 | 2023-02~2026-05 |
| 설정 > Comfy > Nodes 2.0 > 모던 노드 디자인을 켜면 워크플로우 배열이 깨지고 일부 커스텀 노드가 오작동한다 | 4 | 0 | 2026-05~2026-08 |
| NAI 의 가중치 문법은 `weight::tag ::` 이고 닫는 `::` 앞에 공백이 필수다 — `tag::` 는 틀리고 `tag ::` 가 맞다. 로컬(A1111·ComfyUI)은 `(tag:weight)` 로 다르다 | 4 | 2 | 2025-06~2026-07 |
| MiniMax H3 는 RTX 3060 12GB + RAM 32GB 급 환경에서도 구동된다 | 4 | 0 | 2026-07~2026-08 |
| MiniMax H3 가속은 MiniMaxH3 Cache(TeaCache 계열, 스텝 스킵이 아니라 계산 결과 재사용)가 EasyCache·Spectrum 보다 품질 손실이 적어 사실상 표준이다 | 4 | 0 | 2026-08~2026-08 |
| ANIMA 의 가중치 문법은 ComfyUI 에서 SDXL 과 같은 `(tag:weight)` 이지만 cross attention 구조상 SDXL 보다 훨씬 높은 값이 필요해 `(chibi:2)` 처럼 :2 정도에서 시작하며, 4 이상을 남발하면 연산이 깨져 검은 화면이 나올 수 있다 | 4 | 0 | 2026-05~2026-07 |
| 모델이 diffusion model 단독으로 배포되면 models/checkpoints 가 아니라 models/diffusion_models 에 넣고 Load Diffusion Model 계열 노드로 불러야 하며, 텍스트 인코더와 VAE 도 각각 models/text_encoders, models/vae 에 따로 넣어 연결해야 한다 | 4 | 0 | 2026-05~2026-08 |
| MiniMax H3 터보 LoRA 는 H3-Cache 와 원리가 겹쳐 함께 쓰면 결과물이 망가지며, 품질은 Cache 쪽이 낫다 | 4 | 0 | 2026-08~2026-08 |
| 뉴비가 공유받은 워크플로우에서 오류가 터지는 범인 1위는 sage-attention 이다 | 3 | 0 | 2026-05~2026-08 |
| 커스텀 시그마(그래프 편집)로 노이즈 스케줄을 직접 조절하면 결과가 훨씬 역동적이 되지만 품질이 극적으로 좋아지지는 않는다 | 3 | 0 | 2026-03~2026-03 |
| VFI(프레임 보간) rife 모델은 ComfyUI/models/frame_interpolation 폴더에 넣어야 인식된다 | 3 | 0 | 2026-04~2026-08 |
| ANIMA 의 퀄리티 태그는 두 계통이다 — 사람 좋아요/싫어요 기준 `masterpiece, best quality, good quality, normal quality, low quality, worst quality` 와 PonyV7 품질 판정 AI 기준 `score_1`(최하)~`score_9`(최상)이며, 둘 다 써도 되고 하나만 쓰거나 안 써도 동작한다 | 3 | 0 | 2026-02~2026-05 |
| ComfyUI 통합팩은 한글이 없는 경로에 압축을 풀어야 한다 | 3 | 0 | 2026-02~2026-08 |
| AI 그림의 모델·문법·수치는 GPT·제미나이 같은 LLM 에 묻지 말아야 한다 — 학습 시점이 낡아 몇 세대 전 정보를 자신 있게 답한다. 실제 사례 셋: GPT 는 캐릭터 LoRA 데이터가 '최소 30장, 평균 50장' 필요하다고 했으나 단순한 디자인이면 1장, 데이터가 더 필요한 ILXL 도 깔끔한 자료면 20장이면 끝났다. 제미나이는 움짤 입문용으로 AnimateDiff(`v3_sd15_mm.ckpt` / `mm_sd_v15_v2.ckpt`)를 추천했으나 지금은 아무도 쓰지 않고 I2V 는 MiniMax H3 다. 제미나이가 알려 준 NAI 전용 가중치 문법 `가중치::태그::` 는 WebUI 에서 통째로 동작하지 않았다. 대신 채널 공지·배포글·EXIF 를 공유하는 그림 탭 추천글을 보라 | 3 | 0 | 2026-06~2026-08 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [최근 연달아 업데이트 한 EXIF 뷰어 기능 소개함](https://arca.live/b/aiart/70916246) — 2023-03, 추천 63
- [NoobAI-XL user Manual(24.12.25 버전)](https://arca.live/b/aiart/124830494) — 2024-12, 추천 49
- [ILXL 프롬프트 가이드](https://arca.live/b/aiart/118111192) — 2024-10, 추천 47
- [Comfyui portable v0.30.0 + sage 외 여러가지.](https://arca.live/b/aiart/178800540) — 2026-08, 추천 47
- [FLF2V 업데이트 : 정말 빠른데 품질도 좋은 WAN 2.2 워크플로우](https://arca.live/b/aiart/160657113) — 2026-01, 추천 46
- [개빠른데 품질도 좋은 WAN 2.2 워크플로우 (VRAM 12GB 이상 권장)](https://arca.live/b/aiart/160633807) — 2026-01, 추천 45
- [Seedance 2.0](https://arca.live/b/aiart/162007977) — 2026-02, 추천 44
- [Anima 찍먹해보기 - 이미지생성](https://arca.live/b/aiart/171031030) — 2026-05, 추천 44
- [뉴비들은 webui neo 쓰자](https://arca.live/b/aiart/176802949) — 2026-07, 추천 44
- [ComfyUI에서 MiniMax H3 구동 시 확인할 사항들](https://arca.live/b/aiart/179458112) — 2026-08, 추천 44
- [NlxlMix - Noob 1.1 eps + Illustrious 1.0 기반 병합 모델](https://arca.live/b/aiart/130197990) — 2025-03, 추천 43
- [Comfyui portable v0.22.0 + sage + triton.](https://arca.live/b/aiart/171586136) — 2026-05, 추천 41
- [내용 추가2/잘못된 내용 수정]4.5f) 추가적으로 알아낸 것들, 가이던스 6~8 은 과용이다](https://arca.live/b/aiart/138557595) — 2025-06, 추천 40
- [샘플러에 대해 알아보자.](https://arca.live/b/aiart/69343204) — 2023-02, 추천 38
- [Comfyui portable v0.31.0 + sage 외 여러가지.](https://arca.live/b/aiart/179342860) — 2026-08, 추천 38
- [간단한 MinimaxH3 레퍼런스 I2V 워크플로우 공유](https://arca.live/b/aiart/179460713) — 2026-08, 추천 38
- [DPM++ 종류](https://arca.live/b/aiart/69388839) — 2023-02, 추천 37
- [comfyui portable v0.20.1 + sage + triton.](https://arca.live/b/aiart/169293039) — 2026-04, 추천 36
- [WAN2.2 통합 워크플로우 - 설치 및 기초 사용법](https://arca.live/b/aiart/167528900) — 2026-04, 추천 35
- [MiniMax H3 가속 노드 별 속도 후기](https://arca.live/b/aiart/179038650) — 2026-08, 추천 35
- [MiniMax H3 int8convrot Video VAE 올라옴](https://arca.live/b/aiart/179114541) — 2026-08, 추천 34
- [NAI-XL 2dac / 2.5dac 색감 개선모델 (권장 세팅 추가)](https://arca.live/b/aiart/140191370) — 2025-06, 추천 33
- [LTX 2.3 워크플로우 공유](https://arca.live/b/aiart/172797485) — 2026-06, 추천 32
- [Comfyui portable v0.26.0 + sage 외 여러가지](https://arca.live/b/aiart/175163102) — 2026-06, 추천 32
- [[ComfyUI] 복잡한 시그마를 초보자도 쉽게 요리해 보자.](https://arca.live/b/aiart/165103750) — 2026-03, 추천 30
- [오픈소스 무검열 비디오 생성 모델 Sulphur 2 배포!!!!!!!!](https://arca.live/b/aiart/169565904) — 2026-05, 추천 30
- [DaSiWa에서 만든 미니맥스 워크플로우 꽤 괜찮은듯](https://arca.live/b/aiart/178949797) — 2026-08, 추천 26
- [Comfyui portable v0.23.0 + sage + grok i2v 외 여러가지](https://arca.live/b/aiart/172596107) — 2026-06, 추천 25
- [Anima에서 사용할 수 있는 DMD2 LoRA](https://arca.live/b/aiart/164898297) — 2026-03, 추천 23
- [1분 넘는 영상을 고속으로 뽑는 Helios 모델 출시](https://arca.live/b/aiart/163968817) — 2026-03, 추천 22
- [SCAIL-2 RV2V 편의성 패치 워크플로우](https://arca.live/b/aiart/173906280) — 2026-06, 추천 22
- [[제작] Exif AI 프롬 확인 프로그램 :: v2.3.4 [메인]](https://arca.live/b/aiart/83667711) — 2023-08, 추천 21
- [오픈소스 무검열 비디오 생성 모델 Sulphur 2 발표](https://arca.live/b/aiart/169384763) — 2026-05, 추천 21
- [알리바바에서 딸내미 하나 샀음 (happy horse 1.0 출시)](https://arca.live/b/aiart/169030124) — 2026-04, 추천 20
- [comfyui portable v0.11.1 + sage + triton.](https://arca.live/b/aiart/161206430) — 2026-02, 추천 18
- [Seedance 2.0 프리미엄 맴버십 효율](https://arca.live/b/aiart/162514113) — 2026-02, 추천 18
- [[ComfyUI] LTX-2.3 커스텀 시그마로 영상과 음질을 개선해 보자.](https://arca.live/b/aiart/165196910) — 2026-03, 추천 18
- [ComfyUI SAM3 / RIFE 자체 지원 노드 추가](https://arca.live/b/aiart/168617494) — 2026-04, 추천 18
- [NAI 채널에 올리는 오픈웨이트 영상모델 소식 (Minimax H3)](https://arca.live/b/aiart/178537097) — 2026-07, 추천 18
- [ComfyOrg 공식모델들에 int8convrot 추가됨](https://arca.live/b/aiart/175519662) — 2026-07, 추천 17
- [MiniMax-H3 오픈웨이트 모델의 출시일이 공개](https://arca.live/b/aiart/178585330) — 2026-07, 추천 15
- [ComfyUI-MiniMaxH3-Cache 노드 진짜 보배네.](https://arca.live/b/aiart/179044166) — 2026-08, 추천 15
- [LTX I2V + FLF2V 추가 테스트](https://arca.live/b/aiart/164076209) — 2026-03, 추천 14
- [LTX2.3 멀티모달 옵션 설명](https://arca.live/b/aiart/166755710) — 2026-04, 추천 14
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [Comfy 자동프롬프트 + 영상연결 딸깍 워크 플로우 - 가챠용](https://arca.live/b/aiart/163169341) — 2026-02, 추천 13
- [(오픈소스 아님 확정) 새로운 SOTA급 T2V/I2V 모델 HappyHorse 출시예정](https://arca.live/b/aiart/167106042) — 2026-04, 추천 13
- [WAN2.2 SVI 결과에 음성 추가용 WAN2.2 (SVI) + LTX Worfkflow](https://arca.live/b/aiart/173733176) — 2026-06, 추천 13
- [comfyui portable v0.15.1 + sage + triton.](https://arca.live/b/aiart/163592169) — 2026-02, 추천 12
- [[워크플로] LTX2.3 Distilled Simple + 생성속도 간단 테스트](https://arca.live/b/aiart/164232718) — 2026-03, 추천 12
- [lightx2v minimax fl2v 터보로라 공개 (v0.1 프리뷰)](https://arca.live/b/aiart/179258094) — 2026-08, 추천 12
- [미니맥스(MiniMax) LLM 프롬프트 생성 워크플로우 공유](https://arca.live/b/aiart/179083162) — 2026-08, 추천 10
- [nvidia에서 cosmos3 출시했네.](https://arca.live/b/aiart/172423630) — 2026-06, 추천 9
- [MiniMax H3 ComfyUI 성능 관련 세부 정보 일부 공개](https://arca.live/b/aiart/178717529) — 2026-08, 추천 9
- [간단한 미니맥스(MiniMax) 워크플로우 공유](https://arca.live/b/aiart/178942263) — 2026-08, 추천 9
- [I2V CacheDit 테스트 - LTX 2 (Qwen, Wan, ZIT 등 사용가능)](https://arca.live/b/aiart/161698458) — 2026-02, 추천 8
- [LTX2.3 아니메 미세팁](https://arca.live/b/aiart/164305753) — 2026-03, 추천 8
- [GPT를 이용해 아니마 캐릭터 로라 만드는건 처음인데 잘 되려나...](https://arca.live/b/aiart/178963807) — 2026-08, 추천 8
- [wan 2.2 프롬프트 릴레이 (kijai 아재가 작업 중)](https://arca.live/b/aiart/168139926) — 2026-04, 추천 7
- ["버니니 다시왔네" 제작법 및 초간단 후기 (역양자화 파이선 스크립트 공유 - 링크7일만료)](https://arca.live/b/aiart/175630790) — 2026-07, 추천 7
- [재밌는 비디오 제네레이션 모델 나왔네.](https://arca.live/b/aiart/176717035) — 2026-07, 추천 7
- [MiniMax H3 스펙트럼 노드 적용 방법](https://arca.live/b/aiart/178930365) — 2026-08, 추천 7
- [Forge neo 에서 돌아가는 tagger 찾음](https://arca.live/b/aiart/168352863) — 2026-04, 추천 6
- [미니맥스 H3 터보로라 나온듯?](https://arca.live/b/aiart/179094410) — 2026-08, 추천 6
- [1시간전에 올라온 H3 고속 로라 테스트](https://arca.live/b/aiart/179280493) — 2026-08, 추천 6
- [Google의 Veo 3.2 유출](https://arca.live/b/aiart/163312367) — 2026-02, 추천 5
- [라데온 sageattention whl로 만들어왔어](https://arca.live/b/aiart/179413848) — 2026-08, 추천 5
- [GPT PRO가 맨든 미니맥스 고속노드](https://arca.live/b/aiart/179254885) — 2026-08, 추천 4
- [뉴비의 간단한 워크 플로우](https://arca.live/b/aiart/161471075) — 2026-02, 추천 0
- [어쩌다 찾은 svi 워크플로우](https://arca.live/b/aiart/164696140) — 2026-03, 추천 0
- [콘돔 관련 몇가지 질문 드립니다.](https://arca.live/b/aiart/171151416) — 2026-05, 추천 0
- [이 사진처럼 뿌연 처리가 잘 안나오는데 도움](https://arca.live/b/aiart/171363238) — 2026-05, 추천 0
- [NAI)혹시 물 속에 있는 느낌 어떻게 냄?](https://arca.live/b/aiart/172077937) — 2026-05, 추천 0
- [가슴 때리는 태그 어떻게 짬?](https://arca.live/b/aiart/172118644) — 2026-05, 추천 0
- [계속 오드아이만 나오는데 해결 방법 있나](https://arca.live/b/aiart/172340770) — 2026-05, 추천 0
- [늘어난 유두 프롬프트 질문](https://arca.live/b/aiart/172547260) — 2026-06, 추천 0
- [(보추주의) Nai 바닥딸 태그 없숨?](https://arca.live/b/aiart/172731925) — 2026-06, 추천 0
- [4일차 뉴비 로컬 야짤 정액량 관련 질문 드립니다.](https://arca.live/b/aiart/173111055) — 2026-06, 추천 0
- [로컬 ai 입문 3일차 뉴비 움짤을 만들고 싶은데....](https://arca.live/b/aiart/179060623) — 2026-08, 추천 0