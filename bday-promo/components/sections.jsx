// Shared small components for the Birthday Promo sales page (/bday-promo)

const Eyebrow = ({ children, color = 'var(--blush-deep)' }) => (
  <div style={{
    fontFamily: 'Work Sans, sans-serif',
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

const SerifH = ({ children, size = 64, style = {}, as = 'h2' }) => {
  const Tag = as;
  return (
    <Tag style={{
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
// CAMPAIGN CONFIG — edit these five values, nothing else.
// ---------------------------------------------------------------------------

// ⚠️ TODO: swap in the new Thrivecart link for the birthday promo.
//    This is currently pointing at the old May Reset cart as a placeholder so
//    the page is previewable. Every CTA on /bday-promo and /bday-promo/ty
//    reads from this one constant.
const CHECKOUT_BASE_URL = 'https://sales.thewlacademy.com/may-reset/';

// Pricing
const PRICE          = '£7';   // birthday offer price
const PRICE_WAS      = '£97';  // regular price, shown struck through
const PRICE_SAVING   = '£90';  // PRICE_WAS − PRICE

// Timeline — the Reset starts Monday 31st August 2026 (BST).
// The birthday offer closes the moment the Reset begins.
const CAMPAIGN_START = new Date('2026-08-31T00:00:00+01:00').getTime();

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

// Campaign timeline:
//   open    → now < Mon 31 Aug 2026 00:00 BST  (birthday offer live, countdown showing)
//   started → now ≥ Mon 31 Aug 2026 00:00 BST  (Reset has begun; countdown hidden,
//             birthday-specific scarcity copy retired)
function getCampaignPhase() {
  return Date.now() < CAMPAIGN_START ? 'open' : 'started';
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
      fontSize: small ? 15 : 17,
      fontWeight: 600,
      letterSpacing: '0.04em',
      padding: small ? '14px 24px' : '20px 36px',
      borderRadius: 999,
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
  Eyebrow, SerifH, Italic, Body, PrimaryCTA, Placeholder, SoftCard, QuoteMark, Tick, Cross, Divider,
  trackCtaClick, getCheckoutUrl, getCampaignPhase,
  CHECKOUT_BASE_URL, CAMPAIGN_START, PRICE, PRICE_WAS, PRICE_SAVING,
});
