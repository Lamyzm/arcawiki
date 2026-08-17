"""카드의 software/models 표기를 개체로 정규화한다.

원문 표기가 제각각이라 (Wan 2.2 / WAN2.2 / WAN, rgthree / rgthree-comfy)
그대로 두면 같은 것이 여러 문서로 쪼개진다. 별칭을 여기 한곳에 모아 둔다.

멱등이다. 카드가 늘어날 때마다 다시 돌리면 된다.

usage:
    python normalize_entities.py          # 정규화 후 통계
    python normalize_entities.py --list   # 미분류로 남은 표기 확인
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata

import queue_api as q

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

# (정규명, 종류, 별칭들)
# 별칭 비교는 소문자·공백/하이픈/언더바 제거 후 이뤄지므로 대소문자만 다른 것은 안 적어도 된다.
ENTITIES: list[tuple[str, str, list[str]]] = [
    # ── 실행 환경 ──────────────────────────────────────────────
    ("ComfyUI", "software", ["컴피", "comfy"]),
    ("ComfyUI Manager", "software", []),
    ("Stable Diffusion WebUI", "software", ["webui", "sd-webui", "forge"]),
    ("Wan2GP", "software", []),
    ("comfy-kitchen", "software", []),
    ("CoNAI", "software", []),

    # ── 가속·최적화 ────────────────────────────────────────────
    ("SageAttention", "software", ["sage attention", "sage"]),
    ("Triton", "software", []),
    ("xformers", "software", []),
    ("FlashAttention", "software", []),
    ("PyTorch", "software", ["torch"]),

    # ── 커스텀 노드 ────────────────────────────────────────────
    ("KJNodes", "node", ["comfyui-kjnodes", "kj nodes"]),
    ("rgthree", "node", ["rgthree-comfy", "rgthrees comfyui nodes"]),
    ("MiniMaxH3-Cache", "node", ["comfyui-minimaxh3-cache", "minimaxh3 cache", "h3-cache"]),
    ("negpip", "node", []),
    ("Autocomplete Plus", "node", ["autocomplete plus", "tag-autocomplete", "autocomplete"]),
    ("ComfyUI-GGUF", "node", ["gguf loader"]),
    ("ComfyUI Impact Pack", "node", ["impact pack"]),
    ("UltimateSDUpscale", "node", ["ultimate sd upscale"]),
    ("efficiency-nodes-ED", "node", ["efficiency nodes extended"]),
    ("ComfyUI-SUPIR", "node", ["supir"]),
    ("ComfyUi_NakoNode", "node", ["nakonode"]),
    ("comfyui-ollama", "node", []),
    ("Easy-Models-Linker", "node", []),

    # ── 영상 모델 ──────────────────────────────────────────────
    # 이 말뭉치에서 'WAN' 단독은 사실상 Wan 2.2 를 가리킨다.
    ("Wan 2.2", "model", ["wan2.2", "wan", "wan22"]),
    ("MiniMax H3", "model", ["minimax", "미니맥스", "minimaxh3", "h3"]),
    ("MiniMax-H3-Turbo-Lora", "model", ["h3 turbo lora", "터보로라"]),
    # LTX-2 와 LTX 2.3 은 세대가 다르지만, 이 말뭉치의 'LTX' 단독은 2.3 맥락이다.
    ("LTX 2.3", "model", ["ltx-2.3", "ltx2.3", "ltx", "ltx-2", "ltx2"]),
    ("LTX2.3-10Eros", "model", []),
    ("Seedance 2.0", "model", ["seedance", "시댄스"]),
    ("Seedance 1.5", "model", []),
    ("Sora 2", "model", ["sora"]),
    ("SVI", "model", []),

    # ── 이미지 모델 ────────────────────────────────────────────
    ("ANIMA", "model", ["아니마"]),
    ("SDXL", "model", []),
    ("Illustrious", "model", ["il", "ilxl", "일러스트리어스"]),
    ("WAI-illustrious-SDXL", "model", ["wai"]),
    ("FLUX", "model", []),
    ("Qwen Image", "model", ["qwen image edit", "qwen"]),
    ("NovelAI", "model", ["nai", "노벨ai"]),
    ("GPT-Image-2.0", "model", ["gpt image"]),
    ("Bernini", "model", []),
    ("나노바나나", "model", ["nano banana", "나노바나나"]),
    ("Grok", "model", ["grok cli"]),

    # ── 보조 모델 ──────────────────────────────────────────────
    ("SeedVR2", "model", ["seedvr", "seed vr"]),
    ("SAM3.1", "model", ["sam3", "sam 3"]),
    ("lightx2v", "model", ["lightx2v_i2v_14b_480p_cfg_step_distill_rank128_bf16"]),
    ("ControlNet", "model", ["controlnet-union-sdxl-1.0", "control-lora-depth-rank256",
                             "noobai-xl-controlnet-openpose", "noobai inpainting controlnet",
                             "openposexl2"]),
    ("BiRefNet", "model", ["birefnet general", "comfyui_birefnet_ll"]),
    ("Ollama", "software", ["qwen3-vl-abliterated:8b-instruct"]),

    # ── 서비스 ─────────────────────────────────────────────────
    ("Dreamina", "service", ["dreamina.capcut.com", "jimeng"]),
    ("Civitai", "service", ["시비타이"]),
]


def key(text: str) -> str:
    """비교용 정규화. 대소문자·공백·구분자 차이를 없앤다."""
    t = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"[\s_\-./]+", "", t)


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKC", name).lower()
    s = re.sub(r"[^\w가-힣]+", "-", s).strip("-")
    return s or "entity"


def build_lookup() -> dict[str, tuple[str, str]]:
    """별칭 → (정규명, 종류)"""
    out: dict[str, tuple[str, str]] = {}
    for name, kind, aliases in ENTITIES:
        for a in [name, *aliases]:
            out[key(a)] = (name, kind)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="미분류 표기만 출력")
    args = ap.parse_args()

    lookup = build_lookup()

    with q._conn() as c, c.cursor() as cur:
        cur.execute("SELECT id, software, models FROM knowledge_cards")
        cards = cur.fetchall()

        # 미분류 확인
        unknown: dict[str, int] = {}
        for card in cards:
            for raw in [*card["software"], *card["models"]]:
                if key(raw) not in lookup:
                    unknown[raw] = unknown.get(raw, 0) + 1

        if args.list:
            print(f"미분류 표기 {len(unknown)}종")
            for raw, n in sorted(unknown.items(), key=lambda x: -x[1])[:40]:
                print(f"  {n:>3}  {raw}")
            return

        # 개체 등록 (멱등)
        ids: dict[str, int] = {}
        for name, kind, aliases in ENTITIES:
            cur.execute(
                """INSERT INTO entities (slug, name, kind, aliases)
                   VALUES (%s,%s,%s,%s)
                   ON CONFLICT (slug) DO UPDATE SET name=EXCLUDED.name,
                        kind=EXCLUDED.kind, aliases=EXCLUDED.aliases
                   RETURNING id""",
                (slugify(name), name, kind, aliases),
            )
            ids[name] = cur.fetchone()["id"]

        # 카드 ↔ 개체 연결. 다시 돌려도 중복되지 않는다.
        linked = 0
        for card in cards:
            seen: set[int] = set()
            for raw in [*card["software"], *card["models"]]:
                hit = lookup.get(key(raw))
                if not hit:
                    continue
                eid = ids[hit[0]]
                if eid in seen:
                    continue
                seen.add(eid)
                cur.execute(
                    """INSERT INTO card_entities (card_id, entity_id, role)
                       VALUES (%s,%s,'mentions') ON CONFLICT DO NOTHING""",
                    (card["id"], eid),
                )
                linked += 1
        c.commit()

        cur.execute("SELECT count(*) n FROM entities"); ents = cur.fetchone()["n"]
        cur.execute("SELECT count(*) n FROM card_entities"); links = cur.fetchone()["n"]

    print(f"개체 {ents}종 / 연결 {links}건 / 미분류 표기 {len(unknown)}종")
    print("\n[문서 후보 — 카드 3장 이상]")
    with q._conn() as c, c.cursor() as cur:
        # entity_candidates 뷰가 이미 name/kind 를 갖고 있어 조인이 필요 없다
        cur.execute("SELECT name, kind, cards, earliest, latest FROM entity_candidates LIMIT 22")
        for r in cur.fetchall():
            print(f"  {r['cards']:>3}장  {r['kind']:<8} {r['name']}  ({r['earliest']}~{r['latest']})")


if __name__ == "__main__":
    main()
