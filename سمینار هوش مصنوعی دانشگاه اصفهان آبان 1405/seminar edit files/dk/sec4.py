# -*- coding: utf-8 -*-
"""Section 4 — setup, practical builds, future, closing."""
from pptx.enum.shapes import MSO_SHAPE
from .theme import (W, H, M, CREAM, INK, LIME, GRAY, MONO, RL, LC, CT,
                    rect, line, text, mono, icon, icon_at, stamp, notes)
from . import parts as P
from . import covers, anim, decor


def finish(s, shapes, label, num, total):
    stamp(s, label, num, total)
    anim.transition(s)
    anim.animate(s, shapes)


def s_div8(s, num, total):
    covers.divider(s, 8, "راه‌اندازی و شروع",
                   "INSTALL / FREE OPTIONS / OLLAMA / WORKFLOW",
                   "از نصب تا اولین تسک واقعی؛\nبا گزینه‌های رایگان و مدل‌های محلی.",
                   "mesh_light", num, total)


def s_install(s, num, total):
    P.head(s, "08 / SETUP / INSTALL", "نصب و راه‌اندازی در چهار قدم", size=31, w=10.6)
    steps = [
        ("Node.js 18+", "از nodejs.org نصب کنید و نسخه را بررسی کنید.", "node -v"),
        ("نصب Claude Code", "با npm به‌صورت سراسری نصب شود.", "npm i -g @anthropic-ai/claude-code"),
        ("ورود", "بار اول، احراز هویت از مرورگر انجام می‌شود.", "claude"),
        ("شروع در پروژه", "داخل پوشه‌ی پروژه اجرا و با /init آشنا شوید.", "cd my-app && claude"),
    ]
    y = 2.12
    for i, (t, b, cmd) in enumerate(steps):
        P.pill_num(s, 11.98, y + 0.05, i + 1, 0.34, LIME if i == 0 else (0xE6, 0xE2, 0xD5))
        text(s, 7.55, y - 0.03, 4.30, 0.3, t, size=12.5, bold=True, align=RL)
        text(s, 7.55, y + 0.28, 4.30, 0.32, b, size=9, color=(0x50, 0x51, 0x4A), align=RL)
        rect(s, 0.90, y + 0.02, 6.45, 0.46, INK, radius=0.04)
        mono(s, 1.08, y + 0.14, 6.1, 0.24, "$ " + cmd, size=9, color=LIME, align=LC)
        y += 1.02
    P.terminal(s, 0.90, 5.98, 6.45, 0.95, [
        ("$ claude doctor", (0xD8, 0xD9, 0xCF), False),
        ("✓ node 20.11  ·  ✓ auth  ·  ✓ ready", LIME, True),
    ], bar=False, fs=9)
    finish(s, [], "INSTALL", num, total)


def s_free(s, num, total):
    P.head(s, "08 / SETUP / BUDGET", "رایگان، ارزان یا محلی؟", size=32, w=9.6)
    opts = [
        ("پلن رایگان", "FREE TIER", "برای شروع و یادگیری؛ محدودیت پیام و مدل.", "بدون هزینه", "محدود"),
        ("API با مصرف", "PAY AS YOU GO", "پرداخت به‌ازای توکن؛ کنترل کامل و مقیاس‌پذیر.", "متغیر", "نیاز به کلید"),
        ("مدل محلی", "OLLAMA", "روی سیستم خودتان؛ حریم خصوصی کامل.", "رایگان", "سخت‌افزار"),
        ("جایگزین‌ها", "ALTERNATIVES", "Gemini، ChatGPT، DeepSeek، Qwen و مدل‌های باز.", "متنوع", "انتخاب"),
    ]
    for i, (t, en, b, cost, note) in enumerate(opts):
        x = 6.89 - (i % 2) * 6.02
        y = 2.10 + (i // 2) * 2.12
        rect(s, x, y, 5.72, 1.94, (0xEE, 0xEA, 0xDD) if i % 3 == 0 else None,
             line=None if i % 3 == 0 else (0xC6, 0xC2, 0xB5), lw=1.0, radius=0.04)
        mono(s, x + 0.24, y + 0.18, 2.6, 0.2, en, size=7.5, color=GRAY, align=LC, tracking=1.2)
        text(s, x + 0.24, y + 0.42, 5.2, 0.3, t, size=14, bold=True, align=RL)
        text(s, x + 0.24, y + 0.84, 5.2, 0.65, b, size=9.5, color=(0x4A, 0x4B, 0x45), align=RL, line_spacing=1.45)
        text(s, x + 0.24, y + 1.55, 2.6, 0.24, cost, size=9, bold=True, color=INK, align=LC)
        text(s, x + 3.0, y + 1.55, 2.4, 0.24, note, size=8.5, color=GRAY, align=RL)
    text(s, 0.85, 6.38, 11.7, 0.4, "قیمت‌ها و سهمیه‌ها سریع تغییر می‌کنند؛ قبل از انتخاب، صفحه‌ی رسمی را ببینید. برای داده‌ی حساس، گزینه‌ی محلی همیشه امن‌تر است.",
         size=9.5, color=GRAY, align=RL)
    finish(s, [], "BUDGET OPTIONS", num, total)


def s_ollama(s, num, total):
    P.head(s, "08 / SETUP / LOCAL", "Ollama: هوش مصنوعی روی لپ‌تاپ شما", size=31, w=10.7)
    P.terminal(s, 0.88, 2.10, 4.85, 3.05, [
        ("$ ollama run qwen2.5-coder:7b", LIME, True),
        ("> این تابع را بازنویسی کن", (0xD8, 0xD9, 0xCF), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("✓ loaded in 3.2s  ·  offline", (0x9A, 0xA2, 0x7A), False),
        ("✓ 100% local  ·  private", (0x9A, 0xA2, 0x7A), False),
    ], title="terminal", fs=8.5)
    mono(s, 0.88, 5.32, 4.8, 0.2, "PRIVACY / OFFLINE / NO API KEY", size=7.5, color=GRAY, align=LC, tracking=1.2)
    text(s, 0.88, 5.58, 4.85, 0.85, "مناسب برای داده‌ی حساس، یادگیری و کار بدون اینترنت؛ در عوض، کیفیت مدل‌های کوچک کمتر از مدل‌های ابری است.",
         size=9.5, color=(0x4A, 0x4B, 0x45), align=RL, line_spacing=1.45)
    rows = [
        ("qwen2.5-coder:7b", "۴.۷ GB", "۱۶ GB", "کدنویسی"),
        ("llama3.1:8b", "۴.۹ GB", "۱۶ GB", "عمومی"),
        ("gemma3:12b", "۸.۱ GB", "۲۴ GB", "متن و تصویر"),
        ("deepseek-r1:14b", "۹.۰ GB", "۳۲ GB", "استدلال"),
        ("mistral:7b", "۴.۱ GB", "۱۶ GB", "سبک و سریع"),
    ]
    P.table(s, 6.05, 2.10, 6.45, ["مدل", "حجم", "RAM", "کاربرد"], rows,
            widths=[2.6, 1.0, 1.0, 1.6], row_h=0.48, head_h=0.40, size=8.5, head_size=8.5)
    text(s, 6.05, 5.10, 6.45, 0.4, "اعداد تقریبی‌اند؛ برای کوانتیزه‌ی ۴ بیتی.", size=8, color=GRAY, align=RL)
    text(s, 6.05, 5.45, 6.45, 0.6, "شروع: ollama.com → نصب → ollama pull <model> → ollama run <model>",
         size=9, color=INK, align=RL, font=MONO, rtl=False)
    finish(s, [], "OLLAMA", num, total)


def s_interaction(s, num, total):
    P.head(s, "08 / SETUP / WORKFLOW", "چگونه به Claude Code دستور بدهیم؟", size=30, w=11.2)
    rules = [
        ("هدف را بگو، نه فقط فایل", "«ورود باید موبایل‌فرندلی شود» بهتر از «فایل X را عوض کن» است."),
        ("اول نقشه، بعد کد", "در حالت Plan شروع کنید؛ مسیر را تأیید کنید."),
        ("کوچک و مرحله‌ای", "یک تغییر قابل تست در هر گام؛ نه ده تغییر هم‌زمان."),
        ("تست را طلب کن", "«اول تست بنویس، بعد پیاده‌سازی کن.»"),
        ("قواعد پروژه را بنویس", "CLAUDE.md: ساختار، سبک، دستورهای تست و ممنوعیت‌ها."),
        ("دیف را بخوان", "قبل از کامیت، تغییرات را بازبینی کن؛ تو مسئولی."),
    ]
    for i, (t, b) in enumerate(rules):
        y = 2.08 + i * 0.79
        mono(s, 12.30, y + 0.02, 0.3, 0.2, "", size=7)
        text(s, 8.55, y - 0.02, 3.85, 0.28, t, size=10.5, bold=True, align=RL)
        text(s, 8.55, y + 0.27, 3.85, 0.3, b, size=8.2, color=(0x50, 0x51, 0x4A), align=RL, line_spacing=1.35)
        line(s, 8.55, y + 0.72, 12.55, y + 0.72, (0xDD, 0xD9, 0xCD), 0.7) if i < 5 else None
    P.terminal(s, 0.88, 2.05, 7.35, 4.55, [
        ("$ claude", LIME, True),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("> در حالت Plan بررسی کن:", (0xD8, 0xD9, 0xCF), False),
        ("  1) چرا تست‌های auth شکست می‌خورند؟", (0xD8, 0xD9, 0xCF), False),
        ("  2) حداقل تغییر لازم چیست؟", (0xD8, 0xD9, 0xCF), False),
        ("  3) چه تستی از رگرسیون جلوگیری می‌کند؟", (0xD8, 0xD9, 0xCF), False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("  فعلاً کدی ننویس؛ فقط نقشه بده.", LIME, False),
        ("", (0xD8, 0xD9, 0xCF), False),
        ("● بررسی ۹ فایل...", (0x9A, 0xA2, 0x7A), False),
        ("● ۳ فرضیه؛ تست پیشنهادی آماده است.", (0x9A, 0xA2, 0x7A), False),
    ], title="plan mode", fs=9.5)
    finish(s, [], "WORKING WITH CLAUDE", num, total)


def s_div9(s, num, total):
    covers.divider(s, 9, "کاربردهای عملی",
                   "BUILD / CODE / MOTION / AUTOMATE",
                   "از یک ایده تا یک محصول اجراشدنی؛\nبا زبان طبیعی و یک ایجنت خوب.",
                   "tunnel", num, total)


def s_build_web(s, num, total):
    P.head(s, "09 / BUILD / WEB", "از ایده تا وب‌سایت در شش گام", size=31, w=10.8)
    # browser mock
    bx, by, bw, bh = 0.88, 2.10, 5.55, 3.72
    rect(s, bx, by, bw, bh, (0xEE, 0xEA, 0xDD), line=INK, lw=1.0, radius=0.05)
    rect(s, bx, by, bw, 0.32, INK, radius=0.05)
    rect(s, bx, by + 0.20, bw, 0.12, INK)
    for i in range(3):
        rect(s, bx + 0.16 + i * 0.16, by + 0.11, 0.08, 0.08, (0x6C, 0x6E, 0x64), shape=MSO_SHAPE.OVAL)
    rect(s, bx + 1.75, by + 0.08, 2.05, 0.17, (0x2A, 0x2C, 0x27), radius=0.4)
    mono(s, bx + 1.85, by + 0.11, 1.9, 0.14, "localhost:3000", size=6.5, color=(0xB9, 0xBA, 0xB1), align=LC)
    rect(s, bx + 0.22, by + 0.52, bw - 0.44, 1.05, LIME)
    text(s, bx + 0.40, by + 0.72, 2.6, 0.3, "تیتر اصلی محصول", size=13, bold=True, color=INK, align=LC)
    text(s, bx + 0.40, by + 1.05, 2.9, 0.24, "یک جمله‌ی کوتاه برای توضیح ارزش", size=7.5, color=(0x33, 0x34, 0x2E), align=LC)
    rect(s, bx + 3.95, by + 0.72, 1.15, 0.30, INK, radius=0.4)
    text(s, bx + 3.95, by + 0.79, 1.15, 0.18, "شروع کنید", size=7, color=LIME, align=CT)
    for i in range(3):
        x = bx + 0.22 + i * 1.72
        rect(s, x, by + 1.78, 1.55, 0.95, None, line=(0xB9, 0xB5, 0xA8), lw=0.8, radius=0.04)
        rect(s, x + 0.12, by + 1.90, 0.26, 0.26, LIME)
        rect(s, x + 0.12, by + 2.28, 1.25, 0.08, (0xB9, 0xB5, 0xA8))
        rect(s, x + 0.12, by + 2.44, 0.90, 0.08, (0xB9, 0xB5, 0xA8))
    rect(s, bx + 0.22, by + 2.92, bw - 0.44, 0.52, (0xE2, 0xDE, 0xD1))
    rect(s, bx + 0.34, by + 3.06, 2.2, 0.08, (0xC9, 0xC5, 0xB8))
    rect(s, bx + 0.34, by + 3.22, 1.4, 0.08, (0xC9, 0xC5, 0xB8))
    # steps
    steps = [
        ("۰۱", "ایده و مخاطب", "یک جمله: برای چه کسی، چه مشکلی."),
        ("۰۲", "طرح و محتوا", "ساختار صفحه و متن‌ها را بنویسید."),
        ("۰۳", "پیاده‌سازی", "«با Next.js و Tailwind بساز؛ RTL.»"),
        ("۰۴", "تست و اصلاح", "ریسپانسیو، دسترسی‌پذیری، مرورگرها."),
        ("۰۵", "دیپلوی", "Vercel / Netlify؛ دامنه و آنالیتیکس."),
        ("۰۶", "بهبود", "بازخورد، سرعت، سئو و محتوا."),
    ]
    for i, (n, t, b) in enumerate(steps):
        x = 11.95 - (i % 2) * 3.05
        y = 2.12 + (i // 2) * 1.50
        mono(s, x, y, 0.6, 0.2, n, size=8.5, color=LIME, align=LC)
        text(s, x + 0.70, y - 0.03, 2.25, 0.28, t, size=10, bold=True, align=RL)
        text(s, x + 0.70, y + 0.26, 2.30, 0.45, b, size=7.5, color=(0x50, 0x51, 0x4A), align=RL, line_spacing=1.35)
    finish(s, [], "BUILD WEB", num, total)


def s_build_code(s, num, total):
    P.head(s, "09 / BUILD / CODE", "برنامه‌نویسی با AI: گردش کار درست", size=31, w=11.0)
    steps = [
        ("۰۱", "مسئله را دقیق تعریف کن", "ورودی، خروجی و معیار موفقیت."),
        ("۰۲", "نقشه بگیر", "Plan mode؛ فایل‌ها و ریسک‌ها را ببین."),
        ("۰۳", "تست بنویس", "قبل از پیاده‌سازی، رفتار مطلوب را قفل کن."),
        ("۰۴", "کمترین تغییر", "یک پچ کوچک و قابل بازبینی."),
        ("۰۵", "اجرا و بازبینی", "تست، لینت، دیف و بررسی امنیت."),
        ("۰۶", "کامیت و مستند", "پیام واضح، توضیح تصمیم‌ها."),
    ]
    for i, (n, t, b) in enumerate(steps):
        x = 8.77 - (i % 3) * 3.95
        y = 2.10 + (i // 3) * 2.02
        rect(s, x, y, 3.78, 1.80, (0xEE, 0xEA, 0xDD) if i % 2 else None,
             line=None if i % 2 else (0xC6, 0xC2, 0xB5), lw=0.9, radius=0.04)
        mono(s, x + 0.20, y + 0.15, 0.7, 0.2, n, size=8.5, color=GRAY, align=LC)
        text(s, x + 0.20, y + 0.42, 3.35, 0.3, t, size=11, bold=True, align=RL)
        text(s, x + 0.20, y + 0.80, 3.35, 0.75, b, size=8.5, color=(0x4A, 0x4B, 0x45), align=RL, line_spacing=1.4)
    line(s, 0.90, 6.22, 12.55, 6.22, (0xD6, 0xD2, 0xC6), 1.0)
    text(s, 8.20, 6.34, 4.30, 0.3, "هرگز کورکورانه تأیید نکنید.", size=11, bold=True, align=RL)
    text(s, 0.90, 6.36, 7.0, 0.3, "کد را بخوانید، تست را اجرا کنید، و مسئولیت نهایی را بپذیرید.", size=9.5, color=GRAY, align=RL)
    finish(s, [], "CODE WORKFLOW", num, total)


def s_motion(s, num, total):
    P.head(s, "09 / BUILD / MOTION", "انیمیشن و موشن‌گرافیک با AI", size=32, w=10.6)
    tools = [
        ("Remotion", "ویدیو با React", "film"), ("GSAP", "انیمیشن وب", "zap"),
        ("Manim", "انیمیشن علمی و ریاضی", "route"), ("p5.js", "هنر تعاملی", "pen-tool"),
        ("Three.js", "صحنه‌ی سه‌بعدی", "box"), ("After Effects", "ترکیب نهایی", "palette"),
    ]
    for i, (t, d, ic) in enumerate(tools):
        x = 8.75 - (i % 3) * 3.90
        y = 2.05 + (i // 3) * 1.22
        rect(s, x, y, 3.72, 1.05, None, line=(0xC6, 0xC2, 0xB5), lw=0.9, radius=0.04)
        icon(s, ic, x + 0.24, y + 0.30, 0.40, INK)
        text(s, x + 0.78, y + 0.20, 2.75, 0.28, t, size=10.5, bold=True, align=RL, font=MONO, rtl=False)
        text(s, x + 0.78, y + 0.52, 2.75, 0.3, d, size=8, color=GRAY, align=RL)
    # pipeline
    mono(s, 0.90, 4.90, 3.0, 0.2, "PROMPT → SCENE → RENDER", size=7.5, color=GRAY, align=LC, tracking=1.2)
    steps = [("ایده", "استوری‌برد"), ("صحنه", "کد یا فریم"), ("حرکت", "زمان‌بندی"), ("رندر", "خروجی MP4")]
    for i, (t, b) in enumerate(steps):
        x = 4.52 - i * 1.18
        rect(s, x, 5.18, 1.02, 0.70, LIME if i == 3 else INK, radius=0.05)
        text(s, x, 5.26, 1.02, 0.26, t, size=9, bold=True, color=INK if i == 3 else CREAM, align=CT)
        text(s, x, 5.54, 1.02, 0.2, b, size=7, color=(0x33, 0x34, 0x2E) if i == 3 else GRAY, align=CT)
    text(s, 0.90, 6.12, 11.65, 0.5, "نکته: AI برای «تولید نسخه‌ی اول» عالی است؛ کیفیت نهایی از کارگردانی، ریتم و صدا می‌آید.",
         size=10.5, color=GRAY, align=RL)
    finish(s, [], "MOTION", num, total)


def s_automate(s, num, total):
    P.head(s, "09 / BUILD / AUTOMATION", "کارهای روزمره را خودکار کنید", size=31, w=10.8)
    items = [
        ("مرتب‌سازی فایل‌ها", "۲ ساعت → ۵ دقیقه", "اسکریپت پایتون که بر اساس نام و تاریخ دسته‌بندی می‌کند.", "folder"),
        ("گزارش اکسل", "۳ ساعت → ۱۵ دقیقه", "خواندن CSV، محاسبه‌ی شاخص‌ها و ساخت نمودار.", "chart-line"),
        ("دسته‌بندی ایمیل", "۱ ساعت → ۱۰ دقیقه", "خلاصه، اولویت‌بندی و پیش‌نویس پاسخ.", "mail"),
        ("صورت‌جلسه", "۴۵ دقیقه → ۵ دقیقه", "تبدیل صوت به متن، خلاصه و استخراج اقدام‌ها.", "file-text"),
    ]
    for i, (t, gain, b, ic) in enumerate(items):
        x = 6.89 - (i % 2) * 6.03
        y = 2.08 + (i // 2) * 2.14
        rect(s, x, y, 5.72, 1.95, None, line=(0xC6, 0xC2, 0xB5), lw=0.9, radius=0.04)
        icon(s, ic, x + 5.20, y + 0.24, 0.38, INK)
        text(s, x + 0.24, y + 0.22, 4.60, 0.3, t, size=12.5, bold=True, align=RL)
        text(s, x + 0.24, y + 0.66, 5.15, 0.28, gain, size=11, bold=True, color=INK, align=RL)
        text(s, x + 0.24, y + 1.04, 5.15, 0.72, b, size=8.8, color=(0x4A, 0x4B, 0x45), align=RL, line_spacing=1.45)
    text(s, 0.85, 6.35, 11.7, 0.4, "قاعده: کارهای تکراری، مشخص و قابل بررسی را خودکار کنید؛ نه تصمیم‌های حساس و برگشت‌ناپذیر.",
         size=10, color=GRAY, align=RL)
    finish(s, [], "AUTOMATION", num, total)


def s_nl_tools(s, num, total):
    P.head(s, "09 / BUILD / TOOLS", "ابزار بساز، فقط با زبان طبیعی", size=31, w=10.6)
    cases = [
        ("پاک‌کننده‌ی CSV", "«یک اسکریپت بنویس که ردیف‌های تکراری را حذف کند، تاریخ‌ها را یکسان کند و خروجی اکسل بدهد.»",
         "python clean.py data.csv"),
        ("استخراج فاکتور", "«از این PDF، شماره فاکتور، تاریخ، مبلغ و فروشنده را در JSON استخراج کن.»",
         "extract_invoice(pdf) → json"),
        ("ربات تلگرام", "«رباتی بساز که خلاصه‌ی روزانه‌ی خبرهای AI را هر صبح بفرستد.»",
         "cron 08:00 → telegram"),
    ]
    for i, (t, prompt, out) in enumerate(cases):
        y = 2.10 + i * 1.55
        rect(s, 0.88, y, 11.67, 1.37, INK if i == 1 else None,
             line=None if i == 1 else (0xC6, 0xC2, 0xB5), lw=0.9, radius=0.04)
        fg = CREAM if i == 1 else INK
        text(s, 1.10, y + 0.16, 2.4, 0.3, t, size=13, bold=True, color=fg, align=RL)
        mono(s, 1.10, y + 1.00, 2.6, 0.2, out, size=7.5, color=LIME if i == 1 else GRAY, align=LC)
        text(s, 3.70, y + 0.18, 8.55, 0.85, prompt, size=10.5, color=(0xD8, 0xD9, 0xCF) if i == 1 else (0x3E, 0x3F, 0x39),
             align=RL, line_spacing=1.5)
    text(s, 0.88, 6.72, 11.6, 0.24, "هر ابزار کوچک = یک قدم بزرگ در بهره‌وری شخصی.", size=9.5, color=GRAY, align=RL)
    finish(s, [], "NATURAL LANGUAGE TOOLS", num, total)


def s_div10(s, num, total):
    covers.divider(s, 10, "آینده و جمع‌بندی",
                   "TRENDS / WORK / SKILLS / ETHICS",
                   "هوش مصنوعی جای ما را نمی‌گیرد؛\nکسی که بلد است، جای کسی که بلد نیست را می‌گیرد.",
                   "halftone", num, total)


def s_trends(s, num, total):
    P.head(s, "10 / FUTURE / TRENDS", "پنج روندی که باید دنبال کنید", size=31, w=10.8)
    rows = [
        ("استدلال", "REASONING", "مدل‌ها بیشتر «فکر می‌کنند» و مسیر حل را می‌سازند.", "brain"),
        ("چندوجهی", "MULTIMODAL", "متن، تصویر، صدا و ویدیو در یک مدل و یک جریان کار.", "layers"),
        ("ایجنت‌ها", "AGENTS", "از پاسخ به اقدام؛ نرم‌افزاری که خودش کار را تمام می‌کند.", "workflow"),
        ("مدل‌های کوچک", "ON-DEVICE", "مدل سبک روی گوشی و لپ‌تاپ؛ سریع، خصوصی و ارزان.", "cpu"),
        ("بدن و رباتیک", "EMBODIED AI", "ترکیب مدل با حسگر و حرکت؛ از کارخانه تا خانه.", "bot"),
    ]
    for i, (t, en, b, ic) in enumerate(rows):
        y = 2.05 + i * 0.92
        icon(s, ic, 12.10, y + 0.12, 0.34, INK)
        mono(s, 11.45, y + 0.18, 0.55, 0.2, "0%d" % (i + 1), size=7.5, color=GRAY, align=RL)
        text(s, 5.55, y - 0.03, 5.75, 0.3, t, size=12.5, bold=True, align=RL)
        mono(s, 5.55, y + 0.30, 5.75, 0.18, en, size=7, color=LIME, align=RL, tracking=1.2)
        text(s, 0.90, y + 0.20, 4.55, 0.5, b, size=9, color=(0x50, 0x51, 0x4A), align=RL, line_spacing=1.4)
        line(s, 0.90, y + 0.80, 12.55, y + 0.80, (0xDD, 0xD9, 0xCD), 0.7) if i < 4 else None
    text(s, 0.90, 6.72, 11.6, 0.24, "مهم‌ترین روند؟ ترکیب همین‌ها: ایجنتی که چندوجهی است و روی دستگاه شما فکر می‌کند.",
         size=9, color=GRAY, align=RL)
    finish(s, [], "TRENDS", num, total)


def s_work(s, num, total):
    P.head(s, "10 / FUTURE / WORK", "AI چه چیزی را عوض می‌کند؟", size=32, w=9.8)
    # matrix
    mx, my, mw, mh = 0.95, 2.15, 6.20, 4.10
    line(s, mx + mw / 2, my, mx + mw / 2, my + mh, INK, 1.0)
    line(s, mx, my + mh / 2, mx + mw, my + mh / 2, INK, 1.0)
    mono(s, mx + 0.10, my + 0.10, 2.0, 0.2, "AUTOMATE", size=7, color=GRAY, align=LC, tracking=1)
    mono(s, mx + mw - 1.6, my + 0.10, 1.5, 0.2, "AUGMENT", size=7, color=GRAY, align=RL, tracking=1)
    quads = [
        (mx + 0.15, my + 0.18, "کارهای روتین", "داده‌ی ورود، فاکتور، پاسخ‌های تکراری", LIME),
        (mx + mw / 2 + 0.15, my + 0.18, "تحلیل و تصمیم", "پژوهش، مدل‌سازی، استراتژی", None),
        (mx + 0.15, my + mh / 2 + 0.15, "خلاقیت مقیاس‌پذیر", "محتوا، طراحی، ویدیو", None),
        (mx + mw / 2 + 0.15, my + mh / 2 + 0.15, "همکاری انسان–AI", "کد، مشاوره، آموزش", None),
    ]
    for x, y, t, b, fill in quads:
        if fill:
            rect(s, x, y, 2.55, 1.45, fill)
        text(s, x + 0.10, y + 0.12, 2.35, 0.28, t, size=10.5, bold=True, align=RL)
        text(s, x + 0.10, y + 0.48, 2.35, 0.8, b, size=8, color=(0x45, 0x46, 0x40), align=RL, line_spacing=1.4)
    text(s, mx, 6.38, 6.2, 0.23, "محورها: نوع کار × نقش انسان", size=8, color=GRAY, align=LC)
    P.bullets(s, 7.55, 2.10, 5.00, [
        ("جابه‌جایی، نه حذف", "بیشتر مشاغل بازطراحی می‌شوند؛ وظایف تکراری کم و وظایف نظارتی زیاد می‌شود."),
        ("مهارت‌های برنده", "تعریف مسئله، راستی‌آزمایی، ترکیب ابزارها و ارتباط انسانی."),
        ("مزیت کسب‌وکار", "سرعت اجرا و شخصی‌سازی؛ نه صرفاً کاهش هزینه."),
    ], size=10, gap=0.14)
    finish(s, [], "FUTURE OF WORK", num, total)


def s_skills(s, num, total):
    P.head(s, "10 / FUTURE / SKILLS", "نقشه‌راه ۹۰ روزه‌ی یادگیری", size=31, w=10.2)
    cols = [
        ("۳۰ روز اول", "پایه", ["یک ابزار را روزانه استفاده کن", "پرامپت‌نویسی را تمرین کن", "Ollama را نصب و تست کن"]),
        ("۳۰ روز دوم", "ساخت", ["یک پروژه‌ی کوچک با Claude Code", "اتوماسیون یک کار تکراری", "خواندن کد و بازبینی دیف"]),
        ("۳۰ روز سوم", "تخصص", ["یک ایجنت واقعی با ابزار", "RAG روی اسناد خودت", "ساخت محتوای حرفه‌ای با AI"]),
    ]
    for i, (t, tag, items) in enumerate(cols):
        x = 8.75 - i * 4.03
        rect(s, x, 2.10, 3.85, 3.90, INK if i == 2 else None,
             line=None if i == 2 else (0xC6, 0xC2, 0xB5), lw=1.0, radius=0.05)
        fg = CREAM if i == 2 else INK
        mono(s, x + 0.24, 2.28, 2.0, 0.2, "PHASE 0%d" % (i + 1), size=7.5, color=LIME, align=LC, tracking=1.2)
        text(s, x + 0.24, 2.55, 3.35, 0.35, t, size=16, bold=True, color=fg, align=RL)
        text(s, x + 0.24, 2.98, 3.35, 0.3, tag, size=9, color=(0x9F, 0xA1, 0x96) if i == 2 else GRAY, align=RL)
        yy = 3.45
        for it in items:
            rect(s, x + 3.42, yy + 0.06, 0.10, 0.10, LIME)
            text(s, x + 0.24, yy - 0.04, 3.05, 0.55, it, size=8.8, color=fg if i == 2 else (0x3E, 0x3F, 0x39),
                 align=RL, line_spacing=1.4)
            yy += 0.70
    text(s, 0.88, 6.25, 11.65, 0.6, "منابع پیشنهادی: دوره‌ی Machine Learning اندرو اینگ، سری «Zero to Hero» آندری کارپاتی، مستندات Anthropic و OpenAI Cookbook.",
         size=9.5, color=GRAY, align=RL, line_spacing=1.4)
    finish(s, [], "SKILL ROADMAP", num, total)


def s_ethics(s, num, total):
    P.head(s, "10 / FUTURE / ETHICS", "اخلاق، امنیت و قانون", size=32, w=9.4)
    items = [
        ("حریم خصوصی", "داده‌ی شخصی و محرمانه را وارد نکنید؛ سیاست نگهداری را بخوانید.", "lock"),
        ("سوگیری", "داده‌ی آموزش می‌تواند تبعیض را بازتولید کند؛ خروجی را با گروه‌های مختلف تست کنید.", "users"),
        ("حق نشر", "مجوز تصویر و متن تولیدشده را بررسی کنید؛ برای برند، اصالت را حفظ کنید.", "scale"),
        ("امنیت", "تزریق پرامپت و دسترسی ابزار، سطح حمله‌ی جدیدی می‌سازد؛ حداقل دسترسی بدهید.", "shield"),
    ]
    for i, (t, b, ic) in enumerate(items):
        x = 6.91 - (i % 2) * 6.05
        y = 2.10 + (i // 2) * 2.20
        rect(s, x, y, 5.70, 2.02, None, line=(0xC6, 0xC2, 0xB5), lw=0.9, radius=0.04)
        icon(s, ic, x + 5.15, y + 0.24, 0.38, INK)
        text(s, x + 0.24, y + 0.22, 4.55, 0.3, t, size=13, bold=True, align=RL)
        text(s, x + 0.24, y + 0.66, 5.15, 1.0, b, size=9.5, color=(0x4A, 0x4B, 0x45), align=RL, line_spacing=1.5)
    finish(s, [], "ETHICS & SAFETY", num, total)


def s_summary(s, num, total):
    P.head(s, "10 / WRAP-UP / 10 TAKEAWAYS", "ده نکته که با خودتان ببرید", size=31, w=10.6)
    points = [
        "AI = یادگیری الگو از داده، نه جادو.",
        "مدل زبانی، پیش‌بینی‌کننده‌ی توکن بعدی است.",
        "کیفیت داده و هم‌ترازی، مهم‌تر از اندازه است.",
        "Attention، قلب درک زمینه در Transformer است.",
        "Context، حافظه‌ی کاری و محدودیت اصلی است.",
        "پرامپت خوب = هدف + زمینه + قالب + مثال.",
        "ابزار را با کار انتخاب کنید، نه با تبلیغ.",
        "ایجنت = مدل + ابزار + حافظه + حلقه.",
        "Claude Code برای ساختن است، نه فقط پاسخ دادن.",
        "انسانِ مسئول، همیشه بخشی از حلقه بماند.",
    ]
    for i, p in enumerate(points):
        col = i // 5
        row = i % 5
        x = 7.00 if col == 0 else 0.90
        y = 2.10 + row * 0.88
        mono(s, x + 5.05, y + 0.05, 0.55, 0.22, "%02d" % (i + 1), size=9, color=LIME, align=RL, bold=True)
        text(s, x, y, 4.90, 0.6, p, size=10.5, align=RL, line_spacing=1.35)
        line(s, x, y + 0.74, x + 5.55, y + 0.74, (0xDD, 0xD9, 0xCD), 0.7) if row < 4 else None
    line(s, 6.82, 2.10, 6.82, 6.45, (0xD6, 0xD2, 0xC6), 0.9)
    finish(s, [], "SUMMARY", num, total)


def s_resources(s, num, total):
    P.head(s, "10 / WRAP-UP / RESOURCES", "برای ادامه‌ی مسیر", size=32, w=9.4)
    cols = [
        ("دوره‌ها", "COURSES", ["Machine Learning — Andrew Ng", "Deep Learning Specialization", "Karpathy: Zero to Hero", "Fast.ai"]),
        ("مستندات", "DOCS", ["docs.anthropic.com", "Claude Code Docs", "OpenAI Cookbook", "Hugging Face Course"]),
        ("کتاب و مقاله", "READS", ["Attention Is All You Need", "Build a Large Language Model", "Designing Machine Learning Systems", "The Alignment Problem"]),
    ]
    for i, (t, en, items) in enumerate(cols):
        x = 8.75 - i * 4.03
        mono(s, x, 2.10, 3.7, 0.2, en, size=7.5, color=LIME, align=LC, tracking=1.4)
        text(s, x, 2.35, 3.7, 0.35, t, size=15, bold=True, align=RL)
        line(s, x, 2.82, x + 3.70, 2.82, INK, 1.2)
        for j, it in enumerate(items):
            text(s, x, 3.02 + j * 0.78, 3.70, 0.6, it, size=8.8, color=(0x45, 0x46, 0x40), align=RL, line_spacing=1.4)
    rect(s, 0.88, 6.28, 11.67, 0.52, LIME)
    text(s, 1.05, 6.40, 11.35, 0.3, "بهترین منبع، پروژه‌ی خودتان است: یک کار واقعی را انتخاب کنید و با AI انجامش دهید.",
         size=10.5, bold=True, color=INK, align=RL)
    finish(s, [], "RESOURCES", num, total)


def s_qa(s, num, total):
    covers.qa(s, total)
    anim.transition(s, "fade", "slow")
