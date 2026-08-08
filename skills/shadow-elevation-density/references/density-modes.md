# Density Modes — Complete 3-Mode Density System

## Density Philosophy

Density controls how much information and interaction surface area fits within a given viewport. It is the spatial equivalent of typography's voice — spacious density whispers, compact density shouts data. Neither is inherently better; the right density depends on the user, the task, and the device.

The three canonical modes are:
- **Spacious:** Prioritizes comfort, clarity, and touch interaction
- **Comfortable:** Balances information density with visual breathing room
- **Compact:** Maximizes information per viewport for power users and data-heavy workflows

---

## Complete Density Token Specifications

### Spacious Mode

Designed for touch-first interfaces, casual users, content consumption, onboarding flows, and mobile devices.

```css
[data-density="spacious"] {
  /* Spacing */
  --density-space-xs: 8px;
  --density-space-sm: 12px;
  --density-space-md: 16px;
  --density-space-lg: 24px;
  --density-space-xl: 32px;
  --density-space-2xl: 48px;
  --density-space-3xl: 64px;

  /* Component sizing */
  --density-target-min: 48px;       /* Minimum touch target (Material guideline) */
  --density-target-default: 48px;
  --density-target-large: 56px;
  --density-button-height: 48px;
  --density-input-height: 48px;
  --density-checkbox-size: 24px;
  --density-radio-size: 24px;
  --density-switch-width: 52px;
  --density-switch-height: 32px;

  /* Typography */
  --density-font-xs: 12px;
  --density-font-sm: 14px;
  --density-font-base: 16px;
  --density-font-lg: 18px;
  --density-font-xl: 20px;
  --density-line-height-tight: 1.3;
  --density-line-height-base: 1.6;
  --density-line-height-relaxed: 1.8;
  --density-paragraph-spacing: 24px;

  /* Icons */
  --density-icon-xs: 16px;
  --density-icon-sm: 20px;
  --density-icon-md: 24px;
  --density-icon-lg: 32px;

  /* Padding */
  --density-padding-button-x: 24px;
  --density-padding-button-y: 12px;
  --density-padding-input-x: 16px;
  --density-padding-input-y: 14px;
  --density-padding-card: 24px;
  --density-padding-cell: 16px;
  --density-padding-section: 32px;
  --density-padding-page: 24px;

  /* Gaps */
  --density-gap-inline: 12px;
  --density-gap-stack: 16px;
  --density-gap-form: 24px;
  --density-gap-section: 48px;
  --density-gap-grid: 24px;

  /* Table */
  --density-table-row-height: 64px;
  --density-table-header-height: 56px;
  --density-table-cell-padding-x: 16px;
  --density-table-cell-padding-y: 16px;

  /* List */
  --density-list-item-height: 72px;
  --density-list-item-padding-x: 16px;
  --density-list-item-padding-y: 16px;
  --density-list-avatar-size: 48px;

  /* Navigation */
  --density-nav-item-height: 56px;
  --density-nav-item-padding-x: 20px;
  --density-sidebar-width: 280px;
  --density-topbar-height: 64px;

  /* Modal */
  --density-modal-padding: 32px;
  --density-modal-gap: 24px;
  --density-modal-max-width: 560px;
}
```

### Comfortable Mode (Default)

The balanced default. Works for most web applications, dashboard layouts, and mouse-primary interfaces.

```css
[data-density="comfortable"], :root {
  /* Spacing */
  --density-space-xs: 4px;
  --density-space-sm: 8px;
  --density-space-md: 12px;
  --density-space-lg: 16px;
  --density-space-xl: 24px;
  --density-space-2xl: 32px;
  --density-space-3xl: 48px;

  /* Component sizing */
  --density-target-min: 36px;
  --density-target-default: 40px;
  --density-target-large: 48px;
  --density-button-height: 40px;
  --density-input-height: 40px;
  --density-checkbox-size: 20px;
  --density-radio-size: 20px;
  --density-switch-width: 44px;
  --density-switch-height: 24px;

  /* Typography */
  --density-font-xs: 11px;
  --density-font-sm: 13px;
  --density-font-base: 14px;
  --density-font-lg: 16px;
  --density-font-xl: 18px;
  --density-line-height-tight: 1.25;
  --density-line-height-base: 1.5;
  --density-line-height-relaxed: 1.7;
  --density-paragraph-spacing: 16px;

  /* Icons */
  --density-icon-xs: 14px;
  --density-icon-sm: 16px;
  --density-icon-md: 20px;
  --density-icon-lg: 24px;

  /* Padding */
  --density-padding-button-x: 16px;
  --density-padding-button-y: 8px;
  --density-padding-input-x: 12px;
  --density-padding-input-y: 10px;
  --density-padding-card: 16px;
  --density-padding-cell: 12px;
  --density-padding-section: 24px;
  --density-padding-page: 16px;

  /* Gaps */
  --density-gap-inline: 8px;
  --density-gap-stack: 12px;
  --density-gap-form: 16px;
  --density-gap-section: 32px;
  --density-gap-grid: 16px;

  /* Table */
  --density-table-row-height: 52px;
  --density-table-header-height: 48px;
  --density-table-cell-padding-x: 12px;
  --density-table-cell-padding-y: 10px;

  /* List */
  --density-list-item-height: 56px;
  --density-list-item-padding-x: 12px;
  --density-list-item-padding-y: 10px;
  --density-list-avatar-size: 40px;

  /* Navigation */
  --density-nav-item-height: 44px;
  --density-nav-item-padding-x: 16px;
  --density-sidebar-width: 256px;
  --density-topbar-height: 56px;

  /* Modal */
  --density-modal-padding: 24px;
  --density-modal-gap: 16px;
  --density-modal-max-width: 520px;
}
```

### Compact Mode

Maximum information density. For power users, data tables, admin panels, IDEs, financial interfaces, and complex enterprise tools.

```css
[data-density="compact"] {
  /* Spacing */
  --density-space-xs: 2px;
  --density-space-sm: 4px;
  --density-space-md: 8px;
  --density-space-lg: 12px;
  --density-space-xl: 16px;
  --density-space-2xl: 24px;
  --density-space-3xl: 32px;

  /* Component sizing */
  --density-target-min: 28px;
  --density-target-default: 32px;
  --density-target-large: 40px;
  --density-button-height: 32px;
  --density-input-height: 32px;
  --density-checkbox-size: 16px;
  --density-radio-size: 16px;
  --density-switch-width: 36px;
  --density-switch-height: 20px;

  /* Typography */
  --density-font-xs: 10px;
  --density-font-sm: 11px;
  --density-font-base: 13px;
  --density-font-lg: 14px;
  --density-font-xl: 16px;
  --density-line-height-tight: 1.2;
  --density-line-height-base: 1.4;
  --density-line-height-relaxed: 1.5;
  --density-paragraph-spacing: 12px;

  /* Icons */
  --density-icon-xs: 12px;
  --density-icon-sm: 14px;
  --density-icon-md: 16px;
  --density-icon-lg: 20px;

  /* Padding */
  --density-padding-button-x: 12px;
  --density-padding-button-y: 4px;
  --density-padding-input-x: 8px;
  --density-padding-input-y: 6px;
  --density-padding-card: 12px;
  --density-padding-cell: 8px;
  --density-padding-section: 16px;
  --density-padding-page: 12px;

  /* Gaps */
  --density-gap-inline: 4px;
  --density-gap-stack: 8px;
  --density-gap-form: 12px;
  --density-gap-section: 20px;
  --density-gap-grid: 12px;

  /* Table */
  --density-table-row-height: 40px;
  --density-table-header-height: 36px;
  --density-table-cell-padding-x: 8px;
  --density-table-cell-padding-y: 6px;

  /* List */
  --density-list-item-height: 40px;
  --density-list-item-padding-x: 8px;
  --density-list-item-padding-y: 6px;
  --density-list-avatar-size: 28px;

  /* Navigation */
  --density-nav-item-height: 36px;
  --density-nav-item-padding-x: 12px;
  --density-sidebar-width: 220px;
  --density-topbar-height: 44px;

  /* Modal */
  --density-modal-padding: 16px;
  --density-modal-gap: 12px;
  --density-modal-max-width: 480px;
}
```

---

## Side-by-Side Comparison Table

| Property | Spacious | Comfortable | Compact |
|----------|----------|-------------|---------|
| **Min touch target** | 48px | 36px | 28px |
| **Button height** | 48px | 40px | 32px |
| **Input height** | 48px | 40px | 32px |
| **Base font** | 16px | 14px | 13px |
| **Base line-height** | 1.6 | 1.5 | 1.4 |
| **Icon (md)** | 24px | 20px | 16px |
| **Card padding** | 24px | 16px | 12px |
| **Grid gap** | 24px | 16px | 12px |
| **Table row** | 64px | 52px | 40px |
| **List item** | 72px | 56px | 40px |
| **Sidebar width** | 280px | 256px | 220px |
| **Topbar height** | 64px | 56px | 44px |
| **Form gap** | 24px | 16px | 12px |
| **Checkbox size** | 24px | 20px | 16px |

---

## Implementation Strategies

### Strategy 1: CSS Custom Properties (Recommended)

The simplest and most performant approach. Set a `data-density` attribute on a container element (usually `<html>` or `<body>`) and define all density tokens as custom properties.

```html
<html data-density="comfortable">
  <body>
    <button style="height: var(--density-button-height); padding: var(--density-padding-button-y) var(--density-padding-button-x);">
      Click me
    </button>
  </body>
</html>
```

**Switching density via JavaScript:**
```javascript
function setDensity(mode) {
  document.documentElement.setAttribute('data-density', mode);
  localStorage.setItem('user-density', mode);
}

// Initialize from saved preference
const savedDensity = localStorage.getItem('user-density') || 'comfortable';
setDensity(savedDensity);
```

### Strategy 2: Tailwind CSS Variants

Create a custom Tailwind plugin that generates density-aware utility classes.

```javascript
// tailwind.config.js
const plugin = require('tailwindcss/plugin');

module.exports = {
  theme: {
    extend: {
      spacing: {
        'density-xs': 'var(--density-space-xs)',
        'density-sm': 'var(--density-space-sm)',
        'density-md': 'var(--density-space-md)',
        'density-lg': 'var(--density-space-lg)',
        'density-xl': 'var(--density-space-xl)',
      },
      height: {
        'density-target': 'var(--density-target-default)',
        'density-button': 'var(--density-button-height)',
        'density-input': 'var(--density-input-height)',
      },
      fontSize: {
        'density-xs': 'var(--density-font-xs)',
        'density-sm': 'var(--density-font-sm)',
        'density-base': 'var(--density-font-base)',
        'density-lg': 'var(--density-font-lg)',
      },
      gap: {
        'density-inline': 'var(--density-gap-inline)',
        'density-stack': 'var(--density-gap-stack)',
        'density-form': 'var(--density-gap-form)',
        'density-grid': 'var(--density-gap-grid)',
      },
      padding: {
        'density-card': 'var(--density-padding-card)',
        'density-cell': 'var(--density-padding-cell)',
        'density-section': 'var(--density-padding-section)',
      },
    },
  },
  plugins: [
    plugin(function({ addVariant }) {
      addVariant('spacious', '[data-density="spacious"] &');
      addVariant('compact', '[data-density="compact"] &');
    }),
  ],
};
```

**Usage in markup:**
```html
<button class="h-density-button px-density-lg text-density-base compact:px-density-md spacious:px-density-xl">
  Density-aware button
</button>

<table class="gap-density-stack">
  <tr class="h-[var(--density-table-row-height)]">
    <td class="px-density-cell py-density-cell">Content</td>
  </tr>
</table>
```

### Strategy 3: React Context

For React applications, a context provider cleanly manages density state and propagation.

```tsx
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';

type DensityMode = 'spacious' | 'comfortable' | 'compact';

interface DensityContextValue {
  density: DensityMode;
  setDensity: (mode: DensityMode) => void;
}

const DensityContext = createContext<DensityContextValue>({
  density: 'comfortable',
  setDensity: () => {},
});

export function DensityProvider({ children }: { children: ReactNode }) {
  const [density, setDensityState] = useState<DensityMode>(() => {
    if (typeof window !== 'undefined') {
      return (localStorage.getItem('user-density') as DensityMode) || 'comfortable';
    }
    return 'comfortable';
  });

  const setDensity = (mode: DensityMode) => {
    setDensityState(mode);
    document.documentElement.setAttribute('data-density', mode);
    localStorage.setItem('user-density', mode);
  };

  useEffect(() => {
    document.documentElement.setAttribute('data-density', density);
  }, [density]);

  return (
    <DensityContext.Provider value={{ density, setDensity }}>
      {children}
    </DensityContext.Provider>
  );
}

export function useDensity() {
  return useContext(DensityContext);
}
```

**Density switcher component:**
```tsx
function DensitySwitcher() {
  const { density, setDensity } = useDensity();

  return (
    <fieldset className="flex gap-2" aria-label="Display density">
      <legend className="sr-only">Display density</legend>
      {(['spacious', 'comfortable', 'compact'] as const).map((mode) => (
        <label key={mode} className="flex items-center gap-1 cursor-pointer">
          <input
            type="radio"
            name="density"
            value={mode}
            checked={density === mode}
            onChange={() => setDensity(mode)}
            className="sr-only"
          />
          <span className={`px-3 py-1 rounded text-sm capitalize ${
            density === mode ? 'bg-primary text-white' : 'bg-surface-raised'
          }`}>
            {mode}
          </span>
        </label>
      ))}
    </fieldset>
  );
}
```

**Density-aware component example:**
```tsx
function Button({ children, size, ...props }: ButtonProps) {
  const { density } = useDensity();

  // Density affects default size behavior
  const effectiveHeight =
    density === 'spacious' ? '48px' :
    density === 'compact' ? '32px' : '40px';

  return (
    <button
      style={{ height: `var(--density-button-height, ${effectiveHeight})` }}
      className="px-[var(--density-padding-button-x)] text-[length:var(--density-font-base)]"
      {...props}
    >
      {children}
    </button>
  );
}
```

### Strategy 4: Vue Composable

```typescript
// useDensity.ts
import { ref, watch, onMounted } from 'vue';

type DensityMode = 'spacious' | 'comfortable' | 'compact';

const density = ref<DensityMode>('comfortable');

export function useDensity() {
  onMounted(() => {
    const saved = localStorage.getItem('user-density') as DensityMode;
    if (saved) density.value = saved;
    document.documentElement.setAttribute('data-density', density.value);
  });

  watch(density, (newVal) => {
    document.documentElement.setAttribute('data-density', newVal);
    localStorage.setItem('user-density', newVal);
  });

  return { density };
}
```

---

## Component-Specific Density Adjustments

### Tables

Tables benefit most from density control. A data table in compact mode can display 50% more rows without scrolling.

```css
/* Density-aware table */
.data-table {
  font-size: var(--density-font-sm);
  line-height: var(--density-line-height-base);
}
.data-table th {
  height: var(--density-table-header-height);
  padding: var(--density-table-cell-padding-y) var(--density-table-cell-padding-x);
  font-size: var(--density-font-xs);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.data-table td {
  height: var(--density-table-row-height);
  padding: var(--density-table-cell-padding-y) var(--density-table-cell-padding-x);
}
/* Compact tables can remove some padding from less important columns */
[data-density="compact"] .data-table .col-secondary {
  padding-left: var(--density-space-xs);
  padding-right: var(--density-space-xs);
}
```

### Lists

```css
.list-item {
  min-height: var(--density-list-item-height);
  padding: var(--density-list-item-padding-y) var(--density-list-item-padding-x);
  display: flex;
  align-items: center;
  gap: var(--density-gap-inline);
}
.list-item-avatar {
  width: var(--density-list-avatar-size);
  height: var(--density-list-avatar-size);
  border-radius: var(--radius-full);
  flex-shrink: 0;
}
.list-item-text {
  font-size: var(--density-font-base);
  line-height: var(--density-line-height-base);
}
.list-item-secondary {
  font-size: var(--density-font-sm);
  color: var(--color-text-secondary);
}
```

### Forms

Forms need density-aware field sizing and spacing between fields.

```css
.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--density-space-sm);
}
.form-stack {
  display: flex;
  flex-direction: column;
  gap: var(--density-gap-form);
}
.form-label {
  font-size: var(--density-font-sm);
  font-weight: 500;
  line-height: var(--density-line-height-tight);
}
.form-input {
  height: var(--density-input-height);
  padding: var(--density-padding-input-y) var(--density-padding-input-x);
  font-size: var(--density-font-base);
  border-radius: var(--radius-md);
}
.form-helper {
  font-size: var(--density-font-xs);
  color: var(--color-text-tertiary);
  line-height: var(--density-line-height-base);
}
.form-actions {
  display: flex;
  gap: var(--density-gap-inline);
  padding-top: var(--density-space-lg);
}
```

### Navigation

```css
.sidebar {
  width: var(--density-sidebar-width);
  padding: var(--density-space-md);
}
.nav-item {
  height: var(--density-nav-item-height);
  padding: 0 var(--density-nav-item-padding-x);
  display: flex;
  align-items: center;
  gap: var(--density-gap-inline);
  font-size: var(--density-font-sm);
  border-radius: var(--radius-md);
}
.nav-item-icon {
  width: var(--density-icon-md);
  height: var(--density-icon-md);
  flex-shrink: 0;
}
.topbar {
  height: var(--density-topbar-height);
  padding: 0 var(--density-padding-page);
  display: flex;
  align-items: center;
}
```

### Cards

```css
.card {
  padding: var(--density-padding-card);
  border-radius: var(--radius-lg);
  display: flex;
  flex-direction: column;
  gap: var(--density-gap-stack);
}
.card-header {
  display: flex;
  align-items: center;
  gap: var(--density-gap-inline);
}
.card-title {
  font-size: var(--density-font-lg);
  font-weight: 600;
  line-height: var(--density-line-height-tight);
}
.card-body {
  font-size: var(--density-font-base);
  line-height: var(--density-line-height-base);
}
.card-footer {
  display: flex;
  gap: var(--density-gap-inline);
  padding-top: var(--density-space-sm);
}
```

### Toolbar / Action Bar

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: var(--density-space-sm);
  padding: var(--density-space-sm) var(--density-space-md);
  height: var(--density-topbar-height);
}
.toolbar-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: var(--density-target-default);
  height: var(--density-target-default);
  padding: var(--density-space-xs) var(--density-space-sm);
  font-size: var(--density-font-sm);
  gap: var(--density-space-xs);
  border-radius: var(--radius-md);
}
.toolbar-separator {
  width: 1px;
  height: calc(var(--density-target-default) * 0.6);
  background: var(--color-border-subtle);
  margin: 0 var(--density-space-xs);
}
```

---

## User Preference Persistence

### localStorage Approach (Simple)

```javascript
const DENSITY_KEY = 'app-density-preference';
const DEFAULT_DENSITY = 'comfortable';

function getDensity() {
  return localStorage.getItem(DENSITY_KEY) || DEFAULT_DENSITY;
}

function setDensity(mode) {
  localStorage.setItem(DENSITY_KEY, mode);
  document.documentElement.setAttribute('data-density', mode);
}

// Apply on page load (before paint to avoid flash)
// Place this in <head> as a blocking script:
// <script>document.documentElement.setAttribute('data-density', localStorage.getItem('app-density-preference') || 'comfortable')</script>
```

### Server-Side Preference (Cookie)

```javascript
// Set preference via cookie for SSR
function setDensityCookie(mode) {
  document.cookie = `density=${mode};path=/;max-age=31536000;SameSite=Lax`;
  document.documentElement.setAttribute('data-density', mode);
}

// Server reads cookie and sets attribute in initial HTML
// Express example:
// app.get('*', (req, res) => {
//   const density = req.cookies.density || 'comfortable';
//   res.send(`<html data-density="${density}">...`);
// });
```

### Respecting System Preferences

Density can be inferred from device type or user accessibility settings:

```javascript
function inferDensity() {
  // Touch device -> spacious
  if ('ontouchstart' in window && window.innerWidth < 768) {
    return 'spacious';
  }

  // Large screen with high resolution -> could handle compact
  if (window.innerWidth > 1440) {
    return 'comfortable'; // Still default, let user choose compact
  }

  // Accessibility: reduced motion often correlates with preference for spacious
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return 'spacious';
  }

  return 'comfortable';
}

// Apply inferred density only if no saved preference
const saved = localStorage.getItem(DENSITY_KEY);
setDensity(saved || inferDensity());
```

---

## Mixed Density Within a Page

Different areas of the same interface can use different densities. This is common and recommended:

```html
<html data-density="comfortable">
  <body>
    <!-- Global nav: compact to save space -->
    <nav data-density="compact">
      <a class="nav-item" href="/">Dashboard</a>
      <a class="nav-item" href="/data">Data</a>
    </nav>

    <main>
      <!-- Content area: comfortable or spacious -->
      <section class="content" data-density="comfortable">
        <h1>Welcome back</h1>
        <p>Here is your overview.</p>
      </section>

      <!-- Data table: compact for maximum rows -->
      <section data-density="compact">
        <table class="data-table">
          <!-- Compact table rows -->
        </table>
      </section>
    </main>
  </body>
</html>
```

CSS custom properties naturally cascade — a `data-density="compact"` attribute on a child overrides the parent's values within that subtree.

---

## Density and Accessibility

### Touch Target Minimums

Even in compact mode, interactive elements must meet minimum accessibility requirements:

| Standard | Minimum Target Size | Applies To |
|----------|-------------------|------------|
| WCAG 2.2 Level AA (2.5.8) | 24x24 CSS pixels | All interactive targets |
| WCAG 2.2 Level AAA | 44x44 CSS pixels | All interactive targets |
| Apple HIG | 44x44 points | iOS touch targets |
| Material Design | 48x48 dp | Android touch targets |

**Compact mode compliance strategy:**
```css
/* Visual size can be small, but touch area must be large */
[data-density="compact"] .icon-button {
  /* Visual size: 28px */
  width: 28px;
  height: 28px;

  /* Touch target: at least 44px via padding or ::before */
  position: relative;
}
[data-density="compact"] .icon-button::before {
  content: '';
  position: absolute;
  inset: -8px; /* Extends touch target to 44px */
}
```

### Font Size Minimums

Compact mode reduces font sizes, but never below readable thresholds:
- **Absolute minimum:** 10px (for labels, annotations only)
- **Body text minimum:** 12px (compact), 13px preferred
- **Users with low vision:** Ensure density does not disable browser text scaling

### Keyboard Navigation Spacing

Compact mode can make focus indicators harder to distinguish. Ensure:
- Focus rings remain visible (at least 2px width)
- Focused elements have enough spacing to show the ring without clipping
- Tab order remains logical when elements are packed tighter

---

## Density Design Tokens (JSON Export)

Complete token set for design tool integration (Figma Tokens, Style Dictionary, etc.):

```json
{
  "density": {
    "spacious": {
      "space": { "xs": "8px", "sm": "12px", "md": "16px", "lg": "24px", "xl": "32px" },
      "target": { "min": "48px", "default": "48px", "large": "56px" },
      "button": { "height": "48px", "padding-x": "24px", "padding-y": "12px" },
      "input": { "height": "48px", "padding-x": "16px", "padding-y": "14px" },
      "font": { "xs": "12px", "sm": "14px", "base": "16px", "lg": "18px" },
      "line-height": { "tight": "1.3", "base": "1.6", "relaxed": "1.8" },
      "icon": { "xs": "16px", "sm": "20px", "md": "24px", "lg": "32px" },
      "card": { "padding": "24px" },
      "table": { "row-height": "64px", "header-height": "56px" },
      "list": { "item-height": "72px", "avatar-size": "48px" },
      "nav": { "item-height": "56px", "sidebar-width": "280px", "topbar-height": "64px" },
      "gap": { "inline": "12px", "stack": "16px", "form": "24px", "grid": "24px" }
    },
    "comfortable": {
      "space": { "xs": "4px", "sm": "8px", "md": "12px", "lg": "16px", "xl": "24px" },
      "target": { "min": "36px", "default": "40px", "large": "48px" },
      "button": { "height": "40px", "padding-x": "16px", "padding-y": "8px" },
      "input": { "height": "40px", "padding-x": "12px", "padding-y": "10px" },
      "font": { "xs": "11px", "sm": "13px", "base": "14px", "lg": "16px" },
      "line-height": { "tight": "1.25", "base": "1.5", "relaxed": "1.7" },
      "icon": { "xs": "14px", "sm": "16px", "md": "20px", "lg": "24px" },
      "card": { "padding": "16px" },
      "table": { "row-height": "52px", "header-height": "48px" },
      "list": { "item-height": "56px", "avatar-size": "40px" },
      "nav": { "item-height": "44px", "sidebar-width": "256px", "topbar-height": "56px" },
      "gap": { "inline": "8px", "stack": "12px", "form": "16px", "grid": "16px" }
    },
    "compact": {
      "space": { "xs": "2px", "sm": "4px", "md": "8px", "lg": "12px", "xl": "16px" },
      "target": { "min": "28px", "default": "32px", "large": "40px" },
      "button": { "height": "32px", "padding-x": "12px", "padding-y": "4px" },
      "input": { "height": "32px", "padding-x": "8px", "padding-y": "6px" },
      "font": { "xs": "10px", "sm": "11px", "base": "13px", "lg": "14px" },
      "line-height": { "tight": "1.2", "base": "1.4", "relaxed": "1.5" },
      "icon": { "xs": "12px", "sm": "14px", "md": "16px", "lg": "20px" },
      "card": { "padding": "12px" },
      "table": { "row-height": "40px", "header-height": "36px" },
      "list": { "item-height": "40px", "avatar-size": "28px" },
      "nav": { "item-height": "36px", "sidebar-width": "220px", "topbar-height": "44px" },
      "gap": { "inline": "4px", "stack": "8px", "form": "12px", "grid": "12px" }
    }
  }
}
```

---

## Density Audit Checklist

- [ ] All three density modes are defined with complete token sets
- [ ] Density switching does not cause layout shifts or content jumps
- [ ] Compact mode still meets WCAG 2.5.8 minimum target sizes (24x24px)
- [ ] Font sizes in compact mode do not go below 10px anywhere
- [ ] Focus indicators remain visible in compact mode
- [ ] User density preference is persisted across sessions
- [ ] Initial density is applied before first paint (no flash of wrong density)
- [ ] Mixed density sections (compact table inside comfortable layout) work correctly
- [ ] Touch devices default to spacious or comfortable, never compact
- [ ] Density affects all component families consistently (not just some components)
- [ ] Tables, lists, forms, navigation, cards, and modals all respect density tokens
- [ ] Dark mode and density are independent and combinable
- [ ] Spacing in compact mode still provides clear visual grouping
- [ ] Line-height adjustments maintain text readability at all density levels
