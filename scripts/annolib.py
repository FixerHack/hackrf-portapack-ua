"""Малювання анотацій: пронумеровані рамки/стрілки на фото."""
import math
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
RED = (235, 40, 40)
COLORS = [(235, 40, 40), (255, 160, 0), (0, 170, 90), (170, 60, 220), (0, 140, 230), (230, 60, 150)]


def _font(sz):
    return ImageFont.truetype(FONT, sz)


def badge(d, xy, n, r, color):
    x, y = xy
    d.ellipse([x - r, y - r, x + r, y + r], fill=color, outline="white", width=max(2, r // 7))
    f = _font(int(r * 1.25))
    d.text((x, y), str(n), fill="white", font=f, anchor="mm")


def arrow(d, a, b, color, w):
    d.line([a, b], fill=color, width=w)
    ang = math.atan2(b[1] - a[1], b[0] - a[0]); L = w * 5
    for s in (-0.45, 0.45):
        p = (b[0] - L * math.cos(ang + s), b[1] - L * math.sin(ang + s))
        d.line([b, p], fill=color, width=w)


def annotate(src, out, items, scale=None):
    """items: dict(n, box=(x0,y0,x1,y1), tag=(x,y) [де номер]). Координати — у пікселях src."""
    im = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    W = im.width
    r = max(14, W // 55); w = max(3, W // 300)
    for it in items:
        n = it["n"]; col = COLORS[(n - 1) % len(COLORS)]
        x0, y0, x1, y1 = it["box"]
        d.rectangle([x0, y0, x1, y1], outline=col, width=w)
        d.rectangle([x0, y0, x1, y1], fill=col + (38,))
        tag = it.get("tag") or (x0 - r, y0 - r)
        # стрілка від значка до рамки, якщо значок далеко
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if math.hypot(tag[0] - cx, tag[1] - cy) > r * 2.2 + min(x1 - x0, y1 - y0) / 2:
            ang = math.atan2(cy - tag[1], cx - tag[0])
            start = (tag[0] + r * math.cos(ang), tag[1] + r * math.sin(ang))
            # кінець на межі рамки
            end = (cx - (x1 - x0) / 2 * 0.0, cy)
            end = _edge(box=(x0, y0, x1, y1), frm=tag)
            arrow(d, start, end, col, w)
        badge(d, tag, n, r, col)
    im.save(out, quality=90)


def _edge(box, frm):
    x0, y0, x1, y1 = box
    px = min(max(frm[0], x0), x1); py = min(max(frm[1], y0), y1)
    return (px, py)
