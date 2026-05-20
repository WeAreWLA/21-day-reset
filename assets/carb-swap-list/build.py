#!/usr/bin/env python3
"""Generate the Simplified Carb Swap List PDF in The Weight Loss Academy
house style (matching The No-Fuss Batch Cookbook layout, using the brand
fonts Libre Baskerville + Alegreya Sans).

Run:  python3 build.py
Output:  ../Simplified-Carb-Swap-List.pdf
"""

import os
import fitz  # PyMuPDF

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "..", "Simplified-Carb-Swap-List.pdf")

# ---------------------------------------------------------------- brand
PAGE_W, PAGE_H = 595.276, 841.89          # A4, matches the cookbook
MARGIN = 51
LEFT = MARGIN
RIGHT = PAGE_W - MARGIN
CW = RIGHT - LEFT                          # content width

CREAM = (0xF9 / 255, 0xF7 / 255, 0xF4 / 255)   # Cream White  #F9F7F4
NAVY = (0x00 / 255, 0x30 / 255, 0x60 / 255)    # Deep Navy    #003060
BLUSH = (0xF7 / 255, 0x9F / 255, 0x83 / 255)   # Soft Blush   #F79F83
BEIGE = (0xE9 / 255, 0xDF / 255, 0xD3 / 255)   # Warm Beige   #E9DFD3
INK = (0x33 / 255, 0x33 / 255, 0x33 / 255)     # Grey Black   #333333
RULE = (0.80, 0.83, 0.87)                      # soft cool hairline

FONTS = {
    "lb":    ("LibreBaskerville-Regular.ttf"),
    "lbi":   ("LibreBaskerville-Italic.ttf"),
    "as":    ("AlegreyaSans-Regular.ttf"),
    "asm":   ("AlegreyaSans-Medium.ttf"),
    "asb":   ("AlegreyaSans-Bold.ttf"),
}
FACE = {k: fitz.Font(fontfile=os.path.join(FONT_DIR, v)) for k, v in FONTS.items()}

# ---------------------------------------------------------------- content
SUBTITLE = ("This guide is designed to help you easily customise your "
            "meals by swapping out carbohydrates and legumes.")

WELCOME_PARAS = [
    "This guide is designed to help you easily customise your meals by "
    "swapping out carbohydrates and legumes.",

    "You can effortlessly adapt your meals to suit your chosen carbohydrate "
    "structure (i.e. LC/HC, MC/MC or HC/LC) by removing, reducing or adding "
    "a carbohydrate element using the quantities outlined in the table below.",

    "For reference, a high carb meal typically consists of about 1/4 of your "
    "plate filling with a carbohydrate element(s), while a medium carb meal "
    "includes just a few tablespoons.",

    "With flexible options and a variety of alternatives, you can create "
    "dishes that meet your taste preferences and dietary needs.",

    "Enjoy experimenting with different combinations to make each meal "
    "delicious and satisfying!",
]

ROWS = [
    ("Any Type Of Bean (Cannellini, Haricot, Soya, Kidney etc.)",
     "3 tablespoons", "> 3 tablespoons"),
    ("Baked Beans, Reduced Sugar", "3 tablespoons", "> 3 tablespoons"),
    ("Brown or Wholewheat Bread", "1 slice", "2 slices"),
    ("Brown Bread Roll", "1 small", "1 large"),
    ("Chickpeas", "3 tablespoons", "> 3 tablespoons"),
    ("Falafels", "2-3 pieces", "> 3 pieces"),
    ("Flour, Wholewheat", "1 - 2 tablespoons", "> 2 tablespoons"),
    ("Hummus", "1 tablespoon", "> 1 tablespoon"),
    ("Lentils or Split peas", "3 tablespoons", "> 3 tablespoons"),
    ("Oat Flakes or Porridge Oats", "1 tablespoon - 40g (½ cup)", "> 40g"),
    ("Potatoes or Sweet Potatoes", "< 100g", "> 100g"),
    ("Rice, Buckwheat, Bulgar Wheat, Couscous, Orzo or Quinoa",
     "30-40g", "> 40g"),
    ("Sugar Free Muesli", "30g (⅓ cup)", "> 30g"),
    ("Wholewheat Pasta", "30-40g", "> 40g"),
    ("Wholewheat Tortilla Wrap", "1 small wrap", "1 large wrap"),
    ("Wholewheat Noodles", "30-40g", "> 40g"),
]

# ---------------------------------------------------------------- helpers
doc = fitz.open()
pages = []


def new_page():
    page = doc.new_page(width=PAGE_W, height=PAGE_H)
    page.draw_rect(fitz.Rect(0, 0, PAGE_W, PAGE_H), color=None, fill=CREAM)
    for alias, fname in FONTS.items():
        page.insert_font(fontname=alias, fontfile=os.path.join(FONT_DIR, fname))
    pages.append(page)
    return page


def tw(text, font, size):
    """Width of a string."""
    return FACE[font].text_length(text, size)


def draw(page, x, y, text, font, size, color):
    """Draw a string with its baseline at (x, y)."""
    page.insert_text((x, y), text, fontname=font, fontsize=size, color=color)


def draw_center(page, cx, y, text, font, size, color):
    draw(page, cx - tw(text, font, size) / 2, y, text, font, size, color)


def draw_right(page, rx, y, text, font, size, color):
    draw(page, rx - tw(text, font, size), y, text, font, size, color)


def draw_tracked(page, x, y, text, font, size, color, tracking):
    """Draw uppercase label text with extra letter-spacing."""
    cx = x
    for ch in text:
        draw(page, cx, y, ch, font, size, color)
        cx += tw(ch, font, size) + tracking
    return cx - tracking


def tracked_width(text, font, size, tracking):
    return sum(tw(ch, font, size) + tracking for ch in text) - tracking


def wrap(text, font, size, max_w):
    """Greedy word wrap -> list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if tw(trial, font, size) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_size(text, font, target_w, hi=120, lo=8):
    """Largest font size at which `text` is <= target_w wide."""
    for _ in range(40):
        mid = (hi + lo) / 2
        if tw(text, font, mid) <= target_w:
            lo = mid
        else:
            hi = mid
    return lo


# ================================================================ PAGE 1
p = new_page()

# kicker
draw_tracked(p, LEFT, 60, "A SIMPLE GUIDE",
             "asb", 9, NAVY, 1.6)
kx = LEFT + tracked_width("A SIMPLE GUIDE", "asb", 9, 1.6)
draw(p, kx + 11, 60, "·", "asb", 9, BLUSH)
draw_tracked(p, kx + 22, 60, "THE WEIGHT LOSS ACADEMY", "asb", 9, NAVY, 1.6)

# title - three lines, sized so the widest line fills the column
TITLE_TARGET = 406
t_lines = [
    ("Simplified", "lbi", NAVY),
    ("Carb Swap", "lb", BLUSH),
    ("List.", "lbi", NAVY),
]
T = min(fit_size(txt, fnt, TITLE_TARGET) for txt, fnt, _ in t_lines)
LH = T * 1.18
b1 = 284
for i, (txt, fnt, col) in enumerate(t_lines):
    draw(p, LEFT, b1 + i * LH, txt, fnt, T, col)

# subtitle - blush italic, narrow measure
sub_size = 13
sub_lines = wrap(SUBTITLE, "lbi", sub_size, 342)
sy = b1 + 2 * LH + 52
for i, ln in enumerate(sub_lines):
    draw(p, LEFT, sy + i * (sub_size + 7.5), ln, "lbi", sub_size, BLUSH)


# ================================================================ PAGE 2
p = new_page()

# heading
HEAD_TARGET = 466
h_lines = [
    ("Welcome to the", "lb"),
    ("Simplified Carb Swap List", "lbi"),
]
H = min(fit_size(txt, fnt, HEAD_TARGET) for txt, fnt in h_lines)
hb1 = 86
hLH = H * 1.18
for i, (txt, fnt) in enumerate(h_lines):
    draw(p, LEFT, hb1 + i * hLH, txt, fnt, H, NAVY)

# blush rule under the heading
ruley = hb1 + hLH + H * 0.42
p.draw_line((LEFT, ruley), (LEFT + 54, ruley), color=BLUSH, width=2.4)

# welcome body
BODY = 11.5
BODY_LH = 15.6
PARA_GAP = 8.5
y = ruley + 30
for para in WELCOME_PARAS:
    for ln in wrap(para, "as", BODY, CW):
        draw(p, LEFT, y, ln, "as", BODY, INK)
        y += BODY_LH
    y += PARA_GAP

# NOTE line
y += 2
draw(p, LEFT, y, "NOTE:", "asb", BODY, NAVY)
note_x = LEFT + tw("NOTE: ", "asb", BODY)
draw(p, note_x, y, "> means greater than", "asb", BODY, INK)

# ---------------------------------------------------------------- table
# column geometry
C1 = LEFT                      # food column left
C2 = 286                       # medium-carb column left
C3 = 415                       # high-carb column left
TABLE_R = RIGHT
NAME_X = C1 + 14               # food name text x
NAME_W = C2 - NAME_X - 12      # food name wrap width
C2_CTR = (C2 + C3) / 2
C3_CTR = (C3 + TABLE_R) / 2

HEADER_H = 31
NAME_SIZE = 11
NAME_LH = 14
VAL_SIZE = 11
ROW_PAD = 13                   # vertical padding inside a row
ROW_MIN = 41                   # minimum row height
BOTTOM_LIMIT = PAGE_H - 66     # keep clear of the footer


def draw_table_header(page, top):
    band = fitz.Rect(C1, top, TABLE_R, top + HEADER_H)
    page.draw_rect(band, color=None, fill=BEIGE)
    ty = top + HEADER_H / 2 + 3.1
    lbl_w2 = tracked_width("MEDIUM CARB", "asb", 9, 1.3)
    draw_tracked(page, C2_CTR - lbl_w2 / 2, ty, "MEDIUM CARB",
                 "asb", 9, NAVY, 1.3)
    lbl_w3 = tracked_width("HIGH CARB", "asb", 9, 1.3)
    draw_tracked(page, C3_CTR - lbl_w3 / 2, ty, "HIGH CARB",
                 "asb", 9, NAVY, 1.3)
    return top + HEADER_H


def row_height(name_lines):
    return max(ROW_MIN, len(name_lines) * NAME_LH + 2 * ROW_PAD)


def draw_row(page, top, name_lines, med, high):
    h = row_height(name_lines)
    rc = top + h / 2                       # row centre
    cap = NAME_SIZE * 0.35                 # baseline offset to optical centre
    n = len(name_lines)
    # food name block, optically centred on the row
    ny = rc + cap - (n - 1) * NAME_LH / 2
    for ln in name_lines:
        draw(page, NAME_X, ny, ln, "asm", NAME_SIZE, NAVY)
        ny += NAME_LH
    # values share the row centreline
    vy = rc + VAL_SIZE * 0.35
    draw_center(page, C2_CTR, vy, med, "as", VAL_SIZE, INK)
    draw_center(page, C3_CTR, vy, high, "as", VAL_SIZE, INK)
    # separator hairline
    page.draw_line((C1, top + h), (TABLE_R, top + h), color=RULE, width=0.7)
    return top + h


# place the table, flowing onto continuation pages as needed
y += 26
cur = p
cur_y = draw_table_header(cur, y)

for i, (name, med, high) in enumerate(ROWS):
    name_lines = wrap(name, "asm", NAME_SIZE, NAME_W)
    h = row_height(name_lines)
    if cur_y + h > BOTTOM_LIMIT:
        # continuation page
        cur = new_page()
        draw(cur, LEFT, 88, "The Carb Swap List", "lbi", 21, NAVY)
        cur.draw_line((LEFT, 100), (LEFT + 54, 100), color=BLUSH, width=2.4)
        cur_y = draw_table_header(cur, 124)
    cur_y = draw_row(cur, cur_y, name_lines, med, high)


# ================================================================ footers
total = len(pages)
for idx in range(total):
    page = doc[idx]
    fy = PAGE_H - 40
    draw_tracked(page, LEFT, fy, "THE WEIGHT LOSS ACADEMY",
                 "asb", 7.5, NAVY, 1.2)
    draw_right(page, RIGHT, fy, f"{idx + 1:02d}", "as", 8.5, NAVY)


doc.set_metadata({
    "title": "The Simplified Carb Swap List",
    "author": "The Weight Loss Academy",
    "subject": "Easily customise your meals by swapping carbohydrates and legumes",
    "keywords": "carb swap, low carb, weight loss, nutrition, meal planning",
    "creator": "The Weight Loss Academy",
})
doc.save(OUT, deflate=True, garbage=4)
print(f"wrote {OUT}  ({total} pages)")
