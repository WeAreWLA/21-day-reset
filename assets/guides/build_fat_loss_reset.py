#!/usr/bin/env python3
"""The 5 Day Fat Loss Reset Guide, WLA house style (No-Fuss Cookbook).

A scaffold matching the editorial design of the No-Fuss Batch Cookbook.
Framing content (mission, founder note, tips, guidelines, swap list,
drink / snack tips, educational pages) is fully written. Member-results
photos and the recipe content are intentionally left as placeholders.
"""
import os
import fitz
from wla_style import (Guide, PAGE_W, PAGE_H, LEFT, RIGHT, CW, MARGIN,
                       CONTENT_TOP, CONTENT_BOTTOM,
                       NAVY, BLUSH, INK, BEIGE, CREAM, RULE,
                       wrap, tw, fit_size)

HERE = os.path.dirname(os.path.abspath(__file__))
TESTI_PHOTOS = os.path.join(HERE, "testimonials", "before-after")
TESTI_SHOTS = os.path.join(HERE, "testimonials", "screenshots")
SNACK_IMAGES = os.path.join(HERE, "recommended-snacks")
DIAGRAMS = os.path.join(HERE, "diagrams")
OUT = os.path.join(HERE, "..", "5-Day-Fat-Loss-Reset-Guide.pdf")


def find_file(folder, stem):
    """Find first image file in folder whose name starts with stem
    (case-insensitive). Returns full path or None."""
    if not os.path.isdir(folder):
        return None
    stem = stem.lower()
    for f in sorted(os.listdir(folder)):
        if (f.lower().startswith(stem)
                and f.lower().endswith((".jpg", ".jpeg", ".png"))):
            return os.path.join(folder, f)
    return None


def find_snack_image(stem):
    return find_file(SNACK_IMAGES, stem)


def find_founder_photo():
    """Look for the founder photo in a few sensible places."""
    for folder in (TESTI_PHOTOS, HERE,
                   os.path.join(HERE, "testimonials")):
        f = find_file(folder, "anna-before-after")
        if f:
            return f
    return None

g = Guide(OUT)


# --------------------------------------------------- small helpers
def toc(items):
    g._new_content_page()
    g.heading([[("Table of ", False), ("Contents", True)]])
    for label, pages in items:
        g.ensure(20)
        y = g.y + 12
        g.text(LEFT + 4, y, label, "as", 10.8, INK)
        # dotted leader
        x = LEFT + tw(label, "as", 10.8) + 10
        while x < RIGHT - tw(pages, "as", 10.8) - 10:
            g.page.draw_circle((x, y - 3), 0.6, color=None, fill=(0.6, 0.6, 0.6))
            x += 3.3
        g.text_right(RIGHT - 2, y, pages, "as", 10.8, INK)
        g.y += 19


def photo_placeholder(width=CW, height=240, caption="[ photo ]"):
    g.ensure(height + 16)
    g.page.draw_rect(fitz.Rect(LEFT, g.y, LEFT + width, g.y + height),
                     color=RULE, fill=(0.97, 0.93, 0.90), width=0.6)
    g.text_center(LEFT + width / 2, g.y + height / 2 + 4, caption,
                  "lbi", 12, (0.55, 0.55, 0.55))
    g.y += height + 16


def grid_placeholder(rows, cols, item_h=180, caption="[ photo ]",
                     gap=14):
    """Image grid placeholder, used for member-results pages."""
    cw = (CW - gap * (cols - 1)) / cols
    total_h = rows * item_h + (rows - 1) * gap
    g.ensure(total_h + 8)
    top = g.y
    for r in range(rows):
        for c in range(cols):
            x0 = LEFT + c * (cw + gap)
            y0 = top + r * (item_h + gap)
            g.page.draw_rect(fitz.Rect(x0, y0, x0 + cw, y0 + item_h),
                             color=RULE, fill=(0.97, 0.93, 0.90), width=0.6)
            g.text_center(x0 + cw / 2, y0 + item_h / 2 + 4,
                          caption, "lbi", 11, (0.55, 0.55, 0.55))
    g.y = top + total_h + 12


def kicker(text):
    """Small tracked coral kicker above a content block."""
    g.ensure(20)
    g.tracked(LEFT, g.y + 10, text.upper(), "asb", 8.5, BLUSH, 1.4)
    g.y += 18


def stat_block(label, value):
    """Coral small-caps label + navy value, side by side."""
    g.tracked(LEFT, g.y + 10, label.upper(), "asb", 8.5, BLUSH, 1.4)
    g.text(LEFT, g.y + 28, value, "lb", 14, NAVY)
    g.y += 38


# =========================================================== cover
# clean cover, no top kicker
page = g._blank_page()
g.page = page
title_lines = [("The 5 Day", "lb", NAVY),
               ("Fat Loss", "lbi", BLUSH),
               ("Reset", "lb", NAVY)]
target = 408
T = min(fit_size(t[0], t[1], target) for t in title_lines)
T = min(T, 78)
LH = T * 1.18
b1 = 286
for i, (txt, font, color) in enumerate(title_lines):
    g.text(LEFT, b1 + i * LH, txt, font, T, color)
subtitle = ("Start today, kickstart fat loss and lose up to 5lbs in "
            "5 days. A simple, no-fluff reset for women ready to "
            "feel lighter and more in control.")
sy = b1 + (len(title_lines) - 1) * LH + 56
for ln in wrap(subtitle, "lbi", 13, 348):
    g.text(LEFT, sy, ln, "lbi", 13, NAVY)
    sy += 20.5


# =========================================================== table of contents
toc([
    ("About Us",                                       "03"),
    ("The WLA Mission",                                "04-05"),
    ("A Note From Our Founder, Anna Wallace",          "06"),
    ("WLA Members Results / Our Community Success",    "07-09"),
    ("Important Tips for Getting Started",             "10-11"),
    ("The 5 Day Fat Loss Reset Guidelines",            "12"),
    ("The 5 Day Fat Loss Reset Meal Overview",         "13"),
    ("Breakfast Recipes",                              "14-16"),
    ("Lunch Recipes",                                  "17-19"),
    ("Dinner Recipes",                                 "20-23"),
    ("Mid-Afternoon Snack Recipes",                    "24-26"),
    ("The Swap List",                                  "27-39"),
    ("Drink Tips",                                     "40"),
    ("Snack Tips",                                     "41-44"),
    ("What Balanced Blood Sugar Gives You",            "45"),
    ("Easily Reduce Sugar Cravings in 5 Days",         "46-48"),
    ("Why Breakfast is Important",                     "49"),
    ("Why Snacking is Important",                      "50"),
    ("The WLA Nutrition Formula",                      "51"),
])


# =========================================================== welcome
g._new_content_page()
g.heading([[("Hello, ", False), ("Welcome to", True)],
           [("The WLA Community!", False)]])
g.paragraph("Really excited that you've registered for the 5 Day Fat "
            "Loss Reset, a midlife-friendly week designed to break "
            "the sugar cycle, settle your blood sugar and get the "
            "scales moving again.")
g.paragraph("No 1,200-calorie plans. No banned food lists. No "
            "starting over every Monday. Real food, real life, "
            "and a structure that actually fits a busy week.")

g.subhead([("Your 5-day wins", "lbi")])
WINS = [
    "Lose up to 5 pounds",
    "Calmer cravings in 72 hours",
    "More stable energy",
    "Less mindless snacking",
    "Less bloated feeling",
    "Brighter skin",
]
# 3 col × 2 row mini-cards with coral check badge + navy benefit text
wcols = 3
wgap = 14
wcw = (CW - wgap * (wcols - 1)) / wcols
wch = 80
g.ensure(2 * wch + wgap + 8)
top = g.y
for i, w in enumerate(WINS):
    r = i // wcols
    c = i % wcols
    x0 = LEFT + c * (wcw + wgap)
    y0 = top + r * (wch + wgap)
    # coral left strip
    g.page.draw_rect(fitz.Rect(x0, y0, x0 + 4, y0 + wch),
                     color=None, fill=BLUSH)
    # cream cell
    g.page.draw_rect(fitz.Rect(x0 + 4, y0, x0 + wcw, y0 + wch),
                     color=RULE, fill=(0.985, 0.97, 0.95), width=0.7)
    # coral check disc top-left
    cx, cy, r_ = x0 + 24, y0 + 24, 10
    g.page.draw_circle((cx, cy), r_, color=None, fill=BLUSH)
    g.page.draw_line((cx - 4, cy + 0.5), (cx - 1, cy + 4),
                     color=(1, 1, 1), width=1.6)
    g.page.draw_line((cx - 1, cy + 4), (cx + 5, cy - 3),
                     color=(1, 1, 1), width=1.6)
    # benefit label
    for j, ln in enumerate(wrap(w, "lb", 11.5, wcw - 28)):
        g.text(x0 + 14, y0 + 56 + j * 14, ln, "lb", 11.5, NAVY)
g.y = top + 2 * (wch + wgap) + 4

# closing lines
g.gap(8)
g.paragraph("Ready to feel better faster?", font="asb", size=13,
            color=NAVY, lh=18, gap_after=4)
g.paragraph("Let's dive in.", font="lbi", size=18, color=BLUSH,
            lh=24, gap_after=14)
g.paragraph("Before you start the reset, we want to introduce The "
            "Weight Loss Academy (WLA) very briefly and share "
            "useful tips for getting started in the easiest way.")


# =========================================================== mission
g._new_content_page()
g.heading([[("The ", False), ("WLA Mission", True)]])
g.paragraph("Our mission at The WLA is to help women lose weight for "
            "the last time.")
g.paragraph("Empowering women to achieve sustainable and easy weight "
            "loss through a simple approach that focuses on flexible "
            "nutrition, behavioural change strategies that promote "
            "long-lasting results, and coaching that empowers you to "
            "take control of your lifestyle.")
g.paragraph("Say goodbye to traditional diets and hello to freedom.",
            font="asb", color=NAVY)
g.paragraph("The Weight Loss Academy is focused on maximum effortless "
            "results without deprivation.")
g.subhead([("Helping our clients", "lbi")])
g.bullets([
    "Burn body fat",
    "Build confidence",
    "Slay cravings naturally",
    "Skyrocket energy",
])

g._new_content_page()
g.heading([[("The ", False), ("WLA Mission", True)]])
g.paragraph("The WLA focuses on three main core strategies in our "
            "signature WLA Approach to support clients with every "
            "tool needed for long-lasting, transformative change.")
g.subhead([("The WLA Nutrition Formula", "lbi")])
g.paragraph("Promotes easy weight loss with a flexible approach to "
            "nutrition using everyday foods. Feel lighter within "
            "days, say hello to confidence, lose weight "
            "consistently, increase your energy and say goodbye to "
            "fad diets.")
g.subhead([("Behavioural Change Strategies", "lbi")])
g.paragraph("Centred around the psychology behind weight loss, lose "
            "weight but keep it off. Have food freedom and say "
            "goodbye to self-sabotaging food guilt.")
g.subhead([("Expert Coaching", "lbi")])
g.paragraph("Focuses on consistency strategies so you finally stop "
            "“falling off track”. We guide you every step of the "
            "way with our professional, women-only and "
            "non-judgemental coaching community, focusing on "
            "accountability, staying on track and empowerment.")
# pull-quote callout
g.gap(14)
g.ensure(110)
_qtop = g.y
_qh = 96
g.page.draw_rect(fitz.Rect(LEFT, _qtop, RIGHT, _qtop + _qh),
                 color=None, fill=BEIGE)
g.page.draw_rect(fitz.Rect(LEFT, _qtop, LEFT + 5, _qtop + _qh),
                 color=None, fill=BLUSH)
_qx = LEFT + 22
_qmax = CW - 36
_qtext = ("Join us on a journey back to your happy place in your "
          "body. It's time to feel lighter, more confident, "
          "healthier and more energised, without minimal calories "
          "or extreme workouts.")
_lines = wrap(_qtext, "lbi", 13, _qmax)
_ty = _qtop + (_qh - (len(_lines) - 1) * 19) / 2 + 4
for ln in _lines:
    g.text(_qx, _ty, ln, "lbi", 13, NAVY)
    _ty += 19
g.y = _qtop + _qh + 14


# =========================================================== founder
g._new_content_page()
g.heading([[("A Note From ", False), ("Our Founder", True)]])
# square portrait + body
photo_w = 240
photo_h = 240
photo_top = g.y
photo_path = find_founder_photo()
if photo_path:
    g.page.insert_image(fitz.Rect(LEFT, photo_top, LEFT + photo_w,
                                  photo_top + photo_h),
                        filename=photo_path, keep_proportion=True)
else:
    g.page.draw_rect(fitz.Rect(LEFT, photo_top, LEFT + photo_w,
                               photo_top + photo_h),
                     color=RULE, fill=(0.97, 0.93, 0.90), width=0.6)
    g.text_center(LEFT + photo_w / 2, photo_top + photo_h / 2 - 6,
                  "[ image placeholder ]", "lbi", 11,
                  (0.5, 0.5, 0.55))
    g.text_center(LEFT + photo_w / 2, photo_top + photo_h / 2 + 12,
                  "upload as: anna-before-after.png", "asi", 9.5,
                  (0.55, 0.55, 0.6))
# white signature card sitting OVER the bottom edge of the photo
# (drawn after the image so it renders on top), most of it extends
# below the photo so it doesn't obscure the portrait
pill_y = photo_top + photo_h - 12
g.page.draw_rect(fitz.Rect(LEFT, pill_y, LEFT + photo_w,
                           pill_y + 50),
                 color=None, fill=(1, 1, 1))
g.page.draw_rect(fitz.Rect(LEFT, pill_y, LEFT + 4, pill_y + 50),
                 color=None, fill=BLUSH)
g.text(LEFT + 14, pill_y + 18, "Anna Wallace", "lbi", 12, BLUSH)
g.text(LEFT + 14, pill_y + 32, "BSc Food & Nutrition", "asi", 9, NAVY)
g.text(LEFT + 14, pill_y + 43, "Registered Associate Nutritionist",
       "asi", 9, NAVY)
# body, right column then full width
tx_narrow = LEFT + photo_w + 26
tw_narrow = CW - photo_w - 26
tx_full = LEFT
tw_full = CW
ty = photo_top + 4
photo_bottom = photo_top + photo_h + 56  # photo + overlapping card
intro = ("This is the reset I built from 10 years coaching "
         "women over 45.")
for ln in wrap(intro, "lbi", 13.5, tw_narrow):
    g.text(tx_narrow, ty + 11, ln, "lbi", 13.5, NAVY)
    ty += 19
ty += 8
paragraphs = [
    "I once struggled with my weight, starting each day with "
    "determination but often resorting to unhealthy habits like "
    "the Special K diet or just going hours without food.",
    "Evenings would often end with takeaway, excessive eating, "
    "or alcohol to cope.",
    "Feeling lost and unhappy, I believed I was the \"fat\" one "
    "in my family and didn't know how to change.",
    "After hitting rock bottom, I enrolled in University to study "
    "Food and Nutrition. This decision transformed me. I lost "
    "weight and maintained it, even after pregnancy.",
    "I founded The Weight Loss Academy, supporting over 50,000 "
    "clients globally over 10 years.",
    "Our WLA Approach helps to burn body fat simply and flexibly, "
    "restoring confidence and eliminating sugar cravings.",
]
for txt in paragraphs:
    use_full = ty > photo_bottom - 14
    tx = tx_full if use_full else tx_narrow
    twb = tw_full if use_full else tw_narrow
    for ln in wrap(txt, "as", 10.6, twb):
        g.text(tx, ty + 8, ln, "as", 10.6, INK)
        ty += 14.6
    ty += 7
g.y = max(photo_bottom + 22, ty + 8)

# closing pull-quote that stands out — two sentences with a gap
g.gap(8)
_qparas = [
    ("If you're reading this, know that achieving your goals is "
     "possible, even if you've tried everything and feel like "
     "giving up."),
    ("Your journey matters, and like mine, finding the right "
     "weight loss approach can change everything."),
]
_qlines = []
for p in _qparas:
    _qlines.append(wrap(p, "lbi", 12.5, CW - 36))
_total_lines = sum(len(L) for L in _qlines)
_qh = 24 + _total_lines * 18 + (len(_qparas) - 1) * 10
g.ensure(_qh)
_qtop = g.y
g.page.draw_rect(fitz.Rect(LEFT, _qtop, RIGHT, _qtop + _qh),
                 color=None, fill=BEIGE)
g.page.draw_rect(fitz.Rect(LEFT, _qtop, LEFT + 5, _qtop + _qh),
                 color=None, fill=BLUSH)
_ty = _qtop + 20
for lines in _qlines:
    for ln in lines:
        g.text(LEFT + 22, _ty, ln, "lbi", 12.5, NAVY)
        _ty += 18
    _ty += 10
g.y = _qtop + _qh + 8


# =========================================================== member results
def _images_in(folder):
    if not os.path.isdir(folder):
        return []
    return sorted([os.path.join(folder, f)
                   for f in os.listdir(folder)
                   if f.lower().endswith((".jpg", ".jpeg", ".png"))])


def image_grid(files, rows, cols, item_h=265, gap=14, caption=""):
    """Tile up to rows*cols image files into a grid.  Pads with empty
    placeholders when fewer files are provided."""
    cw = (CW - gap * (cols - 1)) / cols
    total_h = rows * item_h + (rows - 1) * gap
    g.ensure(total_h + 8)
    top = g.y
    n = rows * cols
    for i in range(n):
        r = i // cols
        c = i % cols
        x0 = LEFT + c * (cw + gap)
        y0 = top + r * (item_h + gap)
        rect = fitz.Rect(x0, y0, x0 + cw, y0 + item_h)
        if i < len(files):
            g.page.insert_image(rect, filename=files[i], keep_proportion=True)
        else:
            g.page.draw_rect(rect, color=RULE,
                             fill=(0.97, 0.93, 0.90), width=0.6)
            g.text_center(x0 + cw / 2, y0 + item_h / 2 + 4,
                          caption, "lbi", 11, (0.55, 0.55, 0.55))
    g.y = top + total_h + 12


_photos = _images_in(TESTI_PHOTOS)
_shots = _images_in(TESTI_SHOTS)

g._new_content_page()
g.heading([[("WLA Members ", False), ("Results", True)]])
# square cells, no padding mismatch with the 1080x1080 sources
_cw = (CW - 14) / 2
image_grid(_photos[:4], 2, 2, item_h=_cw,
           caption="[ Member before / after photo ]")

g._new_content_page()
g.heading([[("WLA Members ", False), ("Results", True)]])
image_grid(_photos[4:8], 2, 2, item_h=_cw,
           caption="[ Member before / after photo ]")

g._new_content_page()
g.heading([[("Our ", False), ("Community Success", True)]])
if not _shots:
    g.paragraph("Real posts and messages from our community, to be "
                "added.", font="asi")
image_grid(_shots[:6], 3, 2, item_h=150,
           caption="[ Member post screenshot ]")


# =========================================================== tips
g._new_content_page()
g.heading([[("Important Tips for", False)],
           [("Getting Started", True)]])
g.paragraph("The 5 Day Fat Loss Reset meal guide can include "
            "whatever variation of the meal options you want, it's "
            "fully adjustable depending on the recipes and "
            "ingredients you like.")
g.paragraph("Pick the recipe you like most from the reset meal "
            "overview for each meal (breakfast, lunch, dinner and "
            "snack). Feel free to duplicate recipes that are easy to "
            "batch.")
g.paragraph("Feel free to swap each ingredient around. Or leave out "
            "ingredients you don't like. Season foods more if "
            "required.")
g.note("Go with the flow of the recipes in the guide in terms of "
       "variety, or adjust and simplify by repeating meals more "
       "often. This will not impact results.")

g.subhead([("Meals", "lbi")])
g.bullets([
    "Pick one breakfast for 5 days, or pick and choose from the "
    "guide if you want more variety.",
    "If unable to have one of the lunch recipes due to being out "
    "or busy, go for a protein-based salad, soup, or any egg dish.",
    "Repeat lunches more often if that's easier (e.g. an easy-batch "
    "recipe can cover multiple days).",
    "Always have a portion of protein in each meal. If having "
    "soup, have a piece of protein on the side such as a boiled "
    "egg or some meat / fish.",
])
g.subhead([("Drinks", "lbi")])
g.bullets([
    "Aim to have only one milky coffee per day (i.e. latte / "
    "cappuccino). Tea and coffee with small amounts of milk are "
    "fine.",
    "Aim for 8 glasses of water per day approximately if you can "
    "(see the Drink Tips section for ideas on how to drink more "
    "water).",
])
g.subhead([("Snacks", "lbi")])
g.bullets([
    "Aim for one bigger snack between lunch and dinner to manage "
    "appetite and sugar cravings. Snacking at other times of the "
    "day is fine, but only when physically hungry.",
])
g.keep_together(140)
g.subhead([("Portions", "lbi")])
g.bullets([
    "If you feel it's too much food for you, don't eat it all. "
    "Listen to your body and don't eat just for the sake of eating.",
    "Eat until you've had enough and feel satisfied. Recipes are "
    "for 1 serving unless stated otherwise.",
])
g.subhead([("A note on perfection", "lbi")])
g.bullets([
    "Don't expect perfection, just do your best. Five focused "
    "days beat five perfect ones you never start.",
    "If you slip up at lunch, the next meal is your chance to "
    "reset. Nothing is ruined.",
])


# =========================================================== guidelines
g._new_content_page()
g.heading([[("The 5 Day Fat Loss", False)],
           [("Reset ", False), ("Guidelines", True)]])
g.paragraph("Stick to these eight simple principles and the reset "
            "will do the heavy lifting for you.")

CARDS = [
    ("01", "Eat breakfast",
     "Within 1 hour of waking, every day."),
    ("02", "Protein at breakfast",
     "Sets satiety and steadies blood sugar for the day."),
    ("03", "Protein at every meal",
     "The single biggest lever for staying full."),
    ("04", "Reduce processed foods",
     "And added sugars, cut packaged shortcuts where you can."),
    ("05", "3 meals + smart snacks",
     "Eat 3 meals; snack only when truly hungry."),
    ("06", "Hydrate",
     "At least 8 glasses of water per day."),
    ("07", "Move daily",
     "Even a 20-minute walk counts."),
    ("08", "Dairy-free at breakfast?",
     "Add a scoop of protein powder to keep protein up."),
]

CG = 18          # gap between cards
CH = 110         # card height
ccw = (CW - CG) / 2

g.ensure(CH * 4 + CG * 3 + 8)
top = g.y
for i, (num, title, desc) in enumerate(CARDS):
    r = i // 2
    c = i % 2
    x0 = LEFT + c * (ccw + CG)
    y0 = top + r * (CH + CG)
    # subtle border + cream fill
    g.page.draw_rect(fitz.Rect(x0, y0, x0 + ccw, y0 + CH),
                     color=RULE, fill=(0.985, 0.97, 0.95), width=0.7)
    # coral left accent strip
    g.page.draw_rect(fitz.Rect(x0, y0, x0 + 4, y0 + CH),
                     color=None, fill=BLUSH)
    # coral number, tracked
    g.tracked(x0 + 22, y0 + 30, num, "asb", 11, BLUSH, 1.6)
    # navy title
    g.text(x0 + 22, y0 + 58, title, "lb", 15, NAVY)
    # italic descriptor (wrapped)
    desc_lines = wrap(desc, "asi", 10.5, ccw - 44)
    ty = y0 + 79
    for ln in desc_lines:
        g.text(x0 + 22, ty, ln, "asi", 10.5, INK)
        ty += 13.5
g.y = top + 4 * (CH + CG)
g.gap(4)


# =========================================================== meal overview
g._new_content_page()
g.heading([[("The Reset ", False), ("Meal Overview", True)]])
g.paragraph("Choose any breakfast, lunch or dinner option for each "
            "day from the overview below. Feel free to mix and match. "
            "Batch cook to repeat a recipe or choose a new one each "
            "day.")

g.subhead([("Breakfast Options", "lbi")])
g.bullets(["Option 1, [ recipe ]",
           "Option 2, [ recipe ]",
           "Option 3, [ recipe ]"])

g.subhead([("Morning Snack", "lbi")])
g.paragraph("Opt for a smaller snack, a portion of fruit or "
            "vegetables if hungry. (See snack tips for more info.)")

g.subhead([("Lunch Options", "lbi")])
g.bullets(["Option 1, [ recipe ]",
           "Option 2, [ recipe ]",
           "Option 3, [ recipe ]",
           "Option 4, [ recipe ]"])

g.subhead([("Mid-Afternoon Snack", "lbi")])
g.paragraph("Opt for a bigger snack, select one of our snack "
            "recipes or bigger snack options later in the guide.")

g.subhead([("Dinner Options", "lbi")])
g.bullets(["Option 1, [ recipe ]",
           "Option 2, [ recipe ]",
           "Option 3, [ recipe ]",
           "Option 4, [ recipe ]",
           "Option 5, [ recipe ]"])


# =========================================================== recipes
def placeholder_recipe(slot=None):
    ingredients = [f"[ ingredient {i + 1} ]" for i in range(8)]
    instructions = [f"[ step {i + 1} ]" for i in range(6)]
    g.recipe("[ Recipe Name ]", "?", ingredients, instructions,
             note=(f"[ {slot}, Anna to add recipe ]" if slot
                   else "[ Anna to add recipe ]"))


g.divider("Breakfast", "Recipes.")
placeholder_recipe()
placeholder_recipe()
placeholder_recipe()

g.divider("Lunch", "Recipes.")
placeholder_recipe("15 Min Option")
placeholder_recipe("Easy Batch")
placeholder_recipe("Family Fav")
placeholder_recipe("No Fuss, Zero Time")

g.divider("Dinner", "Recipes.")
placeholder_recipe("20 Min Option")
placeholder_recipe("Family Fav")
placeholder_recipe("Easy Batch")
placeholder_recipe("Easy Batch")
placeholder_recipe("No Fuss, Zero Time")

g.divider("Snack", "Recipes.")
placeholder_recipe()
placeholder_recipe()
placeholder_recipe()


# =========================================================== swap list
g._new_content_page()
g.heading([[("The Food ", False), ("Swap List", True)]])
g.coral_heading("Every single ingredient can easily be changed, just "
                "swap with foods from the same group.")
g.paragraph("The meals and recipes are flexible. Leave out any "
            "ingredients you do not enjoy, or replace with another "
            "alternative. Reduce or increase flavours to your own "
            "liking.")
g.paragraph("Fruits and vegetables can be changed. If you do not "
            "like carrots, swap with peppers; courgettes with peas, "
            "etc.")
g.paragraph("If you do not want chicken, swap with another meat. If "
            "you do not like fish, swap with another protein. Use "
            "vegetarian sausages if you don't eat meat.")
g.paragraph("You can leave out ingredients you do not want, add or "
            "decrease herbs and spices, and taste everything to suit "
            "your preferences.")
g.paragraph("Everything can be adjusted, as long as the adjustment "
            "is done within the right group, you can still get the "
            "best possible results.")

# the swap tables, using list_table for 2-col, select_table for 3-col
PROTEIN_ANIMAL = [
    ("Beef, lamb or pork mince", "100g (3½ oz) to 140g (5 oz)"),
    ("Beef pieces", "100g (3½ oz)"),
    ("Beef sirloin steak", "1 small, approx. 120g (4 oz)"),
    ("Chicken fillet", "Medium, 100g (3½ oz) to 130g (4¾ oz)"),
    ("Chicken thigh", "1 large or 2 small"),
    ("Chorizo", "30g (1 oz)"),
    ("Cod fillet", "175g (6 oz) approx"),
    ("Cubed lamb", "100g (3½ oz)"),
    ("Eggs", "2 eggs"),
    ("Ham", "2 slices"),
    ("Lean bacon / rashers", "2 pieces"),
    ("Pork", "Around 130g pork chop"),
    ("Pork (beef or chicken) sausages", "2 sausages"),
    ("Prawns", "140g (5 oz)"),
    ("Salmon fillet", "1 small approx. 110g (3¾ oz)"),
    ("Salmon (tinned)", "Around 155g / tin"),
    ("Small beef, stewing steak", "110g (4 oz) approx."),
    ("Smoked salmon", "55g (2 oz)"),
    ("Tuna steak", "1 small approx. 110g (3¾ oz)"),
    ("Tuna (tinned)", "1 small can approx. 70g (2½ oz)"),
    ("Turkey or chicken mince", "100g (3½ oz) to 130g (4¾ oz)"),
    ("White fish fillets", "185g (6½ oz)"),
]
PROTEIN_VEGGIE = [
    ("Full-fat Greek yoghurt", "125g (½ cup)"),
    ("Full-fat cottage cheese", "100g (⅔ cup)"),
    ("Halloumi", "70g (2½ oz)"),
    ("Nut roast", "150g (1 cup)"),
    ("Paneer cheese", "70g (2½ oz)"),
    ("Quorn fillet", "1 piece"),
    ("Quorn mince", "75g (3oz)"),
    ("Quorn pieces", "75g (3oz)"),
    ("Ricotta cheese", "30g (2 tablespoons)"),
    ("Semi-skimmed milk", "100ml to 250ml (1 cup)"),
    ("Seitan", "100g (⅔ cup)"),
    ("Tempeh", "100g (⅔ cup)"),
    ("Tofu", "¼ block (115g (4 oz) approx) to 125g (½ cup)"),
    ("Vegetarian sausages", "2 sausages"),
]
LEGUMES = [
    ("Baked beans, reduced sugar", "3 tablespoons", "> 3 tablespoons"),
    ("Black beans", "3 tablespoons", "> 3 tablespoons"),
    ("Butter beans", "3 tablespoons", "> 3 tablespoons"),
    ("Cannellini beans", "3 tablespoons", "> 3 tablespoons"),
    ("Chickpeas", "3 tablespoons", "> 3 tablespoons"),
    ("Falafels", "2-3 pieces", "> 3 pieces"),
    ("Haricot beans", "3 tablespoons", "> 3 tablespoons"),
    ("Hummus", "1 tablespoon", "> 1 tablespoon"),
    ("Pinto beans", "3 tablespoons", "> 3 tablespoons"),
    ("Red kidney beans", "3 tablespoons", "> 3 tablespoons"),
    ("Red lentils", "3 tablespoons", "> 3 tablespoons"),
    ("Soya or edamame beans", "3 tablespoons", "> 3 tablespoons"),
    ("Split peas", "3 tablespoons", "> 3 tablespoons"),
    ("Mixed beans", "3 tablespoons", "> 3 tablespoons"),
]
CARBS = [
    ("Brown bread", "1 medium slice", "2 medium slices"),
    ("Brown bread roll", "1 small", "1 large"),
    ("Brown rice", "30-40g", "> 40g"),
    ("Buckwheat", "30-40g", "> 40g"),
    ("Bulgar wheat", "30-40g", "> 40g"),
    ("Couscous, whole wheat", "30-40g", "> 40g"),
    ("Flour, wholewheat", "1-2 tablespoons", "> 2 tablespoons"),
    ("Giant couscous, whole wheat", "30-40g", "> 40g"),
    ("Oat flakes", "1 tbsp to 40g (½ cup)", "> 40g"),
    ("Orzo", "30-40g", "> 40g"),
    ("Porridge oats", "1 tbsp to 40g (½ cup)", "> 40g"),
    ("Potatoes", "< 100g", "> 100g"),
    ("Quinoa", "30-40g", "> 40g"),
    ("Soba noodles", "30-40g", "> 40g"),
    ("Sugar-free muesli", "30g (⅓ cup)", "> 30g"),
    ("Sweet potato", "< 100g", "> 100g"),
    ("Whole grain rice", "30-40g", "> 40g"),
    ("Whole wheat tortilla wrap", "1 small wrap", "1 large wrap"),
    ("Whole wheat pasta", "30-40g", "> 40g"),
    ("Wholewheat bread", "1 slice", "2 slices"),
    ("Wholewheat noodles", "30-40g", "> 40g"),
    ("Wholewheat spaghetti", "30-40g", "> 40g"),
]
FRUITS_VEG = [
    ("Apple", "1 small"), ("Aubergine", "½ average"),
    ("Avocado", "½ small / ¼ large"), ("Banana", "½ to 1 small"),
    ("Beansprouts", "100g (1¼ cups)"), ("Blueberries", "15 pieces"),
    ("Broccoli", "140g (2 cups)"),
    ("Butternut squash", "70g (½ cup) to 140g (1 cup)"),
    ("Cabbage", "80g"),
    ("Canned tomatoes", "150g (¾ cup) to 200g (1 cup)"),
    ("Carrot", "1 medium"), ("Cauliflower", "100g (½ cup)"),
    ("Cherry tomatoes", "6 pieces"),
    ("Chopped tomatoes", "100g (½ cup)"),
    ("Corn on the cob", "1 medium sized"),
    ("Courgette", "80g (½ cup)"),
    ("Cranberries, fresh or frozen", "40g (½ cup)"),
    ("Cucumber", "½ average or 4 mini"), ("Dates", "2-3 dates"),
    ("Dried fruit (raisins, sultanas)", "1 tablespoon to 30g"),
    ("Frozen mango", "70g (½ cup) to 125g (¾ cup)"),
    ("Frozen peas", "3 tablespoons"),
    ("Fruit salad of your choice", "100g (¾ cup)"),
    ("Green beans", "4 tablespoons to 80g (1 cup)"),
    ("Green pepper", "½ average"), ("Kale", "4 tablespoons"),
    ("Mangetout", "10 pieces"),
    ("Mixed berries, frozen", "3 tablespoons"),
    ("Mixed salad leaves", "50g (2 cups)"),
    ("Mushrooms", "75g (⅔ cup)"), ("Parsnip", "1 small"),
    ("Pineapple", "4 rings"),
    ("Portobello mushrooms", "2 mushrooms"),
    ("Raspberries", "50g (½ cup)"), ("Red pepper", "½ average"),
    ("Rocket", "50g (2 cups)"), ("Sauté vegetables", "250g (2 cups)"),
    ("Spinach leaves", "1 cup to 40g (1¼ cup) / 1 cereal bowl"),
    ("Strawberries", "7-8 pieces"), ("Sundried tomato", "3 pieces"),
    ("Sweetcorn", "2 tablespoons"),
    ("Vegetable stir-fry packet", "200g"), ("Watercress", "1 cup"),
]
FATS = [
    ("Almond butter", "1 tablespoon"), ("Avocado", "¼ or 35g frozen"),
    ("Butter, unsalted", "1 teaspoon"),
    ("Cheddar cheese", "15-30g (⅓ cup)"),
    ("Chia seeds", "1 teaspoon"),
    ("Chocolate chips, dark", "1 tsp up to 80g (⅓ cup)"),
    ("Coconut milk, canned", "100g (½ cup) to 200g (1 cup)"),
    ("Cream", "1 tablespoon"), ("Cream cheese", "1 tablespoon"),
    ("Creme fraiche, full-fat", "1 tablespoon"),
    ("Desiccated coconut", "1 tsp up to 45g (½ cup)"),
    ("Feta cheese", "30g (¼ cup)"),
    ("Flaxseed", "1 tsp up to 50g (⅓ cup)"),
    ("Full-fat goats cheese", "30g (¼ cup)"),
    ("Green pesto", "1 tablespoon"),
    ("Mayonnaise, full-fat", "1 teaspoon"),
    ("Mixed nuts", "1 tablespoon to 30g"), ("Olive oil", "1 teaspoon"),
    ("Olives", "6 pieces"), ("Parmesan cheese", "15-30g (⅓ cup)"),
    ("Peanut butter", "1 tablespoon"),
    ("Salad cream, full-fat", "1 teaspoon"),
    ("Sesame seeds", "1 teaspoon"),
    ("Shredded mozzarella cheese", "30g (⅓ cup)"),
    ("Sour cream, full-fat", "1 tablespoon"),
    ("Sunflower and pumpkin seed mix", "1 teaspoon"),
    ("Sunflower seeds", "1 teaspoon"), ("Tzatziki", "1 tablespoon"),
    ("Vegetarian cheddar cheese", "15-30g (⅓ cup)"),
]
OTHER = [
    ("Balsamic vinegar", "1 tablespoon"),
    ("Chilli sauce", "1 teaspoon"),
    ("Crackers (cream / rye crispbread)", "3 pieces"),
    ("Curry paste", "1 tablespoon"), ("Honey", "1 teaspoon"),
    ("Jam", "1 teaspoon"), ("Lentil crisps", "20-25g"),
    ("Maple syrup", "1 teaspoon"), ("Popcorn, plain", "20-25g"),
    ("Salsa or tomato relish, reduced sugar", "1 tablespoon"),
    ("Soy sauce, reduced-salt", "1 tablespoon"),
    ("Teriyaki sauce", "2 tablespoons"),
    ("Tomato ketchup, reduced sugar", "1 teaspoon"),
    ("Tomato puree", "1 tbsp to 120ml (1½ cup)"),
    ("Worcestershire sauce", "1 tablespoon"),
]


def two_col(items):
    """Render a 2-column food/portion list as a select_table."""
    g.select_table(["Food", "Portion"],
                   [[a for a, _ in items], [b for _, b in items]])


def three_col(items):
    g.select_table(["Food", "Medium carb", "High carb"],
                   [[a for a, _, _ in items],
                    [b for _, b, _ in items],
                    [c for _, _, c in items]])


g._new_content_page()
g.subhead([("Protein, Animal Sources", "lbi")], gap_before=0)
two_col(PROTEIN_ANIMAL)
g._new_content_page()
g.subhead([("Protein, Vegetarian Sources", "lbi")], gap_before=0)
two_col(PROTEIN_VEGGIE)
g._new_content_page()
g.subhead([("Legumes", "lbi")], gap_before=0)
three_col(LEGUMES)
g._new_content_page()
g.subhead([("Carbohydrates", "lbi")], gap_before=0)
three_col(CARBS)
g._new_content_page()
g.subhead([("Fruit and Vegetables", "lbi")], gap_before=0)
two_col(FRUITS_VEG)
g._new_content_page()
g.subhead([("Fats", "lbi")], gap_before=0)
two_col(FATS)
g._new_content_page()
g.subhead([("Other", "lbi")], gap_before=0)
two_col(OTHER)


# --------------------------------------------------- card layout helpers
def numbered_cards(cards, ch=120, gap=18, cols=2):
    """2-column (or other) card grid: coral number, navy title, italic body."""
    cw = (CW - gap * (cols - 1)) / cols
    rows = (len(cards) + cols - 1) // cols
    g.ensure(ch * rows + gap * (rows - 1) + 8)
    top = g.y
    for i, (num, title, desc) in enumerate(cards):
        r = i // cols
        c = i % cols
        x0 = LEFT + c * (cw + gap)
        y0 = top + r * (ch + gap)
        g.page.draw_rect(fitz.Rect(x0, y0, x0 + cw, y0 + ch),
                         color=RULE, fill=(0.985, 0.97, 0.95), width=0.7)
        g.page.draw_rect(fitz.Rect(x0, y0, x0 + 4, y0 + ch),
                         color=None, fill=BLUSH)
        g.tracked(x0 + 22, y0 + 30, num, "asb", 11, BLUSH, 1.6)
        # title
        title_lines = wrap(title, "lb", 15, cw - 44)
        ty = y0 + 56
        for ln in title_lines:
            g.text(x0 + 22, ty, ln, "lb", 15, NAVY)
            ty += 18
        # descriptor
        ty += 4
        for ln in wrap(desc, "as", 10.5, cw - 44):
            g.text(x0 + 22, ty, ln, "as", 10.5, INK)
            ty += 13.5
    g.y = top + rows * ch + (rows - 1) * gap + 4


def diagram_tall(name, max_h=560, max_w=CW, gap_before=4, gap_after=14):
    """Embed a diagram with a higher height cap than g.diagram()."""
    path = os.path.join(DIAGRAMS, f"{name}.png")
    pm = fitz.Pixmap(path)
    ar = pm.width / pm.height
    w = min(max_w, CW)
    h = w / ar
    if h > max_h:
        h = max_h
        w = h * ar
    g.ensure(h + gap_before + gap_after)
    g.y += gap_before
    x0 = LEFT + (CW - w) / 2
    g.page.insert_image(fitz.Rect(x0, g.y, x0 + w, g.y + h),
                        filename=path, keep_proportion=True)
    g.y += h + gap_after


def callout(text, font="asi", size=10.8, lh=14.5,
            fill=BEIGE, gap_before=14, pad=14):
    g.y += gap_before
    lines = wrap(text, font, size, CW - 2 * pad)
    h = lh * len(lines) + 2 * pad
    g.ensure(h + 4)
    top = g.y
    g.page.draw_rect(fitz.Rect(LEFT, top, RIGHT, top + h),
                     color=None, fill=fill)
    ty = top + pad + size * 0.6
    for ln in lines:
        g.text(LEFT + pad, ty, ln, font, size, INK)
        ty += lh
    g.y = top + h + 6


# =========================================================== drink tips
g._new_content_page()
g.heading([[("Drink ", False), ("Tips", True)]])
g.coral_heading("Hydration is one of the quickest wins of the reset.")
g.paragraph("Four small habits make hitting eight glasses a day "
            "almost automatic.")
numbered_cards([
    ("01", "Get a pretty reusable bottle",
     "A bottle on your desk or in your bag is a constant nudge to "
     "sip. Fill it before you leave home and you're already winning."),
    ("02", "Anchor water to your routine",
     "First thing on waking, before each meal, while you're at the "
     "computer. Tie it to things you already do and it sticks."),
    ("03", "Make it fruity",
     "Lemon, lime, orange, cucumber, watermelon, kiwi or "
     "strawberries. A few fresh mint leaves work beautifully too."),
    ("04", "Eat your water",
     "Lettuce, celery, cucumber, watermelon and grapefruit are "
     "loaded with water plus vitamins, minerals and antioxidants."),
], ch=128)
callout("Tea & coffee count, sort of. You can have one milky "
        "coffee (latte or cappuccino) per day. Multiple teas with a "
        "little milk are fine, just keep drinking water alongside.",
        gap_before=20)


# =========================================================== snack tips
g._new_content_page()
g.heading([[("Snack ", False), ("Tips", True)]])
g.coral_heading("Three balanced meals, with snacks only when truly "
                "hungry.")
g.paragraph("Listen to your body and respond to your own hunger "
            "signals, not the clock or the biscuit tin.")
numbered_cards([
    ("01", "Mid-morning",
     "Most people don't need a snack between breakfast and lunch. "
     "If you're genuinely hungry, a piece of fruit or raw veg is "
     "plenty."),
    ("02", "Afternoon",
     "The lunch to dinner gap is longer, this is where the "
     "afternoon \"bigger\" snack lives. It heads off the 3pm slump "
     "and stops you reaching for sugar."),
    ("03", "Very active?",
     "If you exercise regularly, you'll likely benefit from an "
     "additional bigger snack to fuel your energy needs."),
    ("04", "Less active?",
     "If you're mostly sedentary, you may find you need fewer "
     "snacks. Hunger is the dial, not habit."),
], ch=128)
callout("Bananas only once a day, please. They're more calorie-"
        "dense than other fruits, one is plenty.",
        gap_before=18)
g.subhead([("Final tips", "lbi")], gap_before=14)
g.bullets([
    "Eat when you're hungry, not out of boredom or habit.",
    "Pause and check in with your body before reaching for a snack.",
    "Aim for nourishment, every bite is a chance to fuel your "
    "body well.",
])

# fruit & veg snack inspiration table
g._new_content_page()
g.heading([[("Fruit & Veg ", False), ("Snack Inspiration", True)]])
FV = ["Apples", "Asparagus", "Aubergine",
      "Banana (max 1 per day)", "Beetroot", "Blackberries",
      "Blueberries", "Bok choy", "Broccoli", "Carrots",
      "Celery", "Cherries", "Courgette", "Cranberries (fresh)",
      "Cucumber", "Grapefruit", "Grapes (1 cup)", "Kelp",
      "Kiwi", "Mandarins", "Mango", "Melon", "Mushrooms",
      "Onions", "Orange (1 large)", "Pears", "Peppers",
      "Pineapple (1 cup)", "Plums", "Radishes", "Raspberries",
      "Spinach", "Strawberries", "Sugar snap peas (1 cup)",
      "Tomatoes", "Watercress"]
# arrange into 3 columns
cols = [[], [], []]
for i, item in enumerate(FV):
    cols[i % 3].append(item)
# pad
maxlen = max(len(c) for c in cols)
for c in cols:
    while len(c) < maxlen:
        c.append("")
g.select_table(None, cols)

g._new_content_page()
g.heading([[("Bigger ", False), ("Snack Inspiration", True)]])
g.paragraph("Some women only need one bigger snack per day, others "
            "more. If you exercise regularly you may need more than "
            "someone less mobile.")
g.paragraph("We recommend a bigger snack between lunch and dinner to "
            "prevent sugar cravings. You may need another in the "
            "evening. Some days you may need two bigger snacks and "
            "some days one, tune in and be flexible.")
diagram_tall("bigger-snack-inspiration", max_h=640, max_w=CW * 0.85)

g._new_content_page()
g.heading([[("Some ", False), ("Recommended Snacks", True)]])
g.paragraph("Brands we genuinely like for when you want something "
            "from the shop.")

SNACKS = [
    ("lindt",     "Lindt Dark Chocolate", "70%+ cocoa"),
    ("propercorn","Propercorn", "Sweet & Salty"),
    ("nakd",      "Nakd Bars", "natural fruit & nut"),
    ("hazelnut",  "Deliciously Ella", "Hazelnut Bites"),
    ("almonds",   "Deliciously Ella", "Dipped Almonds"),
    ("nush",      "Nush", "Strawberry yoghurt + berries"),
    ("bear",      "Bear Fruit Rolls", "yoyos & strips"),
    ("oat-bars",  "Deliciously Ella", "Oat Bars"),
]
cols, rows = 4, 2
gap = 14
cw = (CW - gap * (cols - 1)) / cols
img_h = 140
label_h = 38
ch = img_h + label_h
g.ensure(rows * (ch + gap) + 8)
top = g.y
for i, (stem, name, sub) in enumerate(SNACKS):
    r = i // cols
    c = i % cols
    x0 = LEFT + c * (cw + gap)
    y0 = top + r * (ch + gap)
    img = find_snack_image(stem)
    if img:
        g.page.insert_image(fitz.Rect(x0, y0, x0 + cw, y0 + img_h),
                            filename=img, keep_proportion=True)
    else:
        g.page.draw_rect(fitz.Rect(x0, y0, x0 + cw, y0 + img_h),
                         color=RULE, fill=(0.97, 0.93, 0.90), width=0.6)
        g.text_center(x0 + cw / 2, y0 + img_h / 2 + 4,
                      "[ product ]", "lbi", 10, (0.55, 0.55, 0.55))
    # name + sub
    g.text_center(x0 + cw / 2, y0 + img_h + 14, name, "lb", 9.5, NAVY)
    g.text_center(x0 + cw / 2, y0 + img_h + 28, sub, "asi", 9, INK)
g.y = top + rows * (ch + gap) + 8


# --------------------------------------------------- check-list helper
def check_box(x, y, size=14):
    """Draw a navy outline check box."""
    g.page.draw_rect(fitz.Rect(x, y, x + size, y + size),
                     color=NAVY, fill=None, width=1.0)


def image_with_checks(image_name, items, image_w=0.5,
                      img_max_h=320, gap_after=14,
                      image_y=0, text_y=0):
    """Place an image on the left and a checkbox list on the right.
    Falls back to a labelled placeholder if the image isn't present.
    image_y/text_y let callers shift each column vertically."""
    path = os.path.join(DIAGRAMS, f"{image_name}.png")
    have_image = os.path.exists(path)
    tx0 = LEFT + CW * image_w + 12
    tw_box = CW - (CW * image_w) - 12
    line_size = 11
    line_h = 15.5
    item_gap = 10
    items_h = 0
    for it in items:
        ln_count = len(wrap(it, "as", line_size, tw_box - 26))
        items_h += max(ln_count * line_h, 22) + item_gap
    if have_image:
        pm = fitz.Pixmap(path)
        ar = pm.width / pm.height
        w = CW * image_w
        h = w / ar
        if h > img_max_h:
            h = img_max_h
            w = h * ar
    else:
        w = CW * image_w
        h = min(img_max_h, max(items_h, 200))
    block_h = max(h + max(0, image_y),
                  items_h + max(0, text_y))
    g.ensure(block_h + gap_after)
    top = g.y
    x0 = LEFT
    img_top = top + image_y
    if have_image:
        g.page.insert_image(fitz.Rect(x0, img_top, x0 + w,
                                      img_top + h),
                            filename=path, keep_proportion=True)
    else:
        g.page.draw_rect(fitz.Rect(x0, img_top, x0 + w, img_top + h),
                         color=RULE, fill=(0.97, 0.93, 0.90), width=0.6)
        g.text_center(x0 + w / 2, img_top + h / 2 - 6,
                      "[ image placeholder ]", "lbi", 11,
                      (0.5, 0.5, 0.55))
        g.text_center(x0 + w / 2, img_top + h / 2 + 12,
                      f"upload as: {image_name}.png", "asi", 9.5,
                      (0.55, 0.55, 0.6))
    ty = top + 4 + text_y
    for it in items:
        ln_count = len(wrap(it, "as", line_size, tw_box - 26))
        row_h = max(ln_count * line_h, 22)
        check_box(tx0, ty + 2, size=14)
        lines = wrap(it, "as", line_size, tw_box - 26)
        ly = ty + 12
        for ln in lines:
            g.text(tx0 + 22, ly, ln, "as", line_size, INK)
            ly += line_h
        ty += row_h + item_gap
    g.y = top + block_h + gap_after


def image_above_checks(image_name, items, image_w=0.7,
                       img_max_h=360, gap_after=18, gap_between=14):
    """Big image centred on top, with the checkbox list below it."""
    path = os.path.join(DIAGRAMS, f"{image_name}.png")
    have_image = os.path.exists(path)
    if have_image:
        pm = fitz.Pixmap(path)
        ar = pm.width / pm.height
        w = CW * image_w
        h = w / ar
        if h > img_max_h:
            h = img_max_h
            w = h * ar
    else:
        w = CW * image_w
        h = 240
    line_size = 11
    line_h = 15.5
    item_gap = 8
    items_h = 0
    for it in items:
        ln_count = len(wrap(it, "as", line_size, CW - 30))
        items_h += ln_count * line_h + item_gap
    g.ensure(h + gap_between + items_h + gap_after)
    top = g.y
    # image centred horizontally
    x0 = LEFT + (CW - w) / 2
    if have_image:
        g.page.insert_image(fitz.Rect(x0, top, x0 + w, top + h),
                            filename=path, keep_proportion=True)
    else:
        g.page.draw_rect(fitz.Rect(x0, top, x0 + w, top + h),
                         color=RULE, fill=(0.97, 0.93, 0.90),
                         width=0.6)
        g.text_center(x0 + w / 2, top + h / 2 - 6,
                      "[ image placeholder ]", "lbi", 11,
                      (0.5, 0.5, 0.55))
        g.text_center(x0 + w / 2, top + h / 2 + 12,
                      f"upload as: {image_name}.png", "asi", 9.5,
                      (0.55, 0.55, 0.6))
    # checkbox list, full-width below
    ty = top + h + gap_between
    for it in items:
        check_box(LEFT, ty + 2, size=14)
        for ln in wrap(it, "as", line_size, CW - 30):
            g.text(LEFT + 22, ty + 12, ln, "as", line_size, INK)
            ty += line_h
        ty += item_gap
    g.y = top + h + gap_between + items_h + gap_after


# =========================================================== Why balanced blood sugar
def _icon_sugar_cubes(cx, cy, s=14):
    """3 stacked cube outlines."""
    g.page.draw_rect(fitz.Rect(cx - s + 1, cy - s/3, cx - 1, cy + s/3),
                     color=NAVY, fill=None, width=1.0)
    g.page.draw_rect(fitz.Rect(cx + 1, cy - s/3, cx + s - 1, cy + s/3),
                     color=NAVY, fill=None, width=1.0)
    g.page.draw_rect(fitz.Rect(cx - s/2, cy - s, cx + s/2, cy - s/3),
                     color=NAVY, fill=None, width=1.0)


def _icon_smile(cx, cy, s=14):
    g.page.draw_circle((cx, cy), s, color=NAVY, fill=None, width=1.0)
    g.page.draw_circle((cx - s/3, cy - s/4), 0.9,
                       color=None, fill=NAVY)
    g.page.draw_circle((cx + s/3, cy - s/4), 0.9,
                       color=None, fill=NAVY)
    # smile arc — short bezier as 4 line segments
    pts = [(cx - s/2.2, cy + s/5), (cx - s/4, cy + s/2.2),
           (cx + s/4, cy + s/2.2), (cx + s/2.2, cy + s/5)]
    for a, b in zip(pts, pts[1:]):
        g.page.draw_line(a, b, color=NAVY, width=1.0)


def _icon_plate(cx, cy, s=14):
    # plate (circle) with fork left and knife right
    g.page.draw_circle((cx, cy), s * 0.85, color=NAVY, fill=None,
                       width=1.0)
    # pie slice marker inside plate (small line)
    g.page.draw_line((cx, cy), (cx + s/2, cy - s/3),
                     color=NAVY, width=0.8)
    # fork
    fx = cx - s * 1.4
    g.page.draw_line((fx, cy - s), (fx, cy + s),
                     color=NAVY, width=1.0)
    for dx in (-0.3, 0, 0.3):
        g.page.draw_line((fx + dx * s/2, cy - s),
                         (fx + dx * s/2, cy - s/2),
                         color=NAVY, width=0.8)
    # knife
    kx = cx + s * 1.4
    g.page.draw_line((kx, cy - s), (kx, cy + s),
                     color=NAVY, width=1.0)
    g.page.draw_line((kx - s/4, cy - s), (kx, cy - s/2),
                     color=NAVY, width=0.8)
    g.page.draw_line((kx, cy - s/2), (kx, cy - s),
                     color=NAVY, width=0.8)


def _icon_scale(cx, cy, s=14):
    # bathroom scale — rectangle with display circle
    g.page.draw_rect(fitz.Rect(cx - s, cy - s*0.7, cx + s, cy + s*0.7),
                     color=NAVY, fill=None, width=1.0)
    g.page.draw_circle((cx, cy + s*0.1), s * 0.35,
                       color=NAVY, fill=None, width=0.8)
    # display tick at top
    g.page.draw_line((cx, cy + s*0.1 - s*0.35),
                     (cx + s*0.15, cy + s*0.1 - s*0.18),
                     color=NAVY, width=0.8)


def _icon_donut(cx, cy, s=14):
    # outer + inner circle
    g.page.draw_circle((cx, cy), s, color=NAVY, fill=None, width=1.2)
    g.page.draw_circle((cx, cy), s * 0.38, color=NAVY, fill=None,
                       width=1.0)
    # sprinkle marks
    for ang_deg, _ in [(40, 1), (130, 1), (220, 1), (310, 1)]:
        import math
        ang = math.radians(ang_deg)
        x1, y1 = cx + s*0.65*math.cos(ang), cy + s*0.65*math.sin(ang)
        x2, y2 = cx + s*0.8*math.cos(ang), cy + s*0.8*math.sin(ang)
        g.page.draw_line((x1, y1), (x2, y2), color=NAVY, width=0.9)


def _icon_appetite(cx, cy, s=14):
    # fork + down arrow
    fx = cx - s * 0.55
    g.page.draw_line((fx, cy - s), (fx, cy + s),
                     color=NAVY, width=1.0)
    for dx in (-1, 0, 1):
        g.page.draw_line((fx + dx * s*0.25, cy - s),
                         (fx + dx * s*0.25, cy - s*0.45),
                         color=NAVY, width=0.8)
    # down arrow on right
    ax = cx + s * 0.6
    g.page.draw_line((ax, cy - s*0.8), (ax, cy + s*0.8),
                     color=NAVY, width=1.2)
    g.page.draw_line((ax - s*0.35, cy + s*0.3),
                     (ax, cy + s*0.8), color=NAVY, width=1.2)
    g.page.draw_line((ax + s*0.35, cy + s*0.3),
                     (ax, cy + s*0.8), color=NAVY, width=1.2)


def _icon_chart_down(cx, cy, s=14):
    # zigzag down with arrowhead
    pts = [(cx - s*0.95, cy - s*0.6), (cx - s*0.3, cy + s*0.1),
           (cx + s*0.2, cy - s*0.35), (cx + s*0.95, cy + s*0.6)]
    for a, b in zip(pts, pts[1:]):
        g.page.draw_line(a, b, color=NAVY, width=1.2)
    # arrowhead at last point
    ex, ey = pts[-1]
    g.page.draw_line((ex, ey), (ex - s*0.35, ey + s*0.05),
                     color=NAVY, width=1.0)
    g.page.draw_line((ex, ey), (ex - s*0.1, ey - s*0.32),
                     color=NAVY, width=1.0)


def icon_card(x0, y0, w, h, draw_fn, label):
    """Beige badge with the icon + 2-line label below."""
    badge_r = 28
    cx = x0 + w / 2
    cy = y0 + badge_r + 6
    g.page.draw_circle((cx, cy), badge_r, color=None,
                       fill=(0.93, 0.88, 0.83))
    draw_fn(cx, cy, s=14)
    # label below
    lines = wrap(label, "as", 10.5, w - 14)
    ty = y0 + badge_r + 22
    for ln in lines:
        g.text_center(cx, ty + 10, ln, "as", 10.5, INK)
        ty += 13


g._new_content_page()
g.heading([[("What balanced ", False), ("blood sugar", True)],
           [("gives you.", False)]])
g.paragraph("Maintaining balanced blood sugar levels is a key "
            "component of overall health and wellness. Fluctuations "
            "in blood sugar can impact many aspects of your daily "
            "life, from your energy levels to your mood and even "
            "your long-term health. By focusing on keeping your "
            "blood sugar steady, you can enhance your well-being "
            "and support your fat loss goals.")
g.paragraph("Here's why balanced blood sugar is so important:",
            font="asb", color=NAVY, gap_after=22)

BENEFITS = [
    ("01", "Reduced desire for sugar"),
    ("02", "Improved mood"),
    ("03", "More control around food"),
    ("04", "Weight stabilises / weight reduction"),
    ("05", "Reduced cravings"),
    ("06", "Appetite falls and stabilises"),
    ("07", "No extreme highs followed by severe plummets"),
]

# 7 numbered cards — same pattern as the Guidelines page
bcols = 2
bgap = 16
bcw = (CW - bgap * (bcols - 1)) / bcols
bch = 76
rows = (len(BENEFITS) + bcols - 1) // bcols
g.ensure(rows * bch + (rows - 1) * bgap + 8)
top = g.y
for i, (num, label) in enumerate(BENEFITS):
    r = i // bcols
    c = i % bcols
    x0 = LEFT + c * (bcw + bgap)
    y0 = top + r * (bch + bgap)
    # cream card + coral left accent
    g.page.draw_rect(fitz.Rect(x0, y0, x0 + bcw, y0 + bch),
                     color=RULE, fill=(0.985, 0.97, 0.95), width=0.7)
    g.page.draw_rect(fitz.Rect(x0, y0, x0 + 4, y0 + bch),
                     color=None, fill=BLUSH)
    g.tracked(x0 + 22, y0 + 26, num, "asb", 11, BLUSH, 1.6)
    # label, possibly wrapped
    for j, ln in enumerate(wrap(label, "lb", 13, bcw - 44)):
        g.text(x0 + 22, y0 + 50 + j * 17, ln, "lb", 13, NAVY)
g.y = top + rows * bch + (rows - 1) * bgap + 8


# =========================================================== easily reduce sugar cravings
g._new_content_page()
g.heading([[("Easily ", False), ("Reduce Sugar Cravings", True),
            (" in 5 Days", False)]])
g.paragraph("When the right amount of food is consumed at the right "
            "times this will result in balanced blood sugar levels "
            "throughout the day (when less sugar is consumed "
            "overall). The body can handle some sugar but excessive "
            "amounts have an impact.")
image_above_checks("ideal-blood-sugar", [
    "Peaks after each meal or snack (think balanced meals).",
    "Small peaks and troughs.",
    "Blood sugar level dips = signal to eat.",
], image_w=0.55, img_max_h=270, gap_between=14)

g._new_content_page()
g.subhead([("The ", "lbi"),
           ("Rollercoaster Blood Sugar Levels", "lb")], gap_before=0)
image_above_checks("rollercoaster-danger", [
    "High spike, a more volatile reaction to the muffin.",
    "Body releases a big hit of insulin to clear the sugar.",
    "Extreme high followed by extreme slump.",
], image_w=0.55, img_max_h=270, gap_between=14)

g._new_content_page()
g.subhead([("The Rollercoaster, ", "lbi"),
           ("Highs and Lows", "lb")], gap_before=0)
image_above_checks("rollercoaster-highs-lows", [
    "Extreme highs.",
    "Extreme lows.",
    "Low mood / high mood.",
    "Unbalanced overall.",
    "More sugar cravings and generally eating more sugar overall.",
], image_w=0.55, img_max_h=270, gap_between=14)
callout("Side note, weight loss can be extremely difficult here.",
        font="asi", gap_before=10)


# =========================================================== why breakfast
g._new_content_page()
g.heading([[("Why ", False), ("Breakfast", True),
            (" Is Important", False)]])
g.paragraph("When breakfast is skipped, blood sugar levels will "
            "continue to dip and it will be more likely that foods "
            "high in sugar for energy will be consumed. Having "
            "breakfast within an hour of waking will allow blood "
            "sugar and insulin levels to stabilise.")
g.paragraph("In addition, having a protein element with breakfast "
            "will help with satiety levels (feeling of fullness) "
            "and sets the body up for the day, meaning there will "
            "likely be less snacking on less nutrient-dense options "
            "throughout the day.")
image_with_checks("breakfast-sugar-insulin", [
    "Blood sugar levels dip due to skipping breakfast.",
    "This results in looking for something to give a quick \"hit\" "
    "to stop feeling shaky, hungry, tired, have crazy cravings and "
    "so more sugar is reached for.",
    "High spike followed by a big hit of insulin to remove the "
    "sugar from the blood to the cells.",
    "Extreme high followed by extreme slump.",
    "The cycle continues.",
], image_w=0.45, img_max_h=240)


# =========================================================== why snacking
g._new_content_page()
g.heading([[("Why ", False), ("Snacking", True),
            (" Is Important", False)]])
g.paragraph("Snacking is really important as it helps keep blood "
            "sugar levels steady during the day. If food is eaten "
            "at regular intervals throughout the day, having a dip "
            "in the blood sugar levels will be less likely and "
            "therefore reaching for less nutrient-dense foods for a "
            "kick of energy will not happen.")
g.paragraph("Snacking is important to bridge the gap between "
            "breakfast and lunch and then lunch and dinner. "
            "However, snacks should not be eaten just for the sake "
            "of it, snacking is supposed to tide the body over "
            "until the next meal.")
image_with_checks("snacking-curves", [
    "Gentle peaks after each meal or snack (think balanced meals).",
    "Small peaks and troughs.",
    "A blood sugar dip is your body's signal to eat, not stress.",
], image_w=0.55, img_max_h=240, text_y=30)


# =========================================================== nutrition formula
g._new_content_page()
g.heading([[("The ", False), ("WLA Nutrition", True)],
           [("Formula.", False)]])
g.paragraph("At The WLA, we use our unique Nutrition Formula to "
            "help reduce sugar cravings in as little as 3 days and "
            "support visible weight loss within 5 days.")
g.paragraph("This formula is built around portion control and a "
            "healthy balance of all food groups, carbohydrates, "
            "protein, and fats, rather than restriction or "
            "elimination.")
g.paragraph("The WLA Nutrition Formula focuses on building meals "
            "that are high in protein and adjusted to be low, "
            "medium, or higher in carbohydrates, depending on the "
            "meal and the individual. This structure teaches you "
            "how to create nutritionally balanced meals that "
            "support fat loss, improve health, and help reduce "
            "sugar cravings, while still being realistic and "
            "sustainable long term.")
g.paragraph("Your 5 Day Fat Loss Reset Guide has been designed "
            "using this formula for maximum results. You don't "
            "need to calculate or overthink anything, simply "
            "follow the guide and the setup provided.")
g.subhead([("The WLA Nutrition Formula focuses on", "lbi")])
g.bullets([
    "Reducing carbohydrate intake (not eliminating carbohydrates, "
    "just adjusting amounts).",
    "Reducing processed foods and added sugars.",
    "Prioritising whole, nourishing foods including:",
], gap_after=0)
# nested sub-items (tight, no extra gap above)
for sub in ["Wholegrain carbohydrates", "Lean meats and fish",
            "Full-fat dairy", "Healthy fats",
            "Fruits and vegetables"]:
    g.page.draw_circle((LEFT + 30, g.y + 9), 1.4, color=None,
                       fill=BLUSH)
    g.text(LEFT + 42, g.y + 13, sub, "as", 11, INK)
    g.y += 16
g.y += 8
g.bullets([
    "Including snacks when guided by hunger signals.",
    "Using an 80:20 approach across the week.",
    "Drinking adequate water (around 8 glasses per day).",
    "Including regular daily movement.",
])


# =========================================================== save
g.save({
    "title": "The 5 Day Fat Loss Reset Guide",
    "author": "The Weight Loss Academy",
    "subject": "A simple 5 day fat loss reset",
    "keywords": "fat loss, reset, 5 day, nutrition, weight loss",
    "creator": "The Weight Loss Academy",
})
