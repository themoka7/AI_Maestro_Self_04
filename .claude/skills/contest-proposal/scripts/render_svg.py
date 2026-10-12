"""SVG → PNG. 일러스트 에이전트가 그린 배치도·타임라인을 docx 에 넣기 위해 쓴다.

사용: python render_svg.py <in.svg> [out.png] [--scale 2]
cairosvg 가 있으면 쓰고, 없으면 Chrome/Edge/Chromium 헤드리스로 스크린샷한다.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BROWSERS = [
    "chromium", "chromium-browser", "google-chrome", "chrome", "msedge",
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]


def size_of(svg_text):
    m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', svg_text)
    if not m:
        sys.exit("SVG 에 viewBox 가 필요하다")
    return int(float(m.group(1))), int(float(m.group(2)))


def find_browser():
    for b in BROWSERS:
        p = shutil.which(b) or (b if os.path.exists(b) else None)
        if p:
            return p
    return None


def render(src, out, scale=2):
    text = Path(src).read_text(encoding="utf-8")
    w, h = size_of(text)
    try:
        import cairosvg
        cairosvg.svg2png(bytestring=text.encode(), write_to=str(out),
                         output_width=w * scale, output_height=h * scale)
        return
    except ImportError:
        pass
    browser = find_browser()
    if not browser:
        sys.exit("cairosvg 또는 Chrome/Edge/Chromium 이 필요하다")
    html = (f"<html><body style='margin:0'><div style='width:{w}px;height:{h}px'>"
            f"{text}</div></body></html>")
    with tempfile.TemporaryDirectory() as d:
        page = Path(d) / "p.html"
        page.write_text(html, encoding="utf-8")
        subprocess.run([browser, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", f"--force-device-scale-factor={scale}",
                        f"--window-size={w},{h}", f"--screenshot={Path(out).resolve()}",
                        page.as_uri()], check=True, capture_output=True)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--scale")]
    scale = 2
    for a in sys.argv[1:]:
        if a.startswith("--scale"):
            scale = int(a.split("=")[1]) if "=" in a else 2
    if not args:
        sys.exit("사용: python render_svg.py <in.svg> [out.png]")
    out = args[1] if len(args) > 1 else str(Path(args[0]).with_suffix(".png"))
    render(args[0], out, scale)
    print(out)
