#!/usr/bin/env python3
"""Збирає docs/ з англомовної вікі Mayhem + українських перекладів з translations/.

Сторінки, для яких є переклад, беруться з translations/; решта копіюються
англійською з банером «ще не перекладено». Вікі-посилання перетворюються на
відносні посилання MkDocs.
"""
import re, shutil, sys, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from annolegend import process as legends

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "upstream/mayhem-wiki"
TR = ROOT / "translations"
DOCS = ROOT / "docs"
WIKI_URL = "https://github.com/portapack-mayhem/mayhem-firmware/wiki/"
SKIP = {"all_wiki.md", "_Sidebar.md", "_Footer.md"}

BANNER = ('!!! warning "Ще не перекладено"\n'
          '    Цю сторінку ще не перекладено українською. Нижче наведено оригінальний англійський текст. '
          'Допомогти з перекладом можна — див. [Участь у перекладі](translation-guide.md). '
          '[Оригінал на GitHub]({url}).\n\n')


def norm(name: str) -> str:
    name = urllib.parse.unquote(name).strip().replace(" ", "-")
    return re.sub(r"[-‐‑–—]+", "-", name).lower()


def slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9_]+", "-", norm(name))
    return s.strip("-") or "page"


# ім'я сторінки (нормалізоване) -> slug
pages = {}
for p in sorted(WIKI.glob("*.md")):
    if p.name in SKIP:
        continue
    pages[norm(p.stem)] = slug(p.stem)
for p in TR.glob("*.md"):
    pages.setdefault(norm(p.stem), slug(p.stem))
for p in (ROOT / "site_pages").glob("*.md"):
    pages.setdefault(norm(p.stem), p.stem)
pages.setdefault("home", "index")
pages["home"] = "index"


def target(raw: str):
    """повертає (url, ok) для вікі-посилання без розширення."""
    page, _, anchor = raw.partition("#")
    key = norm(page)
    if key in pages:
        return pages[key] + ".md" + ("#" + anchor.lower() if anchor else ""), True
    return WIKI_URL + urllib.parse.quote(page.replace(" ", "-")) + ("#" + anchor if anchor else ""), False


def fix(text: str, depth_prefix: str = "") -> str:
    # [[Page|Text]] and [[Page]]
    def wl(m):
        inner = m.group(1)
        img = inner.split("|")[0]
        if re.search(r"\.(png|jpe?g|gif|webp)$", img, re.I):
            return f"![]({img})"
        page, _, label = inner.replace("\\|", "|").partition("|")
        url, _ = target(page)
        return f"[{label or page}]({depth_prefix}{url})"
    text = re.sub(r"\[\[([^\]]+)\]\]", wl, text)

    def ml(m):
        label, href = m.group(1), m.group(2).strip()
        if href.startswith("../wiki/"):
            href = href[len("../wiki/"):]
        if href.startswith(WIKI_URL):
            href = re.sub(r"\.md(#|$)", r"\1", href)
        if href.startswith(WIKI_URL):
            url, ok = target(href[len(WIKI_URL):])
            return f"[{label}]({depth_prefix}{url})" if ok else m.group(0)
        if re.match(r"^(https?:|mailto:|#|/|img/)", href) or href.endswith((".png", ".jpg", ".gif")):
            return m.group(0)
        if href.endswith(".md") and not "/" in href:
            return m.group(0)
        if href.startswith("hackrf/"):
            pg, _, anc = href.partition("#")
            return f"[{label}]({depth_prefix}{pg}.md" + (f"#{anc}" if anc else "") + ")"
        url, ok = target(re.sub(r"\.md(#|$)", r"\1", href))
        return f"[{label}]({depth_prefix}{url})"
    # посилання у формі ](<Назва (з дужками)>)
    text = re.sub(r"(?<!!)\[([^\]]*)\]\(<([^>]+)>\)", lambda m: ml(m), text)
    text = re.sub(r"(?<!!)\[([^\]]*)\]\(([^()\s<]+(?:\([^()]*\))?[^()\s]*)\)", ml, text)
    # GitHub alert syntax -> admonitions
    def alert(m):
        kind = m.group(1).lower()
        kind = {"important": "danger", "warning": "warning", "caution": "danger", "tip": "tip", "note": "note"}.get(kind, "note")
        body = m.group(2)
        lines = [re.sub(r"^>\s?", "", l) for l in body.splitlines()]
        lines = [l for l in lines]
        return f'!!! {kind}\n' + "\n".join("    " + l for l in lines) + "\n"
    text = re.sub(r"^> \[!(\w+)\][ \t]*\n((?:>.*\n?|[^\n>].*\n)?(?:>.*\n?)*)", alert, text, flags=re.M | re.I)
    return text


def first_title(text: str, fallback: str) -> str:
    for l in text.splitlines():
        m = re.match(r"^#{1,3}\s+(.+)", l)
        if m:
            return re.sub(r"[*`]+|<[^>]+>|\[|\]|\(.*?\)", "", m.group(1)).strip() or fallback
    return fallback


def main():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    # images
    shutil.copytree(WIKI / "img", DOCS / "img")
    stats = {"translated": 0, "untranslated": 0}
    titles = {}
    translated = set()
    for key, sl in pages.items():
        tr = None
        for cand in TR.glob("*.md"):
            if norm(cand.stem) == key:
                tr = cand
        if tr:
            text = legends(fix(tr.read_text(encoding="utf-8")))
            (DOCS / f"{sl}.md").write_text(text, encoding="utf-8")
            translated.add(sl)
            stats["translated"] += 1
            titles[sl] = first_title(text, sl)
            continue
        src = next((p for p in WIKI.glob("*.md") if norm(p.stem) == key and p.name not in SKIP), None)
        if not src:
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        if text.strip().startswith("### [Moved to here") or len(text.strip()) < 3:
            text += "\n"
        text = fix(text)
        titles[sl] = src.stem.replace("-", " ")
        title = src.stem.replace("-", " ")
        banner = BANNER.format(url=WIKI_URL + urllib.parse.quote(src.stem))
        if not re.match(r"^\s*#\s", text):
            text = f"# {title}\n\n" + text
        # insert banner after the first heading
        m = re.search(r"^#\s.*\n", text, flags=re.M)
        text = text[:m.end()] + "\n" + banner + text[m.end():]
        (DOCS / f"{sl}.md").write_text(text, encoding="utf-8")
        stats["untranslated"] += 1
    # hackrf docs
    (DOCS / "hackrf").mkdir()
    for p in (TR / "hackrf").glob("*.md"):
        t = p.read_text(encoding="utf-8")
        t = re.sub(r"(?<!!)\]\(([a-z0-9_]+)(#[^)]*)?\)", lambda m: f"]({m.group(1)}.md{m.group(2) or ''})", t)
        (DOCS / "hackrf" / p.name).write_text(t, encoding="utf-8")
    imgsrc = ROOT / "upstream/hackrf-images"
    if imgsrc.exists():
        shutil.copytree(imgsrc, DOCS / "hackrf" / "images")
    # misc pages
    for p in (ROOT / "site_pages").glob("*.md"):  # extra.css копіюється нижче
        t = re.sub(r"\]\(([A-Za-z][\w-]*)\.md(#[^)]*)?\)", lambda m: f"]({m.group(1)}{m.group(2) or ''})", p.read_text(encoding="utf-8"))
        (DOCS / p.name).write_text(fix(t), encoding="utf-8")
    for d in ("screens", "annotated"):
        if (ROOT / "assets" / d).exists():
            shutil.copytree(ROOT / "assets" / d, DOCS / d, ignore=shutil.ignore_patterns("_*"))
    (DOCS / "stylesheets").mkdir()
    shutil.copy(ROOT / "site_pages" / "extra.css", DOCS / "stylesheets" / "extra.css")
    import json
    (ROOT / "scripts" / "titles.json").write_text(json.dumps({"titles": titles, "translated": sorted(translated)}, ensure_ascii=False, indent=1))
    print(stats, file=sys.stderr)


main()
