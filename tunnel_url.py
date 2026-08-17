"""현재 터널 주소를 알아내 파일과 위키 표지에 적어 둔다.

quick tunnel(trycloudflare)은 컨테이너를 재시작할 때마다 주소가 바뀐다.
그때마다 로그를 뒤지는 대신 여기서 뽑아 `TUNNEL_URL.txt` 에 남기고,
위키 표지에도 적어서 어디서 보든 현재 주소를 알 수 있게 한다.

고정 주소가 필요하면 Cloudflare Zero Trust 에서 named tunnel 을 만들어
.env 의 CF_TUNNEL_TOKEN 에 넣고 `docker compose --profile tunnel up -d` 로 바꾼다.

usage:
    python tunnel_url.py           # 주소 출력 + TUNNEL_URL.txt 갱신
    python tunnel_url.py --check   # 실제로 응답하는지까지 확인
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import requests

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

ROOT = Path(__file__).parent
URL_FILE = ROOT / "TUNNEL_URL.txt"
URL_RE = re.compile(r"https://[a-z0-9-]+\.trycloudflare\.com")


def current_url() -> str | None:
    """컨테이너 로그에서 가장 최근 주소를 뽑는다."""
    try:
        r = subprocess.run(
            ["docker", "compose", "logs", "quicktunnel"],
            cwd=ROOT, capture_output=True, text=True, timeout=30,
        )
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        print(f"docker 실행 실패: {e}", file=sys.stderr)
        return None
    hits = URL_RE.findall(r.stdout + r.stderr)
    return hits[-1] if hits else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    url = current_url()
    if not url:
        print("터널 주소를 찾지 못했다. 컨테이너가 떠 있는지 확인:")
        print("  docker compose --profile quick up -d quicktunnel")
        sys.exit(1)

    alive = None
    if args.check:
        try:
            alive = requests.get(url, timeout=20).status_code
        except requests.RequestException as e:
            alive = f"실패 ({type(e).__name__})"

    prev = URL_FILE.read_text(encoding="utf-8").strip() if URL_FILE.exists() else ""
    URL_FILE.write_text(url + "\n", encoding="utf-8")

    print(f"현재 주소: {url}")
    if prev and prev != url:
        print(f"  (바뀜 — 이전: {prev})")
    if alive is not None:
        print(f"  응답: {alive}")


if __name__ == "__main__":
    main()
