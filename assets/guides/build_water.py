#!/usr/bin/env python3
"""The Importance Of Water — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "The-Importance-Of-Water.pdf")

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("The", "lbi", NAVY),
     ("Importance", "lb", BLUSH),
     ("Of Water.", "lbi", NAVY)],
    "Why water matters, how much you need, and simple ways to drink more.",
)

# ---- The Function of Water
g._new_content_page()
g.heading([[("The Function of", False)], [("Water ", False),
                                          ("in the Body", True)]])
g.paragraph("About two thirds of the body is water and all the organs, "
            "tissues and fluids in the body contain water as an "
            "essential constituent.")
g.paragraph("For the human body, water is a vital resource. We know it "
            "is indispensable for life itself, and it provides a host "
            "of essential functions for good health. There is no more "
            "important nutrient in our bodies than water. It is the "
            "most widely used nutrient at work within the body's "
            "functions and processes, as well as constituting a huge "
            "part of its physical makeup.")
g.coral_heading("Main Functions of Water", size=20)
g.bullets([
    "Regulates appetite",
    "Supports digestion, excretion, absorption & circulation",
    "Increases energy levels",
    "Aids with elimination of toxic waste",
    "Decreases water retention",
    "Helps to reduce blood pressure",
    "Supports a healthy body temperature",
    "Transporting nutrients around the body",
])

# ---- Water Balance
g.heading([[("Water ", False), ("Balance", True)]])
g.paragraph("The body maintains water balance by two main methods:")
g.bullets([
    "Regulating water loss: Water loss is regulated by regulating the "
    "excretion by the kidneys. Water is continually being lost from "
    "the body, in urine, sweat and water vapour in the gases expelled "
    "in respiration. Under usual climatic conditions and without "
    "physical activity the minimal fluid loss from sweat and breathing "
    "is about 500ml water daily. Another 200-300ml is lost from stools "
    "and it is necessary to pass at least 750ml of urine to keep the "
    "kidneys functioning and being able to remove toxic waste.",
    "Regulating water intake: Water intake is increased by the "
    "sensation of thirst. If the body is to function optimally, the "
    "water that is lost must be replaced. As the body is constantly "
    "losing water, the amount being lost varies greatly due to "
    "environmental factors, activity, factors in food and drink, drug "
    "effects etc. Water should be consumed regularly throughout the "
    "day so it does not overload the kidneys.",
], bold_prefix=True)
g.keep_together(330)
g.diagram("water-balance", max_w=340)

# ---- Water Sources
g.heading([[("Water ", False), ("Sources", True)]])
g.paragraph("The following are sources of fluid:", gap_after=5)
g.bullets([
    "Tap water",
    "Still / sparkling water",
    "Non-caffeinated herbal tea",
    "Milk (be mindful of the consumption of large quantities of milk - "
    "1 cup or milky drink per day is fine)",
    "Caffeine and decaffeinated drinks (do not go towards overall water "
    "intake. Caffeinated drinks may have a diuretic effect on the body "
    "in some people, which leads to dehydration)",
])
g.paragraph("Dietary water can come from the water contained in food as "
            "well as from drinks, for example in fruit and vegetables, "
            "soups and stews. It is estimated that foods contribute to "
            "about 20% of total fluid intakes. Fruits and vegetables "
            "that are particularly high in water include:")
g.keep_together(420)
g.coral_heading("Fruits & Vegetables as Water Sources", size=18)
g.select_table(
    ["Fruit or Vegetable", "% Water Content"],
    [
        ["Cucumber", "Tomatoes", "Spinach", "Mushrooms", "Melon",
         "Broccoli", "Oranges", "Blueberries"],
        ["96", "95", "93", "92", "91", "90", "86", "85"],
    ],
)

# ---- Recommended Water Intake
g.heading([[("Recommended", False)], [("Water ", False),
                                      ("Intake", True)]])
g.paragraph("General guidance suggests that around 8 glasses or around "
            "1500ml - 2000ml is the minimum amount of water a person "
            "should consume per day.")
g.paragraph("Consume 1-1.5ml of water for each calorie expended daily. "
            "For example: if your daily expenditure (BMR x activity "
            "level) is 2000kcal per day, then you would require 2-3 "
            "litres per day.")
g.paragraph("However, it is important to note - this amount varies "
            "greatly between individuals (physical activity and "
            "climate) and also due to body size. Larger people must "
            "consume more water because they have greater skin area, "
            "so lose more water through sweating.")

g.coral_heading("Tips for increasing water intake", size=20)
TIPS = [
    ("Get a pretty reusable water bottle",
     "Keeping a water bottle handy can serve as a visual reminder to "
     "drink more water. If the bottle is on the desk or table, it will "
     "be a constant reminder to drink more. It can also be challenging "
     "to drink enough water when travelling or on the go. Fill a water "
     "bottle before leaving home, and bring it along on daily travels. "
     "Plus, it is better for the environment than relying on "
     "single-use plastic water bottles."),
    ("Add water to a daily routine",
     "Make drinking water a habit by drinking at set points during the "
     "day, e.g. as soon as waking up, drink with a meal, drink while "
     "at the computer or watching TV, etc. Sipping on water "
     "consistently throughout the day is another easy way to help meet "
     "fluid goals."),
    ("Make it fruity",
     "If the flavour of water is not appealing or a bit of flavour is "
     "needed to help drink more, there are many choices. Adding fruit "
     "to water can give that lovely fruity hint. For a citrus kick try "
     "lemons, limes and oranges or stick to the classic cucumber, "
     "watermelon or kiwi and strawberries. The combinations are "
     "endless. Feeling adventurous, why not have a play with adding "
     "some fresh herbs such as mint!"),
    ("Eat water",
     "One simple way to get more water is to eat more foods that are "
     "high in water. Fruits and vegetables that are particularly high "
     "in water include lettuce, celery, cucumber, watermelon and "
     "grapefruit. In addition to their high fluid content, these "
     "fruits and vegetables are packed with vitamins, minerals, and "
     "antioxidants that promote overall health."),
]
for title, body in TIPS:
    g.keep_together(120)
    g.coral_heading(title, size=14, gap_before=8, gap_after=7)
    g.paragraph(body)

g.bullets([
    "Sparkling water may increase bloating in some people, but can be "
    "included in a healthy lifestyle",
    "Flavoured squash - can be used to improve overall water intake. "
    "The amount could be reduced over time",
    "If cold water is preferred, water can be stored in the fridge or "
    "served with ice cubes",
    "Large amounts of water should be consumed away from meals as it "
    "can increase the fullness feeling",
    "Drinking water regularly over the course of the day is better "
    "than drinking big amounts in one go - it allows the body time to "
    "absorb the water effectively (this may also help with frequent "
    "urination which some ladies get when drinking lots of water in at "
    "the one time)",
    "Water should be consumed throughout the day as thirst can be "
    "mistaken for hunger",
])

# ---- Dehydration
g.keep_together(240)
g.heading([[("Dehydration", True)]])
g.paragraph("Dehydration is when the body does not have as much water "
            "as it needs (i.e. the body is losing more fluids than "
            "taken in).")
g.paragraph("Symptoms of dehydration include feeling thirsty, dark "
            "yellow pee and dizziness.")
g.cards([
    ("1% Dehydration", "We become thirsty with reduced concentration"),
    ("5% Dehydration", "We become hot and tired with reduced performance"),
    ("10% Dehydration", "Delirium and blurred vision"),
    ("20% Dehydration", "May result in death"),
])
g.keep_together(260)
g.diagram("water-urine", max_w=470)
g.paragraph("It is also possible to over consume water, which is not "
            "good for the body as it flushes out nutrients. You are "
            "aiming for pale yellow or straw coloured urine (like "
            "number 1). Clear urine could be an indication that you are "
            "over consuming water.")

g.keep_together(140)
g.coral_heading("Final Note", size=18)
g.paragraph("These general guidelines work very well:", gap_after=4)
g.numbered([
    "When thirsty, drink",
    "When not thirsty anymore, stop",
    "During high heat and exercise, drink enough to compensate for the "
    "lost fluids",
])

g.save({
    "title": "The Importance Of Water",
    "author": "The Weight Loss Academy",
    "subject": "Why water matters for health and weight loss",
    "keywords": "water, hydration, dehydration, health, weight loss",
    "creator": "The Weight Loss Academy",
})
