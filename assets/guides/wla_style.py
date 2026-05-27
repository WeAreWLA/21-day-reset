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
    if not any(k in s for k in _FRAC):
        return s
    out = []
    for ch in s:
        if ch in _FRAC:
            if out and out[-1][-1:].isdigit():   # mixed number e.g. 2⅔
                out.append(" ")
            out.append(_FRAC[ch])
        else:
            out.append(ch)
    return "".join(out)


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

    def coral_heading(self, text, size=20, gap_before=14, gap_after=13):
        """Blush italic heading that wraps across the column."""
        self.y += gap_before
        for ln in wrap(text, "lbi", size, CW):
            self.ensure(size * 1.3)
            self.text(LEFT, self.y + size * 0.80, ln, "lbi", size, BLUSH)
            self.y += size * 1.28
        self.y += gap_after

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

    # -------------------------------------------------- image cover-fit
    def _insert_cover_image(self, rect, path):
        """Insert path into rect with cover-fit (no distortion, center-crop)."""
        from PIL import Image
        import tempfile, hashlib
        with Image.open(path) as im:
            im = im.convert("RGB")
            iw, ih = im.size
            src_ar = iw / ih
            dst_ar = rect.width / rect.height
            if src_ar > dst_ar:
                new_w = int(ih * dst_ar)
                x0 = (iw - new_w) // 2
                box = (x0, 0, x0 + new_w, ih)
            else:
                new_h = int(iw / dst_ar)
                y0 = (ih - new_h) // 2
                box = (0, y0, iw, y0 + new_h)
            cropped = im.crop(box)
            key = hashlib.md5(f"{path}-{box}".encode()).hexdigest()[:10]
            tmp = os.path.join(tempfile.gettempdir(), f"wla_cover_{key}.jpg")
            cropped.save(tmp, "JPEG", quality=88, optimize=True)
        self.page.insert_image(rect, filename=tmp)

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
        """Grid table. headers = list (or None for no header band).
        columns = list of cell-lists. Robust across page breaks."""
        n = len(columns)
        col_w = CW / n
        size = 10.5 if n >= 4 else 11
        hsize = 9 if n >= 4 else 9.5
        line_h = 13.2
        pad = 7
        nrows = max(len(c) for c in columns)
        header_h = 34 if headers else 0

        def cell_lines(s):
            return wrap(s, "as", size, col_w - 14) if s else []

        def row_h(ri):
            mx = 1
            for c in columns:
                if ri < len(c) and c[ri]:
                    mx = max(mx, len(cell_lines(c[ri])))
            return max(40, mx * line_h + 2 * pad)

        def vrules(t, b):
            for i in range(1, n):
                x = LEFT + i * col_w
                self.page.draw_line((x, t), (x, b), color=RULE, width=0.7)

        def draw_header(top):
            if headers:
                self.page.draw_rect(fitz.Rect(LEFT, top, RIGHT,
                                    top + header_h), color=None, fill=BEIGE)
                for i, htxt in enumerate(headers):
                    cx = LEFT + i * col_w + col_w / 2
                    hl = wrap(htxt, "asb", hsize, col_w - 12)
                    ty = top + header_h / 2 - (len(hl) - 1) * 6.4 + 3
                    for hln in hl:
                        self.text_center(cx, ty, hln, "asb", hsize, NAVY)
                        ty += 12.8
                vrules(top, top + header_h)
                return top + header_h
            self.page.draw_line((LEFT, top), (RIGHT, top), color=RULE,
                                width=0.7)
            return top

        self.y += gap_before
        self.ensure(header_h + row_h(0))
        top = draw_header(self.y)

        ri = 0
        while ri < nrows:
            h = row_h(ri)
            if top + h > CONTENT_BOTTOM:
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
            vrules(top, top + h)
            top += h
            ri += 1
        self.y = top + gap_after

    def list_table(self, header, rows, gap_before=8, gap_after=14):
        size = 11
        line_h = 14.5
        pad = 9
        header_h = 32 if header else 0

        def row_h(s):
            return max(38, len(wrap(s, "as", size, CW - 40)) * line_h + 2 * pad)

        def draw_header(top):
            if header:
                self.page.draw_rect(fitz.Rect(LEFT, top, RIGHT,
                                    top + header_h), color=None, fill=BEIGE)
                self.tracked(
                    PAGE_W / 2 - self.tracked_w(header, "asb", 10, 1.3) / 2,
                    top + header_h / 2 + 3.4, header, "asb", 10, NAVY, 1.3)
                return top + header_h
            self.page.draw_line((LEFT, top), (RIGHT, top), color=RULE,
                                width=0.7)
            return top

        self.y += gap_before
        self.ensure(header_h + row_h(rows[0]))
        top = draw_header(self.y)
        for s in rows:
            h = row_h(s)
            if top + h > CONTENT_BOTTOM:
                self._new_content_page()
                top = draw_header(self.y)
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

    def section_label(self, text, gap_before=18, gap_after=10):
        """Coral uppercase section divider label."""
        self.ensure(30 + gap_before)
        self.y += gap_before
        base = self.y + 9
        self.tracked(LEFT, base, text.upper(), "asb", 11, BLUSH, 1.5)
        self.y = base + 6
        self.page.draw_line((LEFT, self.y), (LEFT + 42, self.y),
                            color=BLUSH, width=2.2)
        self.y += gap_after

    def matrix_table(self, col_headers, rows, label_header="",
                     gap_before=10, gap_after=14, label_w=74, size=8.7):
        """Navy-header grid. rows = [(label, [values]), ...]."""
        n = len(col_headers)
        col_w = (CW - label_w) / n
        header_h = 34
        line_h = size + 2
        white = (1, 1, 1)

        def cl(s, w, fnt="as"):
            return wrap(s, fnt, size, w - 8)

        heights = []
        for label, vals in rows:
            mx = max([len(cl(label, label_w, "asm"))] +
                     [len(cl(v, col_w)) for v in vals])
            heights.append(max(34, mx * line_h + 16))

        self.y += gap_before
        self.ensure(header_h + heights[0])
        top = self.y

        def draw_header(t):
            self.page.draw_rect(fitz.Rect(LEFT, t, LEFT + label_w,
                                          t + header_h), color=None, fill=NAVY)
            if label_header:
                self.text_center(LEFT + label_w / 2, t + header_h / 2 + 3,
                                 label_header.upper(), "asb", 8.5, white)
            for i, h in enumerate(col_headers):
                x = LEFT + label_w + i * col_w
                self.page.draw_rect(fitz.Rect(x, t, x + col_w, t + header_h),
                                    color=CREAM, fill=NAVY, width=0.6)
                hl = cl(h.upper(), col_w, "asb")
                ty = t + header_h / 2 - (len(hl) - 1) * 5.3 + 3
                for ln in hl:
                    self.text_center(x + col_w / 2, ty, ln, "asb", 8.5, white)
                    ty += 10.6
            return t + header_h

        ry = draw_header(top)
        for (label, vals), h in zip(rows, heights):
            if ry + h > CONTENT_BOTTOM:
                self._new_content_page()
                ry = draw_header(self.y)
            self.page.draw_rect(fitz.Rect(LEFT, ry, LEFT + label_w, ry + h),
                                color=RULE, fill=None, width=0.7)
            ll = cl(label, label_w, "asm")
            ty = ry + h / 2 - (len(ll) - 1) * line_h / 2 + 3
            for ln in ll:
                self.text_center(LEFT + label_w / 2, ty, ln, "asm", size, NAVY)
                ty += line_h
            for i, v in enumerate(vals):
                x = LEFT + label_w + i * col_w
                self.page.draw_rect(fitz.Rect(x, ry, x + col_w, ry + h),
                                    color=RULE, fill=None, width=0.7)
                vl = cl(v, col_w)
                ty = ry + h / 2 - (len(vl) - 1) * line_h / 2 + 3
                for ln in vl:
                    self.text_center(x + col_w / 2, ty, ln, "as", size, INK)
                    ty += line_h
            ry += h
        self.y = ry + gap_after

    def cards(self, items, gap_before=14, gap_after=14):
        """Row of info cards: items = [(header, body), ...]."""
        n = len(items)
        gap = 11
        cw = (CW - (n - 1) * gap) / n
        head_h = 26
        size = 9
        bmax = max(len(wrap(b, "as", size, cw - 16)) for _, b in items)
        body_h = max(70, bmax * 12 + 30)
        H = head_h + body_h
        self.ensure(H + gap_before + gap_after)
        self.y += gap_before
        top = self.y
        for i, (htxt, btxt) in enumerate(items):
            x = LEFT + i * (cw + gap)
            self.page.draw_rect(fitz.Rect(x, top, x + cw, top + head_h),
                                color=None, fill=NAVY)
            self.text_center(x + cw / 2, top + head_h / 2 + 3.2, htxt,
                             "asb", 9, (1, 1, 1))
            self.page.draw_rect(fitz.Rect(x, top + head_h, x + cw, top + H),
                                color=None, fill=BLUSH)
            bl = wrap(btxt, "as", size, cw - 16)
            ty = top + head_h + (body_h - (len(bl) - 1) * 12) / 2
            for ln in bl:
                self.text_center(x + cw / 2, ty, ln, "as", size, (1, 1, 1))
                ty += 12
        self.y = top + H + gap_after

    def recipe(self, title, serves, ingredients, instructions,
               note=None, image=None, time=None, subtitle=None,
               kicker=None, to_serve=None, image_h=320, **_):
        """WLA Weight Loss Cookbook style recipe page (one per page)."""
        self._new_content_page()

        if image:
            rect = fitz.Rect(0, 0, PAGE_W, image_h)
            self._insert_cover_image(rect, image)
            y = image_h + 34
        else:
            y = CONTENT_TOP + 8

        # kicker: ("RECIPE 01", "BREAKFAST") -> "RECIPE 01  ·  BREAKFAST"
        if kicker:
            ka, kb = (kicker if isinstance(kicker, (tuple, list))
                      else (kicker, None))
            kx = self.tracked(LEFT, y, ka.upper(), "asb", 8.5, BLUSH, 1.4)
            if kb:
                dx = kx + 10
                self.text(dx, y, "·", "asb", 8.5, BLUSH)
                self.tracked(dx + 12, y, kb.upper(), "asb", 8.5, BLUSH, 1.4)
            y += 26

        # title
        tsize = 25
        for tl in wrap(title, "lbi", tsize, CW):
            self.text(LEFT, y + tsize * 0.78, tl, "lbi", tsize, NAVY)
            y += tsize * 1.1

        # subtitle
        if subtitle:
            y += 6
            for sl in wrap(subtitle, "lbi", 12, CW):
                self.text(LEFT, y + 10, sl, "lbi", 12, BLUSH)
                y += 16

        # serves + time row
        y += 22
        col_w = 132
        self.tracked(LEFT, y, "SERVES", "asb", 8.5, BLUSH, 1.4)
        if time:
            self.tracked(LEFT + col_w, y, "TIME", "asb", 8.5, BLUSH, 1.4)
        y += 18
        self.text(LEFT, y + 12, str(serves), "lbi", 17, NAVY)
        if time:
            self.text(LEFT + col_w, y + 12, str(time), "lbi", 17, NAVY)
        y += 26

        # hairline rule
        self.page.draw_line((LEFT, y), (RIGHT, y), color=RULE, width=0.6)
        y += 22

        # two-column body
        col_gap = 28
        lw = (CW - col_gap) * 0.40
        rw = (CW - col_gap) * 0.60
        rx = LEFT + lw + col_gap

        self.tracked(LEFT, y, "INGREDIENTS", "asb", 8.5, BLUSH, 1.4)
        self.tracked(rx, y, "METHOD", "asb", 8.5, BLUSH, 1.4)
        y_top = y + 18

        size = 9.5
        lh = 12.6

        def render_ing(items, x, max_w, start_y, label=None):
            yL = start_y
            if label:
                self.text(x, yL + 10, label, "lbi", 11, BLUSH)
                yL += 18
            for it in items:
                self.text(x, yL + 9, "—", "as", size, INK)
                for ln in wrap(it, "as", size, max_w - 16):
                    self.text(x + 16, yL + 9, ln, "as", size, INK)
                    yL += lh
                yL += 3.5
            return yL

        yL = render_ing(ingredients, LEFT, lw, y_top)
        if to_serve:
            yL += 6
            yL = render_ing(to_serve, LEFT, lw, yL, label="To serve")

        # method
        yR = y_top
        for k, step in enumerate(instructions, 1):
            self.tracked(rx, yR + 9, f"{k:02d}", "asb", 8.5, BLUSH, 1.4)
            for ln in wrap(step, "as", size, rw - 28):
                self.text(rx + 28, yR + 9, ln, "as", size, INK)
                yR += lh
            yR += 4

        body_end = max(yL, yR)

        # WLA TIP
        if note:
            ty = body_end + 22
            self.tracked(LEFT, ty, "WLA TIP", "asb", 8.5, BLUSH, 1.4)
            ty += 18
            for ln in wrap(note, "asi", 10, CW):
                self.text(LEFT, ty + 10, ln, "asi", 10, INK)
                ty += 14

        self.y = 1e6  # force a fresh page for the next block

    def divider(self, top_italic, bottom):
        """Full-page chapter divider."""
        page = self._blank_page()
        self.page = page
        size = 58
        cy = PAGE_H * 0.40
        self.text_center(PAGE_W / 2, cy, top_italic, "lbi", size, NAVY)
        self.text_center(PAGE_W / 2, cy + size * 1.0, bottom, "lb", size, NAVY)
        rule_y = cy + size * 1.0 + 34
        self.page.draw_line((PAGE_W / 2 - 26, rule_y), (PAGE_W / 2 + 26,
                            rule_y), color=BLUSH, width=2.6)
        self.y = 1e6  # force next content onto a fresh page

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
