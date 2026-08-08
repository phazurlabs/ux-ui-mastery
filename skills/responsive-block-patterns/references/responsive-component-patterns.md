# Responsive Component Patterns — 50+ Patterns with Production Code

Production-ready responsive component patterns with CSS and React code for every common UI element.

---

## Pattern 1: Responsive Typography (Fluid + Stepped)

### Fluid Approach (Preferred)

```css
/* Fluid type that scales smoothly between breakpoints */
.heading-display {
  font-size: clamp(2rem, 1rem + 5vw, 4.5rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
  font-weight: 800;
}

.heading-page {
  font-size: clamp(1.5rem, 0.75rem + 3.75vw, 3rem);
  line-height: 1.15;
  letter-spacing: -0.015em;
}

.heading-section {
  font-size: clamp(1.25rem, 0.875rem + 1.875vw, 2rem);
  line-height: 1.2;
  letter-spacing: -0.01em;
}

.body-large {
  font-size: clamp(1.125rem, 1rem + 0.625vw, 1.375rem);
  line-height: 1.5;
}

.body-default {
  font-size: clamp(1rem, 0.9375rem + 0.3125vw, 1.125rem);
  line-height: 1.6;
}

.caption {
  font-size: clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem);
  line-height: 1.4;
  letter-spacing: 0.01em;
}
```

### Stepped Approach (When Precise Control Needed)

```css
.heading-display {
  font-size: 2rem;
  line-height: 1.15;
}

@media (min-width: 480px) {
  .heading-display { font-size: 2.5rem; line-height: 1.1; }
}

@media (min-width: 768px) {
  .heading-display { font-size: 3rem; }
}

@media (min-width: 1024px) {
  .heading-display { font-size: 3.75rem; }
}

@media (min-width: 1440px) {
  .heading-display { font-size: 4.5rem; line-height: 1.05; }
}
```

### React Component

```tsx
interface TypographyProps {
  as?: 'h1' | 'h2' | 'h3' | 'h4' | 'p' | 'span';
  variant: 'display' | 'page' | 'section' | 'body-lg' | 'body' | 'caption';
  children: React.ReactNode;
  className?: string;
}

const variantMap = {
  display: 'heading-display',
  page: 'heading-page',
  section: 'heading-section',
  'body-lg': 'body-large',
  body: 'body-default',
  caption: 'caption',
};

export function Typography({ as: Tag = 'p', variant, children, className = '' }: TypographyProps) {
  return <Tag className={`${variantMap[variant]} ${className}`}>{children}</Tag>;
}
```

---

## Pattern 2: Responsive Images (srcset, sizes, art direction)

### Resolution Switching (Same Crop, Different Sizes)

```html
<img
  src="photo-800.jpg"
  srcset="
    photo-400.jpg 400w,
    photo-800.jpg 800w,
    photo-1200.jpg 1200w,
    photo-1600.jpg 1600w,
    photo-2400.jpg 2400w
  "
  sizes="
    (min-width: 1280px) 600px,
    (min-width: 768px) 50vw,
    100vw
  "
  alt="Product photograph"
  loading="lazy"
  decoding="async"
  width="800"
  height="600"
/>
```

### Art Direction (Different Crops for Different Sizes)

```html
<picture>
  <!-- Wide: landscape crop -->
  <source
    media="(min-width: 1024px)"
    srcset="hero-landscape-1200.webp 1200w, hero-landscape-2400.webp 2400w"
    sizes="100vw"
    type="image/webp"
  />
  <!-- Medium: square crop -->
  <source
    media="(min-width: 480px)"
    srcset="hero-square-600.webp 600w, hero-square-1200.webp 1200w"
    sizes="100vw"
    type="image/webp"
  />
  <!-- Small: portrait crop (face-focused) -->
  <source
    srcset="hero-portrait-400.webp 400w, hero-portrait-800.webp 800w"
    sizes="100vw"
    type="image/webp"
  />
  <img
    src="hero-landscape-800.jpg"
    alt="Hero image"
    loading="eager"
    fetchpriority="high"
    width="1200"
    height="800"
  />
</picture>
```

### React Component

```tsx
interface ResponsiveImageProps {
  src: string;
  alt: string;
  widths: number[];
  sizes: string;
  aspect?: string;
  priority?: boolean;
  className?: string;
}

export function ResponsiveImage({
  src,
  alt,
  widths,
  sizes,
  aspect = '16 / 9',
  priority = false,
  className = '',
}: ResponsiveImageProps) {
  const basePath = src.replace(/\.[^.]+$/, '');
  const ext = src.match(/\.[^.]+$/)?.[0] ?? '.jpg';

  const srcSet = widths.map((w) => `${basePath}-${w}w.webp ${w}w`).join(', ');

  return (
    <picture>
      <source srcSet={srcSet} sizes={sizes} type="image/webp" />
      <img
        src={src}
        alt={alt}
        loading={priority ? 'eager' : 'lazy'}
        fetchPriority={priority ? 'high' : 'auto'}
        decoding="async"
        className={className}
        style={{ aspectRatio: aspect, objectFit: 'cover', width: '100%' }}
      />
    </picture>
  );
}
```

---

## Pattern 3: Responsive Tables — 4 Strategies

### Strategy A: Horizontal Scroll

```css
.table-scroll-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
}

.table-scroll-wrapper table {
  min-width: 640px;
  width: 100%;
  border-collapse: collapse;
}

.table-scroll-wrapper th,
.table-scroll-wrapper td {
  padding: var(--space-sm) var(--space-md);
  text-align: left;
  white-space: nowrap;
  border-bottom: 1px solid var(--border);
}

/* Scroll shadow hints */
.table-scroll-wrapper {
  background:
    linear-gradient(to right, var(--surface) 30%, transparent) left center,
    linear-gradient(to left, var(--surface) 30%, transparent) right center;
  background-size: 40px 100%;
  background-repeat: no-repeat;
  background-attachment: local;
}
```

### Strategy B: Stack to Cards

```css
.table-stack {
  width: 100%;
  border-collapse: collapse;
}

.table-stack th,
.table-stack td {
  padding: var(--space-sm) var(--space-md);
  border-bottom: 1px solid var(--border);
}

@media (max-width: 767px) {
  .table-stack thead {
    display: none;
  }

  .table-stack tr {
    display: block;
    padding: var(--space-md);
    margin-bottom: var(--space-sm);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
  }

  .table-stack td {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--space-xs) 0;
    border-bottom: 1px solid var(--border-subtle);
  }

  .table-stack td:last-child {
    border-bottom: none;
  }

  .table-stack td::before {
    content: attr(data-label);
    font-weight: 600;
    font-size: var(--text-sm);
    color: var(--text-secondary);
    flex-shrink: 0;
    margin-right: var(--space-md);
  }
}
```

### Strategy C: Hide Columns Progressively

```css
.table-progressive th,
.table-progressive td {
  padding: var(--space-sm) var(--space-md);
}

/* Priority classes: p1 always visible, p2 from md, p3 from lg */
.table-progressive .col-p2 { display: none; }
.table-progressive .col-p3 { display: none; }

@media (min-width: 768px) {
  .table-progressive .col-p2 { display: table-cell; }
}

@media (min-width: 1024px) {
  .table-progressive .col-p3 { display: table-cell; }
}
```

### Strategy D: Collapse Rows (Expandable Detail)

```css
.table-collapse tr {
  cursor: pointer;
}

.table-collapse .row-detail {
  display: none;
}

.table-collapse tr[data-expanded="true"] + .row-detail {
  display: table-row;
}

@media (min-width: 1024px) {
  .table-collapse .row-detail {
    display: none; /* On desktop, all data visible in columns */
  }

  .table-collapse .col-detail {
    display: table-cell; /* Show inline instead */
  }
}
```

### React Table Component

```tsx
interface Column<T> {
  key: keyof T;
  label: string;
  priority: 1 | 2 | 3;
  render?: (value: T[keyof T], row: T) => React.ReactNode;
}

interface ResponsiveTableProps<T> {
  data: T[];
  columns: Column<T>[];
  strategy?: 'scroll' | 'stack' | 'progressive' | 'collapse';
}

export function ResponsiveTable<T extends Record<string, unknown>>({
  data,
  columns,
  strategy = 'stack',
}: ResponsiveTableProps<T>) {
  return (
    <div className={`table-wrapper table-${strategy}`}>
      <table className={`table-${strategy}`}>
        <thead>
          <tr>
            {columns.map((col) => (
              <th key={String(col.key)} className={`col-p${col.priority}`}>
                {col.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              {columns.map((col) => (
                <td
                  key={String(col.key)}
                  className={`col-p${col.priority}`}
                  data-label={col.label}
                >
                  {col.render ? col.render(row[col.key], row) : String(row[col.key])}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

---

## Pattern 4: Responsive Navigation

### Hamburger to Horizontal

```css
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-sm) var(--space-md);
  position: sticky;
  top: 0;
  background: var(--surface);
  z-index: 100;
}

.nav__logo {
  flex-shrink: 0;
}

.nav__menu-button {
  display: flex;
  width: 44px;
  height: 44px;
  align-items: center;
  justify-content: center;
}

.nav__links {
  position: fixed;
  inset: 0;
  background: var(--surface);
  display: flex;
  flex-direction: column;
  padding: 80px var(--space-lg) var(--space-lg);
  gap: var(--space-xs);
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.32, 0.72, 0, 1);
  z-index: 99;
  overflow-y: auto;
}

.nav__links[data-open="true"] {
  transform: translateX(0);
}

.nav__link {
  padding: var(--space-sm) var(--space-md);
  font-size: var(--text-md);
  border-radius: var(--radius-md);
}

@media (min-width: 768px) {
  .nav__menu-button { display: none; }

  .nav__links {
    position: static;
    flex-direction: row;
    padding: 0;
    gap: var(--space-2xs);
    transform: none;
    transition: none;
    background: transparent;
    overflow: visible;
  }

  .nav__link {
    padding: var(--space-xs) var(--space-sm);
    font-size: var(--text-sm);
  }
}
```

### Bottom Tab Bar to Top Nav

```css
.app-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-around;
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: var(--space-2xs) 0;
  padding-bottom: max(var(--space-2xs), env(safe-area-inset-bottom));
  z-index: 100;
}

.app-nav__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: var(--space-2xs) var(--space-xs);
  font-size: 10px;
  min-width: 48px;
  min-height: 48px;
  justify-content: center;
  color: var(--text-secondary);
}

.app-nav__item[aria-current="page"] {
  color: var(--primary);
}

@media (min-width: 768px) {
  .app-nav {
    position: sticky;
    top: 0;
    bottom: auto;
    justify-content: flex-start;
    border-top: none;
    border-bottom: 1px solid var(--border);
    padding: 0 var(--space-lg);
    gap: var(--space-2xs);
  }

  .app-nav__item {
    flex-direction: row;
    gap: var(--space-xs);
    font-size: var(--text-sm);
    padding: var(--space-sm) var(--space-md);
    min-height: 44px;
  }
}
```

### React Navigation Component

```tsx
import { useState, useEffect } from 'react';

interface NavItem {
  label: string;
  href: string;
  icon?: React.ReactNode;
}

interface ResponsiveNavProps {
  logo: React.ReactNode;
  items: NavItem[];
  cta?: { label: string; href: string };
}

export function ResponsiveNav({ logo, items, cta }: ResponsiveNavProps) {
  const [isOpen, setIsOpen] = useState(false);

  // Close menu on resize to desktop
  useEffect(() => {
    const mq = window.matchMedia('(min-width: 768px)');
    const handler = () => { if (mq.matches) setIsOpen(false); };
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);

  // Lock body scroll when menu is open
  useEffect(() => {
    document.body.style.overflow = isOpen ? 'hidden' : '';
    return () => { document.body.style.overflow = ''; };
  }, [isOpen]);

  return (
    <nav className="nav" role="navigation" aria-label="Main navigation">
      <div className="nav__logo">{logo}</div>

      <button
        className="nav__menu-button"
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
        aria-controls="nav-links"
        aria-label={isOpen ? 'Close menu' : 'Open menu'}
      >
        {isOpen ? <CloseIcon /> : <MenuIcon />}
      </button>

      <div
        id="nav-links"
        className="nav__links"
        data-open={isOpen}
        role="menubar"
      >
        {items.map((item) => (
          <a
            key={item.href}
            href={item.href}
            className="nav__link"
            role="menuitem"
            onClick={() => setIsOpen(false)}
          >
            {item.icon && <span className="nav__link-icon">{item.icon}</span>}
            {item.label}
          </a>
        ))}
        {cta && (
          <a href={cta.href} className="nav__cta button button--primary">
            {cta.label}
          </a>
        )}
      </div>
    </nav>
  );
}
```

---

## Pattern 5: Responsive Forms

```css
.form {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-md);
  max-width: 720px;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}

.form-field__label {
  font-size: var(--text-sm);
  font-weight: 500;
}

.form-field__input {
  height: 48px;
  padding: 0 var(--space-sm);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  font-size: 16px; /* Prevents iOS zoom */
}

.form-field__input:focus {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
  border-color: var(--primary);
}

.form-field__helper {
  font-size: var(--text-xs);
  color: var(--text-secondary);
}

.form-field__error {
  font-size: var(--text-xs);
  color: var(--error);
}

.form__actions {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.form__actions .button {
  width: 100%;
}

/* Two-column on larger screens */
@media (min-width: 640px) {
  .form {
    grid-template-columns: repeat(2, 1fr);
  }

  .form-field--full {
    grid-column: 1 / -1;
  }

  .form__actions {
    grid-column: 1 / -1;
    flex-direction: row;
    justify-content: flex-end;
  }

  .form__actions .button {
    width: auto;
  }
}

/* Inline labels on wide screens */
@media (min-width: 1024px) {
  .form-field--inline {
    flex-direction: row;
    align-items: center;
    gap: var(--space-md);
  }

  .form-field--inline .form-field__label {
    min-width: 120px;
    flex-shrink: 0;
    text-align: right;
  }

  .form-field--inline .form-field__input {
    height: 40px;
  }
}
```

---

## Pattern 6: Responsive Cards (Vertical to Horizontal)

```css
.card {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: box-shadow 0.2s ease;
}

.card__image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  width: 100%;
}

.card__body {
  padding: var(--space-md);
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
  flex: 1;
}

.card__title {
  font-size: var(--text-md);
  font-weight: 600;
  line-height: 1.3;
}

.card__description {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card__footer {
  margin-top: auto;
  padding-top: var(--space-sm);
  border-top: 1px solid var(--border-subtle);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Horizontal variant on wider containers */
@container card-container (min-width: 480px) {
  .card--adaptive {
    flex-direction: row;
  }

  .card--adaptive .card__image {
    width: 40%;
    aspect-ratio: auto;
    flex-shrink: 0;
  }

  .card--adaptive .card__body {
    padding: var(--space-lg);
  }
}

/* Hover effects for pointer devices */
@media (hover: hover) {
  .card:hover {
    box-shadow: var(--shadow-md);
  }
}
```

### React Card Component

```tsx
interface CardProps {
  image?: { src: string; alt: string };
  title: string;
  description?: string;
  footer?: React.ReactNode;
  href?: string;
  adaptive?: boolean;
}

export function Card({ image, title, description, footer, href, adaptive = true }: CardProps) {
  const Wrapper = href ? 'a' : 'div';
  const wrapperProps = href ? { href } : {};

  return (
    <div className="card-container" style={{ containerType: 'inline-size', containerName: 'card-container' }}>
      <Wrapper className={`card ${adaptive ? 'card--adaptive' : ''}`} {...wrapperProps}>
        {image && (
          <img
            className="card__image"
            src={image.src}
            alt={image.alt}
            loading="lazy"
            decoding="async"
          />
        )}
        <div className="card__body">
          <h3 className="card__title">{title}</h3>
          {description && <p className="card__description">{description}</p>}
          {footer && <div className="card__footer">{footer}</div>}
        </div>
      </Wrapper>
    </div>
  );
}
```

---

## Pattern 7: Responsive Modals

```css
/* Overlay */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.2s ease;
}

/* Modal */
.modal {
  background: var(--surface);
  width: 100%;
  max-height: 100dvh;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  animation: slideUp 0.3s cubic-bezier(0.32, 0.72, 0, 1);
}

.modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-md) var(--space-lg);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  background: var(--surface);
  z-index: 1;
}

.modal__body {
  padding: var(--space-lg);
}

.modal__footer {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  padding: var(--space-md) var(--space-lg);
  border-top: 1px solid var(--border);
  position: sticky;
  bottom: 0;
  background: var(--surface);
}

.modal__footer .button {
  width: 100%;
}

/* Drag handle for mobile */
.modal__drag-handle {
  display: block;
  width: 36px;
  height: 4px;
  background: var(--border);
  border-radius: 2px;
  margin: var(--space-xs) auto 0;
}

/* Desktop: centered overlay */
@media (min-width: 768px) {
  .modal-overlay {
    align-items: center;
    padding: var(--space-lg);
  }

  .modal {
    max-width: 560px;
    max-height: 85dvh;
    border-radius: var(--radius-xl);
    animation: scaleIn 0.2s ease;
  }

  .modal__drag-handle {
    display: none;
  }

  .modal__footer {
    flex-direction: row;
    justify-content: flex-end;
  }

  .modal__footer .button {
    width: auto;
  }
}

@media (min-width: 1024px) {
  .modal { max-width: 640px; }
}

/* Size variants */
.modal--sm { max-width: 400px; }
.modal--lg { max-width: 800px; }
.modal--xl { max-width: 1000px; }

/* Full-screen on mobile variant */
.modal--fullscreen-mobile {
  border-radius: 0;
  min-height: 100dvh;
}

@media (min-width: 768px) {
  .modal--fullscreen-mobile {
    border-radius: var(--radius-xl);
    min-height: auto;
  }
}

/* Animations */
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes slideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
@keyframes scaleIn { from { transform: scale(0.95); opacity: 0; } to { transform: scale(1); opacity: 1; } }
```

---

## Pattern 8: Responsive Data Visualization

```css
.chart-wrapper {
  container: chart / inline-size;
  width: 100%;
}

.chart {
  width: 100%;
  aspect-ratio: 4 / 3;
}

@container chart (min-width: 600px) {
  .chart {
    aspect-ratio: 16 / 9;
  }
}

.chart__legend {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-xs) var(--space-md);
  justify-content: center;
  margin-top: var(--space-sm);
  font-size: var(--text-xs);
}

@container chart (min-width: 600px) {
  .chart__container {
    display: flex;
    gap: var(--space-lg);
  }

  .chart__legend {
    flex-direction: column;
    flex-wrap: nowrap;
    width: 140px;
    flex-shrink: 0;
    margin-top: 0;
    justify-content: flex-start;
  }
}

/* Axis labels */
.chart__x-label {
  font-size: 10px;
}

@container chart (min-width: 400px) {
  .chart__x-label { font-size: 11px; }
}

@container chart (min-width: 600px) {
  .chart__x-label { font-size: 12px; }
}

/* Simplify on small sizes */
@container chart (max-width: 400px) {
  .chart__gridlines { display: none; }
  .chart__annotations { display: none; }
  .chart__y-axis-label:nth-child(odd) { display: none; }
}
```

---

## Pattern 9: Touch Target Scaling

```css
/* Base: accessible touch targets for all devices */
.interactive {
  min-height: 44px;
  min-width: 44px;
}

/* Touch devices: larger targets */
@media (pointer: coarse) {
  .interactive {
    min-height: 48px;
    min-width: 48px;
  }

  /* Extend touch area without changing visual size */
  .interactive--padded {
    position: relative;
  }

  .interactive--padded::after {
    content: "";
    position: absolute;
    inset: -8px;
  }

  /* List items need more height */
  .list-item {
    min-height: 56px;
    padding: var(--space-sm) var(--space-md);
  }

  /* Increase spacing between tappable elements */
  .button-group {
    gap: var(--space-sm);
  }

  .link-list a {
    padding: var(--space-xs) 0;
  }
}

/* Precise pointer: compact targets */
@media (pointer: fine) {
  .interactive {
    min-height: 32px;
    min-width: 32px;
  }

  .list-item {
    min-height: 36px;
    padding: var(--space-xs) var(--space-md);
  }

  .button-group {
    gap: var(--space-xs);
  }
}

/* Hover capability detection */
@media (hover: hover) {
  .interactive:hover {
    background: var(--hover-overlay);
  }

  .card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
  }

  .link:hover {
    text-decoration: underline;
  }
}

@media (hover: none) {
  .interactive:active {
    background: var(--active-overlay);
  }

  .card:active {
    box-shadow: var(--shadow-md);
  }
}
```

---

## Pattern 10: Focus Indicator Scaling

```css
/* Base focus styles — ALWAYS visible for keyboard users */
:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

/* Remove focus ring for mouse/touch users */
:focus:not(:focus-visible) {
  outline: none;
}

/* Scale focus indicators by context */
.button:focus-visible {
  outline-offset: 2px;
}

.card:focus-visible {
  outline-offset: 4px;
  border-radius: var(--radius-lg);
}

.input:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: -1px; /* Inset for inputs */
  border-color: var(--primary);
}

/* Larger focus ring on touch devices */
@media (pointer: coarse) {
  :focus-visible {
    outline-width: 3px;
    outline-offset: 3px;
  }
}

/* High contrast mode support */
@media (forced-colors: active) {
  :focus-visible {
    outline: 3px solid Highlight;
    outline-offset: 2px;
  }
}
```

---

## Pattern 11: Responsive Grid with Subgrid Alignment

```css
.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-lg);
}

@media (min-width: 640px) {
  .card-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .card-grid { grid-template-columns: repeat(3, 1fr); }
}

/* Subgrid: align card internals across the row */
.card-grid .card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 4; /* image, title, body, action */
  gap: 0;
}

.card-grid .card__image { grid-row: 1; }
.card-grid .card__title { grid-row: 2; padding: var(--space-sm) var(--space-md) 0; }
.card-grid .card__body  { grid-row: 3; padding: var(--space-xs) var(--space-md); }
.card-grid .card__action { grid-row: 4; padding: 0 var(--space-md) var(--space-md); align-self: end; }
```

---

## Pattern 12: Responsive Spacing Utility Classes

```css
/* Responsive padding utilities */
.p-responsive {
  padding: var(--space-md);
}

@media (min-width: 768px) {
  .p-responsive { padding: var(--space-lg); }
}

@media (min-width: 1280px) {
  .p-responsive { padding: var(--space-xl); }
}

/* Section spacing */
.section-padding {
  padding-block: var(--space-4xl);
  padding-inline: var(--space-md);
}

@media (min-width: 768px) {
  .section-padding { padding-inline: var(--space-xl); }
}

/* Container */
.container-responsive {
  width: 100%;
  max-width: var(--max-width-content, 1200px);
  margin-inline: auto;
  padding-inline: var(--space-md);
}

@media (min-width: 768px) {
  .container-responsive { padding-inline: var(--space-lg); }
}

@media (min-width: 1280px) {
  .container-responsive { padding-inline: var(--space-xl); }
}
```

---

## Pattern 13: Responsive Bottom Sheet

```css
.bottom-sheet {
  position: fixed;
  inset: auto 0 0 0;
  z-index: 200;
  background: var(--surface);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  box-shadow: var(--shadow-xl);
  transform: translateY(100%);
  transition: transform 0.3s cubic-bezier(0.32, 0.72, 0, 1);
  max-height: 90dvh;
  display: flex;
  flex-direction: column;
  overscroll-behavior: contain;
}

.bottom-sheet[data-state="open"] {
  transform: translateY(0);
}

.bottom-sheet__handle {
  width: 36px;
  height: 4px;
  border-radius: 2px;
  background: var(--border);
  margin: var(--space-xs) auto var(--space-sm);
  flex-shrink: 0;
}

.bottom-sheet__header {
  padding: 0 var(--space-md) var(--space-sm);
  flex-shrink: 0;
}

.bottom-sheet__body {
  overflow-y: auto;
  padding: 0 var(--space-md) var(--space-md);
  flex: 1;
  padding-bottom: max(var(--space-md), env(safe-area-inset-bottom));
}

/* On desktop: convert to side panel */
@media (min-width: 1024px) {
  .bottom-sheet {
    inset: 0 0 0 auto;
    width: 400px;
    max-height: none;
    border-radius: 0;
    transform: translateX(100%);
  }

  .bottom-sheet[data-state="open"] {
    transform: translateX(0);
  }

  .bottom-sheet__handle {
    display: none;
  }
}
```

---

## Pattern 14: Responsive Skeleton Loading

```css
.skeleton {
  background: var(--surface-raised);
  border-radius: var(--radius-md);
  position: relative;
  overflow: hidden;
}

.skeleton::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.1) 50%,
    transparent 100%
  );
  animation: shimmer 1.5s ease-in-out infinite;
}

@keyframes shimmer {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

/* Skeleton shapes */
.skeleton--text {
  height: 1em;
  width: 100%;
  border-radius: var(--radius-sm);
}

.skeleton--title {
  height: 1.5em;
  width: 60%;
}

.skeleton--avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.skeleton--image {
  aspect-ratio: 16 / 9;
  width: 100%;
}

.skeleton--button {
  height: 40px;
  width: 120px;
  border-radius: var(--radius-md);
}

/* Responsive skeleton card */
.skeleton-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  padding: var(--space-md);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
}

@media (min-width: 768px) {
  .skeleton-card {
    flex-direction: row;
  }

  .skeleton-card .skeleton--image {
    width: 40%;
    flex-shrink: 0;
    aspect-ratio: auto;
  }
}

/* Reduce motion */
@media (prefers-reduced-motion: reduce) {
  .skeleton::after {
    animation: none;
  }
}
```

---

## Pattern 15: Responsive Notification Toast

```css
.toast-container {
  position: fixed;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  pointer-events: none;

  /* Mobile: bottom center, full-width */
  bottom: var(--space-md);
  left: var(--space-md);
  right: var(--space-md);
  align-items: stretch;
}

.toast {
  pointer-events: auto;
  background: var(--surface-raised);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  padding: var(--space-sm) var(--space-md);
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
  animation: toastSlideUp 0.3s ease;
}

.toast__message {
  font-size: var(--text-sm);
}

.toast__actions {
  display: flex;
  gap: var(--space-xs);
}

/* Desktop: bottom-right, fixed width */
@media (min-width: 768px) {
  .toast-container {
    left: auto;
    right: var(--space-lg);
    bottom: var(--space-lg);
    width: 380px;
    align-items: flex-end;
  }

  .toast {
    flex-direction: row;
    align-items: center;
    animation: toastSlideLeft 0.3s ease;
  }

  .toast__message {
    flex: 1;
  }

  .toast__actions {
    flex-shrink: 0;
  }
}

@keyframes toastSlideUp {
  from { transform: translateY(100%); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes toastSlideLeft {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}
```

---

## Patterns 16-25: Responsive Layout Utilities

### Pattern 16: Responsive Stack

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}

@media (min-width: 768px) {
  .stack--row-md {
    flex-direction: row;
    align-items: center;
  }
}

@media (min-width: 1024px) {
  .stack--row-lg {
    flex-direction: row;
    align-items: center;
  }
}
```

### Pattern 17: Responsive Cluster (Flex Wrap)

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm);
  align-items: center;
}

.cluster--center { justify-content: center; }
.cluster--between { justify-content: space-between; }
```

### Pattern 18: Responsive Switcher

Auto-switches from horizontal to vertical when items can't fit.

```css
.switcher {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-md);
}

.switcher > * {
  flex-grow: 1;
  flex-basis: calc((30rem - 100%) * 999);
  /* When container < 30rem, items go full-width (stack) */
  /* When container > 30rem, items share the row */
}
```

### Pattern 19: Responsive Sidebar Layout (Intrinsic)

No media queries needed.

```css
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-lg);
}

.with-sidebar > :first-child {
  flex-basis: 240px;
  flex-grow: 1;
}

.with-sidebar > :last-child {
  flex-basis: 0;
  flex-grow: 999;
  min-inline-size: 60%;
}
```

### Pattern 20: Responsive Center

```css
.center {
  box-sizing: content-box;
  max-inline-size: var(--max-width-content, 1200px);
  margin-inline: auto;
  padding-inline: var(--space-md);
}
```

### Pattern 21: Responsive Cover (Centered Content in Full Viewport)

```css
.cover {
  display: flex;
  flex-direction: column;
  min-block-size: 100dvh;
  padding: var(--space-md);
}

.cover > * {
  margin-block: var(--space-md);
}

.cover > .cover__center {
  margin-block: auto;
}
```

### Pattern 22: Responsive Reel (Horizontal Scroll)

```css
.reel {
  display: flex;
  gap: var(--space-md);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: var(--space-md);
  padding: var(--space-md);
  -webkit-overflow-scrolling: touch;
}

.reel::-webkit-scrollbar { display: none; }

.reel > * {
  flex-shrink: 0;
  scroll-snap-align: start;
}

.reel > .reel__item {
  width: clamp(200px, 40vw, 320px);
}
```

### Pattern 23: Responsive Frame (Aspect Ratio Container)

```css
.frame {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.frame > img,
.frame > video {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.frame--square { aspect-ratio: 1; }
.frame--portrait { aspect-ratio: 3 / 4; }

/* Responsive aspect ratio */
.frame--responsive {
  aspect-ratio: 4 / 3;
}

@media (min-width: 768px) {
  .frame--responsive { aspect-ratio: 16 / 9; }
}

@media (min-width: 1280px) {
  .frame--responsive { aspect-ratio: 21 / 9; }
}
```

### Pattern 24: Responsive Imposter (Overlay Positioning)

```css
.imposter {
  position: fixed;
  /* Mobile: bottom-aligned for thumb reach */
  inset: auto var(--space-md) var(--space-md);
}

@media (min-width: 768px) {
  .imposter {
    /* Desktop: centered */
    inset: 50% auto auto 50%;
    transform: translate(-50%, -50%);
  }
}
```

### Pattern 25: Responsive Grid with Named Lines

```css
.page-grid {
  display: grid;
  grid-template-columns:
    [full-start] var(--space-md)
    [content-start] 1fr
    [content-end] var(--space-md)
    [full-end];
}

@media (min-width: 1024px) {
  .page-grid {
    grid-template-columns:
      [full-start] 1fr
      [wide-start] var(--space-lg)
      [content-start] min(720px, 100%)
      [content-end] var(--space-lg)
      [wide-end] 1fr
      [full-end];
  }
}

.page-grid > * { grid-column: content; }
.page-grid > .wide { grid-column: wide; }
.page-grid > .full { grid-column: full; }
```

---

## Patterns 26-50: Component Quick Reference

### Pattern 26: Responsive Accordion

```css
.accordion { display: flex; flex-direction: column; gap: var(--space-2xs); }
.accordion__trigger { padding: var(--space-sm) var(--space-md); display: flex; justify-content: space-between; align-items: center; width: 100%; min-height: 48px; }
.accordion__content { padding: 0 var(--space-md) var(--space-md); }

@media (min-width: 1024px) {
  .accordion__trigger { min-height: 40px; }
  .accordion--always-open .accordion__content { display: block !important; }
}
```

### Pattern 27: Responsive Popover

```css
.popover { position: fixed; inset: auto 0 0 0; max-height: 80dvh; background: var(--surface); border-radius: var(--radius-xl) var(--radius-xl) 0 0; box-shadow: var(--shadow-xl); overflow-y: auto; }

@media (min-width: 768px) {
  .popover { position: absolute; inset: auto; width: 320px; border-radius: var(--radius-lg); max-height: 400px; }
}
```

### Pattern 28: Responsive Tabs to Accordion

```css
.tabcordion__tab { display: none; }
.tabcordion__trigger { display: flex; }
.tabcordion__panel { display: none; }
.tabcordion__panel[data-state="open"] { display: block; }

@media (min-width: 768px) {
  .tabcordion__tab { display: flex; }
  .tabcordion__trigger { display: none; }
  .tabcordion__panel { display: none; }
  .tabcordion__panel[data-active="true"] { display: block; }
}
```

### Pattern 29: Responsive Chip Group

```css
.chip-group { display: flex; flex-wrap: wrap; gap: var(--space-xs); }
.chip { padding: var(--space-2xs) var(--space-sm); border-radius: var(--radius-full); border: 1px solid var(--border); font-size: var(--text-sm); white-space: nowrap; }

@media (max-width: 479px) {
  .chip-group--scroll { flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch; }
  .chip-group--scroll .chip { flex-shrink: 0; }
}
```

### Pattern 30: Responsive Avatar Stack

```css
.avatar-stack { display: flex; }
.avatar-stack__item { width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--surface); margin-left: -8px; }
.avatar-stack__item:first-child { margin-left: 0; }
.avatar-stack__overflow { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: var(--text-xs); background: var(--surface-raised); margin-left: -8px; }

@media (min-width: 768px) {
  .avatar-stack__item { width: 40px; height: 40px; margin-left: -10px; }
  .avatar-stack__overflow { width: 40px; height: 40px; margin-left: -10px; }
}
```

### Pattern 31: Responsive Progress Steps

```css
.steps { display: flex; flex-direction: column; gap: var(--space-md); }
.step { display: flex; gap: var(--space-sm); align-items: flex-start; }
.step__number { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }

@media (min-width: 768px) {
  .steps { flex-direction: row; }
  .step { flex-direction: column; align-items: center; text-align: center; flex: 1; }
}
```

### Pattern 32: Responsive Badge

```css
.badge { display: inline-flex; align-items: center; gap: var(--space-2xs); padding: 2px 8px; border-radius: var(--radius-full); font-size: var(--text-xs); white-space: nowrap; }

@media (max-width: 479px) {
  .badge--dot-mobile { width: 8px; height: 8px; padding: 0; overflow: hidden; text-indent: -9999px; }
}
```

### Pattern 33: Responsive Divider

```css
.divider { border: none; height: 1px; background: var(--border); margin: var(--space-md) 0; }

@media (min-width: 768px) {
  .divider--responsive { margin: var(--space-lg) 0; }
  .divider--vertical { width: 1px; height: auto; margin: 0 var(--space-md); align-self: stretch; }
}
```

### Pattern 34: Responsive Empty State

```css
.empty-state { display: flex; flex-direction: column; align-items: center; text-align: center; padding: var(--space-3xl) var(--space-md); gap: var(--space-md); }
.empty-state__illustration { width: clamp(120px, 30vw, 280px); }
.empty-state__title { font-size: var(--text-lg); }
.empty-state__description { font-size: var(--text-sm); color: var(--text-secondary); max-width: 400px; }
.empty-state__action { width: 100%; max-width: 280px; }
```

### Pattern 35: Responsive FAB (Floating Action Button)

```css
.fab { position: fixed; bottom: calc(var(--space-md) + 64px); /* Above bottom nav */ right: var(--space-md); width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: var(--shadow-lg); z-index: 50; }

@media (min-width: 768px) {
  .fab { bottom: var(--space-lg); right: var(--space-lg); }
  .fab--extended { border-radius: var(--radius-xl); width: auto; padding: 0 var(--space-lg); gap: var(--space-xs); }
  .fab--extended .fab__label { display: inline; }
}
```

### Patterns 36-50: Compact Reference

```css
/* 36: Responsive Breadcrumb */
.breadcrumb { display: flex; gap: var(--space-2xs); font-size: var(--text-sm); overflow: hidden; }
@media (max-width: 767px) { .breadcrumb__item--collapse { display: none; } .breadcrumb__ellipsis { display: inline; } }
@media (min-width: 768px) { .breadcrumb__ellipsis { display: none; } }

/* 37: Responsive Search Bar */
.search-bar { display: flex; align-items: center; }
.search-bar__input { flex: 1; height: 48px; font-size: 16px; }
@media (min-width: 768px) { .search-bar__input { height: 40px; font-size: 14px; } .search-bar__filters { display: flex; } }

/* 38: Responsive Tag Cloud */
.tag-cloud { display: flex; flex-wrap: wrap; gap: var(--space-xs); }
@media (max-width: 479px) { .tag-cloud { overflow-x: auto; flex-wrap: nowrap; } .tag-cloud > * { flex-shrink: 0; } }

/* 39: Responsive Stat Card */
.stat-card { padding: var(--space-md); }
.stat-card__value { font-size: clamp(1.5rem, 4cqi, 2.5rem); font-weight: 700; }
@container (min-width: 250px) { .stat-card__sparkline { display: block; } }

/* 40: Responsive Timeline */
.timeline { padding-left: var(--space-md); border-left: 2px solid var(--border); }
@media (min-width: 1024px) { .timeline { padding-left: 0; border-left: none; display: flex; border-top: 2px solid var(--border); padding-top: var(--space-md); overflow-x: auto; } }

/* 41: Responsive File Upload */
.upload-zone { border: 2px dashed var(--border); border-radius: var(--radius-lg); padding: var(--space-lg); text-align: center; }
@media (pointer: coarse) { .upload-zone { padding: var(--space-md); } .upload-zone__drag-text { display: none; } }

/* 42: Responsive Color Swatch Grid */
.swatch-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(40px, 1fr)); gap: var(--space-2xs); }
@media (min-width: 768px) { .swatch-grid { grid-template-columns: repeat(auto-fill, minmax(56px, 1fr)); gap: var(--space-xs); } }

/* 43: Responsive Toggle Group */
.toggle-group { display: inline-flex; border: 1px solid var(--border); border-radius: var(--radius-md); overflow: hidden; }
.toggle-group__item { padding: var(--space-xs) var(--space-sm); min-height: 40px; min-width: 40px; }
@media (min-width: 768px) { .toggle-group__item { min-height: 32px; min-width: auto; padding: var(--space-2xs) var(--space-md); } .toggle-group__label { display: inline; } }

/* 44: Responsive Meter / Progress */
.meter { width: 100%; height: 8px; border-radius: 4px; background: var(--surface-raised); overflow: hidden; }
.meter__fill { height: 100%; border-radius: 4px; transition: width 0.3s ease; }
@media (min-width: 768px) { .meter { height: 6px; } .meter--with-label { display: flex; align-items: center; gap: var(--space-sm); } .meter--with-label .meter { flex: 1; } }

/* 45: Responsive Banner */
.banner { display: flex; flex-direction: column; gap: var(--space-xs); padding: var(--space-sm) var(--space-md); text-align: center; }
@media (min-width: 768px) { .banner { flex-direction: row; align-items: center; justify-content: center; gap: var(--space-md); text-align: left; } }

/* 46: Responsive Callout Box */
.callout { padding: var(--space-md); border-radius: var(--radius-lg); border-left: 4px solid var(--primary); }
@media (min-width: 768px) { .callout { padding: var(--space-lg); display: flex; gap: var(--space-md); align-items: flex-start; } }

/* 47: Responsive Cookie Banner */
.cookie-banner { position: fixed; bottom: 0; left: 0; right: 0; padding: var(--space-md); background: var(--surface); border-top: 1px solid var(--border); display: flex; flex-direction: column; gap: var(--space-sm); z-index: 9999; }
@media (min-width: 768px) { .cookie-banner { flex-direction: row; align-items: center; padding: var(--space-sm) var(--space-lg); } .cookie-banner__text { flex: 1; } .cookie-banner__actions { flex-shrink: 0; } }

/* 48: Responsive Inline Edit */
.inline-edit { display: flex; align-items: center; gap: var(--space-xs); min-height: 40px; }
.inline-edit__input { flex: 1; }
@media (pointer: coarse) { .inline-edit { min-height: 48px; } }

/* 49: Responsive Key-Value Pair */
.kv-pair { display: flex; flex-direction: column; gap: var(--space-2xs); }
.kv-pair__key { font-size: var(--text-xs); color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; }
@media (min-width: 768px) { .kv-pair { flex-direction: row; gap: var(--space-md); } .kv-pair__key { min-width: 120px; flex-shrink: 0; } }

/* 50: Responsive Code Block */
.code-block { overflow-x: auto; border-radius: var(--radius-lg); padding: var(--space-md); font-size: var(--text-sm); line-height: 1.6; }
.code-block__line-numbers { display: none; }
.code-block__copy { display: none; }
@media (min-width: 768px) { .code-block { font-size: var(--text-sm); } .code-block__line-numbers { display: block; } .code-block__copy { display: flex; position: absolute; top: var(--space-xs); right: var(--space-xs); } }
```
