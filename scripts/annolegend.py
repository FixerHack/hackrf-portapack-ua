"""Підміна скріншотів на анотовані та вставка нумерованих легенд у блоки <div class="app">."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from annot_data import A

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r'(<div class="app" markdown>.*?)(</div>\s*</div>\n)', re.S)


def process(text: str) -> str:
    def blk(m):
        body, tail = m.group(1), m.group(2)
        ids = [int(x) for x in re.findall(r"screens/(\d{3})\.jpg", body)]
        ids = [i for i in ids if i in A and (ROOT / f"assets/annotated/app-{i:03d}.jpg").exists()]
        if not ids:
            return m.group(0)
        for i in ids:
            body = body.replace(f"screens/{i:03d}.jpg", f"annotated/app-{i:03d}.jpg")
        leg = ""
        for k, i in enumerate(ids):
            head = "Елементи екрана" if len(ids) == 1 else f"Елементи екрана ({k + 1}-й знімок)"
            leg += f"\n**{head}:**\n\n"
            for n, it in enumerate(A[i], 1):
                leg += f"{n}. {it[4]}\n"
        # легенда лишається всередині правого стовпчика
        return body + leg + "\n" + tail
    return BLOCK.sub(blk, text)
