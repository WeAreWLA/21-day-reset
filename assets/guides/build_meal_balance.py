#!/usr/bin/env python3
"""Nutrition Formula Meal Balance — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "Nutrition-Formula-Meal-Balance.pdf")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("Nutrition", "lbi", NAVY),
     ("Formula", "lb", BLUSH),
     ("Meal Balance.", "lbi", NAVY)],
    "How to balance low, medium and high carb meals across your week.",
)

g._new_content_page()

g.heading([[("Different ", False), ("Meal Structures", True)]])

g.subhead([("Low Carb/High Carb Balance", "lbi")], color=NAVY,
          gap_before=8, gap_after=16)
g.week_table(DAYS, [
    ("Structure", ["LC or HC"] * 7),
    ("Lunch", ["Low Carb"] * 7),
    ("Dinner", ["High Carb"] * 7),
])
g.note("Note: Alternatively a high carb lunch can be balanced with a "
       "low carb dinner.", font="lbi", color=NAVY, size=11,
       gap_before=12, gap_after=8)

g.keep_together(200)
g.subhead([("Medium Carb/Medium Carb Balance", "lbi")], color=NAVY,
          gap_before=22, gap_after=16)
g.week_table(DAYS, [
    ("Structure", ["MC or MC"] * 7),
    ("Lunch", ["Medium Carb"] * 7),
    ("Dinner", ["Medium Carb"] * 7),
])

g.save({
    "title": "Nutrition Formula — Meal Balance",
    "author": "The Weight Loss Academy",
    "subject": "Balancing meal structures across the week",
    "keywords": "meal balance, low carb, high carb, medium carb, weekly plan",
    "creator": "The Weight Loss Academy",
})
