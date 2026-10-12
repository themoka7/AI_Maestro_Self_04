"""out.docx → out.pdf + out-<n>.png (페이지별). 심사 에이전트가 '눈으로' 보는 용도.

사용: python preview.py <out.docx>
의존성: LibreOffice(soffice), poppler(pdftoppm)
"""
import shutil
import subprocess
import sys
from pathlib import Path


def main(docx):
    docx = Path(docx).resolve()
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        sys.exit("LibreOffice(soffice)가 필요하다")
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir",
                    str(docx.parent), str(docx)], check=True, capture_output=True)
    pdf = docx.with_suffix(".pdf")
    if shutil.which("pdftoppm"):
        subprocess.run(["pdftoppm", "-png", "-r", "80", str(pdf),
                        str(docx.with_suffix(""))], check=True)
    print(pdf)


if __name__ == "__main__":
    main(sys.argv[1])
