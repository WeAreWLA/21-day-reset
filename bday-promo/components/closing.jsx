// Pricing, FAQ, Final CTA, Sticky bar, Footer — Birthday Promo (/bday-promo)

// Live countdown — counts down the £7 window. Hidden once the price
// has gone up. Phase is recomputed every second so it transitions without a
// page refresh.
function computeCountdownTick() {
  const diff = Math.max(0, window.OFFER_END - Date.now());
  return {
    days:    Math.floor(diff / 86400000),
    hours:   Math.floor((diff % 86400000) / 3600000),
    minutes: Math.floor((diff % 3600000) / 60000),
    seconds: Math.floor((diff % 60000) / 1000),
  };
}

const CountdownSection = () => {
  const [phase, setPhase] = React.useState(() => window.getCampaignPhase());
  const [tick, setTick]   = React.useState(() => computeCountdownTick());

  React.useEffect(() => {
    const id = setInterval(() => {
      const newPhase = window.getCampaignPhase();
      if (newPhase !== phase) setPhase(newPhase);
      setTick(computeCountdownTick());
    }, 1000);
    return () => clearInterval(id);
  }, [phase]);

  if (phase !== 'open' || !tick) return null;

  return (
    <section className="countdown-section" style={{
      background: 'var(--peach)',
      padding: '60px 32px',
      textAlign: 'center',
    }}>
      <div style={{ maxWidth: 920, margin: '0 auto' }}>
        <SerifH size={46} className="countdown-heading" style={{ marginBottom: 26, lineHeight: 1.2 }}>
          The <Italic>£7 price</Italic> disappears in
        </SerifH>
        <div className="countdown-grid" style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(4, 1fr)',
          gap: 14,
          maxWidth: 720,
          margin: '0 auto 28px',
        }}>
          {[
            { n: tick.days,    l: 'days' },
            { n: tick.hours,   l: 'hours' },
            { n: tick.minutes, l: 'mins' },
            { n: tick.seconds, l: 'secs' },
          ].map((item, i) => (
            <div key={i} className="countdown-box" style={{
              background: 'var(--paper)',
              border: '1px solid var(--blush-deep)',
              borderRadius: 14,
              padding: '24px 8px',
              boxShadow: '0 14px 30px -16px rgba(232, 127, 99, 0.4)',
            }}>
              <div className="countdown-num" style={{
                fontFamily: '"Libre Baskerville", serif',
                fontSize: 52, fontWeight: 700,
                color: 'var(--ink)', lineHeight: 1,
                fontVariantNumeric: 'tabular-nums',
              }}>
                {String(item.n).padStart(2, '0')}
              </div>
              <div className="countdown-lab" style={{
                fontFamily: '"Alegreya Sans", sans-serif',
                fontSize: 12, letterSpacing: '0.16em',
                textTransform: 'uppercase', color: 'var(--blush-deep)',
                fontWeight: 600, marginTop: 12,
              }}>
                {item.l}
              </div>
            </div>
          ))}
        </div>
        <div className="countdown-facts" style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 12,
          maxWidth: 720,
          margin: '0 auto',
        }}>
          {[
            { k: `${window.OFFER_HOURS} hours`, v: 'then the price increases' },
            { k: '100 spots', v: 'and no more after that' },
            { k: 'Mon 31 Aug', v: 'pre-week starts' },
          ].map((f, i) => (
            <div key={i} style={{
              background: 'rgba(253, 251, 248, 0.65)',
              border: '1px solid var(--blush-deep)',
              borderRadius: 12,
              padding: '14px 10px',
            }}>
              <div style={{
                fontFamily: '"Libre Baskerville", serif',
                fontWeight: 700, fontSize: 19,
                color: 'var(--ink)', lineHeight: 1.2,
              }}>{f.k}</div>
              <div style={{
                fontFamily: '"Alegreya Sans", sans-serif',
                fontSize: 13, color: 'var(--ink)',
                opacity: 0.75, marginTop: 4, lineHeight: 1.35,
              }}>{f.v}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

// Spots-remaining bar. Numbers come from SPOTS_TAKEN in sections.jsx and must
// be kept truthful — see the note there.
const SpotsRemainingSection = () => {
  const total = window.SPOTS_AVAILABLE;
  const taken = window.SPOTS_TAKEN;
  const left  = window.SPOTS_LEFT;
  const pct   = Math.round((taken / total) * 100);
  return (
    <section className="spots-section" style={{
      padding: '52px 32px 12px',
      background: 'var(--bg)',
    }}>
      <div style={{
        maxWidth: 760,
        margin: '0 auto',
        background: 'var(--paper)',
        border: '1px solid var(--hairline)',
        borderLeft: '4px solid var(--blush-deep)',
        borderRadius: 16,
        padding: '26px 30px',
        boxShadow: '0 24px 48px -32px rgba(80, 40, 20, 0.28)',
      }}>
        <div className="spots-head" style={{
          display: 'flex', alignItems: 'baseline', justifyContent: 'space-between',
          gap: 16, flexWrap: 'wrap', marginBottom: 14,
        }}>
          <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontWeight: 700,
            fontSize: 22,
            color: 'var(--ink)',
            lineHeight: 1.3,
          }}>
            <Italic>{left}</Italic> of {total} places left
          </div>
          <div style={{
            fontFamily: '"Alegreya Sans", sans-serif',
            fontSize: 14,
            color: 'var(--blush-deep)',
            fontWeight: 600,
            letterSpacing: '0.02em',
          }}>
            {taken} already taken
          </div>
        </div>

        <div style={{
          height: 12,
          borderRadius: 999,
          background: 'var(--cream-deep)',
          overflow: 'hidden',
        }}>
          <div style={{
            width: pct + '%',
            height: '100%',
            borderRadius: 999,
            background: 'linear-gradient(90deg, var(--terracotta) 0%, var(--blush-deep) 100%)',
          }} />
        </div>

        <Body size={14} style={{ marginTop: 12 }}>
          Places are limited to {total} so everyone gets proper coaching. When they&rsquo;re gone, they&rsquo;re gone —
          the next round won&rsquo;t be at this price.
        </Body>
      </div>
    </section>
  );
};

const PricingSection = ({ sectionId = "join", showHeading = true, bridgeHeading = null, phase: phaseProp }) => {
  const phase = phaseProp || (typeof window !== 'undefined' && window.getCampaignPhase ? window.getCampaignPhase() : 'open');
  const isOpen = phase === 'open';
  return (
  <section id={sectionId} className={bridgeHeading ? 'pricing-bridge' : ''} style={{
    padding: bridgeHeading ? '48px 32px 120px' : '120px 32px',
    background: 'var(--cream-deep)',
  }}>
    <div style={{ maxWidth: 820, margin: '0 auto', textAlign: 'center' }}>
      {showHeading && (
        <>
          <Eyebrow>My birthday, your gift</Eyebrow>
          <SerifH size={62} style={{ marginTop: 20, marginBottom: 16 }}>
            One price.<br /><Italic>One reset.</Italic><br />Everything included.
          </SerifH>
          <Body size={18} style={{ maxWidth: 560, margin: '0 auto 48px' }}>
            {isOpen
              ? `It’s my birthday, so the whole 21 Day Reset is £7 — for ${window.OFFER_HOURS} hours only, and only 100 spots are available. The price increases when the timer runs out. Pre-week starts Monday 31st August.`
              : 'Join today for £7 and start the 21 Day Reset with us.'}
          </Body>
        </>
      )}
      {bridgeHeading && (
        <div style={{ marginBottom: 48 }}>
          {bridgeHeading}
        </div>
      )}

      <div style={{
        background: 'var(--paper)',
        border: '1px solid var(--hairline)',
        borderRadius: 24,
        padding: '48px 56px',
        boxShadow: '0 30px 60px -30px rgba(80, 40, 20, 0.25)',
        position: 'relative',
      }}>
        {isOpen && <div style={{
          position: 'absolute',
          top: -14,
          left: '50%',
          transform: 'translateX(-50%)',
          background: 'var(--blush-deep)',
          color: 'var(--paper)',
          padding: '6px 20px',
          borderRadius: 999,
          fontFamily: '"Libre Baskerville", serif',
          fontSize: 13,
          fontStyle: 'italic',
          fontWeight: 400,
          letterSpacing: '0.04em',
        }}>🎂 Birthday offer · save £90</div>}

        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'center', gap: 14, marginBottom: 10 }}>
          <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontWeight: 700,
              fontSize: 100,
            color: 'var(--ink)',
            lineHeight: 1,
          }}>£7</div>
          {isOpen && <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 22,
            color: 'var(--ink-muted)',
            textDecoration: 'line-through',
          }}>£97</div>}
        </div>
        <PriceAnchor style={{ marginBottom: 6 }} />
        <Body size={15} style={{ marginBottom: 32 }}>
          One-time payment · full access
        </Body>

        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, textAlign: 'left', maxWidth: 460, margin: '0 auto 36px' }}>
          {[
            'Full 21-day flexible nutrition and weight meal guide + recipes',
            'Daily coaching + weekly live Zoom with Anna',
            'Multiple supporting guides & workbook',
            'Bonus 1: instant access to the WLA Members’ Area (100s of recipes, meal guides & shopping lists)',
            'Bonus 2: three weekly live weight-loss masterclasses',
            '7-day money-back guarantee',
          ].filter(Boolean).map((f, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
              <Tick />
              <Body size={16}>{f}</Body>
            </div>
          ))}
        </div>

        <PrimaryCTA location="pricing" style={{ width: '100%', maxWidth: 460 }}>
          Join the Reset — £7
        </PrimaryCTA>

        <PayPalCTA location="pricing" style={{ maxWidth: 460, margin: '10px auto 0' }} />

        <GuaranteeNote style={{ maxWidth: 460, margin: '12px auto 0' }} />

        <div style={{
          marginTop: 24,
          display: 'flex',
          justifyContent: 'center',
          gap: 24,
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 12,
          color: 'var(--ink-muted)',
          letterSpacing: '0.04em',
          flexWrap: 'wrap',
        }}>
          <span>🔒 Secure checkout · card or PayPal</span>
          <span>·</span>
          <span>7-day guarantee</span>
          <span>·</span>
          <span>Pre-week: Mon 31 Aug</span>
        </div>
      </div>

      {/* Guarantee callout */}
      <div style={{
        marginTop: 48,
        display: 'grid',
        gridTemplateColumns: '80px 1fr',
        gap: 24,
        alignItems: 'center',
        background: 'var(--paper)',
        border: '1px dashed var(--blush-deep)',
        borderRadius: 16,
        padding: '28px 36px',
        textAlign: 'left',
      }}>
        <div style={{
          width: 80,
          height: 80,
          borderRadius: '50%',
          background: 'var(--peach)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: '"Libre Baskerville", serif',
          fontWeight: 700,
              fontSize: 28,
          color: 'var(--blush-deep)',
        }}>7</div>
        <div>
          <SerifH size={22} style={{ marginBottom: 6 }}>Our 7-day money-back guarantee</SerifH>
          <Body size={15} muted>
            Join, open the materials, show up to the first live call. If within 7 days you don't feel this is for you, email us — full refund, no questions, no hoops.
          </Body>
        </div>
      </div>
    </div>
  </section>
  );
};

const FAQ_ITEMS = [
  {
    q: "I've tried everything. Why would this work now?",
    a: "Because most of what you've tried hasn't shown you how to properly fuel your body for fat loss and is not sustainable. The Reset is built around simple, balanced nutrition: keeping blood sugar steady, prioritising protein to support your metabolism, creating meals that keep you full, and including carbs in a way that actually works. It's the opposite of restrictive diets and low-calorie plans that leave you hungry and stuck in the same cycle.",
  },
  {
    q: "Will this work during menopause?",
    a: "Yes, the Reset focuses on fuelling your body properly, keeping your energy steady, and giving you a simple structure you can stick to. Most women find that once they're eating the right balance of foods again, cravings settle, energy improves, and weight loss starts to feel much easier.",
  },
  {
    q: "Do I need to exercise?",
    a: "No. 80% of results come from nutrition. If you already move, keep moving. If you don't, the Reset works without it — and we'll guide you gently if and when you want to add simple strength work to protect muscle through midlife.",
  },
  {
    q: "I'm short on time and cook for a family.",
    a: "The meal guides are batch-cookable, family-friendly, and flexible. You'll cook one meal — family eats it too, you just portion differently. There's also a no-prep food list and freezer dinner pack for busy days.",
  },
  {
    q: "I'm vegetarian / fussy / don't like some ingredients.",
    a: "That's totally fine. Every recipe has vegetarian swaps available. A dedicated Food Swap List makes it easy to substitute anything you don't like. You won't have to force down food you hate, that never works long-term.",
  },
  {
    q: "What if I don't get results?",
    a: "You're covered by our 7-day money-back guarantee — show up, open the materials, and if it's not for you we refund in full. If you complete the 21 days and show up to the coaching, typical members report cravings calmer by day 3 and visible changes within the first 7 days.",
  },
  {
    q: "Why is it only £7?",
    a: "Because it's my birthday, and this is how I like to celebrate it. Every year I open the Reset up at a price that makes it a no-brainer, so that money is never the reason a woman puts herself last again. It's the full 21 Day Reset — nothing stripped out, nothing held back, plus instant access to the WLA Members' Area. It's £7 for a few days only and there are just 100 spots — the price increases when the timer runs out.",
  },
  {
    q: "When does it start?",
    a: "Pre-week starts Monday 31st August. You'll get your materials — and instant access to the WLA Members' Area — as soon as you join, so you can read through and get set up before Day 1.",
  },
  {
    q: "Will my grocery bill go up?",
    a: "Usually it goes down. You'll shop from a plan instead of daily top-up trips, use staples you likely already have, and there are budget-friendly swap options built into every guide.",
  },
];

const FAQItem = ({ item, isOpen, onToggle }) => (
  <div style={{
    borderBottom: '1px solid var(--hairline)',
  }}>
    <button
      onClick={onToggle}
      style={{
        width: '100%',
        padding: '28px 0',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: 24,
        background: 'transparent',
        border: 'none',
        cursor: 'pointer',
        textAlign: 'left',
        fontFamily: '"Libre Baskerville", serif',
        fontWeight: 700,
              fontSize: 22,
        color: 'var(--ink)',
        letterSpacing: '-0.005em',
      }}
    >
      <span style={{ flex: 1 }}>{item.q}</span>
      <span style={{
        fontSize: 24,
        color: 'var(--blush-deep)',
        transform: isOpen ? 'rotate(45deg)' : 'rotate(0)',
        transition: 'transform .25s ease',
        fontFamily: '"Alegreya Sans", sans-serif',
        fontWeight: 300,
      }}>+</span>
    </button>
    <div style={{
      maxHeight: isOpen ? 400 : 0,
      overflow: 'hidden',
      transition: 'max-height .35s ease, padding .25s ease',
      paddingBottom: isOpen ? 28 : 0,
    }}>
      <Body size={17} style={{ maxWidth: 780 }}>{item.a}</Body>
    </div>
  </div>
);

const FAQSection = () => {
  const [open, setOpen] = React.useState(0);
  const items = FAQ_ITEMS;
  return (
    <section id="faq" className="faq-section" style={{
      padding: '48px 32px 120px',
      background: 'var(--bg)',
    }}>
      <div style={{
        maxWidth: 1000,
        margin: '0 auto',
        display: 'grid',
        gridTemplateColumns: '0.7fr 1.3fr',
        gap: 72,
        alignItems: 'start',
      }}>
        <div style={{ position: 'sticky', top: 60 }}>
          <Eyebrow>Answers</Eyebrow>
          <SerifH size={52} style={{ marginTop: 20, marginBottom: 18 }}>
            Questions from<br /><Italic>women like you.</Italic>
          </SerifH>
          <Body size={15}>
            Can't find what you're looking for? Email <a href="mailto:support@theweightloss-academy.com" style={{ color: 'var(--blush-deep)', textDecoration: 'none' }}>support@theweightloss-academy.com</a> — we answer every message.
          </Body>
        </div>
        <div>
          {items.map((item, i) => (
            <FAQItem
              key={i}
              item={item}
              isOpen={open === i}
              onToggle={() => setOpen(open === i ? -1 : i)}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

// Final CTA
const FinalCTA = () => (
  <section style={{
    padding: '140px 32px',
    background: `linear-gradient(180deg, var(--cream-deep) 0%, var(--peach) 100%)`,
    textAlign: 'center',
  }}>
    <div style={{ maxWidth: 860, margin: '0 auto' }}>
      <Divider style={{ marginBottom: 32 }} />
      <SerifH size={76} style={{ marginBottom: 32 }}>
        It’s my birthday{'\u00a0'}— <Italic>the gift is yours.</Italic>
        <br />You don’t need to start over again.
        <br />You need something you can stick to.
      </SerifH>
      <Body size={19} style={{ maxWidth: 620, margin: '0 auto 40px' }}>
        21 days. £7 — for {window.OFFER_HOURS} hours, for 100 women. The whole Reset, led by a registered nutritionist who has walked 50,000 women through it. The price increases when the timer runs out.
      </Body>
      <PrimaryCTA location="final">Join the 21 Day Reset — £7</PrimaryCTA>
      <PayPalCTA location="final" style={{ maxWidth: 340, margin: '12px auto 0' }} />
      <PriceAnchor style={{ marginTop: 16 }} />
      <GuaranteeNote style={{ maxWidth: 520, margin: '10px auto 0' }} />
      <div style={{
        marginTop: 8,
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 13,
        color: 'var(--ink-muted)',
      }}>
        Pre-week starts Monday 31st August
      </div>
    </div>
  </section>
);

const StickyCTA = ({ visible }) => (
  <div className="sticky-cta" style={{
    position: 'fixed',
    bottom: visible ? 20 : -120,
    left: '50%',
    transform: 'translateX(-50%)',
    transition: 'bottom .35s ease',
    background: 'var(--ink)',
    color: 'var(--paper)',
    borderRadius: 999,
    padding: '10px 10px 10px 24px',
    display: 'flex',
    alignItems: 'center',
    gap: 20,
    boxShadow: '0 20px 40px -15px rgba(0,0,0,0.4)',
    zIndex: 100,
    flexWrap: 'nowrap',
    maxWidth: 'calc(100vw - 24px)',
    boxSizing: 'border-box',
  }}>
    <div className="sticky-cta-text" style={{
      fontFamily: '"Alegreya Sans", sans-serif',
      fontSize: 13,
      letterSpacing: '0.02em',
      whiteSpace: 'nowrap',
      minWidth: 0,
      overflow: 'hidden',
      textOverflow: 'ellipsis',
    }}>
      <span style={{ color: 'var(--peach)' }}>●</span> 🎂 Birthday offer · <strong>£7</strong>
      <span className="sticky-cta-secondary" style={{ opacity: 0.6, marginLeft: 8, fontSize: 12 }}>{window.OFFER_HOURS} hrs only</span>
    </div>
    <a href={typeof window !== 'undefined' && window.getCheckoutUrl ? window.getCheckoutUrl() : '#'} target="_blank" rel="noopener" className="sticky-cta-button"
      onClick={(e) => {
        if (window.getCheckoutUrl) e.currentTarget.href = window.getCheckoutUrl();
        if (window.trackCtaClick) window.trackCtaClick('sticky', 'Secure your place');
      }}
      style={{
      background: 'var(--blush-deep)',
      color: 'var(--paper)',
      padding: '12px 22px',
      borderRadius: 999,
      fontFamily: '"Alegreya Sans", sans-serif',
      fontSize: 14,
      fontWeight: 600,
      textDecoration: 'none',
      whiteSpace: 'nowrap',
      flexShrink: 0,
    }}>Secure your place →</a>
  </div>
);

// Exit-intent modal — desktop only, once per browser session.
// Triggers when the cursor leaves through the top of the viewport, which on a
// desktop means heading for the tab bar / close button.
const ExitIntentModal = () => {
  const [open, setOpen] = React.useState(false);
  const [tick, setTick] = React.useState(null);

  React.useEffect(() => {
    // Desktop only: skip touch devices and anything narrow.
    const isDesktop = window.matchMedia('(min-width: 961px) and (hover: hover) and (pointer: fine)').matches;
    if (!isDesktop) return;
    if (window.getCampaignPhase && window.getCampaignPhase() !== 'open') return;
    try { if (sessionStorage.getItem('wla_exit_shown')) return; } catch (e) { /* private mode */ }

    let armed = false;
    const arm = setTimeout(() => { armed = true; }, 8000); // don't fire on an instant bounce

    const onLeave = (e) => {
      if (!armed || e.clientY > 0 || e.relatedTarget) return;
      setOpen(true);
      try { sessionStorage.setItem('wla_exit_shown', '1'); } catch (err) { /* ignore */ }
      document.removeEventListener('mouseout', onLeave);
    };
    document.addEventListener('mouseout', onLeave);
    return () => { clearTimeout(arm); document.removeEventListener('mouseout', onLeave); };
  }, []);

  React.useEffect(() => {
    if (!open) return;
    const compute = () => {
      const diff = Math.max(0, window.OFFER_END - Date.now());
      return {
        d: Math.floor(diff / 86400000),
        h: Math.floor((diff % 86400000) / 3600000),
        m: Math.floor((diff % 3600000) / 60000),
        s: Math.floor((diff % 60000) / 1000),
      };
    };
    setTick(compute());
    const id = setInterval(() => setTick(compute()), 1000);
    const onKey = (e) => { if (e.key === 'Escape') setOpen(false); };
    document.addEventListener('keydown', onKey);
    return () => { clearInterval(id); document.removeEventListener('keydown', onKey); };
  }, [open]);

  if (!open || !tick) return null;

  const Box = ({ n, l }) => (
    <div style={{
      background: 'var(--paper)',
      border: '1px solid var(--blush-deep)',
      borderRadius: 12,
      padding: '14px 6px',
      minWidth: 68,
    }}>
      <div style={{
        fontFamily: '"Libre Baskerville", serif',
        fontWeight: 700, fontSize: 32, lineHeight: 1,
        color: 'var(--ink)', fontVariantNumeric: 'tabular-nums',
      }}>{String(n).padStart(2, '0')}</div>
      <div style={{
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 10, letterSpacing: '0.14em', textTransform: 'uppercase',
        color: 'var(--blush-deep)', fontWeight: 600, marginTop: 8,
      }}>{l}</div>
    </div>
  );

  return (
    <div
      className="exit-intent-backdrop"
      role="dialog"
      aria-modal="true"
      aria-label="Before you go"
      onClick={() => setOpen(false)}
      style={{
        position: 'fixed', inset: 0, zIndex: 300,
        background: 'rgba(0, 48, 96, 0.55)',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: 24,
      }}
    >
      <div
        onClick={(e) => e.stopPropagation()}
        style={{
          position: 'relative',
          maxWidth: 560, width: '100%',
          background: `linear-gradient(160deg, var(--paper) 0%, var(--peach) 100%)`,
          border: '2px solid var(--blush-deep)',
          borderRadius: 22,
          padding: '44px 48px 40px',
          textAlign: 'center',
          boxShadow: '0 40px 80px -30px rgba(0, 0, 0, 0.5)',
        }}
      >
        <button
          onClick={() => setOpen(false)}
          aria-label="Close"
          style={{
            position: 'absolute', top: 14, right: 16,
            background: 'transparent', border: 'none', cursor: 'pointer',
            fontSize: 26, lineHeight: 1, color: 'var(--ink-muted)',
          }}
        >×</button>

        <div style={{ fontSize: 34, marginBottom: 10 }}>🎂</div>
        <SerifH size={34} style={{ lineHeight: 1.2, marginBottom: 12 }}>
          Before you go —<br /><Italic>the £7 price is still open</Italic>
        </SerifH>
        <Body size={16} style={{ marginBottom: 22 }}>
          The whole 21 Day Fat Loss Reset, both bonuses included. When this timer runs out the price increases.
        </Body>

        <div style={{ display: 'flex', gap: 10, justifyContent: 'center', marginBottom: 24 }}>
          <Box n={tick.d} l="days" />
          <Box n={tick.h} l="hrs" />
          <Box n={tick.m} l="min" />
          <Box n={tick.s} l="sec" />
        </div>

        <PrimaryCTA location="exit-intent" onClick={() => setOpen(false)} style={{ width: '100%' }}>
          Join the Reset — £7
        </PrimaryCTA>
        <PayPalCTA location="exit-intent" style={{ marginTop: 10 }} />
        <GuaranteeNote style={{ marginTop: 12 }} />
      </div>
    </div>
  );
};

const Footer = () => (
  <footer style={{
    background: 'var(--ink)',
    color: 'oklch(0.7 0.015 50)',
    padding: '48px 32px 36px',
    textAlign: 'center',
    fontFamily: '"Alegreya Sans", sans-serif',
    fontSize: 13,
  }}>
    <div style={{
      fontFamily: '"Libre Baskerville", serif',
      fontWeight: 700,
              fontSize: 22,
      color: 'var(--paper)',
      marginBottom: 12,
    }}>Weight Loss Academy</div>
    <div style={{ opacity: 0.7, marginBottom: 20 }}>
      © 2026 AW Nutrition Solutions Limited · All rights reserved
    </div>
    <div style={{ display: 'flex', justifyContent: 'center', gap: 24, opacity: 0.7 }}>
      <a href="https://www.wearewla.com/privacy-policy" target="_blank" rel="noopener" style={{ color: 'inherit', textDecoration: 'none' }}>Privacy Policy</a>
      <span>·</span>
      <a href="https://www.wearewla.com/terms-of-service" target="_blank" rel="noopener" style={{ color: 'inherit', textDecoration: 'none' }}>Terms of Service</a>
      <span>·</span>
      <a href="mailto:support@theweightloss-academy.com" style={{ color: 'inherit', textDecoration: 'none' }}>Contact</a>
    </div>
  </footer>
);

Object.assign(window, { PricingSection, SpotsRemainingSection, ExitIntentModal, FAQSection, FinalCTA, StickyCTA, Footer, CountdownSection });
