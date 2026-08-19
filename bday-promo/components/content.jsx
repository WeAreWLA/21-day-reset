// Included, testimonials, about, pricing, FAQ

// Line icons for the "What's inside" grid. Single stroke weight, brand navy,
// so they read as one set rather than clip-art.
const IncludedIcon = ({ name }) => {
  const paths = {
    // fork + knife
    plate: <><path d="M6 3v7a2.5 2.5 0 0 0 5 0V3M8.5 3v6M8.5 12.5V21" /><path d="M17.5 21V3c-1.8 1-2.8 3-2.8 5.5s1 3.5 2.8 3.5" /></>,
    chat: <><path d="M20 14.5a2 2 0 0 1-2 2H8l-4 3.5v-14a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2z" /><path d="M8.5 9.5h7M8.5 12.5h4.5" /></>,
    video: <><rect x="2.5" y="6" width="12.5" height="12" rx="2" /><path d="M15 11l6-3.5v9L15 13z" /></>,
    // spiral notebook
    book: <><rect x="5.5" y="3.5" width="14" height="17" rx="2" /><path d="M9.5 3.5v17" /><path d="M12.5 8.5h4M12.5 12h4M12.5 15.5h2.5" /></>,
    swap: <><path d="M4 8.5h13l-3.5-3.5" /><path d="M20 15.5H7l3.5 3.5" /></>,
    // water droplet
    drink: <><path d="M12 3.2c3.4 4 5.5 6.6 5.5 9.3a5.5 5.5 0 0 1-11 0c0-2.7 2.1-5.3 5.5-9.3z" /><path d="M9.5 13.5a2.5 2.5 0 0 0 2.5 2.5" /></>,
    snow: <><path d="M12 3v18M4.2 7.5l15.6 9M19.8 7.5l-15.6 9" /><path d="M12 6.6l-2 -2M12 6.6l2 -2M12 17.4l-2 2M12 17.4l2 2" /></>,
    list: <><path d="M9 6.5h11M9 12h11M9 17.5h11" /><path d="M3.8 6.3l1.2 1.2 2-2.4M3.8 11.8l1.2 1.2 2-2.4M3.8 17.3l1.2 1.2 2-2.4" /></>,
  };
  return (
    <svg width="30" height="30" viewBox="0 0 24 24" fill="none"
      stroke="var(--blush-deep)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"
      aria-hidden="true" style={{ flexShrink: 0 }}>
      {paths[name]}
    </svg>
  );
};

const INCLUDED = [
  {
    title: '21-Day Flexible Meal Guide',
    icon: 'plate',
    body: 'Weight loss breakfasts, lunches and dinners flexible meal guides. Family-friendly. Designed to keep you full, satisfied, on track and lighter within days.',
    tag: 'Core',
  },
  {
    title: 'Daily Coaching & Check-ins',
    icon: 'chat',
    body: 'Guidance inside the reset group each day so you stay on track, without feeling like you\'re doing it alone. Stay consistent and motivated every step of the way.',
    tag: 'Core',
  },
  {
    title: 'Weekly Live Zoom Coaching',
    icon: 'video',
    body: 'Live sessions with Anna every week. Ask questions, hear what\'s working for women like you.',
    tag: 'Live',
  },
  {
    title: 'Reset Workbook',
    icon: 'book',
    body: 'Set clear goals, stay focused, and track your progress each week, so you actually follow through and see results.',
    tag: 'Core',
  },
  {
    title: 'Snack & Food Swap Guides',
    icon: 'swap',
    body: 'Zero-prep options, smart swaps, and snack ideas that satisfy without derailing progress.',
    tag: 'Reference',
  },
  {
    title: 'Drinks & Hydration Guide',
    icon: 'drink',
    body: 'What to drink, what to swap, how alcohol fits, and how to stay hydrated in a way that actually supports fat loss.',
    tag: 'Reference',
  },
  {
    title: 'Easy Freezer Dinner Pack',
    icon: 'snow',
    body: 'No-cook meals you can have ready without effort, perfect for busy days when you don\'t want to think about what to eat.',
    tag: 'Bonus',
  },
  {
    title: 'No-Prep Food List',
    icon: 'list',
    body: 'Grab-and-go foods that keep you on track even on your busiest or lowest-energy days.',
    tag: 'Reference',
  },
];

const IncludedSection = () => (
  <section id="included" className="included-section" style={{
    padding: '40px 32px 40px',
    background: 'var(--bg)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.2fr', gap: 80, alignItems: 'end', marginBottom: 56 }}>
        <div>
          <Eyebrow>What's inside</Eyebrow>
          <SerifH size={58} style={{ marginTop: 20 }}>
            Everything you need.<br /><Italic>Nothing you don't.</Italic>
          </SerifH>
        </div>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: 1,
        background: 'var(--hairline)',
        border: '1px solid var(--hairline)',
        borderRadius: 16,
        overflow: 'hidden',
      }}>
        {INCLUDED.map((item, i) => (
          <div key={i} style={{
            background: 'var(--paper)',
            padding: '32px 28px',
            minHeight: 220,
            display: 'flex',
            flexDirection: 'column',
            gap: 10,
          }}>
            <IncludedIcon name={item.icon} />
            <SerifH size={22} style={{ lineHeight: 1.2 }}>{item.title}</SerifH>
            <Body size={14} muted style={{ marginTop: 'auto' }}>{item.body}</Body>
          </div>
        ))}
      </div>

      {/* Birthday bonuses */}
      <MembersAreaBlock />
      <MasterclassesBlock />

    </div>
  </section>
);

// ---------------------------------------------------------------------------
// WLA Members' Area — birthday bonus block inside "What's included".
// Recipe photos live in /assets. If a file is missing the tile degrades to a
// soft peach card with the dish name rather than a broken-image icon.
// ---------------------------------------------------------------------------
const MEMBERS_RECIPES = [
  { img: '/assets/members-recipe-01.jpg', name: 'Steak fajita wrap' },
  { img: '/assets/members-recipe-02.jpg', name: 'Strawberry overnight oats' },
  { img: '/assets/members-recipe-03.jpg', name: 'Creamy chicken & broccoli pasta' },
  { img: '/assets/members-recipe-04.jpg', name: 'Raspberry baked oat muffins' },
  { img: '/assets/members-recipe-05.jpg', name: 'Cheeseburger gnocchi' },
];

const MEMBERS_PERKS = [
  'Hundreds of healthy, family-friendly weight loss recipes',
  '100’s of extra weekly meal guides',
  'Done-for-you shopping lists',
  'Nutrition and weight-loss tools',
  'Easy ideas for breakfasts, lunches, dinners and snacks',
];

const MASTERCLASSES = [
  {
    title: 'Your 21-Day Weight-Loss Roadmap',
    body: 'Set your goal and create your personal plan.',
  },
  {
    title: 'Eat for Better Weight-Loss Results',
    body: 'Build satisfying meals that support fat loss.',
  },
  {
    title: 'Five Habits of Consistent Weight Loss',
    body: 'Discover the secret strategies that Anna’s 1-2-1 clients use to lose up to 2 stone.',
  },
];

const RecipeTile = ({ item }) => {
  const [failed, setFailed] = React.useState(false);
  return (
    <div style={{
      aspectRatio: '1/1',
      borderRadius: 12,
      overflow: 'hidden',
      background: 'var(--peach)',
      border: '1px solid var(--hairline)',
      position: 'relative',
    }}>
      {!failed && (
        <img
          src={item.img}
          alt={item.name}
          loading="lazy"
          decoding="async"
          onError={() => setFailed(true)}
          style={{ width: '100%', height: '100%', objectFit: 'cover', display: 'block' }}
        />
      )}
      {failed && (
        <div style={{
          position: 'absolute', inset: 0,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          padding: 14, textAlign: 'center',
          fontFamily: '"Libre Baskerville", serif',
          fontStyle: 'italic',
          fontSize: 14,
          color: 'var(--ink)',
          lineHeight: 1.4,
        }}>
          {item.name}
        </div>
      )}
    </div>
  );
};

// Shared shell so both bonuses read as a matched pair.
const BonusCard = ({ number, label, title, lead, children }) => (
  <div className="bonus-card" style={{
    background: `linear-gradient(135deg, var(--peach) 0%, #F8C4B0 100%)`,
    border: '2px dashed var(--blush-deep)',
    borderRadius: 22,
    padding: '46px 44px 40px',
    position: 'relative',
    boxShadow: '0 30px 60px -30px rgba(232, 127, 99, 0.35)',
  }}>
    <div style={{
      position: 'absolute',
      top: -16, left: '50%', transform: 'translateX(-50%)',
      background: 'var(--blush-deep)', color: 'var(--paper)',
      padding: '8px 22px', borderRadius: 999,
      fontFamily: '"Alegreya Sans", sans-serif',
      fontSize: 12, fontWeight: 600,
      letterSpacing: '0.16em', textTransform: 'uppercase',
      whiteSpace: 'nowrap',
    }}>
      🎂 Bonus {number} · {label}
    </div>

    <div style={{ textAlign: 'center', marginTop: 10, marginBottom: 28 }}>
      <SerifH size={38} style={{ lineHeight: 1.2, marginBottom: lead ? 14 : 0 }}>
        {title}
      </SerifH>
      {lead && (
        <Body size={17} style={{ maxWidth: 640, margin: '0 auto' }}>{lead}</Body>
      )}
    </div>

    {children}
  </div>
);

// Bonus 1 — WLA Members' Area
const MembersAreaBlock = () => (
  <div className="members-area-block" style={{ marginTop: 34 }}>
    <BonusCard
      number={1}
      label="Members’ Area"
      title={<>Instant access to the<br /><Italic>WLA Members’ Area</Italic></>}
      lead="Immediate access throughout the Reset. Everything in one place, from the moment you join."
    >
      <div className="members-recipe-grid" style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(5, 1fr)',
        gap: 12,
        marginBottom: 28,
      }}>
        {MEMBERS_RECIPES.map((item, i) => <RecipeTile key={i} item={item} />)}
      </div>

      <div className="members-perks" style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(2, 1fr)',
        gap: 10,
        maxWidth: 820,
        margin: '0 auto 24px',
      }}>
        {MEMBERS_PERKS.map((perk, i) => (
          <div key={i} style={{
            // A trailing odd item spans both columns and centres, rather than
            // hanging on the left with a gap beside it.
            ...(i === MEMBERS_PERKS.length - 1 && MEMBERS_PERKS.length % 2
              ? { gridColumn: '1 / -1', justifySelf: 'center', maxWidth: 420, width: '100%' }
              : null),
            display: 'flex', gap: 12, alignItems: 'flex-start',
            background: 'rgba(253, 251, 248, 0.7)',
            border: '1px solid rgba(232, 127, 99, 0.35)',
            borderRadius: 10,
            padding: '12px 16px',
          }}>
            <span style={{ color: 'var(--blush-deep)', fontSize: 15, lineHeight: 1.55, flexShrink: 0 }}>✦</span>
            <Body size={15} style={{ flex: 1, minWidth: 0 }}>{perk}</Body>
          </div>
        ))}
      </div>

      <div style={{
        fontFamily: '"Libre Baskerville", serif',
        fontStyle: 'italic',
        fontSize: 17,
        color: 'var(--ink)',
        textAlign: 'center',
        maxWidth: 700,
        margin: '0 auto',
        lineHeight: 1.5,
      }}>
        So whenever you need fresh inspiration, a quick dinner or help getting back on track,
        you’ll have everything available in one place.
      </div>
    </BonusCard>
  </div>
);

// Bonus 2 — Three weekly live masterclasses
const MasterclassesBlock = () => (
  <div className="masterclasses-block" style={{ marginTop: 40 }}>
    <BonusCard
      number={2}
      label="Masterclasses"
      title={<>Three Weekly<br /><Italic>Weight-Loss Masterclasses</Italic></>}
    >
      <div className="masterclass-grid" style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(3, 1fr)',
        gap: 14,
      }}>
        {MASTERCLASSES.map((m, i) => (
          <div key={i} style={{
            background: 'rgba(253, 251, 248, 0.8)',
            border: '1px solid rgba(232, 127, 99, 0.4)',
            borderRadius: 14,
            padding: '24px 22px 22px',
            display: 'flex',
            flexDirection: 'column',
            gap: 10,
          }}>
            <div style={{
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              fontSize: 14,
              color: 'var(--blush-deep)',
              letterSpacing: '0.04em',
            }}>Week {i + 1}</div>
            <SerifH size={20} style={{ lineHeight: 1.25 }}>{m.title}</SerifH>
            <Body size={15} style={{ marginTop: 'auto' }}>{m.body}</Body>
          </div>
        ))}
      </div>
    </BonusCard>
  </div>
);

// Testimonials// Testimonials
const TESTIMONIALS = [
  {
    quote: "I lost 12 pounds, sugar cravings vanished and my menopause symptoms significantly improved.",
    name: 'Ruth',
    age: 54,
    result: '12 lbs down · 21 days',
  },
  {
    quote: "Since starting I've lost 2 stone. Within 2 weeks my skin cleared up and I felt so different.",
    name: 'Laura',
    age: 52,
    result: '2 stone · skin cleared',
  },
  {
    quote: "I have lost 2 stone, dropped 1–2 dress sizes, but most importantly, I understand and enjoy food in a way that is positive and healthy.",
    name: 'Tara',
    age: 49,
    result: 'Dropped 1–2 dress sizes',
  },
  {
    quote: "I started a size 20 and am now a 10/12. Not counted a calorie in over a year.",
    name: 'Vicky',
    age: 56,
    result: 'Size 20 → 10/12',
  },
  {
    quote: "I'm the slimmest I have been since I got married 16 years ago.",
    name: 'Lisa',
    age: 51,
    result: 'Slimmest in 16 years',
  },
  {
    quote: "I've become more confident in myself and finally I'm at my happy place. It's been an incredible journey.",
    name: 'Barbara',
    age: 58,
    result: 'Confident again',
  },
];

const TestimonialsSection = () => (
  <section id="testimonials" style={{
    padding: '120px 32px',
    background: 'var(--ink)',
    color: 'var(--paper)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 80 }}>
        <Eyebrow color="var(--peach)">Real women · real results</Eyebrow>
        <SerifH size={62} style={{ color: 'var(--paper)', marginTop: 20 }}>
          50,000 women. <Italic>One reset.</Italic>
        </SerifH>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(3, 1fr)',
        gap: 24,
      }}>
        {TESTIMONIALS.map((t, i) => (
          <div key={i} style={{
            background: '#F9F7F4',
            padding: 32,
            borderRadius: 14,
            border: '1px solid var(--hairline)',
            display: 'flex',
            flexDirection: 'column',
            gap: 18,
          }}>
            <QuoteMark color="#F79F83" size={28} />
            <Body size={17} style={{
              color: '#333333',
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              lineHeight: 1.5,
              flex: 1,
            }}>
              {t.quote}
            </Body>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: 14,
              paddingTop: 16,
              borderTop: '1px solid var(--hairline)',
            }}>
              <div style={{
                width: 40,
                height: 40,
                borderRadius: '50%',
                background: '#F79F83',
                flexShrink: 0,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontFamily: '"Libre Baskerville", serif',
                fontWeight: 700,
              fontSize: 16,
                color: '#F9F7F4',
              }}>
                {t.name[0]}
              </div>
              <div style={{ flex: 1 }}>
                <div style={{
                  fontFamily: '"Libre Baskerville", serif',
                  fontWeight: 700,
              fontSize: 17,
                  color: '#333333',
                }}>{t.name}, {t.age}</div>
                <div style={{
                  fontFamily: '"Alegreya Sans", sans-serif',
                  fontSize: 12,
                  color: '#E87F63',
                  letterSpacing: '0.02em',
                }}>{t.result}</div>
              </div>
            </div>
          </div>
        ))}
      </div>

    </div>
  </section>
);

// Before/after photo wall — sits directly under the hero so results land first.
const RESULTS_PHOTOS = [
  { name: 'VICKY, 56', img: '/assets/vicky-before-after.png' },
  { name: 'LAURA, 52', img: '/assets/jill-before-after.jpg' },
  { name: 'RUTH, 54', img: '/assets/ruth-before-after.jpg' },
  { name: 'BARBARA, 58', img: '/assets/barbara-before-after.png' },
  { name: 'MEMBER, 5', img: '/assets/member-05-before-after.png' },
  { name: 'MEMBER, 6', img: '/assets/member-06-before-after.png' },
  { name: 'MEMBER, 7', img: '/assets/member-07-before-after.png', fit: 'cover', pos: 'center 25%' },
  { name: 'MEMBER, 8', img: '/assets/member-08-before-after.jpeg' },
  { name: 'MEMBER, 9', img: '/assets/member-09-before-after.png', fit: 'cover', pos: 'center 25%' },
  { name: 'MEMBER, 10', img: '/assets/member-10-before-after.png', fit: 'cover' },
  { name: 'MEMBER, 11', img: '/assets/member-11-before-after.png', fit: 'cover', pos: 'center 25%' },
  { name: 'MEMBER, 12', img: '/assets/member-12-before-after.png' },
];

const ResultsGridSection = () => (
  <section id="results" className="results-grid-section" style={{
    padding: '72px 32px 80px',
    background: 'var(--ink)',
    color: 'var(--paper)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 40 }}>
        <SerifH size={44} style={{ color: 'var(--paper)', lineHeight: 1.2 }}>
          Real results from women <em style={{ fontStyle: 'italic', fontWeight: 400, color: 'var(--peach)' }}>just like you</em>
        </SerifH>
      </div>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: 16,
      }}>
        {RESULTS_PHOTOS.map((item, i) => (
          <div key={i}>
            <div style={{
              aspectRatio: '1/1',
              borderRadius: 4,
              overflow: 'hidden',
              background: '#F9F7F4',
            }}>
              <img src={item.img} alt={`Before and after of ${item.name}`} loading="lazy" decoding="async" style={{
                width: '100%', height: '100%', objectFit: item.fit || 'contain', objectPosition: item.pos || 'center center', display: 'block',
              }} />
            </div>
          </div>
        ))}
      </div>
      <div style={{
        textAlign: 'center',
        marginTop: 32,
        fontFamily: '"Alegreya Sans", sans-serif',
        fontSize: 12,
        color: '#ffffff',
        letterSpacing: '0.04em',
        opacity: 0.8,
      }}>
        *Results vary depending on the individual. There is no guarantee of specific results.
      </div>
    </div>
  </section>
);

// About Anna
const AboutSection = () => (
  <section style={{
    padding: '130px 32px',
    background: 'var(--bg)',
  }}>
    <div style={{
      maxWidth: 1160,
      margin: '0 auto',
      display: 'grid',
      gridTemplateColumns: '0.8fr 1.2fr',
      gap: 80,
      alignItems: 'center',
    }}>
      <div style={{ position: 'relative' }}>
        <div style={{
          aspectRatio: '4/5',
          borderRadius: 4,
          overflow: 'hidden',
          background: '#F9F7F4',
        }}>
          <img src="/assets/anna-portrait.jpg" alt="Anna Wareham" loading="lazy" decoding="async" style={{
            width: '100%', height: '100%', objectFit: 'cover', display: 'block',
          }} />
        </div>
        <div style={{
          position: 'absolute',
          bottom: 20,
          right: -24,
          background: 'var(--paper)',
          padding: '16px 20px',
          borderRadius: 10,
          border: '1px solid var(--hairline)',
          boxShadow: '0 14px 30px -12px rgba(80, 40, 20, 0.2)',
        }}>
          <div style={{
            fontFamily: '"Alegreya Sans", sans-serif',
            fontSize: 10,
            letterSpacing: '0.18em',
            color: 'var(--ink-muted)',
            textTransform: 'uppercase',
            marginBottom: 4,
          }}>Credentials</div>
          <div style={{
            fontFamily: '"Libre Baskerville", serif',
            fontStyle: 'italic',
            fontSize: 14,
            color: 'var(--ink)',
            lineHeight: 1.5,
          }}>
            BSc Food &amp; Nutrition<br />
            Reg. Associate Nutritionist
          </div>
        </div>
      </div>

      <div>
        <Eyebrow>Meet your nutritionist</Eyebrow>
        <SerifH size={58} style={{ marginTop: 20, marginBottom: 24 }}>
          I'm Anna and I've been the woman <Italic>starting over every Monday.</Italic>
        </SerifH>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <Body size={18}>
            I used to try a new diet every week. By evening I'd be bingeing and by Monday I'd be starting again. Exhausting. Shame-filled. Getting nowhere.
          </Body>
          <Body size={18}>
            So I went back to university. Four years. A degree in Food &amp; Nutrition. I became a Registered Associate Nutritionist and have spent over 10 years helping women get real, lasting results.
          </Body>
          <Body size={18}>
            Especially for women in midlife, where most advice simply misses the mark.
          </Body>
          <Body size={18} style={{ fontFamily: '"Libre Baskerville", serif', fontStyle: 'italic', color: 'var(--blush-deep)', fontSize: 21 }}>
            50,000 clients later, this is the simplest approach that actually gets results.
          </Body>
        </div>
      </div>
    </div>
  </section>
);

// Video testimonials (Vimeo embeds)
const VIDEO_TESTIMONIALS = [
  {
    id: '1147300902',
    hash: '58fbd0c85a',
    name: 'Vicky',
    quote: '"I started the WLA a size 20 and am now a 10/12"',
  },
  {
    id: '1147300577',
    hash: '65f81455af',
    name: 'Ruth',
    quote: '"I lost 12 pounds, sugar cravings vanished and my menopause symptoms significantly improved."',
  },
  {
    id: '1147300457',
    hash: '4d750b2063',
    name: 'Lisa',
    quote: '"My biggest NSV (non scale victory) is getting into size 10 and buying small gym leggings."',
  },
  {
    id: '1147299763',
    hash: 'a1064cfe85',
    name: 'Lucy',
    quote: '"2 ½ stone down, not counted a calorie in over a year and bought a crop top for the first time in my life"',
  },
];

const VideoTestimonialsSection = () => (
  <section className="video-testimonials-section" style={{
    padding: '120px 32px 48px',
    background: 'var(--bg)',
  }}>
    <div style={{ maxWidth: 1160, margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: 64 }}>
        <Eyebrow>Member stories</Eyebrow>
        <SerifH size={52} style={{ marginTop: 20, maxWidth: 820, marginInline: 'auto' }}>
          Hear what some of our <Italic>WLA members</Italic> have achieved
        </SerifH>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(2, 1fr)',
        gap: 48,
      }}>
        {VIDEO_TESTIMONIALS.map((v, i) => (
          <div key={i}>
            <div style={{
              aspectRatio: '16 / 9',
              borderRadius: 12,
              overflow: 'hidden',
              background: '#000',
              border: '1px solid var(--hairline)',
              boxShadow: '0 20px 40px -22px rgba(0, 48, 96, 0.25)',
            }}>
              <iframe
                src={`https://player.vimeo.com/video/${v.id}?h=${v.hash}&title=0&byline=0&portrait=0`}
                style={{ width: '100%', height: '100%', border: 0 }}
                title={`${v.name} testimonial`}
                allow="autoplay; fullscreen; picture-in-picture; clipboard-write"
                allowFullScreen
                loading="lazy"
              />
            </div>
            <div style={{
              marginTop: 20,
              fontFamily: '"Libre Baskerville", serif',
              fontStyle: 'italic',
              fontSize: 18,
              lineHeight: 1.5,
              color: 'var(--ink)',
              textAlign: 'center',
              maxWidth: 500,
              marginInline: 'auto',
            }}>
              {v.quote}
            </div>
            <div style={{
              marginTop: 12,
              textAlign: 'center',
              fontFamily: '"Alegreya Sans", sans-serif',
              fontSize: 12,
              letterSpacing: '0.18em',
              textTransform: 'uppercase',
              color: 'var(--blush-deep)',
              fontWeight: 600,
            }}>
              {v.name}
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

Object.assign(window, { IncludedSection, MembersAreaBlock, MasterclassesBlock, TestimonialsSection, ResultsGridSection, AboutSection, VideoTestimonialsSection });
