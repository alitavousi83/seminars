# -*- coding: utf-8 -*-
"""Stitch rendered previews into contact sheets for quick visual QA."""
import os, sys, glob
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "preview")
OUT = os.path.join(HERE, "assets", "out")
COLS, ROWS = 4, 4
TW, TH = 400, 225


def main(prefix="slide", cols=COLS, rows=ROWS):
    os.makedirs(OUT, exist_ok=True)
    files = sorted(glob.glob(os.path.join(SRC, prefix + "-*.png")))
    if not files:
        print("no previews; run render.py first")
        return
    per = cols * rows
    for page in range((len(files) + per - 1) // per):
        chunk = files[page * per:(page + 1) * per]
        sheet = Image.new("RGB", (cols * TW, rows * TH), (245, 241, 232))
        d = ImageDraw.Draw(sheet)
        for i, f in enumerate(chunk):
            im = Image.open(f).convert("RGB").resize((TW - 4, TH - 4), Image.LANCZOS)
            x, y = (i % cols) * TW + 2, (i // cols) * TH + 2
            sheet.paste(im, (x, y))
            d.rectangle([x, y, x + TW - 4, y + TH - 4], outline=(17, 17, 17))
            d.text((x + 6, y + 4), os.path.basename(f), fill=(200, 255, 0))
        out = os.path.join(OUT, "sheet-%02d.png" % (page + 1))
        sheet.save(out)
        print("saved", out, len(chunk), "slides")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "slide")
