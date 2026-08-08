# Social Proof Patterns — 40+ Production-Ready Variants

## Social Proof Psychology

Social proof is the psychological phenomenon where people follow the actions and opinions of others. Robert Cialdini identified it as one of the six principles of persuasion. In web design, social proof blocks serve as trust accelerators — they reduce perceived risk, validate the user's consideration, and provide third-party evidence that the product delivers value.

Placement matters as much as content. Social proof placed immediately after a value proposition reinforces it. Social proof placed before pricing reduces price sensitivity. Social proof placed near a CTA boosts conversion by 12-34% (Baymard Institute). The most effective pages use 3-5 social proof blocks, varied in type, distributed throughout the page.

### The Trust Hierarchy
From weakest to strongest social proof:
1. **Self-claimed** ("We're the best") — zero trust value
2. **Quantitative** ("10,000+ users") — moderate, verifiable
3. **Logo display** ("Trusted by Google, Apple") — strong, brand association
4. **Ratings aggregate** ("4.8/5 from 2,000 reviews") — strong, quantified
5. **Individual testimonials** (named person + photo) — very strong, personal
6. **Video testimonials** (real person speaking) — strongest, hardest to fake
7. **Case studies with metrics** ("Acme increased revenue 40%") — strongest, data-backed

---

## Universal Social Proof Specs

### Section Wrapper
- Max-width: 1200px (standard), 1400px (logo bars)
- Vertical padding: 48-96px (varies by block density)
- Background: white, gray-50, or dark (for contrast)

### Quote Typography
- Quote text: 18-24px (large quotes), 16-18px (card quotes)
- Quote style: italic or regular with large quotation marks
- Attribution: 14-16px, font-weight 600 for name, regular for role
- Quotation marks: decorative 48-64px serif marks (optional)

---

## Variant 1: Testimonial Card Grid

3-column grid of testimonial cards. The bread-and-butter social proof pattern.

### Layout Specs
- Grid: 3 columns, gap 24-32px
- Card: padding 32px, border-radius 12-16px, background white, shadow-sm or border 1px gray-200
- Card anatomy: quote text (16-18px, gray-700) + avatar (48px, rounded-full) + name (16px, font-weight 600) + role/company (14px, gray-500)
- Star rating (optional): 5 stars above quote, 16px, yellow-400 fill
- Quote marks: large decorative open-quote at top-left of card (optional)

### Responsive Behavior
- `xl`+: 3 columns
- `lg`: 2 columns
- `md`: 1 column
- Cards maintain consistent padding at all sizes

### Production Code (React/TSX)
```tsx
interface Testimonial {
  quote: string;
  name: string;
  role: string;
  company?: string;
  avatar: string;
  rating?: number;
}

export function TestimonialGrid({ testimonials, title }: { testimonials: Testimonial[]; title: string }) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-12 lg:mb-16">{title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((t, i) => (
            <div key={i} className="rounded-2xl bg-white p-8 shadow-sm ring-1 ring-gray-900/5">
              {t.rating && (
                <div className="flex gap-1 mb-4">
                  {Array.from({ length: 5 }).map((_, j) => (
                    <svg key={j} className={`h-5 w-5 ${j < t.rating! ? 'text-yellow-400' : 'text-gray-200'}`} fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                  ))}
                </div>
              )}
              <p className="text-base text-gray-700 leading-relaxed">{t.quote}</p>
              <div className="mt-6 flex items-center gap-3">
                <img src={t.avatar} alt={t.name} className="h-10 w-10 rounded-full object-cover" loading="lazy" />
                <div>
                  <div className="text-sm font-semibold text-gray-900">{t.name}</div>
                  <div className="text-sm text-gray-500">{t.role}{t.company && `, ${t.company}`}</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Accessibility
- Quote cards are not interactive unless clickable; no special ARIA needed
- Avatar images have alt text with person's name
- Star ratings: provide text alternative ("Rated 5 out of 5 stars")

---

## Variant 2: Testimonial Carousel

Horizontally sliding testimonials with navigation controls.

### Layout Specs
- Container: overflow-hidden, full section width
- Slide width: 100% (single slide) or 33-50% (multi-slide peek)
- Navigation: left/right arrows (48px circles at edges) + dots below
- Auto-advance: 5-7 second interval, pause on hover and focus
- Transition: 400ms ease, translateX slide or opacity fade
- Each slide: quote (20-24px, centered) + avatar + name + role

### Accessibility Requirements
- Carousel container: `role="group"` with `aria-label="Testimonials"`
- Each slide: `role="group"` with `aria-label="Testimonial X of Y"`
- Arrows: `<button>` with `aria-label="Previous testimonial"` / `"Next testimonial"`
- Dots: `role="tablist"` with `role="tab"` per dot
- Auto-play: provide pause button, respect prefers-reduced-motion
- Keyboard: arrow keys navigate between slides when carousel is focused

### Production Code (React/TSX)
```tsx
import { useState, useEffect, useCallback } from 'react';

interface Testimonial { quote: string; name: string; role: string; avatar: string; }

export function TestimonialCarousel({ testimonials }: { testimonials: Testimonial[] }) {
  const [current, setCurrent] = useState(0);
  const [paused, setPaused] = useState(false);

  const next = useCallback(() => setCurrent((c) => (c + 1) % testimonials.length), [testimonials.length]);
  const prev = useCallback(() => setCurrent((c) => (c - 1 + testimonials.length) % testimonials.length), [testimonials.length]);

  useEffect(() => {
    if (paused) return;
    const timer = setInterval(next, 6000);
    return () => clearInterval(timer);
  }, [paused, next]);

  return (
    <section className="bg-gray-50 py-16 md:py-20 lg:py-24">
      <div
        className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center"
        onMouseEnter={() => setPaused(true)}
        onMouseLeave={() => setPaused(false)}
        role="group"
        aria-label="Customer testimonials"
      >
        <div className="relative">
          <svg className="mx-auto mb-8 h-12 w-12 text-gray-300" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M4.583 17.321C3.553 16.227 3 15 3 13.011c0-3.5 2.457-6.637 6.03-8.188l.893 1.378c-3.335 1.804-3.987 4.145-4.247 5.621.537-.278 1.24-.375 1.929-.311 1.804.167 3.226 1.648 3.226 3.489a3.5 3.5 0 01-3.5 3.5c-1.073 0-2.099-.49-2.748-1.179zm10 0C13.553 16.227 13 15 13 13.011c0-3.5 2.457-6.637 6.03-8.188l.893 1.378c-3.335 1.804-3.987 4.145-4.247 5.621.537-.278 1.24-.375 1.929-.311 1.804.167 3.226 1.648 3.226 3.489a3.5 3.5 0 01-3.5 3.5c-1.073 0-2.099-.49-2.748-1.179z" />
          </svg>
          <blockquote>
            <p className="text-xl sm:text-2xl font-medium text-gray-900 leading-relaxed max-w-3xl mx-auto">
              {testimonials[current].quote}
            </p>
          </blockquote>
          <div className="mt-8 flex items-center justify-center gap-3">
            <img src={testimonials[current].avatar} alt={testimonials[current].name} className="h-12 w-12 rounded-full object-cover" />
            <div className="text-left">
              <div className="font-semibold text-gray-900">{testimonials[current].name}</div>
              <div className="text-sm text-gray-500">{testimonials[current].role}</div>
            </div>
          </div>
        </div>
        <div className="mt-8 flex items-center justify-center gap-4">
          <button onClick={prev} className="rounded-full p-2 text-gray-400 hover:text-gray-600 transition-colors" aria-label="Previous testimonial">
            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" /></svg>
          </button>
          <div className="flex gap-2" role="tablist">
            {testimonials.map((_, i) => (
              <button key={i} role="tab" aria-selected={i === current} onClick={() => setCurrent(i)} className={`h-2 rounded-full transition-all ${i === current ? 'w-6 bg-blue-600' : 'w-2 bg-gray-300'}`} aria-label={`Go to testimonial ${i + 1}`} />
            ))}
          </div>
          <button onClick={next} className="rounded-full p-2 text-gray-400 hover:text-gray-600 transition-colors" aria-label="Next testimonial">
            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" /></svg>
          </button>
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 3: Single Large Testimonial

One featured testimonial, full-width, maximum impact.

### Layout Specs
- Centered layout, max-width 800px
- Large decorative quotation marks: 48-64px, gray-200 or brand-100
- Quote text: 24-32px, font-weight 500, line-height 1.4
- Attribution below: avatar (64px) + name (18px bold) + role (16px gray-500)
- Background: white, gray-50, or dark for contrast
- Optional: company logo instead of or with avatar

### When to Use
- When you have one extremely strong testimonial from a recognizable person/company
- As a transition between feature sections and pricing
- In a dark background section for visual contrast

---

## Variant 4: Customer Logo Bar

The simplest and most universally applicable social proof pattern.

### Layout Specs
- Single horizontal row of logos
- Logo count: 5-8 (optimal for single row)
- Logo height: 28-40px, auto width (preserve aspect ratio)
- Logo treatment: grayscale by default, full color on hover
- Opacity: 50-60% default, 100% on hover
- Gap between logos: 32-48px
- Optional label above: "Trusted by", "Used by teams at", "Powering"
- Label: 13-14px, font-weight 500, gray-500, uppercase tracking

### Responsive Behavior
- `xl`+: Single row, all logos visible
- `lg`: Single row, may reduce gap to 24px
- `md`: Wrap to 2 rows, 3-4 per row
- `sm`: Wrap to 2-3 rows, 2-3 per row, reduce logo height to 24px

### Production Code
```tsx
export function LogoBar({ logos, label }: { logos: Array<{ src: string; alt: string }>; label?: string }) {
  return (
    <section className="bg-white py-12 md:py-16">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        {label && <p className="text-center text-sm font-medium text-gray-500 mb-8">{label}</p>}
        <div className="flex flex-wrap items-center justify-center gap-x-8 gap-y-6 sm:gap-x-12 lg:gap-x-16">
          {logos.map((logo) => (
            <img key={logo.alt} src={logo.src} alt={logo.alt} className="h-7 sm:h-8 lg:h-9 w-auto opacity-60 grayscale hover:opacity-100 hover:grayscale-0 transition-all duration-200" loading="lazy" />
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Psychology
Logo bars work through the "bandwagon effect" and authority bias. Recognizable logos transfer trust from those brands to your product. Place logo bars immediately after the hero for maximum early trust impact.

---

## Variant 5: Scrolling Logo Marquee

Infinite horizontal scroll of logos. Modern, dynamic alternative to static logo bar.

### Layout Specs
- Animation: continuous translateX scroll, 20-40 seconds per loop
- Direction: right-to-left (natural reading direction)
- Duplicate logo set for seamless loop (render logos twice)
- Logo gap: 48-64px
- Logo height: 32-40px
- Pause on hover (CSS animation-play-state: paused)
- No scroll controls needed

### Production Code (CSS)
```css
.marquee-container {
  overflow: hidden;
  mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
}

.marquee-track {
  display: flex;
  gap: 3rem;
  animation: marquee 30s linear infinite;
  width: max-content;
}

.marquee-track:hover {
  animation-play-state: paused;
}

@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@media (prefers-reduced-motion: reduce) {
  .marquee-track {
    animation: none;
    flex-wrap: wrap;
    justify-content: center;
    width: auto;
  }
}
```

---

## Variant 6: Metric Callout Bar

3-4 large numbers displayed prominently. Quantitative social proof.

### Layout Specs
- Horizontal row: 3-4 stat items
- Number: 36-56px, font-weight 700-800, brand color or gray-900
- Label: 14-16px, gray-500, below number
- Dividers: optional 1px vertical lines between items (40px height)
- Background: gray-50 or brand-tinted
- Section padding: compact (py-12 to py-16)

### Number Formatting
- Use abbreviations for large numbers: "10K+", "1M+", "$2.5B"
- Include units: "98%", "4.8/5", "24/7"
- Add trend context where possible: "10K+ customers" not just "10K+"

### Animation: Count-Up
```tsx
import { useEffect, useRef, useState } from 'react';

function useCountUp(target: number, duration: number = 2000) {
  const [count, setCount] = useState(0);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        const start = Date.now();
        const step = () => {
          const elapsed = Date.now() - start;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
          setCount(Math.round(eased * target));
          if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        observer.disconnect();
      }
    }, { threshold: 0.5 });

    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [target, duration]);

  return { count, ref };
}
```

### Production Code
```tsx
interface Stat { value: string; label: string; }

export function MetricCalloutBar({ stats }: { stats: Stat[] }) {
  return (
    <section className="bg-gray-50 py-12 md:py-16 border-y border-gray-100">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((stat, i) => (
            <div key={i} className="text-center">
              <div className="text-3xl sm:text-4xl lg:text-5xl font-bold text-gray-900">{stat.value}</div>
              <div className="mt-2 text-sm text-gray-500">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 7: Star Rating Display

Aggregate rating with star visualization.

### Layout Specs
- Stars: 5-star row, 20-24px each, yellow-400 fill for active, gray-200 for inactive
- Half-star support: clip path or two overlapping stars
- Score: "4.8" in 32-48px bold text beside stars
- Review count: "(2,341 reviews)" in 14px gray-500
- Optional: link to full reviews
- Source attribution: "on G2" or "on Capterra" with platform logo

### Psychological Impact
Star ratings are the most universally understood trust signal. 4.5+ stars significantly boost conversion. Display them near CTAs and pricing for maximum effect. Always include review count — stars without count appear fabricated.

---

## Variant 8: Case Study Card Grid

Case study preview cards for detailed social proof.

### Layout Specs
- Grid: 2-3 columns, gap 32px
- Card: cover image (16:9, rounded-t-xl) + company logo (32-40px height) + title (20px bold) + key metric ("40% increase in conversion") + "Read case study" link
- Key metric: large text (24-32px), brand color, prominent placement
- Card shadow: sm default, md on hover
- Card border-radius: 16px

### Production Code
```tsx
interface CaseStudy { image: string; logo: string; logoAlt: string; title: string; metric: string; metricLabel: string; href: string; }

export function CaseStudyGrid({ studies, title }: { studies: CaseStudy[]; title: string }) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-12 lg:mb-16">{title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {studies.map((s, i) => (
            <a key={i} href={s.href} className="group rounded-2xl overflow-hidden shadow-sm ring-1 ring-gray-900/5 hover:shadow-lg transition-shadow">
              <div className="aspect-video overflow-hidden">
                <img src={s.image} alt="" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
              </div>
              <div className="p-6">
                <img src={s.logo} alt={s.logoAlt} className="h-8 w-auto mb-4" />
                <h3 className="text-lg font-semibold text-gray-900 mb-3">{s.title}</h3>
                <div className="text-2xl font-bold text-blue-600">{s.metric}</div>
                <div className="text-sm text-gray-500 mt-1">{s.metricLabel}</div>
                <div className="mt-4 text-sm font-semibold text-blue-600 group-hover:text-blue-500">
                  Read case study &rarr;
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 9: Press Mention Bar

"As seen in" with media publication logos.

### Layout Specs
- Label: "As seen in" or "Featured in" (13px, gray-500, uppercase)
- Logos: major publication logos (TechCrunch, Forbes, Bloomberg, etc.)
- Logo treatment: same as logo bar (grayscale, 28-36px height)
- Layout: centered row below label
- Background: white or gray-50
- Compact section: py-8 to py-12

### Psychology
Press mentions leverage authority bias. Even a brief mention in a recognizable publication transfers credibility. Display the most recognizable publications first (left to right = most to least prominent).

---

## Variant 10: Trust Badge Bar

Security seals, certifications, and compliance badges.

### Layout Specs
- Badges: SOC 2, GDPR, HIPAA, PCI-DSS, ISO 27001, etc.
- Badge size: 48-64px height
- Layout: centered horizontal row, gap 32-48px
- Optional: text label below each badge
- Background: white, often placed near pricing or checkout
- Border: optional top/bottom 1px gray-100

### Placement Psychology
Trust badges are most effective near conversion points. Place them below pricing tables, near payment forms, or beside CTA buttons. They reduce anxiety at the moment of commitment.

---

## Variants 11-20: Detailed Specs

### 11. Video Testimonial Grid
3-column grid of video thumbnails with play buttons. Thumbnail: 16:9 ratio. Play button: white circle (64px) centered, with triangle icon. Click: opens modal with video player. Name + role overlay at bottom of thumbnail.

### 12. Video Testimonial Featured
Single large video embed (16:9). Below: pull quote from the video. Beside or below: name, role, company logo. Background: dark for cinematic feel. Video thumbnail with custom play button before user clicks.

### 13. Review Aggregation Display
Large average score (4.8), star row, total review count, plus distribution bars (5-star: 80%, 4-star: 12%, etc.). Similar to Amazon/Google review summaries. Source attribution required.

### 14. Before/After Comparison
Drag slider dividing two images. Left: before state. Right: after state. Slider handle: vertical line with drag arrows. Images: same dimensions, aligned. Label: "Before" / "After" above or on images. Touch: drag support on mobile.

### 15. NPS Score Display
Large number (0-100) in colored circle/gauge. Color: red (0-30), yellow (30-70), green (70+). Label: "Net Promoter Score" below. Context: industry average comparison. Gauge: arc chart or radial progress.

### 16. Customer Map
World map (SVG or Mapbox) with dots at customer locations. Dot density indicates concentration. Hover: show city/region name + customer count. Mobile: simplified map or replace with country list. Color: brand with opacity gradient.

### 17. Social Proof Notification (Toast)
Small popup in bottom-left: "Sarah from Austin just signed up 2 minutes ago." Auto-dismiss after 5 seconds. Appears every 10-30 seconds. Avatar + name + location + action + time. Close button. Respect: frequency cap, don't annoy. Ethical note: only use with real data.

### 18. Community Stats
Large numbers for community metrics. Format: "50K+ members", "1M+ messages", "10K+ contributions." Grid: 3-4 stats in a row. Icons per stat (users, messages, code, etc.). Used by developer tools and community platforms.

### 19. GitHub Stars Badge
For open source: GitHub star count badge. Format: star icon + "12.5K" + "stars on GitHub." Link to GitHub repository. Real-time count via GitHub API (cache for performance). Styled as a subtle badge, not a full section.

### 20. App Store Rating
Stars + average score + total ratings + "on the App Store." Apple App Store or Google Play badge beside rating. Link to app listing. Format: 4.9 stars (12K ratings). Combined with download count for extra impact.

---

## Variants 21-40: Extended Patterns

### 21. G2/Capterra Badge Embed
Embed official review platform badges. G2 Grid badge: "Leader", "High Performer". Capterra: star rating + "X reviews." Use official embed codes for authenticity. Place near pricing or in footer.

### 22. ROI Calculator Result
Interactive calculator where users input their numbers and see projected ROI. Inputs: current cost, team size, efficiency. Output: savings, time saved, ROI percentage. The result itself IS social proof — "companies like yours save $X."

### 23. Testimonial with CTA
Standard testimonial card + "Read the full story" link. Links to case study page. Card has a subtle hover effect. Right arrow icon on link. Bridges social proof and detailed content.

### 24. Industry-Specific Proof
Logo bar grouped by industry tabs. Tab: "Healthcare", "Finance", "E-Commerce", etc. Each tab shows relevant customer logos. Demonstrates breadth + depth. Effective for horizontal products serving multiple industries.

### 25. Partner Logo Tier
Gold/Silver/Bronze partner levels in separate rows. Gold: largest logos, top row. Silver: medium, second row. Bronze: smaller, third row. Used for marketplace and partner ecosystem pages.

### 26. Success Story Accordion
Expandable customer stories in accordion format. Trigger: company logo + name + one-line result. Expanded: full story, metrics, quote, photo. Single column, max-width 800px. More detail than cards, more compact than full case studies.

### 27. Testimonial Masonry
Pinterest-style varying-height testimonial cards. Short quotes = shorter cards, long quotes = taller cards. 2-3 columns. Creates visual interest through irregular heights. CSS columns or masonry layout.

### 28. Live Customer Counter
Animated number showing real-time or near-real-time customer count. Format: "12,847 companies trust us." Number updates periodically (WebSocket or polling). Count-up animation on load. Ethical: use real, current numbers only.

### 29. Testimonial with Rating
Combined format: star rating at top + quote below + attribution. Merges the authority of ratings with the personality of quotes. Card format in a grid. Most effective format for B2C products.

### 30. Social Media Embed Grid
Embedded tweets, LinkedIn posts, or Instagram posts. 2-3 column grid. Use official embed codes. Shows authentic, unedited social proof. Curate the best posts. Performance note: embeds are heavy — lazy-load.

### 31. User-Generated Content Grid
Instagram-style photo grid from customers. Photos: square (1:1), uniform grid, 3-6 columns. Lightbox on click. Hashtag: encourage with branded hashtag. Used by D2C, fashion, food, and lifestyle brands.

### 32. Award Badge Display
Award icons/images in a horizontal row. Awards: "Best of 2024", "Editor's Choice", "Product of the Year." Badge size: 64-80px. Labels below. Background: gray-50 or white. Compact section.

### 33. Press Quote Cards
Publication logo + quote excerpt in card format. Card: logo at top, quote below, publication name. 2-3 column grid. Quote: 16-18px italic. Logo: 24-32px height. "Read full article" link optional.

### 34. Client Wall
Dense grid of small avatar or logo thumbnails. 8-12 columns of small items (40-48px). Creates visual impression of scale. Hover: show name tooltip. No individual detail — the mass IS the message.

### 35. Testimonial with Photo (Large)
Full-width or wide layout: large photo of the person/scene + quote overlaid or beside. Photo: 50% of section width. Quote: large (24-28px). Creates strong personal connection. Best for 1-2 featured testimonials.

### 36. Customer Count Badge
Simple inline badge: "Trusted by 10,000+ companies." Format: icon + number + text. Placement: below hero CTA, in nav bar, or in footer. Small: 14px text, subtle styling. Effective as micro social proof.

### 37. Testimonial with Logo (Company)
Quote card with company logo prominent instead of personal avatar. Logo: 80-120px width, above or beside quote. Name + role below quote. Best for B2B where company name carries more weight than individual.

### 38. Case Study Featured (Hero-Style)
Single large case study preview spanning full width. Background: customer's brand color or photo. Large metric: "250% increase in efficiency." Company logo: white on dark bg. "Read full case study" CTA button. Used as a section divider.

### 39. Social Proof Composite Block
Combines multiple proof types in one section: logo bar + single testimonial + metric callouts. Three-layer approach: logos at top, quote in middle, stats at bottom. Maximum trust density in one section.

### 40. Partner Logo Ecosystem
Visual network of connected logos showing integrations or partnerships. Centered product logo with partner logos around it in a radial pattern. Lines or dots connecting them. Shows ecosystem breadth. Interactive: hover for partner details.

---

## Social Proof Placement Strategy

### Above the Fold (Hero Area)
- Logo bar immediately after hero CTA
- Customer count badge in hero text
- Best for: early trust establishment

### After Value Proposition (Features Section)
- Testimonials validating specific features
- Case study metrics related to claimed benefits
- Best for: evidence-based persuasion

### Before Pricing
- Review aggregation (star ratings)
- Customer count and metric callouts
- Best for: reducing price sensitivity

### Near CTA Buttons
- Trust badges and security seals
- Single testimonial quote
- Customer count inline with CTA text
- Best for: conversion anxiety reduction

### After Pricing (Below Fold)
- Full case studies and video testimonials
- Detailed press mentions
- Best for: reassurance for still-undecided visitors

### Footer Area
- Award badges
- Certification badges
- Review platform badges (G2, Capterra)
- Best for: bottom-of-page trust reinforcement

---

## Social Proof Ethics

1. **Never fabricate testimonials** — use real quotes from real customers with permission
2. **Never create fake urgency** (fake countdown timers, fake "only 2 left")
3. **Social proof notifications must use real data** — showing fake "John from NYC just signed up" is deceptive
4. **Display actual metrics** — inflated numbers destroy trust if discovered
5. **Get permission** — always get written consent before using a customer's name, photo, or quote
6. **Keep testimonials current** — refresh quarterly, remove outdated ones
7. **Disclose sponsored or incentivized reviews** — FTC requires disclosure
8. **Don't cherry-pick misleadingly** — represent the true range of customer experience
