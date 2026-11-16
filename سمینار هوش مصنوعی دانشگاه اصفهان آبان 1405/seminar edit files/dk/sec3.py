# -*- coding: utf-8 -*-
"""Section 3 — tools, agents, Claude."""
from pptx.enum.shapes import MSO_SHAPE
from .theme import (W, H, M, CREAM, INK, LIME, GRAY, MONO, RL, LC, CT,
                    rect, line, text, mono, icon, icon_at, stamp)
from . import parts as P
from . import covers, anim, decor

LAB = "05 / TOOLS"


def finish(s, shapes, label, num, total):
    stamp(s, label, num, total)
    anim.transition(s)
    anim.animate(s, shapes)


def s_div5(s, num, total):
    covers.divider(s, 5, "جعبه‌ابزار هوش مصنوعی",
                   "TEXT / IMAGE / VIDEO / AUDIO / CODE",
                   "چه ابزاری برای چه کاری؟\nیک نقشه‌ی کاربردی برای انتخاب سریع و درست.",
                   "wave", num, total)


def s_toolmap(s, num, total):
    P.head(s, "05 / TOOLS / LANDSCAPE", "چهار خانواده‌ی ابزار", size=32, w=10.0)
    quads = [
        ("متن و تحقیق", "TEXT & RESEARCH", "message-square",
         "ChatGPT · Claude · Gemini · Perplexity · NotebookLM"),
        ("تصویر و ویدیو", "IMAGE & VIDEO", "image",
         "Midjourney · DALL·E · Flux · Sora · Runway · Kling"),
        ("صدا و موسیقی", "AUDIO & MUSIC", "music",
         "ElevenLabs · Suno · Udio · Whisper · Adobe Podcast"),
        ("کد و بهره‌وری", "CODE & WORKFLOW", "code",
         "Copilot · Cursor · Claude Code · v0 · Notion AI"),
    ]
    for i, (t, en, ic, tools) in enumerate(quads):
        x = 6.78 if i % 2 == 0 else 0.75
        y = 2.05 + (i // 2) * 2.20
        rect(s, x, y, 5.82, 2.02, (0xEE, 0xEA, 0xDD) if i % 2 else None,
             line=None if i % 2 else (0xC6, 0xC2, 0xB5), lw=1.0, radius=0.04)
        icon(s, ic, x + 0.30, y + 0.26, 0.44, INK)
        mono(s, x + 0.30, y + 0.84, 4.6, 0.2, en, size=7.5, color=GRAY, align=LC, tracking=1.2)
        text(s, x + 0.80, y + 0.24, 4.65, 0.35, t, size=15, bold=True, align=RL)
        text(s, x + 0.30, y + 1.12, 5.20, 0.7, tools, size=10.5, color=(0x45, 0x46, 0x40),
             align=RL, line_spacing=1.5)
    finish(s, [], "TOOL LANDSCAPE", num, total)


def s_text_tools(s, num, total):
    P.head(s, "05 / TOOLS / TEXT", "متن، تحقیق و تحلیل", size=32, w=9.6)
    # chat mock
    rect(s, 0.85, 2.10, 4.70, 4.45, INK, radius=0.06)
    rect(s, 0.85, 2.10, 4.70, 0.38, (0x1B, 0x1D, 0x19), radius=0.06)
    mono(s, 1.05, 2.20, 3.4, 0.2, "research / chat", size=8, color=(0x8E, 0x90, 0x85), align=LC)
    # user bubble
    rect(s, 2.05, 2.70, 3.20, 0.62, LIME, radius=0.10)
    text(s, 2.18, 2.80, 2.95, 0.42, "سه روند اصلی بازار EV را با منبع بگو.", size=9.5, color=INK, align=RL)
    # answer lines
    rect(s, 1.10, 3.55, 4.15, 0.10, (0x3B, 0x3D, 0x36))
    rect(s, 1.10, 3.80, 4.15, 0.10, (0x3B, 0x3D, 0x36))
    rect(s, 1.10, 4.05, 3.30, 0.10, (0x3B, 0x3D, 0x36))
    for i, sname in enumerate(["منبع ۱", "منبع ۲", "منبع ۳"]):
        w = 0.95
        x = 4.95 - i * (w + 0.12)
        rect(s, x, 4.42, w, 0.28, None, line=(0x5B, 0x5E, 0x52), lw=0.8, radius=0.4)
        text(s, x, 4.47, w, 0.18, sname, size=7.5, color=(0xC9, 0xCA, 0xC0), align=CT)
    rect(s, 1.10, 5.05, 3.85, 0.10, (0x3B, 0x3D, 0x36))
    rect(s, 1.10, 5.30, 2.70, 0.10, (0x3B, 0x3D, 0x36))
    mono(s, 1.10, 5.85, 4.2, 0.2, "SEARCH + CITE + SYNTHESIZE", size=7.5, color=LIME, align=LC, tracking=1)
    text(s, 1.10, 6.10, 4.2, 0.3, "پاسخ با ارجاع، قابل بررسی", size=9, color=(0x9F, 0xA1, 0x96), align=LC)
    # right list
    rows = [
        ("ChatGPT", "دستیار عمومی؛ استدلال، کد، تحلیل فایل و جستجو."),
        ("Claude", "متن‌های بلند، تحلیل دقیق، نوشتن و کار با کد."),
        ("Gemini", "یکپارچه با Google؛ جستجو، ویدیو و Workspace."),
        ("Perplexity", "پاسخ با منبع؛ جایگزین هوشمند جستجو."),
        ("NotebookLM", "پرسش از اسناد و کتاب‌های خودتان."),
    ]
    for i, (t, b) in enumerate(rows):
        y = 2.18 + i * 0.86
        mono(s, 11.95, y + 0.02, 0.55, 0.22, "0%d" % (i + 1), size=8, color=GRAY, align=RL)
        text(s, 6.10, y - 0.03, 5.55, 0.28, t, size=12.5, bold=True, align=RL)
        text(s, 6.10, y + 0.28, 5.55, 0.34, b, size=9.5, color=(0x50, 0x51, 0x4A), align=RL)
        line(s, 0.88, y + 0.76, 12.55, y + 0.76, (0xDD, 0xD9, 0xCD), 0.7) if i < 4 else None
    finish(s, [], "TEXT TOOLS", num, total)


def s_visual_tools(s, num, total):
    P.head(s, "05 / TOOLS / VISUAL", "تصویر و ویدیو: از ایده تا فریم", size=31, w=10.8)
    tiles = [
        ("Midjourney", "تصویر هنری", "geo"), ("DALL·E", "تصویر از متن", "halftone"),
        ("Flux / SD", "مدل باز و قابل تنظیم", "mesh_light"), ("Sora", "ویدیوی سینمایی", "contour"),
        ("Runway", "ابزار ویدیو و افکت", "tunnel"), ("Kling", "ویدیوی کوتاه", "wave"),
    ]
    tw_, th_ = 3.00, 1.68
    for i, (name, desc, art) in enumerate(tiles):
        x = 9.78 - (i % 3) * 3.18
        y = 2.05 + (i // 3) * 1.85
        img = decor.ensure_art([art])[art]
        P.picture(s, img, x, y, tw_, th_, frame=None)
        P.veil(s, x, y, tw_, th_, INK, 0.35)
        mono(s, x + 0.16, y + th_ - 0.44, 1.4, 0.18, "0%d" % (i + 1), size=7, color=LIME, align=LC, tracking=1)
        text(s, x + 0.16, y + th_ - 0.67, 2.6, 0.28, name, size=12.5, bold=True, color=CREAM, align=LC, font=MONO, rtl=False)
        text(s, x + 0.16, y + th_ - 0.30, 2.7, 0.2, desc, size=8.5, color=(0xD5, 0xD6, 0xCB), align=LC)
    text(s, 0.88, 5.82, 11.7, 0.4, "برای ویدیو، «کارگردانی» مهم‌تر از ابزار است: نما، حرکت دوربین، نور و تدوین را مرحله‌به‌مرحله بسازید.",
         size=11, color=(0x45, 0x46, 0x40), align=RL)
    rect(s, 0.88, 6.28, 11.70, 0.42, LIME)
    text(s, 1.05, 6.36, 11.35, 0.26, "حق نشر و اصالت را جدی بگیرید: مجوز تجاری، واترمارک و سیاست هر ابزار را قبل از استفاده‌ی رسمی بخوانید.",
         size=9.5, bold=True, color=INK, align=RL)
    finish(s, [], "VISUAL TOOLS", num, total)


def s_audio_tools(s, num, total):
    P.head(s, "05 / TOOLS / AUDIO", "صدا، موسیقی و گفتار", size=32, w=9.4)
    art = decor.ensure_art(["wave"])["wave"]
    P.picture(s, art, 0.88, 2.18, 4.55, 2.55, frame=None)
    P.veil(s, 0.88, 2.18, 4.55, 2.55, INK, 0.15)
    rect(s, 2.62, 2.95, 0.95, 0.95, LIME, shape=MSO_SHAPE.OVAL)
    text(s, 2.62, 3.10, 0.95, 0.5, "▶", size=20, bold=True, color=INK, align=CT)
    text(s, 0.88, 4.88, 4.55, 0.3, "پادکست، دوبله، نریشن و موسیقی — همه با AI", size=10, color=GRAY, align=LC)
    rows = [
        ("ElevenLabs", "صدای طبیعی و دوبله‌ی چندزبانه", "mic"),
        ("Suno / Udio", "ساخت آهنگ کامل از یک توضیح", "music"),
        ("Whisper", "تبدیل صوت به متن با دقت بالا", "file-text"),
        ("Adobe Podcast", "بهبود کیفیت صدای ضبط‌شده", "headphones"),
    ]
    for i, (t, b, ic) in enumerate(rows):
        y = 2.15 + i * 0.92
        icon(s, ic, 12.05, y + 0.10, 0.34, INK)
        text(s, 6.10, y - 0.02, 5.65, 0.3, t, size=13, bold=True, align=RL)
        text(s, 6.10, y + 0.30, 5.65, 0.3, b, size=10, color=(0x50, 0x51, 0x4A), align=RL)
        line(s, 0.88, y + 0.80, 12.55, y + 0.80, (0xDD, 0xD9, 0xCD), 0.7) if i < 3 else None
    text(s, 0.88, 6.08, 11.67, 0.55, "کاربردها: نریشن دوره، پادکست، دوبله‌ی محتوا، دستیار صوتی و تبدیل جلسات به صورت‌جلسه.",
         size=10.5, color=GRAY, align=RL, line_spacing=1.4)
    finish(s, [], "AUDIO TOOLS", num, total)


def s_code_tools(s, num, total):
    P.head(s, "05 / TOOLS / CODE", "کدنویسی و بهره‌وری", size=32, w=9.6)
    P.terminal(s, 0.85, 2.12, 5.10, 4.10, [
        ("$ claude", LIME, True),
        ("> این تست را شکست‌خورده بررسی کن", (0xD8, 0xD9, 0xCF), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("● خواندن ۱۲ فایل مرتبط", (0x9A, 0xA2, 0x7A), False),
        ("● یافتن علت در auth.ts:84", (0x9A, 0xA2, 0x7A), False),
        ("● اجرای تست‌ها", (0x9A, 0xA2, 0x7A), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("✓ پچ پیشنهادی آماده است", LIME, True),
        ("  +12  -3   tests: 48 passed", (0xC9, 0xCA, 0xC0), False),
    ], title="claude code", fs=9.5)
    cats = [
        ("تکمیل کد", "GitHub Copilot — پیشنهاد درون‌خطی در IDE"),
        ("IDE عامل‌محور", "Cursor · Windsurf — ویرایش چندفایلی با دستور"),
        ("ترمینال", "Claude Code — اجرا، تست، گیت و ابزارها"),
        ("ساخت اپ", "v0 · Bolt · Replit — از توضیح تا اپ اجراشدنی"),
        ("بهره‌وری", "Notion AI · Gamma — مستند، اسلاید و خلاصه"),
    ]
    for i, (t, b) in enumerate(cats):
        y = 2.16 + i * 0.86
        text(s, 6.55, y, 5.20, 0.28, t, size=12, bold=True, align=RL)
        text(s, 6.55, y + 0.28, 5.20, 0.34, b, size=9.3, color=(0x50, 0x51, 0x4A), align=RL)
        line(s, 0.88, y + 0.75, 12.55, y + 0.75, (0xDD, 0xD9, 0xCD), 0.7) if i < 4 else None
    finish(s, [], "CODE TOOLS", num, total)


def s_matrix(s, num, total):
    P.head(s, "05 / TOOLS / DECISION", "کدام ابزار برای کدام کار؟", size=32, w=9.8)
    rows = [
        ("نوشتن، ویرایش و خلاصه‌سازی", "مدل زبانی", "Claude · ChatGPT · Gemini"),
        ("تحقیق با منبع و استناد", "موتور پاسخ", "Perplexity · NotebookLM"),
        ("تصویر تبلیغاتی و کانسپت", "تولید تصویر", "Midjourney · DALL·E · Flux"),
        ("ویدیوی کوتاه و تبلیغ", "تولید ویدیو", "Sora · Runway · Kling"),
        ("نریشن، دوبله و پادکست", "صدا", "ElevenLabs · Whisper"),
        ("کدنویسی و رفع باگ", "ایجنت کد", "Claude Code · Cursor · Copilot"),
        ("اسلاید و محتوای بصری", "بهره‌وری", "Gamma · Canva · Beautiful.ai"),
    ]
    P.table(s, 0.90, 2.15, 11.65, ["نیاز شما", "دسته‌ی ابزار", "نمونه‌ها"], rows,
            widths=[3.9, 2.2, 5.5], row_h=0.52, head_h=0.44, size=9.5, head_size=9.5)
    text(s, 0.90, 6.42, 11.6, 0.4, "قاعده‌ی طلایی: ابزار را با «کار» انتخاب کنید، نه با تبلیغات؛ و همیشه یک گزینه‌ی دوم داشته باشید.",
         size=10.5, color=GRAY, align=RL)
    finish(s, [], "TOOL MATRIX", num, total)


def s_div6(s, num, total):
    covers.divider(s, 6, "ایجنت‌های هوش مصنوعی",
                   "AGENTS / TOOLS / MEMORY / AUTOMATION",
                   "از چت‌بات که فقط جواب می‌دهد، تا ایجنتی که کار را تمام می‌کند.\nاینجا مرز دستیار و همکار مشخص می‌شود.",
                   "contour", num, total)


def s_agent(s, num, total):
    P.head(s, "06 / AGENTS / DEFINITION", "ایجنت چیست و چگونه کار می‌کند؟", size=31, w=10.6)
    # loop diagram
    cx, cy = 3.25, 4.30
    rect(s, cx - 1.05, cy - 0.55, 2.10, 1.10, INK, radius=0.10)
    text(s, cx - 1.0, cy - 0.33, 2.0, 0.3, "LLM", size=16, bold=True, color=LIME, align=CT, font=MONO, rtl=False)
    text(s, cx - 1.0, cy + 0.02, 2.0, 0.3, "استدلال و تصمیم", size=9, color=(0xC9, 0xCA, 0xC0), align=CT)
    nodes = [
        (cx - 0.85, 2.05, 1.70, 0.62, "ادراک", "Perceive"),
        (cx + 1.55, cy - 0.31, 1.70, 0.62, "برنامه‌ریزی", "Plan"),
        (cx - 0.85, 5.75, 1.70, 0.62, "اقدام", "Act"),
        (cx - 2.60, cy - 0.31, 1.70, 0.62, "مشاهده", "Observe"),
    ]
    for x, y, w, h, fa, en in nodes:
        rect(s, x, y, w, h, None, line=INK, lw=1.1, radius=0.08)
        text(s, x, y + 0.09, w, 0.26, fa, size=10.5, bold=True, align=CT)
        mono(s, x, y + 0.36, w, 0.18, en, size=7, color=GRAY, align=CT)
    P.arrow(s, cx - 0.55, cy - 0.58, cx - 0.35, 2.70, INK, 1.2)
    P.arrow(s, cx + 1.08, cy - 0.30, cx + 1.50, cy - 0.28, INK, 1.2)
    P.arrow(s, cx + 1.35, cy + 0.70, cx + 0.30, 5.72, INK, 1.2)
    P.arrow(s, cx - 1.10, cy + 0.30, cx - 2.55, cy + 0.10, INK, 1.2)
    text(s, cx - 1.25, cy + 0.95, 2.4, 0.24, "حلقه‌ی بسته", size=8, color=GRAY, align=CT)
    # right
    text(s, 6.20, 2.05, 6.35, 0.9, "ایجنت = مدل + ابزار + حافظه + حلقه", size=17, bold=True, align=RL)
    text(s, 6.20, 2.75, 6.35, 0.7, "مدلی که فقط جواب نمی‌دهد؛ هدف را می‌شکند، ابزار را صدا می‌زند، نتیجه را می‌بیند و ادامه می‌دهد.",
         size=11, color=(0x45, 0x46, 0x40), align=RL, line_spacing=1.5)
    P.bullets(s, 6.20, 3.62, 6.30, [
        ("ابزار (Tools)", "جستجو، اجرای کد، خواندن فایل، API و مرورگر."),
        ("حافظه (Memory)", "تاریخچه‌ی گفتگو، فایل‌های پروژه و حافظه‌ی بلندمدت."),
        ("برنامه‌ریزی (Planning)", "تجزیه‌ی هدف به گام‌ها و اصلاح مسیر بر اساس نتیجه."),
        ("محدوده (Guardrails)", "مجوزها، سندباکس و تأیید انسانی برای کارهای حساس."),
    ], size=10.5, gap=0.10)
    finish(s, [], "WHAT IS AN AGENT", num, total)


def s_chat_vs_agent(s, num, total):
    P.head(s, "06 / AGENTS / COMPARISON", "چت‌بات در برابر ایجنت", size=32, w=10.0)
    rows = [
        ("واحد کار", "یک پیام، یک پاسخ", "یک هدف، چند گام"),
        ("ابزار", "معمولاً بدون ابزار", "جستجو، کد، فایل، API"),
        ("حافظه", "تاریخچه‌ی کوتاه", "حافظه‌ی پروژه و بلندمدت"),
        ("خطا", "پاسخ اشتباه می‌دهد", "اشتباه را می‌بیند و اصلاح می‌کند"),
        ("نقش انسان", "پرسش‌گر", "تعیین هدف و تأیید نهایی"),
        ("مثال", "پاسخ به یک سؤال", "رفع باگ، ساخت گزارش، رزرو سفر"),
    ]
    P.table(s, 0.90, 2.15, 11.65, ["ویژگی", "Chatbot", "AI Agent"], rows,
            widths=[2.3, 3.9, 4.4], row_h=0.55, head_h=0.46, size=10, head_size=10, accent_col=2)
    text(s, 0.90, 6.35, 11.6, 0.5, "هر ایجنت خوب، یک چت‌بات خوب هم هست؛ اما هر چت‌باتی ایجنت نیست.",
         size=11.5, bold=True, align=RL)
    finish(s, [], "CHATBOT VS AGENT", num, total)


def s_agent_parts(s, num, total):
    P.head(s, "06 / AGENTS / ANATOMY", "یک ایجنت از چه چیزی ساخته می‌شود؟", size=31, w=11.0)
    layers = [
        ("مدل استدلال", "LLM", "فهم هدف، برنامه‌ریزی، تصمیم و تولید پاسخ", INK, CREAM),
        ("ابزارها", "TOOLS", "شل، مرورگر، دیتابیس، API، MCP", LIME, INK),
        ("حافظه", "MEMORY", "تاریخچه، فایل‌ها، برداشت‌های بلندمدت", None, INK),
        ("برنامه‌ریزی", "PLANNING", "شکستن کار، اولویت‌بندی، بازگشت از خطا", None, INK),
        ("محافظ‌ها", "GUARDRAILS", "مجوز، سندباکس، لاگ، تأیید انسانی", None, INK),
    ]
    y = 2.05
    for i, (fa, en, desc, fill, fg) in enumerate(layers):
        rect(s, 0.90, y, 6.40, 0.80, fill, line=None if fill else (0xB9, 0xB5, 0xA8), lw=1.0, radius=0.04)
        text(s, 1.10, y + 0.07, 2.9, 0.28, fa, size=12.5, bold=True, color=fg, align=RL)
        mono(s, 4.10, y + 0.12, 1.1, 0.2, en, size=7, color=INK if fill == LIME else GRAY, align=RL, tracking=1)
        text(s, 1.10, y + 0.40, 6.0, 0.3, desc, size=8.5, color=(0x5A, 0x5B, 0x53) if fill != INK else (0xC9, 0xCA, 0xC0), align=RL)
        y += 0.88
    text(s, 7.75, 2.10, 4.80, 0.4, "ترتیب اهمیت:", size=13, bold=True, align=RL)
    P.bullets(s, 7.75, 2.55, 4.80, [
        ("۱. ابزار درست", "بدون ابزار، ایجنت فقط حرف می‌زند."),
        ("۲. حلقه‌ی بازخورد", "دیدن نتیجه و اصلاح، تفاوت اصلی است."),
        ("۳. محدودیت شفاف", "دسترسی کم = ریسک کم."),
    ], size=10.5, gap=0.14)
    text(s, 7.75, 5.95, 4.75, 0.8, "مثال: یک ایجنت گزارش‌ساز به دیتابیس، ماشین‌حساب و قالب گزارش نیاز دارد؛ نه فقط مدل قوی.",
         size=9.5, color=GRAY, align=RL, line_spacing=1.5)
    finish(s, [], "AGENT ANATOMY", num, total)


def s_mcp(s, num, total):
    P.head(s, "06 / AGENTS / MCP", "MCP: استاندارد اتصال مدل به ابزار", size=31, w=11.0)
    text(s, 6.10, 2.00, 6.45, 0.5, "Model Context Protocol — یک قرارداد مشترک تا هر ابزاری به هر مدلی وصل شود.",
         size=11.5, color=(0x3E, 0x3F, 0x39), align=RL)
    # center
    cx, cy = 7.90, 4.30
    rect(s, cx - 1.05, cy - 0.55, 2.10, 1.10, LIME, radius=0.10)
    text(s, cx - 1.0, cy - 0.42, 2.0, 0.4, "MCP", size=24, bold=True, color=INK, align=CT, font=MONO, rtl=False)
    text(s, cx - 1.0, cy + 0.10, 2.0, 0.24, "Server", size=8, color=INK, align=CT, font=MONO, rtl=False)
    # model side
    rect(s, 10.55, cy - 0.42, 1.95, 0.84, INK, radius=0.08)
    text(s, 10.55, cy - 0.32, 1.95, 0.28, "Claude / LLM", size=10.5, bold=True, color=CREAM, align=CT)
    text(s, 10.55, cy + 0.00, 1.95, 0.22, "Client", size=7.5, color=GRAY, align=CT, font=MONO, rtl=False)
    P.arrow(s, 10.50, cy, 8.98, cy, INK, 1.4)
    P.arrow(s, 8.95, cy + 0.16, 10.48, cy + 0.16, (0xB9, 0xB5, 0xA8), 1.0)
    text(s, 9.15, cy - 0.30, 1.6, 0.22, "JSON-RPC", size=7.5, color=GRAY, align=CT, font=MONO, rtl=False)
    # tools
    tools = [("فایل‌ها", "folder"), ("دیتابیس", "database"), ("مرورگر", "globe"), ("GitHub", "git-branch"), ("Slack", "message-circle")]
    for i, (t, ic) in enumerate(tools):
        y = 2.42 + i * 0.80
        rect(s, 4.90, y, 1.75, 0.60, None, line=(0xB9, 0xB5, 0xA8), lw=1.0, radius=0.06)
        icon(s, ic, 5.02, y + 0.17, 0.26, INK)
        text(s, 5.30, y + 0.16, 1.20, 0.3, t, size=9, bold=True, align=RL)
        line(s, 6.70, y + 0.30, 6.80, cy, (0xB9, 0xB5, 0xA8), 0.9)
    P.arrow(s, 6.82, cy, 4.90, cy, (0xB9, 0xB5, 0xA8), 0.9, head=False)
    text(s, 0.90, 6.55, 10.0, 0.36, "یک‌بار بنویس، همه‌جا استفاده کن: ابزارها به MCP Server تبدیل می‌شوند و هر کلاینتی می‌تواند از آن‌ها استفاده کند.",
         size=9.5, color=GRAY, align=LC)
    finish(s, [], "MCP", num, total)


def s_agent_use(s, num, total):
    P.head(s, "06 / AGENTS / IMPACT", "کاربردها، ریسک‌ها و کنترل", size=32, w=10.6)
    text(s, 7.60, 2.02, 4.95, 0.3, "کجا واقعاً ارزش می‌سازد؟", size=12.5, bold=True, align=RL)
    uses = [
        ("پشتیبانی مشتری", "پاسخ با دانش داخلی + ارجاع هوشمند"),
        ("مهندسی نرم‌افزار", "رفع باگ، تست، بازبینی و مستندسازی"),
        ("تحقیق و تحلیل", "جمع‌آوری، مقایسه و تولید گزارش"),
        ("عملیات", "دسته‌بندی ایمیل، فاکتور، ورود داده"),
    ]
    for i, (t, b) in enumerate(uses):
        y = 2.45 + i * 1.02
        rect(s, 7.95, y + 0.06, 0.10, 0.10, LIME)
        text(s, 8.18, y - 0.03, 4.35, 0.28, t, size=11, bold=True, align=RL)
        text(s, 8.18, y + 0.26, 4.35, 0.3, b, size=9, color=(0x50, 0x51, 0x4A), align=RL)
    text(s, 0.90, 2.02, 6.35, 0.3, "چه چیزی می‌تواند خراب شود؟", size=12.5, bold=True, align=RL)
    risks = [
        ("تزریق پرامپت", "دستور مخفی در یک صفحه یا فایل، ایجنت را فریب می‌دهد."),
        ("اقدام مخرب", "حذف فایل یا ارسال ایمیل بدون تأیید."),
        ("نشت داده", "ارسال اطلاعات حساس به ابزار بیرونی."),
        ("هزینه‌ی مهارنشده", "حلقه‌ای که بی‌نهایت ابزار صدا می‌زند."),
    ]
    for i, (t, b) in enumerate(risks):
        y = 2.45 + i * 1.02
        text(s, 0.95, y - 0.03, 0.3, 0.3, "×", size=13, bold=True, color=INK, align=LC)
        text(s, 1.30, y - 0.03, 5.95, 0.28, t, size=11, bold=True, align=RL)
        text(s, 1.30, y + 0.26, 5.95, 0.3, b, size=9, color=(0x50, 0x51, 0x4A), align=RL)
    line(s, 7.45, 2.00, 7.45, 6.55, (0xD6, 0xD2, 0xC6), 1.0)
    rect(s, 0.90, 6.35, 6.30, 0.42, LIME)
    text(s, 1.05, 6.43, 6.0, 0.25, "قاعده: دسترسی حداقلی + تأیید انسانی برای اقدام حساس.", size=9.5, bold=True, color=INK, align=RL)
    finish(s, [], "AGENT IMPACT", num, total)


def s_div7(s, num, total):
    covers.divider(s, 7, "Claude و Claude Code",
                   "ANTHROPIC / CLAUDE / CLAUDE CODE",
                   "یک مدل برای فکر کردن، یک ابزار برای ساختن.\nتفاوت این دو، تفاوت «مشاور» و «همکار» است.",
                   "attention", num, total)


def s_claude(s, num, total):
    P.head(s, "07 / CLAUDE / MODEL", "Claude: مدلی برای کار جدی", size=32, w=9.8)
    fams = [
        ("Haiku", "سریع و ارزان", "برای حجم بالا، دسته‌بندی و پاسخ سریع"),
        ("Sonnet", "تعادل قدرت و سرعت", "انتخاب پیش‌فرض برای بیشتر کارها"),
        ("Opus", "قوی‌ترین استدلال", "برای مسائل پیچیده و تحلیل عمیق"),
    ]
    for i, (name, tag, desc) in enumerate(fams):
        x = 8.72 - i * 3.95
        y = 2.02
        rect(s, x, y, 3.78, 1.56, LIME if i == 1 else (0xEE, 0xEA, 0xDD) if i == 0 else INK,
             radius=0.05)
        fg = INK if i != 2 else CREAM
        text(s, x + 0.22, y + 0.10, 3.3, 0.42, name, size=21, bold=True, color=fg, align=RL, font=MONO, rtl=False)
        text(s, x + 0.22, y + 0.56, 3.3, 0.26, tag, size=10, bold=True, color=fg, align=RL)
        text(s, x + 0.22, y + 0.94, 3.3, 0.50, desc, size=8.5,
             color=(0x3E, 0x3F, 0x39) if i == 1 else ((0x9F, 0xA1, 0x96) if i == 2 else (0x55, 0x56, 0x50)),
             align=RL, line_spacing=1.4)
    feats = [
        ("Context طولانی", "پنجره‌ی بزرگ برای اسناد، مخزن کد و گفتگوهای طولانی."),
        ("چندوجهی", "خواندن تصویر، نمودار و PDF؛ مناسب تحلیل مستندات."),
        ("Artifacts", "تولید و ویرایش تعاملی کد، سند و صفحه‌ی وب."),
        ("Constitutional AI", "هم‌ترازی بر پایه‌ی اصول مکتوب، نه فقط بازخورد انسانی."),
        ("امنیت و صداقت", "امتناع هوشمند، شفافیت محدودیت‌ها و کاهش توهم."),
    ]
    for i, (t, b) in enumerate(feats):
        x = 0.88 if i < 3 else 6.70
        y = 3.82 + (i if i < 3 else i - 3) * 0.88
        rect(s, x + 5.34, y + 0.09, 0.10, 0.10, LIME)
        text(s, x, y - 0.04, 5.18, 0.3, t, size=11, bold=True, align=RL)
        text(s, x, y + 0.26, 5.18, 0.52, b, size=9, color=(0x4E, 0x4F, 0x48), align=RL, line_spacing=1.4)
    line(s, 0.88, 6.45, 12.55, 6.45, (0xD6, 0xD2, 0xC6), 0.75)
    mono(s, 0.88, 6.60, 11.6, 0.22, "ANTHROPIC / CONSTITUTIONAL AI / 200K CONTEXT / VISION", size=8, color=GRAY, align=LC, tracking=1.4)
    finish(s, [], "CLAUDE", num, total)


def s_claude_code(s, num, total):
    P.head(s, "07 / CLAUDE / CODE", "Claude Code: ایجنت کدنویسی در ترمینال", size=30, w=11.4)
    P.terminal(s, 0.85, 2.10, 5.55, 4.30, [
        ("$ cd my-app && claude", LIME, True),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("> صفحه‌ی ورود را ریسپانسیو کن", (0xD8, 0xD9, 0xCF), False),
        ("> و برای موبایل تست بنویس.", (0xD8, 0xD9, 0xCF), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("● خواندن ۸ فایل و ساختار پروژه", (0x9A, 0xA2, 0x7A), False),
        ("● ویرایش ۳ فایل", (0x9A, 0xA2, 0x7A), False),
        ("● اجرای تست‌ها و لینت", (0x9A, 0xA2, 0x7A), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("✓ آماده‌ی بازبینی؛ git diff را ببین.", LIME, True),
    ], title="claude code / terminal", fs=9)
    P.bullets(s, 6.65, 2.10, 5.85, [
        ("کل مخزن را می‌خواند", "فایل‌ها را پیدا می‌کند، وابستگی‌ها را می‌فهمد و چند فایل را هم‌زمان ویرایش می‌کند."),
        ("اجرا و آزمون", "دستور شل، تست، بیلد و لینت را اجرا می‌کند و از خطا یاد می‌گیرد."),
        ("گیت", "کامیت، دیف و بازبینی؛ با تأیید شما."),
        ("MCP و ابزار", "اتصال به دیتابیس، مرورگر و سرویس‌های بیرونی."),
        ("قابل تنظیم", "CLAUDE.md برای قواعد پروژه، Hookها و Subagentها."),
    ], size=10, gap=0.06)
    finish(s, [], "CLAUDE CODE", num, total)


def s_claude_vs(s, num, total):
    P.head(s, "07 / CLAUDE / COMPARISON", "Claude و Claude Code چه تفاوتی دارند؟", size=30, w=11.4)
    rows = [
        ("ماهیت", "مدل زبانی (API / اپ)", "ابزار ایجنت روی ترمینال"),
        ("محیط", "مرورگر و اپ", "پروژه‌ی شما روی سیستم"),
        ("ورودی", "متن، تصویر، فایل", "کل مخزن کد + دستور شما"),
        ("خروجی", "پاسخ، سند، کد", "تغییر فایل، اجرای تست، کامیت"),
        ("تعامل", "پرسش و پاسخ", "حلقه‌ی چندگامی و خودکار"),
        ("مناسب برای", "تحلیل، نوشتن، مشاوره", "ساخت، رفع باگ، اتوماسیون"),
    ]
    P.table(s, 0.90, 2.08, 11.65, ["", "Claude", "Claude Code"], rows,
            widths=[2.0, 4.5, 5.15], row_h=0.52, head_h=0.44, size=9.8, head_size=10, accent_col=2)
    text(s, 0.90, 6.10, 11.6, 0.7, "Claude فکر می‌کند؛ Claude Code فکر می‌کند و کار را در محیط واقعی انجام می‌دهد. برای ساختن، دومی را انتخاب کنید.",
         size=10.5, color=GRAY, align=RL, line_spacing=1.4)
    finish(s, [], "CLAUDE VS CLAUDE CODE", num, total)
