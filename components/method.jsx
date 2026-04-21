// Problem agitation + SHIFT method sections

const ProblemSection = () => {
  const thoughts = [
    '"Nothing works anymore."',
    '"I\'m eating less and still gaining."',
    '"Is this just menopause now?"',
    '"I don\'t recognise my body."',
    '"I\'ve tried everything."',
    '"I just want to feel like me."',
  ];

  return (
    <section style={{
      background: 'var(--cream-deep)',
      padding: '110px 32px',
    }}>
      <div style={{ maxWidth: 1100, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', maxWidth: 780, margin: '0 auto 64px' }}>
          <Eyebrow>If this sounds familiar</Eyebrow>
          <SerifH size={56} style={{ marginTop: 20 }}>
            You used to know how your body worked.
            <br />
            <Italic>And then, somewhere around 48, it changed.</Italic>
          </SerifH>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 16,
          marginBottom: 56,
        }}>
          {thoughts.map((t, i) => (
            <div key={i} style={{
              padding: '22px 26px',
              background: 'var(--paper)',
              borderRadius: 10,
              border: '1px solid var(--hairline)',
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              fontSize: 17,
              color: 'var(--ink)',
              lineHeight: 1.4,
              transform: `rotate(${(i % 2 === 0 ? -0.6 : 0.6)}deg)`,
            }}>
              {t}
            </div>
          ))}
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: 80,
          alignItems: 'start',
          padding: '48px 0 0',
          borderTop: '1px solid var(--hairline)',
        }}>
          <div>
            <Body size={19}>
              You’re not imagining it, perimenopause and menopause do change how your body responds to food, stress, and fat storage
            </Body>
            <Body size={19} muted style={{ marginTop: 18 }}>
              The approaches that used to work, like eating less, skipping meals, or doing lots of cardio can start to feel harder to sustain and often leave you feeling more hungry, more tired, and stuck in a cycle of starting and stopping
            </Body>
          </div>
          <div style={{
            background: 'var(--paper)',
            padding: '32px 36px',
            borderRadius: 14,
            border: '1px solid var(--hairline)',
          }}>
            <div style={{
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              fontSize: 13,
              color: 'var(--blush-deep)',
              letterSpacing: '0.04em',
              marginBottom: 10,
            }}>The honest truth</div>
            <Body size={18} style={{ lineHeight: 1.55 }}>
              You don't need more discipline.
              You don't need to try harder.
              You need a <strong style={{ color: 'var(--blush-deep)' }}>plan designed for the body you have now</strong>, not the one you had at 32.
            </Body>
          </div>
        </div>
      </div>
    </section>
  );
};

// WLA Reset Method
const SHIFT_STEPS = [
  {
    letter: '1',
    word: 'Stabilise',
    title: 'Stabilising blood sugar: stops cravings',
    body: 'Protein-forward meals that end the 4pm crash and the evening snacking. When blood sugar steadies, cravings quiet down, usually within 3–4 days.',
  },
  {
    letter: '2',
    word: 'Structure',
    title: 'Structuring meals properly: no overeating',
    body: 'The right balance of protein, fibre and smart carbs on the plate, at the right times. You finish meals satisfied, not hungry an hour later.',
  },
  {
    letter: '3',
    word: 'Simplify',
    title: 'Simple daily habits: results without thinking',
    body: 'Small, repeatable routines that run in the background of a busy life. No tracking, no willpower battles, just habits that quietly do the work for you.',
  },
];

const MethodSection = () => (
  <section id="method" style={{
    padding: '130px 32px 110px',
    background: 'var(--bg)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 72 }}>
        <Eyebrow>The WLA Reset Method</Eyebrow>
        <SerifH size={62} style={{ marginTop: 20, marginBottom: 20, maxWidth: 840, marginInline: 'auto' }}>
          Three simple principles. <Italic>Built for the body you have now.</Italic>
        </SerifH>
        <Body size={18} muted style={{ maxWidth: 620, margin: '0 auto' }}>
          Evidence-based. Designed around the physiology of women 45+, not recycled from a 2010 weight-loss book.
        </Body>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
        {SHIFT_STEPS.map((s, i) => (
          <div key={i} style={{
            display: 'grid',
            gridTemplateColumns: '120px 1fr 2fr',
            gap: 48,
            padding: '36px 0',
            borderTop: '1px solid var(--hairline)',
            borderBottom: i === SHIFT_STEPS.length - 1 ? '1px solid var(--hairline)' : 'none',
            alignItems: 'baseline',
          }}>
            <div style={{
              fontFamily: '"Libre Baskerville", serif',
              fontWeight: 700,
              fontSize: 92,
              color: 'var(--blush-deep)',
              lineHeight: 0.85,
              letterSpacing: '-0.04em',
            }}>
              {s.letter}
            </div>
            <div>
              <div style={{
                fontFamily: '"Alegreya Sans", sans-serif',
                fontSize: 11,
                letterSpacing: '0.18em',
                color: 'var(--ink-muted)',
                textTransform: 'uppercase',
                marginBottom: 8,
              }}>Step {i + 1}</div>
              <SerifH size={30} style={{ lineHeight: 1.1 }}>{s.word}</SerifH>
            </div>
            <div>
              <Body size={18} style={{ marginBottom: 8, fontWeight: 500 }}>{s.title}</Body>
              <Body size={16} muted style={{ maxWidth: 540 }}>{s.body}</Body>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

// Transformation: Before / After (not bodies — mindset/lifestyle)
const TransformSection = () => {
  const before = [
    'Cutting calories lower and lower',
    'Ravenous and snacky by 6pm',
    'Blaming yourself when you "fall off"',
    'Starting over every Monday',
    'Afraid to eat bread',
    'The scale dictates your mood',
  ];
  const after = [
    'Eating enough to actually feel full',
    'Steady energy from breakfast to bed',
    'Understanding why your body changed',
    'One plan. You finish it.',
    'Carbs back on the table, strategically',
    'Measuring what actually matters',
  ];

  return (
    <section style={{
      padding: '100px 32px',
      background: 'var(--cream-deep)',
    }}>
      <div style={{ maxWidth: 1100, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: 56 }}>
          <Eyebrow>What changes in 21 days</Eyebrow>
          <SerifH size={52} style={{ marginTop: 20 }}>
            From <Italic>stuck</Italic> to finally in control.
          </SerifH>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: 4,
          background: 'var(--hairline)',
          border: '1px solid var(--hairline)',
          borderRadius: 18,
          overflow: 'hidden',
        }}>
          <div style={{ background: 'var(--paper)', padding: 40 }}>
            <div style={{
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              fontSize: 14,
              color: 'var(--ink-muted)',
              marginBottom: 18,
              letterSpacing: '0.04em',
            }}>Where most women are stuck</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              {before.map((b, i) => (
                <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
                  <Cross />
                  <Body size={17} muted>{b}</Body>
                </div>
              ))}
            </div>
          </div>
          <div style={{ background: 'var(--paper)', padding: 40 }}>
            <div style={{
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              fontSize: 14,
              color: 'var(--blush-deep)',
              marginBottom: 18,
              letterSpacing: '0.04em',
            }}>What the Reset gives you</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              {after.map((a, i) => (
                <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
                  <Tick />
                  <Body size={17}>{a}</Body>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

Object.assign(window, { ProblemSection, MethodSection, TransformSection });
