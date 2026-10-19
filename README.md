# HackRF + PortaPack Mayhem — українська документація

Неофіційний український переклад вікі [Mayhem](https://github.com/portapack-mayhem/mayhem-firmware/wiki) та документації [HackRF](https://hackrf.readthedocs.io), опублікований на GitHub Pages (MkDocs Material).

- `translations/` — українські переклади (ім'я файлу = ім'я сторінки вікі; `translations/hackrf/` — документація HackRF).
- `upstream/` — англомовні оригінали (для сторінок, що ще не перекладені).
- `scripts/build_docs.py` — збирає `docs/`; `scripts/gen_mkdocs.py` — генерує навігацію `mkdocs.yml`.
- `site_pages/` — додаткові сторінки сайту.

Локальна збірка:

```bash
pip install "mkdocs<2" mkdocs-material
python scripts/build_docs.py && python scripts/gen_mkdocs.py && mkdocs serve
```

Як допомогти з перекладом — див. [Участь у перекладі](site_pages/translation-guide.md). Оригінальні тексти належать авторам проєктів Mayhem та HackRF (GPL-2.0).
