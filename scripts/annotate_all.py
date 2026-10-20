"""Малює анотації з scripts/annot_data.py: рамки + стрілки з номерами на полях."""
import sys, math; sys.path.insert(0, "scripts")
from PIL import Image, ImageDraw
from annolib import COLORS, badge, arrow
from annot_data import A

# ці номери розмічено в координатах «листа» (три екрани поспіль із проміжком 10 px)
SHEET = {86, 87, 89, 90, 92, 93, 95, 96} | {i for i in range(97, 131) if i % 3 != 1}
def tile_off(i):
    g = (i - 1) // 3 * 3 + 1
    return sum(Image.open(f"assets/screens/{k:03d}.jpg").size[0] + 10 for k in range(g, i))
OFF = {i: tile_off(i) for i in SHEET}
M = 80  # поле для значків


def render(i, items):
    off = OFF.get(i, 0)
    im = Image.open(f"assets/screens/{i:03d}.jpg").convert("RGB")
    W, H = im.size
    VM = 10  # вертикальне поле, щоб значки не «вилітали» за край
    canvas = Image.new("RGB", (W + 2 * M, H + 2 * VM), (20, 20, 24))
    canvas.paste(im, (M, VM))
    d = ImageDraw.Draw(canvas, "RGBA")
    r = 17
    items2 = []
    for n, (x0, y0, x1, y1, _t) in enumerate(items, 1):
        x0 -= off; x1 -= off
        x0, x1 = max(0, x0), min(W, x1); y0, y1 = max(0, y0), min(H, y1)
        items2.append((n, x0 + M, y0 + VM, x1 + M, y1 + VM))
    for n, x0, y0, x1, y1 in items2:
        col = COLORS[(n - 1) % len(COLORS)]
        d.rectangle([x0, y0, x1, y1], fill=col + (42,), outline=col, width=3)
    # розкладка значків по колонках зліва/справа; розводимо так, щоб жоден не вийшов за полотно
    CH = H + 2 * VM
    step = 2 * r + 6
    lo_b, hi_b = r + 2, CH - r - 2
    for side in ("L", "R"):
        sel = [(n, x0, y0, x1, y1) for n, x0, y0, x1, y1 in items2
               if ((x0 + x1) / 2 < W / 2 + M) == (side == "L")]
        sel.sort(key=lambda t: (t[2] + t[4]) / 2)
        # бажана позиція — центр елемента; розводимо вниз із мінімальним кроком
        ys = []
        for _, x0, y0, x1, y1 in sel:
            y = (y0 + y1) / 2
            if ys:
                y = max(y, ys[-1] + step)
            ys.append(y)
        # зсунути вгору, якщо нижній значок вийшов за полотно
        if ys and ys[-1] > hi_b:
            shift = ys[-1] - hi_b
            ys = [y - shift for y in ys]
        # якщо все одно не влазить згори — рівномірно стиснути
        if ys and ys[0] < lo_b:
            if len(ys) > 1 and ys[-1] - ys[0] > 0:
                span = hi_b - lo_b
                ys = [lo_b + span * k / (len(ys) - 1) for k in range(len(ys))]
            else:
                ys = [max(lo_b, min(hi_b, y)) for y in ys]
        for k, (n, x0, y0, x1, y1) in enumerate(sel):
            col = COLORS[(n - 1) % len(COLORS)]
            y = ys[k]
            bx = M / 2 if side == "L" else W + M + M / 2
            ex = x0 if side == "L" else x1
            ey = min(max(y, y0), y1)
            sx = bx + r if side == "L" else bx - r
            arrow(d, (sx, y), (ex, ey), col, 3)
            badge(d, (bx, y), n, r, col)
    return canvas

for i, items in sorted(A.items()):
    render(i, items).save(f"assets/annotated/app-{i:03d}.jpg", quality=86)
print(len(A))
