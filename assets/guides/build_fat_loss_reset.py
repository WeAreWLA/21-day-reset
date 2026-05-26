#!/usr/bin/env python3
"""Build the WLA 5 Day Fat Loss Reset Guide.

A scaffold matching the structure & visual style of the existing
7 Day Sugar Cravings Reset. Framing content (mission, founder note,
tips, guidelines, swop list, drink / snack tips, educational pages)
is fully written and ready. Member-results photos and the recipe
content are intentionally left as placeholders so Anna can drop
them in.
"""
import os
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "..", "5-Day-Fat-Loss-Reset-Guide.pdf")

CREAM = (249 / 255, 247 / 255, 244 / 255)
NAVY = (0 / 255, 48 / 255, 95 / 255)
CORAL = (247 / 255, 159 / 255, 131 / 255)
DUSTPINK = (250 / 255, 232 / 255, 222 / 255)
BEIGE = (233 / 255, 223 / 255, 211 / 255)
INK = (0.18, 0.18, 0.18)
RULE = (0.82, 0.82, 0.86)
WHITE = (1, 1, 1)
MUTED = (0.55, 0.55, 0.60)

FONTS = {
    "lb":  "LibreBaskerville-Regular.ttf",
    "lbi": "LibreBaskerville-Italic.ttf",
    "as":  "AlegreyaSans-Regular.ttf",
    "asm": "AlegreyaSans-Medium.ttf",
    "asb": "AlegreyaSans-Bold.ttf",
    "asi": "AlegreyaSans-Italic.ttf",
}
FACE = {k: fitz.Font(fontfile=os.path.join(FONT_DIR, v))
        for k, v in FONTS.items()}

PW, PH = 595.0, 842.0
M = 60
FOOTER_H = 32


def tw(s, font, size):
    return FACE[font].text_length(s, size)


def wrap(s, font, size, w):
    out, cur = [], ""
    for word in s.split():
        t = word if not cur else cur + " " + word
        if tw(t, font, size) <= w or not cur:
            cur = t
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


class P:
    """Page drawing helper."""

    def __init__(self, doc, page_n=None, footer=True):
        self.pg = doc.new_page(width=PW, height=PH)
        for a, fn in FONTS.items():
            self.pg.insert_font(fontname=a,
                                fontfile=os.path.join(FONT_DIR, fn))
        self.pg.draw_rect(self.pg.rect, color=None, fill=CREAM)
        if footer and page_n is not None:
            self._footer(page_n)

    def _footer(self, n):
        self.pg.draw_rect(fitz.Rect(0, PH - FOOTER_H, PW, PH),
                          color=None, fill=NAVY)
        bx, by, bs = PW - 86, PH - FOOTER_H - 6, 26
        self.pg.draw_rect(fitz.Rect(bx, by, bx + bs, by + bs),
                          color=NAVY, fill=CREAM, width=1.0)
        self.tc(bx + bs / 2, by + 11, "W", "asb", 8, NAVY)
        self.tc(bx + bs / 2, by + 22, "LA", "asb", 8, NAVY)
        self.t(PW - 38, PH - 12, str(n), "asb", 16, WHITE)

    def t(self, x, y, s, font, size, color):
        self.pg.insert_text((x, y), s, fontname=font, fontsize=size,
                            color=color)

    def tc(self, cx, y, s, font, size, color):
        self.t(cx - tw(s, font, size) / 2, y, s, font, size, color)

    def tr(self, rx, y, s, font, size, color):
        self.t(rx - tw(s, font, size), y, s, font, size, color)

    def rect(self, x0, y0, x1, y1, fill=None, stroke=None, w=0.8):
        self.pg.draw_rect(fitz.Rect(x0, y0, x1, y1), color=stroke,
                          fill=fill, width=w)

    def line(self, x0, y0, x1, y1, color=RULE, w=0.7):
        self.pg.draw_line((x0, y0), (x1, y1), color=color, width=w)

    def circle(self, cx, cy, r, fill=None, stroke=None, w=1.0):
        self.pg.draw_circle((cx, cy), r, color=stroke, fill=fill, width=w)

    def para(self, x, y, s, font, size, color, maxw, lh, center=False):
        for ln in wrap(s, font, size, maxw):
            if center:
                self.tc(x + maxw / 2, y, ln, font, size, color)
            else:
                self.t(x, y, ln, font, size, color)
            y += lh
        return y

    def bullet(self, x, y, s, font, size, color, maxw, lh):
        self.pg.draw_circle((x + 3, y - 3), 1.6, color=None, fill=INK)
        return self.para(x + 13, y, s, font, size, color, maxw - 13, lh)

    def heading(self, segs, y, size=34, center=False):
        """Navy Libre Baskerville heading with italics for some words."""
        total = sum(tw(t, "lbi" if it else "lb", size) for t, it in segs)
        x = (PW - total) / 2 if center else M
        for txt, it in segs:
            f = "lbi" if it else "lb"
            self.t(x, y, txt, f, size, NAVY)
            x += tw(txt, f, size)

    def section_title(self, segs, y, underline=True, size=24):
        """In-page section title (navy, with optional coral underline)."""
        cx = M
        for txt, it in segs:
            f = "lbi" if it else "lb"
            self.t(cx, y, txt, f, size, NAVY)
            cx += tw(txt, f, size)
        if underline:
            self.line(M, y + 8, M + 80, y + 8, color=CORAL, w=2.0)


def navy_check(p, x, y, sz=18):
    """Navy checkbox with white tick."""
    p.rect(x, y, x + sz, y + sz, fill=NAVY, w=0)
    p.pg.draw_line((x + 4, y + sz / 2),
                   (x + sz / 2 - 1, y + sz - 4),
                   color=WHITE, width=2.0)
    p.pg.draw_line((x + sz / 2 - 1, y + sz - 4),
                   (x + sz - 3, y + 4),
                   color=WHITE, width=2.0)


def empty_check(p, x, y, sz=18):
    p.rect(x, y, x + sz, y + sz, stroke=NAVY, w=1.2)


# ====================================================== covers / TOC

def cover(doc):
    p = P(doc, footer=False)
    # decorative thin navy border
    inset = 28
    p.rect(inset, inset, PW - inset, PH - inset, stroke=NAVY, w=0.9)
    # WLA logo box top-left
    p.rect(M, 90, M + 44, 134, stroke=NAVY, w=1.0)
    p.tc(M + 22, 112, "W", "asb", 11, NAVY)
    p.line(M + 8, 116, M + 36, 116, color=NAVY, w=0.6)
    p.tc(M + 22, 128, "LA", "asb", 11, NAVY)
    # title block
    ly = 250
    p.t(M, ly, "The 5 Day", "lb", 58, NAVY)
    p.t(M, ly + 80, "Fat Loss", "lbi", 80, NAVY)
    p.t(M, ly + 160, "Reset", "lb", 58, NAVY)
    # subhead
    sy = ly + 220
    for ln in wrap("Start today, kickstart fat loss + lose up to "
                   "5lbs in 5 days.", "asb", 16, PW - 2 * M):
        p.t(M, sy, ln, "asb", 16, NAVY)
        sy += 22
    # coral pill with descriptor
    py0 = sy + 24
    py1 = py0 + 72
    px0, px1 = M, PW - M
    p.pg.draw_rect(fitz.Rect(px0, py0, px1, py1),
                   color=None, fill=CORAL,
                   stroke_opacity=0, fill_opacity=1)
    text = ("A simple, no-fluff reset for women ready to ignite fat "
            "loss and feel lighter, leaner and more in control.")
    lines = wrap(text, "as", 13, px1 - px0 - 60)
    ty = py0 + (py1 - py0) / 2 - (len(lines) - 1) * 8 - 2
    for ln in lines:
        p.tc((px0 + px1) / 2, ty, ln, "as", 13, NAVY)
        ty += 17


def toc(doc, n):
    p = P(doc, n)
    p.heading([("Table of ", False), ("Contents", True)], 110,
              size=44)
    items = [
        ("3",       "About Us"),
        ("4-5",     "The WLA Mission"),
        ("6",       "A Note From Our Founder - Anna Wallace"),
        ("7-9",     "WLA Members Results / Our Community Success"),
        ("10-11",   "Important Tips for Getting Started"),
        ("12",      "The 5 Day Fat Loss Reset Guidelines"),
        ("13",      "The 5 Day Fat Loss Reset Meal Overview"),
        ("14-16",   "Breakfast Recipes"),
        ("17-20",   "Lunch Recipes"),
        ("21-25",   "Dinner Recipes"),
        ("26-28",   "Mid-Afternoon Snack Recipes"),
        ("29-39",   "The Swop List"),
        ("40",      "Drink Tips"),
        ("41-44",   "Snack Tips"),
        ("45",      "Why Balanced Blood Sugar Supports Fat Loss"),
        ("46-47",   "Easily Kickstart Fat Loss in 5 Days"),
        ("48",      "Why Breakfast is Important"),
        ("49",      "Why Snacking is Important"),
        ("50",      "The WLA Nutrition Formula"),
    ]
    y = 220
    for pg, label in items:
        p.t(M + 30, y, pg, "as", 10.5, INK)
        # dotted leader
        x = M + 110
        while x < M + 200:
            p.pg.draw_circle((x, y - 3), 0.5, color=None, fill=MUTED)
            x += 3.2
        p.t(M + 215, y, label, "as", 10.5, INK)
        y += 22


# ====================================================== welcome
def welcome(doc, n):
    p = P(doc, n)
    p.t(M, 90, "Hello, Welcome to", "lb", 22, NAVY)
    p.t(M, 116, "The WLA Community!", "lb", 22, NAVY)
    paras = [
        "Really excited that you have registered for our 5 Day Fat "
        "Loss Reset. Start today, kickstart fat loss + lose up to "
        "5lbs in 5 days.",
        "A simple, no-fluff reset for women ready to ignite fat loss "
        "and feel lighter, leaner and more in control.",
    ]
    y = 158
    for para in paras:
        for ln in wrap(para, "as", 11.5, 360):
            p.t(M, y, ln, "as", 11.5, INK)
            y += 16
        y += 8
    # checklist
    benefits = [
        "Kickstart up to 5 pounds of fat loss",
        "More stable energy",
        "Less mindless snacking",
        "Reduced sugar cravings",
        "Less bloated feeling",
        "Brighter skin",
    ]
    cy = 280
    for b in benefits:
        navy_check(p, M, cy, sz=22)
        p.t(M + 64, cy + 16, b, "as", 11.5, INK)
        cy += 48
    # close
    p.t(M, cy + 4, "Ready to feel better faster?", "as", 11.5, INK)
    p.t(M, cy + 24, "Let's dive in!", "as", 11.5, INK)
    for i, ln in enumerate(wrap(
            "Before you start the reset, we want to introduce The "
            "Weight Loss Academy (WLA) very briefly and share useful "
            "tips for getting started in the easiest way.",
            "as", 11.5, 360)):
        p.t(M, cy + 56 + i * 16, ln, "as", 11.5, INK)
    # photo placeholder column on right
    for i, y in enumerate([158, 360, 562]):
        p.rect(PW - M - 180, y, PW - M, y + 170,
               fill=DUSTPINK, stroke=RULE)
        p.tc(PW - M - 90, y + 90, "[ photo ]", "asi", 10.5, MUTED)


def soft_band(p, y0, y1):
    """Soft dust-pink wash with diagonal accent across the top of a page."""
    p.rect(0, y0, PW, y1, fill=DUSTPINK)


def mission_1(doc, n):
    p = P(doc, n)
    soft_band(p, 0, 280)
    p.rect(M, 90, PW - M, 250, fill=BEIGE, stroke=RULE)
    p.tc(PW / 2, 175, "[ Community photo ]", "asi", 11, MUTED)
    p.rect(0, 270, PW, 320, fill=DUSTPINK)
    p.heading([("The ", False), ("WLA Mission", True)], 310,
              size=34, center=True)
    text = [
        "Our mission at The WLA is to help women lose weight for the "
        "last time.",
        "Empowering women to achieve sustainable and easy weight "
        "loss through a simple approach that focuses on flexible "
        "nutrition, behavioural change strategies that promote "
        "long-lasting results and coaching that empowers you to take "
        "control of your lifestyle.",
        "Say goodbye to traditional diets and hello to freedom!",
        "The Weight Loss Academy is focused on maximum effortless "
        "results without deprivation...",
    ]
    y = 360
    for t in text:
        for ln in wrap(t, "as", 11.5, PW - 2 * M):
            p.t(M, y, ln, "as", 11.5, INK)
            y += 16
        y += 8
    p.t(M, y + 6, "Helping our clients:", "as", 11.5, INK)
    bullets = ["Burn body fat", "Build confidence",
               "Slay cravings naturally", "Skyrocket energy"]
    by = y + 32
    for b in bullets:
        p.bullet(M + 16, by, b, "as", 11.5, INK, 360, 16)
        by += 22


def mission_2(doc, n):
    p = P(doc, n)
    soft_band(p, 0, 280)
    p.rect(M, 90, PW - M, 250, fill=BEIGE, stroke=RULE)
    p.tc(PW / 2, 175, "[ Community photo ]", "asi", 11, MUTED)
    p.rect(0, 270, PW, 320, fill=DUSTPINK)
    p.heading([("The ", False), ("WLA Mission", True)], 310,
              size=34, center=True)
    intro = ("The WLA focuses on 3 main core strategies in our "
             "signature WLA Approach to support clients with every "
             "tool that's needed for long lasting, transformative "
             "change.")
    y = 360
    for ln in wrap(intro, "as", 11.5, PW - 2 * M):
        p.t(M, y, ln, "as", 11.5, INK)
        y += 16
    y += 10
    pillars = [
        ("The WLA Nutrition Formula promotes easy weight loss with "
         "a flexible approach to nutrition with everyday foods. Feel "
         "lighter within days, say hello to confidence, lose weight "
         "consistently, increase your energy and say goodbye to fad "
         "diets."),
        ("Our behavioural change strategies centre around the "
         "psychology behind weight loss — lose weight but keep it "
         "off. Have food freedom and goodbye to that self-sabotaging "
         "food guilt."),
        ("Our expert coaching focuses on consistency strategies so "
         "you finally stop “falling off track”. We guide "
         "you every step of the way with our professional, women-"
         "only and non-judgemental coaching community. Focusing on "
         "accountability, staying on track and empowerment."),
    ]
    for t in pillars:
        empty_check(p, M, y - 12, sz=18)
        lines = wrap(t, "as", 10.8, PW - 2 * M - 34)
        ty = y
        for ln in lines:
            p.t(M + 30, ty, ln, "as", 10.8, INK)
            ty += 15
        y = ty + 10
    close = ("Join us on a journey back to your happy place in your "
             "body — it's time to feel lighter, more confident, "
             "healthier and more energised without going down the "
             "traditional diet route filled with minimal calories "
             "and extreme workouts.")
    for ln in wrap(close, "as", 11, PW - 2 * M):
        p.t(M, y, ln, "as", 11, INK)
        y += 15


def founder(doc, n):
    p = P(doc, n)
    # placeholder photo
    p.rect(PW - M - 220, 80, PW - M, 280, fill=DUSTPINK, stroke=RULE)
    p.tc(PW - M - 110, 175, "[ Before / After photo ]", "asi", 11, MUTED)
    # heading
    p.t(M, 340, "A Note From", "lb", 38, NAVY)
    p.t(M, 380, "Our Founder", "lb", 38, NAVY)
    p.t(M, 420, "Anna Wallace", "lbi", 24, NAVY)
    text = [
        "I once struggled with my weight, starting each day with "
        "determination but often resorting to unhealthy habits like "
        "the Special K diet or just going hours without food.",
        "Evenings would often end with takeaway, excessive eating, "
        "or alcohol to cope.",
        "Feeling lost and unhappy, I believed I was the \"fat\" one "
        "in my family and didn't know how to change.",
        "After hitting rock bottom, I enrolled in University to "
        "study Food and Nutrition. This decision transformed me — "
        "I lost weight and maintained it, even after pregnancy.",
        "I founded The Weight Loss Academy, supporting over 50,000 "
        "clients globally over 9 years.",
        "Our WLA Approach helps to burn body fat simply and "
        "flexibly, restoring confidence and igniting sustainable "
        "fat loss.",
        "If you're reading this, know that achieving your goals is "
        "possible, even if you've tried everything and feel like "
        "giving up. Your journey matters, and like mine, finding "
        "the right weight loss approach can change everything.",
    ]
    y = 450
    for t in text:
        for ln in wrap(t, "as", 10.8, PW - 2 * M):
            p.t(M, y, ln, "as", 10.8, INK)
            y += 14.5
        y += 7


def results_placeholder(doc, n, title_segs):
    p = P(doc, n)
    p.heading(title_segs, 110, size=44)
    # 2x2 photo placeholder grid
    cols, rows = 2, 2
    gx0, gx1 = M, PW - M
    gy0, gy1 = 180, 760
    cw = (gx1 - gx0 - 30) / cols
    rh = (gy1 - gy0 - 30) / rows
    for r in range(rows):
        for c in range(cols):
            x0 = gx0 + c * (cw + 30)
            y0 = gy0 + r * (rh + 30)
            p.rect(x0, y0, x0 + cw, y0 + rh,
                   fill=DUSTPINK, stroke=RULE)
            p.tc(x0 + cw / 2, y0 + rh / 2,
                 "[ Before / After ]", "asi", 11, MUTED)


def community_placeholder(doc, n):
    p = P(doc, n)
    p.heading([("Our ", False), ("Community Success", True)], 110,
              size=40)
    # screenshot placeholders
    y = 180
    for i in range(3):
        for c in range(2):
            x0 = M + c * (PW - 2 * M) / 2 + (8 if c else 0)
            x1 = x0 + (PW - 2 * M) / 2 - 8
            p.rect(x0, y, x1, y + 160, fill=WHITE, stroke=RULE)
            p.tc((x0 + x1) / 2, y + 80,
                 "[ Member screenshot ]", "asi", 10.5, MUTED)
        y += 180


def disclaimer_pill(p, y):
    p.rect(M, y, PW - M, y + 100, fill=WHITE, stroke=RULE, w=0.8)
    lines = [
        "The weight loss results shown are individual experiences "
        "and are not guaranteed.",
        "Each person's body, metabolism, and level of commitment "
        "are unique, so results will vary.",
        "We recommend consulting a GP or healthcare provider before "
        "starting any weight loss programme.",
    ]
    ty = y + 22
    for ln in lines:
        p.tc(PW / 2, ty, ln, "as", 9.8, INK)
        ty += 16


# ====================================================== tips
def tips_1(doc, n):
    p = P(doc, n)
    # banner band like the original
    p.rect(0, 0, PW, 220, fill=BEIGE)
    p.t(M, 130, "Important Tips for", "lb", 38, NAVY)
    p.t(M, 178, "Getting Started", "lbi", 38, NAVY)
    intro = [
        "The 5-day fat loss reset meal guide can include whatever "
        "variation of the meal options you want. It's fully "
        "adjustable depending on the recipes and ingredients you "
        "like.",
        "Pick the recipe you like most from the reset meal overview "
        "for each meal (breakfast, lunch, dinner and snack). Feel "
        "free to duplicate recipes that are easy to batch.",
        "Feel free to swap each ingredient around. Or leave out "
        "ingredients you don't like. Season foods more if required.",
        "Go with the flow of the recipes in the guide in terms of "
        "variety, or adjust and simplify by repeating meals more "
        "often. This will not impact results.",
    ]
    y = 250
    for t in intro:
        for ln in wrap(t, "as", 11, PW - 2 * M):
            p.t(M, y, ln, "as", 11, INK)
            y += 15
        y += 8
    p.section_title([("Meals", False)], y + 10, underline=True, size=18)
    bullets = [
        "Pick one breakfast for 5 days or pick and choose from the "
        "guide if you want more variety.",
        "If unable to have one of the lunch recipes due to being out "
        "or busy, go for a protein based salad, soup or any egg "
        "dish.",
        "Repeat lunches more often if that's easier (e.g. an easy "
        "batch recipe can cover multiple days).",
        "Always have a portion of protein in each meal. If having "
        "soup, have a piece of protein on the side such as a boiled "
        "egg or some meat / fish.",
    ]
    by = y + 38
    for b in bullets:
        ny = p.bullet(M + 6, by, b, "as", 11, INK, PW - 2 * M - 6, 15)
        by = ny + 6


def tips_2(doc, n):
    p = P(doc, n)
    p.section_title([("Drinks", False)], 110, underline=True, size=18)
    by = 138
    for b in [
        "Aim to have only one milky coffee per day (i.e. latte / "
        "cappuccino). Tea and coffee with small amounts of milk are "
        "fine.",
        "Aim for 8 glasses of water per day approximately if you "
        "can (see the Drink Tips section for ideas on how to drink "
        "more water).",
    ]:
        ny = p.bullet(M + 6, by, b, "as", 11, INK, PW - 2 * M - 6, 15)
        by = ny + 6

    p.section_title([("Snacks", False)], by + 18, underline=True, size=18)
    by = by + 46
    for b in [
        "Aim for one bigger snack between lunch and dinner to manage "
        "appetite and sugar cravings. Snacking at other times of "
        "the day is fine but aim to only snack when physically "
        "hungry.",
    ]:
        ny = p.bullet(M + 6, by, b, "as", 11, INK, PW - 2 * M - 6, 15)
        by = ny + 6

    p.section_title([("Portions", False)], by + 18, underline=True,
                    size=18)
    by = by + 46
    for b in [
        "If you feel that it is too much food for you, don't eat it "
        "all. Listen to your own body and don't eat just for the "
        "sake of eating.",
        "Eat until you've had enough and feel satisfied. Recipes "
        "are for 1 serving unless stated otherwise.",
    ]:
        ny = p.bullet(M + 6, by, b, "as", 11, INK, PW - 2 * M - 6, 15)
        by = ny + 6

    p.section_title([("Note", False)], by + 18, underline=True, size=18)
    by = by + 46
    p.bullet(M + 6, by, "Don't expect perfection — just do your best.",
             "as", 11, INK, PW - 2 * M - 6, 15)


# ====================================================== guidelines + overview
def guidelines(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 260, fill=BEIGE)
    p.t(M, 140, "The 5 Day", "lb", 42, NAVY)
    p.t(M, 188, "Fat Loss Reset", "lb", 42, NAVY)
    p.t(M, 236, "Guidelines", "lbi", 32, NAVY)
    rules = [
        "Eat breakfast within 1 hour of waking (if possible)",
        "Ensure every breakfast has a protein element**",
        "Include protein with every meal",
        "Reduce processed foods and added sugars",
        "Eat 3 healthy meals per day with healthy snacks in between "
        "when hungry",
        "Stay hydrated by drinking at least 8 glasses of water per "
        "day",
        "Move your body daily — even a 20 minute walk counts",
    ]
    cy = 320
    for r in rules:
        navy_check(p, M, cy, sz=22)
        lines = wrap(r, "as", 11.5, 410)
        ty = cy + 16
        for ln in lines:
            p.t(M + 50, ty, ln, "as", 11.5, INK)
            ty += 15
        cy = max(cy + 44, ty + 6)
    p.t(M + 50, cy + 12,
        "**if using dairy-free milk, add protein powder",
        "asi", 9.5, MUTED)


def meal_overview(doc, n):
    p = P(doc, n)
    # heading
    p.heading([("The 5 Day Fat Loss Reset", False)], 90, size=22,
              center=True)
    p.heading([("Meal ", False), ("Overview", True)], 122, size=22,
              center=True)
    p.line(PW / 2 - 40, 134, PW / 2 + 40, 134, color=CORAL, w=2.0)
    # breakfast
    p.section_title([("Breakfast Options", True)], 180, underline=False,
                    size=16)
    bk_cols = [("Option 1", "[ recipe 1 ]"),
               ("Option 2", "[ recipe 2 ]"),
               ("Option 3", "[ recipe 3 ]")]
    _draw_overview_table(p, 200, bk_cols)
    p.section_title([("Morning Snack", True)], 280, underline=False,
                    size=16)
    p.t(M, 302, "Opt for smaller snack option. Portion of fruit / "
        "vegetables if hungry. (See snack tips for more info)",
        "as", 10, INK)
    p.section_title([("Lunch Options", True)], 332, underline=False,
                    size=16)
    lu_cols = [("Option 1", "[ recipe 1 ]"),
               ("Option 2", "[ recipe 2 ]"),
               ("Option 3", "[ recipe 3 ]"),
               ("Option 4", "[ recipe 4 ]")]
    _draw_overview_table(p, 352, lu_cols)
    p.section_title([("Mid-Afternoon Snack Options", True)], 432,
                    underline=False, size=16)
    p.t(M, 454, "Opt for bigger snack option. Select one of our snack "
        "recipes or bigger snack options inside the guide.",
        "as", 10, INK)
    p.section_title([("Dinner Options", True)], 484, underline=False,
                    size=16)
    dn_cols = [("Option 1", "[ recipe 1 ]"),
               ("Option 2", "[ recipe 2 ]"),
               ("Option 3", "[ recipe 3 ]"),
               ("Option 4", "[ recipe 4 ]"),
               ("Option 5", "[ recipe 5 ]")]
    _draw_overview_table(p, 504, dn_cols)
    note = ("Choose any breakfast, lunch or dinner option for each "
            "day from the meal overview above that suits you best. "
            "Feel free to mix and match according to your "
            "preferences. Batch cook to repeat a recipe or choose a "
            "new recipe each day.")
    y = 600
    for ln in wrap(note, "as", 10, PW - 2 * M):
        p.t(M, y, ln, "as", 10, INK)
        y += 14


def _draw_overview_table(p, y0, cols):
    n = len(cols)
    w = (PW - 2 * M) / n
    for i, (head, body) in enumerate(cols):
        x0 = M + i * w
        x1 = x0 + w - 4
        p.rect(x0, y0, x1, y0 + 28, stroke=NAVY, w=0.8)
        p.tc((x0 + x1) / 2, y0 + 18, head, "asb", 9.5, NAVY)
        p.rect(x0, y0 + 32, x1, y0 + 60, stroke=NAVY, w=0.8)
        p.tc((x0 + x1) / 2, y0 + 50, body, "asi", 9, MUTED)


# ====================================================== recipe pages
def section_divider(doc, n, title_two_words):
    """Divider page with decorative circle + italic title."""
    p = P(doc, n)
    p.rect(0, 0, PW, 280, fill=DUSTPINK)
    cx, cy = PW / 2, 320
    r = 175
    p.circle(cx, cy, r + 8, stroke=CORAL, w=1.5)
    p.circle(cx, cy, r, fill=WHITE, stroke=CORAL, w=1.5)
    p.tc(cx, cy + 4, "[ photo ]", "asi", 12, MUTED)
    # title — first word italic, second word regular
    w1, w2 = title_two_words
    t1 = tw(w1, "lbi", 44)
    t2 = tw(w2, "lb", 44)
    p.tc(cx, cy + r + 60, w1, "lbi", 44, NAVY)
    p.tc(cx, cy + r + 100, w2, "lb", 44, NAVY)


def recipe_placeholder(doc, n, slot=""):
    p = P(doc, n)
    # blue title strips
    p.rect(M, 80, PW - M, 84, fill=NAVY)
    p.t(M, 130, "[ Recipe Name ]", "lb", 22, CORAL)
    # serves icon area
    p.tc(PW - M - 30, 124, "Serves: ?", "asb", 10, INK)
    p.t(PW - M - 80, 138, slot, "asb", 10, CORAL)
    p.line(M, 158, PW - M, 158, color=NAVY, w=1.5)
    # 2 column
    mid = PW / 2 - 4
    p.t(M, 184, "Ingredients:", "asb", 11, INK)
    p.t(mid + 14, 184, "Instructions:", "asb", 11, INK)
    # dotted vertical divider
    yy = 196
    while yy < 740:
        p.pg.draw_circle((mid, yy), 0.6, color=None, fill=MUTED)
        yy += 5
    # placeholder bullets
    for i, y in enumerate(range(210, 380, 18)):
        p.bullet(M + 4, y, "[ ingredient ]", "asi", 10, MUTED,
                 mid - M - 14, 15)
    for i, y in enumerate(range(210, 400, 22)):
        p.t(mid + 18, y, f"{i + 1}.  [ step ]", "asi", 10, MUTED)
    # bottom strip
    p.rect(M, 780, PW - M, 784, fill=NAVY)


# ====================================================== swop list
SWOP_INTRO = [
    "The meals/recipes are flexible — leave out any ingredients you "
    "do not enjoy or replace with another alternative. Reduce or "
    "increase flavours to your own liking.",
    "Fruits and vegetables can be changed. If you do not like "
    "carrots, swap with peppers, courgettes with peas, etc.",
    "If you do not want chicken, swap with another meat. If you do "
    "not like fish, swap with another protein. Use vegetarian "
    "sausages if you don't eat meat.",
    "You can leave out ingredients you do not want, add or decrease "
    "herbs and spices, taste everything to suit your preferences.",
    "Everything can be adjusted and, as long as the adjustment is "
    "done within the right group as shown in the swop list, you can "
    "still get the best possible results.",
]


def swop_intro(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 240, fill=BEIGE)
    p.t(M, 130, "The Food", "lb", 42, NAVY)
    p.t(M, 178, "Swop List", "lbi", 42, NAVY)
    p.t(M, 270, "Don't like an ingredient?", "asb", 14, NAVY)
    p.t(M, 304, "Every single ingredient can ", "lb", 14, NAVY)
    x = M + tw("Every single ingredient can ", "lb", 14)
    p.t(x, 304, "easily be changed", "lbi", 14, CORAL)
    x += tw("easily be changed", "lbi", 14)
    p.t(x, 304, " using our simple ", "lb", 14, NAVY)
    x += tw(" using our simple ", "lb", 14)
    p.t(x, 304, "swop list.", "lbi", 14, CORAL)
    p.t(M, 326, "Just swap around with foods from the same groups.",
        "lb", 14, NAVY)
    y = 380
    for t in SWOP_INTRO:
        for ln in wrap(t, "as", 11, PW - 2 * M):
            p.t(M, y, ln, "as", 11, INK)
            y += 15
        y += 8


def swop_table(doc, n, title, rows, ncols=2):
    """Render a centered table page (ncols = 2 or 3)."""
    p = P(doc, n)
    # outer header
    tx0, tx1 = M - 14, PW - M + 14
    y = 90
    p.rect(tx0, y, tx1, y + 32, stroke=NAVY, w=0.9)
    p.tc(PW / 2, y + 21, title, "asb", 12, NAVY)
    y += 36
    if ncols == 3:
        head = ["", "MEDIUM CARB", "HIGH CARB"]
        p.rect(tx0, y, tx1, y + 26, stroke=NAVY, w=0.8)
        cw = (tx1 - tx0) / 3
        for i, h in enumerate(head):
            cx = tx0 + cw * i + cw / 2
            p.tc(cx, y + 17, h, "asb", 9.5, NAVY)
        y += 30
    cw = (tx1 - tx0) / ncols
    for row in rows:
        p.rect(tx0, y, tx1, y + 24, stroke=NAVY, w=0.6)
        for i, cell in enumerate(row):
            cx = tx0 + cw * i + cw / 2
            p.tc(cx, y + 16, cell, "as", 9.3, INK)
        y += 26
        if y > PH - FOOTER_H - 30:
            return


# All the swop list data — sourced from the WLA brand swop tables
PROTEIN_ANIMAL = [
    ("Beef, lamb or pork mince", "100g (3½ oz) — 140g (5 oz)"),
    ("Beef pieces", "100g (3½ oz)"),
    ("Beef sirloin steak", "1 small, (approx. 120g (4 oz))"),
    ("Chicken fillet", "Medium sized, 100g (3½ oz) — 130g (4¾ oz)"),
    ("Chicken thigh", "1 large or 2 small"),
    ("Chorizo", "30g (1 oz)"),
    ("Cod fillet", "175g (6 oz) approx"),
    ("Cubed lamb", "100g (3½ oz)"),
    ("Eggs", "2 eggs"),
    ("Ham", "2 slices"),
    ("Lean bacon / rashers", "2 pieces"),
    ("Pork", "Around 130g pork chop"),
    ("Pork (beef or chicken) sausages", "2 sausages"),
    ("Prawns", "140g (5 oz)"),
    ("Salmon fillet", "1 small approx. 110g (3¾ oz)"),
    ("Salmon (tinned)", "Around 155g / tin"),
    ("Small beef, stewing steak", "110g (4 oz) approx."),
    ("Smoked salmon", "55g (2 oz)"),
    ("Tuna steak", "1 small approx. 110g (3¾ oz)"),
    ("Tuna (tinned)", "1 small can approx. 70g (2½ oz)"),
    ("Turkey or chicken mince", "100g (3½ oz) — 130g (4¾ oz)"),
    ("White fish fillets", "185g (6½ oz)"),
]
PROTEIN_VEGGIE = [
    ("Full-fat Greek yoghurt", "125g (½ cup)"),
    ("Full-fat cottage cheese", "100g (⅔ cup)"),
    ("Halloumi", "70g (2½ oz)"),
    ("Nut roast", "150g (1 cup)"),
    ("Paneer cheese", "70g (2½ oz)"),
    ("Quorn fillet", "1 piece"),
    ("Quorn mince", "75g (3oz)"),
    ("Quorn pieces", "75g (3oz)"),
    ("Ricotta cheese", "30g (2 tablespoons)"),
    ("Semi-skimmed milk", "100ml — 250ml (1 cup)"),
    ("Seitan", "100g (⅔ cup)"),
    ("Tempeh", "100g (⅔ cup)"),
    ("Tofu", "¼ block (115g (4 oz) approx) — 125g (½ cup)"),
    ("Vegetarian sausages", "2 sausages"),
]
LEGUMES = [
    ("Baked beans, reduced sugar", "3 tablespoons", "> 3 tablespoons"),
    ("Black beans", "3 tablespoons", "> 3 tablespoons"),
    ("Butter beans", "3 tablespoons", "> 3 tablespoons"),
    ("Cannellini beans", "3 tablespoons", "> 3 tablespoons"),
    ("Chickpeas", "3 tablespoons", "> 3 tablespoons"),
    ("Falafels", "2-3 pieces", "> 3 pieces"),
    ("Haricot beans", "3 tablespoons", "> 3 tablespoons"),
    ("Hummus", "1 tablespoon", "> 1 tablespoon"),
    ("Pinto beans", "3 tablespoons", "> 3 tablespoons"),
    ("Red kidney beans", "3 tablespoons", "> 3 tablespoons"),
    ("Red lentils", "3 tablespoons", "> 3 tablespoons"),
    ("Soya or edamame beans", "3 tablespoons", "> 3 tablespoons"),
    ("Split peas", "3 tablespoons", "> 3 tablespoons"),
    ("Mixed beans", "3 tablespoons", "> 3 tablespoons"),
]
CARBS = [
    ("Brown bread", "1 medium slice", "2 medium slices"),
    ("Brown bread roll", "1 small", "1 large"),
    ("Brown rice", "30-40g", "> 40g"),
    ("Buckwheat", "30-40g", "> 40g"),
    ("Bulgar wheat", "30-40g", "> 40g"),
    ("Couscous, whole wheat", "30-40g", "> 40g"),
    ("Flour, wholewheat", "1 - 2 tablespoons", "> 2 tablespoons"),
    ("Giant couscous, whole wheat", "30-40g", "> 40g"),
    ("Oat flakes", "1 tbsp — 40g (½ cup)", "> 40g"),
    ("Orzo", "30-40g", "> 40g"),
    ("Porridge oats", "1 tbsp — 40g (½ cup)", "> 40g"),
    ("Potatoes", "< 100g", "> 100g"),
    ("Quinoa", "30-40g", "> 40g"),
    ("Soba noodles", "30-40g", "> 40g"),
    ("Sugar free muesli", "30g (⅓ cup)", "> 30g"),
    ("Sweet potato", "< 100g", "> 100g"),
    ("Whole grain rice", "30-40g", "> 40g"),
    ("Whole wheat tortilla wrap", "1 small wrap", "1 large wrap"),
    ("Whole wheat pasta", "30-40g", "> 40g"),
    ("Wholewheat bread", "1 slice", "2 slices"),
    ("Wholewheat noodles", "30-40g", "> 40g"),
    ("Wholewheat spaghetti", "30-40g", "> 40g"),
]
FRUITS_VEG = [
    ("Apple", "1 small"),
    ("Aubergine", "½ average"),
    ("Avocado", "½ small / ¼ large"),
    ("Banana", "½ - 1 small"),
    ("Beansprouts", "100g (1¼ cups)"),
    ("Blueberries", "15 pieces"),
    ("Broccoli", "140g (2 cups)"),
    ("Butternut squash", "70g (½ cup) — 140g (1 cup)"),
    ("Cabbage", "80g"),
    ("Canned tomatoes", "150g (¾ cup) — 200g (1 cup)"),
    ("Carrot", "1 medium"),
    ("Cauliflower", "100g (½ cup)"),
    ("Cherry tomatoes", "6 pieces"),
    ("Chopped tomatoes", "100g (½ cup)"),
    ("Corn on the cob", "1 medium sized"),
    ("Courgette", "80g (½ cup)"),
    ("Cranberries, fresh or frozen", "40g (½ cup)"),
    ("Cucumber", "½ average or 4 mini"),
    ("Dates", "2-3 dates"),
    ("Dried fruit (raisins, sultanas)", "1 tablespoon — 30g"),
    ("Frozen mango", "70g (½ cup) — 125g (¾ cup)"),
    ("Frozen peas", "3 tablespoons"),
    ("Fruit salad of your choice", "100g (¾ cup)"),
    ("Green beans", "4 tablespoons — 80g (1 cup)"),
    ("Green pepper", "½ average"),
    ("Kale", "4 tablespoons"),
    ("Mangetout", "10 pieces"),
    ("Mixed berries, frozen", "3 tablespoons"),
    ("Mixed salad leaves", "50g (2 cup)"),
    ("Mushrooms", "75g (⅔ cup)"),
    ("Parsnip", "1 small"),
    ("Pineapple", "4 rings"),
    ("Portobello Mushrooms", "2 mushrooms"),
    ("Raspberries", "50g (½ cup)"),
    ("Red Pepper", "½ average"),
    ("Rocket", "50g (2 cups)"),
    ("Sauté vegetables", "250g (2 cups)"),
    ("Spinach leaves", "1 cup — 40g (1¼ cup) / 1 cereal bowl"),
    ("Strawberries", "7-8 pieces"),
    ("Sundried tomato", "3 pieces"),
    ("Sweetcorn", "2 tablespoons"),
    ("Vegetable — stir fry packet", "200g"),
    ("Watercress", "1 cup"),
]
FATS = [
    ("Almond butter", "1 tablespoon"),
    ("Avocado", "¼ or 35g frozen"),
    ("Butter, unsalted", "1 teaspoon"),
    ("Cheddar cheese", "15-30g (⅓ cup)"),
    ("Chia seeds", "1 teaspoon"),
    ("Chocolate chips, dark", "1 tsp up to 80g (⅓ cup)"),
    ("Coconut milk, canned", "100g (½ cup) — 200g (1 cup)"),
    ("Cream", "1 tablespoon"),
    ("Cream cheese", "1 tablespoon"),
    ("Creme fraiche, full fat", "1 tablespoon"),
    ("Desiccated coconut", "1 tsp up to 45g (½ cup)"),
    ("Feta cheese", "30g (¼ cup)"),
    ("Flaxseed", "1 tsp up to 50g (⅓ cup)"),
    ("Full-fat goats cheese", "30g (¼ cup)"),
    ("Green pesto", "1 tablespoon"),
    ("Mayonnaise, full-fat", "1 teaspoon"),
    ("Mixed nuts", "1 tablespoon — 30g"),
    ("Olive oil", "1 teaspoon"),
    ("Olives", "6 pieces"),
    ("Parmesan cheese", "15-30g (⅓ cup)"),
    ("Peanut butter", "1 tablespoon"),
    ("Salad cream, full-fat", "1 teaspoon"),
    ("Sesame seeds", "1 teaspoon"),
    ("Shredded mozzarella cheese", "30g (⅓ cup)"),
    ("Sour cream, full-fat", "1 tablespoon"),
    ("Sunflower and pumpkin seed mix", "1 teaspoon"),
    ("Sunflower seeds", "1 teaspoon"),
    ("Tzatziki", "1 tablespoon"),
    ("Vegetarian cheddar cheese", "15-30g (⅓ cup)"),
]
OTHER = [
    ("Balsamic vinegar", "1 tablespoon"),
    ("Brown sauce", "1 teaspoon"),
    ("Chilli sauce", "1 teaspoon"),
    ("Crackers (cream crackers, rye crispbread etc.)", "3 pieces"),
    ("Curry paste", "1 tablespoon"),
    ("Honey", "1 teaspoon"),
    ("Jam", "1 teaspoon"),
    ("Lentil crisps", "20-25g"),
    ("Maple syrup", "1 teaspoon"),
    ("Popcorn, plain", "20-25g"),
    ("Salsa or tomato relish, reduced sugar", "1 tablespoon"),
    ("Soy sauce, reduced-salt", "1 tablespoon"),
    ("Teriyaki sauce", "2 tablespoons"),
    ("Tomato ketchup, reduced sugar", "1 teaspoon"),
    ("Tomato puree", "1 tbsp — 120ml (1½ cup)"),
    ("Worcestershire Sauce", "1 tablespoon"),
]


def build_swop_pages(doc, start_n):
    """Render the swop list across multiple pages. Returns next n."""
    n = start_n
    # protein animal — fits one page (22 rows)
    swop_table(doc, n, "PROTEIN — ANIMAL SOURCES", PROTEIN_ANIMAL)
    n += 1
    # protein veggie + quorn etc on next page
    swop_table(doc, n, "PROTEIN — VEGETARIAN SOURCES", PROTEIN_VEGGIE)
    n += 1
    # legumes
    swop_table(doc, n, "LEGUMES", LEGUMES, ncols=3)
    n += 1
    # carbs split across two pages
    half = len(CARBS) // 2
    swop_table(doc, n, "CARBOHYDRATES", CARBS[:half], ncols=3)
    n += 1
    swop_table(doc, n, "CARBOHYDRATES", CARBS[half:], ncols=3)
    n += 1
    # fruits/veg split
    half = len(FRUITS_VEG) // 2 + 1
    swop_table(doc, n, "FRUIT AND VEGETABLES", FRUITS_VEG[:half])
    n += 1
    swop_table(doc, n, "FRUIT AND VEGETABLES", FRUITS_VEG[half:])
    n += 1
    # fats split
    half = len(FATS) // 2
    swop_table(doc, n, "FATS", FATS[:half])
    n += 1
    swop_table(doc, n, "FATS", FATS[half:])
    n += 1
    # other
    swop_table(doc, n, "OTHER", OTHER)
    n += 1
    return n


# ====================================================== drink + snack
def drink_tips(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 220, fill=BEIGE)
    p.tc(PW / 2, 130, "Drink Tips", "lbi", 44, NAVY)
    p.section_title([("Water Tips", True)], 252, underline=True,
                    size=18)
    items = [
        ("1. Get a pretty reusable water bottle",
         "Keeping a water bottle handy can serve as a visual "
         "reminder to drink more water. If you see the bottle on "
         "your desk or table, you will constantly be reminded to "
         "drink more. It can also be challenging to drink enough "
         "water when travelling or on the go. Fill your water "
         "bottle before you leave home, and bring it along on your "
         "daily travels."),
        ("2. Add water to your daily routine",
         "Make drinking water a habit by drinking at set points "
         "during the day, e.g. as soon as you get up, drink before "
         "a meal, drink while at the computer or watching TV. "
         "Sipping consistently throughout the day is another easy "
         "way to help you meet your fluid goals."),
        ("3. Make it fruity",
         "If you dislike the flavour of water, or just need a bit "
         "of flavour to help you drink more, you have many choices. "
         "Try lemon, lime, orange, cucumber, watermelon, kiwi or "
         "strawberries — or fresh herbs like mint."),
        ("4. Eat your water",
         "One simple way to get more water is to eat more foods "
         "that are high in water. Lettuce, celery, cucumber, "
         "watermelon and grapefruit are all great options."),
    ]
    y = 290
    for title, body in items:
        p.t(M, y, title, "asb", 11, NAVY)
        y += 16
        for ln in wrap(body, "as", 10.5, PW - 2 * M):
            p.t(M, y, ln, "as", 10.5, INK)
            y += 14
        y += 8
    # coffee note in coral box
    p.rect(M, y + 6, PW - M, y + 60, stroke=NAVY, w=0.8)
    p.t(M + 16, y + 26, "You can have one milky coffee (latte or "
        "cappuccino) per day.", "as", 10.5, INK)
    p.t(M + 16, y + 46, "Multiple teas with a little milk are also "
        "fine — just make sure you're also drinking water.",
        "as", 10.5, INK)


def snack_tips_1(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 220, fill=BEIGE)
    p.tc(PW / 2, 130, "Snack Tips", "lbi", 44, NAVY)
    y = 260
    p.t(M, y, "Snacking System", "asb", 12, NAVY)
    y += 18
    intro = ("We recommend sticking to three balanced meals per day, "
             "with snacks in between but only if you're truly hungry. "
             "The key is to listen to your body and respond to your "
             "own hunger signals.")
    for ln in wrap(intro, "as", 11, PW - 2 * M):
        p.t(M, y, ln, "as", 11, INK)
        y += 15
    y += 8
    p.bullet(M, y, "Mid-Morning Snacks", "asb", 11, NAVY, 400, 15)
    y += 18
    for ln in wrap("Most people find they don't need a snack between "
                   "breakfast and lunch. However, if you do feel "
                   "genuinely hungry, choose a light option like a "
                   "piece of fruit or raw vegetables.",
                   "as", 11, PW - 2 * M):
        p.t(M + 14, y, ln, "as", 11, INK)
        y += 15
    y += 10
    p.bullet(M, y, "Afternoon Snacks", "asb", 11, NAVY, 400, 15)
    y += 18
    for ln in wrap("The gap between lunch and dinner tends to be "
                   "longer, which is why many people benefit from a "
                   "more substantial snack in the afternoon. We call "
                   "these the \"bigger\" snack options. This can help "
                   "you avoid the 3pm slump and reduce the temptation "
                   "to reach for sugary or processed foods.",
                   "as", 11, PW - 2 * M - 14):
        p.t(M + 14, y, ln, "as", 11, INK)
        y += 15
    y += 14
    p.t(M, y, "Snack Amounts — What's Right for You?", "asb", 11,
        NAVY)
    y += 16
    for ln in wrap("The number and size of snacks you need can vary "
                   "depending on your lifestyle:",
                   "as", 11, PW - 2 * M):
        p.t(M, y, ln, "as", 11, INK)
        y += 15
    y += 4
    for label, txt in [
        ("Very active or exercise regularly?",
         " You may benefit from additional bigger snacks to fuel "
         "your energy needs."),
        ("Less active or sedentary?",
         " You might find you need fewer snacks."),
    ]:
        p.bullet(M, y, label + txt, "as", 11, INK, PW - 2 * M, 15)
        y += 26
    y += 8
    p.t(M, y, "Final Tips:", "asb", 11, NAVY)
    y += 16
    for f in [
        "Eat when you're hungry — not out of boredom or habit.",
        "Pause and check in with your body before reaching for a "
        "snack.",
        "Aim for nourishment — every bite is a chance to fuel your "
        "body well!",
    ]:
        p.bullet(M, y, f, "as", 11, INK, PW - 2 * M, 15)
        y += 22


def snack_tips_2_fruitveg(doc, n):
    p = P(doc, n)
    p.heading([("Fruit and Vegetables ", False),
               ("Snack Inspiration", True)], 110, size=24)
    items = [
        "Apples", "Asparagus", "Aubergine", "Banana (no more than 1 per day)",
        "Beetroot", "Blackberries", "Blueberries", "Bok Choy",
        "Broccoli", "Carrots", "Celery", "Cherries",
        "Courgette", "Cranberries (fresh)", "Cucumber", "Grapefruit",
        "Grapes (1 cup)", "Kelp", "Kiwi", "Mandarins",
        "Mango", "Melon", "Mushrooms", "Onions",
        "Orange (1 large)", "Pears", "Peppers", "Pineapple (1 cup)",
        "Plums", "Radishes", "Raspberries", "Spinach",
        "Strawberries", "Sugar snap peas (1 cup)", "Tomatoes",
        "Watercress",
    ]
    cols, rows = 3, 12
    gx0, gx1 = M - 14, PW - M + 14
    gy0 = 200
    cw = (gx1 - gx0) / cols
    rh = 38
    for i, it in enumerate(items):
        if i >= cols * rows:
            break
        c = i % cols
        r = i // cols
        x0 = gx0 + c * cw
        y0 = gy0 + r * rh
        p.rect(x0 + 4, y0, x0 + cw - 4, y0 + rh - 4,
               stroke=NAVY, w=0.6)
        p.tc(x0 + cw / 2, y0 + 22, it, "as", 9, INK)


def snack_tips_3_bigger(doc, n):
    p = P(doc, n)
    intro = [
        "We also recommend bigger snacks. With regards to \"bigger\" "
        "snacks, some women may only need one per day and others "
        "more. If you exercise regularly you may need more compared "
        "to someone that is less mobile.",
        "It is recommended to have a bigger snack between lunch and "
        "dinner — this will prevent sugar cravings and support "
        "appetite until dinner. You may require another snack in "
        "the evening. Some days you may need 2 bigger snacks and "
        "some days 1. Tune in and be flexible based on how you feel.",
    ]
    y = 100
    for t in intro:
        for ln in wrap(t, "as", 11, PW - 2 * M):
            p.t(M, y, ln, "as", 11, INK)
            y += 15
        y += 6
    # header
    y += 10
    p.rect(M - 14, y, PW - M + 14, y + 30, stroke=NAVY, w=0.8)
    p.tc(PW / 2, y + 21, "BIGGER SNACK INSPIRATION", "asb", 12, NAVY)
    y += 34
    snacks = [
        "3 crackers with nut butter, cream cheese, cottage cheese, "
        "hummus, avocado, cheddar or tuna",
        "1 natural cereal bar of your choice (Nakd brand is a "
        "healthy option)",
        "Apple slices with 1 tablespoon of nut butter",
        "Small handful of nuts and raisins",
        "1 banana sliced and topped with 1 tablespoon of nut butter",
        "2 medjool dates and cream cheese or nut butter",
        "1 cup of grapes and 1 boiled egg",
        "2 boiled eggs",
        "30g dark chocolate",
        "1 cup of homemade popcorn",
        "125g of Greek yoghurt and fruit",
    ]
    for sn in snacks:
        p.rect(M - 14, y, PW - M + 14, y + 38, stroke=NAVY, w=0.5)
        lines = wrap(sn, "as", 9.8, (PW - 2 * M))
        ty = y + (38 - (len(lines) - 1) * 12) / 2 + 4
        for ln in lines:
            p.tc(PW / 2, ty, ln, "as", 9.8, INK)
            ty += 12
        y += 40


def snack_tips_4_recommended(doc, n):
    p = P(doc, n)
    p.section_title([("Some ", False), ("More Recommended Snacks", True)],
                    110, underline=True, size=24)
    items = [
        "Lindt Dark Chocolate (70%+ Cocoa)",
        "Propercorn Sweet & Salty",
        "Nakd Bars",
        "Deliciously Ella Hazelnut Bites",
        "Deliciously Ella Dipped Almonds",
        "Nush Strawberry Yoghurt & Berries",
        "Bear Fruit Rolls",
        "Deliciously Ella Oat Bars",
    ]
    cols, rows = 3, 3
    gx0, gx1 = M, PW - M
    gy0 = 180
    cw = (gx1 - gx0) / cols
    rh = 170
    for i, it in enumerate(items):
        c = i % cols
        r = i // cols
        x0 = gx0 + c * cw + 8
        y0 = gy0 + r * rh
        p.rect(x0, y0, x0 + cw - 16, y0 + 110,
               fill=DUSTPINK, stroke=RULE)
        p.tc(x0 + (cw - 16) / 2, y0 + 60, "[ image ]", "asi", 10, MUTED)
        lines = wrap(it, "as", 10, cw - 24)
        ty = y0 + 130
        for ln in lines:
            p.tc(x0 + (cw - 16) / 2, ty, ln, "as", 10, INK)
            ty += 13


# ====================================================== educational

def why_blood_sugar(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 280, fill=BEIGE)
    p.t(M, 140, "Why Balanced", "lb", 36, NAVY)
    p.t(M, 184, "Blood Sugar", "lbi", 36, NAVY)
    p.t(M, 228, "Supports Fat Loss", "lb", 30, NAVY)
    y = 320
    intro = ("Maintaining balanced blood sugar levels is a key part "
             "of fat loss. Fluctuations in blood sugar drive "
             "cravings, energy crashes and over-eating. Keeping "
             "blood sugar steady supports your fat loss goals and "
             "your energy at the same time.")
    for ln in wrap(intro, "as", 11.5, PW - 2 * M):
        p.t(M, y, ln, "as", 11.5, INK)
        y += 16
    y += 16
    p.t(M, y, "Here's why balanced blood sugar matters:", "asb", 11.5,
        NAVY)
    y += 26
    icons = [
        ("Reduced desire for sugar", "Improved mood",
         "More control around food"),
        ("Weight stabilises / weight reduction",
         "Reduced cravings", "Appetite falls / stabilises"),
    ]
    for row in icons:
        for i, lbl in enumerate(row):
            cx = M + 70 + i * (PW - 2 * M - 140) / 2
            p.circle(cx, y + 20, 22, fill=BEIGE, stroke=RULE, w=0)
            for j, ln in enumerate(wrap(lbl, "as", 10, 130)):
                p.tc(cx, y + 60 + j * 12, ln, "as", 10, INK)
        y += 110
    p.tc(PW / 2, y + 20, "No extreme highs followed by severe plummets",
         "as", 10.5, INK)


def easily_kickstart_1(doc, n):
    p = P(doc, n)
    p.section_title([("Easily ", False),
                     ("Kickstart Fat Loss", True),
                     (" in 5 Days", False)], 110, underline=True,
                    size=24)
    intro = ("When the right amount of food is consumed at the right "
             "times, this will result in balanced blood sugar levels "
             "throughout the day (when less sugar is consumed "
             "overall). The body can handle some sugar but excessive "
             "amounts have an impact on fat loss.")
    y = 160
    for ln in wrap(intro, "as", 11.5, PW - 2 * M):
        p.t(M, y, ln, "as", 11.5, INK)
        y += 16
    # diagram 1
    y += 20
    p.rect(M, y, PW - M, y + 190, stroke=NAVY, w=1.0)
    p.tc(PW / 2, y + 26, "Ideal Blood Sugar Level", "asb", 12, NAVY)
    # sketch a smooth wave
    bx0, by0 = M + 80, y + 140
    bx1, by1 = PW - M - 60, y + 70
    p.pg.draw_line((bx0, by0), (bx1, by0), color=NAVY, width=0.8)
    p.pg.draw_line((bx0, by0), (bx0, by1), color=NAVY, width=0.8)
    # wave using line approximations
    import math
    pts = []
    for i in range(0, 30):
        xx = bx0 + i * (bx1 - bx0) / 30
        yy = by0 - 25 - 22 * math.sin(i / 30 * 6.28 * 1.5)
        pts.append((xx, yy))
    for a, b in zip(pts[:-1], pts[1:]):
        p.pg.draw_line(a, b, color=NAVY, width=1.2)
    p.t(M + 18, y + 110, "Blood Sugar", "asi", 9.5, INK)
    p.t(bx0, by0 + 16, "Breakfast", "asi", 9, INK)
    p.t(bx0 + (bx1 - bx0) / 2 - 14, by0 + 16, "Lunch", "asi", 9, INK)
    p.tr(bx1, by0 + 16, "Dinner", "asi", 9, INK)
    y += 210
    for f in [
        "Peaks after each meal / snack (think balanced meals)",
        "Small peaks and troughs",
        "Blood sugar level dips = signal to eat",
    ]:
        p.bullet(M + 6, y, f, "as", 11, INK, PW - 2 * M - 6, 15)
        y += 22
    y += 10
    # diagram 2
    p.rect(M, y, PW - M, y + 190, stroke=NAVY, w=1.0)
    p.tc(PW / 2, y + 26, "The Rollercoaster Blood Sugar Levels",
         "asb", 12, NAVY)
    p.t(M + 60, y + 80, "*", "as", 12, INK)
    p.t(M + 70, y + 80, "Danger", "asi", 10, INK)
    p.pg.draw_line((M + 100, y + 160), (M + 230, y + 80),
                   color=NAVY, width=1.4)
    p.pg.draw_line((PW - M - 230, y + 160), (PW - M - 165, y + 60),
                   color=NAVY, width=1.4)
    p.pg.draw_line((PW - M - 165, y + 60), (PW - M - 100, y + 160),
                   color=NAVY, width=1.4)
    p.t(PW - M - 100, y + 75, "*", "as", 12, INK)
    p.t(PW - M - 90, y + 75, "Danger", "asi", 10, INK)
    p.t(PW - M - 100, y + 165, "*", "as", 12, INK)
    p.t(PW - M - 90, y + 165, "Danger", "asi", 10, INK)


def easily_kickstart_2(doc, n):
    p = P(doc, n)
    p.rect(M, 90, PW - M, 280, stroke=NAVY, w=1.0)
    p.tc(PW / 2, 120, "The Rollercoaster Blood Sugar Levels",
         "asb", 12, NAVY)
    p.tc(PW / 2, 145, "Highs and Lows", "asi", 11, INK)
    # zig-zag
    pts = [(M + 50, 250), (M + 110, 170), (M + 170, 250),
           (M + 230, 170), (M + 290, 250), (M + 350, 170),
           (M + 410, 250)]
    for a, b in zip(pts[:-1], pts[1:]):
        p.pg.draw_line(a, b, color=NAVY, width=1.3)
    p.t(M + 24, 215, "Blood Sugar", "asi", 9.5, INK)
    p.t(PW / 2 - 10, 270, "Time", "asi", 9.5, INK)
    y = 320
    p.t(M, y, "The day looks like this:", "asi", 11.5, INK)
    y += 24
    for f in ["Extreme highs", "Extreme lows", "Low mood / high mood",
              "Unbalanced overall",
              "More sugar cravings and generally eating more sugar "
              "overall"]:
        p.bullet(M + 6, y, f, "as", 11, INK, PW - 2 * M - 6, 15)
        y += 22
    p.t(M, y + 16,
        "Side Note — fat loss can be extremely difficult here",
        "asi", 11, INK)


def why_breakfast(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 320, fill=BEIGE)
    p.t(M, 150, "Why", "lb", 44, NAVY)
    p.t(M + 110, 150, "Breakfast", "lbi", 44, NAVY)
    p.t(M, 200, "Is Important", "lb", 44, NAVY)
    y = 350
    paras = [
        "When breakfast is skipped, blood sugar levels will continue "
        "to dip and it will be more likely that foods high in sugar "
        "for energy will be consumed. Having breakfast within an "
        "hour of waking will allow blood sugar and insulin levels to "
        "stabilise.",
        "In addition, having a protein element with breakfast will "
        "help with satiety levels (feeling of fullness) and sets the "
        "body up for the day, meaning there will likely be less "
        "snacking on less nutrient-dense options throughout the day "
        "— which is exactly what supports fat loss.",
    ]
    for t in paras:
        for ln in wrap(t, "as", 11.5, PW - 2 * M):
            p.t(M, y, ln, "as", 11.5, INK)
            y += 16
        y += 8
    y += 10
    for ln in [
        "Blood sugar levels dip due to skipping breakfast",
        "This results in looking for something to give a quick "
        "\"hit\" to stop feeling shaky, hungry or tired",
        "High spike followed by a big hit of insulin to remove the "
        "sugar from the blood to the cells",
        "Extreme high followed by extreme slump",
        "The cycle continues",
    ]:
        empty_check(p, M, y - 12, sz=14)
        lines = wrap(ln, "as", 11, PW - 2 * M - 28)
        ty = y
        for L in lines:
            p.t(M + 24, ty, L, "as", 11, INK)
            ty += 15
        y = ty + 6


def why_snacking(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 320, fill=BEIGE)
    p.t(M, 150, "Why", "lb", 44, NAVY)
    p.t(M + 110, 150, "Snacking", "lbi", 44, NAVY)
    p.t(M, 200, "Is Important", "lb", 44, NAVY)
    paras = [
        "Snacking is really important as it helps keep blood sugar "
        "levels steady during the day. If food is eaten at regular "
        "intervals throughout the day, having a dip in the blood "
        "sugar levels will be less likely and therefore reaching "
        "for less nutrient-dense foods for a kick of energy will "
        "not happen.",
        "Snacking is important to bridge the gap between breakfast "
        "and lunch and then lunch and dinner. However, snacks should "
        "not be eaten just for the sake of it — snacking is "
        "supposed to tide the body over until the next meal.",
    ]
    y = 350
    for t in paras:
        for ln in wrap(t, "as", 11.5, PW - 2 * M):
            p.t(M, y, ln, "as", 11.5, INK)
            y += 16
        y += 8
    y += 10
    for ln in [
        "Peaks after each meal / snack (think balanced meals)",
        "Small peaks and troughs",
        "Blood sugar level dips = signal to eat",
    ]:
        empty_check(p, M, y - 12, sz=14)
        p.t(M + 24, y, ln, "as", 11, INK)
        y += 22


def nutrition_formula(doc, n):
    p = P(doc, n)
    p.rect(0, 0, PW, 280, fill=BEIGE)
    p.t(M, 150, "The ", "lb", 44, NAVY)
    p.t(M + tw("The ", "lb", 44), 150, "WLA Nutrition",
        "lbi", 44, NAVY)
    p.t(M, 200, "Formula", "lb", 44, NAVY)
    paras = [
        "At The WLA, we use our unique Nutrition Formula to help "
        "kickstart fat loss in as little as 5 days and support "
        "visible weight loss within a week.",
        "This formula is built around portion control and a healthy "
        "balance of all food groups — carbohydrates, protein, and "
        "fats — rather than restriction or elimination.",
        "The WLA Nutrition Formula focuses on building meals that "
        "are high in protein and adjusted to be low, medium, or "
        "higher in carbohydrates, depending on the meal and the "
        "individual. This structure teaches you how to create "
        "nutritionally balanced meals that support fat loss, "
        "improve health, and help reduce sugar cravings — while "
        "still being realistic and sustainable long term.",
        "Your 5 Day Fat Loss Reset has been designed using this "
        "formula for maximum results. You don't need to calculate "
        "or overthink anything — simply follow the guide and the "
        "setup provided.",
    ]
    y = 320
    for t in paras:
        for ln in wrap(t, "as", 11, PW - 2 * M):
            p.t(M, y, ln, "as", 11, INK)
            y += 15
        y += 7
    p.t(M, y + 4, "The WLA Nutrition Formula focuses on:",
        "asb", 11, NAVY)
    y += 22
    for f in [
        "Reducing carbohydrate intake (not eliminating — just "
        "adjusting amounts)",
        "Reducing processed foods and added sugars",
        "Prioritising whole, nourishing foods",
        "Including snacks when guided by hunger signals",
        "Using an 80:20 approach across the week",
        "Drinking adequate water (around 8 glasses per day)",
        "Including regular daily movement",
    ]:
        p.bullet(M + 6, y, f, "as", 11, INK, PW - 2 * M - 6, 15)
        y += 22


# ====================================================== main
def build():
    doc = fitz.open()
    cover(doc)
    toc(doc, 2)
    welcome(doc, 3)
    mission_1(doc, 4)
    mission_2(doc, 5)
    founder(doc, 6)
    results_placeholder(doc, 7, [("WLA Members ", False),
                                 ("Results", True)])
    results_placeholder(doc, 8, [("WLA Members ", False),
                                 ("Results", True)])
    community_placeholder(doc, 9)
    tips_1(doc, 10)
    tips_2(doc, 11)
    guidelines(doc, 12)
    meal_overview(doc, 13)
    # recipes (placeholders)
    section_divider(doc, 14, ("Breakfast", "Recipes"))
    recipe_placeholder(doc, 15)
    recipe_placeholder(doc, 16)
    section_divider(doc, 17, ("Lunch", "Recipes"))
    recipe_placeholder(doc, 18, slot="15 Min Option")
    recipe_placeholder(doc, 19, slot="Easy Batch")
    recipe_placeholder(doc, 20, slot="Family Fav")
    section_divider(doc, 21, ("Dinner", "Recipes"))
    recipe_placeholder(doc, 22, slot="20 Min Option")
    recipe_placeholder(doc, 23, slot="Family Fav")
    recipe_placeholder(doc, 24, slot="Easy Batch")
    recipe_placeholder(doc, 25, slot="No Fuss, Zero Time")
    section_divider(doc, 26, ("Snack", "Recipes"))
    recipe_placeholder(doc, 27)
    recipe_placeholder(doc, 28)
    # swop list
    swop_intro(doc, 29)
    next_n = build_swop_pages(doc, 30)
    # drink + snack
    drink_tips(doc, next_n)
    snack_tips_1(doc, next_n + 1)
    snack_tips_2_fruitveg(doc, next_n + 2)
    snack_tips_3_bigger(doc, next_n + 3)
    snack_tips_4_recommended(doc, next_n + 4)
    # educational
    why_blood_sugar(doc, next_n + 5)
    easily_kickstart_1(doc, next_n + 6)
    easily_kickstart_2(doc, next_n + 7)
    why_breakfast(doc, next_n + 8)
    why_snacking(doc, next_n + 9)
    nutrition_formula(doc, next_n + 10)

    doc.set_metadata({
        "title": "The 5 Day Fat Loss Reset Guide",
        "author": "The Weight Loss Academy",
        "subject": "A simple 5 day fat loss reset",
        "creator": "The Weight Loss Academy",
    })
    doc.save(OUT, deflate=True, garbage=4)
    print(f"wrote {OUT} ({len(doc)} pages)")


if __name__ == "__main__":
    build()
