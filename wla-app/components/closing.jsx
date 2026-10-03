// Pricing, FAQ, Final CTA, Sticky bar, Footer — WLA App (/wla-app)

// Live countdown — counts down the offer window. Hidden once the price
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

  // No confirmed closing date yet, so no countdown. See OFFER_END_CONFIRMED.
  if (!window.OFFER_END_CONFIRMED) return null;
  if (phase !== 'open' || !tick) return null;

  return (
    <section className="countdown-section" style={{
      background: 'var(--peach)',
      padding: '60px 32px',
      textAlign: 'center',
    }}>
      <div style={{ maxWidth: 920, margin: '0 auto' }}>
        <SerifH size={46} className="countdown-heading" style={{ marginBottom: 26, lineHeight: 1.2 }}>
          Founding Member pricing <Italic>closes in</Italic>
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
            { k: window.SPOTS_TAKEN > 0 ? `${window.SPOTS_LEFT} places left` : `${window.SPOTS_AVAILABLE} places`, v: 'in this first round' },
            { k: 'Mon 19 Oct', v: 'the 8 Week Challenge kicks off' },
            { k: `${window.PRICE} locked in`, v: `every year you renew, instead of ${window.PRICE_WAS}` },
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
            {taken > 0
              ? <><Italic>{left}</Italic> of {total} places left</>
              : <><Italic>{total}</Italic> Founding Member places</>}
          </div>
          {taken > 0 && (
            <div style={{
              fontFamily: '"Alegreya Sans", sans-serif',
              fontSize: 14,
              color: 'var(--blush-deep)',
              fontWeight: 600,
              letterSpacing: '0.02em',
            }}>
              {taken} already taken
            </div>
          )}
        </div>

        {taken > 0 && (
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
        )}

        <Body size={14} style={{ marginTop: 12 }}>
          This first Founding Member round is capped at {total} places. Once they are gone, the app opens to
          everyone at {window.PRICE_WAS} a year.
        </Body>
      </div>
    </section>
  );
};

const PRICING_INCLUDES = [
  '12 months of WLA app access',
  'FREE 8 Week Fat Loss Challenge, starting Monday 19th October (worth £197)',
  'FREE January Reset and the first Challenge of 2027 (worth £297 combined)',
  'Your £97 annual rate locked in for as long as you remain a member',
  'Founding Member status, early access to new features and feedback rounds',
];

const PricingSection = ({ sectionId = "join", showHeading = true, bridgeHeading = null, phase: phaseProp }) => {
  const phase = phaseProp || (typeof window !== 'undefined' && window.getCampaignPhase ? window.getCampaignPhase() : 'open');
  const isOpen = phase === 'open';
  return (
  <section id={sectionId} className={bridgeHeading ? 'pricing-bridge' : ''} style={{
    padding: bridgeHeading ? '48px 32px 120px' : '110px 32px',
    background: 'var(--cream-deep)',
  }}>
    <div style={{ maxWidth: 820, margin: '0 auto', textAlign: 'center' }}>
      {showHeading && (
        <>
          <Eyebrow>Founding Member launch</Eyebrow>
          <SerifH size={58} style={{ marginTop: 20, marginBottom: 16 }}>
            Secure your<br /><Italic>Founding Member place</Italic>
          </SerifH>
          <Body size={18} style={{ maxWidth: 580, margin: '0 auto 48px' }}>
            {isOpen
              ? <>Only {window.SPOTS_AVAILABLE} places in this first round. You get first access before doors open to everyone next week.</>
              : <>Founding Member pricing has closed. The WLA App is now {window.PRICE_WAS} for 12 months.</>}
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
          whiteSpace: 'nowrap',
        }}>Founding Member rate · save {window.PRICE_SAVING} a year</div>}

        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'center', gap: 14, marginBottom: 10 }}>
          <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontWeight: 700,
            fontSize: 100,
            color: 'var(--ink)',
            lineHeight: 1,
          }}>{window.PRICE}</div>
          {isOpen && <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 22,
            color: 'var(--ink-muted)',
            textDecoration: 'line-through',
          }}>{window.PRICE_WAS}</div>}
        </div>
        <Body size={15} style={{ marginBottom: 4 }}>
          for 12 months{isOpen ? <> · regular price {window.PRICE_WAS} a year</> : null}
        </Body>
        <PriceAnchor style={{ marginBottom: 32 }} />

        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, textAlign: 'left', maxWidth: 480, margin: '0 auto 32px' }}>
          {PRICING_INCLUDES.map((f, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
              <Tick />
              <Body size={16}>{f}</Body>
            </div>
          ))}
        </div>

        <PrimaryCTA location="pricing" style={{ width: '100%', maxWidth: 480 }}>
          Claim My Founding Member Place
        </PrimaryCTA>

        <Body size={14} muted style={{ maxWidth: 480, margin: '14px auto 0' }}>
          Full WLA app access and all Founding Member bonuses included. If you choose to renew, your price
          stays {window.PRICE} for another year.
        </Body>

        {isOpen && (
          <div style={{
            marginTop: 18,
            fontFamily: '"Libre Baskerville", serif',
            fontWeight: 700,
            fontSize: 17,
            color: 'var(--blush-deep)',
          }}>
            {window.SPOTS_TAKEN > 0
              ? `${window.SPOTS_LEFT} of ${window.SPOTS_AVAILABLE} places remaining`
              : `Only ${window.SPOTS_AVAILABLE} places in this first round`}
          </div>
        )}

        <div className="pricing-trust-row" style={{
          marginTop: 26,
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 10,
          maxWidth: 480,
          margin: '26px auto 0',
          borderTop: '1px solid var(--hairline)',
          paddingTop: 18,
        }}>
          {[
            { icon: '🔒', k: 'Secure checkout', v: 'One payment' },
            { icon: '📅', k: 'Challenge starts', v: 'Mon 19 Oct' },
            { icon: '🎟️', k: 'First round', v: `${window.SPOTS_AVAILABLE} places` },
          ].map((t, i) => (
            <div key={i} style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 15, lineHeight: 1.2, marginBottom: 5 }}>{t.icon}</div>
              <div style={{
                fontFamily: '"Alegreya Sans", sans-serif',
                fontSize: 12.5, fontWeight: 600,
                color: 'var(--ink)', lineHeight: 1.3,
              }}>{t.k}</div>
              <div style={{
                fontFamily: '"Alegreya Sans", sans-serif',
                fontSize: 11.5, color: 'var(--ink-muted)',
                lineHeight: 1.3, marginTop: 1,
              }}>{t.v}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  </section>
  );
};

const FAQ_ITEMS = [
  { q: 'What does "locked in" mean?',
    a: 'You pay £97 for your first year. If you want to renew after year one, you keep paying £97, even when the regular price is £297.' },
  { q: 'When does the 8 Week Fat Loss Challenge start?',
    a: 'We start together on Monday 19th October, so you have a full eight weeks to Christmas.' },
  { q: 'Do I need to count calories?',
    a: 'No. The WLA Formula is about carb balancing your meals and focusing on adequate amounts of protein, fibre and healthy fats.' },
  { q: 'Can my family eat the same meals?',
    a: 'Yes. WLA recipes are real, everyday food the whole family will enjoy.' },
  { q: "What if I'm not very techy?",
    a: 'The app is simple to use, and my team and I are here to help if you get stuck.' },
  { q: 'Will this promo come back?',
    a: 'No. Founding Member pricing, status and the free challenge are only available in this first round. Future members will pay £297 a year.' },
  { q: 'What happens when all 500 places are gone?',
    a: 'Founding Member pricing closes for good and the app will open later at £297 a year.' },
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
            Can't find what you're looking for? Email <a href="mailto:support@theweightloss-academy.com" style={{ color: 'var(--blush-deep)', textDecoration: 'none' }}>support@theweightloss-academy.com</a> and we answer every message.
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
      <SerifH size={72} style={{ marginBottom: 32 }}>
        Be one of the first 500.<br /><Italic>Start the challenge on 19th October.</Italic>
      </SerifH>
      <Body size={19} style={{ maxWidth: 620, margin: '0 auto 40px' }}>
        You don’t need to have it all together to join. You just need to be ready to take the next step
        with support.
      </Body>
      <PrimaryCTA location="final">Become a Founding Member {window.PRICE}</PrimaryCTA>
      <PriceAnchor style={{ marginTop: 16 }} />
      <div style={{
        marginTop: 8,
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 13,
        color: 'var(--ink-muted)',
      }}>
        {window.SPOTS_TAKEN > 0
          ? `${window.SPOTS_LEFT} of ${window.SPOTS_AVAILABLE} Founding Member places remaining`
          : `Only ${window.SPOTS_AVAILABLE} Founding Member places in this first round`}
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
      <span style={{ color: 'var(--peach)' }}>●</span> Founding Member · <strong>{window.PRICE}</strong>
      <span className="sticky-cta-secondary" style={{ opacity: 0.6, marginLeft: 8, fontSize: 12 }}>for 12 months</span>
    </div>
    <a href={typeof window !== 'undefined' && window.getCheckoutUrl ? window.getCheckoutUrl() : '#'} target="_blank" rel="noopener" className="sticky-cta-button"
      onClick={(e) => {
        if (window.getCheckoutUrl) e.currentTarget.href = window.getCheckoutUrl();
        if (window.trackCtaClick) window.trackCtaClick('sticky', 'Claim my place');
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
    }}>Claim my place →</a>
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
    const onKeyOnly = (e) => { if (e.key === 'Escape') setOpen(false); };
    if (!window.OFFER_END_CONFIRMED) {
      document.addEventListener('keydown', onKeyOnly);
      return () => document.removeEventListener('keydown', onKeyOnly);
    }
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

  if (!open) return null;

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

        <div style={{ fontSize: 34, marginBottom: 10 }}>✨</div>
        <SerifH size={34} style={{ lineHeight: 1.2, marginBottom: 12 }}>
          Before you go,<br /><Italic>the challenge is included free</Italic>
        </SerifH>
        <Body size={16} style={{ marginBottom: 22 }}>
          Founding Members get the 8 Week Fat Loss Challenge, starting Monday 19th October, at no extra cost,
          plus a full year of the app for {window.PRICE} instead of {window.PRICE_WAS}. This first round is
          capped at {window.SPOTS_AVAILABLE} places.
        </Body>

        {tick && (
          <div style={{ display: 'flex', gap: 10, justifyContent: 'center', marginBottom: 24 }}>
            <Box n={tick.d} l="days" />
            <Box n={tick.h} l="hrs" />
            <Box n={tick.m} l="min" />
            <Box n={tick.s} l="sec" />
          </div>
        )}

        <PrimaryCTA location="exit-intent" onClick={() => setOpen(false)} style={{ width: '100%' }}>
          Claim My Founding Member Place
        </PrimaryCTA>
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
    }}>Weight Loss &amp; Lifestyle Academy</div>
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
