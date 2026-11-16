# -*- coding: utf-8 -*-
"""Section 1 — foundations: AI, ML, DL."""
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR
from .theme import (W, H, M, CREAM, INK, LIME, GRAY, FONT, MONO, RL, LC, CT,
                    rect, line, text, rich, mono, icon, icon_at, stamp)
from . import parts as P
from . import covers, anim

LAB = "01 / FOUNDATIONS"


def finish(s, shapes, label, num, total, dark=False):
    stamp(s, label, num, total, dark)
    anim.transition(s)
    anim.animate(s, shapes)


def s_cover(s, num, total):
    covers.cover(s, num, total)
    anim.transition(s, "fade", "slow")


def s_agenda(s, num, total):
    top = P.head(s, "ROADMAP / 10 SECTIONS", "نقشه راه سمینار", size=34, w=10.2)
    items = [
        ("تاریخچه و مبانی", "AI HISTORY / ML / DL", "۰۱"),
        ("مدل‌های زبانی بزرگ", "LARGE LANGUAGE MODELS", "۰۲"),
        ("زبان، Attention و Transformer", "HOW AI READS US", "۰۳"),
        ("مهندسی پرامپت", "PROMPT ENGINEERING", "۰۴"),
        ("ابزارهای کاربردی", "AI TOOLS", "۰۵"),
        ("ایجنت‌های هوش مصنوعی", "AI AGENTS", "۰۶"),
        ("Claude و Claude Code", "ANTHROPIC ECOSYSTEM", "۰۷"),
        ("راه‌اندازی و مدل‌های محلی", "SETUP / OLLAMA", "۰۸"),
        ("کاربردهای عملی", "BUILD WITH AI", "۰۹"),
        ("آینده و جمع‌بندی", "FUTURE / Q&A", "۱۰"),
    ]
    ys = 2.02
    for i, (t, en, n) in enumerate(items[:5]):
        y = ys + i * 0.94
        mono(s, 11.35, y + 0.03, 0.9, 0.25, n, size=10, color=LIME if False else GRAY, align=RL, bold=True)
        text(s, 6.85, y, 4.3, 0.32, t, size=15.5, bold=True, align=RL)
        mono(s, 6.85, y + 0.34, 4.3, 0.2, en, size=7.5, color=GRAY, align=RL, tracking=1.1)
    for i, (t, en, n) in enumerate(items[5:]):
        y = ys + i * 0.94
        mono(s, 5.05, y + 0.03, 0.9, 0.25, n, size=10, color=GRAY, align=RL, bold=True)
        text(s, 0.78, y, 4.2, 0.32, t, size=15.5, bold=True, align=RL)
        mono(s, 0.78, y + 0.34, 4.2, 0.2, en, size=7.5, color=GRAY, align=RL, tracking=1.1)
    line(s, 6.62, 2.02, 6.62, 6.55, (0xD8, 0xD4, 0xC8), 0.9)
    line(s, 0.78, 6.62, 12.55, 6.62, INK, 1.0)
    text(s, 8.9, 6.72, 3.65, 0.24, "%d اسلاید · ۱۰ بخش · حدود ۹۰ دقیقه" % total, size=10.5,
         color=GRAY, align=RL)
    mono(s, 0.78, 6.74, 4.0, 0.22, "AI SEMINAR / 2026", size=8, color=GRAY, align=LC, tracking=1.6)
    finish(s, [], "AGENDA", num, total)


def s_div1(s, num, total):
    covers.divider(s, 1, "تاریخچه و مبانی", "AI HISTORY / MACHINE LEARNING / DEEP LEARNING",
                   "هوش مصنوعی چه بود، چه شد و امروز کجاست؟\nاز قاعده‌های دستی تا شبکه‌هایی که خودشان الگو می‌آموزند.",
                   "nodes_dark", num, total)


def s_what_is_ai(s, num, total):
    top = P.head(s, LAB + " / DEFINITION", "هوش مصنوعی چیست؟", size=34, w=9.4)
    text(s, 5.55, 2.02, 7.05, 0.95,
         "مجموعه‌ای از روش‌ها که به ماشین امکان می‌دهد از داده الگو یاد بگیرد، تصمیم بگیرد و محتوا تولید کند — بدون اینکه برای هر حالت دستور جداگانه نوشته باشیم.",
         size=14.5, color=(0x3A, 0x3B, 0x35), align=RL, line_spacing=1.5)
    # nested diagram
    x0, y0, w0, h0 = 0.82, 2.95, 4.35, 3.55
    e1 = rect(s, x0, y0, w0, h0, None, line=INK, lw=1.3)
    text(s, x0 + 0.18, y0 + 0.14, 1.2, 0.3, "AI", size=15, bold=True, color=INK, align=LC, font=MONO, rtl=False)
    rect(s, x0 + 0.32, y0 + 0.55, w0 - 0.64, h0 - 0.72, None, line=(0xB5, 0xB2, 0xA6), lw=1.1)
    text(s, x0 + 0.50, y0 + 0.66, 1.6, 0.28, "MACHINE LEARNING", size=8, bold=True, color=GRAY,
         align=LC, font=MONO, rtl=False)
    rect(s, x0 + 0.72, y0 + 1.08, w0 - 1.44, h0 - 1.28, INK, line=None)
    text(s, x0 + 0.92, y0 + 1.22, 2.4, 0.24, "DEEP LEARNING", size=8, bold=True, color=LIME,
         align=LC, font=MONO, rtl=False)
    rect(s, x0 + 1.28, y0 + 2.02, 1.65, 0.42, LIME)
    text(s, x0 + 1.28, y0 + 2.10, 1.65, 0.26, "GenAI / LLM", size=10, bold=True, color=INK,
         align=CT, font=MONO, rtl=False)
    # three generations
    rows = [
        ("نسل ۱ / قاعده‌محور", "۱۹۵۰–۱۹۸۰", "منطق، قواعد و درخت تصمیم. سیستم دقیق است اما شکننده؛ هر استثنا یک باگ جدید."),
        ("نسل ۲ / یادگیری ماشین", "۱۹۸۰–۲۰۱۲", "مدل از داده الگو می‌آموزد، اما مهندس باید «ویژگی‌ها» را دستی طراحی کند."),
        ("نسل ۳ / یادگیری عمیق", "۲۰۱۲–امروز", "شبکه‌های عصبی چندلایه خودشان ویژگی می‌سازند؛ سوخت آن داده و GPU است."),
    ]
    for i, (t, y, b) in enumerate(rows):
        yy = 3.90 + i * 1.02
        text(s, 8.95, yy, 3.6, 0.26, y, size=9, color=GRAY, align=RL, font=MONO, rtl=False)
        text(s, 5.55, yy - 0.03, 3.25, 0.3, t, size=14.5, bold=True, align=RL)
        text(s, 5.55, yy + 0.34, 7.0, 0.55, b, size=11.5, color=(0x55, 0x56, 0x50), align=RL, line_spacing=1.4)
    finish(s, [], "WHAT IS AI", num, total)


def s_timeline(s, num, total):
    P.head(s, LAB + " / 1950 → 2026", "هفتاد سال در یک نگاه", size=34, w=10.0)
    y = 4.02
    line(s, 0.95, y, 12.40, y, INK, 1.4)
    events = [
        ("1950", "آزمون تورینگ", 0), ("1956", "کارگاه دارتموث؛ تولد AI", 0),
        ("1966", "ELIZA؛ اولین چت‌بات", 1), ("1980", "شکوفایی سیستم‌های خبره", 0),
        ("1997", "Deep Blue کاسپاروف را برد", 1), ("2012", "AlexNet؛ انقلاب یادگیری عمیق", 0),
        ("2016", "AlphaGo لی سدول را برد", 1), ("2017", "Transformer متولد شد", 0),
        ("2020", "GPT-3 با ۱۷۵ میلیارد پارامتر", 1), ("2022", "ChatGPT؛ AI به دست مردم", 0),
        ("2024", "چندوجهی، استدلال و MCP", 1), ("2025+", "عصر ایجنت‌ها و خودکارسازی", 0),
    ]
    step = (12.10 - 1.20) / 11
    marks = {"2012", "2017", "2022", "2025+"}
    for i, (yy, label, up) in enumerate(events):
        x = 1.20 + i * step
        hero = yy in marks
        if up:
            mono(s, x - 0.5, y - 0.55, 1.0, 0.24, yy, size=10.5, color=LIME if hero else INK,
                 align=CT, bold=True)
            text(s, x - 0.68, y - 1.42, 1.36, 0.8, label, size=8.2, color=(0x4A, 0x4B, 0x45),
                 align=CT, line_spacing=1.3)
            line(s, x, y - 0.26, x, y - 0.06, (0xB9, 0xB5, 0xA8), 0.9)
        else:
            mono(s, x - 0.5, y + 0.24, 1.0, 0.24, yy, size=10.5, color=LIME if hero else INK,
                 align=CT, bold=True)
            text(s, x - 0.68, y + 0.55, 1.36, 0.8, label, size=8.2, color=(0x4A, 0x4B, 0x45),
                 align=CT, line_spacing=1.3)
            line(s, x, y + 0.06, x, y + 0.20, (0xB9, 0xB5, 0xA8), 0.9)
        rect(s, x - 0.075, y - 0.075, 0.15, 0.15, LIME if hero else INK, shape=MSO_SHAPE.OVAL)
    text(s, 0.95, 6.30, 11.6, 0.4, "دو زمستان AI (دهه ۷۰ و پایان دهه ۸۰) نشان داد هیاهو بدون ارزش واقعی دوام ندارد؛ درسِ امروز: به کاربرد بسنجیم، نه به دمو.",
         size=10.5, color=GRAY, align=RL)
    finish(s, [], "TIMELINE", num, total)


def s_ml(s, num, total):
    P.head(s, LAB + " / MACHINE LEARNING", "یادگیری ماشین: از قاعده به داده", size=32, w=10.6)
    # two pipelines
    rows = [
        ("برنامه‌نویسی سنتی", "داده", "قواعد / کد", "پاسخ", "برای هر حالت، انسان قاعده می‌نویسد."),
        ("یادگیری ماشین", "داده + پاسخ", "الگوریتم یادگیری", "قواعد / مدل", "الگوریتم از مثال‌ها قاعده را کشف می‌کند."),
    ]
    for ri, (name, a, b, c, note) in enumerate(rows):
        y = 2.18 + ri * 1.72
        mono(s, 0.95, y - 0.30, 6.0, 0.24, "%02d" % (ri + 1) + " / " + name, size=8.5,
             color=GRAY, align=LC, tracking=1.2)
        boxes = [(9.95, a), (7.15, b), (4.35, c)]
        for j, (x, label) in enumerate(boxes):
            fill = INK if (ri == 1 and j == 2) else None
            sp = rect(s, x, y, 2.42, 0.92, fill, line=None if fill else (0xB8, 0xB4, 0xA7), lw=1.1, radius=0.06)
            text(s, x + 0.1, y + (0.28 if len(label) < 12 else 0.22), 2.22, 0.42, label,
                 size=12.5, bold=True, color=LIME if fill else INK, align=CT)
        for j in range(2):
            x_start = 9.95 - 0.08
            x_end = 7.15 + 2.44 + 0.02
            P.arrow(s, x_start, y + 0.46, x_end, y + 0.46, INK, 1.3)
        text(s, 0.95, y + 1.02, 6.4, 0.24, note, size=9.5, color=GRAY, align=LC)
    # insight
    line(s, 0.95, 5.90, 12.40, 5.90, INK, 1.0)
    text(s, 4.6, 6.02, 7.8, 0.3, "جان کلام:", size=12, bold=True, align=RL)
    text(s, 0.95, 6.02, 3.55, 0.5, "در ML، «برنامه» خروجی یادگیری است، نه ورودی آن.", size=12,
         color=(0x3E, 0x3F, 0x39), align=RL)
    finish(s, [], "MACHINE LEARNING", num, total)


def s_three_types(s, num, total):
    P.head(s, LAB + " / THREE PARADIGMS", "سه خانواده‌ی یادگیری", size=33, w=9.8)
    items = [
        dict(num="01", ic="target", title="یادگیری نظارت‌شده",
             body="مدل با جفت «ورودی–برچسب» آموزش می‌بیند.\nطبقه‌بندی: تشخیص اسپم، تشخیص چهره\nرگرسیون: قیمت خانه، پیش‌بینی فروش"),
        dict(num="02", ic="scan", title="یادگیری بدون نظارت",
             body="داده برچسب ندارد؛ مدل ساختار پنهان را پیدا می‌کند.\nخوشه‌بندی مشتریان، کاهش ابعاد،\nتشخیص ناهنجاری و ساخت Embedding"),
        dict(num="03", ic="repeat", title="یادگیری تقویتی",
             body="عامل با آزمون‌وخطا و پاداش یاد می‌گیرد.\nبازی، رباتیک، کنترل، و RLHF\nبرای هم‌ترازی مدل‌های زبانی"),
    ]
    P.cards_row(s, 0.75, 2.15, 11.85, 3.55, items, gap=0.22)
    line(s, 0.75, 6.10, 12.60, 6.10, (0xD5, 0xD1, 0xC4), 1.0)
    text(s, 7.4, 6.22, 5.2, 0.3, "در عمل، بیشتر محصولات امروز ترکیبی از این سه هستند.", size=12,
         color=(0x45, 0x46, 0x40), align=RL)
    mono(s, 0.75, 6.26, 4.0, 0.24, "SUPERVISED / UNSUPERVISED / RL", size=8, color=GRAY, align=LC,
         tracking=1.2)
    finish(s, [], "PARADIGMS", num, total)


def s_supervised(s, num, total):
    P.head(s, LAB + " / SUPERVISED", "یادگیری نظارت‌شده در عمل", size=32, w=9.6)
    # scatter visual
    bx, by, bw, bh = 0.90, 2.35, 4.10, 3.55
    rect(s, bx, by, bw, bh, (0xEE, 0xEA, 0xDD))
    line(s, bx, by + bh, bx + bw, by + bh, INK, 1.2)
    line(s, bx, by, bx, by + bh, INK, 1.2)
    pts_a = [(1.45, 5.35), (1.70, 5.10), (1.95, 5.35), (2.10, 4.95), (2.30, 5.20), (2.45, 4.80),
             (1.55, 4.80), (1.85, 4.65), (2.20, 4.55), (2.60, 5.00), (2.05, 4.35), (1.30, 5.05),
             (2.70, 4.60), (1.65, 4.30)]
    pts_b = [(3.35, 3.15), (3.60, 3.40), (3.85, 3.10), (4.05, 3.55), (4.25, 3.05), (4.40, 3.45),
             (3.45, 2.95), (3.75, 2.70), (4.10, 2.80), (4.55, 3.15), (3.90, 2.55), (3.25, 3.55),
             (4.30, 2.65), (3.50, 3.75)]
    for x, y in pts_a:
        rect(s, x, y, 0.13, 0.13, LIME, shape=MSO_SHAPE.OVAL)
    for x, y in pts_b:
        rect(s, x, y, 0.13, 0.13, INK, shape=MSO_SHAPE.OVAL)
    line(s, 3.05, 3.05, 2.35, 5.75, INK, 1.6)
    text(s, 0.98, 2.45, 2.0, 0.24, "مرز تصمیم (Decision Boundary)", size=8.5, color=GRAY, align=LC)
    mono(s, 3.95, 5.62, 1.0, 0.2, "x1", size=8, color=GRAY, align=LC)
    mono(s, 0.98, 2.72, 1.0, 0.2, "x2", size=8, color=GRAY, align=LC)
    text(s, 3.25, 5.35, 1.6, 0.28, "کلاس B", size=10, bold=True, color=INK, align=LC)
    text(s, 1.35, 3.95, 1.4, 0.28, "کلاس A", size=10, bold=True, color=INK, align=LC)
    # right text
    P.bullets(s, 5.35, 2.18, 7.15, [
        ("تعریف", "مدل از نمونه‌های برچسب‌دار یاد می‌گیرد و برای داده‌ی جدید پیش‌بینی می‌کند."),
        ("دو نوع اصلی", "طبقه‌بندی (برچسب گسسته) و رگرسیون (عدد پیوسته)."),
        ("تقسیم داده", "Train / Validation / Test — هرگز روی داده‌ی آموزش ارزیابی نکنید."),
        ("معیارها", "Accuracy، Precision/Recall، F1، ROC-AUC، MAE و RMSE."),
        ("خطر اصلی", "Overfitting: حفظ کردن داده‌ی آموزش به‌جای یادگیری الگوی واقعی."),
    ], size=12.5, gap=0.16)
    finish(s, [], "SUPERVISED", num, total)


def s_unsupervised(s, num, total):
    P.head(s, LAB + " / UNSUPERVISED", "کشف ساختار بدون برچسب", size=32, w=9.8)
    bx, by, bw, bh = 0.90, 2.30, 4.20, 3.75
    rect(s, bx, by, bw, bh, INK, radius=0.05)
    clusters = [
        ((1.70, 3.10), LIME, "C1"), ((3.55, 3.05), (0xE9, 0xE5, 0xD9), "C2"), ((2.70, 4.95), (0x8A, 0x8A, 0x84), "C3"),
    ]
    pts = [[(1.55,2.95),(1.85,3.25),(1.95,2.85),(1.45,3.30),(1.75,3.55),(2.05,3.10)],
           [(3.40,2.90),(3.70,3.20),(3.85,2.85),(3.30,3.30),(3.60,3.55),(3.95,3.10)],
           [(2.55,4.80),(2.85,5.05),(2.95,4.70),(2.45,5.15),(2.75,5.35),(3.05,4.95)]]
    for (c, col, name), ps in zip(clusters, pts):
        for x, y in ps:
            rect(s, x, y, 0.12, 0.12, col, shape=MSO_SHAPE.OVAL)
        text(s, c[0] - 0.3, c[1] + 0.42, 0.6, 0.24, name, size=8, color=col, align=CT, font=MONO, rtl=False)
        rect(s, c[0] - 0.02, c[1] - 0.02, 0.07, 0.07, LIME, shape=MSO_SHAPE.OVAL)
    text(s, 0.98, 5.72, 3.9, 0.24, "داده‌ی بدون برچسب؛ مدل خودش گروه‌ها را می‌سازد.", size=9,
         color=(0xC9, 0xCA, 0xC0), align=LC)
    P.bullets(s, 5.45, 2.15, 7.05, [
        ("خوشه‌بندی", "K-Means، DBSCAN، خوشه‌بندی سلسله‌مراتبی — تقسیم مشتریان، بازار و اسناد."),
        ("کاهش ابعاد", "PCA، t-SNE و UMAP برای ساده‌سازی و مصورسازی داده‌های پرابعاد."),
        ("تشخیص ناهنجاری", "پیدا کردن تراکنش مشکوک یا قطعه‌ی معیوب بدون نمونه‌ی برچسب‌دار."),
        ("Embedding", "تبدیل متن، تصویر و صدا به بردار؛ پایه‌ی جستجوی معنایی و RAG."),
    ], size=12.5, gap=0.17)
    text(s, 5.45, 6.02, 7.0, 0.5, "نکته: پیش‌آموزش LLM هم بدون برچسب انسانی است؛ هدف «پیش‌بینی توکن بعدی» خودش برچسب می‌سازد.",
         size=10.5, color=GRAY, align=RL, line_spacing=1.4)
    finish(s, [], "UNSUPERVISED", num, total)


def s_rl(s, num, total):
    P.head(s, LAB + " / REINFORCEMENT LEARNING", "یادگیری از پاداش و خطا", size=31, w=10.4)
    ax, ay, aw, ah = 2.25, 3.30, 2.15, 0.85
    ex, ey, ew, eh = 2.25, 5.55, 2.15, 0.85
    P.node(s, ax, ay, aw, ah, "عامل / Agent", fill=INK, fg=CREAM, size=12.5, ic=None)
    P.node(s, ex, ey, ew, eh, "محیط / Environment", fill=None, fg=INK, border=INK, size=12.5)
    P.arrow(s, ax + 0.35, ay + ah, ax + 0.35, ey - 0.04, INK, 1.4)
    P.arrow(s, ax + aw - 0.35, ey - 0.04, ax + aw - 0.35, ay + ah, INK, 1.4)
    text(s, ax - 1.02, 4.38, 1.3, 0.26, "Action", size=9.5, color=GRAY, align=CT, font=MONO, rtl=False)
    text(s, ax + aw - 0.15, 4.30, 1.55, 0.45, "State + Reward", size=9, color=GRAY, align=LC, font=MONO, rtl=False)
    rect(s, ax + 0.02, ay + ah + 0.20, 0.9, 0.30, LIME)
    text(s, ax + 0.02, ay + ah + 0.255, 0.9, 0.22, "r = +1", size=8.5, bold=True, color=INK, align=CT, font=MONO, rtl=False)
    mono(s, 0.95, 2.98, 4.4, 0.24, "AGENT–ENVIRONMENT LOOP", size=8, color=GRAY, align=LC, tracking=1.4)
    # right column
    P.bullets(s, 5.30, 2.20, 7.15, [
        ("سیاست (Policy)", "استراتژی عامل برای انتخاب اقدام در هر حالت."),
        ("پاداش (Reward)", "سیگنالی که درست و غلط را، با تأخیر، مشخص می‌کند."),
        ("کاوش در برابر بهره‌برداری", "آزمودن گزینه‌های جدید در برابر استفاده از بهترین گزینه‌ی فعلی."),
        ("RLHF", "مدل زبانی با بازخورد انسانی تنظیم می‌شود؛ همان‌جا که «مؤدب و مفید بودن» یاد گرفته می‌شود."),
    ], size=12.5, gap=0.18)
    text(s, 5.30, 5.90, 7.1, 0.5, "مثال‌ها: بازی‌های استراتژیک، رباتیک، کنترل ترافیک، بهینه‌سازی تبلیغات و آموزش مدل‌های استدلالی.",
         size=10.5, color=GRAY, align=RL, line_spacing=1.4)
    finish(s, [], "REINFORCEMENT LEARNING", num, total)


def s_deep(s, num, total):
    P.head(s, LAB + " / DEEP LEARNING", "شبکه‌های عصبی: لایه به لایه", size=32, w=10.0)
    layers = [4, 6, 6, 3]
    xs = [1.15, 2.15, 3.15, 4.15]
    ys = []
    for li, n in enumerate(layers):
        total_h = 2.55
        gap = total_h / (n - 1) if n > 1 else 0
        ys.append([3.55 - total_h / 2 + k * gap for k in range(n)])
    for li in range(3):
        for y1 in ys[li]:
            for y2 in ys[li + 1]:
                line(s, xs[li] + 0.10, y1 + 0.10, xs[li + 1], y2 + 0.10, (0xCE, 0xCA, 0xBE), 0.6)
    # highlight path
    path = [0, 2, 3, 1]
    for li in range(3):
        line(s, xs[li] + 0.10, ys[li][path[li]] + 0.10, xs[li + 1], ys[li + 1][path[li + 1]] + 0.10, LIME, 2.2)
    for li, xx in enumerate(xs):
        for yy in ys[li]:
            rect(s, xx, yy, 0.20, 0.20, INK, shape=MSO_SHAPE.OVAL)
    for li, lab in enumerate(["ورودی", "پنهان ۱", "پنهان ۲", "خروجی"]):
        text(s, xs[li] - 0.35, 6.30, 0.95, 0.24, lab, size=9, color=GRAY, align=CT)
    mono(s, 0.95, 2.80, 4.4, 0.24, "INPUT → HIDDEN → OUTPUT", size=8, color=GRAY, align=LC, tracking=1.2)
    # right
    P.bullets(s, 5.35, 2.15, 7.10, [
        ("ایده‌ی اصلی", "هر لایه نمایشی انتزاعی‌تر از داده می‌سازد: لبه → بافت → شیء → مفهوم."),
        ("آموزش", "وزن‌ها با گرادیان کاهشی و الگوریتم Backpropagation تنظیم می‌شوند."),
        ("چرا حالا؟", "سه چیز هم‌زمان رسید: داده‌ی عظیم، GPUهای قدرتمند و الگوریتم‌های بهتر."),
    ], size=12.5, gap=0.17)
    # stat band
    rect(s, 5.35, 5.55, 7.15, 0.95, (0xEC, 0xE8, 0xDC))
    text(s, 5.60, 5.70, 1.55, 0.55, "۲۰۱۲", size=22, bold=True, color=INK, align=LC, font=MONO, rtl=False)
    text(s, 7.15, 5.72, 5.15, 0.62, "AlexNet خطای ImageNet را از ۲۶٪ به ۱۵٪ رساند؛ نقطه‌ی شروع انقلاب عمیق.",
         size=10.5, color=(0x3C, 0x3D, 0x37), align=RL, line_spacing=1.35)
    finish(s, [], "DEEP LEARNING", num, total)
