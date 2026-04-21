# 21 Day Reset Sales Page

A soft editorial sales page for the WLA (Weight Loss Academy) 21 Day Reset — designed for women 45+ navigating menopause-related weight changes.

---

## Live link

All CTA buttons point to: **https://sales.thewlacademy.com/may-reset/**

---

## File structure

```
21 Day Reset.html          # Main entry. Hero + app shell + tweaks panel + responsive CSS
components/
  sections.jsx             # Shared primitives: Eyebrow, SerifH, Italic, Body, PrimaryCTA,
                           # Placeholder, SoftCard, QuoteMark, Tick, Cross, Divider
  hero.jsx                 # Announcement bar, Nav, StatPill, (legacy Hero — overridden)
  method.jsx               # ProblemSection, WLA Reset Method (3 steps), TransformSection
  content.jsx              # IncludedSection, TestimonialsSection, AboutSection
  closing.jsx              # PricingSection, FAQSection, FinalCTA, StickyCTA, Footer
assets/
  anna-hero.jpg            # Hero portrait of Anna
  anna-portrait.jpg        # About-section portrait
  vicky-before-after.png   # Before/after photos in Results grid
  laura-before-after.png
  jill-before-after.jpg    # (Laura slot, shows Jill's result)
  ruth-before-after.jpg
  barbara-before-after.png
```

---

## Brand system

### Colors (CSS variables in `21 Day Reset.html`)

| Token           | Hex       | Role                                    |
|-----------------|-----------|-----------------------------------------|
| `--bg`          | `#F9F7F4` | Cream White — page background           |
| `--cream-deep`  | `#E9DFD3` | Warm Beige — secondary sections         |
| `--paper`       | `#FDFBF8` | Near-white — cards                      |
| `--ink`         | `#003060` | Deep Navy — headlines, primary CTA      |
| `--ink-muted`   | `#5B6B82` | Supporting text                         |
| `--body-ink`    | `#333333` | Grey Black — paragraphs                 |
| `--terracotta`  | `#F79F83` | Soft Blush — accents                    |
| `--blush-deep`  | `#E87F63` | Deeper blush for contrast text/icons    |
| `--peach`       | `#F5D9CE` | Lighter blush tint                      |
| `--hairline`    | `#D9CFC3` | Borders                                 |

### Typography

- **Libre Baskerville** (700 bold + 400 italic) — headlines, display, decorative italic
- **Alegreya Sans** (400/500/600) — body, UI, buttons, captions

Loaded from Google Fonts in the `<head>` of the main HTML file.

---

## Page sections (in order)

1. **Announcement bar** — launch date + price
2. **Nav** — logo + section links + CTA
3. **Hero** — headline, sub, primary CTA, stats bar, Anna portrait, floating testimonial + credential chips
4. **Problem agitation** — "thoughts" grid + honest-truth card
5. **WLA Reset Method** — three principles (Stabilise · Structure · Simplify)
6. **Transformation** — before/after (mindset, not bodies)
7. **What's included** — 8-card grid + Early-bird bonus
8. **Testimonials** — 6 written testimonials (cream cards, blush accents)
9. **Before / after photos** — 4 member results
10. **About Anna** — portrait + story + credentials
11. **Pricing** — £17 (£97 crossed out) + 7-day guarantee
12. **FAQ** — 8 menopause-aware objection handlers
13. **Final CTA** + **Footer**
14. **Sticky price bar** (fades in after scroll)

---

## Tweaks panel

Toggle via the toolbar "Tweaks" button. Controls:

- **CTA button colour** — Deep Navy (primary) or Soft Blush
- **Hero headline variant** — three variations
- **Sticky price bar** — on/off

Defaults are persisted inside the `/*EDITMODE-BEGIN*/…/*EDITMODE-END*/` block in the main HTML file.

---

## Responsive

Breakpoints in the `<style>` block of `21 Day Reset.html`:

- **≤ 960px (tablet)** — all grids collapse to single column; nav links hidden; headline sizes shrink; floating hero chips stack under the image
- **641–960px** — before/after photo grid shows 2 columns
- **≤ 640px (phone)** — section padding reduced; card padding reduced; tweaks panel fills width

---

## Editing content

- **Copy changes** — edit the relevant component in `components/` (e.g. testimonials in `content.jsx`, FAQ in `closing.jsx`).
- **Hero headline variants** — edit the `HEADLINES` object inside `21 Day Reset.html`.
- **Swap a photo** — drop the file into `assets/` and update the `src` in the relevant component.
- **CTA destination** — all primary CTAs use `https://sales.thewlacademy.com/may-reset/`, defined in `components/sections.jsx` (`PrimaryCTA` component) and `components/closing.jsx` (sticky bar).
- **Support email** — `support@theweightloss-academy.com` in the FAQ section (`components/closing.jsx`).

---

## Tech

- React 18.3.1 + Babel Standalone 7.29.0 (inline JSX, no build step)
- Google Fonts (Libre Baskerville + Alegreya Sans)
- No framework, no bundler — open `21 Day Reset.html` directly in a browser or host statically.
