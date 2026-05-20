#!/usr/bin/env python3
"""Shift & Sustain — Fat Loss Booster — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "Fat-Loss-Booster.pdf")

MEALS = ["Breakfast", "Snack", "Lunch", "Snack", "Dinner", "Snack (Optional)"]
SNACKS = ["Smoothie", "2 Eggs", "Greek Yoghurt (125G) with berries",
          "Egg muffins", "Apple slices with 1 tbsp peanut butter",
          "Small handful of nuts", "Celery sticks and cream cheese",
          "Chocolate chia-pudding", "Any type of meat/fish"]

g = Guide(OUT)

g.cover(
    "SHIFT & SUSTAIN", "THE WEIGHT LOSS ACADEMY",
    [("Fat Loss", "lbi", NAVY), ("Booster.", "lb", BLUSH)],
    "Recommendations to kickstart fat loss again after a weight loss "
    "plateau.",
)

g._new_content_page()

g.heading([[("Background", True)]])
g.paragraph("The Fat Loss Booster is a set of recommendations for those "
            "who have reached a weight loss plateau, followed the weight "
            "loss plateau guide and are still wanting that extra boost "
            "to help with progress. It is important to remember that "
            "normal healthy weight loss would be around 1-2 pounds per "
            "week but bear in mind it will not be possible to lose "
            "weight every week. This is due to physiology in the body "
            "and social factors such as eating out/trips away etc.")
g.paragraph("A plateau is when an individual has not seen results for "
            "more than 4 weeks despite eating consistently and moving "
            "their body. It is not recommended to weigh every week as "
            "this will provide inaccurate results. If weighing, once a "
            "month is sufficient and will give a clearer picture of "
            "overall results. Implementing the Fat Loss Booster "
            "principles for 3-5 days should be enough to kickstart the "
            "fat loss process again.")
g.paragraph("The Fat Loss Booster is not recommended for highly "
            "physically active clients who undertake high-intensity "
            "training or fitness classes.", font="asb", color=NAVY)
g.paragraph("The Fat Loss Booster focuses on 4 main areas:", gap_after=4)
g.bullets([
    "Breakfast - Swap breakfasts for low carb/high protein combination",
    "Vegetables - Include plenty of vegetables at lunch and dinner",
    "Snacks - Aim to have high protein snacks throughout the day",
    "Lunch and Dinner - Go for high protein/lower carb options",
])

g.section_label("Breakfast")
g.paragraph("As above, swap breakfasts for low carbohydrate and high "
            "protein options.")
g.paragraph("For example, rather than having oats and muesli, opt for a "
            "protein-based breakfast, such as:", gap_after=5)
g.bullets([
    "Smoothie - with one frozen banana and a small handful of other "
    "fruit (berries, mango etc.), Greek yoghurt, choice of milk, "
    "protein powder (useful if using dairy free milk/yoghurt), add any "
    "other superfoods, just be mindful of portions.",
    "Eggs - omelette, poached eggs, scrambled eggs, with mushrooms, "
    "tomatoes, avocado or any veg essentially.",
    "Greek yoghurt - with berries or in a choc chia pudding.",
])
g.paragraph("Get creative - Try to make these combinations more "
            "interesting, just remove the carbohydrate component.")

g.keep_together(190)
g.heading([[("High Protein / ", False), ("Low Carb Snacks", True)]])
g.bullets(SNACKS)

g.section_label("Lunch and Dinner")
g.paragraph("Instead of using the regular Nutrition Formula daily "
            "structure of low carbohydrate/high carbohydrate or "
            "medium/medium carbohydrate, the lunch and dinner meals "
            "should both be low carbohydrate and high protein. When "
            "both meals are low carbohydrate, however, it is important "
            "to note that this is not about restriction or having a "
            "small meal.")
g.paragraph("It is important to note that low carbohydrate does not "
            "mean no carbohydrate - rather reducing the amount of "
            "carbohydrates by reducing the portion of the additional "
            "carbohydrate element (pasta, regular potatoes, sweet "
            "potatoes, couscous, rice, grains, bread, wraps, pita "
            "bread, naan bread etc.). Carbohydrates will still be "
            "present in the fruits and vegetables in the meal.")

g.keep_together(440)
g.paragraph("This will look like the following:", gap_after=2)
g.diagram_title("How To Build A Low Carb Meal")
g.diagram("booster-plate")
g.bullets([
    "STEP 1: Fill 3/4 of your plate with vegetables and fruits",
    "STEP 2: Fill 1/4 of your plate with lean protein",
    "STEP 3: Add a small portion of healthy fats",
], bold_prefix=True)

g.keep_together(200)
g.coral_heading("The daily structure for fat loss booster:", size=20)
g.matrix_table(MEALS, [
    ("Structure", ["Breakfast (high protein / low carb)",
                   "A portion of fruit / vegetables",
                   "High protein / lower carb lunch",
                   "Bigger snack (high protein low carb)",
                   "High protein / lower carb dinner",
                   "A portion of fruit / vegetables"]),
], label_header="")

g.keep_together(200)
g.coral_heading("An example of this daily structure for 5 days would be "
                "the following:", size=20)
g.matrix_table(MEALS, [
    ("1", ["Pina Colada Smoothie", "Small handful of grapes",
           "Pesto & Roasted Veg Omelette Wrap",
           "Apple Slices With 1 TBSP Peanut Butter",
           "Chicken Gyros & Tzatziki", "1 pear"]),
    ("2", ["Berry & Peanut Butter Thickshake", "1 orange",
           "Vegetable Curry Soup", "2 Boiled Eggs",
           "Halloumi & Mediterranean Vegetable Medley",
           "Small handful of blueberries"]),
    ("3", ["Green Smoothie Bowl", "Small handful of blueberries",
           "Green Shakshuka", "Small Handful Of Nuts",
           "Turkey Stuffed Peppers (Bell Peppers)", "1 apple"]),
    ("4", ["Fruit Salad & Yoghurt", "1 pear", "Prawn Marie Rose Salad",
           "1 Sliced Banana Topped With 1 TBSP Nut Butter",
           "Greek Frittata", "1 orange"]),
    ("5", ["Mango & Passionfruit Smoothie Bowl", "1 apple",
           "Cheats Tomato Soup", "Celery Sticks & Cream Cheese",
           "Salmon & Egg Bake", "Small handful of grapes"]),
], label_header="Day")
g.note("* See fat loss booster meal guide for recipes")

g.keep_together(540)
g.coral_heading("An example of this daily structure for 5 days for a "
                "vegetarian would be the following:", size=20)
g.matrix_table(MEALS, [
    ("1", ["Pina Colada Smoothie", "Small Handful Of Grapes",
           "Pesto & Roasted Veg Omelette Wrap", "2 Boiled Eggs",
           "Vegetable Stuffed Peppers (Bell Peppers)", "1 Pear"]),
    ("2", ["Berry & Peanut Butter Thickshake", "1 Orange",
           "Vegetable Curry Soup", "Chocolate Chia-Pudding",
           "Veggie Crustless Quiche", "Small Handful Of Blueberries"]),
    ("3", ["Green Smoothie Bowl", "Small Handful Of Blueberries",
           "Mini Eggplant Pizzas and Salad", "Small Handful Of Nuts",
           "Feta & Egg Bake", "1 Apple"]),
    ("4", ["Fruit Salad & Yoghurt", "1 Pear", "Quorn Maire Rose Salad",
           "Apple Slices With 1 Tbsp Peanut Butter",
           "Halloumi & Mediterranean Vegetable Medley", "1 Orange"]),
    ("5", ["Mango & Passionfruit Smoothie Bowl", "1 Apple",
           "Cheats Tomato Soup", "Celery Sticks & Cream Cheese",
           "Greek Frittata", "Small Handful Of Grapes"]),
], label_header="Day")
g.note("* See fat loss booster meal guide for recipes")

g.section_label("Vegetables")
g.paragraph("As outlined above, the meal structure for the fat loss "
            "booster should follow a low carbohydrate lunch and low "
            "carbohydrate dinner for 3-5 days. During this time it is "
            "even more important to include plenty of vegetables at "
            "lunch and dinner. The recommendation is to fill 3/4 of the "
            "plate with a variety of vegetables (and fruits) when "
            "balancing a low carbohydrate meal along with a portion of "
            "lean protein.")
g.paragraph("Remember that legumes and beans will count towards the "
            "carbohydrate content of a meal so opt for protein sources "
            "such as lean meat, fish, yoghurt, eggs, protein powders, "
            "milk, cheese, tofu, and tempeh.")

g.section_label("Snacks")
g.paragraph("Aim to have high protein snacks during the day rather than "
            "high carbohydrate options.")
g.keep_together(250)
g.coral_heading("Some examples of high protein snacks include:", size=18)
g.bullets(SNACKS)

g.save({
    "title": "Fat Loss Booster",
    "author": "The Weight Loss Academy",
    "subject": "The Fat Loss Booster for breaking a weight loss plateau",
    "keywords": "fat loss, booster, plateau, weight loss, high protein",
    "creator": "The Weight Loss Academy",
})
