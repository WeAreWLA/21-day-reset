#!/usr/bin/env python3
"""The Food Swap List — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "The-Food-Swap-List.pdf")

ANIMAL = [
    ("Beef, lamb or pork mince", "100g (3½ oz) - 140g (5 oz)"),
    ("Beef pieces", "100g (3½ oz)"),
    ("Beef sirloin steak", "1 small, (approx. 120g (4 oz))"),
    ("Chicken fillet", "Medium sized, 100g (3½ oz) - 130g (4¾ oz)"),
    ("Chicken thigh", "1 large or 2 small"),
    ("Chorizo", "30g (1 oz)"),
    ("Cod fillet", "175g (6 oz) approx"),
    ("Cubed lamb", "100g (3½ oz)"),
    ("Duck", "small sized, 220–250g"),
    ("Eggs", "2 eggs"),
    ("Ham", "2 slices"),
    ("Lean bacon/rashers", "2 pieces"),
    ("Mackerel", "1 fillet"),
    ("Pork", "Around 130g pork chop"),
    ("Pork (beef or chicken) sausages", "2 sausages"),
    ("Prawns", "140g (5 oz)"),
    ("Protein powders", "1 scoop / 25g"),
    ("Salmon fillet", "1 small approx. 110g (3¾ oz)"),
    ("Salmon (tinned)", "Around 155g / tin"),
    ("Sardines", "1 small can, approx. 120g"),
    ("Small beef, stewing steak", "110g (4 oz) approx."),
    ("Smoked salmon", "55g (2 oz)"),
    ("Tuna steak", "1 small approx. 110g (3¾ oz)"),
    ("Tuna (tinned)", "1 small can approx. 70g (2½ oz)"),
    ("Turkey or chicken mince", "100g (3½ oz) - 130g (4¾ oz)"),
    ("White fish fillets", "185g (6½ oz)"),
]
VEGETARIAN = [
    ("Full-fat Greek yoghurt", "125g (½ cup)"),
    ("Full-fat cottage cheese", "100g (⅔ cup)"),
    ("Halloumi", "70g (2½ oz)"),
    ("Kefir", "125g"),
    ("Nut roast", "150g (1 cup)"),
    ("Paneer cheese", "70g (2½ oz)"),
    ("Quorn fillet", "1 piece"),
    ("Quorn mince", "75g (3oz)"),
    ("Quorn pieces", "75g (3oz)"),
    ("Ricotta cheese", "30g (2 tablespoons)"),
    ("Semi-skimmed milk", "100ml - 250ml (1 cup)"),
    ("Seitan", "100g (⅔ cup)"),
    ("Tempeh", "100g (⅔ cup)"),
    ("Tofu", "¼ block (115g (4 oz) approx) - 125g (½ cup)"),
    ("Vegetarian sausages", "2 sausages"),
]
PROT_CARB = [
    ("Breaded or battered fish", "½ fillet", "1 fillet"),
    ("Breaded chicken fillet", "½ fillet", "1 fillet"),
    ("Chicken Goujons", "<3 goujons", ">3 goujons"),
    ("Chicken Kiev", "½ Kiev", "1 Kiev"),
    ("Fish Goujons", "<3 goujons", ">3 goujons"),
    ("Quiche (with pastry)", "<¼ large quiche", "¼ large quiche"),
]
LEGUMES = [
    ("Baked beans, reduced sugar", "3 tablespoons", "> 3 tablespoons"),
    ("Black beans", "3 tablespoons", "> 3 tablespoons"),
    ("Butter beans", "3 tablespoons", "> 3 tablespoons"),
    ("Cannellini beans", "3 tablespoons", "> 3 tablespoons"),
    ("Chickpeas", "3 tablespoons", "> 3 tablespoons"),
    ("Falafels", "2-3 pieces", "> 3 pieces"),
    ("Haricot beans", "3 tablespoons", "> 3 tablespoons"),
    ("Hummus", "2-3 tablespoons", "> 3 tablespoons"),
    ("Pinto beans", "3 tablespoons", "> 3 tablespoons"),
    ("Red kidney beans", "3 tablespoons", "> 3 tablespoons"),
    ("Red lentils", "3 tablespoons", "> 3 tablespoons"),
    ("Soya or edamame beans", "3 tablespoons", "> 3 tablespoons"),
    ("Split peas", "3 tablespoons", "> 3 tablespoons"),
    ("Mixed beans", "3 tablespoons", "> 3 tablespoons"),
]
CARBS = [
    ("Bagels", "½ bagel or 1 bagel thin", "1 bagel"),
    ("Brown bread", "1 medium slice", "2 medium slices"),
    ("Breadcrumbs", "30–40g", "> 40g"),
    ("Brown bread roll", "1 small", "1 large"),
    ("Brown rice", "30-40g", "> 40g"),
    ("Buckwheat", "30-40g", "> 40g"),
    ("Bulgar wheat", "30-40g", "> 40g"),
    ("Burger buns", "½ burger bun", "1 burger bun"),
    ("Couscous, whole wheat", "30-40g", "> 40g"),
    ("Crackers (cream crackers, rye crispbread etc.)", "2-3 pieces",
     "> 3 pieces"),
    ("Flour, wholewheat", "1 - 2 tablespoons", "> 2 tablespoons"),
    ("Giant couscous, whole wheat", "30-40g", "> 40g"),
    ("Gnocchi", "<100g", ">100g"),
    ("Hash browns", "3 hash browns", ">3 hash browns"),
    ("Lasagne sheets", "1 lasagne sheet", "2 lasagne sheets"),
    ("Naan bread", "1 mini naan bread", "1 regular sized naan bread"),
    ("Oat flakes", "1 tablespoon - 40g (½ cup)", "> 40g"),
    ("Orzo", "30-40g", "> 40g"),
    ("Pitta bread", "1 mini pitta bread", "1 regular sized pitta bread"),
    ("Porridge oats", "1 tablespoon - 40g (½ cup)", "> 40g"),
    ("Potatoes", "< 100g", "> 100g"),
    ("Puff pastry", "⅛ sheet", "¼ sheet"),
    ("Quinoa", "30-40g", "> 40g"),
    ("Rice cakes", "<3 rice cakes", ">3 rice cakes"),
    ("Soba noodles", "30-40g", "> 40g"),
    ("Sourdough", "1 small slice", "2 small slices"),
    ("Sugar free muesli or granola", "30g (⅓ cup)", "> 30g"),
    ("Sweet potato", "< 100g", "> 100g"),
    ("Whole grain rice", "30-40g", "> 40g"),
    ("Whole wheat tortilla wrap", "1 small wrap", "1 large wrap"),
    ("Whole wheat pasta", "30-40g", "> 40g"),
    ("Wholewheat bread", "1 slice", "2 slices"),
    ("Wholewheat noodles", "30-40g", "> 40g"),
    ("Wholewheat spaghetti", "30-40g", "> 40g"),
]
FRUIT_VEG = [
    ("Apple", "1 small"), ("Artichokes", "½ average"),
    ("Aubergine", "½ average"), ("Avocado", "½ small / ¼ large"),
    ("Banana", "½ - 1 small"), ("Beansprouts", "100g (1¼ cups)"),
    ("Beetroot", "1 large / 2 small"), ("Blueberries", "15 pieces"),
    ("Broccoli", "140g (2 cups)"), ("Brussels sprouts", "8 pieces"),
    ("Butternut squash / pumpkin", "70g (½ cup) - 140g (1 cup)"),
    ("Cabbage", "80g"), ("Canned tomatoes", "150g (¾ cup) - 200g (1 cup)"),
    ("Carrot", "1 medium"), ("Cauliflower", "100g (½ cup)"),
    ("Cherry tomatoes", "6 pieces"),
    ("Clementines / satsumas", "1-2 small"),
    ("Chopped tomatoes", "100g (½ cup)"),
    ("Corn on the cob", "1 medium sized"), ("Courgette", "80g (½ cup)"),
    ("Cranberries, fresh or frozen", "40g (½ cup)"),
    ("Cucumber", "½ average or 4 mini"), ("Dates", "2-3 dates"),
    ("Dried fruit (raisins, sultanas)", "1 tablespoon - 30g"),
    ("Frozen mango", "70g (½ cup) - 125g (¾ cup)"),
    ("Frozen peas", "3 tablespoons"),
    ("Fruit salad made from fruit of your choice", "100g (¾ cup)"),
    ("Grapefruit", "½ average"),
    ("Green beans", "4 tablespoons - 80g (1 cup)"),
    ("Green pepper", "½ average"), ("Kale", "4 tablespoons"),
    ("Kiwi", "1-2 small"), ("Leeks", "½ average"),
    ("Mangetout", "10 pieces"), ("Mixed berries, frozen", "3 tablespoons"),
    ("Mixed salad leaves", "50g (2 cup)"), ("Mushrooms", "75g (⅔ cup)"),
    ("Parsnip", "1 small"), ("Peaches / nectarines", "1 average"),
    ("Pineapple", "4 rings"), ("Plums", "1-2 small"),
    ("Pomegranate", "½ average"), ("Portobello Mushrooms", "2 mushrooms"),
    ("Raddish", "6 pieces"), ("Raspberries", "50g (½ cup)"),
    ("Red Pepper", "½ average"), ("Rocket", "50g (2 cups)"),
    ("Saute vegetables", "250g (2 cups)"),
    ("Spinach leaves", "1 cup - 40g (1¼ cup) / 1 cereal bowl"),
    ("Strawberries", "7-8 pieces"), ("Sundried tomato", "3 pieces"),
    ("Sweetcorn", "2 tablespoons"),
    ("Vegetable - stir fry packet", "200g"), ("Watercress", "1 cup"),
]
FATS = [
    ("Almond butter", "1 tablespoon"), ("Avocado", "¼ or 35g frozen"),
    ("Butter, unsalted", "1 teaspoon"),
    ("Cheddar cheese", "15-30g (⅓ cup)"),
    ("Chia seeds", "1 teaspoon - 1 tablespoon"),
    ("Chocolate chips, dark", "1 teaspoon up to 80g (⅓ cup)"),
    ("Coconut milk, canned", "100g (½ cup) - 200g (1 cup)"),
    ("Cream", "> 4 tablespoons"), ("Cream cheese", "1 tablespoon"),
    ("Creme fraiche, full fat", "1 tablespoon"),
    ("Desiccated coconut", "1 teaspoon up to 45g (½ cup)"),
    ("Feta cheese", "30g (¼ cup)"),
    ("Flaxseeds", "1 teaspoon - 1 tablespoon"),
    ("Full-fat goats cheese", "30g (¼ cup)"),
    ("Green pesto", "1 tablespoon"),
    ("Mayonnaise, full-fat", "1 teaspoon"),
    ("Mixed nuts", "1 tablespoon - 30g"), ("Olive oil", "1 teaspoon"),
    ("Olives", "6 pieces"), ("Parmesan cheese", "15-30g (⅓ cup)"),
    ("Peanut butter", "1 teaspoon - 1 tablespoon"),
    ("Salad cream, full-fat", "1 teaspoon"),
    ("Sesame seeds", "1 teaspoon - 1 tablespoon"),
    ("Shredded mozzarella cheese", "30g (⅓ cup)"),
    ("Sour cream, full-fat", "1 tablespoon"),
    ("Sun and pumpkin seed mix", "1 teaspoon - 1 tablespoon"),
    ("Sunflower seeds", "1 teaspoon - 1 tablespoon"),
    ("Tzatziki", "1 tablespoon"),
    ("Vegetarian cheddar cheese", "15-30g (⅓ cup)"),
]
OTHER = [
    ("Balsamic vinegar", "1 tablespoon"), ("Brown sauce", "1 teaspoon"),
    ("Chilli sauce", "1 teaspoon"), ("Cornflakes", "30g"),
    ("Curry paste", "1 tablespoon"), ("Ghee", "1 teaspoon"),
    ("Herbs / Spices",
     "¼ teaspoon - 1 teaspoon (adjust to taste/preference)"),
    ("Honey", "1 teaspoon"), ("Jam", "1 teaspoon"),
    ("Lentil crisps", "20-25g"), ("Maple syrup", "1 teaspoon"),
    ("Mustard", "1 teaspoon"), ("Popcorn, plain", "20-25g"),
    ("Salad dressing (Caesar, vinaigrette etc.)", "1 teaspoon"),
    ("Salsa or tomato relish, reduced sugar", "1 tablespoon"),
    ("Sauerkraut", "1 tablespoon"),
    ("Soy sauce, reduced-salt", "1 tablespoon"),
    ("Stock cube (chicken, vegetable - low sodium)",
     "¼ - ½ stock cube"),
    ("Teriyaki sauce", "1 teaspoon - 1 tablespoon"),
    ("Tomato ketchup, reduced sugar", "1 teaspoon"),
    ("Tomato puree", "1 teaspoon - 1 tablespoon"),
    ("Worcestershire sauce", "1 tablespoon"),
]

g = Guide(OUT)

g.cover(
    "A SIMPLE GUIDE", "THE WEIGHT LOSS ACADEMY",
    [("The", "lbi", NAVY),
     ("Food Swap", "lb", BLUSH),
     ("List.", "lbi", NAVY)],
    "Swap any food for another in the same group, using the portions "
    "listed below.",
)

g._new_content_page()
g.heading([[("Welcome to", False)], [("Food Swapping", True)]])
g.paragraph("Please look at the food lists below if you would like to "
            "make adjustments to your meals/recipes. All food items "
            "within each section can be swapped around. All protein "
            "sources within the list can be switched around using the "
            "relevant portions below. The same goes for the rest of "
            "the food groups (carbohydrates, fats and fruits/"
            "vegetables).")
g.paragraph("The meals/recipes are flexible, leave out any "
            "ingredients you do not enjoy or replace them with another "
            "alternative. Reduce or increase flavours to your own "
            "liking. The recipes are not rigid.")
g.paragraph("NOTE: > means greater than", font="asb", color=NAVY)


def two_col(rows):
    g.select_table(None, [[r[0] for r in rows], [r[1] for r in rows]])


def three_col(rows):
    g.select_table(["", "Medium Carb", "High Carb"],
                   [[r[0] for r in rows], [r[1] for r in rows],
                    [r[2] for r in rows]])


def section(title, builder):
    g.keep_together(150)
    g.coral_heading(title, size=26, gap_before=18, gap_after=12)
    builder()


section("Protein  ·  Animal Sources", lambda: two_col(ANIMAL))
section("Protein  ·  Vegetarian Sources", lambda: two_col(VEGETARIAN))
section("Protein & Carbohydrates", lambda: three_col(PROT_CARB))
section("Protein  ·  Legumes", lambda: three_col(LEGUMES))
section("Carbohydrate Types", lambda: three_col(CARBS))
section("Fruit & Vegetables", lambda: two_col(FRUIT_VEG))
section("Fat Types", lambda: two_col(FATS))
section("Other Foods", lambda: two_col(OTHER))

g.note("Please note: Portion sizes listed are only guidelines and may "
       "be adjusted to suit individual needs.")

g.save({
    "title": "The Food Swap List",
    "author": "The Weight Loss Academy",
    "subject": "Food swaps and portion guidance",
    "keywords": "food swap, portions, protein, carbohydrate, weight loss",
    "creator": "The Weight Loss Academy",
})
