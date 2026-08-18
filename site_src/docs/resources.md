# 자원 — 받는 곳 모음

> **원문 338건 → 이 문서 하나** · 주장 503개 · 정리 2026-08-14

**URL 을 그대로 실은 문서다.** 종류별로 묶고, 각 링크마다 뭐가 있는 곳인지 한 줄을 붙였다.
죽은 것으로 확인된 링크도 지우지 않고 **링크 죽음**으로 표시해 두었다 — 같은 것을 다시 찾아 헤매지 않기 위해서다.
어느 파일을 어느 폴더에 넣는지는 [설치와 환경 구성](install.md) 의 폴더 경로 표를 본다.

## 0. 먼저 알아 둘 것 — base64 링크와 기한 만료
<small>2026-06 기준 · 근거 7건</small>

채널에는 **배포 링크를 base64 로 인코딩해 올리는 관행**이 있다. 본문에 뜻 없는 영문+숫자 덩어리가 보이면 base64 디코더에 넣으면 실제 주소가 나온다.

```
aHR0cHM6Ly9raW8uYWMvYy8...   →  https://kio.ac/c/...
aHR0cHM6Ly9tZWdhLm56L2Zv... →  https://mega.nz/folder/...
```

그리고 **오래된 배포글은 링크가 죽어 있을 것을 전제**해야 한다. `kio.ac` 는 대개 **한 달**, 통합팩 배포는 **비번 `ai` / 기한 한 달**, 일부 스크립트는 7일·30일 만료다. 죽었으면 **댓글의 대체 링크**를 먼저 확인한다.

<small>근거 — [ai 뮤직 넌 미쳤다 @@추가 정보 있음 22.12](https://arca.live/b/aiart/64778052) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [한애니 캐릭터들 만든 로라 공유 26.03](https://arca.live/b/aiart/165664117) · [LTX2.3 lora 몇개 공유 26.06](https://arca.live/b/aiart/173653906)</small>

??? note "근거 7건 전부 보기"
    [ai 뮤직 넌 미쳤다 @@추가 정보 있음 22.12](https://arca.live/b/aiart/64778052) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [한애니 캐릭터들 만든 로라 공유 26.03](https://arca.live/b/aiart/165664117) · [LTX2.3 lora 몇개 공유 26.06](https://arca.live/b/aiart/173653906) · [크퀘스타일 도트 로라 공유 26.04](https://arca.live/b/aiart/167362821) · [트릭컬 스타일 로라 공유 26.05](https://arca.live/b/aiart/169478146) · [(Q6_K)Smooth Mix Wan I2V high+Low… 25.10](https://arca.live/b/aiart/151608989)

## 1. 모델 (체크포인트)
<small>2026-08 기준 · 근거 11건</small>

```
# ANIMA — 2026년 채널 기본 아니메 모델 (본체·텍스트인코더·VAE 3파일)
https://huggingface.co/circlestone-labs/Anima
https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors
https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors
https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors

# ANIMA — civitai 배포 (Base v1.0 / Aesthetic v1.1)
https://civitai.red/models/2458426

# ANIMA 양자화판 — VRAM 8GB 급이면 INT8
https://huggingface.co/Bedovyy/Anima-INT8        # 모델+인코더+VAE 합쳐 4GB 미만, 1.3배 이상 빠름
https://huggingface.co/sylvanian/anima-int8
https://huggingface.co/Bedovyy/Anima-GGUF        # Q8_0 이 마지노선, 그 아래는 유화처럼 뭉개짐
https://huggingface.co/Bedovyy/Anima-FP8

# SDXL/Illustrious 계열 기본 권장 체크포인트
https://civitai.red/models/827184/wai-illustrious-sdxl

# Illustrious 계열 추천 2종
https://civitai.com/models/1984400   # Animayhem Pale Rider — JANKU 보다 찐빠가 적다는 후기
https://civitai.com/models/2385399   # Akium Lumen Ill Base — 빛 표현 특화, 자체 VAE 라 CFG 를 높이면 붉어짐

# 참고용 (채널 평가가 갈리는 것)
https://huggingface.co/SeeSee21/Z-Anime          # Z-Image Base 6B 파인튜닝. 8GB 에서 돌지만 데이터셋 우려
https://huggingface.co/Laxhar/noobai-XL-1.1
https://huggingface.co/lodestones/Chroma1-HD     # 무검열 최고 성능이나 매우 느림
https://novelai.net/                             # 웹서비스

# 이미지 편집 모델 (그림을 새로 그리는 게 아니라 지시로 고치는 쪽)
https://huggingface.co/Qwen/Qwen-Image-Edit-2511
https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0          # 위를 SFT+DPO 로 미세조정, 지시문을 길게 쓸수록 유리
https://huggingface.co/cocorang/FireRed-Image-Edit-1.0-FP8_And_BF16
```

**양자화판이 없는 튜닝 모델은 직접 만들어도 된다.** 공식 툴로 아무 옵션 없이 양자화해도 상대 오차 2% 미만·코사인 유사도 최저 0.999936 이 나온다.

```
https://github.com/Comfy-Org/comfy-model-tools
```

→ [모델 고르기](models.md) · [ANIMA](anima.md)

<small>근거 — [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [Qwen-Image-Edit-2511 vs FireRed-I… 26.02](https://arca.live/b/aiart/162479433)</small>

??? note "근거 11건 전부 보기"
    [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [Qwen-Image-Edit-2511 vs FireRed-I… 26.02](https://arca.live/b/aiart/162479433) · [(미니 정보) 26년 5월 기준 간단하게 소개하는 그림 AI… 26.05](https://arca.live/b/aiart/169601993) · [Z-image 애니메 파인튜닝 Z-Anime 26.04](https://arca.live/b/aiart/169161957) · [NAIA 및 아니마 사용을 위한 Webui Forge Neo… 26.05](https://arca.live/b/aiart/170554328) · [Anima GGUF 양자화 모델 26.02](https://arca.live/b/aiart/161385741) · [체크포인트 2개 추천 (JANKU 사용자한테 추천) 26.03](https://arca.live/b/aiart/165778645) · [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089) · [(anima) 원본+int8 convrot 모델 3종 비교 26.07](https://arca.live/b/aiart/177372687)

## 2. 로라 — 공식 보조 로라
<small>2026-07 기준 · 근거 7건</small>

```
# circlestone-labs 공식 — 해상도 개선 (Highres / Aesthetic Boost v1.0)
Civitai: "Anima Highres/Aesthetic Boost - v1.0" (Anima LoRA)
  · 1536 은 문제없고 2048(4MP)도 완전히 깨지지는 않는다
  · 제작진 스스로 미적 향상 효과는 미미하다고 밝힘
  · 그림체 변화가 커서 화풍을 새로 깎아야 할 수준이고 세로로 긴 해상도에서 찐빠가 심하다는 보고

# circlestone-labs 공식 — 강화학습 퀄리티 개선 (Anima RL v0.1)
https://civitai.com/models/2583128/anima-rl
  · 이미지가 너무 밝거나 어둡거나 단색으로 나오는 것을 잡아 준다
  · 작가 태그가 없을 때는 원본과 차이가 적다

# 자작 4스텝 터보 로라 — er_sde / step 4 / cfg 1
https://huggingface.co/sorryhyun/anima-turbo-4step
  · RTX 5070 Ti 장당 1.2~1.31초, M1 Pro 512x512 11~13초

# 터보 로라 (civitai)
https://civitai.red/models/2560840/anima-turbo-lora

# 2048 해상도 전용 로라
https://drive.google.com/file/d/17r0eRVGiHLJ3X79XwBakHfgus7a6gm7b/view
  · novaAnime 은 1536 이하 학습 탓인지 2048x3072 에서 붕괴 → Anima Base 1.0 으로
```

> **터보/고속 로라 주의** — 배경과 역동적 표현이 크게 열화된다. 저해상도 원본 생성에만 쓰고 **highres 단계에서는 빼는** 운용이 권장된다. 셀채색·플랫한 스타일에서는 열화가 덜하다.

<small>근거 — [아니마 공식 해상도 개선 로라. 26.04](https://arca.live/b/aiart/167659142) · [아니아니마 고속고속마 품질비교마 26.05](https://arca.live/b/aiart/171972064) · [Circlestone Labs 공식 anima-rl-v0.1… 26.05](https://arca.live/b/aiart/169414949) · [아니마 공식 퀄리티 개선 로라 26.04](https://arca.live/b/aiart/169264526)</small>

??? note "근거 7건 전부 보기"
    [아니마 공식 해상도 개선 로라. 26.04](https://arca.live/b/aiart/167659142) · [아니아니마 고속고속마 품질비교마 26.05](https://arca.live/b/aiart/171972064) · [Circlestone Labs 공식 anima-rl-v0.1… 26.05](https://arca.live/b/aiart/169414949) · [아니마 공식 퀄리티 개선 로라 26.04](https://arca.live/b/aiart/169264526) · [하지만 빨랐죠? 자작 아니마 4스텝 로라 업데이트 26.07](https://arca.live/b/aiart/176518628) · [하지만 빨랐죠? 자작 4스텝 로라 또? 업데이트 26.07](https://arca.live/b/aiart/177849905) · [아니마용 2048 로라 26.05](https://arca.live/b/aiart/171203636)

## 3. 로라 — 스타일·캐릭터
<small>2026-07 기준 · 근거 18건</small>

**ANIMA 눈·화풍 로라** (civitai)

| 로라 | 효과 | 주의 |
|---|---|---|
| `yzsss` | 얼굴·눈이 커지는 씹덕 그림체 | 트리거워드 필요 |
| `ogipote` | 색감 선명, 동공 표현 | 홍조가 패시브로 붙는다 |
| `BetaBee Style` | 선이 예뻐지고 머리카락 표현 변화 | 스케줄러 영향을 받는다 |
| `chen bin` | 눈 색감이 다채로워짐 | 그림이 잘 망가져 **디테일러 필수** |

```
# ANIMA 스타일 로라
https://civitai.com/models/2383428    # kieed style (Anima)
https://civitai.com/models/723360     # AI styles dump — ANIMA/Illustrious/Rouwei/NoobAI 공용
https://civitai.red/models/2605859    # nakkar (Anima.ver), 트리거 @na1kar
https://civitai.red/models/2530730    # Blue Archive Style (Anima B1)
https://civitai.com/models/1459730    # **\(o_o)/** | Anima | Illustrious Style
https://civitai.com/models/2648375    # Yujin Hare Style [Anima], 트리거 @YujinHare

# 도트·픽셀아트
https://kio.ac/c/c7V7im4DEGGgP01sHRQP0b   # 크퀘스타일 도트 로라 (재업로드분)
https://kio.ac/c/dKh3Y5dlREIOL28qOC354b   # 같은 로라 다른 재업로드분
https://kio.ac/c/au2-BU-RXgU9P0sqxfC58b   # ilxl 판으로 추정
https://kio.ac/c/aekeNTHaj9NKL4n4FuEP0b   # (링크 죽음) 최초 배포분
  필수 프롬프트: pixel, cqstyles, widescreen, chibi, wide shot, zoomed out, small character, distant view
  해상도 1024x1024, 체크포인트 WAI v14

# 트릭컬 스타일
https://kio.ac/c/dyb0RsYqCbJW15MpZ3550b   # WAI v14 용. 고정 프롬프트: chibi, trickca1, 1girl, solo
mega.nz (base64 배포)                      # ANIMA Preview3 판 / 정발 Base 1.0 판. 트리거 @diyap_trickcal, chibi only

# 한국 애니메이션 캐릭터 묶음 (Illustrious)
https://mega.nz/folder/xnoT2Q4a#NqEKi0yc304f9B78eIus8Q
  터닝메카드 · 장금이의 꿈 · 아스타를 향해 차구차구 · 천년여우 여우비
  예시값: 스텝 25~30 / CFG 5~7 / Euler a

# 웹툰 캐릭터
civitai: "Lee Wonjin, 이원진 | Today's Han Yoil is a Woman - v1.0 | Illustrious LoRA"
  · 눈이 많이 깨지므로 디테일러 필수
civitai: "Who's That Girl? 오늘의 한요일은 여자다 - v2.0 | Anima LoRA"
  · 캐릭터 혼합 문제는 WAI-Anima 와 함께 쓰면 대부분 해소

# LTX 2.3 영상용 LoRA
https://huggingface.co/WarmBloodAban/Singularity-LTX-2.3_OmniCine_V1
  · 중국어로 훈련 → LoRA Audio 강도를 0 으로 둘 것
  · ltx-2.3-22b-distilled-1.1_transformer_only_fp8_scaled.safetensors 로만 쓸 것
https://drive.google.com/drive/folders/1Eh-QKmDGEM4Kl8ex_JuMgs_51QO9E4KO
  · 자작 4종(Anime-OG / Anime-10E / Idle_motion / PV / MV), 트리거워드 전부 dalstyle
  · Idle_motion 은 no-audio 학습이라 audio 사용 금지

# NAI 그림체를 로컬(Illustrious)에서 재현하는 로라
https://civitai.com/models/2396302?modelVersionId=2749219   # NAI 스타일 로라 v5
  · 사용 모델 dxjmxIllus_x8.safetensors, 로라 가중치 0.6
  · v4 보다 NAI 같아진 대신 다소 불안정하고 캐릭터 프롬프트가 애매해진다(임베딩 병용으로 완화)
  · **여러 작가를 섞을 때 생기는 이질감은 네거티브의 `(artist collaboration:1.5)` 로 억제한다**

# ANIMA — 원신 · 붕괴 스타레일 인게임 느낌 조합 (로라 2개)
https://civitai.com/models/2690646/genshin-impact-style-animav1     # 가중치 1.0 (이것만으로도 인게임 느낌)
https://civitai.com/models/2659822/honkai-star-rail-cg              # 가중치 0.4
  퀄리티 태그: unity \(medium\), unity \(game engine\), game model, game screenshot, cel rendering
  네거티브  : shading mismatch
  · **로라를 3개에서 2개로 줄이자 코 양옆에 생기던 이상한 그림자가 잡혔다**(완전히 없어지지는 않는다)
  · 뺀 것: Honkai Star Rail 3D Style Anima — 명도가 너무 높게 나온다
  · 결과가 '살짝' 원신 느낌이고 평범한 3D·MMD 처럼 보이기도 한다는 반응이 있다

# 트릭컬 스탠딩 SD(2등신) 스타일 로라
https://kio.ac/c/c1OASZS134KOP1i02MVP0b     # (기한 5월 18일 — **링크 죽음 유력**, 재배포 금지)
  트리거워드 TrickcalSD + deformed(2등신) + colored pencil \(medium\)(색연필 질감)
  머리 크기가 고정되지 않는 한계 → 네거티브에 big head, chibi
```

> **ANIMA 는 기존 ILXL 로라를 쓸 수 없다.** 로라는 ANIMA 계열(프리뷰1~3 · 정발 Base 1.0)로 학습된 것을 **베이스 버전에 맞춰** 골라야 한다.
> **인물 1명 위주로 학습된 로라**를 물리면 ANIMA 의 강점인 다인 구도가 약해진다.

**Illustrious 계열 그림체·캐릭터 로라 (추가분)**

```
# ILXL 계열 모델의 그림체를 NAI 느낌으로 일관되게 만드는 로라
https://huggingface.co/Bedovyy/arcaillous-xl/blob/main/lora_arcain.safetensors
  · 파인튜닝 모델 arcaillous-xl 과 같은 데이터셋을 Illustrious-XL 베이스에 학습한 것
  · NoobAI 를 작가 태그 없이 쓸 때 그림체가 들쭉날쭉해지는 문제를 잡으려고 만들었다
  · 권장 weight 0.75~1 (e621 태그를 쓸 때는 0.4~0.75)
  · Euler a + Normal 또는 DPM++ 2M SDE + SGM Uniform, CFG 5.0~7.0, Steps 25 안팎
  · 파인튜닝 비교용이라 DIM 이 커서 용량이 1.37GB 로 매우 크다
  · ⚠️ 데이터셋 편향으로 **블루아카이브 halo(머리 위 고리)가 나오고 가슴이 커진다**
    → weight 0.75 로 낮추고 네거티브에 halo 추가
  · ⚠️ 데이터셋에 아티스트 태그를 남겨 둬서 NAI 에서 자주 쓰는 작가는 오염이 있을 수 있고,
    NoobAI 에 얹어 아티스트를 혼합하면 가중치가 틀어진다

# 웹툰 '아카데미에서 살아남기' 캐릭터 로라 13종 (직접 스크린샷한 데이터셋)
https://arca.live/b/aiart/138102033   # 엘리스·아니스 헤일란·아일라 트리스·벨 마이아·클레어 엘핀·클라리스
https://arca.live/b/aiart/138135282   # 로르텔 케헬른·루시 메이릴·메릴다·페니아·타냐·예니카·아델 세리스
  LoRA Base illustriousXL_v1.1 / 실제 생성 체크포인트 WaiNSFWillustrious V140
  트리거 ale / annis halelan / ayla tris / bell maya / claire elfin / clrc / kylie echne
        lortel keherun / lucy mayreel / mrda / penia elias kroel / tanya rothtaylor
  공통 네거티브 bad quality, worst quality, worst detail, sketch, (censor:1.1),
               (shaded face:1.1), (dark:1.1)
  · 트리거 워드 없이도 잘 나오는 편이나 의상·장식·특이한 눈동자·문신은 제대로 안 나올 수 있다
  · 동봉된 WebUI Metadata 파일은 **LoRA 파일명과 똑같이** 유지해 같은 폴더에 둬야 인식된다

# ANIMA 메이플스토리 아크메이지(썬콜/빙썬) 로라
https://kio.ac/c/bWTowfC_x6SrD0e7_zw58b   # 본문은 base64 로 가려져 있다. 압축 비번 ai, 보관 한 달
  캐릭터  magician_(ice_lightning), maplestory, ringed eyes, eyelashes, tsurime,
          grey eyes, blue long hair, black hairband
  등신조절 chibi 를 넣으면 인게임 같은 2~3등신
  · 스태프(archmage il staff)는 형태 붕괴 확률이 있다. 작성자가 처음 만든 로라라 과적합 가능성 명시
```

> **'LoRA Base Model' 과 'Checkpoint Model' 은 다른 것이다.** 배포글에 적힌 Base 는 **그 로라를 만들 때 쓴 학습용 모델**이고, 그림을 실제로 뽑는 것은 별도의 체크포인트다. 로라를 받을 때 이 둘을 구분해야 "베이스 모델이 있는데 왜 그림이 안 나오지" 를 피한다 → [로라 쓰는 법](lora-usage.md)

<small>근거 — [트릭컬 스탠딩 sd 스타일 로라 공유 26.03](https://arca.live/b/aiart/165287857) · [웹툰 Lora 공유) 아카데미에서 살아남기 로르텔 케헬른｜루… 25.05](https://arca.live/b/aiart/138135282) · [한요일 올인원 로라 업뎃 26.06](https://arca.live/b/aiart/172772627) · [(로라공유) lora_arcain (ilxl 베이스) 24.10](https://arca.live/b/aiart/119240181)</small>

??? note "근거 18건 전부 보기"
    [트릭컬 스탠딩 sd 스타일 로라 공유 26.03](https://arca.live/b/aiart/165287857) · [웹툰 Lora 공유) 아카데미에서 살아남기 로르텔 케헬른｜루… 25.05](https://arca.live/b/aiart/138135282) · [한요일 올인원 로라 업뎃 26.06](https://arca.live/b/aiart/172772627) · [(로라공유) lora_arcain (ilxl 베이스) 24.10](https://arca.live/b/aiart/119240181) · [LTX2.3 lora 몇개 공유 26.06](https://arca.live/b/aiart/173653906) · [한애니 캐릭터들 만든 로라 공유 26.03](https://arca.live/b/aiart/165664117) · [정발 Anima용 트릭컬 스타일 로라 공유 26.06](https://arca.live/b/aiart/172973086) · [크퀘스타일 도트 로라 공유 26.04](https://arca.live/b/aiart/167362821) · [웹툰 Lora 공유) 아카데미에서 살아남기  엘리스｜아니스 … 25.05](https://arca.live/b/aiart/138102033) · [LTX 2.3 테스트중인 로라 하나 추천 26.06](https://arca.live/b/aiart/173213921) · [트릭컬 스타일 로라 공유 26.05](https://arca.live/b/aiart/169478146) · [Anima 로라 사용 후기 + 링크 26.03](https://arca.live/b/aiart/163664637) · [NAI 스타일 로라 v5 공유 26.03](https://arca.live/b/aiart/164149050) · [ANIMA 눈이 이뻐지는 로라 26.05](https://arca.live/b/aiart/169512883) · [Anima용 트릭컬 스타일 로라 공유 26.05](https://arca.live/b/aiart/169486310) · [ANIMA 메이플 썬콜 로라 공유 26.07](https://arca.live/b/aiart/176777447) · [원신도 붕스도 아닌 별 거 없는 로라 조합 26.07](https://arca.live/b/aiart/177985468) · [한요일의 이원진 로라 쪄왔음 26.03](https://arca.live/b/aiart/164820596)

## 3-b. 웹툰·애니 캐릭터 로라 — 작품별 배포 목록과 공통 규격
<small>⚠️ 2025-07 기준 · 근거 28건</small>

채널에서 가장 꾸준히 올라오는 배포물이 **웹툰·애니 캐릭터 로라**다. 대부분 같은 제작자들이 같은 규격으로 만들어
사용법이 통일돼 있다. **받는 규격이 하나이니 한 번만 익히면 전부에 통한다.**

### 공통 규격

| 항목 | 값 |
|---|---|
| LoRA Base Model | `illustriousXL_v1.1` (초기 글은 `illustriousXL_v0.1` / `v1.0`) |
| 실제 생성 Checkpoint | `WaiNSFWillustrious V140` |
| 샘플러 · CFG · 스케줄러 | `euler a` / `5.0` / `kl_optimal` |
| 해상도 | `1024x1344` (저사양 `832x1216`, 정사각 `1024x1024`) |
| 공통 네거티브 | `bad quality, worst quality, worst detail, sketch, (censor:1.1), (shaded face:1.1), (dark:1.1)` |

> 해상도에 특별한 이유는 없고 **SDXL 규격에 맞으면 자유롭게 쓰면 된다**고 제작자가 답했다.
> `LoRA Base Model` 과 `Checkpoint Model` 의 차이는 이 문서 위쪽 "3. 로라 — 스타일·캐릭터" 끝의 주석을 보라.

**동봉 파일 두 개를 반드시 같이 쓴다.**

```text
1) Metadata(json) 파일명을 LoRA(.safetensors) 파일명과 똑같이 맞춰 같은 폴더에 둔다
   → WebUI 에서 트리거워드와 프롬프트가 자동으로 뜬다 (ComfyUI 전용이 아니라 WebUI 사용자도 그대로 쓴다)
2) 배포글의 예시 이미지를 ComfyUI 캔버스에 끌어다 놓는다
   → 그 이미지를 만든 워크플로우가 그대로 불러와진다
```

트리거 워드는 **없어도 대체로 나오지만 넣는 편이 타율이 높다.** 다만 의상·장식·특이한 눈동자·문신은 재현이
잘 안 될 수 있어서 배포글이 캐릭터별 의상 태그를 따로 나열해 두었다 — 그 부분은 그대로 복사해 쓰는 것이 맞다.

### ⚠️ 링크가 여기저기 흩어져 있는 이유

```text
키오스크(kio.ac)  →  civitai  →  아카라이브
```

처음 쓰던 파일 호스트 **키오스크가 불안정해 civitai 로 옮겼고**, 이후 일부 제작자는 civitai 서버·정책에
회의를 느껴 **업로드를 중단하고 아카라이브로 다시 옮겼다.** 그래서 같은 시리즈인데 받는 곳이 글마다 다르다.
**링크가 죽어 있으면 civitai 에서 작품명으로 검색하는 편이 빠르다.**

```text
https://civitai.com/search/models?query=작품명
```

### 섹톱워치 — 13종 (베이스 `illustriousXL_v0.1`, 박나영·우유연만 `v1.0`)

| 캐릭터 | 트리거 | 받는 곳 |
|---|---|---|
| 윤대리 | `manager yoon` | `https://civitai.com/models/602386` |
| 오희정 | `oh heejeong` | `https://civitai.com/models/606515` |
| 강지혜 | `kang jihye` | `https://civitai.com/models/596265` |
| 강안나 | `kang anna` | `https://civitai.com/models/596259` |
| 구혜리 | `goo hye-ri` | `https://civitai.com/models/594238` |
| 최나나 | `choi nana` | `https://civitai.com/models/1722132` |
| 우유연 | `woo yu-yeon` | `https://civitai.com/models/606521` |
| 박나영 | `park nayoung` | `https://civitai.com/models/602327` |
| 박나미 | `park nami` | `https://civitai.com/models/598421` |
| 유정원 | `yoo jeong-won` | `https://civitai.com/models/600351` |
| 윤민영 | `yoon minyoung` | `https://civitai.com/models/600363` |

박나미는 의상 세트가 5개(트랙자켓·슈러그·플로럴 드레스·정장·개귀)로 가장 많다.
김란·고윤지는 **글에는 없고 civitai 에만 있다**(원문 135304065 댓글 6).

### 나 혼자만 레벨업 — 13종

```text
트리거  chiani(차해인) · esil ladir · gina · han semi · han song-yi
        seo jiwoo · sung jin-ah · smzakr(시미즈 아카리) · twtkn(타와타 카나에)
        hakwa(하네카와) · lee bora · lee joo-hee · park heejin

⚠️ smzakr · twtkn · hakwa 는 축약형 인공 토큰이라 반드시 그대로 써야 한다

서지우          https://civitai.com/models/1725832
성진아          https://civitai.com/models/590177
시미즈 아카리   https://civitai.com/models/1725869
타와타 카나에   https://civitai.com/models/1725882
하네카와        https://civitai.com/models/1725743
이보라          https://civitai.com/models/1725774
이주희          https://civitai.com/models/590161
박희진          https://civitai.com/models/1725803
```

차해인 예시 — `chiani, blonde hair, short hair, purple eyes, sidelocks, bob cut, anime coloring`

### 그 밖의 작품 (전부 같은 규격)

| 작품 | 종수 | 트리거 / 비고 |
|---|---|---|
| **동아리** | 11종 + 박다영 단독 | 조회 22만이 넘는 이 시리즈 최대 인기 글. 박다영 단독판은 베이스가 `waiNSFWIllustrious_v80`, 트리거 `Dayoung`, `Steps 50 / Euler a / Beta / CFG 5` — `https://civitai.com/models/1517725?modelVersionId=1717140` |
| **퀘스트지상주의** | 6종 | `baek chaerin, elisa, kim dahyeon, lee jihyeon, yang soha, yeon seohui` |
| **초인의 게임** | 6종 | `higpr`(대사제), `baek hayeon`, `lee nayeon`, `qun1`(여왕), `saniya ahmetova`, `shuran` — **의상 세트를 별도 토큰으로 학습**: 백하연은 `clothes1` · `clothes2` 만 넣으면 복장 세트가 통째로 나온다 |
| **일진담당일진** | 5종 | 백수지·이사임·미도리카와 요코·오춘심·서지인 |
| **수요웹툰의 나강림** | 13종 | 두 글로 나뉘어 있다 |
| **사시미 한 자루로 아카데미를 씹어먹음** | 6종 | 아벨 폰 니벨룽·클로이 아디토레·최설아·메디아 포이즌·레이첼 드 뮈라·사키 료조 |
| **전지적 독자 시점** | 14종 | 짝 글 — `https://arca.live/b/aiart/139326347` ↔ `https://arca.live/b/aiart/139333927` |
| **현실퀘스트** | 7종 | `choi minhye` 외. 캐릭터마다 초반/후반 헤어스타일 태그가 나뉘어 있다 (최민혜 후반부 = 기본 태그 + `colored inner hair, two-tone hair, white hair, streaked hair`) |
| **이세계 밀프 헌터** | 10종 | 짝 글 — `https://arca.live/b/aiart/140473932` ↔ `https://arca.live/b/aiart/140480040` (뒤쪽 댓글에 학습 파라미터가 상세히 있다) |
| **광마회귀** | 공손월 | 나머지 캐릭터는 civitai 에 남아 있다 |
| **귀환자의 마법은 특별해야 합니다** | 3종 | `ajest jedgar` `https://civitai.com/models/596285` · `brigette` `https://civitai.com/models/598370` · `romantica eru` `https://civitai.com/models/598376` |

### 단품 로라

```text
# 새로구미(여구미) — 소주 브랜드 마스코트
https://civitai.com/models/1727202/anime-character-saero-gumi-saero-soju
  트리거 saero-gumi (여우 형태) / Saro (인간형)
  외형   saero-gumi, fox girl, animal ears, animal ear fluff, long hair, green hair,
         aqua hair, streaked hair, parted bangs, multicolored hair, white hair,
         aqua eyes, green eyes, white pupils, diamond-shaped pupils, kyuubi,
         multicolored tails, green tail, white tail
  의상   한복(hanbok) · 한푸(hanfu) · 기모노 세트가 따로 정리돼 있다
  ※ kyuubi 는 구미호(꼬리 아홉)를 뜻하는 단부루 태그다

# 갸루에게 상냥한 오타쿠 군 — 나루미 유우아이
https://civitai.com/models/1639028
  트리거 narumi1 (필수)   예시 모델 WAI-NSFW-illustrious-SDXL v14
  흑백   monochrome, narumi1, long hair, single sidelock, gradient eyes, medium breasts,
         earrings, hoodie jacket, collared shirt, skirt,
  컬러   anime screencap, narumi1, blonde hair, long hair, single sidelock, grey eyes,
         gradient eyes, medium breasts, earrings, white hoodie jacket, collared shirt,
         blue shirt, black skirt,
  네거   shiny skin, red pupils, gradient hair,

# 성인웹툰 속 엑스트라가 되었다 — 주연 3인 + 조연 1인을 한 파일에
https://civitai.com/models/1664554
  트리거 parkgonggi(박공기) / jungsil(정실) / nohyeju(노예주) / leezy(이지)
  ※ 캐릭터마다 의상이 1~3벌씩 모두 학습돼 있어 의상 프롬을 세밀하게 적어야 한다
  예) jungsil, purple eyes, silver hair, hair stick, butterfly hair stick
      + 의상1 black sleeveless, seethrough cleavage, midriff, crop top, denim pants, baggy pants
      + 의상2 off-shoulder dress, floral print, strap
      + 의상3 blue pajamas, square neckline, cleavage

# 클로저스 — 비나
https://civitai.com/models/1792789?modelVersionId=2028848
  트리거 binah   832x1216 / step 35 / cfg 5.0 / euler
  ※ 학습 이미지가 단 3장, 베이스 illustrious 0.1 XL — 적은 데이터로도 캐릭터 로라가 나온다는 실례
```

### ⚠️ 받을 수 없는 것 — 기한이 끝난 배포

| 무엇 | 주소 | 상태 |
|---|---|---|
| 손발 삽입 컨셉 로라 (2025-04) | `https://kio.ac/c/dq8L0M26r0RdX2LCgKzPyb` (본문 base64 디코딩분) | **만료 추정** — 공유 기간이 **일주일**이었고 댓글에 재업 요청이 있었다 |
| 왕자림 × 이경우 NTR 로라 (2025-05) | (본문 링크) | **다운로드 불가** — 본문에 '3일간 공유' 라고 적혀 있고 댓글에서도 링크가 닫혔다는 요청이 이어졌다 |

지웠으면 다시 찾아 헤매게 되므로 **남겨 둔다.** 두 글에서 살아남는 것은 파일이 아니라 태그 문법이다.

```text
# 손발 삽입 — 실제 사용 문법은 severed __ in __
severed hand in pussy / 2 severed hands in pussy / severed hand in ass
severed foot in pussy / 2 severed feet in ass
  · 학습 태깅은 severed limb insertion 을 썼지만 없어도 된다
  · 2개가 들어간 것(2 severed ...)은 학습만 한 수준이라 실사용이 어렵다
  · 삽입 부위에 이상한 것이 생기므로 네거티브에 blood, vaginal prolapse 를 넣는다

# 왕자림 × 이경우 — 한 로라에 두 인물을 같이 학습시킨 사례
트리거 jarim / lgw / jarimlgw / jarimlgwlr 를 함께 쓴다
1boy, 1girl 태그만 써도 이 두 명이 거의 고정적으로 등장한다
사용 체크포인트 hesperidesIllustrious_v10
호출 문법 <lora:jarimlgwlr-000002:1>  ← 뒤의 -000002 는 학습 중 저장된 2번째 에폭 파일
```

→ 로라를 넣는 위치와 가중치는 [로라 쓰는 법](lora-usage.md), 안 나올 때는 아래 "3-c" 를 보라.


<small>근거 — [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  차해인｜에실… 25.05](https://arca.live/b/aiart/136191062) · [웹툰 Lora 공유) 현실퀘스트 최민혜｜현진서｜제니｜주아린｜… 25.06](https://arca.live/b/aiart/140055598) · [웹툰 Lora 공유) 전지적 독자 시점 정희원｜이지혜｜민지원… 25.06](https://arca.live/b/aiart/139333927) · [애니메이션 캐릭터 Lora 공유) 새로구미(여구미) 25.05](https://arca.live/b/aiart/136921678)</small>

??? note "근거 28건 전부 보기"
    [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  차해인｜에실… 25.05](https://arca.live/b/aiart/136191062) · [웹툰 Lora 공유) 현실퀘스트 최민혜｜현진서｜제니｜주아린｜… 25.06](https://arca.live/b/aiart/140055598) · [웹툰 Lora 공유) 전지적 독자 시점 정희원｜이지혜｜민지원… 25.06](https://arca.live/b/aiart/139333927) · [애니메이션 캐릭터 Lora 공유) 새로구미(여구미) 25.05](https://arca.live/b/aiart/136921678) · [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜… 25.05](https://arca.live/b/aiart/137508828) · [웹툰 Lora 공유) 이세계 밀프 헌터 아리엘라 레이븐｜벨리… 25.06](https://arca.live/b/aiart/140473932) · [웹툰 Lora 공유) 동아리  안지영｜백가인｜한나리｜강수연｜… 25.05](https://arca.live/b/aiart/137475690) · [웹툰 캐릭터 Lora 공유) 퀘스트지상주의  백채린｜엘리사｜… 25.05](https://arca.live/b/aiart/136525702) · [웹툰 Lora 공유) 광마회귀 공손월 25.06](https://arca.live/b/aiart/140540745) · [웹툰 Lora 공유) 수요웹툰의 나강림  박정아｜홍 사장｜서… 25.05](https://arca.live/b/aiart/137766502) · [웹툰 Lora 공유) 전지적 독자 시점 아일렌 메이크필드｜아… 25.06](https://arca.live/b/aiart/139326347) · [웹툰 Lora 공유) 수요웹툰의 나강림  방예림｜차시린｜큐피… 25.05](https://arca.live/b/aiart/137729551) · [웹툰 Lora 공유) 사시미 한 자루로 아카데미를 씹어먹음 … 25.06](https://arca.live/b/aiart/138521652) · [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  서지우｜성진… 25.05](https://arca.live/b/aiart/136376313) · [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  하네카와｜이… 25.05](https://arca.live/b/aiart/136373651) · [웹툰 Lora 공유) 일진담당일진  백수지｜이사임｜미도리카와… 25.05](https://arca.live/b/aiart/137557622) · [웹툰 Lora) 성인웹툰 속 엑스트라가 되었다 - 주연 3인… 25.06](https://arca.live/b/aiart/139125184) · [웹툰 캐릭터 Lora 공유) 초인의 게임  대사제｜백하연｜이… 25.05](https://arca.live/b/aiart/136828343) · [웹툰) 동아리-박다영 (로라 공유) 25.04](https://arca.live/b/aiart/135221703) · [애니 캐릭터 Lora 공유) 귀환자의 마법은 특별해야 합니다… 25.05](https://arca.live/b/aiart/135848518) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 우유연… 25.05](https://arca.live/b/aiart/135573919) · [왕자림 x 이경우 NTR 로라 공유 25.05](https://arca.live/b/aiart/135597261) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 강안나… 25.04](https://arca.live/b/aiart/135389458) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 윤대리… 25.04](https://arca.live/b/aiart/135304065) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 유정원… 25.05](https://arca.live/b/aiart/135646986) · [고어, 이상성욕) 방금만든 손발 삽입로라 공유 25.04](https://arca.live/b/aiart/134892006) · [Lora 공유) 갸루에게 상냥한 오타쿠 군 - 나루미 유우아이 25.05](https://arca.live/b/aiart/138283386) · [클로저스 비나 로라 25.07](https://arca.live/b/aiart/142890947)

## 3-c. 캐릭터 로라가 뜻대로 안 나올 때 — 답은 배포글 댓글에 있다
<small>⚠️ 2025-06 기준 · 근거 18건 · 자료 엇갈림</small>

배포글의 **본문이 아니라 댓글에** 답이 있는 것들이다. 같은 질문이 시리즈 내내 반복됐다.

### 로라가 목록에 아예 안 뜬다

**현재 로드된 체크포인트를 SDXL(Illustrious) 계열로 바꾸면 나타난다.**
WebUI 는 지금 체크포인트와 아키텍처가 다른 로라를 목록에서 **숨긴다.**
질문자가 로라 폴더에 분명히 넣었는데 안 보인다고 했고, **체크포인트만 SDXL 로 바꾸니 떴다**고 확인했다
(원문 137508828 댓글 12~14).

### 예시와 똑같이 안 나온다

**"체크포인트만 같으면 같은 그림이 나온다" 는 생각은 틀렸다.**

| 원인 | 어떻게 |
|---|---|
| 체크포인트가 원본 ILXL 이다 | `illustriousXL` 원본이 아니라 **`wainsfw140v`** 로 바꾸고, 그 모델 배포처에 적힌 세팅을 그대로 쓴다 |
| 확장 프로그램 · **hires(고해상도 보정) 설정** 차이 | 업스케일 단계 설정까지 맞춰야 한다 |
| 제작자는 ComfyUI, 나는 WebUI | 도구가 다르면 결과가 다르다고 제작자가 직접 답했다 |

프롬프트를 통째로 얻고 싶으면 **civitai 에 올린 이미지의 설명란**에 전문이 들어 있다. 부정 프롬만 배포글 값으로
바꿔도 무방하다. 반대로 **아카라이브 첨부 이미지에는 EXIF 가 남지 않아** 프롬프트 추출 노드에 넣어도 아무것도 안 나온다.

### 원하지 않은 것이 딸려 나온다

| 증상 | 대처 |
|---|---|
| 인물이 둘 이상 나온다 | 네거티브에 `2girls`, 긍정에 `(solo:1.1)` |
| 갑옷이 새어 나온다 | 네거티브에 `(shoulder armor:1.1), (breastplate:1.1), (pauldrons:1.1)` |
| 붉은 테두리가 새어 나온다 | 네거티브에 `(red trim:1.2)` |
| **말풍선이 튀어나온다** | 웹툰을 학습했기 때문이다. 네거티브에 **`speech bubble`** 을 반드시 넣는다 |
| **효과음(의성어) 글자가 나온다** | `monochrome` + `motion lines` 조합에서 높은 확률로 생긴다. 네거티브에 **`sound effects`**, 그래도 안 되면 인페인트로 지운다 |
| 특징이 너무 강하게 찍힌다 | `(mole on breast:0.8)` 처럼 **가중치를 낮춰** 넣는다 |
| 모자이크가 필요하다 | 반대로 `blank censor` 를 **넣으면** 떡툰 특유의 모자이크가 나온다 |

### ⚠️ 동봉 워크플로우에서 색이 물 빠진다 — 본문이 아니라 배포 상태의 문제였다

`Load Image` 노드만 빼고 나머지를 켰더니 **`ModelSamplingDiscrete`(모델 샘플링 이산) 때문에 색이 물 빠진 것처럼
나오고 `TiPO` 를 적용하면 그림이 이상해진다**는 질문이 있었다.

> **원글쓴이의 정정** — 자신은 **모델 샘플링과 TiPO 를 비활성화한 상태로 올렸다**며,
> 쓰는 체크포인트에 맞춰 꺼 두거나 설정에 맞게 쓰라고 답했다.
> **즉 이 두 노드는 필수가 아니고, 체크포인트와 궁합이 안 맞으면 꺼도 된다** (원문 136373651 댓글 1·2).

`TiPO` 는 짧은 프롬프트를 LLM 으로 부풀려 주는 확장 노드다. 워크플로우를 켤 때 켜져 있다고 해서 필수인 것은 아니다.

### ComfyUI 가 복잡해 포기하겠다면

이 시리즈 제작자(스스로 입문 2달차라고 밝혔다)의 답은 하나다 — **남들이 올려 준 워크플로우를 그대로 갖다 쓰는 것이
제일 편하다.** → [ComfyUI 쓰는 법](comfyui.md)

### ⚠️ 학습 가이드 링크 — 틀린 것과 맞는 것이 함께 남아 있다

이 제작자들이 참고한 가이드를 물었을 때 질문자가 짚은 링크가 **틀렸고**, 원글쓴이가 정정해 주었다.

| | 주소 |
|---|---|
| ❌ 질문자가 짚은 것 | `https://arca.live/b/hypernetworks/84182575` |
| ✅ **원글쓴이의 정정** | `https://arca.live/b/hypernetworks/110021224` (포리x 개정판) |

제작자는 이 가이드에서 **로라 타입·해상도·Epoch 만 바꿔** 쓴다고 밝혔고, 실제 값도 공개했다.

```text
Text Encoder learning rate   0
Network Rank = Alpha         16   ← 둘은 반드시 같은 값. 한 파일에 캐릭터 1~2명만 담아 용량 때문에 16 고정
Max Token Length             225  ← 기본 75 에서 올린다
Epoch                        6
스텝   캐릭터·컨셉  2000~2200
       그림체(스타일) 15000~20000
```

**그림체 로라는 캐릭터와 체급이 다르다** — 캐릭터가 2000스텝이면 그림체는 **10000~20000 스텝**이 필요하고,
데이터도 그 작품 캐릭터를 있는 대로 다 넣고 **일반적인 배경 그림까지** 넣는 것이 좋다.

**학습 베이스는 `illustrious 0.1` 보다 `1.1`** — 요즘 병합 모델들이 1.0 기준으로 만들어지는 추세라
0.1 로 만든 로라는 잘 안 나올 때가 있다. 베이스 링크는 `https://civitai.com/models/1252206/illustrious-xl-11`.

> **데이터가 없는 캐릭터는 만들 수 없다.** 갤부루·단부루에 자료가 비어 있으면 학습 데이터셋을 못 모으기 때문이고,
> 제작자들도 데이터셋이 없는 작품 요청은 거절했다. 반대로 **이미지 3장으로 만든 캐릭터 로라도 쓸 만하게 나왔다**
> (위 "클로저스 비나").

→ 학습 자체는 [로라 쓰는 법](lora-usage.md), 프롬프트 문법은 [프롬프트 쓰는 법](prompting.md)


<small>근거 — [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  차해인｜에실… 25.05](https://arca.live/b/aiart/136191062) · [웹툰 Lora 공유) 전지적 독자 시점 정희원｜이지혜｜민지원… 25.06](https://arca.live/b/aiart/139333927) · [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜… 25.05](https://arca.live/b/aiart/137508828) · [웹툰 Lora 공유) 동아리  안지영｜백가인｜한나리｜강수연｜… 25.05](https://arca.live/b/aiart/137475690)</small>

??? note "근거 18건 전부 보기"
    [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  차해인｜에실… 25.05](https://arca.live/b/aiart/136191062) · [웹툰 Lora 공유) 전지적 독자 시점 정희원｜이지혜｜민지원… 25.06](https://arca.live/b/aiart/139333927) · [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜… 25.05](https://arca.live/b/aiart/137508828) · [웹툰 Lora 공유) 동아리  안지영｜백가인｜한나리｜강수연｜… 25.05](https://arca.live/b/aiart/137475690) · [웹툰 캐릭터 Lora 공유) 퀘스트지상주의  백채린｜엘리사｜… 25.05](https://arca.live/b/aiart/136525702) · [웹툰 Lora 공유) 광마회귀 공손월 25.06](https://arca.live/b/aiart/140540745) · [웹툰 Lora 공유) 수요웹툰의 나강림  박정아｜홍 사장｜서… 25.05](https://arca.live/b/aiart/137766502) · [웹툰 Lora 공유) 사시미 한 자루로 아카데미를 씹어먹음 … 25.06](https://arca.live/b/aiart/138521652) · [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  서지우｜성진… 25.05](https://arca.live/b/aiart/136376313) · [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  하네카와｜이… 25.05](https://arca.live/b/aiart/136373651) · [웹툰 Lora 공유) 일진담당일진  백수지｜이사임｜미도리카와… 25.05](https://arca.live/b/aiart/137557622) · [웹툰 Lora) 성인웹툰 속 엑스트라가 되었다 - 주연 3인… 25.06](https://arca.live/b/aiart/139125184) · [웹툰 캐릭터 Lora 공유) 초인의 게임  대사제｜백하연｜이… 25.05](https://arca.live/b/aiart/136828343) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 강안나… 25.04](https://arca.live/b/aiart/135389458) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 윤대리… 25.04](https://arca.live/b/aiart/135304065) · [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 유정원… 25.05](https://arca.live/b/aiart/135646986) · [Lora 공유) 갸루에게 상냥한 오타쿠 군 - 나루미 유우아이 25.05](https://arca.live/b/aiart/138283386) · [클로저스 비나 로라 25.07](https://arca.live/b/aiart/142890947)

## 3-d. 스타일 로라와 디테일러 로라 — 실측 비교 자료
<small>2026-01 기준 · 근거 4건</small>

캐릭터가 아니라 **그림체 자체**를 바꾸는 로라와, 화질을 올린다고 주장하는 로라들의 실측 자료다.

### 스타일 로라

```
# 블루 아카이브 공식 컷씬 그림체 (2025-08)
https://civitai.com/models/1884029?modelVersionId=2132494
  데이터셋 783장 / Epoch 11 채택 (Epoch 12 는 찐빠가 너무 많이 나서 탈락)
  예시는 WAI14 체크포인트에 로라 강도 1 — 강도는 아무렇게나 써도 된다고 한다
  · 데이터셋 정제가 핵심이다 — 최신 인게임 일러스트와 화풍이 안 맞는 그림을 삭제하고
    copyright logo / copyright name / copyright notice / english text / speech bubble 이 든 그림도 뺐다
  · 데이터셋과 결과물 모두 Landscape(가로) 해상도가 메인이라 세로 그림은 표본이 적다
  · 글 작성 후 일섭에 새로 나온 캐릭터는 학습에 없으니 캐릭터 로라를 따로 쓴다

# gore(ゴア) 작가 그림체 (2025-11)
https://civitai.com/models/2176185?modelVersionId=2450625     작가 원본 gore.fanbox.cc
  트리거 gore_style   추천 프롬 best quality, chibi,
  ⚠️ 사용법이 거꾸로다 — 네거티브에서 품질 프롬을 전부 빼라고 안내하며,
     퀄리티 프롬을 빼면 오히려 원작(오리지널) 느낌이 난다
  · 스타일 로라에서 품질 태그가 원작 화풍을 지워 버릴 수 있다는 실례다
  · 작가 그림이 만화와 섞여 있어 문자가 대량으로 들어간 난해한 데이터셋이었고,
    실험적이라 결과가 좋지 않을 수 있다고 제작자가 명시했다

# VRChat 인기 3D 아바타 (2025-11) — 베이스가 NoobAI V-pred 다
https://civitai.com/models/2113947/noobai-v-pred-vrchat-3d-character-karin    # 카린
https://civitai.com/models/2116458/noobai-v-pred-vrchat-3d-character-mafuyu   # 마후유
  ⚠️ v-prediction 을 지원하는 환경(reForge / Forge / ComfyUI, 또는 ZeroSNR 이 되는 A1111 특정 버전)이 필요하다
  · 트리거는 별도 인공 토큰이 아니라 단부루에 기록된 표기를 그대로 쓴다
  · 3D 아바타는 데이터가 정형화돼 있어 학습이 생각보다 잘 됐다는 것이 배포 이유다
```

> **civitai 가 이유를 알려 주지 않고 업로드를 반려하는 일이 있다.** 블루 아카이브 로라는 두 번 반려당했고
> **WebP 무손실 압축 후 학습·업로드**로 우회했다.

### 디테일러 · 인핸서 로라 20종 실측 비교 (2026-01)

'채널에 디테일러 로라 정보가 하나도 없어서' 직접 검증한 글이다. 조건은 모델 `wai illustrious v16`,
VAE `MS DPipe fp32 112k Anime VAE SDXL`, 강도 `0.0 / 0.2 / 0.5 / 0.8 / 1.0`.

**원글쓴이의 최종 선택은 `Smooth Detailer Booster` 를 약하게 + `PornMaster 增加细节` 를 곁들이는 것**이며,
전반적으로는 *"디테일 추가라는 면에서는 다들 잘 모르겠다"* 는 솔직한 총평을 남겼다.

| 갈래 | 로라 (civitai 번호) | 관찰 |
|---|---|---|
| 디테일 | **Smooth Detailer Booster** `1145743` | **자세를 거의 유지하면서 많이 쨍해진다** — 최종 선택 |
| 디테일 | **PornMaster-noobXL & Illustrious 增加细节** `998657` | 땀·입김 표현 중심. 제작자 안내가 **0.1 에서 시작해 0.01 씩 올리라**고 돼 있다 |
| 디테일 | Aesthetic Quality Modifiers - Masterpiece `929497` | 광택·채도가 오르되 위보다 덜해 '슴슴하게' 좋다 |
| 디테일 | Add Micro Details - Concept `1377820` | 디테일해지는 느낌은 확실하나 **그림체도 약간 바뀐다** |
| 디테일 | Illustrious Extreme Resolution `2022120` | 엄청 쨍해지고 디테일해진다 |
| 디테일 | Detail enhancer IL\|Pony `1450571` | **0.5~0.8 부터 그림체가 바뀐다.** 그전엔 채도·명암만 약간 |
| 디테일 | illustrious Detailer `1586731` | 머리카락·배경 디테일이 조금 느는 정도 |
| 디테일 | sexy details `1615374` · FUCKED SILLY v2.0 `1273929` | 차이를 잘 모르겠음 |
| 색감 | Control LoRA Collection - NAI vpred fix `99619` | 디테일러라기보다 vpred 용이지만 색감 개선 효과는 있다 |
| 광택 | **Oiled Skin/Shiny Skin Enhancer** `1446130` | 광택은 직빵이지만 ⚠️ **그림체가 바뀌고 가슴·허벅지가 커진다** |
| 광택 | **shiny skin [光沢のある皮膚]** `1753461` | 광택 최고이나 ⚠️ 역시 가슴·허벅지가 커진다 (학습 그림체 탓) |
| 광택 | Glossy Skin `1032320` | 구도는 바뀌어도 **그림체는 어느 정도 유지**하며 광택이 는다 |
| 광택 | Shiny Nai style `618752` · shiny wet skin `1568999` | 타원형 광택이 특징 / 거기에 증기 효과 추가 |
| 광택 | Matte/Shiny Skin `1105924` | 변화가 은은해 잘 안 보임 |
| 눈 | **Eyes for Illustrious** `1826240` | 확실히 바뀐다 |
| 눈 | Eye detail LoRA `1300857` · Eye Enhancer `1731594` | 차이를 모르겠다 |

> ### 쓰는 법이 결과를 가른다
>
> **강도를 `0.05~0.1` 로 아주 낮추고, 모델 강도뿐 아니라 CLIP 강도까지 함께(보통 같은 값으로) 조절**하면
> 영향이 큰 것은 확확 바뀌고, 프롬프트를 더 잘 알아먹으며 디테일이 추가되는 느낌이 확실해진다(댓글 2·3).
>
> 디테일러 로라는 **그림체·몸매·구도·배경 모두에 영향을 주는데 그때마다 다르게 작용해** 방향성을 가늠하기 어렵다.
> **eye detailer 는 애프터 디테일러 단계에만 적용하는 편이 나을 수 있다**(댓글 8).

→ 얼굴을 다시 그리는 것 자체는 [디테일러](detailer.md), 화질은 [업스케일과 화질](upscale.md)


<small>근거 — [블루 아카이브 컷씬(?) 그림체 로라 배포 25.08](https://arca.live/b/aiart/145720807) · [Detailer / Enhancer용 11개 + 피부 광택 … 26.01](https://arca.live/b/aiart/159981349) · [VRChat 인기 아바타 카린, 마후유 로라 배포 25.11](https://arca.live/b/aiart/153368473) · [ゴア gore 작가 스타일 로라 공유 게시 25.11](https://arca.live/b/aiart/155353897)</small>

## 4. 컨트롤넷 · LLLite
<small>2026-08 기준 · 근거 9건</small>

전부 `설치폴더\ComfyUI\models\controlnet` 에 넣는다 (ANIMA LLLite 는 ComfyUI 버전에 따라 `models/model_patches`).

```
# SDXL/Illustrious 계열
https://huggingface.co/xinsir/controlnet-union-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors
https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/OpenPoseXL2.safetensors
https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
https://civitai.red/models/962537/noobai-xl-controlnet-openpose     # 기본 OpenPoseXL2 가 잘 안 들으면 이쪽으로 교체

# SDXL/ILXL 에서 실제로 동작하는 오픈포즈 (2023년 컨트롤넷 글은 전부 SD1.5 용이라 안 먹는다)
https://huggingface.co/xinsir/controlnet-openpose-sdxl-1.0
  diffusion_pytorch_model 과 diffusion_pytorch_model_twins 둘 다 ILXL 에서 동작 확인 (reForge 기준)
  같은 저장소에 depth, canny 도 있다. 여러 전처리기를 하나로 처리하는 `union sdxl` 쪽이 편하다는 권고

# 인페인팅 — 디노이즈 1.0 까지 올려도 경계가 어색하지 않다 (사실상 2D 전용)
https://civitai.com/models/1376234/noobai-inpainting-controlnet

# ANIMA 용 LLLite (LoRA Like Lite)
https://huggingface.co/kohya-ss/Anima-LLLite/resolve/main/anima-lllite-inpainting-v2.safetensors
https://huggingface.co/kohya-ss/misc-models/blob/main/anima-lllite-lineart-test-1.safetensors   # lineart 테스트판
https://civitai.red/models/2708551/anima-tile-and-repair-controlnet-lllite                       # noob 팀 데이터셋 기반
https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI                                            # 노드

# SAM3 (마스크 자동 검출)
https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors
```

<small>근거 — [컨트롤넷 초보 기본 사용법 (Openpose, 전처리기 종류… 23.07](https://arca.live/b/aiart/80881919) · [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860)</small>

??? note "근거 9건 전부 보기"
    [컨트롤넷 초보 기본 사용법 (Openpose, 전처리기 종류… 23.07](https://arca.live/b/aiart/80881919) · [Comfyui portable v0.30.0 + sage 외… 26.08](https://arca.live/b/aiart/178800540) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [Comfyui portable v0.31.0 + sage 외… 26.08](https://arca.live/b/aiart/179342860) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [로컬 comfyui 찍먹해보기 - 컨트롤넷을 사용한 인페인팅… 26.02](https://arca.live/b/aiart/162809080) · [SDXL(ILXL) 컨트롤넷 모델 정보 24.11](https://arca.live/b/aiart/122545929) · [noobai팀이 만든거) Anima Tile & Repair… 26.06](https://arca.live/b/aiart/174094973) · [kohya가만든 anima용 lineart ControlNe… 26.04](https://arca.live/b/aiart/168801930)

## 4-b. 로라를 찾고 관리하는 법
<small>2026-05 기준 · 근거 5건</small>

**civitai 에서 그림체 찾기** — 우측 상단 필터 → 기간 전체 / 모델 타입 **체크포인트** / 베이스 모델 **illustrious · NoobAI · SDXL 1.0** → 정렬 **Most downloaded**. 다운로드가 많은 모델일수록 그 모델로 만든 그림이 많아 그림체 표본이 넓다. 이미지 목록은 **Most Reactions** 로 정렬해 고른다.
일관된 그림체를 원하면 모델 타입을 **Lora** 로 바꿔 다운로드 순으로 정렬하고 **STYLE** 을 누른다.

**'똑같이 따라했는데 왜 다르게 나오나' — EXIF 로 미리 판별한다**
reForge/WebUI 는 로라를 부르면 프롬프트에 `<lora:ponyv6_noobV1_2_adamW:1>` 같은 문자가 **반드시 남는다.**
- 모델·로라 정보가 있고 프롬프트에 호출문이 **전부** 들어 있다 → 비슷하게 나올 확률이 높다
- 로라를 쓴 티가 나는데 프롬프트에 호출문이 없다 → ComfyUI 나 Civitai 생성기로 만든 것. **과감히 포기한다**
- 그림체는 화려한데 프롬프트가 이상하게 짧다 → 안 될 확률이 높다

**로라 이름으로 검색해도 안 나올 때** — Civitai 제목과 파일 이름이 다른 경우가 많다. EXIF 로라 항목의 **해시값**(예: `7a6cdc714921`)을 그대로 Civitai 검색창에 넣으면 바로 뜬다.

**퀄리티 로라 조합** (작가 태그 대신 로라로 퀄리티와 그림체를 함께 맞추는 방식)

```
<lora:ppw_v8_Illuv2stable_128:0.4> <lora:NOOB_vp1_detailer_by_volnovik_v1:0.3>
<lora:noobai_ep11_stabilizer_v0.138_fp16:0.3> <lora:ponyv6_noobV1_2_adamW:0.3>
```

> 주의 — 퀄리티 로라는 찾는 그림체에 의도치 않은 변형을 주고 AI 특유의 느낌을 넣는 경우가 있다. 수치를 조절해 가며 쓴다.

**로라가 프롬프트를 무시할 때 — LoRA Block Weight**

```
https://github.com/hako-mikan/sd-webui-lora-block-weight
문법: <lora:로라이름:가중치:프리셋>     예) <lora:이름:0.2:OUTALL>
프리셋: NONE, ALL, INS, IND, INALL, MIDD, OUTD, OUTS, OUTALL, ALL0.5
```

X/Y plot 에서 X Types 를 `original weight`, X Values 에 프리셋 전체를 넣어 격자로 비교한 뒤 마음에 드는 것을 고른다. 여러 개를 섞어 쓸 수도 있다 — `<lora:이름:0.5:INALL>, <lora:이름:0.5:MIDD>, <lora:이름:0.3:OUTS>`.

**로라가 많아졌을 때** — 로라 파일과 **같은 이름의 .txt** 에 URL · 버전 · 추천 가중치 · 추천 해상도 · 트리거 워드 · 추가 네거티브를 적어 두고, SublimeText 로 로라 폴더를 열어 `Ctrl+P` 로 찾는 방식이 2023년에 쓰였다. 지금은 Civitai 메타데이터를 읽는 확장(A1111 로라 카드 설명란 · ComfyUI LoraInfo 노드)이 같은 역할을 한다.

**프롬프트만으로 안 나오는 것은 컨셉 로라로** — 예를 들어 `upside-down` 태그만 넣으면 엉뚱한 자세가 나오므로 전용 로라를 쓴다. Illustrious/Pony 계열 컨셉 로라 목록이 civitai 링크로 정리돼 있다(원문 137644242).

> **ComfyUI 주의** — 프롬프트 칸에 `<lora:이름:0.4>` 라고 써도 적용되지 않는다. **로라 로더 노드**로 따로 불러와야 한다.

**같은 모델을 다르게 쓰는 법 — 유틸리티 튜닝 로라**
Civitai 의 `Pony Tweaker Collection` 에 있는 **밝기 / 대비 / 채도 / 선명도 / 윤곽선** 다섯 종을 얹으면
같은 체크포인트로도 전혀 다른 느낌이 나온다. **음수 가중치를 줄 수 있어** 속성을 낮출 수도 있다.

```
예시 A : 밝기 -0.6 / 대비  0.3 / 채도  0.3 / 선명도  0.4 / 윤곽선 0.4
예시 B : 밝기 -0.6 / 대비 -0.6 / 채도 -0.6 / 선명도 -0.2 / 윤곽선 0.2
```

방향 규칙은 한 줄이다 — **다섯을 전체적으로 올리면 애니메이션 풍에 가까워지고, 내리면 일러스트·회화 쪽으로 멀어진다.**
후처리 색보정과 달리 생성 단계에서 개입하므로 **선 자체와 명암 표현이 함께** 달라지고, 적당히 병합해 새 체크포인트로 만들 수도 있다
(akium v3 · IL v14 에서 확인, 2026-05, 한 글에서만 언급됨).

<small>근거 — [preview 및 출처 정리된 LoRa 111개 공유 (씹덕… 23.02](https://arca.live/b/aiart/70646351) · [여러가지 꽤 쓸만했던 로라들 링크 25.05](https://arca.live/b/aiart/137644242) · [CIVITAI 에서 로컬 그림체를 찾는법 ( 똑같이 따라했는… 25.09](https://arca.live/b/aiart/147183795) · [로라 얼굴만, LoRA Block Weight 사용방법 23.03](https://arca.live/b/aiart/71644460)</small>

??? note "근거 5건 전부 보기"
    [preview 및 출처 정리된 LoRa 111개 공유 (씹덕… 23.02](https://arca.live/b/aiart/70646351) · [여러가지 꽤 쓸만했던 로라들 링크 25.05](https://arca.live/b/aiart/137644242) · [CIVITAI 에서 로컬 그림체를 찾는법 ( 똑같이 따라했는… 25.09](https://arca.live/b/aiart/147183795) · [로라 얼굴만, LoRA Block Weight 사용방법 23.03](https://arca.live/b/aiart/71644460) · [같은 모델 다르게 쓰는 법 26.05](https://arca.live/b/aiart/171170750)

## 5. 확장 · 스크립트 · 도구
<small>2026-08 기준 · 근거 11건</small>

```
# EXIF 뷰어 (유저스크립트) — 클릭만으로 프롬프트를 본다
https://greasyfork.org/ko/scripts/464214
  Tampermonkey / Violentmonkey 에 설치. NovelAI · SD WebUI · InvokeAI 의 png/jpeg/webp 지원
  동작 사이트: AI그림채널 · AI그림학습채널 · AI반실사그림채널 · AI실사채널 · 픽시브
  개선판(NAI 드래그 없이도 EXIF 표시): https://arca.live/b/aiart/99243596
  원본 글: https://arca.live/b/aiart/82100684
  · 2.0.0 부터 **글쓰기 창에 직접 드래그앤드롭한 이미지도 'Exif 데이터 보존' 체크 설정을 따른다**(기본값 저장)
  · Greasemonkey 는 API 변경으로 동작하지 않는다 — Tampermonkey / Violentmonkey 만 지원
  · 드래그앤드롭을 가로채 우회 업로드하므로 **이미지가 항상 글 맨 아래로 들어간다**(커서 위치 삽입 불가)
  · ⚠️ 폰카로 찍은 실사를 EXIF 보존으로 올리면 **촬영일시와 GPS 좌표가 노출될 수 있다**

# 프롬프트(EXIF) 추출 유저스크립트 — 마우스만 올려도 EXIF 를 보여 준다 (2023-02)
https://greasyfork.org/scripts/460848-prompt-extractor-user-js/code/prompt-extractoruserjs.user.js
  Violentmonkey 에 설치 (Chrome / Firefox / Edge). PNG·WebP·JPEG 의 EXIF 를 읽는다
  · **LoRA 정보는 표시되지 않는다**
  · 파란 로딩 아이콘만 계속 도는 것은 대개 **그 그림에 EXIF 가 없어서**다
  · 2023년 자료라 지금 채널 구조에서의 동작은 확인이 필요하다 → 더 최신은 위 EXIF 뷰어 3.0

# 태그 자동완성 (A1111 계열)
https://github.com/DominikDoom/a1111-sd-webui-tagcomplete
  · 로컬이 아니라 서버를 열어 원격 접속하면 동작하지 않는다

# triton + sageattention 인스톨러
https://github.com/DazzleML/comfyui-triton-and-sageattention-installer
https://github.com/DazzleML/comfyui-triton-and-sageattention-installer/releases
  · ComfyUI 폴더에서 git clone 후 포터블 내부 파이썬으로 --install

# ComfyUI 본체 / 매니저
https://github.com/Comfy-Org/ComfyUI
https://github.com/Comfy-Org/ComfyUI-Manager

# 라데온(ROCm on Windows 11)용 SageAttention 빌드 참고
https://github.com/thu-ml/SageAttention/pull/368
https://github.com/linkdesu/task-skills/tree/main/skills/build-sageattention-rocm-on-win11
  · 배포된 whl 링크(https://kio.ac/c/d9yR2HAEWXHBP2YWty5z8b)는 30일 만료 — **링크 죽음** 가능성 높음

# 프롬프트 확장 (WebUI Neo)
확장기능에서 "all-in-one" 으로 검색 (sd-webui-prompt-all-in-one)
  · 압축 해제 후 \WebUI Forge - Neo\extensions 에 넣는다

# 로라 관리
ComfyUI-Lora-Manager
  · ANIMA 는 models/diffusion_models 에 있어야 하므로 mklink /J 정션 필요

# 포토샵 연동 (2023-01, A1111 시대)
https://github.com/AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin
```

<small>근거 — [최근 연달아 업데이트 한 EXIF 뷰어 기능 소개함 23.03](https://arca.live/b/aiart/70916246) · [프롬프트(Exif) 추출 유저스크립트 23.02](https://arca.live/b/aiart/70755960) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [챈에서 nai 짤 프롬 확인하는법 23.12](https://arca.live/b/aiart/94872564)</small>

??? note "근거 11건 전부 보기"
    [최근 연달아 업데이트 한 EXIF 뷰어 기능 소개함 23.03](https://arca.live/b/aiart/70916246) · [프롬프트(Exif) 추출 유저스크립트 23.02](https://arca.live/b/aiart/70755960) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [챈에서 nai 짤 프롬 확인하는법 23.12](https://arca.live/b/aiart/94872564) · [(WebUI 기본 확장기능) 프롬프트 자동완성 tag-aut… 23.02](https://arca.live/b/aiart/70421901) · [AI 이미지 EXIF 뷰어 - 드래그+드롭 업로드 EXIF … 23.05](https://arca.live/b/aiart/76070805) · [Anima 찍먹해보기 - 아니마 체크포인트, 로라 다운로드 26.05](https://arca.live/b/aiart/171506089) · [Comfy로 anima 실행 및 최적화하기 26.06](https://arca.live/b/aiart/175408089) · [미니맥스 속도 캐싱 3종세트 안되는 사람들 26.08](https://arca.live/b/aiart/179226965) · [라데온 sageattention whl로 만들어왔어 26.08](https://arca.live/b/aiart/179413848) · [ComfyUI에서 Muse Glimmer 찍어 먹어보기 26.08](https://arca.live/b/aiart/179575129)

## 5-b. 옛 확장·스크립트 (2023) — 지금은 무엇이 대신하나
<small>⚠️ 2023-04 기준 · 근거 2건</small>

2023년 A1111 전성기의 자료다. **지금 그대로 받아 쓸 것은 없다** — 무엇이 대신하는지와 함께 남긴다.

| 옛 것 | 시점 | 지금 무엇이 대신하나 |
|---|---|---|
| **ddsd** (DDetailer + Upscaler 통합 확장) | **2023-04** | **ADetailer** 또는 **ComfyUI 의 디테일러 노드** |
| **딥단부루 태그 변환 파이썬 스크립트** | **2023-02** | **WD14 Tagger** (`wd-eva02-large-tagger-v3` 등) — ComfyUI·WebUI 확장으로 내장돼 있다 |

### 딥단부루 태그 변환 스크립트 (2023-02)

DeepDanbooru(`https://huggingface.co/spaces/hysts/DeepDanbooru`)에 이미지를 넣으면
`1girl 100% / breasts 99% / leotard 95% ...` 처럼 태그와 확률이 줄줄이 나온다.
이걸 복사해 넣으면 `(1girl), (breasts), (leotard), ...` 형태로 정리해 주는 작은 스크립트였다.

```text
https://mega.nz/file/cplnjIrY#PCOvCgRmlt0FrFGP9GHoXlvnzniOfoQ7DN-tLUKC1GI   (exe 빌드 없이 .py 그대로)
```

> **지금 이 스크립트를 쓸 이유는 거의 없다.** WD14 Tagger 가 태그를 **쉼표로 구분된 프롬프트 형식으로 바로 뱉는다.**
> 소괄호로 감싸는 것도 당시 A1111 의 강조 문법(**괄호 1겹 = 1.1배**)을 노린 것인데,
> 요즘은 `(tag:1.1)` 로 수치를 직접 쓴다.
>
> 살아남는 것은 **'이미지에서 태그를 역추출해 프롬프트로 되돌린다'는 발상** 자체이고,
> 그것이 지금의 태거·VLM 캡셔닝으로 그대로 이어진다.

### ddsd 확장 (2023-04) — 두 가지가 지금도 읽을 값이 있다

**① 확장이 특정 torch 버전에 묶이는 문제의 전형적 사례**

배포 방식을 파일 직접 배포에서 **깃허브 URL 설치**로 바꾸면서 버전 충돌을 막으려고 **종속성 패키지 버전을 아예
고정해 버렸다.** 그 부작용을 제작자가 예고했고, 댓글 7 에서 실제로 확인됐다.

```text
torch 2.0        →  오류가 쏟아진다
torch 1.13.1+cu117 →  잘 작동한다
```

**② ControlNet 이미지 랜덤 — '기대 가능한 타율의 랜덤'**

텍스트박스에 **glob 경로**를 넣으면 그 폴더의 이미지 중 하나를 무작위로 뽑아 쓴다.

```text
D:\Insta-v10\*.png
```

이걸로 OpenPose 포즈를 랜덤으로 돌리며 뽑을 수 있는데, **여기서 나온 통찰이 지금도 유효하다** —
약 100장을 돌려 90~95장을 건졌고, **못 건진 5장의 원인은 ControlNet 이미지와 출력 이미지의 비율이 달라
ControlNet 이미지가 잘리면서 얼굴이 잘려 나간 것**이었다.
즉 **동일한 비율의 포즈 레퍼런스만 모아 그 비율로 돌리면 타율이 크게 오른다.** → [컨트롤넷](controlnet.md)

> **곁다리로 정리된 개념 하나** — **DDetailer 는 자동으로 검출한 영역만 고쳐 주는 기능이고,
> 내가 칠한 부분만 고치는 것은 인페인팅이다**(댓글 10~16).
> → [디테일러](detailer.md) · [인페인팅](inpainting.md)

*⚠️ 위 두 건 모두 **2023년 SD1.5·A1111 시절** 자료다. 이번 정리에 들어온 자료의 97% 는 2025~2026년 것이고,
이 둘만 예외적으로 오래됐다.*


<small>근거 — [ddsd 옵션 업데이트(필수X)(약스압 주의) 23.04](https://arca.live/b/aiart/74090707) · [사소한거)딥단부루 태그 변환 파이썬파일임 23.02](https://arca.live/b/aiart/69903265)</small>

## 5-c. GPU 가 없을 때 — 클라우드로 로컬 워크플로우 돌리기 (Vast.ai · RunPod)
<small>2025-12 기준 · 근거 2건</small>

**GPU 가 없거나 사양이 모자라도 로컬과 똑같은 ComfyUI 워크플로우를 돌릴 수 있다.** 시간 단위로 남의 GPU 를 빌리는
것이고, 채널에 실제 세팅기가 두 편 있다. 둘 다 *"초기화된 PC 를 매번 빌리는 것"* 이라는 점이 핵심이라
**세팅 반복을 없애는 장치(프로비저닝 스크립트 · 도커 이미지)** 를 갖추는 것이 절반이다.

| | Vast.ai (2025-12) | RunPod (2025-10) |
|---|---|---|
| 무엇을 하나 | `ai-dock/comfyui` 를 포크해 **모델 목록을 스크립트로 관리** | **딸깍 도커 이미지**(WAN 2.2 전용)를 받아 쓴다 |
| 단가 | RTX 5090 · 디스크 40GB 기준 **시간당 0.31~0.40 USD** | (본문에 단가 표기 없음) |
| 최소 충전 | 본문 10 USD → **댓글에서 실제로는 5 USD** 로 정정 | — |
| 데이터 전송 | **약 0.003 USD/GB** (34.9GB 다운로드에 총 −0.09 USD, 댓글) | — |
| 정지 중 보관비 | 40GB 기준 **하루 약 0.53 USD** | — |
| 결과물 회수 | **Syncthing** 실시간 동기화 | (내장 워크플로우로 처리) |

### Vast.ai — 프로비저닝 스크립트를 자기 것으로 만든다

```text
템플릿    https://cloud.vast.ai?ref_id=62897&template_id=53478aac54ffed2deace9e69d93e52dc
CUDA      edit 에서 cuda-12.9-auto 선택   (5090 속도 저하 방지)
Key       CIVITAI_TOKEN = 발급받은 토큰   ← 값을 넣고 옆의 [+] 버튼을 반드시 눌러야 추가된다
          HF_TOKEN 도 같은 식 (접근 권한이 필요한 모델을 받을 때만)
```

포크할 저장소는 `https://github.com/ai-dock/comfyui` 이고, 고칠 파일은 `config/provisioning/default.sh` 하나다.

```text
① Ctrl+F 로  ESRGAN_MODELS  →  UPSCALE_MODELS  전체 치환
   (현 ComfyUI 와 폴더 경로가 다르기 때문이다. 이걸 안 하면 업스케일 모델이 엉뚱한 곳에 받아진다)
② 기본으로 박혀 있는 huggingface 링크들은 기초 모델이라 다 지우고 괄호 사이에 자기 모델 링크를 채운다
   · 앞에 탭 공백이 있어야 하고 링크는 큰따옴표 안에 넣는다
   · civitai  : 다운로드 버튼 우클릭 → 링크 주소 복사
                예) https://civitai.com/api/download/models/2260110?type=Model&format=SafeTensor&size=pruned&fp=fp8
   · 허깅페이스 : Copy download link
   · 링크 앞에 # 을 붙이면 주석 처리되어 그 파일만 건너뛴다
③ NODE 항목에는 커스텀 노드 깃허브 링크를 넣는다
④ Commit → Raw 클릭 → 주소를 PROVISIONING_SCRIPT 값에 붙여넣는다
   https://raw.githubusercontent.com/<깃허브ID>/comfyui/refs/heads/main/config/provisioning/default.sh
```

| 항목 | 값 |
|---|---|
| 저장공간 | **설정한 모델 총합 + 20GB** (체크포인트 2개 + 로라 몇 개면 40GB, Wan 을 쓰면 65GB) |
| **저장소 공개 여부** | **반드시 Private.** 아니면 스크립트에 든 API 토큰이 다 털린다 |

### 결과물 받아 오기 — Syncthing

| 쪽 | 설정 |
|---|---|
| 로컬(받는 쪽) | `http://127.0.0.1:8384` → 폴더 추가 → 고급 설정에서 폴더 유형 **'수신 전용'**, 파일 수신 순서 **'오랜 파일 순'** (무작위 다운로드로 인한 경로 불안정 방지) |
| 원격(보내는 쪽) | 폴더 경로 `/workspace/ComfyUI/output` (ai-dock 공통), 폴더 유형 **'송신 전용'** |
| 양쪽 공통 | 고급 설정에서 압축을 **'하지 않음'** 으로 (EXIF 보존 + 업로드 속도 향상) |

> ⚠️ 공유 설정에서 폴더를 선택하되 **자물쇠는 절대 누르지 마라 — 파일이 다 깨진다.**

### ⚠️ 인스턴스는 뽑기다 — 버릴 기준을 먼저 정해 둔다

**두 글이 공통으로 강조하는 것**이 이것이다. 나쁜 서버를 붙들고 있으면 그 시간이 전부 요금이다.

| 신호 | 판단 |
|---|---|
| **다운로드 속도 10MB/s 이하** | **그 인스턴스는 버리고 새로 빌려라.** 한 시간 돌려도 안 끝난다 |
| 로그에 `comfyui startup paused until instance provisioning has completed` 만 **15분 이상** | 인스턴스가 맛이 갔다. 재실행하거나 다른 서버로 |
| RunPod 에서 `CUDA initialization failed. Exiting...` 뜨며 모델 다운로드 멈춤 | **그 서버의 GPU 가 고장난 것**이다. 포드를 빨리 버리고 새로 만든다 (모델 다운로더가 일부러 간단한 작동 테스트를 한다) |

**서버 고르는 법** — 정렬을 `Price(inc.)` 로 바꾸고 GPU 를 좁힌 뒤 **카드의 숫자를 본다.**

```text
↑ 업로드 속도    Syncthing 회수 속도
↓ 다운로드 속도 · 포트 수    초기 구성 시간
시스템 메모리 (64/258GB = 내가 쓸 수 있는 양 / 서버 최대)
디스크 대역폭 (예 2588 MB/s)   ← 최소 2000 이상
```

> 파키스탄·인도·독일 서버는 실제 다운로드가 박살나는 경우가 있어 피한다는 것이 작성자의 경험칙이다.
> Vast 의 서버 타입은 **Secure**(비싸지만 다운로드 문제가 적음) / **Community**(저렴) / **Spot**(더 싸지만
> 여유 자원이 없으면 랜덤하게 뺏김) 이고, 작성자는 온디맨드를 쓴다.

### RunPod — WAN 2.2 딸깍 도커 이미지

```text
바로 가기   https://console.runpod.io/deploy?gpu=RTX+5090&count=1&template=9lkpdziphh
템플릿명    rhplus-comfyui-video          (템플릿 검색으로는 안 뜰 수 있다)
⚠️ CUDA 12.9 기준으로 빌드했으므로 CUDA 버전 제한을 12.9 이상으로 수동 설정해야 한다
```

| 항목 | 값 |
|---|---|
| 모델 볼륨 | 전부 받으면 **약 90GB** (모델 2개만이면 46GB 이므로 60~70GB 로도 가능) |
| 결과물 볼륨 | **10GB** 정도 |
| 모델 링크 | 세미콜론으로 구분해 `A;B;C` 로 넣으면 포드가 켜질 때 `diffusion_models` 폴더로 자동 다운로드 |
| 접속 | `Download Done!` 과 `0.0.0.0:8188` 이 뜨면 Connect → ComfyUI (2분 기다려도 안 뜨면 `Ctrl+F5`) |
| 실측(720p 급, 업스케일 + 보간 포함) | 기본 샘플러 **약 160초** / 스케줄드 샘플러 **약 200~240초**(역동적 동작에 유리) |

### 공통 — 끝나면 반드시 정리한다

포드를 켜 둔 채로 두면 크레딧이 계속 샌다. **정지(■)** 하면 스토리지 보관비만 나가고, **휴지통 삭제**는 모든
데이터가 사라진다. Vast 는 인스턴스를 지우면 받아 둔 모델도 같이 사라지므로, 다음에 또 쓸 거라면
프로비저닝 스크립트를 잘 만들어 두는 쪽이 결국 싸다.

*(2025-10 ~ 2025-12. 단가와 UI 는 바뀔 수 있으니 실제 화면의 숫자를 확인할 것. 로컬 설치는
[설치와 환경 구성](install.md), 워크플로우 자체는 [ComfyUI 쓰는 법](comfyui.md) 을 보라.)*


<small>근거 — [30분내로 끝내는 Vast.ai 사용법 (시간당 0.3$로 … 25.12](https://arca.live/b/aiart/158013422) · [런팟 RTX 5090용 WAN 2.2 딸깍 도커 이미지 25.10](https://arca.live/b/aiart/151440980)</small>

## 6. 와일드카드 · 태그 · 작가 데이터
<small>2026-04 기준 · 근거 11건</small>

```
# ANIMA 용 아티스트 와일드카드 — 이스케이프와 @ 접두사가 이미 적용돼 있다
https://huggingface.co/arcacolab/foranima/tree/main/artist_txt
  풀버전 + 태그 카운트 하한 50/100/150/200/250 총 6개 버전
https://huggingface.co/arcacolab/foranima/tree/main/characters_txt
  캐릭터명만 남긴 것 — 복장 와일드카드와 합쳐 쓰는 용도

# 원본 태그 아카이브
https://github.com/DraconicDragon/dbr-e621-lists-archive/blob/main/tag-lists/danbooru/danbooru_2025-09-01_pt20-ia-dd.csv

# 작가 태그 조합 미리보기
https://thetacursed.github.io/Anima-Style-Explorer/index.html    # 996개 그림체를 생성 샘플과 함께
https://conaitagdex.com/?lang=ko                                  # 긍정·부정 조합 프리뷰 + 랜덤 추출 API

# 아티스트 썸네일 60,000장 (NAIA 2.0)
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/Anima_artist_thumbnail/artist_thumbnail_anima.zip
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/Anima_artist_thumbnail/artist_thumbnail_anima_bucket2.zip
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/Anima_artist_thumbnail/artist_thumbnail_anima_bucket3.zip
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/Anima_artist_thumbnail/artist_viewer.zip

# 니케 캐릭터 영문명 와일드카드 (NovelAI 4.5)
https://drive.google.com/file/d/1SyiXlUi3VjatGu63afBw-7v2dpAxBzxy/view
```

> **2022년 대형 한국어 태그 분류 사전(8.8만 자)은 참고용으로만.** 실제 단부루 태그가 아닌 창작 태그(`yellow_man`, `Eastern_Quota` 등)와 오기가 섞여 있다 — '배경/무늬' 항목에 legwear·panties 가 들어가 있고, 인원 항목에 존재하지 않는 `1boys`·`1girls` 가 적혀 있다.


### 배포된 와일드카드 팩 셋 — 수집 조건까지 공개된 것부터 본다

| 팩 | 무엇 | 받는 곳 · 주의 |
|---|---|---|
| **ANIMA/NAI 아티스트 와일드카드 `petit_tags.zip`** (2026-02) | **수집 조건이 공개돼 있는 것**이 값어치다. `6_100` = 2024~2025년 11월 활동 이력 + danbooru post **51건 이상** + 해당 태그 비율 **6% 이상** / `2_6` = 같은 조건에 비율 **2~5.99%** / `1_2` = post **100건 이상**에 비율 **1~1.99%**. 파일명 앞뒤 숫자는 그 파일 안 최고·최저 count 다 | `https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/Beta/petit_tags.zip` · **표기가 두 벌** — 기본 폴더는 ANIMA 형식(`@leafy \(kitsuneya\)`), NAI 폴더는 `leafy (kitsuneya)` 형식. 동봉 엑셀에 태그 포함/비포함 포스트 수가 들어 있다 |
| **개인용 와일드카드 팩** (2026-02) | 채널·Civitai·구글·레딧에서 긁어 모은 로컬용. `CnB`(옷+배경 조합) · `Rantheme` · `CHAR`(블루아카이브·단부루 여캐·니케·버튜버, 2025년 초 기준) · `SEXO V2` · `SFW` / `PRAN` · `NSFW`. `RanartistALL` · `RanartistP` 는 작가만 들어 있으니 제외 | 본체는 kio.ac (base64) — **만료 유력**. 출처 Civitai 링크가 살아 있으니 거기서 개별 수급하는 편이 낫다: `https://civitai.com/models/1796346/go-to-sfw-image-wildcards` · `https://civitai.com/models/2063675/nsfw-collection-promts-wildcard` · ⚠️ **NSFW 폴더는 이상성욕 필터링이 전혀 되어 있지 않다** |
| **1girl, solo 짤멍용 풀랜덤 세트** (2026-04) | `original_characters.txt` · `original_outfit.txt` · `original_pose.txt` 3종에 포즈는 등급별로 갈린다 | `https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/NAIA_2025/many_wildcards.zip` · 아래 등급표 참조 |

```text
포즈 파일 등급 접미사 (작성자가 댓글에서 설명)
  q · e   선정적인 자세 위주   (q 가 다양성이 높고 e 는 덜 다양)
  s       표준
  g       건전

e 에도 야짤 태그 자체는 들어 있지 않다. 그래서 이렇게 나열해야 한다
  __original_pose_e__, nsfw, rating:explicit

세트 전체가 ~medium breasts 정도의 몸매에 최적화돼 있고
loli / flat chest / small breasts 태그는 아예 들어 있지 않아 NAI 공식 웹에서도 처리된다
```

> ### ⚠️ 작성자 본인이 낮춰 평가한 자료다
>
> 위 풀랜덤 세트에 대해 **배포자가 댓글에서 직접 말했다** — *"돌려 보면 조합이 생각보다 단조롭고 프롬프트가
> 길지 않아 재미가 떨어진다. **포즈는 비실용적이고 캐릭터와 의상을 넣는 쪽이 제일 낫다.**
> 그냥 랜덤 프롬프트를 쓰는 것과 큰 차이는 없고 '포즈를 돌릴 때 의상을 완전 랜덤으로 할 수 있다' 정도가 차이다."*
>
> 받아서 쓸 때는 **캐릭터·의상 파일만** 쓰는 편이 낫다. 특정 구도·의상을 빼고 싶으면 txt 파일을 AI 에게 던져
> 지워 달라고 하면 된다. 와일드카드를 처리할 도구(WebUI / ComfyUI / NAIA)는 따로 필요하다.

### 프롬프트 원본을 통째로 긁어 둔 데이터셋 (2025)

```text
# 아카라이브 AI그림채널 NAI 탭 념글 크롤링 데이터셋
정식판  https://huggingface.co/datasets/pls2000/aiart_channel_nai_geachu_20250524_20240909
        2024-09-09 ~ 2025-05-24, 약 94GB
긴급판  https://huggingface.co/datasets/pls2000/aiart_channel_nai_geachu_emergency
        아카라이브 이미지 서버가 잠깐 정상화됐을 때 급히 받아 둔 것 (NAI 념글 4261번부터 12페이지)

구성    추천 수만큼 폴더에 숫자로 정리 + 각 이미지 exif 의 프롬프트를 txt 로 함께 저장
```

| ⚠️ 주의 | 내용 |
|---|---|
| 쓰레기가 섞여 있다 | 페이지를 이미지 태그로 통째로 긁은 것이라 아카콘·스크린샷이 섞인다 → **exif 가 있는 것만** 골라 쓴다 |
| 부분 지정 누락 | NovelAI 의 캐릭터별 프롬프트(`character 1 prompt`)는 포함되지 않았다 |
| 정식판끼리 중복 | 이전 데이터셋과 **2024-09-09 ~ 2024-09-20** 구간이 겹친다 |
| **긴급판의 한계** | 다운로드 직후 이미지 서버에 다시 제한이 걸려 **열화를 피할 수 없고 exif 도 불안정하다.** 작성자가 **"고화질 원본 png 만 추출해 쓰라"** 고 명시했다. 압축 안의 `__MACOSX` · `.DS_Store` 는 지워도 무방 |

> 허깅페이스 데이터셋은 언제까지 남아 있을지 보장이 없다. 용량이 커서 못 받겠다는 반응이 많았고,
> 추천 높은 것만 따로 받는 방법은 제공되지 않는다.

→ 문법은 [프롬프트 쓰는 법](prompting.md)

<small>근거 — [태그 종류 22.10](https://arca.live/b/aiart/61336136) · [ai 그챈 nai 탭 념글 긁은 데이터셋 20240909~2… 25.05](https://arca.live/b/aiart/137717097) · [ai 그챈 nai 탭 념글 긁은 긴?급  데이터셋 25.06](https://arca.live/b/aiart/139830572) · [아니마 가능)싹싹 긁어 모은 개인용 와일드카드 팩 26.02](https://arca.live/b/aiart/162850344)</small>

??? note "근거 11건 전부 보기"
    [태그 종류 22.10](https://arca.live/b/aiart/61336136) · [ai 그챈 nai 탭 념글 긁은 데이터셋 20240909~2… 25.05](https://arca.live/b/aiart/137717097) · [ai 그챈 nai 탭 념글 긁은 긴?급  데이터셋 25.06](https://arca.live/b/aiart/139830572) · [아니마 가능)싹싹 긁어 모은 개인용 와일드카드 팩 26.02](https://arca.live/b/aiart/162850344) · [anima모델용 그림체(996)모음 사이트 26.02](https://arca.live/b/aiart/161801344) · [1girl, solo짤멍용 3+4종 풀랜덤 와일드카드 26.04](https://arca.live/b/aiart/166767807) · [페) 농농단용 ANIMA/NAI 아티스트 와일드카드 26.02](https://arca.live/b/aiart/161289775) · [NAIA2.0용 Anima 아티스트 썸네일 60000 및 뷰… 26.05](https://arca.live/b/aiart/170828753) · [ANIMA 아니마용 아티스트 와일드카드 26.02](https://arca.live/b/aiart/162852234) · [아니아니마용 작가 조합 테스트웹 26.05](https://arca.live/b/aiart/171805357) · [니케 영문명 와일드카드 26.02](https://arca.live/b/aiart/161378127)

## 6-b. 태그 사전과 자세 카탈로그 — 무슨 태그를 써야 할지 모를 때
<small>⚠️ 2023-11 기준 · 근거 9건</small>

"무슨 태그를 써야 하는지 모르겠다" 는 문제를 푸는 자료들이다.
**전부 2022~2023년 자료**라 예시 이미지는 SD1.5·NAI V3 로 뽑은 것이지만,
**danbooru 태그 체계 자체는 지금 Illustrious·NoobAI·ANIMA 계열에도 그대로 통한다.**
다만 태그의 반영 강도는 모델 세대에 따라 달라진다 — 같은 자세 태그가 SD1.5 에서는 타율이 낮았는데 NAI V3 는 다 알아들었다는 보고가 있다.

**태그 시각 카탈로그 4부작 (2022-11)** — 태그를 하나씩 단독으로 돌려 결과 이미지와 함께 정리한 것

```
1편  작화 · 초점 · 가족 · 직업 · 체형   https://arca.live/b/aiart/62521936
2편  머리 모양 · 얼굴 모양 · 표정        https://arca.live/b/aiart/62522258
3편  가슴 · 엉덩이 · 자세                https://arca.live/b/aiart/62522504
4편  의상                                https://arca.live/b/aiart/62522931
```

테스트 방법이 명확해서 값이 있다 — 부가 태그를 최대한 배제하고
`best quality, masterpiece, high quality, (시험할 태그:1.3), 1girl, cowboy shot,` 형식으로만 뽑았다.
즉 **어떤 태그가 그 자체로 힘이 있는지**를 가려낸 자료다.

**자세 태그 모음 4부작 (2023-11, NAI V3 기준)** — ControlNet 을 쓸 수 없는 NAI 사용자를 위해 만들어진 것

```
1편  전신 자세          https://arca.live/b/aiart/91985399
2편  눕기 · 기대기 · 몸통  https://arca.live/b/aiart/91988777
3편  표정 · 입 동작      https://arca.live/b/aiart/91992716
4편  팔 · 손 동작        https://arca.live/b/aiart/91997326
```

작성자가 "남들 다 아는 대중적인 프롬프트는 일부러 뺐다"고 밝혔으므로 `smile`·`blush` 같은 기본 표정 태그는 여기 없다.

> **이 시리즈들이 공통으로 알려 주는 것 — 태그는 단독으로 쓰면 타율이 낮다.**
> 손·발·성기 등 신체 부위 태그는 단독 사용 시 정상 이미지가 안 나오는 확률이 높고,
> `battoujutsu_stance` 는 칼 태그와, `upside-down`·`squatting` 은 `spread legs` 와,
> `fetal_position` 은 앉기/눕기 태그와 함께 써야 한다.
> 대상이 애매한 태그(`arm grab`, `covering mouth`, `pointing`, `lick`)는 **대상을 따로 명시**한다.

**NAI V3 를 쓸 때의 표기 함정** — 단수와 복수를 명확히 구분해 `arm` 과 `arms` 가 다르고,
`arm up` 은 팔을 쫙 뻗는 느낌이 아니다. `torso` 처럼 잘 안 먹는 태그는 `leaning_forward`·`bent_over` 같은
구체적 자세 태그로 대체하고, `thumbs up` 은 되지만 `thumbs down` 은 안 된다.

**크기·그림체 태그**

| 갈래 | 정리 |
|---|---|
| 가슴 크기 | `flat chest` < `small breasts` < `medium breasts` < `large breasts` < `huge breasts` < `gigantic breasts` < `enormous breasts`. `large` 는 머리 크기와 비슷하거나 조금 넘고 `gigantic` 은 머리의 2배. **`huge` 이상부터는 AI 가 크기를 최우선 처리해 취할 수 있는 포즈가 제한된다** (원문 62652820) |
| 작품 그림체 | 작품 이름 뒤에 `_style` 을 붙인다. 눈매가 가장 크게 바뀌고 구작일수록 잘 먹힌다. **부작용** — `naruto_style` 은 나루토 본인이 섞이고, 원피스는 옷 원피스와 충돌하며, `neon_genesis_evangelion_style` 은 옷이 플러그슈트로 바뀐다. 캐릭터 혼입을 피하려면 작품명 대신 **`drawn by 작가이름`** 을 쓴다 (원문 63524889) |
| 작가 태그 (NAI) | `artist:작가명` 형식. danbooru 작가 태그 체계라 Illustrious/NoobAI 에서도 일부 통한다. 로컬에서는 괄호를 `\(...\)` 로 이스케이프할 것. 검증된 24선 목록 `https://arca.live/b/aiart/94333373` |

**성인 태그 대응표** — `https://arca.live/b/aiart/67516417`
부위 / 상태 / 도구 / 인원 / 설정 / 체위 / 애무 / 삽입·사정 / 표정 9개 분류이며,
`cum in 부위` · `cum on 부위` · `penis in 옷` · `vibrator in/under 부위` · `after 행위` ·
`implied 행위` · `cooperative 행위` · `double/triple 행위` 같은 **명명 패턴이 반복돼 규칙을 익히면 응용이 된다.**

→ 문법과 태그 고르는 법은 [프롬프트 쓰는 법](prompting.md)

<small>근거 — [태그 + 실제 테스트 결과 이미지 1편 (작화, 초점, 가족… 22.11](https://arca.live/b/aiart/62521936) · [그림체변경 유의미한 특정작품 프롬 모음 v1.2 22.11](https://arca.live/b/aiart/63524889) · [후방) 가슴 크기에 관한 연구 (시각자료 있음) 22.11](https://arca.live/b/aiart/62652820) · [주워옴 섹스 관련 태그 모음 23.01](https://arca.live/b/aiart/67516417)</small>

??? note "근거 9건 전부 보기"
    [태그 + 실제 테스트 결과 이미지 1편 (작화, 초점, 가족… 22.11](https://arca.live/b/aiart/62521936) · [그림체변경 유의미한 특정작품 프롬 모음 v1.2 22.11](https://arca.live/b/aiart/63524889) · [후방) 가슴 크기에 관한 연구 (시각자료 있음) 22.11](https://arca.live/b/aiart/62652820) · [주워옴 섹스 관련 태그 모음 23.01](https://arca.live/b/aiart/67516417) · [Nai 사용자를 위한 자세 모음 1편 23.11](https://arca.live/b/aiart/91985399) · [(Nai)내가 보려고 만든 작가 정보 24선 23.12](https://arca.live/b/aiart/94333373) · [Nai 사용자를 위한 자세 모음 4 23.11](https://arca.live/b/aiart/91997326) · [Nai 사용자를 위한 자세 모음 2 23.11](https://arca.live/b/aiart/91988777) · [Nai 사용자를 위한 자세 모음 3 23.11](https://arca.live/b/aiart/91992716)

## 6-c. 채널 자작 도구 — 메타데이터를 읽고·고치고·정리한다
<small>2026-06 기준 · 근거 37건 · 자료 엇갈림</small>

채널 사람들이 직접 만들어 배포한 도구들이다. **앞선 정리에서 자료만 모아 두고 문서에 옮기지 못했던 것들을 여기 싣는다.**

> ⚠️ **비공식 NAI 클라이언트를 받기 전에 — 막힌 것이 아니라 길이 바뀌었다.**
> 2026년 중반 NovelAI 가 로그인 API 에 reCAPTCHA 를 도입하면서 **이메일·비밀번호 로그인은 더 이상 못 쓴다**
> (재로그인하면 `please refresh novelai.net` 이 뜬다 — 관련 글 `https://arca.live/b/aiart/176933271`).
> **대신 `Persistent API Token` 을 쓰면 지금도 된다.** NovelAI 도 서드파티 앱에 그쪽을 쓰라고 권고했고,
> NAIApp · NAI-Auto-Generator · NAI Helper · NAIA 는 모두 토큰 방식으로 정식 업데이트됐다.
>
> ```text
> NovelAI 웹 로그인 → 좌측 상단 설정(톱니) → Account → Get Persistent API Token → 앱의 'API 키' 칸에 붙여넣기
> ```
>
> 토큰은 `pst-` 로 시작하고, **Overwrite 로 새로 발급하면 기존 토큰이 무효화되므로** 같은 토큰을 쓰던 다른 앱도
> 전부 새로 등록해야 한다. 2026-07 에 API 서버 주소가 `api.novelai.net` → `image.novelai.net` 으로 옮겨진 것과
> 겹쳐 400 오류가 한꺼번에 터졌으니, **쓰는 도구를 최신판으로 올리는 것이 첫 번째 답**이다.
> 절차와 오류 메시지는 [NovelAI](nai.md) 의 'Persistent API Token' 항목에 정리돼 있다.

**(가) 메타데이터를 읽고 고치는 것**

| 도구 | 무엇을 하나 | 받는 곳 · 주의 |
|---|---|---|
| **EXIF-II** v2.3.4 (2023-08~) | Windows 10/11 전용 무료 AI 메타데이터 뷰어. 로컬 이미지와 **웹 URL 이미지**를 드래그앤드롭으로 조회하고, 모델·해시 추적 검색, `.TXT` 추출, PNG→JPG 변환 시 메타 복제 보존, EXIF 전체 삭제, **NAI 의 PNG·WebP 스텔스 정보**까지 찾아낸다 | `https://rentry.co/ri2aixz8` · **백신이 `Trojan:Script/Wacatac.B!ml` 로 오탐**하므로 화이트리스트 등록 필요. 원본 메타가 삭제됐거나 RGBA 의 A 채널이 지워졌거나 JPG 로 변환된 이미지는 탐지 불가 |
| **프롬프트 간편 복사기** (2026-07) | 윈도우 탐색기에서 **우클릭만으로** 이미지·영상의 긍정 프롬프트를 클립보드에 복사. PNG(A1111 `parameters` / ComfyUI `prompt`·`workflow` / NovelAI `Description`), JPEG·WEBP(EXIF `UserComment`), MP4·WEBM·MKV(VHS Video Combine·SaveVideo) 를 읽고 **KJNodes 의 GetNode/SetNode 를 최대 12단계까지 거슬러 추적**한다 | `python install_menu.py` 로 레지스트리 등록 / `uninstall` 로 해제. **배포 링크는 2026-08-07 만료 — 링크 죽음** |
| **프롬 수정 프로그램 + wlsh_nodes 수정본** (2026-07) | 이미지에 박힌 프롬프트를 **고친다.** 프롬프트 실시간 검색, 자주 쓰는 세트 목록, 폴더 내 이미지의 특정 프롬프트 포함/미포함 필터링. **이 프로그램으로 수정하면 파일 생성 날짜가 바뀌지 않아** 날짜순 관리가 깨지지 않는다 | 프로그램 `https://naver.me/5VxFOsKM` (실행.bat) · 노드 수정 파일 `https://naver.me/5Hyj1P1y` (`wlsh_nodes` 를 먼저 설치하고 `ComfyUI/custom_nodes/wlsh_nodes/` 에 덮어쓴다). `exiftool` 이 필요하다. **분리 규칙 — `Negative prompt:` 문자열 앞을 positive, 뒤를 negative 로 뱉는다** |
| **EXIF 뷰어 3.0** (2026-01) | 단일 HTML 파일. 업로드·드래그앤드롭·클립보드로 이미지를 넣으면 긍정·부정 프롬프트와 설정값·사용 리소스를 카드로 정리해 보여 주고 편집·복사·일괄 저장·로컬 라이브러리 분류·태그 빈도 통계까지 한다. **NAI → ComfyUI 문법 변환** 출력 옵션이 있다 | 본문 base64 를 풀면 `https://mega.nz/folder/GbAUwRpQ#TZqYsVswygbfyZ3ZFeIrvA` · ComfyUI 파서가 **A(범용) / B(서브그래프 복잡도가 높을 때)** 둘이라 안 읽히면 바꿔 본다. 클립보드 붙여넣기는 EXIF 가 온전해야 해서 **드래그앤드롭이 가장 확실**하다. **가중치 값 변환은 의도적으로 넣지 않았다** — 단순 곱하기로는 결과가 나빠서, 변환된 프롬프트를 참고해 다시 만드는 편이 낫다 |

**(나) 쌓인 그림을 정리하고 찾는 것**

| 도구 | 무엇을 하나 | 받는 곳 · 주의 |
|---|---|---|
| **Konomi** (2026-04) | AI 생성 이미지 **정리·검색 전용** 데스크톱 앱(**생성 기능은 없다**). 폴더를 등록하면 프롬프트 메타데이터를 읽어 검색·중복 검출·유사 이미지 묶기를 한다. 0.12.x 에서 썸네일 제공과 pHash 스트리밍 디코딩(이미지당 4.5MB→6KB)으로 메모리를 최대 50% 줄이고 유사도 계산을 최대 22배 빠르게 했다 | 등록한 폴더에 자동 생성 이미지를 계속 저장하면 새로고침이 잦아 사용성이 떨어진다(본문 명시). 네거티브 프롬프트도 검색에 기본 포함된다 |
| **CoNAI** (2026-03 개명, 옛 ComfyUI-Image-Manager) | 이미지·영상 관리 + NAI/ComfyUI 통합. NAI Vibe/Reference 저장, **NAI 와 ComfyUI 의 설정을 모듈로 만들어 워크플로우로 조합**(NAI 로 뽑고 ComfyUI 로 i2i 하는 구성), rgthree Power Lora Loader 지원, 메타정보 수정, 프롬프트 기준 유사·중복 이미지 표시 | `https://github.com/cksdnfas/CoNAI` · 실행 후 `localhost:1677`, 빌드 후 `localhost:1666`. 알파 단계라 기능이 자주 바뀐다 |
| **단부루 검색 툴** v1.0.6 (2026-08) | Danbooru 검색·열람·보관. **데이터 컷오프 날짜를 지정하면 그 날짜까지 등록된 장수만 표시**해 NAI 학습 가능성을 가늠할 수 있다(15장 이상이면 시도할 가치가 있다고 본다). `+태그` 로 검색어 2개 제한을 우회하고 `--태그` 로 제외 검색 | `https://drive.proton.me/urls/BTD7AGYFV4#cCtiEWIhzsB3` · 검색 실패는 통신사(KT 등)의 단부루 차단이 원인일 수 있다 → VPN 또는 대체 주소 |
| **Comfy image browser** (comfyview, 2026-03~04) | ComfyUI 출력물 **선별** 도구. **배치모드**로 같은 프롬프트를 공유하는 이미지를 한 번에 띄워 그 프롬프트가 일관된 결과를 내는지 판별하고, 검색 결과를 `classify result` 로 폴더에 모으며, 한 세션에서 여러 개를 만드는 **배치 크롭**과 `wildcard workshop`(유사도 이상이면 프롬프트를 병합)·태그 분류기·모바일 서버(릴스처럼 넘기며 분류)를 갖췄다 | `https://github.com/IDKonly/Comfy-image-browser` · 릴리스의 **exe 직접 실행 권장**. ⚠️ 프롬프트 추출은 ComfyUI 의 **`Save Image With MetaData`**(`w/MetaData` 가 아니다) 노드로 저장한 이미지에 맞춰져 있다. keep 기본 단축키는 스페이스바 |
| **NAI Image Manager** v3.11 (2026-04) | NAI 로 뽑아 놓은 이미지를 **프롬프트 기반으로 캐릭터별·수위별 자동 분류**하고 로컬 웹 갤러리(`127.0.0.1:5000`)로 본다. 복사/이동 선택 가능, 분류 이력을 남겨 중복 처리를 건너뛴다. 삭제는 실제 삭제가 아니라 `_TRASH` 폴더로 이동해 복구된다. **그림체 연구소** 탭은 내 이미지들의 작가 태그를 수집해 그림체별 미리보기를 보여 주고 작가를 무작위로 뽑아 가중치를 배분해 준다(NAI App key 필요). **실측 — 22,000장 기준 CPU 32스레드 약 6분, AI 분류(19금 판별)를 켜면 약 10분**(RTX 3060 노트북) | 설치는 파이썬을 모르면 `NAIM_Setup_Manager.exe`, 있으면 `naim_setup.py` → 준비되면 `main_executor.pyw`. **파이썬 3.9~3.11 권장**(NAIA 기준에 맞췄다). 수정판 `https://arca.live/b/aiart/170228839` · ⚠️ **'브랜드 동기화'는 danbooru API 로 출처 작품을 찾는 기능이라 danbooru 가 지원을 끊으면 끝난다**(캐릭터 분리를 먼저 해야 하고 약 10분 소요, 하위 copyright 우선 — 아이돌마스터 < 아이돌마스터 밀리언 라이브). 모바일에서 보려면 `app.py` 의 `app.run(host='127.0.0.1', ...)` 을 `0.0.0.0` 으로 바꾸고 `ipconfig` 의 IPv4 주소로 `IPv4주소:5000` 접속(같은 공유기 필요) |
| **DarkNamer** (2023-01) | 무설치 파일명 일괄 변경. WebUI 가 붙인 5자리 일련번호가 띄엄띄엄 남았을 때 다시 매긴다 | `https://blog.naver.com/darkwalk77/222512470291` · 파일 추가 → '선택 지우기'로 **앞 5글자** 삭제 → '번호 붙이기'(자릿수 5) → '실제로 적용'. '숫자만 남기기'로 파일명에 박힌 프롬프트를 지우면 경로 길이 제한도 피한다 |

> **정정 — Konomi 에는 생성 기능이 있다.** 위 표에 "생성 기능은 없다" 고 적혀 있었으나,
> 최초 공개글(2026-03)과 0.14.x 업데이트글(2026-04)이 모두 **NovelAI API 를 이용한 이미지 생성·자동 생성**을
> 명시한다. 제작자 본인의 요약도 *"로컬 단부루 + 간단한 NAI (자동)생성기"* 다. i2i 와 포지션까지 구현돼 있고
> **Inpaint 는 미구현**이다. 유사 이미지 판별은 **Perceptual Hash + 프롬프트 문자열의 Jaccard 유사도** 하이브리드인데,
> pHash 만으로는 적정 임계값을 잡기 어려워 둘을 상호보완으로 쓴다.
> 알려진 한계는 **Negative 프롬프트가 검색에 섞이는데 제외할 수 없다는 것**이고,
> 홈서버·NAS 용 도커 이미지는 제작자가 *"대단히 불안정하므로 현재 시점에는 실사용을 권장하지 않는다"* 고 못박았다.

> **CoNAI 26.5.23 에서 바뀐 것** — 모델 자동 수집이 **폴더 직접 선택 → ComfyUI API** 방식으로 바뀌었다.
> 연결한 서버 중 하나를 **대표 서버**로 지정하면 API 로 목록과 썸네일을 가져오는데,
> **썸네일은 시비타이에서 받아오는 것이 아니라 컴피 폴더에 실제로 파일이 있어야** 표시된다(안 뜨면 옆의 새로고침).
> `API Error: GET /api/danbooru-browser/tags` 가 계속 뜨면
> `https://github.com/cksdnfas/danbooru-db-viewer/releases/tag/26.05.23` 의 DB 파일을 받아 `user/database` 에 넣는다.

> ### ⚠️ NAI Image Manager 의 `ModuleNotFoundError: No module named 'flask'` — 진짜 원인은 제작자도 몰랐다
>
> 서버 실행 시 이 오류가 난다는 보고가 이어졌고, 처음 나온 처방은 임시방편이었다.
>
> ```text
> (1차 처방 — 증상만 덮는다)
> PowerShell 에서  .venv\Scripts\activate  후
>   python -m pip install flask requests pillow
>   python -m pip install torch torchvision transformers      # AI 분류까지 쓸 때
> ```
>
> **진짜 원인은 댓글 15 에서 사용자가 코드 위치까지 짚어 밝혀냈다** —
> `main_executor.pyw` 가 서버를 띄울 때 **`sys.executable`(시스템 파이썬)을 쓰고 있었고**,
> flask 는 거기 없고 **프로젝트의 `.venv` 에만** 있었던 것이다.
>
> ```python
> # start_server() 안에서
> venv_python = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
> # 존재하면 sys.executable 대신 이것을 우선 쓰도록 고친다
> ```
>
> **제작자가 이를 인정하고 코드를 수정하겠다고 답했다.**
> 같은 구조의 오류는 `.venv` 를 쓰는 다른 자작 도구에서도 그대로 나올 수 있다 → [오류 해결](troubleshooting.md)

**(다) 프롬프트를 쓰고 관리하는 것**

| 도구 | 무엇을 하나 | 받는 곳 · 주의 |
|---|---|---|
| **NAI Helper** v1.1 (2026-05) | NAI 용 프롬프트 작성·관리·생성을 한 앱에서. 캐릭터/시리즈 태그 DB 각 **2,000개**, 기본 그림체 프리셋 약 **80종**, 기본 와일드카드 **19종** 내장. 랜더마이저 문법 `\|\|Tag1\|Tag2\|Tag3\|\|`, 대상 지정형 문법 `target#tag` / `source#tag` / `matual#tag` | `https://github.com/HIYO-kor/NAI-Helper/releases/tag/v1.1.0` · **위의 reCAPTCHA 주의를 함께 볼 것** |
| **프롬프트 매니저** (ComfyUI, 2026-06) | 선행·후행·네거티브 버튼으로 **활성화한 것만** 프롬프트 노드에 적용. 생성 당시 쓴 로라를 확인하고 더블클릭으로 로라 매니저로 이동 | `https://drive.google.com/file/d/1KfeJfiulhENWSNllBJQrRGJ6Jc7__WP0/view` · AI 프롬프트 생성 기능은 `llama.cpp` 가 필요하고 사전 프롬프트가 아직 없어 **'이런 게 있다' 수준** |

**(라) 그 밖에**

| 도구 | 무엇을 하나 | 받는 곳 · 주의 |
|---|---|---|
| **방송 플랫폼 데이터셋 확장** v1.3 (2026-06) | 치지직 · 유튜브 · 숲 · 트위치 · vimeo · 빌리빌리 영상에서 **로라 학습용 프레임을 뽑는** 크롬 확장. `[` `]` 로 앞뒤 프레임, shift 병용 시 10프레임 단위 | png 로 위장한 zip 이라 확장자를 zip 으로 바꿔 풀고 `chrome://extensions/` 에서 '압축해제된 확장 프로그램 로드'. 파일명이 0001 부터 시작하며 **수동 초기화 필요** |
| **Agent Scheduler** (2023-06) | WebUI 에 **대기열**을 붙이는 확장. 모델·프롬프트 조합을 여러 개 큐에 넣어 한 번에 뽑고, t2i 뿐 아니라 i2i 도 큐잉되며 컨트롤넷·디테일러와 함께 쓸 수 있다 | `https://github.com/ArtVentureX/sd-webui-agent-scheduler` · **WebUI v1.1.1 이상**에서만 동작. 설치 후 버튼이 안 보이면 UI 리셋이 아니라 **F5 새로고침**. 반복 기능은 없어 같은 항목을 N개 넣어 우회한다 |
| **[AI 미연시]** (2026-04~05) | 로컬 LLM(Ollama) + ComfyUI 를 붙여 **대화 내용에 따라 배경·캐릭터 그림이 실시간 생성**되는 채팅 프로그램. `*행동*` · `[장소]` 로 지문을 넣는다 | ComfyUI 에 **RMBG(배경 제거) 노드**가 있어야 하고 Python 3.10~3.14 · git · Node 가 필요하다(`install.bat` 1회 → `run.bat`). ComfyUI 와 LLM 을 동시에 돌려 사양 부담이 크다(테스트 RTX 5070 + RAM 64GB). **배경 단어 오인식 · 캐릭터 외형 일관성 저하**가 미해결이며 2026-05 에 개발이 중단됐다 |


**(마) 글과 그림을 함께 뽑는 것**

| 도구 | 무엇을 하나 | 받는 곳 · 주의 |
|---|---|---|
| **NOVS (Novel Simulator)** v0.7 (2026-02~03) | **Gemini API 로 소설을 쓰고 그 장면을 NAI API 로 이미지화해** '스토리가 이어지는 짤' 을 자동으로 뽑는다. 반복 횟수를 걸어 두면 자고 오는 사이 수백 페이지가 나온다. 프롬프트 관리(`캐릭1\|캐릭2\|캐릭3`), 커스텀 플롯, 검열 우회 재시도(슬래시 노이즈 1회 자동), 이전 대화 무시 토글, 요약, 이미지 생성 생략(글만 먼저 → 나중에 일괄 렌더링), 시드 고정 | `https://drive.proton.me/urls/JVG55H0VEM#WtFjm7Pc4Fr6` · CC BY-NC-ND 4.0. **Gemini API 키와 NAI API 를 각각 발급받아 등록해야 하고, Gemini 키 발급법을 모르면 쓸 수 없다고 작성자가 못박는다.** 기본 프롬프트가 2차 창작 캐릭터 위주라 자작 캐릭터는 참조 태그와 AI 태그 지침을 고쳐야 한다. **이미지 색상이 이상하면 스케줄러를 `karras` 로**, 업데이트 후에는 **'프롬 초기화' 를 한 번 눌러야** 새 프롬프트가 적용된다 |

> ### ⚠️ 이 도구의 현재 가치는 뒤집혔다 — Gemini 약관 변경
>
> **댓글: *"예전에는 잘 됐는데 Gemini 약관이 바뀐 뒤 검열에 미친 듯이 걸린다."***
> 프로그램 자체는 그대로인데 **의존하는 제3자 API 의 정책이 바뀌어 실사용 가치가 떨어진 사례**다.
> 그 밖에 상단 고정 프롬프트에 `2girls` 를 넣어도 이미지 메타데이터에는 `base 1girl` 로 나온다는 버그 보고가 있고,
> 로컬 LLM 지원 문의에는 답이 달리지 않았다.
>
> **외부 API 를 쓰는 도구는 받기 전에 최신 댓글부터 확인하는 편이 낫다.** 같은 이유로 위의
> reCAPTCHA 주의도 함께 볼 것.

→ EXIF 를 읽는 유저스크립트와 그 밖의 확장은 위 "5. 확장 · 스크립트 · 도구" 에 있다.

### ⚠ 도구 배포글은 본문 링크보다 댓글을 먼저 본다

같은 함정이 반복된다 — **본문의 구글 드라이브 링크가 낡은 판본이고, 최신은 댓글에서 안내된 깃허브 릴리스**인 경우다.

| 도구 | 본문 | 실제 최신 |
|---|---|---|
| **TagMetaUpdater** (72075853, 2023-03) | 구글 드라이브 `https://drive.google.com/file/d/1CTlF-EvZMMFwO4Asxb68HC2qvKSgKeyF/view` | **댓글에서 제작자가 안내** — `https://github.com/aaaammm336/TagMetaUpdater/releases` |
| **Prompt-Classifier v1.0.5** (143463834, 2025-07) | 그 버전 exe 직링크 | **댓글에서 작성자가 더 최신 버전을 안내** — `https://arca.live/b/aiart/154827249` |

### TagMetaUpdater — 태그를 XMP `subject` 에 심는다

이미지 내용을 **wd-14 tagger 로 자동 인식해 그 태그를 파일의 XMP 메타데이터 `subject` 필드에 써 넣는** CLI 도구다.
목적은 **파일명을 바꾸지 않고도 윈도우 탐색기 검색으로 `rating:safe` 같은 태그를 찾는 것**이다.

| | |
|---|---|
| 충돌 안 함 | **Stable Diffusion 이 넣는 EXIF 는 `UserComment` 로 가는데 이 프로그램은 `subject` 로 넣어** 서로 덮어쓰지 않는다 |
| 지원 포맷 | **jpg · jpeg · png 만** (그 외는 메타데이터 규격이 다르다) |
| 주의 | 윈도우는 기본적으로 jpg 태그만 보여 주므로 **png 의 XMP 를 보려면 별도 뷰어**가 필요하다. **한글·특수문자 인식을 위해 사전 설정 하나를 켜야 한다** |
| 태깅 모델 | 릴리스에서 쓸 수 있는 것은 **SwinV2 · ConvNext · ViT** 셋. 최신 모델은 빌드가 안 돼 릴리스에 반영되지 않았다 |
| ConvNextV2 붙이기 | 소스에 `CONV2_MODEL_REPO = "SmilingWolf/wd-v1-4-convnextv2-tagger-v2"` 를 추가하고 `elif model_name == "ConvNextV2":` 분기에서 `load_model(CONV2_MODEL_REPO, MODEL_FILENAME)` 을 호출하면 된다(한 사용자가 성공, 댓글) |

### Prompt-Classifier — 프롬프트·해상도로 폴더를 나눈다

`https://github.com/namemechan/Prompt-Classifier`

| 기능 | |
|---|---|
| **레벨 1~5** | 대분류·소분류 중첩 (레벨1 소속사별 → 레벨2 캐릭터별 → 레벨3 코스튬별) |
| 프롬프트 여러 개 | **`|`** 로 구분 |
| **전체추적** | 레벨을 무시하고 지정 폴더와 **모든 하위 폴더를 한 번에** 검사. NAIA 처럼 날짜별/nsfw별로 이미 폴더가 갈린 경우에 쓴다 |
| **v4.1.0** — 해상도 분류 | 단독 분류 / 선·후 타이밍 / 비율 분류 / **가로세로 통일**(1216x832 와 832x1216 을 묶음) / 허용 오차 / 최소 파일 수 / 컷오프 / 화이트·블랙리스트 |
| **v4.2.0** — 와일드카드 | exe 옆 `wildcard` 폴더 + `__이름__` → 위 "6-i" |
| 성능 | 이미지가 많으면 멀티코어를 켜되 **스레드 전체가 아니라 절반 정도만** 권장 |
| **막힐 때** | *'프롬프트 데이터를 찾을 수 없다'* 가 계속 뜨면 **전체추적 모드로 재시도**(작성자 답변) |
| 캐릭터 태그 | `Yukong (honkai: star rail)` 이 들어 있으면 **`Yukong` 만 넣어도** 분류된다 |

> **야매 팁** — 여러 폴더에 흩어진 이미지를 한곳으로 모으려면 **이름 처리 = '지정'**, **그 외 처리 ON**, **전체 추적 ON** 으로 두고 분류 조건에는 아무 말이나 적은 뒤(예: `오늘점심뭐먹냐`) 사용자 폴더로 이동시킬 곳을 지정한다.
> 아무것도 분류되지 않으므로 **발견된 모든 이미지가 지정 폴더로 옮겨진다.** 안전을 위해 '동일명 숫자 추가' 를 켜 둔다.

### NAI-Tag-Viewer 의 '시드 색인' — 편리하지만 검증하고 쓴다

`https://github.com/namemechan/NAI-Tag-Viewer` (v1.0.5, 171745343, 2026-05)

**ComfyUI 에서 정수 노드 같은 외부 노드로 시드를 연결하면 생성 옵션에 시드 값이 표시되지 않는다.**
'시드 색인' 은 자체 로직으로 시드를 찾아 생성 옵션 맨 위에 적어 주는 기능인데,

> ⚠ **워크플로우에 따라 잘못된 값을 집을 수도 있다.**
> 먼저 같은 이미지를 ComfyUI 에 넣어 실제 시드를 확인해 보고, **제대로 찾는다 싶을 때 쓰라**는 것이 작성자 권고다.

그 밖의 v1.0.5 변경점 — 해상도 표시 추가, 탭 접기(접은 상태는 저장되지 않고 '변환된 프롬' 탭만 기본으로 접혀 있다).

### LoRA Explorer — 로라를 해시로 Civitai 에 물어본다

`https://github.com/doge77/LoRA_Explorer/releases/tag/v3.4` (75634149, 2023-05 ~ 2023-07)
**exe 라 백신이 막을 수 있어 예외 설정이 필요하다.** 첫 실행 시 루트 디렉토리를 묻는데 **lora 폴더**를 지정한다.

| 기능 | |
|---|---|
| **Civitai 정보 불러오기** | **모델 파일의 해시값으로 Civitai 를 조회**해 모델명·버전·주소·제작자를 가져오고, 미리보기 이미지가 없으면 이미지도 받아 온다 |
| 프롬프트 관리 규칙 | 제목이 **`!` 로 시작하면 최상단 키 프롬프트**, **`~` 로 시작하면 최하단 네거티브**로 배치된다 |
| 자동 치환 | 프롬프트 열의 **`__filename__`** 은 그 모델의 파일명으로 자동 치환된다 |
| 가중치 범위 | **`<lora:__filename__:0.6~1.2>`** 처럼 `~` 로 범위를 적으면 프롬프트창으로 옮겨질 때 **평균값으로 자동 변환**된다 |
| 빠른 경로 | exe 와 같은 폴더에 `LoRA Explorer.txt` 를 만들어 `로라|D:\stable-diffusion-webui\models\Lora` 처럼 `제목|경로` 형식으로 적는다 |
| LyCORIS | 설정에서 **`<lora:` 를 `<lyco:` 로 자동 변환**하게 할 수 있다 |
| ⚠ | **'즉시 저장' 은 되돌릴 수 없다.** 불안하면 꺼 두고 수동 저장을 쓴다. 버그가 없는 한 더 이상 업데이트하지 않는다고 못박았다 |

### Random-Resolution — WebUI 기본 randomize 는 실제로 적용되지 않는다

`https://github.com/namemechan/Random-Resolution` (122055428, 2024-11). `Random-Resolution.py` 를 **webui 의 `scripts` 폴더**에 넣으면 설치 끝이다.

> **WebUI 자체의 randomize 옵션은 EXIF 상 해상도만 바뀌고 실제로는 적용되지 않는다.**
> 그래서 그 이미지를 다시 불러오면 **해상도만 이상하게 적용되는** 문제가 있었고, 이 스크립트는 그것을 피하려고 만들어졌다.

슬라이더는 **256~2048 / 64 단위**(기본 W 512~832 · H 512~1024)이고 시드는 랜덤이다. **설정 저장 기능은 없다.**
Forge 에서도 정상 동작이 댓글에서 확인됐다. 댓글에 스크립트 전문이 붙어 있어 파일 없이도 복사해 `.py` 로 저장하면 쓸 수 있다.

> **해상도를 64의 배수로 맞추는 이유** — 잠재공간이 1/8 크기로 동작해 8의 배수(실무상 64 단위)가 아니면 결과가 어긋나기 때문이다.

### DeepDanbooru 로 야짤·건전짤 자동 분류 (2023-03)

그림 20만 장을 나누려고 만든 파이썬 스크립트와 설치 절차다 (71895663). **`rating:safe / questionable / explicit`** 태그만 뽑아 폴더를 나눈다.

```bash
deepdanbooru evaluate '이미지 폴더 경로' --project-path "dataset 폴더 경로" --allow-folder --save-txt
```

> ⚠ **설치의 함정** — `https://github.com/KichangKim/DeepDanbooru` 를 받아 `setup.py` 의 `import re` **위**에 `import os` 를, setuptools import **아래**에 `os.chdir("압축 푼 폴더 절대경로")` 를 넣어야 한다.
> **이 한 줄이 없으면 다른 위치에서 실행할 때 `README.md` 를 못 찾아 실패한다.**

| 제약 | |
|---|---|
| 포맷 | **jpg · jpeg · png 만.** gif 가 섞이면 DeepDanbooru 단계부터 에러 |
| 경로 | **공백이 있으면 안 된다.** 빈칸은 `_` 나 `-` 로 메꾼다 |
| 부하 | i7-12700h 로 223장에 CPU 80~90%, 1~2분 |
| **정확도** | **questionable 로 들어간 것의 80% 가 실제로는 야짤이었고, 가슴은 explicit 으로 인식하지 못하며, 속옷에 비친 유두 같은 것은 safe 로 들어간다** |

### EasyVtuber — `No module named cv2` 가 거의 전부다

AI 로 뽑은 그림을 버튜버 아바타로 움직이게 하는 도구의 원클릭 설치본이다 (72459574, 2023-03).
**배포 링크는 base64 로 가려져 있었고 30일 제한이라 확실히 만료됐다.** 남는 것은 오류 처방이다.

| | |
|---|---|
| 가장 흔한 오류 | **`No module named cv2`** |
| 해결 | `requirements.txt` 맨 아래에 **`opencv-python`** 을 추가하고 **`venv` 폴더를 지운 뒤** `install.bat` 으로 재설치 |
| 그래도 안 되면 | 시스템에 **파이썬이 여러 버전 깔려 있는 경우**가 대부분이다. 다른 버전을 정리한다 |
| ⚠ **하면 안 되는 것** | **사이트패키지 폴더에 모듈 폴더를 직접 복사하는 방식** — numpy → torch → sympy 로 오류가 연쇄된다 |
| 폰을 웹캠으로 | 폰과 PC 양쪽에서 **DroidCam** 실행 → **OBS** 설치 → EasyVtuber 에서 webcam 을 **`obs virtual camera`** 로 지정 |

### ⚠ Prompt Classifier v1.0.7 — NAI 4.0 이미지에 회귀 버그가 있다

`https://github.com/namemechan/Prompt-Classifier/releases/download/v1.0.7/Prompt-Classifier-v1.0.7.exe`
*(기본 사용법은 `https://arca.live/b/aiart/143463834`)*

| v1.0.7 변경점 | |
|---|---|
| 버그 수정 | **NAI v4 이상에서 t2i 로 생성한 이미지를 못 읽던 문제.** 제작 당시 v3 만 확인하고 올려서, v4 이상은 인페인트 등 후처리를 거친 이미지만 분류되고 t2i 원본은 안 됐다 |
| [그 외 처리] | 지정한 분류에 해당하지 않는 이미지를 `other` 폴더로. 이름 변경을 같이 켜면 `other_00001.확장자` 형식. **[전체추적 활성화] + [폴더지정]** 과 함께 쓰면 선택 폴더와 하위 폴더의 모든 이미지를 한 폴더로 몰 수 있다 |
| [동일명 파일 숫자 추가] | 전체추적 시 같은 이름 파일이 있으면 예전엔 덮어썼을 수 있어, 지금은 **나중에 발견한 파일을 옮기지 않는 것이 기본**이고 이 기능을 켜면 `(01) (02)` 를 붙여 옮긴다 |
| 멀티코어 | 수정 후 속도가 크게 느려져서 추가 |

> ⚠️ **댓글에서 회귀 버그가 확인됐다 — v1.0.7 은 NAI 4.5 는 되는데 이전 버전에서 잘 읽던 4.0 이미지를 못 읽는다**
> (NAIA 로 뽑은 4.0 기준). **제작자는 로컬 위주라 NAI 짤 테스트가 어렵고 4.0 은 이제 쓰는 사람이 거의 없으니
> 더 수정하지 않고 넘어가겠다고 답했다.**
> **NAI 4.0 시절 이미지를 분류하려면 구버전을 써야 한다.**

<small>근거 — [신기능) 대기열 확장 - Agent Scheduler 23.06](https://arca.live/b/aiart/77750798) · [노벨 시뮬레이터 NOVS 0.7 26.02](https://arca.live/b/aiart/163625321) · [LORA EXPLORER 3.4 (LyCORIS) 23.05](https://arca.live/b/aiart/75634149) · [로컬 채팅 프로그램 (AI 미연시) v0.6 공유 26.04](https://arca.live/b/aiart/169251837)</small>

??? note "근거 37건 전부 보기"
    [신기능) 대기열 확장 - Agent Scheduler 23.06](https://arca.live/b/aiart/77750798) · [노벨 시뮬레이터 NOVS 0.7 26.02](https://arca.live/b/aiart/163625321) · [LORA EXPLORER 3.4 (LyCORIS) 23.05](https://arca.live/b/aiart/75634149) · [로컬 채팅 프로그램 (AI 미연시) v0.6 공유 26.04](https://arca.live/b/aiart/169251837) · [EasyVtuber 원클릭 설치 실행 23.03](https://arca.live/b/aiart/72459574) · [Konomi: AI 생성 이미지 검색/관리/(자동)생성 앱 26.03](https://arca.live/b/aiart/165583236) · [Compy image viewer 깃헙에 공개함 26.03](https://arca.live/b/aiart/164672367) · [(꼭 다시 받기4)누가 공유 요청해서 올리는 단부루 검색 툴… 26.08](https://arca.live/b/aiart/178778143) · [로컬 AI 채팅 프로그램 26.05](https://arca.live/b/aiart/170019628) · [AI 생성 이미지 관리 앱 Konomi 0.13.x 업데이트 26.04](https://arca.live/b/aiart/166792754) · [(제작) Exif AI 프롬 확인 프로그램 :: v2.3.4… 23.08](https://arca.live/b/aiart/83667711) · [EXIF 뷰어 3.0 html 제작 (완) 26.01](https://arca.live/b/aiart/160704184) · [야밤에 업뎃한 프롬프트분류기(추가) 25.07](https://arca.live/b/aiart/143463834) · [뒤죽박죽 섞인 그림들의 이름을 일괄로 정리해보자 23.01](https://arca.live/b/aiart/67989854) · [NAI 프롬프트 작성 / 관리 / 이미지 생성까지 한큐에 되… 26.05](https://arca.live/b/aiart/170686312) · [NAI 자동생성 앱 (NAIApp) v1.4.0 26.04](https://arca.live/b/aiart/168830995) · [NAI 자동생성 앱 (NAIApp) v1.5.1 핫픽스 26.07](https://arca.live/b/aiart/176933271) · [프롬프트 매니저 업데이트 26.06](https://arca.live/b/aiart/173045392) · [webui 랜덤해상도 및 반복생성 스크립트 24.11](https://arca.live/b/aiart/122055428) · [(윈도우탐색기에서 프롬프트 간편 복사기) ~ 8.7.아침까지… 26.07](https://arca.live/b/aiart/176179807) · [프롬프트 분류기 업데이트+멀티코어추가 25.10](https://arca.live/b/aiart/151098701) · [Exif AI 프롬 확인 프로그램 2.3.4 버전 업글 (서… 24.02](https://arca.live/b/aiart/99531580) · [ComfyUI Image Manager v3.0.0-alph… 26.02](https://arca.live/b/aiart/162063293) · [CoNAI 26.5.17 업데이트 26.05](https://arca.live/b/aiart/170932905) · [NAI 이미지 자동 분류 및 뷰어 v3.11 (26/04/1… 26.04](https://arca.live/b/aiart/166787538) · [nai+로컬 태그뷰어 업뎃 26.05](https://arca.live/b/aiart/171745343) · [(수정)이미지 프롬 수정프로그램 / 이미지 프롬 읽는 Nod… 26.07](https://arca.live/b/aiart/177982416) · [AI 생성 이미지 관리 앱 Konomi 0.14.x 업데이트 26.04](https://arca.live/b/aiart/168139677) · [이미지 태그 분류 프로그램 TagMetaUpdater 23.03](https://arca.live/b/aiart/72075853) · [프롬프트 분류기 해상도별분류 및 일부기능개선 26.05](https://arca.live/b/aiart/171554343) · [CoNAI 26.4.5 버전 업데이트 26.04](https://arca.live/b/aiart/166831098) · [CoNAI로 변경된 이미지+영상관리 시스템 ㅠ 26.03](https://arca.live/b/aiart/165939813) · [방송 플랫폼 데이터셋 확보용 확장 26.06](https://arca.live/b/aiart/173312863) · [CoNAI 26.5.23 업데이트 26.05](https://arca.live/b/aiart/171558427) · [CoNai 26.4.20 업뎃 26.04](https://arca.live/b/aiart/168222915) · [comfyview 업데이트 26.04](https://arca.live/b/aiart/168888732) · [python 2일차 chatgpt로 만든 deepdanboo… 23.03](https://arca.live/b/aiart/71895663)

## 6-d. 끼우기만 하면 그림이 이뻐지는 노드 — DCW
<small>2026-04 기준 · 근거 3건</small>

설치하고 모델 라인 중간에 끼우기만 하면 화질이 오르는 노드다. 옵션이 둘뿐이라 진입 장벽이 낮다.

```
노드   https://github.com/namemechan/ComfyUI-DCW
원 구현 https://github.com/AMAP-ML/DCW
논문   https://arxiv.org/abs/2604.16044
```

**쓰는 법** — 설치 후 노드 검색에서 `DCW` 를 찾아 **모델 라인 중간에 끼워 KSampler 로 보내면 끝**이다.

| 옵션 | 무엇에 관여하나 | 실용 범위 |
|---|---|---|
| **L** (`lambda_l`) | 생성 **초기의 저주파** — 그림 전체의 구조와 형태 | **0 ~ 0.1** (너무 올리면 톤이 탁해진다) |
| **H** | **후기의 고주파** — 디테일 | **0 ~ 0.02** |

**2단 구성이면 나눠 준다** — Anima 로 뽑고 IL 로 다듬거나 KSampler 를 두 번 거치는 hires 구성에서는
**먼저 뽑는 쪽에 `L` 만, 뒤에서 다듬는 쪽에 `H` 만** 준다. L 이 초기 형태를, H 가 후반 마무리를 담당하기 때문이다.

**어떤 모델은 `lambda_l` 0.05 만 줘도 그림이 이상해진다** — 그럴 때는 `H` 를 0 으로 두고
`L` 을 **0.001 부터** 올리며 적정값을 찾는다. 모델별 권장값은 깃허브에 적혀 있다.

댓글의 평가 — FreeU 처럼 아키텍처의 허점을 보정한다는 개념이지만 건드리는 부분은 완전히 다르다.
**병합 체크포인트에서 흔한 색상 과포화를 CFG rescale 보다 안정적으로 잡아 주고** 고주파 디테일, 특히 배경 묘사가 일관되게 개선된다.
v-pred 모델도 그냥 연결하면 되고 SDXL·Anima 양쪽 다 동작한다는 후기가 있다.

> ⚠️ 다만 **NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 같은 가속/보정 노드와 상성이 나쁘다**는
> 보고가 통합팩 배포글에 반복해 실려 있다. 그림이 깨지면 하나씩 바이패스해 원인을 찾는다 → [오류 해결](troubleshooting.md)
>
> 노드는 논문과 완전히 같은 방식이 아니라 여러 모델·샘플러에서 돌아가도록 유사하게 구현한 것이라고 작성자가 밝혔다.

**같이 쓰는 보정 노드** — ANIMA 에서는 `DCW + CWM + SMC` 조합이 쓰이며 `SMC 6 / 0.2` 가 무난하다.
수치는 **DCW 의 `l` 만 남기고 나머지를 0 으로 둔 뒤 → `h` → `cwm` 순**으로 찾는다.
가로로 긴 해상도에 한 명만 뽑는데 인물 분리가 일어나면 SMC 를 꺼야 하고, cfg 리스케일을 쓰면 CWM 과 SMC 가 비활성화된다.

<small>근거 — [아니마 심플하면서 제대로쓰기 26.05](https://arca.live/b/aiart/171770463) · [Comfyui portable v0.22.0 + sage +… 26.05](https://arca.live/b/aiart/171586136) · [ComfyUI-DCW 노드_쓰면그림이 이뻐져요! 26.04](https://arca.live/b/aiart/168389657)</small>

## 6-e. 태그를 찾고 프롬프트를 만들어 주는 도구
<small>2026-07 기준 · 근거 10건</small>

"무슨 태그를 써야 할지" 를 사람이 아니라 도구에 물어보는 쪽이다. 위 "6-b" 가 **읽는 자료**라면 여기는 **돌리는 도구**다.

### 태그 원본 데이터

```text
# 단부루 태그 + 태그 그룹 + 한국어 번역 합본 DB (SQLite)
https://github.com/cksdnfas/danbooru-db-viewer
  · 깃허브 코드는 **뷰어**이고 **릴리즈에 있는 DB 파일이 본체**다
  · 포스트 50개 이상인 캐릭터만 수집. 캐릭터별 수집 때문에 용량이 크다
  · ⚠️ 제작자 본인이 "분류와 번역은 대충 구색만 맞춰 놓은 거라 구릴 것" 이라고 밝혔다 — 검증용·기반용으로
  · 실제로 NAI Helper 앱이 이 DB 를 허락받아 가공해 쓴다

# NAI 로 실제로 뽑아 타율을 확인한 2006~2015년 애니 캐릭터 태그 모음집
https://drive.google.com/file/d/1uf5iyGvt2DsJ6J0BOGEeAyw6SvKwuM2P/view
  · **캐릭터 이름 태그만** 들어 있다 — 의상·구도는 직접 붙이는 전제다
  · 원피스·나루토·블리치·프리큐어·아이마스처럼 캐릭터가 너무 많은 작품은 제외
  · 최신 캐릭터가 안 나올 때, 반대로 '확실히 되는' 구간을 알려 주는 자료
```

### 태그를 골라 프롬프트로 만들어 주는 것

| 도구 | 무엇을 하나 | 받는 곳 · 주의 |
|---|---|---|
| **단부루 태그 복사기** (유저스크립트, 2026-03) | 단부루 페이지의 태그 옆에 복사 버튼을 붙인다. 단순 복사가 아니라 **프롬프트용으로 변환**해 준다 — 언더바 `_` 자동 제거(`@_@` 등은 예외), 괄호 앞 `\` 이스케이프 자동 삽입 | `https://drive.proton.me/urls/CGYZ61A18C#gfT5943LpYpN` · Tampermonkey 등에 설치. **NAI 용으로 이스케이프를 끄는 옵션**이 따로 있다. `dush 1154` 같은 작가 태그는 언더바가 남는 버그 |
| **단부루 프롬프트 생성기** (단일 HTML, 2026-04) | 12개 카테고리에서 태그를 무작위 조합해 컨셉을 던져 준다. **결과에 대중적/균형/희귀 뱃지**를 달아 AI 가 그 조합을 그릴 수 있는지 미리 알려 준다(희귀할수록 안 나온다). 단부루 포스트 URL·ID 로 태그를 역추출하는 기능도 있다 | 본문 링크 만료 → **댓글 11번 복원 링크** `https://kio.ac/c/bxL-NqUdP4P2j5SUqNcP8b` · 태그 풀 12,839개(한국어 99.6%), 의상은 상/하의·원피스·아우터·신발로 세분화돼 충돌 방지, **NovelAI 225 토큰** 근접 시 경고 |
| **단부루 작가 태그 생성기** (단일 HTML, 2026-05) | 작가 **17,229명**(post_count ≥ 100) 풀에서 무작위 추천. 인기도 슬라이더 21단계로 마이너 작가까지 훑고, 즐겨찾기(★)·제외(⊖)로 쓸수록 취향에 맞게 좁혀진다 | **본문 다운로드 링크 만료 — 링크 죽음** · 작가별 강도 0.10~2.00 을 매긴 뒤 **출력 형식을 NAI `1.3::artist::` / 로컬 `(artist:1.3)` 로 자동 변환**한다(1.0 은 이름만 출력). `::` 표기 갈림은 [프롬프트 쓰는 법](prompting.md) 참조 |
| **danbooru-tag-rag-mcp** (2026-06) | 웹 도구였던 '단부루 프롬프트 도우미' 의 MCP 서버판. Claude Desktop·Claude Code·Codex 에 등록해 대화하듯 태그를 뽑는다 | `https://github.com/OneVth/danbooru-tag-rag-mcp` · **RAG 라서 DB 에 실제로 있는 태그만 출력한다 — 없는 태그를 지어낼 수 없는 것이 핵심 이점**. stdio·HTTP 지원. NSFW 는 **클라이언트 LLM(Claude) 자체 제한**에 걸리므로 로컬 LLM 연결이 낫다 |
| **그록 스킬 'NAI 태그 컴파일러'** (2026-06) | 그록의 '스킬' 에 태그 CSV 를 올려 자연어를 NAI 태그로 바꾸는 개인 도구를 만드는 법. `@NAI` 로 호출 | 태그 CSV 는 `https://arca.live/b/aiart/140767328` · 확신이 낮은 태그를 `[미확정 태그]` 로 분리하게 하는 것이 지시문의 뼈대. 검열이 덜해 그록을 골랐을 뿐 야짤이 아니면 ChatGPT 로도 된다(댓글 2) |
| **ANIMA 용 Gemini Gems 지침** (2026-07) | Gemini 의 Gems 에 넣는 ANIMA 프롬프트 빌더. 출력이 **영문 자연어 서술 → 영문 키워드 나열 → 한국어 번역** 3단으로 고정된다 | 검증 CSV 는 `https://github.com/Localsmile/danbooru_KR_wiki_tag_search` (댓글 6) · 강조는 `(키워드:1.20)`, 밑줄은 공백, 2인 이상이면 인원수 태그를 맨 앞 |
| **Danbooru Artist Rater** (2026-07) | **작가 태그도 퀄리티도 네거티브도 모르는 뉴비를 정면으로 겨냥한 도구.** 작가 평가 · 그림체 조합 · NovelAI 생성 · 공유 그림체 수집/분석을 한 프로그램에서 한다. 남이 공유한 그림체가 마음에 들면 **그 작가·퀄리티·네거티브 프롬프트를 그대로 가져다 쓰면 된다**(작성자가 뉴비에게 권하는 방법) | EXE 실행 → 리모콘 **'서버 켜기'** → **'웹사이트 열기'**(내 컴퓨터에서만 열리는 로컬 화면). ⚠️ EXE 옆에 생기는 **`data` 폴더를 절대 지우지 말고** EXE 와 함께 옮긴다. 로컬 ZIP 설치에는 **약 7GB 이상 빈 공간**이 필요하고 **받은 ZIP 은 풀지 말고 그대로 선택**한다. 브라우저 탭만 닫으면 서버가 계속 도니 **리모콘까지 닫는다**. App Key 는 NAI 이미지를 직접 생성할 때만 필요 |
| **GPT·나노바나나 프롬프트 갤러리** (2026-04) | 결과 이미지와 그때 쓴 프롬프트가 **짝지어** 올라오는 사이트. 프롬프트를 역으로 배우기에 좋다 | `https://www.meigen.ai/` · `https://youmind.com/ja-JP/gpt-image-2-prompts` · `https://opennana.com/awesome-prompt-gallery?model=ChatGPT` (로컬이 아니라 클라우드 모델 쪽 자료) |

> ⚠️ **LLM 에 태그 CSV 를 통째로 물리는 방식은 믿을 게 못 된다.** 두 글에서 같은 반박이 나왔다 —
> CSV 가 20~30만 단어(제미나이 기준 340만 토큰) 규모라 **앞부분만 읽고 답을 뱉는다**는 것이고,
> **두 글의 작성자 모두 이 지적을 받아들였다.** Gems 지침 작성자는 *"csv 파일은 사실 넣어놔도 더럽게 안 본다"* 고
> 적으며 `1girl` 대신 **`1woman` 같은 존재하지 않는 태그**를 지어낸다고 밝혔다.
>
> 그래서 실제로 통하는 구성은 둘 중 하나다.
> - **RAG·MCP** 처럼 DB 를 조회해 **실재하는 태그만** 내보내게 한다 (위 `danbooru-tag-rag-mcp`)
> - AI 가 먼저 태그를 만들게 한 뒤 **코드 실행으로 태그 사전을 `grep` 해 존재 여부를 검증**하고 교체한다
>
> 어느 쪽이든 **최종 프롬프트는 사람이 검수해야 한다.** 태그를 고르는 원칙은 [프롬프트 쓰는 법](prompting.md) 을 보라.

### Danbooru Artist Rater 를 쓸 때 — 값 몇 개만 알면 된다

**작가 뽑기** — Danbooru 태그(예 `school_uniform`, `lying`, `looking_at_viewer`)를 넣고 후보를 좁힌다.

| 항목 | 값 |
|---|---|
| **최소 전체 게시물 수** | 기본값 **1000 은 강한 조건**이다. 후보가 적으면 **100~300** 으로 낮춘다 |
| 랜덤 방식 | `uniform`(모두 동등) / `weighted`(조건에 잘 맞는 작가 우대) / `soft_weighted`(중간) |
| 평가 | 샘플 그림을 보고 **1(안 씀) ~ 5(매우 좋음)** 로 매기면 자동 저장되고 이미 평가한 작가는 다시 안 나온다 |

**그림체 제작** — 전체 작가 수와 '공유 작가 최소~최대' 를 정한다.

```text
전체 12 + 공유 4~8   →  공유 작가를 4~8명 넣고 나머지를 내 평가 작가로 채운다
전체 12 + 공유 12~12 →  내 평가 작가 없이 공유 작가만 쓴다      (작성자가 댓글에서 재확인)
가중치 방식 : 랜덤 / 균형(권장 — 일부 작가가 중심을 잡고 나머지가 보조) / 사용자 그래프
```

퀄리티 프롬프트는 공유 그림체 분석 결과가 자동 추천되며 `girl`, `full body` 같은 인물·신체 구성 태그는
추천에서 제외된다. 여러 작가를 섞고 싶으면 5명 이상부터 시작해 볼 만하다.

> ⚠️ **Anlas 낭비 방지** — 생성 전에 **Steps 가 실수로 28 보다 높아지지 않았는지, 해상도가 의도치 않게 바뀌지
> 않았는지** 반드시 확인하라는 것이 본문의 경고다.

> **댓글의 그림체 조합 이론이 본문보다 값지다** (다른 유명 가이드 작성자의 답변).
> NAI 4.5 는 작가의 '특징' 이 강하면 그 특징을 강하게 가져오는 경향이 있어, 사람들이 쓰는 조합 방식은 셋으로 갈린다.
>
> | 방식 | 어떻게 |
> |---|---|
> | **얌전한 조합식** | 작가마다 `0.n` 단위 가중치를 줘서 **아무도 과하게 튀지 않게** 한다 |
> | **융합체 조합식** | 작가를 **아주 많이 넣어 서로 얽히게** 함으로써 안정시킨다 |
> | **끝말잇기 조합식** | 비슷한 분위기의 작가를 **연결해 가며 조금씩** 안정시킨다 |
>
> 같은 작가 조합이라도 선·색감·드로잉 스타일·질감의 영향이 크고, 광원·퀄리티 태그는 있으면 분위기가 좋지만
> 없어서 더 좋을 때도 있다. **그리고 '매 버전마다 그림체 만드는 법이 달라진다' 는 단서가 붙는다 —
> 어떤 방법도 정답이 아니다.**

> **트러블슈팅(댓글)** — `Danbooru API 오류: Connection aborted / ConnectionResetError(10054)` 가 나면
> `https://danbooru.donmai.us/posts.json?limit=1` 에 직접 접속해 본다. 안 열리면 danbooru 의 임시 차단이거나
> 통신사·국가 차단이므로 VPN 이 필요할 수 있다 → 아래 "6-g" 의 단부루 접속 항목.
> 제약 — 그림체 이미지는 한 번에 하나씩만 추가할 수 있고, 작가 평가 샘플은 **NAI 학습 기간 내 그림 중 랜덤 10장**이다.


<small>근거 — [단부루 기반 AI 이미지 프롬프트 생성기.HTML 26.04](https://arca.live/b/aiart/169288451) · [NAI 그림체 제작 보조 프로그램 26.07](https://arca.live/b/aiart/177316727) · [단부루 태그 복사기 유저스크립트 26.03](https://arca.live/b/aiart/164343331) · [단부루 기반 AI 이미지 작가 태그 생성기.HTML 26.05](https://arca.live/b/aiart/169546100)</small>

??? note "근거 10건 전부 보기"
    [단부루 기반 AI 이미지 프롬프트 생성기.HTML 26.04](https://arca.live/b/aiart/169288451) · [NAI 그림체 제작 보조 프로그램 26.07](https://arca.live/b/aiart/177316727) · [단부루 태그 복사기 유저스크립트 26.03](https://arca.live/b/aiart/164343331) · [단부루 기반 AI 이미지 작가 태그 생성기.HTML 26.05](https://arca.live/b/aiart/169546100) · [단부루 태그 + 그룹 + 번역 합본 DB 공유 26-05-02 26.05](https://arca.live/b/aiart/169460152) · [ANIMA용 잼민이 gems 26.07](https://arca.live/b/aiart/176216501) · [GPT(덕테이프), 나노바나나 이미지 프롬 사이트 모음 26.04](https://arca.live/b/aiart/168949757) · [사이버 경로당 노인이 만든 NAI 2006-2015 애니 캐… 26.02](https://arca.live/b/aiart/163615724) · [Danbooru 프롬프트 도우미 MCP 서버 26.06](https://arca.live/b/aiart/174935283) · [그록을 활용한 NAI 프롬프트 생성기 만드는 법 26.06](https://arca.live/b/aiart/174034886)

## 6-f. 작가 태그 대조표와 프롬프트 시트 — 화풍을 눈으로 고르는 자료
<small>⚠️ 2025-04 기준 · 근거 12건</small>

작가 태그는 이름만 봐서는 어떤 그림이 나오는지 알 수 없다. **같은 조건에서 뽑아 나란히 놓은 대조표**가 그것을 풀어 준다. 아래 자료들이 값어치 있는 이유는 그림이 아니라 **조건이 전부 공개돼 있어 그대로 재현되기 때문**이다.

### NAI Diffusion V4 Full 기준 — 표준 조건이 굳어져 있다

세 편의 대조표·프리셋 글이 **완전히 같은 세팅**을 쓴다. 새로 비교표를 만들 때 이 조건을 그대로 쓰면 기존 자료와 바로 견줄 수 있다.

| 항목 | 값 |
|---|---|
| 모델 | `NAI Diffusion V4 Full` |
| Steps | `28` |
| Prompt Guidance (CFG) | `6` |
| Sampler | `Euler Ancestral` |
| Prompt Guidance Rescale | `0.7` |
| Noise Schedule | `karras` |
| Add Quality Tags | `on` |
| Undesired Content Preset | `Heavy` |

```text
공통 프롬프트  nsfw, [작가 태그], year 2024, cowboy shot, solo, straight-on, standing, arm at side
```

> `year 2024` 를 넣는 이유가 있다 — **일부 작가의 옛날 화풍이 튀어나와 그림체를 망가뜨리는 것을 막기 위해서**다.

| 자료 | 무엇이 실려 있나 |
|---|---|
| **V4용 작가 태그/화풍/프리셋 저장글** (2025-03) `https://arca.live/b/aiart/130458775` | 작가 70여 명 + 화풍 태그 실측 + 프리셋 16종. ⚠️ **레거시 업데이트 이전 `{}`·`[]` 문법**이라 아래 후속판이 최신이다 |
| **NAI용 그림체 프리셋 저장글** (2025-03) `https://arca.live/b/aiart/132727305` | 위의 후속판. 작가 75명 해설 + 프리셋 12종. **`1::artist:NAME::` 문법**으로 다시 썼다 |
| **작가 태그 모음집 B편** (2025-04) `https://arca.live/b/aiart/134455790` | 알파벳 B 로 시작하는 작가 **123종**. 머리색·눈색·구도를 전부 고정해 **순수하게 작가 태그가 만드는 차이만** 비교된다 |
| **작가 태그 모음집 0~A 편** (2025-04) `https://arca.live/b/aiart/134331198` | 알파벳 0~A 로 시작하는 작가 **약 125명**. 작성자가 시작 2일차 뉴비였고 `https://zele.st/NovelAI/` 에서 골라 직접 뽑았다 |
| **작가 태그 모음집 C 편** (2025-04) `https://arca.live/b/aiart/134461713` | 알파벳 C **145장**(1장 중복). **댓글에 `artist:` 접두를 붙인 와일드카드용 목록**을 따로 풀어 두어 ComfyUI·NAI 와일드카드 파일에 그대로 넣을 수 있다 |

> **왜 새 작가 태그 자료가 적은가(댓글)** — 이 채널에는 **1년 전에 이미 작가 1100명을 모은 념글**이 있었고
> 그때 태그가 다 털렸다. 추천 아카이브는
> `https://drive.google.com/drive/folders/1Eigme-YpTfhsBp_v4WXDWIy-ha2TIJd1` 다.

**화풍 태그 실측 결과가 특히 쓸모 있다** *(V4 기준)*.

| 태그 | 관찰 |
|---|---|
| `flat color` · `sketch` | **작가 태그 보조 없이 단독으로는 절대 작동하지 않는다** (반복 관찰) |
| `colorful` | **nsfw 가 들어가면 작동하지 않는다** |
| `1970s~2000s (style)` | 70~80년대는 데이터가 부족하고 **2000년대 초반 태그는 아예 안 먹힌다** |
| `pc-98 (style)` | 도트까지 알아서 나온다 |
| `neon palette` | 네온이라기보다 **사이버펑크를 통째로** 가져온다 |
| `abstract` · `surreal` | 색 대비 증가, 배경과 조합하면 초현실적 |

**못 쓰게 된 작가 태그도 기록돼 있다.**

- `dishwasher1910` — **눈매를 박살내고 무슨 짓을 해도 해결이 안 되니 빼는 게 최선**
- `shigure ui` — 그림체·조합력·색감이 모두 뛰어나지만 **캐릭터 프롬을 지정하지 않으면 제작자의 버추얼 캐릭터가 튀어나온다.** 쓰려면 네거티브에 반드시 `pom pom (clothes)` 를 박는다

### 로컬(Illustrious 계열) 기준 대조표

```text
personaStyle_Ilxl10Noob 작가 태그 80종 대조표 (2025-03)   https://arca.live/b/aiart/130266214
  재현 조건 : euler ancestral + sgm uniform, 클립 스킵 -2, 스텝 10, CFG 1.5,
              시드 116050890266963 고정, 1024x1024, LoRA·디테일러·업스케일 전부 없음
  · 작가 태그는 알파벳 오름차순, 태그를 안 쓴 기본 그림체는 맨 마지막
  · 화풍 트리거인 persona 는 알파벳 p 자리에 끼워 뒀다
```

같은 글이 **DMD 저스텝 모델의 속도를 유지하면서 마무리하는 실사용 세팅**도 공개했다.

| 단계 | 값 |
|---|---|
| 얼굴 디테일러 | 가이드 `768` / 최대 `1024` / 스텝 `10` / **denoise `0.1`** |
| 업스케일 | `2x-AnimeSharpV4_Fast_RCAN_Pu` 2배 / 스텝 `6` / **denoise `0.2`** |
| 샘플러·스케줄러·CFG | **모델과 동일하게** |

### 프롬프트를 통째로 모아 둔 곳

```text
# Tag & Prompt Gallery — 채널 이용자가 만든 프롬프트 검색 사이트 (2025-01)
  · 이미지를 클릭하면 그 이미지에 내장된 프롬프트가 클립보드에 복사된다
  · 검색은 이미지명과 프롬프트를 함께 훑는다. 다크모드 지원
  · 즐겨찾기·회원가입·정렬은 서버 비용 때문에 빠져 있고, 작성자 본인도 **단부루를 대체할 수는 없다**고 밝혔다
  · 이미지 등록은 엑셀 매크로 반자동, 배포는 Netlify, 이미지는 imgbb 경유

# 중국어권 NAI 프롬프트 시트 (2024-10)
https://docs.qq.com/sheet/DSXJtZ2ZXRHZvUFV0?tab=BB08J2
https://docs.qq.com/sheet/DSWJ0TVFaQ3VjVktv?tab=BB08J2
  · 텐센트 문서라 **다운로드에 위챗 계정이 필요**하다. 채널 재배포본(kiosk.ac)은 만료 유력
  · 중국어권 커뮤니티가 별도의 프롬프트 시트 문화를 가지고 있다는 것 자체가 정보다

# AIFUN — EXIF 가 살아 있는 NAI 이미지 모음 (2024-10)
https://aitags.fun/
  · 이미지를 NAI 나 WebUI 에 넣으면 프롬프트와 설정을 그대로 꺼낼 수 있다
  · ⚠️ 사이트에 검색 버튼은 있지만 **검색이 실제로 되지 않는다**

# 157색 웹 컬러코드 임베딩 (2023-02, SD1.5 시절)
https://huggingface.co/datasets/qweqwe/embeddings/tree/main
  · 압축을 풀어 stable-diffusion-webui\embeddings 에 그대로 넣고 파일명을 프롬프트에 적는다
  · 색이 원래 프롬프트에 묻히면 → 네거티브에 (black:1.8) 처럼 덮는 색을 넣거나
    `dark green, DarkSlateGray,` 처럼 가까운 일반 색 태그를 함께 적어 유도한다
  · ⚠️ 머리카락 색에는 거의 적용되지 않고 옷 색만 바뀐다는 한계 보고
  · 지금 모델은 색 표현이 훨씬 좋아져 이 정도 보조가 필요하지 않다 — **발상만 참고**

# 프롬프트 서치 사이트 (채널 유저 운영, 2025-01 갱신)
  캐릭터별로 미리 뽑아 둔 이미지와 그 프롬프트를 검색해 복사한다
  · 캐릭터 이름을 어떤 태그로 적어야 하는지 모르는 입문자용
  · 이미지는 ILXL 베이스에 LCM 을 붙여 빠르게 뽑은 것이다
  · ⚠️ 2025-01-04 시점 운영자 본인의 자기 정정 — 치환 작업 중 띄어쓰기와 필요한 요소가 다 날아가
    그 캐릭터 프롬프트로는 정상적인 캐릭터가 나오기 어렵다고 밝혔다. 수정 이후 판인지 확인할 것
```

### 취향 작가만 골라내기 — NAIA 랜덤작가 관리

Noob 1.0 에는 최소 3만 명, NAI 에도 1만 3천 명 수준의 작가명이 학습돼 있어 **그중 내 취향을 찾는 것 자체가 큰일**이다. NAIA 로 좁히는 절차가 정리돼 있다 *(2024-11)*.

1. 원하는 성향의 프롬프트로 검색한다 (예시는 `1girl, large breasts` 로 79만여 건)
2. **'추천 프롬프트 검색'** 을 누르면 결과 안에서 고빈도 키워드·작가명·캐릭터를 뽑아 준다
3. **와일드카드 내보내기** — 여기가 핵심이다

| 버튼 | 내보내는 것 |
|---|---|
| **파란색** | 단부루 post count **70 이상인 모든 작가명** |
| **검은색** | post count 70 이상 **이면서** 검색된 프롬프트 행이 **20개 이상**인 작가만 (= 그 키워드를 실제로 자주 그리는 작가) |

4. **'랜덤작가 관리'** 에서 `[작가명 와일드카드 삽입]` → **4만 개에 달하던 리스트가 1천 개로 압축된다**
5. `Ctrl+C` 로 복사해 메모장에 옮겨 나만의 와일드카드를 만든다

```text
사전 준비 — NAIA 실행 파일이 있는 위치에 artist_thumbnail 이 있어야 한다
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/Danbooru%20Prompt%20Selector/TEST2024/artist_thumbnail
```

→ 문법과 작가 태그를 조합하는 절차는 [프롬프트 쓰는 법](prompting.md), ANIMA 용 작가 와일드카드는 위 "6. 와일드카드 · 태그 · 작가 데이터" 에 있다.

<small>근거 — [내가 쓰려고 만드는 NAI용 그림체 프리셋 저장글 25.03](https://arca.live/b/aiart/132727305) · [프롬프트 서치 사이트 공유 25.01](https://arca.live/b/aiart/125254725) · [포함) V4용 여러가지 작가 태그/화풍/프리셋 저장글 25.03](https://arca.live/b/aiart/130458775) · [157색 컬러코드 임베딩 공유 23.02](https://arca.live/b/aiart/70343512)</small>

??? note "근거 12건 전부 보기"
    [내가 쓰려고 만드는 NAI용 그림체 프리셋 저장글 25.03](https://arca.live/b/aiart/132727305) · [프롬프트 서치 사이트 공유 25.01](https://arca.live/b/aiart/125254725) · [포함) V4용 여러가지 작가 태그/화풍/프리셋 저장글 25.03](https://arca.live/b/aiart/130458775) · [157색 컬러코드 임베딩 공유 23.02](https://arca.live/b/aiart/70343512) · [내가 쓰려고 만든 작가 태그 모음집 C 25.04](https://arca.live/b/aiart/134461713) · [(NAI?) 짱깨 사이트 엑셀 저장한 것 24.10](https://arca.live/b/aiart/117689806) · [내가 쓰려고 만든 NAI 작가 태그 모음집 0~A 25.04](https://arca.live/b/aiart/134331198) · [(NAI) 짱깨 AIFUN NAI 이미지 모음 24.10](https://arca.live/b/aiart/119314105) · [※ 프롬프트 서치 사이트 업데이트 내용  25.01.04 25.01](https://arca.live/b/aiart/125471599) · [NAIA - 작가 스타일 분류 가이드 (testv23b) 24.11](https://arca.live/b/aiart/121061032) · [내가 쓰려고 만든 작가 태그 모음집 B 25.04](https://arca.live/b/aiart/134455790) · [personaStyle_Ilxl10Noob 모델 기준 작가 … 25.03](https://arca.live/b/aiart/130266214)

## 6-g. 태그를 몰라도 프롬프트를 얻는 곳 — 단부루 공식 위키와 웹 도구
<small>2026-04 기준 · 근거 6건</small>

위의 "6-b" 가 **사람이 정리해 둔 읽을거리**, "6-e" 가 **프롬프트를 만들어 주는 도구**라면,
여기는 **태그 자체를 모를 때 가장 먼저 여는 곳**이다.

### ① 단부루 공식 태그 그룹 위키 — 원본이자 기준

```text
https://danbooru.donmai.us/wiki_pages/tag_groups
```

단부루 태그가 **주제별로 그룹화**돼 있다. `tag group: dress` 에 들어가면 드레스 관련 태그를 한 번에 볼 수 있고,
**태그마다 간략한 설명과 예시 그림이 붙어 있다.**
Illustrious·NoobAI·NAI 계열 모델은 모두 단부루 태그로 학습돼 있으니 *"이걸 뭐라고 써야 하지"* 가
막힐 때 가장 먼저 볼 곳이다. 단점은 전부 영어라는 것.

> ⚠️ **안 열리면 VPN 을 쓴다.** 국내에서 단부루 접속이 막히는 경우가 있다(원문 140170773 댓글 4~5).
> 이 문서의 "6-c" 에 있는 단부루 검색 툴에도 같은 안내(통신사 차단 → VPN 또는 대체 주소)가 붙어 있다.

태그를 **조합**해 상황을 만드는 것이 요령이다 — 예시로 올라온 그림은 `faceplant + tripping + falling` 조합이었다.

### ② NAIA-WEB-Lite — **설치가 필요 없다**

```text
https://baqu2213-naia.hf.space/
```

**태그를 하나도 몰라도 버튼만 눌러 프롬프트를 얻는다.** 입문자에게 이 문서에서 가장 실용적인 항목일 수 있다.

핵심은 **Quick Search** 로, 단부루 태그 데이터에서 의상·색상·배경·신체정보를 제외한
**프롬프트 세트 약 400만 개**가 탑재돼 있다. 단순 검색은 지원하지 않는 대신 **속도가 매우 빠르다.**

| 무엇 | 어떻게 |
|---|---|
| Rating | `General`=건전한 태그만 / `Sensitive`=약간 불건전 / `Questionable`=야짤 / `Explicit`=성기 노출·성행위 |
| 인원 수 | 보통 `1 Girl Solo` / `1 Girl` / `1 Girl + 1 Boy` / `1 Girl + Boys` 네 가지 |
| Include / Exclude Tags | 포함된 프롬프트만 검색하고, 그중 제외 태그가 있는 것을 뺀다 |
| **태그 옆의 숫자** | **그 태그를 눌렀을 때 남게 되는 랜덤 프롬프트의 수** |

태그를 모르면 버튼을 하나씩 눌러 좁혀 가면 되고, 누를 때마다 남은 수가 `253479 → 59568 → 13122` 처럼
줄어드는 것이 보인다.

```text
NAI 영구 토큰(API 로그인)을 넣으면  → 사이트에서 곧바로 이미지까지 생성된다
넣지 않으면                        → [랜덤 프롬프트] 버튼으로 나온 프롬프트를 복사해 NAI 등에 붙여 넣는다
NAIA 프로그램 사용자               → 네거티브 프롬프트 옆의 [리모트] 버튼으로 같은 기능을 쓴다
```

2026-01-20 업데이트로 NAIA 의 태그 전처리 기능과 거의 호환돼, 의상 정보나 캐릭터 특징을 웹에서 검색할 수 있고
랜덤 생성 시 의상 제거·배경 제거 기능을 쓸 수 있다.

### ③ NAIA 2.0 이벤트 프리셋 — 랜덤이 아니라 **프롬프트 사전**

단부루에 직접 들어가 이미지를 뒤지며 프롬프트를 따오지 않아도 **원하는 구도의 고빈도 태그를 바로 확인**하게 해 준다.
기존 NAIA 가 쌓인 랜덤 프롬프트를 하나씩 돌려 보는 방식이라면, 이건 **프롬프트를 다 펼쳐 놓고 직접 찾는 방식**이다.

```text
진입      버전 150 이후 → 확장 기능 버튼 → Event Preset
업데이트  기존 폴더에서 git pull
최초 설치 https://arca.live/b/aiart/146196193      이전 버전 148  https://arca.live/b/aiart/162908437
```

> **`Count` 의 뜻이 이 기능의 전부다** — 단부루 데이터셋에서 그 태그 조합이 출현한 빈도다.
> **1개 또는 한 자릿수는 창의적인 조합, 10개 이상은 고빈도**이고,
> **고빈도일수록 태그 수가 적고 안정적인 이미지가 나올 가능성이 높다.**

이벤트를 클릭하면 연관성 높은 `Expressions` / `Clothing` / `Characteristics` 추천 태그가 뜨고, 각 탭에서 출현률을
볼 수 있다(어떤 이벤트에서 `blush` 는 0.8 로 매우 높고 `seductive smile`·`smirk` 는 2% 미만). 클릭해 추가한 태그는
다른 이벤트를 골라도 최대한 유지되므로 디테일을 쌓아 가기 쉽다. **한글 검색을 부분적으로 지원**한다.

| 알아 둘 것 | 내용 |
|---|---|
| 이벤트 목록이 괄호 안 숫자보다 적게(최대 30개) 보인다 | **중복 이벤트를 압축**해 둔 것이다 (댓글 14~15) |
| 하단 [Generate] 로 뽑을 때 | 메인 UI 설정값과 선행/후행 고정 프롬프트를 쓰고 **전처리·자동 숨김 옵션은 무시한다**(캐릭터 프롬프트는 사용). 피하려면 [메인 프롬프트에 전송] 또는 [전송 + 즉시 생성] |
| 전송하면 `1girl` 이 사라진 것 같다 | 무시된 게 아니라 **최상위 위치(NAI) 또는 퀄리티 프롬프트 뒤(ComfyUI-ANIMA)로 이동**한 것이다 (댓글 8~10) |
| 자동 숨김에 `censored` 를 넣었는데 계속 나온다 | 파생 태그가 많아서다. **`__censor__` 로 넣고** 프롬프트 엔지니어링의 디버깅 윈도우에서 검출 여부를 확인한다 (댓글 19~20) |

### ④ 개인이 정리한 것 — 노션 · NotebookLM

```text
# 단부루 태그 모음 노션 (2025-06)
https://arca.live/b/aiart/141047305      ← 실제 링크는 이 후속 글에 있다
  · 최초 글에는 링크가 없다. 원글쓴이가 공유를 망설였고 후속 업데이트판에서 공개했다
  · 단부루 위키는 태그 하나 볼 때마다 페이지가 새로 뜨고 느려서 노션으로 옮겨 담은 것
  · 글 작성 시점에는 체위 관련 태그만 완성된 상태였다

# 단부루 태그를 물어보면 답해 주는 NotebookLM 노트북 (2026-04)
https://notebooklm.google.com/notebook/893681d5-91dd-42bd-ad26-f21a384a9747
  구성 : 유의미한 태그 그룹 63개 + 채널의 태그 종합 글 txt
  · 태그 모음 CSV 를 통째로 넣으면 컨텍스트 과다로 먹통이 돼서 손으로 골라 넣었다
```

> **NotebookLM 판의 솔직한 한계** — 질문을 잘하면 나쁘지 않은 속도로 답이 나오지만
> **태그 그룹에 없는 것을 물으면 혼자 헤매다 대답을 못 한다.** 그 대기 시간이면 직접 찾는 게 나을 수도 있다고
> 원글쓴이가 인정했다.
>
> **특이한 검열 현상** — 다른 건 다 되는데 **`pussy` 태그 그룹만은 절대 안 먹히고 검열당한다**
> (penis, sex acts 같은 것은 다 된다).
> **우회법은 사이트 주소로 넣지 말고 태그를 복사해 텍스트로 넣고 이름을 설정하는 것**이며, 그렇게 하니 인식됐다.
>
> **개선 방향(댓글 2)** — 태그 그룹 형식으로 통째로 넣으면 '이게 어느 태그에 속하는지' 정도만 기억하고
> 그 안의 주소나 작동 방식은 몰라 **환각을 일으킬 가능성이 높다.** 베스트는 태그마다 따로 넣는 것이지만
> 개수 제한에 걸리므로 **자세는 자세만, 캐릭터는 캐릭터만 하는 식으로 분류별 노트북을 나눠 만들어 조합**하는 편이 낫다.
> 같은 결론이 이 문서 "6-e" 끝의 경고("LLM 에 태그 CSV 를 통째로 물리는 방식은 믿을 게 못 된다")와 이어진다.

### ⑤ 작가 태그를 새로 찾을 때 — 코믹바벨 10주년 화보 작가 목록 (2025-07)

일본 성인지 '코믹바벨' 10주년 화보 참여 작가를 **단부루 태그 표기로** 정리한 목록이다.
**이름 옆 숫자는 작성 시점의 단부루 업로드 수**로, 그 작가 태그를 모델이 얼마나 학습했을 가능성이 큰지 가늠하는 지표다.

```text
pyon-kichi 311 / kaikei kei 9 / tel 113 / shiokonbu 491 / derauea 690 / gentsuki 788 /
alp 751 / oouso 1.6k / sekiya asami 418 / sasachin (k+w) 235 / fu-ta 1.0k /
eight tohyama 220 / fujizarashi 85 / toono esuke 1 / tirotata 217 / tcw 12 /
cucchiore 118 / puyocha 93 / konka 304 / tama satou 111 / ariyoshi gen 254 /
ae iueo 112 / cotton kanzaki 73 / rimu (kingyo origin) 181 / susukumo nagi 6 / kyokucho 409
```

> **본문이 비워 둔 자리를 댓글이 채웠다** — 본문에는 태그를 '못 찾겠음' 으로 비워 둔 자리가 세 곳 있는데,
> **댓글 4가 그중 밑에서 6번째는 `Yanagi` 라고 채워 주었다.**

> **이 목록의 실제 쓸모는 '그 작가가 단부루에 있느냐 없느냐' 다**(댓글 2).
> 업로드 수가 한 자릿수인 작가(`toono esuke 1`, `susukumo nagi 6`, `kaikei kei 9`, `tcw 12`)는
> **Illustrious·NoobAI 계열이 작가 태그를 거의 못 알아들을 가능성이 크므로 기대하지 않는 게 좋다.**
> 같은 판단 기준이 이 문서 "6-c" 의 단부루 검색 툴(컷오프 날짜 기준 15장 이상이면 시도할 가치가 있다)에도 쓰인다.

→ 화풍을 눈으로 고르는 대조표는 위 "6-f", 문법은 [프롬프트 쓰는 법](prompting.md)


<small>근거 — [내가 쓰려고 만든 태그 모음 노션 25.06](https://arca.live/b/aiart/140790436) · [NAIA2.0 버전 150 - 이벤트 프리셋 26.02](https://arca.live/b/aiart/163344011) · [코믹바벨 상업지 10주년 화보 작가 모음 25.07](https://arca.live/b/aiart/143644384) · [단부루 태그 총정리 25.06](https://arca.live/b/aiart/140170773)</small>

??? note "근거 6건 전부 보기"
    [내가 쓰려고 만든 태그 모음 노션 25.06](https://arca.live/b/aiart/140790436) · [NAIA2.0 버전 150 - 이벤트 프리셋 26.02](https://arca.live/b/aiart/163344011) · [코믹바벨 상업지 10주년 화보 작가 모음 25.07](https://arca.live/b/aiart/143644384) · [단부루 태그 총정리 25.06](https://arca.live/b/aiart/140170773) · [NAIA-WEB-Lite를 이용하여 웹에서 쉽게 랜덤태그 생… 26.01](https://arca.live/b/aiart/160107104) · [귀찮은 사람들을 위한 NotebookLM 노트북 공유 26.04](https://arca.live/b/aiart/169269240)

## 9. 후처리 · 편집 도구 — 뽑은 뒤에 쓰는 것
<small>2026-08 기준 · 근거 13건</small>

그림을 뽑은 **뒤에** 쓰는 것들이다. 배경을 지우고, 가려야 할 곳을 가리고, 말풍선을 얹고, 프롬프트를 다시 읽는 도구.

### 배경 제거 (누끼)

```
# rembg — 광고·회원가입 없이 로컬에서 (2026-07, 지금 권장)
pip install rembg[cli]
rembg p input output          # input 폴더의 이미지 전부를 처리해 output 에 넣는다
  · 파일 탐색기 주소창에 cmd 를 쳐서 그 폴더에서 명령창을 열면 경로를 칠 필요가 없다
  · 결과가 진짜 투명 PNG 인지 의심이 나왔고, 작성자가 **렌파이(Ren'Py)에 올려 확인**했다
  · 윈도우 사진 앱에도 같은 기능이 있다 (댓글)

# ABG remover — 2023년 A1111 확장 (옛 자료)
  · 확장 기능 탭의 'URL로부터 불러오기' 로 설치 후 WebUI 터미널을 완전히 닫았다 다시 연다
  · sd-depth 모델로 깊이 이미지를 만들어 마스킹하고 알파값을 넣는 방식
  · 실행하면 원본 / 마스크 / 투명배경 세 장이 나온다
  · ⚠️ 2026년 기준 **ComfyUI 의 RMBG 계열 노드가 같은 일을 더 잘한다**
```

> **어느 쪽을 쓰든 흰 배경으로 뽑은 그림이 가장 깔끔하게 떨어진다.** 생성 단계에서 프롬프트에
> `simple background, white background` 를 넣어 두면 배경이 단순해져 깊이 추정이 잘 되기 때문이다.
> 비주얼 노벨용 캐릭터 입상(立ち絵)이나 게임 에셋을 만들 때 바로 쓸 수 있다.

### 모자이크 · 블러

```
# Image Processor v1.0 — 무설치 윈도우 프로그램 (2026-05)
'Image Processor v1.0.exe' 실행. 설치 불필요
  영역 선택 : 좌클릭=점 추가 / Enter·더블클릭=확정 / 우클릭=마지막 영역 취소 / Esc=전체 취소
  단축키   : Ctrl+Z 또는 S=실행 취소 / A=직전 모자이크·블러 재적용 / D=다음 이미지 / F=일괄 저장
  대기열   : [+] 추가 / [-] 제거 / [-] 더블클릭이면 전체 비우기
  · 다각형 올가미로 여러 영역을 골라 한꺼번에 모자이크 또는 블러
  · 일괄 저장은 원본 파일명을 그대로 쓰고 중복이면 _2, _3 번호가 붙는다
  · 모자이크 크기·블러 강도는 자동 저장되며 실행 위치에 settings.json 이 생긴다
  · 국내 커뮤니티에 올릴 때 여러 장을 일괄 처리하는 용도
```

### 말풍선 — 만화를 만들 때

```
# ComfyUI-SpeechBubble — 이미지 위에 말풍선을 얹는 노드
https://kio.ac/c/blnkaN0CGwMUf2Au1Q0z4b            # (기한 있음)
설치 : custom_nodes\ComfyUI-SpeechBubble 에 풀고  pip -r requirements.txt
폰트 : 용량·저작권 문제로 빠져 있다 →  custom_nodes\ComfyUI-SpeechBubble\assets\font 에 직접 복사
출력 : image(합성본) / layer_image(말풍선만 alpha) / bubbles_info(JSON)
  탭 4개 — shape(모양) / Tail(꼬리: 삼각형·생각형·직선형, 길이는 preview 의 빨간 점을 끌어 조절)
          / HandDrawn / Text(HTML 속성이라 편집기 style 이 preview 에 그대로 렌더된다)
  · HandDrawn 이 이 노드의 핵심 — 서로 다른 주파수의 파형을 섞은 랜덤 노이즈를 path 에 더해
    외곽선을 매번 조금씩 흔든다. 끄면 매번 완전히 동일한 말풍선이 나온다
  · bubbles_info 에 preview as text 를 연결하면 JSON 이 나온다 → 저장해 뒀다 import 로 재사용
  · layer_image 를 따로 저장했다가 나중에 mask 를 invert 해 image composite masked 로 합쳐도 된다

# 말풍선을 SAM3 로 자동 검출해 대사를 채워 넣는 워크플로우 (2026-06)
git clone https://github.com/Toraong/ComfyUI-SpeechBubble
git clone https://github.com/Toraong/ComfyUI-RMBG
  Font_name 은 오픈소스 폰트 5개 동봉 / SAM3 검색어는 기본값 `speech bubble` 을 그대로 둘 것
  Segment_pick : 1이면 가장 큰 말풍선, 6이면 6번째로 큰 말풍선
  Text_Color   : 16진수 색상 코드 / 마스크 블러는 5 정도가 자연스럽다(조금 지저분해질 수 있음)
```

> ### ⚠️ SAM3 를 여러 개 쓸 때의 VRAM 함정
>
> **ComfyUI-RMBG 는 3.4GB 짜리 SAM3 모델을 노드마다 따로 로딩한다.**
>
> | 말풍선 수 | 필요 VRAM |
> |---|---|
> | 1개 | 10GB |
> | 2개 | 14GB |
> | 3개 | 18GB |
> | 4개 | 22GB |
>
> 작성자가 **모델을 한 번만 전역 로딩하도록 노드를 고쳤다.** 아래 파일을 받아 덮어쓰면
> **SAM3 노드를 10개 써도 10GB 로 끝난다.**
>
> ```text
> https://github.com/Toraong/ComfyUI-RMBG/blob/main/py/AILab_SAM3Segment.py
>    →  custom_nodes\comfyui-rmbg\py  에 덮어쓰기
> ```
>
> VRAM 32GB(5090)면 패치 없이도 말풍선 6개까지는 된다.
> **미해결 버그** — 말풍선이 좌우 끝 벽에 딱 붙어 있으면 가끔 폭을 잘못 재서 글자가 밖으로 튄다.

### 그 밖

```
# 맥용 EXIF 프롬프트 리더 — 채널 EXIF 뷰어의 Electron 앱 판 (2026-04)
https://kio.ac/c/bbq-aa0Sj1VQ5Xb6-auz0b   (비밀번호 12345)
원본 글 : https://arca.live/b/aiart/160704184
받은 파일(index.html, app.js, style.css, ui-layout-*.css, main.js, package.json)을 한 폴더에 모으고
  cd "/받은폴더경로" → npm install → npm start
앱(.app)으로 만들려면  npm run build-mac  후  open dist/mac
  · Dock 아이콘 우클릭 > 옵션 > Dock에 유지 로 고정
  · 터미널에 `cd ` 를 치고 Finder 에서 폴더를 드래그하면 경로가 자동으로 들어간다
  · dmg 배포는 macOS 코드 서명 문제로 포기해서 **사용자가 직접 빌드하는 방식**이 됐다

# sd-webui-photopea-embed — WebUI 탭 안에 웹 이미지 편집기 Photopea (2023-05, A1111 시대)
https://github.com/yankooliveira/sd-webui-photopea-embed
  · 'Send to Photopea' 로 결과를 보내 수정하고 'Send to txt2img ControlNet' 으로 전송
  · 인페인팅 마스크도 Photopea 안에서 만들어 보낼 수 있다
  · ⚠️ **인페인팅 전송 기능이 WebUI 한글화 확장과 충돌한다.** 한글화를 안 썼는데도 안 되는 사례가 있어
    확장을 전부 끄고 하나씩 켜 보며 범인을 찾으라는 조언이 붙었다. 태블릿 필압은 다소 떨어진다

# Embedding-inspector — 두 단어의 임베딩을 섞어 새 단어 만들기 (2023-01, A1111 시대)
https://github.com/tkalayci71/embedding-inspector
  섞을 두 단어를 1·2번 칸에, 새 이름을 3번 칸에, 비중을 4·5번에 넣고 Save Mixed
  · 1~2초 만에 생성돼 임베딩 폴더에 자동 저장되고, 이후 3번의 이름을 프롬프트에 그냥 적어 쓴다
  · 확장자가 .bin 으로 특이하지만 정상 동작한다. 최대 6개까지 섞어 RGB·명암·효과를 조합할 수 있다
```

→ EXIF 를 읽고 고치는 도구 전반은 위 "6-c. 채널 자작 도구", 업스케일과 화질 보정 자체는
[업스케일과 화질](upscale.md), 얼굴 재생성은 [디테일러](detailer.md) 를 보라.

### 포토샵 안에서 Stable Diffusion 돌리기 — Auto-Photoshop-StableDiffusion-Plugin (2023-03)

```
https://github.com/AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin
소개 영상: https://youtu.be/KDZloMNzNGk
```

무료 오픈소스 플러그인이고 **`.ccx` 파일 원클릭 설치**로 포토샵 안에서 바로 생성할 수 있다 (71190958, v1.2.0 기준).

| 기능 | |
|---|---|
| **ControlNet 지원** | 어떤 모델도 쓸 수 있지만 개발자는 **선화·러프 스케치에 특히 잘 맞는 `canny`** 를 추천 |
| **Heal Brush 모드** | 원치 않는 피사체 제거 |
| **GPU 가 없는 사람** | ① A1111 의 horde client 확장을 거쳐 붙기(A1111 기능을 그대로 쓸 수 있다) ② A1111 자체를 설치할 수 없으면 플러그인에서 곧바로 붙는 **Native Horde 모드**. Stable Horde 는 자원봉사자 GPU 를 빌려 쓰는 **무료 분산 생성망**이다 |
| 업스케일 | A1111 의 **Extras 탭 지원**으로 포토샵 안에서 가능 |
| 라이브 프리뷰 | 생성 과정을 캔버스에 실시간 표시 |
| ⚠ | 스마트 마스킹·이미지 검색은 **선택 사항인 무료 A1111 확장을 추가로** 깔아야 한다 |

> **검열에 막혀 도안을 못 만들 때의 우회로**로도 같은 방향이 권해진다 — 노출이 포함된 도안 같은 작업은 **로컬 AI 를 새로 구축하는 것보다 포토샵에 내장된 생성형 AI 를 쓰는 편이 훨씬 쉽다**(175410884, 한 글에서만 언급됨). 몸에 얹어 보는 것이라면 '포토샵으로 타투 넣는 법' 을 검색해 합성으로 처리하는 방법도 있다.

### ⚠ 상용 서비스의 프롬프트 템플릿은 유통기한이 있다

GPT 이미지 생성으로 3주간 템플릿을 쌓아 다시 적용해 본 기록이다 (179117331, 2026-08).

> **특수한 상황이 아닌 일반적인 의상에서의 노출조차 처음 시작했을 때보다 검열이 심해졌다.**
> 전에 잘 되던 템플릿 중 일부가 **'프롬프트 사망' 상태가 되어 참조 이미지 없이는 생성 자체가 불가능**해졌고,
> 어떤 것은 **입력 단계에서 아예 거절**돼 되살리기에 실패했다. 이유를 알 수 없이 출력 실패율만 압도적으로 높은 템플릿도 있었다.

**잘 되던 프롬프트라도 주기적으로 다시 확인해야 한다**는 것이 교훈이다.

### 출력 용량이 부담되면 — JPG 화질 85 가 변곡점이다 (2023-02, A1111 기준)

먼저 흔한 오해 하나 — WebUI 의 'text info 저장' 옵션은 **PNG 의 특정 청크**에 프롬을 저장하겠다는 뜻이고,
**JPG 와 WebP 는 애초에 EXIF 에 프롬이 저장되는 것이 기본**이라 별도 옵션 없이도 프롬이 남는다.

```text
설정 : settings → Saving images/grids → JPG 화질 0~100
```

> **핵심 수치는 85 다.** 화질이 85 를 넘는 순간 파일 용량이 기하급수적으로 불어나지만
> **85 이상부터는 원본과 육안 차이가 거의 없어**, 화질 100 은 사실상 더미 데이터로 저장장치를 채우는 짓이다(구글도 85% 를 권장한다).

| 포맷·화질 | 용량 |
|---|---|
| png | 1,322KB |
| jpg 100 | 684KB |
| jpg 95 | 307KB |
| jpg 90 | 205KB |
| **jpg 85** | **159KB** (PNG 대비 약 1/8) |

단점은 **손실 압축과 알파채널(누끼) 미지원**이다.
퀵세팅 바에 포맷·화질을 올리려면 `samples_format`, `jpeg_quality` 를 추가한다.
WebP 는 JPG 보다 30% 정도 작으면서 알파를 지원하지만 당시에는 카톡 등 일부 서비스가 못 읽어 시기상조라는 평이었다.

**⚠ 일괄 변환하면 EXIF 가 소실된다 — exiftool 로 이식한다**

```text
exiftool -TagsFromFile "PNG디렉토리\%f.png" "-PNG:parameters>UserComment" "-FileModifyDate>FileModifyDate" -ext jpg "JPG디렉토리"
```

`exiftool.exe` 로 이름을 바꿔 `C:\Windows` 에 넣어 두면 어디서든 부를 수 있다.
**`-FileModifyDate>FileModifyDate` 는 생략 가능하지만, 빼면 변환본이 전부 오늘 날짜가 되어 갤러리 정렬이 뒤섞인다.**
작업 후 생기는 `*.jpg_original` 백업은 EXIF 없는 깡통이므로 PNG 와 함께 지운다.
꿀뷰로 일괄 변환할 때는 파일명을 맞춰야 하므로 '저장되는 파일명 앞에 붙일 글자' 기본값 `수정됨_` 을 지운다.


### 그림을 다른 물건으로 만들어 주는 웹 도구

```
# パケつく | AVパッケージをつくろう！ — AI 그림을 AV 패키지 표지 컨셉으로 (2025-11)
사용법 : 준비된 표지 프리셋 중 하나를 고르고 원하는 이미지를 넣으면 끝
         일부 프리셋은 추가 이미지 삽입이나 이름 같은 텍스트 입력도 지원
  ⚠️ 뒷표지는 만들 수 없고 출력 화질이 낮다 — 저화질은 따로 업스케일을 돌려 보완한다
  · 정교한 결과물을 기대할 도구가 아니라 맛보기·재미용이라고 소개자가 선을 그었다
```

→ 인쇄용 굿즈로 뽑는 후처리(1440dpi · CMYK · 별색)는 [인페인팅](inpainting.md) 의 '아크릴 굿즈로 인쇄하기 위한 후처리' 항목

<small>근거 — [web ui 이미지편집툴 확장 (Photopea) 23.05](https://arca.live/b/aiart/76270877) · [주요 업데이트: Automatic1111 Photoshop … 23.03](https://arca.live/b/aiart/71190958) · [미연시 등 게임 캐릭터 에셋 만들때 쓰기 좋은 sd-webu… 23.01](https://arca.live/b/aiart/67056410) · [output용량이 걱정인 사람들에게 : JPG 포맷 23.02](https://arca.live/b/aiart/69024480)</small>

??? note "근거 13건 전부 보기"
    [web ui 이미지편집툴 확장 (Photopea) 23.05](https://arca.live/b/aiart/76270877) · [주요 업데이트: Automatic1111 Photoshop … 23.03](https://arca.live/b/aiart/71190958) · [미연시 등 게임 캐릭터 에셋 만들때 쓰기 좋은 sd-webu… 23.01](https://arca.live/b/aiart/67056410) · [output용량이 걱정인 사람들에게 : JPG 포맷 23.02](https://arca.live/b/aiart/69024480) · [원하는 색을 만들어서 사용해보자(3) Embedding-in… 23.01](https://arca.live/b/aiart/67003072) · [Comfy의 이미지에 말풍선을 추가하는 커스텀노드 26.06](https://arca.live/b/aiart/174020000) · [말풍선 감지해서 대사 채워넣는 워크플로우 26.06](https://arca.live/b/aiart/175373331) · [간단하게 AV 커버 만들 수 있는 사이트 25.11](https://arca.live/b/aiart/153101276) · [맥북으로 exif 프롬 리더 필요한사람? 26.04](https://arca.live/b/aiart/166644059) · [이미지 모자이크/블러 필터 추가 프로그램 26.05](https://arca.live/b/aiart/172341784) · [nai로 뽑은 사진 배경제거 광고 안 보고 하는 법 (렌파이… 26.07](https://arca.live/b/aiart/175979369) · [산란) GPT ai 그림 입문 3주간 템플릿을 한 캐릭터에게… 26.08](https://arca.live/b/aiart/179117331) · [로컬 ai라는걸 오늘 처음 안 늅늅이 질문 26.06](https://arca.live/b/aiart/175410884)

## 7. 가이드 문서 · 색인
<small>2025-12 기준 · 근거 10건</small>

```
# 2026년 4월 입문자용 정보글 모음집 — 지금 기준 최신 색인
https://arca.live/b/aiart/167283401
  1. 설치 / 2. 워크플로우 / 3. ComfyUI 설명서 / 4. 학습

# NAIA 가이드 색인 (2024-06 개설, 2026-02 까지 갱신)
https://arca.live/b/aiart/108288949
  처음이면 제작자 공식 가이드 3개만 읽어도 충분하고, 그 뒤에 검색·자동화 묶음을 본다

# 뉴비용 로컬 기초서 (2025-04) — 출판 계약이 파기되면서 통째로 공개된 개론서
https://docs.google.com/document/d/1vOWiEQTSNAtQFpPiq-YIaMna7pRzZXF8Ft7KWML-fWM/edit
  2장 확장기능 부분이 **미완성**이고 작성자 본인도 '채널만 봐도 나오는 내용' 이라고 평가했다
  SDXL·Illustrious 기준이라 2026년 ANIMA·ComfyUI 환경과는 차이가 있다
  로딩 오류가 나면 구글 드라이브 앱이 아니라 브라우저로 열 것(댓글)

# ComfyUI 기초학개론
https://arca.live/b/aiart/109722465

# 2023년 2월 채널 정보글 모음 공지 — 대부분 outdated (링크 죽음 다수)
https://arca.live/b/aiart/70255821
  작성자 본인이 댓글에서 "대부분의 자료가 outdated 되어 어디서부터 고쳐야 할지 감이 안 온다"고 적었다
  comfyui_segment_anything 리포지토리 삭제 등 죽은 링크가 보고돼 있다

# 한 작성자의 NAI 정보글 모음 (2025-12)
https://arca.live/b/aiart/158172868
  수록: NAI 사용법 떠먹기 92677065 / NAI V3 프롬프트 최신정보 92596607 / 프롬프트에 _ 언더바 금지 92642041
        스텝수 이해하기 96958882 / 프롬프트는 다다익선? 96954230 / 30분내로 끝내는 Vast.ai 158013422
  · ⚠️ **앞의 여섯 편은 2023년 NAI V3 시절 글**이라 지금(V4.5/ANIMA) 기준과 다를 수 있다
  · 작성자 본인이 단서를 달았다 — AI채널·NAI 공식 디스코드·논문·구글링·전공자 조언·개인적 추측에 의존했고
    일반인이 이해하기 쉽도록 축약·생략한 부분이 있어 실제와 100% 일치하지 않으니
    **기반 지식을 쌓는 선에서 읽으라**고 한다
  · 'NAI 의 SMEA 에 대해 짤막하게 정리' 링크는 **죽어 있다** (V3 용이라 없어도 무방하다는 것이 작성자 답)
  · 이 중 Vast.ai 글은 위 "5-c. GPU 가 없을 때" 항목에 풀어 두었다
```

**ComfyUI 로라 학습 워크플로우에 대한 주의** — 소개된 학습 워크플로우들은 **프론트엔드일 뿐이고 뒤에서 kohya 스크립트가 돈다.** 코햐로 직접 돌리는 것과 결과가 같고 UI 와 세부 설정만 다르다.

→ [처음이라면](overview.md) · [NovelAI](nai.md)

```
# AI 그림 뉴비를 위한 내비게이션 — 한두 단어로 검색하는 용어 사전
https://ainav.netlify.app/
  · 문장이 아니라 한두 단어로 검색한다. 오타·유사표기까지 잡는다('web ai'→WEBUI, '슈퍼텐서'→Safetensors)
  · ⚠️ 접속은 되지만 **업데이트가 멈춰 있어 A1111 WebUI 시절 기준**이다 (작성자 확인)
  · ComfyUI·ANIMA 시대의 내용은 없다. 모델·VAE·safetensors 같은 기본 용어용

# 모델 목록은 채널 위키 문서가 기준이다
https://arca.live/w/aiart/모델
  · 예전의 '그래서 그 모델 어디있음? 종합모음집' 글이 삭제된 뒤 이쪽으로 대체됐다

# 채널 규정
https://arca.live/b/aiart/76093127
  · ⚠️ **후원이나 광고도 수익화로 판단되어 금지**된다. 자작 도구·자료를 공유할 때 알아 둘 것
```

<small>근거 — [AI 그림 뉴비를 위한 내비게이션 23.03](https://arca.live/b/aiart/71132324) · [프롬프트 서치 사이트 공유 25.01](https://arca.live/b/aiart/125254725) · [ComfyUI 기초학개론의 집필이 완료되었습니다. 24.06](https://arca.live/b/aiart/109722465) · [뉴비용 로컬 기초서 공유 25.04](https://arca.live/b/aiart/132819559)</small>

??? note "근거 10건 전부 보기"
    [AI 그림 뉴비를 위한 내비게이션 23.03](https://arca.live/b/aiart/71132324) · [프롬프트 서치 사이트 공유 25.01](https://arca.live/b/aiart/125254725) · [ComfyUI 기초학개론의 집필이 완료되었습니다. 24.06](https://arca.live/b/aiart/109722465) · [뉴비용 로컬 기초서 공유 25.04](https://arca.live/b/aiart/132819559) · [2026년 4월 입문자용 정보글 모음집 26.04](https://arca.live/b/aiart/167283401) · [뉴비들은 webui neo 쓰자 26.07](https://arca.live/b/aiart/176802949) · [필독) AI그림 채널 정보글 모음 23.02](https://arca.live/b/aiart/70255821) · [NAIA 기능 가이드 모음 (260217) 24.06](https://arca.live/b/aiart/108288949) · [ai 모델 이상형 월드컵(최대 511개), 다른 월드컵까지 … 23.03](https://arca.live/b/aiart/72227415) · [썻던정보글모음집 25.12](https://arca.live/b/aiart/158172868)

## 8. 링크 죽음 목록 (확인된 것)
<small>2026-08 기준 · 근거 34건</small>

지우지 않고 남겨 둔다. 같은 것을 다시 찾아 헤매지 않기 위해서다.

| 무엇 | 주소 | 상태 |
|---|---|---|
| Wan 2.2 Q6_K 양자화 3종 | (본문 링크) | **링크 죽음** — 2025-11-01 만료. 대체: arca.live/b/aiart/151865975, 152063755 |
| 크퀘스타일 도트 로라 최초 배포분 | `https://kio.ac/c/aekeNTHaj9NKL4n4FuEP0b` | **링크 죽음** — 재업로드분 사용 |
| 버니니 역양자화 스크립트 | `https://kio.ac/c/bY_sY4UmJBQMX_tF7Jiz8b` | **링크 죽음** — 7일 만료 |
| ComfyUI portable 통합팩 각 판(0.11.1 ~ 0.26.0) | kio.ac (base64) | **링크 죽음** — 기한 한 달. 최신판만 유효 |
| Mubert Text-to-Music 코랩 (2022-12) | `https://huggingface.co/spaces/Mubert/Text-to-Music` | 4년 가까이 지난 글 — 서비스 상태 확인 필요 |
| 아니마 로라 학습 워크플로우 글 | (삭제됨) | 대체: `https://arca.live/b/aiart/164705533` |
| ComfyUi_NakoNode | github | **배포 중단** — 포터블 압축 안의 `custom_nodes\ComfyUi_NakoNode` 폴더를 복사해 쓴다 |
| Grok i2v 워크플로우 | — | 그록 서비스 자체가 종료 |
| 컨트롤넷 입문 6부작 번역 블로그 (2023-07) | 원문 80881919 의 외부 블로그 링크 | **링크 죽음 유력** — 댓글 다수가 '글이 막혔다', '안 보여'라고 보고. 목차만 남아 있다 |
| comfyui_segment_anything 리포지토리 | github | **삭제됨** (2023년 정보글 모음에서 보고) |
| 윈도우 탐색기 프롬프트 간편 복사기 | kio.ac (base64) | **링크 죽음** — 2026-08-07 만료 |
| 비공식 NAI 클라이언트 전반 (NAIApp 등) | — | **죽지 않았다 — 로그인 방식만 바뀌었다.** reCAPTCHA 도입으로 ID/PW 로그인은 막혔고 `Persistent API Token` 으로 대체됐다. 각 도구를 최신판으로 올리면 된다 → [NovelAI](nai.md) |
| 손발 삽입 컨셉 로라 (2025-04) | `https://kio.ac/c/dq8L0M26r0RdX2LCgKzPyb` (본문 base64 디코딩분) | **만료 추정** — 공유 기간이 **일주일**이었고 댓글에 재업 요청이 있었다 |
| 왕자림 × 이경우 NTR 로라 (2025-05) | (본문 링크) | **다운로드 불가** — 본문에 '3일간 공유', 댓글에서도 링크가 닫혔다는 요청이 이어졌다 |
| 웹툰 캐릭터 로라 시리즈의 옛 kio.ac 링크 | kio.ac | **키오스크 서버 장애로 전부 이전됨** — civitai 에서 작품명 검색 → 위 "3-b" |
| CoNAI 포터블·도커 빌드 | github | 오류 있음 — 클론하거나 압축을 풀고 배치파일로 실행 |
| 개인용 와일드카드 팩 (2026-02) | `https://kio.ac/c/a71vm3B1lQOlj1jVvdD5Wb` (본문 base64 디코딩분) | **만료 유력** — 댓글에 '사이트가 닫혔다', '연장 가능하냐' 는 반응. 출처 Civitai 링크로 개별 수급 → 위 "6" |
| 에픽세븐 신월의 루나 캐릭터 로라 (2025-01) | `https://kiosk.ac/c/012o1s1h3e281Q3Z2M1Z3P38073i0J1Y` (비번 `epicseven`) | **링크 죽음** — 2025년 1월 말 만료 |
| tirotata style 로라 (2025-01) | `https://kiosk.ac/c/012o1L2I2l011P3x303C1X0A3V2m0j0t` | **링크 죽음** — 60일 공유 |
| 도라에몽 리루루 캐릭터 로라 (2025-01) | `https://kiosk.ac/c/012o2D2x2q0m212I2Q0U2k2T0I1n2U1q` | **링크 죽음** — 본문에 '3월 28일까지' 명시 |
| '롱 믹스' 병합모델 (2023-04) | `https://drive.google.com/file/d/1slPrjzXMXlcYYDKudKmTPeFCSb1iS-UE/view` (본문 base64) | **만료 유력** — 2023년 구글드라이브 링크. 8GB 초과 무압축본이라 코랩 로딩도 터진다 |
| 설화 모음집(2023 국내 병합모델 샘플) | `https://drive.google.com/drive/folders/147ImFn3SINYCMHUd5Sdw_LI9xdMJG045` | 2023-04 링크 — 상태 확인 필요. **그 글의 남는 값어치는 샘플이 아니라 그때 이미 배포처에서 사라져 있던 모델 목록**(UnetPastelAbyss, AreKore Edition v1.0, AniDosMix V2/Final, dualcamellusion, MIX-HIRES-V3, MMix1.0, Septen Trigger, MoonTea 등)이다 |
| 하이퍼링크만 걸린 2023년 배포글 전반 | — | 본문에 URL 텍스트가 남아 있지 않아 **복원 불가**한 경우가 많다(ExpMix·ZemiHR 계열) |
| **'일주일동안 만든 로라 결산' 30여 종 (2023-02)** | `https://drive.google.com/drive/folders/1wkZecNOo5IEKefSvGZU_dZGx6vEkHP5u` | 🔴 **파일 자체가 없다.** 재업 요청에 작성자가 *"옛날 SD 1.5 시절 구닥다리여서 삭제했고 컴터도 바꿔서 소실돼버렸습니다"* 라고 **댓글에서 확인**했다 |
| 한복 로라 v1 · v2 (2023-02) | 구글 드라이브 | 2023년 개인 공유 링크 — **만료 유력** |
| hiro(아케비의 세일러복) 스타일 로라 (2023-03) | `https://drive.google.com/file/d/1IymacxUzrnFSG5xYRu4WwtWTQ_HQ2y-H/view` | 2023년 개인 공유 — **만료 유력**. 학습 베이스가 Anything V3.0(SD1.5)이라 현행 계열엔 안 붙는다 |
| 동방프로젝트 첸·오린·쇼·미케 로라 (2023-03) | `https://drive.google.com/drive/folders/18P5_Coe8-XZSnU05kqThOOF0RN0wvrw1` | 2023년 링크 — 상태 확인 필요. **`test` 폴더의 학습 데이터셋+태그 파일**이 이 글의 값어치다 |
| 요가 포즈 컨트롤넷 자료 (2023-03) | `https://drive.google.com/file/d/1uXy7x-5fw990_rrrycxeul4kWYQndmZS/view` | 2023년 링크 — **만료 유력.** 남는 것은 전처리기·가중치 판단 기준 → 위 "4-c" |
| ComfyUI 워크플로우 공모전 출품작 모음 (2025-07) | `https://kio.ac/c/aPj7B1OOlRTir8e0FsnzGb` | **기한 1달 — 만료 유력.** 개별 출품작 글은 채널 **[대회] 탭**에 남아 있다 |
| 무직전생 아이샤 로라 (2023-05) | `https://drive.google.com/drive/folders/18krIgfWp277620RJdhodYtaznMEfZ0r9` | 2023년 링크 — 만료 유력 |

### ⚠ 만료 가능 — 지우지 않고 표시만 해 둔다 (이번 확인분)

아직 죽었다고 확인되지는 않았지만 **개인 공유·임시 파일 서비스라 언제든 사라질 수 있는 것**들이다.

| 자료 | 링크 종류 | 비고 |
|---|---|---|
| 단부루 태그 기반 프롬프트 생성기 개조본 (2026-05) | **Proton Drive** 개인 공유 | 원본은 원문 169288451 |
| NAIA + 외부 고해상도 수정 Extension (2026-06) | **Proton Drive** 개인 공유 (버전별로 여러 개) | — |
| NAI 그림체 테스트 HTML (2026-02) | **mega** | 위 '작가명 썸네일 뷰어' 절 참조 |
| Kusayarou 그림체 로라 (2026-04) | **kio.ac** (base64 로 가려져 있었고 디코딩됨) | `https://kio.ac/c/bqpB01iFAlJ_96NqtBLz0b` — 임시 파일 공유 서비스 |
| 여성 의상 프롬프트 공유 페이지 (2026-07) | `prompt.mifplus.com/outfitlist.php` | **'다음 주 수요일까지' 기간 한정 공개 — 지금은 만료됐을 가능성이 높다** |
| 캡셔닝용 Colab 노트북 (2026-02) | 개인 구글 드라이브 공유 | 위 '6-c-2' 절 참조 |


<small>근거 — [컨트롤넷 초보 기본 사용법 (Openpose, 전처리기 종류… 23.07](https://arca.live/b/aiart/80881919) · [일주일동안 만든 로라 결산 (모음집 업데이트) 23.02](https://arca.live/b/aiart/70704280) · [ai 뮤직 넌 미쳤다 @@추가 정보 있음 22.12](https://arca.live/b/aiart/64778052) · [아니마 가능)싹싹 긁어 모은 개인용 와일드카드 팩 26.02](https://arca.live/b/aiart/162850344)</small>

??? note "근거 34건 전부 보기"
    [컨트롤넷 초보 기본 사용법 (Openpose, 전처리기 종류… 23.07](https://arca.live/b/aiart/80881919) · [일주일동안 만든 로라 결산 (모음집 업데이트) 23.02](https://arca.live/b/aiart/70704280) · [ai 뮤직 넌 미쳤다 @@추가 정보 있음 22.12](https://arca.live/b/aiart/64778052) · [아니마 가능)싹싹 긁어 모은 개인용 와일드카드 팩 26.02](https://arca.live/b/aiart/162850344) · [comfyui portable v0.20.1 + sage +… 26.04](https://arca.live/b/aiart/169293039) · [ComfyUI 워크플로우 공모전 마무리 및 수상자 발표 25.07](https://arca.live/b/aiart/143116458) · [아 한복 로라 누가 공유해줬네 23.02](https://arca.live/b/aiart/69440453) · [Comfyui portable v0.26.0 + sage 외… 26.06](https://arca.live/b/aiart/175163102) · [필독) AI그림 채널 정보글 모음 23.02](https://arca.live/b/aiart/70255821) · [청아) 도라에몽 극장판 철인병단 리루루 로라 만들었음 (+공… 25.01](https://arca.live/b/aiart/127342012) · [요가 자세 포즈 몇 개 만든거 공유 (컨트롤넷) 23.03](https://arca.live/b/aiart/71112036) · [설화모음집 위키ver 끝 23.04](https://arca.live/b/aiart/73816109) · [Comfyui portable v0.23.0 + sage +… 26.06](https://arca.live/b/aiart/172596107) · [크퀘스타일 도트 로라 공유 26.04](https://arca.live/b/aiart/167362821) · [NAIA+외부 고해상도 이미지 수정 Extension 제작해… 26.06](https://arca.live/b/aiart/174711559) · [직접 만든 여성 의상 -8- 26.07](https://arca.live/b/aiart/175557540) · [hiro 스타일(아케비의 세일러복 작가) LORA 공유 23.03](https://arca.live/b/aiart/71891910) · [NAI 자동생성 앱 (NAIApp) v1.4.0 26.04](https://arca.live/b/aiart/168830995) · [NAI 자동생성 앱 (NAIApp) v1.5.1 핫픽스 26.07](https://arca.live/b/aiart/176933271) · [왕자림 x 이경우 NTR 로라 공유 25.05](https://arca.live/b/aiart/135597261) · [(Q6_K)Smooth Mix Wan I2V high+Low… 25.10](https://arca.live/b/aiart/151608989) · [(윈도우탐색기에서 프롬프트 간편 복사기) ~ 8.7.아침까지… 26.07](https://arca.live/b/aiart/176179807) · [고어, 이상성욕) 방금만든 손발 삽입로라 공유 25.04](https://arca.live/b/aiart/134892006) · [에픽세븐-신월의루나 캐릭터 로라 공유 25.01](https://arca.live/b/aiart/126126545) · [(모델공유) (요청) 롱 믹스 (링크 수정) 23.04](https://arca.live/b/aiart/74350978) · [(noob-vpred) tirotata style lora … 25.01](https://arca.live/b/aiart/126429473) · [단부루 기반 AI 이미지 프롬프트 생성기 개조 버전 26.05](https://arca.live/b/aiart/169490491) · [(인외,몬무스,퍼리) Kusayarou 그림체 로라 공유 26.04](https://arca.live/b/aiart/167861783) · [무직전생 아이샤 그레이렛 LoRA 23.05](https://arca.live/b/aiart/77356160) · ["버니니 다시왔네" 제작법 및 초간단 후기 (역양자화 파이선… 26.07](https://arca.live/b/aiart/175630790) · [동방프로젝트 첸,오린,쇼,미케 LoRA 모델 23.03](https://arca.live/b/aiart/71116117) · [nai 그림체 테스트하는 페이지 공유 26.02](https://arca.live/b/aiart/161192747) · [CoNAI로 변경된 이미지+영상관리 시스템 ㅠ 26.03](https://arca.live/b/aiart/165939813) · [colab으로 VLM을 실행해보자. 26.02](https://arca.live/b/aiart/161842488)

## 3-b-2. 웹툰·애니 캐릭터 로라 — 2025 후반 ~ 2026 추가분과 ANIMA 전환
<small>2026-07 기준 · 근거 29건</small>

위 "3-b" 와 **같은 제작자·같은 규격**의 후속 배포다. **공통 재료는 하나뿐이니 여기서 한 번만 읽고,
아래 표는 어느 작품이 있고 어디서 받는지만 본다.**

### 공통 재료 (Illustrious 판 · 2025)

| 항목 | 값 |
|---|---|
| LoRA 학습 베이스 | `illustriousXL_v1.1` |
| 실제 생성 체크포인트 | `WaiNSFWillustrious V140` |
| 학습 도구 | **로컬 `kohya ss`** (civitai 온라인 트레이너가 아니다) |
| 학습 설정 출처 | `https://arca.live/b/hypernetworks/110021224` (포리x 개정판)에서 **로라 타입·해상도·Epoch 만 바꿔** 쓴다 |
| 워크플로우 복원 | 예시 이미지를 **ComfyUI 캔버스에 끌어다 놓으면** 노드가 그대로 불러와진다 |
| 프롬프트 | 배포글이 아니라 **각 CivitAI 모델 페이지**에 있다 |
| VAE | 특별한 것이 아니라 **평범한 `SDXL VAE`** (댓글 확인) |
| 공통 한계 | **의상 · 장식 · 특이한 눈동자 · 문신**은 제대로 구현되지 않을 수 있다 |

### ⚠️ 2026 — ANIMA 계열로 갈아탔다

```text
LoRA 학습 베이스   anima-base-v1.0
생성 체크포인트    waiANIMA_v10Base10
※ Illustrious 용 LoRA 와는 호환되지 않는다. 체크포인트를 계열에 맞춰야 한다
※ 링크 도메인이 civitai.com 에서 civitai.red 로 바뀌었다
```

| 작품 | 종수 | 시점 | 계열 |
|---|---|---|---|
| 히어로 킬러 | 24종 | 2025-07 | ILXL |
| 킬러경찰(다시 돌아온 혈귀 경찰) | 14종 | 2025-07 | ILXL |
| 모르는 여자랑 하라구요? | 5종 | 2025-08 | ILXL |
| 놀이감 | 7종 | 2025-08 | ILXL |
| 신과함께 돌아온 기사왕님 | 11종 | 2025-08 | ILXL |
| 인턴해녀 | 5종 | 2025-09 | ILXL |
| 일렉시드 | 15종 (`civitai 1952007~1952196`) | 2025-09 | ILXL |
| 부패의 사제 | 7종 | 2025-10 | ILXL |
| 네크로맨서 학교의 소환천재 | **22종** (`civitai 2146777~2147270`) | 2025-11 | ILXL |
| 2회차 환관이 남성을 되찾음 | 8종 (`civitai 2172491~2172590`) | 2025-11 | ILXL |
| 회귀한 용병은 다 계획이 있다 | 6종 (`civitai 2189935~2190010`) | 2025-12 | ILXL |
| 저 그런 인재 아닙니다 | 9종 (`civitai 2211271~2211410`) | 2025-12 | ILXL |
| 파브르 in 사천당가 | 7종 (`civitai 2243146~2243237`) | 2025-12 | ILXL |
| 화이트데이(게임, 2017.ver) | 4종 — 한소영·김성아·설지현·유지민 | 2025-05 | ILXL |
| 입학용병 | 10종 (`civitai 726145~1792511`) | 2025-07 | ILXL |
| 별이삼샵 | 2종 — 김다슬 `1795350` · 설효림 `684540` | 2025-07 | ILXL |
| **현실퀘스트** | 9종 | 2026-06 | **ANIMA** |
| **화이트데이** | 4종 — `civitai.red 1727433 / 1727335 / 1727614 / 1727691` | 2026-07 | **ANIMA** |
| **아카데미에서 살아남기** | 17종 | 2026-07 | **ANIMA** |
| **아카데미에 위장취업당했다** | 약 30종 (`civitai.red 2808198~2808356` 대) | 2026-07 | **ANIMA** |

### 개별 로라 · 컨셉 로라

| 무엇 | 트리거 / 세팅 | 받는 곳 |
|---|---|---|
| 기어스 눈 (코드기어스) — ANIMA 컨셉 | 붉은 띠가 안 나오면 `red glowing eyes` 가중치 ↑ 또는 로라 가중치 ↑ | `https://civitai.red/models/119685/geass-eyes` |
| 하이그레 자세·의상 (짱구 극장판) — ANIMA 컨셉 | 가끔 자세가 엇갈리거나 섞인다 | `https://civitai.red/models/941059/haigure-outfit-and-pose` |
| 마법천자문 7종 (Pony / ILXL) | 그림체 태그를 안 넣으면 원작 그림체 (단 `Wai` 기준). 데이터는 구글 북에서 만화를 구매해 캡처 | 손오공 `523192` · 삼장 `525049` · 샤오 `541721` · 옥동자 `1400656` · 혼세마왕 `1400251` · 이랑 `1400349` · 돈돈 `1401213` |
| 치즈인더트랩 5종 | `lr9hs`(홍설) `lr9kay` `lr9jbr` `lr9bih` `lr9njy` | 본문 kio.ac 가 아니라 **`https://arca.live/b/aiart/149271136`** |
| K-버츄얼 3D 그림체 | 트리거 `3d` · 학습 `Illustrious XL 1.0` · 예시 `3D-Stock v2.0` | `https://civitai.com/models/1869863/3d-virtual-anime` |
| 고어 작가 로라 5종 (ILXL) | `lazyman` / `hatrx` / `blslmx` / `chifudoon` / `gblptto` | civitai `1405248` · `1217814` · 나머지는 mega |
| Hechima(issindotai) 스타일 | `hech1ma` — **넣든 안 넣든 차이가 없었다**고 배포자가 밝혔다 | `https://civitai.com/models/2131530/hechima-style-or-illustrious` |
| 에픽세븐 4종 (NoobAI V-Pred 1.0 학습) | `bystander_hwayoung` · `remnant_violet` · `lone_crescent_bellona` · `new_moon_luna` | **기간 일주일 — 만료** |

### 실전 요령 몇 가지

- **치즈인더트랩** 5종은 캐릭터마다 '높은 가중치' 판과 '**낮은 가중치 + 체크포인트 변경**' 판을 나란히 보여 준다 —
  캐릭터 로라는 **가중치를 낮추고 체크포인트를 바꾸는 조합으로도 재현되는 경우가 많다.**
  `il2.0` · `NoobAI ep0.75` · `ep1.1` · `Addillust4.0` · `ILpersonalmerge3.0` 에서 두루 동작한다.
- **최신 버전이 항상 낫지 않다.** WAI 15 가 나왔는데도 `V140`(14)을 계속 쓰는 이유를 묻자
  **'15는 눈이랑 손가락이 14보다 더 이상하게 나와서'** 라고 답했다. 다른 제작자도 `wai v14` 가 가장 예쁘고
  v16 도 괜찮다고 평했다.
- **제작 요청이 거절되는 기준 = 로라를 못 만드는 조건**이다 — 학습 이미지가 아예 없거나(좋은 품질 데이터가
  1장뿐인 경우 포함), 캐릭터 이름이 잘 나오지 않거나, 분량이 지나치게 많은 작품.

→ 굽는 쪽은 [로라 쓰는 법](lora-usage.md) 의 "굽기 준비 ① — 무엇을 베이스로 구울 것인가"


### 만화 원작 캐릭터 로라

```
# 코믹 메이플스토리 캐릭터 로라 2종 (2025-04)
https://civitai.com/models/1479558   # 아르웬  — 5권 이전 모습은 데이터셋에서 제외
https://civitai.com/models/1479578   # 라케니스 — 첫 등장 / 마녀 복장 / 후드 로브 3종 의상 포함
  ⚠️ 배포글이 두 링크에 같은 modelVersionId 를 달아 놓아 오기 가능성이 있다 — 모델 페이지에서 버전을 직접 확인할 것
  · 예시 이미지를 뽑을 시간이 없어 공유가 늦었다고 밝혔다
  · 후속으로 '판타지 수학대전' 데이터셋도 구했으나 화질이 나빠 학습이 오래 걸릴 것 같다고 함
    → 만화 스캔 기반 로라는 원본 화질이 곧 병목이다
```

<small>근거 — [웹툰 캐릭터 Lora 공유) 히어로 킬러 25.07](https://arca.live/b/aiart/141649376) · [스압)마법천자문 캐릭터 7명 IL 로라 CivitAI에 올림 25.03](https://arca.live/b/aiart/132320391) · [웹툰 캐릭터 Lora 공유) 킬러경찰 25.07](https://arca.live/b/aiart/142253313) · [K-버츄얼 그림체 로라 공유 25.08](https://arca.live/b/aiart/145274862)</small>

??? note "근거 29건 전부 보기"
    [웹툰 캐릭터 Lora 공유) 히어로 킬러 25.07](https://arca.live/b/aiart/141649376) · [스압)마법천자문 캐릭터 7명 IL 로라 CivitAI에 올림 25.03](https://arca.live/b/aiart/132320391) · [웹툰 캐릭터 Lora 공유) 킬러경찰 25.07](https://arca.live/b/aiart/142253313) · [K-버츄얼 그림체 로라 공유 25.08](https://arca.live/b/aiart/145274862) · [웹툰 캐릭터 Lora 공유) 별이삼샵 설효림, 김다슬 25.07](https://arca.live/b/aiart/142923442) · [웹툰 캐릭터 Lora 공유) 놀이감 25.08](https://arca.live/b/aiart/145481603) · [웹툰 캐릭터 Lora 공유) 2회차 환관이 남성을 되찾음 25.11](https://arca.live/b/aiart/155204071) · [웹툰 캐릭터 Lora 공유) 모르는 여자랑 하라구요? 25.08](https://arca.live/b/aiart/144614023) · [웹툰 캐릭터 Lora 공유) 저 그런 인재 아닙니다 25.12](https://arca.live/b/aiart/156388159) · [웹툰 캐릭터 Lora 공유) 파브르 in 사천당가 25.12](https://arca.live/b/aiart/157461151) · [웹툰 캐릭터 Lora 공유) 회귀한 용병은 다 계획이 있다 25.12](https://arca.live/b/aiart/155693668) · [Anima 웹툰 캐릭터 Lora 공유) 아카데미에서 살아남기 26.07](https://arca.live/b/aiart/176619574) · [웹툰 캐릭터 Lora 공유) 입학용병 25.07](https://arca.live/b/aiart/142870110) · [웹툰 캐릭터 Lora 공유) 네크로맨서 학교의 소환천재 25.11](https://arca.live/b/aiart/154565123) · [웹툰 캐릭터 Lora 공유) 부패의 사제 25.10](https://arca.live/b/aiart/150271493) · [Anima 웹툰 캐릭터 Lora 공유) 현실퀘스트 26.06](https://arca.live/b/aiart/175287930) · [Anima 게임 캐릭터 Lora 공유) 화이트데이 26.07](https://arca.live/b/aiart/175617365) · [Anima 컨셉 Lora 공유) 하이그레 자세와 의상 26.05](https://arca.live/b/aiart/171864098) · [웹툰 캐릭터 Lora 공유) 인턴해녀 25.09](https://arca.live/b/aiart/146809624) · [웹툰) 치즈인더트랩 로라 공유 25.06](https://arca.live/b/aiart/139739277) · [웹툰 캐릭터 Lora 공유) 일렉시드 25.09](https://arca.live/b/aiart/147768075) · [웹툰 캐릭터 Lora 공유) 신과함께 돌아온 기사왕님 25.08](https://arca.live/b/aiart/146268794) · [Anima 웹툰 캐릭터 Lora 공유) 아카데미에 위장취업당… 26.07](https://arca.live/b/aiart/178038139) · [게임 캐릭터 Lora 공유) 화이트데이: 학교라는 이름의 미… 25.05](https://arca.live/b/aiart/137118271) · [고어, 페도, 스압주의) 고어작가 로라 몇개 (ILXL) 25.05](https://arca.live/b/aiart/136124750) · [Anima 컨셉 Lora 공유) 기어스 눈 (기어스에 걸린 … 26.05](https://arca.live/b/aiart/171229773) · [스타일 LoRA) Hechima (issindotai) 스타일 25.11](https://arca.live/b/aiart/153935164) · [코믹 메이플 캐릭터 로라 2종(아르웬, 라케니스) 25.04](https://arca.live/b/aiart/134271092) · [에픽세븐 캐릭터 로라 공유 (신월의 루나, 월광 벨로나, 잔… 25.08](https://arca.live/b/aiart/146053426)

## 3-e. ⚠️ 배포글 본문이 틀렸던 것들 — 정정은 댓글에 있다
<small>2026-01 기준 · 근거 9건 · 자료 엇갈림</small>

**본문을 그대로 믿으면 헛수고를 하는 것들**이다. 넷 다 작성자 본인이나 댓글에서 정정됐다.

### 1) "WebUI 용 Metadata 파일이 동봉되어 있습니다" — 이제 지원하지 않는다

| | 무엇이라 했나 |
|---|---|
| ❌ **본문** | "Metadata 파일명과 LoRA 파일명을 같게 하고 같은 폴더에 넣으세요" |
| ✅ **댓글 (작성자 본인)** | 파일을 못 찾겠다는 질문에 **"메타데이터 파일은 이제 지원하지 않아요"** |

**이 설명은 틀렸다.** 동봉되던 시기(2025-08-27 `146268794` 등)의 글에는 유효하지만,
그 뒤 글의 본문 문구는 남아 있을 뿐 실제로는 파일이 들어 있지 않다. **찾아 헤맬 필요가 없다.**

### 2) "아무리 찾아도 ilxl 베이스 마나카 모델이 없다" — 있었다. 그런데…

| | |
|---|---|
| ❌ **본문** | ilxl 베이스 사죠 마나카 LoRA 는 없고 SD1.5 같은 구식만 있다 |
| ✅ **댓글** | `https://civitai.com/models/1388829?modelVersionId=1569544` 를 제시 |
| ⚠️ **그 댓글의 단서** | **그 작성자도 "지금 찾아보니 없네, 삭제됐나" 라고 덧붙였다** |

**본문의 '없다' 는 사실과 달랐지만**, 글 작성 시점에 시비타이에서 내려가 있었을 가능성도 함께 남는다.
**양쪽을 다 적어 둔다.** 두 로라를 같이 쓰니 퀄리티가 올라가고 찐빠가 줄었다는 후기가 달렸다.
(본문 로라는 `https://civitai.com/models/1950918` · 권장 강도 **0.7**)

### 3) `gucci backpack` 은 사실 루이비통 가방이었다

한예나 v2 로라의 교복 세트 프롬프트에 들어 있던 태그다.

```text
school uniform, white dress shirt, necktie, collar, pencil skirt,
gucci backpack,        ← 실제로는 구찌가 아니라 루이비통 가방이었다 (글쓴이 인정)
grey blazer, white sneakers
```

**태그가 실제 사물과 다르면 다른 모델에서는 원하는 결과가 안 나올 수 있다.**
남의 프롬프트를 그대로 옮길 때는 태그가 실물과 맞는지 확인해야 한다.

### 4) 아카라이브 첨부 이미지의 EXIF — 조건에 따라 갈린다

| 쪽 | 무엇이 확인됐나 |
|---|---|
| **남지 않는다** | 아카라이브 첨부 이미지에는 EXIF 가 남지 않아 프롬프트 추출 노드에 넣어도 아무것도 안 나온다 |
| **남는다** | 치즈인더트랩 배포자 — **"첨부 이미지는 전부 `1000x1500` 이하라 EXIF 가 살아 있다"** (아카라이브는 **큰 이미지의 EXIF 를 지우는 경우가 있다**). 치가라시 마히나 배포자도 "첨부 이미지에는 모두 EXIF 가 들어 있어 세팅을 그대로 볼 수 있다" |

**즉 이미지를 줄여 올리면 EXIF 가 살아남는다.** 프롬프트를 남기려는 배포자는 크기를 줄여 올린다.
프롬프트를 통째로 얻고 싶을 때 가장 확실한 곳은 여전히 **civitai 에 올린 이미지의 설명란**이다.

### 1) 의 근거 — 같은 정정이 두 글에서 반복됐다

| 글 | 본문 | 정정 |
|---|---|---|
| **143481842** 웹툰 '모비딕' 7종 (2025-07) | "WebUI 용 Metadata 파일이 동봉되어 있다" | 같은 작성자가 후속 글 댓글에서 **"메타데이터 파일은 더 이상 지원하지 않고 Civitai 의 트리거 내용을 쓰라"** 고 정정 |
| **144042734** 웹툰 '정글쥬스' 12종 (2025-08) | "Metadata 파일명과 LoRA 파일명을 똑같이 유지해 같은 폴더에 넣으라" | 파일이 없다는 지적을 받자 작성자가 같은 답을 반복 |

**즉 트리거 워드는 각 Civitai 페이지에서 확인해야 한다.**

같은 시리즈의 댓글에서 나온 다른 실전 정보 둘도 함께 적어 둔다.

- **로라 베이스로 `illustriousXL 2.0` 은 전체적으로 결과가 좋지 못했다.** `1.1` 은 `1.0` 을 약간 개선한 정도라 큰 차이가 없어 **1.1 을 쓴다.**
- **데이터셋 이미지 크기는 억지로 늘리거나 줄일 필요가 없다** — 학습툴이 알아서 처리한다.

### 5) 트리거 태그가 캐릭터 이름과 뒤바뀐 로라

'이 시국에 개인교습' 주연 3인방 로라(138627507, 2025-06)는 **데이터셋 태깅에서 여캐 2명의 이름을 서로 반대로 입력한 실수**가 있다.
**재학습이 귀찮아 그대로 배포**됐으므로 **트리거를 반대로 적어야 한다.**

```text
설채은  →  ch4ew0n   ← 이름과 뒤바뀜
설채원  →  ch4eeun   ← 이름과 뒤바뀜
김유찬  →  yuch4n
```

같은 글의 실전 주의점 둘 — 네거티브에 **`speech bubble` 을 반드시 넣어야** 그림마다 말풍선이 튀어나오지 않고,
떡툰 특유의 **흰 모자이크**를 원하면 `blank censor` 를 입력한다.


### 6) 옛 병합모델 배포글은 링크가 죽고 정정이 댓글에 남는다

| 글 | 무엇이 틀렸나 |
|---|---|
| **MIX-Pro-V4_Beta** (70413762, 2023-02) | 본문의 `MIX-Pro-V4.safetensors` 링크가 **이후 무효화**됐다. 댓글이 대체 링크를 안내한다 — `huggingface.co/GIMG/AIChan_Model/resolve/main/Blend/MIX-Pro-V3.5%2BLignes.safetensors` · `civitai.com/models/14206`. **글쓴이 본인도 "테스트하다 V3 보다 못한 부분이 있었다" 고 인정**했으므로 V4 를 굳이 찾을 이유도 없다. 예시 EXIF 는 `huggingface.co/GIMG/AIChan_Model/tree/main/Blend/Pro-example-V4` |

<small>근거 — [(병합대회) MIX-Pro-V4_Beta 23.02](https://arca.live/b/aiart/70413762) · [웹툰) 한예나 v2 25.06](https://arca.live/b/aiart/140973650) · [웹툰 캐릭터 Lora 공유) 별이삼샵 설효림, 김다슬 25.07](https://arca.live/b/aiart/142923442) · [웹툰 캐릭터 Lora 공유) 정글쥬스 25.08](https://arca.live/b/aiart/144042734)</small>

??? note "근거 9건 전부 보기"
    [(병합대회) MIX-Pro-V4_Beta 23.02](https://arca.live/b/aiart/70413762) · [웹툰) 한예나 v2 25.06](https://arca.live/b/aiart/140973650) · [웹툰 캐릭터 Lora 공유) 별이삼샵 설효림, 김다슬 25.07](https://arca.live/b/aiart/142923442) · [웹툰 캐릭터 Lora 공유) 정글쥬스 25.08](https://arca.live/b/aiart/144042734) · [웹툰 캐릭터 Lora 공유) 모비딕 25.07](https://arca.live/b/aiart/143481842) · [웹툰 Lora) 이 시국에 개인교습 - 주연 3인방 25.06](https://arca.live/b/aiart/138627507) · [웹툰) 치즈인더트랩 로라 공유 25.06](https://arca.live/b/aiart/139739277) · [(캐릭터 LoRA공유) ilxl베이스의 사죠 마나카 lora… 25.09](https://arca.live/b/aiart/147745539) · [스케어리 캠퍼스 칼리지 유니버시티 - 치가라시 마히나 로라 … 25.06](https://arca.live/b/aiart/139055598)

## 8-b. 만료된 배포 목록 (2025 로라 · 확인분)
<small>2026-03 기준 · 근거 9건</small>

**지우지 않고 남긴다** — 같은 것을 다시 찾아 헤매지 않기 위해서다.
`kio.ac` / `kiosk.ac` 는 기한이 있는 임시 공유라 오래된 배포글은 대부분 죽어 있다.

| 무엇 | 기한 | 상태 |
|---|---|---|
| **웹툰 '동아리' 백가인** (트리거 `backgain`) | kio.ac 3개 링크 | 🔴 **복구 불가** — 아래 참조 |
| 웹툰 한예나 **v2** (ILXL / Pony 두 판) | **1개월** | 만료. 글쓴이가 재공유를 여러 번 반복했다 |
| 웹툰 한예나 **v3** (WAI14) | '하루만 복구' 반복 | 만료. 이후 신버전을 두 차례 게시했으므로 **최신판을 찾는 편이 낫다** |
| 웹툰 별이삼샵 설효림 (`hyorim2` / `hyo2`) | 반복 만료 | 만료 |
| 스케어리 캠퍼스 치가라시 마히나 (`chigarasi mahina`) | **일주일** | 만료 |
| 에픽세븐 4종 (NoobAI V-Pred 1.0) | **일주일** | 만료 |
| 떡신(체위) 컨셉 로라 3종 (ILXL v1.0) | **2달** | 만료 추정 |
| 웹툰 한예나 (wai16 판, `hanyena`) | 4/13 · 6/29 두 번 | 만료 |
| 코이카츠 정규화 이미지 700장 + 워크플로우 | **2025-03-29 명시** | 만료 (다만 **워크플로우는 본문 예시 이미지의 EXIF 로 복원 가능**) |

### 🔴 재업로드를 기대할 수 없는 것

**웹툰 '동아리' 백가인 로라(`136255690`)** — kio.ac 링크가 모두 만료된 데 더해,
**글쓴이가 ANIMA 로 넘어가면서 `ilxl` 파일을 전부 지웠다고 마지막 댓글에서 밝혔다.**
**원본 파일 자체가 사라져 복구가 불가능하다.**

그래도 남는 것이 있다 — 트리거와 태그다.

```text
트리거   backgain
기본     very long hair, bangs, black hair, purple hair, purple eyes, large breasts, parted lips
의상 ①   cleavage, bare shoulders, off shoulder, sweater, long sleeves, skirt, pencil skirt, black skirt
의상 ②   choker, camisole, bare shoulders, black skirt, crop top, pencil skirt, black skirt, thigh strap
의상 ③   crop top, cleavage, choker, off shoulder, bare shoulders, pencil skirt, miniskirt,
         camisole, midriff, open jacket, black jacket
같이 쓰면 좋은 것   circles manhwa style v1.0 (Illustrious LoRA) @ 0.8
예시에 섞여 있던 'ILv10-PN19' 의 정체 → https://civitai.com/models/1158891/detailed-panties-lora
```

### 죽었을 때

**댓글의 대체 링크를 먼저 본다.** base64 로 가려 올린 것은 디코더에 넣으면 실제 주소가 나오고,
시리즈물이면 **civitai 에서 작품명으로 검색**하는 편이 빠르다.


<small>근거 — [웹툰) 별이삼샵 설효림 로라 공유 25.06](https://arca.live/b/aiart/140762910) · [코이카츠 3D 스크린샷만으로 2D 캐릭터 학습 25.01](https://arca.live/b/aiart/127423265) · [웹툰 Lora 공유함 동아리 백가인 25.05](https://arca.live/b/aiart/136255690) · [웹툰) 한예나 v2 25.06](https://arca.live/b/aiart/140973650)</small>

??? note "근거 9건 전부 보기"
    [웹툰) 별이삼샵 설효림 로라 공유 25.06](https://arca.live/b/aiart/140762910) · [코이카츠 3D 스크린샷만으로 2D 캐릭터 학습 25.01](https://arca.live/b/aiart/127423265) · [웹툰 Lora 공유함 동아리 백가인 25.05](https://arca.live/b/aiart/136255690) · [웹툰) 한예나 v2 25.06](https://arca.live/b/aiart/140973650) · [웹툰) 지겹다 지겨워! 또왔다 한예나로라 공유 25.08](https://arca.live/b/aiart/144186702) · [웹툰로라) 한예나 26.03](https://arca.live/b/aiart/164851217) · [그냥 학습시킨 떡신 로라 3개 공유입니다 25.04](https://arca.live/b/aiart/134371628) · [에픽세븐 캐릭터 로라 공유 (신월의 루나, 월광 벨로나, 잔… 25.08](https://arca.live/b/aiart/146053426) · [스케어리 캠퍼스 칼리지 유니버시티 - 치가라시 마히나 로라 … 25.06](https://arca.live/b/aiart/139055598)

## 3-f. 받는 곳이 civitai 라면 — 검열·등급 필터 때문에 안 보이는 것
<small>2025-10 기준 · 근거 4건</small>

"분명히 있다는데 검색이 안 된다" 의 원인은 대개 둘 중 하나다.

### 1) 등급 필터 — 계정 설정에서 X/XXX 를 켜라

모델이 '사라졌다' 는 댓글이 있었는데 실제로는 **계정 설정에서 X/XXX 등급을 보이도록 바꾸면 나왔다.**
**civitai 에서 모델이 안 보일 때 제일 먼저 확인할 것이 이 등급 필터다.**

배포자 쪽 대응도 있다 — `loli` 처럼 **시비타이 금지어**가 들어가는 프롬프트는
**트리거 워드에만 넣고 예시 이미지 프롬프트에서는 빼는** 식으로 우회한다.

### 2) 애초에 올릴 수 없는 소재다

```text
줄줄이 삭제당하는 소재
  오줌 · 학교 · 교복 · 빈유 · 강간으로 보이는 것 · 최면 · 약물
→ 이런 LoRA 는 civitai 에 올리는 순간 잘리므로 구글 드라이브 등으로 공유된다
```

**예외** — `personality excretion`(인격배설, 색깔 똥) 계열은 스캇 취급이 아니라서 검열되지 않고 검색된다.

시비타이는 **이유를 알려 주지 않고 업로드를 반려**하기도 하며, WebP 무손실 압축 후 학습·업로드로
우회한 사례가 있다(2025-08).

> **파일에 남은 단서** — civitai 에 올라가지 않은 로라라도 **파일 메타데이터에 학습 태그가 남아 있어**
> 직접 열어 확인할 수 있다. 학습 세팅도 마찬가지다.

### ⚠ '모델은 보이는데 이미지가 안 뜬다' 는 필터 때문이 아니다 (2025-06)

필터 UI 를 잘못 이해해 생기는 착각이 많아 정리된 글이다.

> **필터가 정상적으로 설정돼 있으면 일부러 이미지만 가리는 동작은 없다.**
> 안 보이는 경우는 둘뿐이다 — **모델이 통째로 안 보이거나, 그냥 서버 문제로 이미지가 안 뜨거나.**

- **'감추기' 설정은 체크하면 안 보이게 되는 쪽**이다 (직관과 반대로 읽기 쉬운 부분).
- **태그 기반 감추기보다 '유저 감추기'(히든 유저)가 낫다** — 업로더가 태그를 제대로 달아 준다는 보장이 없고,
  취향이 갈리는 것을 자주 올리는 계정은 거의 정해져 있어 꼬박꼬박 숨기면 잘 걸러진다.

**civitai UI 는 그 뒤로 여러 번 바뀌었으므로 화면 구성은 지금과 다를 수 있고, 원칙(태그보다 유저 차단)만 유효하다고 본다.**


<small>근거 — [웹툰 캐릭터 Lora 공유) 부패의 사제 25.10](https://arca.live/b/aiart/150271493) · [@@@스캇주의@@@ 스캇_IL로라 공유 25.05](https://arca.live/b/aiart/137226294) · [고어, 페도, 스압주의) 고어작가 로라 몇개 (ILXL) 25.05](https://arca.live/b/aiart/136124750) · [Civitai 필터 설정 25.06](https://arca.live/b/aiart/139808399)</small>

## 1-b. ANIMA ↔ Illustrious 짝 모델 목록 — 같은 제작자가 두 계열로 낸 것
<small>2026-05 기준 · 근거 2건</small>

ANIMA 와 Illustrious 를 **한 워크플로우에서 같이 쓰려는 사람**을 위한 대조표다(2026-05).
ANIMA 는 Cosmos-Predict2 기반, Illustrious 는 SDXL 기반이라 계보가 완전히 다른데도
ilxl 스타일을 ANIMA 에서 재현하거나 ANIMA 로 뽑고 ilxl 로 다듬는 조합을 많이 쓴다.

| | ANIMA 용 | Illustrious 용 |
|---|---|---|
| **WAI** | `civitai.red/models/2544636/wai-anima` | `civitai.red/models/827184/wai-illustrious-sdxl` |
| **NTR MIX 4.0** | `civitai.red/models/2393785/ntrmix-or-style` (모델이 아니라 **로라**) | `civitai.com/models/926443` |
| **Yume** | `civitai.red/models/2385278/animayume` | `civitai.red/models/1308285/illumiyume-xl-illustrious` |
| **Ika** | `civitai.red/models/2426265/animaika` | `civitai.red/models/874216/ikastrious` |
| **PornMaster** | `civitai.red/models/2505864/pornmaster-anima-preview` | `civitai.red/models/1033851` |
| **Hakushi Mix** | `civitai.red/models/2515015/hakushi-mix-anima` | `civitai.red/models/1337666` |
| **Liquid VAE** | `civitai.red/models/2487530/qwenimagevaeliquid1087` ← **시비타이에서 현재 유일한 ANIMA 전용 튜닝 VAE** | `civitai.red/models/85106` |
| **SinGlo** (고딕 펑크) | `civitai.red/models/2583535/singlo-anima` | `civitai.red/models/1552304` |
| **Cat** | `civitai.red/models/2383017/anima-cat-tower` | `civitai.red/models/860278` |
| **Cotton** | `civitai.red/models/2382223/cottonanima` | `civitai.red/models/1432671` |

> `WAI` 는 튜닝한 사람 닉네임에서 딴 이름이다.

### ⚠️ 받을 때 두 가지

- **PornMaster ANIMA preview3** 파일은 확장자가 이상해 시비타이에서 `safetensors` 가 아니라 **`other`** 로
  표시되고, 그 때문에 **LoRA 매니저 류 도구의 자동 다운로드가 안 된다.**
- **`Cat` · `Cotton` · `AnimaYume` 은 작가 태그의 존재감이 많이 희석된다.**
  대체로 **튜닝 색이 강한 모델일수록 작가 태그가 잘 안 먹으므로**, 작가 조합으로 그림체를 만드는 사람은
  모델을 고르기 전에 이 점을 먼저 확인해야 한다.

→ 계열 차이는 [모델 고르기](models.md), ANIMA 자체는 [ANIMA](anima.md)


<small>근거 — [개인적인 Anima+IL 워크플로우 세트 구성품 추천 26.05](https://arca.live/b/aiart/169680210) · [첸돚거 그림체 커스텀+기타 개인 설정세팅값 자료 26.06](https://arca.live/b/aiart/174789689)</small>

## 6-h. 용어와 약칭의 함정 — 채널 글을 읽을 때
<small>2026-06 기준 · 근거 4건</small>

같은 글자가 다른 것을 가리켜 생기는 사고가 반복된다.

### `Nai` 는 두 가지다

```text
Nai  =  NovelAI   (웹 서비스)
Nai  =  NoobAI    (로컬 체크포인트)
```

스타일 로라 배포글에 달린 **"Nai 에서도 먹힌다"** 는 댓글은 **NovelAI 가 LoRA 를 지원한다는 말이 아니라**
'NovelAI 에서 그 **작가 태그 자체가** 잘 먹힌다' 는 뜻이었다. **NovelAI 는 LoRA 를 쓸 수 없다.**

### `wai anima` 는 `WAI Illustrious` 와 다른 물건이다

`WAI Illustrious` 는 SDXL 계열이고 `WAI ANIMA` 는 Cosmos-Predict2 기반 ANIMA 다.
**SDXL 용 로라·VAE·워크플로우가 그대로 통하지 않는다.**

### `LoRA Base Model` 과 `Checkpoint Model` 은 다른 것이다

배포글마다 반복해서 못 박는 구분이다 — 앞은 **로라를 만들 때 쓴 바탕**이고, 뒤가 **실제로 그림을 뽑는 모델**이다.

### 2023년 배포글의 두 판 표기

```text
aris-hq / aris-hv   →  hq = 의상 고정형, hv = 미고정형
soz-aoh / soz-nf    →  aoh = 어비스오렌지2하드 학습판, nf = 애니풀 학습판  (배포자는 nf 추천)
```

같은 캐릭터라도 **학습에 쓴 베이스 모델에 따라 결과가 달라져** 배포자가 두 판을 모두 올리던 관행이다.
'의상 고정형 / 미고정형' 은 **캡션에서 의상 태그를 지웠느냐 남겼느냐**의 차이다.

### 한 그림에 두 캐릭터를 각각 다르게 꾸미려면

| 방법 | 언제 |
|---|---|
| **Regional Prompter** (구역마다 다른 프롬프트) | 확실하게 하고 싶을 때 |
| 머리 색·의상만 대충 맞춰 여러 번 뽑아 구도를 **70% 정도** 맞춘 뒤 **인페인트로 나머지 디테일** | 어렵거나 귀찮을 때 |

→ [용어집](glossary.md) · [인페인팅](inpainting.md) · [같은 캐릭터 계속 뽑기](consistency.md)


<small>근거 — [이것저것 만든 LoRA 모음집 공유 23.01](https://arca.live/b/aiart/68474447) · [게임 캐릭터 Lora 공유) 화이트데이: 학교라는 이름의 미… 25.05](https://arca.live/b/aiart/137118271) · [스타일 LoRA) Hechima (issindotai) 스타일 25.11](https://arca.live/b/aiart/153935164) · [첸돚거 그림체 커스텀+기타 개인 설정세팅값 자료 26.06](https://arca.live/b/aiart/174789689)</small>

## 6-f-2. NAI 작가 태그 대조표 — 조건이 통제된 것 (2025-04)
<small>⚠️ 2025-08 기준 · 근거 2건</small>

`NAI Diffusion V4 Full` 에서 잘 먹히는 작가 태그 **30개**를 한 세팅으로 뽑아 비교한 개인 모음집이다.
**값어치는 목록이 아니라 비교 조건이 통제돼 있다는 점에 있다** — 작가 이름만 바꿔 같은 프롬프트·같은 설정으로
뽑았으므로 그대로 재현해 볼 수 있다.

```text
프롬프트 틀
nsfw, artist:"Name", 1girl, year 2024, black hair, black eyes,
cowboy_shot, solo, straight-on, standing, arm at side, simple background

부정 (NAI 가중치 문법)
1.2::worst quality::, 1.2::bad quality::, 1.2::lowres::, 1.2::censored::,
1.2::Imperfect Fingers::, 1.1::Imperfect Fingers::, 1.2::Approximate::,
1.1::very displeasing::, 1.1::mess::, 1::unfinished::, 1::unclear fingertips::,
1::twist::, 1::Squiggly::, 1::Grumpy::, 1::incomplete::, 1::Cheesy::

설정
Add Quality Tags        on
Undesired Content       Heavy
Steps                   28
Prompt Guidance         6
Sampler                 Euler Ancestral
Prompt Guidance Rescale 0.7
Noise Schedule          karras
```

수록 작가 30인 —
`akina 422` · `atdan` · `drunkoak` · `jima` · `kamiya yuu` · `kidmo` · `kkuem` · `kodama (wa-ka-me)` ·
`kouyafu` · `lack` · `lam (ramdayo)` · `mamenomoto` · `meion` · `mika pikazo` · `mikan03 26` · `mmu` ·
`neps` · `nuppehofu (nibuta)` · `onono imoko` · `pottsness` · `qiandaiyiyu` · `sakimichan` · `senano-yu` ·
`sencha (senchat)` · `sheya` · `tokkyu` · `wlop` · `yoggi (stretchmen)` · `yoshito` · `yuuki hagure`

> 댓글에서 반실사풍 작가들도 V4 에서 생각보다 잘 나온다는 평이 있었다.
> `qiandaiyiyu` 는 Illustrious 용 그림체 로라도 있다 — `https://civitai.com/models/1836271/qiandaiyiyu-style-illustrious`
> (데이터셋 만드는 과정이 [로라 쓰는 법](lora-usage.md) 의 "굽기 준비 ②" 에 정리돼 있다).


<small>근거 — [qiandaiyiyu 그림체 로라 배포 25.08](https://arca.live/b/aiart/144192001) · [내가 보려고 만든 작가 모음집 25.04](https://arca.live/b/aiart/134253509)</small>

## 6-i. ⚠ 와일드카드는 복붙이 아니다 — 폴더에 넣어야 `__파일명__` 이 동작한다
<small>2026-06 기준 · 근거 2건</small>

와일드카드 묶음을 받아 놓고 **"안 되는데요"** 하는 사람의 대부분이 여기서 막힌다.
받은 `.txt` 를 **프롬프트 칸에 그대로 복붙하는 것이 아니다.** 와일드카드로 **설치**해야 한다 (77728087, 2023-06 · 지금도 그대로 유효).

### A1111 계열 설치 절차

| 순서 | |
|---|---|
| 1 | **Dynamic Prompts** 확장을 설치한다 |
| 2 | `stable-diffusion-webui\extensions\sd-dynamic-prompts\wildcards` 폴더에 **`.txt` 파일을 넣는다** |
| 3 | webui 상단의 **`Wildcards` 탭에서 새로고침**하면 목록에 뜬다 |
| 4 | 프롬프트에 **`__파일명__`** 형태로 적는다 |

그러면 생성할 때마다 **그 파일의 한 줄이 무작위로 뽑혀** 들어간다.

```text
1girl, solo, __landmark__, masterpiece
        ↑ landmark.txt 의 한 줄이 매번 무작위로 치환된다
```

> ⚠ **폴더째로 풀면 안 된다** — `__폴더명/파일명__` 이 되어 인식되지 않는다. `wildcards` 루트에 **평평하게** 푼다.
> ⚠ 와일드카드 파일 인코딩은 **UTF-8** 이어야 한글이 깨지지 않는다.
> ⚠ `{ A | B | C }` 는 **랜덤이 아니라 순차 사이클**이다 → [ComfyUI 쓰는 법](comfyui.md)

### ComfyUI 쪽

Impact Pack 의 **'와일드카드 처리기(Impact)'** 계열 텍스트 출력형 노드를 쓴다. 순차 출력·폴더 호출 개조는 [ComfyUI 쓰는 법](comfyui.md) 참조.

### 도구 쪽에서도 같은 규칙을 쓴다

Prompt-Classifier 는 **exe(또는 `main.py`)와 같은 위치에 `wildcard` 폴더**를 만들어 `.txt` 를 넣고,
'와일드카드 처리' 를 체크한 뒤 키워드 칸에 **`__이름__`** 으로 적으면 동작한다 (173039358, 2026-06).
그 안의 줄바꿈은 내부에서 `|` 로 자동 치환되고 **중첩도 된다.**

### 실제 배포물 하나 — 배경용 와일드카드

배경 프롬프트를 고민하지 않아도 되도록 만든 모음이다 (77728087). 안에 랜드마크 목록이 두 개 들어 있는데 차이가 있다.

| | |
|---|---|
| 랜드마크 1 | **나라 이름이 전부 들어 있다** |
| 랜드마크 2 | 나라가 있는 것도 없는 것도 섞여 있지만 **양이 훨씬 많다** |

제작자도 전부 잘 나오는지는 모르며 안 나오는 항목은 노이즈용으로 써도 될지 모른다고 솔직히 밝혔다. 예시 이미지의 체크포인트는 댓글에서 `yabalMixV3` 로 확인됐다(2023년 자료).

→ 위 '6. 와일드카드 · 태그 · 작가 데이터' · [프롬프트 쓰는 법](prompting.md)

<small>근거 — [배경용 와일드카드 모음 23.06](https://arca.live/b/aiart/77728087) · [프롬프트 분류기 와일드카드 지원 및 이스케이프 처리개선 26.06](https://arca.live/b/aiart/173039358)</small>

## 4-c. 포즈 자료를 쓸 때 — 전처리기와 가중치를 자세 난이도에 맞춘다
<small>⚠️ 2025-04 기준 · 근거 3건</small>

공유된 포즈 이미지를 ControlNet 에 넣을 때 **어떤 전처리기를 어떤 가중치로 쓰느냐**가 결과를 가른다.
포즈마다 실험해 적어 둔 기록이 있다 (71112036, 2023-03, 검증 모델 AOM3 a3 / 기준 해상도 768x512).

| 자세 | 전처리기 / 가중치 | 비고 |
|---|---|---|
| **쉬운 자세** | `openpose` / **weight 1** | 금방 나온다 |
| **선명한 윤곽** | `canny` / **weight 1** | |
| **손발이 복잡한 포즈** | `canny` / **weight 1~1.5** | 그래도 양발이 깔끔한 것을 찾기가 더 힘들고, **위로 뻗은 팔이 다리가 되기도** 한다 |
| **관절이 꼬인 어려운 자세** | **`normal map` / weight 1** | 같은 그림을 `canny`·`openpose` 로 시도하면 **자세가 어려워 잘 못 읽는다** |

**일반화하면** — 관절이 꼬인 어려운 자세일수록 `openpose` 보다 `normal map` 이나 `canny` 가 유리하고, **가중치는 모델과 그림에 맞춰 능동적으로 조절해야 한다.**
이는 "오픈포즈는 사람 사진에서 포즈를 추출하려고 만든 것이라 그림에서는 타율이 낮다" 는 일반론과 같은 방향이다 → [컨트롤넷](controlnet.md)

### 두 전처리기를 함께 쓰기

**전체 포즈는 오픈포즈로 잡고, 오픈포즈가 잘 못 잡는 손 부분만 캐니용 참조 이미지로 따로 보정**하는 조합이 쓰인다 (72773785, 2023-03).
다만 그렇게 해도 **포즈가 이상하게 나오는 경우가 있다**고 작성자가 솔직히 밝혔고, 공유된 캐니용 사진은 인페인트에서 위치를 맞춘 것이라 **쓰는 사람이 손 위치를 적절히 수정**해야 한다.

### 배경만 바꾸고 싶을 때

| 전처리기 | 방법 |
|---|---|
| `canny` · `openpose` | **프롬프트만** 바꾸면 된다 |
| `normal` | **그림판에서 캐릭터 주변만 남기고 지운 뒤** 배경 프롬을 추가한다 |

### 포즈만 받아 쓰는 형태도 있다

워크플로 JSON 없이 **포즈 이미지만 공유되는 경우**도 많다 (135095099, 2025-04).
그럴 때는 그 이미지를 ControlNet 에 넣고, **자세에 어울리는 보조 프롬프트**(예: `sitting, lifting skirt, cellphone`)를 함께 넣으면 타율이 올라간다.
남이 공유한 뼈대 이미지를 직접 넣을 때는 `Preprocessor: none` + `Model: openpose` 로 맞춰야 한다 → [컨트롤넷](controlnet.md)

> ⚠ 2023년 구글 드라이브 링크가 대부분이라 **파일 자체는 만료됐을 가능성이 높다.** 남는 것은 위의 전처리기·가중치 판단 기준이다.

<small>근거 — [요가 자세 포즈 몇 개 만든거 공유 (컨트롤넷) 23.03](https://arca.live/b/aiart/71112036) · [오픈 포즈 공유 25.04](https://arca.live/b/aiart/135095099) · [독학한 컨트롤넷 그림(+ 포즈 공유) 23.03](https://arca.live/b/aiart/72773785)</small>

## 3-g. 2023년 SD1.5 시절 로라·모델 — 지금 무엇이 남았나
<small>⚠️ 2023-06 기준 · 근거 12건</small>

채널 초창기(2023년) 배포글이 아직 검색에 잔뜩 걸린다. **먼저 알아야 할 것은 이것이다.**

> **2023년 SD1.5 시절에 배포된 LoRA·병합 모델은 현행 Illustrious / Pony / SDXL 계열 체크포인트와 호환되지 않는다.**
> 실사용 가치는 거의 없고 **옛 모델 계보를 확인할 때만** 쓸모가 있다.

### 그래도 남는 것 — 이 시절 글에서 건질 것들

| 무엇 | 어디서 |
|---|---|
| **허깅페이스 SD1.5 로라 저장소 목록** — 주제별 20여 곳. 저장소 자체는 대부분 살아 있다 | 68188770 (2023-01) |
| **국내 병합 모델 계보** — CamelliaMix / ExpMix / ZemiHR / NabiMix 계열 전체 목록 | 72189422 (2023-03) |
| **모델 비교 이미지 모음** — 채널 위키 등재 모델을 같은 프롬프트('설화')로 전부 뽑은 것 | 72707563 (2023-03) |
| **로라 학습 데이터셋과 태그 파일의 실물** — 배포 폴더의 `test` 폴더에 작성자가 직접 수정한 학습용 그림 + 태그가 들어 있다. **드문 공개 사례다** | 71116117 (2023-03) |

### 이 시절 로라를 실제로 돌려야 한다면

| 함정 | |
|---|---|
| **트리거 워드가 없는 경우가 많다** | 정규화 이미지에 태그를 잔뜩 넣어 학습한 경우가 많아, **샘플에 붙은 긴 태그 나열을 전부 적어 줘야** 제대로 나온다(작성자 본인 인정, 70704280) |
| 로라가 화투패에 안 보인다 | 로라 폴더에 넣은 뒤 **탭에서 `refresh`** 를 누른다 |
| 한 로라에 복장이 여러 개 | **복장 수가 늘수록 각 복장의 구현도가 떨어진다** (70704280) |
| 재현 정보가 없다 | 트리거·권장 가중치·학습 파라미터(epoch, repeat, learning rate, dim)를 안 적은 배포글이 많다. **그 수치만 풀어도 참고가 크게 된다**는 지적이 당시에도 반복해서 나왔다 |

### 구체적인 사용값이 남아 있는 것들

| 로라 | 값 |
|---|---|
| **개량한복 `FusionHanbok`** (75964340) | 가중치 **0.6~0.8**(1.0 은 모델에 따라 색이 바랜다). 배포 파일 1~15번 중 **1~3 라이트 / 10+ 헤비하지만 뭉개짐 → 5~10 중간대**. 색이 흑백으로만 고정되면 **LoRA Block Weight**. 짧은 스커트는 `thighs:1.3` 또는 `thigh gap:1.2` |
| **한복 LoRA** (69440453) | 학습 베이스 **Counterfeit V2.5**, 가중치 **0.8**. v1 은 오버피팅이라 v2 를 다시 학습시켰다. 약점 — **저고리 옷고름이 잘 안 나온다**(그 부분만 가중치를 높여 inpaint) |
| **미라화·거미줄** (70195871) | 강도 **0.6~0.7**(초과하면 의도와 다른 결과). **업스케일하면 자주 뭉개져** 640x640 → 1000x1000 정도가 안전. 7th anime 모델에서만 검증 |
| **무직전생 아이샤** (77356160) | `aisha-04.safetensors` weight **0.8** + **무직전생 걸팩 로라를 weight 0.4 로 반드시 병용**. 보조 로라 `add_detail 0.8` / `_L2090 0.3` / `add_saturation 1.5` / **`add_brightness -2`** |

> **음수 가중치** — `add_brightness` 에 `-2` 를 준 것처럼 **LoRA 가중치에 음수를 넣으면 학습된 효과가 역방향으로 작동한다.** 이것은 지금도 그대로 쓰인다 → [로라 쓰는 법](lora-usage.md)

### 의상 로라를 만들 거라면 (지금도 유효한 요령)

> **학습 이미지의 모델이 한 사람뿐이면 그 사람 얼굴까지 함께 학습되므로 눈 아래쪽으로 잘라 준다.**
> 의상 로라가 캐릭터 로라가 되는 사고를 막는다 (75964340 댓글).

### 링크

**대부분 죽었다고 보는 편이 맞다.** 특히 아래는 확인된 것이다.

| 무엇 | 상태 |
|---|---|
| **'일주일동안 만든 로라 결산'(70704280)의 구글 드라이브 30여 개** | 🔴 **파일 자체가 없다.** 재업 요청에 작성자가 *"옛날 SD 1.5 시절 구닥다리여서 삭제했고 컴터도 바꿔서 소실돼버렸습니다"* 라고 댓글에서 답했다 |
| 구드 공유 모델 전반 | **다운로드 용량 초과 오류**가 잦다. 댓글의 우회법이나 제3자 허깅페이스 미러를 찾는다(예: CamelliaMix `https://huggingface.co/Powidl43/CamelliaMix/tree/main`) |
| 하이퍼링크만 걸린 배포글 | 본문에 URL 텍스트가 남아 있지 않아 **복원 불가** |

> 병합 모델 공유글은 **설정값을 본문에 적는 대신 레퍼런스 이미지(설화)의 EXIF 에 담아** 배포하는 관행이 있었다. 이미지를 받아 EXIF 를 열면 프롬프트·시드·샘플러가 통째로 나온다.

→ 위 '8. 링크 죽음 목록' · '0. 먼저 알아 둘 것'

### 자세·상황 하나에 LoRA 하나 — 2023년식 구성의 표본 (2023-05)

캐릭터 대회 출품작 하나가 쓴 자원을 통째로 공개했는데, **그 목록 자체가 시대 차이를 보여 준다.**

| 자리 | 무엇 |
|---|---|
| 병합 모델 | `https://huggingface.co/GIMG/AIChan_Model/blob/main/Blend/MIX-MIX.safetensors` — 대회용으로 적당히 병합한 것이고 '좀 두껍게 나온다' 는 것 외에 특별한 건 없다고 했다 |
| 프롬프트 전문 | `https://huggingface.co/GIMG/AIChan_Model/blob/main/prompt/mirko/prompt.txt` (메모장 첨부) |
| 기본 LoRA (전 그림 공통) | 캐릭터 LoRA `civitai.com/models/33149` + 체형 컨셉 `civitai.com/models/44785` (Venus Body) |
| **장면마다 갈아 끼운 LoRA** | On Fire(54524) · 역번역 바니슈트(8682) · 차이나 드레스(56029) · **implied fellatio(7203)** · **ahegao rolling eyes(55551)** · Murky's pronebone(17741) · after sex lying(18194) · public toilet girl(52414) · dogeza(14905) · Jack-o' challenge pose(10353) · kitchen apron naked(65090) |

> **지금의 Illustrious/NoobAI 계열은 이 자세·상황들을 대체로 태그만으로 처리한다.**
> `implied fellatio` · `ahegao` 는 LoRA 가 아니라 **단부루 태그로 존재한다**
> → [프롬프트 쓰는 법](prompting.md). 2023년 자료에서 'LoRA 로 해결' 이라고 적힌 것을 볼 때 먼저 태그를 찾아본다.

**링크는 3년 이상 지난 것이라 civitai 항목은 삭제됐을 가능성이 있고**, 첨부 프롬프트 파일도 저장소가 유지돼야 열린다.
댓글에서 *'디테일러 같은 걸 쓴 것이냐'* 는 질문에 작성자는 *'그딴 거 없다, 너무 어렵다'* 고 답해,
**이 결과가 순수 모델+LoRA 조합이었음**을 확인했다.


<small>근거 — [모델모음 공유링크(카멜리아, Exp 등) 23.03](https://arca.live/b/aiart/72189422) · [일주일동안 만든 로라 결산 (모음집 업데이트) 23.02](https://arca.live/b/aiart/70704280) · [일단 허깅 돌면서 적당히 쓸만해보이는 lora들 주워옴 23.01](https://arca.live/b/aiart/68188770) · [개량한복 로라 23.05](https://arca.live/b/aiart/75964340)</small>

??? note "근거 12건 전부 보기"
    [모델모음 공유링크(카멜리아, Exp 등) 23.03](https://arca.live/b/aiart/72189422) · [일주일동안 만든 로라 결산 (모음집 업데이트) 23.02](https://arca.live/b/aiart/70704280) · [일단 허깅 돌면서 적당히 쓸만해보이는 lora들 주워옴 23.01](https://arca.live/b/aiart/68188770) · [개량한복 로라 23.05](https://arca.live/b/aiart/75964340) · [아 한복 로라 누가 공유해줬네 23.02](https://arca.live/b/aiart/69440453) · [hiro 스타일(아케비의 세일러복 작가) LORA 공유 23.03](https://arca.live/b/aiart/71891910) · [설화 모음집 만들어옴 23.03](https://arca.live/b/aiart/72707563) · [(미르코)(38장)강력한 미르미르코 23.05](https://arca.live/b/aiart/76765824) · [미라화,거미줄 lora 입니다 23.02](https://arca.live/b/aiart/70195871) · [무직전생 아이샤 그레이렛 LoRA 23.05](https://arca.live/b/aiart/77356160) · [동방프로젝트 첸,오린,쇼,미케 LoRA 모델 23.03](https://arca.live/b/aiart/71116117) · [(사지절단 주의) Mi-Ke 로라 23.03](https://arca.live/b/aiart/71028103)

## 7-b. ComfyUI 워크플로우 공모전(2025-07) 수상작 — 검증된 출발점
<small>⚠️ 2025-07 기준 · 근거 2건</small>

직접 짜기 전에 **검증된 워크플로우를 받아 쓰는 것**이 채널의 방법론인데, 그 후보 목록으로 가장 쓸모 있는 것이 공모전 결과다 (143116458, 2025-07).

| 상 | 작품 | 심사평 |
|---|---|---|
| **최우수상** | 고라니카 **'올인원 워크플로우'** `https://arca.live/b/aiart/140108163` | 이번 대회 최고 출품작. **명료성·확장성·사용 난이도를 모두 충족**하며 ComfyUI 에서 일반적으로 쓰는 모든 기능을 담고 있어 **각 기능에 처음 입문하는 사람이 참고하고 공부하기에 부족함이 없다** |
| **최우수상** | GAVN **'라면보다 쉽다! 간편 종합 워크플로우'** `https://arca.live/b/aiart/141991828` | T2I 워크플로우를 **리저널 프롬프트까지 포함해 압축적이고 강력하게** 구성. **"누가 짜준 워크플로우 하나만 편하게 쓰고 싶다"** 는 사람에게 추천 |
| **우수상** | bedovyy **'겁나빠른 투닥뽑'** `https://arca.live/b/aiart/140754696` | 쉽고 간단하고 빠르다. **그림체·로라 테스트용**이나 한 번에 많은 양을 빠르게 뽑아 선별할 때 좋고, 와일드카드와 **TIPO** 를 공부해 파생 워크플로우를 만들기에도 적합 |

수상하지 않은 참가자에게도 참가비 1만원씩 지급됐다.
**출품작 전체 모음 Kiosk 링크는 기한이 1달이라 이미 만료됐을 가능성이 높다** — 개별 출품작 글은 채널 **[대회] 탭**에 남아 있다.

### 심사 기준 자체가 '좋은 워크플로우' 의 정의다

받아 쓸 워크플로우를 고를 때 그대로 체크리스트로 쓸 수 있다.

| | |
|---|---|
| 1 | **Pony 계열보다 ILXL(Illustrious XL) 계열에 최적화** |
| 2 | **왼쪽에서 오른쪽 또는 위에서 아래로 흐르는 순방향 구성** |
| 3 | 모델·설정 변경과 기능 추가가 쉬운 **범용성** |
| 4 | **낮은 사용 난이도** |
| 5 | 업스케일링 모델·bbox·segm **배포처 링크 첨부** |

→ [ComfyUI 쓰는 법](comfyui.md) 의 '배포 워크플로우를 처음 열었을 때'

<small>근거 — [ComfyUI 워크플로우 공모전 마무리 및 수상자 발표 25.07](https://arca.live/b/aiart/143116458) · [(워크플로우 공모전) 라면보다 쉽다! 간편 종합 워크플로우 … 25.07](https://arca.live/b/aiart/141991828)</small>

## ANIMA 로라 — 받기 전에 대상 판을 확인하라
<small>2026-07 기준 · 근거 11건</small>

**ANIMA 로라는 받기 전에 어느 판으로 학습했는지 확인해야 한다.** 판이 다르면 노이즈가 끼거나 결과가 지저분해진다.
판별 계보와 재학습 커트라인은 [ANIMA](anima.md) 의 "판이 바뀌면 뒤집히는 것" 에 정리돼 있다.

### 판이 확인된 것들

| 로라 | 대상 판 | 상태·비고 |
|---|---|---|
| `age control 年齢操作 - anima_v1.0` | **PREVIEW** | ⚠️ **정출(BASE)에서 노이즈.** 제작자가 업데이트 방치. Civitai 성인 분리 이슈로 페이지가 안 보이던 시기도 있었다 |
| **`Age Slider LoRA \| ANIMA - v0.9`** | **정출(BASE) 대응** | 위의 대체품. 트리거 없이 강도 `-3.00 ~ 3.00`. 음수(어린) 쪽은 세밀하지만 **양수(고령) 쪽은 얼굴 외 체형이 잘 안 따라온다** |
| `Anima Detail Tweaker - preview3-test` | **PREVIEW3** | 트리거 없이 강도 `-1.0 ~ 1.0` 으로 Aesthetics 조정. highres 를 뭉갠다는 별도 보고가 있다 |
| `@mx2jstyle` · `@7peachstyle` (블아 공식 원화가) | **PREVIEW3** | `civitai.com/models/2542289` · `/2542240` |
| `@a11iss` (`anima-style-a11iss`) | **BASE v1.0** | `civitai.red/models/2623147`. ⚠️ **동공이 별·십자·하트 모양으로 튄다.** 공식 RL 로라 + Highres 로라 병용 권장, 가중치는 배포 이미지 EXIF |
| `@BlueArchStyle` · `@Nikkestyle` | **BASE v1.0** | `civitai.red/models/2530730` · `/2534308`. **작가 태그 없이 트리거만으로** 그림체가 나온다 |
| `@custom1231` · 병합 그림체 로라들 (2026-07) | **aesthetic v1.1** | 아래 "공통으로 밟는 것" 참조 |
| `AnimaYume V02` 전용 (`ricostyle`) | **AnimaYume 파인튜닝 구판** | 🔴 **링크 죽음** (구글드라이브 한시 공유 종료) |
| '브더2 느낌' 그림체 (2026-03) | **PREVIEW2** · 학습 해상도 1536 | 🔴 **링크 죽음** (kio.ac, 2026-03-21 만료) |
| '브더 느낌' `nineng8` (2026-07) | **BASE v1.0** · 학습 해상도 2048 | 🔴 **공개 직후 닫힌 것으로 보인다** |
| `damada21/anima-tlora` (T-LoRA 실험) | **PREVIEW2** | 실험용 |

> **base64 로 가린 링크**와 **kio.ac · mega · 구글 드라이브 한시 공유**가 많다.
> base64 는 저작권 시비를 피하려는 챈의 관행이고, 임시 공유는 **며칠 만에 닫히는 경우가 흔하다.**
> 위 🔴 셋은 만료가 확인된 것이다. 0번 항목 "base64 링크와 기한 만료" 를 함께 볼 것.

### 자유 라이선스

**WTFPL v2** 로 배포된 Anima 그림체 로라가 있다 — 무단 재배포·수정·병합이 전부 자유다.
Civitai 배포본이 재배포·병합 조건을 거는 경우가 많은 것과 대비되므로, 병합해서 다시 배포할 재료로 쓸 수 있다.
반대로 '재배포 금지·개인 사용만' 을 명시한 배포도 많으니 병합 전에 확인할 것.

*(2026-03 ~ 2026-07)*

<small>근거 — [아니마 B1.0 그림체 로라 만든거 2개 공유 26.05](https://arca.live/b/aiart/170817757) · [아니마 디테일 트위커 로라 나왔음. 26.05](https://arca.live/b/aiart/170584706) · [브더느낌의 아니마 로라 26.07](https://arca.live/b/aiart/178293143) · [블아 작가로라 2개 26.04](https://arca.live/b/aiart/167677263)</small>

??? note "근거 11건 전부 보기"
    [아니마 B1.0 그림체 로라 만든거 2개 공유 26.05](https://arca.live/b/aiart/170817757) · [아니마 디테일 트위커 로라 나왔음. 26.05](https://arca.live/b/aiart/170584706) · [브더느낌의 아니마 로라 26.07](https://arca.live/b/aiart/178293143) · [블아 작가로라 2개 26.04](https://arca.live/b/aiart/167677263) · [브더2 느낌의 amima 로라 26.03](https://arca.live/b/aiart/165231841) · [나만 쓰던 그림체 로라 공유함 26.07](https://arca.live/b/aiart/175489941) · [ANIMA 로라: alllisso 그림체 26.05](https://arca.live/b/aiart/170685979) · [허접한 AnimaYumeV02 용 LoRA 공유함 26.03](https://arca.live/b/aiart/164800666) · [(anima, 페, 할) 연령 조절 슬라이더 로라 26.06](https://arca.live/b/aiart/174677230) · [채신기법으로 anima lora 학습시켜봄 (2) 26.03](https://arca.live/b/aiart/165954535) · [아니마 연령 조절 로라 26.05](https://arca.live/b/aiart/170858259)

## ANIMA 그림체·캐릭터 로라를 쓸 때 되풀이되는 것
<small>2026-07 기준 · 근거 13건</small>

Anima 그림체·캐릭터 로라를 받아 쓸 때 **여러 배포글에서 반복해 나오는** 것들이다.

### 트리거 워드

| 유형 | 동작 |
|---|---|
| 트리거 없음 | 강도만으로 동작. 대신 **데이터셋 편향이 그대로 나온다**(아래) |
| `@` + 무의미 4자 코드 | NAI 작가 그림체 계열의 관례 — `fr8r`=freng, `fr9t`=fymrie, `qr4k`=quasarcake. **배포자는 병합판보다 개별 로라를 권한다** |
| 작가 태그와 같은 이름 | ⚠️ **이중 적용을 피해 작가 태그 가중치를 낮춘다.** 실사용 예: `novaAnima + @buzzlyears 0.4 + 작가 로라 1.0 + 터보 로라 1.0` |
| 있어도 효과가 미미한 것 | 학습 중 딸려 들어간 `@a6uj` 같은 코드는 음영이 조금 강해지는 정도였다고 제작자가 밝혔다 |

트리거가 없어도 동작하지만 **넣으면 가중치가 붙는 것처럼 효과가 강해진다**는 보고가 있고,
이때 작가 태그는 따로 쓰지 않아도 그림체가 나온다.

### ⚠️ 데이터셋 편향은 프롬프트 없이 그대로 나온다 (3건)

> 학습 데이터가 흰 고양이 캐릭터 위주였던 판은 **깡으로 돌리면 비슷한 헤어스타일만 계속 나온다.**
> 다른 판도 *"프롬프트 없이 그냥 돌리면 거의 일관된 색과 헤어가 나온다"* 고 제작자가 명시했다.

**해결은 간단하다 — 색·헤어를 프롬프트로 지정하면 잘 따라온다.** 소규모 데이터셋 스타일 로라의 일반 성질로 알아 둘 것.

### 눈이 작게 나오면 뭉개진다 (melowh 계열 3건)

`wide shot` 처럼 멀리서 보거나 반눈을 뜬 상태에서 **눈 디테일이 깨진다.**
눈 디테일이 좋은 작가(Ramanda)를 하나 더 섞은 개선판에서도 **이 증상은 고치지 못했다.**
디테일러나 인페인팅으로 따로 손봐야 한다 → [디테일러](detailer.md) · [인페인팅](inpainting.md)

### 캐릭터 태그 하나로 끝내지 마라

`kisaki_(swimsuit)_(blue_archive)` 만으로는 캐릭터는 나오지만 **특유의 헤어스타일이 잘 안 나온다.**
외형을 전부 묘사하는 편이 타율이 높다 —
`grey eyes, black hair, long hair, braid over shoulder, small breasts, grey halo`.

### 그밖에 되풀이되는 것

| 증상 | 대처 |
|---|---|
| 웹툰 색감이 안 살아난다 | **`(flat color:0.8)`** — Anima 는 기본적으로 음영과 광택을 넣는 경향이 있다 |
| 옅은 점박이('비듬') 무늬 | **로라 탓이 아니다.** 고해상도·업스케일에서 나오는 XL 시절부터의 AI 고질병이고, **완성도가 높은 로라일수록 오히려 심하다**는 지적 |
| 세부 묘사가 안 나온다 | 가중치를 `2` 정도로 세게 준다 (`(long labia:2)`) → [ANIMA](anima.md) |
| `[Errno2] No such file or directory: mixed` | **LoraManager 웹 UI(`http://127.0.0.1:38188/loras`)** 에서 상단 시계 아이콘으로 새로고침 |
| `AnimaSafePAG`·`ResShiftLoader`·`ResShiftUpscale` 누락 | **ComfyUI 매니저에 없는 챈산 노드**라 챈에서 검색해 받아야 한다 |
| Illustrious 용 로라를 얹었는데 안 먹는다 | **Anima 는 SDXL 계열 로라 비호환.** 새로 구워야 한다. 같은 Civitai 페이지 안에 IL 판과 ANIMA 판이 함께 있는 경우가 많으니 버전을 골라 받을 것 |
| NAI 에서 쓰고 싶다 | **불가능.** NAI 는 외부 로라를 지원하지 않는다 → [NovelAI](nai.md) |

### 여러 로라를 하나로 합치기

각각 로드하는 대신 **비율을 정해 병합**해 쓰는 방식이 쓰인다 —
커스텀 로라 `1` : melowh `0.4` : 리얼스킨 `0.2` 를 챈의 '고효율 파이프라인' 병합 기능으로 통합한 사례.
NAI 풍을 낼 때는 작가 태그를 **계단식**으로 배분하는 검증된 조합이 있다 —
`(@brws:1.5), (@quasarcake:1.5), (@lowlight kirilenko:1.4), (@pottsness:1.3), (@yoneyama mai:1.2), (@say hana:1.1)`.

*(2026-05 ~ 2026-07)*

<small>근거 — [아니마 B1.0 그림체 로라 만든거 2개 공유 26.05](https://arca.live/b/aiart/170817757) · [마참내 병합성공한 그림체 로라 공유 26.07](https://arca.live/b/aiart/177903059) · [아니마용 그림체 로라 개선판 공유 26.07](https://arca.live/b/aiart/178144808) · [아니마 그림체 로라 공유 26.07](https://arca.live/b/aiart/177882714)</small>

??? note "근거 13건 전부 보기"
    [아니마 B1.0 그림체 로라 만든거 2개 공유 26.05](https://arca.live/b/aiart/170817757) · [마참내 병합성공한 그림체 로라 공유 26.07](https://arca.live/b/aiart/177903059) · [아니마용 그림체 로라 개선판 공유 26.07](https://arca.live/b/aiart/178144808) · [아니마 그림체 로라 공유 26.07](https://arca.live/b/aiart/177882714) · [스압)아니마 커스텀 믹스 로라 공유 26.07](https://arca.live/b/aiart/176513464) · [로리캐 로라 만든다고 시빗 밴먹은 기념 모델 덤프트럭 25.09](https://arca.live/b/aiart/149271136) · [아니마로 NAI 그림체 만들어본거 공유 26.06](https://arca.live/b/aiart/173054724) · [NAI풍 아니마 로라 공유 26.05](https://arca.live/b/aiart/171228963) · [ANIMA LoRA: NAI 스타일 콜렉션 1편 26.05](https://arca.live/b/aiart/170929440) · [아니마 그림체 로라 공유 26.07](https://arca.live/b/aiart/178524790) · [웹툰,페) 수희0 - 조수정 아니마 로라 26.07](https://arca.live/b/aiart/177767092) · [ANIMA 농농한 그림체 스타일 로라 26.05](https://arca.live/b/aiart/171208757) · [ANIMA) 수영복 키사키 (수사키, 수키키) 로라 26.06](https://arca.live/b/aiart/175182246)

## ANIMA 자동완성 CSV · 그림체 사이트 · 파인튜닝 체크포인트
<small>2026-08 기준 · 근거 8건</small>

### 작가 태그 자동완성 CSV — 일반 단부루 CSV 는 `@` 가 없다

Anima 는 작가 태그 앞에 **`@`** 가 있어야 인식하는데 일반 단부루 자동완성 CSV 에는 `@` 가 없어서
**자동완성으로 넣으면 작가 태그가 그냥 안 먹는다.** 두 가지 길이 있다.

| 방법 | |
|---|---|
| **Anima 전용 CSV** | `huggingface.co/arcacolab/foranima` 의 `for_anima_danbooru_2025-09-01_pt20-ia-dd.csv` — 원본(`github.com/DraconicDragon/dbr-e621-lists-archive`)에서 작가 태그 앞에 `@` 를 붙인 판. **태그 기준일은 `2025-09-01`** 이라 그 뒤의 새 캐릭터·작가는 없다. chibi 프론트엔드에서 쓰려면 파일명을 `danbooru_241106_compact` 로 바꿔야 인식한다 |
| **노드 설정** | `ComfyUI-Autocomplete-Plus` 에 **artist prefix** 기능이 있다. 작가 태그 앞에 붙을 문구(Anima 라면 `@`)를 지정해 두면 **CSV 를 고칠 필요 없이** 자동으로 붙는다 |

### 작가 그림체를 눈으로 고르기

**`anima.mooshieblob.com`** — 작가당 예시 이미지 2장, 즐겨찾기와 랜덤 추천.
가치의 핵심은 **예시가 Anima BASE 모델로 직접 뽑은 것**이라 실제 출력과 가깝다는 점이고,
각 예시의 프롬프트와 설정값도 공개돼 있어 그대로 따라 쓸 수 있다.

> ⚠️ **이 계통 사이트는 언제든 사라진다.** 예전에 쓰이던 다른 그림체 사이트는 **운영자의 GitHub 계정이 정지**되면서 닫혔다.
> 자주 쓰는 작가 조합은 **로컬에 따로 메모해 두는 편이 좋다.**

### BASE 정출 이후의 파인튜닝 체크포인트

`DaSiWa - Anima - Luminous Labyrinth v1`(WAN/LTX 파인튜닝으로 알려진 DarkSideWalker 작) ·
`Animaika` · `Cat Tower` · `Cotton` · `Anzhc/AAAAnima` · `novaAnimeAM` · `WAI-ANIMA`.

**`AAAAnima`** 는 25 에폭 · 데이터셋 120k 이고, 이전 판이 태그만으로 캡션을 달던 것을 **자연어 태깅으로 바꾼 것**이 가장 큰 변화다
(Anima 는 Qwen3 인코더를 써서 자연어 이해가 강점이므로 태그만 학습한 파인튜닝은 그 강점을 깎아먹을 수 있다).

> ⚠️ **파인튜닝 Anima 를 고를 때 확인할 것은 '지식 망각' 이다.** AAAAnima 이전 판은 베이스보다 살짝 미묘했고
> 원래 알던 캐릭터·개념을 일부 잊었다. 파인튜닝판은 **순정 BASE 와 권장 값도 갈린다**
> (예: `anima-highresaesthetic-boost` 는 파인튜닝이면 0.7, 순정 BASE 면 0.2~0.5).
> 이 주제 전반은 [ANIMA](anima.md) 의 "병합·파인튜닝의 한계" 절에 있다.

*(2026-02 ~ 2026-08)*

<small>근거 — [Anima 웹툰 캐릭터 Lora 공유) 역대급 영지 설계사 26.05](https://arca.live/b/aiart/172324042) · [Anima 웹툰 캐릭터 Lora 공유) 나 혼자 특성빨로 무… 26.05](https://arca.live/b/aiart/171699762) · [ANIMA 아니마용 단부루 자동완성 csv 26.02](https://arca.live/b/aiart/161315560) · [Anzhc/AAAAnima not so early 26.07](https://arca.live/b/aiart/176018707)</small>

??? note "근거 8건 전부 보기"
    [Anima 웹툰 캐릭터 Lora 공유) 역대급 영지 설계사 26.05](https://arca.live/b/aiart/172324042) · [Anima 웹툰 캐릭터 Lora 공유) 나 혼자 특성빨로 무… 26.05](https://arca.live/b/aiart/171699762) · [ANIMA 아니마용 단부루 자동완성 csv 26.02](https://arca.live/b/aiart/161315560) · [Anzhc/AAAAnima not so early 26.07](https://arca.live/b/aiart/176018707) · [아니마 그림체 사이트 26.08](https://arca.live/b/aiart/179093581) · [anima 파인튜닝해본 모델 26.05](https://arca.live/b/aiart/170997672) · [Anima-INT8Rowwise 모델 26.02](https://arca.live/b/aiart/163367034) · [DaSiWa - Anima 26.05](https://arca.live/b/aiart/170910843)

## 6-f-3. 작가명 썸네일 뷰어 — 이름 옆 숫자가 곧 태그가 먹힐 확률이다
<small>2026-02 기준 · 근거 2건</small>

작가명 태그를 넣었을 때 **어떤 그림체가 나오는지 썸네일로 미리 훑어보는** 독립 실행 뷰어다 (1건, 2025-06).
NAIA 의 작가명 미리보기 기능만 떼어내 만들었다.

```text
https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/artist_thumbnail%20%EB%B7%B0%EC%96%B4.exe
```

exe 직접 다운로드라 브라우저에서 '더보기 → 유지 → 그래도 계속' 을 눌러야 받아진다.
실행 후 상단의 **'썸네일 파일 불러오기'** 로 목적에 맞는 데이터 파일을 따로 불러와야 동작한다.

### ⚠ 데이터 파일이 모델 계열별로 나뉘어 있다

| 데이터 파일 | 대상 |
|---|---|
| NAI v4.5 상위 22,000명 / 상위 31,000명 | NAI V4.5 |
| NAI v4 상위 55,000명 | NAI V4 |
| Noob v-pred 상위 19,000명(6/14) / 33,000명(6/18) | NoobAI v-pred |

**같은 작가 태그라도 모델 계열마다 재현 결과가 다르므로 자기가 쓰는 모델에 맞는 파일을 받아야 한다.**
NAI v4 용 파일은 용량이 커서 다운로드가 htm 으로 깨져 받아지는 문제가 있었고, download 텍스트를 우클릭해 '다른 이름으로 링크 저장' 하면 된다.

### 이름 옆의 숫자 = Danbooru 포스트 카운트

> **작가 이름 옆에 붙는 숫자는 Danbooru 포스트 카운트**로, 그 작가가 학습됐을 것으로 추정되는 이미지 수량이다.
> 곧 **그 작가 태그가 먹힐 확률의 지표**로 쓰면 된다.

이 지표와 짝이 되는 실측이 있다 — NoobAI v-pred 작가 재현 특화 모델에서 **재현 가능한 범위는 단부루 작품 수 70건 정도까지**였다
(→ [모델 고르기](models.md)). NAI 쪽에서도 **레퍼런스가 적은 작가는 태그로 부르지 말고 LoRA 를 쓰라**는 같은 결론이 나온다.

### 그림체를 격자로 비교할 때 — 캐릭터 프롬을 빼라

NAI 작가 조합을 격자로 대량 비교하는 **단일 HTML 페이지**도 공유돼 있다 (1건, 2026-02).
NovelAI API 키를 넣고 art style 칸에 **작가 이름만** 넣으면 도구가 `artist:` 양식을 알아서 씌우며, 가중치를 0.1~2.5 슬라이더로 조절한다.
import 는 `1.7::artist:name1, artist:name2::, 1.1::artist:name3::` 형식을 파싱하지만
**`arist`/`atrist` 같은 오타나 쉼표 누락이 있으면 양식이 엉키므로** 검수해서 넣어야 한다.

> ⚠️ **댓글의 중요한 정정 — 그림체를 테스트할 때는 캐릭터 프롬을 반드시 빼야 한다.**
> **캐릭터 스타일이 그림체까지 변형시키기 때문**이며, 작성자도 *"어쩐지 살짝씩 삐꾸나더라니"* 라며 수긍했다.

로컬 HTML 이라 CORS 때문에 이미지 요청 외의 API 기능이 막혀 **잔여 Anlas 확인이 안 되므로**,
조금씩 돌려 보며 NovelAI 페이지에서 소모를 직접 확인해야 한다.
⚠️ 배포가 **mega 링크**라 만료 가능성이 있다 → 아래 「8. 링크 죽음 목록」.

<small>근거 — [작가명 태그 썸네일 미리보기 뷰어 (30mb) 25.06](https://arca.live/b/aiart/139028012) · [nai 그림체 테스트하는 페이지 공유 26.02](https://arca.live/b/aiart/161192747)</small>

## 6-e-2. NAI `{}`·`[]` 를 WebUI 문법으로 — 괄호 1개당 ±5%
<small>⚠️ 2025-04 기준 · 근거 2건</small>

NAI 프롬프트를 로컬(WebUI) 문법으로 옮길 때 가중치를 손으로 계산하지 않아도 된다.
**NAI-Tag-Viewer** 에 변환 기능이 붙어 있다 (1건, 2025-04. 저장소 `https://github.com/DCP-arca/NAI-Tag-Viewer`).

```text
변환 규칙 : 괄호 하나당 ±5%  (소수점 둘째 자리까지, 섞여 있어도 처리)
예시      : [a, {b], c}   →   (a:0.95), b, (c:1.05)
```

> ⚠️ **중괄호 `{}` · 대괄호 `[]` 로 조절한 것만 변환된다. 최근 추가된 `::` 문법은 변환되지 않는다.**
> 그쪽은 이미 가중치가 눈에 보이기 때문에 굳이 만들지 않았다는 것이 제작자 설명이다.

이미지를 불러올 필요 없이 **프롬프트 칸에 직접 적어서 변환기만 쓸 수도 있고**, 변환 결과를 복사하는 버튼이 있다.
WebUI 로 생성한 이미지도 정상적으로 불러와지며, 줄바꿈으로 작성된 프롬프트가 잘리던 문제도 고쳐졌다.

### 스테가노그래피로 숨은 정보

이 뷰어의 초기 버전은 **EXIF 에 태그가 살아 있는 이미지만 읽었고, NAI 가 스테가노그래피로 숨겨 넣은 정보는 못 읽었다.**
1.0.2 이후 패치로 대부분 읽히게 됐다. 로컬 A1111 에서는 **`sd-webui-stealth-pnginfo`** 확장이 그 숨은 정보를 읽는다.
서명되지 않은 실행파일이라 백신이 트로이 목마로 오탐하는 사례가 있다 — 불안하면 코드가 공개돼 있으니 직접 빌드하라는 것이 제작자 답변이다.

`{}`·`[]` 와 `::` 가 각각 어느 판본의 문법인지는 [NovelAI](nai.md) 의 프롬프트 문법 절 참조.

<small>근거 — [이미지 파일에서 NAI 프롬프트(Exif)를 확인할 수 있는… 23.12](https://arca.live/b/aiart/94581185) · [NAI 이미지 태그 뷰어 업뎃된거 알고있었움? (with w… 25.04](https://arca.live/b/aiart/133417496)</small>

## 6-e-3. Danbooru 프롬프트 도우미 — RAG 로 지어낸 태그를 구조적으로 차단한다
<small>2026-06 기준 · 근거 1건</small>

LLM 에게 태그를 물으면 **존재하지 않는 태그를 그럴듯하게 지어내는** 것이 오래된 문제였다.
이것을 **도구 차원에서 구조적으로 막은** 것이 있다 (1건, 2026-06).

```text
https://taghelper.baepoyong.com/       Danbooru 프롬프트 도우미
```

채널의 Danbooru 태그 자료(원문 139793445)를 기반으로 **RAG 시스템을 구축**해,
**출력을 DB 에 실재하는 태그로 엄격히 제한 — DB 에 없는 태그는 아예 출력할 수 없게** 만들었다.

| 구성 | 값 |
|---|---|
| 임베딩 모델 | `https://huggingface.co/intfloat/multilingual-e5-large` — **약 2GB 라 CPU 에 올려도 충분히 빠르다** |
| 코드 | `https://github.com/joykst96/danbooru-tag-rag` (태그 파일은 직접 넣어야 하고, `.env` 는 example 을 환경에 맞게 수정) |
| LLM 서빙 | 레포에 안내가 없다 — 제작자는 llama.cpp 를 썼다 |

> ⚠️ **공개 웹은 제작자 개인 서버를 경유하고 백엔드에 LLM 이 도는 구조다.**
> 커스텀 노드로 자동화해 요청을 쏟아부으면 **사이트를 닫거나 요청당 시간제한을 걸겠다고 제작자가 명시했다.**
> ComfyUI 에서 쓰려면 로컬에 직접 구축해 연결해야 하고, LLM 없이 순수 벡터 검색만 붙이는 것은 어렵지 않다고 한다.

같은 '환각 차단' 계열로 MCP 판(`danbooru-tag-rag-mcp`)과 Gemini Function Calling 판이 위 「6-e」 절에 있다.

<small>근거 — [Danbooru 프롬프트 도우미 26.06](https://arca.live/b/aiart/174228063)</small>

## ⚠ 2026-07 NAI 로그인 로직 변경 — 서드파티 도구가 전면 인증 실패했다
<small>2026-07 기준 · 근거 1건</small>

**2026년 7월 초 NovelAI 의 로그인 로직이 바뀌면서 서드파티 도구가 전면 인증 실패했다** (1건, 2026-06 글의 댓글).

```text
로그인 실패: accessToken
Error getting ANLAS: trainingStepsLeft
API 키 검증 실패: 토큰이 유효하지 않습니다
```

**아이디 로그인과 API 로그인이 둘 다 막혔고**, 제작자가 로직 변경을 확인하고 수정을 마쳤다.

> **교훈 — NAI 연동 도구는 NAI 측 인증이 바뀔 때마다 업데이트가 필요하다.**
> 갑자기 로그인이 안 되면 도구를 의심하기 전에 **그 도구의 최신 릴리스부터 확인**하라.

### 같은 글에서 고쳐진 두 버그 (NAI-Auto-Generator 비공식 V4.5 포크)

`https://github.com/sagawa8b/NAI-Auto-Generator-V4/releases`

| 증상 | 원인 |
|---|---|
| **자동완성이 콤마 뒤에 안 뜬다** | 콤마가 'end of word' 문자에 포함돼 팝업이 강제 종료되고 이후 QCompleter 내부 상태가 복구되지 않았다 — eow 에서 콤마를 빼고 minimum prefix 를 2로 통일, popup index 접근 전 유효성 체크를 넣어 해결 |
| **자동 생성 중 프롬프트가 반영되지 않는다** | 연속 생성 도중 프롬프트를 편집하면 **편집 중인 불완전한 텍스트가 그대로 반영**됐다. 원인은 워커 스레드가 GUI 위젯을 직접 읽은 **thread-safety 위반**(PyQt 에서 GUI 접근은 메인 스레드에서만 가능)이고, 시그널/슬롯 + `threading.Event` 동기화로 고쳤다 |

NAI 도구 전반은 [NovelAI](nai.md) 의 '보조 도구' 절.

<small>근거 — [NAI-Auto-Generator v4.5 (비공식) 업데이… 26.06](https://arca.live/b/aiart/174988734)</small>

## 6-c-2. 갤러리·분류·캡셔닝 도구 (2025-11 ~ 2026-05)
<small>2026-05 기준 · 근거 5건</small>

이미지를 뽑은 뒤 **찾고·분류하고·캡션을 다는** 도구들이다. 위 「6-c」 의 연장이다.

### TagGallery_Web — 태그로 검색하는 로컬 갤러리 (2025-11)

`https://github.com/moonhole0512/TagGallery_Web` (이전 데스크톱 판 `.../TagGallery`)
**데스크톱 버전이 ComfyUI 와 드래그앤드롭·복사붙여넣기가 안 되던 문제 때문에 웹으로 옮긴 것**이다.
실행 파일 배포가 없어 **파이썬이 필요**하고, 사용 순서는 **설정 → 스캔 → 검색**.
스캔해도 아무것도 안 뜨면 cmd 창의 에러 로그를 봐야 한다.

### Konomi 0.15.x — 실시간 폴더 감시가 제거됐다 (2026-05)

가장 큰 변경이 **기능 제거**라 알아 둬야 한다.

> NAS/SMB/느린 디스크 환경에서 **디스크 IO 문제가 너무 많아 실시간 폴더 감시를 삭제했다.**
> 이제 외부에서 폴더에 파일이 추가·삭제·이름변경되면 사이드바의 **'전체 폴더 새로고침'** 이나
> 폴더 우클릭 → **재스캔**으로 사용자가 직접 갱신해야 한다(앱 내부 NAI 생성기로 만든 이미지는 자동 반영).

**12만 장 규모 사용자가 '수동 갱신 쪽이 10배 낫다' 고 확인해 줬다.**
성능 면에서 로컬 SQLite 를 **WAL 모드 + 읽기/쓰기 연결 분리**로 바꿔 스캔 중에도 갤러리가 멈추지 않는다.
고쳐진 것 — Synology/NAS 의 `@eaDir`·`#recycle`·`__MACOSX` 썸네일 혼입, 호스트와 같은 GID 를 쓰는 Docker 컨테이너의 `gid in use` 시작 실패(PUID/PGID 명시로 기존 그룹 재사용),
긴 프롬프트·경로에서 검색이 죽던 문제, 하위 폴더 필터가 많을 때의 413, 느린 NAS MariaDB 의 트랜잭션 타임아웃.
⚠️ 이 시점의 Docker 환경은 실사용 불가 수준이다.

### ⚠ 자동 분류가 섞인다면 — EXIF 에 직전 이미지의 프롬프트가 남는 경우가 있다

프롬프트 분류기 `Prompt-Classifier` 가 v3.0.0 에서 **제외 키워드**를 넣은 이유가 실전 지식이다 (1건, 2026-05).

> **NAIA 로 ComfyUI 자동 생성을 돌리면 이미지 정보에 '해당 이미지의 프롬프트' 는 안 남고
> '이전에 뽑은 이미지의 프롬프트' 가 남아 있는 경우가 있다.** (워크플로우에 따라 다르다)

분류 결과가 계속 섞인다면 도구를 의심하기 전에 **EXIF 에 무엇이 실제로 들어 있는지부터 확인**해야 한다.

### 캡셔닝용 VLM 을 무료 Colab 으로 (2026-02)

학습용 태그·자연어 설명을 만들 VLM 을 GPU 없이 돌리는 경로다.
노트북이 하는 일은 **구글 드라이브 연동 → llama.cpp·cloudflared·GGUF·mmproj 다운로드 → llama.cpp 라우터 모드 실행 + cloudflared 터널링** 이다.

| 항목 | 값 |
|---|---|
| 기본 모델 | `https://huggingface.co/mradermacher/Qwen3-VL-8B-NSFW-Caption-V4-GGUF` 의 **Q4_K_M** |
| 드라이브 여유 | **5GB** (GGUF 캐시용 — 2회차부터 시간을 아낀다) |
| 속도 | 연결 10초 · **모델 로딩 2~3분** · 응답 **8~13초** |
| ComfyUI 연동 | **`comfyui-openai-api`** 노드로 llama.cpp 라우터에 연결 |

⚠️ 노트북이 개인 구글 드라이브 공유 링크라 만료 가능성이 있다.

### CoNAI 에 ComfyUI 를 물릴 때의 두 함정 (2026-04)

| 증상 | 원인 |
|---|---|
| **'입력 필드 없음'** | 워크플로를 ComfyUI 에서 **반드시 'API 로 내보내기' 로 저장**해야 내부 항목이 잡힌다 |
| **시드가 고정돼 두 번째 요청이 씹힌다** | API 내보내기로 만든 워크플로는 **고정 시드로만 동작**한다. KSampler 안의 randomize 만으로는 안 되고 **`Seed (rgthree)` 같은 별도 랜덤 시드 노드**를 연결해야 한다 |

포트는 빌드 후 **1666**, 빌드 전 dev 실행이면 **1677** 이다.

<small>근거 — [AI 이미지 갤러리 web버전 만듬 25.11](https://arca.live/b/aiart/155413135) · [프롬프트 분류기 업뎃 26.05](https://arca.live/b/aiart/169675680) · [CoNai 26.4.15 업뎃 챈섭?기능 추가 26.04](https://arca.live/b/aiart/167738002) · [colab으로 VLM을 실행해보자. 26.02](https://arca.live/b/aiart/161842488)</small>

??? note "근거 5건 전부 보기"
    [AI 이미지 갤러리 web버전 만듬 25.11](https://arca.live/b/aiart/155413135) · [프롬프트 분류기 업뎃 26.05](https://arca.live/b/aiart/169675680) · [CoNai 26.4.15 업뎃 챈섭?기능 추가 26.04](https://arca.live/b/aiart/167738002) · [colab으로 VLM을 실행해보자. 26.02](https://arca.live/b/aiart/161842488) · [AI 생성 이미지 관리 앱 Konomi 0.15.x 업데이트 26.05](https://arca.live/b/aiart/171481122)

## 6-e-4. WD14 Auto Prompt Generator — 이미지에서 프롬프트를 역추론하는 도구 (v1 · v2)
<small>⚠️ 2025-07 기준 · 근거 2건</small>

NAIA 제작자가 만든 img2prompt 도구다. 이미지를 넣으면 태그를 역추론해 프롬프트를 만들어 준다.

```text
v1  https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/WD14_Auto_Prompt_Generator.zip
v2  https://huggingface.co/baqu2213/PoemForSmallFThings/resolve/main/NAIA/WD14_Auto_Prompt_Generator_v2.zip
```
*(2GB 초과, exe 실행. 내장 태거는 `wd-vit-large-tagger-v3` 이고 **사용자 CPU 로 돌아간다.**)*

| 설정 | |
|---|---|
| 태그 임계값 | 이미지에서 태그를 뽑아낼 강도 |
| ⚠️ **캐릭터 임계값** | **제대로 작동하지 않으니 그냥 무시하라고 제작자가 직접 밝혔다** |
| 즉시 추론 | 붙여넣기·불러오기만 해도 바로 태그를 뽑는다 |
| 캐릭터 특징+이름 제거 | 활성화한 태그가 결과에서 빠진다 |
| **WEBUI/Comfy 모드** | 태그 안의 괄호를 자동으로 `\(`, `\)` 로 **이스케이프**한다 — NAI 는 이스케이프가 필요 없고 로컬은 필요하다는 계열 차이를 도구가 대신 처리해 주는 것 |
| 선행/후행 프롬프트 | 선행은 `1girl`·`1boy` 등 인물 태그 **뒤**에, 후행은 추출된 태그 **맨 끝**에 붙는다 |

**이미지 투입은 클립보드 복사 후 `ctrl + v` 가 가장 확실하다** — 드래그는 사이트 호환을 타서 실패하는 경우가 있다.

### v2 — NAI API 직결 생성

NAI v4.5-full 에 물릴 수 있는 생성 UI 가 추가돼 `rating:questionable` · `nsfw` 를 자동 할당하고,
[즉시 추론] 옆의 **[즉시 생성]** 으로 붙여넣기 → 추론 → 생성까지 한 번에 간다.
**생성 UI 는 NAI 전용이라 로컬 계열에는 붙지 않는다.**

> ⚠️ **NAI 공식 홈페이지로 이미지를 보낼 때는 반드시 '파일을 클립보드에 복사' → `ctrl + v` 로 처리해야 한다.**
> 탐색기의 기본 Copy 버튼이나 '이미지를 클립보드에 복사' 기능은 **exif 를 남기지 않는 사양**이라
> 그 경로로 넣으면 프롬프트가 딸려 오지 않는다.

**알려진 버그** — 여러 캐릭터 프롬프트를 쓰는 중 갑자기 엉뚱한 캐릭터가 나오면 **C1 의 프롬프트를 한 번 껐다 켠다.**

**한계** *(댓글)* — WD14 추론이라 **implied tag 가 딸려 나오고 디테일이 날아간다.**
로라 학습용 태깅이면 시비타이에 던져 넣고 다시 받는 편이 낫다는 의견이 있다.

→ 다른 태그 추출 도구는 위 '6-e. 태그를 찾고 프롬프트를 만들어 주는 도구' 절.

<small>근거 — [WD14 Auto Prompt Generator - img2… 25.07](https://arca.live/b/aiart/141451403) · [WD14 Auto Prompt Generator (버전2) … 25.07](https://arca.live/b/aiart/141522681)</small>

## 6-e-5. 그림에서 작가를 되찾는 도구 — Kaloscope 2.0, 그리고 aitag.win
<small>2026-03 기준 · 근거 3건</small>

### Kaloscope 2.0 — 그림 → 작가 스타일 분류

```text
모델   https://huggingface.co/heathcliff01/Kaloscope2.0
체험   https://huggingface.co/spaces/DraconicDragon/Kaloscope-artist-style-classifier   (설치 없이 바로)
```

| 스펙 | |
|---|---|
| 아키텍처 | LSNet, 약 **183M** 파라미터 |
| 입력 | **448×448** (v1.1 의 224 에서 상향) |
| 분류 대상 | **39,260개 작가 스타일** (v1.1 의 31,770 에서 상향) |
| Top-1 정확도 | **90.13%** (v1.1 은 85.6%) |
| 학습 데이터 | 2025-09 단부루에서 **이미지 40장 이상인 작가**만 추리고, imgutils 로 중복 제거 후 미러링·회전 증강으로 **작가당 100장** 균형 |

쓸모 — 마음에 드는 그림의 작가 태그를 찾거나, **애니 스샷 같은 것을 넣어 '그런 느낌으로 그리는 작가' 를 역으로 찾아낸다.**

> ⚠️ **여러 작가가 섞인 그림은 못 맞힌다.** 작가 8명이 랜덤으로 섞인 짤 30장을 돌려 한 명도 못 맞혔다는 보고가 있고
> '무용지물' 이라는 평가가 붙었는데, **이 모델은 단일 스타일 예측이 목적**이라 섞은 조합을 역추적하라는 건 애초에 다른 문제다.
> **섞은 조합을 되찾으려면 exif 를 봐야 한다.**

ComfyUI 커스텀 노드로도 설치되지만 **작가 링크는 만들어 주지 않고**, 결과값이 `작가_이름 (어쩌구)` 처럼
언더바와 괄호가 붙은 형태라 **`CR Text Replace` 같은 노드로 후처리해야** 프롬프트에 바로 넣을 수 있다.

### aitag.win — 남의 그림 exif 를 검색해서 본다

`https://aitag.win/` — 검색어를 넣고 결과 이미지 좌측 상단의 타입 표시로 고른다.
검색창에 `nai` 라고 쳐도 다른 유형이 섞이므로, **NAI 만 보려면 아무 NAI 그림에 들어가 `TYPE=nai` 를 누른다.**

```text
상세 화면에서 json 을 누르면 원본 필드가 그대로 보인다
  prompt=   메인 프롬프트
  c=        캐릭터 프롬프트 1 · 2 · 3
  ntags=    네거티브 프롬프트
  그 아래   생성 설정값
```

특히 쓸모 있는 이유 — **픽시브에서 exif 를 못 따는 그림도 여기엔 살아 있는 경우가 있고**,
업로더가 모자이크 등 추가 작업을 한 뒤에도 원본 상태의 exif 가 남아 있는 사례가 있다.
그림 위에서는 스크롤이 안 먹히니 창을 제일 왼쪽에 두고 스크롤한다. 정렬은 최신순이고 SD·ComfyUI 짤도 꽤 있다.

### NAI 아티스트 셔플기 — 개선판을 쓸 것

작가 태그를 잔뜩 넣어 두면 그중 몇을 랜덤으로 뽑고 랜덤 가중치를 매겨 주는 단일 HTML 도구다.
출력이 `1::artist:작가명 ::,` 형태라 **NAI 전용**이고, 로컬에 쓰려면 `(작가명:가중치)` 로 바꿔야 한다.

> ⚠️ **원글(`ver.0.02`)보다 댓글에 링크된 개선판이 낫다 — `https://arca.live/b/aiart/165942863`**
> 작가명 뒤 띄어쓰기와 마지막 콤마가 제대로 붙게 고쳤고 모바일에서 복사 버튼이 안 먹던 문제를 수정했다.
> 또 다른 댓글에는 **베이스 작가 한 명 고정 + 뽑을 작가 수 0~15 선택** 기능을 더한 파생판이 있다.

<small>근거 — [Kaloscope2.0 아티스트 스타일 분류, 예측 모델 25.11](https://arca.live/b/aiart/153259226) · [외부 ai exif사이트 26.03](https://arca.live/b/aiart/165668485) · [(NAI) 아티스트 셔플기 ver.0.02 26.03](https://arca.live/b/aiart/164687273)</small>

## 6-b-2. 자세·체위 레퍼런스 — 그림은 여기, 태그는 e621
<small>2025-11 기준 · 근거 1건</small>

`https://sexpositions.club/positions` — 체위 이름과 그림을 짝지어 보여 주는 외부 사이트. **결제 없이 전부 볼 수 있다.**
주 체위를 누르면 관련 체위들이 한꺼번에 펼쳐지는 구조라, 이름만 봐서는 감이 안 오는 세부 체위를 직관적으로 확인할 수 있다.

| 쓰임 | |
|---|---|
| 아이디어 소스 | 포즈가 머리에서 안 떠오를 때 훑어본다 |
| 레퍼런스 이미지 | 정 안 되면 그림 자체를 넣어 버린다 |

> ⚠️ **여기 나오는 체위 이름이 전부 태그로 존재하지는 않는다.** 글쓴이도 *"단부루에 있는 자세도 있고 없는 자세도 있다"* 고 밝혔다.
>
> **댓글이 더 나은 경로를 제시했다 — 체위는 단부루보다 `e621` 쪽에 훨씬 다양하게 태그로 학습돼 있어서,
> 이 사이트를 보는 것보다 e621 을 탐사하는 편이 실사용에는 더 낫다.**
> 이름만 있고 태그가 없는 체위는 결국 못 쓰므로 **태그 존재부터 확인하는 e621 경로가 우선**이다.

→ 태그를 확인하는 실전 경로는 [프롬프트 쓰는 법](prompting.md), 태그 사전은 위 '6-b' 절.

<small>근거 — [야스 체위 관련 정보 사이트 25.11](https://arca.live/b/aiart/152506261)</small>

## 6-i-2. 프롬프트 모음 HTML — png 로 위장해 올리고 json 으로 채운다
<small>2026-03 기준 · 근거 2건</small>

아카라이브가 html 첨부를 막아서 채널의 프롬프트 모음 HTML 은 **png 로 위장해 올라온다.**

```text
1. 첨부된 png 를 받는다
2. 확장자를 .zip 으로 바꿔 압축을 푼다
3. 안의 html 을 브라우저로 연다  →  처음엔 비어 있다
4. 좌측 사이드바 아래 '백업불러오기'  →  html 이름과 맞는 json 을 불러오면 채워진다
```

별도 프로그램이 필요 없고 크롬 등 일반 브라우저로 바로 열린다. 태그에 마우스를 올려 클릭하면 자동 복사되고,
좌측 상하단의 '내용수정' 으로 편집 모드에 들어가며 사이드바 툴 위치도 버튼으로 옮길 수 있다.

| 구성 규칙 *(NAI 개인 프롬 모음 260311 판)* | |
|---|---|
| `각종태그.html` | 2인 이상 행위 틀이 들어 있다. **왼쪽은 여자 캐릭터 프롬 칸에, 오른쪽은 `///` 로 나뉘어 있으니 남자 캐릭터 칸을 추가해 나눠 넣는다** |
| 2+boy 인데 남자 행동 프롬이 하나뿐 | 남자 칸 두 개에 똑같이 넣는다 (여자 쪽도 동일) |
| 행동 프롬 | 전부 **위치 자동설정**으로 뽑은 것이라 가로/세로 해상도만 맞춰 주면 된다 |

**안 열릴 때** — 브라우저 쿠키 차단이나 광고 차단 확장 때문일 수 있다. 크롬으로 열면 대개 된다.

같은 방식의 **프리큐어 캐릭터 태그 HTML** 도 있다 — `https://mega.nz/file/0FFiRByR#yGE_rbuuKcLDmu0QL1_bpJcEOXeoQYftktoWqPP-1is`.

> ⚠️ **파일 자체는 제미나이·그록·GPT 에게 만들게 한 것이고 글쓴이가 뽑던 캐릭·상황 위주라 빠진 것이 많다.**
> **첨부·메가 링크라 시간이 지나면 만료·삭제될 수 있다.**

<small>근거 — [NAI) 개인 프롬 저장해둔 html 파일 공유 260311 26.03](https://arca.live/b/aiart/163685712) · [프리큐어 캐릭터 태그 html 공유 26.02](https://arca.live/b/aiart/163071111)</small>

## ⚠ ANIMA 그림체 로라 4종 (2026-08) — 구글 드라이브 개인 공유라 만료 위험
<small>2026-08 기준 · 근거 1건</small>

만들어 두고 올리지 않았던 **ANIMA 전용 그림체(스타일) 로라 4개**를 한데 모아 공유한 글이다 *(2026-08-13)*.

```text
https://drive.google.com/drive/folders/1YxP3Xmw--eganjjGHed_13Gsg8Ww4igf?usp=sharing
```
*(본문은 base64 로 가려 올렸고, 디코딩하면 위 주소다.)*

| | |
|---|---|
| 구성 | 본문에 1·2·3·4 로 번호를 매긴 **로라별 그림체 예시 이미지**가 붙어 있다. 처음 올렸을 때는 3개뿐이라 '4가 없다' 는 지적이 있었고 글쓴이가 곧바로 4번을 추가했다 |
| 대상 모델 | **ANIMA** (댓글에서 확인). 다른 계열 체크포인트에는 그대로 쓸 수 없다 |
| ⚠ 정보 부족 | **개별 로라의 이름·권장 가중치·트리거 워드가 본문에 적혀 있지 않다.** 받아서 예시 이미지와 대조해 가며 써야 한다 |

> ⚠️ **만료 위험 — 개인 구글 드라이브 공유 폴더다.** 배포자가 내리거나 구글이 차단하면 언제든 접근이 끊긴다.
> **필요하면 미리 받아 둘 것.** (지우지 않고 표시만 해 둔다)

→ ANIMA 로라를 쓸 때 되풀이되는 것은 위 'ANIMA 그림체·캐릭터 로라를 쓸 때' 절.

<small>근거 — [아니마 그림체 로라 만들어둔거 공유 26.08](https://arca.live/b/aiart/179776875)</small>

## 3-f-2. ⚠ CivitAI 의 X/XXX 필터 — 두 배포글이 정반대로 적었다
<small>2025-09 기준 · 근거 2건 · **근거 약함** · 자료 엇갈림</small>

로리 캐릭터로 플래그된 로라 페이지가 안 보일 때 **계정의 X/XXX 열람 설정을 어느 쪽으로 두어야 하는지 자료가 갈린다.**

| 원문 | 설명 |
|---|---|
| `148268845` (Twintails Marra) | 본문은 *"설정에서 X/XXX 를 **꺼야** 보인다"* 고 적었으나, **댓글에서 제작자가 'X/XXX 필터를 **켜 둔** 상태여야 보인다' 고 정정**했고 질문자도 수긍했다 |
| `148357981` (Kelly Marra) | *"계정의 X/XXX 열람 설정을 **꺼야** 페이지가 보인다(켜 두면 오히려 안 보인다)"* |

**둘 중 어느 쪽이 맞는지 판정할 자료가 없다.** 시비타이 모더레이터가 로리 캐릭터 로라에 플래그를 달아 두어서 생기는
현상이라는 배경만 공통이므로, **안 보이면 두 방향을 다 시도해 보는 수밖에 없다.**

> ⚠️ **두 로라 모두 시비타이에서 잘렸다(밴)는 보고가 있어 링크가 이미 죽었을 수 있다.**
> 제작자는 프로필에 있던 것들의 백업 글을 따로 올렸다고 답했다.

곁가지로 얻을 것 — 원작의 초록 눈은 **`green sclera, glowing eyes`** 로 바로 나왔다.
**흰자 자체를 초록으로 만드는 `green sclera` 를 쓰는 것이 요점이고 `green eyes` 로는 안 된다.**

→ 검열·등급 필터 일반은 위 '3-f. 받는 곳이 civitai 라면' 절.

<small>근거 — [(페도) 넷플릭스 힐다 Kelly Marra 로라 공유 25.09](https://arca.live/b/aiart/148357981) · [(페도) 넷플릭스 힐다 Twintails Marra 로라 공유 25.09](https://arca.live/b/aiart/148268845)</small>

## 3-b-3. 웹툰 로라의 공통 요령 — 말풍선 지우기와 그림체 근접
<small>2025-11 기준 · 근거 2건</small>

웹툰 원본을 학습한 로라 전반에 통하는 요령이다.

| 문제 | 처방 |
|---|---|
| 말풍선·효과음이 그림에 딸려 나온다 | 네거티브에 **`speech bubbles`** 또는 **`sound effects`** |
| 만화 그림체에 더 가깝게 | 긍정에 **`sketch`**, 네거티브에 **`lipstick`** |
| 떡툰 특유의 흰색 모자이크 재현 | **`blank censor`** *(로라와 무관하게 검열 표현 전반에 쓸 수 있다)* |

배포 사례 두 개의 프롬프트 —

| 로라 | 트리거 · 프롬프트 |
|---|---|
| 「우리 길드 아이돌」 배아진 `https://civitai.com/models/1935990?modelVersionId=2191143` | 트리거 **`ahjin`** / `ahjin, long hair, black hair, parted bangs, hair behind ear, mature female` |
| 「쓰리엑스라지러브(3XLOVE)」 천보경 `https://civitai.com/models/2125602?modelVersionId=2404465` | 트리거 **`bokyung`** / 대학생 `sketch, bokyung, brown eyes, brown hair, long hair, skinny` · 고등학생은 `medium hair` |

3XLOVE 쪽은 **대학생 시점과 고등학생 시점을 모두 학습**시켰고 교복도 하복·춘추복 둘 다 넣어 트리거만 잘 쓰면 그대로 나온다.

```text
춘추복  school uniform, white shirt, long sleeves, diagonal-striped necktie, yellow vest, grey plaid skirt
하복    school uniform, white shirt, untucked shirt, short sleeves, breast pocket, blue skirt
```

`skinny` 는 필수가 아니지만 넣는 쪽이 몸매가 더 예쁘게 나오고, NSFW 를 뽑아도 성기는 자연스럽게 잘 나온다.
배아진 쪽 제작자는 **원작 특유의 분위기까지 완벽히 재현되지는 않는다**고 미리 밝혔다.

→ 작품별 목록은 위 '3-b. 웹툰·애니 캐릭터 로라' 절.

<small>근거 — [웹툰 LoRA 공유) 우리 길드 아이돌 - 배아진 25.09](https://arca.live/b/aiart/147279963) · [웹툰 Lora) 쓰리엑스라지러브(3XLOVE) - 천보경 25.11](https://arca.live/b/aiart/153703989)</small>

## 이 문서가 딛고 선 주장

이 문서가 인용한 원문에서 뽑은 것이다. 여러 글이 같은 말을 하는지 센 것이고, 근거가 1건뿐인 주장은 그만큼 약하다.

근거가 센 40개만 싣는다 (나머지 463개는 생략).

| 주장 | 찬성 | 반대 | 시점 |
|---|---:|---:|---|
| 이 시리즈의 예시 이미지는 ComfyUI 로 뽑았으므로 이미지를 ComfyUI 캔버스에 끌어다 놓으면 노드(워크플로우)가 그대로 불러와진다 | 44 | 0 | 2025-04~2026-07 |
| 배포글에 적힌 'LoRA Base Model' 은 그 로라를 만들 때 쓴 학습용 베이스 모델일 뿐이고, 그림을 실제로 뽑는 것은 별도의 'Checkpoint Model' 이다 — 제작자가 뉴비 혼동을 막으려고 본문에 못 박아 둔 문구다 | 31 | 0 | 2025-02~2026-07 |
| 같은 제작자의 웹툰·애니 캐릭터 LoRA 배포 목록 (전부 LoRA Base illustriousXL_v1.1 / 체크포인트 WaiNSFWillustrious V140) — 퀘스트지상주의 6종 `baek chaerin, elisa, kim dahyeon, lee jihyeon, yang soha, yeon seohui` · 초인의 게임 6종 `higpr(대사제), baek hayeon, lee nayeon, qun1(여왕), saniya ahmetova, shuran` · 일진담당일진 5종 · 수요웹툰의 나강림 13종 · 사시미 한 자루로 아카데미를 씹어먹음 6종 · 전지적 독자 시점 14종 · 현실퀘스트 7종 `choi minhye` 외 · 이세계 밀프 헌터 10종 · 광마회귀 공손월 · 동아리 11종. 짝 글 관계 — 전독시 https://arca.live/b/aiart/139326347 ↔ https://arca.live/b/aiart/139333927 , 밀프헌터 https://arca.live/b/aiart/140473932 ↔ https://arca.live/b/aiart/140480040 | 26 | 0 | 2025-05~2025-12 |
| 채널의 웹툰·애니 캐릭터 LoRA 배포 시리즈는 동봉된 Metadata(json) 파일의 파일명을 LoRA(.safetensors) 파일명과 똑같이 맞춰 같은 폴더에 넣으면 WebUI 에서 트리거워드·프롬프트가 자동으로 뜬다. 이 json 은 ComfyUI 전용이 아니라 WebUI(Stable Diffusion) 사용자도 로라 폴더에 같이 넣으면 된다 | 25 | 0 | 2025-04~2025-08 |
| 채널의 모델·로라 배포글은 한 달 기한 링크나 만료된 클라우드 주소가 많아, 오래된 배포글은 링크가 죽어 있을 것을 전제하고 댓글의 대체 링크를 먼저 확인해야 한다 | 24 | 0 | 2022-12~2026-06 |
| 이 시리즈의 트리거 워드는 없어도 대체로 잘 나오지만 넣는 편이 타율이 높다. 다만 의상·장식·특이한 눈동자·문신은 재현이 잘 안 될 수 있어 배포글이 의상 태그를 따로 나열해 두었다 | 15 | 0 | 2025-04~2025-06 |
| 이 시리즈의 공통 부정 프롬프트는 `bad quality, worst quality, worst detail, sketch, (censor:1.1), (shaded face:1.1), (dark:1.1)` 이다(초기 글은 `(shaded face:1.1), (dark:1.1)` 없이 `shaded face` 만 쓴다) | 13 | 0 | 2025-04~2025-06 |
| 채널에는 배포 링크를 base64 로 인코딩해 올리는 관행이 있어, 뜻 없는 영문+숫자 덩어리가 보이면 base64 디코더에 넣으면 실제 주소(kio.ac · mega.nz 가 많다)가 나온다 | 12 | 0 | 2023-03~2026-06 |
| 워크플로우는 EXIF 가 든 이미지·영상 파일을 다운로드해 ComfyUI 창에 드래그앤드롭해 불러온다 | 11 | 0 | 2024-06~2026-08 |
| 통합팩에서 sage attention을 쓰려면 run_nvidia_gpu.bat 대신 run_nvidia_gpu_fast_fp16_accumulation.bat 으로 실행한다 | 8 | 0 | 2026-02~2026-08 |
| ComfyUI 포터블 통합팩 배포 링크는 본문에 base64 로 올라오고 압축 비밀번호는 `ai`, 기한은 한 달이라 지난 판은 대개 만료돼 있다 | 8 | 0 | 2026-02~2026-08 |
| 학습 데이터셋 장수 권장치는 자료마다 다르다 — 캐릭터 10~50장(스타일 100~4000장), 한 의상당 20~40장, 50~150장에 100장이 적당, 최소 30장·50장 이상 안정권·200장 초과는 의미 없음 | 8 | 0 | 2023-03~2026-06 |
| sage attention은 ComfyUI 작업 속도를 10~15% 높인다 | 8 | 1 | 2026-02~2026-08 |
| 캐릭터 LoRA 는 트리거워드 하나로 끝나지 않고 외형·의상 태그를 함께 적어야 한다 — 리루루 LoRA 는 전투복/사복1/사복2 세 벌의 태그 묶음을, 신월의 루나 LoRA(트리거 `new_moon_luna`)는 트리거 뒤에 외형 태그를 길게 붙이는 예시를 제공한다 | 7 | 0 | 2025-01~2025-08 |
| 캐릭터·작가·매체 태그 안의 괄호는 역슬래시로 이스케이프해 nagisa \(blue archive\), star \(sky\), graphite \(medium\) 처럼 적는다 | 7 | 0 | 2025-08~2026-07 |
| NAI Diffusion V4 Full 로 작가 태그를 비교할 때 채널이 쓰는 표준 조건은 Steps 28 / Prompt Guidance 6 / Sampler Euler Ancestral / Prompt Guidance Rescale 0.7 / Noise Schedule karras / Add Quality Tags on / Undesired Content Preset Heavy 이고, 공통 프롬프트는 `nsfw, [작가 태그], year 2024, cowboy shot, solo, straight-on, standing, arm at side` 다 | 6 | 0 | 2025-03~2025-04 |
| ComfyUI 통합팩의 지원 GPU는 지포스 3000~5000번대이며 라데온은 미확인이다 | 6 | 0 | 2026-02~2026-08 |
| 이 웹툰 캐릭터 LoRA 시리즈의 다운로드처는 '키오스크(kio.ac)' 서버 장애로 civitai 로 옮겨졌고, 이후 일부 제작자는 civitai 서버·정책에 회의를 느껴 아카라이브로 다시 옮겼다 — 링크가 죽었으면 civitai 에서 작품명으로 검색하는 편이 빠르다(https://civitai.com/search/models?query=작품명) | 6 | 0 | 2025-05~2025-06 |
| negpip 덕에 일반 프롬프트 칸에서 (tag:-1), 형식의 음수 가중치를 쓸 수 있다 | 6 | 0 | 2026-02~2026-08 |
| 와일드카드는 언더바 두 개로 감싼 __파일명__ 형태로 호출하고, 하위 폴더에 있으면 __폴더/파일명__ 으로 적는다 | 6 | 0 | 2024-03~2026-07 |
| 단품 캐릭터 LoRA 배포 — 웹툰 '동아리' 박다영(베이스 waiNSFWIllustrious_v80, 트리거 `Dayoung`, Steps 50 / Euler a / Beta / CFG 5) https://civitai.com/models/1517725?modelVersionId=1717140 · 애니 '귀환자의 마법은 특별해야 합니다' 3종(`ajest jedgar` https://civitai.com/models/596285 , `brigette` https://civitai.com/models/598370 , `romantica eru` https://civitai.com/models/598376) · '새로구미(여구미)' (트리거 `saero-gumi` / 인간형 `Saro`, 한복·한푸·기모노 의상 세트) https://civitai.com/models/1727202/anime-character-saero-gumi-saero-soju · '갸루에게 상냥한 오타쿠 군' 나루미 유우아이 (트리거 `narumi1` 필수) https://civitai.com/models/1639028 · '성인웹툰 속 엑스트라가 되었다' 4인 통합 (`parkgonggi`, `jungsil`, `nohyeju`, `leezy`) https://civitai.com/models/1664554 · 게임 '클로저스' 비나 (트리거 `binah`) https://civitai.com/models/1792789?modelVersionId=2028848 | 6 | 0 | 2025-04~2025-07 |
| ANIMA 계열 LoRA 배포글 머리의 `LoRA Base Model: anima-base-v1.0` 은 학습에 쓴 베이스일 뿐 그림을 만드는 모델이 아니다. 실제로 그림을 뽑는 체크포인트는 `waiANIMA_v10Base10` 이고 그 위에 캐릭터 LoRA 를 얹는다. | 6 | 0 | 2026-05~2026-06 |
| 2023년 SD1.5 시절에 배포된 LoRA·병합 모델은 현행 Illustrious/Pony/SDXL 계열 체크포인트와 호환되지 않아 실사용 가치가 거의 없고, 옛 모델 계보를 확인할 때만 쓸모가 있다 | 6 | 0 | 2023-01~2023-03 |
| 포니 계열에서 유래한 스코어 태그는 score_9 부터 score_1 까지 아홉 단계이며, 긍정에 score_9/score_8/score_7 중 1~3개를, 네거티브에 score_1/score_2/score_3 을 넣는 것이 관례다 | 6 | 0 | 2026-02~2026-06 |
| 데이터가 없는 캐릭터는 LoRA 를 만들 수 없다 — 갤부루·단부루에 자료가 비어 있으면 학습 데이터셋을 못 모으기 때문이다. 제작자들도 데이터셋이 없는 작품 요청은 거절했다 | 6 | 0 | 2025-03~2026-07 |
| 2026년 Illustrious·SDXL·ANIMA 계열의 퀄리티 태그 관례는 masterpiece, best quality, highres, absurdres 를 프롬프트 앞머리에 두는 것이다 | 6 | 0 | 2026-02~2026-07 |
| 이 캐릭터 LoRA 시리즈 제작자들이 참고한 학습 가이드는 학습채널(hypernetworks)의 https://arca.live/b/hypernetworks/110021224 (포리x 개정판) 이다 — 질문자가 https://arca.live/b/hypernetworks/84182575 를 짚었을 때 원글쓴이가 그게 아니라고 정정해 주었다 | 6 | 0 | 2025-05~2025-08 |
| 통합팩 출력물은 설치폴더\ComfyUI\output\날짜 에, 중간 과정은 그 아래 WIP 폴더에 저장된다 | 6 | 0 | 2026-02~2026-08 |
| NovelAI 계열 가중치 문법은 1.2::태그, 태그:: 형식이고 음수도 되어 -1::tears, bags under eyes:: 처럼 원치 않는 요소를 억제한다 | 5 | 0 | 2026-02~2026-08 |
| NoobAI·V-pred 계열 체크포인트는 Kohya Deep Shrink·DCW·Spectrum 가속 노드와 상성이 나쁘므로 하나씩 바이패스해 원인을 찾는다 | 5 | 0 | 2026-05~2026-08 |
| 캐릭터의 신체·고유 특징 태그(뿔·눈 색·머리 색·가슴 크기 등)는 캡션에서 지워야 그 특징이 캐릭터의 일부로 흡수되어 항상 따라 나오고, 태그를 남기면 학습기가 '태그로 지정된 별도 요소'로 인식해 매번 프롬프트에 그 태그를 적어야 한다 | 5 | 0 | 2023-02~2026-06 |
| 통합팩의 Controlnet Mode Select 값은 1=일반, 2=컨트롤넷 오픈포즈, 3=리저널이며 ANIMA 워크플로우는 1=일반, 2=컨트롤넷이다 | 5 | 0 | 2026-05~2026-08 |
| ANIMA는 Base v1.0을 models\diffusion_models, 텍스트 인코더를 models\text_encoders(qwen_3_06b_base.safetensors 로 개명), VAE를 models\vae 에 넣는다 | 5 | 0 | 2026-05~2026-08 |
| ComfyUI-Image-Manager 는 2026-03 에 CoNAI(cksdnfas/CoNAI)로 이름을 바꾸며 프론트엔드를 새로 만들었고, 26.4.5~26.5.17 을 거치며 NAI Vibe/Reference 저장, NAI 와 ComfyUI 설정을 모듈로 조합하는 워크플로우, rgthree Power Lora Loader 지원이 들어갔다 (실행 후 localhost:1677, 빌드 후 localhost:1666) | 5 | 0 | 2026-02~2026-05 |
| 해상도 프리셋은 Illustrious/SDXL은 custom_nodes\ComfyUi_NakoNode\py\aspect_ratio.py, ANIMA는 custom_nodes\comfyui-kjnodes\custom_dimensions.json 에서 수정한다 | 5 | 0 | 2026-05~2026-08 |
| ANIMA 작가 태그는 반드시 @ 로 시작하며, 단부루 등록명이 aaaaa_bbb 이면 @aaaaa bbb 로 적는다 | 5 | 0 | 2026-02~2026-07 |
| ANIMA 캐릭터 LoRA 는 의상·장식·특이한 눈동자·문신이 제대로 구현되지 않을 가능성이 높다고 제작자가 미리 고지한다. | 5 | 0 | 2026-05~2026-06 |
| SDXL 계열 기본 권장 체크포인트는 WAI-illustrious-SDXL 이며 설치폴더\ComfyUI\models\checkpoints 에 넣는다 | 5 | 0 | 2026-02~2026-08 |
| 트리거 워드·권장 가중치·학습 파라미터(epoch, repeat, learning rate, dim)를 적지 않은 LoRA 배포글은 재현이 어렵다 — 채널에서도 그 수치만 풀어도 참고가 크게 된다는 지적이 반복해서 나왔다 | 5 | 0 | 2023-02~2026-07 |
| 기존 ComfyUI의 모델 폴더는 Add-Ons\Easy-Models-Linker.bat 로 연결하거나 extra_model_paths.yaml 을 복사해 공유한다 | 5 | 0 | 2026-02~2026-08 |

## 출처

본문은 아카라이브에 있다. 여기서는 링크만 건다.

- [모델모음 공유링크(카멜리아, Exp 등)](https://arca.live/b/aiart/72189422) — 2023-03, 추천 103
- [신기능) 대기열 확장 - Agent Scheduler](https://arca.live/b/aiart/77750798) — 2023-06, 추천 95
- [내가 쓰려고 만든 태그 모음 노션](https://arca.live/b/aiart/140790436) — 2025-06, 추천 92
- [태그 종류](https://arca.live/b/aiart/61336136) — 2022-10, 추천 90
- [preview 및 출처 정리된 LoRa 111개 공유 (씹덕위주) + LoRa 많을때 팁](https://arca.live/b/aiart/70646351) — 2023-02, 추천 88
- [AI 그림 뉴비를 위한 내비게이션](https://arca.live/b/aiart/71132324) — 2023-03, 추천 84
- [내가 쓰려고 만드는 NAI용 그림체 프리셋 저장글](https://arca.live/b/aiart/132727305) — 2025-03, 추천 80
- [프롬프트 서치 사이트 공유](https://arca.live/b/aiart/125254725) — 2025-01, 추천 79
- [블루 아카이브 컷씬(?) 그림체 로라 배포](https://arca.live/b/aiart/145720807) — 2025-08, 추천 79
- [컨트롤넷 초보 기본 사용법 (Openpose, 전처리기 종류, 설정값, 멀티 컨트롤넷)](https://arca.live/b/aiart/80881919) — 2023-07, 추천 75
- [포함) V4용 여러가지 작가 태그/화풍/프리셋 저장글](https://arca.live/b/aiart/130458775) — 2025-03, 추천 75
- [ComfyUI 기초학개론의 집필이 완료되었습니다.](https://arca.live/b/aiart/109722465) — 2024-06, 추천 71
- [157색 컬러코드 임베딩 공유](https://arca.live/b/aiart/70343512) — 2023-02, 추천 65
- [야스 체위 관련 정보 사이트](https://arca.live/b/aiart/152506261) — 2025-11, 추천 65
- [최근 연달아 업데이트 한 EXIF 뷰어 기능 소개함](https://arca.live/b/aiart/70916246) — 2023-03, 추천 63
- [여러가지 꽤 쓸만했던 로라들 링크](https://arca.live/b/aiart/137644242) — 2025-05, 추천 63
- [노벨 시뮬레이터 NOVS 0.7](https://arca.live/b/aiart/163625321) — 2026-02, 추천 60
- [Danbooru 프롬프트 도우미](https://arca.live/b/aiart/174228063) — 2026-06, 추천 60
- [ai 그챈 nai 탭 념글 긁은 데이터셋 20240909~20250524](https://arca.live/b/aiart/137717097) — 2025-05, 추천 58
- [[병합대회] MIX-Pro-V4_Beta](https://arca.live/b/aiart/70413762) — 2023-02, 추천 57
- [web ui 이미지편집툴 확장 (Photopea)](https://arca.live/b/aiart/76270877) — 2023-05, 추천 57
- [뉴비용 로컬 기초서 공유](https://arca.live/b/aiart/132819559) — 2025-04, 추천 57
- [NAI) 개인 프롬 저장해둔 html 파일 공유 260311](https://arca.live/b/aiart/163685712) — 2026-03, 추천 56
- [아니마 심플하면서 제대로쓰기](https://arca.live/b/aiart/171770463) — 2026-05, 추천 56
- [일주일동안 만든 로라 결산 (모음집 업데이트)](https://arca.live/b/aiart/70704280) — 2023-02, 추천 55
- [웹툰) 별이삼샵 설효림 로라 공유](https://arca.live/b/aiart/140762910) — 2025-06, 추천 55
- [ai 뮤직 넌 미쳤다 @@추가 정보 있음](https://arca.live/b/aiart/64778052) — 2022-12, 추천 54
- [웹툰 캐릭터 Lora 공유) 히어로 킬러](https://arca.live/b/aiart/141649376) — 2025-07, 추천 54
- [일단 허깅 돌면서 적당히 쓸만해보이는 lora들 주워옴](https://arca.live/b/aiart/68188770) — 2023-01, 추천 53
- [Kaloscope2.0 아티스트 스타일 분류, 예측 모델](https://arca.live/b/aiart/153259226) — 2025-11, 추천 53
- [외부 ai exif사이트](https://arca.live/b/aiart/165668485) — 2026-03, 추천 53
- [코이카츠 3D 스크린샷만으로 2D 캐릭터 학습](https://arca.live/b/aiart/127423265) — 2025-01, 추천 52
- [스압)마법천자문 캐릭터 7명 IL 로라 CivitAI에 올림](https://arca.live/b/aiart/132320391) — 2025-03, 추천 51
- [웹툰 Lora 공유함 동아리 백가인](https://arca.live/b/aiart/136255690) — 2025-05, 추천 51
- [qiandaiyiyu 그림체 로라 배포](https://arca.live/b/aiart/144192001) — 2025-08, 추천 51
- [프롬프트(Exif) 추출 유저스크립트](https://arca.live/b/aiart/70755960) — 2023-02, 추천 50
- [태그 + 실제 테스트 결과 이미지 1편 (작화, 초점, 가족, 직업, 체형)](https://arca.live/b/aiart/62521936) — 2022-11, 추천 49
- [개량한복 로라](https://arca.live/b/aiart/75964340) — 2023-05, 추천 48
- [CIVITAI 에서 로컬 그림체를 찾는법 ( 똑같이 따라했는데도 다르게 나오는 이유가 뭘까? )](https://arca.live/b/aiart/147183795) — 2025-09, 추천 48
- [단부루 기반 AI 이미지 프롬프트 생성기.HTML](https://arca.live/b/aiart/169288451) — 2026-04, 추천 47
- [NAI 그림체 제작 보조 프로그램](https://arca.live/b/aiart/177316727) — 2026-07, 추천 47
- [Comfyui portable v0.30.0 + sage 외 여러가지.](https://arca.live/b/aiart/178800540) — 2026-08, 추천 47
- [아니마 B1.0 그림체 로라 만든거 2개 공유](https://arca.live/b/aiart/170817757) — 2026-05, 추천 46
- [그림체변경 유의미한 특정작품 프롬 모음 v1.2](https://arca.live/b/aiart/63524889) — 2022-11, 추천 45
- [LORA EXPLORER 3.4 (LyCORIS)](https://arca.live/b/aiart/75634149) — 2023-05, 추천 45
- [2026년 4월 입문자용 정보글 모음집](https://arca.live/b/aiart/167283401) — 2026-04, 추천 45
- [뉴비들은 webui neo 쓰자](https://arca.live/b/aiart/176802949) — 2026-07, 추천 44
- [로라 얼굴만, LoRA Block Weight 사용방법](https://arca.live/b/aiart/71644460) — 2023-03, 추천 42
- [챈에서 nai 짤 프롬 확인하는법](https://arca.live/b/aiart/94872564) — 2023-12, 추천 42
- [주요 업데이트: Automatic1111 Photoshop Stable Diffusion 플러그인 V1.2.0](https://arca.live/b/aiart/71190958) — 2023-03, 추천 41
- [웹툰) 한예나 v2](https://arca.live/b/aiart/140973650) — 2025-06, 추천 41
- [트릭컬 스탠딩 sd 스타일 로라 공유](https://arca.live/b/aiart/165287857) — 2026-03, 추천 41
- [Comfyui portable v0.22.0 + sage + triton.](https://arca.live/b/aiart/171586136) — 2026-05, 추천 41
- [후방) 가슴 크기에 관한 연구 (시각자료 있음)](https://arca.live/b/aiart/62652820) — 2022-11, 추천 39
- [미연시 등 게임 캐릭터 에셋 만들때 쓰기 좋은 sd-webui 확장: ABG remover](https://arca.live/b/aiart/67056410) — 2023-01, 추천 39
- [ai 그챈 nai 탭 념글 긁은 긴?급  데이터셋](https://arca.live/b/aiart/139830572) — 2025-06, 추천 39
- [웹툰 캐릭터 Lora 공유) 킬러경찰](https://arca.live/b/aiart/142253313) — 2025-07, 추천 39
- [K-버츄얼 그림체 로라 공유](https://arca.live/b/aiart/145274862) — 2025-08, 추천 39
- [ComfyUI-DCW 노드_쓰면그림이 이뻐져요!](https://arca.live/b/aiart/168389657) — 2026-04, 추천 39
- [로컬 채팅 프로그램 [AI 미연시] v0.6 공유](https://arca.live/b/aiart/169251837) — 2026-04, 추천 39
- [마참내 병합성공한 그림체 로라 공유](https://arca.live/b/aiart/177903059) — 2026-07, 추천 39
- [EasyVtuber 원클릭 설치 실행](https://arca.live/b/aiart/72459574) — 2023-03, 추천 38
- [WD14 Auto Prompt Generator - img2prompt (버전1)](https://arca.live/b/aiart/141451403) — 2025-07, 추천 38
- [아니마 가능)싹싹 긁어 모은 개인용 와일드카드 팩](https://arca.live/b/aiart/162850344) — 2026-02, 추천 38
- [Comfyui portable v0.31.0 + sage 외 여러가지.](https://arca.live/b/aiart/179342860) — 2026-08, 추천 38
- [내가 보려고 만든 작가 모음집](https://arca.live/b/aiart/134253509) — 2025-04, 추천 36
- [comfyui portable v0.20.1 + sage + triton.](https://arca.live/b/aiart/169293039) — 2026-04, 추천 36
- [아니마용 그림체 로라 개선판 공유](https://arca.live/b/aiart/178144808) — 2026-07, 추천 36
- [anima모델용 그림체(996)모음 사이트](https://arca.live/b/aiart/161801344) — 2026-02, 추천 35
- [단부루 태그 복사기 유저스크립트](https://arca.live/b/aiart/164343331) — 2026-03, 추천 35
- [Compy image viewer 깃헙에 공개함](https://arca.live/b/aiart/164672367) — 2026-03, 추천 35
- [Konomi: AI 생성 이미지 검색/관리/(자동)생성 앱](https://arca.live/b/aiart/165583236) — 2026-03, 추천 35
- [아니마 그림체 로라 공유](https://arca.live/b/aiart/177882714) — 2026-07, 추천 35
- [output용량이 걱정인 사람들에게 : JPG 포맷](https://arca.live/b/aiart/69024480) — 2023-02, 추천 34
- [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  차해인｜에실 라디르｜지나｜한세미｜한송이](https://arca.live/b/aiart/136191062) — 2025-05, 추천 34
- [웹툰 Lora 공유) 아카데미에서 살아남기 로르텔 케헬른｜루시 메이릴｜메릴다｜페니아 엘리어스 클로엘｜타냐 로스테일러｜예니카 페일로버｜아델 세리스](https://arca.live/b/aiart/138135282) — 2025-05, 추천 34
- [ComfyUI 워크플로우 공모전 마무리 및 수상자 발표](https://arca.live/b/aiart/143116458) — 2025-07, 추천 34
- [Qwen-Image-Edit-2511 vs FireRed-Image-Edit](https://arca.live/b/aiart/162479433) — 2026-02, 추천 34
- [스압)아니마 커스텀 믹스 로라 공유](https://arca.live/b/aiart/176513464) — 2026-07, 추천 34
- [주워옴 섹스 관련 태그 모음](https://arca.live/b/aiart/67516417) — 2023-01, 추천 33
- [웹툰 Lora 공유) 현실퀘스트 최민혜｜현진서｜제니｜주아린｜김청월｜김예나｜시연](https://arca.live/b/aiart/140055598) — 2025-06, 추천 33
- [웹툰 캐릭터 Lora 공유) 별이삼샵 설효림, 김다슬](https://arca.live/b/aiart/142923442) — 2025-07, 추천 33
- [웹툰 캐릭터 Lora 공유) 놀이감](https://arca.live/b/aiart/145481603) — 2025-08, 추천 33
- [한요일 올인원 로라 업뎃](https://arca.live/b/aiart/172772627) — 2026-06, 추천 33
- [아 한복 로라 누가 공유해줬네](https://arca.live/b/aiart/69440453) — 2023-02, 추천 32
- [웹툰 Lora 공유) 전지적 독자 시점 정희원｜이지혜｜민지원｜셀레나 킴｜신유승｜우리엘｜유상아](https://arca.live/b/aiart/139333927) — 2025-06, 추천 32
- [웹툰 캐릭터 Lora 공유) 정글쥬스](https://arca.live/b/aiart/144042734) — 2025-08, 추천 32
- [로리캐 로라 만든다고 시빗 밴먹은 기념 모델 덤프트럭](https://arca.live/b/aiart/149271136) — 2025-09, 추천 32
- [30분내로 끝내는 Vast.ai 사용법 (시간당 0.3$로 로컬굴리기)](https://arca.live/b/aiart/158013422) — 2025-12, 추천 32
- [NAIA2.0 버전 150 - 이벤트 프리셋](https://arca.live/b/aiart/163344011) — 2026-02, 추천 32
- [Comfyui portable v0.26.0 + sage 외 여러가지](https://arca.live/b/aiart/175163102) — 2026-06, 추천 32
- [애니메이션 캐릭터 Lora 공유) 새로구미(여구미)](https://arca.live/b/aiart/136921678) — 2025-05, 추천 31
- [웹툰 캐릭터 Lora 공유) 2회차 환관이 남성을 되찾음](https://arca.live/b/aiart/155204071) — 2025-11, 추천 31
- [[미니 정보] 26년 5월 기준 간단하게 소개하는 그림 AI 모델들](https://arca.live/b/aiart/169601993) — 2026-05, 추천 31
- [Nai 사용자를 위한 자세 모음 1편](https://arca.live/b/aiart/91985399) — 2023-11, 추천 30
- [배경용 와일드카드 모음](https://arca.live/b/aiart/77728087) — 2023-06, 추천 29
- [[로라공유] lora_arcain (ilxl 베이스)](https://arca.live/b/aiart/119240181) — 2024-10, 추천 29
- [내가 쓰려고 만든 작가 태그 모음집 C](https://arca.live/b/aiart/134461713) — 2025-04, 추천 29
- [웹툰 캐릭터 Lora 공유) 모르는 여자랑 하라구요?](https://arca.live/b/aiart/144614023) — 2025-08, 추천 29
- [필독) AI그림 채널 정보글 모음](https://arca.live/b/aiart/70255821) — 2023-02, 추천 28
- [웹툰 Lora 공유) 동아리  이예린｜박다영｜박세윤｜전재희｜송연우｜유은희](https://arca.live/b/aiart/137508828) — 2025-05, 추천 28
- [웹툰 캐릭터 Lora 공유) 모비딕](https://arca.live/b/aiart/143481842) — 2025-07, 추천 28
- [코믹바벨 상업지 10주년 화보 작가 모음](https://arca.live/b/aiart/143644384) — 2025-07, 추천 28
- [웹툰 캐릭터 Lora 공유) 저 그런 인재 아닙니다](https://arca.live/b/aiart/156388159) — 2025-12, 추천 28
- [웹툰 캐릭터 Lora 공유) 파브르 in 사천당가](https://arca.live/b/aiart/157461151) — 2025-12, 추천 28
- [Z-image 애니메 파인튜닝 Z-Anime](https://arca.live/b/aiart/169161957) — 2026-04, 추천 28
- [단부루 기반 AI 이미지 작가 태그 생성기.HTML](https://arca.live/b/aiart/169546100) — 2026-05, 추천 28
- [아니마 디테일 트위커 로라 나왔음.](https://arca.live/b/aiart/170584706) — 2026-05, 추천 28
- [[꼭 다시 받기4]누가 공유 요청해서 올리는 단부루 검색 툴 v1.0.6](https://arca.live/b/aiart/178778143) — 2026-08, 추천 28
- [웹툰 Lora 공유) 동아리  안지영｜백가인｜한나리｜강수연｜김가을](https://arca.live/b/aiart/137475690) — 2025-05, 추천 27
- [웹툰 Lora 공유) 이세계 밀프 헌터 아리엘라 레이븐｜벨리타 그레이스｜칼리사｜세실리아｜피오나 아렌테](https://arca.live/b/aiart/140473932) — 2025-06, 추천 27
- [웹툰 LoRA 공유) 우리 길드 아이돌 - 배아진](https://arca.live/b/aiart/147279963) — 2025-09, 추천 27
- [웹툰 캐릭터 Lora 공유) 회귀한 용병은 다 계획이 있다](https://arca.live/b/aiart/155693668) — 2025-12, 추천 27
- [한애니 캐릭터들 만든 로라 공유](https://arca.live/b/aiart/165664117) — 2026-03, 추천 27
- [LTX2.3 lora 몇개 공유](https://arca.live/b/aiart/173653906) — 2026-06, 추천 27
- [요가 자세 포즈 몇 개 만든거 공유 (컨트롤넷)](https://arca.live/b/aiart/71112036) — 2023-03, 추천 26
- [[NAI?] 짱깨 사이트 엑셀 저장한 것](https://arca.live/b/aiart/117689806) — 2024-10, 추천 26
- [청아) 도라에몽 극장판 철인병단 리루루 로라 만들었음 (+공유)](https://arca.live/b/aiart/127342012) — 2025-01, 추천 26
- [웹툰 캐릭터 Lora 공유) 퀘스트지상주의  백채린｜엘리사｜김다현｜이지현｜양소하｜연서희](https://arca.live/b/aiart/136525702) — 2025-05, 추천 26
- [웹툰 캐릭터 Lora 공유) 입학용병](https://arca.live/b/aiart/142870110) — 2025-07, 추천 26
- [1girl, solo짤멍용 3+4종 풀랜덤 와일드카드](https://arca.live/b/aiart/166767807) — 2026-04, 추천 26
- [아니마 공식 해상도 개선 로라.](https://arca.live/b/aiart/167659142) — 2026-04, 추천 26
- [단부루 태그 + 그룹 + 번역 합본 DB 공유 26-05-02](https://arca.live/b/aiart/169460152) — 2026-05, 추천 26
- [NAIA 및 아니마 사용을 위한 Webui Forge Neo 포지네오 설치 가이드 (수정)](https://arca.live/b/aiart/170554328) — 2026-05, 추천 26
- [Anima 웹툰 캐릭터 Lora 공유) 아카데미에서 살아남기](https://arca.live/b/aiart/176619574) — 2026-07, 추천 26
- [브더느낌의 아니마 로라](https://arca.live/b/aiart/178293143) — 2026-07, 추천 26
- [[WebUI 기본 확장기능] 프롬프트 자동완성 tag-autocomplete](https://arca.live/b/aiart/70421901) — 2023-02, 추천 25
- [설화모음집 위키ver 끝](https://arca.live/b/aiart/73816109) — 2023-04, 추천 25
- [AI 이미지 갤러리 web버전 만듬](https://arca.live/b/aiart/155413135) — 2025-11, 추천 25
- [페) 농농단용 ANIMA/NAI 아티스트 와일드카드](https://arca.live/b/aiart/161289775) — 2026-02, 추천 25
- [아니아니마 고속고속마 품질비교마](https://arca.live/b/aiart/171972064) — 2026-05, 추천 25
- [Comfyui portable v0.23.0 + sage + grok i2v 외 여러가지](https://arca.live/b/aiart/172596107) — 2026-06, 추천 25
- [정발 Anima용 트릭컬 스타일 로라 공유](https://arca.live/b/aiart/172973086) — 2026-06, 추천 25
- [원하는 색을 만들어서 사용해보자(3) Embedding-inspector](https://arca.live/b/aiart/67003072) — 2023-01, 추천 24
- [이미지 파일에서 NAI 프롬프트(Exif)를 확인할 수 있는 간단한 프로그램 만들어옴](https://arca.live/b/aiart/94581185) — 2023-12, 추천 24
- [웹툰 Lora 공유) 광마회귀 공손월](https://arca.live/b/aiart/140540745) — 2025-06, 추천 24
- [웹툰 캐릭터 Lora 공유) 네크로맨서 학교의 소환천재](https://arca.live/b/aiart/154565123) — 2025-11, 추천 24
- [AI 생성 이미지 관리 앱 Konomi 0.13.x 업데이트](https://arca.live/b/aiart/166792754) — 2026-04, 추천 24
- [크퀘스타일 도트 로라 공유](https://arca.live/b/aiart/167362821) — 2026-04, 추천 24
- [개인적인 Anima+IL 워크플로우 세트 구성품 추천](https://arca.live/b/aiart/169680210) — 2026-05, 추천 24
- [로컬 AI 채팅 프로그램](https://arca.live/b/aiart/170019628) — 2026-05, 추천 24
- [Anima 웹툰 캐릭터 Lora 공유) 역대급 영지 설계사](https://arca.live/b/aiart/172324042) — 2026-05, 추천 24
- [NAIA 기능 가이드 모음 (260217)](https://arca.live/b/aiart/108288949) — 2024-06, 추천 23
- [웹툰 Lora 공유) 수요웹툰의 나강림  박정아｜홍 사장｜서은영｜선아별｜송유라｜유다희｜유나리](https://arca.live/b/aiart/137766502) — 2025-05, 추천 23
- [웹툰 Lora 공유) 전지적 독자 시점 아일렌 메이크필드｜아스모데우스｜아스카 렌｜한수영｜이설화｜이리스 블라지미로브나 레베제바｜장하영](https://arca.live/b/aiart/139326347) — 2025-06, 추천 23
- [웹툰 캐릭터 Lora 공유) 부패의 사제](https://arca.live/b/aiart/150271493) — 2025-10, 추천 23
- [블아 작가로라 2개](https://arca.live/b/aiart/167677263) — 2026-04, 추천 23
- [NAIA+외부 고해상도 이미지 수정 Extension 제작해서 공유해봄](https://arca.live/b/aiart/174711559) — 2026-06, 추천 23
- [Anima 웹툰 캐릭터 Lora 공유) 현실퀘스트](https://arca.live/b/aiart/175287930) — 2026-06, 추천 23
- [AI 이미지 EXIF 뷰어 - 드래그+드롭 업로드 EXIF 보존 지원](https://arca.live/b/aiart/76070805) — 2023-05, 추천 22
- [[Nai]내가 보려고 만든 작가 정보 24선](https://arca.live/b/aiart/94333373) — 2023-12, 추천 22
- [[NAI] 짱깨 AIFUN NAI 이미지 모음](https://arca.live/b/aiart/119314105) — 2024-10, 추천 22
- [내가 쓰려고 만든 NAI 작가 태그 모음집 0~A](https://arca.live/b/aiart/134331198) — 2025-04, 추천 22
- [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  서지우｜성진아｜시미즈 아카리｜타와타 카나에](https://arca.live/b/aiart/136376313) — 2025-05, 추천 22
- [웹툰 Lora 공유) 수요웹툰의 나강림  방예림｜차시린｜큐피트왕｜주라미｜권미야｜나민정](https://arca.live/b/aiart/137729551) — 2025-05, 추천 22
- [웹툰 Lora 공유) 아카데미에서 살아남기  엘리스｜아니스 헤일란｜아일라 트리스｜벨 마이아｜클레어 엘핀｜클라리스(카일리 에크네)](https://arca.live/b/aiart/138102033) — 2025-05, 추천 22
- [웹툰 Lora 공유) 사시미 한 자루로 아카데미를 씹어먹음  아벨 폰 니벨룽｜클로이 아디토레｜최설아｜메디아 포이즌｜레이첼 드 뮈라｜사키 료조](https://arca.live/b/aiart/138521652) — 2025-06, 추천 22
- [작가명 태그 썸네일 미리보기 뷰어 (30mb)](https://arca.live/b/aiart/139028012) — 2025-06, 추천 22
- [단부루 태그 총정리](https://arca.live/b/aiart/140170773) — 2025-06, 추천 22
- [Anima GGUF 양자화 모델](https://arca.live/b/aiart/161385741) — 2026-02, 추천 22
- [LTX 2.3 테스트중인 로라 하나 추천](https://arca.live/b/aiart/173213921) — 2026-06, 추천 22
- [직접 만든 여성 의상 -8-](https://arca.live/b/aiart/175557540) — 2026-07, 추천 22
- [Anima 게임 캐릭터 Lora 공유) 화이트데이](https://arca.live/b/aiart/175617365) — 2026-07, 추천 22
- [[제작] Exif AI 프롬 확인 프로그램 :: v2.3.4 [메인]](https://arca.live/b/aiart/83667711) — 2023-08, 추천 21
- [Nai 사용자를 위한 자세 모음 2](https://arca.live/b/aiart/91988777) — 2023-11, 추천 21
- [Nai 사용자를 위한 자세 모음 4](https://arca.live/b/aiart/91997326) — 2023-11, 추천 21
- [※ 프롬프트 서치 사이트 업데이트 내용  25.01.04](https://arca.live/b/aiart/125471599) — 2025-01, 추천 21
- [애니 캐릭터 Lora 공유) 나 혼자만 레벨업  하네카와｜이보라｜이주희｜박희진](https://arca.live/b/aiart/136373651) — 2025-05, 추천 21
- [웹툰 Lora) 이 시국에 개인교습 - 주연 3인방](https://arca.live/b/aiart/138627507) — 2025-06, 추천 21
- [WD14 Auto Prompt Generator (버전2) -> NAI API 적용](https://arca.live/b/aiart/141522681) — 2025-07, 추천 21
- [EXIF 뷰어 3.0 html 제작 (완)](https://arca.live/b/aiart/160704184) — 2026-01, 추천 21
- [(NAI) 아티스트 셔플기 ver.0.02](https://arca.live/b/aiart/164687273) — 2026-03, 추천 21
- [Anima 찍먹해보기 - 아니마 체크포인트, 로라 다운로드](https://arca.live/b/aiart/171506089) — 2026-05, 추천 21
- [Anima 웹툰 캐릭터 Lora 공유) 나 혼자 특성빨로 무한 성장](https://arca.live/b/aiart/171699762) — 2026-05, 추천 21
- [이것저것 만든 LoRA 모음집 공유](https://arca.live/b/aiart/68474447) — 2023-01, 추천 20
- [웹툰 Lora 공유) 일진담당일진  백수지｜이사임｜미도리카와 요코｜오춘심｜서지인](https://arca.live/b/aiart/137557622) — 2025-05, 추천 20
- [웹툰 Lora) 성인웹툰 속 엑스트라가 되었다 - 주연 3인 + 조연 1인](https://arca.live/b/aiart/139125184) — 2025-06, 추천 20
- [야밤에 업뎃한 프롬프트분류기(추가)](https://arca.live/b/aiart/143463834) — 2025-07, 추천 20
- [웹툰 캐릭터 Lora 공유) 인턴해녀](https://arca.live/b/aiart/146809624) — 2025-09, 추천 20
- [Anima 컨셉 Lora 공유) 하이그레 자세와 의상](https://arca.live/b/aiart/171864098) — 2026-05, 추천 20
- [Comfy의 이미지에 말풍선을 추가하는 커스텀노드](https://arca.live/b/aiart/174020000) — 2026-06, 추천 20
- [뒤죽박죽 섞인 그림들의 이름을 일괄로 정리해보자](https://arca.live/b/aiart/67989854) — 2023-01, 추천 19
- [hiro 스타일(아케비의 세일러복 작가) LORA 공유](https://arca.live/b/aiart/71891910) — 2023-03, 추천 19
- [ai 모델 이상형 월드컵(최대 511개), 다른 월드컵까지  최종본](https://arca.live/b/aiart/72227415) — 2023-03, 추천 19
- [웹툰 캐릭터 Lora 공유) 초인의 게임  대사제｜백하연｜이나연｜여왕｜사니야 아흐메토바｜슈란](https://arca.live/b/aiart/136828343) — 2025-05, 추천 19
- [웹툰) 치즈인더트랩 로라 공유](https://arca.live/b/aiart/139739277) — 2025-06, 추천 19
- [웹툰) 지겹다 지겨워! 또왔다 한예나로라 공유](https://arca.live/b/aiart/144186702) — 2025-08, 추천 19
- [웹툰 캐릭터 Lora 공유) 일렉시드](https://arca.live/b/aiart/147768075) — 2025-09, 추천 19
- [ANIMA 아니마용 단부루 자동완성 csv](https://arca.live/b/aiart/161315560) — 2026-02, 추천 19
- [로컬 comfyui 찍먹해보기 - 컨트롤넷을 사용한 인페인팅/아웃페인팅](https://arca.live/b/aiart/162809080) — 2026-02, 추천 19
- [브더2 느낌의 amima 로라](https://arca.live/b/aiart/165231841) — 2026-03, 추천 19
- [체크포인트 2개 추천 [JANKU 사용자한테 추천]](https://arca.live/b/aiart/165778645) — 2026-03, 추천 19
- [NAIA2.0용 Anima 아티스트 썸네일 60000 및 뷰어 HTML](https://arca.live/b/aiart/170828753) — 2026-05, 추천 19
- [아니마로 NAI 그림체 만들어본거 공유](https://arca.live/b/aiart/173054724) — 2026-06, 추천 19
- [Comfy로 anima 실행 및 최적화하기](https://arca.live/b/aiart/175408089) — 2026-06, 추천 19
- [Anzhc/AAAAnima not so early](https://arca.live/b/aiart/176018707) — 2026-07, 추천 19
- [SDXL(ILXL) 컨트롤넷 모델 정보](https://arca.live/b/aiart/122545929) — 2024-11, 추천 18
- [오픈 포즈 공유](https://arca.live/b/aiart/135095099) — 2025-04, 추천 18
- [웹툰 캐릭터 Lora 공유) 신과함께 돌아온 기사왕님](https://arca.live/b/aiart/146268794) — 2025-08, 추천 18
- [(페도) 넷플릭스 힐다 Kelly Marra 로라 공유](https://arca.live/b/aiart/148357981) — 2025-09, 추천 18
- [웹툰로라) 한예나](https://arca.live/b/aiart/164851217) — 2026-03, 추천 18
- [NAI 자동생성 앱 (NAIApp) v1.4.0](https://arca.live/b/aiart/168830995) — 2026-04, 추천 18
- [NAI 프롬프트 작성 / 관리 / 이미지 생성까지 한큐에 되는 [NAI Helper] v1.1 업데이트](https://arca.live/b/aiart/170686312) — 2026-05, 추천 18
- [anima 파인튜닝해본 모델](https://arca.live/b/aiart/170997672) — 2026-05, 추천 18
- [noobai팀이 만든거) Anima Tile & Repair LLLite](https://arca.live/b/aiart/174094973) — 2026-06, 추천 18
- [말풍선 감지해서 대사 채워넣는 워크플로우](https://arca.live/b/aiart/175373331) — 2026-06, 추천 18
- [나만 쓰던 그림체 로라 공유함](https://arca.live/b/aiart/175489941) — 2026-07, 추천 18
- [Anima 웹툰 캐릭터 Lora 공유) 아카데미에 위장취업당했다](https://arca.live/b/aiart/178038139) — 2026-07, 추천 18
- [아니마 그림체 사이트](https://arca.live/b/aiart/179093581) — 2026-08, 추천 18
- [설화 모음집 만들어옴](https://arca.live/b/aiart/72707563) — 2023-03, 추천 17
- [NAI 이미지 태그 뷰어 업뎃된거 알고있었움? (with webui)](https://arca.live/b/aiart/133417496) — 2025-04, 추천 17
- [그냥 학습시킨 떡신 로라 3개 공유입니다](https://arca.live/b/aiart/134371628) — 2025-04, 추천 17
- [웹툰) 동아리-박다영 (로라 공유)](https://arca.live/b/aiart/135221703) — 2025-04, 추천 17
- [게임 캐릭터 Lora 공유) 화이트데이: 학교라는 이름의 미궁 (2017.ver)  한소영｜김성아｜설지현｜유지민](https://arca.live/b/aiart/137118271) — 2025-05, 추천 17
- [(페도) 넷플릭스 힐다 Twintails Marra 로라 공유](https://arca.live/b/aiart/148268845) — 2025-09, 추천 17
- [트릭컬 스타일 로라 공유](https://arca.live/b/aiart/169478146) — 2026-05, 추천 17
- [NAI풍 아니마 로라 공유](https://arca.live/b/aiart/171228963) — 2026-05, 추천 17
- [NAI 자동생성 앱 (NAIApp) v1.5.1 핫픽스](https://arca.live/b/aiart/176933271) — 2026-07, 추천 17
- [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 우유연｜박나영｜박나미](https://arca.live/b/aiart/135573919) — 2025-05, 추천 16
- [애니 캐릭터 Lora 공유) 귀환자의 마법은 특별해야 합니다  아제스트 킹스크라운｜브리지이트｜로맨티카 에루](https://arca.live/b/aiart/135848518) — 2025-05, 추천 16
- [[캐릭터 LoRA공유] ilxl베이스의 사죠 마나카 lora 공유](https://arca.live/b/aiart/147745539) — 2025-09, 추천 16
- [썻던정보글모음집](https://arca.live/b/aiart/158172868) — 2025-12, 추천 16
- [Detailer / Enhancer용 11개 + 피부 광택 6개 + 눈 개선 3개 Lora 비교](https://arca.live/b/aiart/159981349) — 2026-01, 추천 16
- [Anima 로라 사용 후기 + 링크](https://arca.live/b/aiart/163664637) — 2026-03, 추천 16
- [NAI 스타일 로라 v5 공유](https://arca.live/b/aiart/164149050) — 2026-03, 추천 16
- [kohya가만든 anima용 lineart ControlNet-LLLite](https://arca.live/b/aiart/168801930) — 2026-04, 추천 16
- [Circlestone Labs 공식 anima-rl-v0.1 로라 테스트](https://arca.live/b/aiart/169414949) — 2026-05, 추천 16
- [ddsd 옵션 업데이트(필수X)(약스압 주의)](https://arca.live/b/aiart/74090707) — 2023-04, 추천 15
- [[미르코][38장]강력한 미르미르코](https://arca.live/b/aiart/76765824) — 2023-05, 추천 15
- [Nai 사용자를 위한 자세 모음 3](https://arca.live/b/aiart/91992716) — 2023-11, 추천 15
- [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 강안나｜구혜리｜최나나](https://arca.live/b/aiart/135389458) — 2025-04, 추천 15
- [왕자림 x 이경우 NTR 로라 공유](https://arca.live/b/aiart/135597261) — 2025-05, 추천 15
- [고어, 페도, 스압주의) 고어작가 로라 몇개 (ILXL)](https://arca.live/b/aiart/136124750) — 2025-05, 추천 15
- [@@@스캇주의@@@ 스캇_IL로라 공유](https://arca.live/b/aiart/137226294) — 2025-05, 추천 15
- [NAIA-WEB-Lite를 이용하여 웹에서 쉽게 랜덤태그 생성하기](https://arca.live/b/aiart/160107104) — 2026-01, 추천 15
- [프리큐어 캐릭터 태그 html 공유](https://arca.live/b/aiart/163071111) — 2026-02, 추천 15
- [ANIMA 눈이 이뻐지는 로라](https://arca.live/b/aiart/169512883) — 2026-05, 추천 15
- [webui 랜덤해상도 및 반복생성 스크립트](https://arca.live/b/aiart/122055428) — 2024-11, 추천 14
- [웹툰 Lora) 쓰리엑스라지러브(3XLOVE) - 천보경](https://arca.live/b/aiart/153703989) — 2025-11, 추천 14
- [스타일 LoRA) Hechima (issindotai) 스타일](https://arca.live/b/aiart/153935164) — 2025-11, 추천 14
- [ANIMA 아니마용 아티스트 와일드카드](https://arca.live/b/aiart/162852234) — 2026-02, 추천 14
- [아니마 공식 퀄리티 개선 로라](https://arca.live/b/aiart/169264526) — 2026-04, 추천 14
- [ANIMA 로라: alllisso 그림체](https://arca.live/b/aiart/170685979) — 2026-05, 추천 14
- [Anima 컨셉 Lora 공유) 기어스 눈 (기어스에 걸린 사람)](https://arca.live/b/aiart/171229773) — 2026-05, 추천 14
- [프롬프트 매니저 업데이트](https://arca.live/b/aiart/173045392) — 2026-06, 추천 14
- [ANIMA용 잼민이 gems](https://arca.live/b/aiart/176216501) — 2026-07, 추천 14
- [미니맥스 속도 캐싱 3종세트 안되는 사람들](https://arca.live/b/aiart/179226965) — 2026-08, 추천 14
- [NAIA - 작가 스타일 분류 가이드 (testv23b)](https://arca.live/b/aiart/121061032) — 2024-11, 추천 13
- [[Q6_K]Smooth Mix Wan I2V high+Low + DaSiWa WAN Lightspeed RadiantCrush Low](https://arca.live/b/aiart/151608989) — 2025-10, 추천 13
- [Anima용 트릭컬 스타일 로라 공유](https://arca.live/b/aiart/169486310) — 2026-05, 추천 13
- [하지만 빨랐죠? 자작 아니마 4스텝 로라 업데이트](https://arca.live/b/aiart/176518628) — 2026-07, 추천 13
- [허접한 AnimaYumeV02 용 LoRA 공유함](https://arca.live/b/aiart/164800666) — 2026-03, 추천 12
- [귀찮은 사람들을 위한 NotebookLM 노트북 공유](https://arca.live/b/aiart/169269240) — 2026-04, 추천 12
- [ANIMA LoRA: NAI 스타일 콜렉션 1편](https://arca.live/b/aiart/170929440) — 2026-05, 추천 12
- [ANIMA 메이플 썬콜 로라 공유](https://arca.live/b/aiart/176777447) — 2026-07, 추천 12
- [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 윤대리｜오희정｜강지혜](https://arca.live/b/aiart/135304065) — 2025-04, 추천 10
- [웹툰, Webtoon 캐릭터 Lora 공유) 섹톱워치 유정원｜윤민영](https://arca.live/b/aiart/135646986) — 2025-05, 추천 10
- [에픽세븐-신월의루나 캐릭터 로라 공유](https://arca.live/b/aiart/126126545) — 2025-01, 추천 9
- [고어, 이상성욕) 방금만든 손발 삽입로라 공유](https://arca.live/b/aiart/134892006) — 2025-04, 추천 9
- [간단하게 AV 커버 만들 수 있는 사이트](https://arca.live/b/aiart/153101276) — 2025-11, 추천 9
- [Anima-INT8Rowwise 모델](https://arca.live/b/aiart/163367034) — 2026-02, 추천 9
- [[윈도우탐색기에서 프롬프트 간편 복사기] ~ 8.7.아침까지 유효링크](https://arca.live/b/aiart/176179807) — 2026-07, 추천 9
- [[모델공유] (요청) 롱 믹스 (링크 수정)](https://arca.live/b/aiart/74350978) — 2023-04, 추천 8
- [Exif AI 프롬 확인 프로그램 2.3.4 버전 업글 [서브]](https://arca.live/b/aiart/99531580) — 2024-02, 추천 8
- [(noob-vpred) tirotata style lora 공유](https://arca.live/b/aiart/126429473) — 2025-01, 추천 8
- [personaStyle_Ilxl10Noob 모델 기준 작가 태그별 그림체](https://arca.live/b/aiart/130266214) — 2025-03, 추천 8
- [코믹 메이플 캐릭터 로라 2종(아르웬, 라케니스)](https://arca.live/b/aiart/134271092) — 2025-04, 추천 8
- [내가 쓰려고 만든 작가 태그 모음집 B](https://arca.live/b/aiart/134455790) — 2025-04, 추천 8
- [프롬프트 분류기 업데이트+멀티코어추가](https://arca.live/b/aiart/151098701) — 2025-10, 추천 8
- [런팟 RTX 5090용 WAN 2.2 딸깍 도커 이미지](https://arca.live/b/aiart/151440980) — 2025-10, 추천 8
- [ComfyUI Image Manager v3.0.0-alpha + MCP](https://arca.live/b/aiart/162063293) — 2026-02, 추천 8
- [GPT(덕테이프), 나노바나나 이미지 프롬 사이트 모음](https://arca.live/b/aiart/168949757) — 2026-04, 추천 8
- [단부루 기반 AI 이미지 프롬프트 생성기 개조 버전](https://arca.live/b/aiart/169490491) — 2026-05, 추천 8
- [[anima] 원본+int8 convrot 모델 3종 비교](https://arca.live/b/aiart/177372687) — 2026-07, 추천 8
- [하지만 빨랐죠? 자작 4스텝 로라 또? 업데이트](https://arca.live/b/aiart/177849905) — 2026-07, 추천 8
- [원신도 붕스도 아닌 별 거 없는 로라 조합](https://arca.live/b/aiart/177985468) — 2026-07, 추천 8
- [아니마 그림체 로라 공유](https://arca.live/b/aiart/178524790) — 2026-07, 추천 8
- [아니마 그림체 로라 만들어둔거 공유](https://arca.live/b/aiart/179776875) — 2026-08, 추천 8
- [미라화,거미줄 lora 입니다](https://arca.live/b/aiart/70195871) — 2023-02, 추천 7
- [동방프로젝트 첸,오린,쇼,미케 LoRA 모델](https://arca.live/b/aiart/71116117) — 2023-03, 추천 7
- [무직전생 아이샤 그레이렛 LoRA](https://arca.live/b/aiart/77356160) — 2023-05, 추천 7
- [에픽세븐 캐릭터 로라 공유 (신월의 루나, 월광 벨로나, 잔비, 월광 화영)](https://arca.live/b/aiart/146053426) — 2025-08, 추천 7
- [nai 그림체 테스트하는 페이지 공유](https://arca.live/b/aiart/161192747) — 2026-02, 추천 7
- [사이버 경로당 노인이 만든 NAI 2006-2015 애니 캐릭 모음집](https://arca.live/b/aiart/163615724) — 2026-02, 추천 7
- [한요일의 이원진 로라 쪄왔음](https://arca.live/b/aiart/164820596) — 2026-03, 추천 7
- [NAI 이미지 자동 분류 및 뷰어 v3.11 (26/04/14 수정)](https://arca.live/b/aiart/166787538) — 2026-04, 추천 7
- [[인외,몬무스,퍼리] Kusayarou 그림체 로라 공유](https://arca.live/b/aiart/167861783) — 2026-04, 추천 7
- [CoNAI 26.5.17 업데이트](https://arca.live/b/aiart/170932905) — 2026-05, 추천 7
- [nai+로컬 태그뷰어 업뎃](https://arca.live/b/aiart/171745343) — 2026-05, 추천 7
- [아니아니마용 작가 조합 테스트웹](https://arca.live/b/aiart/171805357) — 2026-05, 추천 7
- [[anima, 페, 할] 연령 조절 슬라이더 로라](https://arca.live/b/aiart/174677230) — 2026-06, 추천 7
- [Danbooru 프롬프트 도우미 MCP 서버](https://arca.live/b/aiart/174935283) — 2026-06, 추천 7
- ["버니니 다시왔네" 제작법 및 초간단 후기 (역양자화 파이선 스크립트 공유 - 링크7일만료)](https://arca.live/b/aiart/175630790) — 2026-07, 추천 7
- [웹툰,페) 수희0 - 조수정 아니마 로라](https://arca.live/b/aiart/177767092) — 2026-07, 추천 7
- [Lora 공유) 갸루에게 상냥한 오타쿠 군 - 나루미 유우아이](https://arca.live/b/aiart/138283386) — 2025-05, 추천 6
- [[워크플로우 공모전] 라면보다 쉽다! 간편 종합 워크플로우 - 종합 개선 업데이트 1.4 버전](https://arca.live/b/aiart/141991828) — 2025-07, 추천 6
- [클로저스 비나 로라](https://arca.live/b/aiart/142890947) — 2025-07, 추천 6
- [채신기법으로 anima lora 학습시켜봄 (2)](https://arca.live/b/aiart/165954535) — 2026-03, 추천 6
- [CoNai 26.4.15 업뎃 챈섭?기능 추가](https://arca.live/b/aiart/167738002) — 2026-04, 추천 6
- [AI 생성 이미지 관리 앱 Konomi 0.14.x 업데이트](https://arca.live/b/aiart/168139677) — 2026-04, 추천 6
- [프롬프트 분류기 업뎃](https://arca.live/b/aiart/169675680) — 2026-05, 추천 6
- [DaSiWa - Anima](https://arca.live/b/aiart/170910843) — 2026-05, 추천 6
- [(수정)이미지 프롬 수정프로그램 / 이미지 프롬 읽는 Node (comfyui용)](https://arca.live/b/aiart/177982416) — 2026-07, 추천 6
- [이미지 태그 분류 프로그램 TagMetaUpdater](https://arca.live/b/aiart/72075853) — 2023-03, 추천 5
- [VRChat 인기 아바타 카린, 마후유 로라 배포](https://arca.live/b/aiart/153368473) — 2025-11, 추천 5
- [맥북으로 exif 프롬 리더 필요한사람?](https://arca.live/b/aiart/166644059) — 2026-04, 추천 5
- [CoNAI 26.4.5 버전 업데이트](https://arca.live/b/aiart/166831098) — 2026-04, 추천 5
- [아니마 연령 조절 로라](https://arca.live/b/aiart/170858259) — 2026-05, 추천 5
- [ANIMA 농농한 그림체 스타일 로라](https://arca.live/b/aiart/171208757) — 2026-05, 추천 5
- [프롬프트 분류기 해상도별분류 및 일부기능개선](https://arca.live/b/aiart/171554343) — 2026-05, 추천 5
- [라데온 sageattention whl로 만들어왔어](https://arca.live/b/aiart/179413848) — 2026-08, 추천 5
- [사소한거)딥단부루 태그 변환 파이썬파일임](https://arca.live/b/aiart/69903265) — 2023-02, 추천 4
- [스케어리 캠퍼스 칼리지 유니버시티 - 치가라시 마히나 로라 공유](https://arca.live/b/aiart/139055598) — 2025-06, 추천 4
- [Civitai 필터 설정](https://arca.live/b/aiart/139808399) — 2025-06, 추천 4
- [ゴア gore 작가 스타일 로라 공유 게시](https://arca.live/b/aiart/155353897) — 2025-11, 추천 4
- [니케 영문명 와일드카드](https://arca.live/b/aiart/161378127) — 2026-02, 추천 4
- [CoNAI로 변경된 이미지+영상관리 시스템 ㅠ](https://arca.live/b/aiart/165939813) — 2026-03, 추천 4
- [같은 모델 다르게 쓰는 법](https://arca.live/b/aiart/171170750) — 2026-05, 추천 4
- [아니마용 2048 로라](https://arca.live/b/aiart/171203636) — 2026-05, 추천 4
- [CoNAI 26.5.23 업데이트](https://arca.live/b/aiart/171558427) — 2026-05, 추천 4
- [방송 플랫폼 데이터셋 확보용 확장](https://arca.live/b/aiart/173312863) — 2026-06, 추천 4
- [그록을 활용한 NAI 프롬프트 생성기 만드는 법](https://arca.live/b/aiart/174034886) — 2026-06, 추천 4
- [python 2일차 chatgpt로 만든 deepdanbooru 이용 SFW, NSFW 분류기(ver 1.1)](https://arca.live/b/aiart/71895663) — 2023-03, 추천 3
- [colab으로 VLM을 실행해보자.](https://arca.live/b/aiart/161842488) — 2026-02, 추천 3
- [CoNai 26.4.20 업뎃](https://arca.live/b/aiart/168222915) — 2026-04, 추천 3
- [comfyview 업데이트](https://arca.live/b/aiart/168888732) — 2026-04, 추천 3
- [AI 생성 이미지 관리 앱 Konomi 0.15.x 업데이트](https://arca.live/b/aiart/171481122) — 2026-05, 추천 3
- [이미지 모자이크/블러 필터 추가 프로그램](https://arca.live/b/aiart/172341784) — 2026-05, 추천 3
- [첸돚거 그림체 커스텀+기타 개인 설정세팅값 자료](https://arca.live/b/aiart/174789689) — 2026-06, 추천 3
- [(사지절단 주의) Mi-Ke 로라](https://arca.live/b/aiart/71028103) — 2023-03, 추천 2
- [독학한 컨트롤넷 그림(+ 포즈 공유)](https://arca.live/b/aiart/72773785) — 2023-03, 추천 2
- [NAI-Auto-Generator v4.5 (비공식) 업데이트 (06/28)](https://arca.live/b/aiart/174988734) — 2026-06, 추천 2
- [ANIMA) 수영복 키사키 (수사키, 수키키) 로라](https://arca.live/b/aiart/175182246) — 2026-06, 추천 2
- [nai로 뽑은 사진 배경제거 광고 안 보고 하는 법 (렌파이까지 배경제거 검증 완료)](https://arca.live/b/aiart/175979369) — 2026-07, 추천 2
- [ComfyUI에서 Muse Glimmer 찍어 먹어보기](https://arca.live/b/aiart/179575129) — 2026-08, 추천 2
- [프롬프트 분류기 와일드카드 지원 및 이스케이프 처리개선](https://arca.live/b/aiart/173039358) — 2026-06, 추천 1
- [산란) GPT ai 그림 입문 3주간 템플릿을 한 캐릭터에게 적용해 보았다](https://arca.live/b/aiart/179117331) — 2026-08, 추천 1
- [로컬 ai라는걸 오늘 처음 안 늅늅이 질문](https://arca.live/b/aiart/175410884) — 2026-06, 추천 0