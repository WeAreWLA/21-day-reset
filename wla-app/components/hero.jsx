// Announcement bar — WLA App (/wla-app)

// Ticks once a second so the bar always shows live time remaining.
function useOfferRemaining() {
  const compute = () => {
    const diff = Math.max(0, window.OFFER_END - Date.now());
    return {
      expired: diff <= 0,
      d: Math.floor(diff / 86400000),
      h: Math.floor((diff % 86400000) / 3600000),
      m: Math.floor((diff % 3600000) / 60000),
      s: Math.floor((diff % 60000) / 1000),
    };
  };
  const [t, setT] = React.useState(compute);
  React.useEffect(() => {
    const id = setInterval(() => setT(compute()), 1000);
    return () => clearInterval(id);
  }, []);
  return t;
}

const BarDigit = ({ n, label }) => (
  <span style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center', lineHeight: 1 }}>
    <span style={{
      background: 'rgba(253, 251, 248, 0.16)',
      border: '1px solid rgba(245, 217, 206, 0.45)',
      borderRadius: 6,
      padding: '3px 6px',
      minWidth: 26,
      textAlign: 'center',
      fontFamily: '"Alegreya Sans", sans-serif',
      fontWeight: 700,
      fontSize: 15,
      fontVariantNumeric: 'tabular-nums',
      color: 'var(--paper)',
    }}>{String(n).padStart(2, '0')}</span>
    <span style={{
      fontSize: 8,
      letterSpacing: '0.12em',
      textTransform: 'uppercase',
      color: 'var(--peach)',
      marginTop: 3,
    }}>{label}</span>
  </span>
);

// The countdown only runs once a real closing date is set (OFFER_END_CONFIRMED
// in sections.jsx). Until then the bar carries the places message instead of a
// deadline nobody has committed to.
const AnnouncementBar = () => {
  const phase = (typeof window !== 'undefined' && window.getCampaignPhase) ? window.getCampaignPhase() : 'open';
  const isOpen = phase === 'open';
  const timed = !!window.OFFER_END_CONFIRMED;
  const t = useOfferRemaining();
  return (
    <div className="announcement-bar" style={{ color: 'var(--paper)' }}>
      <div className="announcement-inner" style={{
        maxWidth: 1240,
        margin: '0 auto',
        fontFamily: '"Alegreya Sans", sans-serif',
        textAlign: 'left',
        letterSpacing: '0.04em',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'flex-start',
        gap: 14,
        flexWrap: 'wrap',
      }}>
        {timed && isOpen ? (
          <span className="announcement-timer" style={{ display: 'inline-flex', alignItems: 'center', gap: 10 }}>
            <span style={{ fontSize: 13 }}>Your exclusive early-access window ends in</span>
            <span style={{ display: 'inline-flex', alignItems: 'flex-start', gap: 4 }}>
              <BarDigit n={t.d} label="days" />
              <BarDigit n={t.h} label="hrs" />
              <BarDigit n={t.m} label="min" />
              <BarDigit n={t.s} label="sec" />
            </span>
          </span>
        ) : isOpen ? (
          <span style={{ fontSize: 13 }}>
            Founding Member launch &middot; Only {window.SPOTS_AVAILABLE} places &middot; 8 Week Fat Loss Challenge included free
          </span>
        ) : (
          <span style={{ fontSize: 13 }}>
            Founding Member pricing has closed &middot; The WLA App is now {window.PRICE_WAS} a year
          </span>
        )}
      </div>
    </div>
  );
};

Object.assign(window, { AnnouncementBar });
