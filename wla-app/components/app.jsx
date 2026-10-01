// App screenshot gallery for /wla-app.
// The four screens are the real app, shot at varying aspect ratios, so the
// frames are a fixed 4:5 with contain — cover would crop three of the four.

const APP_SCREENS = [
  { img: '/assets/app-01-daily-tracker.jpg', cap: 'Placeholder caption — daily tracker' },
  { img: '/assets/app-02-log-meal.jpg',      cap: 'Placeholder caption — log a meal' },
  { img: '/assets/app-03-meal-plan.jpg',     cap: 'Placeholder caption — weekly meal plan' },
  { img: '/assets/app-04-recipes.jpg',       cap: 'Placeholder caption — recipe library' },
];

const AppGallerySection = () => (
  <section className="app-gallery-section" style={{
    padding: '72px 32px 64px',
    background: 'var(--cream-deep)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 44 }}>
        <Eyebrow>Inside the app</Eyebrow>
        {/* ⚠️ PLACEHOLDER heading */}
        <SerifH size={48} style={{ marginTop: 18, lineHeight: 1.2 }}>
          Placeholder heading<br /><Italic>for the app gallery</Italic>
        </SerifH>
      </div>

      <div className="app-screens" style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: 18,
      }}>
        {APP_SCREENS.map((s, i) => (
          <div key={i} style={{ textAlign: 'center' }}>
            <div style={{
              aspectRatio: '4 / 5',
              borderRadius: 18,
              overflow: 'hidden',
              background: 'var(--paper)',
              border: '1px solid var(--hairline)',
              boxShadow: '0 22px 44px -26px rgba(0, 48, 96, 0.35)',
              padding: 10,
            }}>
              <img src={s.img} alt={s.cap} loading="lazy" decoding="async" style={{
                width: '100%', height: '100%', objectFit: 'contain',
                objectPosition: 'top center', display: 'block', background: '#fff',
              }} />
            </div>
            <Body size={14} style={{ marginTop: 10, fontWeight: 600, color: 'var(--ink)' }}>{s.cap}</Body>
          </div>
        ))}
      </div>
    </div>
  </section>
);

Object.assign(window, { AppGallerySection, APP_SCREENS });
