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

        <div className="problem-thoughts-grid" style={{
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

        <div className="problem-paragraphs" style={{
          maxWidth: 780,
          margin: '0 auto',
          paddingTop: 48,
          borderTop: '1px solid var(--hairline)',
          textAlign: 'center',
        }}>
          <Body size={19}>
            You’re not imagining it, perimenopause and menopause do change how your body responds to food, stress and fat storage.
          </Body>
          <Body size={19} style={{ marginTop: 18 }}>
            The approaches that used to work — eating less, skipping meals, or doing lots of cardio — start to feel harder to sustain and often leave you more hungry, more tired, and stuck in a cycle of starting and stopping.
          </Body>
        </div>
      </div>
    </section>
  );
};

// Section A: Here's What Can Change In Just 21 Days
const WhatChangesIn21DaysSection = () => {
  const changes = [
    'Drop a dress size and start seeing real changes',
    'Lose up to a stone without extreme dieting',
    'Feel back in control around food (no more all-or-nothing)',
    'Wake up feeling lighter, less bloated, and more comfortable in your clothes',
    'Have steady energy that actually lasts all day',
  ];

  return (
    <section className="whatchanges-section" style={{
      padding: '72px 32px 120px',
      background: 'var(--bg)',
    }}>
      <div style={{ maxWidth: 920, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: 56 }}>
          <Eyebrow>In just 21 days</Eyebrow>
          <SerifH size={56} style={{ marginTop: 20 }}>
            Here’s what can change<br className="mobile-break" /> <Italic>in just 21 days…</Italic>
          </SerifH>
        </div>

        <div style={{
          background: 'var(--paper)',
          border: '1px solid var(--hairline)',
          borderRadius: 18,
          overflow: 'hidden',
          boxShadow: '0 20px 40px -28px rgba(0, 48, 96, 0.2)',
        }}>
          {changes.map((c, i) => (
            <div key={i} style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 10,
              padding: '26px 32px',
              borderBottom: i < changes.length - 1 ? '1px solid var(--hairline)' : 'none',
              textAlign: 'center',
            }}>
              <div style={{
                fontFamily: '"Libre Baskerville", serif',
                fontStyle: 'italic',
                fontSize: 22,
                color: 'var(--blush-deep)',
                lineHeight: 1,
              }}>
                {String(i + 1).padStart(2, '0')}
              </div>
              <Body size={18} style={{ lineHeight: 1.5, maxWidth: 540 }}>{c}</Body>
            </div>
          ))}
        </div>

        <div style={{ marginTop: 48, textAlign: 'center' }}>
          <div className="mobile-no-italic" style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 20,
            color: 'var(--ink)',
            marginBottom: 8,
            lineHeight: 1.5,
          }}>
            This isn’t about being perfect…
          </div>
          <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 24,
            color: 'var(--blush-deep)',
            lineHeight: 1.4,
          }}>
            It’s about finally building momentum that lasts.
          </div>
        </div>
      </div>
    </section>
  );
};

// Section B: The Honest Truth — standalone navy section
const HonestTruthSection = () => (
  <section style={{
    padding: '120px 32px',
    background: 'var(--ink)',
    color: 'var(--paper)',
  }}>
    <div style={{ maxWidth: 820, margin: '0 auto', textAlign: 'center' }}>
      <Eyebrow color="#F79F83">The honest truth…</Eyebrow>
      <SerifH size={56} style={{ color: 'var(--paper)', marginTop: 20, marginBottom: 28 }}>
        You don’t struggle because you <Italic>don’t know what to do.</Italic>
      </SerifH>

      <div className="mobile-no-italic" style={{
        fontFamily: '"Libre Baskerville", serif',
        fontStyle: 'italic',
        fontSize: 26,
        lineHeight: 1.4,
        color: 'var(--paper)',
        marginBottom: 48,
      }}>
        And it’s not because you lack willpower.
      </div>

      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        gap: 16, marginBottom: 64,
      }}>
        <span style={{ flex: '0 0 40px', height: 1, background: '#F79F83', opacity: 0.45 }} />
        <div style={{
          fontFamily: '"Libre Baskerville", serif',
          fontStyle: 'italic',
          fontSize: 28,
          color: '#F79F83',
          lineHeight: 1.35,
          maxWidth: 600,
        }}>
          You’ve just never had a plan you can actually stick to.
        </div>
        <span style={{ flex: '0 0 40px', height: 1, background: '#F79F83', opacity: 0.45 }} />
      </div>

      <div style={{
        background: 'var(--peach)',
        borderRadius: 16,
        padding: '40px 40px 32px',
        marginBottom: 56,
        boxShadow: '0 30px 60px -24px rgba(232, 127, 99, 0.35)',
      }}>
        <div style={{
          fontFamily: '"Alegreya Sans", sans-serif',
          fontSize: 12, letterSpacing: '0.22em', textTransform: 'uppercase',
          color: 'var(--blush-deep)', marginBottom: 26, fontWeight: 600,
        }}>
          Most diets rely on
        </div>
        {['Being perfect', 'Cutting everything out', 'Motivation that doesn’t last'].map((item, i) => (
          <div key={i} style={{
            padding: '18px 0',
            borderBottom: i < 2 ? '1px solid rgba(0, 48, 96, 0.15)' : 'none',
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 22,
            color: 'var(--ink)',
            lineHeight: 1.4,
          }}>
            {item}
          </div>
        ))}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginBottom: 64 }}>
        {['So you start strong…', 'Then life gets busy…', 'And you fall back into the same cycle.'].map((line, i) => (
          <div key={i} className="mobile-no-italic" style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 19,
            color: 'var(--paper)',
            opacity: 0.8,
            lineHeight: 1.5,
          }}>
            {line}
          </div>
        ))}
      </div>

      <div style={{
        fontFamily: '"Libre Baskerville", serif',
        fontSize: 28,
        fontStyle: 'italic',
        color: '#F79F83',
        lineHeight: 1.4,
      }}>
        That’s not your fault.<br />
        It’s the <strong style={{ fontWeight: 700 }}>approach</strong> that’s been wrong.
      </div>
    </div>
  </section>
);

// Section C: Why This Reset Works When Others Haven't
const WhyThisResetWorksSection = () => (
  <section className="whythisworks-section" style={{
    padding: '120px 32px 64px',
    background: 'var(--bg)',
  }}>
    <div style={{ maxWidth: 980, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 56 }}>
        <Eyebrow>The difference</Eyebrow>
        <SerifH size={54} style={{ marginTop: 20 }}>
          Why this reset works <Italic>when others haven’t</Italic>
        </SerifH>
      </div>

      <div style={{ textAlign: 'center', marginBottom: 40, maxWidth: 720, margin: '0 auto 40px' }}>
        <Body size={17} style={{ marginBottom: 16 }}>
          Instead of extremes, this Reset focuses on one thing:
        </Body>
        <div style={{
          fontFamily: '"Libre Baskerville", serif',
          fontSize: 28, fontStyle: 'italic',
          color: 'var(--blush-deep)', lineHeight: 1.3,
          marginBottom: 36,
        }}>
          Helping you fuel your body properly for fat loss.
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(2, 1fr)',
          gap: 18,
          maxWidth: 640, margin: '0 auto',
          textAlign: 'left',
        }}>
          {[
            'Stay full and satisfied',
            'Reduce cravings naturally',
            'Have more energy throughout the day',
            'Actually stick to it',
          ].map((item, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start' }}>
              <Tick />
              <Body size={17}>{item}</Body>
            </div>
          ))}
        </div>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(3, 1fr)',
        gap: 16,
        marginBottom: 56,
      }}>
        {['No cutting everything out.', 'No 1,200 calorie plans.', 'No starting again next week.'].map((item, i) => (
          <div key={i} style={{
            background: 'var(--cream-deep)',
            borderRadius: 10,
            padding: '22px 22px',
            textAlign: 'center',
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 16,
            color: 'var(--ink)',
            lineHeight: 1.4,
          }}>
            {item}
          </div>
        ))}
      </div>

      <div style={{ textAlign: 'center', maxWidth: 680, margin: '0 auto' }}>
        <SerifH size={36} style={{ lineHeight: 1.3 }}>
          Just a <Italic>simple structure</Italic> that works in real life.
        </SerifH>
      </div>
    </div>
  </section>
);

// WLA Reset Method
const SHIFT_STEPS = [
  {
    letter: '1',
    word: 'Stabilise',
    title: <>Stabilising blood sugar: <strong style={{ fontWeight: 700 }}>stops cravings</strong></>,
    body: 'Protein-forward meals that end the 4pm crash and the evening snacking. When blood sugar steadies, cravings quiet down, usually within 3–4 days.',
  },
  {
    letter: '2',
    word: 'Structure',
    title: <>Structuring meals properly: <strong style={{ fontWeight: 700 }}>no overeating</strong></>,
    body: 'The right balance of protein, fibre and smart carbs on the plate, at the right times. You finish meals satisfied, not hungry an hour later.',
  },
  {
    letter: '3',
    word: 'Simplify',
    title: <>Simple daily habits: <strong style={{ fontWeight: 700 }}>results without thinking</strong></>,
    body: 'Small, repeatable routines that run in the background of a busy life. No tracking, no willpower battles, just habits that quietly do the work for you.',
  },
];

const MethodSection = () => (
  <section id="method" style={{
    padding: '72px 32px 60px',
    background: 'var(--bg)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 72 }}>
        <Eyebrow>The WLA Reset Method</Eyebrow>
        <SerifH size={62} style={{ marginTop: 20, marginBottom: 20, maxWidth: 840, marginInline: 'auto' }}>
          Three simple principles. <Italic>Designed to help you get results now.</Italic>
        </SerifH>
        <Body size={18} style={{ maxWidth: 620, margin: '0 auto' }}>
          Evidence-based. Built around real life, not recycled from outdated weight-loss advice.
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
              <Body size={16} style={{ maxWidth: 540 }}>{s.body}</Body>
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

// Section D: Here's What Happens When You Follow The Reset
const WhatHappensSection = () => {
  const outcomes = [
    'Follow a simple, proven formula used by 50,000+ women',
    'Reduce cravings and feel in control without cutting everything out',
    'Feel lighter, less bloated, and more energised within days',
    'Know exactly what to eat with flexible, family-friendly meals',
    'Stay on track even on busy days with quick, easy options',
    'Boost your energy and mood through simple daily habits',
    'Track progress properly without obsessing over the scales',
  ];

  return (
    <section className="whathappens-section" style={{
      padding: '64px 32px 120px',
      background: 'var(--bg)',
    }}>
      <div style={{ maxWidth: 960, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: 56 }}>
          <Eyebrow>What happens next</Eyebrow>
          <SerifH size={52} style={{ marginTop: 20 }}>
            Here’s what happens when <Italic>you follow the Reset</Italic>
          </SerifH>
        </div>

        <div style={{
          background: 'var(--paper)',
          border: '1px solid var(--hairline)',
          borderRadius: 18,
          overflow: 'hidden',
          maxWidth: 780,
          margin: '0 auto',
          boxShadow: '0 20px 40px -28px rgba(0, 48, 96, 0.2)',
        }}>
          {outcomes.map((o, i) => (
            <div key={i} style={{
              display: 'flex',
              gap: 16,
              alignItems: 'center',
              padding: '20px 32px',
              borderBottom: i < outcomes.length - 1 ? '1px solid var(--hairline)' : 'none',
            }}>
              <Tick />
              <Body size={17} style={{ lineHeight: 1.5, flex: 1, minWidth: 0 }}>{o}</Body>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

Object.assign(window, {
  ProblemSection, MethodSection, TransformSection,
  WhatChangesIn21DaysSection, HonestTruthSection, WhyThisResetWorksSection, WhatHappensSection,
});
