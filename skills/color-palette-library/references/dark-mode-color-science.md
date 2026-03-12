# Dark Mode Color Science — Complete Guide

Deep dive into the science, principles, and production implementation of dark mode color systems. Covers luminance reduction, surface elevation, desaturation, text adjustments, accent adaptation, shadow treatment, image handling, complete token mapping, OS detection, and 10 production-ready light/dark palette pairs.

---

## Part 1: Why Dark Mode Is Not Color Inversion

The most common dark mode mistake is inverting the color values: swapping white backgrounds to black, black text to white, and calling it done. This fails for fundamental perceptual reasons:

### Problem 1: Pure Black Creates Halation

Pure black (#000000, oklch 0%) backgrounds create "halation" — a halo effect around light text caused by the pupil dilating in response to the dark field. This makes text appear to bleed and glow, reducing readability. Use L:10-14% instead.

### Problem 2: White Text Is Too Heavy

Light text on dark backgrounds appears bolder than the same weight of dark text on light backgrounds. This is the "irradiation illusion" — bright areas appear to expand into dark areas. The fix: reduce font weight by one step in dark mode, or use L:90-93% instead of L:100%.

### Problem 3: Saturated Colors Vibrate

Colors at high chroma (C > 0.20) that look balanced on white backgrounds will appear to vibrate, glow, or pulse on dark backgrounds. The visual system processes saturated colors differently against dark fields. Fix: reduce chroma by 15-25% for dark mode.

### Problem 4: Shadows Are Useless in Dark Mode

In light mode, elevation is communicated through shadows (darker = lower). In dark mode, shadows are invisible against dark backgrounds. Instead, elevation must be communicated through lightness: higher-elevation surfaces are LIGHTER.

### Problem 5: Contrast Polarity Is Not Symmetric

APCA research shows that light text on dark backgrounds requires approximately 15-20% more contrast to achieve the same readability as dark text on light backgrounds. A dark mode palette that simply flips lightness values will feel less readable.

---

## Part 2: Luminance Reduction Principles

### The Background Lightness Spectrum

| L Value | Result | Recommendation |
|---------|--------|----------------|
| 0% | Pure black | Never use — causes halation |
| 5-8% | Very dark | Use sparingly (immersive media apps, cinema mode) |
| 10-14% | Standard dark mode bg | Recommended for most apps |
| 15-18% | Elevated dark surface | Secondary panels, cards |
| 20-24% | Highest elevation | Modals, popovers, dropdown menus |
| 25-30% | Borders, subtle dividers | Subtle structure |

### Surface Elevation System

In dark mode, each elevation step increases lightness by 2-3%:

```css
[data-theme="dark"] {
  /* Base level — page background */
  --surface-0: oklch(12% 0.02 var(--brand-hue));

  /* Level 1 — cards, sidebars */
  --surface-1: oklch(15% 0.02 var(--brand-hue));

  /* Level 2 — hover states, active cards */
  --surface-2: oklch(18% 0.02 var(--brand-hue));

  /* Level 3 — dropdowns, modals */
  --surface-3: oklch(21% 0.02 var(--brand-hue));

  /* Level 4 — popovers, tooltips */
  --surface-4: oklch(24% 0.02 var(--brand-hue));

  /* Level 5 — top-level overlay */
  --surface-5: oklch(27% 0.02 var(--brand-hue));
}
```

### Brand Tinting Dark Surfaces

Pure neutral dark backgrounds (C: 0.00) feel cold and generic. Adding a trace of brand hue warms the palette:

```css
/* Neutral (cold, generic) */
--surface: oklch(12% 0 0);

/* Brand-tinted (warm, branded) */
--surface: oklch(12% 0.02 265);  /* Blue tint — for blue brands */
--surface: oklch(12% 0.02 295);  /* Purple tint — for purple brands */
--surface: oklch(12% 0.02 155);  /* Green tint — for green brands */
--surface: oklch(12% 0.015 75);  /* Warm tint — for warm brands */
```

The chroma should be extremely low (0.01-0.03). Any higher and the tint becomes distracting.

---

## Part 3: Desaturation Rules for Dark Mode

### Why Desaturate?

On white backgrounds (L:97-100%), your eye adapts to high ambient brightness. Saturated colors are perceived normally. On dark backgrounds (L:10-14%), your pupil dilates and color sensitivity increases. Colors at the same chroma will appear MORE vivid — sometimes unpleasantly so.

### Desaturation Formula

```
C_dark = C_light * 0.80  (reduce chroma by 20%)
L_dark = L_light + 10%   (increase lightness to maintain visibility)
```

**Example — Primary Blue:**
```
Light mode:  oklch(55% 0.22 265)  — vivid, balanced on white
Dark mode:   oklch(65% 0.18 265)  — lighter, less vivid on dark bg
```

### Per-Color Desaturation Guidelines

| Color Role | Light Mode (L, C) | Dark Mode (L, C) | Shift |
|-----------|-------------------|-------------------|-------|
| Primary | 55%, 0.22 | 65%, 0.18 | +10% L, -18% C |
| Success | 55%, 0.18 | 65%, 0.14 | +10% L, -22% C |
| Warning | 68%, 0.16 | 72%, 0.13 | +4% L, -19% C |
| Error | 55%, 0.20 | 62%, 0.16 | +7% L, -20% C |
| Info | 55%, 0.16 | 65%, 0.13 | +10% L, -19% C |
| Link | 50%, 0.18 | 62%, 0.15 | +12% L, -17% C |

### When NOT to Desaturate

- **Brand mark/logo:** Keep at original chroma — it is the brand identity
- **Data visualization categorical colors:** Maintain relative chroma for distinguishability
- **Small accent dots/badges:** Small chromatic areas do not cause vibration
- **User-generated content:** Do not modify user photos or media

---

## Part 4: Text Color Adjustments

### Text Weight in Dark Mode

Light text on dark backgrounds appears bolder due to the irradiation illusion. Mitigations:

**Option 1: Reduce font weight**
```css
[data-theme="dark"] {
  body {
    font-weight: 300; /* Instead of 400 */
  }
  h1, h2, h3 {
    font-weight: 500; /* Instead of 600 */
  }
}
```

**Option 2: Use variable font optical adjustments**
```css
[data-theme="dark"] {
  body {
    font-variation-settings: 'wght' 350; /* Finer control than font-weight */
  }
}
```

**Option 3: Use slight transparency**
```css
[data-theme="dark"] {
  --color-text-primary: oklch(93% 0.01 265 / 0.95); /* 95% opacity */
}
```

### Text Lightness Hierarchy in Dark Mode

| Role | Light Mode L | Dark Mode L | Notes |
|------|-------------|-------------|-------|
| Primary text | 15-20% | 90-93% | NOT pure white (100%) |
| Secondary text | 45-50% | 68-72% | Readable but subdued |
| Tertiary text | 55-60% | 52-55% | Minimal emphasis |
| Disabled text | 65-70% | 38-42% | Barely visible |
| Placeholder | 60-65% | 45-50% | Lighter than disabled |
| Link text | Brand color | Brand +10% L | Distinguishable from body |
| Error text | 50-55% | 62-65% | Visible on dark |
| Caption/footnote | 48-52% | 60-65% | Small text needs more contrast |

### Anti-Aliasing Differences

Dark mode text rendering varies by OS:
- **macOS:** Uses subpixel antialiasing which can make light-on-dark text appear heavy. Add `-webkit-font-smoothing: antialiased;`
- **Windows:** ClearType is optimized for dark-on-light. Light-on-dark may appear fuzzy. Reducing weight helps.
- **iOS/Android:** Generally handles both polarities well.

```css
[data-theme="dark"] {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

---

## Part 5: Accent Color Adjustments

### Buttons in Dark Mode

Primary buttons in dark mode face a dilemma: the light-mode primary color at L:55% may not have enough contrast against dark text on the button, or may vibrate against the dark background.

**Strategy: Lighten the button, keep text dark**
```css
/* Light mode */
--button-primary-bg: oklch(55% 0.22 265);  /* Blue */
--button-primary-text: oklch(100% 0 0);     /* White */

/* Dark mode */
--button-primary-bg: oklch(65% 0.18 265);   /* Lighter blue */
--button-primary-text: oklch(12% 0.02 265);  /* Dark text on light button */
```

Or: **Keep the button color, ensure text contrast**
```css
/* Dark mode alternative */
--button-primary-bg: oklch(55% 0.20 265);   /* Same-ish blue */
--button-primary-text: oklch(100% 0 0);      /* White (higher contrast needed) */
```

### Subtle/Ghost Buttons

```css
/* Light mode */
--button-subtle-bg: oklch(95% 0.03 265);     /* Light blue tint */
--button-subtle-text: oklch(45% 0.20 265);   /* Blue text */
--button-subtle-border: oklch(85% 0.06 265); /* Light blue border */

/* Dark mode */
--button-subtle-bg: oklch(18% 0.04 265);      /* Dark blue tint */
--button-subtle-text: oklch(68% 0.16 265);    /* Lighter blue text */
--button-subtle-border: oklch(28% 0.06 265);  /* Subtle blue border */
```

### Status Colors in Dark Mode

Status colors (success, warning, error, info) need special treatment in dark mode:

```css
/* Light mode subtle status backgrounds */
--success-subtle-bg: oklch(94% 0.04 155);   /* Light green tint */
--warning-subtle-bg: oklch(94% 0.04 85);    /* Light yellow tint */
--error-subtle-bg: oklch(94% 0.04 25);      /* Light red tint */
--info-subtle-bg: oklch(94% 0.04 255);      /* Light blue tint */

/* Dark mode subtle status backgrounds */
--success-subtle-bg: oklch(16% 0.04 155);   /* Dark green tint */
--warning-subtle-bg: oklch(16% 0.04 85);    /* Dark yellow tint */
--error-subtle-bg: oklch(16% 0.04 25);      /* Dark red tint */
--info-subtle-bg: oklch(16% 0.04 255);      /* Dark blue tint */

/* Dark mode status text colors (lightened) */
--success-text: oklch(65% 0.14 155);
--warning-text: oklch(72% 0.14 85);
--error-text: oklch(65% 0.16 25);
--info-text: oklch(65% 0.14 255);
```

---

## Part 6: Shadow and Elevation in Dark Mode

### Light Mode Elevation Model

```css
/* Light mode: shadows communicate elevation */
--shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.05);
--shadow-md: 0 4px 6px oklch(0% 0 0 / 0.07), 0 2px 4px oklch(0% 0 0 / 0.06);
--shadow-lg: 0 10px 15px oklch(0% 0 0 / 0.10), 0 4px 6px oklch(0% 0 0 / 0.05);
--shadow-xl: 0 20px 25px oklch(0% 0 0 / 0.10), 0 8px 10px oklch(0% 0 0 / 0.04);
```

### Dark Mode Elevation Model

```css
/* Dark mode: surface lightness communicates elevation */
/* Shadows are barely visible — reduce opacity dramatically */
--shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.20);
--shadow-md: 0 4px 6px oklch(0% 0 0 / 0.30);
--shadow-lg: 0 10px 15px oklch(0% 0 0 / 0.40);
--shadow-xl: 0 20px 25px oklch(0% 0 0 / 0.50);

/* Primary elevation signal: surface lightness */
--surface-base: oklch(12% 0.02 265);       /* Lowest */
--surface-card: oklch(15% 0.02 265);       /* Cards (+3%) */
--surface-overlay: oklch(18% 0.02 265);    /* Overlays (+6%) */
--surface-modal: oklch(21% 0.02 265);      /* Modals (+9%) */
--surface-popover: oklch(24% 0.02 265);    /* Popovers (+12%) */
```

### Border Treatment in Dark Mode

Borders are more important in dark mode because shadows are less visible:

```css
/* Light mode: subtle borders, shadows do heavy lifting */
--border-subtle: oklch(90% 0.003 265);    /* Very light */
--border-default: oklch(85% 0.004 265);   /* Light */
--border-strong: oklch(75% 0.005 265);    /* Medium */

/* Dark mode: borders must be more visible */
--border-subtle: oklch(20% 0.02 265);     /* Just above surface */
--border-default: oklch(25% 0.02 265);    /* Visible */
--border-strong: oklch(32% 0.02 265);     /* Strong divider */
```

---

## Part 7: Image Treatment in Dark Mode

### Image Dimming

Full-brightness images on dark backgrounds create jarring contrast. Dim images slightly:

```css
[data-theme="dark"] {
  img:not([data-no-dim]) {
    filter: brightness(0.85);
  }

  /* Restore on hover for full view */
  img:not([data-no-dim]):hover {
    filter: brightness(1.0);
    transition: filter 0.2s ease;
  }

  /* Exclude logos and icons from dimming */
  img[data-no-dim],
  .logo img,
  .icon img {
    filter: none;
  }
}
```

### Background Image Overlay

For hero sections with background images:

```css
[data-theme="dark"] .hero {
  /* Add a dark overlay to reduce brightness */
  position: relative;
}

[data-theme="dark"] .hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: oklch(0% 0 0 / 0.40); /* 40% dark overlay */
  pointer-events: none;
}
```

### SVG and Icon Treatment

```css
[data-theme="dark"] {
  /* Invert dark icons for dark mode */
  .icon--dark {
    filter: invert(1) brightness(0.9);
  }

  /* Or use CSS custom properties for SVG fill */
  --icon-color: oklch(88% 0.01 265); /* Light gray icons */
  --icon-color-muted: oklch(55% 0.01 265); /* Muted icons */
}
```

---

## Part 8: OS Dark Mode Detection and Toggle

### CSS Detection

```css
/* Automatic detection */
@media (prefers-color-scheme: dark) {
  :root {
    /* Dark mode tokens */
  }
}

/* Manual override via data attribute */
[data-theme="light"] { /* Light tokens */ }
[data-theme="dark"] { /* Dark tokens */ }
```

### JavaScript Detection and Toggle

```javascript
// Detect system preference
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

// Listen for system changes
window.matchMedia('(prefers-color-scheme: dark)')
  .addEventListener('change', (e) => {
    if (!getUserPreference()) {
      // Only auto-switch if user hasn't set manual preference
      setTheme(e.matches ? 'dark' : 'light');
    }
  });

// Theme toggle with persistence
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme-preference', theme);
}

function getTheme() {
  // Priority: 1) User preference, 2) System preference, 3) Default
  return localStorage.getItem('theme-preference')
    ?? (prefersDark ? 'dark' : 'light');
}

// Initialize on page load
document.documentElement.setAttribute('data-theme', getTheme());
```

### Three-State Toggle (System / Light / Dark)

Best practice is offering three choices: follow system, always light, always dark.

```javascript
function setThemePreference(pref) {
  if (pref === 'system') {
    localStorage.removeItem('theme-preference');
    const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.setAttribute('data-theme', systemDark ? 'dark' : 'light');
  } else {
    localStorage.setItem('theme-preference', pref);
    document.documentElement.setAttribute('data-theme', pref);
  }
}
```

### Preventing Flash of Wrong Theme (FOWT)

Place this script in the `<head>` before any CSS loads:

```html
<script>
  (function() {
    var t = localStorage.getItem('theme-preference');
    if (!t) t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', t);
  })();
</script>
```

---

## Part 9: Complete Light/Dark Palette Pairs (10 Production-Ready)

### Pair 1: Blue Professional

```css
/* Light */
:root[data-theme="light"] {
  --bg: oklch(99% 0.003 255);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(98% 0.003 255); --border: oklch(88% 0.004 255);
  --text-primary: oklch(16% 0.02 255);   --text-secondary: oklch(48% 0.006 255);
  --primary: oklch(48% 0.20 255);        --primary-hover: oklch(40% 0.18 255);
  --primary-subtle: oklch(94% 0.04 255); --success: oklch(48% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
/* Dark */
:root[data-theme="dark"] {
  --bg: oklch(12% 0.02 255);            --surface: oklch(15% 0.02 255);
  --surface-raised: oklch(18% 0.02 255); --border: oklch(24% 0.02 255);
  --text-primary: oklch(92% 0.01 255);   --text-secondary: oklch(68% 0.02 255);
  --primary: oklch(62% 0.17 255);        --primary-hover: oklch(68% 0.15 255);
  --primary-subtle: oklch(18% 0.06 255); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 2: Purple Creative

```css
:root[data-theme="light"] {
  --bg: oklch(99% 0.002 295);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(97% 0.003 295); --border: oklch(88% 0.004 295);
  --text-primary: oklch(15% 0.02 295);   --text-secondary: oklch(50% 0.006 295);
  --primary: oklch(48% 0.22 295);        --primary-hover: oklch(40% 0.20 295);
  --primary-subtle: oklch(94% 0.04 295); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(11% 0.03 295);            --surface: oklch(14% 0.03 295);
  --surface-raised: oklch(17% 0.03 295); --border: oklch(23% 0.03 295);
  --text-primary: oklch(92% 0.01 295);   --text-secondary: oklch(68% 0.02 295);
  --primary: oklch(62% 0.18 295);        --primary-hover: oklch(68% 0.16 295);
  --primary-subtle: oklch(18% 0.06 295); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 3: Green Growth

```css
:root[data-theme="light"] {
  --bg: oklch(98% 0.005 155);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(96% 0.005 155); --border: oklch(88% 0.005 155);
  --text-primary: oklch(16% 0.02 155);   --text-secondary: oklch(48% 0.006 155);
  --primary: oklch(48% 0.18 155);        --primary-hover: oklch(40% 0.16 155);
  --primary-subtle: oklch(94% 0.04 155); --success: oklch(48% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(11% 0.02 155);            --surface: oklch(14% 0.02 155);
  --surface-raised: oklch(17% 0.02 155); --border: oklch(23% 0.02 155);
  --text-primary: oklch(92% 0.01 155);   --text-secondary: oklch(68% 0.02 155);
  --primary: oklch(62% 0.15 155);        --primary-hover: oklch(68% 0.13 155);
  --primary-subtle: oklch(17% 0.05 155); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 4: Warm Neutral

```css
:root[data-theme="light"] {
  --bg: oklch(97% 0.006 75);            --surface: oklch(100% 0.002 75);
  --surface-raised: oklch(95% 0.006 75); --border: oklch(86% 0.006 75);
  --text-primary: oklch(18% 0.008 75);   --text-secondary: oklch(50% 0.006 75);
  --primary: oklch(48% 0.18 265);        --primary-hover: oklch(40% 0.16 265);
  --primary-subtle: oklch(92% 0.04 265); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(12% 0.01 75);             --surface: oklch(15% 0.01 75);
  --surface-raised: oklch(18% 0.01 75); --border: oklch(24% 0.01 75);
  --text-primary: oklch(92% 0.005 75);   --text-secondary: oklch(68% 0.005 75);
  --primary: oklch(62% 0.15 265);        --primary-hover: oklch(68% 0.13 265);
  --primary-subtle: oklch(18% 0.05 265); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 5: Cool Minimal (Vercel-style)

```css
:root[data-theme="light"] {
  --bg: oklch(100% 0 0);                --surface: oklch(100% 0 0);
  --surface-raised: oklch(97% 0.002 265); --border: oklch(88% 0.003 265);
  --text-primary: oklch(0% 0 0);         --text-secondary: oklch(50% 0.004 265);
  --primary: oklch(0% 0 0);              --primary-hover: oklch(20% 0.003 265);
  --primary-subtle: oklch(96% 0.002 265); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(0% 0 0);                  --surface: oklch(8% 0.003 265);
  --surface-raised: oklch(14% 0.003 265); --border: oklch(20% 0.003 265);
  --text-primary: oklch(98% 0.002 265);  --text-secondary: oklch(58% 0.004 265);
  --primary: oklch(100% 0 0);            --primary-hover: oklch(85% 0.003 265);
  --primary-subtle: oklch(12% 0.002 265); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 6: Teal Healthcare

```css
:root[data-theme="light"] {
  --bg: oklch(98% 0.004 195);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(96% 0.004 195); --border: oklch(88% 0.005 195);
  --text-primary: oklch(16% 0.01 195);   --text-secondary: oklch(48% 0.006 195);
  --primary: oklch(48% 0.14 195);        --primary-hover: oklch(40% 0.12 195);
  --primary-subtle: oklch(94% 0.04 195); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(11% 0.02 195);            --surface: oklch(14% 0.02 195);
  --surface-raised: oklch(17% 0.02 195); --border: oklch(23% 0.02 195);
  --text-primary: oklch(92% 0.01 195);   --text-secondary: oklch(68% 0.02 195);
  --primary: oklch(60% 0.12 195);        --primary-hover: oklch(66% 0.10 195);
  --primary-subtle: oklch(17% 0.05 195); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 7: Indigo SaaS

```css
:root[data-theme="light"] {
  --bg: oklch(99% 0.002 270);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(97% 0.003 270); --border: oklch(88% 0.004 270);
  --text-primary: oklch(15% 0.02 270);   --text-secondary: oklch(48% 0.006 270);
  --primary: oklch(45% 0.22 270);        --primary-hover: oklch(38% 0.20 270);
  --primary-subtle: oklch(94% 0.04 270); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(11% 0.02 270);            --surface: oklch(14% 0.02 270);
  --surface-raised: oklch(17% 0.02 270); --border: oklch(23% 0.02 270);
  --text-primary: oklch(92% 0.01 270);   --text-secondary: oklch(68% 0.02 270);
  --primary: oklch(62% 0.18 270);        --primary-hover: oklch(68% 0.16 270);
  --primary-subtle: oklch(18% 0.06 270); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 8: Rose Consumer

```css
:root[data-theme="light"] {
  --bg: oklch(99% 0.003 355);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(97% 0.003 355); --border: oklch(88% 0.005 355);
  --text-primary: oklch(16% 0.01 355);   --text-secondary: oklch(50% 0.005 355);
  --primary: oklch(52% 0.20 355);        --primary-hover: oklch(44% 0.18 355);
  --primary-subtle: oklch(94% 0.04 355); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(11% 0.02 355);            --surface: oklch(14% 0.02 355);
  --surface-raised: oklch(17% 0.02 355); --border: oklch(23% 0.02 355);
  --text-primary: oklch(92% 0.01 355);   --text-secondary: oklch(68% 0.02 355);
  --primary: oklch(62% 0.16 355);        --primary-hover: oklch(68% 0.14 355);
  --primary-subtle: oklch(18% 0.06 355); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 9: Amber Warm SaaS

```css
:root[data-theme="light"] {
  --bg: oklch(98% 0.006 80);            --surface: oklch(100% 0.002 80);
  --surface-raised: oklch(96% 0.006 80); --border: oklch(86% 0.006 80);
  --text-primary: oklch(18% 0.01 80);    --text-secondary: oklch(48% 0.006 80);
  --primary: oklch(58% 0.18 65);         --primary-hover: oklch(50% 0.16 65);
  --primary-subtle: oklch(92% 0.06 65);  --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(12% 0.01 80);             --surface: oklch(15% 0.01 80);
  --surface-raised: oklch(18% 0.01 80); --border: oklch(24% 0.01 80);
  --text-primary: oklch(92% 0.005 80);   --text-secondary: oklch(68% 0.005 80);
  --primary: oklch(68% 0.15 65);         --primary-hover: oklch(72% 0.13 65);
  --primary-subtle: oklch(18% 0.05 65);  --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

### Pair 10: Slate Developer

```css
:root[data-theme="light"] {
  --bg: oklch(98% 0.003 240);           --surface: oklch(100% 0 0);
  --surface-raised: oklch(96% 0.003 240); --border: oklch(86% 0.004 240);
  --text-primary: oklch(14% 0.01 240);   --text-secondary: oklch(48% 0.005 240);
  --primary: oklch(50% 0.16 240);        --primary-hover: oklch(42% 0.14 240);
  --primary-subtle: oklch(94% 0.03 240); --success: oklch(50% 0.16 155);
  --warning: oklch(65% 0.14 70);         --error: oklch(50% 0.20 25);
}
:root[data-theme="dark"] {
  --bg: oklch(10% 0.02 240);            --surface: oklch(13% 0.02 240);
  --surface-raised: oklch(16% 0.02 240); --border: oklch(22% 0.02 240);
  --text-primary: oklch(90% 0.005 240);  --text-secondary: oklch(62% 0.01 240);
  --primary: oklch(62% 0.14 240);        --primary-hover: oklch(68% 0.12 240);
  --primary-subtle: oklch(16% 0.05 240); --success: oklch(62% 0.14 155);
  --warning: oklch(72% 0.12 70);         --error: oklch(62% 0.16 25);
}
```

---

## Part 10: Dark Mode Design Checklist

### Before Launch

- [ ] Background is not pure black (L >= 10%)
- [ ] Primary text is not pure white (L <= 95%)
- [ ] Surface elevation increases lightness (2-3% per step)
- [ ] Accent colors desaturated 15-25% from light mode values
- [ ] Font weight reduced or anti-aliasing adjusted for dark mode
- [ ] All body text pairings achieve Lc >= 75 (APCA)
- [ ] Status colors (success/warning/error) are distinguishable on dark surfaces
- [ ] Images have brightness reduction (85-90%)
- [ ] Borders are visible (not lost against dark surfaces)
- [ ] Focus indicators are visible on dark backgrounds
- [ ] Shadows are adjusted (increased opacity or replaced with surface lightness)
- [ ] Brand tint applied to dark surfaces (C: 0.01-0.03)
- [ ] Three-state toggle available (System / Light / Dark)
- [ ] No flash of wrong theme on page load
- [ ] User preference persists across sessions
- [ ] System preference changes are respected when user has no manual override
