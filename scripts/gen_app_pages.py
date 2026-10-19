#!/usr/bin/env python3
"""Генерує translations/Screens-*.md зі scripts/apps_data.py (фото користувача)."""
import sys; sys.path.insert(0, "scripts")
from pathlib import Path
from apps_data import *

OUT = Path("translations")
HDR = "<!-- згенеровано scripts/gen_app_pages.py з scripts/apps_data.py — правте дані там -->\n"


def entry(i, title, wiki, desc, bullets, level="###"):
    s = f'{level} {title} {{#shot-{i:03d}}}\n\n<div class="app" markdown>\n<div class="shot" markdown>\n![{title}](screens/{i:03d}.jpg)\n</div>\n<div class="txt" markdown>\n\n{desc}\n\n'
    for b in bullets:
        s += f"- {b}\n"
    if wiki:
        s += f"\n[Докладніше на сторінці застосунку](<{wiki}>)\n"
    s += "\n</div>\n</div>\n\n"
    return s


def page(name, title, intro, groups):
    t = HDR + f"# {title}\n\n{intro}\n\n"
    for g, data in groups:
        t += f"## {g}\n\n"
        for i in sorted(data):
            a = data[i]
            t += entry(i, *a)
    (OUT / name).write_text(t, encoding="utf-8")

NOTE = ('!!! info "Скріншоти з вашого пристрою"\n    Усі знімки зроблено на HackRF One + PortaPack H2 з прошивкою Mayhem v2.4.0. '
        'Більшість застосунків показано у стані «за замовчуванням», до приймання чи передавання. '
        'Опис складено за вікі Mayhem та екранами; дрібні відмінності залежать від версії прошивки.\n\n')

page("Screens-Receivers.md", "Приймачі: огляд застосунків",
     NOTE + "У меню **Receive** — застосунки для приймання й декодування сигналів. " + G.replace("main-controls.md#pidsilennya-na-prijmannya-rx", "Main-Controls"),
     [("Меню Receive", {k: (v[0], None, "Пункти меню: " + v[1] + ".", []) for k, v in MENUS.items() if k in (2, 3)}), ("Застосунки", RX)])
page("Screens-Transmitters.md", "Передавачі: огляд застосунків",
     NOTE + '!!! danger "Передавайте відповідально"\n    Передавання радіосигналів без дозволу, глушіння, підміна GPS, підроблені сигнали лиха та аварійні оповіщення незаконні в більшості країн. Тестуйте лише на власному обладнанні, на еквіваленті навантаження або в екранованому середовищі. Див. [Призначення та законність використання](Intended-Use-and-Legality).\n\n'
     "У меню **Transmit** — застосунки для передавання. Внизу екрана передавача є стандартна панель: частота, крок, смуга, **Gain**, **Amp** і кнопка **START**.",
     [("Меню Transmit", {k: (v[0], None, "Пункти меню: " + v[1] + ".", []) for k, v in MENUS.items() if k in (4, 5)}), ("Застосунки", TX)])
oth_menus = {k: (v[0], None, "Пункти меню: " + v[1] + ".", []) for k, v in MENUS.items() if k in (6, 12, 13, 14)}
page("Screens-Other.md", "Трансівери, Recon, Capture, Replay та утиліти",
     NOTE + "Інші розділи головного меню: **Transceiver**, **Recon**, **Capture**, **Replay**, **Remote**, **Looking Glass**, **Utilities** (з меню **Debug**) і **Games**.",
     [("Меню розділів", oth_menus),
      ("Трансівери", {k: OTHER[k] for k in (86, 87)}),
      ("Recon, Capture, Replay, Remote, Looking Glass", {k: OTHER[k] for k in (7, 9, 8, 10, 11)}),
      ("Утиліти", {k: OTHER[k] for k in (88, 89, 90, 91, 92, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109)}),
      ("Debug", {k: OTHER[k] for k in (93, 94, 95)})])
print("ok")
