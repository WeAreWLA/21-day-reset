#!/usr/bin/env python3
"""How To Build A Low Carb Meal — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "How-To-Build-A-Low-Carb-Meal.pdf")

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("How to build a", "lbi", NAVY),
     ("Low Carb", "lb", BLUSH),
     ("Meal.", "lbi", NAVY)],
    "Protein, plenty of vegetables and healthy fats — with no added "
    "carbohydrate.",
)

g._new_content_page()

g.heading([
    [("When building a low", False)],
    [("carb meal there will be a ", False), ("focus on:", True)],
])

g.bullets([
    "A portion of protein (tofu, egg, fish etc), whether it is meat or "
    "plant protein",
    "A portion of vegetables or salad",
    "Some healthy fats such as extra virgin olive oil, avocado, seeds, "
    "flaxseed, sunflower seeds or walnuts",
    "No additional carbohydrate element such as potatoes, pasta, rice, "
    "bread or couscous etc.",
])

g.subhead([("This will ", "lb"), ("look like this:", "lbi")])
g.diagram_title("How To Build A Low Carb Meal")
g.diagram("low-plate")
g.bullets([
    "STEP 1: Fill ¾ of your plate with vegetables and fruits",
    "STEP 2: Fill ¼ of your plate with lean protein",
    "STEP 3: Add a small portion of healthy fats",
], bold_prefix=True)

g.keep_together(250)
g.subhead([("To ", "lb"), ("prepare", "lbi"), (" your meal:", "lb")])
g.bullets([
    "Select one protein",
    "Select a vegetable or fruit options",
    "Select a healthy fat",
])

g.select_table(
    ["Select Your Protein", "Select Your Veg/Fruit", "Add A Healthy Fat"],
    [
        ["1-2 Eggs (Boiled, Scrambled, Omelette, Frittata)",
         "Canned Fish (Tuna, Salmon, Mackerel)",
         "Cold Meats (Ham, Rotisserie Chicken Etc)",
         "Cheese or Dairy (Halloumi, Feta, Greek Yoghurt)",
         "Vegetarian Alternatives (Tofu, Tempeh, Quorn)"],
        ["Side Salad", "Steamed Veg", "Stir Fry Veg", "Roasted Veg",
         "Fruit Salad"],
        ["Olive Oil", "Nuts", "Seeds", "Nut Butter", "Avocado"],
    ],
)

g.subhead([("Some ", "lb"), ("examples of low carb meals", "lbi"),
           (" include:", "lb")])
g.list_table("LUNCH OR DINNER", [
    "Soup With Protein",
    "Egg Based Dish (Omelette, Frittata, Egg Muffins) With Veggies",
    "Meat (Chicken, Beef, Fish, Veggie Alternative) With Salad",
    "Meat (Chicken, Fish, Veggie Alternative) With Veggies "
    "(Steamed, Roasted, Stir-Fry)",
])
g.note("Within the 12-week meal plans (winter and summer) the low carb "
       "meals are labelled as LC")

g.save({
    "title": "How To Build A Low Carb Meal",
    "author": "The Weight Loss Academy",
    "subject": "Building a balanced low carb meal",
    "keywords": "low carb, meal, weight loss, nutrition, plate",
    "creator": "The Weight Loss Academy",
})
