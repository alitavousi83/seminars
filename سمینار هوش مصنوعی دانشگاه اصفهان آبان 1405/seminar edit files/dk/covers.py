# -*- coding: utf-8 -*-
"""Cover, section dividers, closing slide."""
from .theme import (W, H, M, CREAM, INK, LIME, GRAY, MONO, RL, LC, CT,
                    rect, line, text, mono, picture, bg)
from . import decor


def cover(slide, num, total, title1="هوش مصنوعی", title2="از صفر تا ایجنت",
          subtitle="تاریخچه، یادگیری ماشین، مدل‌های زبانی بزرگ، پرامپت‌نویسی، ایجنت‌ها و Claude Code",
          presenter="نام و نام خانوادگی شما", date="آبان ۱۴۰۵"):
    bg(slide, INK)
    p = decor.ensure_art(["orb"])["orb"]
    picture(slide, p, 7.05, 0, 6.28, H, frame=None)
    text(slide, M, 0.62, 6.0, 0.24, "SEMINAR / ARTIFICIAL INTELLIGENCE", size=9, color=LIME,
         align=LC, font=MONO, rtl=False)
    line(slide, M, 0.92, M + 1.7, 0.92, LIME, 2.5)
    text(slide, M, 1.05, 6.3, 0.3, "سمینار تخصصی", size=12, color=(0x8F, 0x91, 0x87), align=LC)
    text(slide, M, 1.66, 6.4, 2.45, [[(title1, {"size": 60, "bold": True, "color": CREAM})],
                                      [(title2, {"size": 46, "bold": True, "color": LIME})]],
         size=60, align=LC, line_spacing=1.15)
    line(slide, M, 4.28, M + 1.9, 4.28, (0x3E, 0x40, 0x39), 1.2)
    text(slide, M, 4.46, 5.9, 1.0, subtitle, size=14.5, color=(0xBF, 0xC0, 0xB6), align=LC, line_spacing=1.55)
    text(slide, M, 6.08, 2.2, 0.22, "PRESENTED BY", size=8.5, color=(0x7E, 0x80, 0x76), align=LC,
         font=MONO, rtl=False)
    text(slide, M, 6.32, 4.2, 0.34, presenter, size=14, bold=True, color=CREAM, align=LC)
    text(slide, M + 4.3, 6.32, 2.1, 0.34, date, size=12, color=(0x9A, 0x9C, 0x92), align=LC)
    x = M
    for i in range(10):
        rect(slide, x, 6.86, 0.24, 0.035, LIME if i % 3 == 0 else (0x3A, 0x3C, 0x36))
        x += 0.30
    mono(slide, W - M - 1.2, 6.74, 1.2, 0.2, "2026 / 01", size=8, color=(0x6E, 0x70, 0x67),
         align=RL, tracking=1)


def divider(slide, num, fa, en, items, art, idx, total):
    from .parts import est_lines
    from . import anim
    bg(slide, INK)
    full = decor.ensure_art([art])[art]
    picture(slide, full, 0, 0, W, H, frame=None)
    veil(slide, 0, 0, W, H, INK, 0.58)
    num_box = text(slide, M - 0.15, 3.30, 5.4, 4.30, "%02d" % num, size=228, bold=True, color=LIME,
                   font=MONO, align=LC, rtl=False)
    text(slide, M, 0.62, 4.0, 0.24, "SECTION %02d / 10" % num, size=9.5, color=LIME, align=LC,
         font=MONO, rtl=False)
    text(slide, W - M - 3.2, 0.62, 3.2, 0.24, "AI SEMINAR / 2026", size=8.5, color=(0x8A, 0x8C, 0x82),
         align=RL, font=MONO, rtl=False)
    line(slide, W - M - 0.06, 1.30, W - M - 0.06, 4.55, LIME, 3)
    lines = est_lines(fa, 46, 7.6, bold=True)
    th = lines * 46 * 1.18 / 72.0
    text(slide, 4.55, 1.55, 7.6, th + 0.15, fa, size=46, bold=True, color=CREAM, align=RL, line_spacing=1.1)
    title_box = slide.shapes[-1]
    ey = 1.55 + th + 0.13
    text(slide, 4.55, ey, 7.55, 0.3, en, size=11, color=LIME, align=RL, font=MONO, rtl=False)
    en_box = slide.shapes[-1]
    iy = ey + 0.52
    line(slide, 11.1, iy - 0.08, 12.55, iy - 0.08, (0x50, 0x52, 0x48), 1.0)
    text(slide, 4.55, iy + 0.10, 7.5, 1.5, items, size=13.5, color=(0xC5, 0xC6, 0xBC), align=RL, line_spacing=1.75)
    items_box = slide.shapes[-1]
    text(slide, W - M - 1.4, 6.92, 1.4, 0.24, "%02d / %02d" % (idx, total), size=9,
         color=(0x9C, 0x9E, 0x94), align=RL, font=MONO, rtl=False)
    anim.transition(slide, "fade", "slow")
    anim.animate(slide, [num_box, title_box, en_box, items_box], dur=0.5, gap=0.12, delay=0.10)


def veil(slide, x, y, w, h, color=INK, alpha=0.55):
    from pptx.oxml.ns import qn
    from lxml import etree
    sp = rect(slide, x, y, w, h, color)
    solid = sp.fill._xPr.find(qn("a:solidFill"))
    srgb = solid.find(qn("a:srgbClr"))
    el = etree.SubElement(srgb, qn("a:alpha"))
    el.set("val", str(int(alpha * 100000)))
    return sp


def qa(slide, total):
    bg(slide, INK)
    full = decor.ensure_art(["nodes_dark"])["nodes_dark"]
    picture(slide, full, 0, 0, W, H, frame=None)
    veil(slide, 0, 0, W, H, INK, 0.62)
    text(slide, M, 0.70, 5.0, 0.25, "THE END / THE BEGINNING", size=10, color=LIME, align=LC,
         font=MONO, rtl=False)
    text(slide, M, 1.50, 8.4, 1.6, "پرسش و پاسخ", size=76, bold=True, color=CREAM, align=LC)
    line(slide, M, 3.45, M + 2.2, 3.45, LIME, 3)
    text(slide, M, 3.75, 7.6, 1.0,
         "هر سؤالی دارید بپرسید؛ و اگر خواستید، با هم یک دموی زنده اجرا کنیم.",
         size=18, color=(0xC9, 0xCA, 0xC0), align=LC)
    text(slide, M, 6.55, 6.0, 0.24, "THANK YOU FOR YOUR ATTENTION", size=9,
         color=(0x84, 0x86, 0x7C), align=LC, font=MONO, rtl=False)
    text(slide, W - M - 2.4, 6.55, 2.4, 0.24, "%02d / %02d" % (total, total), size=9,
         color=(0xA9, 0xAB, 0xA0), align=RL, font=MONO, rtl=False)
