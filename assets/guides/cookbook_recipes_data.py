"""Recipe data for The WLA Weight Loss Cookbook.

Each recipe is a dict with: section, title, tagline, serves, time,
ingredients (list of strings or sub-section tuples),
to_serve (optional list), instructions (list of strings), note (optional).

Sections (order in the cookbook):
  1. Breakfast & Lunch
  2. Slow Cooker
  3. Traybakes
  4. Bowls
  5. Pasta & Comfort Dinners
"""

RECIPES = [
    # ============================== BREAKFAST & LUNCH
    {
        "section": "Breakfast & Lunch",
        "title": "Nutty Chocolate Baked Oats",
        "tagline": "Cosy, chocolatey, and made for slow mornings.",
        "serves": 4,
        "time": "55 mins",
        "image": "nutty-chocolate-baked-oats.jpg",
        "ingredients": [
            "½ tsp butter",
            "90g porridge oats",
            "1 tsp baking powder",
            "½ tsp cinnamon",
            "1 egg",
            "175ml milk (of your choice)",
            "1 large banana, mashed",
            "3 tsp maple syrup",
            "1 tbsp nut butter (peanut or almond)",
            "3 tbsp flaxseeds",
            "60g walnuts, finely chopped",
            "2 heaped tbsp dark chocolate chips",
        ],
        "to_serve": [
            "1–2 tbsp full-fat Greek yoghurt",
            "Portion of fruit of your choice (handful of berries, "
            "1 banana, etc.)",
        ],
        "instructions": [
            "Preheat the oven to 180°C and grease a baking dish with "
            "butter.",
            "Add the oats, baking powder and cinnamon to a bowl.",
            "In a separate bowl, whisk together the egg, milk, mashed "
            "banana, maple syrup and nut butter until well combined.",
            "Combine the wet and dry ingredients and fold in the "
            "flaxseeds, walnuts and chocolate chips. Reserve a few "
            "walnuts and chocolate chips for topping.",
            "Pour the mixture into the prepared baking dish. "
            "Sprinkle over the reserved walnuts and chocolate chips.",
            "Bake for around 45 minutes.",
            "Take out, allow to cool and then slice.",
            "Serve warm or cold, with Greek yoghurt and a portion of "
            "fruit of your choice.",
        ],
        "note": (
            "Makes 4 portions. Store the remainder in the fridge for "
            "up to 5 days. You can also freeze individual portions "
            "for up to 2 months — defrost overnight and serve cold "
            "or warm."
        ),
    },
    {
        "section": "Breakfast & Lunch",
        "title": "Bacon, Leek and Cheese Frittata Salad",
        "tagline": "A protein-packed lunch you can eat hot or cold.",
        "serves": 1,
        "time": "25 mins",
        "image": "bacon-leek-cheese-frittata-salad.jpg",
        "ingredients": [
            "2 slices of bacon",
            "1 tsp olive oil",
            "½ leek, sliced",
            "2 eggs",
            "Black pepper, to taste",
            "½ tsp mixed herbs",
            "30g cheese, grated",
            "Side salad of your choice",
        ],
        "instructions": [
            "Grill the bacon and chop into pieces when cooked. Set "
            "aside.",
            "In a pan, add the olive oil and leek and cook for 3–4 "
            "minutes until softened.",
            "In a bowl, whisk the eggs with black pepper and mixed "
            "herbs. Add the grated cheese, cooked leek and bacon, and "
            "mix well.",
            "Reduce the heat to low and pour the egg mixture into the "
            "pan, ensuring everything is evenly spread.",
            "Cook gently for 8–10 minutes until almost set.",
            "Preheat the grill to high, then place the pan under the "
            "grill for 3–5 minutes until the top is fully set and "
            "lightly golden.",
            "Serve with a simple side salad and enjoy.",
        ],
        "note": (
            "Store in an airtight container in the fridge for up to "
            "2–3 days. Can be enjoyed hot or cold."
        ),
    },

    # ============================== BOWLS
    {
        "section": "Bowls",
        "title": "Harissa Chicken Bowl",
        "tagline": "Smoky, jammy tomatoes and a creamy feta-yoghurt drizzle.",
        "serves": 1,
        "time": "20 mins",
        "image": "harissa-chicken-bowl.jpg",
        "ingredients": [
            "1 tsp olive oil",
            "1 chicken fillet (approx. 100–130g)",
            "6 cherry tomatoes, halved",
            "½ red onion, sliced",
            "½ tsp paprika",
            "½ tsp garlic powder",
            "Black pepper, to taste",
            "1 tbsp harissa paste",
            "1 wholemeal pitta bread",
            "Handful of rocket",
            "½ small avocado (or ¼ of a large avocado)",
            "1 tbsp pickled red onions (optional)",
        ],
        "ingredients_sub": [
            ("For the yoghurt sauce", [
                "1 tbsp Greek yoghurt",
                "1 tsp mayo",
                "½ tsp oregano",
                "30g feta cheese, crumbled",
                "Juice of ¼–½ lemon, to taste",
            ]),
        ],
        "instructions": [
            "Heat the olive oil in a frying pan over a medium heat.",
            "Add the chicken fillet, cherry tomatoes and red onion, "
            "then cook for a few minutes.",
            "Sprinkle over the paprika, garlic powder and black "
            "pepper, then stir through the harissa paste to coat "
            "everything evenly.",
            "Cook for 10–12 minutes, turning the chicken occasionally, "
            "until cooked through and the tomatoes have softened and "
            "become slightly jammy.",
            "While the chicken cooks, make the yoghurt sauce by "
            "mixing together the Greek yoghurt, mayo, oregano, "
            "crumbled feta and lemon juice. Taste and adjust "
            "seasoning if needed.",
            "Warm the wholemeal pitta bread if desired.",
            "Add the harissa chicken mixture to a bowl, then add the "
            "rocket, avocado and pickled red onions (if using). "
            "Serve the pitta bread alongside. Finish with the yoghurt "
            "sauce and serve straight away.",
        ],
        "note": (
            "Store the harissa chicken and yoghurt sauce separately "
            "in airtight containers in the fridge for up to 3 days. "
            "Add the rocket, avocado and pitta bread fresh before "
            "serving for the best texture."
        ),
    },

    # ============================== PASTA & COMFORT DINNERS
    {
        "section": "Pasta & Comfort Dinners",
        "title": "Marry Me Meatballs",
        "tagline": "Creamy, herby meatballs in a sun-dried tomato sauce.",
        "serves": 1,
        "time": "30 mins",
        "image": "marry-me-meatballs.jpg",
        "ingredients": [
            "1 heaped tsp olive oil",
            "4 meatballs (beef, lamb, chicken or vegetarian; homemade "
            "or store-bought)",
            "½ red pepper, thinly sliced",
            "½ red onion, thinly sliced",
            "4 mushrooms, sliced",
            "1 tsp garlic powder",
            "1 tsp dried oregano",
            "1 tsp dried basil",
            "1 tsp paprika or ½ tsp crushed red pepper flakes "
            "(optional)",
            "Pinch of ground black pepper",
            "150ml vegetable stock (low sodium)",
            "3 sun-dried tomatoes, chopped",
            "1 tbsp tomato puree",
            "1 tbsp crème fraîche",
            "1 tbsp parmesan cheese, grated",
            "Fresh basil leaves, to garnish (optional)",
        ],
        "to_serve": [
            "60g wholegrain rice",
            "80g green beans",
        ],
        "instructions": [
            "Heat the olive oil in a large non-stick pan over a "
            "medium heat.",
            "Add the meatballs and cook for 4–5 minutes, turning "
            "occasionally, until lightly browned on all sides. They "
            "don't need to be fully cooked at this stage. Remove "
            "from the pan and set aside.",
            "In the same pan, add the red pepper, red onion and "
            "mushrooms. Cook for 6–7 minutes until softened.",
            "Add the garlic powder, oregano, dried basil, paprika or "
            "chilli flakes and black pepper. Stir and cook for 1–2 "
            "minutes to release the flavours.",
            "Return the meatballs to the pan.",
            "Add the vegetable stock, sun-dried tomatoes and tomato "
            "puree. Stir well and bring to a gentle boil.",
            "Reduce to a simmer and cook for 12–15 minutes, stirring "
            "occasionally, until the meatballs are cooked through.",
            "Meanwhile, cook the rice and green beans.",
            "Stir the crème fraîche and parmesan cheese into the "
            "meatball mixture. Taste and adjust seasoning if needed.",
            "Garnish with fresh basil and serve with rice and green "
            "beans.",
        ],
        "note": (
            "Best enjoyed fresh, but can be stored in the fridge for "
            "up to 2 days. Reheat gently on the hob, adding a splash "
            "of water or stock if needed to loosen the sauce. For "
            "best results, stir in the crème fraîche after reheating "
            "to keep the sauce smooth. Can also be frozen for up to "
            "2–3 months — freeze before adding the crème fraîche and "
            "stir it in fresh when reheating."
        ),
    },
    {
        "section": "Pasta & Comfort Dinners",
        "title": "Steak Fajitas",
        "tagline": "Smoky, spiced beef with all the toppings.",
        "serves": 1,
        "time": "20 mins",
        "image": "steak-fajitas.jpg",
        "ingredients": [
            "1 tsp olive oil",
            "100g beef strips",
            "½ red pepper, sliced",
            "½ green pepper, sliced",
            "½ red onion, sliced",
            "½ tsp cumin",
            "½ tsp dried chilli flakes (adjust to taste)",
            "½ tsp smoked paprika",
            "½ tsp dried oregano",
            "½ tsp garlic powder",
            "½ tsp ground coriander",
            "Black pepper, for seasoning",
            "1 heaped tsp tomato puree",
            "1 large or 2 small wraps (wholegrain if possible)",
            "1 tbsp sour cream",
            "6 cherry tomatoes, halved",
            "½ small (or ¼ large) avocado, sliced",
            "30g cheese, grated",
            "1 tbsp fresh coriander, chopped (optional)",
            "1 tsp lime juice (optional)",
        ],
        "instructions": [
            "Heat a frying pan over a medium-high heat and add the "
            "olive oil.",
            "Add the beef strips and cook for 2–3 minutes until "
            "browned on the outside.",
            "Add the sliced peppers and onion to the pan. Stir well "
            "and cook for 4–5 minutes until softened.",
            "Add the cumin, chilli flakes, smoked paprika, oregano, "
            "garlic powder, ground coriander, black pepper and tomato "
            "puree. Stir to coat everything evenly and cook for a "
            "further 2–3 minutes until the beef is cooked through and "
            "the spices are fragrant.",
            "Warm the wrap(s) in a dry pan for 20–30 seconds.",
            "Spread the sour cream over the wrap(s).",
            "Spoon the beef and vegetable mixture onto the wrap(s).",
            "Top with cherry tomatoes, avocado slices and grated "
            "cheese.",
            "Finish with fresh coriander and a squeeze of lime juice "
            "(if using).",
            "Fold the wrap(s) and serve immediately.",
        ],
        "note": (
            "Batch cooking tip: scale the beef, vegetables and wraps "
            "in line with how many servings you need, adjusting "
            "spices gradually to taste. Store leftovers in an "
            "airtight container in the fridge for up to 3 days and "
            "reheat thoroughly before serving. The beef mixture can "
            "also be frozen for up to 2 months."
        ),
    },
]

# Recipes still to come from Anna:
MISSING = [
    ("Slow Cooker",            "Slow Cooker Thai Green Curry"),  # in old PDF
    ("Slow Cooker",            "Slow Cooker Katsu Noodles"),     # in old PDF
    ("Traybakes",              "Cheesy Tomato Sausage Traybake"),  # in old PDF
    ("Traybakes",              "One Tray Harissa Traybake (V)"),  # in old PDF
    ("Bowls",                  "Cajun Beef Bowl (HC)"),
    ("Bowls",                  "Cajun Steak + Potato Bowl (HC)"),
    ("Bowls",                  "Creamy Chickpeas & Salmon (HC)"),
    ("Pasta & Comfort Dinners", "Chicken, Broccoli and Mushroom Pasta"),
    ("Pasta & Comfort Dinners", "Deconstructed Fish Pie (HC)"),
    ("Breakfast & Lunch",      "Scrambled Egg + Balsamic Tomatoes"),
]
