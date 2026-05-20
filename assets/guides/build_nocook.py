#!/usr/bin/env python3
"""Shift & Sustain — No Cook Fat Loss Guide — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "No-Cook-Fat-Loss-Guide.pdf")

g = Guide(OUT)

g.cover(
    "SHIFT & SUSTAIN", "THE WEIGHT LOSS ACADEMY",
    [("No Cook", "lbi", NAVY),
     ("Fat Loss", "lb", BLUSH),
     ("Guide.", "lbi", NAVY)],
    "Smart, weight-conscious meals — without cooking elaborate dishes.",
)

g._new_content_page()

g.paragraph("Losing fat doesn't always mean spending hours in the "
            "kitchen. With busy schedules, long workdays, or even just "
            "wanting to simplify meal prep, you can still make smart, "
            "weight-conscious decisions without cooking elaborate meals.",
            size=12.5, lh=16.8, gap_after=11)
g.paragraph("Here's your Shift & Sustain guide to no-cook fat loss "
            "strategies that focus on convenience without compromising "
            "health.", size=12.5, lh=16.8, gap_after=6)

g.coral_heading("Why No-Cook Meals?", size=20)
g.paragraph("Cooking fresh meals is ideal for controlling ingredients "
            "and keeping meals nutrient-dense. However, life doesn't "
            "always allow for daily cooking. Enter no-cook solutions: "
            "quick, easy, and efficient ways to support your fat-loss "
            "goals without resorting to highly processed options.")

g.coral_heading("Key Principles for No-Cook Fat Loss", size=20)

PRINCIPLES = [
    ("1. Whole Food Focus",
     "Choose whole, minimally processed foods that deliver nutrients "
     "with fewer additives. Avoid frozen meals with long ingredient "
     "lists and opt for single-ingredient frozen items, such as "
     "vegetables, fruits, and proteins. This will help you avoid "
     "hidden sugars, sodium, and unhealthy fats."),
    ("2. High Protein Choices",
     "Protein is essential for fat loss as it helps keep you full and "
     "supports muscle mass. Keep frozen cooked chicken, prawns, or "
     "plant-based protein sources like Quorn on hand. Greek yoghurt, "
     "cottage cheese, and halloumi are also excellent options."),
    ("3. Prioritise Fibre-Rich Foods",
     "Fibre helps control hunger, supports digestion, and slows the "
     "absorption of carbohydrates, keeping blood sugar levels steady. "
     "Frozen mixed vegetables, pre-washed salad greens, and canned "
     "beans are quick to assemble in meals or snacks."),
    ("4. Healthy Fats are Your Friend",
     "Adding healthy fats keeps you satisfied longer. Avocado slices, "
     "nuts, seeds (like chia or flax), and ready-made guacamole can be "
     "incorporated into no-cook meals. Be mindful of portion sizes, as "
     "fats are calorie-dense."),
    ("5. Keep It Balanced",
     "The key to fat loss is balancing macronutrients - protein, fat, "
     "and carbohydrates. Choose options like pre-cooked quinoa or "
     "brown rice or whole-grain wraps to accompany your proteins and "
     "veggies in a high carb meal. These options provide energy and "
     "sustain satiety."),
]
for title, body in PRINCIPLES:
    g.keep_together(110)
    g.coral_heading(title, size=14, gap_before=8, gap_after=7)
    g.paragraph(body)

g.keep_together(150)
g.subhead([("To ", "lb"), ("prepare", "lbi"), (" your frozen dinner:", "lb")])
g.bullets([
    "Select one protein",
    "Select a vegetable or fruit option",
    "Select a carbohydrate",
    "Select a healthy fat",
])
g.keep_together(540)

NA = "Not applicable as protein has a carb component"
SWAP = "Add a carbohydrate from the swap list"
SERVE = "Serve with any frozen vegetables or salad"
g.select_table(
    ["Pick Your Protein", "Serve With?", "Carbohydrate Element", "Side"],
    [
        ["1x Piece of Breaded Fish", "1x Fish Cake", "3 Chicken Goujons",
         "3 Fish Goujons", "1x Chicken Kiev", "¼ Quiche (with pastry)",
         "1x Vegetarian Burger", "4 Falafels", "2 x Sausages",
         "1 x Fillet of fish (plain)", "1 x Fillet of chicken (plain)"],
        [SERVE] * 11,
        [NA, NA, NA, NA, NA, NA, NA, NA, SWAP, SWAP, SWAP],
        ["1 tbsp tzatziki, coleslaw or low sugar tomato sauce"],
    ],
)
g.note("***Note, to keep these meals simple, any frozen item that has "
       "breadcrumbs /pastry etc serve with 1/2 plate of salad or "
       "vegetables, rather than an additional carbohydrate. If the food "
       "item is plain i.e. plain chicken breast or piece of fish, feel "
       "free to add carbohydrate element from WLA swap list. One side "
       "can be added to each meal.")

g.save({
    "title": "No Cook Fat Loss Guide",
    "author": "The Weight Loss Academy",
    "subject": "No-cook fat loss strategies",
    "keywords": "no cook, fat loss, weight loss, frozen, convenience",
    "creator": "The Weight Loss Academy",
})
