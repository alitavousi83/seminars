# -*- coding: utf-8 -*-
"""Edge-bleed check on rendered previews (proxy for clipped layouts)."""
import os, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "preview")


def main():
    files = sorted(glob.glob(os.path.join(SRC, "slide-*.png")))
    rows = []
    for f in files:
        im = np.asarray(Image.open(f).convert("RGB").resize((480, 270)), dtype=np.float32)
        mean = im.mean()
        band = 3
        edges = np.concatenate([
            im[:band].reshape(-1, 3), im[-band:].reshape(-1, 3),
            im[:, :band].reshape(-1, 3), im[:, -band:].reshape(-1, 3),
        ])
        bg = np.array([245, 241, 232], dtype=np.float32)
        dev = np.abs(edges - bg).max(axis=1)
        frac = float((dev > 28).mean())
        rows.append((int(os.path.basename(f)[6:8]), round(mean, 0), round(frac, 3)))
    print("slide  mean  edge-ink")
    for n, m, fr in rows:
        flag = ""
        if m > 200 and fr > 0.20:
            flag = "  <-- check (light slide with edge ink)"
        print("%5d  %5.0f  %5.3f%s" % (n, m, fr, flag))


if __name__ == "__main__":
    main()
