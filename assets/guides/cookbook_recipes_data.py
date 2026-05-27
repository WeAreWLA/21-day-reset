"""Recipe data for The WLA Weight Loss Cookbook.

Each recipe is a dict with: section, title, tagline, serves, time,
ingredients (list of strings), ingredients_sub (optional list of
(heading, [items]) sub-sections), to_serve (optional list),
instructions (list of strings), note (optional), image (filename).

Sections (order in the cookbook):
  1. Breakfast & Lunch
  2. Slow Cooker
  3. Bowls
  4. Dinners
"""

NAME = "The WLA Weight Loss Cookbook"
TAGLINE = (
    "15 fuss-free, macro-balanced recipes. Designed by a "
    "nutritionist to make weight loss feel easy, not restrictive."
)

SECTIONS = ["Breakfast & Lunch", "Slow Cooker", "Bowls", "Dinners"]

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

    # ============================== SLOW COOKER
    {
        "section": "Slow Cooker",
        "title": "Slow Cooker Thai Green Curry",
        "tagline": "Restaurant-style curry with five minutes of prep.",
        "serves": 4,
        "time": "4 hrs (high) / 6–8 hrs (low)",
        "image": "slow-cooker-thai-green-curry.jpg",
        "ingredients": [
            "4 chicken fillets",
            "1 large onion, sliced",
            "1 red pepper, sliced",
            "1 courgette, sliced",
            "130g baby corn",
            "1 tsp garlic powder",
            "1 tsp ground ginger",
            "Black pepper, for seasoning",
            "3–4 tbsp curry paste (Thai green)",
            "2 tbsp soy sauce",
            "1 chicken or vegetable stock cube (low sodium)",
            "1 tin coconut milk",
        ],
        "to_serve": [
            "60g wholewheat noodles",
            "1 spring onion, finely sliced",
            "1 tbsp fresh coriander, chopped (optional)",
            "Squeeze of lime juice",
        ],
        "instructions": [
            "Add all ingredients to the slow cooker. Stir well to "
            "combine.",
            "Cover and cook on high for 4 hours or on low for 6–8 "
            "hours.",
            "About 30 minutes before serving, shred or slice the "
            "chicken using two forks and return it to the slow "
            "cooker.",
            "Taste and adjust seasoning or spices if needed.",
            "Cook the noodles according to the packet instructions.",
            "To serve, add noodles to a bowl and top with the "
            "chicken curry. Sprinkle over the spring onion, "
            "coriander (if using) and a squeeze of lime juice.",
        ],
        "note": (
            "Store leftovers in an airtight container in the fridge "
            "for up to 3 days, or freeze for up to 2 months."
        ),
    },
    {
        "section": "Slow Cooker",
        "title": "Slow Cooker Katsu Noodles",
        "tagline": "All the cosy comfort of katsu — done while you get on with your day.",
        "serves": 4,
        "time": "6–7 hrs (low) / 3–4 hrs (high)",
        "image": "slow-cooker-katsu-noodles.jpg",
        "ingredients": [
            "1 onion, diced",
            "3–4 carrots, peeled and sliced",
            "1 red pepper, diced",
            "4 chicken fillets, diced",
            "Black pepper, for seasoning",
            "1 tsp garlic powder",
            "1 heaped tsp curry powder",
            "4 tbsp katsu curry paste",
            "2 tbsp soy sauce, low sodium",
            "1 tin coconut milk",
            "1 chicken stock cube, low sodium",
            "240g noodles",
            "12 tbsp peas",
        ],
        "to_serve": [
            "1 spring onion, sliced (optional)",
            "1 tsp sesame seeds (optional)",
            "1 tbsp fresh coriander, chopped (optional)",
        ],
        "instructions": [
            "Add the onion, carrots, red pepper and diced chicken "
            "to the slow cooker.",
            "Season with black pepper, then add the garlic powder "
            "and curry powder.",
            "Stir in the katsu curry paste and soy sauce, ensuring "
            "everything is well coated.",
            "Pour in the coconut milk and crumble in the stock "
            "cube. Stir gently to combine.",
            "Place the lid on and cook on low for 6–7 hours or high "
            "for 3–4 hours, until the chicken is fully cooked and "
            "tender.",
            "Around 15–20 minutes before serving, cook the noodles "
            "according to the packet instructions and cook the "
            "peas until tender (or any vegetables of your choice).",
            "Taste the curry and adjust seasoning if needed.",
            "Add the cooked noodles and peas to the slow cooker "
            "and mix well. Add a splash of water if needed to "
            "loosen the sauce.",
            "Serve in bowls and top with spring onions, sesame "
            "seeds and fresh coriander (all optional).",
        ],
        "note": (
            "Store leftovers in an airtight container in the fridge "
            "for up to 3–4 days, or freeze in portions (without "
            "noodles for best texture) for up to 3 months."
        ),
    },
    {
        "section": "Slow Cooker",
        "title": "Slow Cooker Sausages + Beans",
        "tagline": "Hearty, smoky, and packed with veg — proper comfort food.",
        "serves": 4,
        "time": "6–7 hrs (low) / 3–4 hrs (high)",
        "image": "slow-cooker-sausages-beans.jpg",
        "ingredients": [
            "1 tsp olive oil",
            "8 sausages (pork, beef, chicken/turkey or veggie)",
            "1 red pepper, diced",
            "1 onion, diced",
            "1 celery stick, diced",
            "2–3 carrots, diced",
            "1 tin cannellini beans, drained and rinsed",
            "400g potatoes, washed and cubed (skin on)",
            "Black pepper, for seasoning",
            "1 heaped tsp garlic",
            "1 heaped tsp smoked paprika",
            "1 heaped tsp cumin",
            "2 tbsp tomato puree",
            "2 tbsp Worcestershire sauce",
            "1 tin tomatoes",
            "1 low-salt stock cube",
            "400ml water",
        ],
        "to_serve": [
            "30g grated cheese (optional)",
            "1 tbsp fresh parsley, chopped (optional)",
        ],
        "instructions": [
            "Heat a frying pan with olive oil over a medium heat "
            "and cook the sausages until lightly browned on the "
            "outside. They don't need to be fully cooked through at "
            "this stage. Slice into bite-sized pieces if desired.",
            "Add the browned sausages to the slow cooker along with "
            "the red pepper, onion, celery, carrots, cannellini "
            "beans and cubed potatoes.",
            "Season with black pepper, then add the garlic, smoked "
            "paprika and cumin. Stir in the tomato puree, "
            "Worcestershire sauce, tinned tomatoes and crumble in "
            "the stock cube.",
            "Pour in the 400ml water, then stir gently so everything "
            "is evenly coated.",
            "Place the lid on the slow cooker and cook on low for "
            "6–7 hours or high for 3–4 hours, until the potatoes "
            "are tender and the sausages are fully cooked through.",
            "Stir well before serving and taste for seasoning.",
            "Top with cheese and fresh parsley (both optional).",
        ],
        "note": (
            "Serves 4. Store any leftovers in an airtight container "
            "in the fridge for up to 4 days, or freeze in single "
            "portions for up to 3 months."
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

    # ============================== DINNERS
    {
        "section": "Dinners",
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
        "section": "Dinners",
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
        "section": "Dinners",
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
        "section": "Dinners",
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
    {
        "section": "Dinners",
        "title": "One Tray Harissa Traybake (V)",
        "tagline": "Spiced chickpeas, halloumi, and roasted veg with a coriander yoghurt drizzle.",
        "serves": "1 (easily scaled)",
        "time": "35 mins",
        "image": "one-tray-harissa-traybake.jpg",
        "ingredients": [
            "½ red onion, sliced",
            "½ red pepper, sliced",
            "6 cherry tomatoes",
            "½ courgette, sliced",
            "6 tbsp chickpeas, rinsed and drained",
            "½ tsp garlic powder",
            "½ tsp dried thyme",
            "½ tsp oregano",
            "Pinch of black pepper",
            "1 tsp olive oil",
            "4 tsp harissa paste",
            "70g halloumi, sliced",
            "3–4 falafels (optional)",
            "Handful of baby spinach (or rocket)",
        ],
        "ingredients_sub": [
            ("For the coriander dressing", [
                "1 heaped tbsp full-fat Greek yoghurt",
                "1 heaped tsp mayonnaise",
                "1 tbsp fresh coriander, chopped",
            ]),
        ],
        "instructions": [
            "Preheat the oven to 200°C.",
            "In a large bowl, add all the ingredients except the "
            "halloumi, falafels, spinach and 1 tsp of harissa. Mix "
            "until well coated.",
            "Spread the spiced vegetables and chickpeas on a "
            "baking tray and roast for 15–20 minutes, until tender "
            "and golden.",
            "Mix the halloumi with the remaining 1 tsp of harissa.",
            "Place the halloumi slices on top of the roasted "
            "vegetables along with the falafels (if using). Return "
            "to the oven for 8–10 minutes, until the halloumi is "
            "golden and slightly crisp.",
            "While the traybake is cooking, mix the dressing "
            "ingredients in a small bowl.",
            "To serve, plate up the traybake, add the spinach (or "
            "rocket), then drizzle with the coriander dressing.",
        ],
        "note": (
            "Easy to batch cook — just scale up the vegetables, "
            "chickpeas and halloumi. Increase harissa, herbs and "
            "spices gradually and adjust to taste."
        ),
    },
]
