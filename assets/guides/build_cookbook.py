#!/usr/bin/env python3
"""The WLA Weight Loss Cookbook — WLA house style.

Builds The-WLA-Weight-Loss-Cookbook.pdf from cookbook_recipes_data.py.
Each recipe sits on one page with a hero photo across the top and a
two-column ingredients / method block below.
"""
import os
import fitz

from wla_style import (Guide, PAGE_W, PAGE_H, LEFT, RIGHT, CW, MARGIN,
                       CONTENT_TOP, CONTENT_BOTTOM,
                       NAVY, BLUSH, INK, BEIGE, CREAM, RULE,
                       wrap, tw, fit_size, norm)
from cookbook_recipes_data import RECIPES, SECTIONS, NAME, TAGLINE

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "cookbook-recipes")
OUT = os.path.join(HERE, "..", "The-WLA-Weight-Loss-Cookbook.pdf")

PHOTO_H = 232  # hero photo height in points

g = Guide(OUT)


def section_kicker(n):
    """Map section name to the kicker label used at top of recipe pages."""
    return SECTIONS[n].upper()


def section_index_of(title):
    for r in RECIPES:
        if r["title"] == title:
            return SECTIONS.index(r["section"])
    return 0


# =========================================================== cover
page = g._blank_page()
g.page = page

# top kicker
kx = g.tracked(LEFT, 60, "A FREE GUIDE", "asb", 9, NAVY, 1.6)
g.text(kx + 11, 60, "·", "asb", 9, BLUSH)
g.tracked(kx + 22, 60, "THE WEIGHT LOSS ACADEMY", "asb", 9, NAVY, 1.6)

# title block
title_lines = [
    ("The WLA", "lb", NAVY),
    ("Weight Loss", "lbi", BLUSH),
    ("Cookbook.", "lb", NAVY),
]
target = 408
T = min(fit_size(t[0], t[1], target) for t in title_lines)
T = min(T, 78)
LH = T * 1.18
b1 = 286
for i, (txt, font, color) in enumerate(title_lines):
    g.text(LEFT, b1 + i * LH, txt, font, T, color)

# subtitle / tagline
sy = b1 + (len(title_lines) - 1) * LH + 56
for ln in wrap(TAGLINE, "lbi", 13, 360):
    g.text(LEFT, sy, ln, "lbi", 13, NAVY)
    sy += 20.5

# small "WEIGHT LOSS ACADEMY" mark near bottom
g.tracked(LEFT, PAGE_H - 70, "WEIGHT LOSS ACADEMY", "asb", 9, NAVY, 1.8)


# =========================================================== inside-title spread
g._new_content_page()
g.gap(60)
g.heading([[("Cook simply.", True)],
           [("Eat well.", False)]])
g.paragraph(
    "If you've ever stared into the fridge at 6pm wondering what on "
    "earth you're going to feed everyone, this book is for you.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "The reason most healthy eating plans fall apart isn't willpower. "
    "It's tired Tuesdays. It's coming home shattered, opening the "
    "freezer, finding nothing, and ordering a takeaway.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "These 15 recipes are designed to take the thinking out of it. "
    "They're built around protein, fibre and flavour — so you stay "
    "full, hit your macros, and lose weight without feeling like "
    "you're missing out. Some are slow-cooker dump-and-go meals. "
    "Some are quick weekday bowls. All of them are family-friendly, "
    "nutritionist-approved, and built for real life.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "No fuss. No restriction. Just food that works.",
    size=12.5, lh=17.5, font="lbi", color=BLUSH, gap_after=14)


# =========================================================== contents
g._new_content_page()
g.heading([[("What's ", False), ("Inside.", True)]])
g.paragraph(
    f"{len(RECIPES)} fuss-free, macro-balanced recipes — split into "
    f"four sections so you can flick straight to what you fancy.",
    size=11.5, lh=15.6, gap_after=18)


def toc_section(name, recipes, start_page):
    """Render a contents section. start_page is the first page number
    of that section. Returns the next start_page."""
    g.ensure(28)
    g.tracked(LEFT, g.y + 11, name.upper(), "asb", 9.5, BLUSH, 1.6)
    g.y += 26
    pg = start_page
    for i, r in enumerate(recipes, 1):
        g.ensure(20)
        y = g.y + 12
        num = f"{i:02d}"
        # leading number in coral
        g.text(LEFT + 4, y, num, "asb", 10.4, BLUSH)
        # title
        g.text(LEFT + 32, y, r["title"], "as", 10.8, INK)
        # dotted leader
        x = LEFT + 32 + tw(r["title"], "as", 10.8) + 10
        pgs = f"{pg:02d}"
        while x < RIGHT - tw(pgs, "as", 10.8) - 10:
            g.page.draw_circle((x, y - 3), 0.6, color=None,
                               fill=(0.6, 0.6, 0.6))
            x += 3.3
        g.text_right(RIGHT - 2, y, pgs, "as", 10.8, INK)
        g.y += 19
        pg += 1
    g.y += 12
    return pg


# Recipes start on page 5 (cover=1, inside title=2, contents=3, plus 1
# extra page slot for the section dividers? — we don't use dividers).
# But we have one page per recipe.
# Pages: 1 cover, 2 inside title, 3 contents, 4..N recipes, N+1 closing.
section_groups = []
for s in SECTIONS:
    group = [r for r in RECIPES if r["section"] == s]
    section_groups.append((s, group))

start_pg = 4
for name, group in section_groups:
    start_pg = toc_section(name, group, start_pg)


# =========================================================== recipe pages
def draw_hero(image_path):
    """Full-width photo across the top of the page (cover-cropped)."""
    if not os.path.exists(image_path):
        g.page.draw_rect(fitz.Rect(0, 0, PAGE_W, PHOTO_H),
                         color=None, fill=(0.95, 0.92, 0.88))
        g.text_center(PAGE_W / 2, PHOTO_H / 2 + 4, "[ photo ]",
                      "lbi", 12, (0.55, 0.55, 0.55))
        return
    from PIL import Image
    import io
    im = Image.open(image_path).convert("RGB")
    iw, ih = im.size
    target_ar = PAGE_W / PHOTO_H
    ar = iw / ih
    if ar > target_ar:
        crop_h = ih
        crop_w = int(ih * target_ar)
        x0 = (iw - crop_w) // 2
        im = im.crop((x0, 0, x0 + crop_w, ih))
    else:
        crop_w = iw
        crop_h = int(iw / target_ar)
        y0 = (ih - crop_h) // 2
        im = im.crop((0, y0, iw, y0 + crop_h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=88)
    rect = fitz.Rect(0, 0, PAGE_W, PHOTO_H)
    g.page.insert_image(rect, stream=buf.getvalue())


def draw_recipe(idx, r):
    """One recipe per page."""
    section = r["section"]
    sec_n = SECTIONS.index(section)
    # number recipes by their position in the overall list
    rnum = idx + 1

    page = g._blank_page()
    g.page = page

    # hero photo
    img_path = os.path.join(IMG_DIR, r["image"])
    draw_hero(img_path)

    # vertical cursor below photo
    g.y = PHOTO_H + 28

    # kicker: RECIPE 02 · SLOW COOKER
    kicker = f"RECIPE {rnum:02d}"
    kx = g.tracked(LEFT, g.y, kicker, "asb", 8.5, NAVY, 1.5)
    g.text(kx + 10, g.y, "·", "asb", 8.5, BLUSH)
    g.tracked(kx + 20, g.y, section.upper(), "asb", 8.5, NAVY, 1.5)
    g.y += 16

    # title (Libre Baskerville italic for emphasis)
    title = r["title"]
    title_size = 26 if len(title) < 30 else (22 if len(title) < 42 else 19)
    title_lines = wrap(title, "lbi", title_size, CW)
    for tl in title_lines:
        g.text(LEFT, g.y + title_size * 0.80, tl, "lbi", title_size, NAVY)
        g.y += title_size * 1.05
    g.y += 4

    # tagline
    if r.get("tagline"):
        for ln in wrap(r["tagline"], "lbi", 11.5, CW):
            g.text(LEFT, g.y + 10, ln, "lbi", 11.5, BLUSH)
            g.y += 15
    g.y += 8

    # serves / time row
    serves = str(r["serves"])
    time_s = r.get("time", "")
    g.tracked(LEFT, g.y + 9, "SERVES", "asb", 8.5, BLUSH, 1.4)
    g.text(LEFT, g.y + 28, serves, "lb", 13, NAVY)
    if time_s:
        col2 = LEFT + 120
        g.tracked(col2, g.y + 9, "TIME", "asb", 8.5, BLUSH, 1.4)
        g.text(col2, g.y + 28, time_s, "lb", 13, NAVY)
    g.y += 42

    # divider rule
    g.page.draw_line((LEFT, g.y), (RIGHT, g.y), color=RULE, width=0.7)
    g.y += 14

    # two-column ingredients / method — size scales to content density
    col_gap = 22
    lw = (CW - col_gap) * 0.42
    rw = (CW - col_gap) * 0.58
    rx = LEFT + lw + col_gap
    coltop = g.y

    # estimate content density and pick font sizes
    def count_items():
        n = 0
        for sub in (r.get("ingredients_sub") or []):
            n += len(sub[1])
        n += len(r.get("ingredients") or [])
        n += len(r.get("to_serve") or [])
        return n
    ing_count = count_items()
    meth_count = len(r["instructions"])
    is_dense = ing_count > 18 or meth_count > 10

    size = 9.2 if is_dense else 9.5
    lh = 12.1 if is_dense else 12.6
    item_gap = 2.0 if is_dense else 2.5
    tip_size = 9.0 if is_dense else 9.5
    tip_lh = 12.0 if is_dense else 12.5

    g.text(LEFT, coltop + 9, "INGREDIENTS", "asb", 9, NAVY)
    yL = coltop + 24

    def render_ing_list(items, x0, w, y):
        for it in items:
            lines = wrap(it, "as", size, w - 14)
            for i, ln in enumerate(lines):
                if i == 0:
                    g.text(x0, y + 8, "—", "as", size, BLUSH)
                g.text(x0 + 12, y + 8, ln, "as", size, INK)
                y += lh
            y += item_gap
        return y

    # Render order: main ingredients first, then sub-sections, then to_serve
    if r.get("ingredients"):
        yL = render_ing_list(r["ingredients"], LEFT, lw, yL)
    if r.get("ingredients_sub"):
        for sub_head, sub_items in r["ingredients_sub"]:
            yL += 3
            g.text(LEFT, yL + 9, sub_head, "asi", 9.3, NAVY)
            yL += 17
            yL = render_ing_list(sub_items, LEFT, lw, yL)
    if r.get("to_serve"):
        yL += 3
        g.text(LEFT, yL + 9, "To serve", "asi", 9.3, NAVY)
        yL += 17
        yL = render_ing_list(r["to_serve"], LEFT, lw, yL)

    # RIGHT: method
    g.text(rx, coltop + 9, "METHOD", "asb", 9, NAVY)
    yR = coltop + 24
    for k, step in enumerate(r["instructions"], 1):
        num = f"{k:02d}"
        g.text(rx, yR + 8, num, "asb", size, BLUSH)
        for ln in wrap(step, "as", size, rw - 22):
            g.text(rx + 22, yR + 8, ln, "as", size, INK)
            yR += lh
        yR += item_gap

    # WLA Tip (under whichever column ended higher)
    end_y = max(yL, yR)
    if r.get("note"):
        end_y += 12
        g.tracked(LEFT, end_y + 9, "WLA TIP", "asb", 8.5, BLUSH, 1.5)
        end_y += 20
        for ln in wrap(r["note"], "asi", tip_size, CW):
            g.text(LEFT, end_y + 8, ln, "asi", tip_size, INK)
            end_y += tip_lh

    g.y = end_y + 10


# render each recipe page in order
ordered = []
for s in SECTIONS:
    ordered.extend([r for r in RECIPES if r["section"] == s])

for idx, r in enumerate(ordered):
    draw_recipe(idx, r)


# =========================================================== closing page
g._new_content_page()
g.gap(60)
g.heading([[("Easy meals.", False)],
           [("Easier life.", True)]])
g.paragraph(
    "Eating well isn't about willpower — it's about making the "
    "healthy choice the easy one. The right recipes, prepped ahead, "
    "in the fridge or freezer.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "These 15 recipes are a starting point. Cook them on rotation. "
    "Swap proteins to suit your week. Double up when you've got time, "
    "so you've got dinners waiting on the nights you don't.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "And remember — fat loss doesn't come from being perfect. It "
    "comes from being consistent.",
    size=12.5, lh=17.5, gap_after=20)
g.paragraph(
    "You've got this.",
    size=20, lh=24, font="lbi", color=BLUSH, gap_after=24)
g.tracked(LEFT, g.y + 12, "THE WEIGHT LOSS ACADEMY", "asb", 9.5,
          NAVY, 1.6)


# =========================================================== save
g.save({
    "title": NAME,
    "author": "The Weight Loss Academy",
    "subject": "Cookbook",
    "creator": "WLA",
})
