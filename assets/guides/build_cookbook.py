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
from cookbook_recipes_data import (RECIPES, SECTIONS, NAME, TAGLINE,
                                   SECTION_PARENT)

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "cookbook-recipes")
OUT = os.path.join(HERE, "..", "The-WLA-Weight-Loss-Cookbook.pdf")

PHOTO_H = 200  # hero photo height in points

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
    "They're built around protein, fibre and flavour, so you stay "
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
    f"{len(RECIPES)} fuss-free, macro-balanced recipes, split into "
    f"four sections so you can flick straight to what you fancy.",
    size=11.5, lh=15.6, gap_after=18)


# TOC entries record (toc_page_index, link_rect, target_page_index)
# Page layout: 0=cover, 1=inside title, 2=contents, 3..=recipes
TOC_LINKS = []


def toc_parent(name):
    """Big parent group label (e.g. DINNERS) above its sub-sections."""
    g.ensure(34)
    g.y += 6
    g.tracked(LEFT, g.y + 12, name.upper(), "asb", 11, NAVY, 2.0)
    g.y += 18
    g.page.draw_line((LEFT, g.y), (LEFT + 38, g.y),
                     color=BLUSH, width=2.0)
    g.y += 10


def toc_section(name, recipes, start_page, indent=False):
    """Render a contents section. start_page is the 1-based page number
    of that section. Returns the next start_page. If indent=True the
    section sits visually under a parent group."""
    label_x = LEFT + (14 if indent else 0)
    num_x = LEFT + (18 if indent else 4)
    title_x = LEFT + (46 if indent else 32)
    g.ensure(26)
    g.tracked(label_x, g.y + 11, name.upper(), "asb", 9.5, BLUSH, 1.6)
    g.y += 24
    pg = start_page
    for i, r in enumerate(recipes, 1):
        g.ensure(20)
        y = g.y + 12
        num = f"{i:02d}"
        g.text(num_x, y, num, "asb", 10.4, BLUSH)
        g.text(title_x, y, r["title"], "as", 10.8, INK)
        x = title_x + tw(r["title"], "as", 10.8) + 10
        pgs = f"{pg:02d}"
        while x < RIGHT - tw(pgs, "as", 10.8) - 10:
            g.page.draw_circle((x, y - 3), 0.6, color=None,
                               fill=(0.6, 0.6, 0.6))
            x += 3.3
        g.text_right(RIGHT - 2, y, pgs, "as", 10.8, INK)
        row_rect = fitz.Rect(LEFT, y - 12, RIGHT, y + 6)
        TOC_LINKS.append((g.npages - 1, row_rect, pg - 1))
        g.y += 19
        pg += 1
    g.y += 10
    return pg


section_groups = []
for s in SECTIONS:
    group = [r for r in RECIPES if r["section"] == s]
    section_groups.append((s, group))

start_pg = 4  # first recipe is on page 4 (1-based)
current_parent = None
for name, group in section_groups:
    parent = SECTION_PARENT.get(name)
    if parent and parent != current_parent:
        toc_parent(parent)
        current_parent = parent
    elif not parent:
        current_parent = None
    start_pg = toc_section(name, group, start_pg,
                           indent=bool(parent))


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

    # kicker: RECIPE NN · [PARENT ·] SECTION
    parent = SECTION_PARENT.get(section)
    chips = [f"RECIPE {rnum:02d}"]
    if parent:
        chips.append(parent.upper())
    chips.append(section.upper())
    cx = LEFT
    for i, chip in enumerate(chips):
        if i > 0:
            g.text(cx + 4, g.y, "·", "asb", 8.5, BLUSH)
            cx += 14
        cx = g.tracked(cx, g.y, chip, "asb", 8.5, NAVY, 1.5)
        cx += 6
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

    # estimate content density and pick font sizes; we keep a
    # readable floor of 9.6pt even for the densest recipes.
    def count_items():
        n = 0
        for sub in (r.get("ingredients_sub") or []):
            n += len(sub[1])
        n += len(r.get("ingredients") or [])
        n += len(r.get("to_serve") or [])
        return n
    ing_count = count_items()
    meth_count = len(r["instructions"])
    note_len = len(r.get("note") or "")
    has_subs = bool(r.get("ingredients_sub")) or bool(r.get("to_serve"))
    score = ing_count + meth_count + (note_len // 90) + (2 if has_subs else 0)

    if score >= 26:
        size, lh, item_gap = 9.6, 12.4, 1.8
    elif score >= 22:
        size, lh, item_gap = 9.9, 12.8, 2.0
    elif score >= 18:
        size, lh, item_gap = 10.2, 13.3, 2.2
    else:
        size, lh, item_gap = 10.5, 13.8, 2.6

    head_size = 10
    sub_head_size = max(9.6, size - 0.4)
    bullet_indent = max(13, int(size * 1.3))

    g.text(LEFT, coltop + 9, "INGREDIENTS", "asb", head_size, NAVY)
    yL = coltop + 24

    def render_ing_list(items, x0, w, y):
        for it in items:
            lines = wrap(it, "as", size, w - bullet_indent - 1)
            for i, ln in enumerate(lines):
                if i == 0:
                    g.text(x0, y + 8, "—", "as", size, BLUSH)
                g.text(x0 + bullet_indent, y + 8, ln, "as", size, INK)
                y += lh
            y += item_gap
        return y

    # Render order: main ingredients first, then sub-sections, then to_serve
    if r.get("ingredients"):
        yL = render_ing_list(r["ingredients"], LEFT, lw, yL)
    if r.get("ingredients_sub"):
        for sub_head, sub_items in r["ingredients_sub"]:
            yL += 3
            g.text(LEFT, yL + 9, sub_head, "asi", sub_head_size, NAVY)
            yL += sub_head_size + 8
            yL = render_ing_list(sub_items, LEFT, lw, yL)
    if r.get("to_serve"):
        yL += 3
        g.text(LEFT, yL + 9, "To serve", "asi", sub_head_size, NAVY)
        yL += sub_head_size + 8
        yL = render_ing_list(r["to_serve"], LEFT, lw, yL)

    # RIGHT: instructions
    step_indent = max(22, int(size * 2.4))
    g.text(rx, coltop + 9, "INSTRUCTIONS", "asb", head_size, NAVY)
    yR = coltop + 24
    for k, step in enumerate(r["instructions"], 1):
        num = f"{k:02d}"
        g.text(rx, yR + 8, num, "asb", size, BLUSH)
        for ln in wrap(step, "as", size, rw - step_indent):
            g.text(rx + step_indent, yR + 8, ln, "as", size, INK)
            yR += lh
        yR += item_gap

    # WLA Tip — adaptive sizing so it never crashes into the footer
    end_y = max(yL, yR)
    if r.get("note"):
        end_y += 12
        # leave a comfortable gap above the footer
        SAFE_BOTTOM = CONTENT_BOTTOM - 22
        header_h = 20
        candidates = [(10.5, 13.6), (10.2, 13.2), (10.0, 12.9),
                      (9.8, 12.6), (9.6, 12.3)]
        for sz, lh_ in candidates:
            note_h = len(wrap(r["note"], "asi", sz, CW)) * lh_
            if end_y + header_h + note_h <= SAFE_BOTTOM:
                tip_size, tip_lh = sz, lh_
                break
        else:
            tip_size, tip_lh = 9.4, 12.0
        g.tracked(LEFT, end_y + 9, "WLA TIP", "asb", 8.5, BLUSH, 1.5)
        end_y += header_h
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
    "Eating well isn't about willpower. It's about making the "
    "healthy choice the easy one. The right recipes, prepped ahead, "
    "in the fridge or freezer.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "These 15 recipes are a starting point. Cook them on rotation. "
    "Swap proteins to suit your week. Double up when you've got time, "
    "so you've got dinners waiting on the nights you don't.",
    size=12.5, lh=17.5, gap_after=12)
g.paragraph(
    "And remember, fat loss doesn't come from being perfect. It "
    "comes from being consistent.",
    size=12.5, lh=17.5, gap_after=20)
g.paragraph(
    "You've got this.",
    size=20, lh=24, font="lbi", color=BLUSH, gap_after=20)
g.paragraph(
    "Anna Wallace and the WLA Team",
    size=12, lh=16, font="lbi", color=NAVY, gap_after=0)


# =========================================================== links
for src_page_idx, rect, target_page_idx in TOC_LINKS:
    g.doc[src_page_idx].insert_link({
        "kind": fitz.LINK_GOTO,
        "from": rect,
        "page": target_page_idx,
        "to": fitz.Point(0, 0),
    })


# =========================================================== save
g.save({
    "title": NAME,
    "author": "The Weight Loss Academy",
    "subject": "Cookbook",
    "creator": "WLA",
})
