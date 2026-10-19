// Page shell for /wla-app: campaign copy, the App component and the hero.
// Compiled into app.js by build.mjs — edit here, never the compiled file.


const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "headlineVariant": "default",
  "showStickyCTA": true,
  "ctaStyle": "navy"
} /*EDITMODE-END*/;

const HEADLINES = {
  "default": {
    eyebrow: "Exclusive Founding Member invitation",
    title: <>Become a WLA App Founding Member.<br /><Italic>Get my 8 Week Fat Loss Challenge FREE.</Italic></>,
  },
  "alt-a": {
    eyebrow: "Exclusive Founding Member invitation",
    title: <>Lose up to a stone<br /><Italic>before Christmas.</Italic></>,
  },
  "alt-b": {
    eyebrow: "Exclusive Founding Member invitation",
    title: <>The new WLA App is here.<br /><Italic>Be one of the first 500.</Italic></>,
  }
};

const SUBHEADLINE = <>Join for <strong>£97 for 12 months</strong>. Pre-Week starts <strong>Monday 19th October</strong> and we kick off on <strong>Monday 26th</strong>. Lose up to a stone before Christmas, without counting calories.</>;

// The four things a Founding Member gets, in one block under the headline.
const HERO_POINTS = [
  <><strong>12 months of WLA app access £97</strong> <span style={{ color: 'var(--ink-muted)' }}>(regular price £297)</span></>,
  <><strong>FREE 8 Week Fat Loss Challenge</strong>, kicking off Monday 26th October</>,
  <><strong>FREE January Reset</strong> + first 2027 Challenge</>,
  <><strong>Renew for £97 (never £297)</strong> if you want to stay in the future</>,
];

function App() {
  const [tweaks, setTweaks] = React.useState(TWEAK_DEFAULTS);
  const [tweaksOpen, setTweaksOpen] = React.useState(false);
  const [stickyVisible, setStickyVisible] = React.useState(false);
  const [phase, setPhase] = React.useState(() => (window.getCampaignPhase ? window.getCampaignPhase() : 'open'));

  // Re-check the campaign phase every minute so the page flips from the
  // open state to the started state when the timer runs out, without a refresh.
  React.useEffect(() => {
    if (!window.getCampaignPhase) return;
    const id = setInterval(() => {
      const p = window.getCampaignPhase();
      setPhase((prev) => (prev !== p ? p : prev));
    }, 60000);
    return () => clearInterval(id);
  }, []);

  // Apply CTA style
  React.useEffect(() => {
    if (tweaks.ctaStyle === 'blush') {
      document.documentElement.style.setProperty('--cta-bg', '#E87F63');
    } else {
      document.documentElement.style.setProperty('--cta-bg', '#003060');
    }
  }, [tweaks.ctaStyle]);

  // Sticky CTA visibility
  React.useEffect(() => {
    const onScroll = () => {
      setStickyVisible(window.scrollY > 800 && window.scrollY < document.body.scrollHeight - 1400);
    };
    window.addEventListener('scroll', onScroll);
    onScroll();
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  // Edit mode handshake
  React.useEffect(() => {
    const handler = (e) => {
      if (e.data?.type === '__activate_edit_mode') setTweaksOpen(true);
      if (e.data?.type === '__deactivate_edit_mode') setTweaksOpen(false);
    };
    window.addEventListener('message', handler);
    window.parent.postMessage({ type: '__edit_mode_available' }, '*');
    return () => window.removeEventListener('message', handler);
  }, []);

  const updateTweak = (key, value) => {
    const next = { ...tweaks, [key]: value };
    setTweaks(next);
    window.parent.postMessage({ type: '__edit_mode_set_keys', edits: { [key]: value } }, '*');
  };

  // Override Hero per tweak
  const headline = HEADLINES[tweaks.headlineVariant] || HEADLINES['default'];

  return (
    <>
      <AnnouncementBar />
      {/* Tweakable hero wrapper */}
      <TweakableHero headline={headline} phase={phase} />
      <ResultsGridSection />
      {/* After the first proof block: seen early, but belief before urgency. */}
      {phase === 'open' && <SpotsRemainingSection />}
      <AppIntroSection />
      <AppGallerySection />
      <AppClipsSection />
      <ChallengeBonusSection />
      <FeaturesSection />
      <BonusesSection />
      {/* Renders nothing until OFFER_END_CONFIRMED is set in sections.jsx. */}
      <CountdownSection />
      <PricingSection sectionId="join-early" phase={phase} />
      <WhyJoinNowSection />
      <ForYouSection />
      <TestimonialsSection />
      <AboutSection />
      <PricingSection showHeading={false} phase={phase} bridgeHeading={
        <SerifH size={40} style={{ lineHeight: 1.3 }}>
          {phase === 'open'
            ? <>Join the first 500. Pre-Week starts Monday 19th, we kick off <Italic>Monday 26th October.</Italic></>
            : <>The WLA App is open to <Italic>everyone.</Italic></>}
        </SerifH>
      } />
      <VideoTestimonialsSection />
      <FAQSection />
      <FinalCTA />
      <Footer />
      {tweaks.showStickyCTA && <StickyCTA visible={stickyVisible} />}
      <ExitIntentModal />

      {tweaksOpen &&
      <div className="tweaks-panel">
          <h4>Tweaks</h4>
          <label>CTA button colour</label>
          <select value={tweaks.ctaStyle}
        onChange={(e) => updateTweak('ctaStyle', e.target.value)}
        style={{ marginBottom: 14 }}>
            <option value="navy">Deep Navy (primary)</option>
            <option value="blush">Soft Blush</option>
          </select>
          <label>Hero headline variant</label>
          <select value={tweaks.headlineVariant}
        onChange={(e) => updateTweak('headlineVariant', e.target.value)}
        style={{ marginBottom: 14 }}>
            <option value="default">"Become a WLA App Founding Member"</option>
            <option value="alt-a">"Lose up to a stone before Christmas"</option>
            <option value="alt-b">"The new WLA App is here"</option>
          </select>
          <label style={{ display: 'flex', alignItems: 'center', gap: 8, textTransform: 'none', letterSpacing: 0, fontSize: 13, color: 'var(--ink)' }}>
            <input type="checkbox" checked={tweaks.showStickyCTA}
          onChange={(e) => updateTweak('showStickyCTA', e.target.checked)} />
            Sticky price bar
          </label>
        </div>
      }
    </>);

}

function TweakableHero({ headline, phase = 'open' }) {
  return (
    <>
    <section className="hero-section" style={{
      maxWidth: 1240,
      margin: '0 auto',
      padding: '40px 32px 80px',
      display: 'grid',
      gridTemplateColumns: '1.1fr 0.9fr',
      gap: 72,
      alignItems: 'center'
    }}>
      <div className="hero-left" style={{ display: 'flex', flexDirection: 'column' }}>
        <div className="hero-badge" style={{
          display: 'inline-flex', alignItems: 'center', gap: 10,
          alignSelf: 'flex-start',
          background: 'var(--peach)',
          border: '1px solid var(--blush-deep)',
          borderRadius: 999,
          padding: '10px 22px',
          marginBottom: 20,
        }}>
          <span style={{ fontSize: 20, lineHeight: 1 }}>✨</span>
          <span style={{
            fontFamily: '"Libre Baskerville", serif',
            fontWeight: 700,
            fontSize: 15,
            letterSpacing: '0.01em',
            color: 'var(--ink)',
            lineHeight: 1.3,
          }}>{headline.eyebrow}</span>
        </div>
        <SerifH as="h1" className="hero-title" size={60} style={{ marginTop: 0, marginBottom: 18 }}>
          {headline.title}
        </SerifH>
        <div className="hero-sub" style={{
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 20,
          lineHeight: 1.5,
          color: 'var(--body-ink)',
          maxWidth: 560,
          marginBottom: 26,
        }}>{SUBHEADLINE}</div>
        <div className="programme-results" style={{
          display: 'flex', flexDirection: 'column', gap: 10,
          maxWidth: 560, marginBottom: 30,
          background: 'var(--paper)',
          border: '1px solid var(--hairline)',
          borderLeft: '4px solid var(--blush-deep)',
          borderRadius: 14,
          padding: '22px 26px',
        }}>
          {HERO_POINTS.map((r, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
              <span style={{ flexShrink: 0, marginTop: 4 }}><Tick color="var(--blush-deep)" /></span>
              <div style={{
                fontFamily: '"Alegreya Sans", sans-serif',
                fontSize: 18,
                lineHeight: 1.35,
                color: 'var(--ink)',
              }}>{r}</div>
            </div>
          ))}
          <div style={{
            marginTop: 6,
            paddingTop: 14,
            borderTop: '1px solid var(--hairline)',
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 16,
            color: 'var(--blush-deep)',
          }}>
            One-off payment. That works out at less than £2 a week.
          </div>
        </div>

        <div className="hero-cta-block" style={{ marginBottom: 44 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 360 }}>
            <PrimaryCTA location="hero" style={{ width: '100%' }}>Become a Founding Member {window.PRICE}</PrimaryCTA>
            <PayPalCTA location="hero" align="left" style={{ marginTop: 0 }} />
            <GuaranteeNote align="left" style={{ marginTop: 0, maxWidth: 480 }} />
          </div>
        </div>

        <div className="hero-stats" style={{
          display: 'flex', gap: 48, paddingTop: 28, borderTop: '1px solid var(--hairline)'
        }}>
          <div><div style={{ fontFamily: '"Libre Baskerville", serif', fontSize: 32, lineHeight: 1 }}>50,000+</div><div style={{ fontSize: 12, color: 'var(--ink-muted)', letterSpacing: '0.04em', marginTop: 8 }}>WOMEN SUPPORTED</div></div>
          <div><div style={{ fontFamily: '"Libre Baskerville", serif', fontSize: 32, lineHeight: 1 }}>11 yrs</div><div style={{ fontSize: 12, color: 'var(--ink-muted)', letterSpacing: '0.04em', marginTop: 8 }}>CLINICAL PRACTICE</div></div>
          <div><div style={{ fontFamily: '"Libre Baskerville", serif', fontSize: 32, lineHeight: 1 }}>4.9 ★</div><div style={{ fontSize: 12, color: 'var(--ink-muted)', letterSpacing: '0.04em', marginTop: 8 }}>MEMBER RATING</div></div>
        </div>
      </div>

      <div className="hero-media" style={{ position: 'relative' }}>
        <div className="hero-photo" style={{
          aspectRatio: '4/5',
          borderRadius: 4,
          overflow: 'hidden',
          background: '#F9F7F4',
        }}>
          <img src="/assets/anna-hero.jpg" alt="Anna Wallace" className="hero-img" fetchpriority="high" decoding="async" style={{
            width: '100%', height: '100%', objectFit: 'cover', display: 'block',
          }} />
        </div>

        {/* The app itself, playing, over the left edge of the photo. */}
        <div className="hero-phone" style={{
          position: 'absolute', left: -46, bottom: 54,
          width: 184,
          aspectRatio: '1004 / 2000',
          borderRadius: 24,
          border: '7px solid var(--ink)',
          overflow: 'hidden',
          background: 'var(--bg)',
          boxShadow: '0 30px 56px -22px rgba(0, 48, 96, 0.55)',
        }}>
          <video
            poster="/assets/app-clip-home-poster.jpg"
            autoPlay muted loop playsInline preload="metadata"
            aria-label="The WLA app home screen"
            style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'top center', display: 'block' }}
          >
            <source src="/assets/app-clip-home.webm" type="video/webm" />
            <source src="/assets/app-clip-home.mp4" type="video/mp4" />
          </video>
        </div>

        <div className="hero-cred" style={{
          position: 'absolute', bottom: -28, right: -20,
          background: 'var(--paper)', padding: '18px 22px', borderRadius: 12,
          boxShadow: '0 20px 40px -18px rgba(80, 40, 20, 0.25)',
          border: '1px solid var(--hairline)', maxWidth: 260
        }}>
          <div style={{ fontFamily: '"Libre Baskerville", serif', fontStyle: 'italic', fontSize: 13, color: 'var(--terracotta)', marginBottom: 6 }}>Led by</div>
          <div style={{ fontFamily: '"Libre Baskerville", serif', fontSize: 22, color: 'var(--ink)', marginBottom: 2 }}>Anna Wallace</div>
          <div style={{ fontSize: 12, color: 'var(--ink-muted)', letterSpacing: '0.02em', lineHeight: 1.4 }}>
            BSc Food &amp; Nutrition<br />Registered Associate Nutritionist
          </div>
        </div>
        <div className="hero-quote" style={{
          position: 'absolute', top: -26, left: 8,
          background: 'var(--cream-deep)', padding: '14px 18px', borderRadius: 10,
          maxWidth: 220, border: '1px solid var(--hairline)', transform: 'rotate(-2deg)'
        }}>
          <div style={{ fontFamily: '"Libre Baskerville", serif', fontStyle: 'italic', fontSize: 14, color: 'var(--ink)', lineHeight: 1.4 }}>
            "My menopause symptoms improved and I lost 12 lbs."
          </div>
          <div style={{ fontSize: 11, color: 'var(--ink-muted)', marginTop: 6, letterSpacing: '0.06em' }}>RUTH, 54</div>
        </div>
      </div>
    </section>

    </>);

}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
