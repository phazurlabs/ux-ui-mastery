---
name: shadow-elevation-density
description: "Complete elevation, shadow, depth, density, border-radius, and visual effects systems. Covers shadow scales, elevation hierarchy, glassmorphism, density modes (compact/comfortable/spacious), border-radius systems, blur effects, and modern CSS visual treatments with production code. Use when the user mentions: shadow, elevation, depth, z-index, box-shadow, density, compact mode, spacious mode, glassmorphism, blur, backdrop, border radius, rounded corners, card shadow, dropdown shadow, modal shadow, frosted glass, neumorphism, visual effects."
---

# Shadow, Elevation & Density Systems

## 1. Shadow Theory

### Light Source Model
All shadows in a UI should originate from a single, consistent light source. The standard convention is a **top-center light** (slightly left of center in LTR interfaces), positioned above the viewport plane. This creates shadows that fall primarily downward with a slight rightward offset.

Key principles:
- **Consistency**: Every element on the same elevation shares identical shadow direction
- **Single source**: Multiple light sources create conflicting shadows and destroy spatial coherence
- **Ambient + direct**: Realistic shadows combine a tight, darker direct shadow with a softer, wider ambient shadow
- **Distance attenuation**: Elements farther from the surface cast larger, softer, lighter shadows

### Shadow Anatomy
Every CSS `box-shadow` is defined by five properties:

| Property | Role | Typical range |
|----------|------|---------------|
| **x-offset** | Horizontal displacement. Positive = right (matches light from left) | 0 - 4px |
| **y-offset** | Vertical displacement. Positive = down (matches light from above) | 1 - 50px |
| **blur-radius** | Gaussian blur. Larger = softer, more diffuse edge | 1 - 50px |
| **spread-radius** | Expands or contracts the shadow shape. Negative = tighter | -4px - 4px |
| **color** | Shadow color with alpha. Never pure black | oklch(0 0 0 / 0.04) - oklch(0 0 0 / 0.25) |

### Layered Shadows for Realism
Single shadows look flat and artificial. Production-quality elevation uses 2-3 stacked shadows:

1. **Ambient layer** (bottom): Large blur, low opacity, no offset — simulates scattered ambient light
2. **Direct layer** (middle): Medium blur, medium opacity, vertical offset — the primary depth cue
3. **Contact layer** (top, optional): Tiny blur, higher opacity, minimal offset — grounds the element to its surface

```css
/* Anatomy of a realistic 3-layer shadow */
.card {
  box-shadow:
    0 0 0 1px oklch(0 0 0 / 0.03),    /* contact/edge definition */
    0 2px 4px oklch(0 0 0 / 0.04),      /* direct shadow */
    0 12px 24px oklch(0 0 0 / 0.06);    /* ambient shadow */
}
```

---

## 2. Five-Level Shadow Scale

Each level uses 2-3 layered shadows for realistic depth. These are designed for a white/light surface.

### Level 0 — Flat / Flush
**Use for**: Inline content, table rows, flat cards in dense layouts, backgrounds
**Elevation**: 0dp — element sits on the surface plane

```css
--shadow-0: none;
/* Alternative: subtle border for definition without elevation */
--shadow-0-bordered: 0 0 0 1px oklch(0 0 0 / 0.06);
```

### Level 1 — Subtle Lift
**Use for**: Cards, input fields, list items on hover, secondary surfaces
**Elevation**: 1-2dp — slight separation from base surface

```css
--shadow-1:
  0 1px 2px oklch(0 0 0 / 0.06),
  0 1px 3px oklch(0 0 0 / 0.10);

/* Expanded variant for larger cards */
--shadow-1-lg:
  0 0 0 1px oklch(0 0 0 / 0.03),
  0 1px 2px oklch(0 0 0 / 0.05),
  0 2px 6px oklch(0 0 0 / 0.08);
```

### Level 2 — Raised
**Use for**: Dropdowns, popovers, autocomplete menus, floating action buttons, sticky headers
**Elevation**: 4-8dp — clearly above the base surface

```css
--shadow-2:
  0 2px 4px oklch(0 0 0 / 0.04),
  0 4px 8px oklch(0 0 0 / 0.06),
  0 12px 24px oklch(0 0 0 / 0.06);

/* Tight variant for small dropdowns */
--shadow-2-tight:
  0 1px 3px oklch(0 0 0 / 0.08),
  0 6px 12px oklch(0 0 0 / 0.08);
```

### Level 3 — Floating
**Use for**: Modals, dialogs, bottom sheets, notification panels, drawer overlays
**Elevation**: 12-16dp — prominent floating layer, usually with scrim/backdrop

```css
--shadow-3:
  0 4px 8px oklch(0 0 0 / 0.04),
  0 8px 16px oklch(0 0 0 / 0.06),
  0 20px 40px oklch(0 0 0 / 0.10);

/* Softer variant for bottom sheets */
--shadow-3-soft:
  0 -2px 8px oklch(0 0 0 / 0.04),
  0 -8px 24px oklch(0 0 0 / 0.06),
  0 -20px 48px oklch(0 0 0 / 0.08);
```

### Level 4 — Dramatic
**Use for**: Drag states, hero elements, onboarding spotlights, active drag-and-drop, image lightbox
**Elevation**: 24dp+ — maximum separation, cinematic depth

```css
--shadow-4:
  0 8px 16px oklch(0 0 0 / 0.06),
  0 16px 32px oklch(0 0 0 / 0.08),
  0 32px 64px oklch(0 0 0 / 0.12);

/* Ultra-dramatic for drag states */
--shadow-4-drag:
  0 12px 24px oklch(0 0 0 / 0.08),
  0 24px 48px oklch(0 0 0 / 0.10),
  0 48px 96px oklch(0 0 0 / 0.14);
```

### Complete Token System

```css
:root {
  --shadow-0: none;
  --shadow-1: 0 1px 2px oklch(0 0 0 / 0.06), 0 1px 3px oklch(0 0 0 / 0.10);
  --shadow-2: 0 2px 4px oklch(0 0 0 / 0.04), 0 4px 8px oklch(0 0 0 / 0.06), 0 12px 24px oklch(0 0 0 / 0.06);
  --shadow-3: 0 4px 8px oklch(0 0 0 / 0.04), 0 8px 16px oklch(0 0 0 / 0.06), 0 20px 40px oklch(0 0 0 / 0.10);
  --shadow-4: 0 8px 16px oklch(0 0 0 / 0.06), 0 16px 32px oklch(0 0 0 / 0.08), 0 32px 64px oklch(0 0 0 / 0.12);
}
```

---

## 3. Shadow Color Theory

### Never Use Pure Black
Pure black (`#000000` / `rgb(0,0,0)`) shadows look harsh and unnatural. In the real world, shadows pick up color from the environment. Use very low lightness with slight chroma instead.

```css
/* Bad — harsh, lifeless */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);

/* Good — neutral warm */
box-shadow: 0 4px 12px oklch(0.15 0.005 250 / 0.15);

/* Good — simple low-lightness approach */
box-shadow: 0 4px 12px oklch(0 0 0 / 0.12);
```

### Brand-Tinted Shadows
Tinting shadows with a desaturated version of the element's color creates cohesion and richness:

```css
/* Blue brand card */
.card-blue {
  background: oklch(0.55 0.2 255);
  box-shadow:
    0 2px 4px oklch(0.25 0.06 255 / 0.20),
    0 8px 24px oklch(0.20 0.08 255 / 0.25);
}

/* Green success card */
.card-green {
  background: oklch(0.60 0.18 145);
  box-shadow:
    0 2px 4px oklch(0.25 0.05 145 / 0.20),
    0 8px 24px oklch(0.20 0.06 145 / 0.25);
}

/* Red/warm card */
.card-red {
  background: oklch(0.55 0.22 25);
  box-shadow:
    0 2px 4px oklch(0.25 0.06 25 / 0.20),
    0 8px 24px oklch(0.20 0.08 25 / 0.25);
}
```

### OKLCH Shadow Color Scale
Build a systematic shadow palette using oklch for perceptual uniformity:

```css
:root {
  /* Neutral shadows — slight cool tint */
  --shadow-color-subtle: oklch(0.15 0.005 260 / 0.04);
  --shadow-color-light:  oklch(0.15 0.005 260 / 0.08);
  --shadow-color-medium: oklch(0.15 0.005 260 / 0.12);
  --shadow-color-strong: oklch(0.15 0.005 260 / 0.18);
  --shadow-color-heavy:  oklch(0.15 0.005 260 / 0.25);

  /* Brand-tinted shadows — adjust hue to match brand */
  --shadow-color-brand-subtle: oklch(0.20 0.04 var(--brand-hue) / 0.06);
  --shadow-color-brand-medium: oklch(0.20 0.06 var(--brand-hue) / 0.12);
  --shadow-color-brand-strong: oklch(0.20 0.08 var(--brand-hue) / 0.20);
}
```

### Shadow color tips
- Keep chroma low (0.005-0.08) — shadows are desaturated by nature
- Hue should match the dominant surface or brand color
- Increase opacity for higher elevation, not chroma
- On colored backgrounds, match shadow hue to background hue
- For colored buttons/cards, the shadow should be a darker, desaturated version of the element color

---

## 4. Shadow Animation

### Hover Lift
The most common elevation change. Card rises from Level 1 to Level 2 on hover.

```css
.card {
  box-shadow: var(--shadow-1);
  transition: box-shadow 200ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
  box-shadow: var(--shadow-2);
  transform: translateY(-2px);
}
```

### Press / Active State
Element compresses — drops from current elevation toward surface.

```css
.card:active {
  box-shadow: var(--shadow-1);
  transform: translateY(0px) scale(0.98);
  transition: box-shadow 100ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 100ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Drag State
Element lifts dramatically when grabbed, then settles on drop.

```css
.draggable {
  box-shadow: var(--shadow-1);
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 300ms cubic-bezier(0.4, 0, 0.2, 1);
}

.draggable.is-dragging {
  box-shadow: var(--shadow-4-drag);
  transform: scale(1.03) rotate(1deg);
  transition: box-shadow 150ms cubic-bezier(0, 0, 0.2, 1),
              transform 150ms cubic-bezier(0, 0, 0.2, 1);
  z-index: 9999;
}

.draggable.is-dropping {
  box-shadow: var(--shadow-1);
  transform: scale(1) rotate(0deg);
  transition: box-shadow 400ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Focus Ring + Shadow
Combine focus-visible with elevation for interactive elements.

```css
.interactive:focus-visible {
  box-shadow:
    var(--shadow-2),
    0 0 0 3px oklch(0.55 0.2 255 / 0.40);
  outline: none;
}
```

### Transition Timing Reference

| State change | Duration | Easing | Notes |
|-------------|----------|--------|-------|
| Rest to hover | 200ms | ease-out (0.4, 0, 0.2, 1) | Standard Material easing |
| Hover to rest | 150ms | ease-in (0.4, 0, 1, 1) | Slightly faster return |
| Rest to active/press | 100ms | ease-out | Immediate feedback |
| Pick up (drag start) | 150ms | decelerate (0, 0, 0.2, 1) | Quick lift |
| Drop (drag end) | 400ms | standard (0.4, 0, 0.2, 1) | Gentle settle |
| Modal enter | 300ms | decelerate | Scale + shadow together |
| Modal exit | 200ms | accelerate (0.4, 0, 1, 1) | Fast dismiss |

---

## 5. Z-Index Scale

### Systematic Layering System
A predictable z-index scale prevents stacking context wars. Use named tokens with 100-step intervals to leave room for sub-layers.

```css
:root {
  --z-base:           0;
  --z-raised:         1;     /* Subtle lift above siblings */
  --z-dropdown:       100;
  --z-sticky:         200;
  --z-fixed:          300;
  --z-drawer:         400;
  --z-modal-backdrop: 500;
  --z-modal:          510;
  --z-popover:        600;
  --z-toast:          700;
  --z-tooltip:        800;
  --z-drag:           900;
  --z-max:            9999;  /* Debug overlays, emergency only */
}
```

### Stacking Context Rules
- Each element with `position: relative/absolute/fixed/sticky` + `z-index` creates a new stacking context
- `transform`, `filter`, `opacity < 1`, `will-change`, and `isolation: isolate` also create stacking contexts
- Z-index only competes within the same stacking context
- Use `isolation: isolate` on layout containers to scope z-index conflicts

```css
/* Isolate a component's z-index from the page */
.card-stack {
  isolation: isolate;
}

/* Now these z-indexes only compete within .card-stack */
.card-stack .card { z-index: 1; }
.card-stack .card:hover { z-index: 2; }
.card-stack .card.is-dragging { z-index: var(--z-drag); }
```

### Common Stacking Patterns

```css
/* Sticky header that respects modals */
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
}

/* Dropdown within the header */
.site-header .dropdown-menu {
  position: absolute;
  z-index: var(--z-dropdown);
}

/* Modal with backdrop */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal-backdrop);
  background: oklch(0 0 0 / 0.5);
}

.modal {
  position: fixed;
  z-index: var(--z-modal);
}

/* Toast on top of everything except tooltips */
.toast-container {
  position: fixed;
  z-index: var(--z-toast);
}

/* Tooltips always on top */
[role="tooltip"] {
  z-index: var(--z-tooltip);
}
```

---

## 6. Elevation in Material Design 3

### Tonal Elevation vs Shadow Elevation
Material Design 3 introduced **tonal elevation** as an alternative to shadow-based elevation. Instead of casting shadows, surfaces become lighter (in light mode) or lighter-tinted (in dark mode) as they rise.

**Shadow elevation** (traditional):
- Uses `box-shadow` to convey depth
- More obvious spatial hierarchy
- Works universally across themes

**Tonal elevation** (M3):
- Surface color shifts toward the primary color at higher elevation
- Overlay opacity increases with elevation: 0% (level 0) to 14% (level 5)
- Better for dark themes where shadows are nearly invisible

```css
/* M3 tonal elevation in CSS */
:root {
  --md-elevation-0: oklch(0.99 0 0);                          /* surface */
  --md-elevation-1: color-mix(in oklch, var(--md-primary) 5%, var(--md-surface));
  --md-elevation-2: color-mix(in oklch, var(--md-primary) 8%, var(--md-surface));
  --md-elevation-3: color-mix(in oklch, var(--md-primary) 11%, var(--md-surface));
  --md-elevation-4: color-mix(in oklch, var(--md-primary) 12%, var(--md-surface));
  --md-elevation-5: color-mix(in oklch, var(--md-primary) 14%, var(--md-surface));
}

/* M3 shadow elevation levels (dp to CSS) */
--md-shadow-1: 0 1px 2px oklch(0 0 0 / 0.30), 0 1px 3px 1px oklch(0 0 0 / 0.15);
--md-shadow-2: 0 1px 2px oklch(0 0 0 / 0.30), 0 2px 6px 2px oklch(0 0 0 / 0.15);
--md-shadow-3: 0 4px 8px 3px oklch(0 0 0 / 0.15), 0 1px 3px oklch(0 0 0 / 0.30);
--md-shadow-4: 0 6px 10px 4px oklch(0 0 0 / 0.15), 0 2px 3px oklch(0 0 0 / 0.30);
--md-shadow-5: 0 8px 12px 6px oklch(0 0 0 / 0.15), 0 4px 4px oklch(0 0 0 / 0.30);
```

### M3 Elevation Mapping

| M3 Level | dp | Use case | Tonal overlay | Shadow |
|----------|-----|----------|---------------|--------|
| 0 | 0 | Surface | 0% | none |
| 1 | 1 | Cards, navigation rail | 5% | shadow-1 |
| 2 | 3 | FAB resting, navigation drawer | 8% | shadow-2 |
| 3 | 6 | FAB pressed, bottom sheet | 11% | shadow-3 |
| 4 | 8 | App bars | 12% | shadow-4 |
| 5 | 12 | Dialogs, navigation drawer (modal) | 14% | shadow-5 |

---

## 7. iOS Shadow Conventions

### UIKit NSShadow Equivalents
iOS shadows use `CALayer.shadow*` properties, which map to CSS differently:

| CALayer property | CSS equivalent | Notes |
|------------------|---------------|-------|
| `shadowColor` | color in box-shadow | CGColor, typically black |
| `shadowOpacity` | alpha in shadow color | 0.0 - 1.0, separate from color |
| `shadowOffset` | x-offset, y-offset | CGSize (width, height) |
| `shadowRadius` | blur-radius / 2 | iOS radius is roughly half the CSS blur |
| `shadowPath` | N/A (auto in CSS) | Performance optimization in iOS |

### SwiftUI Shadow Modifiers

```swift
// SwiftUI shadow levels matching the 5-level scale
extension View {
    func shadowLevel0() -> some View {
        self // no shadow
    }

    func shadowLevel1() -> some View {
        self.shadow(color: .black.opacity(0.08), radius: 2, x: 0, y: 1)
            .shadow(color: .black.opacity(0.05), radius: 4, x: 0, y: 2)
    }

    func shadowLevel2() -> some View {
        self.shadow(color: .black.opacity(0.06), radius: 4, x: 0, y: 2)
            .shadow(color: .black.opacity(0.08), radius: 12, x: 0, y: 6)
    }

    func shadowLevel3() -> some View {
        self.shadow(color: .black.opacity(0.05), radius: 8, x: 0, y: 4)
            .shadow(color: .black.opacity(0.10), radius: 24, x: 0, y: 12)
    }

    func shadowLevel4() -> some View {
        self.shadow(color: .black.opacity(0.06), radius: 16, x: 0, y: 8)
            .shadow(color: .black.opacity(0.12), radius: 48, x: 0, y: 24)
    }
}
```

### iOS-Specific Shadow Notes
- iOS prefers subtler shadows than Android/Material
- In iOS 26 Liquid Glass, traditional shadows are largely replaced by glass material blur effects
- Always set `shadowPath` in UIKit for performance (avoids offscreen rendering)
- SwiftUI `.shadow()` does not auto-clip; use `.clipShape()` first if needed
- Dark mode on iOS: reduce shadow opacity significantly or switch to border-based separation

---

## 8. Density Modes

Three density levels control spacing, touch targets, font sizes, and information density across the entire UI.

### Comfortable (Default)
**Use for**: General consumer apps, marketing sites, reading-heavy interfaces
**Philosophy**: Generous breathing room, accessible touch targets, relaxed visual rhythm

```css
:root[data-density="comfortable"] {
  /* Spacing scale */
  --density-spacing-xs: 8px;
  --density-spacing-sm: 12px;
  --density-spacing-md: 16px;
  --density-spacing-lg: 24px;
  --density-spacing-xl: 32px;
  --density-spacing-2xl: 48px;

  /* Touch targets */
  --density-target-min: 48px;   /* WCAG AAA */
  --density-target-comfortable: 52px;

  /* Typography */
  --density-line-height-body: 1.5;
  --density-line-height-heading: 1.3;
  --density-paragraph-spacing: 1em;

  /* Components */
  --density-input-height: 48px;
  --density-button-height: 48px;
  --density-button-padding: 16px 24px;
  --density-table-row-height: 56px;
  --density-table-cell-padding: 16px;
  --density-list-item-height: 56px;
  --density-card-padding: 24px;
  --density-nav-item-height: 48px;

  /* Gap between elements */
  --density-stack-gap: 16px;
  --density-inline-gap: 12px;
  --density-section-gap: 48px;
}
```

### Compact
**Use for**: Dashboards, admin panels, productivity apps, desktop-first interfaces
**Philosophy**: Reduced spacing without sacrificing readability, mouse-friendly targets

```css
:root[data-density="compact"] {
  /* Spacing scale */
  --density-spacing-xs: 4px;
  --density-spacing-sm: 8px;
  --density-spacing-md: 12px;
  --density-spacing-lg: 16px;
  --density-spacing-xl: 24px;
  --density-spacing-2xl: 32px;

  /* Touch targets */
  --density-target-min: 36px;
  --density-target-comfortable: 40px;

  /* Typography */
  --density-line-height-body: 1.4;
  --density-line-height-heading: 1.2;
  --density-paragraph-spacing: 0.75em;

  /* Components */
  --density-input-height: 36px;
  --density-button-height: 36px;
  --density-button-padding: 8px 16px;
  --density-table-row-height: 44px;
  --density-table-cell-padding: 12px;
  --density-list-item-height: 44px;
  --density-card-padding: 16px;
  --density-nav-item-height: 40px;

  /* Gap between elements */
  --density-stack-gap: 12px;
  --density-inline-gap: 8px;
  --density-section-gap: 32px;
}
```

### Dense
**Use for**: Data tables, spreadsheet views, financial dashboards, power-user tools, IDE-like interfaces
**Philosophy**: Maximum information density, every pixel earns its place

```css
:root[data-density="dense"] {
  /* Spacing scale */
  --density-spacing-xs: 2px;
  --density-spacing-sm: 4px;
  --density-spacing-md: 8px;
  --density-spacing-lg: 12px;
  --density-spacing-xl: 16px;
  --density-spacing-2xl: 24px;

  /* Touch targets */
  --density-target-min: 32px;   /* Absolute minimum */
  --density-target-comfortable: 32px;

  /* Typography */
  --density-line-height-body: 1.3;
  --density-line-height-heading: 1.15;
  --density-paragraph-spacing: 0.5em;
  --density-font-size-adjust: 0.875; /* scale down to ~14px from 16px base */

  /* Components */
  --density-input-height: 32px;
  --density-button-height: 32px;
  --density-button-padding: 6px 12px;
  --density-table-row-height: 36px;
  --density-table-cell-padding: 8px;
  --density-list-item-height: 36px;
  --density-card-padding: 12px;
  --density-nav-item-height: 32px;

  /* Gap between elements */
  --density-stack-gap: 8px;
  --density-inline-gap: 6px;
  --density-section-gap: 24px;
}
```

### Density Switching Pattern

```css
/* User preference toggle */
.density-toggle {
  /* Store preference in data attribute on root */
}

/* Responsive density: auto-compact on small viewports with pointer */
@media (pointer: fine) and (max-width: 1024px) {
  :root:not([data-density]) {
    /* auto-apply compact tokens */
  }
}

/* Touch devices always get comfortable minimum */
@media (pointer: coarse) {
  :root[data-density="dense"] {
    --density-target-min: 44px; /* override back to touch-safe */
  }
}
```

---

## 9. Border Radius Systems

### Consistent Scale
A harmonious radius scale with clear steps. Each value serves specific component sizes.

```css
:root {
  --radius-0:    0px;      /* Sharp: technical, corporate */
  --radius-1:    2px;      /* Minimal: subtle softening */
  --radius-2:    4px;      /* Small: inputs, small buttons */
  --radius-3:    8px;      /* Medium: cards, dialogs — most common */
  --radius-4:    12px;     /* Large: large cards, panels */
  --radius-5:    16px;     /* XL: hero cards, onboarding */
  --radius-6:    24px;     /* XXL: floating UI, bottom sheets */
  --radius-full: 9999px;   /* Pill: buttons, badges, tags, avatars */
}
```

### Per-Component Recommendations

| Component | Recommended radius | Notes |
|-----------|-------------------|-------|
| Input fields | `--radius-2` (4px) | Subtle, professional |
| Buttons (small) | `--radius-2` (4px) | Match input radius |
| Buttons (default) | `--radius-3` (8px) | Friendly, clickable |
| Buttons (pill) | `--radius-full` | CTA, tags, badges |
| Cards | `--radius-3` to `--radius-4` | 8-12px depending on size |
| Dialogs/Modals | `--radius-4` to `--radius-5` | 12-16px, larger = friendlier |
| Dropdowns | `--radius-3` (8px) | Match card radius |
| Tooltips | `--radius-2` (4px) | Small, unobtrusive |
| Avatars | `--radius-full` | Circular |
| Bottom sheets | `--radius-5` top only | 16px top-left, top-right |
| Chips/Tags | `--radius-full` | Pill shape |
| Images (in cards) | Match card radius | Or use `overflow: hidden` on parent |
| Toggle tracks | `--radius-full` | Pill shape |

### Nested Radius Rule
When an element with rounded corners contains a child with rounded corners, the inner radius must account for padding to maintain optical consistency.

```
inner-radius = outer-radius - padding
```

```css
.card {
  border-radius: 16px;
  padding: 8px;
}

.card .card-image {
  /* 16px - 8px = 8px */
  border-radius: 8px;
}

/* If padding > radius, inner goes to 0 */
.card-compact {
  border-radius: 12px;
  padding: 16px;
}

.card-compact .inner {
  border-radius: 0px; /* max(12 - 16, 0) = 0 */
}
```

### Radius + Shadow Interaction
Shadows automatically follow border-radius on `box-shadow`. For `drop-shadow` filter, the shadow follows the element's alpha mask (useful for irregular shapes).

```css
/* box-shadow respects border-radius */
.rounded-card {
  border-radius: var(--radius-3);
  box-shadow: var(--shadow-2);
}

/* drop-shadow follows actual shape (including transparency) */
.irregular-shape {
  filter: drop-shadow(0 4px 8px oklch(0 0 0 / 0.1));
}
```

---

## 10. Glassmorphism / Frosted Glass

### Core Recipe

```css
.glass-surface {
  background: oklch(1 0 0 / 0.6);              /* semi-transparent white */
  backdrop-filter: blur(16px) saturate(1.8);
  -webkit-backdrop-filter: blur(16px) saturate(1.8);
  border: 1px solid oklch(1 0 0 / 0.2);        /* subtle border for edge definition */
  border-radius: var(--radius-4);
  box-shadow:
    0 4px 16px oklch(0 0 0 / 0.06),
    inset 0 1px 0 oklch(1 0 0 / 0.3);          /* inner highlight for light source */
}

/* Dark glass variant */
.glass-surface-dark {
  background: oklch(0.15 0 0 / 0.5);
  backdrop-filter: blur(20px) saturate(1.5) brightness(0.8);
  -webkit-backdrop-filter: blur(20px) saturate(1.5) brightness(0.8);
  border: 1px solid oklch(1 0 0 / 0.08);
  box-shadow:
    0 4px 16px oklch(0 0 0 / 0.3),
    inset 0 1px 0 oklch(1 0 0 / 0.05);
}

/* Colored/tinted glass */
.glass-surface-tinted {
  background: oklch(0.6 0.1 255 / 0.15);       /* blue tint */
  backdrop-filter: blur(24px) saturate(2);
  -webkit-backdrop-filter: blur(24px) saturate(2);
  border: 1px solid oklch(0.7 0.1 255 / 0.2);
}
```

### When to Use Glassmorphism
- Navigation bars overlaying hero images or video
- Floating toolbars and controls over content
- Notification cards that need context awareness
- Music/media player overlays
- iOS-style system UI elements

### When NOT to Use
- Over plain/solid backgrounds (no benefit, just blurry nothing)
- On text-heavy reading surfaces (readability suffers)
- When high contrast is required (accessibility concern)
- Performance-constrained environments (low-end mobile)

### Performance Considerations
- `backdrop-filter` forces compositing of all underlying layers
- Blur radius directly impacts GPU cost — keep under 24px
- Avoid nesting glass surfaces (each adds a full-screen blur pass)
- Use `will-change: backdrop-filter` sparingly; prefer `contain: paint`
- Test on low-end devices — Intel integrated GPUs struggle with large blur areas

---

## 11. Neumorphism

### Core Specs
Neumorphism creates soft, extruded elements using dual shadows (one light, one dark) on a colored background.

```css
:root {
  --neu-bg: oklch(0.92 0.01 250);           /* Soft gray-blue background */
  --neu-light: oklch(1 0 0 / 0.7);          /* Light shadow (top-left) */
  --neu-dark: oklch(0.5 0.02 250 / 0.25);   /* Dark shadow (bottom-right) */
}

/* Raised neumorphic element */
.neu-raised {
  background: var(--neu-bg);
  border-radius: var(--radius-4);
  box-shadow:
    6px 6px 12px var(--neu-dark),
    -6px -6px 12px var(--neu-light);
}

/* Pressed/inset neumorphic element */
.neu-inset {
  background: var(--neu-bg);
  border-radius: var(--radius-4);
  box-shadow:
    inset 4px 4px 8px var(--neu-dark),
    inset -4px -4px 8px var(--neu-light);
}

/* Neumorphic button with states */
.neu-button {
  background: var(--neu-bg);
  border: none;
  border-radius: var(--radius-full);
  padding: 12px 32px;
  box-shadow:
    4px 4px 8px var(--neu-dark),
    -4px -4px 8px var(--neu-light);
  transition: box-shadow 150ms ease;
}

.neu-button:active {
  box-shadow:
    inset 3px 3px 6px var(--neu-dark),
    inset -3px -3px 6px var(--neu-light);
}
```

### Accessibility Concerns
Neumorphism has significant accessibility problems:
- **Low contrast boundaries**: Elements blend into their backgrounds (fails WCAG 1.4.11 non-text contrast)
- **Unclear interactive states**: Hard to distinguish clickable from decorative
- **Poor screen reader mapping**: Visual affordance is purely shadow-based, no semantic distinction
- **Mitigation**: Add a subtle 1px border at 3:1 contrast ratio minimum; use clear focus indicators

### When Appropriate
- Decorative/artistic interfaces (music players, personal portfolios)
- Single-feature showcase elements (not full-page layouts)
- Settings panels with toggle/slider controls (limited interaction set)
- Never for data-dense or accessibility-critical interfaces

---

## 12. Depth Cues Beyond Shadows

Shadows are one of many depth cues. A rich spatial UI combines several:

### Overlapping (Occlusion)
Elements partially covering others instantly convey layering order.
```css
.stacked-cards {
  display: grid;
  grid-template-columns: 1fr;
}
.stacked-cards > * {
  grid-area: 1 / 1;
}
.stacked-cards > :nth-child(1) { transform: rotate(-3deg); z-index: 1; }
.stacked-cards > :nth-child(2) { transform: rotate(0deg); z-index: 2; }
.stacked-cards > :nth-child(3) { transform: rotate(3deg); z-index: 3; }
```

### Scale (Size)
Larger elements feel closer. Useful for focus/zoom effects.
```css
.card-focused { transform: scale(1.05); z-index: 2; }
.card-background { transform: scale(0.95); opacity: 0.7; }
```

### Blur (Depth of Field)
Background blur simulates camera depth of field.
```css
.background-layer { filter: blur(4px); }
.foreground-layer { filter: none; }
```

### Opacity / Fog
Distant elements fade toward the background color.
```css
.depth-layer-far { opacity: 0.5; }
.depth-layer-mid { opacity: 0.8; }
.depth-layer-near { opacity: 1; }
```

### Parallax
Layers move at different speeds during scroll, creating depth.
```css
.parallax-container {
  perspective: 1000px;
  overflow-y: auto;
}
.parallax-far {
  transform: translateZ(-200px) scale(1.2);
}
.parallax-near {
  transform: translateZ(0);
}
```

### Atmospheric Perspective
Combine blur + desaturation + lightening for distant elements.
```css
.distant-element {
  filter: blur(2px) saturate(0.6) brightness(1.1);
}
```

---

## 13. Surface Materials

### Glass

```css
.surface-glass {
  background: oklch(1 0 0 / 0.5);
  backdrop-filter: blur(16px) saturate(1.8);
  -webkit-backdrop-filter: blur(16px) saturate(1.8);
  border: 1px solid oklch(1 0 0 / 0.25);
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.3);
}
```

### Paper

```css
.surface-paper {
  background: oklch(0.97 0.005 80);  /* Warm off-white */
  box-shadow:
    0 1px 3px oklch(0 0 0 / 0.08),
    0 0 0 1px oklch(0 0 0 / 0.04);
  /* Optional: noise texture for paper grain */
  background-image: url("data:image/svg+xml,..."); /* inline noise SVG */
}
```

### Metal (Brushed)

```css
.surface-metal {
  background: linear-gradient(
    135deg,
    oklch(0.85 0.005 250),
    oklch(0.78 0.005 250) 30%,
    oklch(0.88 0.005 250) 50%,
    oklch(0.76 0.005 250) 70%,
    oklch(0.82 0.005 250)
  );
  border: 1px solid oklch(0.70 0.005 250);
  box-shadow:
    inset 0 1px 0 oklch(1 0 0 / 0.25),
    inset 0 -1px 0 oklch(0 0 0 / 0.1),
    0 2px 8px oklch(0 0 0 / 0.15);
}
```

### Fabric / Soft

```css
.surface-fabric {
  background: oklch(0.95 0.01 80);
  /* Subtle woven texture via repeating gradients */
  background-image:
    repeating-linear-gradient(
      0deg,
      oklch(0 0 0 / 0.02) 0px,
      oklch(0 0 0 / 0.02) 1px,
      transparent 1px,
      transparent 3px
    ),
    repeating-linear-gradient(
      90deg,
      oklch(0 0 0 / 0.02) 0px,
      oklch(0 0 0 / 0.02) 1px,
      transparent 1px,
      transparent 3px
    );
  border-radius: var(--radius-3);
  box-shadow: 0 1px 4px oklch(0 0 0 / 0.05);
}
```

---

## 14. Dark Mode Shadows

### The Problem
Shadows on dark backgrounds are nearly invisible because there is very little contrast between a dark surface and a dark shadow. The standard shadow scale breaks down.

### Strategies

**1. Reduce shadow opacity and increase ambient**
```css
[data-theme="dark"] {
  --shadow-1: 0 1px 3px oklch(0 0 0 / 0.40), 0 1px 2px oklch(0 0 0 / 0.30);
  --shadow-2: 0 2px 8px oklch(0 0 0 / 0.50), 0 4px 16px oklch(0 0 0 / 0.35);
  --shadow-3: 0 4px 12px oklch(0 0 0 / 0.50), 0 12px 32px oklch(0 0 0 / 0.45);
  --shadow-4: 0 8px 24px oklch(0 0 0 / 0.60), 0 24px 64px oklch(0 0 0 / 0.50);
}
```

**2. Switch to border-based elevation**
```css
[data-theme="dark"] .card {
  background: oklch(0.25 0.01 250);
  border: 1px solid oklch(1 0 0 / 0.08);
  box-shadow: none; /* or very subtle */
}

[data-theme="dark"] .card-elevated {
  background: oklch(0.28 0.01 250); /* slightly lighter = higher */
  border: 1px solid oklch(1 0 0 / 0.10);
}
```

**3. Use tonal elevation (Material 3 approach)**
```css
[data-theme="dark"] {
  --surface-0: oklch(0.15 0.01 250);
  --surface-1: oklch(0.18 0.01 250);
  --surface-2: oklch(0.21 0.01 250);
  --surface-3: oklch(0.24 0.01 250);
  --surface-4: oklch(0.27 0.01 250);
}
```

**4. Inner shadows for recessed areas**
```css
[data-theme="dark"] .inset-well {
  background: oklch(0.12 0.01 250);
  box-shadow:
    inset 0 2px 4px oklch(0 0 0 / 0.4),
    inset 0 0 0 1px oklch(0 0 0 / 0.2);
}
```

**5. Glow for emphasis (inverse shadow)**
```css
[data-theme="dark"] .card-glow {
  box-shadow:
    0 0 20px oklch(0.55 0.2 255 / 0.15),
    0 0 40px oklch(0.55 0.2 255 / 0.05);
}
```

---

## 15. Performance

### Shadow Rendering Cost
Shadows trigger paint operations. The cost scales with:
- **Blur radius**: Larger blur = more pixels sampled = slower
- **Number of shadows**: Each shadow layer adds a paint pass
- **Element count**: 100 cards with 3-layer shadows = 300 shadow paints
- **Animation**: Transitioning `box-shadow` triggers repaint every frame

### Optimization Strategies

**`will-change` for animated shadows**
```css
.card-will-animate {
  will-change: box-shadow, transform;
}

/* Remove will-change when animation completes */
.card-will-animate.at-rest {
  will-change: auto;
}
```

**Prefer `transform` over `box-shadow` animation**
```css
/* Expensive: animating box-shadow */
.card:hover {
  box-shadow: var(--shadow-3); /* triggers repaint every frame */
}

/* Cheap: pre-render shadow, animate opacity */
.card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  box-shadow: var(--shadow-3);
  opacity: 0;
  transition: opacity 200ms ease;
  pointer-events: none;
}
.card:hover::after {
  opacity: 1; /* GPU-composited opacity change */
}
```

**GPU compositing with `filter: drop-shadow`**
```css
/* drop-shadow is sometimes GPU-accelerated where box-shadow is not */
.perf-shadow {
  filter: drop-shadow(0 4px 8px oklch(0 0 0 / 0.1));
}
```

**Reduce shadow layers in lists**
```css
/* Full shadow for standalone cards */
.card { box-shadow: var(--shadow-2); }

/* Simplified shadow for repeated list items */
.list-item { box-shadow: var(--shadow-1); }

/* Or border-only for dense lists */
.dense-list-item {
  border-bottom: 1px solid oklch(0 0 0 / 0.08);
  box-shadow: none;
}
```

### `contain` for Paint Isolation
```css
.card {
  contain: layout paint;  /* isolates paint to this element */
}
```

---

## 16. Full CSS Custom Property System

### Complete Elevation Token Set

```css
:root {
  /* ============================================
     ELEVATION TOKENS
     ============================================ */

  /* Shadow scale */
  --elevation-shadow-0: none;
  --elevation-shadow-1: 0 1px 2px oklch(0 0 0 / 0.06), 0 1px 3px oklch(0 0 0 / 0.10);
  --elevation-shadow-2: 0 2px 4px oklch(0 0 0 / 0.04), 0 4px 8px oklch(0 0 0 / 0.06), 0 12px 24px oklch(0 0 0 / 0.06);
  --elevation-shadow-3: 0 4px 8px oklch(0 0 0 / 0.04), 0 8px 16px oklch(0 0 0 / 0.06), 0 20px 40px oklch(0 0 0 / 0.10);
  --elevation-shadow-4: 0 8px 16px oklch(0 0 0 / 0.06), 0 16px 32px oklch(0 0 0 / 0.08), 0 32px 64px oklch(0 0 0 / 0.12);

  /* Z-index scale */
  --elevation-z-base: 0;
  --elevation-z-raised: 1;
  --elevation-z-dropdown: 100;
  --elevation-z-sticky: 200;
  --elevation-z-fixed: 300;
  --elevation-z-drawer: 400;
  --elevation-z-modal-backdrop: 500;
  --elevation-z-modal: 510;
  --elevation-z-popover: 600;
  --elevation-z-toast: 700;
  --elevation-z-tooltip: 800;
  --elevation-z-drag: 900;

  /* Border radius scale */
  --elevation-radius-0: 0px;
  --elevation-radius-xs: 2px;
  --elevation-radius-sm: 4px;
  --elevation-radius-md: 8px;
  --elevation-radius-lg: 12px;
  --elevation-radius-xl: 16px;
  --elevation-radius-2xl: 24px;
  --elevation-radius-full: 9999px;

  /* Surface colors (tonal elevation) */
  --elevation-surface-0: oklch(0.99 0 0);
  --elevation-surface-1: oklch(0.97 0.005 var(--brand-hue, 250));
  --elevation-surface-2: oklch(0.96 0.008 var(--brand-hue, 250));
  --elevation-surface-3: oklch(0.95 0.010 var(--brand-hue, 250));
  --elevation-surface-4: oklch(0.94 0.012 var(--brand-hue, 250));

  /* ============================================
     DENSITY TOKENS
     ============================================ */
  --density-target-min: 48px;
  --density-spacing-unit: 8px;
  --density-line-height: 1.5;

  /* ============================================
     GLASS TOKENS
     ============================================ */
  --glass-blur: 16px;
  --glass-saturation: 1.8;
  --glass-bg-opacity: 0.6;
  --glass-border-opacity: 0.2;
}

/* Dark mode overrides */
[data-theme="dark"] {
  --elevation-shadow-1: 0 1px 3px oklch(0 0 0 / 0.40), 0 1px 2px oklch(0 0 0 / 0.30);
  --elevation-shadow-2: 0 2px 8px oklch(0 0 0 / 0.50), 0 4px 16px oklch(0 0 0 / 0.35);
  --elevation-shadow-3: 0 4px 12px oklch(0 0 0 / 0.50), 0 12px 32px oklch(0 0 0 / 0.45);
  --elevation-shadow-4: 0 8px 24px oklch(0 0 0 / 0.60), 0 24px 64px oklch(0 0 0 / 0.50);

  --elevation-surface-0: oklch(0.15 0.01 250);
  --elevation-surface-1: oklch(0.18 0.01 250);
  --elevation-surface-2: oklch(0.21 0.01 250);
  --elevation-surface-3: oklch(0.24 0.01 250);
  --elevation-surface-4: oklch(0.27 0.01 250);

  --glass-bg-opacity: 0.3;
  --glass-border-opacity: 0.08;
}
```

### Semantic Aliases

```css
:root {
  /* Component-level semantic tokens */
  --card-shadow: var(--elevation-shadow-1);
  --card-radius: var(--elevation-radius-md);

  --dropdown-shadow: var(--elevation-shadow-2);
  --dropdown-radius: var(--elevation-radius-md);
  --dropdown-z: var(--elevation-z-dropdown);

  --modal-shadow: var(--elevation-shadow-3);
  --modal-radius: var(--elevation-radius-xl);
  --modal-z: var(--elevation-z-modal);

  --tooltip-shadow: var(--elevation-shadow-2);
  --tooltip-radius: var(--elevation-radius-sm);
  --tooltip-z: var(--elevation-z-tooltip);

  --toast-shadow: var(--elevation-shadow-2);
  --toast-radius: var(--elevation-radius-md);
  --toast-z: var(--elevation-z-toast);

  --input-shadow: var(--elevation-shadow-0);
  --input-radius: var(--elevation-radius-sm);

  --button-radius: var(--elevation-radius-md);
}
```

---

## 17. Figma Shadow Setup

### Creating Shadow Styles
In Figma, set up shared shadow styles that match each elevation level:

**Level 1 — Subtle Lift**
- Effect 1: Drop Shadow — X:0, Y:1, Blur:2, Spread:0, Color:#000 6%
- Effect 2: Drop Shadow — X:0, Y:1, Blur:3, Spread:0, Color:#000 10%

**Level 2 — Raised**
- Effect 1: Drop Shadow — X:0, Y:2, Blur:4, Spread:0, Color:#000 4%
- Effect 2: Drop Shadow — X:0, Y:4, Blur:8, Spread:0, Color:#000 6%
- Effect 3: Drop Shadow — X:0, Y:12, Blur:24, Spread:0, Color:#000 6%

**Level 3 — Floating**
- Effect 1: Drop Shadow — X:0, Y:4, Blur:8, Spread:0, Color:#000 4%
- Effect 2: Drop Shadow — X:0, Y:8, Blur:16, Spread:0, Color:#000 6%
- Effect 3: Drop Shadow — X:0, Y:20, Blur:40, Spread:0, Color:#000 10%

**Level 4 — Dramatic**
- Effect 1: Drop Shadow — X:0, Y:8, Blur:16, Spread:0, Color:#000 6%
- Effect 2: Drop Shadow — X:0, Y:16, Blur:32, Spread:0, Color:#000 8%
- Effect 3: Drop Shadow — X:0, Y:32, Blur:64, Spread:0, Color:#000 12%

### Auto-Layout Interaction
- Shadows extend beyond the frame bounds — ensure parent frames have **Clip content: OFF** or sufficient padding
- When using auto-layout, add padding to the outer container equal to the largest shadow's blur + offset to prevent clipping
- For Level 4 shadows, this means at least 96px padding (64px blur + 32px offset)
- Use Figma's "Layer" blend mode section to adjust shadow rendering to match CSS more closely

### Figma Variables for Shadows
As of Figma's variable system, shadow values can be stored as variables:
- Create a collection named "Elevation"
- Define color variables for each shadow layer's color
- Mode switching (Light/Dark) automatically swaps shadow intensities
- Shadow blur and offset values require number variables

### Design-to-Code Handoff
- Name shadow styles with the token name: `elevation/shadow-1`, `elevation/shadow-2`, etc.
- Use the same naming convention in CSS custom properties for 1:1 mapping
- Figma's Dev Mode exports shadow values as CSS — verify multi-layer shadows export correctly
- Plugins like Tokens Studio can sync Figma variables directly to CSS/JSON token files

---

## Cross-References
- design-token-presets — Complete token systems including elevation presets by industry
- platform-visual-standards — iOS 26 Liquid Glass, Material 3 Expressive elevation specifics
- component-patterns-code — Production components using these elevation tokens
- animation-recipe-library — Full motion recipes for elevation transitions
- color-palette-library — Shadow color derivation from palette
- accessibility-inclusive-design — WCAG non-text contrast requirements for elevation boundaries
