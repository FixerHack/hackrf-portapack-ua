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
    canvas = Image.new("RGB", (W + 2 * M, H), (20, 20, 24))
    canvas.paste(im, (M, 0))
    d = ImageDraw.Draw(canvas, "RGBA")
    r = 17
    placed = {"L": [], "R": []}
    items2 = []
    for n, (x0, y0, x1, y1, _t) in enumerate(items, 1):
        x0 -= off; x1 -= off
        x0, x1 = max(0, x0), min(W, x1); y0, y1 = max(0, y0), min(H, y1)
        items2.append((n, x0 + M, y0, x1 + M, y1))
    for n, x0, y0, x1, y1 in items2:
        col = COLORS[(n - 1) % len(COLORS)]
        d.rectangle([x0, y0, x1, y1], fill=col + (42,), outline=col, width=3)
    for n, x0, y0, x1, y1 in items2:
        col = COLORS[(n - 1) % len(COLORS)]
        cy = (y0 + y1) / 2; cx = (x0 + x1) / 2
        side = "L" if cx < W / 2 + M else "R"
        y = cy
        for py in sorted(placed[side]):
            if abs(py - y) < 2 * r + 4: y = py + 2 * r + 4
        placed[side].append(y)
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
