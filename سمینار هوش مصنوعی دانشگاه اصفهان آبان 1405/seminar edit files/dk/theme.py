# -*- coding: utf-8 -*-
"""Design system + low level drawing primitives."""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree
from PIL import Image
from . import decor

W, H = 13.333, 7.5
M = 0.72  # outer margin

CREAM = RGBColor(0xF5, 0xF1, 0xE8)
INK = RGBColor(0x11, 0x11, 0x11)
LIME = RGBColor(0xC8, 0xFF, 0x00)
GRAY = RGBColor(0x8A, 0x8A, 0x84)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Vazirmatn"
MONO = "Consolas"

RL = PP_ALIGN.RIGHT
LC = PP_ALIGN.LEFT
CT = PP_ALIGN.CENTER


def _c(v):
    if isinstance(v, RGBColor):
        return v
    if isinstance(v, tuple):
        return RGBColor(*v)
    v = v.lstrip("#")
    return RGBColor(int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))


def new_deck():
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    return prs


def blank(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    return s


def bg(slide, color=CREAM):
    f = slide.background.fill
    f.solid()
    f.fore_color.rgb = _c(color)


def no_line(shape):
    shape.line.fill.background()


def shadow_off(shape):
    try:
        shape.shadow.inherit = False
    except Exception:
        pass


def rect(slide, x, y, w, h, fill=INK, line=None, lw=1.0, radius=None,
         shape=MSO_SHAPE.RECTANGLE, transparency=0):
    if radius is not None:
        shape = MSO_SHAPE.ROUNDED_RECTANGLE
    sp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    shadow_off(sp)
    if fill is None:
        sp.fill.background()
    elif transparency:
        sp.fill.solid()
        sp.fill.fore_color.rgb = _c(fill)
        _set_alpha(sp.fill.fore_color, 1 - transparency)
    else:
        sp.fill.solid()
        sp.fill.fore_color.rgb = _c(fill)
    if line is None:
        no_line(sp)
    else:
        sp.line.color.rgb = _c(line)
        sp.line.width = Pt(lw)
    if radius is not None and sp.adjustments:
        sp.adjustments[0] = radius
    sp.text_frame.word_wrap = True
    return sp


def _set_alpha(color, alpha):
    srgb = color._xFill.find(qn("a:srgbClr"))
    if srgb is None:
        return
    el = etree.SubElement(srgb, qn("a:alpha"))
    el.set("val", str(int(alpha * 100000)))


def line(slide, x1, y1, x2, y2, color=INK, lw=1.0, dash=None):
    from pptx.enum.shapes import MSO_CONNECTOR
    cn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    cn.line.color.rgb = _c(color)
    cn.line.width = Pt(lw)
    if dash:
        cn.line.dash_style = dash
    return cn


def _set_font(run, name, size, color, bold, italic=False):
    f = run.font
    f.name = name
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = _c(color)
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:latin", "a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = etree.SubElement(rPr, qn(tag))
        el.set("typeface", name)


def text(slide, x, y, w, h, content, size=18, color=INK, bold=False, font=FONT,
         align=RL, anchor=MSO_ANCHOR.TOP, line_spacing=1.15, space_after=0,
         rtl=True, margins=(0, 0, 0, 0), italic=False, justification=None):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left, tf.margin_right, tf.margin_top, tf.margin_bottom = [Inches(m) for m in margins]
    tf.vertical_anchor = anchor
    tf.clear()
    paras = content if isinstance(content, list) else [content]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        pPr = p._p.get_or_add_pPr()
        if rtl:
            pPr.set("rtl", "1")
        runs = para if isinstance(para, list) else [(para, {})]
        for t, st in runs:
            r = p.add_run()
            r.text = t
            _set_font(r, st.get("font", font), st.get("size", size), st.get("color", color),
                      st.get("bold", bold), st.get("italic", italic))
    return box


def rich(slide, x, y, w, h, runs, size=18, color=INK, bold=False, **kw):
    """runs: list of (text, overrides) for a single paragraph."""
    return text(slide, x, y, w, h, [runs], size=size, color=color, bold=bold, **kw)


def mono(slide, x, y, w, h, s, size=10, color=GRAY, bold=False, align=LC, tracking=0, **kw):
    box = text(slide, x, y, w, h, s, size=size, color=color, bold=bold, font=MONO,
               align=align, rtl=False, **kw)
    if tracking:
        for p in box.text_frame.paragraphs:
            for r in p.runs:
                r._r.get_or_add_rPr().set("spc", str(int(tracking * 100)))
    return box


def picture(slide, path, x, y, w, h, frame=None, fw=1.0):
    """Cover-fit picture inside the rect (no distortion)."""
    iw, ih = Image.open(path).size
    target = w / h
    src = iw / ih
    pic = slide.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    if src > target:
        crop = (1 - target / src) / 2
        pic.crop_left = crop
        pic.crop_right = crop
    elif src < target:
        crop = (1 - src / target) / 2
        pic.crop_top = crop
        pic.crop_bottom = crop
    shadow_off(pic)
    if frame:
        pic.line.color.rgb = _c(frame)
        pic.line.width = Pt(fw)
    return pic


def icon(slide, name, x, y, size, color=LIME, stroke=2.0, px=256):
    if isinstance(color, str):
        c = tuple(int(color.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    elif isinstance(color, RGBColor):
        c = tuple(int(str(color)[i:i + 2], 16) for i in (0, 2, 4))
    else:
        c = tuple(color)
    p = decor.icon_path(name, px=px, color=c, stroke=stroke)
    pic = slide.shapes.add_picture(p, Inches(x), Inches(y), Inches(size), Inches(size))
    shadow_off(pic)
    return pic


def icon_at(slide, name, cx, cy, size, color=LIME, stroke=2.0):
    return icon(slide, name, cx - size / 2, cy - size / 2, size, color, stroke)


def notes(slide, s):
    slide.notes_slide.notes_text_frame.text = s


def stamp(slide, label, num, total, dark=False):
    """Editorial furniture: section label, page number, hairline."""
    fg = CREAM if dark else INK
    gt = RGBColor(0x9A, 0x9A, 0x92) if not dark else RGBColor(0x77, 0x79, 0x70)
    line(slide, M, 0.52, W - M, 0.52, fg if not dark else RGBColor(0x33, 0x35, 0x30), 0.75)
    rect(slide, W - M - 0.075, 0.40, 0.075, 0.075, LIME)
    mono(slide, W - M - 3.1, 0.33, 2.9, 0.22, label, size=8.5, color=gt, align=RL)
    mono(slide, M, 7.05, 2.4, 0.22, "AI SEMINAR / 2026", size=8, color=gt, align=LC, tracking=1.2)
    mono(slide, W - M - 1.25, 7.03, 1.25, 0.24,
         "%02d" % num + " / " + "%02d" % total, size=9, color=fg, align=RL, tracking=0.6)
    mono(slide, M + 2.8, 7.05, 3.0, 0.22, "HUMAN × MACHINE", size=8, color=gt, align=LC, tracking=1.2)


def tick(slide, x, y, size=0.06, color=GRAY):
    rect(slide, x, y, size, size, color)


def dotgrid(slide, x, y, w, h, color=GRAY, step=0.22, d=0.018, alpha=0.55):
    cols = int(w / step)
    rows = int(h / step)
    for i in range(cols):
        for j in range(rows):
            rect(slide, x + i * step, y + j * step, d, d, color, shape=MSO_SHAPE.OVAL, transparency=alpha)
