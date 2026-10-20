#!/usr/bin/env python3
"""How To Build A Medium Carb Meal — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "How-To-Build-A-Medium-Carb-Meal.pdf")

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("How to build a", "lbi", NAVY),
     ("Medium Carb", "lb", BLUSH),
     ("Meal.", "lbi", NAVY)],
    "Protein, vegetables, healthy fats and a medium portion of "
    "carbohydrate.",
)

g._new_content_page()

g.heading([
    [("When building a medium", False)],
    [("carb meal there will be a ", False), ("focus on:", True)],
])

g.bullets([
    "A portion of protein (tofu, egg, fish, falafel, beans etc), whether "
    "it is meat or plant protein",
    "A portion of vegetables or salad",
    "Some healthy fats such as extra virgin olive oil, avocado, seeds, "
    "flaxseed, sunflower seeds or walnuts",
    "A medium amount of additional carbohydrates, such as a few "
    "tablespoons of grain, a few smaller potatoes, one slice of bread, "
    "half a wrap, a small roll etc. - roughly half the amount of a high "
    "carbohydrate meal",
])

g.keep_together(430)
g.subhead([("This will ", "lb"), ("look like this:", "lbi")])
g.diagram_title("How To Build A Medium Carb Meal")
g.diagram("medium-plate")
g.bullets([
    "STEP 1: Fill more than ½ of your plate with vegetables and fruits",
    "STEP 2: Fill ⅛ of your plate with complex carbohydrates (i.e. half "
    "the amount of carbohydrate used in the high-carbohydrate meal)",
    "STEP 3: Fill ¼ of your plate with lean protein",
    "STEP 4: Add a small portion of healthy fats",
], bold_prefix=True)

g.keep_together(430)
g.subhead([("Or", "lbi")])
g.diagram_title("Medium Carbohydrate Meals With A "
                "Carbohydrate/Protein Element")
g.diagram("medium-legume-plate")
g.bullets([
    "STEP 1: Fill more than ½ of your plate with vegetables and fruits",
    "STEP 2: Fill ⅓ of your plate with legumes [i.e. chickpeas, beans "
    "etc. (3 tbsp) or falafel (2-3 pieces)]",
    "STEP 3: Add a small portion of healthy fats",
], bold_prefix=True)

g.keep_together(150)
g.subhead([("To ", "lb"), ("prepare", "lbi"), (" your meal:", "lb")])
g.bullets([
    "Select one protein",
    "Select a vegetable or fruit option",
    "Select a carbohydrate *",
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
         "Falafels (2-3) *",
         "Beans or chickpeas (3 tbsp) *",
         "Cheese or Dairy (Halloumi, Feta)",
         "Vegetarian Alternatives (Tofu, Tempeh, Quorn)",
         "Breaded fish, fish cake, chicken goujons etc *"],
        ["Side Salad", "Steamed Veg", "Stir Fry Veg", "Roasted Veg"],
        ["Wholemeal Pasta (30-40g)", "Wholegrain Rice (30-40g)",
         "Potatoes (<100g)", "Sweet Potatoes (<100g)",
         "Couscous (30-40g)", "Wholemeal Bread (1 slice)",
         "Noodles (30-40g)", "Quinoa (30-40g)"],
        ["Olive Oil", "Nuts", "Seeds", "Nut Butter", "Avocado",
         "Greek Yoghurt"],
    ],
)
g.note("*  Adding a carb element is not applicable as protein has a "
       "carb component")

g.keep_together(380)
g.subhead([("Some ", "lb"), ("examples of medium carb meals", "lbi"),
           (" include:", "lb")])
g.list_table("LUNCH OR DINNER", [
    "Soup With Protein and 1 slice of bread",
    "Meat (Chicken, Beef, Fish, Veggie Alternative) With Salad and a "
    "medium portion of potatoes/sweet potatoes etc.",
    "Meat (Chicken, Fish, Veggie Alternative) With Veggies (Steamed, "
    "Roasted, Stir-Fry) and a medium portion of rice/pasta/noodles/"
    "quinoa etc.",
    "Falafel (2-3) with Salad or Veggies",
    "Any beans/chickpeas (3 tbsp) With Salad or Veggies",
])
g.note("Within the 12-week meal plans (winter and summer) the medium "
       "carb meals are labelled as MC")

g.save({
    "title": "How To Build A Medium Carb Meal",
    "author": "The Weight Loss Academy",
    "subject": "Building a balanced medium carb meal",
    "keywords": "medium carb, meal, weight loss, nutrition, plate",
    "creator": "The Weight Loss Academy",
})
