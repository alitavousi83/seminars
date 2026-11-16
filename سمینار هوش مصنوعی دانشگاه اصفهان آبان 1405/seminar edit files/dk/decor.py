# -*- coding: utf-8 -*-
"""Generative art + vector icon rasterizer for the deck (no external assets)."""
import os, re, math, hashlib, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(HERE, "assets", "art")
ICONS = os.path.join(HERE, "assets", "icons")
os.makedirs(ART, exist_ok=True)
os.makedirs(ICONS, exist_ok=True)

CREAM = (245, 241, 232)
INK = (17, 17, 17)
LIME = (200, 255, 0)
GRAY = (138, 138, 132)

FONT_DIR = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "Windows", "Fonts")
F_BLACK = os.path.join(FONT_DIR, "Vazirmatn-Black.ttf")
F_BOLD = os.path.join(FONT_DIR, "Vazirmatn-Bold.ttf")
F_MED = os.path.join(FONT_DIR, "Vazirmatn-Medium.ttf")


# ----------------------------------------------------------------------------- icons
def fetch_svg(name):
    path = os.path.join(ICONS, name + ".svg")
    if not os.path.exists(path):
        url = "https://unpkg.com/lucide-static@latest/icons/%s.svg" % name
        data = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
        open(path, "w", encoding="utf-8").write(data)
    return open(path, encoding="utf-8").read()


def _nums(s):
    return [float(v) for v in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", s)]


def _arc(cx, cy, rx, ry, a0, a1, n=14):
    if rx == 0 or ry == 0:
        return [(cx, cy)]
    pts = []
    for i in range(n + 1):
        a = a0 + (a1 - a0) * i / n
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    return pts


def _arc_from_endpoints(x1, y1, rx, ry, phi, large, sweep, x2, y2):
    """SVG endpoint arc -> center parameterization (W3C implementation notes)."""
    phi = math.radians(phi)
    cosp, sinp = math.cos(phi), math.sin(phi)
    dx2, dy2 = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    x1p = cosp * dx2 + sinp * dy2
    y1p = -sinp * dx2 + cosp * dy2
    rx, ry = abs(rx), abs(ry)
    lam = x1p ** 2 / (rx ** 2) + y1p ** 2 / (ry ** 2)
    if lam > 1:
        rx *= math.sqrt(lam); ry *= math.sqrt(lam)
    num = rx ** 2 * ry ** 2 - rx ** 2 * y1p ** 2 - ry ** 2 * x1p ** 2
    den = rx ** 2 * y1p ** 2 + ry ** 2 * x1p ** 2
    co = math.sqrt(max(0, num / den)) if den else 0
    if large == sweep:
        co = -co
    cxp = co * rx * y1p / ry
    cyp = -co * ry * x1p / rx
    cx = cosp * cxp - sinp * cyp + (x1 + x2) / 2
    cy = sinp * cxp + cosp * cyp + (y1 + y2) / 2
    def ang(ux, uy, vx, vy):
        a = math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
        return a
    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not sweep and dt > 0:
        dt -= 2 * math.pi
    if sweep and dt < 0:
        dt += 2 * math.pi
    return cx, cy, rx, ry, phi, t1, t1 + dt


def _path_subpaths(d):
    tok = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|-?\d*\.?\d+(?:e-?\d+)?", d)
    i = 0; cmd = None; cur = (0, 0); start = (0, 0); prev_ctrl = None
    subs = []; pts = []
    def flush():
        nonlocal pts
        if len(pts) > 1:
            subs.append(pts)
        pts = []
    while i < len(tok):
        t = tok[i]
        if re.match(r"[A-Za-z]", t):
            cmd = t; i += 1
            if cmd in "Zz":
                if pts:
                    pts.append(start); flush()
                cur = start; prev_ctrl = None
                continue
        rel = cmd.islower(); C = cmd.upper()
        def take(n):
            nonlocal i
            vals = [float(v) for v in tok[i:i + n]]
            i += n
            return vals
        if C == "M":
            x, y = take(2)
            if rel: x, y = cur[0] + x, cur[1] + y
            flush(); pts = [(x, y)]; cur = (x, y); start = (x, y); prev_ctrl = None
            cmd = "l" if rel else "L"
        elif C == "L":
            x, y = take(2)
            if rel: x, y = cur[0] + x, cur[1] + y
            pts.append((x, y)); cur = (x, y); prev_ctrl = None
        elif C == "H":
            x = take(1)[0]
            x = cur[0] + x if rel else x
            pts.append((x, cur[1])); cur = (x, cur[1]); prev_ctrl = None
        elif C == "V":
            y = take(1)[0]
            y = cur[1] + y if rel else y
            pts.append((cur[0], y)); cur = (cur[0], y); prev_ctrl = None
        elif C in "CS":
            if C == "C":
                x1, y1, x2, y2, x, y = take(6)
                if rel:
                    x1 += cur[0]; y1 += cur[1]; x2 += cur[0]; y2 += cur[1]; x += cur[0]; y += cur[1]
            else:
                x2, y2, x, y = take(4)
                if rel:
                    x2 += cur[0]; y2 += cur[1]; x += cur[0]; y += cur[1]
                x1, y1 = (2 * cur[0] - prev_ctrl[0], 2 * cur[1] - prev_ctrl[1]) if prev_ctrl else cur
            p0 = cur
            for k in range(1, 17):
                u = k / 16
                bx = (1-u)**3*p0[0] + 3*(1-u)**2*u*x1 + 3*(1-u)*u*u*x2 + u**3*x
                by = (1-u)**3*p0[1] + 3*(1-u)**2*u*y1 + 3*(1-u)*u*u*y2 + u**3*y
                pts.append((bx, by))
            prev_ctrl = (x2, y2); cur = (x, y)
        elif C in "QT":
            if C == "Q":
                x1, y1, x, y = take(4)
                if rel:
                    x1 += cur[0]; y1 += cur[1]; x += cur[0]; y += cur[1]
            else:
                x, y = take(2)
                if rel: x += cur[0]; y += cur[1]
                x1, y1 = (2*cur[0]-prev_ctrl[0], 2*cur[1]-prev_ctrl[1]) if prev_ctrl else cur
            p0 = cur
            for k in range(1, 17):
                u = k / 16
                bx = (1-u)**2*p0[0] + 2*(1-u)*u*x1 + u*u*x
                by = (1-u)**2*p0[1] + 2*(1-u)*u*y1 + u*u*y
                pts.append((bx, by))
            prev_ctrl = (x1, y1); cur = (x, y)
        elif C == "A":
            rx, ry, phi = take(3)
            def flag():
                nonlocal i
                t = tok[i]; i += 1
                if len(t) > 1 and t[0] in "01":
                    tok.insert(i, t[1:])
                    return int(t[0])
                return int(float(t))
            large, sweep = flag(), flag()
            x, y = take(2)
            if rel: x += cur[0]; y += cur[1]
            if rx == 0 or ry == 0:
                pts.append((x, y))
            else:
                cx, cy, rx, ry, ph, a1, a2 = _arc_from_endpoints(
                    cur[0], cur[1], rx, ry, phi, int(large), int(sweep), x, y)
                seg = []
                for k in range(1, 17):
                    a = a1 + (a2 - a1) * k / 16
                    ex, ey = cx + rx*math.cos(a), cy + ry*math.sin(a)
                    seg.append((ph == 0 and (ex, ey) or (
                        math.cos(ph)*(ex-cx) - math.sin(ph)*(ey-cy) + cx,
                        math.sin(ph)*(ex-cx) + math.cos(ph)*(ey-cy) + cy)))
                pts.extend(seg)
            cur = (x, y); prev_ctrl = None
        else:
            i += 1
    flush()
    return subs


def _svg_subpaths(svg):
    subs = []
    for m in re.finditer(r"<path[^>]*\sd=\"([^\"]+)\"", svg):
        subs.extend(_path_subpaths(m.group(1)))
    for m in re.finditer(r"<circle[^>]*>", svg):
        cx, cy = _attr(m.group(0), "cx", 0), _attr(m.group(0), "cy", 0)
        r = _attr(m.group(0), "r", 0)
        subs.append(_arc(cx, cy, r, r, 0, 2 * math.pi, 40))
    for m in re.finditer(r"<rect[^>]*>", svg):
        x, y = _attr(m.group(0), "x", 0), _attr(m.group(0), "y", 0)
        w, h = _attr(m.group(0), "width", 0), _attr(m.group(0), "height", 0)
        rx = _attr(m.group(0), "rx", 0)
        if rx:
            subs.extend([_arc(x+rx, y+rx, rx, rx, math.pi, 1.5*math.pi),
                         [(x+rx, y), (x+w-rx, y)],
                         _arc(x+w-rx, y+rx, rx, rx, 1.5*math.pi, 2*math.pi),
                         [(x+w, y+rx), (x+w, y+h-rx)],
                         _arc(x+w-rx, y+h-rx, rx, rx, 0, .5*math.pi),
                         [(x+w-rx, y+h), (x+rx, y+h)],
                         _arc(x+rx, y+h-rx, rx, rx, .5*math.pi, math.pi),
                         [(x, y+h-rx), (x, y+rx)]])
        else:
            subs.append([(x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)])
    for m in re.finditer(r"<line[^>]*>", svg):
        s = m.group(0)
        subs.append([(_attr(s, "x1", 0), _attr(s, "y1", 0)), (_attr(s, "x2", 0), _attr(s, "y2", 0))])
    for m in re.finditer(r"<poly(?:line|gon)[^>]*>", svg):
        s = m.group(0)
        v = _nums(re.search(r"points=\"([^\"]+)\"", s).group(1))
        sub = list(zip(v[0::2], v[1::2]))
        if "polygon" in s and sub:
            sub.append(sub[0])
        subs.append(sub)
    return subs


def _attr(s, name, default):
    m = re.search(r"\s%s=\"([^\"]+)\"" % name, s)
    return float(m.group(1)) if m else default


def icon_path(name, px=512, color=LIME, stroke=2.0, ss=3):
    """Rasterize a lucide icon to a transparent PNG, return path."""
    key = hashlib.md5(("%s|%d|%s|%s" % (name, px, color, stroke)).encode()).hexdigest()[:10]
    out = os.path.join(ICONS, "r_%s_%s.png" % (name, key))
    if os.path.exists(out):
        return out
    subs = _svg_subpaths(fetch_svg(name))
    size = px * ss
    pad = stroke / 2 + 0.6
    k = size / (24 + 2 * pad)
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    w = max(1, int(round(stroke * k)))
    col = tuple(color) + (255,)
    for sp in subs:
        pts = [((x + pad) * k, (y + pad) * k) for x, y in sp]
        if len(pts) < 2:
            continue
        d.line(pts, fill=col, width=w, joint="curve")
        for p in (pts[0], pts[-1]):
            d.ellipse([p[0]-w/2, p[1]-w/2, p[0]+w/2, p[1]+w/2], fill=col)
    img = img.resize((px, px), Image.LANCZOS)
    img.save(out)
    return out


# ----------------------------------------------------------------------------- helpers
def _canvas(w, h):
    return np.zeros((h, w, 3), dtype=np.float32)


def _grid(w, h):
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    return x / w, y / h


def _gauss(X, Y, cx, cy, sx, sy, rot=0.0):
    dx, dy = X - cx, Y - cy
    if rot:
        c, s = math.cos(rot), math.sin(rot)
        dx, dy = c*dx + s*dy, -s*dx + c*dy
    return np.exp(-((dx/sx)**2 + (dy/sy)**2))


def _blend(base, color, alpha):
    a = np.clip(alpha, 0, 1)[..., None]
    c = np.array(color, dtype=np.float32)
    return base * (1 - a) + c * a


def _grain(img, amount=6, seed=7):
    rng = np.random.default_rng(seed)
    n = rng.normal(0, amount, img.shape[:2])[..., None]
    return np.clip(img + n, 0, 255)


def _finish(arr, path, quality=87):
    img = Image.fromarray(_grain(arr).astype(np.uint8))
    if path.endswith(".png"):
        img.save(path)
    else:
        img.save(path, quality=quality, subsampling=1, optimize=True)
    return path


def _vignette(arr, strength=0.35):
    h, w = arr.shape[:2]
    X, Y = _grid(w, h)
    v = 1 - strength * (((X-0.5)**2 + (Y-0.5)**2) * 2.2) ** 1.3
    return np.clip(arr * np.clip(v, 0.25, 1)[..., None], 0, 255)


# ----------------------------------------------------------------------------- artworks
def art_orb(path, dark=True, seed=3, w=2200, h=1240):
    X, Y = _grid(w, h)
    base = np.zeros((h, w, 3), dtype=np.float32) + (np.array(INK) if dark else np.array(CREAM))
    # backdrop glow
    base = _blend(base, LIME, 0.10 * _gauss(X, Y, 0.72, 0.5, 0.42, 0.55))
    cx, cy, r = 0.66, 0.5, 0.30
    dx, dy = (X - cx) * w / h, (Y - cy)
    d = np.sqrt(dx**2 + dy**2)
    inside = np.clip((r - d) / 0.006, 0, 1)
    z = np.sqrt(np.clip(1 - (d / r) ** 2, 0, 1))
    # lighting
    lx, ly, lz = -0.45, -0.55, 0.7
    shade = np.clip((dx/r)*lx + (dy/r)*ly + z*lz, 0, 1)
    sphere = np.zeros((h, w, 3), dtype=np.float32) + np.array([22, 24, 26])
    sphere = _blend(sphere, (60, 66, 58), shade ** 2.2)
    sphere = _blend(sphere, LIME, 0.55 * np.clip(shade - 0.55, 0, 1) ** 1.5)
    rim = np.clip((z - 0.55) / 0.45, 0, 1) ** 6
    sphere = _blend(sphere, LIME, 0.9 * rim)
    out = base * (1 - inside[..., None]) + sphere * inside[..., None]
    # orbit rings
    for i, (rr, al) in enumerate([(0.365, 0.30), (0.415, 0.16)]):
        ring = np.exp(-((np.sqrt(dx**2 + (dy*1.0)**2) - rr) / 0.0025) ** 2)
        out = _blend(out, LIME, al * ring)
    # scanline ticks
    out = _vignette(out, 0.45)
    return _finish(out, path)


def art_mesh(path, seed=11, dark=False, w=2200, h=1240):
    rng = np.random.default_rng(seed)
    X, Y = _grid(w, h)
    arr = np.zeros((h, w, 3), dtype=np.float32) + (np.array(INK) if dark else np.array(CREAM))
    palette = [LIME, (255, 255, 240), (70, 72, 66), (200, 255, 0)]
    for i in range(5):
        cx, cy = rng.uniform(0.1, 0.95), rng.uniform(0.0, 1.0)
        sx, sy = rng.uniform(0.12, 0.42), rng.uniform(0.10, 0.35)
        a = rng.uniform(0.18, 0.5) if dark else rng.uniform(0.10, 0.30)
        col = palette[int(rng.integers(0, len(palette)))] if dark else [LIME, (17,17,17), (138,138,132)][int(rng.integers(0,3))]
        arr = _blend(arr, col, a * _gauss(X, Y, cx, cy, sx, sy, rng.uniform(-1, 1)))
    arr = np.clip(arr, 0, 255)
    arr = np.array(Image.fromarray(arr.astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)))
    return _finish(_vignette(arr, 0.18), path)


def art_nodes(path, dark=True, seed=5, w=2200, h=1240):
    rng = np.random.default_rng(seed)
    ss = 2
    W, H = w * ss, h * ss
    bg = (INK if dark else CREAM)
    img = Image.new("RGB", (W, H), bg)
    layer = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(layer)
    n = 78
    pts = []
    for i in range(n):
        # cluster toward right side
        x = rng.normal(0.66, 0.24) if rng.random() < 0.8 else rng.uniform(0, 1)
        y = rng.normal(0.52, 0.3)
        pts.append((np.clip(x, 0.02, 0.98) * W, np.clip(y, 0.02, 0.98) * H, rng.uniform(2, 9)))
    for i, p in enumerate(pts):
        dists = sorted(((math.dist(p[:2], q[:2]), j) for j, q in enumerate(pts) if j != i))[:3]
        for dd, j in dists:
            if dd < 0.38 * W:
                a = int(60 + 150 * (1 - dd / (0.38 * W)))
                col = LIME if dark else (30, 30, 30)
                d.line([p[:2], pts[j][:2]], fill=tuple(int(c * a / 255) for c in col), width=int(1.2 * ss))
    glow = layer.filter(ImageFilter.GaussianBlur(9 * ss))
    img = Image.fromarray(np.clip(np.array(img, dtype=np.float32) + np.array(glow, dtype=np.float32) * 1.5, 0, 255).astype(np.uint8))
    d2 = ImageDraw.Draw(img)
    for x, y, r in pts:
        rr = r * ss
        d2.ellipse([x-rr, y-rr, x+rr, y+rr], fill=(LIME if dark else (17, 17, 17)))
        d2.ellipse([x-rr*0.35, y-rr*0.35, x+rr*0.35, y+rr*0.35], fill=bg)
    img = img.resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.3), path)


def art_halftone(path, dark=True, seed=9, w=2200, h=1240):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), (INK if dark else CREAM))
    d = ImageDraw.Draw(img)
    step = int(34 * ss)
    fg = LIME if dark else (17, 17, 17)
    cx, cy = W * 0.68, H * 0.5
    for y in range(0, H, step):
        for x in range(0, W, step):
            dx, dy = (x - cx) / W, (y - cy) / H
            r = math.hypot(dx, dy)
            v = 0.5 + 0.5 * math.sin(r * 38 + math.atan2(dy, dx) * 1.2)
            rad = (0.10 + 0.95 * v) * step * 0.42 * max(0.15, 1 - r * 0.9)
            if rad > 0.4:
                d.ellipse([x-rad, y-rad, x+rad, y+rad], fill=fg)
    img = img.resize((w, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.4))
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.35), path)


def art_contour(path, seed=21, w=2200, h=1240):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    for i in range(46):
        t = i / 45
        pts = []
        for k in range(240):
            a = 2 * math.pi * k / 240
            rr = (0.16 + 0.55 * t) * (1 + 0.10 * math.sin(3 * a + t * 7) + 0.05 * math.cos(5 * a - t * 4))
            pts.append((W * (0.62 + rr * math.cos(a) * 1.15), H * (0.52 + rr * math.sin(a))))
        col = LIME if i % 5 == 0 else (70, 74, 66)
        d.line(pts + [pts[0]], fill=col, width=2 * ss if i % 5 == 0 else 1 * ss)
    img = img.filter(ImageFilter.GaussianBlur(int(1.2 * ss))).resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.35), path)


def art_tunnel(path, seed=4, w=2200, h=1240):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    cx, cy = W * 0.62, H * 0.5
    for i in range(26):
        t = i / 25
        rw = W * (0.55 * (1 - t) ** 1.7 + 0.012)
        rh = H * (0.62 * (1 - t) ** 1.7 + 0.015)
        col = LIME if i in (0, 6, 14, 25) else (48 + int(40 * t), 50 + int(40 * t), 44 + int(38 * t))
        d.rectangle([cx - rw, cy - rh, cx + rw, cy + rh], outline=col, width=(3 if i in (0,6,14,25) else 1) * ss)
    for k in range(28):
        a = 2 * math.pi * k / 28
        d.line([(cx, cy), (cx + math.cos(a) * W, cy + math.sin(a) * H)], fill=(26, 28, 26), width=ss)
    img = img.filter(ImageFilter.GaussianBlur(int(0.6 * ss))).resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.3), path)


def art_attention(path, seed=12, w=2200, h=1240):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    n = 22
    cs = int(H * 0.82 / n)
    ox, oy = int(W * 0.52), int(H * 0.09)
    rng = np.random.default_rng(seed)
    for i in range(n):
        for j in range(n):
            v = math.exp(-abs(i - j) / 3.0) * 0.8 + rng.uniform(0, 0.25)
            if i in (4, 11) or j in (4, 11):
                v += 0.22
            v = min(1.0, v)
            col = tuple(int(c * (0.06 + 0.94 * v)) for c in LIME)
            if v < 0.12:
                col = (32, 34, 30)
            d.rectangle([ox + j*cs, oy + i*cs, ox + j*cs + cs - 2*ss, oy + i*cs + cs - 2*ss], fill=col)
    img = img.resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.3), path)


def art_wave(path, seed=6, w=2200, h=1240):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    rng = np.random.default_rng(seed)
    n = 96
    step = W / n
    for i in range(n):
        t = i / (n - 1)
        env = math.exp(-((t - 0.55) ** 2) / 0.08) * 0.85 + 0.08
        hh = env * (0.28 + 0.72 * abs(math.sin(t * 19 + 1.2)) * rng.uniform(0.5, 1))
        hh = hh * H * 0.55
        x = i * step
        col = LIME if i % 7 == 0 else (150, 190, 0)
        d.rectangle([x, H * 0.52 - hh / 2, x + step * 0.42, H * 0.52 + hh / 2], fill=col)
    img = img.filter(ImageFilter.GaussianBlur(int(1.4 * ss))).resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.35), path)


def art_geo(path, seed=8, w=2200, h=1240):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), CREAM)
    rng = np.random.default_rng(seed)
    shapes = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(shapes)
    for i in range(7):
        cx, cy = rng.uniform(0.45, 0.95) * W, rng.uniform(-0.1, 1.1) * H
        r = rng.uniform(0.12, 0.34) * W
        col = [(17, 17, 17, 40), (200, 255, 0, 70), (138, 138, 132, 45)][i % 3]
        if i % 3 == 0:
            d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=col)
        elif i % 3 == 1:
            d.rectangle([cx-r*0.8, cy-r*0.8, cx+r*0.8, cy+r*0.8], fill=col)
        else:
            d.polygon([(cx, cy-r), (cx+r*0.9, cy+r*0.7), (cx-r*0.9, cy+r*0.7)], fill=col)
    img = Image.alpha_composite(img.convert("RGBA"), shapes).convert("RGB")
    img = img.filter(ImageFilter.GaussianBlur(int(0.8 * ss))).resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.12), path)


def art_poster(path, word="AI", w=1400, h=1800):
    ss = 2
    W, H = w * ss, h * ss
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    # concentric lime arcs
    for i in range(9):
        r = W * (0.42 + i * 0.075)
        d.arc([W*0.5-r, H*0.52-r, W*0.5+r, H*0.52+r], 200, 340, fill=LIME if i % 3 == 0 else (60, 64, 56), width=(3 if i % 3 == 0 else 1) * ss)
    from PIL import ImageFont
    try:
        f = ImageFont.truetype(F_BLACK, int(W * 0.94))
    except Exception:
        f = ImageFont.load_default()
    bbox = d.textbbox((0, 0), word, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((W - tw) / 2 - bbox[0], (H - th) / 2 - bbox[1] - H * 0.02), word, font=f, fill=LIME)
    img = img.resize((w, h), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    return _finish(_vignette(arr, 0.3), path)


ARTWORKS = {
    "orb": lambda p: art_orb(p),
    "mesh_dark": lambda p: art_mesh(p, seed=11, dark=True),
    "mesh_light": lambda p: art_mesh(p, seed=23, dark=False),
    "nodes_dark": lambda p: art_nodes(p, dark=True),
    "nodes_light": lambda p: art_nodes(p, seed=15, dark=False),
    "halftone": lambda p: art_halftone(p),
    "contour": lambda p: art_contour(p),
    "tunnel": lambda p: art_tunnel(p),
    "attention": lambda p: art_attention(p),
    "wave": lambda p: art_wave(p),
    "geo": lambda p: art_geo(p),
    "poster": lambda p: art_poster(p),
}


def ensure_art(names=None):
    out = {}
    for name in (names or ARTWORKS):
        p = os.path.join(ART, name + (".png" if name == "poster" else ".jpg"))
        if not os.path.exists(p):
            ARTWORKS[name](p)
        out[name] = p
    return out
