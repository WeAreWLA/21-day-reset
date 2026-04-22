// Hero + announcement bar

const AnnouncementBar = () => (
  <div className="announcement-bar" style={{
    color: 'var(--paper)',
    fontFamily: '"Alegreya Sans", sans-serif',
    textAlign: 'center',
    letterSpacing: '0.04em',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 18,
    flexWrap: 'wrap',
  }}>
    <span style={{ display: 'inline-flex', alignItems: 'center', gap: 10 }}>
      <span className="announcement-dot" />
      Pre-week starts <strong style={{ color: 'var(--peach)' }}>Monday 4th May</strong>
    </span>
    <span style={{ opacity: 0.5 }}>·</span>
    <span>
      Just <strong style={{ color: 'var(--peach)', fontSize: '1.05em' }}>£17</strong>
      {' '}
      <span style={{ opacity: 0.65, textDecoration: 'line-through' }}>£97</span>
      {' '}— price rises soon
    </span>
    <a href="https://sales.thewlacademy.com/may-reset/" target="_blank" rel="noopener" className="announcement-cta"
      onClick={() => window.trackCtaClick && window.trackCtaClick('announcement', 'Secure your place')}>
      Secure your place <span style={{ fontSize: 14 }}>→</span>
    </a>
  </div>
);

const Nav = () => (
  <nav style={{
    maxWidth: 1240,
    margin: '0 auto',
    padding: '22px 32px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
  }}>
    <div style={{
      fontFamily: '"Libre Baskerville", serif',
      fontWeight: 700,
              fontSize: 22,
      letterSpacing: '-0.01em',
      color: 'var(--ink)',
    }}>
      Weight Loss Academy
      <span style={{
        fontFamily: '"Libre Baskerville", serif',
        fontStyle: 'italic',
        fontSize: 13,
        color: 'var(--blush-deep)',
        marginLeft: 8,
      }}>by Anna Wallace</span>
    </div>
    <div style={{
      display: 'flex',
      gap: 28,
      fontFamily: '"Alegreya Sans", sans-serif',
      fontSize: 14,
      color: 'var(--ink-muted)',
      alignItems: 'center',
    }}>
      <a href="#method" style={navLinkStyle}>The method</a>
      <a href="#included" style={navLinkStyle}>What's included</a>
      <a href="#results" style={navLinkStyle}>Results</a>
      <a href="#faq" style={navLinkStyle}>FAQ</a>
      <PrimaryCTA small location="nav">Join for £17</PrimaryCTA>
    </div>
  </nav>
);

const navLinkStyle = {
  color: 'var(--ink-muted)',
  textDecoration: 'none',
  fontWeight: 500,
};

const StatPill = ({ num, label }) => (
  <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
    <span style={{
      fontFamily: '"Libre Baskerville", serif',
      fontWeight: 700,
              fontSize: 32,
      color: 'var(--ink)',
      lineHeight: 1,
    }}>{num}</span>
    <span style={{
      fontFamily: '"Alegreya Sans", sans-serif',
      fontSize: 12,
      color: 'var(--ink-muted)',
      letterSpacing: '0.04em',
    }}>{label}</span>
  </div>
);

const Hero = () => (
  <section style={{
    maxWidth: 1240,
    margin: '0 auto',
    padding: '40px 32px 80px',
    display: 'grid',
    gridTemplateColumns: '1.1fr 0.9fr',
    gap: 72,
    alignItems: 'center',
  }}>
    <div>
      <Eyebrow>A 21-day reset for women 45+</Eyebrow>
      <SerifH as="h1" size={76} style={{ marginTop: 22, marginBottom: 24 }}>
        If you've started over <Italic>more times</Italic> than you can count —
        this is the one that finishes.
      </SerifH>
      <Body size={19} muted style={{ maxWidth: 560, marginBottom: 36 }}>
        An evidence based, nutritionist-designed weight loss reset for women 45+ who feel like their body stopped responding. No 1,200-calorie plans. No cutting out carbs. No intense exercise.
      </Body>

      <div style={{ display: 'flex', alignItems: 'center', gap: 20, flexWrap: 'wrap', marginBottom: 44 }}>
        <PrimaryCTA>Secure your place for £17</PrimaryCTA>
        <div style={{
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 13,
          color: 'var(--ink-muted)',
          lineHeight: 1.5,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <Tick /> 7-day money-back guarantee
          </div>
          <div style={{ marginTop: 4, opacity: 0.75 }}>Regular price £97 · Pre-week Mon 4 May</div>
        </div>
      </div>

      <div style={{
        display: 'flex',
        gap: 48,
        paddingTop: 28,
        borderTop: '1px solid var(--hairline)',
      }}>
        <StatPill num="50,000+" label="WOMEN SUPPORTED" />
        <StatPill num="10 yrs" label="CLINICAL PRACTICE" />
        <StatPill num="4.9 ★" label="MEMBER RATING" />
      </div>
    </div>

    <div style={{ position: 'relative' }}>
      <div style={{
        position: 'relative',
        aspectRatio: '4/5',
        borderRadius: 8,
        overflow: 'hidden',
      }}>
        <Placeholder
          label={`Hero portrait of Anna\n(warm, natural light, kitchen\nor studio. Confident,\napproachable. 45+ relatable.)`}
          ratio="4/5"
          style={{ position: 'absolute', inset: 0, whiteSpace: 'pre-line' }}
        />
      </div>

      {/* Floating credential card */}
      <div style={{
        position: 'absolute',
        bottom: -28,
        left: -28,
        background: 'var(--paper)',
        padding: '18px 22px',
        borderRadius: 12,
        boxShadow: '0 20px 40px -18px rgba(80, 40, 20, 0.25)',
        border: '1px solid var(--hairline)',
        maxWidth: 260,
      }}>
        <div style={{
          fontFamily: '"Libre Baskerville", serif',
          fontStyle: 'italic',
          fontSize: 13,
          color: 'var(--blush-deep)',
          marginBottom: 6,
        }}>Led by</div>
        <div style={{
          fontFamily: '"Libre Baskerville", serif',
          fontWeight: 700,
              fontSize: 22,
          color: 'var(--ink)',
          marginBottom: 2,
        }}>Anna Wareham</div>
        <div style={{
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 12,
          color: 'var(--ink-muted)',
          letterSpacing: '0.02em',
          lineHeight: 1.4,
        }}>
          BSc Food & Nutrition<br />
          Registered Associate Nutritionist
        </div>
      </div>

      {/* Top-right quote chip */}
      <div style={{
        position: 'absolute',
        top: 24,
        right: -24,
        background: 'var(--cream-deep)',
        padding: '14px 18px',
        borderRadius: 10,
        maxWidth: 220,
        border: '1px solid var(--hairline)',
        transform: 'rotate(2deg)',
      }}>
        <div style={{
          fontFamily: '"Libre Baskerville", serif',
          fontStyle: 'italic',
          fontSize: 14,
          color: 'var(--ink)',
          lineHeight: 1.4,
        }}>
          "My menopause symptoms improved and I lost 12 lbs."
        </div>
        <div style={{
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 11,
          color: 'var(--ink-muted)',
          marginTop: 6,
          letterSpacing: '0.06em',
        }}>— RUTH, 54</div>
      </div>
    </div>
  </section>
);

Object.assign(window, { Hero, Nav, AnnouncementBar });
