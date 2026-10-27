"""Render the Nasaq Remote app icon (NR) and the in-app logo strip with Pillow."""
import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
INK, GOLD, MINT = (1, 62, 55), (255, 239, 179), (127, 200, 169)
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def icon(size=1024):
    k = 4                                  # supersample, then downscale for smooth edges
    s = size * k
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    u = s / 100                            # draw on a 100x100 grid (matches the SVG)
    pad = 6 * u                            # macOS-style margin around the rounded square
    d.rounded_rectangle([pad, pad, s - pad, s - pad], radius=20 * u, fill=INK)
    d.rounded_rectangle([18 * u, 22 * u, 82 * u, 66 * u], radius=7 * u, fill=GOLD)          # screen
    d.polygon([(43 * u, 66 * u), (57 * u, 66 * u), (60 * u, 74 * u), (40 * u, 74 * u)], fill=GOLD)  # stand
    d.rounded_rectangle([31 * u, 73 * u, 69 * u, 78 * u], radius=2.5 * u, fill=GOLD)        # base
    f = ImageFont.truetype(BOLD, int(28 * u))
    d.text((50 * u, 44.5 * u), "NR", font=f, fill=INK, anchor="mm")
    d.ellipse([71 * u, 15 * u, 87 * u, 31 * u], fill=MINT, outline=INK, width=int(2.6 * u))  # online dot
    return im.resize((size, size), Image.LANCZOS)


def logo(dark):
    """300x60 strip at 2x: Nasaq mark + 'Nasaq Remote' (the app scales it into its 300x60 box)."""
    w, h, k = 600, 120, 4
    im = Image.new("RGBA", (w * k, h * k), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    fg = GOLD if dark else INK
    sub = MINT if dark else (15, 122, 107)
    m, x0, y0 = 84 * k, 18 * k, 18 * k       # Nasaq mark: 2x2 grid, last cell a circle
    c, g, r = m * 0.44, m * 0.12, m * 0.12
    d.rounded_rectangle([x0, y0, x0 + c, y0 + c], radius=r, fill=fg)
    a = fg[:3] + (110,)
    d.rounded_rectangle([x0 + c + g, y0, x0 + 2 * c + g, y0 + c], radius=r, fill=a)
    d.rounded_rectangle([x0, y0 + c + g, x0 + c, y0 + 2 * c + g], radius=r, fill=a)
    d.ellipse([x0 + c + g, y0 + c + g, x0 + 2 * c + g, y0 + 2 * c + g], fill=fg)
    d.text((130 * k, 58 * k), "Nasaq", font=ImageFont.truetype(BOLD, 46 * k), fill=fg, anchor="lm")
    d.text((276 * k, 60 * k), "Remote", font=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 44 * k), fill=sub, anchor="lm")
    return im.resize((w, h), Image.LANCZOS)


big = icon(1024)
big.save(f"{OUT}/icon-1024.png")
for n in (16, 32, 48, 64, 128, 256, 512):
    big.resize((n, n), Image.LANCZOS).save(f"{OUT}/icon-{n}.png")
big.save(f"{OUT}/app_icon.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
logo(False).save(f"{OUT}/logo_light.png")
logo(True).save(f"{OUT}/logo_dark.png")
print("ok")
