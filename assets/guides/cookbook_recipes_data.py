"""Recipe data for The WLA Weight Loss Cookbook.

Each recipe is a dict with: section, title, tagline, serves, time,
ingredients (list of strings), ingredients_sub (optional list of
(heading, [items]) sub-sections), to_serve (optional list),
instructions (list of strings), note (optional), image (filename).

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
    {
        "section": "Breakfast & Lunch",
        "title": "Scrambled Egg + Balsamic Tomatoes",
        "tagline": "Creamy cottage-cheese eggs with jammy balsamic tomatoes.",
        "serves": 1,
        "time": "15 mins",
        "image": "scrambled-egg-balsamic-tomatoes.jpg",
        "ingredients": [
            "2 eggs",
            "100g cottage cheese",
            "10ml milk (of your choice)",
            "Salt and black pepper, to taste",
            "1 tsp olive oil or butter",
            "2 tomatoes, quartered",
            "1 tbsp balsamic vinegar",
            "Side salad of your choice",
        ],
        "instructions": [
            "Crack the eggs into a bowl and add the cottage cheese, "
            "milk, salt and black pepper. Mix well until combined.",
            "Heat the olive oil or butter in a non-stick pan over a "
            "low–medium heat.",
            "Pour in the egg mixture and cook gently, stirring "
            "continuously, until soft and scrambled to your liking.",
            "Remove from the heat and set aside.",
            "In the same pan, add the tomatoes and cook over a "
            "medium heat for 3–4 minutes until softened.",
            "Add the balsamic vinegar and cook for a further 1–2 "
            "minutes until slightly reduced and glossy.",
            "Serve the scrambled eggs with the balsamic tomatoes and "
            "a side salad.",
        ],
        "note": (
            "Best enjoyed fresh. The cottage cheese can be left out "
            "if preferred for a more traditional scrambled egg "
            "texture."
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
    {
        "section": "Bowls",
        "title": "Cajun Beef Bowl",
        "tagline": "Smoky, spiced mince stirred through wholegrain rice and spinach.",
        "serves": 1,
        "time": "25 mins",
        "image": "cajun-beef-bowl.jpg",
        "ingredients": [
            "60g wholegrain rice",
            "120g minced beef (or pork, turkey, chicken) — or 75g "
            "Quorn mince",
            "½ red onion, diced",
            "½ celery stick, diced",
            "75g mushrooms, sliced",
            "½ tsp garlic powder",
            "1 tsp Cajun seasoning",
            "½ tsp paprika",
            "1 tbsp tomato purée",
            "½ stock cube, low sodium",
            "Black pepper, for seasoning",
            "Handful of spinach",
            "30g grated cheese",
            "¼ lime wedge (optional)",
        ],
        "instructions": [
            "Cook the rice according to packet instructions. Drain "
            "and set aside.",
            "Heat a frying pan over a medium heat and cook the beef "
            "mince until browned, breaking it up as it cooks. Drain "
            "any excess liquid if needed.",
            "Add the onion, celery and mushrooms. Cook for 4–5 "
            "minutes until softened.",
            "Stir in the garlic powder, Cajun seasoning, paprika, "
            "tomato purée, stock cube and black pepper.",
            "Allow to simmer for 4–5 minutes.",
            "Add the cooked rice to the pan along with the spinach. "
            "Stir everything together until fully coated and the "
            "spinach has wilted.",
            "If the mixture looks a little dry, add a splash of "
            "water (50–100ml) to loosen. Taste and adjust seasoning "
            "if needed — more Cajun seasoning could be added.",
            "Serve in a bowl and top with grated cheese and a "
            "squeeze of lime juice.",
        ],
        "note": (
            "Short on time? Use half a packet of pre-cooked rice "
            "and stir it straight into the mince until heated "
            "through. Store in an airtight container in the fridge "
            "for up to 3–4 days. Can also be frozen in portions for "
            "up to 3 months. Reheat thoroughly before serving."
        ),
    },
    {
        "section": "Bowls",
        "title": "Cajun Steak + Potato Bowl",
        "tagline": "Crispy Cajun potatoes, steak, and a punchy yoghurt sauce.",
        "serves": 1,
        "time": "40 mins",
        "image": "cajun-steak-potato-bowl.jpg",
        "ingredients": [
            "160g potatoes, washed and cubed",
            "1 heaped tsp olive oil",
            "1 tsp Cajun seasoning",
            "1 small beef sirloin steak (approx. 120g)",
            "100g broccoli, cut into small florets",
            "2–3 tbsp sweetcorn",
            "Handful of rocket",
            "6 slices pickled red onion (or ½ regular red onion)",
            "30g parmesan",
            "Fresh parsley (optional)",
        ],
        "ingredients_sub": [
            ("For the Cajun yoghurt sauce", [
                "1 heaped tbsp Greek yoghurt",
                "1 heaped tsp mayo",
                "½ tsp Cajun seasoning",
                "1 tsp lemon juice",
                "½ tsp onion powder",
                "1 tsp water",
                "½ tsp soy sauce (low sodium)",
                "Black pepper, for seasoning",
            ]),
        ],
        "instructions": [
            "Preheat the air fryer to 200°C or oven to 200°C "
            "(180°C fan).",
            "Toss the potatoes with olive oil and Cajun seasoning.",
            "Air fryer: cook for 25–30 minutes, shaking halfway, "
            "until crisp and golden. Oven: roast for 30–35 minutes, "
            "turning halfway, until golden and crisp.",
            "Season the steak as you like (add optional extra Cajun "
            "seasoning). Cook to your liking, then rest for 5 "
            "minutes before slicing.",
            "Steam or lightly cook the broccoli and heat the "
            "sweetcorn.",
            "In a small bowl, mix together all the sauce "
            "ingredients. Taste and adjust seasoning, then place in "
            "the fridge until ready.",
            "To assemble, add rocket to a bowl, top with potatoes, "
            "broccoli, sweetcorn and (pickled) red onion.",
            "Add the sliced steak, finish with parmesan, fresh "
            "parsley and a drizzle of the Cajun yoghurt sauce.",
            "Serve and enjoy immediately.",
        ],
        "note": (
            "If making a larger batch, store any leftovers in an "
            "airtight container in the fridge for up to 2–3 days. "
            "For best results, store the dressing separately and "
            "mix before serving. Cajun seasoning is available in "
            "most supermarkets, including Marks & Spencer."
        ),
    },
    {
        "section": "Bowls",
        "title": "Creamy Chickpeas & Salmon",
        "tagline": "Soft baked salmon over a creamy parmesan-chickpea base.",
        "serves": 1,
        "time": "25 mins",
        "image": "creamy-chickpeas-salmon.jpg",
        "ingredients": [
            "1 salmon fillet (approx. 110g)",
            "Black pepper, to taste",
            "1 tsp olive oil",
            "½ leek, sliced",
            "½ courgette, sliced into chunks",
            "1 tsp garlic powder",
            "1 tsp mixed herbs",
            "6 tbsp chickpeas (drained and rinsed if from a tin)",
            "4 tbsp frozen peas",
            "½ low-salt vegetable or chicken stock cube",
            "50ml water",
            "1 tsp soy sauce",
            "50ml cream",
            "30g parmesan, grated",
        ],
        "instructions": [
            "Preheat the oven to 180°C (fan) or 200°C "
            "(conventional). Season the salmon with a pinch of "
            "black pepper, then bake for 12–15 minutes until cooked "
            "through.",
            "Heat 1 tsp of olive oil in a non-stick frying pan over "
            "a medium heat. Add the leek and courgette and cook for "
            "around 5 minutes until softened.",
            "Stir in the garlic powder, mixed herbs and black "
            "pepper to taste. Cook for a further 1–2 minutes.",
            "Add the chickpeas, peas, stock cube, water and soy "
            "sauce. Bring to a gentle simmer and cook for a few "
            "minutes until the vegetables are tender and most of "
            "the liquid has reduced.",
            "Turn down the heat and stir in the cream and most of "
            "the parmesan (reserve a little for serving). Mix until "
            "the sauce is creamy and well combined.",
            "Spoon the creamy chickpea mixture onto a plate, place "
            "the salmon fillet on top.",
            "Finish with the remaining parmesan and serve.",
        ],
        "note": (
            "If you increase the servings for another day, store "
            "the salmon and chickpea mixture separately. Reheat "
            "the chickpea mixture gently in a pan over a low heat, "
            "adding a splash of water if needed to loosen the "
            "sauce. Reheat the salmon gently or enjoy it cold. "
            "Avoid overheating to prevent the sauce from splitting."
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
        "title": "Chicken, Broccoli and Mushroom Pasta",
        "tagline": "Creamy, savoury pasta with tender chicken and greens.",
        "serves": 1,
        "time": "25 mins",
        "image": "chicken-broccoli-mushroom-pasta.jpg",
        "ingredients": [
            "60g wholewheat pasta",
            "1 chicken fillet (approx. 125g), cut into bite-sized "
            "chunks",
            "Black pepper, for seasoning",
            "1 tsp paprika",
            "1 tsp oregano",
            "1 tsp olive oil",
            "½ leek, sliced",
            "6 mushrooms, sliced",
            "100g broccoli, cut into florets",
            "½ tsp garlic",
            "½ stock cube",
            "50ml water",
            "1 tbsp Worcestershire sauce",
            "1 tbsp cream cheese",
        ],
        "instructions": [
            "Cook the pasta according to packet instructions "
            "(reserve a little pasta water).",
            "Season the chicken with black pepper, paprika and "
            "oregano.",
            "Heat the olive oil in a pan and cook the chicken until "
            "lightly golden.",
            "Add the leek, mushrooms and broccoli and cook for a "
            "few minutes.",
            "Stir in the garlic and cook for 30–60 seconds.",
            "Crumble in the stock cube, add water (or pasta water) "
            "and Worcestershire sauce.",
            "Bring to the boil, then simmer for 5–10 minutes.",
            "Stir in the cream cheese and allow it to melt into "
            "the sauce.",
            "Add the drained pasta and mix well until fully coated. "
            "Add a touch more water if needed.",
            "Taste and add more seasoning (oregano, black pepper, "
            "garlic or paprika) if needed.",
            "Serve and enjoy immediately.",
        ],
        "note": None,
    },
    {
        "section": "Pasta & Comfort Dinners",
        "title": "Deconstructed Fish Pie",
        "tagline": "All the comfort of fish pie, in fresh, lighter form.",
        "serves": 2,
        "time": "35 mins",
        "image": "deconstructed-fish-pie.jpg",
        "ingredients": [],
        "ingredients_sub": [
            ("For the potatoes", [
                "320g potatoes, washed and chopped",
                "1 heaped tsp olive oil",
                "Black pepper, to taste",
                "1 tsp garlic granules",
                "1 tsp mixed herbs",
            ]),
            ("For the fish pie filling", [
                "2 tsp butter",
                "½ leek (or onion), finely sliced",
                "Salt and black pepper, to taste",
                "1 tbsp plain flour",
                "300ml milk",
                "½ stock cube, low sodium (vegetable)",
                "½ tsp Dijon mustard",
                "340g fish pie mix (salmon, haddock and cod)",
                "70g peas",
                "Juice of ¼–½ lemon (to taste)",
                "1 tbsp fresh parsley, chopped",
                "2 tbsp parmesan cheese, grated",
            ]),
        ],
        "to_serve": [
            "140g broccoli",
            "70g sweetcorn",
        ],
        "instructions": [
            "Preheat the air fryer to 200°C.",
            "Place the potatoes into a bowl with olive oil, black "
            "pepper, garlic granules and mixed herbs. Mix well.",
            "Add to the air fryer and cook for 20 minutes, shaking "
            "halfway through, until golden and crispy.",
            "Meanwhile, heat the butter in a pan over a medium heat. "
            "Add the leek or onion, season with salt and black "
            "pepper, and cook for 4–5 minutes until softened.",
            "Stir in the flour and cook for 1 minute.",
            "Gradually add the milk, stirring continuously until a "
            "smooth sauce forms and begins to thicken. Crumble in "
            "the stock cube and stir well.",
            "Add the Dijon mustard and mix through.",
            "Add the fish and peas. Simmer gently for 5–7 minutes "
            "until the fish is cooked through.",
            "Meanwhile, prepare the broccoli and sweetcorn.",
            "Finish with lemon juice, parsley and parmesan cheese. "
            "Taste and adjust seasoning if needed.",
            "Add the crispy potatoes to a bowl, serve with broccoli "
            "and sweetcorn, and spoon over the fish pie mixture.",
        ],
        "note": (
            "Serves 2 — can be stored in the fridge for up to 2 "
            "days. Reheat gently on the hob, adding a splash of "
            "water or milk if needed to loosen the sauce. The "
            "potatoes are best made fresh for maximum crispiness "
            "but can be reheated in the air fryer for 5–8 minutes."
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

# Recipes still to come from Anna (text already in original PDF, just
# need fresh-styled images uploaded as JPEGs):
IMAGES_NEEDED = [
    ("Slow Cooker", "Slow Cooker Thai Green Curry",
     "slow-cooker-thai-green-curry.jpg"),
    ("Slow Cooker", "Slow Cooker Katsu Noodles",
     "slow-cooker-katsu-noodles.jpg"),
    ("Traybakes", "Cheesy Tomato Sausage Traybake",
     "cheesy-tomato-sausage-traybake.jpg"),
    ("Traybakes", "One Tray Harissa Traybake (V)",
     "one-tray-harissa-traybake.jpg"),
]
