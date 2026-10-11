
const { useState, useEffect } = React;

const trackLead = () => {
  try { if (window.fbq) window.fbq('track', 'Lead', { content_name: '5 Day Reset Tester', content_category: 'optin' }); } catch (e) {}
  try { if (window.gtag) window.gtag('event', 'generate_lead', { freebie: 'five_day_reset_tester' }); } catch (e) {}
};
// Open the MailerLite sign-up popup (defined in a plain script in the body).
const openSignup = (e) => {
  if (e) e.preventDefault();
  try { trackLead(); } catch (_) {}
  try { if (window.openTesterModal) window.openTesterModal(); } catch (_) {}
};

const Check = () => (<svg viewBox="0 0 24 24"><polyline points="4 12.5 10 18 20 6.5" /></svg>);
const Arrow = ({ className = 'arrow' }) => (
  <svg className={className} width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
    <line x1="5" y1="12" x2="19" y2="12" /><polyline points="13 6 19 12 13 18" />
  </svg>
);
const Bolt = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
  </svg>
);
const CardIcon = () => (<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="2" y="6" width="20" height="14" rx="2"/><line x1="2" y1="10.5" x2="22" y2="10.5"/><line x1="6" y1="16" x2="10" y2="16"/></svg>);
const Gift = () => (<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M5 12v7a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7"/><path d="M12 8S10.5 3 8 3a2 2 0 0 0 0 4"/><path d="M12 8s1.5-5 4-5a2 2 0 0 1 0 4"/></svg>);
const IcBook = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M4 4v13a3 3 0 0 0 3 3"/></svg>);
const IcLive = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3" fill="currentColor"/></svg>);
const IcChef = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M6 12a4 4 0 1 1 2-7.5A4 4 0 0 1 16 4.5 4 4 0 1 1 18 12v6H6z"/><path d="M6 18h12"/></svg>);
const IcWhatsApp = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.14 8.44 9.94v-7.03H7.9v-2.91h2.54V9.84c0-2.52 1.49-3.91 3.78-3.91 1.09 0 2.24.2 2.24.2v2.47h-1.26c-1.24 0-1.63.77-1.63 1.57v1.88h2.78l-.44 2.91h-2.34V22c4.78-.8 8.43-4.94 8.43-9.94Z"/></svg>);
const IcCheckBox = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="4" y="4" width="16" height="16" rx="3"/><polyline points="8 12.5 11 15.5 16 9.5"/></svg>);
const IcPhone = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="6" y="2.5" width="12" height="19" rx="2.5"/><line x1="11" y1="18.5" x2="13" y2="18.5"/><path d="M9.5 6.2c.6.5 1.5.8 2.5.8s1.9-.3 2.5-.8"/></svg>);
const IcChart = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><line x1="4" y1="20" x2="4" y2="12"/><line x1="10" y1="20" x2="10" y2="5"/><line x1="16" y1="20" x2="16" y2="9"/><line x1="20" y1="20" x2="20" y2="14"/></svg>);
const IcCalendar = () => (<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/></svg>);

function PrimaryCTA({ label = 'Test New Reset', className = 'cta-btn', showFoot = true }) {
  return (
    <>
      <a href="#register" className={className} onClick={openSignup}>
        {label} <Arrow />
      </a>
      {showFoot && (
        <div className="micro-foot">
          <span className="item"><Bolt /> Kicks off Mon 12th Oct</span>
          <span className="item"><Check /> Limited tester spots</span>
        </div>
      )}
    </>
  );
}

function UrgencyBanner() {
  // Free tester registration closes at kick-off: 9am London, Mon 12 Oct 2026.
  const REG_CLOSE = React.useMemo(() => new Date('2026-10-12T09:00:00+01:00').getTime(), []);
  const [left, setLeft] = useState(() => Math.max(0, REG_CLOSE - Date.now()));
  useEffect(() => {
    const id = setInterval(() => setLeft(Math.max(0, REG_CLOSE - Date.now())), 1000);
    return () => clearInterval(id);
  }, [REG_CLOSE]);
  const pad = (n) => String(n).padStart(2, '0');
  const units = [
    [Math.floor(left / 86400000), 'days'],
    [pad(Math.floor((left % 86400000) / 3600000)), 'hrs'],
    [pad(Math.floor((left % 3600000) / 60000)), 'mins'],
    [pad(Math.floor((left % 60000) / 1000)), 'secs'],
  ];
  return (
    <div className="urgency-banner" role="alert">
      <div className="urgency-inner">
        <span className="urg-label">Free Tester Registration Closes In</span>
        <span className="urg-timer">
          {units.map(([v, l], i) => (
            <span className="cd" key={i}><b>{v}</b><i>{l}</i></span>
          ))}
        </span>
      </div>
    </div>
  );
}

function Hero() {
  const bullets = [
    <>The <strong>5 Day Reset Protocol</strong>, laid out in the WLA app</>,
    <><strong>Mouth-watering recipes</strong> to fuel your fat loss</>,
    <><strong>Live coaching</strong> + daily support</>,
    <><strong>Daily check-ins</strong> to keep you on track</>,
  ];
  return (
    <section className="hero-section" id="top" style={{
      maxWidth: 1240, margin: '0 auto', padding: '40px 32px 80px',
      display: 'grid', gridTemplateColumns: '1.1fr 0.9fr', gap: 72, alignItems: 'center'
    }}>
      <div className="hero-left" style={{ display: 'flex', flexDirection: 'column' }}>
        <div className="hero-badge" style={{
          display: 'inline-flex', alignItems: 'center', gap: 10, alignSelf: 'flex-start',
          background: '#F5D9CE', border: '1px solid var(--coral)', borderRadius: 999,
          padding: '10px 22px', marginBottom: 20,
        }}>
          <span style={{ fontSize: 20, lineHeight: 1 }}>✨</span>
          <span style={{ fontFamily: "'Libre Baskerville', serif", fontWeight: 700, fontSize: 15, letterSpacing: '0.01em', color: 'var(--navy)', lineHeight: 1.3 }}>
            Looking for limited testers ·<br className="badge-mobile-br" /> Brand new reset
          </span>
        </div>

        <h1 className="hero-title serif" style={{
          margin: '0 0 14px', color: 'var(--navy)', fontWeight: 700,
          fontSize: 'clamp(30px, 4.2vw, 44px)', lineHeight: 1.1, letterSpacing: '-0.01em'
        }}>
          5 Day Fat Loss Reset
        </h1>

        <div className="hero-sub" style={{
          fontFamily: '"Libre Baskerville", serif', fontWeight: 400, fontStyle: 'italic',
          fontSize: 'clamp(22px, 2.6vw, 30px)', lineHeight: 1.25, letterSpacing: '-0.005em',
          color: 'var(--coral)', maxWidth: 560, marginBottom: 12, textWrap: 'balance',
        }}>
          Lose up to <strong style={{ color: 'var(--navy)', fontWeight: 400 }}>5 pounds</strong>, gain <strong style={{ color: 'var(--navy)', fontWeight: 400 }}>energy</strong> and <strong style={{ color: 'var(--navy)', fontWeight: 400 }}>confidence</strong>, and say goodbye to sugar cravings in 5 days.
        </div>

        <div className="hero-kickoff" style={{
          fontFamily: "'Libre Baskerville', serif", fontStyle: 'normal',
          fontSize: 18, lineHeight: 1.4, color: 'var(--navy)', marginBottom: 26,
        }}>
          Kicks off Monday 12th October
        </div>

        <div className="programme-results" style={{
          display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 560, marginBottom: 30,
          background: 'var(--paper)', border: '1px solid var(--rule)', borderLeft: '4px solid var(--coral)',
          borderRadius: 14, padding: '22px 26px',
        }}>
          {bullets.map((r, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
              <span style={{ flexShrink: 0, marginTop: 3 }}>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--coral)" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><polyline points="4 12.5 10 18 20 6.5" /></svg>
              </span>
              <div style={{ fontFamily: "'Alegreya Sans', sans-serif", fontSize: 18, lineHeight: 1.35, color: 'var(--navy)' }}>{r}</div>
            </div>
          ))}
        </div>

        <div className="hero-cta-block" style={{ marginBottom: 44 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 360 }}>
            <PrimaryCTA label="Test New Reset" showFoot={false} />
            <div style={{ fontSize: 13, color: 'var(--muted)', lineHeight: 1.5 }}>Limited tester spots. All we ask is your honest feedback at the end.</div>
          </div>
        </div>

        <div className="hero-stats" style={{ display: 'flex', gap: 48, paddingTop: 28, borderTop: '1px solid var(--rule)' }}>
          <div><div style={{ fontFamily: "'Libre Baskerville', serif", fontSize: 32, lineHeight: 1, color: 'var(--navy)' }}>50,000+</div><div style={{ fontSize: 12, color: 'var(--muted)', letterSpacing: '0.04em', marginTop: 8 }}>WOMEN SUPPORTED</div></div>
          <div><div style={{ fontFamily: "'Libre Baskerville', serif", fontSize: 32, lineHeight: 1, color: 'var(--navy)' }}>10 yrs</div><div style={{ fontSize: 12, color: 'var(--muted)', letterSpacing: '0.04em', marginTop: 8 }}>CLINICAL PRACTICE</div></div>
          <div><div style={{ fontFamily: "'Libre Baskerville', serif", fontSize: 32, lineHeight: 1, color: 'var(--navy)' }}>4.9 ★</div><div style={{ fontSize: 12, color: 'var(--muted)', letterSpacing: '0.04em', marginTop: 8 }}>MEMBER RATING</div></div>
        </div>
      </div>

      <div className="hero-media" style={{ position: 'relative' }}>
        <div className="hero-photo" style={{ aspectRatio: '4/5', borderRadius: 4, overflow: 'hidden', background: 'var(--cream)' }}>
          <img src="/assets/anna-hero.jpg" alt="Anna Wallace, founder of The Weight Loss Academy" className="hero-img" fetchpriority="high" decoding="async" style={{ width: '100%', height: '100%', objectFit: 'cover', display: 'block' }} />
        </div>

        {/* The WLA app itself, playing, over the left edge of the photo. */}
        <div className="hero-phone" style={{
          position: 'absolute', left: -46, bottom: 54, width: 184, aspectRatio: '1004 / 2000',
          borderRadius: 24, border: '7px solid var(--navy)', overflow: 'hidden', background: 'var(--cream)',
          boxShadow: '0 30px 56px -22px rgba(14, 39, 70, 0.55)',
        }}>
          <video poster="/assets/app-clip-home-poster.jpg" autoPlay muted loop playsInline preload="metadata" aria-label="The WLA app home screen"
            style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'top center', display: 'block' }}>
            <source src="/assets/app-clip-home.webm" type="video/webm" />
            <source src="/assets/app-clip-home.mp4" type="video/mp4" />
          </video>
        </div>

        <div className="hero-cred" style={{
          position: 'absolute', bottom: -28, right: -20, background: 'var(--paper)', padding: '18px 22px',
          borderRadius: 12, boxShadow: '0 20px 40px -18px rgba(80, 40, 20, 0.25)', border: '1px solid var(--rule)', maxWidth: 260,
        }}>
          <div style={{ fontFamily: "'Libre Baskerville', serif", fontStyle: 'italic', fontSize: 13, color: 'var(--coral)', marginBottom: 6 }}>Led by</div>
          <div style={{ fontFamily: "'Libre Baskerville', serif", fontSize: 22, color: 'var(--navy)', marginBottom: 2 }}>Anna Wallace</div>
          <div style={{ fontSize: 12, color: 'var(--muted)', letterSpacing: '0.02em', lineHeight: 1.4 }}>
            BSc Food &amp; Nutrition<br />Registered Associate Nutritionist
          </div>
        </div>

        <div className="hero-quote" style={{
          position: 'absolute', top: -26, left: 8, background: 'var(--cream-2)', padding: '14px 18px',
          borderRadius: 10, maxWidth: 220, border: '1px solid var(--rule)', transform: 'rotate(-2deg)',
        }}>
          <div style={{ fontFamily: "'Libre Baskerville', serif", fontStyle: 'italic', fontSize: 14, color: 'var(--navy)', lineHeight: 1.4 }}>
            "5lbs down this week — and I can satisfy my sweet cravings without the sugar."
          </div>
          <div style={{ fontSize: 11, color: 'var(--muted)', marginTop: 6, letterSpacing: '0.06em' }}>HOLLY</div>
        </div>
      </div>
    </section>
  );
}

function Trust() {
  return (
    <div className="trust">
      <div className="trust-inner">
        <div className="trust-item"><div className="num">50,000+</div><div className="lab">WOMEN SUPPORTED</div></div>
        <div className="trust-item"><div className="num">10 yrs</div><div className="lab">CLINICAL PRACTICE</div></div>
        <div className="trust-item"><div className="num">4.9 ★</div><div className="lab">MEMBER RATING</div></div>
      </div>
    </div>
  );
}

function Problem() {
  return (
    <section className="problem">
      <div className="problem-inner">
        <h2 className="serif">If you're a woman over 45, you've probably noticed<br /><em>everything's changed.</em></h2>
        <p className="lead-in">The weight that used to come off with a bit of effort now won't budge.<span className="break"> </span>The plans that used to work feel like a punishment.</p>
        <ul className="signal-list">
          <li>You're eating less than ever, and the scale isn't moving.</li>
          <li>The 4pm sugar pull has become non-negotiable.</li>
          <li>Energy crashes mid-afternoon and again after dinner.</li>
          <li>You don't quite recognise your own body anymore.</li>
          <li>You've started so many "Mondays" you've lost count.</li>
        </ul>
        <div className="verdict">
          <p>None of this is laziness. None of it is willpower. It's hormones, blood sugar, and a body that needs a different approach to the one that worked in your thirties.</p>
          <p>That's exactly what these 5 days are for.</p>
        </div>
      </div>
    </section>
  );
}

function Outcomes() {
  const items = [
    { stat: '2–5 lbs',     t: 'Scales shift by day 5',           d: 'Many women notice the scales drop by day 5, largely from reduced bloating and water retention that builds up from processed foods, sugar and inconsistent eating habits.' },
    { stat: '1–3 days',    t: 'Sugar cravings handled',          d: 'Within the first 1–3 days, the afternoon snacking pull starts to fade and the snack cycle breaks.' },
    { stat: 'All day',     t: 'Steady, balanced energy',         d: 'No more afternoon crashes or evening energy dips. Feel fuller, clearer, and more in control throughout the day.' },
    { stat: 'Real food',   t: 'No banned lists',                 d: 'Proper meals built around protein, vegetables and the right carbs at the right time.' },
    { stat: 'Real life',   t: 'Food you\'ll actually enjoy',     d: 'Flexible meals that work around work, kids, social plans and busy days, without feeling like you\'re "on a diet".' },
    { stat: '5 days +',    t: 'A reset you can keep going',      d: 'Habits that compound for the weeks after. Not a one-off you start over from on Monday.' },
  ];
  return (
    <section className="outcomes" id="outcomes">
      <div className="section-head">
        <span className="eyebrow">What you'll walk away with</span>
        <h2 className="serif">Your <em>5-day wins.</em></h2>
        <p>What most women experience by the end of the week. Yours might vary but this is what real previous resetters have reported.</p>
      </div>
      <div className="outcomes-grid">
        {items.map((it, i) => (
          <div className="outcome" key={i}>
            <div className="stat">{it.stat}</div>
            <h3>{it.t}</h3>
            <p>{it.d}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function Results() {
  const tiles = [
    { name: 'Vicky, 56',  img: '/assets/vicky-before-after.png' },
    { name: 'Laura, 52',  img: '/assets/jill-before-after.jpg' },
    { name: 'Ruth, 54',   img: '/assets/ruth-before-after.jpg' },
    { name: 'Barbara, 58', img: '/assets/barbara-before-after.png' },
    { name: 'Member, 5',  img: '/assets/member-05-before-after.png' },
    { name: 'Member, 6',  img: '/assets/member-06-before-after.png' },
    { name: 'Member, 7',  img: '/assets/member-07-before-after.png' },
    { name: 'Member, 8',  img: '/assets/member-08-before-after.jpeg' },
    { name: 'Member, 9',  img: '/assets/member-09-before-after.png' },
    { name: 'Member, 10', img: '/assets/member-10-before-after.png' },
    { name: 'Member, 11', img: '/assets/member-11-before-after.png' },
    { name: 'Member, 12', img: '/assets/member-12-before-after.png' },
  ];

  const trackRef = React.useRef(null);
  const [page, setPage] = React.useState(0);
  const [pageCount, setPageCount] = React.useState(1);

  const recompute = React.useCallback(() => {
    const track = trackRef.current;
    if (!track) return;
    const tile = track.querySelector('.results-tile');
    if (!tile) return;
    const tileWidth = tile.offsetWidth + 16;
    const visible = Math.max(1, Math.round(track.clientWidth / tileWidth));
    const columns = Math.ceil(tiles.length / 2);
    const count = Math.max(1, columns - visible + 1);
    setPageCount(count);
    setPage(Math.min(Math.round(track.scrollLeft / tileWidth), count - 1));
  }, [tiles.length]);

  React.useEffect(() => {
    recompute();
    const track = trackRef.current;
    if (!track) return;
    let frame;
    const onScroll = () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const tile = track.querySelector('.results-tile');
        if (!tile) return;
        const tileWidth = tile.offsetWidth + 16;
        setPage(Math.round(track.scrollLeft / tileWidth));
      });
    };
    track.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', recompute);
    return () => {
      track.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', recompute);
      cancelAnimationFrame(frame);
    };
  }, [recompute]);

  const goTo = (idx) => {
    const track = trackRef.current;
    if (!track) return;
    const tile = track.querySelector('.results-tile');
    if (!tile) return;
    track.scrollTo({ left: idx * (tile.offsetWidth + 16), behavior: 'smooth' });
  };
  const scrollBy = (dir) => goTo(Math.min(Math.max(page + dir, 0), pageCount - 1));

  return (
    <section className="results" id="why-wla">
      <div className="section-head">
        <span className="eyebrow">Real results from real WLA women</span>
        <h2 className="serif">See why so many women <em>live by the WLA.</em></h2>
      </div>
      <div className="results-carousel">
        <button className="results-nav prev" onClick={() => scrollBy(-1)} disabled={page === 0} aria-label="Previous results">‹</button>
        <div className="results-track" ref={trackRef}>
          {tiles.map((t, i) => (
            <div className="results-tile" key={i}>
              <img src={t.img} alt={`Before and after of ${t.name}`} loading="lazy" decoding="async" />
            </div>
          ))}
        </div>
        <button className="results-nav next" onClick={() => scrollBy(1)} disabled={page >= pageCount - 1} aria-label="Next results">›</button>
        <div className="results-dots" role="tablist">
          {Array.from({ length: pageCount }).map((_, i) => (
            <button key={i} className={'results-dot' + (i === page ? ' active' : '')} onClick={() => goTo(i)} aria-label={'Go to page ' + (i + 1)} />
          ))}
        </div>
      </div>
      <p className="results-disclaimer">*Results vary depending on the individual. There is no guarantee of specific results.</p>
    </section>
  );
}

function Inside() {
  const items = [
    { ic: <IcBook />,     t: '5 Day Reset Protocol Guide',        d: 'Your exact eating rhythm, macro balance and meal structure for the 5 days, laid out in the app. Designed to cut sugar cravings within 72 hours and put real fat loss on the scale by the end of the week.' },
    { ic: <IcPhone />,    t: 'Access In The WLA App',             d: 'Everything in one place, right on your phone. Open the app and your reset, recipes, coaching and check-ins are ready and waiting, whenever you are.' },
    { ic: <IcChef />,     t: 'Mouth-Watering Fat Loss Recipes',   d: "Make every meal work towards your goals and taste amazing. Our recipes bring the WLA Formula to life, with satisfying portions and flavour-packed combinations that make the Reset easy to follow. Enjoy your food, stay consistent and get the most from your five days." },
    { ic: <IcChart />,    t: 'The WLA Daily Tracker',             d: "Track your meals using the WLA Formula alongside sleep, stress and movement. Spot what's helping your progress and where small adjustments could improve your results so you know exactly what to focus on next." },
    { ic: <IcCalendar />, t: 'Your Personalised Meal Planner',    d: "Adjust your reset meals around your week, so a busy day doesn't have to turn into a last-minute takeaway or another 'I'll start tomorrow'." },
    { ic: <IcLive />,     t: 'Live Coaching',                     d: 'Show up for live sessions with me, plus the ongoing coaching inside the community. Q&A, mindset, the day\'s focus, and how to handle the inevitable wobble.' },
    { ic: <IcWhatsApp />, t: 'Private Coaching Community',        d: 'Real-time support, the other women testing alongside you, and a place to ask the questions you\'ve been Googling at 11pm.' },
    { ic: <IcCheckBox />, t: 'Daily Check-Ins',                   d: 'Daily accountability to keep you focused, consistent, and following through. Five days of support, momentum, and staying on track with your goals.' },
  ];
  return (
    <section className="inside" id="whats-inside">
      <div className="section-head">
        <span className="eyebrow">What you get as a tester</span>
        <h2 className="serif">Everything you need to get started, <em>all FREE.</em></h2>
        <p>Real coaching, a proven food plan and the structure to break the sugar cycle, shift the scale and feel like yourself again, all inside the WLA app.</p>
      </div>
      <div className="inside-grid">
        {items.map((it, i) => (
          <div className="feat" key={i}>
            {it.bonus && <span className="bonus-pill">Bonus</span>}
            <div className="ic">{it.ic}</div>
            <h3>{it.t}</h3>
            <p>{it.d}</p>
          </div>
        ))}
      </div>
      <div className="inside-cta">
        <PrimaryCTA />
      </div>
    </section>
  );
}

const APP_CLIPS = [
  { tab: 'Meal planner', stem: '/assets/app-clip-planner', cap: 'Your week, planned in one tap' },
  { tab: 'Daily tracker', stem: '/assets/app-clip-tracker', cap: 'Check in, in seconds' },
];

function AppClips() {
  React.useEffect(() => {
    if (typeof IntersectionObserver === 'undefined') return;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const v = e.target;
        if (e.isIntersecting) { const r = v.play(); if (r && r.catch) r.catch(() => {}); }
        else v.pause();
      });
    }, { threshold: 0.3 });
    document.querySelectorAll('.app-clip-phone video').forEach((v) => io.observe(v));
    return () => io.disconnect();
  }, []);
  return (
    <section className="app-clips" style={{ padding: '72px 28px 80px', background: 'var(--cream)' }}>
      <div className="section-head">
        <span className="eyebrow">See it in action</span>
        <h2 className="serif">Two taps, <em>and your week is sorted.</em></h2>
      </div>
      <div className="app-clip-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 48, maxWidth: 680, margin: '0 auto' }}>
        {APP_CLIPS.map((c) => (
          <div key={c.stem} style={{ textAlign: 'center' }}>
            <h3 className="serif" style={{ fontSize: 21, color: 'var(--navy)', fontWeight: 700, margin: '0 0 4px' }}>{c.tab}</h3>
            <p style={{ fontSize: 15, color: 'var(--muted)', lineHeight: 1.4, margin: '0 0 16px' }}>{c.cap}</p>
            <div className="app-clip-phone" style={{ aspectRatio: '1004 / 2000', borderRadius: 30, border: '8px solid var(--navy)', overflow: 'hidden', background: 'var(--cream)', boxShadow: '0 30px 60px -26px rgba(14, 39, 70, 0.5)' }}>
              <video poster={c.stem + '-poster.jpg'} muted loop playsInline preload="none" aria-label={c.tab + ' — ' + c.cap} style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'top center', display: 'block' }}>
                <source src={c.stem + '.webm'} type="video/webm" />
                <source src={c.stem + '.mp4'} type="video/mp4" />
              </video>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function Why() {
  const pillars = [
    { t: 'Built for women over 45',     d: 'Designed around midlife hormones, slower recovery and stubborn middle weight, not a 25-year-old metabolism.' },
    { t: 'No 1,200-calorie plans',       d: 'You\'ll eat enough to function, sleep and think. Restriction creates rebounds. We\'re doing the opposite.' },
    { t: 'Real food, no cutting carbs',  d: 'A blood-sugar-friendly plate built around proper meals, not shakes, replacements or "diet versions" of anything.' },
    { t: 'Coached, not handed a PDF',    d: 'You get live sessions, a Facebook group and a daily check-in, all in the app. Five days, properly supported.' },
  ];
  return (
    <section className="why">
      <div className="why-inner">
        <div className="section-head">
          <span className="eyebrow">Why this reset is different</span>
          <h2 className="serif">A 5-day reset that <em>doesn't feel like a diet.</em></h2>
        </div>
        <div className="pillar-grid">
          {pillars.map((p, i) => (
            <div className="pillar" key={i}>
              <h3>{p.t}</h3>
              <p>{p.d}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Schedule() {
  const days = [
    { weekday: 'Mon', date: '12th Oct', label: 'Day 1', prep: true, what: 'Reset begins. Kickoff coaching, the plan explained in plain English, and your first steps for the week.' },
    { weekday: 'Tue', date: '13th Oct', label: 'Day 2', what: 'Blood sugar starts to stabilise and the constant sugar cravings begin to quieten down. That intense 4pm pull for snacks starts losing its grip.' },
    { weekday: 'Wed', date: '14th Oct', label: 'Day 3', what: 'Energy feels steadier and more consistent throughout the day. Less crashing, less sluggishness, and more feeling like yourself again.' },
    { weekday: 'Thu', date: '15th Oct', label: 'Day 4', what: 'Bloating starts to settle and you begin feeling lighter, more comfortable, and less puffy in your clothes.' },
    { weekday: 'Fri', date: '16th Oct', label: 'Wrap', what: 'The scales are moving, clothes are fitting better, and you finish the week feeling lighter, more in control, and proud of yourself again.' },
  ];
  return (
    <section className="schedule" id="schedule">
      <div className="section-head">
        <span className="eyebrow">Your 5-day schedule</span>
        <h2 className="serif">Mon 12th → Fri 16th October.</h2>
        <p>Live sessions and check-ins run in the group and the app. Show up live or catch up whenever suits you.</p>
      </div>
      <div className="schedule-grid">
        {days.map((d, i) => (
          <div className={'day-card' + (d.prep ? ' prep' : '')} key={i}>
            <div className="weekday">{d.weekday}</div>
            <div className="date">{d.date}</div>
            <div className="label">{d.label}</div>
            <div className="what">{d.what}</div>
          </div>
        ))}
      </div>
    </section>
  );
}

function Founder() {
  return (
    <section className="founder" id="founder">
      <div className="founder-inner">
        <div className="portrait">
          <img src="/assets/anna-portrait.jpg" alt="Anna Wallace" />
          <div className="signature-tag"><span className="name">Anna Wallace</span>BSc Food &amp; Nutrition<br />Registered Associate Nutritionist</div>
        </div>
        <div>
          <h2 className="serif"><span className="founder-intro">Hi, I'm Anna</span>This is the reset I built from <em>10 years coaching women over 45.</em></h2>
          <div className="body">
            <p>I'm a Registered Associate Nutritionist (BSc Food &amp; Nutrition) and the founder of The Weight Loss Academy. Over the last 10 years my team and I have supported over <strong>50,000 women</strong>, the majority of them in midlife, to lose weight without 1,200-calorie plans, banned food lists or starting over every Monday.</p>
            <p>This 5 Day Reset is brand new, and before we open it up more widely I'm looking for a small group of testers to run through it with me. It's the exact rhythm I use with paying clients to break the sugar cycle in 72 hours, settle blood sugar, and put a structure in place that actually fits a midlife week.</p>
            <p>As a tester you get the full thing free, delivered inside the WLA app with live coaching and a community behind you the whole way, in exchange for your honest feedback at the end.</p>
          </div>
          <div className="signature">— Anna</div>
        </div>
      </div>
    </section>
  );
}

function Testimonials() {
  const items = [
    { i: 'B', n: 'Betty Wright',     loss: 'Lost 7 lbs · ½" hips, ½" waist, 1" bust',
      q: 'I jumped on the scales this morning — I\'ve lost 7lbs. I am sooo thrilled. I\'ve lost ½ inch from my hips, ½ inch from my waist and 1 inch from my boobs! I\'ve got into winter clothes that were very snug last year and up a notch on my jeans belt. On top of that I am getting more sleep and good quality sleep — who knew I could be a morning person! I\'ve got more energy and I feel like I have a new lease of life. Absolutely amazing.' },
    { i: 'S', n: 'Sharon Nesbitt',   loss: 'Lost 7 lbs',
      q: 'I can\'t believe it — I have lost 7lb. I am so amazed considering how my first day went.' },
    { i: 'H', n: 'Holly Heather',    loss: 'Lost 5 lbs · Sweet cravings handled',
      q: 'I\'ve always been the chubby one. My sisters used to make me be Pumbaa if we played Lion King together. WLA has given me the motivation to lose weight for good without being on a "diet" for the rest of my life. I am learning more about food and my children are learning from me and making healthy choices. 5lbs down this week — and I learnt I can satisfy my sweet cravings with something healthy and not full of sugar.' },
    { i: 'D', n: 'Denise Hamilton',  loss: 'Lost 4 lbs · Beat the wine-o\'clock demons',
      q: '4lbs off in total. I\'ve waited and dreamed of this start for months after failing in the usual slimming groups. Last night I had to fight the demons — it was cold, the fire was lit, and that\'s when I normally have a glass of wine. But I made a hot water with lemon and woke up feeling quite smug about my choices.' },
    { i: 'M', n: 'Mary Moane',       loss: 'Lost 2.5 lbs · 4.5 inches off',
      q: 'I\'m 2.5lbs less, but from my waist I have lost 2 inches, from my hips 1 inch and my thighs 1.5 inches. I call that a massive win for one week. You have really smashed it with this reset.' },
    { i: 'J', n: 'Jo Allen',         loss: 'Lost 2 lbs · No Diet Coke, less cravings',
      q: 'I\'ve lost 2lb which I\'m soooooo happy with. Normally I struggle to lose half a pound a week when I try really hard. My big win — I\'ve had no Diet Coke. Normally I have at least one a day. Less cravings, much more control, and I\'m feeling so much better in myself.' },
    { i: 'L', n: 'Lorraine Carroll', loss: 'Dress taken in 4 inches',
      q: 'I\'m so happy I could cry. I\'m off to a masquerade ball next weekend and I needed to get my new dress taken up a few inches — but I\'ve also had to get my dress taken in 4 inches! I haven\'t a clue what I weigh because I\'m not going to be defined by numbers on a scale — but I FEEL AMAZING right now.' },
    { i: 'J', n: 'Joanna Harvey',    loss: 'Walked straight past the sweets',
      q: 'For the very, and I mean very first time in my whole life I walked past the sweets, cakes and bread sections in the supermarket. That\'s the best achievement for me as I always had to buy those just "in case". I have tried everything on this planet before and nothing worked — this works.' },
    { i: 'F', n: 'Fiona Embleton',   loss: 'Healthier family habits, no shame',
      q: 'I\'m inspired about taking accountability but without the shame of not managing to follow strict diets. The WLA plan doesn\'t just work for me, it works for my family too — and I love sharing a healthier way of life with my wee boys.' },
    { i: 'K', n: 'Kathy Roberts',    loss: 'Better sleep · Confidence boost',
      q: 'It has done me the power of good. Sleep patterns improved, my colleagues have mentioned I seem more relaxed. I wore a skirt and top to a function yesterday that hadn\'t fitted in months — felt and looked good. Massive confidence boost. I will be watching from the sidelines — the best thing I did was joining the WLA Academy 4 years ago!' },
  ];

  const trackRef = React.useRef(null);
  const [page, setPage] = React.useState(0);
  const [pageCount, setPageCount] = React.useState(1);

  const recompute = React.useCallback(() => {
    const track = trackRef.current;
    if (!track) return;
    const card = track.querySelector('.t-card');
    if (!card) return;
    const cardWidth = card.offsetWidth + 24;
    const visible = Math.max(1, Math.round(track.clientWidth / cardWidth));
    const count = Math.max(1, items.length - visible + 1);
    setPageCount(count);
    setPage(Math.min(Math.round(track.scrollLeft / cardWidth), count - 1));
  }, [items.length]);

  React.useEffect(() => {
    recompute();
    const track = trackRef.current;
    if (!track) return;
    let frame;
    const onScroll = () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const card = track.querySelector('.t-card');
        if (!card) return;
        const cardWidth = card.offsetWidth + 24;
        setPage(Math.round(track.scrollLeft / cardWidth));
      });
    };
    track.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', recompute);
    return () => {
      track.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', recompute);
      cancelAnimationFrame(frame);
    };
  }, [recompute]);

  const goTo = (idx) => {
    const track = trackRef.current;
    if (!track) return;
    const card = track.querySelector('.t-card');
    if (!card) return;
    track.scrollTo({ left: idx * (card.offsetWidth + 24), behavior: 'smooth' });
  };
  const scrollBy = (dir) => goTo(Math.min(Math.max(page + dir, 0), pageCount - 1));

  return (
    <section className="testimonials" id="results">
      <div className="section-head">
        <h2 className="serif">Real women, <em>real results.</em></h2>
        <p>Straight from past rounds of the reset.</p>
      </div>
      <div className="t-carousel">
        <button className="t-nav prev" onClick={() => scrollBy(-1)} disabled={page === 0} aria-label="Previous testimonials">‹</button>
        <div className="t-track" ref={trackRef}>
          {items.map((it, i) => (
            <div className="t-card" key={i}>
              <div className="t-head">
                <div className="t-stars">★★★★★</div>
                <div className="t-result">{it.loss}</div>
              </div>
              <p className="t-quote">"{it.q}"</p>
              <div className="t-meta">
                <div className="t-avatar">{it.i}</div>
                <div className="t-name">{it.n}</div>
              </div>
            </div>
          ))}
        </div>
        <button className="t-nav next" onClick={() => scrollBy(1)} disabled={page >= pageCount - 1} aria-label="Next testimonials">›</button>
        <div className="t-dots" role="tablist">
          {Array.from({ length: pageCount }).map((_, i) => (
            <button key={i} className={'t-dot' + (i === page ? ' active' : '')} onClick={() => goTo(i)} aria-label={'Go to page ' + (i + 1)} />
          ))}
        </div>
      </div>
    </section>
  );
}

function FAQ() {
  const qs = [
    { q: 'When does it start, and how much time do I need?', a: 'It kicks off Monday 12th October and runs five days (Mon 12th–Fri 16th). Each day is light: a short daily focus, a check-in, and live sessions you can watch live or catch up on later.' },
    { q: 'What does being a tester involve?',                 a: 'You run through the full 5 day reset with us and share your honest feedback at the end, what worked, what didn\'t, what you\'d change. That\'s it. Your feedback helps us make it even better before a wider launch.' },
    { q: 'Is it free? What\'s the catch?',                    a: 'Yes, it\'s free for testers. There\'s no catch and no obligation to buy anything. All we ask is your honest feedback at the end.' },
    { q: 'How do I get access after I sign up?',              a: 'You sign up on this page and before we kick off on the 12th we\'ll email your access to the WLA app plus the link to the private Facebook group. Everything, the plan, recipes, coaching and check-ins, lives in one place on your phone.' },
    { q: 'I\'m on HRT / perimenopausal / post-menopause. Is this suitable?', a: 'Yes. The whole reset is designed around midlife hormones and the way your body responds in your 40s, 50s and beyond. Speak to your GP if you have a specific medical condition, but the food plan is real food in proper portions, nothing extreme.' },
    { q: 'I\'m under 45. Can I still join?',                  a: 'Absolutely. The structure works for any woman, but it\'s been specifically designed around the needs of women 45+. If that\'s you, you\'ll feel the difference.' },
    { q: 'How much weight can I lose?',                       a: 'Many women notice a scale drop, reduced bloating and better energy within the first 5 days. The biggest win though is usually feeling back in control and building momentum again. Results vary from person to person.' },
    { q: 'I\'m busy / I have to feed a family. Will this work?', a: 'Yes, the recipes are family-friendly and there are plenty of no-cook options too. The Facebook group is full of women navigating the same.' },
    { q: 'Do I need to count calories or cut out carbs?',     a: 'No to both. You\'ll eat real meals built around protein, vegetables, healthy fats and the right carbs at the right time. No calorie counting, no banned food lists.' },
    { q: 'Do I need the app?',                                a: 'The reset is delivered through the WLA app so everything lives in one place on your phone. When you sign up you\'ll get the link to download it (Apple and Android) along with your login.' },
    { q: 'Is there exercise involved?',                       a: 'No required exercise. Movement is encouraged, a daily walk is ideal, but this isn\'t a workout programme.' },
    { q: 'Do I need any equipment or supplements?',           a: 'Just food, water, your phone, and 5 days of commitment.' },
  ];
  return (
    <section className="faq" id="faq">
      <div className="faq-inner">
        <div className="section-head">
          <span className="eyebrow">Questions, answered</span>
          <h2 className="serif">Everything you need to know.</h2>
        </div>
        <div className="faq-list">
          {qs.map((it, i) => (
            <details className="faq-item" key={i}>
              <summary>{it.q}</summary>
              <p>{it.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}

function BottomCTA() {
  return (
    <section className="bottom-cta">
      <div className="bottom-cta-inner">
        <span className="doors-pill">Limited tester spots · Kicks off Mon 12th October</span>
        <h2 className="serif">Be one of our testers, <em>from Monday 12th October.</em></h2>
        <p>Free for testers, delivered in the app. Real coaching and a proper structure to break the sugar cycle and feel like yourself again in 5 days.</p>
        <PrimaryCTA />
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="foot">
      <div className="foot-inner">
        <div>© 2026 The Weight Loss Academy. All rights reserved.</div>
        <div style={{display: 'flex', gap: 24}}>
          <a href="https://www.wearewla.com/privacy-policy" target="_blank" rel="noopener">Privacy</a><a href="https://www.wearewla.com/terms-of-service" target="_blank" rel="noopener">Terms</a><a href="mailto:support@theweightloss-academy.com">Contact</a>
        </div>
      </div>
    </footer>
  );
}

function StickyCTA() {
  const [show, setShow] = useState(false);
  useEffect(() => {
    const onScroll = () => {
      setShow(window.scrollY > 900 && window.scrollY < document.body.scrollHeight - 1200);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener('scroll', onScroll);
  }, []);
  return (
    <div className={'sticky-cta' + (show ? ' show' : '')}>
      <div className="text">
        <strong>5 Day Reset · Testers Wanted</strong>
        <span className="sec">Kicks off Mon 12th October · limited spots</span>
      </div>
      <a href="#register" className="sticky-cta-card" onClick={openSignup}><Bolt /> Test New Reset</a>
    </div>
  );
}

function App() {
  return (<><UrgencyBanner /><Hero /><Results /><Outcomes /><Inside /><AppClips /><Testimonials /><Schedule /><Founder /><FAQ /><BottomCTA /><Footer /><StickyCTA /></>);
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
