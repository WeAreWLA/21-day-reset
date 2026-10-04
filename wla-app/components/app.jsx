// WLA App Founding Members — the sections unique to this page.
// Copy lifted from the Founding Members copy doc.

// ---------------------------------------------------------------------------
// App screenshot carousel — tabs on the left, a phone that changes on the
// right, auto-advancing until the visitor takes over.
// ---------------------------------------------------------------------------
const APP_SCREENS = [
  { tab: 'Daily tracker',  img: '/assets/app-home-tracker.jpg',  cap: 'Check in, in seconds' },
  { tab: 'Log a meal',     img: '/assets/app-log-meal.jpg',      cap: 'Log what you ate, straight from your meal plan' },
  { tab: 'Meal planner',   img: '/assets/app-meal-planner.jpg',  cap: 'Your week, planned in one tap' },
  { tab: 'Nutrition hub',  img: '/assets/app-nutrition-hub.jpg', cap: 'A fresh WLA meal guide every Friday' },
  { tab: 'Your progress',  img: '/assets/app-progress.jpg',      cap: 'See your results, even when the scales stand still' },
];

const AppGallerySection = () => {
  const [i, setI] = React.useState(0);
  const [paused, setPaused] = React.useState(false);
  const touch = React.useRef(null);
  const n = APP_SCREENS.length;

  React.useEffect(() => {
    if (paused) return;
    const id = setInterval(() => setI((p) => (p + 1) % n), 4500);
    return () => clearInterval(id);
  }, [paused, n]);

  const go = (next) => { setPaused(true); setI(((next % n) + n) % n); };

  const onTouchStart = (e) => { touch.current = e.touches[0].clientX; };
  const onTouchEnd = (e) => {
    if (touch.current === null) return;
    const dx = e.changedTouches[0].clientX - touch.current;
    if (Math.abs(dx) > 40) go(dx < 0 ? i + 1 : i - 1);
    touch.current = null;
  };

  return (
    <section className="app-gallery-section" style={{ padding: '72px 32px 64px', background: 'var(--cream-deep)' }}>
      <div style={{ maxWidth: 1060, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: 44 }}>
          <Eyebrow>Inside the app</Eyebrow>
          <SerifH size={46} style={{ marginTop: 18, lineHeight: 1.2 }}>
            Everything you need to lose weight<br />and keep it off, <Italic>in one simple app.</Italic>
          </SerifH>
        </div>

        <div className="app-carousel" style={{
          display: 'grid', gridTemplateColumns: '1fr 320px', gap: 56, alignItems: 'center',
        }}>
          {/* Tabs */}
          <div className="app-tabs" style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {APP_SCREENS.map((sc, idx) => {
              const on = idx === i;
              return (
                <button
                  key={sc.tab}
                  type="button"
                  onClick={() => go(idx)}
                  className={on ? 'app-tab is-on' : 'app-tab'}
                  style={{
                    textAlign: 'left',
                    border: on ? '1px solid var(--blush-deep)' : '1px solid var(--hairline)',
                    background: on ? 'var(--paper)' : 'rgba(253, 251, 248, 0.45)',
                    borderLeft: on ? '4px solid var(--blush-deep)' : '4px solid transparent',
                    borderRadius: 14,
                    padding: '16px 20px',
                    cursor: 'pointer',
                    font: 'inherit',
                    display: 'flex',
                    alignItems: 'baseline',
                    gap: 12,
                    transition: 'background .2s, border-color .2s',
                  }}
                >
                  <span style={{
                    fontFamily: '"Libre Baskerville", serif',
                    fontWeight: 700, fontSize: 18,
                    color: 'var(--ink)', flexShrink: 0,
                  }}>{sc.tab}</span>
                  <span style={{
                    fontFamily: '"Alegreya Sans", sans-serif',
                    fontSize: 15, lineHeight: 1.35,
                    color: on ? 'var(--blush-deep)' : 'var(--ink-muted)',
                  }}>{sc.cap}</span>
                </button>
              );
            })}
          </div>

          {/* Phone */}
          <div
            onMouseEnter={() => setPaused(true)}
            onTouchStart={onTouchStart}
            onTouchEnd={onTouchEnd}
            style={{ position: 'relative' }}
          >
            <div className="app-phone" style={{
              aspectRatio: '1004 / 2000',
              borderRadius: 34,
              border: '9px solid var(--ink)',
              overflow: 'hidden',
              background: 'var(--bg)',
              boxShadow: '0 34px 64px -28px rgba(0, 48, 96, 0.5)',
              position: 'relative',
            }}>
              {APP_SCREENS.map((sc, idx) => (
                <img
                  key={sc.img}
                  src={sc.img}
                  alt={sc.tab + ' \u2014 ' + sc.cap}
                  loading={idx === 0 ? 'eager' : 'lazy'}
                  decoding="async"
                  style={{
                    position: 'absolute', inset: 0,
                    width: '100%', height: '100%',
                    objectFit: 'cover', objectPosition: 'top center',
                    opacity: idx === i ? 1 : 0,
                    transition: 'opacity .45s ease',
                  }}
                />
              ))}
            </div>

            {/* Dots */}
            <div className="app-dots" style={{
              display: 'flex', justifyContent: 'center', gap: 8, marginTop: 18,
            }}>
              {APP_SCREENS.map((sc, idx) => (
                <button
                  key={sc.tab}
                  type="button"
                  aria-label={sc.tab}
                  onClick={() => go(idx)}
                  style={{
                    width: idx === i ? 26 : 9, height: 9, borderRadius: 999,
                    border: 'none', padding: 0, cursor: 'pointer',
                    background: idx === i ? 'var(--blush-deep)' : 'rgba(0, 48, 96, 0.22)',
                    transition: 'width .25s, background .25s',
                  }}
                />
              ))}
            </div>

            {/* Caption, mobile only — the tabs carry it on desktop */}
            <div className="app-phone-caption" style={{
              display: 'none',
              textAlign: 'center', marginTop: 12,
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic', fontSize: 17, color: 'var(--ink)',
            }}>{APP_SCREENS[i].cap}</div>
          </div>
        </div>
      </div>
    </section>
  );
};

// ---------------------------------------------------------------------------
// The brand new WLA app — intro and the three pillars
// ---------------------------------------------------------------------------
const PILLARS = [
  { k: 'Simple',    v: 'Clear portion guidance, satisfying food and easy meal planning. Less daily guesswork.' },
  { k: 'Personal',  v: 'Choose your meals, set your goals and track the progress that matters to you.' },
  { k: 'Supported', v: 'Daily support from me, my coaching team and women who understand, helping you keep going even when motivation dips.' },
];

const AppIntroSection = () => (
  <section className="app-intro-section" style={{ padding: '80px 32px 64px', background: 'var(--bg)' }}>
    <div style={{ maxWidth: 900, margin: '0 auto', textAlign: 'center' }}>
      <Eyebrow>A one-off opportunity</Eyebrow>
      <SerifH size={52} style={{ marginTop: 20, marginBottom: 24, lineHeight: 1.18 }}>
        The WLA Formula works.<br /><Italic>Now it&rsquo;s even easier to follow.</Italic>
      </SerifH>
      <Body size={18} style={{ maxWidth: 720, margin: '0 auto 18px' }}>
        Join the first Founding Member launch of the brand-new WLA app at our lowest launch price, and help
        shape its future through your feedback.
      </Body>
      <Body size={18} style={{ maxWidth: 720, margin: '0 auto 18px' }}>
        The WLA Formula, built into your everyday life without miserable diet food. Plan your meals, create
        your shopping list and track your habits to see where small changes could help. With recipes, coaching
        and community together in one place, it&rsquo;s easier to feel organised and stay consistent.
      </Body>
      <div style={{
        fontFamily: '"Libre Baskerville", serif', fontSize: 21, lineHeight: 1.5,
        color: 'var(--ink)', maxWidth: 760, margin: '26px auto 44px',
      }}>
        Think of it as your daily accountability, meal planner, progress diary and
        <Italic> WLA support team, all in your pocket.</Italic>
      </div>

      <div className="pillars" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20, textAlign: 'left' }}>
        {PILLARS.map((p, i) => (
          <div key={i} style={{
            background: 'var(--paper)', border: '1px solid var(--hairline)',
            borderRadius: 16, padding: '26px 24px',
          }}>
            <SerifH size={24} className="card-title" style={{ marginBottom: 8 }}>{p.k}</SerifH>
            <Body size={15}>{p.v}</Body>
          </div>
        ))}
      </div>
    </div>
  </section>
);

// ---------------------------------------------------------------------------
// Headline bonus — the 8 Week Fat Loss Challenge
// ---------------------------------------------------------------------------
const CHRISTMAS_OUTCOMES = [
  'Up to a stone lighter, with visible progress towards your goal.',
  'Inches off your waist and clothes fitting more comfortably.',
  'Back in a favourite outfit that’s been sitting unworn in your wardrobe.',
  'Confident in your party outfits, without hiding behind loose layers.',
  'Seeing the difference in your photos, and feeling proud of your progress.',
  'Starting January closer to your goal, with habits in place to keep going.',
];

const ChallengeBonusSection = () => (
  <section className="challenge-section" style={{ padding: '72px 32px', background: 'var(--bg)' }}>
    <div style={{
      maxWidth: 940, margin: '0 auto',
      background: `linear-gradient(135deg, var(--peach) 0%, #F8C4B0 100%)`,
      border: '2px dashed var(--blush-deep)', borderRadius: 22,
      padding: '52px 48px 46px', position: 'relative',
      boxShadow: '0 30px 60px -30px rgba(232, 127, 99, 0.35)',
    }}>
      <div style={{
        position: 'absolute', top: -16, left: '50%', transform: 'translateX(-50%)',
        background: 'var(--blush-deep)', color: 'var(--paper)',
        padding: '8px 22px', borderRadius: 999,
        fontFamily: '"Alegreya Sans", sans-serif', fontSize: 12, fontWeight: 600,
        letterSpacing: '0.16em', textTransform: 'uppercase', whiteSpace: 'nowrap',
      }}>
        Your Founding Member bonus
      </div>

      <div style={{ textAlign: 'center', marginBottom: 28 }}>
        <SerifH size={40} style={{ lineHeight: 1.2, marginBottom: 14 }}>
          Get FREE access to my<br /><Italic>8 Week Fat Loss Challenge</Italic>
        </SerifH>
        <Body size={18} style={{ maxWidth: 640, margin: '0 auto 14px', fontWeight: 600, color: 'var(--ink)' }}>
          Starting Monday 19th October, work towards losing up to a stone before Christmas.
        </Body>
        <Body size={16} style={{ maxWidth: 640, margin: '0 auto' }}>
          Put your new WLA app into action with a focused challenge to help you finish the year feeling
          lighter, more confident and in control.
        </Body>
      </div>

      <div style={{
        fontFamily: '"Libre Baskerville", serif', fontStyle: 'italic', fontSize: 19,
        color: 'var(--ink)', textAlign: 'center', marginBottom: 20,
      }}>
        Imagine arriving at Christmas with:
      </div>

      <div className="christmas-grid" style={{
        display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 10,
        maxWidth: 820, margin: '0 auto 26px',
      }}>
        {CHRISTMAS_OUTCOMES.map((o, i) => (
          <div key={i} style={{
            display: 'flex', gap: 12, alignItems: 'flex-start',
            background: 'rgba(253, 251, 248, 0.7)',
            border: '1px solid rgba(232, 127, 99, 0.35)',
            borderRadius: 10, padding: '12px 16px',
          }}>
            <span style={{ flexShrink: 0, marginTop: 3 }}><Tick color="var(--blush-deep)" /></span>
            <Body size={15} style={{ flex: 1, minWidth: 0 }}>{o}</Body>
          </div>
        ))}
      </div>

      <div style={{
        textAlign: 'center', fontFamily: '"Libre Baskerville", serif',
        fontWeight: 700, fontSize: 19, color: 'var(--ink)',
      }}>
        Included FREE when you join as a WLA App Founding Member.
      </div>
    </div>
  </section>
);

// ---------------------------------------------------------------------------
// The twelve features
// ---------------------------------------------------------------------------
const FEATURES = [
  { n: 1,  t: 'The WLA Daily Tracker',        h: 'Understand what’s helping and what needs adjusting.', b: 'Track your meals using the Formula alongside sleep, stress and movement, so you can spot patterns behind your hunger and habits and make focused changes.' },
  { n: 2,  t: 'Your Personalised Meal Planner', h: 'Know what you’re eating before hunger makes the decision.', b: 'Plan meals around your week, so a busy day doesn’t have to turn into a last-minute takeaway or another “I’ll start tomorrow”.' },
  { n: 3,  t: 'A Fresh Meal Guide Every Friday', h: 'Stay on track without planning from scratch.', b: 'Add a ready-made week of WLA Formula-balanced meals to your planner, making consistency easier when you’re short on time or ideas.' },
  { n: 4,  t: 'Smart Shopping Lists',         h: 'Have the food you need to follow your plan.', b: 'Turn your meal plan into a shopping list in one tap, so you’re ready to cook instead of opening the fridge and wondering what to eat.' },
  { n: 5,  t: '500+ WLA Recipes',             h: 'Lose weight eating meals you look forward to.', b: 'Find filling lunches, family dinners and fakeaway favourites that help you follow the Formula without boring diet food or cooking a separate meal for yourself.' },
  { n: 6,  t: 'Your Progress Tracker',        h: 'See your results even when the scales stand still.', b: 'Track measurements, dress size and photos alongside your weight, so you can recognise changes in your body and keep going through frustrating weeks.' },
  { n: 7,  t: 'Maintenance Mode',             h: 'Reach your goal with a plan for what comes next.', b: 'Shift your focus to maintaining your progress, with continued tools and support to help you keep the habits that got you there.' },
  { n: 8,  t: 'The WLA Community',            h: 'Get support before a difficult day becomes a difficult week.', b: 'Use daily encouragement and evening check-ins with me, my coaching team and fellow members to stay accountable and find your focus again.' },
  { n: 9,  t: 'The WLA Forum',                h: 'Get help with the things that keep tripping you up.', b: 'Ask questions and get practical guidance, so uncertainty about meals, portions or habits doesn’t leave you stuck.' },
  { n: 10, t: 'The Private WLA Podcast',      h: 'Give your motivation a boost while you get on with your day.', b: 'Listen to member-only coaching on your walk or commute to help you refocus when old habits creep in.' },
  { n: 11, t: 'The WLA Toolkit',              h: 'Feel confident about portions, meals and snacks.', b: 'Use the Formula, portion and snack guides to make choices that support your goal, without counting calories or second-guessing every plate.' },
  { n: 12, t: 'Weekly Live Zoom Coaching',    h: 'Leave each week knowing what to focus on next.', b: 'Join me and the WLA coaching team for practical guidance, answers to your questions and a weekly boost to help you overcome obstacles and keep progressing towards your weight loss goal.' },
];

const FeaturesSection = () => (
  <section id="features" className="features-section" style={{ padding: '72px 32px 64px', background: 'var(--cream-deep)' }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 48 }}>
        <Eyebrow>What&rsquo;s inside</Eyebrow>
        <SerifH size={50} style={{ marginTop: 18, marginBottom: 14, lineHeight: 1.2 }}>
          Plus all this inside<br /><Italic>the new WLA app</Italic>
        </SerifH>
        <Body size={18} style={{ maxWidth: 560, margin: '0 auto', fontWeight: 600, color: 'var(--ink)' }}>
          Less guesswork. More consistency. Support to reach your goals.
        </Body>
      </div>

      <div className="features-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 18 }}>
        {FEATURES.map((f) => (
          <div key={f.n} style={{
            background: 'var(--paper)', border: '1px solid var(--hairline)',
            borderRadius: 16, padding: '26px 24px', display: 'flex', flexDirection: 'column', gap: 10,
          }}>
            <div style={{
              fontFamily: '"Libre Baskerville", serif', fontStyle: 'italic',
              fontSize: 15, color: 'var(--blush-deep)',
            }}>{String(f.n).padStart(2, '0')}</div>
            <SerifH size={21} className="card-title" style={{ lineHeight: 1.25 }}>{f.t}</SerifH>
            <Body size={15} style={{ fontWeight: 600, color: 'var(--ink)' }}>{f.h}</Body>
            <Body size={14} muted>{f.b}</Body>
          </div>
        ))}
      </div>
    </div>
  </section>
);

// ---------------------------------------------------------------------------
// The five Founding Member bonuses
// ---------------------------------------------------------------------------
const BONUSES = [
  { n: 1, t: 'The 8 Week Fat Loss Challenge (FREE)', meta: 'Normally £197 · Starts Monday 19th October',
    b: 'Start with a clear goal: work towards losing up to a stone before Christmas. Feel more confident in your party outfits, see progress in how your clothes fit and head into January closer to where you want to be.' },
  { n: 2, t: 'A Full Year of WLA App Access', meta: 'Your support continues long after the eight-week challenge',
    b: 'Get 12 months of meal planning, 500+ recipes, daily tracking, weekly live Zoom coaching and community support. Keep working towards your goal after Christmas, with fresh meal guides and ongoing support to help you maintain your progress.' },
  { n: 3, t: 'January Reset + First Challenge of 2027 (FREE)', meta: 'Combined value £297',
    b: 'Your next steps are already included. Rebuild your routine after Christmas, then keep progressing with the first challenge of 2027 without another payment.' },
  { n: 4, t: 'Your £97 Annual Rate, Locked In', meta: 'Regular price £297 a year',
    b: 'Join now and renew at £97 a year for as long as you remain a member, a £200 saving every year you renew. Keep your access to the app, fresh content, coaching and community at your Founding Member rate. This £97 is not a recurring subscription; you can extend at the Founding Member rate once your year is finished.' },
  { n: 5, t: 'Your Chance to Shape What Comes Next', meta: 'This first round is limited to 500 Founding Members',
    b: 'Get early access to new features and share your ideas through Founding Member feedback rounds.' },
];

const BonusesSection = () => (
  <section className="bonuses-section" style={{ padding: '72px 32px 64px', background: 'var(--bg)' }}>
    <div style={{ maxWidth: 940, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 44 }}>
        <Eyebrow>Your Founding Member bonuses</Eyebrow>
        <SerifH size={46} style={{ marginTop: 18, lineHeight: 1.2 }}>
          One year of WLA support.<br />A goal before Christmas.<br /><Italic>A founding rate you can keep.</Italic>
        </SerifH>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        {BONUSES.map((b) => (
          <div key={b.n} className="bonus-row" style={{
            display: 'grid', gridTemplateColumns: '64px 1fr', gap: 22, alignItems: 'start',
            background: 'var(--paper)', border: '1px solid var(--hairline)',
            borderLeft: '4px solid var(--blush-deep)', borderRadius: 16, padding: '26px 30px',
          }}>
            <div style={{
              width: 64, height: 64, borderRadius: '50%', background: 'var(--peach)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: '"Libre Baskerville", serif', fontWeight: 700, fontSize: 24, color: 'var(--ink)',
            }}>{b.n}</div>
            <div>
              <SerifH size={23} className="card-title" style={{ marginBottom: 4 }}>Bonus {b.n}: {b.t}</SerifH>
              <Body size={14} style={{ color: 'var(--blush-deep)', fontWeight: 600, marginBottom: 8 }}>{b.meta}</Body>
              <Body size={15}>{b.b}</Body>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

// ---------------------------------------------------------------------------
// Why join now — founding vs regular
// ---------------------------------------------------------------------------
const COMPARISON = [
  { f: '£97 for 12 months. Renewal price locked in while you remain a member.',
    l: '£297 for 12 months, with no locked-in renewal price.' },
  { f: 'FREE 8 Week Fat Loss Challenge',
    l: 'The 8 Week Fat Loss Challenge, £197 separately.' },
  { f: 'FREE January Reset + first Challenge of 2027',
    l: 'January Reset and the first Challenge of 2027, £297 combined, separately.' },
  { f: 'Founding Member status, early feature access and feedback opportunities',
    l: 'Founding Member status and early feature access: not available.' },
];

const WhyJoinNowSection = () => (
  <section className="whyjoin-section" style={{ padding: '56px 32px 64px', background: 'var(--cream-deep)' }}>
    <div style={{ maxWidth: 940, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 40 }}>
        <Eyebrow>Why join now</Eyebrow>
        <SerifH size={46} style={{ marginTop: 18, lineHeight: 1.2 }}>
          Founding Member, <Italic>or later at the regular price.</Italic>
        </SerifH>
      </div>

      <div className="compare-grid" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 18 }}>
        <div style={{
          background: 'var(--paper)', border: '2px solid var(--blush-deep)',
          borderRadius: 18, padding: '28px 26px',
          boxShadow: '0 24px 48px -30px rgba(232, 127, 99, 0.45)',
        }}>
          <SerifH size={22} className="card-title" style={{ marginBottom: 18, color: 'var(--blush-deep)' }}>
            Join now as a Founding Member
          </SerifH>
          {COMPARISON.map((c, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start', marginBottom: 14 }}>
              <span style={{ flexShrink: 0, marginTop: 3 }}><Tick color="var(--blush-deep)" /></span>
              <Body size={15}>{c.f}</Body>
            </div>
          ))}
        </div>

        <div style={{
          background: 'rgba(253, 251, 248, 0.5)', border: '1px solid var(--hairline)',
          borderRadius: 18, padding: '28px 26px',
        }}>
          <SerifH size={22} className="card-title" style={{ marginBottom: 18, color: 'var(--ink-muted)' }}>
            Join later at the regular price
          </SerifH>
          {COMPARISON.map((c, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start', marginBottom: 14 }}>
              <span style={{ flexShrink: 0, marginTop: 3 }}><Cross /></span>
              <Body size={15} muted>{c.l}</Body>
            </div>
          ))}
        </div>
      </div>
    </div>
  </section>
);

// ---------------------------------------------------------------------------
// Who it's for
// ---------------------------------------------------------------------------
const FOR_YOU = [
  <><strong>You want to lose weight without counting calories</strong> or spending your day thinking about what you&rsquo;re allowed to eat.</>,
  <><strong>You&rsquo;ve lost weight before, then regained it</strong>, and want habits you can keep.</>,
  <><strong>You want satisfying meals your family can enjoy</strong>, without cooking a separate &ldquo;diet dinner&rdquo;.</>,
  <><strong>You&rsquo;re tired of starting again every Monday</strong> and need structure that fits your life.</>,
  <><strong>You want to understand your habits</strong> and see where small adjustments could help.</>,
  <><strong>You do better with support and accountability</strong>, especially when motivation dips.</>,
  <><strong>You want to feel lighter and more confident by Christmas</strong>, with a plan to keep progressing afterwards.</>,
];

const ForYouSection = () => (
  <section className="foryou-section" style={{ padding: '72px 32px 64px', background: 'var(--bg)' }}>
    <div style={{ maxWidth: 880, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 40 }}>
        <SerifH size={48} style={{ lineHeight: 1.2 }}>
          The WLA App is <Italic>for you if…</Italic>
        </SerifH>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        {FOR_YOU.map((f, i) => (
          <div key={i} style={{
            display: 'flex', gap: 14, alignItems: 'flex-start',
            background: 'var(--paper)', border: '1px solid var(--hairline)',
            borderRadius: 12, padding: '18px 22px',
          }}>
            <span style={{ flexShrink: 0, marginTop: 4 }}><Tick color="var(--blush-deep)" /></span>
            <Body size={16} style={{ flex: 1, minWidth: 0 }}>{f}</Body>
          </div>
        ))}
      </div>
      <div style={{
        fontFamily: '"Libre Baskerville", serif', fontStyle: 'italic', fontSize: 21,
        color: 'var(--ink)', textAlign: 'center', marginTop: 32, lineHeight: 1.5,
      }}>
        You don&rsquo;t need to have it all together to join. You just need to be ready to take the next step with support.
      </div>
    </div>
  </section>
);

Object.assign(window, {
  AppGallerySection, AppIntroSection, ChallengeBonusSection,
  FeaturesSection, BonusesSection, WhyJoinNowSection, ForYouSection,
});
