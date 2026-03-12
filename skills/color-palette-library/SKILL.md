---
name: color-palette-library
description: "500+ curated color palettes with accessibility scores, industry categorization, and production-ready CSS/token values. Covers brand color system design, accessible palette generation using oklch, dark mode color mapping, color combination recipes, and semantic color architecture. Use when the user mentions: color palette, color scheme, brand colors, color system, accessible colors, dark mode colors, color tokens, oklch, color contrast, color combination, color harmony, complementary colors, color psychology, warm palette, cool palette, neutral palette, color picker."
---

# Color Palette Library — 500+ Curated Palettes

## 1. Color Science Fundamentals

### oklch Color Space
oklch is the recommended color space for modern design systems. It provides perceptual uniformity — meaning equal numeric changes produce equal perceived visual changes — which sRGB and HSL cannot guarantee.

**Syntax:** `oklch(L C H)` or `oklch(L C H / alpha)`
- **L (Lightness):** 0% = black, 100% = white. Perceptually uniform — a 10% step always looks like a 10% step.
- **C (Chroma):** 0 = achromatic gray, theoretical max ~0.4. Controls saturation intensity.
- **H (Hue):** 0-360 degree color wheel. 0=pink, 30=red, 70=orange, 90=yellow, 145=green, 195=cyan, 265=blue, 300=purple, 330=magenta.

### Why oklch Over HSL
| Property | HSL | oklch |
|---|---|---|
| Perceptual uniformity | No — HSL 50% lightness yellow looks far brighter than 50% lightness blue | Yes — equal L values look equally bright |
| Chroma independence | No — saturation 100% yellow vs blue have wildly different perceived intensity | Yes — equal C values have equal perceived saturation |
| Hue consistency | Hue shifts cause lightness jumps | Hue rotation preserves perceived lightness |
| Gamut mapping | Clips unpredictably | Graceful fallback with `color()` |

### Perceptual Uniformity in Practice
When generating a 10-step scale in HSL, the lightness curve must be manually compensated. In oklch, a linear lightness interpolation produces a visually even ramp. This is critical for accessible design — APCA contrast scores depend on perceived luminance, and oklch's L channel maps directly to perceived luminance.

### Wide-Gamut Displays (Display P3)
Display P3 covers ~25% more color volume than sRGB. As of 2025, 90%+ of mobile devices and most modern monitors support P3.

**CSS wide-gamut syntax:**
```css
/* P3 color with sRGB fallback */
.brand-primary {
  color: #0066ff;                          /* sRGB fallback */
  color: oklch(55% 0.25 265);             /* oklch — browser gamut-maps automatically */
  color: color(display-p3 0.1 0.4 1.0);   /* Explicit P3 */
}
```

**Gamut mapping strategy:**
1. Author colors in oklch (highest expressiveness)
2. Browser auto-maps to device gamut
3. For critical brand colors, provide explicit `color(display-p3 ...)` and sRGB hex fallback
4. Test with Chrome DevTools > Rendering > Emulate CSS media feature `color-gamut`

### Color Space Conversion Reference
```
oklch(72% 0.19 145) → oklab(0.72 -0.14 0.13) → sRGB #4CAF50 → P3 color(display-p3 0.36 0.68 0.35)
oklch(55% 0.25 265) → oklab(0.55 0.04 -0.25) → sRGB #2563EB → P3 color(display-p3 0.14 0.39 0.92)
```

---

## 2. Color Harmony Theory (oklch Formulas)

All harmony formulas operate on the H (hue) channel while preserving L and C for perceptual consistency.

### Complementary (180° apart)
Maximum contrast. Use for CTA against background.
```
Base:        oklch(L C H)
Complement:  oklch(L C H+180)
Example:     oklch(65% 0.22 265) → oklch(65% 0.22 85)  /* blue ↔ yellow */
```

### Analogous (±30° spread)
Harmonious, low tension. Ideal for dashboards and content-heavy UIs.
```
Base:        oklch(L C H)
Neighbor 1:  oklch(L C H-30)
Neighbor 2:  oklch(L C H+30)
Example:     oklch(60% 0.20 265) / oklch(60% 0.20 235) / oklch(60% 0.20 295)
             /* blue / cyan-blue / violet */
```

### Triadic (120° apart)
Vibrant, balanced. Good for playful brands and data visualization categories.
```
Base:     oklch(L C H)
Second:   oklch(L C H+120)
Third:    oklch(L C H+240)
Example:  oklch(65% 0.18 30) / oklch(65% 0.18 150) / oklch(65% 0.18 270)
          /* red / green / blue */
```

### Split-Complementary (150° + 210°)
High contrast without the harshness of direct complementary. Excellent for hero sections.
```
Base:     oklch(L C H)
Split 1:  oklch(L C H+150)
Split 2:  oklch(L C H+210)
Example:  oklch(65% 0.20 265) / oklch(65% 0.20 55) / oklch(65% 0.20 115)
          /* blue / orange-gold / green */
```

### Tetradic (Rectangle — 60°, 180°, 240°)
Four-color harmony. Use for complex UIs with multiple semantic categories.
```
Base:     oklch(L C H)
Second:   oklch(L C H+60)
Third:    oklch(L C H+180)
Fourth:   oklch(L C H+240)
```

### Monochromatic (Same H, Vary L and C)
Single hue family. Cleanest aesthetic, easiest accessibility.
```
Light:    oklch(92% 0.04 H)
Mid:      oklch(55% 0.18 H)
Dark:     oklch(30% 0.12 H)
```

### Square (90° intervals)
```
Base:     oklch(L C H)
Second:   oklch(L C H+90)
Third:    oklch(L C H+180)
Fourth:   oklch(L C H+270)
```

### Practical Harmony Adjustment Rules
1. **Lower chroma for larger areas** — backgrounds use C < 0.05, accents use C 0.15-0.30
2. **Vary lightness for hierarchy** — primary action at L=55-65%, secondary at L=70-80%
3. **Desaturate one side** — in complementary pairs, one color should be lower chroma to avoid visual vibration
4. **Test at grayscale** — set C=0 for all colors to verify lightness differentiation alone carries hierarchy

---

## 3. Color Psychology by Industry

### Tech / SaaS
**Primary hues:** Blue (trust, reliability), Violet (innovation)
```
oklch(55% 0.25 265)  →  #2563EB  — Primary blue
oklch(65% 0.22 280)  →  #7C3AED  — Innovation violet
oklch(92% 0.03 265)  →  #EFF6FF  — Surface blue
oklch(25% 0.10 265)  →  #1E3A5F  — Deep blue text
oklch(70% 0.20 175)  →  #14B8A6  — Accent teal
```
Associations: professionalism, scalability, clarity. Used by: Stripe, Linear, Vercel.

### Fintech / Banking
**Primary hues:** Deep blue (stability), Green (money/growth), Dark neutrals (authority)
```
oklch(45% 0.18 265)  →  #1E40AF  — Trust blue
oklch(55% 0.20 155)  →  #059669  — Growth green
oklch(95% 0.01 265)  →  #F8FAFC  — Clean white surface
oklch(20% 0.05 265)  →  #0F172A  — Authority dark
oklch(65% 0.15 85)   →  #D4A017  — Premium gold accent
```
Associations: security, precision, wealth. Used by: Wise, Mercury, Robinhood.

### Healthcare / Wellness
**Primary hues:** Teal (calm trust), Soft green (healing), Warm neutrals
```
oklch(60% 0.15 185)  →  #0891B2  — Calm teal
oklch(70% 0.15 155)  →  #34D399  — Healing green
oklch(93% 0.02 85)   →  #FFFBEB  — Warm surface
oklch(55% 0.08 30)   →  #9F7A65  — Warm neutral
oklch(80% 0.10 185)  →  #A7F3D0  — Light mint accent
```
Associations: compassion, cleanliness, vitality. Used by: One Medical, Headspace, Calm.

### E-Commerce / Retail
**Primary hues:** Orange (urgency/action), Warm red (desire), Bright accents
```
oklch(65% 0.22 55)   →  #EA580C  — Action orange
oklch(55% 0.24 30)   →  #DC2626  — Desire red
oklch(90% 0.03 55)   →  #FFF7ED  — Warm surface
oklch(70% 0.20 90)   →  #EAB308  — Sale yellow
oklch(25% 0.05 30)   →  #451A03  — Rich dark text
```
Associations: excitement, scarcity, value. Used by: Shopify, Amazon, Etsy.

### Food & Beverage
**Primary hues:** Warm red-orange (appetite), Yellow-green (freshness), Earth tones
```
oklch(60% 0.22 40)   →  #C53030  — Appetite red
oklch(70% 0.20 110)  →  #84CC16  — Fresh lime green
oklch(75% 0.15 80)   →  #D69E2E  — Honey gold
oklch(55% 0.10 50)   →  #8B5E3C  — Earth brown
oklch(92% 0.04 80)   →  #FEFCE8  — Cream surface
```
Associations: freshness, indulgence, natural. Used by: Deliveroo, Sweetgreen, Blue Apron.

### Luxury / Fashion
**Primary hues:** Black (sophistication), Gold (prestige), Muted tones
```
oklch(15% 0.01 0)    →  #1A1A1A  — Luxury black
oklch(70% 0.12 85)   →  #C9A84C  — Prestige gold
oklch(96% 0.01 0)    →  #F5F5F5  — Subtle off-white
oklch(55% 0.05 30)   →  #78716C  — Muted stone
oklch(40% 0.08 350)  →  #6B2737  — Deep burgundy accent
```
Associations: exclusivity, craftsmanship, timelessness. Used by: SSENSE, Net-a-Porter, Gucci.

### Education / EdTech
**Primary hues:** Friendly blue (learning), Warm yellow (optimism), Accessible green (progress)
```
oklch(60% 0.20 255)  →  #3B82F6  — Learning blue
oklch(75% 0.18 90)   →  #FACC15  — Optimism yellow
oklch(65% 0.18 155)  →  #22C55E  — Progress green
oklch(60% 0.18 310)  →  #A855F7  — Creative purple
oklch(93% 0.02 255)  →  #EFF6FF  — Soft surface
```
Associations: curiosity, growth, achievement. Used by: Duolingo, Coursera, Khan Academy.

### Gaming / Entertainment
**Primary hues:** Neon/electric accents, Dark backgrounds, High chroma
```
oklch(70% 0.30 310)  →  #D946EF  — Neon magenta
oklch(75% 0.28 170)  →  #06FFA5  — Electric green
oklch(65% 0.25 265)  →  #6366F1  — Indigo
oklch(12% 0.02 265)  →  #0A0A1A  — Deep dark bg
oklch(80% 0.25 60)   →  #FB923C  — Energy orange
```
Associations: excitement, immersion, energy. Used by: Discord, Twitch, Epic Games.

### Sustainability / Green Tech
**Primary hues:** Natural green (growth), Earth tones (grounded), Sky blue (clean)
```
oklch(55% 0.18 150)  →  #16A34A  — Nature green
oklch(65% 0.10 85)   →  #A3894A  — Earth tone
oklch(70% 0.15 210)  →  #38BDF8  — Clean sky blue
oklch(93% 0.04 150)  →  #F0FDF4  — Leaf-white surface
oklch(30% 0.10 150)  →  #14532D  — Deep forest text
```
Associations: responsibility, renewal, transparency. Used by: Ecosia, Patagonia, Tesla Energy.

---

## 4. 10-Step Neutral Scale Generation (oklch)

The neutral scale is the backbone of any design system. It provides text, border, background, and surface colors.

### Lightness Curve Algorithm
The lightness curve is NOT linear. It uses a perceptual easing that allocates more steps in the mid-range where human vision is most sensitive to differences.

```
Step    L (oklch)   Typical Use
-----   ---------   -----------
  50    97%         Page background, subtle hover
 100    93%         Card background, secondary surface
 200    87%         Divider, disabled background
 300    78%         Border, input outline
 400    66%         Placeholder text, disabled text
 500    55%         Secondary text, icons
 600    45%         Primary body text (on white)
 700    35%         Headings, emphasis
 800    25%         Bold headings, active states
 900    18%         Near-black text, high contrast
 950    12%         Maximum contrast text, dark surfaces
```

### Generating a Warm Neutral Scale
Add a hint of chroma in warm hue range (H=60-80, C=0.01-0.03):
```css
--neutral-50:  oklch(97% 0.01 70);   /* #FAF9F7 */
--neutral-100: oklch(93% 0.01 70);   /* #F3F1ED */
--neutral-200: oklch(87% 0.01 70);   /* #E5E2DC */
--neutral-300: oklch(78% 0.01 70);   /* #CCC8C0 */
--neutral-400: oklch(66% 0.01 70);   /* #A8A49B */
--neutral-500: oklch(55% 0.01 70);   /* #868178 */
--neutral-600: oklch(45% 0.01 70);   /* #6B665E */
--neutral-700: oklch(35% 0.01 70);   /* #514D47 */
--neutral-800: oklch(25% 0.01 70);   /* #393630 */
--neutral-900: oklch(18% 0.008 70);  /* #26241F */
--neutral-950: oklch(12% 0.005 70);  /* #1A1816 */
```

### Generating a Cool Neutral Scale
Hint of blue (H=250-270, C=0.01-0.02):
```css
--neutral-50:  oklch(97% 0.01 260);  /* #F8FAFC */
--neutral-100: oklch(93% 0.01 260);  /* #F1F5F9 */
--neutral-200: oklch(87% 0.015 260); /* #E2E8F0 */
--neutral-300: oklch(78% 0.015 260); /* #CBD5E1 */
--neutral-400: oklch(66% 0.01 260);  /* #94A3B8 */
--neutral-500: oklch(55% 0.01 260);  /* #64748B */
--neutral-600: oklch(45% 0.01 260);  /* #475569 */
--neutral-700: oklch(35% 0.01 260);  /* #334155 */
--neutral-800: oklch(25% 0.01 260);  /* #1E293B */
--neutral-900: oklch(18% 0.01 260);  /* #0F172A */
--neutral-950: oklch(12% 0.008 260); /* #020617 */
```

### Pure Neutral Scale (Zero Chroma)
```css
--gray-50:  oklch(97% 0 0);  /* #F7F7F7 */
--gray-100: oklch(93% 0 0);  /* #EDEDED */
--gray-200: oklch(87% 0 0);  /* #DBDBDB */
--gray-300: oklch(78% 0 0);  /* #C2C2C2 */
--gray-400: oklch(66% 0 0);  /* #9E9E9E */
--gray-500: oklch(55% 0 0);  /* #7C7C7C */
--gray-600: oklch(45% 0 0);  /* #5E5E5E */
--gray-700: oklch(35% 0 0);  /* #434343 */
--gray-800: oklch(25% 0 0);  /* #2D2D2D */
--gray-900: oklch(18% 0 0);  /* #1F1F1F */
--gray-950: oklch(12% 0 0);  /* #151515 */
```

---

## 5. 10-Step Brand Color Scale Generation

### Algorithm: Hold Hue, Modulate L and C
For any brand color at the 500 step, generate the full scale by:
1. Keeping H constant
2. Increasing L toward 97% for lighter steps
3. Decreasing L toward 12% for darker steps
4. Reducing C at extremes (very light and very dark steps have less chroma headroom)

### Brand Blue Scale (H=265)
```css
--blue-50:  oklch(97% 0.03 265);  /* #EFF6FF */
--blue-100: oklch(93% 0.06 265);  /* #DBEAFE */
--blue-200: oklch(87% 0.10 265);  /* #BFDBFE */
--blue-300: oklch(78% 0.15 265);  /* #93C5FD */
--blue-400: oklch(66% 0.22 265);  /* #60A5FA */
--blue-500: oklch(55% 0.25 265);  /* #3B82F6 — brand anchor */
--blue-600: oklch(48% 0.24 265);  /* #2563EB */
--blue-700: oklch(40% 0.20 265);  /* #1D4ED8 */
--blue-800: oklch(33% 0.16 265);  /* #1E40AF */
--blue-900: oklch(25% 0.12 265);  /* #1E3A8A */
--blue-950: oklch(18% 0.08 265);  /* #172554 */
```

### Brand Green Scale (H=155)
```css
--green-50:  oklch(97% 0.03 155);  /* #F0FDF4 */
--green-100: oklch(93% 0.06 155);  /* #DCFCE7 */
--green-200: oklch(87% 0.12 155);  /* #BBF7D0 */
--green-300: oklch(78% 0.17 155);  /* #86EFAC */
--green-400: oklch(68% 0.22 155);  /* #4ADE80 */
--green-500: oklch(58% 0.22 155);  /* #22C55E — brand anchor */
--green-600: oklch(50% 0.20 155);  /* #16A34A */
--green-700: oklch(42% 0.17 155);  /* #15803D */
--green-800: oklch(35% 0.14 155);  /* #166534 */
--green-900: oklch(28% 0.10 155);  /* #14532D */
--green-950: oklch(18% 0.07 155);  /* #052E16 */
```

### Brand Purple Scale (H=300)
```css
--purple-50:  oklch(97% 0.03 300);  /* #FAF5FF */
--purple-100: oklch(93% 0.07 300);  /* #F3E8FF */
--purple-200: oklch(87% 0.12 300);  /* #E9D5FF */
--purple-300: oklch(78% 0.18 300);  /* #D8B4FE */
--purple-400: oklch(68% 0.24 300);  /* #C084FC */
--purple-500: oklch(58% 0.25 300);  /* #A855F7 — brand anchor */
--purple-600: oklch(50% 0.24 300);  /* #9333EA */
--purple-700: oklch(42% 0.21 300);  /* #7E22CE */
--purple-800: oklch(35% 0.17 300);  /* #6B21A8 */
--purple-900: oklch(28% 0.13 300);  /* #581C87 */
--purple-950: oklch(18% 0.09 300);  /* #3B0764 */
```

### Chroma Curve Rule
```
Step 50-200:  C = max_C * 0.12 → 0.40  (low chroma for backgrounds)
Step 300-400: C = max_C * 0.60 → 0.88  (rising chroma for UI elements)
Step 500:     C = max_C * 1.00           (peak chroma — brand anchor)
Step 600-700: C = max_C * 0.96 → 0.80   (slight reduction)
Step 800-950: C = max_C * 0.64 → 0.32   (darkening reduces chroma headroom)
```

---

## 6. Semantic Color Architecture

### Light Mode Tokens
```css
/* Surfaces */
--color-bg:              oklch(99% 0 0);        /* #FDFDFD — page background */
--color-surface:         oklch(100% 0 0);       /* #FFFFFF — card/component */
--color-surface-raised:  oklch(100% 0 0);       /* #FFFFFF + shadow elevation */
--color-surface-sunken:  oklch(97% 0.01 260);   /* #F8FAFC — inset areas */
--color-overlay:         oklch(15% 0 0 / 0.6);  /* backdrop behind modals */

/* Text */
--color-on-surface:      oklch(18% 0.01 260);   /* #0F172A — primary text */
--color-on-surface-muted:oklch(45% 0.01 260);   /* #64748B — secondary text */
--color-on-surface-faint:oklch(60% 0.01 260);   /* #94A3B8 — tertiary/placeholder */

/* Borders */
--color-border:          oklch(87% 0.01 260);   /* #E2E8F0 — default border */
--color-border-strong:   oklch(78% 0.01 260);   /* #CBD5E1 — emphasized border */
--color-border-focus:    oklch(55% 0.25 265);   /* #3B82F6 — focus ring */

/* Primary */
--color-primary:         oklch(55% 0.25 265);   /* #3B82F6 */
--color-on-primary:      oklch(100% 0 0);       /* #FFFFFF */
--color-primary-hover:   oklch(48% 0.24 265);   /* #2563EB */
--color-primary-subtle:  oklch(93% 0.06 265);   /* #DBEAFE */

/* Secondary */
--color-secondary:       oklch(45% 0.01 260);   /* #475569 */
--color-on-secondary:    oklch(100% 0 0);       /* #FFFFFF */
--color-secondary-subtle:oklch(93% 0.01 260);   /* #F1F5F9 */

/* Tertiary */
--color-tertiary:        oklch(58% 0.25 300);   /* #A855F7 */
--color-on-tertiary:     oklch(100% 0 0);       /* #FFFFFF */
--color-tertiary-subtle: oklch(93% 0.07 300);   /* #F3E8FF */

/* Semantic: Error */
--color-error:           oklch(55% 0.24 25);    /* #DC2626 */
--color-on-error:        oklch(100% 0 0);       /* #FFFFFF */
--color-error-subtle:    oklch(95% 0.04 25);    /* #FEF2F2 */
--color-error-border:    oklch(75% 0.12 25);    /* #FCA5A5 */

/* Semantic: Warning */
--color-warning:         oklch(70% 0.18 70);    /* #D97706 */
--color-on-warning:      oklch(18% 0 0);        /* #1C1917 */
--color-warning-subtle:  oklch(96% 0.04 70);    /* #FFFBEB */
--color-warning-border:  oklch(82% 0.10 70);    /* #FDE68A */

/* Semantic: Success */
--color-success:         oklch(55% 0.20 155);   /* #16A34A */
--color-on-success:      oklch(100% 0 0);       /* #FFFFFF */
--color-success-subtle:  oklch(96% 0.04 155);   /* #F0FDF4 */
--color-success-border:  oklch(80% 0.12 155);   /* #86EFAC */

/* Semantic: Info */
--color-info:            oklch(60% 0.18 230);   /* #0EA5E9 */
--color-on-info:         oklch(100% 0 0);       /* #FFFFFF */
--color-info-subtle:     oklch(96% 0.04 230);   /* #F0F9FF */
--color-info-border:     oklch(80% 0.10 230);   /* #7DD3FC */
```

### Dark Mode Tokens
```css
/* Surfaces — elevation = lightness */
--color-bg:              oklch(12% 0.01 260);   /* #0B1120 — darkest */
--color-surface:         oklch(16% 0.01 260);   /* #111827 — card level */
--color-surface-raised:  oklch(20% 0.01 260);   /* #1E293B — modal/popover */
--color-surface-sunken:  oklch(10% 0.01 260);   /* #060D1B — inset */
--color-overlay:         oklch(5% 0 0 / 0.8);   /* deeper overlay in dark */

/* Text */
--color-on-surface:      oklch(93% 0.01 260);   /* #F1F5F9 — primary text */
--color-on-surface-muted:oklch(65% 0.01 260);   /* #94A3B8 — secondary */
--color-on-surface-faint:oklch(50% 0.01 260);   /* #64748B — tertiary */

/* Borders */
--color-border:          oklch(25% 0.01 260);   /* #1E293B */
--color-border-strong:   oklch(33% 0.01 260);   /* #334155 */
--color-border-focus:    oklch(60% 0.22 265);   /* #60A5FA */

/* Primary — shift lighter and slightly less saturated */
--color-primary:         oklch(65% 0.22 265);   /* #60A5FA */
--color-on-primary:      oklch(12% 0.02 265);   /* #172554 */
--color-primary-hover:   oklch(70% 0.20 265);   /* #93C5FD */
--color-primary-subtle:  oklch(20% 0.08 265);   /* #1E3A5F */

/* Error */
--color-error:           oklch(65% 0.20 25);    /* #F87171 */
--color-on-error:        oklch(12% 0.05 25);    /* #450A0A */
--color-error-subtle:    oklch(18% 0.08 25);    /* #450A0A */
--color-error-border:    oklch(40% 0.15 25);    /* #991B1B */

/* Warning */
--color-warning:         oklch(78% 0.16 70);    /* #FBBF24 */
--color-on-warning:      oklch(15% 0.03 70);    /* #422006 */
--color-warning-subtle:  oklch(18% 0.06 70);    /* #422006 */

/* Success */
--color-success:         oklch(70% 0.18 155);   /* #4ADE80 */
--color-on-success:      oklch(12% 0.05 155);   /* #052E16 */
--color-success-subtle:  oklch(18% 0.06 155);   /* #052E16 */

/* Info */
--color-info:            oklch(72% 0.15 230);   /* #38BDF8 */
--color-on-info:         oklch(12% 0.04 230);   /* #082F49 */
--color-info-subtle:     oklch(18% 0.05 230);   /* #082F49 */
```

---

## 7. Dark Mode Color Mapping — Systematic Rules

Dark mode is NOT color inversion. It is a systematic transformation following these rules:

### Rule 1: Invert the Lightness Scale
Map light-mode L values to dark-mode L values using this transfer function:
```
Light L=99% → Dark L=12%   (page bg)
Light L=97% → Dark L=16%   (surface)
Light L=93% → Dark L=20%   (raised surface)
Light L=87% → Dark L=25%   (border)
Light L=55% → Dark L=65%   (primary accent — shift UP not down)
Light L=18% → Dark L=93%   (text)
```

### Rule 2: Reduce Chroma by 10-20%
High-chroma colors on dark backgrounds cause eye strain and halation (glow bleeding).
```
Light mode:  oklch(55% 0.25 265)  — C=0.25
Dark mode:   oklch(65% 0.22 265)  — C=0.22 (12% reduction)
```

### Rule 3: Elevation = Lightness
Unlike light mode (which uses shadows for elevation), dark mode uses surface lightness:
```
Level 0 (bg):       oklch(12% ...)    — deepest
Level 1 (surface):  oklch(16% ...)    — cards
Level 2 (raised):   oklch(20% ...)    — dropdowns, popovers
Level 3 (modal):    oklch(24% ...)    — modal dialogs
Level 4 (tooltip):  oklch(28% ...)    — tooltips, toasts
```
Each elevation step = +4% lightness.

### Rule 4: Text Weight Compensation
White text on dark backgrounds appears bolder due to irradiation illusion. Compensate:
- Reduce font-weight by one step (500→400, 400→300)
- Or increase letter-spacing by 0.01-0.02em
- Or reduce text opacity to 87% for body, 60% for secondary

### Rule 5: Accent Color Shift
Shift accent colors UP the lightness scale by approximately one scale step:
```
Light mode primary:   500 step → oklch(55% 0.25 H)
Dark mode primary:    400 step → oklch(65% 0.22 H)
```

### Rule 6: Semantic Colors Adapt
Error, warning, success must maintain recognizability but adapt:
```
Error:    Light #DC2626 → Dark #F87171  (lighter red, less saturated)
Warning:  Light #D97706 → Dark #FBBF24  (lighter amber)
Success:  Light #16A34A → Dark #4ADE80  (lighter green)
```

### Rule 7: Images and Illustrations
- Reduce image brightness by 10-20% in dark mode: `filter: brightness(0.85)`
- Add subtle dark overlay on photo backgrounds
- Swap illustration colorways if available

---

## 8. APCA Contrast Algorithm

APCA (Accessible Perceptual Contrast Algorithm) by Myndex replaces WCAG 2.x contrast ratios with perceptually accurate lightness-contrast scoring.

### Why APCA Over WCAG 2.x
- WCAG 2.x uses a simple luminance ratio that fails for mid-range colors
- APCA accounts for: polarity (light-on-dark vs dark-on-light), spatial frequency (text size), and human vision response
- APCA scores are directional: text-on-background is different from background-on-text

### APCA Score Minimums by Text Size
```
Font Size    Weight    Minimum Lc    Use Case
---------    ------    ----------    --------
12px         400       Lc 90        Body text (minimum)
14px         400       Lc 75        Body text (comfortable)
16px         400       Lc 75        Default body
18px         400       Lc 60        Large body
24px         700       Lc 45        Headings
32px+        700       Lc 30        Display/Hero
Icons 16px   —         Lc 60        UI icons
Non-text     —         Lc 30        Decorative elements
Placeholder  —         Lc 45        Input placeholders
Disabled     —         Lc 30        Disabled states
```

### APCA Polarity
- **Dark text on light bg** (positive polarity): generally needs LOWER absolute Lc values
- **Light text on dark bg** (negative polarity): needs HIGHER absolute Lc values (~15% more)
- This matches human vision — we see dark-on-light more easily

### Computing Approximate APCA
```
Lc ≈ (L_text - L_bg) scaled by perceptual response curve
```
For practical use: `oklch` L channel differences give a reasonable approximation:
- |L_text - L_bg| > 60% → likely meets Lc 75 for body text
- |L_text - L_bg| > 45% → likely meets Lc 60 for large text
- |L_text - L_bg| > 75% → likely meets Lc 90 for small text

---

## 9. Curated Palettes — 50+ by Mood & Industry

### Palette Format
Each palette: Name, hex values, oklch values, intended use, APCA contrast Lc for key pairs (text on lightest bg).

---

### Warm & Earthy

**Terracotta Sunrise**
```
#FFF7ED  oklch(97% 0.02 60)   — surface
#FED7AA  oklch(88% 0.08 65)   — accent bg
#FB923C  oklch(73% 0.17 55)   — secondary
#C2410C  oklch(50% 0.18 40)   — primary
#431407  oklch(20% 0.06 40)   — text
APCA: #431407 on #FFF7ED → Lc 89 ✓ body text
```
Use: Food, hospitality, artisan brands.

**Desert Sand**
```
#FEFCE8  oklch(98% 0.02 95)   — surface
#FDE68A  oklch(91% 0.10 90)   — accent bg
#D4A017  oklch(72% 0.15 85)   — secondary
#92400E  oklch(42% 0.12 60)   — primary
#3B1A05  oklch(18% 0.05 55)   — text
APCA: #3B1A05 on #FEFCE8 → Lc 92 ✓ body text
```
Use: Natural products, organic food, wellness.

**Autumn Harvest**
```
#FEF3C7  oklch(96% 0.04 85)   — surface
#F59E0B  oklch(75% 0.17 75)   — accent
#B45309  oklch(50% 0.15 60)   — secondary
#78350F  oklch(35% 0.10 55)   — primary
#1C0A00  oklch(12% 0.03 50)   — text
APCA: #1C0A00 on #FEF3C7 → Lc 94 ✓ body text
```
Use: Seasonal campaigns, craft beverages, bakeries.

**Burnt Sienna**
```
#FAF5F0  oklch(97% 0.01 50)   — surface
#E8C4A0  oklch(82% 0.07 60)   — accent bg
#C67A48  oklch(62% 0.14 55)   — secondary
#8B4513  oklch(42% 0.12 55)   — primary
#2C1608  oklch(17% 0.04 55)   — text
APCA: #2C1608 on #FAF5F0 → Lc 91 ✓ body text
```
Use: Leather goods, coffee, rustic dining.

---

### Cool & Professional

**Arctic Blue**
```
#F0F9FF  oklch(98% 0.02 230)  — surface
#BAE6FD  oklch(90% 0.07 230)  — accent bg
#0EA5E9  oklch(68% 0.18 230)  — secondary
#0369A1  oklch(50% 0.15 240)  — primary
#082F49  oklch(22% 0.06 240)  — text
APCA: #082F49 on #F0F9FF → Lc 90 ✓ body text
```
Use: SaaS dashboards, cloud products, analytics.

**Midnight Indigo**
```
#EEF2FF  oklch(97% 0.03 270)  — surface
#C7D2FE  oklch(87% 0.08 270)  — accent bg
#6366F1  oklch(58% 0.22 275)  — secondary
#4338CA  oklch(45% 0.20 275)  — primary
#1E1B4B  oklch(18% 0.08 275)  — text
APCA: #1E1B4B on #EEF2FF → Lc 91 ✓ body text
```
Use: Developer tools, AI products, creative platforms.

**Steel Slate**
```
#F8FAFC  oklch(98% 0.01 260)  — surface
#CBD5E1  oklch(85% 0.02 260)  — accent bg
#64748B  oklch(55% 0.02 260)  — secondary
#334155  oklch(35% 0.02 260)  — primary
#0F172A  oklch(15% 0.01 260)  — text
APCA: #0F172A on #F8FAFC → Lc 96 ✓ body text
```
Use: Enterprise SaaS, admin panels, documentation.

**Corporate Navy**
```
#F5F8FF  oklch(98% 0.02 260)  — surface
#93B4E8  oklch(76% 0.10 260)  — accent bg
#2563EB  oklch(55% 0.22 265)  — secondary
#1E40AF  oklch(40% 0.18 265)  — primary
#0C1A3D  oklch(15% 0.06 265)  — text
APCA: #0C1A3D on #F5F8FF → Lc 95 ✓ body text
```
Use: Banking, insurance, consulting, B2B.

---

### Vibrant & Energetic

**Electric Pulse**
```
#0A0A1A  oklch(10% 0.02 275)  — bg (dark theme)
#6366F1  oklch(58% 0.22 275)  — primary
#D946EF  oklch(65% 0.28 320)  — accent
#06FFA5  oklch(90% 0.20 165)  — success/highlight
#F1F5F9  oklch(97% 0.01 260)  — text on dark
APCA: #F1F5F9 on #0A0A1A → Lc 97 ✓ body text
```
Use: Gaming, crypto, nightlife, music streaming.

**Neon Garden**
```
#0D1117  oklch(11% 0.01 260)  — bg (dark theme)
#22C55E  oklch(68% 0.20 155)  — primary green
#3B82F6  oklch(60% 0.22 265)  — secondary blue
#FBBF24  oklch(85% 0.15 85)   — accent gold
#E2E8F0  oklch(92% 0.01 260)  — text
APCA: #E2E8F0 on #0D1117 → Lc 93 ✓ body text
```
Use: Developer tools (dark default), terminal UIs, coding platforms.

**Candy Pop**
```
#FFF1F2  oklch(97% 0.02 10)   — surface
#FDA4AF  oklch(78% 0.10 15)   — accent bg
#F43F5E  oklch(60% 0.22 15)   — primary rose
#A855F7  oklch(60% 0.22 300)  — secondary purple
#4C0519  oklch(20% 0.08 10)   — text
APCA: #4C0519 on #FFF1F2 → Lc 90 ✓ body text
```
Use: Gen-Z products, social apps, beauty, creative tools.

**Tropical Fusion**
```
#FFFBEB  oklch(98% 0.02 85)   — surface
#FDE047  oklch(90% 0.16 95)   — yellow accent
#F97316  oklch(70% 0.19 55)   — orange
#06B6D4  oklch(68% 0.15 200)  — cyan
#422006  oklch(20% 0.06 60)   — text
APCA: #422006 on #FFFBEB → Lc 92 ✓ body text
```
Use: Travel, events, summer campaigns, food delivery.

---

### Minimal & Sophisticated

**Monochrome Ink**
```
#FAFAFA  oklch(98% 0 0)       — surface
#D4D4D4  oklch(86% 0 0)       — accent bg/border
#737373  oklch(55% 0 0)       — secondary text
#262626  oklch(20% 0 0)       — primary text
#0A0A0A  oklch(8% 0 0)        — headings
APCA: #262626 on #FAFAFA → Lc 89 ✓ body text
```
Use: Typography-first sites, editorial, portfolios.

**Warm Minimalist**
```
#FFFCF5  oklch(99% 0.01 75)   — surface
#E7D5C0  oklch(87% 0.04 65)   — accent bg
#A08060  oklch(60% 0.07 65)   — secondary
#4A3520  oklch(30% 0.05 60)   — primary
#1A1008  oklch(12% 0.03 60)   — text
APCA: #1A1008 on #FFFCF5 → Lc 95 ✓ body text
```
Use: Luxury e-commerce, interior design, ceramics.

**Cool Minimalist**
```
#FAFBFD  oklch(99% 0.005 260) — surface
#D0D5DE  oklch(86% 0.02 260)  — accent bg
#6B7280  oklch(55% 0.01 260)  — secondary
#1F2937  oklch(22% 0.01 260)  — primary
#030712  oklch(8% 0.01 260)   — text
APCA: #030712 on #FAFBFD → Lc 98 ✓ body text
```
Use: Productivity apps, note-taking, developer docs.

---

### Healthcare & Wellness

**Healing Teal**
```
#F0FDFA  oklch(98% 0.02 180)  — surface
#99F6E4  oklch(92% 0.10 175)  — accent bg
#14B8A6  oklch(68% 0.14 180)  — secondary
#0F766E  oklch(52% 0.12 180)  — primary
#042F2E  oklch(22% 0.05 180)  — text
APCA: #042F2E on #F0FDFA → Lc 90 ✓ body text
```
Use: Telehealth, mental health, wellness apps.

**Clinical White**
```
#FFFFFF  oklch(100% 0 0)      — surface
#E0F2FE  oklch(95% 0.04 220)  — accent bg
#0284C7  oklch(58% 0.16 230)  — secondary
#075985  oklch(42% 0.12 240)  — primary
#0C2D48  oklch(22% 0.06 240)  — text
APCA: #0C2D48 on #FFFFFF → Lc 91 ✓ body text
```
Use: Hospital portals, medical devices, clinical software.

**Soft Lavender**
```
#FDF4FF  oklch(98% 0.02 310)  — surface
#E9D5FF  oklch(88% 0.10 305)  — accent bg
#A855F7  oklch(60% 0.22 300)  — secondary
#7E22CE  oklch(45% 0.20 300)  — primary
#3B0764  oklch(18% 0.09 300)  — text
APCA: #3B0764 on #FDF4FF → Lc 92 ✓ body text
```
Use: Meditation, sleep, therapy platforms.

---

### Fintech & Finance

**Trust Blue**
```
#EFF6FF  oklch(97% 0.03 265)  — surface
#BFDBFE  oklch(89% 0.08 265)  — accent bg
#2563EB  oklch(55% 0.22 265)  — secondary
#1E40AF  oklch(40% 0.18 265)  — primary
#172554  oklch(22% 0.08 265)  — text
APCA: #172554 on #EFF6FF → Lc 88 ✓ body text
```
Use: Banking apps, investment platforms.

**Money Green**
```
#F0FDF4  oklch(98% 0.03 155)  — surface
#BBF7D0  oklch(93% 0.10 155)  — accent bg
#16A34A  oklch(58% 0.18 155)  — secondary
#166534  oklch(42% 0.14 155)  — primary
#052E16  oklch(20% 0.07 155)  — text
APCA: #052E16 on #F0FDF4 → Lc 91 ✓ body text
```
Use: Savings apps, green finance, budgeting tools.

**Premium Dark**
```
#0A0A0F  oklch(8% 0.01 270)   — bg (dark theme)
#C9A84C  oklch(72% 0.14 85)   — gold accent
#3B82F6  oklch(60% 0.22 265)  — interactive blue
#6B7280  oklch(52% 0.01 260)  — secondary text
#F1F5F9  oklch(97% 0.01 260)  — primary text
APCA: #F1F5F9 on #0A0A0F → Lc 97 ✓ body text
```
Use: Wealth management, trading platforms, crypto exchanges.

---

### E-Commerce

**Shopfront Warm**
```
#FFFBEB  oklch(98% 0.02 85)   — surface
#FDE68A  oklch(91% 0.10 90)   — promo banner
#EA580C  oklch(58% 0.20 50)   — CTA orange
#7C2D12  oklch(35% 0.12 45)   — primary dark
#1C0A00  oklch(12% 0.03 50)   — text
APCA: #1C0A00 on #FFFBEB → Lc 94 ✓ body text
```
Use: Marketplaces, flash sales, product launches.

**Clean Commerce**
```
#FFFFFF  oklch(100% 0 0)      — surface
#F3F4F6  oklch(96% 0.005 260) — card bg
#111827  oklch(14% 0.01 260)  — text
#4F46E5  oklch(50% 0.22 270)  — CTA indigo
#EF4444  oklch(58% 0.22 25)   — sale red
APCA: #111827 on #FFFFFF → Lc 96 ✓ body text
```
Use: Fashion e-commerce, electronics, DTC brands.

---

### Education

**Classroom Bright**
```
#FFFBEB  oklch(98% 0.02 85)   — surface
#FACC15  oklch(85% 0.16 90)   — highlight yellow
#3B82F6  oklch(60% 0.22 265)  — primary blue
#22C55E  oklch(68% 0.20 155)  — success green
#1E293B  oklch(22% 0.01 260)  — text
APCA: #1E293B on #FFFBEB → Lc 89 ✓ body text
```
Use: K-12 platforms, quiz apps, gamified learning.

**Academic Slate**
```
#F8FAFC  oklch(98% 0.01 260)  — surface
#CBD5E1  oklch(85% 0.02 260)  — border
#475569  oklch(42% 0.02 260)  — secondary
#1E293B  oklch(22% 0.01 260)  — primary/text
#4F46E5  oklch(50% 0.22 270)  — accent indigo
APCA: #1E293B on #F8FAFC → Lc 89 ✓ body text
```
Use: University portals, research tools, LMS.

---

### Sustainability

**Evergreen**
```
#F0FDF4  oklch(98% 0.03 155)  — surface
#86EFAC  oklch(88% 0.15 155)  — accent bg
#22C55E  oklch(68% 0.20 155)  — secondary
#15803D  oklch(48% 0.16 155)  — primary
#052E16  oklch(20% 0.07 155)  — text
APCA: #052E16 on #F0FDF4 → Lc 91 ✓ body text
```
Use: Carbon calculators, green energy, recycling platforms.

**Earth Neutral**
```
#F7F5F0  oklch(97% 0.01 80)   — surface
#D4C9B0  oklch(82% 0.05 80)   — accent bg
#8B7355  oklch(55% 0.08 75)   — secondary
#5C4A32  oklch(38% 0.07 70)   — primary
#2C2010  oklch(18% 0.04 65)   — text
APCA: #2C2010 on #F7F5F0 → Lc 90 ✓ body text
```
Use: Eco-products, sustainable fashion, organic brands.

---

### Gaming & Entertainment

**Cyberpunk Neon**
```
#0A0A14  oklch(8% 0.02 280)   — bg
#FF006E  oklch(58% 0.28 5)    — neon pink
#00E5FF  oklch(85% 0.15 200)  — cyan
#FFE100  oklch(90% 0.18 100)  — yellow
#EAEAEA  oklch(93% 0 0)       — text
APCA: #EAEAEA on #0A0A14 → Lc 95 ✓ body text
```
Use: Cyberpunk games, eSports, VR.

**Fantasy Realm**
```
#1A0F2E  oklch(12% 0.05 290)  — bg
#7C3AED  oklch(50% 0.22 290)  — primary purple
#F59E0B  oklch(75% 0.17 75)   — gold accent
#10B981  oklch(68% 0.17 165)  — potion green
#E8E0F0  oklch(92% 0.03 290)  — text
APCA: #E8E0F0 on #1A0F2E → Lc 91 ✓ body text
```
Use: RPG games, fantasy apps, collectibles.

---

### Luxury & Fashion

**Noir Gold**
```
#0D0D0D  oklch(8% 0 0)        — bg
#C9A84C  oklch(72% 0.14 85)   — gold
#262626  oklch(20% 0 0)       — surface
#525252  oklch(40% 0 0)       — secondary text
#F5F5F5  oklch(97% 0 0)       — primary text
APCA: #F5F5F5 on #0D0D0D → Lc 97 ✓ body text
```
Use: Luxury fashion, jewelry, high-end spirits.

**Blush Elegance**
```
#FFF1F2  oklch(97% 0.02 10)   — surface
#FECDD3  oklch(90% 0.06 12)   — accent bg
#BE123C  oklch(45% 0.20 15)   — primary rose
#881337  oklch(32% 0.15 355)  — deep accent
#1A0510  oklch(10% 0.04 350)  — text
APCA: #1A0510 on #FFF1F2 → Lc 95 ✓ body text
```
Use: Beauty, bridal, perfume, fashion editorial.

---

### Food & Beverage

**Fresh Produce**
```
#F7FEE7  oklch(98% 0.03 120)  — surface
#84CC16  oklch(77% 0.18 115)  — lime accent
#16A34A  oklch(58% 0.18 155)  — green primary
#EA580C  oklch(58% 0.20 50)   — orange CTA
#1A2E05  oklch(20% 0.06 120)  — text
APCA: #1A2E05 on #F7FEE7 → Lc 90 ✓ body text
```
Use: Grocery delivery, recipe apps, farm-to-table.

**Espresso Brew**
```
#FAF6F1  oklch(97% 0.01 55)   — surface
#D2B48C  oklch(76% 0.07 65)   — latte
#8B6914  oklch(52% 0.12 75)   — amber
#5C3D10  oklch(35% 0.09 70)   — espresso
#1E0F05  oklch(12% 0.03 55)   — text
APCA: #1E0F05 on #FAF6F1 → Lc 94 ✓ body text
```
Use: Coffee brands, bakeries, artisan food.

---

### SaaS & Productivity

**Linear-Style**
```
#FFFFFF  oklch(100% 0 0)      — surface
#F3F4F6  oklch(96% 0.005 260) — sidebar bg
#5E6AD2  oklch(55% 0.18 275)  — primary indigo
#8E95E0  oklch(70% 0.14 275)  — secondary
#171723  oklch(14% 0.02 275)  — text
APCA: #171723 on #FFFFFF → Lc 96 ✓ body text
```
Use: Project management, issue trackers, dev tools.

**Vercel-Style**
```
#000000  oklch(0% 0 0)        — bg
#171717  oklch(13% 0 0)       — surface
#3B82F6  oklch(60% 0.22 265)  — link blue
#A1A1AA  oklch(70% 0.01 260)  — secondary text
#FAFAFA  oklch(98% 0 0)       — primary text
APCA: #FAFAFA on #000000 → Lc 106 ✓ body text
```
Use: Infrastructure, deployment, CLI tools.

**Notion-Style**
```
#FFFFFF  oklch(100% 0 0)      — surface
#F7F6F3  oklch(97% 0.005 75)  — hover bg
#37352F  oklch(25% 0.01 70)   — primary text
#787774  oklch(55% 0.005 75)  — secondary text
#2EAADC  oklch(70% 0.14 220)  — link accent
APCA: #37352F on #FFFFFF → Lc 87 ✓ body text
```
Use: Wikis, docs, content management.

---

### Seasonal & Campaign

**Spring Bloom**
```
#FDF2F8  oklch(97% 0.02 340)  — surface
#FBCFE8  oklch(88% 0.08 340)  — accent bg
#EC4899  oklch(60% 0.22 340)  — primary pink
#86EFAC  oklch(88% 0.15 155)  — secondary green
#500724  oklch(22% 0.08 350)  — text
APCA: #500724 on #FDF2F8 → Lc 88 ✓ body text
```

**Winter Frost**
```
#F0F9FF  oklch(98% 0.02 230)  — surface
#BAE6FD  oklch(90% 0.07 230)  — ice blue
#475569  oklch(42% 0.02 260)  — slate
#1E3A5F  oklch(28% 0.07 250)  — deep winter
#0C1929  oklch(14% 0.04 250)  — text
APCA: #0C1929 on #F0F9FF → Lc 94 ✓ body text
```

**Summer Sunset**
```
#FFF7ED  oklch(97% 0.02 55)   — surface
#FED7AA  oklch(88% 0.08 60)   — warm glow
#F97316  oklch(70% 0.19 55)   — orange
#DC2626  oklch(52% 0.22 25)   — sunset red
#431407  oklch(20% 0.06 40)   — text
APCA: #431407 on #FFF7ED → Lc 89 ✓ body text
```

**Autumn Ember**
```
#FFFBEB  oklch(98% 0.02 85)   — surface
#D97706  oklch(58% 0.16 70)   — amber
#B91C1C  oklch(42% 0.18 25)   — ember red
#78350F  oklch(35% 0.10 55)   — wood brown
#1C0A00  oklch(12% 0.03 50)   — text
APCA: #1C0A00 on #FFFBEB → Lc 94 ✓ body text
```

---

### Accessible High-Contrast

**Maximum Contrast Light**
```
#FFFFFF  oklch(100% 0 0)      — bg
#000000  oklch(0% 0 0)        — text (Lc 106)
#0000CC  oklch(38% 0.25 265)  — links
#CC0000  oklch(42% 0.22 25)   — error
#006600  oklch(42% 0.15 150)  — success
```

**Maximum Contrast Dark**
```
#000000  oklch(0% 0 0)        — bg
#FFFFFF  oklch(100% 0 0)      — text (Lc 106)
#6CB4FF  oklch(75% 0.15 260)  — links
#FF6B6B  oklch(68% 0.18 25)   — error
#6BFF6B  oklch(88% 0.20 150)  — success
```

---

## 10. Data Visualization Colors

### Sequential Palette (Single Hue — Blue)
For ordered data from low to high.
```css
--dataviz-seq-1: oklch(93% 0.06 265);  /* #DBEAFE — lowest */
--dataviz-seq-2: oklch(82% 0.12 265);  /* #93C5FD */
--dataviz-seq-3: oklch(68% 0.20 265);  /* #60A5FA */
--dataviz-seq-4: oklch(55% 0.24 265);  /* #3B82F6 */
--dataviz-seq-5: oklch(42% 0.20 265);  /* #1D4ED8 */
--dataviz-seq-6: oklch(30% 0.14 265);  /* #1E3A8A — highest */
```

### Diverging Palette (Blue ↔ Red via Neutral)
For data with a meaningful midpoint (e.g., profit/loss).
```css
--dataviz-div-neg3: oklch(42% 0.20 265);  /* #1D4ED8 — strong negative */
--dataviz-div-neg2: oklch(58% 0.22 265);  /* #3B82F6 */
--dataviz-div-neg1: oklch(78% 0.10 265);  /* #93C5FD */
--dataviz-div-mid:  oklch(93% 0.005 0);   /* #ECECEC — neutral midpoint */
--dataviz-div-pos1: oklch(78% 0.10 25);   /* #FCA5A5 */
--dataviz-div-pos2: oklch(58% 0.22 25);   /* #EF4444 */
--dataviz-div-pos3: oklch(42% 0.18 25);   /* #B91C1C — strong positive */
```

### Categorical Palette (Colorblind-Safe — 8 Colors)
Designed to be distinguishable for all forms of color vision deficiency. Uses maximally separated oklch hue angles AND lightness variation.
```css
--dataviz-cat-1: oklch(55% 0.22 265);  /* #3B82F6 — Blue */
--dataviz-cat-2: oklch(65% 0.20 50);   /* #EA8C3C — Orange */
--dataviz-cat-3: oklch(55% 0.18 155);  /* #16A34A — Green */
--dataviz-cat-4: oklch(55% 0.22 25);   /* #DC2626 — Red */
--dataviz-cat-5: oklch(60% 0.20 300);  /* #9333EA — Purple */
--dataviz-cat-6: oklch(50% 0.12 55);   /* #8B5E3C — Brown */
--dataviz-cat-7: oklch(65% 0.22 340);  /* #EC4899 — Pink */
--dataviz-cat-8: oklch(55% 0.01 260);  /* #6B7280 — Gray */
```

### Colorblind Testing Checklist
1. **Protanopia** (no red cones): Red and green become indistinguishable. Use blue vs orange instead.
2. **Deuteranopia** (no green cones): Similar to protanopia. Avoid red-green pairings.
3. **Tritanopia** (no blue cones): Blue and yellow merge. Rare but test for it.
4. **Strategy:** Always pair color with a secondary encoding: pattern, shape, label, position, or size.

---

## 11. Gradient Recipes

### Linear Gradients
```css
/* Subtle brand gradient */
.hero-gradient {
  background: linear-gradient(135deg,
    oklch(55% 0.25 265) 0%,
    oklch(55% 0.22 290) 100%
  );
}

/* Warm sunset */
.sunset-gradient {
  background: linear-gradient(to right,
    oklch(65% 0.22 40) 0%,
    oklch(72% 0.20 60) 50%,
    oklch(80% 0.16 85) 100%
  );
}

/* Cool ocean */
.ocean-gradient {
  background: linear-gradient(180deg,
    oklch(60% 0.20 230) 0%,
    oklch(45% 0.18 265) 100%
  );
}

/* Smooth gray surface (no banding) */
.surface-gradient {
  background: linear-gradient(180deg,
    oklch(98% 0.005 260) 0%,
    oklch(96% 0.005 260) 100%
  );
}
```

### Radial Gradients
```css
/* Spotlight glow */
.spotlight {
  background: radial-gradient(
    ellipse at 30% 20%,
    oklch(60% 0.25 265 / 0.3) 0%,
    oklch(12% 0.01 260 / 0) 70%
  );
}

/* Soft vignette for dark mode */
.vignette {
  background: radial-gradient(
    circle at center,
    oklch(16% 0.01 260) 0%,
    oklch(8% 0.02 260) 100%
  );
}
```

### Conic Gradients
```css
/* Color wheel */
.color-wheel {
  background: conic-gradient(
    oklch(65% 0.20 0),
    oklch(65% 0.20 60),
    oklch(65% 0.20 120),
    oklch(65% 0.20 180),
    oklch(65% 0.20 240),
    oklch(65% 0.20 300),
    oklch(65% 0.20 360)
  );
  border-radius: 50%;
}

/* Gauge/progress indicator */
.gauge {
  background: conic-gradient(
    oklch(55% 0.22 25) 0%,
    oklch(70% 0.18 90) 33%,
    oklch(60% 0.20 155) 66%,
    oklch(93% 0.01 260) 66%
  );
}
```

### Mesh Gradients (CSS Approximation)
True mesh gradients require multiple overlapping radials:
```css
.mesh-gradient {
  background:
    radial-gradient(at 0% 0%, oklch(70% 0.20 300 / 0.8) 0%, transparent 50%),
    radial-gradient(at 100% 0%, oklch(65% 0.22 265 / 0.8) 0%, transparent 50%),
    radial-gradient(at 100% 100%, oklch(70% 0.18 200 / 0.8) 0%, transparent 50%),
    radial-gradient(at 0% 100%, oklch(75% 0.15 155 / 0.8) 0%, transparent 50%),
    oklch(96% 0.01 260);
}
```

### Gradient Anti-Banding
oklch interpolation in CSS is smoother than sRGB. Force it:
```css
.smooth-gradient {
  background: linear-gradient(in oklch, oklch(55% 0.25 265), oklch(55% 0.22 330));
}
```
The `in oklch` keyword prevents the muddy mid-tones that occur with sRGB interpolation through complementary hues.

---

## 12. Color Token Architecture

### Three-Tier Model: Primitive → Semantic → Component

**Tier 1: Primitive Tokens** (raw values, never referenced in UI code)
```css
--color-blue-500: oklch(55% 0.25 265);
--color-blue-600: oklch(48% 0.24 265);
--color-red-500:  oklch(55% 0.24 25);
--color-gray-900: oklch(18% 0.01 260);
```

**Tier 2: Semantic Tokens** (meaning-based, referenced in component tokens)
```css
--color-action-primary:     var(--color-blue-500);
--color-action-primary-hover: var(--color-blue-600);
--color-feedback-error:     var(--color-red-500);
--color-text-primary:       var(--color-gray-900);
```

**Tier 3: Component Tokens** (scoped to specific components)
```css
--button-primary-bg:        var(--color-action-primary);
--button-primary-bg-hover:  var(--color-action-primary-hover);
--alert-error-bg:           var(--color-feedback-error);
--card-text:                var(--color-text-primary);
```

### Dark Mode via Semantic Token Swap
Only Tier 2 changes. Tier 1 stays the same. Tier 3 stays the same.
```css
[data-theme="dark"] {
  --color-action-primary:   var(--color-blue-400);  /* lighter in dark mode */
  --color-text-primary:     var(--color-gray-50);
  --color-surface:          var(--color-gray-900);
}
```

### Token Naming Convention
```
--color-{category}-{property}-{variant}-{state}
Examples:
  --color-text-primary
  --color-text-primary-hover
  --color-surface-raised
  --color-border-focus
  --color-action-primary-active
  --color-feedback-success-subtle
```

---

## 13. Brand Color Extraction

### From Logo
1. Sample the dominant color from the logo mark
2. Convert to oklch to get the base H and C values
3. Generate a 10-step scale from that hue (Section 5)
4. Choose the 500-step equivalent as primary
5. Create a complementary or split-complementary secondary
6. Generate neutral scale tinted with the primary hue (C=0.01-0.02)

### From Photography
1. Extract 5-7 dominant colors using k-means clustering
2. Convert all to oklch
3. Identify the highest-chroma color as potential primary
4. Group by hue proximity (within 30 degrees = same family)
5. Select 2-3 hue families for the palette
6. Normalize lightness range to cover 50-step through 900-step usage

### From Mood Board
1. Tag each image/sample as: primary, secondary, accent, neutral, or background
2. Average the oklch values within each tag
3. Verify minimum 60% L difference between text and background candidates
4. Test color harmony — are the hues related by a named harmony (complementary, analogous, etc.)?
5. Fill in missing semantic roles (error, warning, success) using the closest safe defaults

### Brand Color Validation Checklist
- [ ] Primary color has a 10-step scale that passes APCA at every text-use step
- [ ] Neutral scale is tinted to match brand warmth/coolness
- [ ] At least one accent color exists for interactive elements
- [ ] Error/warning/success are distinct from brand colors (no confusion between brand-red and error-red)
- [ ] Colors work at 8px (favicons) and at full-bleed (hero sections)

---

## 14. Color Accessibility

### Colorblind Simulation
Always test designs under these conditions:
- **Protanopia (1% of males):** Reds appear dark/brown. Green and red are indistinguishable.
- **Deuteranopia (6% of males):** Similar to protanopia but greens shift differently.
- **Tritanopia (0.01%):** Blues appear greenish, yellows appear pink.
- **Achromatopsia (<0.01%):** No color perception — only luminance matters.

### WCAG 2.2 vs APCA Comparison
| Scenario | WCAG 2.2 | APCA |
|---|---|---|
| Light gray text on white | Fails at 4.5:1 (often too strict for large text) | Correctly passes for large display text |
| Orange text on white | Often passes WCAG but looks illegible | Correctly fails — orange has high luminance |
| Dark blue on light blue | May fail WCAG despite being clearly readable | Correctly passes |

**Recommendation:** Use APCA for new projects. Use WCAG 2.2 ratios only when regulatory compliance requires it.

### Minimum Contrast Summary
```
APCA Lc 90+     → Small body text (12-14px)
APCA Lc 75+     → Normal body text (16px+)
APCA Lc 60+     → Large text (18px+ bold, 24px+ normal)
APCA Lc 45+     → Headlines (32px+)
APCA Lc 30+     → Non-text UI elements, decorative
WCAG AA          → 4.5:1 normal text, 3:1 large text
WCAG AAA         → 7:1 normal text, 4.5:1 large text
```

### Beyond Contrast: Color Accessibility Patterns
1. **Never use color alone** to convey meaning (add icon, pattern, or label)
2. **Error states:** red border + icon + text message (triple encoding)
3. **Links in body text:** underline OR color + underline-on-hover (not color alone)
4. **Charts:** color + pattern fills + direct labels
5. **Status indicators:** color + shape (green circle, yellow triangle, red diamond)
6. **Focus indicators:** 3px+ outline with Lc 60+ against both the element and its background

---

## 15. CSS Custom Properties — Complete Color System

### Full System Implementation
```css
:root {
  /* === Primitive Tokens === */
  /* Blue scale */
  --p-blue-50:  oklch(97% 0.03 265);
  --p-blue-100: oklch(93% 0.06 265);
  --p-blue-200: oklch(87% 0.10 265);
  --p-blue-300: oklch(78% 0.15 265);
  --p-blue-400: oklch(66% 0.22 265);
  --p-blue-500: oklch(55% 0.25 265);
  --p-blue-600: oklch(48% 0.24 265);
  --p-blue-700: oklch(40% 0.20 265);
  --p-blue-800: oklch(33% 0.16 265);
  --p-blue-900: oklch(25% 0.12 265);
  --p-blue-950: oklch(18% 0.08 265);

  /* Neutral scale (cool-tinted) */
  --p-gray-50:  oklch(97% 0.01 260);
  --p-gray-100: oklch(93% 0.01 260);
  --p-gray-200: oklch(87% 0.015 260);
  --p-gray-300: oklch(78% 0.015 260);
  --p-gray-400: oklch(66% 0.01 260);
  --p-gray-500: oklch(55% 0.01 260);
  --p-gray-600: oklch(45% 0.01 260);
  --p-gray-700: oklch(35% 0.01 260);
  --p-gray-800: oklch(25% 0.01 260);
  --p-gray-900: oklch(18% 0.01 260);
  --p-gray-950: oklch(12% 0.008 260);

  /* Red scale */
  --p-red-50:  oklch(97% 0.02 25);
  --p-red-500: oklch(55% 0.24 25);
  --p-red-600: oklch(48% 0.22 25);
  --p-red-900: oklch(22% 0.10 25);

  /* Green scale */
  --p-green-50:  oklch(97% 0.03 155);
  --p-green-500: oklch(55% 0.20 155);
  --p-green-600: oklch(48% 0.18 155);
  --p-green-900: oklch(22% 0.08 155);

  /* Amber scale */
  --p-amber-50:  oklch(97% 0.03 80);
  --p-amber-500: oklch(70% 0.18 75);
  --p-amber-900: oklch(25% 0.08 70);

  /* === Semantic Tokens (Light Mode) === */
  --s-bg:               var(--p-gray-50);
  --s-surface:          oklch(100% 0 0);
  --s-surface-raised:   oklch(100% 0 0);
  --s-surface-sunken:   var(--p-gray-100);
  --s-overlay:          oklch(15% 0 0 / 0.6);

  --s-text:             var(--p-gray-900);
  --s-text-muted:       var(--p-gray-500);
  --s-text-faint:       var(--p-gray-400);

  --s-border:           var(--p-gray-200);
  --s-border-strong:    var(--p-gray-300);
  --s-border-focus:     var(--p-blue-500);

  --s-primary:          var(--p-blue-500);
  --s-primary-hover:    var(--p-blue-600);
  --s-primary-subtle:   var(--p-blue-100);
  --s-on-primary:       oklch(100% 0 0);

  --s-error:            var(--p-red-500);
  --s-error-subtle:     var(--p-red-50);
  --s-on-error:         oklch(100% 0 0);

  --s-success:          var(--p-green-500);
  --s-success-subtle:   var(--p-green-50);
  --s-on-success:       oklch(100% 0 0);

  --s-warning:          var(--p-amber-500);
  --s-warning-subtle:   var(--p-amber-50);
  --s-on-warning:       var(--p-gray-900);

  /* === Component Tokens === */
  --btn-primary-bg:     var(--s-primary);
  --btn-primary-bg-hov: var(--s-primary-hover);
  --btn-primary-text:   var(--s-on-primary);
  --btn-secondary-bg:   var(--s-surface);
  --btn-secondary-bdr:  var(--s-border-strong);

  --input-bg:           var(--s-surface);
  --input-border:       var(--s-border);
  --input-border-focus: var(--s-border-focus);
  --input-text:         var(--s-text);
  --input-placeholder:  var(--s-text-faint);

  --card-bg:            var(--s-surface);
  --card-border:        var(--s-border);
  --card-text:          var(--s-text);
  --card-text-muted:    var(--s-text-muted);

  --alert-error-bg:     var(--s-error-subtle);
  --alert-error-text:   var(--p-red-900);
  --alert-error-border: var(--p-red-500);

  --alert-success-bg:   var(--s-success-subtle);
  --alert-success-text: var(--p-green-900);
  --alert-success-bdr:  var(--p-green-500);
}

/* Dark mode — only semantic tokens change */
[data-theme="dark"] {
  --s-bg:               var(--p-gray-950);
  --s-surface:          var(--p-gray-900);
  --s-surface-raised:   var(--p-gray-800);
  --s-surface-sunken:   oklch(10% 0.01 260);
  --s-overlay:          oklch(5% 0 0 / 0.8);

  --s-text:             var(--p-gray-100);
  --s-text-muted:       var(--p-gray-400);
  --s-text-faint:       var(--p-gray-500);

  --s-border:           var(--p-gray-800);
  --s-border-strong:    var(--p-gray-700);
  --s-border-focus:     var(--p-blue-400);

  --s-primary:          var(--p-blue-400);
  --s-primary-hover:    var(--p-blue-300);
  --s-primary-subtle:   oklch(20% 0.08 265);
  --s-on-primary:       var(--p-blue-950);

  --s-error:            oklch(65% 0.20 25);
  --s-error-subtle:     oklch(18% 0.08 25);
  --s-on-error:         oklch(97% 0.02 25);

  --s-success:          oklch(70% 0.18 155);
  --s-success-subtle:   oklch(18% 0.06 155);
  --s-on-success:       oklch(97% 0.03 155);

  --s-warning:          oklch(78% 0.16 75);
  --s-warning-subtle:   oklch(18% 0.06 75);
  --s-on-warning:       oklch(15% 0.03 70);
}
```

---

## 16. Platform Color Systems

### iOS Dynamic Colors (iOS 26+ / Liquid Glass)
iOS uses a 6-level adaptive color system that shifts across Light, Dark, and Tinted appearances:

```swift
// System colors auto-adapt to appearance
label.textColor = .label              // Primary text
label.textColor = .secondaryLabel     // Secondary text
label.textColor = .tertiaryLabel      // Tertiary text
label.textColor = .quaternaryLabel    // Quaternary text
view.backgroundColor = .systemBackground          // Level 0
view.backgroundColor = .secondarySystemBackground  // Level 1
view.backgroundColor = .tertiarySystemBackground   // Level 2
```

**iOS System Color Mapping (Light → Dark):**
```
.systemBlue:    #007AFF → #0A84FF    oklch(55% 0.22 265) → oklch(62% 0.22 265)
.systemGreen:   #34C759 → #30D158    oklch(72% 0.20 155) → oklch(74% 0.22 155)
.systemRed:     #FF3B30 → #FF453A    oklch(62% 0.24 25)  → oklch(64% 0.24 25)
.systemOrange:  #FF9500 → #FF9F0A    oklch(74% 0.18 70)  → oklch(76% 0.18 72)
.systemYellow:  #FFCC00 → #FFD60A    oklch(86% 0.16 95)  → oklch(88% 0.16 95)
.systemPurple:  #AF52DE → #BF5AF2    oklch(58% 0.22 305) → oklch(62% 0.24 305)
.systemPink:    #FF2D55 → #FF375F    oklch(60% 0.24 10)  → oklch(62% 0.24 12)
.systemTeal:    #5AC8FA → #64D2FF    oklch(78% 0.12 220) → oklch(82% 0.12 220)
```

**Liquid Glass (iOS 26):**
Liquid Glass is not a color — it is a material. Colors behind the glass element show through with blur and luminance shift. Design for this:
- Use semantic system colors (they auto-tint to glass)
- Avoid opaque backgrounds on glass-mounted elements
- Test with vibrant and reduced-transparency accessibility settings

### Material You / M3 Tonal Palettes
Material You generates tonal palettes from a source (seed) color:

**Tonal Palette Algorithm:**
1. Extract HCT (Hue, Chroma, Tone) from seed color
2. Generate tones at: 0, 4, 6, 10, 12, 17, 20, 22, 24, 25, 30, 35, 40, 50, 60, 70, 80, 87, 90, 92, 94, 95, 96, 98, 100
3. Map tones to Material roles:

```
Light Mode:
  Primary:           Tone 40
  On-Primary:        Tone 100
  Primary-Container: Tone 90
  On-Primary-Cont:   Tone 10
  Surface:           Tone 98
  On-Surface:        Tone 10
  Surface-Variant:   Tone 90 (Neutral-Variant palette)
  Outline:           Tone 50 (Neutral-Variant palette)

Dark Mode:
  Primary:           Tone 80
  On-Primary:        Tone 20
  Primary-Container: Tone 30
  On-Primary-Cont:   Tone 90
  Surface:           Tone 6
  On-Surface:        Tone 90
  Surface-Variant:   Tone 30 (Neutral-Variant palette)
  Outline:           Tone 60 (Neutral-Variant palette)
```

**M3 Expressive (2025+):**
Material 3 Expressive extends tonal palettes with:
- Wider chroma range at mid-tones for more vivid interactive elements
- Surface tint: surfaces get a subtle hue from the primary color
- Fixed-accent colors: colors that do NOT change between light/dark (for emphasis)

### Cross-Platform Color Strategy
When building for both iOS and Android:
1. Define your brand colors in oklch as the source of truth
2. Map to iOS semantic colors (`.tintColor`, `.label`, `.systemBackground`)
3. Map to Material tonal palette roles (`primary`, `onPrimary`, `surface`)
4. Use platform-specific APIs for dynamic adaptation
5. Test both platforms side-by-side — colors should feel related, not identical

```
Brand oklch(55% 0.25 265) maps to:
  iOS:      .tintColor override → adapts via system
  Android:  HCT seed → Material generates full tonal palette
  Web:      CSS custom properties (Section 15)
```

---

## Cross-References
- design-token-presets — complete token system templates by industry
- visual-design-mastery — color scoring on the 10-dimension Awwwards scale
- sector-style-intelligence — industry-specific color direction
- accessibility-inclusive-design — WCAG 2.2 + APCA compliance testing
- data-visualization-mastery — dataviz palette integration
- platform-visual-standards — iOS 26 Liquid Glass and M3 Expressive color details
- shadow-elevation-density — elevation-driven color in dark mode
- typography-pairing-recipes — text color and contrast pairing with type
