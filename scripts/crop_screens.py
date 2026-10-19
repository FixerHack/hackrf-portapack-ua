import sys, glob, numpy as np
from PIL import Image, ImageOps, ImageDraw
src, out = sys.argv[1], sys.argv[2]
fs = sorted(glob.glob(src + "/*.jpg"))
tiles = []
for i, f in enumerate(fs):
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    W, H = im.size
    sm = im.copy(); sm.thumbnail((600, 600))
    a = np.asarray(sm).astype(int); h, w = a.shape[:2]
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = (b > 100) & (b > r + 35) & (g > 60)
    m[int(h * 0.66):] = False          # кільце енкодера внизу
    if i == 0: m = (b > 100) & (b > r + 35); m[:, : int(w*0.35)] = False  # заставка знята інакше
    ys, xs = np.nonzero(m)
    if len(xs) < 50:
        box = (0, 0, W, H)
    else:
        x0, x1 = np.percentile(xs, [1, 99]); y0, y1 = np.percentile(ys, [1, 99])
        pad = 0.06 * max(x1 - x0, y1 - y0)
        s = W / w
        bx0, bx1 = x0 - pad, x1 + pad; by0 = y0 - pad; by1 = by0 + (bx1 - bx0) * 1.7
        box = (max(0, bx0 * s), max(0, by0 * s), min(W, bx1 * s), min(H, by1 * s))
    c = im.crop(tuple(int(v) for v in box)); c.thumbnail((900, 900))
    c.save(f"{out}/{i:03d}.jpg", quality=88)
    t = c.copy(); t.thumbnail((300, 300)); tiles.append((i, t))
per = 20
for s in range(0, len(tiles), per):
    sh = Image.new("RGB", (5 * 300, 4 * 300), "white"); d = ImageDraw.Draw(sh)
    for k, (i, t) in enumerate(tiles[s:s + per]):
        x, y = (k % 5) * 300, (k // 5) * 300
        sh.paste(t, (x, y)); d.rectangle([x, y, x + 36, y + 16], fill="black"); d.text((x + 3, y + 3), str(i), fill="yellow")
    sh.save(f"{out}/_sheet{s // per}.jpg", quality=85)
