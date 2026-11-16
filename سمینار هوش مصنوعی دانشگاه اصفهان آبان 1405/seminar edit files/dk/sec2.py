# -*- coding: utf-8 -*-
"""Section 2 — LLMs, Transformers, prompt engineering."""
from pptx.enum.shapes import MSO_SHAPE
from .theme import (W, H, M, CREAM, INK, LIME, GRAY, MONO, RL, LC, CT,
                    rect, line, text, mono, icon, icon_at, stamp)
from . import parts as P
from . import covers, anim, decor

LAB = "02 / LLM"


def finish(s, shapes, label, num, total):
    stamp(s, label, num, total)
    anim.transition(s)
    anim.animate(s, shapes)


def s_div2(s, num, total):
    covers.divider(s, 2, "مدل‌های زبانی بزرگ", "LARGE LANGUAGE MODELS / TRAINING / LIMITS",
                   "این ماشین‌ها دقیقاً چه می‌کنند؟ چگونه آموزش می‌بینند و چرا گاهی اشتباه می‌گویند؟",
                   "mesh_dark", num, total)


def s_llm(s, num, total):
    P.head(s, LAB + " / NEXT-TOKEN PREDICTION", "مدل زبانی چگونه «فکر» می‌کند؟", size=32, w=10.4)
    px, py, pw, ph = 0.85, 2.18, 4.75, 4.35
    rect(s, px, py, pw, ph, INK, radius=0.06)
    mono(s, px + 0.28, py + 0.22, 3.0, 0.22, "PROMPT", size=8, color=LIME, align=LC, tracking=1.6)
    text(s, px + 0.28, py + 0.48, pw - 0.56, 0.6, "هوا سرد است، باید ...", size=15, color=CREAM, align=RL)
    line(s, px + 0.28, py + 1.10, px + pw - 0.28, py + 1.10, (0x3C, 0x3E, 0x37), 1.0)
    mono(s, px + 0.28, py + 1.22, 4.0, 0.2, "P(next token | context)", size=8, color=GRAY, align=LC, tracking=1)
    cands = [("کاپشن", 0.62), ("چای", 0.17), ("برویم", 0.09), ("بخاری", 0.07), ("بخوابیم", 0.05)]
    by = py + 1.62
    for label, p in cands:
        top = p == 0.62
        text(s, px + 2.95, by, 1.45, 0.28, label, size=11.5, bold=top, color=CREAM if top else (0xB9, 0xBA, 0xB1), align=RL)
        rect(s, px + 0.72, by + 0.06, 2.10, 0.20, (0x2A, 0x2C, 0x27))
        rect(s, px + 0.72, by + 0.06, 2.10 * p, 0.20, LIME if top else (0x6E, 0x7A, 0x4E))
        mono(s, px + 0.25, by + 0.03, 0.45, 0.24, "%d%%" % round(p * 100), size=9,
             color=LIME if top else GRAY, align=LC)
        by += 0.50
    text(s, px + 0.28, py + 4.00, pw - 0.56, 0.24, "مدل فقط احتمال توکن بعدی را می‌دهد؛ بقیه‌اش تکرار است.",
         size=8.5, color=GRAY, align=RL)
    P.bullets(s, 5.95, 2.18, 6.55, [
        ("یک تابع احتمال", "مدل برای هر توکن بعدی یک احتمال می‌دهد و از میان آن نمونه‌گیری می‌کند."),
        ("آموزش ساده، نتیجه‌ی پیچیده", "همین هدف ساده روی تریلیون‌ها کلمه، توانایی ترجمه، استدلال و کدنویسی می‌سازد."),
        ("فشرده‌سازی، نه حافظه", "مدل متن را ذخیره نمی‌کند؛ الگوهای آماری زبان را در وزن‌ها فشرده می‌کند."),
        ("زنجیره‌ی احتمال", "هر توکن به توکن‌های قبلی مشروط است؛ به همین دلیل جمله منسجم می‌شود."),
    ], size=12.5, gap=0.16)
    finish(s, [], "HOW LLMs WORK", num, total)


def s_training(s, num, total):
    P.head(s, LAB + " / TRAINING PIPELINE", "یک مدل زبانی چگونه آموزش می‌بیند؟", size=32, w=11.0)
    items = [
        dict(num="01", ic="book-open", title="پیش‌آموزش (Pretraining)",
             body="پیش‌بینی توکن بعدی روی تریلیون‌ها توکن از وب، کتاب و کد.\nنتیجه: دانش زبانی و جهانی.\nهزینه: بیشترین بخش محاسبات."),
        dict(num="02", ic="message-square", title="تنظیم دستور (SFT)",
             body="آموزش روی جفت‌های «دستور–پاسخ» نوشته‌شده توسط انسان.\nنتیجه: مدل یاد می‌گیرد دستور را بفهمد و پاسخ دهد."),
        dict(num="03", ic="shield", title="هم‌ترازی (RLHF / DPO)",
             body="انسان پاسخ‌ها را رتبه‌بندی می‌کند؛ مدل مؤدب‌تر، مفیدتر و امن‌تر می‌شود.\nConstitutional AI همین کار را با قواعد می‌کند."),
    ]
    P.cards_row(s, 0.75, 2.22, 11.85, 3.35, items, gap=0.22)
    # arrows between cards
    for x in (4.38, 8.30):
        P.arrow(s, x + 0.30, 3.90, x - 0.30, 3.90, INK, 1.2)
    line(s, 0.75, 5.95, 12.60, 5.95, (0xD5, 0xD1, 0xC4), 1.0)
    text(s, 6.55, 6.07, 6.05, 0.5, "دانش از پیش‌آموزش می‌آید، رفتار از هم‌ترازی.", size=12.5, bold=True, align=RL)
    text(s, 0.80, 6.08, 5.55, 0.5, "به همین دلیل دو مدل با دانش مشابه می‌توانند لحن و سیاست کاملاً متفاوتی داشته باشند.",
         size=9.5, color=GRAY, align=RL)
    finish(s, [], "TRAINING", num, total)


def s_scale(s, num, total):
    P.head(s, LAB + " / SCALE", "بزرگ‌شدن، چه چیزی را عوض کرد؟", size=32, w=10.2)
    stats = [("175B", "پارامتر GPT-3", "۲۰۲۰"), ("~15T", "توکن آموزش (تقریبی)", "مدل‌های Frontier"),
             ("100K+", "GPU در یک خوشه‌ی آموزش", "تقریبی"), ("M$", "هزینه‌ی یک دور آموزش", "بسته به مدل")]
    for i, (v, l, note) in enumerate(stats):
        x = 12.55 - i * 2.95 - 2.75
        P.stat(s, x, 2.05, 2.65, v, l, note, size=30, color=INK)
        if i:
            line(s, x + 2.85, 2.10, x + 2.85, 3.05, (0xD6, 0xD2, 0xC6), 0.9)
    # chart
    cx, cy, cw, ch = 0.95, 3.65, 6.15, 2.65
    line(s, cx, cy + ch, cx + cw, cy + ch, INK, 1.1)
    line(s, cx, cy, cx, cy + ch, INK, 1.1)
    pts = [(0.10, 0.10), (0.28, 0.18), (0.46, 0.34), (0.62, 0.52), (0.76, 0.68), (0.90, 0.88)]
    xy = [(cx + cw * a, cy + ch * (1 - b)) for a, b in pts]
    for i in range(len(xy) - 1):
        line(s, xy[i][0], xy[i][1], xy[i + 1][0], xy[i + 1][1], LIME, 3.2)
    for x, y in xy:
        rect(s, x - 0.055, y - 0.055, 0.11, 0.11, INK, shape=MSO_SHAPE.OVAL)
    mono(s, cx + 0.10, cy - 0.28, 3.0, 0.22, "CAPABILITY", size=7.5, color=GRAY, align=LC, tracking=1.2)
    mono(s, cx + cw - 1.5, cy + ch + 0.10, 1.5, 0.22, "COMPUTE →", size=7.5, color=GRAY, align=RL, tracking=1.2)
    text(s, cx + 0.10, cy + ch + 0.36, 5.9, 0.24, "نمودار شماتیک؛ رابطه‌ی توانایی با مقیاس آموزش", size=8, color=GRAY, align=LC)
    P.bullets(s, 7.35, 3.55, 5.20, [
        ("قانون مقیاس", "با افزایش داده، پارامتر و محاسبه، خطا به‌صورت قابل پیش‌بینی کم می‌شود."),
        ("درس Chinchilla", "توازن داده و پارامتر مهم‌تر از بزرگ‌کردن بی‌قاعده است."),
        ("امروز", "کیفیت داده، استدلال و پس‌آموزش مهم‌تر از صرفاً تعداد پارامتر شده است."),
    ], size=11.5, gap=0.14)
    finish(s, [], "SCALE", num, total)


def s_limits(s, num, total):
    P.head(s, LAB + " / LIMITS", "مدل زبانی چه کارهایی را خوب انجام نمی‌دهد؟", size=31, w=11.2)
    items = [
        dict(ic="alert-triangle", title="توهم‌زایی (Hallucination)",
             body="با لحن مطمئن، واقعیت جعلی می‌سازد؛ منبع، عدد یا نقل‌قول را از خودش درمی‌آورد."),
        dict(ic="clock", title="دانش تا تاریخ قطع",
             body="از رویدادهای بعد از آموزش بی‌خبر است، مگر با جستجو یا ابزار به داده‌ی تازه وصل شود."),
        dict(ic="calculator", title="استدلال و ریاضی",
             body="در محاسبات چندمرحله‌ای خطا می‌کند؛ برای عدد و منطق، ابزار و بررسی گام‌به‌گام لازم است."),
        dict(ic="lock", title="حریم خصوصی و امنیت",
             body="ورودی ممکن است ثبت شود؛ داده‌ی حساس، رمز و اطلاعات مشتری را وارد نکنید."),
    ]
    for i, it in enumerate(items):
        x = 6.62 if i % 2 == 0 else 0.75
        y = 2.10 if i < 2 else 4.05
        P.card(s, x, y, 5.88, 1.78, ic=it["ic"], title=it["title"], body=it["body"],
               variant="line", title_size=14, body_size=10.5)
    rect(s, 0.75, 6.02, 11.85, 0.62, LIME)
    text(s, 0.95, 6.17, 11.45, 0.34, "مدل زبانی موتور جستجو نیست؛ یک موتور استدلال احتمالی است. خروجی را همیشه راستی‌آزمایی کنید.",
         size=12, bold=True, color=INK, align=RL)
    finish(s, [], "LIMITS", num, total)


def s_div3(s, num, total):
    covers.divider(s, 3, "زبان، Attention و Transformer",
                   "TOKENS / EMBEDDINGS / SELF-ATTENTION / CONTEXT",
                   "چطور یک سری عدد، معنا و رابطه را یاد می‌گیرند؟\nقلب ماجرا در مکانیزم Attention است.",
                   "tunnel", num, total)


def s_tokens(s, num, total):
    P.head(s, LAB + " / TOKENIZATION", "زبان برای مدل، توکن است نه کلمه", size=31, w=10.8)
    text(s, 6.05, 2.02, 6.45, 0.55, "مدل متن را به قطعه‌های کوچک (توکن) می‌شکند؛ هر توکن یک عدد است.",
         size=12.5, color=(0x3E, 0x3F, 0x39), align=RL)
    # English tokens
    mono(s, 0.90, 2.75, 4.0, 0.22, "ENGLISH", size=8, color=GRAY, align=LC, tracking=1.4)
    x = 0.90
    for t in ["un", "believ", "able"]:
        w = P.tw(t, 19) / 72 + 0.36
        rect(s, x, 3.02, w, 0.52, CREAM, line=INK, lw=1.0, radius=0.06)
        text(s, x, 3.13, w, 0.3, t, size=19, color=INK, align=CT, font=MONO, rtl=False)
        x += w + 0.10
    mono(s, x + 0.10, 3.14, 1.2, 0.24, "= 3 tokens", size=9, color=GRAY, align=LC)
    # Persian tokens
    mono(s, 0.90, 3.85, 4.0, 0.22, "PERSIAN", size=8, color=GRAY, align=LC, tracking=1.4)
    x = 0.90
    for t in ["هوش", "مصنوعی", "زبان", "ما"]:
        w = P.tw(t, 15) / 72 + 0.32
        rect(s, x, 4.12, w, 0.48, LIME, radius=0.06)
        text(s, x, 4.22, w, 0.3, t, size=15, color=INK, align=CT)
        x += w + 0.08
    text(s, 0.90, 4.72, 4.5, 0.24, "فارسی اغلب به بایت‌های بیشتری شکسته می‌شود؛", size=9, color=GRAY, align=LC)
    text(s, 0.90, 4.96, 4.5, 0.24, "یعنی هزینه و مصرف توکن بیشتر.", size=9, color=GRAY, align=LC)
    # ids panel
    rect(s, 0.90, 5.42, 4.42, 1.10, INK, radius=0.05)
    mono(s, 1.10, 5.56, 4.0, 0.22, "سلام دنیا  →  [32412, 8812, 219]", size=10.5, color=LIME, align=LC)
    mono(s, 1.10, 5.86, 4.0, 0.22, "tokens  →  ids  →  vectors", size=9, color=GRAY, align=LC)
    # right notes
    P.bullets(s, 6.05, 2.78, 6.45, [
        ("چرا توکن؟", "مدل با کلمه کار نمی‌کند؛ با واحدهای آماری کار می‌کند که واژگان را کوچک نگه می‌دارند."),
        ("واژگان", "معمولاً ۵۰ تا ۲۰۰ هزار توکن؛ کلمات رایج یک توکن، کلمات کمیاب چند توکن."),
        ("پیامد عملی", "متن فارسی و کد طولانی، توکن بیشتری مصرف می‌کنند؛ در هزینه و Context حساب کنید."),
        ("اعداد", "مدل اعداد را هم توکن‌به‌توکن می‌بیند؛ به همین دلیل محاسبه‌ی دقیق سخت است."),
    ], size=12, gap=0.15)
    finish(s, [], "TOKENS", num, total)


def s_embedding(s, num, total):
    P.head(s, LAB + " / EMBEDDINGS", "معنا، یک موقعیت در فضا است", size=32, w=10.4)
    bx, by, bw, bh = 0.88, 2.25, 4.55, 4.05
    rect(s, bx, by, bw, bh, (0xEE, 0xEA, 0xDD))
    for i in range(1, 4):
        line(s, bx + i * bw / 4, by, bx + i * bw / 4, by + bh, (0xE2, 0xDE, 0xD1), 0.8)
        line(s, bx, by + i * bh / 4, bx + bw, by + i * bh / 4, (0xE2, 0xDE, 0xD1), 0.8)
    pts = {
        "مرد": (1.55, 4.95), "زن": (2.55, 4.95), "پادشاه": (1.55, 3.45), "ملکه": (2.55, 3.45),
        "تهران": (3.85, 3.20), "پاریس": (4.55, 2.85), "گربه": (3.55, 5.45), "سگ": (4.30, 5.55),
    }
    for w, (x, y) in pts.items():
        rect(s, x - 0.05, y - 0.05, 0.10, 0.10, INK, shape=MSO_SHAPE.OVAL)
        text(s, x - 0.38, y + 0.06, 0.85, 0.24, w, size=9, color=INK, align=CT)
    P.arrow(s, 1.62, 4.85, 2.55, 4.85, LIME, 2.0)
    P.arrow(s, 1.62, 3.35, 2.55, 3.35, LIME, 2.0)
    text(s, 1.30, 3.05, 1.6, 0.22, "بردار جنسیت", size=8, color=(0x6C, 0x72, 0x4A), align=LC)
    mono(s, bx + 0.12, by + bh - 0.28, 3.2, 0.2, "SEMANTIC SPACE / 2D", size=7.5, color=GRAY, align=LC, tracking=1)
    P.bullets(s, 5.85, 2.20, 6.65, [
        ("بردار معنایی", "هر کلمه یا جمله به یک بردار چندصد‌بعدی تبدیل می‌شود؛ کلمات هم‌معنا نزدیک‌ترند."),
        ("شباهت کسینوسی", "فاصله‌ی زاویه‌ای بردارها معیار شباهت معنایی است."),
        ("جستجوی معنایی", "جستجو دیگر روی کلمه نیست؛ روی معناست — پایه‌ی RAG و حافظه‌ی ایجنت."),
        ("حساب برداری", "پادشاه − مرد + زن ≈ ملکه؛ معنای رابطه‌ها در هندسه‌ی فضا کد می‌شود."),
    ], size=12, gap=0.16)
    finish(s, [], "EMBEDDINGS", num, total)


def s_transformer(s, num, total):
    P.head(s, LAB + " / TRANSFORMER", "معماری Transformer: یک انقلاب ۲۰۱۷", size=31, w=11.2)
    # stack diagram
    dx, dw = 0.95, 4.35
    y = 2.10
    def blk(txt, h=0.42, fill=None, fg=INK, sub=None):
        nonlocal y
        rect(s, dx, y, dw, h, fill, line=None if fill else (0xB6, 0xB2, 0xA5), lw=1.0, radius=0.04)
        text(s, dx + 0.10, y + 0.07, dw - 0.20, h - 0.08, txt, size=9.5, bold=True, color=fg, align=CT,
             font=MONO, rtl=False)
        y += h + 0.10
    blk("Output probabilities", 0.34)
    blk("Linear + Softmax", 0.34)
    # big block
    by0 = y
    rect(s, dx, by0, dw, 1.72, None, line=INK, lw=1.4, radius=0.04)
    mono(s, dx + 0.12, by0 + 0.10, 3.0, 0.2, "DECODER BLOCK  × N", size=7.5, color=INK, align=LC, tracking=1.2)
    inner = [("Multi-Head Self-Attention", LIME), ("Add & Norm", None),
             ("Feed Forward (MLP)", None), ("Add & Norm", None)]
    yy = by0 + 0.38
    for t, f in inner:
        hh = 0.26
        if f:
            rect(s, dx + 0.30, yy, dw - 0.60, hh, f, radius=0.03)
        else:
            rect(s, dx + 0.30, yy, dw - 0.60, hh, None, line=(0xB6, 0xB2, 0xA5), lw=0.8, radius=0.03)
        text(s, dx + 0.34, yy + 0.035, dw - 0.68, 0.2, t, size=7.5, color=INK, align=CT, font=MONO, rtl=False)
        yy += hh + 0.08
    y = by0 + 1.72 + 0.10
    blk("Positional Encoding  (+)", 0.34)
    blk("Token Embedding", 0.34)
    blk("Input tokens", 0.34, fill=INK, fg=CREAM)
    mono(s, dx, 6.63, 4.4, 0.2, "DECODER-ONLY (GPT-STYLE)", size=7.5, color=GRAY, align=LC, tracking=1)
    # right
    P.bullets(s, 5.55, 2.10, 6.95, [
        ("بدون بازگشت (No RNN)", "کل جمله هم‌زمان پردازش می‌شود؛ آموزش موازی و بسیار سریع‌تر."),
        ("Self-Attention", "هر توکن به همه‌ی توکن‌ها نگاه می‌کند و وزن ارتباط را یاد می‌گیرد."),
        ("Positional Encoding", "چون ترتیب ذاتی نیست، موقعیت توکن‌ها به بردار اضافه می‌شود."),
        ("پشته‌ی لایه‌ها", "ده‌ها بلوک روی هم؛ هر بلوک نمایش را غنی‌تر می‌کند."),
        ("میراث", "GPT، Claude، Gemini، Llama و تقریباً همه‌ی مدل‌های امروز از این معماری می‌آیند."),
    ], size=11.5, gap=0.13)
    finish(s, [], "TRANSFORMER", num, total)


def s_attention(s, num, total):
    P.head(s, LAB + " / SELF-ATTENTION", "Attention: مدل کجا را نگاه می‌کند؟", size=31, w=10.8)
    art = decor.ensure_art(["attention"])["attention"]
    P.picture(s, art, 0.92, 2.22, 4.35, 3.05, frame=INK, fw=1.0)
    mono(s, 0.92, 5.36, 4.3, 0.2, "ATTENTION WEIGHTS / SCHEMATIC", size=7.5, color=GRAY, align=LC, tracking=1)
    text(s, 0.92, 5.62, 4.35, 0.8, "هر خانه: میزان توجه یک توکن به توکن دیگر. ردیف‌های روشن‌تر = توجه بیشتر.",
         size=8.5, color=GRAY, align=LC, line_spacing=1.5)
    # example
    rect(s, 5.55, 2.18, 7.05, 1.28, (0xEE, 0xEA, 0xDD))
    text(s, 5.72, 2.32, 6.7, 0.35, "The animal didn’t cross the street because it was too tired.",
         size=12.5, color=INK, align=LC, font=MONO, rtl=False)
    text(s, 5.72, 2.78, 6.7, 0.4, "«it» به animal اشاره می‌کند، نه street — و Attention همین را کشف می‌کند.",
         size=10.5, color=(0x4A, 0x4B, 0x45), align=RL)
    # QKV chips
    for i, (t, d) in enumerate([("Q", "چه می‌خواهم؟"), ("K", "چه دارم؟"), ("V", "چه می‌دهم؟")]):
        x = 11.55 - i * 2.05
        rect(s, x, 3.66, 0.52, 0.52, LIME)
        text(s, x, 3.76, 0.52, 0.3, t, size=14, bold=True, color=INK, align=CT, font=MONO, rtl=False)
        text(s, x - 0.42, 4.24, 1.4, 0.24, d, size=8, color=GRAY, align=CT)
    P.bullets(s, 5.55, 4.58, 7.05, [
        ("چند سر (Multi-Head)", "هر سر به نوعی رابطه نگاه می‌کند: دستوری، معنایی، مکانی."),
        ("وزن‌دهی پویا", "وزن‌ها برای هر ورودی دوباره محاسبه می‌شوند؛ زمینه، معنا را عوض می‌کند."),
        ("هزینه", "با طول متن، محاسبه درجه‌دو رشد می‌کند — دلیل اهمیت Context و معماری‌های بهینه."),
    ], size=11, gap=0.10)
    finish(s, [], "ATTENTION", num, total)


def s_gpt(s, num, total):
    P.head(s, LAB + " / GPT LOOP", "GPT چگونه جمله می‌سازد؟", size=32, w=9.8)
    # loop diagram
    cx, cy = 3.10, 4.35
    boxes = [
        (0.95, 2.25, 2.55, 0.62, "پرامپت + متن تا اینجا"),
        (0.95, 5.85, 2.55, 0.62, "خروجی نهایی"),
        (4.30, 2.25, 2.05, 0.62, "پردازش مدل"),
        (4.30, 5.85, 2.05, 0.62, "افزودن توکن"),
    ]
    P.node(s, boxes[0][0], boxes[0][1], boxes[0][2], boxes[0][3], "پرامپت + متن", fill=INK, fg=CREAM, size=10.5)
    P.node(s, boxes[2][0], boxes[2][1], boxes[2][2], boxes[2][3], "پردازش مدل", fill=None, border=INK, size=10.5)
    P.node(s, boxes[3][0], boxes[3][1], boxes[3][2], boxes[3][3], "نمونه‌گیری توکن", fill=LIME, size=10)
    P.node(s, boxes[1][0], boxes[1][1], boxes[1][2], boxes[1][3], "تکرار تا پایان", fill=None, border=INK, size=10.5)
    P.arrow(s, 3.55, 2.87, 4.25, 2.50, INK, 1.3)
    P.arrow(s, 5.10, 2.87, 5.10, 5.80, INK, 1.3)
    P.arrow(s, 4.25, 6.16, 3.55, 6.16, INK, 1.3)
    P.arrow(s, 1.95, 5.80, 1.95, 2.92, INK, 1.3)
    text(s, 3.62, 2.40, 0.7, 0.2, "", size=8)
    mono(s, 0.95, 2.00, 5.4, 0.2, "AUTOREGRESSIVE LOOP", size=8, color=GRAY, align=LC, tracking=1.4)
    P.bullets(s, 6.95, 2.15, 5.55, [
        ("خودرگرسیو", "هر بار یک توکن تولید می‌شود و به ورودی بعدی اضافه می‌شود."),
        ("دما (Temperature)", "پایین = محافظه‌کار و قابل تکرار؛ بالا = خلاق و متنوع."),
        ("Top-p / Top-k", "از میان محتمل‌ترین توکن‌ها نمونه‌گیری می‌کند تا خروجی بی‌معنا نشود."),
        ("توقف", "مدل یاد گرفته کجا تمام کند؛ یا با محدودیت طول متوقف می‌شود."),
    ], size=11.5, gap=0.15)
    # mini code
    rect(s, 6.95, 5.86, 5.45, 0.82, INK, radius=0.05)
    mono(s, 7.15, 5.97, 5.05, 0.2, "while not done:", size=8.5, color=LIME, align=LC)
    mono(s, 7.35, 6.20, 5.05, 0.2, "tok = model(context); context += tok", size=8.5, color=(0xD5, 0xD7, 0xCC), align=LC)
    finish(s, [], "GPT LOOP", num, total)


def s_context(s, num, total):
    P.head(s, LAB + " / CONTEXT WINDOW", "Context Window: حافظه‌ی کاری مدل", size=31, w=10.9)
    text(s, 6.05, 2.02, 6.5, 0.4, "همه‌چیز باید داخل این پنجره جا شود: دستور، تاریخچه، اسناد و پاسخ.",
         size=11.5, color=(0x3E, 0x3F, 0x39), align=RL)
    bx, by, bw, bh = 0.90, 2.52, 11.65, 0.92
    segs = [("System", 0.09, (0x8A, 0x8A, 0x84)), ("گفتگو", 0.30, (0x2E, 0x30, 0x2A)),
            ("اسناد / RAG", 0.43, LIME), ("پاسخ", 0.18, (0xC9, 0xC5, 0xB8))]
    x = bx + bw
    for name, frac, col in segs:
        w = bw * frac
        x -= w
        rect(s, x, by, w, bh, col)
        text(s, x, by + 0.30, w, 0.32, name, size=10, bold=True,
             color=INK if col == LIME else (CREAM if col != (0xC9, 0xC5, 0xB8) else INK), align=CT)
    # token ruler
    for i in range(0, 12):
        xx = bx + bw * i / 11
        line(s, xx, by + bh, xx, by + bh + 0.09, (0xB9, 0xB5, 0xA8), 0.8)
        mono(s, xx - 0.35, by + bh + 0.13, 0.7, 0.2, "%dK" % (i * 10), size=6.5, color=GRAY, align=CT)
    stats = [("4K", "GPT-3", "۲۰۲۰"), ("128K", "GPT-4", "2023"), ("200K", "Claude", "2023"), ("1M+", "Gemini / Claude", "2024+")]
    for i, (v, l, y) in enumerate(stats):
        x = 12.55 - i * 2.95 - 2.75
        P.stat(s, x, 4.18, 2.65, v, l, y, size=28, color=INK)
        if i:
            line(s, x + 2.85, 4.25, x + 2.85, 5.05, (0xD6, 0xD2, 0xC6), 0.9)
    line(s, 0.90, 5.60, 12.55, 5.60, (0xD6, 0xD2, 0xC6), 1.0)
    P.bullets(s, 0.90, 5.75, 11.55, [
        ("پنجره‌ی بزرگ‌تر ≠ دقت بیشتر", "مدل در وسط متن طولانی اطلاعات را گم می‌کند (Lost in the Middle)."),
        ("هزینه و سرعت", "هر توکن ورودی پول و زمان می‌برد؛ خلاصه‌سازی و RAG هوشمند، ارزان‌تر از پر کردن پنجره است."),
    ], size=10.5, gap=0.06)
    finish(s, [], "CONTEXT WINDOW", num, total)


# ---------------------------------------------------------------- prompting
def s_div4(s, num, total):
    covers.divider(s, 4, "هنر استفاده از هوش مصنوعی",
                   "PROMPT ENGINEERING / TECHNIQUES / PRACTICE",
                   "همان مدل، با پرامپت بهتر، خروجی کاملاً متفاوتی می‌دهد.\nاین بخش، مهارتِ تبدیل خواسته به دستور است.",
                   "halftone", num, total)


def s_why_prompt(s, num, total):
    P.head(s, "04 / PROMPT / WHY", "چرا پرامپت مهم است؟", size=33, w=9.6)
    # weak
    rect(s, 0.85, 2.15, 5.72, 3.55, None, line=(0xB8, 0xB4, 0xA7), lw=1.2)
    mono(s, 0.85, 1.90, 3.0, 0.2, "VAGUE", size=8, color=GRAY, align=LC, tracking=1.4)
    text(s, 1.05, 2.30, 5.3, 0.3, "پرامپت مبهم", size=14, bold=True, align=RL)
    text(s, 1.05, 2.72, 5.3, 0.6, "«یه متن درباره هوش مصنوعی بنویس.»", size=13, color=(0x3E, 0x3F, 0x39), align=RL)
    line(s, 1.05, 3.38, 6.35, 3.38, (0xD6, 0xD2, 0xC6), 0.9)
    text(s, 1.05, 3.50, 5.3, 1.9, "خروجی: کلی، تکراری، بدون مخاطب مشخص، بدون ساختار و غیرقابل استفاده در ارائه.",
         size=11, color=GRAY, align=RL, line_spacing=1.5)
    # strong
    rect(s, 6.92, 1.82, 5.72, 3.88, INK, radius=0.04)
    mono(s, 7.12, 1.98, 3.0, 0.2, "PRECISE", size=8, color=LIME, align=LC, tracking=1.4)
    text(s, 7.12, 2.22, 5.3, 0.3, "پرامپت حرفه‌ای", size=14, bold=True, color=CREAM, align=RL)
    text(s, 7.12, 2.62, 5.3, 1.55,
         "«تو یک مدرس فناوری هستی. برای دانشجویان کارشناسی ارشد، سه پاراگراف درباره‌ی تأثیر LLM بر برنامه‌نویسی بنویس. لحن: تحلیلی و بدون اغراق. هر پاراگراف یک ادعا با یک مثال. خروجی را با تیتر بده.»",
         size=10.5, color=(0xD8, 0xD9, 0xCF), align=RL, line_spacing=1.5)
    line(s, 7.12, 4.38, 12.42, 4.38, (0x3C, 0x3E, 0x37), 0.9)
    text(s, 7.12, 4.50, 5.3, 0.9, "خروجی: هدفمند، ساختارمند، قابل ویرایش و نزدیک به آنچه می‌خواهید.",
         size=10.5, color=LIME, align=RL, line_spacing=1.45)
    text(s, 0.85, 6.05, 11.8, 0.5, "مدل قرار نیست ذهن شما را بخواند؛ پرامپت، احتمال رسیدن به خروجی درست را بالا می‌برد.",
         size=12.5, bold=True, align=RL)
    finish(s, [], "WHY PROMPTING", num, total)


def s_anatomy(s, num, total):
    P.head(s, "04 / PROMPT / ANATOMY", "آناتومی یک پرامپت حرفه‌ای", size=32, w=10.6)
    parts = [
        ("نقش", "ROLE", "تو یک تحلیلگر داده‌ی ارشد هستی..."),
        ("زمینه", "CONTEXT", "مخاطب: مدیرعامل؛ داده: فروش ۱۲ ماه..."),
        ("وظیفه", "TASK", "سه روند اصلی را استخراج کن و..."),
        ("قالب", "FORMAT", "جدول ۳ ستونه، حداکثر ۲۰۰ کلمه..."),
        ("مثال", "EXAMPLES", "نمونه‌ی خروجی مطلوب: ..."),
        ("محدودیت", "CONSTRAINTS", "بدون اغراق، فقط بر اساس داده..."),
    ]
    y = 2.10
    for i, (fa, en, ex) in enumerate(parts):
        rect(s, 0.85, y, 4.30, 0.62, LIME if i == 2 else (0xEE, 0xEA, 0xDD) if i % 2 == 0 else None,
             line=None if i in (0, 2) else (0xC9, 0xC5, 0xB8), lw=0.9, radius=0.05)
        text(s, 0.98, y + 0.14, 3.2, 0.3, fa, size=12.5, bold=True, align=RL)
        mono(s, 4.10, y + 0.20, 0.9, 0.22, en, size=7, color=GRAY, align=RL, tracking=1)
        y += 0.70
    # right terminal
    P.terminal(s, 5.45, 2.10, 7.15, 4.55, [
        ("[ROLE]", LIME, True),
        ("You are a senior data analyst.", (0xD8, 0xD9, 0xCF), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("[CONTEXT]", LIME, True),
        ("داده: فروش ماهانه ۱۲ ماه، ۳ محصول.", (0xD8, 0xD9, 0xCF), False),
        ("[TASK] + [FORMAT]", LIME, True),
        ("۳ روند اصلی را در جدول ۳ ستونه بده.", (0xD8, 0xD9, 0xCF), False),
        ("هر روند: مشاهده، شاهد عددی، پیشنهاد.", (0xD8, 0xD9, 0xCF), False),
        ("[CONSTRAINTS]", LIME, True),
        ("حداکثر ۲۰۰ کلمه؛ بدون حدس؛ اگر داده کم بود بگو.", (0xD8, 0xD9, 0xCF), False),
    ], title="prompt.md", fs=9.5)
    text(s, 5.45, 6.78, 7.1, 0.22, "شش بلوک؛ لازم نیست همیشه همه باشند، اما آگاهانه انتخاب کنید.",
         size=9.5, color=GRAY, align=RL)
    finish(s, [], "PROMPT ANATOMY", num, total)


def s_principles(s, num, total):
    P.head(s, "04 / PROMPT / PRINCIPLES", "شش اصل پرامپت‌نویسی حرفه‌ای", size=31, w=11.0)
    items = [
        ("۰۱", "شفاف و مشخص", "به‌جای «خوب بنویس»، بگویید چه چیزی، برای چه کسی، با چه لحنی."),
        ("۰۲", "زمینه بدهید", "اطلاعات لازم را در پرامپت بگذارید؛ مدل ذهن شما را نمی‌خواند."),
        ("۰۳", "ساختار بسازید", "نقش، وظیفه، قالب و محدودیت را با تیتر یا XML جدا کنید."),
        ("۰۴", "مثال بدهید", "یک نمونه‌ی خوب، بیشتر از ده خط توضیح، رفتار مدل را شکل می‌دهد."),
        ("۰۵", "خروجی را قالب‌بندی کنید", "جدول، JSON، بولت یا ایمیل — قالب را صریح بخواهید."),
        ("۰۶", "تکرار و اصلاح", "پرامپت اول پیش‌نویس است؛ بر اساس خروجی، آن را دقیق‌تر کنید."),
    ]
    for i, (n, t, b) in enumerate(items):
        x = 8.65 - (i % 3) * 3.95
        y = 2.15 + (i // 3) * 2.05
        rect(s, x, y, 3.78, 1.85, (0xEE, 0xEA, 0xDD) if i % 3 == 1 else None,
             line=None if i % 3 == 1 else (0xC9, 0xC5, 0xB8), lw=0.9, radius=0.05)
        mono(s, x + 0.20, y + 0.14, 0.8, 0.2, n, size=9, color=GRAY, align=LC)
        text(s, x + 0.20, y + 0.40, 3.40, 0.3, t, size=13, bold=True, align=RL)
        text(s, x + 0.20, y + 0.78, 3.40, 0.95, b, size=9.5, color=(0x4C, 0x4D, 0x46), align=RL, line_spacing=1.45)
    finish(s, [], "PRINCIPLES", num, total)


def s_techniques1(s, num, total):
    P.head(s, "04 / PROMPT / TECHNIQUES I", "سه تکنیک پایه که همیشه جواب می‌دهد", size=30, w=11.3)
    items = [
        dict(num="01", ic="layers", title="Zero-shot / Few-shot",
             body="یا بدون مثال توضیح بدهید، یا ۲ تا ۳ نمونه‌ی دقیق از ورودی و خروجی بدهید.\nمثال برای قالب‌بندی و لحن، بهترین ابزار است."),
        dict(num="02", ic="route", title="Chain-of-Thought",
             body="از مدل بخواهید مرحله‌به‌مرحله فکر کند و سپس پاسخ نهایی را بدهد.\nبرای ریاضی، منطق و تصمیم‌های چندمعیاره حیاتی است."),
        dict(num="03", ic="repeat", title="ReAct",
             body="چرخه‌ی «فکر کن → ابزار را صدا بزن → مشاهده کن».\nپایه‌ی ایجنت‌ها؛ مدل به‌جای حدس، اطلاعات را می‌گیرد."),
    ]
    P.cards_row(s, 0.75, 2.18, 11.85, 3.55, items, gap=0.22)
    # example strip
    rect(s, 0.75, 5.95, 11.85, 0.70, (0xEE, 0xEA, 0xDD))
    mono(s, 1.00, 6.12, 2.0, 0.22, "EXAMPLE", size=8, color=GRAY, align=LC, tracking=1.2)
    text(s, 3.10, 6.14, 9.25, 0.3, "«مرحله‌به‌مرحله فکر کن، سپس فقط پاسخ نهایی را در یک خط بده.»", size=11.5, align=RL, color=INK)
    finish(s, [], "TECHNIQUES I", num, total)


def s_techniques2(s, num, total):
    P.head(s, "04 / PROMPT / TECHNIQUES II", "چهار تکنیک برای خروجی حرفه‌ای", size=31, w=11.0)
    items = [
        ("نقش و مخاطب", "ROLE", "«تو یک ویراستار فارسی‌زبان هستی؛ مخاطب: مدیر محصول.»"),
        ("خروجی ساختاریافته", "JSON / TABLE", "«فقط JSON با کلیدهای title, risk, action بده.»"),
        ("نقد و بازنویسی", "SELF-CRITIQUE", "«پاسخ خودت را نقد کن و نسخه‌ی بهتر را بده.»"),
        ("جداکننده‌ها", "DELIMITERS", "«دستورها داخل <rules> و داده داخل <data> باشد.»"),
    ]
    for i, (t, en, ex) in enumerate(items):
        x = 6.83 - (i % 2) * 6.03
        y = 2.10 + (i // 2) * 2.18
        rect(s, x, y, 5.78, 2.00, None, line=(0xC3, 0xBF, 0xB2), lw=0.9, radius=0.05)
        line(s, x + 0.02, y + 0.02, x + 0.90, y + 0.02, LIME, 4)
        mono(s, x + 0.22, y + 0.18, 2.4, 0.2, en, size=7.5, color=GRAY, align=LC, tracking=1.2)
        text(s, x + 0.22, y + 0.42, 5.30, 0.3, t, size=13.5, bold=True, align=RL)
        text(s, x + 0.22, y + 0.85, 5.30, 1.0, ex, size=10, color=(0x4C, 0x4D, 0x46), align=RL, line_spacing=1.5)
    finish(s, [], "TECHNIQUES II", num, total)


def s_before_after(s, num, total):
    P.head(s, "04 / PROMPT / REWRITE", "همان خواسته، دو نتیجه‌ی متفاوت", size=31, w=11.0)
    rect(s, 0.80, 2.05, 5.80, 4.55, None, line=(0xB8, 0xB4, 0xA7), lw=1.0)
    mono(s, 0.98, 2.18, 3.0, 0.2, "BEFORE / WEAK", size=8, color=GRAY, align=LC, tracking=1.2)
    text(s, 1.00, 2.48, 5.35, 1.4, "«برای این محصول یه متن تبلیغاتی بنویس.»", size=14, color=INK, align=RL, line_spacing=1.5)
    line(s, 1.00, 3.62, 6.38, 3.62, (0xD6, 0xD2, 0xC6), 0.9)
    text(s, 1.00, 3.78, 5.35, 2.55,
         "نتیجه: متن کلی، بدون مخاطب، بدون مزیت رقابتی و بدون دعوت به اقدام.\n\nسه بار بازنویسی می‌خواهد؛ زمان بیشتری از نوشتن دستی می‌برد.",
         size=10.5, color=GRAY, align=RL, line_spacing=1.55)
    rect(s, 6.95, 2.05, 5.62, 4.55, INK, radius=0.04)
    mono(s, 7.13, 2.18, 3.0, 0.2, "AFTER / STRONG", size=8, color=LIME, align=LC, tracking=1.2)
    text(s, 7.13, 2.45, 5.22, 0.3, "پرامپت بازنویسی‌شده", size=12.5, bold=True, color=CREAM, align=RL)
    text(s, 7.13, 2.82, 5.22, 2.35,
         "«تو یک کپی‌رایتر هستی. برای اپلیکیشن مدیریت هزینه، یک متن تبلیغاتی ۶۰ کلمه‌ای بنویس. مخاطب: مدیر مالی شرکت‌های کوچک. لحن: مطمئن و بدون اغراق. یک مزیت مشخص + یک دعوت به اقدام. سه نسخه با زاویه‌های متفاوت بده.»",
         size=9.5, color=(0xD8, 0xD9, 0xCF), align=RL, line_spacing=1.55)
    line(s, 7.13, 5.32, 12.38, 5.32, (0x3C, 0x3E, 0x37), 0.9)
    text(s, 7.13, 5.44, 5.22, 0.9, "نتیجه: قابل انتخاب، قابل ویرایش، آماده‌ی انتشار.", size=10, color=LIME, align=RL, line_spacing=1.4)
    finish(s, [], "REWRITE", num, total)


def s_practice(s, num, total):
    P.head(s, "04 / PROMPT / IN PRACTICE", "پرامپت برای چهار کار واقعی", size=31, w=10.8)
    items = [
        ("ایمیل و مکاتبه", "mail", "«این یادداشت خام را به ایمیل رسمی ۱۵۰ کلمه‌ای تبدیل کن؛ لحن محترمانه، بدون تعهد اضافه.»"),
        ("تحلیل داده", "chart-line", "«این CSV را تحلیل کن؛ ۳ یافته، ۳ ریسک و ۳ اقدام پیشنهادی در جدول بده.»"),
        ("دیباگ کد", "code", "«این خطا را با فرضیه‌های مشخص بررسی کن؛ اول علت، بعد تست، بعد پچ حداقلی.»"),
        ("تولید محتوا", "pen-tool", "«سه نسخه‌ی پست لینکدین با زاویه‌های متفاوت بنویس؛ هر کدام با یک قلاب متفاوت.»"),
    ]
    for i, (t, ic, ex) in enumerate(items):
        x = 6.83 - (i % 2) * 6.03
        y = 2.10 + (i // 2) * 2.18
        P.card(s, x, y, 5.78, 2.00, ic=ic, title=t, body=ex, variant="line", title_size=13, body_size=9.5)
    finish(s, [], "PROMPTS IN PRACTICE", num, total)


def s_checklist(s, num, total):
    P.head(s, "04 / PROMPT / CHECKLIST", "چک‌لیست ۷ مرحله‌ای و ۵ اشتباه رایج", size=30, w=11.4)
    checks = [
        "هدف و مخاطب را بنویسید.",
        "زمینه و داده‌ی لازم را بگذارید.",
        "وظیفه را به یک فعل مشخص تبدیل کنید.",
        "قالب خروجی را تعیین کنید.",
        "یک مثال خوب اضافه کنید.",
        "محدودیت‌ها و ممنوعیت‌ها را بگویید.",
        "خروجی را نقد و پرامپت را اصلاح کنید.",
    ]
    for i, c in enumerate(checks):
        y = 2.10 + i * 0.62
        rect(s, 11.90, y + 0.10, 0.16, 0.16, LIME)
        text(s, 7.55, y, 4.20, 0.32, c, size=11, align=RL)
        mono(s, 12.30, y + 0.06, 0.3, 0.2, "", size=8)
    line(s, 7.35, 2.05, 7.35, 6.55, (0xD6, 0xD2, 0xC6), 0.9)
    mistakes = [
        ("پرامپت‌های طولانی و بی‌ساختار", "هدف گم می‌شود."),
        ("نبود زمینه و مخاطب", "خروجی کلی می‌شود."),
        ("درخواست چند کار در یک پیام", "کیفیت هر بخش پایین می‌آید."),
        ("اعتماد بدون راستی‌آزمایی", "خطا و توهم وارد کار می‌شود."),
        ("ندادن بازخورد اصلاحی", "مدل اشتباه را تکرار می‌کند."),
    ]
    for i, (m, note) in enumerate(mistakes):
        y = 2.15 + i * 0.82
        text(s, 0.80, y, 0.3, 0.3, "×", size=14, bold=True, color=INK, align=LC)
        text(s, 1.15, y - 0.02, 5.85, 0.3, m, size=10.5, bold=True, align=RL)
        text(s, 1.15, y + 0.28, 5.85, 0.3, note, size=9, color=GRAY, align=RL)
    finish(s, [], "CHECKLIST", num, total)
