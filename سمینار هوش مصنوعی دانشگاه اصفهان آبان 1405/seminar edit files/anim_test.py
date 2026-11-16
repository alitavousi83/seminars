import sys, os
sys.path.insert(0, '.')
from dk import theme as T
prs = T.new_deck()
s = T.blank(prs); T.bg(s)
for i in range(3):
    T.rect(s, 1+i*2.5, 2, 2, 1.2, T.LIME)
    s.shapes[-1].text_frame.text = "Shape %d" % i
prs.save("test_anim.pptx")

import win32com.client as win32
app = win32.Dispatch("PowerPoint.Application")
pres = app.Presentations.Open(os.path.abspath("test_anim.pptx"), WithWindow=False)
sl = pres.Slides(1)
for i in range(1, 4):
    sh = sl.Shapes(i)
    sh.AnimationSettings.EntryEffect = 10   # fade
    sh.AnimationSettings.TextLevelEffect = 0
sl.SlideShowTransition.EntryEffect = 1793
pres.Save()
pres.Close()
app.Quit()
print("saved")
