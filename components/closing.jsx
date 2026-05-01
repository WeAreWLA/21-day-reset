// Pricing, FAQ, Final CTA, Sticky bar, Footer

// Live countdown — counts to May 4 (early-bird ends) or May 11 (kickoff).
// Hidden once the campaign is live. Phase is recomputed every second so
// it transitions automatically across midnight thresholds.
function computeCountdownTick(phase) {
  const now = Date.now();
  let target;
  if (phase === 'pre-launch')        target = window.CAMPAIGN_EARLY_BIRD_END;
  else if (phase === 'pre-kickoff')  target = window.CAMPAIGN_KICKOFF;
  else return null;
  const diff = Math.max(0, target - now);
  return {
    days:    Math.floor(diff / 86400000),
    hours:   Math.floor((diff % 86400000) / 3600000),
    minutes: Math.floor((diff % 3600000) / 60000),
    seconds: Math.floor((diff % 60000) / 1000),
  };
}

const CountdownSection = () => {
  const [phase, setPhase] = React.useState(() => window.getCampaignPhase());
  const [tick, setTick]   = React.useState(() => computeCountdownTick(phase));

  React.useEffect(() => {
    const id = setInterval(() => {
      const newPhase = window.getCampaignPhase();
      if (newPhase !== phase) setPhase(newPhase);
      setTick(computeCountdownTick(newPhase));
    }, 1000);
    return () => clearInterval(id);
  }, [phase]);

  if (phase === 'expired' || !tick) return null;

  const eyebrow = phase === 'pre-launch' ? 'Early-bird bonus expires in' : 'Reset kicks off in';
  const subtitle = phase === 'pre-launch'
    ? 'When the timer hits zero, the £17 early-bird price and bonus expire.'
    : 'Your 21 Day Reset begins Monday 11th May. Save your seat now.';

  return (
    <section className="countdown-section" style={{
      background: 'var(--peach)',
      padding: '60px 32px',
      textAlign: 'center',
    }}>
      <div style={{ maxWidth: 920, margin: '0 auto' }}>
        <div style={{
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 13, fontWeight: 600,
          letterSpacing: '0.18em', textTransform: 'uppercase',
          color: 'var(--blush-deep)', marginBottom: 22,
        }}>
          {eyebrow}
        </div>
        <div style={{
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
            <div key={i} style={{
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
        <div style={{
          fontFamily: '"Libre Baskerville", serif',
          fontStyle: 'italic',
          fontSize: 17,
          color: 'var(--ink)',
          maxWidth: 540, margin: '0 auto',
          lineHeight: 1.5,
        }}>
          {subtitle}
        </div>
      </div>
    </section>
  );
};

const PricingSection = ({ sectionId = "join", showHeading = true, bridgeHeading = null, phase: phaseProp }) => {
  const phase = phaseProp || (typeof window !== 'undefined' && window.getCampaignPhase ? window.getCampaignPhase() : 'pre-launch');
  const isEarlyBird = phase === 'pre-launch';
  return (
  <section id={sectionId} className={bridgeHeading ? 'pricing-bridge' : ''} style={{
    padding: bridgeHeading ? '48px 32px 120px' : '120px 32px',
    background: 'var(--cream-deep)',
  }}>
    <div style={{ maxWidth: 820, margin: '0 auto', textAlign: 'center' }}>
      {showHeading && (
        <>
          <Eyebrow>Secure your place</Eyebrow>
          <SerifH size={62} style={{ marginTop: 20, marginBottom: 16 }}>
            One price.<br /><Italic>One reset.</Italic><br />Everything included.
          </SerifH>
          <Body size={18} style={{ maxWidth: 560, margin: '0 auto 48px' }}>
            {isEarlyBird
              ? 'Join today for £17, save £80 and access your FREE 3-Week Fat Loss Accelerator Meal Plan (limited available) with the early bird promo.'
              : 'Join today for £17 and start the Reset on Monday 11th May.'}
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
        {isEarlyBird && <div style={{
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
        }}>Early bird · save £80</div>}

        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'center', gap: 14, marginBottom: 10 }}>
          <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontWeight: 700,
              fontSize: 100,
            color: 'var(--ink)',
            lineHeight: 1,
          }}>£17</div>
          {isEarlyBird && <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 22,
            color: 'var(--ink-muted)',
            textDecoration: 'line-through',
          }}>£97</div>}
        </div>
        <Body size={15} style={{ marginBottom: 32 }}>
          One-time payment · full access
        </Body>

        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, textAlign: 'left', maxWidth: 460, margin: '0 auto 36px' }}>
          {[
            'Full 21-day flexible nutrition and weight meal guide + recipes',
            'Daily coaching + weekly live Zoom with Anna',
            'Multiple supporting guides & workbook',
            isEarlyBird ? 'Early-bird bonus: FREE 3-Week Fat Loss Accelerator Meal Plan' : null,
            '7-day money-back guarantee',
          ].filter(Boolean).map((f, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
              <Tick />
              <Body size={16}>{f}</Body>
            </div>
          ))}
        </div>

        <PrimaryCTA location="pricing" style={{ width: '100%', maxWidth: 460 }}>
          Join the Reset — £17
        </PrimaryCTA>

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
          <span>🔒 Secure checkout</span>
          <span>·</span>
          <span>7-day guarantee</span>
          <span>·</span>
          <span>Pre-week: Mon 4 May</span>
        </div>
      </div>

      {/* Early-bird bonus callout */}
      {isEarlyBird && <div style={{
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
          fontSize: 36,
        }}>🎁</div>
        <div>
          <SerifH size={22} style={{ marginBottom: 6 }}>Early-bird bonus</SerifH>
          <Body size={15}>
            Get the <Italic>3-Week Fat Loss Accelerator Meal Plan</Italic> free. First 100 women only · instant access on signup.
          </Body>
        </div>
      </div>}

      {/* Guarantee callout */}
      <div style={{
        marginTop: isEarlyBird ? 24 : 48,
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
    q: "When does it start?",
    a: "You'll get access to the FREE The 3 Week Fat Loss Accelerator Meal Plan the moment you join. The pre-week starts Monday 4th May. The reset tools will be shared on Friday 1st May so you're ready to begin.",
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
          {FAQ_ITEMS.map((item, i) => (
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
        You don’t need to start over <Italic>again.</Italic>
        <br />You need something you can stick to
        <br />long enough to see results.
      </SerifH>
      <Body size={19} style={{ maxWidth: 620, margin: '0 auto 40px' }}>
        21 days. £17. A reset designed to finally get you results led by a registered nutritionist who has walked 50,000 women through it.
      </Body>
      <PrimaryCTA location="final">Join the 21 Day Reset — £17</PrimaryCTA>
      <div style={{
        marginTop: 22,
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 13,
        color: 'var(--ink-muted)',
      }}>
        7-day money-back guarantee · Pre-week starts Monday 4th May
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
      <span style={{ color: 'var(--peach)' }}>●</span> 21 Day Reset · <strong>£17</strong>
      <span className="sticky-cta-secondary" style={{ opacity: 0.6, marginLeft: 8, fontSize: 12 }}>Price rises soon</span>
    </div>
    <a href={typeof window !== 'undefined' && window.getCheckoutUrl ? window.getCheckoutUrl() : 'https://sales.thewlacademy.com/may-reset/'} target="_blank" rel="noopener" className="sticky-cta-button"
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
      <a href="#" style={{ color: 'inherit', textDecoration: 'none' }}>Privacy Policy</a>
      <span>·</span>
      <a href="#" style={{ color: 'inherit', textDecoration: 'none' }}>Terms of Service</a>
      <span>·</span>
      <a href="#" style={{ color: 'inherit', textDecoration: 'none' }}>Contact</a>
    </div>
  </footer>
);

// Fast Action Bonus — limited-spots peach banner for the Accelerator Meal Plan
const FastActionBonusSection = () => (
  <section className="fastaction-section" style={{
    padding: '40px 32px 48px',
    background: 'var(--bg)',
  }}>
    <div style={{
      maxWidth: 820,
      margin: '0 auto',
      background: `linear-gradient(135deg, var(--peach) 0%, #F8C4B0 100%)`,
      border: '2px dashed var(--blush-deep)',
      borderRadius: 22,
      padding: '48px 48px 52px',
      position: 'relative',
      textAlign: 'center',
      boxShadow: '0 30px 60px -30px rgba(232, 127, 99, 0.35)',
    }}>
      <div style={{
        position: 'absolute',
        top: -18, left: '50%', transform: 'translateX(-50%)',
        background: 'var(--blush-deep)', color: 'var(--paper)',
        padding: '8px 22px', borderRadius: 999,
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 12, fontWeight: 600,
        letterSpacing: '0.16em', textTransform: 'uppercase',
        whiteSpace: 'nowrap',
      }}>
        🎁 Fast action bonus (limited)
      </div>

      <SerifH size={40} style={{ marginTop: 16, marginBottom: 18, color: 'var(--ink)', lineHeight: 1.2 }}>
        The first 100 women who join receive my<br />
        <Italic>3-week fat loss accelerator meal plan</Italic><br />completely FREE.
      </SerifH>

      <Body size={17} style={{ maxWidth: 560, margin: '0 auto 32px' }}>
        This is your head-start plan, so you can begin before the Reset even starts.
      </Body>

      <div style={{
        maxWidth: 460, margin: '0 auto 32px',
        display: 'flex', flexDirection: 'column', gap: 14,
        textAlign: 'left',
      }}>
        {[
          'Know exactly what to eat from your next meal',
          'Start making progress straight away',
          'Build momentum before Day 1',
        ].map((item, i) => (
          <div key={i} style={{ display: 'flex', gap: 14, alignItems: 'flex-start' }}>
            <Tick />
            <Body size={16} style={{ flex: 1, minWidth: 0 }}>{item}</Body>
          </div>
        ))}
      </div>

      <div style={{
        fontFamily: '"Libre Baskerville", serif',
        fontSize: 21,
        color: 'var(--ink)',
        marginBottom: 24,
        lineHeight: 1.4,
      }}>
        So when the Reset begins…<br /><em style={{ fontStyle: 'italic', fontWeight: 700, color: 'var(--blush-deep)' }}>You’re already ahead.</em>
      </div>

      <div style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: 10,
        background: 'var(--ink)',
        color: 'var(--paper)',
        padding: '10px 20px',
        borderRadius: 999,
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 13,
        fontWeight: 600,
        letterSpacing: '0.08em',
        textTransform: 'uppercase',
      }}>
        ⚠️ Only available for the first 100 women
      </div>
    </div>
  </section>
);

Object.assign(window, { PricingSection, FAQSection, FinalCTA, StickyCTA, Footer, FastActionBonusSection, CountdownSection });
