import sys, os
sys.path.insert(0, '.')
from dk import theme as T, anim
prs = T.new_deck()
s = T.blank(prs); T.bg(s)
a = T.text(s, 1, 1, 4, 1, "عنوان تست فارسی", size=40, bold=True)
b = T.rect(s, 1, 3, 3, 1.2, T.LIME); b.text_frame.text = "کارت نمونه"
c = T.icon(s, 'brain', 6, 3, 1.2, T.INK)
anim.transition(s, 'fade')
anim.animate(s, [a, b, c])
prs.save('test_anim2.pptx')

import win32com.client as win32
app = win32.Dispatch('PowerPoint.Application')
pres = app.Presentations.Open(os.path.abspath('test_anim2.pptx'), WithWindow=False)
sl = pres.Slides(1)
seq = sl.TimeLine.MainSequence
print('effects:', seq.Count)
for i in range(1, seq.Count+1):
    e = seq.Item(i)
    print(i, 'type', e.EffectType, 'trigger', e.Timing.TriggerType, 'dur', e.Timing.Duration, 'start', e.Timing.Start)
print('transition', sl.SlideShowTransition.EntryEffect)
os.makedirs('assets/preview', exist_ok=True)
sl.Export(os.path.abspath('assets/preview/t1.png'), 'PNG', 1600, 900)
pres.Close(); app.Quit()
print('exported')
