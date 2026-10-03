// Shared small components for the WLA App sales page (/wla-app)

const Eyebrow = ({ children, color = 'var(--blush-deep)' }) => (
  <div style={{
    fontFamily: '"Alegreya Sans", sans-serif',
    fontSize: 12,
    fontWeight: 600,
    letterSpacing: '0.18em',
    textTransform: 'uppercase',
    color,
    display: 'inline-flex',
    alignItems: 'center',
    gap: 10,
  }}>
    <span style={{ width: 24, height: 1, background: color, opacity: 0.6 }} />
    {children}
  </div>
);

const SerifH = ({ children, size = 64, style = {}, as = 'h2', className }) => {
  const Tag = as;
  return (
    <Tag className={className} style={{
      fontFamily: '"Libre Baskerville", serif',
      fontWeight: 700,
      fontSize: size,
      lineHeight: 1.15,
      letterSpacing: '-0.005em',
      color: 'var(--ink)',
      margin: 0,
      textWrap: 'balance',
      ...style,
    }}>
      {children}
    </Tag>
  );
};

const Italic = ({ children }) => (
  <span style={{
    fontFamily: '"Libre Baskerville", serif',
    fontStyle: 'italic',
    fontWeight: 400,
    color: 'var(--blush-deep)',
  }}>{children}</span>
);

const Body = ({ children, size = 17, muted = false, style = {} }) => (
  <p style={{
    fontFamily: '"Alegreya Sans", sans-serif',
    fontSize: size,
    lineHeight: 1.6,
    color: muted ? 'var(--ink-muted)' : 'var(--body-ink)',
    margin: 0,
    textWrap: 'pretty',
    ...style,
  }}>{children}</p>
);

// CTA click tracker: fires both GA4 and Meta Pixel events.
// Safe no-op if either tag is missing (e.g. local dev, ad blockers).
function trackCtaClick(location, label) {
  // Google Analytics 4
  if (typeof window !== 'undefined' && typeof window.gtag === 'function') {
    window.gtag('event', 'cta_click', {
      cta_location: location,
      cta_label: label,
    });
  }
  // Meta Pixel — Lead event signals strong intent to Facebook's optimiser
  if (typeof window !== 'undefined' && typeof window.fbq === 'function') {
    window.fbq('track', 'Lead', {
      content_name: label,
      content_category: location,
    });
  }
}

// ---------------------------------------------------------------------------
// CAMPAIGN CONFIG — WLA App Founding Members
// ---------------------------------------------------------------------------

// ⚠️ TODO: the real Thrivecart link for the Founding Member offer.
const CHECKOUT_BASE_URL = 'https://sales.thewlacademy.com/wla-app/';

// Pricing
const PRICE          = '£97';   // 12 months, Founding Member rate
const PRICE_WAS      = '£297';  // regular annual price
const PRICE_SAVING   = '£200';  // saved every year on renewal
const PRICE_WEEKLY   = '£1.87'; // per week, for the smaller-chunk framing

// Timeline
//   OFFER_END      — Founding Member pricing closes at midnight at the end of
//                    Sunday 11th October, i.e. 00:00 on Monday the 12th.
//   CAMPAIGN_START — the 8 Week Fat Loss Challenge starts Monday 19th October.
const OFFER_START    = new Date('2026-10-03T09:00:00+01:00').getTime();
const OFFER_END      = new Date('2026-10-12T00:00:00+01:00').getTime();
const CAMPAIGN_START = new Date('2026-10-19T00:00:00+01:00').getTime();

const OFFER_HOURS = Math.round((OFFER_END - OFFER_START) / 3600000);

// The closing date is confirmed, so every countdown on the page is live: the
// announcement-bar timer, the countdown section and the timer inside the
// exit-intent modal. Setting this back to false switches all three off at once.
const OFFER_END_CONFIRMED = true;

// Scarcity — 500 Founding Member places in this first round.
// ⚠️ SPOTS_TAKEN must track real sales. Under the Digital Markets, Competition
// and Consumers Act 2024, invented scarcity is an offence.
const SPOTS_AVAILABLE = 500;
const SPOTS_TAKEN     = 0;
const SPOTS_LEFT      = Math.max(0, SPOTS_AVAILABLE - SPOTS_TAKEN);

// Build the Thrivecart checkout URL, forwarding any UTM parameters
// from the current page's query string so attribution carries through.
function getCheckoutUrl() {
  if (typeof window === 'undefined' || !window.location) return CHECKOUT_BASE_URL;
  const incoming = new URLSearchParams(window.location.search);
  const out = new URLSearchParams();
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'].forEach((k) => {
    const v = incoming.get(k);
    if (v) out.set(k, v);
  });
  const tail = out.toString();
  return tail ? CHECKOUT_BASE_URL + '?' + tail : CHECKOUT_BASE_URL;
}

// Campaign phase:
//   open    → now < OFFER_END  (offer price live, countdown showing)
//   started → now ≥ OFFER_END  (price has increased; countdown, "save £90" pill,
//             struck-through was-price and any bonus all drop away)
function getCampaignPhase() {
  if (!OFFER_END_CONFIRMED) return 'open';
  return Date.now() < OFFER_END ? 'open' : 'started';
}

const PrimaryCTA = ({ children, small = false, onClick, style = {}, location = 'primary' }) => (
  <a
    href={getCheckoutUrl()}
    target="_blank"
    rel="noopener"
    onClick={(e) => {
      // Re-resolve href at click time in case the URL has changed since render.
      e.currentTarget.href = getCheckoutUrl();
      trackCtaClick(location, typeof children === 'string' ? children : 'Primary CTA');
      if (onClick) onClick(e);
    }}
    style={{
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      gap: 10,
      background: 'var(--cta-bg, var(--ink))',
      color: '#FDFBF8',
      fontFamily: '"Alegreya Sans", sans-serif',
      fontSize: small ? 15 : 16,
      fontWeight: 600,
      letterSpacing: '0.04em',
      padding: small ? '14px 24px' : '0 30px',
      minHeight: small ? 46 : 56,
      boxSizing: 'border-box',
      borderRadius: 999,
      border: '1px solid transparent',
      lineHeight: 1.25,
      textDecoration: 'none',
      boxShadow: '0 8px 24px -10px rgba(0, 48, 96, 0.4)',
      transition: 'transform .2s, box-shadow .2s',
      cursor: 'pointer',
      ...style,
    }}
    onMouseEnter={(e) => {
      e.currentTarget.style.transform = 'translateY(-2px)';
      e.currentTarget.style.boxShadow = '0 14px 32px -10px rgba(0, 48, 96, 0.55)';
    }}
    onMouseLeave={(e) => {
      e.currentTarget.style.transform = 'translateY(0)';
      e.currentTarget.style.boxShadow = '0 8px 24px -10px rgba(0, 48, 96, 0.4)';
    }}
  >
    {children}
    <span style={{ fontSize: small ? 14 : 16 }}>→</span>
  </a>
);

// Guarantee line — sits under every CTA on the page.
const GuaranteeNote = ({ align = 'center', style = {} }) => (
  <div style={{
    display: 'flex',
    alignItems: 'flex-start',
    justifyContent: align === 'center' ? 'center' : 'flex-start',
    gap: 8,
    marginTop: 12,
    fontFamily: '"Alegreya Sans", sans-serif',
    fontSize: 13.5,
    color: 'var(--ink-muted)',
    lineHeight: 1.45,
    textAlign: align === 'center' ? 'center' : 'left',
    ...style,
  }}>
    <span style={{ flexShrink: 0, marginTop: 1 }}><Tick color="var(--blush-deep)" /></span>
    <span><strong style={{ color: 'var(--ink)' }}>7-day money-back guarantee.</strong> Join, look around, and if it&rsquo;s not for you we refund in full.</span>
  </div>
);

// NOTE: no PayPal button on this page. The Reset's PayPal link would take money
// for the wrong product, and no link exists yet for the Founding Member offer.

// Price anchor — the smaller-chunk framing.
const PriceAnchor = ({ style = {} }) => (
  <div style={{
    fontFamily: '"Libre Baskerville", serif',
    fontStyle: 'italic',
    fontSize: 16,
    color: 'var(--blush-deep)',
    ...style,
  }}>
    One payment, just {PRICE_WEEKLY} a week.
  </div>
);

const Placeholder = ({ label, ratio = '4/5', style = {} }) => (
  <div style={{
    aspectRatio: ratio,
    background: `repeating-linear-gradient(
      45deg,
      oklch(0.88 0.025 55),
      oklch(0.88 0.025 55) 8px,
      oklch(0.85 0.028 55) 8px,
      oklch(0.85 0.028 55) 16px
    )`,
    borderRadius: 4,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontFamily: '"JetBrains Mono", monospace',
    fontSize: 11,
    color: 'oklch(0.35 0.04 50)',
    letterSpacing: '0.06em',
    textTransform: 'uppercase',
    textAlign: 'center',
    padding: 16,
    ...style,
  }}>
    {label}
  </div>
);

const SoftCard = ({ children, style = {} }) => (
  <div style={{
    background: 'var(--paper)',
    border: '1px solid var(--hairline)',
    borderRadius: 20,
    padding: 32,
    ...style,
  }}>{children}</div>
);

// Quote mark SVG
const QuoteMark = ({ size = 40, color = 'var(--blush-deep)' }) => (
  <svg width={size} height={size * 0.75} viewBox="0 0 40 30" fill="none" style={{ opacity: 0.5 }}>
    <path d="M14 30V16H8C8 10.5 10.5 6 14 4V0C6 2 0 8.5 0 18V30H14ZM38 30V16H32C32 10.5 34.5 6 38 4V0C30 2 24 8.5 24 18V30H38Z" fill={color} />
  </svg>
);

// Small icon for checklists
const Tick = ({ color = 'var(--ink)' }) => (
  <svg width="18" height="18" viewBox="0 0 18 18" fill="none" style={{ flexShrink: 0, marginTop: 4 }}>
    <circle cx="9" cy="9" r="9" fill={color} opacity="0.22" />
    <path d="M5 9.5L7.5 12L13 6.5" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

const Cross = ({ color = 'var(--blush-deep)' }) => (
  <svg width="18" height="18" viewBox="0 0 18 18" fill="none" style={{ flexShrink: 0, marginTop: 4 }}>
    <circle cx="9" cy="9" r="9" fill={color} opacity="0.15" />
    <path d="M6 6L12 12M12 6L6 12" stroke={color} strokeWidth="1.8" strokeLinecap="round" />
  </svg>
);

const Divider = ({ style = {} }) => (
  <div style={{
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 14,
    color: 'var(--blush-deep)',
    ...style,
  }}>
    <span style={{ flex: 1, height: 1, background: 'var(--hairline)', maxWidth: 80 }} />
    <svg width="10" height="10" viewBox="0 0 10 10" fill="currentColor"><circle cx="5" cy="5" r="2" /></svg>
    <span style={{ flex: 1, height: 1, background: 'var(--hairline)', maxWidth: 80 }} />
  </div>
);

Object.assign(window, {
  Eyebrow, SerifH, Italic, Body, PrimaryCTA, GuaranteeNote, PriceAnchor,
  Placeholder, SoftCard,
  QuoteMark, Tick, Cross, Divider,
  trackCtaClick, getCheckoutUrl, getCampaignPhase,
  CHECKOUT_BASE_URL, OFFER_START, OFFER_END, OFFER_HOURS, OFFER_END_CONFIRMED, CAMPAIGN_START, PRICE_WEEKLY,
  SPOTS_AVAILABLE, SPOTS_TAKEN, SPOTS_LEFT,
  PRICE, PRICE_WAS, PRICE_SAVING,
});
