"""Render the Nasaq Remote launcher icon (remote.svg) into Microsoft Store logo sizes."""
import os, sys
from PIL import Image, ImageDraw

OUT = sys.argv[1]


def grad(size, c0, c1, diagonal):
    g = Image.new("RGB", (size, size))
    px = g.load()
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * size - 2) if diagonal else y / (size - 1)
            px[x, y] = tuple(round(a + (b - a) * t) for a, b in zip(c0, c1))
    return g


def icon(n):
    k = 2
    s = n * k
    u = s / 100
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, s - 1, s - 1], fill=255)
    im.paste(grad(s, (0x2a, 0x9f, 0xc4), (0x0b, 0x4a, 0x63), True), (0, 0), mask)
    # screen with its vertical gold gradient
    sc = grad(s, (0xff, 0xf6, 0xd6), (0xf1, 0xcf, 0x73), False)
    m = Image.new("L", (s, s), 0)
    ImageDraw.Draw(m).rounded_rectangle([21 * u, 30 * u, 79 * u, 68 * u], radius=6 * u, fill=255)
    im.paste(sc, (0, 0), m)
    ov = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    ink = (0x0b, 0x4a, 0x63)
    d.rounded_rectangle([27 * u, 36 * u, 47 * u, 48 * u], radius=3 * u, fill=ink + (64,))
    d.rounded_rectangle([27 * u, 53 * u, 57 * u, 57 * u], radius=2 * u, fill=ink + (77,))
    im.alpha_composite(ov)
    d = ImageDraw.Draw(im)
    cream = (0xff, 0xf6, 0xd6, 255)
    d.polygon([(44 * u, 68 * u), (56 * u, 68 * u), (59 * u, 76 * u), (41 * u, 76 * u)], fill=cream)
    d.rounded_rectangle([36 * u, 75 * u, 64 * u, 79 * u], radius=2 * u, fill=cream)
    cursor = [(56, 41), (56, 59), (61, 54.5), (64.6, 62.1), (68, 60.5), (64.5, 53.1), (71.1, 53.1)]
    pts = [(x * u, y * u) for x, y in cursor]
    d.line(pts + [pts[0]], fill=cream, width=max(1, round(3.2 * u)), joint="curve")
    d.polygon(pts, fill=ink + (255,))
    mint = (0x7f, 0xe0, 0xc0, 255)
    w = max(1, round(3.2 * u))
    d.arc([62 * u, 22 * u, 78 * u, 38 * u], 270, 360, fill=mint, width=w)
    d.arc([54 * u, 14 * u, 86 * u, 46 * u], 270, 360, fill=mint, width=w)
    d.ellipse([66.6 * u, 26.6 * u, 73.4 * u, 33.4 * u], fill=mint)
    return im.resize((n, n), Image.LANCZOS)


def on_brand(w, h, frac):
    bg = Image.new("RGBA", (w, h), (0x01, 0x3e, 0x37, 255))
    n = round(min(w, h) * frac)
    bg.alpha_composite(icon(n), ((w - n) // 2, (h - n) // 2))
    return bg.convert("RGB")


os.makedirs(OUT, exist_ok=True)
on_brand(1440, 2160, 0.62).save(f"{OUT}/poster-1440x2160.png", optimize=True)
on_brand(2160, 2160, 0.62).save(f"{OUT}/box-2160x2160.png", optimize=True)
for n in (300, 150, 71):
    icon(n).save(f"{OUT}/tile-{n}.png", optimize=True)
print("ok")
