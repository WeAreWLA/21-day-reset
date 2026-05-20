#!/usr/bin/env python3
"""Extract the informational diagrams from the Fat Loss Booster and
Importance Of Water guides (the plate diagram, the water-balance scale
and the urine-colour chart). The pure-white page background is recoloured
to the WLA cream so the artwork drops cleanly onto the redesigned pages.

Run once (needs the source PDFs); the PNGs land in diagrams/.
"""

import os
import fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams")
SRC = "/root/.claude/uploads/21a6d9f7-20f3-4d32-95a9-bcfd1a5d7f9b"

CREAM = (249, 247, 244)
DPI = 300

JOBS = [
    ("bb5c49f6-SS__Fat_Loss_Booster.pdf", 3,
     fitz.Rect(44, 160, 596, 402), "booster-plate"),
    ("52190e95-SS_The_Importance_Of_Water.pdf", 2,
     fitz.Rect(54, 343, 482, 765), "water-balance"),
    ("52190e95-SS_The_Importance_Of_Water.pdf", 6,
     fitz.Rect(54, 343, 540, 560), "water-urine"),
    ("016c5f94-SS__Snack_Guide.pdf", 2,
     fitz.Rect(56, 292, 543, 654), "snack-bloodsugar"),
]


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


for fn, page_idx, clip, name in JOBS:
    doc = fitz.open(f"{SRC}/{fn}")
    pix = doc[page_idx].get_pixmap(clip=clip, dpi=DPI)
    img = recolour_and_trim(pix)
    img.save(os.path.join(OUT, f"{name}.png"))
    print(f"{name}: {img.size[0]}x{img.size[1]}  ar={img.size[0]/img.size[1]:.3f}")
