# Content Section Patterns — 60+ Production-Ready Variants

## Content Block Design Philosophy

Content blocks are the connective tissue of every page. While hero blocks grab attention and CTA blocks drive action, content blocks do the heavy lifting of communication — explaining features, presenting processes, organizing information, and guiding comprehension. A page with a great hero but weak content blocks is like a book with a stunning cover and empty pages.

Content blocks must optimize for two competing goals: scannability (users skim before they read) and depth (users need substance when they decide to engage). The best content blocks serve both — clear hierarchy for scanning, rich detail for reading.

---

## Universal Content Block Specs

### Section Wrapper
- Max-width: 1200px (standard), 960px (narrow for text-heavy), 1400px (wide for grids)
- Horizontal padding: 16px (sm), 24px (md), 32px (lg), 48-80px (xl+)
- Vertical padding: 48px (sm), 64px (md), 80px (lg), 96-120px (xl+)

### Content Typography
- Heading (H2): 36-48px desktop, 28-36px mobile, font-weight 700, tracking -0.02em
- Subheading (H3): 24-32px desktop, 20-24px mobile, font-weight 600
- Body: 16-18px, line-height 1.6-1.7, max-width 65ch
- Small text: 14px, line-height 1.5
- Caption: 12-13px, color gray-500

---

## Variant 1: 3-Column Feature Grid

The most common content layout on the web. Three equal-width cards displaying features, benefits, or services.

### Layout Specs
- Grid: 3 equal columns, gap 32px (desktop), 24px (tablet)
- Card anatomy: Icon (40-48px) + Heading (H3, 20-24px) + Description (16px, 2-4 lines)
- Icon: SVG in colored circle (48x48px bg) or standalone (32x32px)
- Card padding: 32px (with border/shadow) or 0px (borderless)
- Card alignment: center-aligned (icons centered) or left-aligned (icons left)

### Responsive Behavior
- `xl`+: 3 columns
- `lg`: 3 columns (narrower gap: 24px)
- `md`: 2 columns (one card wraps to next row)
- `sm`: 1 column (stacked)

### Production Code (React/TSX)
```tsx
interface Feature {
  icon: React.ReactNode;
  title: string;
  description: string;
}

interface FeatureGridProps {
  label?: string;
  title: string;
  description?: string;
  features: Feature[];
}

export function FeatureGrid3Col({ label, title, description, features }: FeatureGridProps) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-12 lg:mb-16">
          {label && <p className="text-sm font-semibold uppercase tracking-wider text-blue-600 mb-3">{label}</p>}
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-gray-900">{title}</h2>
          {description && <p className="mt-4 text-lg text-gray-600 leading-relaxed">{description}</p>}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-12">
          {features.map((feature, i) => (
            <div key={i} className="text-center">
              <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-blue-100 text-blue-600 mb-5">
                {feature.icon}
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">{feature.title}</h3>
              <p className="text-base text-gray-600 leading-relaxed">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Accessibility
- Each card is a logical group with heading hierarchy (H3 under the section H2)
- Icons are decorative (aria-hidden="true") when heading conveys meaning
- Color is not the only indicator of feature differentiation

---

## Variant 2: 4-Column Feature Grid

Compact, icon-led, for listing many features at a glance.

### Layout Specs
- Grid: 4 columns, gap 24-32px
- Card: icon (32px) + heading (18px, font-weight 600) + short description (14-16px, 1-2 lines)
- More compact than 3-col: less padding, smaller text
- Works best with 8-12 features (2-3 rows)

### Responsive Behavior
- `xl`+: 4 columns
- `lg`: 3 columns
- `md`: 2 columns
- `sm`: 1 column or 2-column compact

---

## Variant 3: 2-Column Feature Grid

For fewer features that need more detail per item.

### Layout Specs
- Grid: 2 columns, gap 32-48px
- Card: larger icon/illustration (64-80px) + heading (24px) + longer description (16-18px, 3-6 lines)
- Optional: "Learn more" link per card
- Ideal for 4-6 features

### Responsive Behavior
- `lg`+: 2 columns
- `md` and below: 1 column

---

## Variant 4: Feature List (Vertical)

Single-column feature list with icon and text side by side.

### Layout Specs
- Single column, max-width 640px
- Each item: icon left (32px, flex-shrink-0) + text right (heading 18px + description 16px)
- Vertical gap between items: 24-32px
- Optional: divider line between items
- Works well inside a sidebar or narrow content area

### Production Code
```tsx
interface FeatureItem { icon: React.ReactNode; title: string; description: string; }

export function FeatureList({ features }: { features: FeatureItem[] }) {
  return (
    <div className="max-w-xl mx-auto space-y-8">
      {features.map((f, i) => (
        <div key={i} className="flex gap-4">
          <div className="flex-shrink-0 flex h-10 w-10 items-center justify-center rounded-lg bg-blue-100 text-blue-600">
            {f.icon}
          </div>
          <div>
            <h3 className="text-lg font-semibold text-gray-900">{f.title}</h3>
            <p className="mt-1 text-base text-gray-600 leading-relaxed">{f.description}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
```

---

## Variant 5: Alternating Zigzag

Image and text alternating sides. One of the most effective layouts for narrative feature presentation.

### Layout Specs
- Each row: 2 columns, image 50% + text 50%
- Odd rows: text left, image right
- Even rows: image left, text right
- Gap between columns: 48-80px
- Gap between rows: 64-96px
- Image: rounded-lg, shadow, aspect-ratio 4:3 or 16:10
- Text: heading (28-32px) + description (16-18px) + optional link/button

### Responsive Behavior
- `lg`+: side-by-side with alternating order
- `md`: stacked, image always on top, text below
- Use CSS `order` or flexbox `flex-direction: column` with `order` override

### Production Code (React/TSX)
```tsx
interface ZigzagItem {
  title: string;
  description: string;
  image: { src: string; alt: string };
  link?: { label: string; href: string };
}

export function ZigzagFeatures({ items, label, title }: { items: ZigzagItem[]; label?: string; title: string }) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-16 lg:mb-20">
          {label && <p className="text-sm font-semibold uppercase tracking-wider text-blue-600 mb-3">{label}</p>}
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-gray-900">{title}</h2>
        </div>
        <div className="space-y-16 lg:space-y-24">
          {items.map((item, i) => (
            <div key={i} className={`lg:grid lg:grid-cols-2 lg:gap-x-16 items-center ${i % 2 === 1 ? 'lg:flex-row-reverse' : ''}`}>
              <div className={i % 2 === 1 ? 'lg:order-2' : ''}>
                <h3 className="text-2xl sm:text-3xl font-bold text-gray-900">{item.title}</h3>
                <p className="mt-4 text-lg text-gray-600 leading-relaxed">{item.description}</p>
                {item.link && (
                  <a href={item.link.href} className="mt-6 inline-flex items-center text-blue-600 font-semibold hover:text-blue-500">
                    {item.link.label} <span className="ml-1">&rarr;</span>
                  </a>
                )}
              </div>
              <div className={`mt-8 lg:mt-0 ${i % 2 === 1 ? 'lg:order-1' : ''}`}>
                <img src={item.image.src} alt={item.image.alt} className="w-full rounded-xl shadow-lg" loading="lazy" />
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 6: Bento Grid

Asymmetric grid with mixed-size cards. Modern, visually dynamic, popularized by Apple.

### Layout Specs
- Grid: CSS Grid with explicit row/column sizing
- Large card: spans 2 columns or 2 rows
- Small cards: 1x1
- Gap: 16-24px
- Cards: rounded-2xl, subtle border or shadow, padding 24-32px
- Background per card: white, gray-50, or brand-tinted
- Typical layout: 2x2 grid with one card spanning the left column full height

### Grid Template (common patterns)
```css
/* Pattern A: 2+1 left, 1+1 right */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto auto;
  gap: 1rem;
}
.bento-grid .large { grid-column: span 2; grid-row: span 2; }

/* Pattern B: Apple-style 4-card bento */
.bento-grid-b {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 200px 200px;
  gap: 1rem;
}
.bento-grid-b .wide { grid-column: span 2; }
.bento-grid-b .tall { grid-row: span 2; }
```

### Responsive Behavior
- `xl`+: Full bento grid
- `lg`: Reduce to 2-column grid, large cards span full width
- `md`: Single column, all cards stack
- Cards maintain aspect ratio or switch to auto-height

---

## Variant 7: Feature Tabs

Tabbed interface where each tab reveals a different feature with content and visual.

### Layout Specs
- Tab bar: horizontal, centered or left-aligned
- Tab items: text-only (16px, font-weight 500), or icon + text
- Active tab: border-bottom 2px brand color, or filled background
- Content panel: appears below tabs, typically image left + text right or reverse
- Transition: fade or slide, 200-300ms
- Content panel min-height: prevent layout shift between tabs

### Tab Specifications
- Tab height: 48px
- Tab horizontal padding: 16-24px
- Tab gap: 4-8px
- Tab font-size: 14-16px
- Active indicator: 2px bottom border (underline style) or filled pill
- Keyboard: arrow keys to navigate between tabs, Tab to enter content

### Responsive Behavior
- `lg`+: Horizontal tabs + side-by-side content
- `md`: Horizontal scrolling tabs (overflow-x auto) + stacked content
- `sm`: Tabs become accordion (each tab is an expandable section)

### Production Code (React/TSX)
```tsx
import { useState } from 'react';

interface TabItem {
  label: string;
  title: string;
  description: string;
  image: { src: string; alt: string };
}

export function FeatureTabs({ tabs }: { tabs: TabItem[] }) {
  const [active, setActive] = useState(0);

  return (
    <section className="bg-gray-50 py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div role="tablist" className="flex gap-1 border-b border-gray-200 mb-12 overflow-x-auto">
          {tabs.map((tab, i) => (
            <button
              key={i}
              role="tab"
              aria-selected={i === active}
              aria-controls={`panel-${i}`}
              onClick={() => setActive(i)}
              className={`px-6 py-3 text-sm font-medium whitespace-nowrap border-b-2 transition-colors ${
                i === active ? 'border-blue-600 text-blue-600' : 'border-transparent text-gray-500 hover:text-gray-700'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
        {tabs.map((tab, i) => (
          <div
            key={i}
            id={`panel-${i}`}
            role="tabpanel"
            hidden={i !== active}
            className="lg:grid lg:grid-cols-2 lg:gap-x-16 items-center"
          >
            <div>
              <h3 className="text-2xl sm:text-3xl font-bold text-gray-900">{tab.title}</h3>
              <p className="mt-4 text-lg text-gray-600 leading-relaxed">{tab.description}</p>
            </div>
            <div className="mt-8 lg:mt-0">
              <img src={tab.image.src} alt={tab.image.alt} className="w-full rounded-xl shadow-lg" loading="lazy" />
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
```

---

## Variant 8: Feature Accordion

Expandable feature descriptions, ideal for mobile-first design and long feature lists.

### Layout Specs
- Single column, max-width 800px or split with image
- Each item: trigger (heading 18-20px + expand icon) + collapsible content (16px body + optional image)
- Trigger height: 56-64px
- Border between items: 1px gray-200
- Only one item open at a time (optional: allow multiple)
- Animation: max-height transition, 200-300ms ease

### Accessibility
- `role="region"` on each panel with `aria-labelledby` pointing to the trigger
- Trigger is a `<button>` with `aria-expanded="true/false"` and `aria-controls`
- Content is hidden with `hidden` attribute or `aria-hidden` + height animation

---

## Variant 9: Stats/Metrics Bar

A horizontal row of 3-4 key statistics. Compact, high-impact social proof.

### Layout Specs
- Layout: flex row, 3-4 items, evenly spaced or separated by vertical dividers
- Each stat: large number (36-48px, font-weight 700) + label (14px, gray-500)
- Number alignment: center within item
- Dividers: 1px gray-200, height 40px, or no dividers with equal spacing
- Section background: gray-50 or matching adjacent sections
- Section height: compact — py-12 to py-16

### Responsive Behavior
- `lg`+: Horizontal row, 3-4 across
- `md`: 2x2 grid
- `sm`: 2x2 grid or stacked single column

### Production Code
```tsx
interface Stat { value: string; label: string; }

export function StatsBar({ stats }: { stats: Stat[] }) {
  return (
    <section className="bg-gray-50 py-12 md:py-16">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-12">
          {stats.map((stat, i) => (
            <div key={i} className="text-center">
              <div className="text-3xl sm:text-4xl font-bold text-gray-900">{stat.value}</div>
              <div className="mt-1 text-sm text-gray-500">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 10: Team Grid

Display team members with photos, names, and roles.

### Layout Specs
- Grid: 3-col (standard) or 4-col (compact)
- Card: photo (aspect-ratio 1:1 or 3:4, rounded-lg or rounded-full) + name (18px, font-weight 600) + role (14px, gray-500)
- Photo size: 200-280px width (constrained by column)
- Optional: social links below role (LinkedIn, Twitter icons, 20px)
- Card spacing: gap 32-48px

### Responsive Behavior
- `xl`+: 4 columns
- `lg`: 3 columns
- `md`: 2 columns
- `sm`: 2 columns (compact) or 1 column (large cards)

### Production Code
```tsx
interface TeamMember { name: string; role: string; photo: string; social?: { linkedin?: string; twitter?: string } }

export function TeamGrid({ members, title }: { members: TeamMember[]; title: string }) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-12 lg:mb-16">{title}</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 lg:gap-12">
          {members.map((m, i) => (
            <div key={i} className="text-center">
              <img src={m.photo} alt={m.name} className="w-full aspect-square object-cover rounded-xl mb-4" loading="lazy" />
              <h3 className="text-lg font-semibold text-gray-900">{m.name}</h3>
              <p className="text-sm text-gray-500">{m.role}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 11: Vertical Timeline

Events displayed chronologically along a vertical line.

### Layout Specs
- Center variant: line at 50%, events alternate left/right
- Left variant: line at left edge, all events on right
- Line: 2px width, gray-200 or brand-100
- Marker: 12-16px circle on line, filled brand color for current/past, outline for future
- Event: date (14px, gray-500) + title (18-20px, font-weight 600) + description (16px) + optional image
- Event spacing: 48-64px vertical between items

### Responsive Behavior
- `lg`+: Center-aligned with alternating left/right
- `md` and below: Left-aligned, all events on right (single column)

### Production Code
```tsx
interface TimelineEvent { date: string; title: string; description: string; }

export function Timeline({ events }: { events: TimelineEvent[] }) {
  return (
    <div className="relative">
      <div className="absolute left-4 lg:left-1/2 top-0 bottom-0 w-0.5 bg-gray-200 lg:-translate-x-px" />
      <div className="space-y-12">
        {events.map((event, i) => (
          <div key={i} className={`relative flex items-start gap-6 lg:gap-0 ${i % 2 === 0 ? 'lg:flex-row-reverse' : ''}`}>
            <div className="absolute left-4 lg:left-1/2 w-3 h-3 bg-blue-600 rounded-full -translate-x-[5px] lg:-translate-x-1.5 mt-1.5 ring-4 ring-white" />
            <div className={`ml-12 lg:ml-0 lg:w-1/2 ${i % 2 === 0 ? 'lg:pr-16 lg:text-right' : 'lg:pl-16'}`}>
              <span className="text-sm font-medium text-blue-600">{event.date}</span>
              <h3 className="text-xl font-semibold text-gray-900 mt-1">{event.title}</h3>
              <p className="text-base text-gray-600 mt-2 leading-relaxed">{event.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
```

---

## Variant 12: Process Steps (Numbered)

Sequential steps showing a process, workflow, or "how it works."

### Layout Specs
- Horizontal (desktop): 3-4 steps in a row, connected by lines/arrows
- Vertical (mobile/alt): stacked steps with vertical connector
- Step anatomy: number circle (48px, brand bg, white text, font-weight 700) + title (18-20px) + description (16px)
- Connector: 2px line or dashed line between circles
- Arrow: optional chevron/arrow on connector line

### Responsive Behavior
- `lg`+: Horizontal row with connectors
- `md` and below: Vertical stack with vertical connectors

### Production Code
```tsx
interface Step { title: string; description: string; }

export function ProcessSteps({ steps, title }: { steps: Step[]; title: string }) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-12 lg:mb-16">{title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 relative">
          {steps.map((step, i) => (
            <div key={i} className="text-center relative">
              <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-blue-600 text-white text-lg font-bold mb-4">
                {i + 1}
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">{step.title}</h3>
              <p className="text-base text-gray-600 leading-relaxed">{step.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 13: Logo Wall / Partner Bar

Display client, partner, or integration logos.

### Layout Specs
- Logos: grayscale by default, full color on hover
- Logo height: 28-40px, auto width (maintain aspect ratio)
- Horizontal layout: flex row, gap 32-48px, centered
- Grid layout: 4-6 columns for many logos
- Marquee variant: infinite horizontal scroll animation
- Background: white or gray-50

### Responsive Behavior
- `lg`+: Single row (up to 6-8 logos) or multi-row grid
- `md`: Wrap to 2 rows
- `sm`: Smaller logos (24-32px height), tighter gap, 2-3 rows

### Production Code
```tsx
export function LogoBar({ logos, label }: { logos: Array<{ src: string; alt: string }>; label?: string }) {
  return (
    <section className="bg-gray-50 py-12 md:py-16">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        {label && <p className="text-center text-sm font-medium text-gray-500 mb-8">{label}</p>}
        <div className="flex flex-wrap items-center justify-center gap-x-8 gap-y-6 sm:gap-x-12">
          {logos.map((logo) => (
            <img key={logo.alt} src={logo.src} alt={logo.alt} className="h-8 w-auto opacity-60 grayscale hover:opacity-100 hover:grayscale-0 transition-all" loading="lazy" />
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 14: Blog Post Grid

Grid of article/blog post cards for content marketing sections.

### Layout Specs
- Grid: 3-col (desktop), 2-col (tablet), 1-col (mobile)
- Card: featured image (16:9 ratio, rounded-t-lg) + category tag (12px, colored badge) + title (18-20px, font-weight 600, 2 lines max) + excerpt (14-16px, 2-3 lines, clamp) + author (avatar 32px + name 14px) + date (14px, gray-500)
- Card shadow: sm, hover: md with translateY(-2px) transition
- Card border-radius: 12px

### Production Code
```tsx
interface Post { title: string; excerpt: string; image: string; category: string; author: { name: string; avatar: string }; date: string; href: string; }

export function BlogGrid({ posts }: { posts: Post[] }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {posts.map((post) => (
        <a key={post.title} href={post.href} className="group rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-all">
          <div className="aspect-video overflow-hidden">
            <img src={post.image} alt="" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          </div>
          <div className="p-6">
            <span className="text-xs font-semibold uppercase tracking-wider text-blue-600">{post.category}</span>
            <h3 className="mt-2 text-lg font-semibold text-gray-900 line-clamp-2 group-hover:text-blue-600 transition-colors">{post.title}</h3>
            <p className="mt-2 text-sm text-gray-600 line-clamp-2">{post.excerpt}</p>
            <div className="mt-4 flex items-center gap-3">
              <img src={post.author.avatar} alt={post.author.name} className="h-8 w-8 rounded-full" />
              <div className="text-sm"><span className="font-medium text-gray-900">{post.author.name}</span><span className="text-gray-500 ml-2">{post.date}</span></div>
            </div>
          </div>
        </a>
      ))}
    </div>
  );
}
```

---

## Variant 15: FAQ Accordion

The standard pattern for frequently asked questions sections.

### Layout Specs
- Single column, max-width 768px, centered
- Item: question (18px, font-weight 500-600) + expand/collapse chevron icon (20px)
- Answer: 16px, color gray-600, padding-bottom 24px
- Border: 1px bottom border between items
- Animation: height transition 200ms ease + chevron rotation 180deg
- Default: first item open, or all closed

### Accessibility Requirements
- Each question is a `<button>` with `aria-expanded`
- Each answer panel has `role="region"` and `aria-labelledby`
- Enter/Space toggles the accordion item
- Focus visible on question buttons

### Production Code
```tsx
import { useState } from 'react';

interface FAQItem { question: string; answer: string; }

export function FAQAccordion({ items, title }: { items: FAQItem[]; title: string }) {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-12">{title}</h2>
        <div className="divide-y divide-gray-200">
          {items.map((item, i) => (
            <div key={i}>
              <button
                onClick={() => setOpenIndex(openIndex === i ? null : i)}
                aria-expanded={openIndex === i}
                className="flex w-full items-center justify-between py-5 text-left text-lg font-medium text-gray-900 hover:text-blue-600 transition-colors"
              >
                {item.question}
                <svg className={`h-5 w-5 flex-shrink-0 transition-transform ${openIndex === i ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {openIndex === i && (
                <div className="pb-5 text-base text-gray-600 leading-relaxed">{item.answer}</div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Variants 16-30: Quick Reference Specs

### 16. Comparison Table
Columns = products/plans, rows = features. Header row sticky on scroll. Checkmark/X icons for boolean features. Text values for specific features. Highlighted column (recommended) with colored border or bg. Responsive: horizontal scroll at md, or card-per-product at sm.

### 17. Masonry Grid
Pinterest-style layout using CSS columns or masonry polyfill. Column count: 3 (xl), 2 (lg), 1 (md). Column gap: 16-24px. Items: variable height cards with images and text. Image loading: lazy with aspect-ratio placeholder.

### 18. Card Carousel
Horizontally scrollable cards with arrow navigation. Container: overflow-hidden with peek (show 20px of next card). Cards: fixed width 300-360px. Gap: 24px. Navigation: left/right arrows (48px circles) at container edges. Dots: below carousel, 8px circles. Touch: swipe enabled.

### 19. Tabbed Content Sections
Horizontal tabs controlling content panels. Tab bar: border-bottom, tabs as buttons. Content: any layout (text, grid, images). Tab count: 3-6 (too many = use dropdown on mobile). Scroll tabs horizontally on mobile.

### 20. Image + Text Side-by-Side
50/50 split. Image: rounded-lg, shadow, 4:3 or 16:10 ratio. Text: vertically centered. Spacing between: 48-80px. Responsive: stacked at md, image on top.

### 21. Full-Width Image with Overlay
Background image covering full section width. Dark overlay 40-60% opacity. Text: white, centered. Max-width for text: 640px. Min-height: 400-500px. Image: object-fit cover, loading lazy.

### 22. Rich Text Block (Article Content)
Single column, max-width 680px, centered. Prose styling: paragraphs with 1.7 line-height, 18px. Headings: H2 at 32px, H3 at 24px. Lists: indented, disc/decimal. Images: full-width within column, rounded-lg. Code: inline with bg-gray-100, block with syntax highlighting.

### 23. Callout/Highlight Box
Colored background panel within content. Left border: 4px brand color. Padding: 24-32px. Icon: optional, left of text. Background: blue-50, yellow-50, red-50, green-50 for different types (info, warning, error, success). Border-radius: 8-12px.

### 24. Download/Resource Block
Card with file icon + title + description + download button. File type icon: PDF, CSV, ZIP, etc. File size displayed. Button: "Download" with download arrow icon. Grid: 2-3 columns for multiple resources.

### 25. Newsletter Inline
Email input + submit button in a section. Max-width: 480px. Input: 48px height, 16px font. Button: same height, brand color. Privacy note: 12px text below. Background: gray-50 or brand-tinted. Can include a heading and brief value prop above.

### 26. Author Bio Block
Avatar (64-80px, rounded-full) + name (18px bold) + bio (16px, 2-3 lines) + social links. Horizontal layout: avatar left, text right. Background: gray-50 or white with border. Padding: 24-32px. Used after blog posts.

### 27. Related Content
3 cards of related posts/resources. Same card format as Blog Post Grid (Variant 14) but with "Related" heading above. Grid: 3-col desktop, 2-col tablet, 1-col mobile. Positioned before footer in blog layouts.

### 28. Table of Contents
Sticky sidebar (position: sticky, top: 80px) with anchor links. Link text: 14px, gray-600, active: blue-600. Active detection: Intersection Observer on content headings. Indentation for H3s under H2s. Mobile: collapsible top banner instead of sidebar.

### 29. Annotated Image
Full-width or contained image with numbered hotspot markers. Markers: 24-32px circles with numbers, brand colored. Click/hover: reveal tooltip with text. Tooltip: white card, shadow, 200px max-width, positioned relative to marker. Mobile: markers become a numbered list below image.

### 30. Collapsible Section
"Read more" / "Show less" toggle for long content. Initial state: shows first 3-4 lines with gradient fade. Button: text-only "Read more" link. Animation: max-height transition. Used for legal text, long descriptions, detailed specs.

---

## Variants 31-60: Extended Content Patterns

### 31. Pros/Cons Block
Two columns: pros (green check icons) and cons (red X icons). Heading: "Pros" / "Cons" with colored icons. Items: 16px text, 12-16px gap between items. Border between columns on desktop, stacked on mobile.

### 32. Key Takeaway Box
Highlighted box within article content. Background: blue-50 or yellow-50. Icon: lightbulb or key. Heading: "Key Takeaway" or "Summary". Text: 16px, slightly indented. Border-radius: 12px. Padding: 24px.

### 33. Statistic Callout
Single large number + context. Number: 48-72px, font-weight 800, brand color. Context: 18px, gray-600, below number. Centered in section. Optional: background card or full-width colored section.

### 34. Embedded Video
Responsive video container. Aspect ratio: 16:9 (padding-top: 56.25% hack or aspect-ratio property). Border-radius: 12px. Shadow: lg. Lazy loading: show thumbnail, load iframe on play click. Source: YouTube, Vimeo, or self-hosted.

### 35. Audio Player Block
Custom audio player. Waveform: horizontal bar with progress indicator. Controls: play/pause (48px), seek bar, time display, volume, speed selector. Background: gray-50 or white card. Height: 80-96px. For podcasts and audio content.

### 36. Embed Block
Responsive iframe container. Set explicit aspect-ratio or min-height. Sources: Google Maps, Calendly, Typeform, CodePen, Figma. Loading: lazy. Border: 1px gray-200. Border-radius: 12px.

### 37. Divider Block
Visual separator between content sections. Variants: simple line (1px gray-200), icon divider (line + centered icon), decorative (wave SVG, dots pattern), whitespace-only (48-96px gap). Full-width or max-width.

### 38. Definition List Block
Term + definition pairs. Term: 16-18px, font-weight 600. Definition: 16px, gray-600, indented or below term. Gap between pairs: 16-24px. Optional: alternate row backgrounds. Max-width: 768px.

### 39. Checklist Block
Vertical list with check icons. Icon: green check circle or checkbox. Text: 16px, left of check icon. Gap: 12-16px between items. Max-width: 640px. Optional: strikethrough for completed items.

### 40. Two-Column FAQ
FAQ questions split into two columns. Column 1: first half of questions. Column 2: second half. Each is an accordion item. Responsive: single column on mobile. More scannable than single-column for 10+ questions.

### 41. FAQ with Categories
Tabs or sidebar nav for FAQ categories. Categories: "General", "Billing", "Technical", etc. Content: accordion FAQ filtered by category. Tab bar: horizontal on desktop, dropdown on mobile.

### 42. FAQ Grid Cards
Questions displayed as cards in a 2-3 column grid. Card: question as heading (16-18px bold) + answer preview (14px, 2 lines) + "Read more" link. Click: expands card or opens modal with full answer.

### 43. Numbered Steps (Horizontal)
Horizontal row of 3-5 steps with connectors. Step: number in circle + title below + optional description. Connector: line or arrow between circles. Responsive: vertical stack on mobile with left-aligned line.

### 44. Case Study Cards
Card grid showcasing customer case studies. Card: cover image (company photo) + company logo + title + key metric result ("40% increase in...") + "Read case study" link. Grid: 2-3 columns. Card shadow: sm, hover: md.

### 45. Icon Wall
Dense grid of small icon + label pairs for listing many features. Grid: 4-6 columns. Each cell: icon (24px) + label (14px). Gap: 16-24px. No descriptions — just scannable feature names. Background: gray-50 or white card.

### 46. Feature with Sticky Visual
Scrolling text on one side, fixed image on the other. As user scrolls through 3-5 text blocks, the image remains visible (position: sticky). Image may change to match current text block. Implementation: Intersection Observer triggers image swap.

### 47. Interactive Feature Demo
Live product preview that responds to UI controls. Tabs or buttons trigger different states in a demo UI. Demo: embedded iframe, screenshot swap, or animated mockup. Great for showing product in action.

### 48. Feature with Code
Split layout: description left, syntax-highlighted code right. Code block: dark bg (#1E1E1E), monospace 14px, language tab, copy button. Used by developer tools and API products. Responsive: stacked, code below text.

### 49. Feature Marquee
Continuously scrolling horizontal strip of feature icons or badges. Animation: CSS translateX, infinite loop, 20-40s duration. Pause on hover. Duplicate content for seamless loop. Used for integration logos, tech stack, or feature tags.

### 50. Feature with Toggle
Toggle/switch between two views of a feature. Before/after, light/dark mode, basic/advanced view. Toggle: centered switch or button group. Content transitions with fade. Used for product comparisons or mode demonstrations.

### 51-55. Table Variants
51. **Simple Table**: Headers + rows, alternating row backgrounds, sortable headers (click to sort).
52. **Responsive Table**: Horizontal scroll on mobile with sticky first column.
53. **Card Table**: Each row becomes a card on mobile, label-value pairs stacked.
54. **Expandable Table**: Click row to reveal detail panel below.
55. **Filterable Table**: Filter controls above table (search, dropdowns, checkboxes).

### 56-60. Specialized Content
56. **Before/After Image Slider**: Draggable handle splits two overlapping images. Range input controls position.
57. **Pricing Feature Matrix**: Detailed grid of features vs. plans. Sticky header row. Check/X or text values per cell.
58. **Roadmap Timeline**: Horizontal or vertical timeline of planned features. Status: completed, in progress, planned. Interactive: click to expand details.
59. **Changelog**: Reverse-chronological list of updates. Each entry: version badge + date + title + description + tags (feature, fix, improvement).
60. **Code Playground**: Live code editor with preview. Editor: Monaco or CodeMirror. Preview: live iframe. Tabs for HTML/CSS/JS. Used for documentation and developer products.

---

## Content Block Performance Optimization

1. **Lazy load all images below the fold** using `loading="lazy"` attribute
2. **Use `content-visibility: auto`** on off-screen sections for rendering performance
3. **Defer non-critical JavaScript** — accordion, carousel, and tab interactions can load after paint
4. **Use CSS containment** (`contain: layout style paint`) on repeating card elements
5. **Optimize images**: WebP/AVIF, responsive srcset, explicit width/height
6. **Skeleton loading**: Show placeholder shapes while content loads in data-driven blocks
7. **Intersection Observer**: Trigger animations and lazy loading efficiently
8. **Font loading**: Ensure content fonts use `font-display: swap` to prevent invisible text
