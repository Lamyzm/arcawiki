"""재료층 추출기 — LLM 없이 정규식으로 프롬프트 자산을 긁는다.

왜 필요한가:
  기존 파이프라인은 한 글을 카드 1장(중앙 1,062자)으로 요약한다. 1만자 넘는 글의
  보존율이 7%인데, 작가 대조표와 태그 사전이 정확히 그 구간에 몰려 있다.
  감사 실측: 원문 작가 737명 중 위키에 96명, EXIF 덤프 168건 중 1건,
  태그 사전형 글 109건에 든 태그 54,627개 중 위키 생존율 10%.
  「직접 만든 여성 의상」 시리즈는 의상 563벌·태그 9,390개가 settings 76~209자로
  압축되면서 `"전문": "원문 참조 (분량이 매우 김)"` 한 줄이 됐다.

  판단 규칙은 잘 정리돼 있는데(작가 조합 50항목, 얼굴 해상도 28항목) 그 규칙을
  실행할 재료가 없는 상태다. 작가 태그·로라 호출·가중치·EXIF 는 전부 모양이
  정해져 있어 판단이 필요 없다. 그러니 요약하지 말고 원문 그대로 받는다.
  LLM 을 안 쓰므로 전 글에 돌릴 수 있다.

usage:
    python extract_assets.py                     # 무엇이 잡히는지 세어만 본다
    python extract_assets.py --apply
    python extract_assets.py --apply --since 2026-01-01
"""

import re
import sys
from decimal import Decimal, InvalidOperation

import queue_api as q

sys.stdout.reconfigure(encoding="utf-8")

CTX = 90                 # 거동 주석("이 작가는 눈을 뭉갠다")을 같이 잡기 위한 문맥 폭
BLOCK_MIN_COMMAS = 5
LABEL_MAX = 40           # 태그 줄 바로 위의 짧은 줄을 이름으로 본다

# --- 작가 표기 세 가지 ---------------------------------------------------
# 채널은 세 문법을 섞어 쓴다. 하나만 보면 3분의 1만 잡힌다.
AT = re.compile(
    r"\(?@([A-Za-z][A-Za-z0-9 _.\-\\()']{1,38}?)\s*"
    r"(?::\s*([0-9]*\.?[0-9]+))?\)?(?=[\s,)\]]|$)")
# 이름을 최소 매칭으로 두면 뒤가 전부 선택적이라 `artist:chamchami` 에서 `ch` 만 잘린다.
# 탐욕 매칭으로 바꾸되, 공백이 이름에 허용되므로 다음 `artist:` 를 넘어가지 않게 막는다.
COLON = re.compile(
    r"\(?\s*artist:\s*([A-Za-z](?:(?!\s*artist:)[A-Za-z0-9 _.\-\\()']){1,38})"
    r"(?:\s*:\s*(-?[0-9]*\.?[0-9]+))?")
NAI = re.compile(r"(-?[0-9]*\.?[0-9]+)\s*::\s*([^:]{2,60}?)\s*::")

LORA = re.compile(r"<lora:([^:>]{1,60}?):(-?[0-9]*\.?[0-9]+)(?::(-?[0-9]*\.?[0-9]+))?>")
WTAG = re.compile(r"\(([^():]{2,60}?):\s*(-?[0-9]*\.?[0-9]+)\)")
SAFET = re.compile(r"([A-Za-z0-9._\-]{3,80}\.(?:safetensors|ckpt|gguf|pt))")
RESO = re.compile(r"\b(\d{3,4})\s*[xX*×]\s*(\d{3,4})\b")

SAMPLERS = (
    "euler_ancestral", "euler a", "euler", r"dpm\+\+ 2m sde", r"dpm\+\+ 2m", r"dpm\+\+ sde",
    "dpmpp_2m_sde", "dpmpp_2m", "dpmpp_sde", "uni_pc", "unipc", "lcm", "ddim", "heun",
    "restart", "res_multistep", "sgm_uniform", "sgm uniform", "karras", "exponential",
    "beta", "simple", "normal", "ipndm", "deis")
SAMPLER = re.compile(r"\b(" + "|".join(SAMPLERS) + r")\b", re.I)

STEPS = re.compile(r"(?:steps?|스텝|스탭)\s*[:=]?\s*(\d{1,3})\b", re.I)
CFG = re.compile(r"(?:cfg(?:\s*scale)?)\s*[:=]?\s*(\d{1,2}(?:\.\d)?)\b", re.I)
SEED = re.compile(r"\bseed\s*[:=]\s*(-?\d{1,20})", re.I)

EXIF = re.compile(r"Steps:\s*\d+.{0,400}?Sampler:", re.I | re.S)
FENCE = re.compile(r"```(.*?)```", re.S)

# 실제 작가명이 아닌 것. 예시 자리표시자와 흔한 오탐.
JUNK = {
    "artist", "artist_name", "artistname", "name", "aaa", "bbb", "ccc", "xxx", "yyy",
    "abc", "test", "here", "your", "nai", "sd", "webui", "comfyui", "lora", "http",
    "https", "www", "gmail", "com", "png", "jpg", "jpeg", "safetensors"}


def clean(nm):
    nm = (nm or "").strip().strip(",.;:").strip()
    return re.sub(r"\s{2,}", " ", nm).lower()


def ok_artist(nm):
    if len(nm) < 2 or nm in JUNK:
        return False
    if not re.search(r"[a-z]", nm):
        return False
    return not re.fullmatch(r"[0-9.\-_ ]+", nm)


def num(s):
    try:
        return Decimal(s)
    except (InvalidOperation, TypeError):
        return None


def ctx(text, i, j):
    return re.sub(r"\s+", " ", text[max(0, i - CTX): j + CTX]).strip()


def scan(text):
    """텍스트 한 덩어리에서 (kind, raw, name, weight, syntax, context) 를 뽑는다."""
    out = []
    if not text:
        return out

    for m in AT.finditer(text):
        nm = clean(m.group(1))
        if ok_artist(nm):
            out.append(("artist", m.group(0).strip(), nm, num(m.group(2)), "at",
                        ctx(text, *m.span())))
    for m in COLON.finditer(text):
        nm = clean(m.group(1))
        if ok_artist(nm):
            out.append(("artist", m.group(0).strip(), nm, num(m.group(2)), "artist_colon",
                        ctx(text, *m.span())))
    # NAI 의 `n::태그::` 는 작가 전용 문법이 아니라 모든 가중치 태그가 쓰는 문법이다.
    # `1.2::lowres::` 를 작가로 잡으면 품질 태그가 작가 목록을 덮는다.
    # 안쪽이 `artist:` 나 `@` 로 시작할 때만 작가로 본다.
    for m in NAI.finditer(text):
        inner = m.group(2).strip()
        w = num(m.group(1))
        pre = re.match(r"(?:artist:|@)\s*(.+)$", inner, re.I)
        if pre:
            nm = clean(pre.group(1))
            if ok_artist(nm):
                out.append(("artist", m.group(0).strip(), nm, w, "nai_colons",
                            ctx(text, *m.span())))
        else:
            nm = clean(inner)
            if nm and "," not in nm:
                out.append(("weighted_tag", m.group(0).strip(), nm, w, "nai_colons",
                            ctx(text, *m.span())))

    for m in LORA.finditer(text):
        out.append(("lora", m.group(0), clean(m.group(1)), num(m.group(2)), "angle",
                    ctx(text, *m.span())))
    for m in WTAG.finditer(text):
        nm = clean(m.group(1))
        if nm and not nm.startswith(("artist:", "@")):
            out.append(("weighted_tag", m.group(0), nm, num(m.group(2)), "paren",
                        ctx(text, *m.span())))
    for m in SAFET.finditer(text):
        out.append(("model_file", m.group(1), clean(m.group(1)), None, "exif",
                    ctx(text, *m.span())))
    for m in RESO.finditer(text):
        w, h = int(m.group(1)), int(m.group(2))
        if 256 <= w <= 4096 and 256 <= h <= 4096:
            out.append(("resolution", m.group(0), "%dx%d" % (w, h), None, "exif",
                        ctx(text, *m.span())))
    for m in SAMPLER.finditer(text):
        out.append(("sampler", m.group(0), clean(m.group(1)), None, "exif",
                    ctx(text, *m.span())))
    for m in STEPS.finditer(text):
        n = int(m.group(1))
        if 1 <= n <= 200:
            out.append(("steps", m.group(0), str(n), Decimal(n), "exif", ctx(text, *m.span())))
    for m in CFG.finditer(text):
        out.append(("cfg", m.group(0), m.group(1), num(m.group(1)), "exif", ctx(text, *m.span())))
    for m in SEED.finditer(text):
        out.append(("seed", m.group(0), m.group(1), None, "exif", ctx(text, *m.span())))
    return out


def _label_for(lines, i):
    """태그 줄 바로 위의 짧은 줄을 이름으로 본다.

    「직접 만든 여성 의상」 시리즈가 `타탄 스쿨 사이렌` / `grey cropped cardigan, ...`
    형태라서, 이름을 안 잡으면 태그 줄만 남고 무슨 옷인지 모르게 된다.
    """
    for k in range(i - 1, max(-1, i - 4), -1):
        s = lines[k].strip()
        if not s:
            continue
        if len(s) <= LABEL_MAX and s.count(",") < 2:
            return s
        return None
    return None


def blocks(text):
    """자르면 안 되는 덩어리 — 태그 나열과 EXIF 덤프를 통째로 잡는다."""
    out = []
    if not text:
        return out
    seen = set()

    def add(role, body, label=None):
        body = body.strip()
        if len(body) < 40 or body in seen:
            return
        seen.add(body)
        n_art = len({a[2] for a in scan(body) if a[0] == "artist"})
        out.append((role, body, label, n_art, body.count(",")))

    for m in EXIF.finditer(text):
        add("exif", text[max(0, m.start() - 600): min(len(text), m.end() + 900)])

    for m in FENCE.finditer(text):
        if m.group(1).count(",") >= BLOCK_MIN_COMMAS:
            add("tag_list", m.group(1))

    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.count(",") >= BLOCK_MIN_COMMAS and len(line) >= 60:
            low = line.lower()
            role = "negative" if re.search(r"negative|네거|부정", low) else "tag_list"
            add(role, line, _label_for(lines, i))
    return out


def main():
    apply = "--apply" in sys.argv
    since = sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv else None

    n_post = n_asset = n_block = 0
    kinds, roles = {}, {}

    with q._conn() as c, c.cursor() as cur:
        if since:
            cur.execute("SELECT id, body, posted_at::date d FROM posts WHERE posted_at >= %s ORDER BY id",
                        (since,))
        else:
            cur.execute("SELECT id, body, posted_at::date d FROM posts ORDER BY id")
        rows = cur.fetchall()
        print("대상 원문 %d건%s" % (len(rows), " (since %s)" % since if since else ""))

        cur.execute("SELECT post_id, seq, body FROM comments")
        cmts = {}
        for r in cur.fetchall():
            cmts.setdefault(r["post_id"], []).append((r["seq"], r["body"]))

        for r in rows:
            n_post += 1
            for seq, body in [(None, r["body"])] + cmts.get(r["id"], []):
                for kind, raw, name, w, syn, cx in scan(body):
                    kinds[kind] = kinds.get(kind, 0) + 1
                    n_asset += 1
                    if apply:
                        cur.execute(
                            "INSERT INTO prompt_assets"
                            " (post_id, comment_seq, kind, raw, name, weight, syntax, context, posted_at)"
                            " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                            (r["id"], seq, kind, raw[:400], name, w, syn, cx[:600], r["d"]))
                for role, b, label, na, nc in blocks(body):
                    roles[role] = roles.get(role, 0) + 1
                    n_block += 1
                    if apply:
                        cur.execute(
                            "INSERT INTO prompt_blocks"
                            " (post_id, comment_seq, role, body, label, n_artists, n_commas, posted_at)"
                            " VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                            (r["id"], seq, role, b[:20000], label, na, nc, r["d"]))
            if apply and n_post % 400 == 0:
                c.commit()
                print("  %d/%d …" % (n_post, len(rows)))
        if apply:
            c.commit()

    print("\n원문 %d · 자산 %d · 블록 %d" % (n_post, n_asset, n_block))
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print("  %-14s %7d" % (k, v))
    print("  --- 블록")
    for k, v in sorted(roles.items(), key=lambda x: -x[1]):
        print("  %-14s %7d" % (k, v))
    if not apply:
        print("\n실제로 넣으려면 --apply")


if __name__ == "__main__":
    main()
