# -*- coding: utf-8 -*-
"""Composite slide components."""
import math
from pptx.util import Inches, Pt
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree
from PIL import ImageFont
from .theme import (W, H, M, CREAM, INK, LIME, GRAY, FONT, MONO, RL, LC, CT,
                    rect, line, text, rich, mono, picture, icon, icon_at, notes,
                    shadow_off, _c, _set_font)
from . import decor

F_REG = r"C:\Users\alita\AppData\Local\Microsoft\Windows\Fonts\Vazirmatn-Regular.ttf"
F_BOLD = r"C:\Users\alita\AppData\Local\Microsoft\Windows\Fonts\Vazirmatn-Bold.ttf"
_fcache = {}


def _font(size, bold=False):
    k = (size, bold)
    if k not in _fcache:
        _fcache[k] = ImageFont.truetype(F_BOLD if bold else F_REG, 100)
    return _fcache[k]


def tw(s, size, bold=False):
    """approximate text width in points"""
    return _font(size, bold).getlength(s) * size / 100.0


def est_lines(s, size, width_in, bold=False):
    if not s:
        return 1
    avail = width_in * 72 * 0.97
    lines = 0
    for part in s.split("\n"):
        words = part.split(" ")
        cur = 0
        n = 1
        for w in words:
            ww = tw(w + " ", size, bold)
            if cur + ww > avail and cur > 0:
                n += 1
                cur = ww
            else:
                cur += ww
        lines += n
    return lines


def text_h(s, size, width_in, bold=False, lead=1.34):
    return est_lines(s, size, width_in, bold) * size * lead / 72.0


# ------------------------------------------------------------------ page head
def head(slide, kicker, title, size=31, w=9.6, dark=False, sub=None, eyebrow=None):
    fg = CREAM if dark else INK
    gt = dim(dark)
    mono(slide, W - M - 4.6, 0.62, 4.6, 0.22, kicker, size=8.5, color=gt, align=RL, tracking=1.4)
    if eyebrow:
        mono(slide, M, 0.62, 4.0, 0.22, eyebrow, size=8.5, color=gt, align=LC, tracking=1.4)
    lines = est_lines(title, size, w, bold=True)
    th = lines * size * 1.28 / 72.0
    box = text(slide, W - M - w, 0.90, w, th + 0.12, title, size=size, bold=True, color=fg,
               align=RL, line_spacing=1.05)
    y = 0.90 + th + 0.10
    line(slide, M, y, W - M, y, LIME if dark else INK, 2.2)
    line(slide, M, y, M + 1.5, y, LIME, 2.2) if not dark else None
    y2 = y + 0.10
    if sub:
        subh = text_h(sub, 13.5, 10.5, lead=1.4)
        text(slide, W - M - 10.5, y2, 10.5, subh + 0.05, sub, size=13.5, color=gt, align=RL)
        y2 += subh + 0.18
    return y2 + 0.18


def dim(dark):
    return CREAM if dark else GRAY


def content_top(slide, kicker, title, **kw):
    return head(slide, kicker, title, **kw)


# ------------------------------------------------------------------ bullets
def bullets(slide, x, y, w, items, size=16, gap=0.16, color=INK, marker=LIME,
            mark=0.085, lead_bold=True, dark=False, numbered=False, num_color=GRAY):
    """items: str | (title, body) | list of runs"""
    cy = y
    shapes = []
    for i, it in enumerate(items):
        if isinstance(it, tuple):
            t, b = it
        elif isinstance(it, list):
            t, b = None, it
        else:
            t, b = None, it
        # measure body
        body_h = 0
        if b:
            bb = b if isinstance(b, list) else b
            if isinstance(bb, list):
                bw = "".join(r[0] for r in bb)
            else:
                bw = bb
            body_h = text_h(bw, size, w - 0.42)
        title_h = text_h(t, size + 0.5, w - 0.42, bold=True) if t else 0
        hgt = title_h + (0.05 if t and b else 0) + body_h
        # marker
        if numbered:
            mono(slide, x + w - 0.42, cy + 0.02, 0.40, 0.3, "%02d" % (i + 1), size=11,
                 color=num_color, align=RL, bold=True)
        else:
            rect(slide, x + w - 0.115, cy + 0.10, mark, mark, marker)
        tx = x + 0.05
        twd = w - 0.42
        if t:
            text(slide, tx, cy - 0.02, twd, title_h + 0.08, t, size=size + 0.5, bold=True,
                 color=CREAM if dark else color, align=RL)
            cy += title_h + 0.03
        if b:
            if isinstance(b, list):
                rich(slide, tx, cy, twd, body_h + 0.05, b, size=size,
                     color=(0xB9, 0xBA, 0xB1) if dark else color, align=RL, line_spacing=1.3)
            else:
                text(slide, tx, cy, twd, body_h + 0.05, b, size=size,
                     color=(0xC9, 0xCA, 0xC1) if dark else color,
                     align=RL, line_spacing=1.3)
        cy += hgt + gap
    return cy


def rule_tick(slide, x, y, w=1.2, color=LIME, lw=3):
    line(slide, x, y, x + w, y, color, lw)


# ------------------------------------------------------------------ cards
def card(slide, x, y, w, h, num=None, ic=None, title="", body="", variant="ink",
         icon_color=None, title_size=17, body_size=12.5, radius=0.09, extra=None):
    if variant == "ink":
        fill, tcol, bcol = INK, CREAM, (0xBE, 0xBF, 0xB6)
        icol = LIME
    elif variant == "lime":
        fill, tcol, bcol = LIME, INK, (0x3A, 0x3A, 0x30)
        icol = INK
    elif variant == "cream":
        fill, tcol, bcol = CREAM, INK, (0x55, 0x56, 0x50)
        icol = INK
    else:  # line
        fill, tcol, bcol = None, INK, GRAY
        icol = INK
    sp = rect(slide, x, y, w, h, fill, line=INK if variant == "line" else None,
              lw=1.0, radius=radius)
    if variant == "line":
        line(slide, x, y, x + w, y, INK, 2.4)
    pad = 0.30
    ty = y + pad
    if ic:
        sz = 0.40
        icon(slide, ic, x + w - pad - sz, y + pad - 0.03, sz, icol)
        title_w = w - 2 * pad - sz - 0.12
        tx = x + pad
    else:
        title_w = w - 2 * pad
        tx = x + pad
    if num is not None:
        mono(slide, x + pad, y + h - 0.36, 0.9, 0.24, num, size=9, color=bcol, align=LC, tracking=1)
    if title:
        th = text_h(title, title_size, title_w, bold=True)
        text(slide, tx, ty, title_w, th + 0.06, title, size=title_size, bold=True,
             color=tcol, align=RL, line_spacing=1.1)
        ty += th + 0.12
    if body:
        bh = h - (ty - y) - pad - (0.18 if num is not None else 0)
        text(slide, x + pad, ty, w - 2 * pad, max(bh, 0.3), body, size=body_size,
             color=bcol, align=RL, line_spacing=1.34)
    return sp


def cards_row(slide, x, y, w, h, items, gap=0.18, **kw):
    n = len(items)
    cw = (w - gap * (n - 1)) / n
    out = []
    for i, it in enumerate(items):
        it = dict(it)
        out.append(card(slide, x + (n - 1 - i) * (cw + gap), y, cw, h, **it, **kw))
    return out


# ------------------------------------------------------------------ stats
def stat(slide, x, y, w, value, label, note=None, size=44, color=INK, dark=False,
         align=RL, accent=None):
    text(slide, x, y, w, size * 1.15 / 72 + 0.1, value, size=size, bold=True, color=color,
         align=align, font=MONO if str(value).replace(".", "").replace("+", "").replace("%", "").isdigit() else FONT)
    ly = y + size * 1.15 / 72 + 0.04
    text(slide, x, ly, w, 0.3, label, size=11, color=(0xBF, 0xC0, 0xB7) if dark else GRAY, align=align)
    if note:
        text(slide, x, ly + 0.24, w, 0.3, note, size=9.5, color=accent or LIME, align=align,
             font=MONO, rtl=False)


# ------------------------------------------------------------------ table
def table(slide, x, y, w, cols, rows, widths=None, head_fill=INK, row_h=0.52,
          head_h=0.46, size=12, head_size=11, dark=False, accent_col=None, align=None):
    """cols: list[str] right-to-left. rows: list[list[str]]"""
    n = len(cols)
    widths = widths or [1.0 / n] * n
    ws = [w * t / sum(widths) for t in widths]
    xs = []
    cx = x + w
    for wi in ws:
        cx -= wi
        xs.append(cx)
    # header
    hd = rect(slide, x, y, w, head_h, head_fill, radius=None)
    cur = x + w
    for i, c in enumerate(cols):
        cur -= ws[i]
        text(slide, cur, y + 0.10, ws[i] - 0.24, head_h - 0.12, c, size=head_size, bold=True,
             color=CREAM, align=RL)
    ry = y + head_h
    for ri, row in enumerate(rows):
        bgc = ((0x1B, 0x1D, 0x19) if ri % 2 == 0 else None) if dark else (CREAM if ri % 2 == 0 else None)
        if dark:
            bgc = None if ri % 2 else (0x1B, 0x1D, 0x19)
        if bgc:
            rect(slide, x, ry, w, row_h, bgc)
        line(slide, x, ry + row_h, x + w, ry + row_h, (0x3A, 0x3C, 0x36) if dark else (0xD9, 0xD5, 0xC9), 0.75)
        cur = x + w
        for ci, cell in enumerate(row):
            cur -= ws[ci]
            bold = (ci == 0)
            col = LIME if (accent_col is not None and ci == accent_col) else ((0xE8, 0xE4, 0xD8) if dark else INK)
            text(slide, cur, ry + 0.10, ws[ci] - 0.22, row_h - 0.12, str(cell), size=size,
                 bold=bold, color=col, align=RL, anchor=MSO_ANCHOR.MIDDLE)
        ry += row_h
    return ry


# ------------------------------------------------------------------ terminal
def terminal(slide, x, y, w, h, lines, title="claude", fs=11, bar=True):
    rect(slide, x, y, w, h, INK, radius=0.06)
    if bar:
        rect(slide, x, y, w, 0.34, (0x1C, 0x1E, 0x1A), radius=0.06)
        rect(slide, x, y + 0.22, w, 0.12, (0x1C, 0x1E, 0x1A))
        for i, c in enumerate([(0x4A, 0x4C, 0x44)] * 3):
            rect(slide, x + 0.16 + i * 0.16, y + 0.12, 0.085, 0.085, c, shape=MSO_SHAPE.OVAL)
        mono(slide, x + w - 0.2 - 2.2, y + 0.09, 2.2, 0.18, title, size=8, color=(0x7C, 0x7E, 0x74), align=RL)
    ly = y + (0.50 if bar else 0.22)
    for ln in lines:
        if isinstance(ln, tuple):
            s, col, bold = ln
        else:
            s, col, bold = ln, (0xD9, 0xDB, 0xD0), False
        mono(slide, x + 0.24, ly, w - 0.48, fs * 1.6 / 72, s, size=fs, color=col, bold=bold, align=LC)
        ly += fs * 1.72 / 72


def prompt_line(slide, x, y, w, s, size=13, dark=True):
    mono(slide, x, y, 0.3, 0.3, ">", size=size, color=LIME)
    mono(slide, x + 0.3, y, w - 0.3, 0.3, s, size=size, color=(0xE4, 0xE0, 0xD4) if dark else INK)


# ------------------------------------------------------------------ chips
def chip(slide, x, y, s, size=11, fill=None, fg=INK, pad=0.18, h=0.34, radius=0.5, border=None):
    w = tw(s, size) / 72 + pad * 2
    sp = rect(slide, x, y, w, h, fill, line=border, radius=radius)
    text(slide, x, y + 0.045, w, h - 0.05, s, size=size, color=fg, align=CT, margins=(0.02, 0.02, 0, 0))
    return w


def tag(slide, x, y, s, dark=False, size=9):
    w = tw(s, size) / 72 + 0.24
    sp = rect(slide, x, y, w, 0.26, None, line=LIME if dark else INK, lw=0.9, radius=0.3)
    mono(slide, x, y + 0.045, w, 0.18, s, size=size, color=LIME if dark else INK, align=CT, tracking=1)
    return w


# ------------------------------------------------------------------ diagram bits
def arrow(slide, x1, y1, x2, y2, color=INK, lw=1.4, head=True, dash=None, size="med"):
    cn = line(slide, x1, y1, x2, y2, color, lw, dash)
    if head:
        ln = cn.line._get_or_add_ln()
        end = etree.SubElement(ln, qn("a:tailEnd"))
        end.set("type", "triangle")
        end.set("w", size)
        end.set("len", size)
    return cn


def node(slide, x, y, w, h, label, sub=None, fill=INK, fg=CREAM, size=13, radius=0.12,
         ic=None, align=CT, border=None):
    sp = rect(slide, x, y, w, h, fill, line=border, radius=radius)
    if ic:
        icon_at(slide, ic, x + w / 2, y + 0.24, 0.30, fg if fill == INK else INK)
        text(slide, x + 0.08, y + h / 2 - 0.02, w - 0.16, 0.3, label, size=size, bold=True,
             color=fg, align=CT)
    else:
        if sub:
            text(slide, x + 0.08, y + h / 2 - 0.20, w - 0.16, 0.3, label, size=size, bold=True,
                 color=fg, align=align)
            text(slide, x + 0.08, y + h / 2 + 0.09, w - 0.16, 0.3, sub, size=size - 3,
                 color=GRAY, align=align)
        else:
            text(slide, x + 0.08, y + h / 2 - 0.16, w - 0.16, 0.34, label, size=size, bold=True,
                 color=fg, align=align)
    return sp


def pill_num(slide, x, y, n, size=0.34, fill=LIME, fg=INK):
    rect(slide, x, y, size, size, fill, shape=MSO_SHAPE.OVAL)
    text(slide, x, y + 0.055, size, size - 0.06, str(n), size=size * 26, bold=True, color=fg, align=CT)


def image_label(slide, x, y, w, label, sub=None, dark=True):
    mono(slide, x, y, w, 0.2, label, size=8.5, color=LIME if dark else GRAY, align=LC, tracking=1.2)
    if sub:
        text(slide, x, y + 0.2, w, 0.3, sub, size=10, color=(0xB9, 0xBA, 0xB1) if dark else GRAY, align=LC)


def side_image(slide, name, x, y, w, h, frame=True):
    p = decor.ensure_art([name])[name]
    return picture(slide, p, x, y, w, h, frame=INK if frame else None, fw=0.75)


def full_image(slide, name, x=0, y=0, w=W, h=H):
    return side_image(slide, name, x, y, w, h, frame=False)


def veil(slide, x, y, w, h, color=INK, alpha=0.55):
    sp = rect(slide, x, y, w, h, color)
    solid = sp.fill._xPr.find(qn("a:solidFill"))
    srgb = solid.find(qn("a:srgbClr"))
    el = etree.SubElement(srgb, qn("a:alpha"))
    el.set("val", str(int(alpha * 100000)))
    return sp
