# Responsive Layout Recipes — 40+ Production-Ready Patterns

Complete CSS Grid and Flexbox code for every common layout, tested across all breakpoints.

---

## Recipe 1: Single Column to 2-Col to 3-Col to 4-Col Grid

The most fundamental responsive layout. Content cards start stacked and progressively fill more columns.

```css
.progressive-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

@media (min-width: 480px) {
  .progressive-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .progressive-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-6);
  }
}

@media (min-width: 1440px) {
  .progressive-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

**Zero-query alternative using RAM:**

```css
.progressive-grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
  gap: var(--space-4);
}
```

---

## Recipe 2: Sidebar Layout (Collapse to Top on Mobile)

Sidebar sits alongside main content on desktop. On mobile, it collapses above main content or becomes a toggle-able drawer.

```css
.sidebar-layout {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-areas:
    "sidebar"
    "main";
  gap: var(--space-4);
}

@media (min-width: 1024px) {
  .sidebar-layout {
    grid-template-columns: 280px 1fr;
    grid-template-areas:
      "sidebar main";
    gap: var(--space-8);
  }
}

.sidebar-layout__sidebar { grid-area: sidebar; }
.sidebar-layout__main { grid-area: main; }
```

**Variant — sidebar collapses to bottom on mobile:**

```css
.sidebar-layout--bottom-mobile {
  grid-template-areas:
    "main"
    "sidebar";
}

@media (min-width: 1024px) {
  .sidebar-layout--bottom-mobile {
    grid-template-areas: "sidebar main";
    grid-template-columns: 280px 1fr;
  }
}
```

---

## Recipe 3: Holy Grail Layout

Header, footer, main content, left sidebar, and right aside. The classic five-region layout.

```css
.holy-grail {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-areas:
    "header"
    "nav"
    "main"
    "aside"
    "footer";
  min-height: 100dvh;
  gap: var(--space-4);
}

@media (min-width: 768px) {
  .holy-grail {
    grid-template-columns: 200px 1fr;
    grid-template-areas:
      "header header"
      "nav    main"
      "nav    aside"
      "footer footer";
  }
}

@media (min-width: 1024px) {
  .holy-grail {
    grid-template-columns: 220px 1fr 260px;
    grid-template-areas:
      "header header header"
      "nav    main   aside"
      "footer footer footer";
    grid-template-rows: auto 1fr auto;
  }
}

.holy-grail__header { grid-area: header; }
.holy-grail__nav    { grid-area: nav; }
.holy-grail__main   { grid-area: main; }
.holy-grail__aside  { grid-area: aside; }
.holy-grail__footer { grid-area: footer; }
```

---

## Recipe 4: Dashboard Card Grid

Dashboard with metric cards that reflow. Cards have varying spans on larger screens.

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

@media (min-width: 480px) {
  .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .dashboard-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-6);
  }
}

.dashboard-grid__card--featured { grid-column: 1 / -1; }

@media (min-width: 480px) {
  .dashboard-grid__card--featured { grid-column: span 2; }
}

.dashboard-grid__card--chart { grid-column: 1 / -1; }

@media (min-width: 1024px) {
  .dashboard-grid__card--chart { grid-column: span 3; }
}
```

---

## Recipe 5: Split Screen (Stack on Mobile)

Two equal halves side-by-side on desktop, stacked vertically on mobile.

```css
.split-screen {
  display: grid;
  grid-template-columns: 1fr;
  min-height: 100dvh;
}

@media (min-width: 768px) {
  .split-screen { grid-template-columns: 1fr 1fr; }
}

.split-screen__left {
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.split-screen__right {
  min-height: 50dvh;
}

@media (min-width: 768px) {
  .split-screen__right { min-height: auto; }
}

/* Variant: 40/60 split */
@media (min-width: 768px) {
  .split-screen--40-60 { grid-template-columns: 2fr 3fr; }
}

/* Variant: reverse order on mobile */
.split-screen--reverse-mobile .split-screen__left { order: 2; }
.split-screen--reverse-mobile .split-screen__right { order: 1; }

@media (min-width: 768px) {
  .split-screen--reverse-mobile .split-screen__left { order: 1; }
  .split-screen--reverse-mobile .split-screen__right { order: 2; }
}
```

---

## Recipe 6: Full-Bleed Section with Constrained Content

Section background goes edge-to-edge. Content inside is centered and width-constrained.

```css
.full-bleed {
  width: 100%;
  padding-block: var(--space-12);
  padding-inline: var(--space-4);
}

@media (min-width: 768px) {
  .full-bleed { padding-inline: var(--space-8); }
}

.full-bleed__content {
  max-width: 1200px;
  margin-inline: auto;
}

/* Alternative: CSS grid full-bleed trick */
.full-bleed-grid {
  display: grid;
  grid-template-columns:
    1fr
    min(1200px, calc(100% - var(--space-8)))
    1fr;
}

.full-bleed-grid > * { grid-column: 2; }
.full-bleed-grid > .breakout { grid-column: 1 / -1; }
```

---

## Recipe 7: Sticky Sidebar with Scrollable Main

```css
.sticky-sidebar-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
}

@media (min-width: 1024px) {
  .sticky-sidebar-layout {
    grid-template-columns: 280px 1fr;
    align-items: start;
  }
}

@media (min-width: 1024px) {
  .sticky-sidebar-layout__sidebar {
    position: sticky;
    top: var(--space-4);
    max-height: calc(100dvh - var(--space-8));
    overflow-y: auto;
    overscroll-behavior: contain;
  }
}

.sticky-sidebar-layout__main {
  min-width: 0;
}
```

---

## Recipe 8: Masonry to Single Column

```css
.masonry-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

@media (min-width: 480px) {
  .masonry-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .masonry-grid { grid-template-columns: repeat(3, 1fr); }
}

/* CSS native masonry (Chrome 128+) */
@supports (grid-template-rows: masonry) {
  @media (min-width: 480px) {
    .masonry-grid { grid-template-rows: masonry; }
  }
}

/* Fallback using columns */
@supports not (grid-template-rows: masonry) {
  @media (min-width: 480px) {
    .masonry-grid--fallback {
      display: block;
      columns: 2;
      column-gap: var(--space-4);
    }
    .masonry-grid--fallback > * {
      break-inside: avoid;
      margin-bottom: var(--space-4);
    }
  }
  @media (min-width: 1024px) {
    .masonry-grid--fallback { columns: 3; }
  }
}
```

---

## Recipe 9: Tab Bar (Mobile) to Horizontal Navigation (Desktop)

```css
.app-nav {
  display: flex;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: var(--space-1) var(--space-2);
  z-index: 100;
  justify-content: space-around;
}

.app-nav__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: var(--space-1);
  font-size: var(--text-xs);
  min-width: 48px;
  min-height: 48px;
  justify-content: center;
}

@media (min-width: 768px) {
  .app-nav {
    position: static;
    flex-direction: row;
    border-top: none;
    border-bottom: 1px solid var(--border);
    padding: 0 var(--space-6);
    justify-content: flex-start;
    gap: var(--space-1);
  }

  .app-nav__item {
    flex-direction: row;
    gap: var(--space-2);
    padding: var(--space-3) var(--space-4);
    font-size: var(--text-sm);
    min-height: 44px;
  }
}
```

---

## Recipe 10: Hamburger Menu (Mobile) to Horizontal Links (Desktop)

```css
.main-nav__links {
  display: none;
  position: fixed;
  inset: 0;
  background: var(--surface);
  flex-direction: column;
  padding: var(--space-16) var(--space-6) var(--space-6);
  gap: var(--space-2);
  z-index: 90;
  overflow-y: auto;
}

.main-nav__links[data-open="true"] { display: flex; }

.main-nav__hamburger {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  z-index: 100;
}

@media (min-width: 768px) {
  .main-nav__links {
    display: flex;
    position: static;
    flex-direction: row;
    padding: 0;
    gap: var(--space-1);
    background: transparent;
    overflow: visible;
  }

  .main-nav__hamburger { display: none; }
}
```

---

## Recipe 11: Bottom Sheet (Mobile) to Side Panel (Desktop)

```css
.panel {
  position: fixed;
  z-index: 200;
  background: var(--surface);
  transition: transform 0.3s ease;
  overflow-y: auto;
  overscroll-behavior: contain;
  inset: auto 0 0 0;
  max-height: 85dvh;
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  transform: translateY(100%);
}

.panel[data-open="true"] { transform: translateY(0); }

.panel__handle {
  display: block;
  width: 36px;
  height: 4px;
  background: var(--border);
  border-radius: 2px;
  margin: var(--space-2) auto var(--space-4);
}

@media (min-width: 1024px) {
  .panel {
    inset: 0 0 0 auto;
    width: 400px;
    max-height: none;
    border-radius: 0;
    transform: translateX(100%);
  }

  .panel[data-open="true"] { transform: translateX(0); }
  .panel__handle { display: none; }
}
```

---

## Recipe 12: Modal — Fullscreen (Mobile) to Centered Overlay (Desktop)

```css
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  z-index: 300;
}

.modal {
  background: var(--surface);
  width: 100%;
  max-height: 100dvh;
  overflow-y: auto;
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  padding: var(--space-6);
}

@media (min-width: 768px) {
  .modal-overlay {
    align-items: center;
    padding: var(--space-6);
  }

  .modal {
    max-width: 560px;
    max-height: 85dvh;
    border-radius: var(--radius-xl);
  }
}

@media (min-width: 1024px) {
  .modal { max-width: 640px; }
}
```

---

## Recipe 13: Drawer — Bottom (Mobile) to Side (Desktop)

```css
.drawer {
  position: fixed;
  z-index: 200;
  background: var(--surface);
  box-shadow: var(--shadow-xl);
  transition: transform 0.3s cubic-bezier(0.32, 0.72, 0, 1);
  overflow-y: auto;
  overscroll-behavior: contain;
  inset: auto 0 0 0;
  max-height: 90dvh;
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  transform: translateY(100%);
  padding: var(--space-4) var(--space-4) var(--space-8);
}

.drawer[data-state="open"] { transform: translateY(0); }

@media (min-width: 1024px) {
  .drawer {
    inset: 0 0 0 auto;
    width: 380px;
    max-height: none;
    border-radius: 0;
    transform: translateX(100%);
    padding: var(--space-6);
  }

  .drawer[data-state="open"] { transform: translateX(0); }
}
```

---

## Recipe 14: Card List — Vertical Stack to Horizontal Cards

```css
.card-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.card-list__item {
  display: flex;
  flex-direction: column;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border);
}

.card-list__image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  width: 100%;
}

@media (min-width: 768px) {
  .card-list__item { flex-direction: row; }

  .card-list__image {
    width: 280px;
    aspect-ratio: auto;
    flex-shrink: 0;
  }
}

@media (min-width: 1280px) {
  .card-list__image { width: 360px; }
}
```

---

## Recipe 15: Feature Grid — Icon + Text Blocks

```css
.feature-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
}

@media (min-width: 480px) {
  .feature-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .feature-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-8);
  }
}

@media (min-width: 1440px) {
  .feature-grid { grid-template-columns: repeat(4, 1fr); }
}

.feature-grid__item {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

@media (min-width: 1024px) {
  .feature-grid__item--horizontal {
    flex-direction: row;
    align-items: flex-start;
  }
}
```

---

## Recipe 16: Pricing Table — Cards to Comparison Table

```css
.pricing {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.pricing__plan {
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
}

@media (min-width: 1024px) {
  .pricing {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0;
  }

  .pricing__plan {
    border-radius: 0;
    border-right: none;
  }

  .pricing__plan:first-child {
    border-radius: var(--radius-lg) 0 0 var(--radius-lg);
  }

  .pricing__plan:last-child {
    border-radius: 0 var(--radius-lg) var(--radius-lg) 0;
    border-right: 1px solid var(--border);
  }

  .pricing__plan {
    display: grid;
    grid-template-rows: subgrid;
    grid-row: span 10;
  }
}
```

---

## Recipe 17: Testimonial Carousel to Grid

```css
.testimonials {
  display: flex;
  gap: var(--space-4);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: var(--space-4);
  -webkit-overflow-scrolling: touch;
}

.testimonials::-webkit-scrollbar { display: none; }

.testimonial-card {
  min-width: 280px;
  max-width: 320px;
  flex-shrink: 0;
  scroll-snap-align: center;
  padding: var(--space-5);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border);
}

@media (min-width: 768px) {
  .testimonials {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    overflow-x: visible;
    scroll-snap-type: none;
  }

  .testimonial-card {
    min-width: auto;
    max-width: none;
  }
}

@media (min-width: 1280px) {
  .testimonials { grid-template-columns: repeat(3, 1fr); }
}
```

---

## Recipe 18: Footer — Stacked to Multi-Column

```css
.footer__columns {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
}

@media (min-width: 480px) {
  .footer__columns { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .footer__columns {
    grid-template-columns: 2fr repeat(3, 1fr);
    gap: var(--space-8);
  }
}

.footer__bottom {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding-top: var(--space-6);
  margin-top: var(--space-6);
  border-top: 1px solid var(--border);
  text-align: center;
}

@media (min-width: 768px) {
  .footer__bottom {
    flex-direction: row;
    justify-content: space-between;
    text-align: left;
  }
}
```

---

## Recipe 19: Hero Section — Centered to Split

```css
.hero {
  display: grid;
  grid-template-columns: 1fr;
  min-height: 80dvh;
  padding: var(--space-8) var(--space-4);
  align-items: center;
  text-align: center;
}

.hero__title {
  font-size: clamp(2rem, 1.4rem + 3vw, 4.5rem);
  line-height: 1.1;
}

.hero__actions {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  margin-top: var(--space-6);
}

@media (min-width: 480px) {
  .hero__actions {
    flex-direction: row;
    justify-content: center;
  }
}

@media (min-width: 1024px) {
  .hero {
    grid-template-columns: 1fr 1fr;
    text-align: left;
    padding: var(--space-12) var(--space-8);
  }

  .hero__actions { justify-content: flex-start; }
}
```

---

## Recipe 20: App Shell — Header + Content + Footer

```css
.app-shell {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100dvh;
}

.app-shell__header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
}

.app-shell__main {
  overflow-y: auto;
  padding: var(--space-4);
}

@media (min-width: 1024px) {
  .app-shell__main { padding: var(--space-6) var(--space-8); }
}

.app-shell__footer {
  border-top: 1px solid var(--border);
}

@media (min-width: 768px) {
  .app-shell__footer { display: none; }
}
```

---

## Recipe 21: Auth / Login Layout

```css
.auth-layout {
  display: grid;
  grid-template-columns: 1fr;
  min-height: 100dvh;
}

.auth-layout__branding { display: none; }

.auth-layout__form-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-6);
}

.auth-layout__form {
  width: 100%;
  max-width: 400px;
}

@media (min-width: 1024px) {
  .auth-layout { grid-template-columns: 1fr 1fr; }

  .auth-layout__branding {
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary);
    color: var(--on-primary);
  }
}
```

---

## Recipe 22: Article + Table of Contents

```css
.article-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
  max-width: 1200px;
  margin-inline: auto;
  padding: var(--space-4);
}

.article-layout__toc { display: none; }

@media (min-width: 1024px) {
  .article-layout {
    grid-template-columns: 1fr 260px;
    padding: var(--space-8);
  }

  .article-layout__toc {
    display: block;
    position: sticky;
    top: var(--space-4);
    align-self: start;
    max-height: calc(100dvh - var(--space-8));
    overflow-y: auto;
  }
}
```

---

## Recipe 23: Image Gallery

```css
.gallery {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-2);
}

@media (min-width: 480px) {
  .gallery { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 768px) {
  .gallery { grid-template-columns: repeat(3, 1fr); gap: var(--space-3); }
}

@media (min-width: 1280px) {
  .gallery { grid-template-columns: repeat(4, 1fr); }
}

.gallery__item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  aspect-ratio: 1 / 1;
}

@media (min-width: 768px) {
  .gallery__item--wide { grid-column: span 2; }
  .gallery__item--tall { grid-row: span 2; }
}
```

---

## Recipe 24: Stat / Metric Row

```css
.stat-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-4);
  text-align: center;
}

@media (min-width: 768px) {
  .stat-row { grid-template-columns: repeat(4, 1fr); }
}

.stat-row__value {
  font-size: clamp(1.5rem, 1rem + 2.5vw, 3rem);
  font-weight: 700;
}
```

---

## Recipe 25: Alert / Notification Bar

```css
.alert-bar {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-4);
  text-align: center;
}

@media (min-width: 768px) {
  .alert-bar {
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: var(--space-4);
    text-align: left;
  }
}
```

---

## Recipe 26: Search Results with Filters

```css
.search-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

.search-layout__filters { display: none; }
.search-layout__filter-toggle { display: block; }

@media (min-width: 1024px) {
  .search-layout {
    grid-template-columns: 260px 1fr;
  }

  .search-layout__filters {
    display: block;
    position: sticky;
    top: var(--space-4);
    align-self: start;
  }

  .search-layout__filter-toggle { display: none; }
}
```

---

## Recipe 27: Timeline — Vertical to Horizontal

```css
.timeline {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
  padding-left: var(--space-6);
  border-left: 2px solid var(--border);
}

.timeline__item {
  position: relative;
}

.timeline__item::before {
  content: "";
  position: absolute;
  left: calc(-1 * var(--space-6) - 5px);
  top: 4px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--primary);
}

@media (min-width: 1024px) {
  .timeline {
    flex-direction: row;
    padding-left: 0;
    border-left: none;
    border-top: 2px solid var(--border);
    padding-top: var(--space-6);
    overflow-x: auto;
    scroll-snap-type: x mandatory;
  }

  .timeline__item {
    min-width: 250px;
    flex-shrink: 0;
    scroll-snap-align: start;
  }

  .timeline__item::before {
    left: 0;
    top: calc(-1 * var(--space-6) - 5px);
  }
}
```

---

## Recipe 28: Breadcrumb — Full to Truncated

```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--text-sm);
  overflow: hidden;
}

.breadcrumb__item--middle { display: none; }
.breadcrumb__ellipsis { display: inline; }

@media (min-width: 768px) {
  .breadcrumb__item--middle { display: inline; }
  .breadcrumb__ellipsis { display: none; }
}
```

---

## Recipe 29: Tabs — Scrollable to Full-Width

```css
.tabs {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  border-bottom: 1px solid var(--border);
  -webkit-overflow-scrolling: touch;
}

.tabs::-webkit-scrollbar { display: none; }

.tab {
  flex-shrink: 0;
  padding: var(--space-3) var(--space-4);
  white-space: nowrap;
  scroll-snap-align: start;
}

@media (min-width: 768px) {
  .tabs { overflow-x: visible; }
  .tab { flex: 1; text-align: center; }
}
```

---

## Recipe 30: Accordion to Expanded Grid

```css
.faq-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.faq-item__answer { display: none; }
.faq-item[open] .faq-item__answer { display: block; }

@media (min-width: 1024px) {
  .faq-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-6);
  }

  .faq-item__answer { display: block; }
  .faq-item__toggle-icon { display: none; }
}
```

---

## Recipe 31: Pagination — Full to Minimal

```css
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-1);
}

.pagination__page { display: none; }
.pagination__page--current,
.pagination__prev,
.pagination__next { display: flex; }
.pagination__info { display: block; margin: 0 var(--space-3); }

@media (min-width: 768px) {
  .pagination__page { display: flex; }
  .pagination__info { display: none; }
}
```

---

## Recipe 32: Settings / Preferences

```css
.settings-layout {
  display: grid;
  grid-template-columns: 1fr;
}

.settings-layout__nav {
  display: flex;
  overflow-x: auto;
  border-bottom: 1px solid var(--border);
}

@media (min-width: 768px) {
  .settings-layout {
    grid-template-columns: 240px 1fr;
    max-width: 1000px;
    margin-inline: auto;
  }

  .settings-layout__nav {
    flex-direction: column;
    overflow-x: visible;
    border-bottom: none;
    border-right: 1px solid var(--border);
  }
}
```

---

## Recipe 33: Media Object

```css
.media-object {
  display: flex;
  gap: var(--space-3);
}

.media-object__avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  flex-shrink: 0;
}

@media (min-width: 768px) {
  .media-object__avatar { width: 48px; height: 48px; }
}

.media-object__content { min-width: 0; }
```

---

## Recipe 34: Command Palette / Spotlight

```css
.spotlight {
  position: fixed;
  z-index: 500;
  inset: 0;
  background: var(--surface);
}

@media (min-width: 768px) {
  .spotlight {
    inset: auto;
    top: 15dvh;
    left: 50%;
    transform: translateX(-50%);
    width: min(600px, calc(100vw - var(--space-8)));
    max-height: 60dvh;
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-2xl);
  }
}
```

---

## Recipe 35: Chip / Tag Cloud

```css
.chip-group {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

@media (max-width: 479px) {
  .chip-group--scroll {
    flex-wrap: nowrap;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
  }

  .chip-group--scroll .chip {
    scroll-snap-align: start;
    flex-shrink: 0;
  }
}
```

---

## Recipe 36: Data Table with Scroll Hint

```css
.table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border-radius: var(--radius-lg);
  border: 1px solid var(--border);
  position: relative;
}

.table-wrapper table {
  min-width: 600px;
  width: 100%;
}

.table-wrapper::after {
  content: "";
  position: absolute;
  top: 0; right: 0; bottom: 0;
  width: 40px;
  background: linear-gradient(to right, transparent, var(--surface));
  pointer-events: none;
}

@media (min-width: 768px) {
  .table-wrapper::after { display: none; }
}
```

---

## Recipe 37: Stepper / Progress Steps

```css
.stepper {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.stepper__step {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
}

@media (min-width: 768px) {
  .stepper {
    flex-direction: row;
    align-items: flex-start;
  }

  .stepper__step {
    flex-direction: column;
    align-items: center;
    text-align: center;
    flex: 1;
  }
}
```

---

## Recipe 38: Side-by-Side Comparison

```css
.comparison {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
}

@media (min-width: 768px) {
  .comparison {
    grid-template-columns: 1fr 1fr;
    gap: var(--space-8);
  }
}
```

---

## Recipe 39: Toolbar with Overflow Menu

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
}

.toolbar__action--secondary { display: none; }
.toolbar__overflow-trigger { display: flex; }

@media (min-width: 768px) {
  .toolbar__action--secondary { display: flex; }
  .toolbar__overflow-trigger { display: none; }
}
```

---

## Recipe 40: Product Detail — Gallery + Info

```css
.product-detail {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
}

.product-detail__gallery {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: var(--space-2);
}

.product-detail__gallery img {
  width: 100%;
  flex-shrink: 0;
  scroll-snap-align: center;
  aspect-ratio: 1 / 1;
  object-fit: cover;
}

@media (min-width: 768px) {
  .product-detail {
    grid-template-columns: 1fr 1fr;
    gap: var(--space-8);
  }

  .product-detail__gallery {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    overflow-x: visible;
  }

  .product-detail__info {
    position: sticky;
    top: var(--space-4);
    align-self: start;
  }
}
```

---

## Recipe 41: Kanban Board

```css
.kanban {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

@media (min-width: 768px) {
  .kanban {
    flex-direction: row;
    overflow-x: auto;
    align-items: flex-start;
  }

  .kanban__column {
    min-width: 300px;
    max-width: 350px;
    flex-shrink: 0;
    max-height: calc(100dvh - 120px);
    overflow-y: auto;
  }
}

@media (min-width: 1280px) {
  .kanban__column {
    flex: 1;
    min-width: 250px;
    max-width: none;
  }
}
```

---

## Recipe 42: Chat / Messaging Layout

```css
.chat-layout {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto 1fr auto;
  height: 100dvh;
}

.chat-layout__sidebar { display: none; }

.chat-layout__messages {
  overflow-y: auto;
  padding: var(--space-4);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.chat-layout__input {
  padding: var(--space-3) var(--space-4);
  border-top: 1px solid var(--border);
  padding-bottom: max(var(--space-3), env(safe-area-inset-bottom));
}

@media (min-width: 768px) {
  .chat-layout {
    grid-template-columns: 320px 1fr;
    grid-template-rows: 1fr auto;
  }

  .chat-layout__sidebar {
    display: flex;
    flex-direction: column;
    grid-row: 1 / -1;
    border-right: 1px solid var(--border);
    overflow-y: auto;
  }
}

@media (min-width: 1280px) {
  .chat-layout { grid-template-columns: 360px 1fr 320px; }
}
```
