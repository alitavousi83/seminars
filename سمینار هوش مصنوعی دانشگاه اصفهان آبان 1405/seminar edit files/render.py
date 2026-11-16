# -*- coding: utf-8 -*-
"""Render via PowerPoint: PNG previews + layout QA report."""
import os, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
import win32com.client as win32

HERE = os.path.dirname(os.path.abspath(__file__))


def main(path="test_deck.pptx"):
    path = os.path.abspath(path)
    outdir = os.path.join(HERE, "assets", "preview")
    os.makedirs(outdir, exist_ok=True)
    for f in glob.glob(os.path.join(outdir, "slide-*.png")):
        os.remove(f)
    app = win32.Dispatch("PowerPoint.Application")
    pres = app.Presentations.Open(path, WithWindow=False)
    total = pres.Slides.Count
    print("slides:", total)
    issues = []
    fonts = {}
    boxes = []
    for i in range(1, total + 1):
        sl = pres.Slides(i)
        sl.Export(os.path.join(outdir, "slide-%02d.png" % i), "PNG", 1600, 900)
        tboxes = []
        for sh in sl.Shapes:
            try:
                name = sh.Name
                if sh.HasTextFrame and sh.TextFrame.HasText:
                    tr = sh.TextFrame2.TextRange
                    bh = tr.BoundHeight
                    bw = tr.BoundWidth
                    if bh > sh.Height + 3:
                        issues.append((i, "overflow", name, round(bh - sh.Height, 1),
                                       tr.Text[:38].replace("\n", " "), round(sh.Height, 1)))
                    fn = tr.Font.NameComplexScript
                    fonts[fn] = fonts.get(fn, 0) + 1
                    tboxes.append((sh.Left, sh.Top, sh.Width, sh.Height, name, tr.Text[:30]))
            except Exception:
                pass
        for a in range(len(tboxes)):
            for b in range(a + 1, len(tboxes)):
                x1 = max(tboxes[a][0], tboxes[b][0]); y1 = max(tboxes[a][1], tboxes[b][1])
                x2 = min(tboxes[a][0] + tboxes[a][2], tboxes[b][0] + tboxes[b][2])
                y2 = min(tboxes[a][1] + tboxes[a][3], tboxes[b][1] + tboxes[b][3])
                if x2 > x1 and y2 > y1:
                    inter = (x2 - x1) * (y2 - y1)
                    small = min(tboxes[a][2] * tboxes[a][3], tboxes[b][2] * tboxes[b][3])
                    if small > 0 and inter / small > 0.30:
                        issues.append((i, "text-overlap", tboxes[a][4][:18] + " <> " + tboxes[b][4][:18],
                                       round(100 * inter / small, 0),
                                       tboxes[a][5] + " | " + tboxes[b][5], 0))
    pres.SaveAs(os.path.join(outdir, "preview.pdf"), 32)
    pres.Close()
    app.Quit()
    print("exported to", outdir)
    print("fonts (complex script):", fonts)
    if issues:
        print("\nISSUES (%d):" % len(issues))
        for it in issues:
            print("  slide %02d | %-12s | %-36s | %.0f | %s" % (it[0], it[1], it[2][:36], it[3], it[4]))
    else:
        print("no layout issues detected")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "test_deck.pptx")
