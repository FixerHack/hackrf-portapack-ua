#!/usr/bin/env python3
"""Генерує mkdocs.yml (з навігацією за _Sidebar.md вікі). Запускати після build_docs.py."""
import re, json, importlib.util, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("bd", ROOT / "scripts/build_docs.py")
# reuse helpers without re-running main: read source and exec only helper defs
src = (ROOT / "scripts/build_docs.py").read_text().replace("\nmain()\n", "\n")
ns = {"__file__": str(ROOT / "scripts/build_docs.py")}
exec(compile(src, "bd", "exec"), ns)
norm, pages = ns["norm"], ns["pages"]
data = json.loads((ROOT / "scripts/titles.json").read_text())
titles, translated = data["titles"], set(data["translated"])

UK = {
 "Start here": "Початок", "Contributors": "Учасники", "Hardware": "Апаратна частина",
 "User manual": "Посібник користувача", "User interface": "Інтерфейс користувача",
 "Troubleshooting": "Усунення несправностей", "Applications": "Застосунки",
 "Receivers": "Приймачі", "Transmitters": "Передавачі", "Utilities": "Утиліти",
 "Games": "Ігри", "Settings": "Налаштування", "Misc": "Різне",
 "Developer Manual": "Посібник розробника", "Compilation of the firmware": "Збирання прошивки",
 "Description of the Structure": "Опис структури", "Software Dev Guides": "Посібники з розробки",
 "Tools": "Інструменти", "Debug Menu": "Меню Debug",
}
sidebar = (ROOT / "upstream/mayhem-wiki/_Sidebar.md").read_text()
groups, order, seen, labels = {}, [], set(), {}
cur = "Початок"
def label_txt(t): return re.sub(r"\*+|<[^>]+>", "", t).strip()
def add(g, key, label):
    if key in seen or key not in pages: return
    seen.add(key)
    labels[pages[key]] = label_txt(label)
    groups.setdefault(g, []).append(pages[key])
    if g not in order: order.append(g)
for line in sidebar.splitlines():
    m = re.match(r"^###\s*(?:<u>)?\s*(?:\[([^\]]+)\]\(([^)]+)\)|([^<\n]+))", line)
    s = re.search(r"<summary>(.*?)</summary>", line)
    if m:
        name = (m.group(1) or m.group(3) or "").strip()
        if not name.startswith("Intended"): cur = UK.get(name, name)
        if m.group(2): add(cur, norm(m.group(2).split('#')[0]), name)
        continue
    if s:
        txt = re.sub(r"<[^>]+>|&nbsp;|↳|[^\w\s/+&.()'-]", "", s.group(1)).strip()
        cur = UK.get(txt, txt)
        h = re.search(r'href="([^"]+)"', s.group(1))
        if h: add(cur, norm(h.group(1).split('#')[0]), txt)
        continue
    for lm in re.finditer(r"\[([^\]]+)\]\(([^)]+(?:\([^)]*\))?[^)]*)\)", line):
        href = lm.group(2)
        if href.startswith("http") or "#" in href: continue
        add(cur, norm(href), lm.group(1))
# leftover pages
MY = ["my-device", "ui-guide", "screens-receivers", "screens-transmitters", "screens-other"]
rest = [sl for k, sl in pages.items() if k not in seen and sl != "index" and sl not in MY and not (ROOT / "site_pages" / f"{sl}.md").exists()]

def label(sl):
    t = titles.get(sl, sl) if sl in translated else labels.get(sl, titles.get(sl, sl))
    return t if len(t) < 60 else t[:57] + "…"

def q(s): return '"' + s.replace('"', "'") + '"'
nav = ["  - Головна: index.md", "  - Документація HackRF:"]
for p in sorted((ROOT / "translations/hackrf").glob("*.md"), key=lambda p: (p.name != "index.md", p.name)):
    t = re.sub(r"^#\s*", "", p.read_text().splitlines()[0])
    nav.append(f"      - \"{t}\": hackrf/{p.name}")
nav.append("  - \"Ваш пристрій і екрани\":")
for sl in MY:
    nav.append(f"      - {q(titles.get(sl, sl))}: {sl}.md")
nav.append("  - Участь у перекладі: translation-guide.md")
def _q(s): return '"' + s.replace('"', "'") + '"'
for g in order:
    items = [sl for sl in groups[g] if sl != "index"]
    if not items: continue
    nav.append(f"  - {q(g)}:")
    for sl in items:
        mark = "" if sl in translated else " (EN)"
        nav.append(f"      - {q(label(sl) + mark)}: {sl}.md")
if rest:
    nav.append("  - \"Інші сторінки (EN)\":")
    for sl in sorted(rest):
        nav.append(f"      - {q(label(sl))}: {sl}.md")

# ---- шкала локалізації ----
WIKI = ROOT / "upstream/mayhem-wiki"
def size_of(sl):
    for k, v in pages.items():
        if v == sl:
            f = next((p for p in WIKI.glob("*.md") if norm(p.stem) == k), None)
            return f.stat().st_size if f else 0
    return 0
def stat(slugs):
    src = [x for x in slugs if size_of(x) > 400]
    tot = sum(size_of(x) for x in src); done = sum(size_of(x) for x in src if x in translated)
    return len(src), sum(1 for x in src if x in translated), tot, done
def bar(pct):
    return f'<div class="pbar"><div class="pfill" style="width:{pct:.1f}%"></div><span>{pct:.0f}%</span></div>'
rows = []
all_src = [sl for k, sl in pages.items() if size_of(sl) > 400 and sl not in MY]
n, nd, tot, done = stat(all_src)
hk_total = sum(f.stat().st_size for f in (ROOT / "upstream/hackrf-sources").glob("*.txt")) if (ROOT / "upstream/hackrf-sources").exists() else 0
hk_done = sum((ROOT / "upstream/hackrf-sources" / (p.stem + ".rst.txt")).stat().st_size for p in (ROOT / "translations/hackrf").glob("*.md") if (ROOT / "upstream/hackrf-sources" / (p.stem + ".rst.txt")).exists())
for g in order:
    sl = [x for x in groups[g] if x != "index"]
    a, b, t, d = stat(sl)
    if a: rows.append((g, b, a, 100 * d / t if t else 0))
rows.sort(key=lambda r: -r[3])
pct_all = 100 * done / tot if tot else 0
pg = ["# Прогрес локалізації", "",
      "Шкала показує частку **вже перекладеного тексту** (за обсягом оригіналу в символах), а не кількість сторінок. Оновлюється автоматично під час збирання сайту.", "",
      "## Усього", "",
      f"**Вікі Mayhem:** перекладено {nd} із {n} сторінок ({pct_all:.0f}% за обсягом)", "", bar(pct_all), ""]
if hk_total:
    hp = 100 * hk_done / hk_total
    pg += [f"**Документація HackRF:** перекладено {sum(1 for p in (ROOT / 'translations/hackrf').glob('*.md') if p.stem != 'index')} із {len(list((ROOT / 'upstream/hackrf-sources').glob('*.txt'))) - 1} сторінок ({hp:.0f}% за обсягом)", "", bar(hp), ""]
pg += ["## За розділами", "", "| Розділ | Сторінок | Прогрес |", "|---|---|---|"]
for g, b, a, p_ in rows:
    pg.append(f"| {g} | {b} / {a} | {bar(p_)} |")
pg += ["", "## Як допомогти", "", "Дивіться [Участь у перекладі](translation-guide.md) і пишіть, яких сторінок вам не вистачає."]
(ROOT / "docs/progress.md").write_text("\n".join(pg) + "\n")
idx = (ROOT / "docs/index.md").read_text().replace("<!--progress-->", f"**Локалізація:** {pct_all:.0f}% вікі Mayhem перекладено — [докладніше](progress.md).\n\n" + bar(pct_all))
(ROOT / "docs/index.md").write_text(idx)
nav.insert(1, "  - Прогрес локалізації: progress.md")
nav.insert(1, "  - \"📋 Завдання для вас\": tasks.md")

yml = f"""site_name: HackRF + PortaPack Mayhem — українська документація
site_description: Неофіційний український переклад документації HackRF та PortaPack Mayhem
site_url: https://REPLACE_USER.github.io/REPLACE_REPO/
repo_url: https://github.com/REPLACE_USER/REPLACE_REPO
docs_dir: docs
use_directory_urls: true
theme:
  name: material
  language: uk
  features:
    - navigation.sections
    - navigation.top
    - search.highlight
    - content.code.copy
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle: {{icon: material/weather-night, name: Темна тема}}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle: {{icon: material/weather-sunny, name: Світла тема}}
extra_css:
  - stylesheets/extra.css
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
      slugify: !!python/object/apply:pymdownx.slugs.slugify {{kwds: {{case: lower}}}}
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
plugins:
  - search
validation:
  absolute_links: ignore
  unrecognized_links: ignore
  anchors: ignore
nav:
""" + "\n".join(nav) + "\n"
(ROOT / "mkdocs.yml").write_text(yml)
print(len(order), "groups,", len(rest), "leftover", file=sys.stderr)
