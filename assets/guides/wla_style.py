#!/usr/bin/env python3
"""Shared house-style toolkit for The Weight Loss Academy guide PDFs.

Matches the No-Fuss Batch Cookbook layout using the WLA brand fonts
(Libre Baskerville + Alegreya Sans) and palette. Provides a simple
flowing layout engine: build a guide as a sequence of blocks and the
engine handles page breaks, footers and page numbers.
"""

import os
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
DIAGRAM_DIR = os.path.join(HERE, "diagrams")

# ---------------------------------------------------------------- brand
PAGE_W, PAGE_H = 595.276, 841.89
MARGIN = 51
LEFT = MARGIN
RIGHT = PAGE_W - MARGIN
CW = RIGHT - LEFT

CREAM = (0xF9 / 255, 0xF7 / 255, 0xF4 / 255)
NAVY = (0x00 / 255, 0x30 / 255, 0x60 / 255)
BLUSH = (0xF7 / 255, 0x9F / 255, 0x83 / 255)
BEIGE = (0xE9 / 255, 0xDF / 255, 0xD3 / 255)
INK = (0x33 / 255, 0x33 / 255, 0x33 / 255)
RULE = (0.80, 0.83, 0.87)

CONTENT_TOP = 74
CONTENT_BOTTOM = PAGE_H - 80

FONTS = {
    "lb":  "LibreBaskerville-Regular.ttf",
    "lbi": "LibreBaskerville-Italic.ttf",
    "as":  "AlegreyaSans-Regular.ttf",
    "asm": "AlegreyaSans-Medium.ttf",
    "asb": "AlegreyaSans-Bold.ttf",
    "asi": "AlegreyaSans-Italic.ttf",
}
FACE = {k: fitz.Font(fontfile=os.path.join(FONT_DIR, v)) for k, v in FONTS.items()}


# Alegreya Sans lacks some vulgar-fraction glyphs (⅙, ⅛ ...); normalise
# every fraction to a plain ASCII form so the set stays consistent.
_FRAC = {"½": "1/2", "⅓": "1/3", "⅔": "2/3", "¼": "1/4", "¾": "3/4",
         "⅕": "1/5", "⅖": "2/5", "⅗": "3/5", "⅘": "4/5",
         "⅙": "1/6", "⅚": "5/6", "⅛": "1/8", "⅜": "3/8",
         "⅝": "5/8", "⅞": "7/8"}


def norm(s):
    for k, v in _FRAC.items():
        if k in s:
            s = s.replace(k, v)
    return s


def tw(text, font, size):
    return FACE[font].text_length(norm(text), size)


def fit_size(text, font, target_w, hi=120, lo=6):
    for _ in range(44):
        mid = (hi + lo) / 2
        if tw(text, font, mid) <= target_w:
            lo = mid
        else:
            hi = mid
    return lo


def wrap(text, font, size, max_w):
    lines, cur = [], ""
    for word in norm(text).split():
        trial = word if not cur else cur + " " + word
        if tw(trial, font, size) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


class Guide:
    """A flowing guide document."""

    def __init__(self, out_path):
        self.out_path = out_path
        self.doc = fitz.open()
        self.page = None
        self.y = 0.0
        self.npages = 0

    # -------------------------------------------------- low-level drawing
    def _register(self, page):
        for alias, fname in FONTS.items():
            page.insert_font(fontname=alias, fontfile=os.path.join(FONT_DIR, fname))

    def _blank_page(self):
        page = self.doc.new_page(width=PAGE_W, height=PAGE_H)
        page.draw_rect(fitz.Rect(0, 0, PAGE_W, PAGE_H), color=None, fill=CREAM)
        self._register(page)
        self.npages += 1
        return page

    def text(self, x, y, s, font, size, color):
        self.page.insert_text((x, y), norm(s), fontname=font, fontsize=size,
                              color=color)

    def text_center(self, cx, y, s, font, size, color):
        self.text(cx - tw(s, font, size) / 2, y, s, font, size, color)

    def text_right(self, rx, y, s, font, size, color):
        self.text(rx - tw(s, font, size), y, s, font, size, color)

    def tracked(self, x, y, s, font, size, color, tracking):
        cx = x
        for ch in s:
            self.text(cx, y, ch, font, size, color)
            cx += tw(ch, font, size) + tracking
        return cx - tracking

    def tracked_w(self, s, font, size, tracking):
        return sum(tw(ch, font, size) + tracking for ch in s) - tracking

    def segs(self, x, y, segments, size, default_color):
        """Draw inline rich text: segments = [(text, font, color?), ...]."""
        cx = x
        for seg in segments:
            s, font = seg[0], seg[1]
            color = seg[2] if len(seg) > 2 else default_color
            self.text(cx, y, s, font, size, color)
            cx += tw(s, font, size)
        return cx

    # -------------------------------------------------- page flow
    def _new_content_page(self):
        self.page = self._blank_page()
        self.y = CONTENT_TOP

    def ensure(self, space):
        if self.page is None or self.y + space > CONTENT_BOTTOM:
            self._new_content_page()

    def gap(self, h):
        self.y += h

    def keep_together(self, h):
        """Start a new page if `h` points of content would not fit."""
        if self.page is None or self.y + h > CONTENT_BOTTOM:
            self._new_content_page()

    # -------------------------------------------------- cover
    def cover(self, kicker_a, kicker_b, title_lines, subtitle):
        """title_lines = [(text, font, color), ...] (3 lines)."""
        page = self._blank_page()
        self.page = page
        # kicker
        kx = self.tracked(LEFT, 60, kicker_a, "asb", 9, NAVY, 1.6)
        self.text(kx + 11, 60, "·", "asb", 9, BLUSH)
        self.tracked(kx + 22, 60, kicker_b, "asb", 9, NAVY, 1.6)
        # title
        target = 408
        T = min(fit_size(t[0], t[1], target) for t in title_lines)
        T = min(T, 78)
        LH = T * 1.18
        b1 = 286
        for i, (txt, font, color) in enumerate(title_lines):
            self.text(LEFT, b1 + i * LH, txt, font, T, color)
        # subtitle
        sy = b1 + (len(title_lines) - 1) * LH + 56
        for ln in wrap(subtitle, "lbi", 13, 348):
            self.text(LEFT, sy, ln, "lbi", 13, BLUSH)
            sy += 20.5

    # -------------------------------------------------- headings
    def heading(self, lines, size=None):
        """Big section heading. lines = [[(text, italic_bool), ...], ...]."""
        target = CW - 4
        flat = ["".join(seg[0] for seg in ln) for ln in lines]
        if size is None:
            size = min(fit_size(s, "lb", target) for s in flat)
            size = min(size, 33)
        LH = size * 1.16
        self.ensure(LH * len(lines) + 16)
        top = self.y
        for i, ln in enumerate(lines):
            base = top + size * 0.80 + i * LH
            cx = LEFT
            for txt, italic in ln:
                font = "lbi" if italic else "lb"
                self.text(cx, base, txt, font, size, NAVY)
                cx += tw(txt, font, size)
        self.y = top + size * 0.80 + (len(lines) - 1) * LH + size * 0.30
        # blush accent rule
        self.y += 9
        self.page.draw_line((LEFT, self.y), (LEFT + 54, self.y),
                            color=BLUSH, width=2.4)
        self.y += 20

    def subhead(self, segments, size=19, color=BLUSH, gap_before=10, gap_after=14):
        """Coral/navy italic-accent sub-heading. segments=[(text,font),...]."""
        self.ensure(size + gap_before + gap_after)
        self.y += gap_before
        base = self.y + size * 0.80
        self.segs(LEFT, base, segments, size, color)
        self.y = base + size * 0.28 + gap_after

    def diagram_title(self, text, size=16.5, gap_before=6, gap_after=12):
        lines = wrap(text, "lb", size, CW - 30)
        self.ensure(size * 1.2 * len(lines) + gap_before + gap_after)
        self.y += gap_before
        for ln in lines:
            base = self.y + size * 0.80
            self.text_center(PAGE_W / 2, base, ln, "lb", size, NAVY)
            self.y = base + size * 0.34
        self.y += gap_after

    # -------------------------------------------------- body
    def paragraph(self, text, size=11.5, lh=15.6, gap_after=9, color=INK,
                  font="as"):
        lines = wrap(text, font, size, CW)
        for ln in lines:
            self.ensure(lh)
            self.text(LEFT, self.y + size * 0.80, ln, font, size, color)
            self.y += lh
        self.y += gap_after

    def bullets(self, items, size=11.5, lh=15.6, item_gap=3.5, gap_after=10,
                bold_prefix=False, indent=20, color=INK):
        for item in items:
            x0 = LEFT + indent
            wrapw = CW - indent
            # split bold prefix at first colon
            prefix, rest = None, item
            if bold_prefix and ":" in item:
                p, r = item.split(":", 1)
                prefix, rest = p + ":", r
            lines = wrap(item, "as", size, wrapw)
            self.ensure(lh * len(lines) + item_gap)
            # marker
            self.page.draw_circle((LEFT + 7, self.y + size * 0.46), 1.7,
                                  color=None, fill=BLUSH)
            for i, ln in enumerate(lines):
                base = self.y + size * 0.80
                if i == 0 and prefix:
                    self.text(x0, base, prefix, "asb", size, NAVY)
                    px = x0 + tw(prefix, "asb", size)
                    self.text(px, base, ln[len(prefix):], "as", size, color)
                else:
                    self.text(x0, base, ln, "as", size, color)
                self.y += lh
            self.y += item_gap
        self.y += gap_after - item_gap

    def numbered(self, items, size=11.5, lh=15.6, item_gap=3.5, gap_after=10,
                 indent=24):
        for n, item in enumerate(items, 1):
            x0 = LEFT + indent
            lines = wrap(item, "as", size, CW - indent)
            self.ensure(lh * len(lines) + item_gap)
            self.text(LEFT + 6, self.y + size * 0.80, f"{n}.", "asb", size, BLUSH)
            for ln in lines:
                self.text(x0, self.y + size * 0.80, ln, "as", size, INK)
                self.y += lh
            self.y += item_gap
        self.y += gap_after - item_gap

    def note(self, text, size=11, lh=15, gap_before=14, gap_after=6,
             font="asi", color=INK):
        self.y += gap_before
        for ln in wrap(text, font, size, CW):
            self.ensure(lh)
            self.text(LEFT, self.y + size * 0.80, ln, font, size, color)
            self.y += lh
        self.y += gap_after

    # -------------------------------------------------- diagram
    def diagram(self, name, gap_before=4, gap_after=14, max_w=CW):
        path = os.path.join(DIAGRAM_DIR, f"{name}.png")
        pm = fitz.Pixmap(path)
        ar = pm.width / pm.height
        w = min(max_w, CW)
        h = w / ar
        if h > 300:
            h = 300
            w = h * ar
        self.ensure(h + gap_before + gap_after)
        self.y += gap_before
        x0 = LEFT + (CW - w) / 2
        rect = fitz.Rect(x0, self.y, x0 + w, self.y + h)
        self.page.insert_image(rect, filename=path)
        self.y += h + gap_after

    # -------------------------------------------------- tables
    def select_table(self, headers, columns, gap_before=8, gap_after=14):
        """Grid table: headers list, columns = list of cell-lists."""
        n = len(headers)
        col_w = CW / n
        size = 10.5 if n >= 4 else 11
        hsize = 9 if n >= 4 else 9.5
        line_h = 13.2
        pad = 7
        nrows = max(len(c) for c in columns)
        header_h = 34

        def cell_lines(s):
            return wrap(s, "as", size, col_w - 14) if s else []

        def row_h(ri):
            mx = 1
            for c in columns:
                if ri < len(c) and c[ri]:
                    mx = max(mx, len(cell_lines(c[ri])))
            return max(40, mx * line_h + 2 * pad)

        def draw_header(top):
            self.page.draw_rect(fitz.Rect(LEFT, top, RIGHT, top + header_h),
                                color=None, fill=BEIGE)
            for i, htxt in enumerate(headers):
                cx = LEFT + i * col_w + col_w / 2
                hl = wrap(htxt, "asb", hsize, col_w - 12)
                ty = top + header_h / 2 - (len(hl) - 1) * 6.4 + 3
                for hln in hl:
                    self.text_center(cx, ty, hln, "asb", hsize, NAVY)
                    ty += 12.8
            return top + header_h

        self.y += gap_before
        self.ensure(header_h + row_h(0))
        top = draw_header(self.y)

        ri = 0
        while ri < nrows:
            h = row_h(ri)
            if top + h > CONTENT_BOTTOM:
                self.y = top
                self._new_content_page()
                top = draw_header(self.y)
            for ci, col in enumerate(columns):
                if ri < len(col) and col[ri]:
                    cx = LEFT + ci * col_w + col_w / 2
                    cl = cell_lines(col[ri])
                    ty = top + h / 2 - (len(cl) - 1) * line_h / 2 + size * 0.34
                    for cln in cl:
                        self.text_center(cx, ty, cln, "as", size, INK)
                        ty += line_h
            self.page.draw_line((LEFT, top + h), (RIGHT, top + h),
                                color=RULE, width=0.7)
            top += h
            ri += 1
        # vertical separators
        for i in range(1, n):
            x = LEFT + i * col_w
            self.page.draw_line((x, self.y), (x, top), color=RULE, width=0.7)
        self.y = top + gap_after

    def list_table(self, header, rows, gap_before=8, gap_after=14):
        size = 11
        line_h = 14.5
        pad = 9
        header_h = 32

        def row_h(s):
            return max(38, len(wrap(s, "as", size, CW - 40)) * line_h + 2 * pad)

        self.y += gap_before
        self.ensure(header_h + row_h(rows[0]))
        # header band
        self.page.draw_rect(fitz.Rect(LEFT, self.y, RIGHT, self.y + header_h),
                            color=None, fill=BEIGE)
        self.tracked(PAGE_W / 2 - self.tracked_w(header, "asb", 10, 1.3) / 2,
                     self.y + header_h / 2 + 3.4, header, "asb", 10, NAVY, 1.3)
        top = self.y + header_h
        for s in rows:
            h = row_h(s)
            if top + h > CONTENT_BOTTOM:
                self._new_content_page()
                top = self.y
            cl = wrap(s, "as", size, CW - 40)
            ty = top + h / 2 - (len(cl) - 1) * line_h / 2 + size * 0.34
            for cln in cl:
                self.text_center(PAGE_W / 2, ty, cln, "as", size, INK)
                ty += line_h
            self.page.draw_line((LEFT, top + h), (RIGHT, top + h),
                                color=RULE, width=0.7)
            top += h
        self.y = top + gap_after

    def week_table(self, days, rows, gap_before=8, gap_after=12):
        """rows = [(label, [7 values]), ...]."""
        label_w = 78
        day_w = (CW - label_w) / 7
        header_h = 30
        size = 9.3
        line_h = 11.5

        def vlines(s):
            return wrap(s, "as", size, day_w - 8)

        row_heights = []
        for _, vals in rows:
            mx = 1
            for v in vals:
                mx = max(mx, len(vlines(v)))
            row_heights.append(max(30, mx * line_h + 14))

        self.y += gap_before
        self.ensure(header_h + sum(row_heights))
        top = self.y
        # header row: blank corner + coral day cells
        for i, day in enumerate(days):
            x = LEFT + label_w + i * day_w
            self.page.draw_rect(fitz.Rect(x, top, x + day_w, top + header_h),
                                color=CREAM, fill=BLUSH, width=0.8)
            self.text_center(x + day_w / 2, top + header_h / 2 + 3.3,
                             day, "asb", size, (1, 1, 1))
        ry = top + header_h
        for (label, vals), h in zip(rows, row_heights):
            # label cell
            self.text(LEFT + 6, ry + h / 2 + 3.2, label, "asm", size, NAVY)
            for i, v in enumerate(vals):
                x = LEFT + label_w + i * day_w
                self.page.draw_rect(fitz.Rect(x, ry, x + day_w, ry + h),
                                    color=RULE, fill=None, width=0.7)
                vl = vlines(v)
                ty = ry + h / 2 - (len(vl) - 1) * line_h / 2 + size * 0.33
                for vln in vl:
                    self.text_center(x + day_w / 2, ty, vln, "as", size, INK)
                    ty += line_h
            ry += h
        self.y = ry + gap_after

    # -------------------------------------------------- finalise
    def save(self, meta):
        for idx in range(self.npages):
            page = self.doc[idx]
            fy = PAGE_H - 40
            self.page = page
            self.tracked(LEFT, fy, "THE WEIGHT LOSS ACADEMY", "asb", 7.5,
                         NAVY, 1.2)
            self.text_right(RIGHT, fy, f"{idx + 1:02d}", "as", 8.5, NAVY)
        self.doc.set_metadata(meta)
        self.doc.save(self.out_path, deflate=True, garbage=4)
        print(f"wrote {self.out_path}  ({self.npages} pages)")
