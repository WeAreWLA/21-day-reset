#!/usr/bin/env python3
"""Shift & Sustain — Fat Loss Booster Recipe Guide (Regular) — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "Fat-Loss-Booster-Recipe-Guide-Regular.pdf")

RECIPES = {
    1: [
        ("Pina Colada Smoothie", 1,
         ["¼ banana",
          "80g (⅓ cup)(3 oz) pineapple chunks, canned or fresh",
          "150ml (⅔ cup)(5 fl oz) coconut milk (carton not canned)",
          "1 tbsp of Full fat Greek yoghurt (0.75 Aus tbsp -15ml)",
          "Few ice cubes"],
         ["Combine all ingredients in a blender.",
          "Blend until smooth around 1 minute. Serve immediately."],
         "Advance prep - Freeze some ice cubes"),
        ("Pesto and Roasted Veg Omelette Wrap", 1,
         ["½ red onion", "½ red pepper (bell pepper)",
          "8 slices courgette (zucchini)", "5 mushrooms",
          "Dash of black pepper", "½ tsp mixed herbs",
          "1 heaped tsp pesto", "2 eggs",
          "15ml (1 tbsp) milk (0.75 Aus tbsp -15ml)", "1 tsp of butter",
          "30g (¼ cup)(1 oz) cheddar cheese, grated",
          "1 tsp olive oil (optional)"],
         ["Preheat the oven at 180 degrees Celsius (350 degrees "
          "Fahrenheit/Gas Mark 4).",
          "In a bowl add the sliced vegetables, season with black "
          "pepper, mixed herbs and add pesto (add a little drop of "
          "olive oil if a bit dry).",
          "Line a baking tray with baking paper and place the "
          "vegetables on it spaced out.",
          "Roast in the oven for around 30 mins.",
          "In the meantime prepare the omelette wrap. Beat the eggs "
          "and milk in a bowl, season.",
          "Add some butter to a non stick pan and once melted, pour "
          "on the egg mixture.",
          "Heat for 2 minutes until the egg solidifies, then turn over.",
          "Bake the other side for ½ minute (can also do the other "
          "side under the grill if can't flip).",
          "Once the omelette is cooked place on a plate and add the "
          "roasted vegetables and top with grated cheese.",
          "Roll up the omelette as a wrap and cut in half."], None),
        ("Chicken Gyros and Tzatziki", 1,
         ["1 tsp olive oil", "½ tsp cumin seeds",
          "½ tsp coriander (cilantro)", "½ tsp oregano",
          "½ tsp garlic powder", "½ tsp cinnamon",
          "½ tsp paprika powder", "1 large or 2 small chicken thighs",
          "½ onion", "6 cherry tomatoes", "7 slices of cucumber",
          "5 olives (optional)", "5 cubes of feta cheese",
          "30g (1 cup)(1 oz) rocket leaves (arugula)",
          "1 tsp lemon juice",
          "1 tbsp of tzatziki (0.75 Aus tbsp -15ml)"],
         ["Preheat oven at 180 degrees Celsius (350 degrees "
          "Fahrenheit/Gas Mark 4).",
          "In a bowl add some olive oil, cumin, coriander (cilantro) , "
          "oregano, garlic powder, cinnamon and paprika powder.",
          "Mix around then add this marinade onto your chicken thighs.",
          "You can leave the chicken thighs overnight in the fridge "
          "for the flavours to really infuse but if you don't have "
          "time just cook straight away.",
          "Pop the thighs onto a baking tray and pop into the oven "
          "until cooked.",
          "In the meantime prepare the Greek salad, once it's ready "
          "squeeze some lemon juice on top. Leave salad in fridge "
          "until chicken thighs are ready.",
          "When ready, serve all together with a spoon of tzatziki "
          "and enjoy!"],
         "Advance prep - chicken can be marinated overnight"),
    ],
    2: [
        ("Berry and Peanut Butter Thickshake", 1,
         ["240ml (1 cup)(8 fl oz) milk",
          "1 tbsp of Full fat Greek yoghurt (0.75 Aus tbsp -15ml)",
          "3 tbsp frozen mixed berries (2.25 Aus tbsp -45ml)",
          "1 tsp of peanut butter", "½ tsp of cinnamon"],
         ["Add all ingredients into a blender and whizz until smooth, "
          "then enjoy!"], None),
        ("Vegetable Curry Soup", 1,
         ["1 tsp olive oil", "½ small onion, diced",
          "½ tsp ginger, ground", "½ clove garlic, crushed",
          "1 medium carrot, peeled and grated",
          "½ red pepper (bell pepper)",
          "5 slices courgette (zucchini)", "1 tsp curry powder",
          "200ml (¾ cup) (7 fl oz) water",
          "½ stock cube, low sodium",
          "1 medium or 6 cherry tomatoes, chopped",
          "1 tbsp (0.75 Aus tbsp - 15ml) full-fat Greek yoghurt"],
         ["In a large pot, heat oil and sauté the onion. Add the "
          "ginger and garlic then continue for 2-3 more minutes.",
          "Add the peeled and grated carrot and sauté for about 2 "
          "minutes, stirring occasionally. Add the chopped pepper "
          "(bell pepper) and courgette (zucchini). Cook the "
          "vegetables for about 5 minutes, season with curry powder "
          "and mix well.",
          "Pour in the water, stock cube and bring to a boil. Cook "
          "covered for about 10 minutes until the vegetables are "
          "soft. In the meantime, add the chopped tomatoes. Season "
          "with any extra herbs/spices",
          "Once vegetables are cooked, take off from heat and blend "
          "using a hand blender. Season for taste, mix well and serve "
          "with a dollop of yoghurt."],
         "Serve with a side portion of protein of your choice."),
        ("Halloumi and Mediterranean Vegetable Medley", 1,
         ["80g (½ cup)(3 oz) courgette (zucchini)", "1 red onion",
          "5 mushrooms", "½ red pepper (bell pepper)",
          "80-100g (2½ -3½ oz)(1 large) potato",
          "Black pepper for seasoning", "1 tsp olive oil",
          "½ tsp of paprika", "1 tsp of mixed herbs",
          "70g (½ cup)(2½ oz) halloumi", "6 cherry tomatoes"],
         ["Preheat oven at 180 degrees Celsius (350 degrees "
          "Fahrenheit/Gas Mark 4). Slice all vegetables.",
          "Add to a bowl (minus the tomatoes), season, add olive oil, "
          "paprika and mixed herbs.",
          "Mix around to ensure everything is coated. Line a baking "
          "tray with baking paper, add the vegetables.",
          "Spread out over the tray.",
          "Pop into the oven and roast for 15 minutes. Take out, mix "
          "around.",
          "Add the halloumi and tomatoes onto the tray (ensure the "
          "halloumi is seasoned).",
          "Pop back into the oven and roast for a further 15-20 "
          "minutes.",
          "Turn the halloumi over half way through cooking.",
          "When ready, serve on a plate.",
          "Could add a tbsp of hummus or coleslaw to meal when "
          "serving."], None),
    ],
    3: [
        ("Green Smoothie Bowl", 1,
         ["180ml (¾ cup)(6 fl oz) milk", "1 frozen banana",
          "Handful frozen mango", "Handful frozen kale",
          "2 tbsp Greek yoghurt (1.5 Aus tbsp -30ml)", "1 tsp honey",
          "1 sliced strawberry", "6 raspberries",
          "1 tsp sunflower seeds", "1 tsp flaxseed"],
         ["Begin by adding the milk, banana, mango, kale, yoghurt and "
          "honey into a blender and whizz for a few minutes.",
          "Once it's all smooth, transfer into a bowl and add the "
          "remaining ingredients on top."], None),
        ("Green Shakshuka", 1,
         ["2 tsp olive oil", "½ onion, diced", "1 clove garlic, minced",
          "½ tsp ground cumin", "Salt to taste", "2 handfuls spinach",
          "½ handful parsley", "2 tbsp milk (1.5 Aus tbsp -30ml)",
          "½ tbsp harissa paste (7.5ml)", "Black pepper to taste",
          "½ green pepper (bell pepper), sliced",
          "75g (½ cup)(2½ oz) green peas, frozen", "2 eggs",
          "Salt and pepper to taste"],
         ["Heat half of the oil in a frying pan over medium heat, and "
          "sauté the onions and garlic until soft.",
          "Season with cumin and salt to taste, then cook for another "
          "2 mins.",
          "Next, transfer the onion into a food processor along with "
          "the spinach, parsley, milk and harissa paste.",
          "Season with freshly ground black pepper, and blend until "
          "smooth.",
          "Using the same pan as earlier, heat the remaining oil and "
          "fry the pepper (bell pepper) for about 5 minutes, until "
          "charred.",
          "Next, pour in the spinach sauce and add the peas. Cook for "
          "about 5 minutes until peas are defrosted.",
          "Make 2 pockets in the sauce and break an egg in each one. "
          "Cook for another 10 minutes, or until the eggs are set.",
          "Cover with a lid to speed up the process. Serve seasoned "
          "with salt and freshly ground black pepper."], None),
        ("Turkey Stuffed Peppers (Bell Peppers)", 1,
         ["½ onion, diced", "1 tsp olive oil",
          "100g (½ cup) (3½ oz) turkey mince", "Black pepper",
          "1 tsp paprika", "½ tsp oregano", "2 cups spinach leaves",
          "1 tsp tomato puree (tomato paste)",
          "1 tin chopped tomatoes", "1 medium red pepper (bell pepper)",
          "30g (⅓ cup) (1 oz) cheddar cheese, grated"],
         ["Preheat oven to 180°C / 350°F / Gas Mark 4.",
          "In a pan add the onion, olive oil and turkey mince.",
          "Continue to cook on a medium heat for 10 minutes.",
          "Season with black pepper, add in paprika powder, oregano, "
          "spinach, tomato puree (tomato paste) and tinned tomatoes.",
          "Allow to cook for a further few minutes.",
          "Taste test and add more seasoning if needed.",
          "In the meantime remove the middle of the red pepper (bell "
          "pepper) and remove the top.",
          "Spoon in the turkey mixture, top with cheese and pop into "
          "the oven for 15 minutes or until the pepper (bell pepper) "
          "is soft (but still has a bite).",
          "Serve with any salad or veggies on the side."], None),
    ],
    4: [
        ("Fruit Salad & Yoghurt", 1,
         ["100g (¾ cup) (3½ oz) fruit salad made from fruit of your "
          "choice",
          "125g (½ cup) (4½ oz) full-fat Greek yoghurt"],
         ["Chop up fruit into bite size chunks and place in a bowl."],
         None),
        ("Prawn Marie Rose Salad", 1,
         ["1 tbsp of mayonnaise (0.75 Aus tbsp -15ml)",
          "1 tbsp of Greek yoghurt (0.75 Aus tbsp -15ml)",
          "½ tsp of paprika", "Black pepper for seasoning",
          "Juice of ½ lemon",
          "1 tbsp of Worcestershire sauce (0.75 Aus tbsp -15ml)",
          "½ tsp of tabasco (optional)",
          "140g (1⅓ cups)(5¼ oz) cooked Prawns (Shrimps)",
          "Bowl of iceberg lettuce", "6 slices of cucumber",
          "1 tomato, sliced", "½ avocado, sliced"],
         ["Add the mayo and yoghurt to a bowl along with paprika, "
          "black pepper, lemon juice, Worcestershire sauce and "
          "tabasco.",
          "Mix around.",
          "Add the cooked prawns (shrimps) to the sauce and mix so "
          "all the prawns (shrimps) are coated in sauce.",
          "Prepare salad - add lettuce to a bowl. Then top with "
          "cucumber, tomatoes and avocado.",
          "Add the prawns (shrimps) on top and then serve."], None),
        ("Greek Frittata", 1,
         ["1 tbsp olive oil (0.75 Aus tbsp -15ml)",
          "½ red onion, sliced", "Bowl of spinach leaves", "2 eggs",
          "Black pepper", "30g (¼ cup)(1 oz) feta cheese, crumbled",
          "1 tomato, chopped", "6 olives (optional)",
          "Side salad ingredients"],
         ["Add the olive oil to a frying pan along with the sliced "
          "onions and sauté for a few minutes.",
          "Add the spinach leaves and allow to wilt. Crack the eggs "
          "into a bowl add some black pepper to season.",
          "In a bowl add the eggs and black pepper. Beat the eggs, "
          "then add in the crumbled feta, chopped tomato and mix.",
          "Pour the egg mixture into the pan ensuring all ingredients "
          "are evenly spread out.",
          "Stir gently once or twice, then cook over a low heat for "
          "8-10 mins until almost set.",
          "Heat the grill to high. Transfer to under the grill for "
          "3-5 mins until set on top.",
          "Make simple side salad (adding the optional olives) and "
          "serve with the frittata."], None),
    ],
    5: [
        ("Mango and Passionfruit Smoothie Bowl", 1,
         ["1 frozen banana", "70g (½ cup)(2½ oz) frozen mango",
          "3 tbsp full fat Greek yoghurt (2.25 Aus tbsp -45ml)",
          "120ml (½ cup)(4 fl oz) milk", "1 passion fruit",
          "2 tbsp muesli (granola), no added sugar (1.5 Aus tbsp "
          "-30ml)"],
         ["Add the banana, mango and Greek yoghurt into a blender "
          "(add only a little of the milk first to ensure you get the "
          "right consistency, seeking thick consistency) and whizz "
          "around.",
          "Add a bit more milk if too thick, then continue to whizz "
          "until everything is smoothly blended and thick.",
          "Pour into a bowl and top with passion fruit and muesli "
          "(granola)"],
         "Advance prep - freeze the banana"),
        ("Cheats Tomato Soup", 1,
         ["1 tsp unsalted butter",
          "½ onion, peeled and finely chopped", "1 tsp plain flour",
          "½ stock cube, low sodium, vegetable",
          "100ml (½ cup) (3½ fl oz) boiling water",
          "200g (1 cup) (7 oz) tinned chopped tomatoes",
          "1 tsp tomato puree (tomato paste)", "Black pepper",
          "1 tsp pesto"],
         ["Melt the butter in a pot, add the onion and cook over a "
          "low heat for 10 minutes or until the onion is soft.",
          "Sprinkle the flour over the onion, stir well, then crumble "
          "in the stock cube and 100ml of boiling water, tinned "
          "tomatoes, tomato puree (tomato paste) and pepper.",
          "Bring to the boil then reduce the heat and simmer for 2-3 "
          "minutes, stirring occasionally.",
          "Leave to cool slightly and blend carefully with a stick "
          "blender - be extremely careful not to splash yourself with "
          "hot soup.",
          "Swirl pesto into soup before serving."],
         "Serve with a side portion of protein of your choice."),
        ("Salmon & Egg Bake", 1,
         ["1 small salmon fillet (approx. 110g (3 ¾ oz))",
          "Black pepper", "2 tsp olive oil", "½ clove garlic",
          "3 spears broccoli", "½ tsp oregano", "½ tsp thyme",
          "1 egg and 1 egg white",
          "100ml (½ cup) (3½ fl oz) semi-skimmed milk", "½ onion",
          "½ red pepper (bell pepper)"],
         ["Preheat oven to 215°C / 420°F / Gas Mark 7. Season the "
          "salmon fillets with pepper.",
          "Heat 1 tsp. of oil in a pan over high heat, and fry the "
          "salmon fillets skin side up for about 2 minutes, then "
          "place on a baking tray, place in the oven and cook for "
          "another 8 minutes. Remove from the oven and set aside.",
          "Preheat oven to 180°C / 350°F / Gas Mark 4.",
          "In the same pan, add the remaining 1 tsp. of oil and cook "
          "the garlic and broccoli, on medium heat for 5 minutes. "
          "Season oregano and thyme, and mix well.",
          "Whisk together the egg, egg white and milk.",
          "Flake the baked salmon into a baking dish, add the chopped "
          "onion and chopped pepper (bell pepper), then pour in the "
          "egg mixture.",
          "Bake for 30-35 minutes or until eggs are set and browned."],
         None),
    ],
}

OVERVIEW = [
    ("Day 1", ["Pina Colada Smoothie",
               "Pesto and Roasted Veg Omelette Wrap",
               "Chicken Gyros and Tzatziki"]),
    ("Day 2", ["Berry and Peanut Butter Thickshake",
               "Vegetable Curry Soup",
               "Halloumi and Mediterranean Vegetable Medley"]),
    ("Day 3", ["Green Smoothie Bowl", "Green Shakshuka",
               "Turkey Stuffed Peppers (Bell Peppers)"]),
    ("Day 4", ["Fruit Salad & Yoghurt", "Prawn Marie Rose Salad",
               "Greek Frittata"]),
    ("Day 5", ["Mango and Passionfruit Smoothie Bowl",
               "Cheats Tomato Soup", "Salmon & Egg Bake"]),
]

g = Guide(OUT)

g.cover(
    "SHIFT & SUSTAIN", "THE WEIGHT LOSS ACADEMY",
    [("Fat Loss Booster", "lbi", NAVY),
     ("Recipe Guide", "lb", BLUSH),
     ("Regular.", "lbi", NAVY)],
    "Fifteen simple recipes for the Fat Loss Booster.",
)

g._new_content_page()
g.heading([[("Recipe ", False), ("Overview", True)]])
g.matrix_table(["Breakfast", "Lunch", "Dinner"], OVERVIEW,
               label_header="", size=10.5)

for day in range(1, 6):
    g.divider(f"Day {day}", "Recipes")
    for title, serves, ingr, instr, note in RECIPES[day]:
        g.recipe(title, serves, ingr, instr, note=note)

g.save({
    "title": "Fat Loss Booster Recipe Guide - Regular",
    "author": "The Weight Loss Academy",
    "subject": "Recipes for the Fat Loss Booster",
    "keywords": "recipes, fat loss, booster, weight loss",
    "creator": "The Weight Loss Academy",
})
