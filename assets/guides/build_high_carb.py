#!/usr/bin/env python3
"""How To Build A High Carb Meal — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "How-To-Build-A-High-Carb-Meal.pdf")

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("How to build a", "lbi", NAVY),
     ("High Carb", "lb", BLUSH),
     ("Meal.", "lbi", NAVY)],
    "Protein, vegetables, healthy fats and a generous portion of "
    "carbohydrate.",
)

g._new_content_page()

g.heading([
    [("When building a high", False)],
    [("carb meal there will be a ", False), ("focus on:", True)],
])

g.bullets([
    "A portion of protein (tofu, egg, fish etc), whether it is meat or "
    "plant protein",
    "A portion of vegetables or salad",
    "Some healthy fats such as extra virgin olive oil, avocado, seeds, "
    "flaxseed, sunflower seeds or walnuts",
    "A higher amount of additional carbohydrates, such as more than a "
    "few tablespoons of grain, 2 slices of bread, a large wrap, more "
    "than 3 tbsps legumes",
])

g.paragraph("This can be built in 3 ways:", gap_after=6)
g.numbered([
    "Adding only a complex carb",
    "Adding a complex carb and a legume",
    "Adding only a legume",
])

# --- Option 1
g.keep_together(120)
g.paragraph("Option 1: When adding only a complex carb (pasta, rice "
            "bread etc.) this will make up roughly ¼ of the plate.")
g.keep_together(430)
g.subhead([("This will ", "lb"), ("look like this:", "lbi")])
g.diagram_title("How To Build A High Carb Meal")
g.diagram("high-plate")
g.bullets([
    "Step 1: Fill ½ of your plate with vegetables and fruits",
    "Step 2: Fill ¼ of your plate with complex carbohydrates",
    "Step 3: Fill ¼ of your plate with lean protein",
    "Step 4: Add a small portion of healthy fats",
], bold_prefix=True)

# --- Option 2
g.keep_together(150)
g.paragraph("Option 2: When including a carbohydrate/protein food like "
            "legumes or falafel in a high carbohydrate meal, the "
            "additional carbohydrate (i.e. pasta, rice etc.) will need "
            "to be reduced, as the carbohydrate/protein food will count "
            "towards the carbohydrate element.")
g.keep_together(440)
g.subhead([("This will ", "lb"), ("look like this:", "lbi")])
g.diagram_title("High Carbohydrate Meals With A "
                "Carbohydrate/Protein Element")
g.diagram("high-legume-plate")
g.bullets([
    "STEP 1: Fill ½ of your plate with vegetables and fruits",
    "STEP 2: Fill ⅓ of your plate with legumes [i.e. chickpeas, beans "
    "etc. (3 tbsp) or falafel (2-3 pieces)]",
    "STEP 3: Fill ⅙ of your plate with complex carbohydrates",
    "STEP 4: Add a small portion of healthy fats",
], bold_prefix=True)

# --- Option 3
g.keep_together(120)
g.paragraph("Option 3: A high carbohydrate meal could also be made up "
            "of only the legumes without the additional carbohydrate "
            "element (i.e. 6 TBSP legumes OR 5-6 falafels).")
g.keep_together(420)
g.subhead([("This will ", "lb"), ("look like this:", "lbi")])
g.diagram_title("High Carbohydrate Meals With Only A "
                "Carbohydrate/Protein Element")
g.diagram("high-legume-only-plate")
g.bullets([
    "Step 1: Fill ½ of your plate with vegetables and fruits",
    "Step 2: Fill ½ of your plate with legumes [i.e. chickpeas, beans "
    "etc. (6 tbsp) or falafels (5-6 pieces)]",
    "Step 3: Add a small portion of healthy fats",
], bold_prefix=True)

g.keep_together(150)
g.subhead([("To ", "lb"), ("prepare", "lbi"), (" your meal:", "lb")])
g.bullets([
    "Select one protein",
    "Select a vegetable or fruit option",
    "Select a carbohydrate",
    "Select a healthy fat",
])

g.keep_together(470)
g.select_table(
    ["Select Your Protein", "Select Your Veg/Fruit",
     "Select Your Carbohydrate", "Add A Healthy Fat"],
    [
        ["Cooked Meats (Beef, Pork, Chicken etc.)",
         "Canned Fish (Tuna, Salmon, Mackerel)",
         "Sausages or Mince",
         "Falafels *",
         "Beans or chickpeas *",
         "Cheese or Dairy (Halloumi, Feta)",
         "Vegetarian Alternatives (Tofu, Tempeh, Quorn)",
         "Breaded fish, fish cake, chicken goujons etc *"],
        ["Side Salad", "Steamed Veg", "Stir Fry Veg", "Roasted Veg"],
        ["Wholemeal Pasta (>40g)", "Wholegrain Rice (>40g)",
         "Potatoes (>100g)", "Sweet Potatoes (>100g)",
         "Couscous (>40g)", "Wholemeal Bread (2 slices)",
         "Noodles (>40g)", "Quinoa (>40g)"],
        ["Olive Oil", "Nuts", "Seeds", "Nut Butter", "Avocado",
         "Greek Yoghurt",
         "Vegetarian Alternatives (Tofu, Tempeh, Quorn)"],
    ],
)
g.note("Depending on the quantity adding a carb element may not be "
       "applicable or need to be reduced to the medium carb portion.")

g.keep_together(280)
g.subhead([("Some ", "lb"), ("examples of high carb meals", "lbi"),
           (" include:", "lb")])
g.list_table("LUNCH OR DINNER", [
    "Soup With Protein and 2 slices of bread",
    "Meat (Chicken, Beef, Fish, Veggie Alternative) With Salad and a "
    "larger portion of potatoes/sweet potatoes etc. (approx. ¼ of the "
    "plate)",
    "Meat (Chicken, Fish, Veggie Alternative) With Veggies (Steamed, "
    "Roasted, Stir-Fry) and a large portion of rice/pasta/noodles/"
    "quinoa etc. (approx. ¼ of the plate)",
    "Falafel (6 falafel) with Salad or Veggies",
    "Any beans/chickpeas (3 tbsp) With Salad or Veggies and a smaller "
    "portion of rice/pasta/noodles/quinoa etc. (30-40g)",
])
g.note("Within the 12-week meal plans (winter and summer) the high "
       "carb meals are labelled as HC")

g.save({
    "title": "How To Build A High Carb Meal",
    "author": "The Weight Loss Academy",
    "subject": "Building a balanced high carb meal",
    "keywords": "high carb, meal, weight loss, nutrition, plate",
    "creator": "The Weight Loss Academy",
})
