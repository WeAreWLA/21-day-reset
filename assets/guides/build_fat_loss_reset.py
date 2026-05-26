#!/usr/bin/env python3
"""The 5 Day Fat Loss Reset Guide — WLA house style (No-Fuss Cookbook).

A scaffold matching the editorial design of the No-Fuss Batch Cookbook.
Framing content (mission, founder note, tips, guidelines, swop list,
drink / snack tips, educational pages) is fully written. Member-results
photos and the recipe content are intentionally left as placeholders.
"""
import os
import fitz
from wla_style import (Guide, PAGE_W, PAGE_H, LEFT, RIGHT, CW, MARGIN,
                       CONTENT_TOP, CONTENT_BOTTOM,
                       NAVY, BLUSH, INK, BEIGE, CREAM, RULE,
                       wrap, tw, fit_size)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "5-Day-Fat-Loss-Reset-Guide.pdf")

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
    """Image grid placeholder — used for member-results pages."""
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
# custom cover — no top kicker; adds "for women 45+" accent line
page = g._blank_page()
g.page = page
title_lines = [("The", "lbi", NAVY),
               ("5 Day", "lb", BLUSH),
               ("Fat Loss Reset.", "lbi", NAVY)]
target = 408
T = min(fit_size(t[0], t[1], target) for t in title_lines)
T = min(T, 78)
LH = T * 1.18
b1 = 240
for i, (txt, font, color) in enumerate(title_lines):
    g.text(LEFT, b1 + i * LH, txt, font, T, color)
# accent line — "for women 45+"
accent_y = b1 + (len(title_lines) - 1) * LH + 56
g.text(LEFT, accent_y, "for women 45+", "lbi", 28, BLUSH)
# subtitle from the registration page
subtitle = ("Break the sugar cycle, steady your energy and start "
            "losing fat again — without 1,200-calorie plans or "
            "cutting out carbs.")
sy = accent_y + 50
for ln in wrap(subtitle, "lbi", 13, 392):
    g.text(LEFT, sy, ln, "lbi", 13, INK)
    sy += 20.5


# =========================================================== table of contents
toc([
    ("About Us",                                       "03"),
    ("The WLA Mission",                                "04-05"),
    ("A Note From Our Founder — Anna Wallace",          "06"),
    ("WLA Members Results / Our Community Success",    "07-09"),
    ("Important Tips for Getting Started",             "10-11"),
    ("The 5 Day Fat Loss Reset Guidelines",            "12"),
    ("The 5 Day Fat Loss Reset Meal Overview",         "13"),
    ("Breakfast Recipes",                              "14-16"),
    ("Lunch Recipes",                                  "17-19"),
    ("Dinner Recipes",                                 "20-23"),
    ("Mid-Afternoon Snack Recipes",                    "24-26"),
    ("The Swop List",                                  "27-40"),
    ("Drink Tips",                                     "41"),
    ("Snack Tips",                                     "42-45"),
    ("Why Balanced Blood Sugar Supports Fat Loss",     "46"),
    ("Easily Kickstart Fat Loss in 5 Days",            "47-48"),
    ("Why Breakfast is Important",                     "49"),
    ("Why Snacking is Important",                      "50"),
    ("The WLA Nutrition Formula",                      "51"),
])


# =========================================================== welcome
g._new_content_page()
g.heading([[("Hello, ", False), ("Welcome to", True)],
           [("The WLA Community!", False)]])
g.paragraph("Really excited that you've registered for the 5 Day Fat "
            "Loss Reset — a midlife-friendly week designed to break "
            "the sugar cycle, settle your blood sugar and get the "
            "scales moving again.")
g.paragraph("No 1,200-calorie plans. No banned food lists. No "
            "starting over every Monday. Real food, real life, "
            "and a structure that actually fits a busy week.")
g.subhead([("Your 5-day wins", "lbi")])
g.bullets([
    "Kickstart your weight loss — most women see 2-7 lbs shift by "
    "day 5, largely from reduced bloating and water retention.",
    "Sugar cravings handled — the afternoon snack pull starts "
    "fading within the first 1-3 days.",
    "Steady, balanced energy — no more mid-afternoon crashes or "
    "post-dinner slumps.",
    "Lighter, less bloated — clothes start fitting better by the "
    "end of the week.",
    "A reset you can keep going — habits that compound for the "
    "next 4 weeks, not a one-off you start over from on Monday.",
])
g.paragraph("Ready to feel better faster? Let's dive in.",
            font="asb", color=NAVY)
g.paragraph("Before you start the reset, we want to introduce The "
            "Weight Loss Academy (WLA) very briefly and share useful "
            "tips for getting started in the easiest way.")


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
g.heading([[("Our ", False), ("Three Pillars", True)]])
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
g.paragraph("Centred around the psychology behind weight loss — lose "
            "weight but keep it off. Have food freedom and say "
            "goodbye to self-sabotaging food guilt.")
g.subhead([("Expert Coaching", "lbi")])
g.paragraph("Focuses on consistency strategies so you finally stop "
            "“falling off track”. We guide you every step of the "
            "way with our professional, women-only and "
            "non-judgemental coaching community — focusing on "
            "accountability, staying on track and empowerment.")
g.note("Join us on a journey back to your happy place in your body. "
       "It's time to feel lighter, more confident, healthier and more "
       "energised — without minimal calories and extreme workouts.")


# =========================================================== founder
g._new_content_page()
g.heading([[("A Note From ", False)],
           [("Our Founder", True)]])
# portrait placeholder + body — two-column treatment
photo_w = CW * 0.42
photo_h = 280
photo_top = g.y
g.page.draw_rect(fitz.Rect(LEFT, photo_top, LEFT + photo_w,
                           photo_top + photo_h),
                 color=RULE, fill=(0.97, 0.93, 0.90), width=0.6)
g.text_center(LEFT + photo_w / 2, photo_top + photo_h / 2 - 12,
              "[ Anna portrait ]", "lbi", 11, (0.55, 0.55, 0.55))
# white signature card overlay near the bottom of the photo
pill_y = photo_top + photo_h - 56
g.page.draw_rect(fitz.Rect(LEFT + 14, pill_y, LEFT + photo_w - 14,
                           pill_y + 44),
                 color=None, fill=(1, 1, 1))
g.text(LEFT + 22, pill_y + 16, "Anna Wallace", "lbi", 12, BLUSH)
g.text(LEFT + 22, pill_y + 28, "BSc Food & Nutrition", "asi", 9, NAVY)
g.text(LEFT + 22, pill_y + 39, "Registered Associate Nutritionist",
       "asi", 9, NAVY)
# body — right column
tx = LEFT + photo_w + 26
tw_body = CW - photo_w - 26
ty = photo_top + 4
# big italic intro line
intro = ("This is the reset I built from 10 years coaching "
         "women over 45.")
for ln in wrap(intro, "lbi", 13.5, tw_body):
    g.text(tx, ty + 11, ln, "lbi", 13.5, NAVY)
    ty += 19
ty += 6
# body paragraphs
for txt in [
    "I'm a Registered Associate Nutritionist (BSc Food & "
    "Nutrition) and the founder of The Weight Loss Academy. Over "
    "the last 10 years my team and I have supported over 50,000 "
    "women — the majority of them in midlife — to lose weight "
    "without 1,200-calorie plans, banned food lists or starting "
    "over every Monday.",
    "This 5 Day Reset is the entry point. It's the exact rhythm "
    "I use with paying clients to break the sugar cycle in 72 "
    "hours, settle blood sugar, and put a structure in place "
    "that actually fits a midlife week.",
    "I once struggled with my weight too — Special K breakfasts, "
    "hours without food, evenings ending with takeaway or wine. "
    "Studying nutrition transformed me, and I built the WLA to "
    "give other women that same shift without the punishment.",
    "If you're reading this, know that your goals are possible — "
    "even if you've tried everything else. Like mine, finding the "
    "right approach can change everything.",
]:
    for ln in wrap(txt, "as", 10.5, tw_body):
        g.text(tx, ty + 8, ln, "as", 10.5, INK)
        ty += 14.4
    ty += 7
# signature
g.y = max(photo_top + photo_h + 22, ty + 8)
g.text(LEFT, g.y + 18, "— Anna", "lbi", 20, BLUSH)
g.y += 30


# =========================================================== member results
g._new_content_page()
g.heading([[("WLA Members ", False), ("Results", True)]])
grid_placeholder(2, 2, item_h=265,
                 caption="[ Member before / after photo ]")

g._new_content_page()
g.heading([[("WLA Members ", False), ("Results", True)]])
grid_placeholder(2, 2, item_h=265,
                 caption="[ Member before / after photo ]")

g._new_content_page()
g.heading([[("Our ", False), ("Community Success", True)]])
g.paragraph("Real posts and messages from our community — to be "
            "added.", font="asi")
grid_placeholder(3, 2, item_h=150,
                 caption="[ Member post screenshot ]")


# =========================================================== tips
g._new_content_page()
g.heading([[("Important Tips for", False)],
           [("Getting Started", True)]])
g.paragraph("The 5 Day Fat Loss Reset meal guide can include "
            "whatever variation of the meal options you want — it's "
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
    "day is fine — but only when physically hungry.",
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
    "Don't expect perfection — just do your best. Five focused "
    "days beat five perfect ones you never start.",
    "If you slip up at lunch, the next meal is your chance to "
    "reset. Nothing is ruined.",
    "Tick off each day in the Facebook group — accountability "
    "compounds. By Friday you'll feel the difference.",
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
     "And added sugars — cut packaged shortcuts where you can."),
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
g.bullets(["Option 1 — [ recipe ]",
           "Option 2 — [ recipe ]",
           "Option 3 — [ recipe ]"])

g.subhead([("Morning Snack", "lbi")])
g.paragraph("Opt for a smaller snack — a portion of fruit or "
            "vegetables if hungry. (See snack tips for more info.)")

g.subhead([("Lunch Options", "lbi")])
g.bullets(["Option 1 — [ recipe ]",
           "Option 2 — [ recipe ]",
           "Option 3 — [ recipe ]",
           "Option 4 — [ recipe ]"])

g.subhead([("Mid-Afternoon Snack", "lbi")])
g.paragraph("Opt for a bigger snack — select one of our snack "
            "recipes or bigger snack options later in the guide.")

g.subhead([("Dinner Options", "lbi")])
g.bullets(["Option 1 — [ recipe ]",
           "Option 2 — [ recipe ]",
           "Option 3 — [ recipe ]",
           "Option 4 — [ recipe ]",
           "Option 5 — [ recipe ]"])


# =========================================================== recipes
def placeholder_recipe(slot=None):
    ingredients = [f"[ ingredient {i + 1} ]" for i in range(8)]
    instructions = [f"[ step {i + 1} ]" for i in range(6)]
    g.recipe("[ Recipe Name ]", "?", ingredients, instructions,
             note=(f"[ {slot} — Anna to add recipe ]" if slot
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


# =========================================================== swop list
g._new_content_page()
g.heading([[("The Food ", False), ("Swop List", True)]])
g.coral_heading("Every single ingredient can easily be changed — just "
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
g.paragraph("Everything can be adjusted — as long as the adjustment "
            "is done within the right group, you can still get the "
            "best possible results.")

# the swop tables — using list_table for 2-col, select_table for 3-col
PROTEIN_ANIMAL = [
    ("Beef, lamb or pork mince", "100g (3½ oz) — 140g (5 oz)"),
    ("Beef pieces", "100g (3½ oz)"),
    ("Beef sirloin steak", "1 small, approx. 120g (4 oz)"),
    ("Chicken fillet", "Medium, 100g (3½ oz) — 130g (4¾ oz)"),
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
    ("Turkey or chicken mince", "100g (3½ oz) — 130g (4¾ oz)"),
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
    ("Semi-skimmed milk", "100ml — 250ml (1 cup)"),
    ("Seitan", "100g (⅔ cup)"),
    ("Tempeh", "100g (⅔ cup)"),
    ("Tofu", "¼ block (115g (4 oz) approx) — 125g (½ cup)"),
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
    ("Oat flakes", "1 tbsp — 40g (½ cup)", "> 40g"),
    ("Orzo", "30-40g", "> 40g"),
    ("Porridge oats", "1 tbsp — 40g (½ cup)", "> 40g"),
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
    ("Avocado", "½ small / ¼ large"), ("Banana", "½ — 1 small"),
    ("Beansprouts", "100g (1¼ cups)"), ("Blueberries", "15 pieces"),
    ("Broccoli", "140g (2 cups)"),
    ("Butternut squash", "70g (½ cup) — 140g (1 cup)"),
    ("Cabbage", "80g"),
    ("Canned tomatoes", "150g (¾ cup) — 200g (1 cup)"),
    ("Carrot", "1 medium"), ("Cauliflower", "100g (½ cup)"),
    ("Cherry tomatoes", "6 pieces"),
    ("Chopped tomatoes", "100g (½ cup)"),
    ("Corn on the cob", "1 medium sized"),
    ("Courgette", "80g (½ cup)"),
    ("Cranberries, fresh or frozen", "40g (½ cup)"),
    ("Cucumber", "½ average or 4 mini"), ("Dates", "2-3 dates"),
    ("Dried fruit (raisins, sultanas)", "1 tablespoon — 30g"),
    ("Frozen mango", "70g (½ cup) — 125g (¾ cup)"),
    ("Frozen peas", "3 tablespoons"),
    ("Fruit salad of your choice", "100g (¾ cup)"),
    ("Green beans", "4 tablespoons — 80g (1 cup)"),
    ("Green pepper", "½ average"), ("Kale", "4 tablespoons"),
    ("Mangetout", "10 pieces"),
    ("Mixed berries, frozen", "3 tablespoons"),
    ("Mixed salad leaves", "50g (2 cups)"),
    ("Mushrooms", "75g (⅔ cup)"), ("Parsnip", "1 small"),
    ("Pineapple", "4 rings"),
    ("Portobello mushrooms", "2 mushrooms"),
    ("Raspberries", "50g (½ cup)"), ("Red pepper", "½ average"),
    ("Rocket", "50g (2 cups)"), ("Sauté vegetables", "250g (2 cups)"),
    ("Spinach leaves", "1 cup — 40g (1¼ cup) / 1 cereal bowl"),
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
    ("Coconut milk, canned", "100g (½ cup) — 200g (1 cup)"),
    ("Cream", "1 tablespoon"), ("Cream cheese", "1 tablespoon"),
    ("Creme fraiche, full-fat", "1 tablespoon"),
    ("Desiccated coconut", "1 tsp up to 45g (½ cup)"),
    ("Feta cheese", "30g (¼ cup)"),
    ("Flaxseed", "1 tsp up to 50g (⅓ cup)"),
    ("Full-fat goats cheese", "30g (¼ cup)"),
    ("Green pesto", "1 tablespoon"),
    ("Mayonnaise, full-fat", "1 teaspoon"),
    ("Mixed nuts", "1 tablespoon — 30g"), ("Olive oil", "1 teaspoon"),
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
    ("Brown sauce", "1 teaspoon"), ("Chilli sauce", "1 teaspoon"),
    ("Crackers (cream crackers, rye crispbread etc.)", "3 pieces"),
    ("Curry paste", "1 tablespoon"), ("Honey", "1 teaspoon"),
    ("Jam", "1 teaspoon"), ("Lentil crisps", "20-25g"),
    ("Maple syrup", "1 teaspoon"), ("Popcorn, plain", "20-25g"),
    ("Salsa or tomato relish, reduced sugar", "1 tablespoon"),
    ("Soy sauce, reduced-salt", "1 tablespoon"),
    ("Teriyaki sauce", "2 tablespoons"),
    ("Tomato ketchup, reduced sugar", "1 teaspoon"),
    ("Tomato puree", "1 tbsp — 120ml (1½ cup)"),
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
g.subhead([("Protein — Animal Sources", "lbi")], gap_before=0)
two_col(PROTEIN_ANIMAL)
g._new_content_page()
g.subhead([("Protein — Vegetarian Sources", "lbi")], gap_before=0)
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


# =========================================================== drink tips
g._new_content_page()
g.heading([[("Drink ", False), ("Tips", True)]])
g.coral_heading("Hydration is one of the quickest wins of the reset.")

g.subhead([("1. Get a pretty reusable water bottle", "lbi")])
g.paragraph("Keeping a water bottle handy serves as a visual "
            "reminder to drink more. Fill it before you leave home — "
            "and it's better for the planet than single-use bottles.")
g.subhead([("2. Add water to your daily routine", "lbi")])
g.paragraph("Drink at set points during the day — as soon as you "
            "wake, before a meal, while at your desk. Sipping "
            "consistently throughout the day makes hitting your "
            "fluid goals effortless.")
g.subhead([("3. Make it fruity", "lbi")])
g.paragraph("Add lemon, lime, orange, cucumber, watermelon, kiwi or "
            "strawberries. A few fresh mint leaves or other herbs "
            "work beautifully too.")
g.subhead([("4. Eat your water", "lbi")])
g.paragraph("Foods like lettuce, celery, cucumber, watermelon and "
            "grapefruit are loaded with water and packed with "
            "vitamins, minerals and antioxidants.")
g.note("You can have one milky coffee (latte or cappuccino) per "
       "day. Multiple teas with a little milk are also fine — just "
       "make sure you're drinking water alongside.")


# =========================================================== snack tips
g._new_content_page()
g.heading([[("Snack ", False), ("Tips", True)]])
g.coral_heading("Three balanced meals, with snacks only when truly "
                "hungry.")
g.paragraph("The key is to listen to your body and respond to your "
            "own hunger signals.")
g.subhead([("Mid-morning snacks", "lbi")])
g.paragraph("Most people find they don't need a snack between "
            "breakfast and lunch. If you do feel genuinely hungry, "
            "choose a light option like a piece of fruit or raw "
            "vegetables.")
g.subhead([("Afternoon snacks", "lbi")])
g.paragraph("The gap between lunch and dinner tends to be longer, "
            "which is why many people benefit from a more "
            "substantial snack in the afternoon. We call these the "
            "“bigger” snacks. They help you avoid the 3pm slump and "
            "reduce the temptation to reach for sugary or processed "
            "foods.")
g.subhead([("Snack amounts — what's right for you?", "lbi")])
g.bullets([
    "Very active or exercise regularly? You may benefit from "
    "additional bigger snacks to fuel your energy needs.",
    "Less active or sedentary? You might find you need fewer "
    "snacks.",
])
g.note("We recommend limiting bananas to one per day, as they're "
       "more calorie-dense than other fruits.")
g.subhead([("Final tips", "lbi")])
g.bullets([
    "Eat when you're hungry — not out of boredom or habit.",
    "Pause and check in with your body before reaching for a snack.",
    "Aim for nourishment — every bite is a chance to fuel your "
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
            "some days one — tune in and be flexible.")
g.bullets([
    "3 crackers with nut butter, cream cheese, cottage cheese, "
    "hummus, avocado, cheddar or tuna",
    "1 natural cereal bar of your choice (Nakd is a great option)",
    "Apple slices with 1 tablespoon of nut butter",
    "Small handful of nuts and raisins",
    "1 banana sliced and topped with 1 tablespoon of nut butter",
    "2 medjool dates with cream cheese or nut butter",
    "1 cup of grapes and 1 boiled egg",
    "2 boiled eggs",
    "30g dark chocolate",
    "1 cup of homemade popcorn",
    "125g Greek yoghurt and fruit",
])

g._new_content_page()
g.heading([[("Some ", False), ("Recommended Snacks", True)]])
g.paragraph("Brands we genuinely like for when you want something "
            "from the shop.")
g.bullets([
    "Lindt Dark Chocolate (70%+ cocoa)",
    "Propercorn Sweet & Salty",
    "Nakd Bars",
    "Deliciously Ella Hazelnut Bites",
    "Deliciously Ella Dipped Almonds",
    "Nush Strawberry Yoghurt & Berries",
    "Bear Fruit Rolls",
    "Deliciously Ella Oat Bars",
])


# =========================================================== educational
g._new_content_page()
g.heading([[("Why Balanced Blood Sugar", False)],
           [("Supports ", False), ("Fat Loss", True)]])
g.paragraph("Maintaining balanced blood sugar levels is a key part "
            "of fat loss. Fluctuations in blood sugar drive "
            "cravings, energy crashes and over-eating. Keeping "
            "blood sugar steady supports your fat loss goals and "
            "your energy at the same time.")
g.subhead([("What balanced blood sugar gives you", "lbi")])
g.bullets([
    "Reduced desire for sugar",
    "Improved mood",
    "More control around food",
    "Weight stabilises / weight reduction",
    "Reduced cravings",
    "Appetite falls and stabilises",
    "No extreme highs followed by severe plummets",
])

g._new_content_page()
g.heading([[("Easily ", False), ("Kickstart Fat Loss", True),
            (" in 5 Days", False)]])
g.paragraph("When the right amount of food is consumed at the right "
            "times, this results in balanced blood sugar levels "
            "throughout the day. The body can handle some sugar — "
            "but excessive amounts have an impact on fat loss.")
g.subhead([("The ideal blood sugar pattern", "lbi")])
g.bullets([
    "Gentle peaks after each meal or snack — think balanced meals.",
    "Small peaks and troughs, not extremes.",
    "A blood sugar dip is your body's signal to eat.",
])

g._new_content_page()
g.subhead([("The rollercoaster — highs and lows", "lbi")],
          gap_before=0)
g.paragraph("Without balance, the day looks like this:")
g.bullets([
    "Extreme highs",
    "Extreme lows",
    "Low mood / high mood",
    "Unbalanced overall",
    "More sugar cravings — and generally more sugar overall",
])
g.note("Fat loss can be extremely difficult on this pattern.")


g._new_content_page()
g.heading([[("Why ", False), ("Breakfast", True),
            (" Is Important", False)]])
g.paragraph("When breakfast is skipped, blood sugar levels continue "
            "to dip and it becomes more likely that foods high in "
            "sugar will be reached for. Having breakfast within an "
            "hour of waking allows blood sugar and insulin levels to "
            "stabilise.")
g.paragraph("Including a protein element with breakfast helps with "
            "satiety (feeling of fullness) and sets the body up for "
            "the day — meaning less snacking on less nutrient-dense "
            "options throughout the day, which is exactly what "
            "supports fat loss.")
g.subhead([("The skip-breakfast cycle", "lbi")])
g.bullets([
    "Blood sugar dips due to skipping breakfast.",
    "Body searches for a quick “hit” — shaky, hungry, tired — so "
    "sugar gets reached for.",
    "High spike followed by a big hit of insulin.",
    "Extreme high followed by extreme slump.",
    "The cycle continues.",
])


g._new_content_page()
g.heading([[("Why ", False), ("Snacking", True),
            (" Is Important", False)]])
g.paragraph("Snacking is really important — it helps keep blood "
            "sugar levels steady during the day. If food is eaten at "
            "regular intervals, dips in blood sugar are less likely, "
            "and reaching for less nutrient-dense foods for a kick of "
            "energy won't happen.")
g.paragraph("Snacking bridges the gap between breakfast and lunch, "
            "and then lunch and dinner. However, snacks should not "
            "be eaten just for the sake of it — snacking is meant to "
            "tide you over until the next meal.")
g.subhead([("With healthy snacks you get", "lbi")])
g.bullets([
    "Gentle peaks after each meal or snack (think balanced meals).",
    "Small peaks and troughs.",
    "A blood sugar dip is your body's signal to eat — not stress.",
])


g._new_content_page()
g.heading([[("The ", False), ("WLA Nutrition", True)],
           [("Formula.", False)]])
g.paragraph("At The WLA, we use our unique Nutrition Formula to "
            "help kickstart fat loss in as little as 5 days and "
            "support visible weight loss within a week.")
g.paragraph("This formula is built around portion control and a "
            "healthy balance of all food groups — carbohydrates, "
            "protein, and fats — rather than restriction or "
            "elimination.")
g.paragraph("The WLA Nutrition Formula focuses on building meals "
            "that are high in protein and adjusted to be low, "
            "medium, or higher in carbohydrates, depending on the "
            "meal and the individual. This teaches you how to "
            "create nutritionally balanced meals that support fat "
            "loss, improve health, and help reduce sugar cravings — "
            "while staying realistic and sustainable long term.")
g.paragraph("Your 5 Day Fat Loss Reset has been designed using this "
            "formula for maximum results. You don't need to "
            "calculate or overthink anything — simply follow the "
            "guide.")
g.subhead([("The formula focuses on", "lbi")])
g.bullets([
    "Reducing carbohydrate intake (not eliminating — just "
    "adjusting amounts).",
    "Reducing processed foods and added sugars.",
    "Prioritising whole, nourishing foods.",
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
