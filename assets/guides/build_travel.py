#!/usr/bin/env python3
"""Shift & Sustain — Travel Guide — WLA house style."""

import os
from wla_style import Guide, NAVY, BLUSH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "Travel-Guide.pdf")

TIPS = [
    ("Tailor Your Experience to Your Goals",
     "Before embarking on your Shift & Sustain journey while "
     "travelling, take a moment to define your objectives. This "
     "program offers you the flexibility to decide whether you wish "
     "to focus on continued weight loss or opt for maintenance to "
     "allow for more relaxation and flexibility during your trip. The "
     "choice is yours—either approach aligns with your unique goals."),
    ("Balance Your Meals with the Nutrition Formula",
     "While on your journey, sticking to a high-carb/low-carb or "
     "medium/medium meal structure will help maintain consistency. "
     "This formula supports your fat loss progress while allowing "
     "room for flexibility, based on your preferences."),
    ("Start the Day Right",
     "Eating breakfast within an hour of waking is key to stabilising "
     "your blood sugar levels, setting you up for a balanced and "
     "energetic day. A well-planned breakfast can prevent mid-morning "
     "hunger and overeating later in the day."),
    ("Stay Hydrated",
     "Hydration is even more important in a warmer climate. Be sure "
     "to drink plenty of water throughout the day, especially since "
     "you'll naturally lose more fluid through sweat. Bring a "
     "reusable water bottle to ensure you can stay hydrated during "
     "travel and on excursions."),
    ("Mindful Eating",
     "Even while indulging in new cuisines, remain mindful of your "
     "hunger cues. Aim to eat until satisfied, avoiding the feeling "
     "of being overly full or stuffed. Practising mindful eating "
     "will help you enjoy your meals while staying on track."),
    ("Stick to Three Meals a Day (Plus Snacks if Needed)",
     "Maintaining the program's structure of three meals a day will "
     "provide a reliable foundation. If hunger strikes between meals, "
     "don't hesitate to have a snack. Allowing yourself to get too "
     "hungry makes it harder to make healthy choices later."),
    ("Plan Ahead for Your Travel",
     "Plan your travel meals and snacks in advance. Consider bringing "
     "healthy, portable snacks like Nakd bars, nuts, seeds, dried "
     "fruit, and popcorn to avoid being forced into unhealthy choices "
     "at airports or train stations."),
    ("Assess Local Food Availability",
     "Before you leave, research the availability of food and shops "
     "at your destination. It may be worth bringing staples like "
     "porridge oats or decaf tea bags if you're unsure whether "
     "they'll be available."),
    ("Food Journaling",
     "Continue logging your meals and snacks in your food journal to "
     "maintain accountability and keep track of your progress. "
     "Journaling helps you stay mindful of what you consume, even "
     "while enjoying yourself abroad."),
    ("Plan Your Meals at Restaurants",
     "Research the restaurants you plan to visit in advance and "
     "review their menus online. This allows you to make healthy "
     "choices ahead of time, preventing impulse decisions when "
     "you're there."),
    ("Prepare for Excursions",
     "For days when you're out and about, consider what food and "
     "drink options will be available. Should you bring snacks, a "
     "bottle of water, or even arrange for hard-boiled eggs or fresh "
     "fruit from your hotel? Being prepared keeps you on track."),
    ("Embrace Fresh Fruit",
     "In warmer climates, take advantage of the abundance of fresh "
     "fruit, which can be refreshing and hydrating. Watermelon, for "
     "example, is a delicious and healthy choice."),
    ("Mind Your Drink Choices",
     "Alcohol consumption may be part of your experience, but be "
     "mindful of the intake. Track it in your food journal to keep "
     "yourself accountable. You can be flexible with alcohol, "
     "allowing for indulgences, but ensure this aligns with your "
     "personal goals."),
    ("Flexibility with Food and Drinks",
     "Indulgences like desserts, ice creams, or cocktails can be "
     "enjoyed, but how flexible you want to be is entirely up to you. "
     "If it aligns with your plan, savour these moments without "
     "guilt."),
    ("Plan Your Return Travel",
     "Just as you planned for the trip out, consider what snacks and "
     "drinks you'll need for your journey home to avoid any "
     "unnecessary temptations."),
    ("Movement Opportunities",
     "Take advantage of your surroundings to incorporate movement "
     "into your routine. Walking while sightseeing, swimming, or "
     "using the available fitness facilities can keep you active and "
     "engaged in your health goals."),
]

g = Guide(OUT)

g.cover(
    "SHIFT & SUSTAIN", "THE WEIGHT LOSS ACADEMY",
    [("Travel", "lbi", NAVY), ("Guide.", "lb", BLUSH)],
    "Staying on track — and still enjoying yourself — while "
    "travelling for work or holiday.",
)

g._new_content_page()
g.heading([[("Travel ", False), ("Tips", True)]])
g.paragraph("When travelling for work, it's important to maintain "
            "structure and routine, as your schedule is often packed "
            "and energy levels need to be sustained throughout "
            "meetings and tasks. Focus on quick, healthy meals, snacks "
            "that are easy to grab, and staying hydrated to keep your "
            "energy up without derailing your goals.")
g.paragraph("On holiday, there's more room for flexibility and "
            "indulgence, but balance is key. While it's important to "
            "enjoy the local food and relax, try to stick to mindful "
            "eating - mixing healthy choices with treats and staying "
            "active through sightseeing or leisure activities to "
            "maintain your progress.")
g.paragraph("Here are some tips:", gap_after=4)

for title, body in TIPS:
    g.keep_together(96)
    g.coral_heading(title, size=13, gap_before=9, gap_after=6)
    g.paragraph(body)

g.paragraph("By planning ahead and staying mindful, your Shift & "
            "Sustain program can be seamlessly integrated into your "
            "travels, ensuring that you return from your trip feeling "
            "both refreshed and empowered in your journey towards "
            "better health.", font="asb", color=NAVY)

# ---- Meal Tips
g.keep_together(280)
g.heading([[("Meal ", False), ("Tips", True)]])
g.paragraph("When on holiday, finding the right balance in meals while "
            "still enjoying local cuisine can be key to maintaining "
            "progress in a weight loss programme. A helpful approach "
            "is to focus on a low-carb breakfast and lunch, followed "
            "by a higher-carb dinner that allows for more indulgence.")
g.paragraph("This may look like the following:", gap_after=4)
g.select_table(["Breakfast", "Lunch", "Dinner"], [
    ["Low Carb / High Protein"],
    ["Low Carb / High Protein"],
    ["High Carb / Indulgent Meal"],
])
g.paragraph("Some example meal ideas are as follows:")

g.keep_together(170)
g.subhead([("Breakfast Options ", "lb"), ("(LC)", "lbi")], color=NAVY,
          size=20)
g.select_table(["Option 1", "Option 2", "Option 3", "Option 4"], [
    ["Smoothie (With fruit, yoghurt and milk of choice)"],
    ["Greek Yoghurt With Fresh Fruit"],
    ["Traditional Breakfast (Sausage, Bacon, Eggs) With Veggies"],
    ["Egg Based Dish (Omelette, Frittata, Egg Muffins) With Veggies"],
])

g.keep_together(190)
g.subhead([("Lunch Options ", "lb"), ("(LC)", "lbi")], color=NAVY, size=20)
g.select_table(["Option 1", "Option 2", "Option 3", "Option 4"], [
    ["Soup With Protein"],
    ["Egg Based Dish (Omelette, Frittata, Egg Muffins) With Veggies"],
    ["Meat (Chicken, Beef, Fish, Veggie Alternative) With Salad"],
    ["Meat (Chicken, Fish, Veggie Alternative) With Veggies "
     "(Steamed, Roasted, Stir-Fry)"],
])

g.keep_together(220)
g.subhead([("Dinner Options ", "lb"), ("(HC)", "lbi")], color=NAVY,
          size=20)
g.select_table(["Option 1", "Option 2", "Option 3", "Option 4"], [
    ["Meat (Chicken, Beef, Fish, Veggie Alternative) With Salad and a "
     "larger portion of potatoes/sweet potatoes etc. (approx. ¼ of "
     "the plate)"],
    ["Meat (Chicken, Fish, Veggie Alternative) With Veggies (Steamed, "
     "Roasted, Stir-Fry) and a large portion of rice/pasta/noodles/"
     "quinoa etc. (approx. ¼ of the plate)"],
    ["Falafel (6 falafel) with Salad or Veggies"],
    ["Any beans/chickpeas (3 tbsp) With Salad or Veggies and a smaller "
     "portion of rice/pasta/noodles/quinoa etc. (30-40g)"],
])

g.save({
    "title": "Travel Guide",
    "author": "The Weight Loss Academy",
    "subject": "Staying on track while travelling",
    "keywords": "travel, holiday, weight loss, nutrition, mindful eating",
    "creator": "The Weight Loss Academy",
})
