# -*- coding: utf-8 -*-
"""Structural QA on the built deck: bounds, animations, fonts, density."""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
import win32com.client as win32

HERE = os.path.dirname(os.path.abspath(__file__))


def main(path="test_deck.pptx"):
    path = os.path.abspath(path)
    app = win32.Dispatch("PowerPoint.Application")
    pres = app.Presentations.Open(path, WithWindow=False)
    sw, sh = pres.PageSetup.SlideWidth, pres.PageSetup.SlideHeight
    total = pres.Slides.Count
    print("slides: %d  size: %.0f x %.0f pt" % (total, sw, sh))
    problems = []
    no_anim, outside, mono_persian = [], [], []
    for i in range(1, total + 1):
        sl = pres.Slides(i)
        shapes = list(sl.Shapes)
        n_anim = sl.TimeLine.MainSequence.Count
        try:
            trans = sl.SlideShowTransition.EntryEffect
        except Exception:
            trans = 0
        if i not in (1,) and n_anim == 0 and trans == 0:
            no_anim.append(i)
        for shp in shapes:
            try:
                if shp.Type == 17:  # picture
                    continue
                if shp.Left < -4 or shp.Top < -4 or shp.Left + shp.Width > sw + 4 or shp.Top + shp.Height > sh + 4:
                    if shp.Width < sw - 8 or shp.Height < sh - 8:
                        outside.append((i, shp.Name, round(shp.Left / 72, 2), round(shp.Top / 72, 2),
                                        round(shp.Width / 72, 2), round(shp.Height / 72, 2)))
                if shp.HasTextFrame and shp.TextFrame.HasText:
                    tr = shp.TextFrame2.TextRange
                    txt = tr.Text
                    if any("\u0600" <= ch <= "\u06FF" for ch in txt) and tr.Font.Name == "Consolas":
                        mono_persian.append((i, txt[:24]))
            except Exception:
                pass
        if len(shapes) < 6:
            problems.append((i, "sparse slide (%d shapes)" % len(shapes)))
    print("slides without animation/transition:", no_anim or "none")
    print("shapes outside bounds:", outside or "none")
    print("persian text in mono font:", mono_persian or "none")
    print("sparse slides:", problems or "none")
    presenters = sum(1 for i in range(1, total + 1) if pres.Slides(i).NotesPage.Shapes(2).TextFrame.HasText)
    print("slides with speaker notes: %d / %d" % (presenters, total))
    pres.Close()
    app.Quit()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "test_deck.pptx")
