# Container Query Patterns — 30+ Component-Level Responsive Patterns

Container queries allow components to respond to their own container's size rather than the viewport. This is the correct model for reusable components: a card component should adapt identically whether it is in a narrow sidebar or a wide main content area.

---

## Fundamentals

### Establishing Containment

```css
/* Inline-size containment (most common — responds to width) */
.container {
  container-type: inline-size;
}

/* Named container (required for targeted queries) */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Shorthand */
.card-wrapper {
  container: card / inline-size;
}

/* Size containment (responds to both width and height) */
.panel {
  container-type: size;
  container-name: panel;
}

/* Normal containment (style queries only, no size queries) */
.theme-region {
  container-type: normal;
  container-name: theme;
}
```

### Container Query Syntax

```css
/* Query by container name */
@container card (min-width: 400px) {
  .card-title { font-size: 1.25rem; }
}

/* Query nearest ancestor container (unnamed) */
@container (min-width: 600px) {
  .widget { flex-direction: row; }
}

/* Range syntax */
@container card (300px <= width <= 600px) {
  .card { padding: 1rem; }
}

/* Combined conditions */
@container card (min-width: 400px) and (max-width: 799px) {
  .card { /* tablet-like layout */ }
}
```

### Container Query Units

```css
/* cqi = 1% of container's inline size (width in horizontal writing modes) */
.card-title {
  font-size: clamp(0.875rem, 4cqi, 1.5rem);
}

/* cqw = 1% of container width */
.card-image {
  height: min(200px, 40cqw);
}

/* cqh = 1% of container height (requires container-type: size) */
.panel-content {
  padding: 2cqh 3cqi;
}

/* cqmin / cqmax = smaller/larger of cqi and cqb */
.responsive-icon {
  width: clamp(16px, 5cqmin, 32px);
  height: clamp(16px, 5cqmin, 32px);
}
```

---

## Pattern 1: Adaptive Card Component

The most common container query pattern. A card that switches from vertical (stacked) to horizontal (side-by-side) based on its container width.

```css
.card-container {
  container: card / inline-size;
}

/* Narrow: vertical stack */
.card {
  display: flex;
  flex-direction: column;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border);
}

.card__image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  width: 100%;
}

.card__body {
  padding: var(--space-4);
}

.card__meta {
  display: none;
}

/* Medium: horizontal layout */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }

  .card__image {
    width: 40%;
    aspect-ratio: auto;
    flex-shrink: 0;
  }

  .card__body {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
}

/* Wide: full horizontal with metadata */
@container card (min-width: 600px) {
  .card__meta {
    display: flex;
    gap: var(--space-3);
    margin-top: var(--space-2);
    color: var(--text-secondary);
  }

  .card__image {
    width: 35%;
  }

  .card__body {
    padding: var(--space-5);
  }
}

/* Extra wide: add actions row */
@container card (min-width: 800px) {
  .card__actions {
    display: flex;
    gap: var(--space-2);
    margin-top: auto;
    padding-top: var(--space-3);
    border-top: 1px solid var(--border-subtle);
  }
}
```

---

## Pattern 2: Morphing Navigation

Navigation that changes form based on available space. Goes from icon-only to icon+label to full horizontal nav.

```css
.nav-container {
  container: nav / inline-size;
}

/* Narrow: icon-only, vertical */
.nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  padding: var(--space-2);
}

.nav__item {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-2);
  border-radius: var(--radius-md);
  min-width: 40px;
  min-height: 40px;
}

.nav__label {
  display: none;
}

.nav__badge {
  display: none;
}

/* Medium: icon + label */
@container nav (min-width: 180px) {
  .nav__item {
    justify-content: flex-start;
    gap: var(--space-2);
    padding: var(--space-2) var(--space-3);
  }

  .nav__label {
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}

/* Wide: icon + label + badge */
@container nav (min-width: 240px) {
  .nav__badge {
    display: flex;
    margin-left: auto;
    padding: 2px 8px;
    border-radius: var(--radius-full);
    font-size: var(--text-xs);
    background: var(--primary);
    color: var(--on-primary);
  }
}

/* Extra wide: horizontal layout */
@container nav (min-width: 600px) {
  .nav {
    flex-direction: row;
    gap: var(--space-1);
  }
}
```

---

## Pattern 3: Table to Card List Transformation

Data table that transforms into a card list when the container is too narrow for columns.

```css
.table-container {
  container: datatable / inline-size;
}

/* Wide: standard table */
.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th,
.data-table td {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  border-bottom: 1px solid var(--border);
}

.data-table thead {
  display: table-header-group;
}

.data-table tbody tr {
  display: table-row;
}

/* Narrow: card list */
@container datatable (max-width: 600px) {
  .data-table thead {
    display: none;
  }

  .data-table,
  .data-table tbody {
    display: block;
  }

  .data-table tbody tr {
    display: flex;
    flex-direction: column;
    padding: var(--space-4);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    margin-bottom: var(--space-3);
    gap: var(--space-2);
  }

  .data-table td {
    display: flex;
    justify-content: space-between;
    padding: var(--space-1) 0;
    border-bottom: none;
  }

  .data-table td::before {
    content: attr(data-label);
    font-weight: 600;
    color: var(--text-secondary);
    flex-shrink: 0;
    margin-right: var(--space-3);
  }
}
```

---

## Pattern 4: Form Layout Adaptation

Form fields that go from single-column to multi-column based on container width.

```css
.form-container {
  container: form / inline-size;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.form-group label {
  font-size: var(--text-sm);
  font-weight: 500;
}

/* Medium: two columns */
@container form (min-width: 500px) {
  .form-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .form-group--full {
    grid-column: 1 / -1;
  }
}

/* Wide: label beside input */
@container form (min-width: 700px) {
  .form-group--inline {
    flex-direction: row;
    align-items: center;
    gap: var(--space-4);
  }

  .form-group--inline label {
    min-width: 120px;
    flex-shrink: 0;
  }
}

/* Extra wide: three columns for short fields */
@container form (min-width: 900px) {
  .form-grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .form-group--half {
    grid-column: span 2;
  }

  .form-group--full {
    grid-column: 1 / -1;
  }
}
```

---

## Pattern 5: Chart Container Responsiveness

Charts that adapt their presentation based on container size.

```css
.chart-container {
  container: chart / inline-size;
}

.chart {
  width: 100%;
  position: relative;
}

/* Narrow: simplified view */
.chart__legend {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  font-size: var(--text-xs);
  justify-content: center;
  margin-top: var(--space-3);
}

.chart__axis-label {
  font-size: 10px;
}

.chart__tooltip-detail {
  display: none;
}

/* Medium: show more detail */
@container chart (min-width: 400px) {
  .chart__axis-label {
    font-size: 12px;
  }

  .chart__tooltip-detail {
    display: block;
  }
}

/* Wide: legend to the side */
@container chart (min-width: 600px) {
  .chart__wrapper {
    display: flex;
    gap: var(--space-4);
  }

  .chart__legend {
    flex-direction: column;
    flex-wrap: nowrap;
    width: 150px;
    flex-shrink: 0;
    margin-top: 0;
    justify-content: flex-start;
  }
}

/* Extra wide: annotations and gridlines */
@container chart (min-width: 800px) {
  .chart__annotations {
    display: block;
  }

  .chart__gridlines--minor {
    display: block;
  }
}
```

---

## Pattern 6: Profile / User Card

User card component that adapts from compact to detailed.

```css
.profile-container {
  container: profile / inline-size;
}

/* Compact: avatar + name only */
.profile {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2);
}

.profile__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex-shrink: 0;
}

.profile__name {
  font-size: var(--text-sm);
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.profile__role,
.profile__bio,
.profile__stats,
.profile__actions {
  display: none;
}

/* Medium: show role */
@container profile (min-width: 200px) {
  .profile__avatar {
    width: 40px;
    height: 40px;
  }

  .profile__role {
    display: block;
    font-size: var(--text-xs);
    color: var(--text-secondary);
  }

  .profile__name-group {
    display: flex;
    flex-direction: column;
  }
}

/* Wide: full card layout */
@container profile (min-width: 350px) {
  .profile {
    flex-direction: column;
    text-align: center;
    padding: var(--space-5);
    gap: var(--space-3);
  }

  .profile__avatar {
    width: 64px;
    height: 64px;
  }

  .profile__bio {
    display: block;
    font-size: var(--text-sm);
    color: var(--text-secondary);
    line-height: 1.5;
  }

  .profile__stats {
    display: flex;
    gap: var(--space-4);
    justify-content: center;
    padding-top: var(--space-3);
    border-top: 1px solid var(--border);
  }

  .profile__actions {
    display: flex;
    gap: var(--space-2);
    width: 100%;
  }
}
```

---

## Pattern 7: Notification / Alert Component

Alert that expands detail based on available space.

```css
.alert-container {
  container: alert / inline-size;
}

.alert {
  display: flex;
  align-items: flex-start;
  gap: var(--space-2);
  padding: var(--space-3);
  border-radius: var(--radius-md);
  border: 1px solid var(--border);
}

.alert__icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.alert__content {
  flex: 1;
  min-width: 0;
}

.alert__title {
  font-weight: 600;
  font-size: var(--text-sm);
}

.alert__description {
  display: none;
}

.alert__actions {
  display: none;
}

.alert__dismiss {
  flex-shrink: 0;
}

/* Medium: show description */
@container alert (min-width: 400px) {
  .alert {
    padding: var(--space-4);
    gap: var(--space-3);
  }

  .alert__description {
    display: block;
    font-size: var(--text-sm);
    color: var(--text-secondary);
    margin-top: var(--space-1);
  }
}

/* Wide: show inline actions */
@container alert (min-width: 600px) {
  .alert {
    align-items: center;
  }

  .alert__actions {
    display: flex;
    gap: var(--space-2);
    flex-shrink: 0;
    margin-left: auto;
  }
}
```

---

## Pattern 8: Search Input Component

Search input that expands capabilities based on space.

```css
.search-container {
  container: search / inline-size;
}

/* Compact: icon button only */
.search {
  display: flex;
  align-items: center;
}

.search__input-group {
  display: none;
}

.search__icon-trigger {
  display: flex;
  width: 40px;
  height: 40px;
  align-items: center;
  justify-content: center;
}

/* Medium: visible input */
@container search (min-width: 200px) {
  .search__input-group {
    display: flex;
    align-items: center;
    flex: 1;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: var(--space-2) var(--space-3);
    gap: var(--space-2);
  }

  .search__icon-trigger {
    display: none;
  }

  .search__input {
    flex: 1;
    border: none;
    outline: none;
    background: transparent;
  }
}

/* Wide: input with filter buttons */
@container search (min-width: 400px) {
  .search__filters {
    display: flex;
    gap: var(--space-1);
    margin-left: var(--space-2);
  }
}

/* Extra wide: input with advanced toggle */
@container search (min-width: 600px) {
  .search__advanced-toggle {
    display: block;
    margin-left: var(--space-2);
  }
}
```

---

## Pattern 9: Pricing Tier Card

Pricing card that shows more detail as space allows.

```css
.pricing-container {
  container: pricing / inline-size;
}

.pricing-card {
  padding: var(--space-4);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
}

.pricing-card__name {
  font-weight: 700;
}

.pricing-card__price {
  font-size: clamp(1.5rem, 5cqi, 2.5rem);
  font-weight: 700;
  margin: var(--space-2) 0;
}

.pricing-card__features {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.pricing-card__feature--secondary {
  display: none;
}

.pricing-card__comparison {
  display: none;
}

/* Medium: show all features */
@container pricing (min-width: 280px) {
  .pricing-card {
    padding: var(--space-5);
  }

  .pricing-card__feature--secondary {
    display: flex;
  }
}

/* Wide: show comparison details */
@container pricing (min-width: 350px) {
  .pricing-card__comparison {
    display: block;
    margin-top: var(--space-4);
    padding-top: var(--space-4);
    border-top: 1px solid var(--border);
  }
}
```

---

## Pattern 10: Media Player Controls

Player controls that add features as container grows.

```css
.player-container {
  container: player / inline-size;
}

/* Compact: play/pause + progress only */
.player {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2);
  background: var(--surface-raised);
  border-radius: var(--radius-md);
}

.player__play-pause {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
}

.player__progress {
  flex: 1;
  height: 4px;
  border-radius: 2px;
  background: var(--border);
}

.player__time,
.player__volume,
.player__speed,
.player__fullscreen,
.player__track-info {
  display: none;
}

/* Medium: add time display */
@container player (min-width: 300px) {
  .player__time {
    display: block;
    font-size: var(--text-xs);
    white-space: nowrap;
    font-variant-numeric: tabular-nums;
  }
}

/* Wide: add volume and track info */
@container player (min-width: 500px) {
  .player__volume {
    display: flex;
    align-items: center;
    gap: var(--space-1);
    width: 100px;
  }

  .player__track-info {
    display: block;
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
}

/* Extra wide: full controls */
@container player (min-width: 700px) {
  .player__speed {
    display: block;
  }

  .player__fullscreen {
    display: block;
  }

  .player {
    padding: var(--space-3) var(--space-4);
  }
}
```

---

## Pattern 11: Comment / Reply Thread

Comments that show more context in wider containers.

```css
.thread-container {
  container: thread / inline-size;
}

.comment {
  display: flex;
  gap: var(--space-2);
  padding: var(--space-3);
}

.comment__avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  flex-shrink: 0;
}

.comment__reactions,
.comment__reply-preview {
  display: none;
}

/* Medium: larger avatar, show reactions */
@container thread (min-width: 400px) {
  .comment__avatar {
    width: 36px;
    height: 36px;
  }

  .comment__reactions {
    display: flex;
    gap: var(--space-1);
    margin-top: var(--space-2);
  }
}

/* Wide: show reply previews inline */
@container thread (min-width: 600px) {
  .comment {
    gap: var(--space-3);
    padding: var(--space-4);
  }

  .comment__reply-preview {
    display: block;
    margin-top: var(--space-3);
    padding-left: var(--space-4);
    border-left: 2px solid var(--border);
    color: var(--text-secondary);
    font-size: var(--text-sm);
  }
}
```

---

## Pattern 12: Badge / Status Indicator

Badge that expands from dot to icon to icon+text.

```css
.badge-container {
  container: badge / inline-size;
}

/* Minimal: colored dot */
.badge {
  display: inline-flex;
  align-items: center;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--status-color);
}

.badge__icon,
.badge__text {
  display: none;
}

/* Medium: icon badge */
@container badge (min-width: 32px) {
  .badge {
    width: 20px;
    height: 20px;
    justify-content: center;
  }

  .badge__icon {
    display: block;
    width: 12px;
    height: 12px;
  }
}

/* Wide: icon + text */
@container badge (min-width: 80px) {
  .badge {
    width: auto;
    height: auto;
    border-radius: var(--radius-full);
    padding: 2px 10px 2px 6px;
    gap: var(--space-1);
  }

  .badge__text {
    display: block;
    font-size: var(--text-xs);
    white-space: nowrap;
  }
}
```

---

## Pattern 13: Sidebar Widget

Widget for sidebars that compacts when space is limited.

```css
.widget-container {
  container: widget / inline-size;
}

.widget {
  padding: var(--space-3);
  border-radius: var(--radius-lg);
  background: var(--surface-raised);
}

.widget__title {
  font-size: var(--text-sm);
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.widget__list-item {
  padding: var(--space-2) 0;
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.widget__item-meta,
.widget__item-action,
.widget__footer {
  display: none;
}

/* Medium: show metadata */
@container widget (min-width: 250px) {
  .widget {
    padding: var(--space-4);
  }

  .widget__item-meta {
    display: block;
    font-size: var(--text-xs);
    color: var(--text-secondary);
    margin-left: auto;
  }
}

/* Wide: show actions and footer */
@container widget (min-width: 350px) {
  .widget__item-action {
    display: block;
    margin-left: var(--space-2);
  }

  .widget__footer {
    display: flex;
    justify-content: center;
    padding-top: var(--space-3);
    margin-top: var(--space-3);
    border-top: 1px solid var(--border);
  }
}
```

---

## Pattern 14: Toolbar / Action Bar

Container-responsive toolbar that shows or hides actions.

```css
.toolbar-container {
  container: toolbar / inline-size;
}

.toolbar {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2);
}

.toolbar__primary {
  display: flex;
  gap: var(--space-1);
}

.toolbar__secondary {
  display: none;
}

.toolbar__divider {
  display: none;
}

.toolbar__overflow {
  display: flex;
  margin-left: auto;
}

/* Medium: show divider and some secondary actions */
@container toolbar (min-width: 400px) {
  .toolbar__divider {
    display: block;
    width: 1px;
    height: 24px;
    background: var(--border);
    margin: 0 var(--space-2);
  }

  .toolbar__secondary {
    display: flex;
    gap: var(--space-1);
  }

  .toolbar__secondary .toolbar__action:nth-child(n+3) {
    display: none;
  }
}

/* Wide: show all actions, hide overflow */
@container toolbar (min-width: 600px) {
  .toolbar__secondary .toolbar__action {
    display: flex;
  }

  .toolbar__overflow {
    display: none;
  }
}
```

---

## Pattern 15: Product Listing Card

E-commerce product card that adapts to container width.

```css
.product-container {
  container: product / inline-size;
}

/* Narrow: compact grid card */
.product-card {
  display: flex;
  flex-direction: column;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border);
}

.product-card__image {
  aspect-ratio: 1 / 1;
  object-fit: cover;
  width: 100%;
}

.product-card__info {
  padding: var(--space-3);
}

.product-card__title {
  font-size: var(--text-sm);
  font-weight: 500;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-card__rating,
.product-card__variants,
.product-card__quick-add {
  display: none;
}

/* Medium: show rating and price more prominently */
@container product (min-width: 200px) {
  .product-card__info {
    padding: var(--space-4);
  }

  .product-card__rating {
    display: flex;
    align-items: center;
    gap: var(--space-1);
    font-size: var(--text-xs);
    margin-top: var(--space-1);
  }

  .product-card__price {
    font-size: var(--text-md);
    font-weight: 700;
    margin-top: var(--space-2);
  }
}

/* Wide: horizontal layout with variants */
@container product (min-width: 400px) {
  .product-card {
    flex-direction: row;
  }

  .product-card__image {
    width: 40%;
    aspect-ratio: auto;
  }

  .product-card__variants {
    display: flex;
    gap: var(--space-1);
    margin-top: var(--space-2);
  }

  .product-card__quick-add {
    display: block;
    margin-top: var(--space-3);
  }
}
```

---

## Pattern 16: Calendar / Date Display

Calendar component that adapts view based on container.

```css
.calendar-container {
  container: calendar / inline-size;
}

/* Narrow: list view of events */
.calendar {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.calendar__grid {
  display: none;
}

.calendar__list {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

/* Medium: compact month grid */
@container calendar (min-width: 300px) {
  .calendar__grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 1px;
  }

  .calendar__list {
    display: none;
  }

  .calendar__day {
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--text-sm);
  }

  .calendar__day-events {
    display: none; /* No room for event indicators */
  }
}

/* Wide: month grid with event dots */
@container calendar (min-width: 500px) {
  .calendar__day {
    aspect-ratio: auto;
    min-height: 60px;
    flex-direction: column;
    align-items: flex-start;
    padding: var(--space-1);
  }

  .calendar__day-events {
    display: flex;
    gap: 2px;
    flex-wrap: wrap;
  }

  .calendar__event-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }
}

/* Extra wide: full event previews */
@container calendar (min-width: 700px) {
  .calendar__day {
    min-height: 100px;
    padding: var(--space-2);
  }

  .calendar__event-preview {
    display: block;
    font-size: var(--text-xs);
    padding: 1px 4px;
    border-radius: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}
```

---

## Pattern 17: Stat / Metric Card

Dashboard metric card that adds sparkline and detail in wider containers.

```css
.metric-container {
  container: metric / inline-size;
}

/* Compact: value only */
.metric-card {
  padding: var(--space-3);
  border-radius: var(--radius-lg);
  background: var(--surface-raised);
}

.metric-card__label {
  font-size: var(--text-xs);
  color: var(--text-secondary);
}

.metric-card__value {
  font-size: clamp(1.25rem, 5cqi, 2rem);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.metric-card__change,
.metric-card__sparkline,
.metric-card__breakdown {
  display: none;
}

/* Medium: show change indicator */
@container metric (min-width: 200px) {
  .metric-card {
    padding: var(--space-4);
  }

  .metric-card__change {
    display: inline-flex;
    align-items: center;
    gap: 2px;
    font-size: var(--text-xs);
    margin-top: var(--space-1);
  }
}

/* Wide: show sparkline */
@container metric (min-width: 300px) {
  .metric-card__sparkline {
    display: block;
    height: 40px;
    margin-top: var(--space-3);
  }
}

/* Extra wide: show breakdown */
@container metric (min-width: 400px) {
  .metric-card__breakdown {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
    margin-top: var(--space-3);
    padding-top: var(--space-3);
    border-top: 1px solid var(--border);
    font-size: var(--text-sm);
  }
}
```

---

## Pattern 18: File / Document Card

File card showing progressive detail.

```css
.file-container {
  container: file / inline-size;
}

/* Icon + name */
.file-card {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2);
  border-radius: var(--radius-md);
}

.file-card__icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.file-card__name {
  flex: 1;
  min-width: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: var(--text-sm);
}

.file-card__size,
.file-card__date,
.file-card__preview,
.file-card__actions {
  display: none;
}

/* Medium: show size */
@container file (min-width: 250px) {
  .file-card__size {
    display: block;
    font-size: var(--text-xs);
    color: var(--text-secondary);
    flex-shrink: 0;
  }
}

/* Wide: show date and actions */
@container file (min-width: 400px) {
  .file-card {
    padding: var(--space-3);
    gap: var(--space-3);
  }

  .file-card__date {
    display: block;
    font-size: var(--text-xs);
    color: var(--text-secondary);
    flex-shrink: 0;
  }

  .file-card__actions {
    display: flex;
    gap: var(--space-1);
    flex-shrink: 0;
  }
}

/* Extra wide: show thumbnail preview */
@container file (min-width: 500px) {
  .file-card__icon {
    display: none;
  }

  .file-card__preview {
    display: block;
    width: 48px;
    height: 48px;
    border-radius: var(--radius-sm);
    object-fit: cover;
    flex-shrink: 0;
  }
}
```

---

## Pattern 19: Style Queries (Container Style Queries)

Style queries let you query CSS custom property values on a container, enabling theme-based adaptation.

```css
/* Container with a theme custom property */
.section {
  container-type: normal;
  container-name: section;
}

.section--dark {
  --theme: dark;
  background: var(--surface-dark);
}

.section--light {
  --theme: light;
  background: var(--surface-light);
}

/* Style query: adapt component based on section theme */
@container section style(--theme: dark) {
  .card {
    background: var(--surface-raised-dark);
    color: var(--text-on-dark);
    border-color: var(--border-dark);
  }

  .button--primary {
    background: var(--primary-light);
    color: var(--primary-dark);
  }
}

@container section style(--theme: light) {
  .card {
    background: white;
    color: var(--text-primary);
    border-color: var(--border);
  }
}
```

---

## Pattern 20: Fallback Strategies for Older Browsers

```css
/* Feature detection with @supports */
.card-container {
  /* Fallback: use media queries */
}

@supports (container-type: inline-size) {
  .card-container {
    container-type: inline-size;
    container-name: card;
  }
}

/* Fallback layout using media queries */
.card {
  flex-direction: column;
}

@media (min-width: 600px) {
  .card {
    flex-direction: row;
  }
}

/* Enhanced layout using container queries (overrides media query when supported) */
@supports (container-type: inline-size) {
  @container card (min-width: 400px) {
    .card {
      flex-direction: row;
    }
  }

  /* Reset the media query override since container query handles it */
  @media (min-width: 600px) {
    .card {
      flex-direction: column; /* Reset — let container query decide */
    }
  }
}
```

**Progressive enhancement pattern (recommended):**

```css
/* 1. Base styles: work everywhere */
.card { flex-direction: column; }

/* 2. Media query fallback: reasonable default for older browsers */
@media (min-width: 768px) {
  .card:not(.cq-enhanced) { flex-direction: row; }
}

/* 3. Container query: precise adaptation for modern browsers */
@supports (container-type: inline-size) {
  .card-container { container: card / inline-size; }
  .card { flex-direction: column; } /* Reset to let CQ take over */

  @container card (min-width: 400px) {
    .card { flex-direction: row; }
  }
}
```

---

## Pattern 21: Container Query Naming Conventions

Consistent naming makes container queries maintainable across large codebases.

```css
/* Convention: container name matches component name or layout role */

/* Layout containers */
.layout-main    { container: layout-main / inline-size; }
.layout-sidebar { container: layout-sidebar / inline-size; }
.layout-panel   { container: layout-panel / inline-size; }

/* Component containers */
.card-container     { container: card / inline-size; }
.table-container    { container: table / inline-size; }
.form-container     { container: form / inline-size; }
.nav-container      { container: nav / inline-size; }
.chart-container    { container: chart / inline-size; }

/* Breakpoint tokens for container queries (conceptual consistency) */
/*
  Narrow:  < 300px
  Compact: 300px - 499px
  Medium:  500px - 699px
  Wide:    700px - 899px
  Full:    900px+
*/

@container card (min-width: 300px) { /* compact */ }
@container card (min-width: 500px) { /* medium */ }
@container card (min-width: 700px) { /* wide */ }
@container card (min-width: 900px) { /* full */ }
```

---

## Patterns 22-30: Quick Reference

### Pattern 22: Responsive Accordion (container-aware)
```css
.accordion-container { container: accordion / inline-size; }

@container accordion (min-width: 600px) {
  .accordion { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
  .accordion__item { border: 1px solid var(--border); border-radius: var(--radius-lg); }
}
```

### Pattern 23: Responsive Tag Input
```css
.tag-input-container { container: taginput / inline-size; }

@container taginput (max-width: 300px) {
  .tag-input__tags { max-height: 60px; overflow-y: auto; }
  .tag-input__tag { font-size: var(--text-xs); }
}
```

### Pattern 24: Responsive Avatar Group
```css
.avatar-group-container { container: avatars / inline-size; }

.avatar-group { display: flex; }
.avatar-group__item { margin-left: -8px; width: 28px; height: 28px; }
.avatar-group__overflow { display: none; }

@container avatars (min-width: 200px) {
  .avatar-group__item { width: 36px; height: 36px; margin-left: -10px; }
}

@container avatars (min-width: 300px) {
  .avatar-group__item { width: 40px; height: 40px; }
  .avatar-group__overflow { display: flex; font-size: var(--text-sm); }
}
```

### Pattern 25: Responsive Timeline Entry
```css
.timeline-container { container: timeline / inline-size; }

@container timeline (min-width: 500px) {
  .timeline-entry { flex-direction: row; gap: var(--space-4); }
  .timeline-entry__timestamp { min-width: 100px; flex-shrink: 0; text-align: right; }
}
```

### Pattern 26: Responsive Breadcrumb
```css
.breadcrumb-container { container: breadcrumb / inline-size; }

@container breadcrumb (max-width: 400px) {
  .breadcrumb__item:not(:first-child):not(:last-child) { display: none; }
  .breadcrumb__ellipsis { display: inline; }
}
```

### Pattern 27: Responsive Footer Widget
```css
.footer-widget-container { container: footerwidget / inline-size; }

@container footerwidget (min-width: 400px) {
  .footer-widget__links { columns: 2; }
}

@container footerwidget (min-width: 600px) {
  .footer-widget { display: flex; gap: var(--space-6); }
  .footer-widget__links { columns: auto; }
}
```

### Pattern 28: Responsive Notification Toast
```css
.toast-container { container: toast / inline-size; }

@container toast (min-width: 400px) {
  .toast { flex-direction: row; align-items: center; }
  .toast__action { margin-left: auto; white-space: nowrap; }
}
```

### Pattern 29: Responsive Code Block
```css
.code-container { container: code / inline-size; }

@container code (min-width: 500px) {
  .code-block { font-size: var(--text-sm); }
  .code-block__line-numbers { display: block; }
}

@container code (min-width: 700px) {
  .code-block__copy-button { display: flex; position: absolute; top: 8px; right: 8px; }
  .code-block__language-tag { display: block; }
}
```

### Pattern 30: Responsive Testimonial Card
```css
.testimonial-container { container: testimonial / inline-size; }

.testimonial { padding: var(--space-4); }
.testimonial__photo { display: none; }

@container testimonial (min-width: 300px) {
  .testimonial { padding: var(--space-5); }
  .testimonial__photo { display: block; width: 48px; height: 48px; border-radius: 50%; }
  .testimonial__author { display: flex; align-items: center; gap: var(--space-3); }
}

@container testimonial (min-width: 500px) {
  .testimonial { display: flex; gap: var(--space-5); }
  .testimonial__photo { width: 64px; height: 64px; }
  .testimonial__quote { font-size: var(--text-md); }
}
```
