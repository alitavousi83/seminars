# -*- coding: utf-8 -*-
import io

EDITS = [
    ("dk/sec2.py", "x = 8.66 - (i % 2) * 6.03", "x = 6.83 - (i % 2) * 6.03"),
    ("dk/sec4.py", "x = 8.72 - (i % 2) * 5.97", "x = 6.89 - (i % 2) * 6.02"),
    ("dk/sec4.py", "x = 8.85 - (i % 3) * 3.95", "x = 8.77 - (i % 3) * 3.95"),
    ("dk/sec4.py", "x = 8.70 - (i % 2) * 5.97", "x = 6.89 - (i % 2) * 6.03"),
    ("dk/sec4.py", "x = 8.80 - i * 4.03", "x = 8.75 - i * 4.03"),
    ("dk/sec4.py", "x = 8.70 - (i % 2) * 5.95", "x = 6.91 - (i % 2) * 6.05"),
]

for path, old, new in EDITS:
    s = io.open(path, encoding="utf-8").read()
    n = s.count(old)
    s = s.replace(old, new)
    io.open(path, "w", encoding="utf-8").write(s)
    print(path, n, old, "->", new)
