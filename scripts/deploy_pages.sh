#!/usr/bin/env bash
# Збирає сайт локально й публікує у гілку gh-pages (GitHub Actions не потрібні).
set -euo pipefail
cd "$(dirname "$0")/.."
OWNER="${1:-FixerHack}"; REPO="${2:-hackrf-portapack-ua}"
.venv/bin/python scripts/gen_app_pages.py
.venv/bin/python scripts/build_docs.py
.venv/bin/python scripts/gen_mkdocs.py
sed "s#REPLACE_USER#$OWNER#g; s#REPLACE_REPO#$REPO#g" mkdocs.yml > mkdocs.final.yml
.venv/bin/mkdocs build -q -f mkdocs.final.yml -d /tmp/site_final
.venv/bin/python scripts/check_links.py /tmp/site_final | head -8
rm mkdocs.final.yml
touch /tmp/site_final/.nojekyll
rm -rf /tmp/ghp && mkdir /tmp/ghp && cp -R /tmp/site_final/. /tmp/ghp/
cd /tmp/ghp && git init -q -b gh-pages && git add -A && git commit -q -m "Deploy site"
git remote add origin "https://github.com/$OWNER/$REPO.git" && git push -q -f origin gh-pages
