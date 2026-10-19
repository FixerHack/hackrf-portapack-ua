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
rest = [sl for k, sl in pages.items() if k not in seen and sl != "index" and sl not in MY]

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
