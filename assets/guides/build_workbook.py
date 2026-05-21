#!/usr/bin/env python3
"""Rebrand the 4 Week Weight Loss Sprint Workbook into the WLA house
style while preserving every fillable form field.

Strategy: open the original (keeping its AcroForm and all 574 widgets),
paint a new cream / Libre Baskerville design over each page, and
restyle the field widgets in place. No widget is moved, deleted or
recreated; field values are reset so the workbook ships blank.

Run:  python3 build_workbook.py
"""

import os
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
SRC = ("/root/.claude/uploads/9bd63364-1958-4ce6-83b4-cafe30e7c875/"
       "43d9bdd9-4_Week_Weight_Loss_Sprint_Workbook__Fillable.pdf")
OUT = os.path.join(HERE, "..", "4-Week-Weight-Loss-Sprint-Workbook.pdf")

CREAM = (0xF9 / 255, 0xF7 / 255, 0xF4 / 255)
NAVY = (0x00 / 255, 0x30 / 255, 0x60 / 255)
BLUSH = (0xF7 / 255, 0x9F / 255, 0x83 / 255)
BEIGE = (0xE9 / 255, 0xDF / 255, 0xD3 / 255)
INK = (0x33 / 255, 0x33 / 255, 0x33 / 255)
RULE = (0.80, 0.83, 0.87)
WHITE = (1, 1, 1)

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

doc = fitz.open(SRC)
PW, PH = doc[0].rect.width, doc[0].rect.height
M = 51


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
    def __init__(self, page):
        self.pg = page
        for a, fn in FONTS.items():
            page.insert_font(fontname=a, fontfile=os.path.join(FONT_DIR, fn))

    def fill(self):
        self.pg.draw_rect(self.pg.rect, color=None, fill=CREAM)

    def rect(self, x0, y0, x1, y1, fill=None, stroke=None, w=0.8):
        self.pg.draw_rect(fitz.Rect(x0, y0, x1, y1), color=stroke,
                          fill=fill, width=w)

    def line(self, x0, y0, x1, y1, color=RULE, w=0.7):
        self.pg.draw_line((x0, y0), (x1, y1), color=color, width=w)

    def text(self, x, y, s, font, size, color):
        self.pg.insert_text((x, y), s, fontname=font, fontsize=size,
                            color=color)

    def tc(self, cx, y, s, font, size, color):
        self.text(cx - tw(s, font, size) / 2, y, s, font, size, color)

    def tr(self, rx, y, s, font, size, color):
        self.text(rx - tw(s, font, size), y, s, font, size, color)

    def tracked(self, x, y, s, font, size, color, tr):
        cx = x
        for ch in s:
            self.text(cx, y, ch, font, size, color)
            cx += tw(ch, font, size) + tr
        return cx - tr

    def para(self, x, y, s, font, size, color, maxw, lh, center=False):
        for ln in wrap(s, font, size, maxw):
            if center:
                self.tc(x + maxw / 2, y, ln, font, size, color)
            else:
                self.text(x, y, ln, font, size, color)
            y += lh
        return y

    def vcentre(self, x, y0, y1, s, font, size, color, maxw,
                lh, center=False):
        lines = wrap(s, font, size, maxw)
        ty = (y0 + y1) / 2 - (len(lines) - 1) * lh / 2 + size * 0.34
        for ln in lines:
            if center:
                self.tc(x + maxw / 2, ty, ln, font, size, color)
            else:
                self.text(x, ty, ln, font, size, color)
            ty += lh

    def heading(self, segs, y, size=25):
        cx = M
        for txt, ital in segs:
            f = "lbi" if ital else "lb"
            self.text(cx, y, txt, f, size, NAVY)
            cx += tw(txt, f, size)
        self.line(M, y + 9, M + 52, y + 9, color=BLUSH, w=2.4)

    def kicker(self, y):
        x = self.tracked(M, y, "A WORKBOOK", "asb", 9, NAVY, 1.6)
        self.text(x + 11, y, "·", "asb", 9, BLUSH)
        self.tracked(x + 22, y, "THE WEIGHT LOSS ACADEMY", "asb", 9,
                     NAVY, 1.6)

    def pageno(self, n):
        self.tr(PW - 34, PH - 16, f"{n:02d}", "as", 8.5, NAVY)


def style_field(w):
    """Restyle a widget as a clean WLA input box and clear its value."""
    if w.field_type_string == "CheckBox":
        w.border_color = NAVY
        w.fill_color = WHITE
        w.border_width = 1.0
        try:
            w.field_value = False
        except Exception:
            pass
    else:
        w.border_color = RULE
        w.fill_color = WHITE
        w.border_width = 0.8
        w.text_color = INK
        if not w.text_fontsize or w.text_fontsize > 12:
            w.text_fontsize = 11
        w.field_value = ""
    w.update()


def rows_of(ws, tol=12):
    ws = sorted(ws, key=lambda w: w.rect.y0)
    rows, cur = [], []
    for w in ws:
        if cur and w.rect.y0 - cur[-1].rect.y0 > tol:
            rows.append(sorted(cur, key=lambda w: w.rect.x0))
            cur = []
        cur.append(w)
    if cur:
        rows.append(sorted(cur, key=lambda w: w.rect.x0))
    return rows


def texts(pg):
    return [w for w in pg.widgets() if w.field_type_string == "Text"]


def checks(pg):
    return [w for w in pg.widgets() if w.field_type_string == "CheckBox"]


# =================================================== page builders
def cover(pg):
    d = P(pg)
    d.fill()
    d.kicker(60)
    lines = [("4-Week", "lbi", NAVY), ("Weight Loss Sprint", "lb", BLUSH),
             ("Workbook.", "lbi", NAVY)]
    T = min(min(470 / tw(t[0], t[1], 1) for t in lines), 70)
    lh = T * 1.18
    b1 = 286
    for i, (txt, f, c) in enumerate(lines):
        d.text(M, b1 + i * lh, txt, f, T, c)
    sy = b1 + 2 * lh + 54
    for ln in wrap("Plan your goal, track your habits and review your "
                   "progress — one focused sprint at a time.",
                   "lbi", 13, 350):
        d.text(M, sy, ln, "lbi", 13, BLUSH)
        sy += 20.5
    d.tracked(M, PH - 60, "THE WEIGHT LOSS ACADEMY", "asb", 9, NAVY, 1.6)


def smart_goal(pg):
    d = P(pg)
    d.fill()
    d.heading([("Smart ", False), ("Goal", True)], 41, size=21)
    txt = sorted(texts(pg), key=lambda w: w.rect.y0)
    g1, g2, smart = txt[0:3], txt[3:6], txt[6:11]
    d.vcentre(M, g1[0].rect.y0, g1[-1].rect.y1,
              "What is your overall goal?", "asm", 9.5, NAVY, 96, 12.5)
    d.vcentre(M, g2[0].rect.y0, g2[-1].rect.y1,
              "Why MUST you achieve your goal?", "asm", 9.5, NAVY,
              96, 12.5)
    info = [("S", "Specific", "Create a SPECIFIC goal."),
            ("M", "Measurable", "Your goal should be measurable. How "
             "will you MEASURE your goal? Think about tracking."),
            ("A", "Achievable", "Can you actually achieve this? "
             "Setting an achievable goal sets you up for success, not "
             "disappointment down the line."),
            ("R", "Relevant", "Why do you want to reach this goal? Ask "
             "yourself what is most important to you, then determine "
             "your goals."),
            ("T", "Time Bound", "When do you plan to reach your goal? "
             "This gives you something to work towards and keeps you "
             "on course.")]
    for w, (letter, name, desc) in zip(smart, info):
        r = w.rect
        d.rect(M, r.y0, M + 78, r.y1, fill=BLUSH)
        d.tc(M + 39, (r.y0 + r.y1) / 2 + 16, letter, "lb", 44, WHITE)
        cx0 = M + 86
        d.rect(cx0, r.y0, r.x0 - 6, r.y1, fill=WHITE, stroke=RULE)
        d.text(cx0 + 13, r.y0 + 23, name.upper(), "asb", 10.5, NAVY)
        d.line(cx0 + 13, r.y0 + 28, cx0 + 13 + tw(name.upper(), "asb",
               10.5), r.y0 + 28, color=BLUSH, w=1.4)
        d.para(cx0 + 13, r.y0 + 45, desc, "as", 9.3, INK,
               r.x0 - 6 - cx0 - 24, 12.3)
    d.pageno(2)


def measure_table(d, data, rowsm, top, data2=None):
    """Measurements table. Columns are derived from widget positions
    so the drawn cells abut the form fields. data2 -> two data cols."""
    mx = 150
    if data2:
        dx0, dx1 = data[0].rect.x0 - 5, data[0].rect.x1 + 5
        d2x0 = data2[0].rect.x0 - 5
        cols = [("DESCRIPTION", M, mx), ("METRIC", mx, dx0),
                ("DATA", dx0, dx1), ("HOW TO MEASURE", dx1, d2x0),
                ("DATA", d2x0, PW - M)]
        datacols = {2, 4}
        hsz = 8
    else:
        dx0 = data[0].rect.x0 - 6
        cols = [("DESCRIPTION", M, mx), ("METRIC", mx, 210),
                ("HOW TO MEASURE", 210, dx0), ("DATA", dx0, PW - M)]
        datacols = {3}
        hsz = 8.5
    d.rect(M, top, PW - M, top + 26, fill=NAVY)
    for lbl, x0, x1 in cols:
        d.tc((x0 + x1) / 2, top + 17, lbl, "asb", hsz, WHITE)
    hcol = cols[3] if data2 else cols[2]
    for ri, (w, (desc, metric, how)) in enumerate(zip(data, rowsm)):
        r = w.rect
        for i, (lbl, x0, x1) in enumerate(cols):
            if i not in datacols:
                d.rect(x0, r.y0, x1, r.y1, fill=WHITE, stroke=RULE)
        d.rect(M, r.y0, PW - M, r.y1, fill=None, stroke=RULE)
        d.tc((cols[0][1] + cols[0][2]) / 2, (r.y0 + r.y1) / 2 + 3,
             desc, "asm", 9, NAVY)
        d.vcentre(cols[1][1] + 3, r.y0, r.y1, metric, "as", 8.3, INK,
                  cols[1][2] - cols[1][1] - 6, 10, center=True)
        d.vcentre(hcol[1] + 6, r.y0, r.y1, how, "as", 8.3, INK,
                  hcol[2] - hcol[1] - 12, 10.6, center=True)
        if ri == 0:
            gy0, gy1 = r.y1 + 6, data[1].rect.y0 - 6
            if gy1 - gy0 > 10:
                d.rect(M, gy0, PW - M, gy1, fill=BEIGE)
                d.tc(PW / 2, (gy0 + gy1) / 2 + 3.5, "MEASUREMENTS",
                     "asb", 9, NAVY)


def checkbox_panels(d, left, right, lt, rt, litems, ritems, others):
    panel_top = left[0].rect.y0 - 40
    for col, items, ttl, isleft in [(left, litems, lt, True),
                                    (right, ritems, rt, False)]:
        x0 = M if isleft else 305
        x1 = 285 if isleft else PW - M
        d.rect(x0, panel_top, x1, panel_top + 30, fill=BLUSH)
        d.vcentre(x0 + 10, panel_top, panel_top + 30, ttl, "asb", 8.7,
                  WHITE, x1 - x0 - 20, 10, center=True)
        for c, it in zip(col, items):
            r = c.rect
            d.rect(x0, r.y0 - 4, c.rect.x0 - 8, r.y1 + 4, fill=WHITE,
                   stroke=RULE)
            d.text(x0 + 10, (r.y0 + r.y1) / 2 + 3, it, "as", 9.3, INK)
    for o in others:
        r = o.rect
        d.text(r.x1 + 8, (r.y0 + r.y1) / 2 + 3, "Other", "as", 9.3, INK)


def starting_details(pg):
    d = P(pg)
    d.fill()
    d.heading([("Starting ", False), ("Details", True)], 64)
    data = sorted(texts(pg), key=lambda w: w.rect.y0)
    meas = [w for w in data if w.rect.y0 < 480]
    rowsm = [("Weight", "Stone & Lbs", "Use a scale to note your "
              "starting weight — weigh only at the start and end of "
              "the sprint for a full picture."),
             ("Chest", "cm", "Place on your torso where you are the "
              "biggest."),
             ("Waist", "cm", "Place on your torso where you are the "
              "smallest."),
             ("Hips", "cm", "Place on your hips where you are the "
              "biggest."),
             ("Leg", "cm", "Around 15cm above your knee."),
             ("Arm", "cm", "Around 10cm from your elbow."),
             ("Dress size", "n/a", "n/a")]
    measure_table(d, meas, rowsm, 92)
    cb = checks(pg)
    pc = sorted([c for c in cb if c.rect.y0 < 520],
                key=lambda c: c.rect.x0)
    qy = pc[0].rect
    d.text(M, (qy.y0 + qy.y1) / 2 + 4, "Starting Photo Taken?", "asm",
           10.5, NAVY)
    d.text(pc[0].rect.x1 + 8, (qy.y0 + qy.y1) / 2 + 4, "Yes", "as",
           10.5, INK)
    d.text(pc[1].rect.x1 + 8, (qy.y0 + qy.y1) / 2 + 4, "No", "as",
           10.5, INK)
    cbp = sorted([c for c in cb if c.rect.y0 > 520],
                 key=lambda c: c.rect.y0)
    left = sorted([c for c in cbp if c.rect.x0 < 300],
                  key=lambda c: c.rect.y0)
    right = sorted([c for c in cbp if c.rect.x0 >= 300],
                   key=lambda c: c.rect.y0)
    others = sorted([w for w in texts(pg) if w.rect.y0 > 700],
                    key=lambda w: w.rect.x0)
    checkbox_panels(d, left, right,
                    "Habits before the 4 week sprint",
                    "How do you feel at the start of the sprint?",
                    ["Sugar everyday", "No breakfast",
                     "Chocolate everyday", "No exercise",
                     "No consistency", "A lot of caffeine"],
                    ["Tired", "No energy", "Bloated", "Moody",
                     "Disappointed", "Sluggish"], others)
    d.pageno(3)


def sprint_results_table(pg):
    d = P(pg)
    d.fill()
    d.heading([("4 Week Sprint ", False), ("Results", True)], 64)
    tx = sorted(texts(pg), key=lambda w: w.rect.y0)
    meas = [w for w in tx if w.rect.y0 < 480]
    d1 = sorted([w for w in meas if w.rect.x0 < 300],
                key=lambda w: w.rect.y0)
    d2 = sorted([w for w in meas if w.rect.x0 >= 300],
                key=lambda w: w.rect.y0)
    rowsm = [("Weight", "Stone & Lbs", "Take your finishing weight on "
              "the same scale."),
             ("Chest", "cm", "Place on your torso where you are the "
              "biggest."),
             ("Waist", "cm", "Place on your torso where you are the "
              "smallest."),
             ("Hips", "cm", "Place on your hips where you are the "
              "biggest."),
             ("Leg", "cm", "Around 15cm above your knee."),
             ("Arm", "cm", "Around 10cm from your elbow."),
             ("Dress size", "n/a", "n/a")]
    measure_table(d, d1, rowsm, 92, data2=d2)
    cb = checks(pg)
    pc = sorted([c for c in cb if c.rect.y0 < 540],
                key=lambda c: c.rect.x0)
    qy = pc[0].rect
    d.text(M, (qy.y0 + qy.y1) / 2 + 4, "Finishing Photo Taken?", "asm",
           10.5, NAVY)
    d.text(pc[0].rect.x1 + 8, (qy.y0 + qy.y1) / 2 + 4, "Yes", "as",
           10.5, INK)
    d.text(pc[1].rect.x1 + 8, (qy.y0 + qy.y1) / 2 + 4, "No", "as",
           10.5, INK)
    cbp = sorted([c for c in cb if c.rect.y0 > 540],
                 key=lambda c: c.rect.y0)
    left = sorted([c for c in cbp if c.rect.x0 < 300],
                  key=lambda c: c.rect.y0)
    right = sorted([c for c in cbp if c.rect.x0 >= 300],
                   key=lambda c: c.rect.y0)
    others = sorted([w for w in tx if w.rect.y0 > 760],
                    key=lambda w: w.rect.x0)
    checkbox_panels(d, left, right,
                    "Habits after the 4 week sprint",
                    "How do you feel at the end of the sprint?",
                    ["Limited added sugar", "Breakfast everyday",
                     "More control around food",
                     "Movement routine in place",
                     "Consistent with nutrition",
                     "Reduction in caffeine"],
                    ["Energised", "Lighter", "No bloating", "Happier",
                     "Confident", "Proud"], others)
    d.pageno(21)


def intro(pg):
    d = P(pg)
    d.fill()
    cx = PW / 2
    d.pg.draw_circle((cx, 165), 56, color=None, fill=BLUSH)
    d.tc(cx, 192, "!", "lb", 68, WHITE)
    d.heading([("Plan Your ", False), ("Sprint", True)], 322)
    paras = [
        "For best results, approach your progress in 4 week weight "
        "loss sprints. This means not thinking too far ahead in the "
        "programme, but really giving each month the best that you "
        "have.",
        "Smaller time frames help you keep focus and momentum, which "
        "in turn can lead to better success.",
        "At the start of each month, look ahead and consider what "
        "goal is possible based on what's going on in your life. Some "
        "months your goals will be bigger, and other months smaller.",
    ]
    y = 364
    for p in paras:
        for ln in wrap(p, "as", 12, PW - 2 * M):
            d.text(M, y, ln, "as", 12, INK)
            y += 17
        y += 10
    d.text(M, y + 4, "Let's plan the first sprint.", "asb", 12.5, NAVY)
    d.pageno(4)


def habit_tracker(pg, n, week):
    d = P(pg)
    d.fill()
    d.heading([("Habit Tracker ", False), (f"— Week {week}", True)],
              58, size=24)
    daycb = [c for c in checks(pg) if c.rect.y0 < 560]
    steps_cb = rows_of(daycb)
    drinkcb = sorted([c for c in checks(pg) if c.rect.y0 > 560],
                     key=lambda c: c.rect.x0)
    tx = texts(pg)
    action = sorted([t for t in tx if t.rect.x0 < 60],
                    key=lambda t: t.rect.y0)
    for a in action:
        r = a.rect
        a.rect = fitz.Rect(M, r.y0, 300, r.y1)
        a.update()
    tpw = sorted([t for t in tx if 90 < t.rect.x0 < 160
                  and t.rect.y0 < 560], key=lambda t: t.rect.y0)
    ach = sorted([t for t in tx if t.rect.x0 > 340
                  and t.rect.y0 < 560], key=lambda t: t.rect.y0)
    water = sorted([t for t in tx if 150 < t.rect.x0 < 180
                    and t.rect.y0 > 560], key=lambda t: t.rect.y0)
    diary = sorted([t for t in tx if t.rect.x0 > 340
                    and t.rect.y0 > 560], key=lambda t: t.rect.y0)
    DAYS = ["M", "T", "W", "T", "F", "S", "S"]
    for i in range(3):
        ab = action[i].rect
        cbs = steps_cb[i]
        d.rect(M, ab.y0 - 26, ab.x1, ab.y0 - 4, fill=NAVY)
        d.text(M + 12, ab.y0 - 11, f"ACTION STEP {i + 1}", "asb", 9,
               WHITE)
        for c, dy in zip(cbs, DAYS):
            d.tc((c.rect.x0 + c.rect.x1) / 2, cbs[0].rect.y0 - 8, dy,
                 "asb", 10, NAVY)
        tr = tpw[i].rect
        d.vcentre(M, tr.y0, tr.y1, "Times per week", "asm", 8, NAVY,
                  tr.x0 - M - 4, 9.5)
        arr = ach[i].rect
        d.text(tr.x1 + 8, (arr.y0 + arr.y1) / 2 + 3, "Achieved", "asm",
               9, NAVY)
    # water tracker
    wt = water[0].rect
    d.rect(M, wt.y0 - 30, 300, wt.y0 - 6, fill=NAVY)
    d.tc((M + 300) / 2, wt.y0 - 14, "WATER INTAKE TRACKER", "asb", 9,
         WHITE)
    DN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
          "Saturday", "Sunday"]
    for w, nm in zip(water, DN):
        r = w.rect
        d.rect(M, r.y0, r.x0 - 6, r.y1, fill=BLUSH)
        d.tc((M + r.x0 - 6) / 2, (r.y0 + r.y1) / 2 + 3, nm.upper(),
             "asb", 7.6, WHITE)
    # drinks diary
    if diary and drinkcb:
        cb0 = drinkcb[0].rect
        d.rect(308, cb0.y0 - 32, PW - M, cb0.y0 - 8, fill=NAVY)
        d.tc((308 + PW - M) / 2, cb0.y0 - 16, "JUICE, COFFEE & TEA",
             "asb", 9, WHITE)
        for c, lbl in zip(drinkcb, ["Juice", "Coffee", "Tea"]):
            d.text(c.rect.x1 + 5, (c.rect.y0 + c.rect.y1) / 2 + 3, lbl,
                   "as", 8.8, INK)
        d.text(308, cb0.y1 + 14, "Note any juice, coffee or tea during "
               "the day, including the amount.", "asi", 8.4, INK)
        for w, nm in zip(diary, DN):
            d.text(308, (w.rect.y0 + w.rect.y1) / 2 + 3, nm[:3].upper(),
                   "asb", 8, NAVY)
    d.pageno(n)


def grid_page(pg, n, week, kind):
    d = P(pg)
    d.fill()
    title = "Food Strategy" if kind == "strategy" else "Food Diary"
    d.heading([(f"{title} ", False), (f"— Week {week}", True)], 39,
              size=19)
    tx = texts(pg)
    top = sorted([t for t in tx if t.rect.y0 < 100],
                 key=lambda t: t.rect.x0)
    smalltop = sorted([t for t in top if t.rect.y0 < 50],
                      key=lambda t: t.rect.x0)
    if len(smalltop) >= 2:
        a, b = smalltop[0], smalltop[1]
        d.tr(a.rect.x0 - 6, (a.rect.y0 + a.rect.y1) / 2 + 3, "From",
             "asm", 9.5, NAVY)
        d.tr(b.rect.x0 - 6, (b.rect.y0 + b.rect.y1) / 2 + 3, "to",
             "asm", 9.5, NAVY)
    focus = [t for t in top if t.rect.y0 >= 50]
    if kind == "strategy" and focus:
        fr = focus[0].rect
        d.tr(fr.x0 - 8, (fr.y0 + fr.y1) / 2 + 3, "Focus of the week:",
             "asm", 9.5, NAVY)
    # normalise the 35 meal cells onto a uniform 7 x 5 grid
    cells = sorted([t for t in tx if t.rect.y0 >= 100],
                   key=lambda t: t.rect.y0)
    GX0, GX1, CG = 56, 563, 7
    GY0, GY1, RG = 130, 808, 8
    cw = (GX1 - GX0 - 4 * CG) / 5
    rh = (GY1 - GY0 - 6 * RG) / 7
    for r in range(7):
        rowcells = sorted(cells[r * 5:r * 5 + 5],
                          key=lambda t: t.rect.x0)
        for c, w in enumerate(rowcells):
            x0 = GX0 + c * (cw + CG)
            y0 = GY0 + r * (rh + RG)
            w.rect = fitz.Rect(x0, y0, x0 + cw, y0 + rh)
            w.field_flags = w.field_flags | 4096
            w.update()
    for c, name in enumerate(["Breakfast", "Snack", "Lunch", "Snack",
                              "Dinner"]):
        x0 = GX0 + c * (cw + CG)
        d.rect(x0, GY0 - 24, x0 + cw, GY0 - 2, fill=BLUSH)
        d.tc(x0 + cw / 2, GY0 - 9, name.upper(), "asb", 8.5, WHITE)
    for r, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat",
                             "Sun"]):
        y0 = GY0 + r * (rh + RG)
        d.rect(14, y0, GX0 - 4, y0 + rh, fill=BLUSH)
        d.tc((14 + GX0 - 4) / 2, y0 + rh / 2 + 3, day.upper(), "asb",
             8.5, WHITE)
    d.pageno(n)


def review(pg, n, week):
    d = P(pg)
    d.fill()
    d.heading([("Week Review ", False), (f"— Week {week}", True)],
              54, size=23)
    ws = sorted(texts(pg), key=lambda w: w.rect.y0)
    # normalise all answer boxes to one width; first three multiline,
    # the Date field single-line
    for i, w in enumerate(ws):
        r = w.rect
        w.rect = fitz.Rect(223, r.y0, 564, r.y1)
        if i < 3:
            w.field_flags = w.field_flags | 4096
        else:
            w.field_flags = w.field_flags & ~4096
        w.update()
    labels = ["Review of meals for the week",
              "What went well? (Specify your non-scale victories)",
              "Areas to focus on next week",
              "Date"]
    for w, lbl in zip(ws, labels):
        r = w.rect
        d.rect(M, r.y0, r.x0 - 8, r.y1, fill=BLUSH)
        d.vcentre(M + 13, r.y0, r.y1, lbl, "asb", 9.5, WHITE,
                  r.x0 - 8 - M - 26, 12.5)
    d.pageno(n)


def results_text(pg, n, prompts):
    d = P(pg)
    d.fill()
    d.heading([("4 Week Sprint ", False), ("Results", True)], 44,
              size=21)
    ws = sorted(texts(pg), key=lambda w: w.rect.y0)
    for w, pr in zip(ws, prompts):
        r = w.rect
        d.rect(M, r.y0, r.x0 - 8, r.y1, fill=BLUSH)
        d.vcentre(M + 13, r.y0, r.y1, pr, "asb", 9.5, WHITE,
                  r.x0 - 8 - M - 26, 12.5)
    d.pageno(n)


# =================================================== render all
cover(doc[0])
smart_goal(doc[1])
starting_details(doc[2])
intro(doc[3])
for wk in range(1, 5):
    base = 5 + (wk - 1) * 4
    habit_tracker(doc[base - 1], base, wk)
    grid_page(doc[base], base + 1, wk, "strategy")
    grid_page(doc[base + 1], base + 2, wk, "diary")
    review(doc[base + 2], base + 3, wk)
sprint_results_table(doc[20])
results_text(doc[21], 22, [
    "What are your non-scale victories? Results or situations you are "
    "proud of that are not related to the scale.",
    "What worked well for you?",
    "What needs some work and attention over the coming month?"])
results_text(doc[22], 23, [
    "Based on your overall goal for the Shift & Sustain program, have "
    "you moved the needle forward over the past month? If yes, how — "
    "and if not, why?",
    "Personal reflections / journaling space."])

for page in doc:
    for w in page.widgets():
        style_field(w)

# clear any demo values left in the original (update() ignores "")
for page in doc:
    for w in page.widgets():
        if w.field_type_string == "Text" and w.field_value not in ("", None):
            doc.xref_set_key(w.xref, "V", "()")
            doc.xref_set_key(w.xref, "AP", "null")

# centre-align the meal-grid cells and the weekly-review Date fields.
# Q sets the alignment; clearing AP + NeedAppearances makes viewers
# regenerate the field appearance and honour it.
for idx in (5, 6, 9, 10, 13, 14, 17, 18):
    for w in doc[idx].widgets():
        if w.field_type_string == "Text" and w.rect.y0 >= 100:
            doc.xref_set_key(w.xref, "Q", "1")
            doc.xref_set_key(w.xref, "AP", "null")
for idx in (7, 11, 15, 19):
    rv = sorted([w for w in doc[idx].widgets()
                 if w.field_type_string == "Text"],
                key=lambda w: w.rect.y0)
    if rv:
        doc.xref_set_key(rv[-1].xref, "Q", "1")
        doc.xref_set_key(rv[-1].xref, "AP", "null")

_af = doc.xref_get_key(doc.pdf_catalog(), "AcroForm")
if _af[0] == "xref":
    doc.xref_set_key(int(_af[1].split()[0]), "NeedAppearances", "true")

doc.set_metadata({
    "title": "4 Week Weight Loss Sprint Workbook",
    "author": "The Weight Loss Academy",
    "subject": "A fillable 4 week weight loss sprint workbook",
    "keywords": "workbook, weight loss, sprint, fillable, tracker",
    "creator": "The Weight Loss Academy",
})
doc.save(OUT, deflate=True, garbage=4)
print(f"wrote {OUT}  ({len(doc)} pages)")
