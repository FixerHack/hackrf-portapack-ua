"""Перевіряє посилання у зібраному site/.
- BROKEN: внутрішнє посилання на неіснуючий файл
- SHOULD-BE-LOCAL: посилання на вікі GitHub, хоча сторінка є на сайті (крім банера «Оригінал на GitHub»)
- MISSING: посилання на сторінки вікі, яких немає ні локально, ні в копії (можуть бути 404 на GitHub)
"""
import re, sys, urllib.parse, html as H
from pathlib import Path
sys.path.insert(0, "scripts")
src = Path("scripts/build_docs.py").read_text().replace("\nmain()\n", "\n")
ns = {"__file__": "scripts/build_docs.py"}; exec(compile(src, "bd", "exec"), ns)
norm, pages = ns["norm"], ns["pages"]
SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
WIKI = "https://github.com/portapack-mayhem/mayhem-firmware/wiki/"
bad, local, missing = [], [], {}
for f in SITE.rglob("*.html"):
    rel = str(f.relative_to(SITE))
    if rel == "404.html" or rel.startswith("search"): continue
    text = f.read_text(errors="ignore")
    for m in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', text, re.S):
        href, label = H.unescape(m.group(1)), re.sub("<[^>]+>", "", m.group(2))
        if href.startswith(WIKI):
            name = urllib.parse.unquote(href[len(WIKI):].split("#")[0])
            if "Оригінал на GitHub" in label: continue
            if norm(name) in pages: local.append((rel, name))
            else: missing.setdefault(name, []).append(rel)
            continue
        if href.startswith(("http", "mailto:", "#", "javascript:", "data:")): continue
        path = urllib.parse.unquote(href.split("#")[0].split("?")[0])
        if not path: continue
        t = (f.parent / path).resolve()
        if t.is_dir(): t = t / "index.html"
        if not t.exists(): bad.append((rel, href))
print("BROKEN internal:", len(bad)); [print("  ", b) for b in sorted(set(bad))[:80]]
print("SHOULD-BE-LOCAL:", len(local)); [print("  ", b) for b in sorted(set(local))[:80]]
print("MISSING pages:", len(missing))
for k, v in sorted(missing.items()): print(f"   {k!r} <- {sorted(set(v))[:3]}")
