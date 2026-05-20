#!/usr/bin/env python3
"""The Snack Guide — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "The-Snack-Guide.pdf")

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("The", "lbi", NAVY), ("Snack", "lb", BLUSH),
     ("Guide.", "lbi", NAVY)],
    "Why snacking helps, when to snack, and what to reach for.",
)

# ---- Benefits
g._new_content_page()
g.heading([[("Benefits of", False)], [("Healthy Snacking", True)]])
g.paragraph("For years and years, snacking has come under scrutiny. "
            "Many are confused whether snacking is beneficial to "
            "overall health / weight loss or if it should be avoided. "
            "This has created a stigma on snacks.")
g.paragraph("However, studies have suggested that for most, snacking "
            "throughout the day is recommended for the reasons below.")
g.bullets([
    "Controls appetite throughout the day",
    "Prevents energy dips",
    "Promotes healthy weight loss",
    "Can help improve concentration",
    "Prevents overeating at meal time",
    "Helps stabilise energy levels between meals",
])

# ---- Blood Sugar
g.heading([[("Snacking and", False)], [("Blood Sugar Levels", True)]])
g.paragraph("Snacking is really important as it helps keep blood sugar "
            "levels steady during the day. If food is eaten at regular "
            "intervals throughout the day, having a dip in blood sugar "
            "levels will be less likely and therefore reaching for "
            "less nutrient-dense foods for a kick of energy will not "
            "happen.")
g.paragraph("Snacking is important to bridge the gap between breakfast "
            "and lunch and then lunch and dinner. However, snacks "
            "should not be eaten just for the sake of it, snacking is "
            "supposed to tide the body over until the next meal.")
g.keep_together(380)
g.diagram("snack-bloodsugar", max_w=430)
g.bullets([
    "Peaks after each meal/ snack (think balanced meals)",
    "Small peaks and troughs",
    "Blood sugar levels dip = signal to eat",
])

# ---- How to Snack
g.heading([[("How to ", False), ("Snack", True)]])
g.bullets([
    "Try to eat more regularly throughout the day to prevent big gaps "
    "between meals",
    "Eat as much fresh fruit and vegetables as liked, but listen to "
    "the body and do not eat just for the sake of it (limit of one "
    "banana per day)",
    "Go for snack/cereal bars with less than 5g of sugar per 100g OR "
    "the least number of ingredients like nakd bars, which have no "
    "added sugar",
    "Go for savoury snacks like plain nuts and seeds, plain popcorn, "
    "lentil crisps or baked vegetable crisps with no added salt",
    "Be mindful of dried fruit, maximum one handful (30g) per day and "
    "nuts/nut butter, maximum one handful (30g) or portion of nuts per "
    "day",
    "Aim to not replace regular meals with snacks, if feeling less "
    "hungry at mealtime prepare a smaller portion of the recipe",
    "Add variety to snacks. For the bigger snack, alternate between "
    "protein-based snacks (boiled eggs, smoothie, Greek yoghurt) or a "
    "carbohydrate-based snack (Nak'd bars, banana bread, crackers with "
    "toppings)",
])

# ---- Snacking System
g.heading([[("Snacking ", False), ("System", True)]])
g.paragraph("Eating more regularly throughout the day prevents large "
            "intervals between meals, which could positively impact "
            "appetite and cravings. It is recommended to have three "
            "meals per day, breakfast, lunch and dinner, along with "
            "2-3 healthy snacks in between. For most, eating every "
            "two-three hours works best.")
g.paragraph("Generally, that looks like this:", gap_after=4)
g.list_table(None, [
    "Breakfast",
    "A small snack - a single portion of fruit or veg",
    "Lunch",
    "A bigger snack - anything bigger than a single portion of fruit "
    "or veg",
    "Dinner",
    "A small or bigger snack, depending on hunger levels",
])
g.paragraph("Some people may have these meals in a different order; "
            "perhaps having the dinner meal in the middle of the day, "
            "so may keep the bigger snack for the evening. Or if "
            "working shifts, having dinner before going to work and "
            "keeping the bigger snack for the middle of the night. The "
            "timing does not matter as long as the recommendation to "
            "eat regularly is followed, in response to actual physical "
            "hunger and not eating snacks just because “allowed”.")

# ---- Small Snacks
g.heading([[("Small ", False), ("Snacks", True)]])
g.paragraph("This is the snack that most people would have to tide "
            "them over between breakfast and lunch. A small snack is a "
            "single portion of fruit or veg e.g an apple or a handful "
            "of carrot sticks.")
g.paragraph("Eat as much fruit and vegetables as you like, there is no "
            "set amount but aim for one portion each time. Listen to "
            "your body and try not to eat just for the sake of it. It "
            "is important to still intuitively consume these foods "
            "like all foods. Eat when hungry. It is not advised to "
            "over-consume any food - even healthy options.")
g.paragraph("Once something else is added to this, say a teaspoon of "
            "peanut butter or hummus, it becomes a bigger snack. So "
            "anything larger than a single portion of fruit or "
            "vegetables is a bigger snack.")
g.keep_together(150)
g.coral_heading("Fruit and Vegetables Snack Inspiration", size=21)
g.select_table(None, [
    ["Strawberries", "Cucumber", "Carrots", "Celery", "Peppers",
     "Mandarins", "Pears", "Raspberries", "Blueberries", "Broccoli",
     "Cauliflower", "Tomatoes", "Radishes"],
    ["Cranberries (fresh)", "Kiwi", "Pears",
     "1 banana (no more than 1 per day)", "1 Grapefruit",
     "1 large orange", "1 cup of grapes", "1 cup of pineapple",
     "1 cup of sugar snap peas", "Apples", "Peas", "Aubergine",
     "Onions"],
    ["Bok Choy", "Watercress", "Courgette", "Kelp", "Plums",
     "Blackberries", "Asparagus", "Spinach", "Beetroot", "Mushrooms",
     "Pomegranate", "Melon"],
])

# ---- Bigger Snacks
g.heading([[("Bigger ", False), ("Snacks", True)]])
g.paragraph("We also recommend bigger snacks. With regards to "
            "“bigger” snacks, some women may only need one "
            "per day and others more. If you exercise intensively "
            "(running, gym workout, HIIT training etc.) regularly you "
            "may need more compared to someone that is less mobile.")
g.paragraph("It is recommended to have a bigger snack between lunch "
            "and dinner, this will prevent sugar cravings and support "
            "your appetite until dinner. You may require another snack "
            "in the evening. Some days you may need 2 bigger snacks "
            "and some days, 1. Tune in and be flexible based on how "
            "you feel.")
g.keep_together(200)
g.coral_heading("Bigger Snack Inspiration", size=21)
g.list_table(None, [
    "3 crackers with nut butter. cream cheese, cottage cheese, "
    "hummus, avocado, cheddar or tuna",
    "1 natural cereal bar of your choice (Nakd brand is a healthy "
    "option)",
    "Apple slices with 1 tablespoon of nut butter",
    "Small handful of nuts and raisins",
    "1 banana sliced and topped with 1 tablespoon of nut butter",
    "2 medjool dates and cream cheese or nut butter",
    "1 cup of grapes and 1 boiled egg",
    "2 boiled eggs",
    "30g dark chocolate",
    "1 cups of homemade popcorn",
    "125g of Greek yoghurt and fruit",
])

# ---- High Protein / Low Carb Snacks
g.heading([[("High Protein / Low Carb", False)], [("Snacks", True)]])
g.list_table(None, [
    "Smoothie", "2 Eggs", "Greek Yoghurt (125G) with berries",
    "Egg muffins", "Apple slices with 1 tbsp peanut butter",
    "Small handful of nuts", "Celery sticks and cream cheese",
    "Chocolate chia-pudding", "Any type of meat/fish",
])
g.paragraph("An important note is to have a good variety across meals "
            "and snacks, do not have a smoothie for a snack if having "
            "one for breakfast. The same goes for eggs, it is okay to "
            "have them as a snack if not having eggs at "
            "breakfast/lunch.")

# ---- Final Note
g.keep_together(200)
g.heading([[("Final ", False), ("Note", True)]])
g.paragraph("The snacking system is a guide, some people may need to "
            "consume another bigger snack in the evening before bed if "
            "they are hungry. It is important to remember to check in "
            "for physical hunger and that physical hunger should never "
            "be ignored.")
g.paragraph("For some, having the larger snack is most beneficial "
            "between lunch and dinner in the afternoon as this period "
            "is the longest window between meals. However, it may "
            "differ depending on the individual circumstances, taking "
            "into account physical activity and hunger levels.")
g.paragraph("It is important to feel satisfied by what foods are being "
            "consumed, so remember to check in with hunger and "
            "fullness levels. Also remember, these are guidelines and "
            "often people may need a little more or less. Larger "
            "people require more food than those who are smaller.")

g.save({
    "title": "The Snack Guide",
    "author": "The Weight Loss Academy",
    "subject": "Healthy snacking for weight loss",
    "keywords": "snacks, snacking, blood sugar, weight loss, nutrition",
    "creator": "The Weight Loss Academy",
})
