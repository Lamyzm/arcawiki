# -*- coding: utf-8 -*-
"""원본 PNG/mp4 에 박힌 생성 정보를 긁는다.

아카는 본문에 보이는 `ac.arca.live` 이미지를 WEBP 로 바꾸며 메타를 지우지만,
`<img data-originalurl="...ac-o.arca.live/...&type=orig">` 에 원본 PNG 링크가 살아 있다.
호스트만 바꿔 끼우면 403 이 난다 — 서명 키가 다르므로 반드시 이 속성값을 써야 한다.
"""
import json, re, struct, sys, psycopg
# 리다이렉트되면 파이썬이 블록 버퍼링으로 바뀌어 진행이 안 보인다.
sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
sys.path.insert(0, r"F:\Project\arcawiki")
import crawler, queue_api as q

ORIG = re.compile(r'data-originalurl="([^"]+)"')


def png_text(b):
    out = {}
    if b[:8] != b"\x89PNG\r\n\x1a\n":
        return out
    i = 8
    while i + 8 <= len(b):
        ln = struct.unpack(">I", b[i:i+4])[0]
        typ = b[i+4:i+8]
        if typ in (b"tEXt", b"iTXt"):
            k, _, v = b[i+8:i+8+ln].partition(b"\0")
            out[k.decode("latin1")] = v.decode("utf-8", "replace").lstrip("\0")
        if typ == b"IEND":
            break
        i += 12 + ln
    return out


def parse(meta):
    """NAI / ComfyUI / A1111 세 갈래를 한 모양으로 맞춘다."""
    if "Comment" in meta:                       # NovelAI
        try:
            c = json.loads(meta["Comment"])
        except Exception:
            return None
        return {"tool": "NovelAI", "model": meta.get("Source", ""),
                "prompt": c.get("prompt", ""), "negative": c.get("uc", ""),
                "steps": c.get("steps"), "cfg": c.get("scale"),
                "sampler": c.get("sampler"), "scheduler": c.get("noise_schedule"),
                "w": c.get("width"), "h": c.get("height"), "seed": c.get("seed")}
    if "parameters" in meta:                    # A1111
        p = meta["parameters"]
        neg = ""
        m = re.search(r"Negative prompt:(.*?)(?:\nSteps:|$)", p, re.S)
        if m:
            neg = m.group(1).strip()
        return {"tool": "A1111", "model": "", "prompt": p.split("Negative prompt:")[0].strip(),
                "negative": neg, "steps": None, "cfg": None, "sampler": None,
                "scheduler": None, "w": None, "h": None, "seed": None}
    if "prompt" in meta or "workflow" in meta:  # ComfyUI
        return {"tool": "ComfyUI", "model": "", "prompt": meta.get("prompt", "")[:8000],
                "negative": "", "steps": None, "cfg": None, "sampler": None,
                "scheduler": None, "w": None, "h": None, "seed": None}
    return None


def harvest(pids):
    S = crawler.session
    got = []
    for pid in pids:
        st, html = crawler.fetch("https://arca.live/b/aiart/%d" % pid)
        if st != "ok":
            print("  %d %s" % (pid, st)); continue
        urls = [u.replace("&amp;", "&") for u in ORIG.findall(html)]
        hit = None
        for u in urls[:4]:
            if not u.lower().split("?")[0].endswith(".png"):
                continue
            try:
                r = S.get(u, timeout=60, headers={"Referer": "https://arca.live/"})
            except Exception as e:
                print("   !", str(e)[:50]); continue
            if r.status_code != 200:
                continue
            d = parse(png_text(r.content))
            if d:
                hit = d; break
        if hit:
            hit["post_id"] = pid
            got.append(hit)
            print("  %d  %s  %s  %d자" % (pid, hit["tool"], hit["model"][:26], len(hit["prompt"])))
        else:
            print("  %d  메타 없음 (이미지 %d장)" % (pid, len(urls)))
        crawler.polite_sleep()
    return got


if __name__ == "__main__":
    crawler.load_cookie()
    c = psycopg.connect(q._dsn())
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    pids = [r[0] for r in c.execute(
        "SELECT id FROM posts WHERE image_count > 0 ORDER BY posted_at DESC LIMIT %s", (n,))]
    print("대상 %d개" % len(pids))
    got = harvest(pids)
    json.dump(got, open(r"F:\Project\arcawiki\harvest_meta.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\n%d/%d 건 확보 -> harvest_meta.json" % (len(got), len(pids)))
