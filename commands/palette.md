---
name: palette
description: "Generate a deep color system — oklch palettes, APCA contrast scores, dark mode, data-viz colors, gradients, and CSS custom properties."
argument-hint: "[brand, mood, or existing colors]"
---

# Palette — Deep Color System Generator

## Before running

This command needs a brand, a mood, or existing colors to work from.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a production-grade color system from a mood, sector, brand color, or open exploration. Every color is in OKLCH for perceptual uniformity, every text/background pair has APCA contrast scores, and every value is copy-paste ready.

This command goes deeper than `/style` on color alone. Use it when you need a standalone color system, want to refine an existing palette, or need specialized palettes (data visualization, gradients, brand extensions).

---

## Input Modes

| Mode | Trigger | What Happens |
|------|---------|-------------|
| **Brand color** | Provide a hex, oklch, or hsl value | Build entire system around that anchor |
| **Mood** | Provide a mood phrase ("warm minimal", "dark cyberpunk", "clean clinical") | Derive hues from mood semantics |
| **Sector** | Provide an industry ("fintech", "wellness", "SaaS") | Use sector color conventions |
| **Explore** | Say "explore" or provide no color input | Generate 3 distinct palette options to choose from |
| **Refine** | Provide an existing palette or `.sumi/style.json` reference | Improve, extend, or audit what exists |

If `.sumi/style.json` exists with color data from `/style`, load it as the starting point and extend/refine rather than regenerate from scratch.

---

## Generation Protocol

### Step 1 — Anchor Color Selection

Determine the **primary brand hue** based on input mode:

**If brand color provided:**
- Convert to OKLCH (all math happens in OKLCH space)
- Identify hue angle, optimal chroma range, and lightness anchor
- Validate that the hue has sufficient chroma range for a 10-step scale

**If mood provided:**
- Map mood keywords to hue ranges:
  - Warm: 20-60 (orange-yellow)
  - Cool: 220-270 (blue-indigo)
  - Fresh: 130-170 (green-teal)
  - Bold: 0-30 or 330-360 (red-magenta)
  - Calm: 180-220 (cyan-blue)
  - Luxurious: 280-320 (purple-magenta)
  - Natural: 80-130 (yellow-green)
  - Neutral: achromatic or very low chroma
- Select specific hue within range based on modifier words

**If sector provided:**
- Use sector color conventions:
  - Fintech: Blue (trust, stability) — hue 240-260
  - Healthcare: Blue-teal (clinical trust) — hue 200-230
  - Wellness: Green-teal (growth, health) — hue 150-180
  - E-commerce: Orange-red (energy, urgency) — hue 20-40
  - Education: Blue-purple (knowledge, calm) — hue 250-280
  - Legal: Navy-charcoal (authority, gravity) — hue 240-250, low chroma
  - Food: Warm red-orange (appetite) — hue 15-35
  - Travel: Sky blue-teal (aspiration, freedom) — hue 200-220
  - Creator tools: Purple-violet (creativity) — hue 280-310
  - Developer tools: Blue-cyan (technical clarity) — hue 210-240

**If explore mode:**
- Generate 3 palette options with different hue strategies:
  1. A safe, conventional option for the context
  2. A distinctive, memorable option
  3. A bold, unexpected option
- Present all 3 with a recommendation

### Step 2 — Neutral Scale (10 Steps)

Generate neutrals with slight hue tinting from the brand color. Pure gray is lifeless — good neutrals carry 0.005-0.015 chroma from the brand hue.

| Step | Token | OKLCH | Hex | Usage |
|------|-------|-------|-----|-------|
| 50 | neutral-50 | oklch(0.985 [c] [h]) | #... | Page background (light) |
| 100 | neutral-100 | oklch(0.965 [c] [h]) | #... | Raised surface, card bg |
| 150 | neutral-150 | oklch(0.945 [c] [h]) | #... | Subtle hover, table stripe |
| 200 | neutral-200 | oklch(0.925 [c] [h]) | #... | Border, divider |
| 300 | neutral-300 | oklch(0.87 [c] [h]) | #... | Disabled, placeholder |
| 400 | neutral-400 | oklch(0.71 [c] [h]) | #... | Helper text, icons |
| 500 | neutral-500 | oklch(0.55 [c] [h]) | #... | Secondary text |
| 600 | neutral-600 | oklch(0.445 [c] [h]) | #... | Body text |
| 700 | neutral-700 | oklch(0.37 [c] [h]) | #... | Strong body text |
| 800 | neutral-800 | oklch(0.27 [c] [h]) | #... | Heading text |
| 900 | neutral-900 | oklch(0.205 [c] [h]) | #... | Maximum contrast |
| 950 | neutral-950 | oklch(0.145 [c] [h]) | #... | Dark mode background |

The `[c]` chroma value is typically 0.005-0.015 (very subtle). The `[h]` hue matches the brand primary.

### Step 3 — Brand/Primary Scale (10 Steps)

Build the primary color scale around the anchor hue.

**Scale construction rules:**
- Lightness: L=0.97 (50) down to L=0.25 (950) in perceptually even steps
- Chroma: Peak at 500-600, taper to 0.02-0.04 at extremes (50/950)
- Hue: Slight hue rotation allowed across the scale (natural in OKLCH — e.g., blue shifts slightly toward cyan at high lightness)
- 500 is the **hero value** — used for primary buttons, links, focus rings

| Step | Token | OKLCH | Hex | Usage |
|------|-------|-------|-----|-------|
| 50 | brand-50 | oklch(0.97 0.02 [h]) | #... | Brand tint background |
| 100 | brand-100 | oklch(0.93 0.04 [h]) | #... | Light brand surface |
| 200 | brand-200 | oklch(0.87 0.08 [h]) | #... | Brand highlight |
| 300 | brand-300 | oklch(0.77 0.12 [h]) | #... | Brand border, tag bg |
| 400 | brand-400 | oklch(0.67 0.16 [h]) | #... | Hover state, secondary |
| 500 | brand-500 | oklch(0.55 0.18 [h]) | #... | Primary brand (hero) |
| 600 | brand-600 | oklch(0.48 0.16 [h]) | #... | Active/pressed state |
| 700 | brand-700 | oklch(0.40 0.14 [h]) | #... | Brand text on light bg |
| 800 | brand-800 | oklch(0.33 0.11 [h]) | #... | Dark brand accent |
| 900 | brand-900 | oklch(0.27 0.08 [h]) | #... | Brand on dark surface |
| 950 | brand-950 | oklch(0.20 0.05 [h]) | #... | Deepest brand |

Chroma values are **maximums** — actual values depend on the hue's gamut at each lightness level. Clamp to sRGB gamut.

### Step 4 — Secondary and Accent Scales

Generate a **secondary** color using one of these strategies (choose based on sector/mood):

| Strategy | Hue Relationship | Best For |
|----------|-----------------|----------|
| Analogous | +/- 30 degrees | Professional, harmonious (SaaS, fintech) |
| Complementary | +180 degrees | High energy, strong contrast (e-commerce, gaming) |
| Split-complementary | +150 / +210 degrees | Balanced variety (marketplace, social) |
| Triadic | +120 / +240 degrees | Vibrant, diverse (creative tools, media) |

Generate a full 10-step scale for the secondary color using the same OKLCH construction rules.

Optionally generate an **accent** color (a third hue) if the design calls for it — typically for CTAs that need to stand apart from both brand and secondary.

### Step 5 — Semantic Color System

| Token | Light Mode OKLCH | Light Hex | Dark Mode OKLCH | Dark Hex | Usage |
|-------|-----------------|-----------|----------------|----------|-------|
| success-50 | oklch(0.96 0.03 145) | #... | oklch(0.20 0.04 145) | #... | Success bg |
| success-100 | oklch(0.91 0.06 145) | #... | oklch(0.25 0.06 145) | #... | Success light |
| success-500 | oklch(0.55 0.17 145) | #... | oklch(0.65 0.17 145) | #... | Success primary |
| success-700 | oklch(0.38 0.13 145) | #... | oklch(0.80 0.10 145) | #... | Success text |
| warning-50 | oklch(0.96 0.04 85) | #... | oklch(0.20 0.04 85) | #... | Warning bg |
| warning-100 | oklch(0.91 0.08 85) | #... | oklch(0.25 0.06 85) | #... | Warning light |
| warning-500 | oklch(0.72 0.17 85) | #... | oklch(0.75 0.15 85) | #... | Warning primary |
| warning-700 | oklch(0.45 0.12 85) | #... | oklch(0.85 0.10 85) | #... | Warning text |
| error-50 | oklch(0.96 0.03 27) | #... | oklch(0.20 0.04 27) | #... | Error bg |
| error-100 | oklch(0.91 0.06 27) | #... | oklch(0.25 0.06 27) | #... | Error light |
| error-500 | oklch(0.55 0.22 27) | #... | oklch(0.65 0.20 27) | #... | Error primary |
| error-700 | oklch(0.38 0.16 27) | #... | oklch(0.80 0.12 27) | #... | Error text |
| info-50 | oklch(0.96 0.02 250) | #... | oklch(0.20 0.03 250) | #... | Info bg |
| info-100 | oklch(0.91 0.05 250) | #... | oklch(0.25 0.05 250) | #... | Info light |
| info-500 | oklch(0.55 0.15 250) | #... | oklch(0.65 0.15 250) | #... | Info primary |
| info-700 | oklch(0.38 0.12 250) | #... | oklch(0.80 0.08 250) | #... | Info text |

### Step 6 — APCA Contrast Verification

For **every functional text/background pairing**, compute the APCA Lc (Lightness Contrast) value. APCA is the successor to WCAG 2.x contrast ratios and provides more accurate readability predictions.

**APCA Minimum Thresholds:**

| Content Type | Minimum Lc | Notes |
|-------------|-----------|-------|
| Body text (16px+) | Lc 60 | Standard readability |
| Large text (24px+) | Lc 45 | Headings, display |
| Sub-text / captions (< 16px) | Lc 75 | Small text needs more contrast |
| Non-text UI (icons, borders) | Lc 30 | Functional elements |
| Disabled / placeholder | Lc 30 | Intentionally low, but still visible |
| Focus indicator | Lc 40 | Against adjacent colors |

**Verification Table:**

| Pair Name | Foreground | Background | APCA Lc | WCAG 2.2 | Body? | Large? | Status |
|-----------|-----------|-----------|---------|----------|-------|--------|--------|
| Primary text on page | neutral-900 | neutral-50 | Lc 106 | 19.2:1 | Pass | Pass | OK |
| Secondary text on page | neutral-600 | neutral-50 | Lc 62 | 7.3:1 | Pass | Pass | OK |
| Brand text on page | brand-700 | neutral-50 | Lc ... | ...:1 | ... | ... | ... |
| Text on brand button | neutral-50 | brand-500 | Lc ... | ...:1 | ... | ... | ... |
| Success text on success bg | success-700 | success-50 | Lc ... | ...:1 | ... | ... | ... |
| Error text on error bg | error-700 | error-50 | Lc ... | ...:1 | ... | ... | ... |
| ... (all functional pairs) | ... | ... | ... | ... | ... | ... | ... |

Flag any failing pairs with the fix applied (e.g., "Shifted foreground from 600 to 700 to reach Lc 60").

### Step 7 — Dark Mode Transformation

Dark mode is NOT lightness inversion. Apply these transformation rules:

**Background strategy:**
- Page background: neutral-950 or neutral-900 (choose based on mood — 950 is darker, moodier)
- Surface (cards, modals): neutral-900 or neutral-800 (1-2 steps lighter than page)
- Elevated surface: neutral-800 or neutral-700 (2-3 steps lighter than page)
- Use incremental lightness for z-layer separation, not shadows

**Text strategy:**
- Primary text: L=0.93 (not pure white — reduces eye strain)
- Secondary text: L=0.70-0.75
- Tertiary/disabled: L=0.50-0.55
- Text should carry the same brand hue tint as neutrals

**Brand color strategy:**
- Shift lightness UP by 0.10-0.15
- Reduce chroma by 10-20% (saturated colors glow on dark backgrounds)
- The 400 step typically becomes the new hero in dark mode (not 500)

**Semantic color strategy:**
- Success/warning/error/info: Increase lightness by 0.10-0.15
- Reduce chroma slightly to prevent glow
- Semantic backgrounds: Use very dark tinted versions (L=0.18-0.22)

**Border strategy:**
- Use oklch(1 0 0 / 0.10) to oklch(1 0 0 / 0.15) (white at 10-15% opacity)
- This adapts naturally to any background shade
- Avoid hardcoded gray borders — they look wrong at different elevations

**Shadow strategy:**
- Shadows are effectively invisible on dark backgrounds
- Replace with 1px borders (oklch(1 0 0 / 0.06-0.10))
- Or use subtle background-color differences for elevation

Output the complete dark mode palette in the same table format as light mode.

### Step 8 — Data Visualization Palette

Generate purpose-built palettes for charts and graphs. These are separate from the UI palette.

**8a. Categorical Palette (6-8 colors)**

For bar charts, pie charts, legends where each color represents a different category.

| # | Name | OKLCH | Hex | Colorblind Safe |
|---|------|-------|-----|----------------|
| 1 | viz-cat-1 | oklch(...) | #... | Yes — distinct hue |
| 2 | viz-cat-2 | oklch(...) | #... | Yes — distinct hue |
| 3 | viz-cat-3 | oklch(...) | #... | Yes — distinct hue |
| 4 | viz-cat-4 | oklch(...) | #... | Yes — distinct hue |
| 5 | viz-cat-5 | oklch(...) | #... | Yes — distinct hue |
| 6 | viz-cat-6 | oklch(...) | #... | Yes — distinct hue |

Rules:
- Perceptually equidistant hues (distribute evenly around the hue wheel)
- Matched lightness (L=0.55-0.65) so no color dominates
- Avoid red-green adjacent pairs (deuteranopia)
- Test with Sim Daltonism or similar for protanopia, deuteranopia, tritanopia
- Each color must be distinguishable in all three common colorblindness types

**8b. Sequential Palette (single hue, 5-7 steps)**

For heatmaps, choropleth maps, single-variable intensity.

| Step | OKLCH | Hex | Value Mapping |
|------|-------|-----|--------------|
| 1 (low) | oklch(0.95 0.02 [h]) | #... | Minimum value |
| 2 | oklch(0.85 0.06 [h]) | #... | Low |
| 3 | oklch(0.72 0.10 [h]) | #... | Below average |
| 4 | oklch(0.60 0.14 [h]) | #... | Average |
| 5 | oklch(0.48 0.16 [h]) | #... | Above average |
| 6 | oklch(0.36 0.14 [h]) | #... | High |
| 7 (high) | oklch(0.25 0.10 [h]) | #... | Maximum value |

Hue should match or complement the brand primary.

**8c. Diverging Palette (two hues, 7-9 steps)**

For data with a meaningful midpoint (profit/loss, above/below average, sentiment).

| Step | OKLCH | Hex | Value Mapping |
|------|-------|-----|--------------|
| 1 (neg extreme) | oklch(0.35 0.15 [h1]) | #... | Strong negative |
| 2 | oklch(0.45 0.12 [h1]) | #... | Moderate negative |
| 3 | oklch(0.60 0.08 [h1]) | #... | Slight negative |
| 4 (neutral) | oklch(0.92 0.01 0) | #... | Midpoint / zero |
| 5 | oklch(0.60 0.08 [h2]) | #... | Slight positive |
| 6 | oklch(0.45 0.12 [h2]) | #... | Moderate positive |
| 7 (pos extreme) | oklch(0.35 0.15 [h2]) | #... | Strong positive |

Common diverging hue pairs: red-blue, orange-teal, purple-green. Avoid red-green.

### Step 9 — Gradient Recipes

Generate 4-6 gradient recipes using the palette colors. Each is CSS-ready.

| Name | CSS | Usage |
|------|-----|-------|
| Brand subtle | `linear-gradient(135deg, oklch(0.97 0.02 [h]) 0%, oklch(0.95 0.03 [h2]) 100%)` | Card backgrounds, hero sections |
| Brand bold | `linear-gradient(135deg, oklch(0.55 0.18 [h]) 0%, oklch(0.45 0.16 [h+30]) 100%)` | CTA buttons, brand banners |
| Warm glow | `radial-gradient(ellipse at top, oklch(0.96 0.04 40) 0%, oklch(0.99 0.01 0) 70%)` | Page background accent |
| Dark surface | `linear-gradient(180deg, oklch(0.18 0.01 [h]) 0%, oklch(0.14 0.01 [h]) 100%)` | Dark mode card variation |
| Mesh (multi-stop) | `background: oklch(0.97 0.01 [h]); background-image: radial-gradient(at 40% 20%, oklch(0.95 0.04 [h1]) 0px, transparent 50%), radial-gradient(at 80% 0%, oklch(0.94 0.03 [h2]) 0px, transparent 50%)` | Hero backgrounds, landing pages |

### Step 10 — CSS Custom Properties Output

Output a complete, copy-paste CSS block.

```css
/* ============================================================
   Color System — [Context]
   Generated by Sumi /palette
   OKLCH-first, sRGB hex fallbacks in comments
   ============================================================ */

:root {
  /* --- Neutral --- */
  --color-neutral-50: oklch(0.985 0.005 [h]);   /* #... */
  --color-neutral-100: oklch(0.965 0.005 [h]);  /* #... */
  --color-neutral-150: oklch(0.945 0.005 [h]);  /* #... */
  --color-neutral-200: oklch(0.925 0.005 [h]);  /* #... */
  --color-neutral-300: oklch(0.87 0.005 [h]);   /* #... */
  --color-neutral-400: oklch(0.71 0.005 [h]);   /* #... */
  --color-neutral-500: oklch(0.55 0.005 [h]);   /* #... */
  --color-neutral-600: oklch(0.445 0.005 [h]);  /* #... */
  --color-neutral-700: oklch(0.37 0.005 [h]);   /* #... */
  --color-neutral-800: oklch(0.27 0.005 [h]);   /* #... */
  --color-neutral-900: oklch(0.205 0.005 [h]);  /* #... */
  --color-neutral-950: oklch(0.145 0.005 [h]);  /* #... */

  /* --- Brand Primary --- */
  --color-brand-50: oklch(...);   /* #... */
  --color-brand-100: oklch(...);  /* #... */
  --color-brand-200: oklch(...);  /* #... */
  --color-brand-300: oklch(...);  /* #... */
  --color-brand-400: oklch(...);  /* #... */
  --color-brand-500: oklch(...);  /* #... hero */
  --color-brand-600: oklch(...);  /* #... */
  --color-brand-700: oklch(...);  /* #... */
  --color-brand-800: oklch(...);  /* #... */
  --color-brand-900: oklch(...);  /* #... */
  --color-brand-950: oklch(...);  /* #... */

  /* --- Secondary --- */
  --color-secondary-50: oklch(...);  /* #... */
  /* ... full scale ... */
  --color-secondary-950: oklch(...); /* #... */

  /* --- Semantic --- */
  --color-success-50: oklch(...);
  --color-success-100: oklch(...);
  --color-success-500: oklch(...);
  --color-success-700: oklch(...);
  --color-warning-50: oklch(...);
  --color-warning-100: oklch(...);
  --color-warning-500: oklch(...);
  --color-warning-700: oklch(...);
  --color-error-50: oklch(...);
  --color-error-100: oklch(...);
  --color-error-500: oklch(...);
  --color-error-700: oklch(...);
  --color-info-50: oklch(...);
  --color-info-100: oklch(...);
  --color-info-500: oklch(...);
  --color-info-700: oklch(...);

  /* --- Semantic Aliases (Light) --- */
  --color-bg: var(--color-neutral-50);
  --color-bg-subtle: var(--color-neutral-100);
  --color-bg-muted: var(--color-neutral-150);
  --color-bg-emphasis: var(--color-brand-500);
  --color-fg: var(--color-neutral-900);
  --color-fg-muted: var(--color-neutral-600);
  --color-fg-subtle: var(--color-neutral-500);
  --color-fg-on-emphasis: var(--color-neutral-50);
  --color-border: var(--color-neutral-200);
  --color-border-strong: var(--color-neutral-300);
  --color-border-brand: var(--color-brand-500);

  /* --- Data Visualization --- */
  --color-viz-cat-1: oklch(...);
  --color-viz-cat-2: oklch(...);
  --color-viz-cat-3: oklch(...);
  --color-viz-cat-4: oklch(...);
  --color-viz-cat-5: oklch(...);
  --color-viz-cat-6: oklch(...);

  /* --- Gradients --- */
  --gradient-brand-subtle: linear-gradient(135deg, var(--color-brand-50) 0%, var(--color-secondary-50) 100%);
  --gradient-brand-bold: linear-gradient(135deg, var(--color-brand-500) 0%, var(--color-secondary-500) 100%);
}

/* --- Dark Mode --- */
[data-theme="dark"],
.dark {
  --color-bg: var(--color-neutral-950);
  --color-bg-subtle: var(--color-neutral-900);
  --color-bg-muted: var(--color-neutral-800);
  --color-bg-emphasis: var(--color-brand-400);
  --color-fg: oklch(0.93 0.005 [h]);
  --color-fg-muted: var(--color-neutral-400);
  --color-fg-subtle: var(--color-neutral-500);
  --color-fg-on-emphasis: var(--color-neutral-950);
  --color-border: oklch(1 0 0 / 0.10);
  --color-border-strong: oklch(1 0 0 / 0.18);
  --color-border-brand: var(--color-brand-400);

  /* Semantic shifts for dark mode */
  --color-success-50: oklch(0.20 0.04 145);
  --color-success-500: oklch(0.65 0.17 145);
  --color-success-700: oklch(0.80 0.10 145);
  --color-warning-50: oklch(0.20 0.04 85);
  --color-warning-500: oklch(0.75 0.15 85);
  --color-warning-700: oklch(0.85 0.10 85);
  --color-error-50: oklch(0.20 0.04 27);
  --color-error-500: oklch(0.65 0.20 27);
  --color-error-700: oklch(0.80 0.12 27);
  --color-info-50: oklch(0.20 0.03 250);
  --color-info-500: oklch(0.65 0.15 250);
  --color-info-700: oklch(0.80 0.08 250);
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    /* Same dark overrides */
  }
}
```

All `(...)` values are replaced with actual computed values at generation time.

### Step 11 — Save to .sumi/style.json

Save the palette section to `.sumi/style.json`. If the file already exists (from `/style`), merge into the `color` key. If not, create with color data.

```json
{
  "meta": {
    "generated": "ISO-8601 timestamp",
    "command": "/palette",
    "input": "[what the user provided]"
  },
  "color": {
    "neutral": { "50": "oklch(...)", "100": "oklch(...)", "...": "..." },
    "brand": { "50": "oklch(...)", "...": "..." },
    "secondary": { "50": "oklch(...)", "...": "..." },
    "semantic": {
      "success": { "50": "...", "100": "...", "500": "...", "700": "..." },
      "warning": { "50": "...", "100": "...", "500": "...", "700": "..." },
      "error": { "50": "...", "100": "...", "500": "...", "700": "..." },
      "info": { "50": "...", "100": "...", "500": "...", "700": "..." }
    },
    "dataViz": {
      "categorical": ["oklch(...)", "oklch(...)", "..."],
      "sequential": ["oklch(...)", "oklch(...)", "..."],
      "diverging": ["oklch(...)", "oklch(...)", "..."]
    },
    "gradients": {
      "brandSubtle": "linear-gradient(...)",
      "brandBold": "linear-gradient(...)"
    },
    "darkMode": {
      "neutral": { "...": "..." },
      "brand": { "...": "..." },
      "secondary": { "...": "..." },
      "semantic": { "...": "..." }
    }
  }
}
```

---

## Output Format

```
## Palette: [Context — mood / sector / brand color]

### Anchor Color
[Hue selection rationale, OKLCH value, mood/sector reasoning]

### Neutral Scale
[Full 12-step table with oklch + hex + usage]

### Brand Primary Scale
[Full 11-step table]

### Secondary Scale
[Full 11-step table with relationship strategy explained]

### Semantic Colors
[Success/warning/error/info — light + dark mode values]

### APCA Contrast Verification
[Every functional pair with Lc score and pass/fail]

### Dark Mode Palette
[Complete transformation with strategy notes]

### Data Visualization
[Categorical (6-8), Sequential (5-7), Diverging (7-9) — all colorblind verified]

### Gradient Recipes
[4-6 CSS-ready gradients]

### CSS Custom Properties
[Complete copy-paste block with light + dark themes]

### Saved
> Palette saved to `.sumi/style.json` — available to `/style`, `/type`, `/tokens`, `/screen`, `/component`
```

---

## Colorblind Safety Verification

For every categorical and diverging palette, verify distinguishability under:

| Condition | Prevalence | Hue Confusion Pairs | Verification Method |
|-----------|-----------|-------------------|-------------------|
| Protanopia (no red) | 1.3% male | Red-green | Simulate and check unique lightness per color |
| Deuteranopia (no green) | 6% male | Red-green | Simulate and check unique lightness per color |
| Tritanopia (no blue) | 0.01% | Blue-yellow | Simulate and check unique lightness per color |
| Achromatopsia (no color) | 0.003% | All hues | Ensure unique lightness for every category |

Strategy: When hues become confusable under simulation, ensure each color has a **unique lightness value** so they remain distinguishable even without hue discrimination. This is the primary advantage of working in OKLCH — lightness is perceptually calibrated.

---

## Cross-References

When generating palettes, draw knowledge from:
- `color-palette-library` skill for 500+ curated palette references and industry conventions
- `ui-visual-design-system` skill for color theory, harmony models, and perceptual principles
- `visual-design-mastery` skill for color scoring, canonical color rules, and design critique
- `accessibility-inclusive-design` skill for WCAG 2.2/3.0, APCA methodology, and colorblind design
- `data-visualization-mastery` skill for data-viz-specific color requirements and chart palette design
- `cross-cultural-i18n-ux` skill for cultural color associations and localization
- `sector-style-intelligence` skill for sector-specific color conventions and psychology
- `design-token-presets` skill for pre-built color token systems as starting points

## Next Step

**Next** -> `/type` — Generate typography system to pair with this palette
**Or** -> `/style` — Full visual identity (color + type + spacing + motion + tone)
**Or** -> `/tokens` — Export palette as production W3C design tokens
**Or** -> `/dark` — Deep-dive dark mode with surface elevation strategy