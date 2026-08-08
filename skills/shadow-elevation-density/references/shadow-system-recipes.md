# Shadow System Recipes — 12 Complete Production Systems

## How to Use This Reference

Each shadow system below includes:
- Design philosophy and when to use it
- Complete 5-level shadow scale (sm, md, lg, xl, 2xl) with exact CSS values
- Design token JSON for integration with any token pipeline
- Component-to-shadow mapping (which component gets which level)
- Dark mode variant with adjusted values
- CSS custom properties ready to copy

---

## 1. Minimal Shadows (Linear / Vercel Style)

**Philosophy:** Shadows should be nearly invisible. They exist only to provide the subtlest separation between surfaces. The interface feels flat but retains just enough depth to communicate layering.

**When to use:** Developer tools, documentation sites, minimalist SaaS, content-heavy platforms, design portfolios.

### Light Mode Scale

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
  --shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.04), 0 2px 4px rgba(0, 0, 0, 0.02);
  --shadow-xl: 0 8px 16px rgba(0, 0, 0, 0.06), 0 2px 4px rgba(0, 0, 0, 0.02);
  --shadow-2xl: 0 14px 28px rgba(0, 0, 0, 0.06), 0 4px 8px rgba(0, 0, 0, 0.02);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.24), 0 1px 2px rgba(0, 0, 0, 0.12);
  --shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.24), 0 2px 4px rgba(0, 0, 0, 0.12);
  --shadow-xl: 0 8px 16px rgba(0, 0, 0, 0.28), 0 2px 4px rgba(0, 0, 0, 0.12);
  --shadow-2xl: 0 14px 28px rgba(0, 0, 0, 0.32), 0 4px 8px rgba(0, 0, 0, 0.12);
}
```

### Design Tokens

```json
{
  "shadow": {
    "minimal": {
      "sm":  { "value": "0 1px 2px rgba(0,0,0,0.04)" },
      "md":  { "value": "0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02)" },
      "lg":  { "value": "0 4px 8px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.02)" },
      "xl":  { "value": "0 8px 16px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.02)" },
      "2xl": { "value": "0 14px 28px rgba(0,0,0,0.06), 0 4px 8px rgba(0,0,0,0.02)" }
    }
  }
}
```

### Component Mapping

| Component | Shadow Level | Notes |
|-----------|-------------|-------|
| Card (resting) | none or sm | Rely on borders instead |
| Card (hovered) | md | Subtle lift on hover |
| Dropdown / Menu | lg | Needs separation from page |
| Modal / Dialog | xl | Clear floating surface |
| Tooltip | md | Small, subtle float |
| Toast / Notification | lg | Noticeable but not dramatic |
| Button | none | Flat, no shadow |
| Popover | lg | Consistent with dropdown |

### Key Characteristics
- Maximum opacity never exceeds 0.06
- Two-layer shadows even at the smallest size
- Borders (1px solid rgba(0,0,0,0.06)) do most of the separation work
- Dark mode multiplies opacity by ~5x

---

## 2. Layered Shadows (Stripe Style)

**Philosophy:** Realistic, sophisticated depth through multiple carefully tuned shadow layers. Each level uses 2-3 layers to simulate penumbra and umbra, creating shadows that feel genuinely three-dimensional.

**When to use:** Fintech, premium SaaS, design tools, dashboards, products that need to feel polished and trustworthy.

### Light Mode Scale

```css
:root {
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08),
               0 1px 2px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.05),
               0 2px 4px rgba(0, 0, 0, 0.04),
               0 1px 2px rgba(0, 0, 0, 0.03);
  --shadow-lg: 0 10px 20px rgba(0, 0, 0, 0.06),
               0 4px 8px rgba(0, 0, 0, 0.04),
               0 1px 3px rgba(0, 0, 0, 0.03);
  --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.08),
               0 8px 16px rgba(0, 0, 0, 0.04),
               0 2px 4px rgba(0, 0, 0, 0.03);
  --shadow-2xl: 0 32px 64px rgba(0, 0, 0, 0.1),
                0 16px 32px rgba(0, 0, 0, 0.06),
                0 4px 8px rgba(0, 0, 0, 0.03);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3),
               0 1px 2px rgba(0, 0, 0, 0.24);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.28),
               0 2px 4px rgba(0, 0, 0, 0.2),
               0 0 0 1px rgba(255, 255, 255, 0.04);
  --shadow-lg: 0 10px 20px rgba(0, 0, 0, 0.32),
               0 4px 8px rgba(0, 0, 0, 0.2),
               0 0 0 1px rgba(255, 255, 255, 0.04);
  --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.36),
               0 8px 16px rgba(0, 0, 0, 0.2),
               0 0 0 1px rgba(255, 255, 255, 0.04);
  --shadow-2xl: 0 32px 64px rgba(0, 0, 0, 0.4),
                0 16px 32px rgba(0, 0, 0, 0.24),
                0 0 0 1px rgba(255, 255, 255, 0.04);
}
```

### Design Tokens

```json
{
  "shadow": {
    "layered": {
      "sm":  { "value": "0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)" },
      "md":  { "value": "0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03)" },
      "lg":  { "value": "0 10px 20px rgba(0,0,0,0.06), 0 4px 8px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.03)" },
      "xl":  { "value": "0 20px 40px rgba(0,0,0,0.08), 0 8px 16px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.03)" },
      "2xl": { "value": "0 32px 64px rgba(0,0,0,0.1), 0 16px 32px rgba(0,0,0,0.06), 0 4px 8px rgba(0,0,0,0.03)" }
    }
  }
}
```

### Component Mapping

| Component | Shadow Level | Notes |
|-----------|-------------|-------|
| Card (resting) | sm | Always visible depth |
| Card (hovered) | lg | Noticeable lift |
| Dropdown / Menu | lg | Floating panel feel |
| Modal / Dialog | 2xl | Maximum depth |
| Tooltip | md | Subtle float |
| Toast / Notification | xl | Demands attention |
| Button (resting) | sm | Slight raised feel |
| Button (pressed) | none or inset | Pushed-in feedback |
| Popover | xl | Clear hierarchy |

### Key Characteristics
- Three layers at md and above for maximum realism
- Each layer roughly doubles blur from previous
- Dark mode adds a 1px ring shadow for edge definition
- Opacity stays below 0.1 per layer for subtlety

---

## 3. Material Shadows (Google Style)

**Philosophy:** Systematic, dp-based elevation that maps directly to the Material Design specification. Shadows are directional (light from top-left) with consistent key light and ambient light separation.

**When to use:** Material Design apps, Android-focused products, Google-ecosystem products, any project using Material UI or Material Web.

### Light Mode Scale

```css
:root {
  /* Key light (directional) + Ambient light (omnidirectional) */
  --shadow-sm: 0 1px 1px 0 rgba(0, 0, 0, 0.14),
               0 2px 1px -1px rgba(0, 0, 0, 0.12),
               0 1px 3px 0 rgba(0, 0, 0, 0.2);
  --shadow-md: 0 3px 4px 0 rgba(0, 0, 0, 0.14),
               0 3px 3px -2px rgba(0, 0, 0, 0.12),
               0 1px 8px 0 rgba(0, 0, 0, 0.2);
  --shadow-lg: 0 6px 10px 0 rgba(0, 0, 0, 0.14),
               0 1px 18px 0 rgba(0, 0, 0, 0.12),
               0 3px 5px -1px rgba(0, 0, 0, 0.2);
  --shadow-xl: 0 9px 12px -6px rgba(0, 0, 0, 0.14),
               0 6px 30px 5px rgba(0, 0, 0, 0.12),
               0 12px 17px 2px rgba(0, 0, 0, 0.2);
  --shadow-2xl: 0 11px 15px -7px rgba(0, 0, 0, 0.14),
                0 9px 46px 8px rgba(0, 0, 0, 0.12),
                0 24px 38px 3px rgba(0, 0, 0, 0.2);
}
```

### Dark Mode Scale (Material 3 tint approach)

```css
:root[data-theme="dark"] {
  /* Material 3: Shadows + surface tint overlay */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 2px 6px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.3);
  --shadow-xl: 0 8px 24px rgba(0, 0, 0, 0.3);
  --shadow-2xl: 0 12px 36px rgba(0, 0, 0, 0.3);

  /* Surface tint overlays (apply as background-color blend) */
  --surface-tint-1: rgba(var(--primary-rgb), 0.05);
  --surface-tint-2: rgba(var(--primary-rgb), 0.08);
  --surface-tint-3: rgba(var(--primary-rgb), 0.11);
  --surface-tint-4: rgba(var(--primary-rgb), 0.12);
  --surface-tint-5: rgba(var(--primary-rgb), 0.14);
}
```

### Design Tokens

```json
{
  "shadow": {
    "material": {
      "sm":  { "value": "0 1px 1px 0 rgba(0,0,0,0.14), 0 2px 1px -1px rgba(0,0,0,0.12), 0 1px 3px 0 rgba(0,0,0,0.2)", "dp": 2 },
      "md":  { "value": "0 3px 4px 0 rgba(0,0,0,0.14), 0 3px 3px -2px rgba(0,0,0,0.12), 0 1px 8px 0 rgba(0,0,0,0.2)", "dp": 6 },
      "lg":  { "value": "0 6px 10px 0 rgba(0,0,0,0.14), 0 1px 18px 0 rgba(0,0,0,0.12), 0 3px 5px -1px rgba(0,0,0,0.2)", "dp": 12 },
      "xl":  { "value": "0 9px 12px -6px rgba(0,0,0,0.14), 0 6px 30px 5px rgba(0,0,0,0.12), 0 12px 17px 2px rgba(0,0,0,0.2)", "dp": 16 },
      "2xl": { "value": "0 11px 15px -7px rgba(0,0,0,0.14), 0 9px 46px 8px rgba(0,0,0,0.12), 0 24px 38px 3px rgba(0,0,0,0.2)", "dp": 24 }
    }
  }
}
```

### Component Mapping (Material Spec)

| Component | Shadow Level | Material dp |
|-----------|-------------|------------|
| Card (resting) | sm | 1-2dp |
| Button (raised) | sm | 2dp |
| FAB (resting) | md | 6dp |
| App bar (scrolled) | sm | 4dp |
| Bottom sheet | lg | 8dp |
| Navigation drawer | lg | 12dp |
| Modal side sheet | xl | 16dp |
| Dialog | 2xl | 24dp |

### Key Characteristics
- Three layers per shadow mimicking key light + ambient light
- Negative spread values to keep shadows tight
- Higher base opacity than other systems (0.12-0.2)
- Dark mode relies on surface tint more than shadow

---

## 4. Soft Shadows (Apple Style)

**Philosophy:** Large blur radius, very low opacity, generous spread. Shadows feel like a soft glow rather than a hard edge. This creates a sense of objects floating gently above the surface.

**When to use:** iOS/macOS-inspired apps, premium consumer products, health/wellness apps, creative tools, editorial design.

### Light Mode Scale

```css
:root {
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 8px 30px rgba(0, 0, 0, 0.08);
  --shadow-xl: 0 12px 48px rgba(0, 0, 0, 0.1);
  --shadow-2xl: 0 24px 80px rgba(0, 0, 0, 0.12);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.2),
               0 0 0 1px rgba(255, 255, 255, 0.03);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.28),
               0 0 0 1px rgba(255, 255, 255, 0.04);
  --shadow-lg: 0 8px 30px rgba(0, 0, 0, 0.36),
               0 0 0 1px rgba(255, 255, 255, 0.04);
  --shadow-xl: 0 12px 48px rgba(0, 0, 0, 0.4),
               0 0 0 1px rgba(255, 255, 255, 0.05);
  --shadow-2xl: 0 24px 80px rgba(0, 0, 0, 0.48),
                0 0 0 1px rgba(255, 255, 255, 0.05);
}
```

### Design Tokens

```json
{
  "shadow": {
    "soft": {
      "sm":  { "value": "0 2px 8px rgba(0,0,0,0.04)" },
      "md":  { "value": "0 4px 16px rgba(0,0,0,0.06)" },
      "lg":  { "value": "0 8px 30px rgba(0,0,0,0.08)" },
      "xl":  { "value": "0 12px 48px rgba(0,0,0,0.1)" },
      "2xl": { "value": "0 24px 80px rgba(0,0,0,0.12)" }
    }
  }
}
```

### Component Mapping

| Component | Shadow Level | Notes |
|-----------|-------------|-------|
| Card (resting) | sm | Gentle float |
| Card (hovered) | md | Lifts slightly |
| Dropdown / Menu | lg | Soft floating panel |
| Modal / Dialog | 2xl | Dramatic but gentle |
| Tooltip | sm | Barely there |
| Sheet / Drawer | xl | Large overlay |
| Button | none | Flat by default |
| Popover | lg | Matches dropdown |

### Key Characteristics
- Single-layer shadows (simplicity is the point)
- Blur radius is always 4-6x the y-offset
- Opacity never exceeds 0.12 in light mode
- Very large blur values at xl/2xl create ethereal floating effect
- Dark mode adds thin ring shadows for edge definition

---

## 5. Flat Design (No Shadows — Border-Based)

**Philosophy:** Zero shadows. Separation is achieved entirely through borders, background colors, and spacing. The interface is purely two-dimensional.

**When to use:** Brutalist design, technical tools, code editors, terminal-inspired UIs, retro-styled products, some editorial designs.

### Light Mode Scale

```css
:root {
  --shadow-sm: none; /* Use --border-subtle instead */
  --shadow-md: none;
  --shadow-lg: none;
  --shadow-xl: none;
  --shadow-2xl: none;

  /* Replacement system: borders and backgrounds */
  --border-subtle: 1px solid rgba(0, 0, 0, 0.06);
  --border-default: 1px solid rgba(0, 0, 0, 0.12);
  --border-strong: 1px solid rgba(0, 0, 0, 0.2);
  --border-heavy: 2px solid rgba(0, 0, 0, 0.8);
  --border-solid: 1px solid #000;

  --surface-raised: rgba(0, 0, 0, 0.02);
  --surface-overlay: rgba(0, 0, 0, 0.04);
  --surface-backdrop: rgba(0, 0, 0, 0.5);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --border-subtle: 1px solid rgba(255, 255, 255, 0.06);
  --border-default: 1px solid rgba(255, 255, 255, 0.12);
  --border-strong: 1px solid rgba(255, 255, 255, 0.2);
  --border-heavy: 2px solid rgba(255, 255, 255, 0.8);
  --border-solid: 1px solid #fff;

  --surface-raised: rgba(255, 255, 255, 0.03);
  --surface-overlay: rgba(255, 255, 255, 0.06);
  --surface-backdrop: rgba(0, 0, 0, 0.7);
}
```

### Design Tokens

```json
{
  "shadow": {
    "flat": {
      "sm": { "value": "none" },
      "md": { "value": "none" },
      "lg": { "value": "none" },
      "xl": { "value": "none" },
      "2xl": { "value": "none" }
    }
  },
  "border": {
    "subtle":  { "value": "1px solid rgba(0,0,0,0.06)" },
    "default": { "value": "1px solid rgba(0,0,0,0.12)" },
    "strong":  { "value": "1px solid rgba(0,0,0,0.2)" },
    "heavy":   { "value": "2px solid rgba(0,0,0,0.8)" },
    "solid":   { "value": "1px solid #000" }
  }
}
```

### Component Mapping

| Component | Elevation Method | Notes |
|-----------|-----------------|-------|
| Card (resting) | border-subtle + surface-raised | Background tint replaces shadow |
| Card (hovered) | border-default | Border darkens on hover |
| Dropdown / Menu | border-strong | Stronger border = higher |
| Modal / Dialog | border-heavy + surface-backdrop | Heavy border + dimmed backdrop |
| Tooltip | border-default + surface-raised | Subtle box |
| Toast | border-strong | Ring notification style |
| Button | border-default | Classic bordered button |

### Key Characteristics
- Zero box-shadow anywhere in the system
- Hierarchy communicated through border weight and background color
- Clean, fast rendering (no paint operations for shadows)
- Works perfectly for print-inspired or brutalist aesthetics

---

## 6. Colored Shadows (Brand-Tinted)

**Philosophy:** Shadows pick up color from the element they belong to or from the brand palette. This creates a vibrant, energetic feel where shadows reinforce brand identity rather than being neutral gray.

**When to use:** Creative agencies, gaming, music/entertainment, bold consumer brands, marketing landing pages, playful products.

### Light Mode Scale

```css
:root {
  --primary-h: 230;
  --primary-s: 80%;

  --shadow-sm: 0 2px 4px hsla(var(--primary-h), var(--primary-s), 30%, 0.08);
  --shadow-md: 0 4px 12px hsla(var(--primary-h), var(--primary-s), 30%, 0.12);
  --shadow-lg: 0 8px 24px hsla(var(--primary-h), var(--primary-s), 30%, 0.16);
  --shadow-xl: 0 12px 40px hsla(var(--primary-h), var(--primary-s), 30%, 0.2);
  --shadow-2xl: 0 20px 60px hsla(var(--primary-h), var(--primary-s), 30%, 0.24);
}

/* Element-specific colored shadows */
.btn-primary {
  box-shadow: 0 4px 14px hsla(var(--primary-h), var(--primary-s), 40%, 0.3);
}
.btn-success {
  box-shadow: 0 4px 14px hsla(142, 70%, 35%, 0.3);
}
.btn-danger {
  box-shadow: 0 4px 14px hsla(0, 70%, 45%, 0.3);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --shadow-sm: 0 2px 4px hsla(var(--primary-h), var(--primary-s), 20%, 0.2),
               0 0 0 1px rgba(255, 255, 255, 0.04);
  --shadow-md: 0 4px 12px hsla(var(--primary-h), var(--primary-s), 20%, 0.28);
  --shadow-lg: 0 8px 24px hsla(var(--primary-h), var(--primary-s), 20%, 0.32);
  --shadow-xl: 0 12px 40px hsla(var(--primary-h), var(--primary-s), 20%, 0.36);
  --shadow-2xl: 0 20px 60px hsla(var(--primary-h), var(--primary-s), 20%, 0.4);
}
```

### Design Tokens

```json
{
  "shadow": {
    "colored": {
      "sm":  { "value": "0 2px 4px hsla(230,80%,30%,0.08)" },
      "md":  { "value": "0 4px 12px hsla(230,80%,30%,0.12)" },
      "lg":  { "value": "0 8px 24px hsla(230,80%,30%,0.16)" },
      "xl":  { "value": "0 12px 40px hsla(230,80%,30%,0.2)" },
      "2xl": { "value": "0 20px 60px hsla(230,80%,30%,0.24)" }
    }
  }
}
```

### Component Mapping

| Component | Shadow Level | Notes |
|-----------|-------------|-------|
| Card (resting) | sm | Subtle tint |
| Card (hovered) | lg | Color becomes visible |
| CTA button | md | Always tinted |
| Dropdown | lg | Brand-tinted floating |
| Modal | 2xl | Dramatic brand glow |
| Image card | element-specific | Shadow matches dominant image color |
| Badge/Tag | sm | Subtle color reinforcement |

### Key Characteristics
- Shadow hue matches the brand primary (or the element's own color)
- Lower lightness in the shadow (30-40%) keeps it grounded
- Creates strong visual identity
- Dark mode uses even lower lightness values
- Per-element colored shadows possible for image-heavy UIs

---

## 7. Dark Mode Shadows (Ambient Glow Approach)

**Philosophy:** Abandon traditional downward shadows entirely for dark mode. Instead, use omnidirectional glows, luminous edges, and surface color gradients to convey elevation. This matches how we perceive depth in low-light environments — light sources glow, they do not cast dark shadows.

**When to use:** Any dark mode interface. Especially effective for media apps, music players, creative tools, and entertainment platforms.

### Glow Scale

```css
:root[data-theme="dark"] {
  --glow-sm: 0 0 1px rgba(255, 255, 255, 0.04),
             0 0 4px rgba(255, 255, 255, 0.02);
  --glow-md: 0 0 1px rgba(255, 255, 255, 0.06),
             0 0 8px rgba(255, 255, 255, 0.03),
             0 2px 8px rgba(0, 0, 0, 0.3);
  --glow-lg: 0 0 1px rgba(255, 255, 255, 0.08),
             0 0 16px rgba(255, 255, 255, 0.04),
             0 4px 16px rgba(0, 0, 0, 0.3);
  --glow-xl: 0 0 1px rgba(255, 255, 255, 0.1),
             0 0 24px rgba(255, 255, 255, 0.05),
             0 8px 32px rgba(0, 0, 0, 0.3);
  --glow-2xl: 0 0 2px rgba(255, 255, 255, 0.12),
              0 0 40px rgba(255, 255, 255, 0.06),
              0 16px 48px rgba(0, 0, 0, 0.3);
}
```

### Surface Color Scale (Complementary)

```css
:root[data-theme="dark"] {
  --surface-base: #0a0a0a;
  --surface-1: #141414;
  --surface-2: #1c1c1c;
  --surface-3: #242424;
  --surface-4: #2e2e2e;
  --surface-5: #383838;

  --border-glow-subtle: 1px solid rgba(255, 255, 255, 0.04);
  --border-glow-default: 1px solid rgba(255, 255, 255, 0.08);
  --border-glow-strong: 1px solid rgba(255, 255, 255, 0.12);
}
```

### Design Tokens

```json
{
  "shadow": {
    "glow": {
      "sm":  { "value": "0 0 1px rgba(255,255,255,0.04), 0 0 4px rgba(255,255,255,0.02)" },
      "md":  { "value": "0 0 1px rgba(255,255,255,0.06), 0 0 8px rgba(255,255,255,0.03), 0 2px 8px rgba(0,0,0,0.3)" },
      "lg":  { "value": "0 0 1px rgba(255,255,255,0.08), 0 0 16px rgba(255,255,255,0.04), 0 4px 16px rgba(0,0,0,0.3)" },
      "xl":  { "value": "0 0 1px rgba(255,255,255,0.1), 0 0 24px rgba(255,255,255,0.05), 0 8px 32px rgba(0,0,0,0.3)" },
      "2xl": { "value": "0 0 2px rgba(255,255,255,0.12), 0 0 40px rgba(255,255,255,0.06), 0 16px 48px rgba(0,0,0,0.3)" }
    }
  }
}
```

### Component Mapping

| Component | Shadow Level | Surface Level | Notes |
|-----------|-------------|--------------|-------|
| Card (resting) | sm | surface-2 | Glow barely visible |
| Card (hovered) | md | surface-3 | Glow intensifies |
| Dropdown | lg | surface-3 | Clear glow ring |
| Modal | 2xl | surface-4 | Full glow treatment |
| Tooltip | md | surface-3 | Small luminous box |
| Sidebar | sm | surface-1 | Subtle differentiation |
| Floating button | lg | surface-3 | Prominent glow |

### Key Characteristics
- White/light-colored shadow layers create glow effect
- Dark shadow layers underneath add grounding
- Surface colors step lighter at each elevation
- Thin luminous borders reinforce edges
- Combined effect: elements seem to emit light rather than block it

---

## 8. High Contrast Shadows (Accessibility-Focused)

**Philosophy:** Shadows that are clearly visible to users with low vision or in high-contrast modes. These are intentionally stronger and more defined than typical shadows to ensure that elevation differences are perceivable.

**When to use:** Accessibility-critical applications, healthcare, government, education, interfaces for older users, any product with WCAG AAA aspirations.

### Light Mode Scale

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.12),
               0 0 0 1px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 2px 6px rgba(0, 0, 0, 0.16),
               0 0 0 1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.2),
               0 0 0 1px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 8px 24px rgba(0, 0, 0, 0.24),
               0 0 0 1px rgba(0, 0, 0, 0.12);
  --shadow-2xl: 0 16px 40px rgba(0, 0, 0, 0.28),
                0 0 0 1px rgba(0, 0, 0, 0.14);
}

/* Forced high-contrast mode support */
@media (forced-colors: active) {
  .elevated {
    border: 2px solid ButtonText;
    box-shadow: none;
  }
}

/* prefers-contrast: more */
@media (prefers-contrast: more) {
  :root {
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(0, 0, 0, 0.16);
    --shadow-md: 0 2px 6px rgba(0, 0, 0, 0.28), 0 0 0 1px rgba(0, 0, 0, 0.2);
    --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.32), 0 0 0 1px rgba(0, 0, 0, 0.2);
    --shadow-xl: 0 8px 24px rgba(0, 0, 0, 0.36), 0 0 0 1px rgba(0, 0, 0, 0.24);
    --shadow-2xl: 0 16px 40px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(0, 0, 0, 0.28);
  }
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.4),
               0 0 0 1px rgba(255, 255, 255, 0.1);
  --shadow-md: 0 2px 6px rgba(0, 0, 0, 0.5),
               0 0 0 1px rgba(255, 255, 255, 0.12);
  --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.5),
               0 0 0 1px rgba(255, 255, 255, 0.14);
  --shadow-xl: 0 8px 24px rgba(0, 0, 0, 0.6),
               0 0 0 1px rgba(255, 255, 255, 0.16);
  --shadow-2xl: 0 16px 40px rgba(0, 0, 0, 0.6),
                0 0 0 1px rgba(255, 255, 255, 0.2);
}
```

### Design Tokens

```json
{
  "shadow": {
    "high-contrast": {
      "sm":  { "value": "0 1px 2px rgba(0,0,0,0.12), 0 0 0 1px rgba(0,0,0,0.08)" },
      "md":  { "value": "0 2px 6px rgba(0,0,0,0.16), 0 0 0 1px rgba(0,0,0,0.1)" },
      "lg":  { "value": "0 4px 12px rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.1)" },
      "xl":  { "value": "0 8px 24px rgba(0,0,0,0.24), 0 0 0 1px rgba(0,0,0,0.12)" },
      "2xl": { "value": "0 16px 40px rgba(0,0,0,0.28), 0 0 0 1px rgba(0,0,0,0.14)" }
    }
  }
}
```

### Key Characteristics
- Every shadow level includes a ring shadow (0 0 0 1px) for hard edge definition
- Base opacity starts at 0.12 (3x typical minimal shadows)
- `forced-colors` media query replaces shadows with visible borders
- `prefers-contrast: more` increases all shadow intensities
- Dark mode ring shadows use white for clear edge visibility

---

## 9. Neumorphic Shadows (Soft UI)

**Philosophy:** Elements appear extruded from or pressed into the background surface. Achieved by combining a light shadow (top-left, simulating reflected light) with a dark shadow (bottom-right, simulating cast shadow). The background color must closely match the element color.

**When to use:** Experimental UIs, creative portfolios, music/audio interfaces, calculator-style UIs. Use with extreme caution — neumorphism has significant accessibility concerns.

### Light Mode Scale

```css
:root {
  --bg-color: #e0e0e0;

  /* Raised (extruded) variants */
  --shadow-sm: 2px 2px 4px rgba(0, 0, 0, 0.1),
               -2px -2px 4px rgba(255, 255, 255, 0.7);
  --shadow-md: 4px 4px 8px rgba(0, 0, 0, 0.12),
               -4px -4px 8px rgba(255, 255, 255, 0.8);
  --shadow-lg: 6px 6px 16px rgba(0, 0, 0, 0.14),
               -6px -6px 16px rgba(255, 255, 255, 0.8);
  --shadow-xl: 10px 10px 24px rgba(0, 0, 0, 0.16),
               -10px -10px 24px rgba(255, 255, 255, 0.8);
  --shadow-2xl: 16px 16px 40px rgba(0, 0, 0, 0.18),
                -16px -16px 40px rgba(255, 255, 255, 0.8);

  /* Pressed (inset) variants */
  --shadow-inset-sm: inset 2px 2px 4px rgba(0, 0, 0, 0.1),
                     inset -2px -2px 4px rgba(255, 255, 255, 0.7);
  --shadow-inset-md: inset 4px 4px 8px rgba(0, 0, 0, 0.12),
                     inset -4px -4px 8px rgba(255, 255, 255, 0.8);
  --shadow-inset-lg: inset 6px 6px 16px rgba(0, 0, 0, 0.14),
                     inset -6px -6px 16px rgba(255, 255, 255, 0.8);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --bg-color: #2a2a2a;

  --shadow-sm: 2px 2px 4px rgba(0, 0, 0, 0.4),
               -2px -2px 4px rgba(255, 255, 255, 0.04);
  --shadow-md: 4px 4px 8px rgba(0, 0, 0, 0.5),
               -4px -4px 8px rgba(255, 255, 255, 0.05);
  --shadow-lg: 6px 6px 16px rgba(0, 0, 0, 0.5),
               -6px -6px 16px rgba(255, 255, 255, 0.05);
  --shadow-xl: 10px 10px 24px rgba(0, 0, 0, 0.6),
               -10px -10px 24px rgba(255, 255, 255, 0.06);
  --shadow-2xl: 16px 16px 40px rgba(0, 0, 0, 0.6),
                -16px -16px 40px rgba(255, 255, 255, 0.06);

  --shadow-inset-sm: inset 2px 2px 4px rgba(0, 0, 0, 0.4),
                     inset -2px -2px 4px rgba(255, 255, 255, 0.04);
  --shadow-inset-md: inset 4px 4px 8px rgba(0, 0, 0, 0.5),
                     inset -4px -4px 8px rgba(255, 255, 255, 0.05);
}
```

### Design Tokens

```json
{
  "shadow": {
    "neumorphic": {
      "raised": {
        "sm":  { "value": "2px 2px 4px rgba(0,0,0,0.1), -2px -2px 4px rgba(255,255,255,0.7)" },
        "md":  { "value": "4px 4px 8px rgba(0,0,0,0.12), -4px -4px 8px rgba(255,255,255,0.8)" },
        "lg":  { "value": "6px 6px 16px rgba(0,0,0,0.14), -6px -6px 16px rgba(255,255,255,0.8)" },
        "xl":  { "value": "10px 10px 24px rgba(0,0,0,0.16), -10px -10px 24px rgba(255,255,255,0.8)" },
        "2xl": { "value": "16px 16px 40px rgba(0,0,0,0.18), -16px -16px 40px rgba(255,255,255,0.8)" }
      },
      "inset": {
        "sm":  { "value": "inset 2px 2px 4px rgba(0,0,0,0.1), inset -2px -2px 4px rgba(255,255,255,0.7)" },
        "md":  { "value": "inset 4px 4px 8px rgba(0,0,0,0.12), inset -4px -4px 8px rgba(255,255,255,0.8)" },
        "lg":  { "value": "inset 6px 6px 16px rgba(0,0,0,0.14), inset -6px -6px 16px rgba(255,255,255,0.8)" }
      }
    }
  }
}
```

### Accessibility Warnings

- Low contrast between raised elements and background is inherent to the style
- Buttons may not look clickable — always pair with text labels, never icon-only
- Inset states can be confused with disabled states
- Not suitable for data-heavy or productivity applications
- Always provide alternative high-contrast mode
- Screen readers cannot perceive neumorphic state changes — ensure proper ARIA states

---

## 10. Dramatic Shadows (Editorial / Heavy)

**Philosophy:** Shadows as a bold design statement. Large offsets, strong opacity, sometimes hard-edged. These shadows do not simulate physics — they are graphic elements in their own right.

**When to use:** Editorial design, portfolio sites, fashion/luxury, magazine-style layouts, hero sections, artistic/expressive interfaces.

### Light Mode Scale

```css
:root {
  --shadow-sm: 4px 4px 0 rgba(0, 0, 0, 0.1);
  --shadow-md: 6px 6px 0 rgba(0, 0, 0, 0.15);
  --shadow-lg: 8px 8px 0 rgba(0, 0, 0, 0.2);
  --shadow-xl: 12px 12px 0 rgba(0, 0, 0, 0.2);
  --shadow-2xl: 20px 20px 0 rgba(0, 0, 0, 0.25);

  /* Hard-edge variant (no blur at all) */
  --shadow-hard-sm: 3px 3px 0 #000;
  --shadow-hard-md: 5px 5px 0 #000;
  --shadow-hard-lg: 8px 8px 0 #000;
  --shadow-hard-xl: 12px 12px 0 #000;
  --shadow-hard-2xl: 20px 20px 0 #000;

  /* Colored hard-edge */
  --shadow-hard-primary: 4px 4px 0 var(--color-primary);
  --shadow-hard-accent: 4px 4px 0 var(--color-accent);
}
```

### Dark Mode Scale

```css
:root[data-theme="dark"] {
  --shadow-sm: 4px 4px 0 rgba(0, 0, 0, 0.4);
  --shadow-md: 6px 6px 0 rgba(0, 0, 0, 0.5);
  --shadow-lg: 8px 8px 0 rgba(0, 0, 0, 0.5);
  --shadow-xl: 12px 12px 0 rgba(0, 0, 0, 0.6);
  --shadow-2xl: 20px 20px 0 rgba(0, 0, 0, 0.6);

  --shadow-hard-sm: 3px 3px 0 rgba(255, 255, 255, 0.2);
  --shadow-hard-md: 5px 5px 0 rgba(255, 255, 255, 0.2);
  --shadow-hard-lg: 8px 8px 0 rgba(255, 255, 255, 0.2);
}
```

### Design Tokens

```json
{
  "shadow": {
    "dramatic": {
      "sm":  { "value": "4px 4px 0 rgba(0,0,0,0.1)" },
      "md":  { "value": "6px 6px 0 rgba(0,0,0,0.15)" },
      "lg":  { "value": "8px 8px 0 rgba(0,0,0,0.2)" },
      "xl":  { "value": "12px 12px 0 rgba(0,0,0,0.2)" },
      "2xl": { "value": "20px 20px 0 rgba(0,0,0,0.25)" }
    },
    "dramatic-hard": {
      "sm":  { "value": "3px 3px 0 #000" },
      "md":  { "value": "5px 5px 0 #000" },
      "lg":  { "value": "8px 8px 0 #000" },
      "xl":  { "value": "12px 12px 0 #000" },
      "2xl": { "value": "20px 20px 0 #000" }
    }
  }
}
```

### Key Characteristics
- Equal x and y offset (diagonal shadow)
- Zero or near-zero blur for graphic hard-edge look
- Can use solid colors including brand palette
- Dark mode can invert to light hard-edge shadows
- Hover effects can shift offset: `transform: translate(-2px, -2px)` with increased shadow

---

## 11. Elevation Transition Shadows (Interactive Focus)

**Philosophy:** Designed specifically for state transitions. Each level pair (resting/active) is tuned for smooth CSS transitions between them. The emphasis is on how shadows feel in motion.

**When to use:** Any interface with interactive cards, buttons with hover states, draggable elements, selectable items.

### Complete Scale with Transition Pairs

```css
:root {
  /* Resting states */
  --shadow-rest: 0 1px 3px rgba(0, 0, 0, 0.06),
                 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-hover: 0 4px 12px rgba(0, 0, 0, 0.08),
                  0 2px 4px rgba(0, 0, 0, 0.04);
  --shadow-active: 0 1px 2px rgba(0, 0, 0, 0.08);
  --shadow-focus: 0 0 0 3px rgba(var(--primary-rgb), 0.3),
                  0 1px 3px rgba(0, 0, 0, 0.06);
  --shadow-dragging: 0 16px 40px rgba(0, 0, 0, 0.12),
                     0 4px 12px rgba(0, 0, 0, 0.06);
  --shadow-selected: 0 0 0 2px var(--color-primary),
                     0 2px 8px rgba(0, 0, 0, 0.06);
}

/* Performant transition using pseudo-element */
.interactive-card {
  position: relative;
  box-shadow: var(--shadow-rest);
  transition: transform 0.2s ease;
}
.interactive-card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  box-shadow: var(--shadow-hover);
  opacity: 0;
  transition: opacity 0.2s ease;
  pointer-events: none;
}
.interactive-card:hover {
  transform: translateY(-2px);
}
.interactive-card:hover::after {
  opacity: 1;
}
.interactive-card:active {
  transform: translateY(0);
  box-shadow: var(--shadow-active);
}
.interactive-card:active::after {
  opacity: 0;
}
```

### Drag Shadow Recipe

```css
.draggable {
  transition: box-shadow 0.15s ease, transform 0.15s ease;
}
.draggable.is-dragging {
  box-shadow: var(--shadow-dragging);
  transform: scale(1.02) rotate(1deg);
  z-index: 999;
  cursor: grabbing;
}
```

### Key Characteristics
- Paired resting/active states for every interaction
- Uses pseudo-element trick for 60fps shadow transitions
- Includes focus ring shadows for keyboard accessibility
- Drag state includes scale and subtle rotation for physicality
- Transition durations tuned: 0.15-0.2s for responsive feel

---

## 12. Tailwind CSS Shadow Presets

**Philosophy:** Direct mapping to Tailwind CSS shadow utilities for teams using Tailwind. Each system above can be mapped into Tailwind config.

### Default Tailwind Shadow Scale

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        'xs': '0 1px 2px rgba(0, 0, 0, 0.05)',
        'sm': '0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06)',
        'md': '0 4px 6px rgba(0, 0, 0, 0.07), 0 2px 4px rgba(0, 0, 0, 0.06)',
        'lg': '0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05)',
        'xl': '0 20px 25px rgba(0, 0, 0, 0.1), 0 8px 10px rgba(0, 0, 0, 0.04)',
        '2xl': '0 25px 50px rgba(0, 0, 0, 0.25)',
        'inner': 'inset 0 2px 4px rgba(0, 0, 0, 0.06)',
        'none': 'none',
      },
    },
  },
}
```

### Custom Layered System for Tailwind

```javascript
// tailwind.config.js — Stripe-style layered shadows
module.exports = {
  theme: {
    boxShadow: {
      'none': 'none',
      'sm': '0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)',
      'DEFAULT': '0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03)',
      'md': '0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03)',
      'lg': '0 10px 20px rgba(0,0,0,0.06), 0 4px 8px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.03)',
      'xl': '0 20px 40px rgba(0,0,0,0.08), 0 8px 16px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.03)',
      '2xl': '0 32px 64px rgba(0,0,0,0.1), 0 16px 32px rgba(0,0,0,0.06), 0 4px 8px rgba(0,0,0,0.03)',
      'inner': 'inset 0 2px 4px rgba(0,0,0,0.06)',
      'glow-sm': '0 0 8px rgba(255,255,255,0.04)',
      'glow-md': '0 0 16px rgba(255,255,255,0.06)',
      'glow-lg': '0 0 32px rgba(255,255,255,0.08)',
    },
  },
}
```

### Dark Mode Tailwind Integration

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      boxShadow: {
        'dark-sm': '0 1px 3px rgba(0,0,0,0.3), 0 0 0 1px rgba(255,255,255,0.04)',
        'dark-md': '0 4px 6px rgba(0,0,0,0.28), 0 0 0 1px rgba(255,255,255,0.04)',
        'dark-lg': '0 10px 20px rgba(0,0,0,0.32), 0 0 0 1px rgba(255,255,255,0.04)',
        'dark-xl': '0 20px 40px rgba(0,0,0,0.36), 0 0 0 1px rgba(255,255,255,0.04)',
        'dark-2xl': '0 32px 64px rgba(0,0,0,0.4), 0 0 0 1px rgba(255,255,255,0.04)',
      },
    },
  },
}
```

### Usage in Markup

```html
<!-- Light mode card with hover shadow -->
<div class="shadow-sm hover:shadow-lg transition-shadow duration-200 rounded-lg p-6">
  Card content
</div>

<!-- Dark mode with explicit dark shadows -->
<div class="shadow-sm dark:shadow-dark-sm hover:shadow-lg dark:hover:shadow-dark-lg transition-shadow">
  Dark-aware card
</div>

<!-- Neumorphic button -->
<button class="shadow-[4px_4px_8px_rgba(0,0,0,0.12),_-4px_-4px_8px_rgba(255,255,255,0.8)]
               active:shadow-[inset_4px_4px_8px_rgba(0,0,0,0.12),_inset_-4px_-4px_8px_rgba(255,255,255,0.8)]">
  Neumorphic
</button>
```

---

## Shadow System Selection Guide

| If your product is... | Use this system | Key reason |
|----------------------|-----------------|------------|
| Developer tool / docs | Minimal | Content-first, shadows distract |
| Premium SaaS / fintech | Layered | Trust through polish |
| Material Design app | Material | Specification compliance |
| Apple ecosystem | Soft | Platform consistency |
| Brutalist / technical | Flat | Intentional flatness |
| Creative / bold brand | Colored | Brand reinforcement |
| Dark-mode-first | Ambient Glow | Physics of dark environments |
| Accessibility-critical | High Contrast | Perceivability |
| Experimental / artistic | Neumorphic | Novel interaction feel |
| Editorial / magazine | Dramatic | Graphic design expression |
| Interactive / draggable | Elevation Transition | Motion quality |
| Tailwind project | Tailwind Presets | Framework integration |
