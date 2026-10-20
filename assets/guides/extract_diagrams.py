#!/usr/bin/env python3
"""Extract the plate diagrams from the original Canva PDFs.

The diagrams are pure vector art (pie chart, food line-icons, fork,
connector lines and bold captions). We locate the pie, render the
diagram band at high resolution and recolour the pure-white page
background to the WLA cream so the artwork drops cleanly onto the
redesigned cream pages.

Run once (needs the source PDFs); the resulting PNGs live in diagrams/.
"""

import os
import fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams")
os.makedirs(OUT, exist_ok=True)

SRC = "/root/.claude/uploads/21a6d9f7-20f3-4d32-95a9-bcfd1a5d7f9b"
PDFS = {
    "low": f"{SRC}/bbe24114-SS__How_to_build_a_low_carb_meal.pdf",
    "medium": f"{SRC}/a8a11d08-_SS__How_to_build_a__medium_carb_meal.pdf",
    "high": f"{SRC}/46754fb6-_SS__How_to_build_a__high_carb_meal.pdf",
}

# guide -> list of (page_index, output_name)
DIAGRAMS = {
    "low":    [(1, "low-plate")],
    "medium": [(1, "medium-plate"), (2, "medium-legume-plate")],
    "high":   [(2, "high-plate"), (3, "high-legume-plate"),
               (4, "high-legume-only-plate")],
}

CREAM = (249, 247, 244)
DPI = 260


def pie_cluster(page):
    """Bounding box of the filled pie wedges."""
    box = None
    for d in page.get_drawings():
        r = d.get("rect")
        if not r or not d.get("fill"):
            continue
        if r.width > 560 and r.height > 780:        # page background
            continue
        area = r.width * r.height
        if 1500 < area < 120000 and r.width < 420 and r.height < 420:
            box = r if box is None else box | r
    return box


def recolour_and_trim(pix):
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if r >= 250 and g >= 250 and b >= 250:
                px[x, y] = CREAM
    bbox = None
    for y in range(h):
        for x in range(w):
            if px[x, y] != CREAM:
                bbox = [x, y, x, y] if bbox is None else [
                    min(bbox[0], x), min(bbox[1], y),
                    max(bbox[2], x), max(bbox[3], y)]
    if bbox:
        m = 12
        img = img.crop((max(0, bbox[0] - m), max(0, bbox[1] - m),
                        min(w, bbox[2] + m + 1), min(h, bbox[3] + m + 1)))
    return img


for guide, items in DIAGRAMS.items():
    doc = fitz.open(PDFS[guide])
    for page_idx, name in items:
        page = doc[page_idx]
        pie = pie_cluster(page)
        clip = fitz.Rect(44, pie.y0 - 26, 596, pie.y1 + 22)
        pix = page.get_pixmap(clip=clip, dpi=DPI)
        img = recolour_and_trim(pix)
        path = os.path.join(OUT, f"{name}.png")
        img.save(path)
        print(f"{name}: {img.size[0]}x{img.size[1]}  ar={img.size[0]/img.size[1]:.3f}")
