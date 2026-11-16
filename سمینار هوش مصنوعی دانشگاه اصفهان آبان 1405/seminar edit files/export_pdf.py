# -*- coding: utf-8 -*-
"""Export the final deck to PDF for easy sharing."""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
import win32com.client as win32

HERE = os.path.dirname(os.path.abspath(__file__))

src = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "AI-Seminar.pptx")
dst = os.path.splitext(src)[0] + ".pdf"

app = win32.Dispatch("PowerPoint.Application")
pres = app.Presentations.Open(src, WithWindow=False)
pres.SaveAs(dst, 32)
pres.Close()
app.Quit()
print("wrote", dst, "%.1f MB" % (os.path.getsize(dst) / 1048576.0))
