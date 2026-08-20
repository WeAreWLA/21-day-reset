# 21 Day Reset Sales Page

A soft editorial sales page for the WLA (Weight Loss Academy) 21 Day Reset — designed for women 45+ navigating menopause-related weight changes.

**Live:** https://join.wearewla.com/21-day-reset

All purchase CTAs link to: **https://sales.thewlacademy.com/may-reset/**

---

## Tech stack

- **React 18.3.1 + Babel Standalone 7.29.0** — inline JSX, no build step.
- **Google Fonts** — Libre Baskerville (serif) + Alegreya Sans (sans).
- **Vercel** — static hosting via file-based routing (`/21-day-reset/index.html` serves at `/21-day-reset`).
- **Subdomain** — `join.wearewla.com` → CNAME → `cname.vercel-dns.com`.

The page has no bundler. Open `21-day-reset/index.html` directly in a browser, or push to the connected Vercel project to deploy.

---

## Repo layout

```
.
├── 21-day-reset/
│   └── index.html              # Page entry — Hero, App shell, HEADLINES, responsive CSS, analytics
├── components/
│   ├── sections.jsx            # Shared primitives + trackCtaClick helper
│   ├── hero.jsx                # AnnouncementBar, Nav, StatPill, legacy Hero (overridden)
│   ├── method.jsx              # ProblemSection, WhatChangesIn21Days, HonestTruth,
│   │                           # WhyThisResetWorks, MethodSection, TransformSection, WhatHappens
│   ├── content.jsx             # IncludedSection, TestimonialsSection, AboutSection,
│   │                           # VideoTestimonialsSection
│   └── closing.jsx             # PricingSection, FAQSection, FinalCTA, StickyCTA, Footer,
│                               # FastActionBonusSection
├── assets/
│   ├── anna-hero.jpg           # Hero image (Anna at desk)
│   ├── anna-portrait.jpg       # About Anna portrait
│   ├── vicky-before-after.png  # Top-row before/after photos
│   ├── jill-before-after.jpg
│   ├── ruth-before-after.jpg
│   ├── barbara-before-after.png
│   ├── laura-before-after.png
│   ├── member-05-before-after.png  # 12-photo grid expansion
│   ├── member-06-before-after.png
│   ├── member-07-before-after.png  (objectFit: cover, objectPosition: 25%)
│   ├── member-08-before-after.jpeg
│   ├── member-09-before-after.png  (objectFit: cover, objectPosition: 25%)
│   ├── member-10-before-after.png  (objectFit: cover)
│   ├── member-11-before-after.png  (objectFit: cover, objectPosition: 25%)
│   └── member-12-before-after.png
├── vercel.json                 # { "trailingSlash": false }
└── README.md
```

All asset URLs in markup use **absolute paths** (`/assets/…`, `/components/…`) so the page works regardless of which path serves it.

---

## Page sections — current order

The render order lives in `App()` inside `21-day-reset/index.html`.

1. **AnnouncementBar** — animated navy → blush gradient bar with peach pulsing dot. "Pre-week starts Monday 4th May · Just £17 £97 — price rises soon." (Libre Baskerville)
2. **Nav** — logo + section links + "Join for £17" CTA. Hidden ≤960px.
3. **TweakableHero** — three swappable headlines (HEADLINES object), primary CTA, 7-day guarantee + £97 → £17 callout, 3-stat row (50,000+ women supported, 10 yrs, 4.9★), Anna hero image with two floating chips ("Led by Anna Wallace" credentials + "My menopause symptoms improved" Ruth quote).
4. **Early-bird banner** — peach card under the hero with 🎁 + "Early-bird bonus: 3-Week Fat Loss Accelerator Meal Plan / First 100 women only · instant access on signup / INCLUDED FREE."
5. **WhatChangesIn21DaysSection** — *"Here's what can change in just 21 days…"* — paper card with italic-blush numerals 01–05 next to each outcome, closing italic about momentum.
6. **ProblemSection** — *"You used to know how your body worked. And then, somewhere around 48, it changed."* — six rotated paper "thoughts" cards, then centered paragraphs about peri-/menopause physiology.
7. **HonestTruthSection** — Navy background. *"You don't struggle because you don't know what to do."* — peach hairline rules around italic insight, peach card listing what most diets rely on, italic "you start strong / life gets busy / fall back" beats, closing italic peach: "That's not your fault. It's the approach that's been wrong."
8. **WhyThisResetWorksSection** — *"Why this reset works when others haven't."* — "Helping you fuel your body properly for fat loss" centered italic, 4 Tick-bulleted benefits, three "No cutting everything out / No 1,200 calorie plans / No starting again next week" tiles, closing 36px serif: "Just a *simple structure* that works in real life."
9. **MethodSection** (`#method`) — *"Three simple principles. Designed to help you get results now."* — SHIFT steps 1/2/3 with bold second-clause titles ("stops cravings", "no overeating", "results without thinking").
10. **WhatHappensSection** — *"Here's what happens when you follow the Reset."* — paper card with 7 Tick-bulleted outcomes.
11. **IncludedSection** (`#included`) — *"Everything you need. Nothing you don't."* — 8-card grid (Meal Guide, Daily Coaching, Live Zoom, Workbook, Snack/Food Swaps, Drinks/Hydration, Freezer Pack, No-Prep List). No tag rows.
12. **FastActionBonusSection** — peach gradient card with dashed blush border. *"🎁 FAST ACTION BONUS (LIMITED) — The first 100 women who join receive my 3-week fat loss accelerator meal plan, completely FREE."* + 3 Tick bullets + "⚠️ Only available for the first 100 women" pill.
13. **PricingSection** (`#join-early`) — first £17 card. Includes Eyebrow "Secure your place", "One price. One reset. Everything included.", intro body, white card with crossed-out £97 + giant £17, Early-bird pill ("Early bird · save £80" in Libre Baskerville italic), 5-bullet feature list, primary CTA, footer trust line, then Early-bird and 7-day guarantee callouts.
14. **TestimonialsSection** (`#results`) — *"50,000 women. One reset."* on navy background. 3-col grid of 6 written testimonials with peach quote marks. Below: 3×4 grid (12) of before/after photos, big italic *"Real results from women just like you"* caption (white).
15. **AboutSection** — *"I'm Anna and I've been the woman starting over every Monday."* — Anna portrait + credentials sticker (BSc Food & Nutrition, Reg. Associate Nutritionist), bio paragraphs, closing italic blush: "50,000 clients later, this is the simplest approach that actually gets results."
16. **TransformSection** — *"From stuck to finally in control."* — two-column where-most-women-are-stuck (Cross icons) vs. what-the-Reset-gives-you (Tick icons).
17. **PricingSection (main, no heading)** — second £17 card. Replaces default heading with bridgeHeading: *"Join now to lock in the £17 early bird rate."* Same white card + Early-bird and guarantee callouts.
18. **VideoTestimonialsSection** — *"Hear what some of our WLA members have achieved."* 4 Vimeo embeds (Vicky, Ruth, Lisa, Lucy) with quote + name underneath.
19. **FAQSection** (`#faq`) — *"Questions from women like you."* 8 expandable items (sticky left column on desktop, support email mailto link).
20. **FinalCTA** — peach-gradient closing call-to-action. "You don't need to start over again."
21. **Footer** — navy.
22. **StickyCTA** — fixed bottom pill that fades in on scroll. Hidden on the very bottom of the page so it doesn't overlap the Footer.

---

## Brand system

### Colour palette (CSS variables in `21-day-reset/index.html`)

| Token           | Hex       | Role                                     |
|-----------------|-----------|------------------------------------------|
| `--bg`          | `#F9F7F4` | Cream White — page background            |
| `--cream-deep`  | `#E9DFD3` | Warm Beige — secondary sections          |
| `--paper`       | `#FDFBF8` | Near-white — cards                       |
| `--ink`         | `#003060` | Deep Navy — headlines, primary CTA       |
| `--ink-muted`   | `#5B6B82` | Supporting text (rarely used now)        |
| `--body-ink`    | `#333333` | Grey-Black — paragraphs (default)        |
| `--terracotta`  | `#F79F83` | Soft Blush — accents, italic emphasis    |
| `--blush-deep`  | `#E87F63` | Stronger blush — links, highlights, CTA  |
| `--peach`       | `#F5D9CE` | Lighter blush — bonus banners, callouts  |
| `--hairline`    | `#D9CFC3` | Borders                                  |

### Typography

- **Libre Baskerville** — 400 italic, 700 bold. All headlines, decorative italic emphasis (`<Italic>` component), the announcement bar, and the early-bird "save £80" pill.
- **Alegreya Sans** — 400/500/600. Body copy, UI, buttons, captions.

Both loaded via Google Fonts in the `<head>`.

---

## Analytics & tracking

All scripts live in the `<head>` of `21-day-reset/index.html`.

- **Google Analytics 4** — measurement ID `G-XSBKM60YTB`. Auto pageviews. Custom event `cta_click` fires from every CTA with `cta_location` and `cta_label` parameters.
- **Vercel Web Analytics** — `<script defer src="/_vercel/insights/script.js"></script>`. Auto pageviews + speed insights.
- **Meta Pixel** — ID `410999599864541`. Auto `PageView` + `Lead` event on every CTA click (alongside the GA4 event). `noscript` fallback included.

CTA tracking runs through `trackCtaClick(location, label)` in `components/sections.jsx`. It fires both GA4 and Meta events, and is also exposed on `window.trackCtaClick` for the announcement-bar / sticky-bar links to use (those aren't React `<PrimaryCTA>` instances).

| `cta_location` value | Where the button sits |
|---|---|
| `nav` | Nav bar — "Join for £17" (desktop only) |
| `hero` | Below the hero headline — "Secure your place for £17" |
| `pricing` | Both £17 white cards — "Join the Reset — £17" |
| `final` | Final CTA at the bottom — "Join the 21 Day Reset — £17" |
| `sticky` | Floating sticky bar — "Secure your place →" |

In GA4, register `cta_location` and `cta_label` as **custom dimensions** (Admin → Custom definitions) to break clicks down by button location in Explore reports.

---

## Responsive

Three breakpoints in `21-day-reset/index.html`:

- **≤ 960px (tablet)** — multi-col grids collapse to single column; nav hidden; headline sizes shrink; floating hero chips reposition; pricing card top padding bumped to 72 so the Early-bird pill clears the £17.
- **641 – 960px (tablet only)** — before/after photo grid is 2 columns instead of 4.
- **≤ 640px (phone)** — section padding reduced; tweaks panel fills width; sticky CTA bar shrinks; Ruth quote chip pulled to the top-left corner of the hero image; Early-bird banner inlines its 🎁 emoji and breaks the plan name onto its own line; many section gaps tightened with class-specific overrides (`.hero-section`, `.early-bird-banner-section`, `.whatchanges-section`, `section#method`, `.whathappens-section`, `.included-section`, `.fastaction-section`, `.transform-section`, `.pricing-bridge`, `.video-testimonials-section`, `section#faq.faq-section`).
- **≤ 420px (small phones, mostly Android)** — sticky CTA tightens further; hero image `object-position: 25% center` so Anna stays in frame.

---

## Tweaks panel

Toggle by sending `__activate_edit_mode` from the parent window. Controls:

- **CTA button colour** — Deep Navy (default) or Soft Blush
- **Hero headline variant** — three options (`nothing-works`, `feel-like-me`, `metabolism-broken`)
- **Sticky price bar** — on/off

Defaults persist inside the `/*EDITMODE-BEGIN*/…/*EDITMODE-END*/` block at the top of the inline `<script type="text/babel">` in `21-day-reset/index.html`.

---

## Editing content

- **Hero copy** — `HEADLINES` object near the top of `21-day-reset/index.html`.
- **Stats row** — inline JSX inside `TweakableHero` in `21-day-reset/index.html`.
- **Section copy** — edit the relevant component:
  - Problem agitation, SHIFT method, transformation, etc. → `components/method.jsx`
  - Included grid, written testimonials, before/after photo array, About bio, video testimonials → `components/content.jsx`
  - Pricing, FAQ items, Final CTA, sticky bar, footer, fast-action bonus → `components/closing.jsx`
  - Announcement bar copy and nav → `components/hero.jsx`
- **Photos** — drop the file into `/assets/`, update the `src` (use absolute path: `/assets/filename.ext`).
- **CTA destination** — all primary CTAs use `https://sales.thewlacademy.com/may-reset/`. Defined in `components/sections.jsx` (`PrimaryCTA`) and `components/closing.jsx` (sticky bar).
- **Support email** — `support@theweightloss-academy.com` in the FAQ section sticky column (`components/closing.jsx`).
- **Vimeo testimonials** — array `VIDEO_TESTIMONIALS` at the bottom of `components/content.jsx`. Each item is `{ id, hash, name, quote }`. Embed URL is built from id + hash.

---

## Deployment

- Push to the connected branch (`claude/implement-21-day-reset-ynZ5a`).
- Vercel auto-deploys in ~30 seconds. Production branch can be set in Vercel → project → Settings → Git.
- DNS: `join.wearewla.com` → CNAME → `cname.vercel-dns.com` (configured in Squarespace DNS).
- Routing: file-based via `21-day-reset/index.html` resolved at `/21-day-reset` thanks to `vercel.json` `trailingSlash: false`.

---

## Birthday promo — `/bday-promo`

Anna's birthday offer: the same 21 Day Reset at **£7** (was £97), starting **Monday 31st August**.

**Live:** https://join.wearewla.com/bday-promo
**Thank you page:** https://join.wearewla.com/bday-promo/ty

It's a standalone clone of the `/21-day-reset` page, so editing it can never affect the
original. It has its own copy of the components:

```
bday-promo/
├── index.html                  # Page entry — HEADLINES, App shell, responsive CSS, analytics
├── components/                 # Private copies of the shared components
│   ├── sections.jsx            # ⭐ CAMPAIGN CONFIG lives here (see below)
│   ├── hero.jsx                # AnnouncementBar, Nav
│   ├── method.jsx              # unchanged from /components
│   ├── content.jsx             # unchanged from /components
│   └── closing.jsx             # Countdown, Pricing, FAQ, FinalCTA, StickyCTA, BirthdayBonusSection
└── ty/
    └── index.html              # Thank-you page (static HTML, no React)
```

### Checkout

Card checkout is `https://sales.thewlacademy.com/bday-promo/`, held in
`CHECKOUT_BASE_URL` at the top of `bday-promo/components/sections.jsx`. Every primary
CTA reads from it — hero, both pricing cards, final CTA, sticky bar, exit-intent modal
and the social-proof toast. UTM parameters on the incoming URL are forwarded through.

PayPal is `PAYPAL_URL` in the same block and appears as a second button under each CTA.

`bday-promo/upsell-1-year.html` is the ThriveCart upsell shown after purchase: WLA App
Founding Member, one year for £97 against a planned £297 public price, 50 places. It
contains **no buttons** — ThriveCart's own Add / Decline render below it. Suggested
button labels are in the file header.

The upsell's app gallery expects four screenshots in `/assets/`, referenced by absolute
URL so they resolve on ThriveCart's domain:

| Filename | Screen |
|---|---|
| `app-01-daily-tracker.jpg` | Daily Tracker, the food/mood/water/sleep/movement cards |
| `app-02-log-meal.jpg` | The Breakfast "Log your meal" sheet |
| `app-03-meal-plan.jpg` | Nutrition → Plan, "Anna's picked your week" |
| `app-04-recipes.jpg` | Nutrition → Recipes with the Filters sheet open |

The four crops range from 0.50 to 0.87 in aspect, so the frames are a fixed 4:5 with
`object-fit: contain` on a cream ground — a phone-shaped frame with `cover` would cut the
bottom off most of them. Each is capped at 1000px and saved as progressive JPEG. If a
file is missing its tile falls back to a named card rather than a broken image.

Note these are *not* the same as the older shots in `assets/app-screenshots/`, which show
a previous version of the app.

`bday-promo/cart-content.html` is the marketing block for the ThriveCart cart page
itself: paste it into ThriveCart's HTML content area. All CSS is scoped under
`.wla-cart`. **Its countdown has its own copy of the deadline** (`WLA_OFFER_END` in the
inline script) because it runs outside this codebase — change it whenever `OFFER_END`
changes, or the cart and the sales page will show different times.

### Campaign config

All five values live in one block at the top of `bday-promo/components/sections.jsx`:

| Constant | Value | Used for |
|---|---|---|
| `CHECKOUT_BASE_URL` | live | Card checkout — every primary CTA |
| `PAYPAL_URL` | live | PayPal alternative — the yellow button under each CTA |
| `PRICE` | `£7` | Offer price |
| `PRICE_WAS` | `£97` | Struck-through regular price |
| `PRICE_SAVING` | `£90` | "save £90" pill |
| `OFFER_START` | Thu 20 Aug 2026 08:00 BST | Cart opens |
| `OFFER_END` | Sun 23 Aug 2026 23:59 BST | Cart closes — countdown target + phase switch |
| `OFFER_HOURS` | *derived* | `OFFER_END − OFFER_START`, rounded to whole hours (88) |
| `CAMPAIGN_START` | Mon 31 Aug 2026 | Pre-week start date shown in copy |
| `SPOTS_AVAILABLE` | `100` | Total places |
| `SPOTS_TAKEN` | `10` | Places gone — **update by hand as real sales come in** |
| `SPOTS_LEFT` | *derived* | `SPOTS_AVAILABLE − SPOTS_TAKEN` |

⚠️ `SPOTS_TAKEN` drives the "X of 100 places left" bar above *What can change in 21 days*.
It must reflect real numbers: under the Digital Markets, Competition and Consumers Act
2024 invented scarcity is an offence, so never inflate it.

**Never hard-code an hour count in copy.** Every "for N hours only" line reads
`window.OFFER_HOURS`, so changing `OFFER_START` or `OFFER_END` updates the announcement
bar, hero key facts, countdown tiles, pricing intro, sticky bar and final CTA together.

`getCampaignPhase()` returns `open` before `OFFER_END` and `started` after it. The page
re-checks every minute, so when the window closes it switches itself over without a
redeploy: the countdown, the birthday-bonus banner, the "save £90" pill and the
struck-through £97 all drop away.

### Promo graphic

`bday-promo/promo-graphic.html` is the source for the 1:1 campaign graphic (coral banner,
title, fanned guide covers, device, starburst price, scarcity pill, navy footer). Exports
are `assets/bday-promo-square.png` (1080) and `assets/bday-promo-square@2x.png` (2160).

Regenerate by serving the repo root and screenshotting the `.card` element at
`deviceScaleFactor: 2`. It pulls the guide-cover photos from `/assets`, so it must be
served rather than opened as a file.

Two content rules for this graphic: it shows **only what the £7 offer includes** — no app
or Members' Area screens, since those belong to the upsell — and the scarcity pill reads
"ONLY 100 PLACES" rather than a places-left count, which should only appear once the
figure is true.

### Recipe photos

The WLA Members' Area block showcases five recipe photos. Drop these files into `/assets/`:

| Filename | Photo |
|---|---|
| `members-recipe-01.jpg` | Steak fajita wrap |
| `members-recipe-02.jpg` | Strawberry overnight oats |
| `members-recipe-03.jpg` | Creamy chicken & broccoli pasta |
| `members-recipe-04.jpg` | Raspberry baked oat muffins |
| `members-recipe-05.jpg` | Cheeseburger gnocchi |

All five are capped at 900px on the long edge and saved as progressive JPEG (~130 KB
each). Keep replacements to the same treatment — the tiles render at roughly 215px, so
anything larger is wasted bytes on a paid-traffic page.

They're square-cropped (`object-fit: cover`), so any aspect ratio works. If a file is
missing the tile degrades to a soft peach card with the dish name rather than a
broken-image icon. The list lives in `MEMBERS_RECIPES` in
`bday-promo/components/content.jsx` — filenames and captions must both be updated there
if the photos are swapped.

### Page order

1. Hero — title, promise line, key-facts panel (£7 / OFFER_HOURS, pre-week Mon 31 Aug, 100 spots)
2. **Real results from women just like you** — 12 before/after photos on navy (`ResultsGridSection`)
3. Countdown — live timer to `OFFER_END`
4. What changes in 21 days → Problem → Honest truth → Why this works → Method → What happens
5. What's included — 8 cards **+ two birthday bonus cards**
6. Bonus 1 (WLA Members' Area) and Bonus 2 (three weekly masterclasses) sit inside What's included → Pricing
7. Written testimonials → About Anna → Transform → Pricing (bridge)
8. Video testimonials → FAQ → Final CTA → Footer

Plus, outside the flow: the sticky price bar and an **exit-intent modal** (desktop only,
once per browser session, 8-second arming delay, carries the live timer).

On phones the hero children are explicitly re-ordered with flexbox `order` so the CTA
sits above the fold — badge, headline, results, **CTA**, then the detail panel. Every
child needs an explicit order there or an ordered one jumps the whole column.

### What differs from `/21-day-reset`

- Birthday framing throughout — announcement bar, hero, pricing eyebrow, final CTA.
- £7 / £97 / save £90 in place of £17 / £97 / save £80.
- Single countdown to Monday 31st August (the original had a two-stage pre-week/kickoff timeline).
- "Early-bird bonus" renamed to "Birthday bonus" (`BirthdayBonusSection`).
- Extra FAQ: *"Why is it only £7?"*; the start-date FAQ answer points at 31st August.
- Meta Pixel `1159782482636500` (matching the current campaign pages) rather than the older `410999599864541`.
- Three hero headline variants in `HEADLINES`, default `birthday`, swappable from the tweaks panel.

### Thank-you page

`bday-promo/ty/index.html` follows the same pattern as the other paid thank-you pages:
success tick, "you're in" tag, start-date card, welcome-email preview, and the two next
steps (whitelist the email, join the private Facebook group `446785765084694`). It fires
a Meta `Purchase` event with `value: 7, currency: GBP`, and is `noindex`.
