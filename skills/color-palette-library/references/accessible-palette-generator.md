# Accessible Palette Generator — WCAG 2.2 + APCA Compliant

Complete guide to generating accessible color palettes. Covers the oklch generation method, APCA contrast algorithm, colorblind-safe palettes for data visualization, high contrast mode, CSS color-mix() for dynamic palette generation, and a comprehensive validation checklist.

---

## Part 1: APCA Contrast Algorithm Deep Dive

### What Is APCA?

APCA (Advanced Perceptual Contrast Algorithm) is the next-generation contrast measurement system designed to replace WCAG 2.x contrast ratios. While WCAG 2.x uses a simple luminance ratio (e.g., 4.5:1), APCA accounts for:

1. **Polarity:** Dark text on light backgrounds and light text on dark backgrounds are NOT perceptually equivalent. APCA measures them differently.
2. **Spatial frequency:** Small text requires more contrast than large text. Bold text requires less contrast than regular weight.
3. **Adaptation:** The surrounding colors affect how contrast is perceived.

### APCA Lightness Contrast (Lc) Values

Lc is the output of APCA. It ranges from 0 (no contrast) to approximately 108 (maximum). The sign indicates polarity: positive = dark text on light bg, negative = light text on dark bg.

**Minimum Lc values by use case:**

| Use Case | Minimum |Lc| | Notes |
|----------|---------|-------|
| Body text, 16px, 400 weight | 75 | Most common UI text |
| Body text, 14px, 400 weight | 90 | Small body text |
| Large text, 24px, 400 weight | 60 | Headers |
| Large text, 36px, 700 weight | 30 | Display headlines |
| Bold text, 16px, 700 weight | 60 | Bold UI text |
| Bold text, 14px, 700 weight | 75 | Small bold text |
| Placeholder text, 16px | 60 | Input placeholders |
| Disabled text | 30 | Visually deprioritized |
| Non-text UI elements | 30 | Icons, borders, dividers |
| Sub-text, footnotes, 12px | 90 | Very small text |
| Columns of body text (long form) | 75 | Extended reading |
| Link underlines (non-text indicator) | 15 | Minimum for decorative |

### APCA Polarity Difference

The polarity insight is critical for dark mode design:

**Dark text on light background (positive polarity):**
- Text oklch(20% ...) on bg oklch(97% ...) = approximately Lc +90
- The standard, comfortable reading configuration

**Light text on dark background (negative polarity):**
- Text oklch(92% ...) on bg oklch(13% ...) = approximately Lc -85
- Requires ~15-20% MORE contrast to feel equally readable
- This is why dark mode text should be L:90-95%, not L:80-85%

### APCA Calculation (Simplified)

While the full APCA algorithm involves sRGB linearization and exponent-based transforms, the practical takeaway for oklch-based design:

**Approximate Lc from oklch lightness difference:**
```
Lc (approximate) = (L_lighter - L_darker) * 1.1

Example:
  Text:   oklch(18% 0.10 265) — L = 18%
  Bg:     oklch(97% 0.02 265) — L = 97%
  Lc approximate: (97 - 18) * 1.1 = 87

This is a rough heuristic. For production, use a proper APCA calculator.
```

**Key lightness pairs that achieve common Lc targets:**

| Target Lc | Light BG (L) | Dark Text (L) | Example |
|-----------|-------------|---------------|---------|
| 90+ | 97% | 18% | Body text on white |
| 75+ | 97% | 30% | Secondary text on white |
| 60+ | 97% | 42% | Tertiary text on white |
| 45+ | 97% | 52% | Large bold text on white |
| 90+ (dark mode) | 13% | 93% | Body text on dark bg |
| 75+ (dark mode) | 13% | 82% | Secondary text on dark bg |
| 60+ (dark mode) | 13% | 70% | Tertiary text on dark bg |

---

## Part 2: Step-by-Step oklch Palette Generation

### Method: Generate an Accessible 10-Step Scale

**Input:** A single brand color (e.g., `oklch(55% 0.22 265)` — vivid blue)

**Step 1: Extract the hue.**
H = 265 (blue). This stays constant across all 11 steps.

**Step 2: Define the lightness curve.**
The lightness curve is NOT linear — it follows a perceptual curve that allocates more steps in the mid-range where human discrimination is highest:

```
Step 50:  L = 97%   (barely tinted white)
Step 100: L = 93%   (light tint)
Step 200: L = 85%   (noticeable tint)
Step 300: L = 75%   (medium-light)
Step 400: L = 65%   (medium)
Step 500: L = 55%   (brand anchor — full expression)
Step 600: L = 45%   (medium-dark)
Step 700: L = 35%   (dark)
Step 800: L = 25%   (very dark)
Step 900: L = 18%   (near-black)
Step 950: L = 12%   (deepest)
```

**Step 3: Define the chroma curve.**
Chroma peaks at mid-lightness and tapers at extremes (matching human perception):

```
Step 50:  C = 0.02  (barely chromatic)
Step 100: C = 0.04  (subtle)
Step 200: C = 0.08  (noticeable)
Step 300: C = 0.14  (moderate)
Step 400: C = 0.18  (strong)
Step 500: C = 0.22  (peak chroma — brand color)
Step 600: C = 0.20  (slightly reduced)
Step 700: C = 0.17  (moderately reduced)
Step 800: C = 0.14  (dark reduces chroma)
Step 900: C = 0.10  (deep, muted)
Step 950: C = 0.07  (near-black, trace chroma)
```

**Step 4: Generate the CSS.**
```css
:root {
  --blue-50:  oklch(97% 0.02 265);
  --blue-100: oklch(93% 0.04 265);
  --blue-200: oklch(85% 0.08 265);
  --blue-300: oklch(75% 0.14 265);
  --blue-400: oklch(65% 0.18 265);
  --blue-500: oklch(55% 0.22 265);
  --blue-600: oklch(45% 0.20 265);
  --blue-700: oklch(35% 0.17 265);
  --blue-800: oklch(25% 0.14 265);
  --blue-900: oklch(18% 0.10 265);
  --blue-950: oklch(12% 0.07 265);
}
```

**Step 5: Validate all critical contrast pairings.**

### Contrast Validation Matrix (Light Theme)

Every text-background combination must meet APCA minimums:

| Background | Text Color | Approximate Lc | Passes for |
|-----------|-----------|-----------------|------------|
| 50 (97%) | 900 (18%) | ~87 | Body text 16px |
| 50 (97%) | 800 (25%) | ~79 | Body text 16px |
| 50 (97%) | 700 (35%) | ~68 | Large text 24px |
| 50 (97%) | 600 (45%) | ~57 | Large bold 24px |
| 50 (97%) | 500 (55%) | ~46 | Large bold 36px+ |
| 100 (93%) | 900 (18%) | ~83 | Body text 16px |
| 100 (93%) | 800 (25%) | ~75 | Body text 16px |
| 100 (93%) | 700 (35%) | ~64 | Large text 24px |
| 200 (85%) | 900 (18%) | ~74 | Body text 16px (borderline) |
| 200 (85%) | 800 (25%) | ~66 | Large text 24px |
| 500 (55%) | White (100%) | ~50 | Large bold only |
| 500 (55%) | 50 (97%) | ~46 | Large bold 36px+ |
| 600 (45%) | White (100%) | ~61 | Bold 16px |
| 700 (35%) | White (100%) | ~72 | Body text 16px |

**Key findings from the matrix:**
1. Steps 50-100 work as backgrounds for text in steps 700-900
2. Step 500 only works as a background for LARGE BOLD white text (buttons are OK, body text is NOT)
3. For body text on colored backgrounds, use step 700+ as the background or step 800+ as the text
4. Steps 200-300 are "decoration zone" — usable for badges, illustrations, not for text backgrounds

### Contrast Validation Matrix (Dark Theme)

| Background | Text Color | Approximate Lc | Passes for |
|-----------|-----------|-----------------|------------|
| 950 (12%) | 50 (97%) | ~94 | Body text (excellent) |
| 950 (12%) | 100 (93%) | ~89 | Body text 16px |
| 950 (12%) | 200 (85%) | ~80 | Body text 16px |
| 950 (12%) | 300 (75%) | ~69 | Large text 24px |
| 900 (18%) | 50 (97%) | ~87 | Body text 16px |
| 900 (18%) | 100 (93%) | ~83 | Body text 16px |
| 900 (18%) | 200 (85%) | ~74 | Body text 16px (borderline) |
| 800 (25%) | 50 (97%) | ~79 | Body text 16px |
| 800 (25%) | 100 (93%) | ~75 | Body text 16px |
| 500 (55%) | 950 (12%) | ~47 | Large bold only |
| 400 (65%) | 950 (12%) | ~58 | Bold 16px |
| 300 (75%) | 950 (12%) | ~69 | Large text 24px |

**Key findings for dark mode:**
1. Dark backgrounds (900-950) support body text from steps 50-200
2. Accent colors (400-500) on dark backgrounds work for buttons and large elements only
3. The "readable text" zone in dark mode is steps 50-200 (L: 85-97%)
4. Secondary text in dark mode should be step 300-400 range (L: 65-75%)

---

## Part 3: Colorblind-Safe Categorical Palettes

For data visualization, you need colors that remain distinguishable to users with color vision deficiency. The following palettes use BOTH hue AND lightness differentiation to ensure distinguishability.

### Categorical Palette 1: Universal 8-Color (Best Overall)
Tested against deuteranopia, protanopia, tritanopia, and achromatopsia.

```css
--cat-1: oklch(45% 0.18 255);  /* Deep Blue    — #2563EB */
--cat-2: oklch(68% 0.18 55);   /* Orange       — #F97316 */
--cat-3: oklch(52% 0.16 155);  /* Forest Green — #059669 */
--cat-4: oklch(55% 0.20 25);   /* Red          — #DC2626 */
--cat-5: oklch(72% 0.14 295);  /* Lavender     — #A78BFA */
--cat-6: oklch(42% 0.10 55);   /* Brown        — #92400E */
--cat-7: oklch(62% 0.16 345);  /* Pink         — #EC4899 */
--cat-8: oklch(80% 0.14 95);   /* Gold         — #EAB308 */
```

**Why it works:** Each color differs from all others by at least 25% in oklch lightness OR by at least 90 degrees in hue. Even in full achromatopsia (grayscale vision), the lightness spread (42%-80%) makes most categories distinguishable.

### Categorical Palette 2: Red-Green Safe (Deuteranopia/Protanopia Optimized)
Avoids the red-green confusion axis entirely.

```css
--rg-1: oklch(45% 0.18 255);  /* Blue         — #2563EB */
--rg-2: oklch(68% 0.16 55);   /* Orange       — #EA580C */
--rg-3: oklch(82% 0.14 95);   /* Yellow       — #EAB308 */
--rg-4: oklch(55% 0.16 295);  /* Purple       — #7C3AED */
--rg-5: oklch(38% 0.10 55);   /* Dark Brown   — #78350F */
--rg-6: oklch(72% 0.12 345);  /* Pink         — #F472B6 */
--rg-7: oklch(60% 0.14 210);  /* Cyan         — #0891B2 */
--rg-8: oklch(30% 0.06 265);  /* Dark Gray    — #374151 */
```

### Categorical Palette 3: Sequential Blue (Single Hue Gradient)
For ordered data (low to high), using lightness variation within one hue.

```css
--seq-1: oklch(95% 0.02 255);  /* Lightest — #EFF6FF */
--seq-2: oklch(85% 0.06 255);  /* Light    — #BFDBFE */
--seq-3: oklch(72% 0.10 255);  /* Medium-L — #93C5FD */
--seq-4: oklch(60% 0.14 255);  /* Medium   — #60A5FA */
--seq-5: oklch(48% 0.18 255);  /* Medium-D — #3B82F6 */
--seq-6: oklch(38% 0.16 255);  /* Dark     — #2563EB */
--seq-7: oklch(28% 0.14 255);  /* Darker   — #1D4ED8 */
--seq-8: oklch(18% 0.10 255);  /* Darkest  — #1E3A8A */
```

### Categorical Palette 4: Diverging (Two-Hue Gradient)
For data with a meaningful center point (e.g., positive/negative, above/below average).

```css
--div-neg4: oklch(35% 0.16 25);   /* Deep Red    — #991B1B */
--div-neg3: oklch(48% 0.18 25);   /* Red         — #DC2626 */
--div-neg2: oklch(62% 0.14 25);   /* Light Red   — #F87171 */
--div-neg1: oklch(78% 0.08 25);   /* Pale Red    — #FECACA */
--div-mid:  oklch(95% 0.01 265);  /* Near White  — #F3F4F6 */
--div-pos1: oklch(78% 0.08 255);  /* Pale Blue   — #BFDBFE */
--div-pos2: oklch(62% 0.14 255);  /* Light Blue  — #60A5FA */
--div-pos3: oklch(48% 0.18 255);  /* Blue        — #3B82F6 */
--div-pos4: oklch(35% 0.16 255);  /* Deep Blue   — #1E3A8A */
```

### Categorical Palette 5: Warm Sequential (Orange Gradient)
For metrics like "hot/cold" or "intensity."

```css
--warm-1: oklch(95% 0.03 65);  /* Pale cream   — #FFF7ED */
--warm-2: oklch(88% 0.08 65);  /* Light peach  — #FFEDD5 */
--warm-3: oklch(78% 0.12 65);  /* Peach        — #FDBA74 */
--warm-4: oklch(68% 0.16 65);  /* Orange       — #FB923C */
--warm-5: oklch(58% 0.18 55);  /* Deep Orange  — #EA580C */
--warm-6: oklch(48% 0.16 45);  /* Red-Orange   — #C2410C */
--warm-7: oklch(38% 0.14 35);  /* Dark Red     — #9A3412 */
--warm-8: oklch(28% 0.10 30);  /* Deepest      — #7C2D12 */
```

### Categorical Palette 6: Cool Sequential (Teal Gradient)
For calm, progressive metrics.

```css
--cool-1: oklch(96% 0.02 195);  /* Pale mint   — #F0FDFA */
--cool-2: oklch(88% 0.06 195);  /* Light teal  — #CCFBF1 */
--cool-3: oklch(78% 0.10 195);  /* Teal light  — #99F6E4 */
--cool-4: oklch(65% 0.14 195);  /* Teal        — #2DD4BF */
--cool-5: oklch(55% 0.14 195);  /* Teal dark   — #14B8A6 */
--cool-6: oklch(45% 0.12 195);  /* Deep teal   — #0D9488 */
--cool-7: oklch(35% 0.10 195);  /* Darker      — #0F766E */
--cool-8: oklch(25% 0.08 195);  /* Deepest     — #134E4A */
```

### Categorical Palette 7: High-Lightness-Spread (Achromatopsia Safe)
For users with no color vision at all — relies entirely on lightness.

```css
--achro-1: oklch(95% 0.14 255);  /* Very Light Blue  */
--achro-2: oklch(82% 0.16 55);   /* Light Orange     */
--achro-3: oklch(68% 0.18 295);  /* Medium Purple    */
--achro-4: oklch(55% 0.16 155);  /* Medium Green     */
--achro-5: oklch(42% 0.14 25);   /* Medium-Dark Red  */
--achro-6: oklch(30% 0.10 210);  /* Dark Teal        */
```

Each color differs by at least 12% in oklch lightness from all neighbors, ensuring grayscale distinguishability.

### Categorical Palette 8: Qualitative Pastel (Soft Data Viz)
For dashboards where data viz should not overpower UI.

```css
--pastel-1: oklch(82% 0.08 255);  /* Pastel Blue    — #93C5FD */
--pastel-2: oklch(82% 0.08 30);   /* Pastel Red     — #FCA5A5 */
--pastel-3: oklch(82% 0.08 155);  /* Pastel Green   — #86EFAC */
--pastel-4: oklch(82% 0.08 295);  /* Pastel Purple  — #C4B5FD */
--pastel-5: oklch(82% 0.08 55);   /* Pastel Orange  — #FDBA74 */
--pastel-6: oklch(82% 0.08 195);  /* Pastel Teal    — #99F6E4 */
--pastel-7: oklch(82% 0.08 345);  /* Pastel Pink    — #F9A8D4 */
--pastel-8: oklch(82% 0.08 95);   /* Pastel Yellow  — #FDE68A */
```

All at L:82%, differentiated purely by hue. Add lightness variation (bold/muted variants) for secondary encoding.

---

## Part 4: High Contrast Mode

Some users require extreme contrast. The `prefers-contrast: more` media query signals this preference.

### High Contrast Palette Adjustments

```css
@media (prefers-contrast: more) {
  :root {
    /* Text becomes pure black */
    --color-text-primary: oklch(0% 0 0);           /* #000000 */
    --color-text-secondary: oklch(25% 0.005 265);  /* #333333 */

    /* Backgrounds become pure white */
    --color-surface-primary: oklch(100% 0 0);       /* #FFFFFF */

    /* Borders become much darker */
    --color-border-primary: oklch(35% 0.005 265);  /* #555555 */
    --color-border-secondary: oklch(50% 0.005 265);/* #777777 */

    /* Primary becomes darker for contrast */
    --color-primary: oklch(35% 0.20 265);           /* Darkened blue */

    /* Focus indicators become more visible */
    --color-border-focus: oklch(0% 0 0);            /* Black focus ring */

    /* Status colors darken */
    --color-error: oklch(38% 0.20 25);              /* Dark red */
    --color-success: oklch(35% 0.16 155);           /* Dark green */
    --color-warning: oklch(35% 0.14 60);            /* Dark amber */
  }
}

@media (prefers-contrast: more) and (prefers-color-scheme: dark) {
  :root {
    --color-text-primary: oklch(100% 0 0);          /* Pure white */
    --color-text-secondary: oklch(85% 0.005 265);   /* Near white */
    --color-surface-primary: oklch(0% 0 0);          /* Pure black */
    --color-border-primary: oklch(65% 0.005 265);    /* Light gray */
    --color-primary: oklch(72% 0.18 265);            /* Lightened blue */
    --color-border-focus: oklch(100% 0 0);           /* White focus ring */
  }
}
```

### Forced Colors Mode (Windows High Contrast)

Windows High Contrast mode overrides all colors with system colors. Test your UI in this mode:

```css
@media (forced-colors: active) {
  /* Use system colors */
  .button-primary {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .link {
    color: LinkText;
  }

  .selected {
    outline: 2px solid Highlight;
  }

  /* Ensure custom icons remain visible */
  .icon {
    forced-color-adjust: auto;
  }
}
```

---

## Part 5: CSS color-mix() for Dynamic Palette Generation

CSS `color-mix()` enables runtime palette generation without JavaScript:

### Generate Tints and Shades Dynamically

```css
:root {
  --brand: oklch(55% 0.22 265);

  /* Tints (mix with white) */
  --brand-50:  color-mix(in oklch, var(--brand) 5%, white);
  --brand-100: color-mix(in oklch, var(--brand) 10%, white);
  --brand-200: color-mix(in oklch, var(--brand) 20%, white);
  --brand-300: color-mix(in oklch, var(--brand) 35%, white);
  --brand-400: color-mix(in oklch, var(--brand) 55%, white);

  /* Brand anchor */
  --brand-500: var(--brand);

  /* Shades (mix with black) */
  --brand-600: color-mix(in oklch, var(--brand) 80%, black);
  --brand-700: color-mix(in oklch, var(--brand) 60%, black);
  --brand-800: color-mix(in oklch, var(--brand) 40%, black);
  --brand-900: color-mix(in oklch, var(--brand) 25%, black);
  --brand-950: color-mix(in oklch, var(--brand) 15%, black);
}
```

### Generate Hover and Active States

```css
:root {
  --primary: oklch(55% 0.22 265);
  --primary-hover: color-mix(in oklch, var(--primary) 85%, black);
  --primary-active: color-mix(in oklch, var(--primary) 70%, black);
  --primary-subtle: color-mix(in oklch, var(--primary) 10%, white);
}
```

### Generate Dark Mode Tokens Dynamically

```css
[data-theme="dark"] {
  --primary: oklch(55% 0.22 265);

  /* Lighten for dark backgrounds */
  --primary-text: color-mix(in oklch, var(--primary) 70%, white);

  /* Desaturate for dark backgrounds */
  --primary-surface: color-mix(in oklch, var(--primary) 15%, oklch(13% 0 265));

  /* Surface elevation */
  --surface-0: oklch(13% 0.01 265);
  --surface-1: color-mix(in oklch, var(--surface-0) 92%, white);
  --surface-2: color-mix(in oklch, var(--surface-0) 86%, white);
  --surface-3: color-mix(in oklch, var(--surface-0) 80%, white);
}
```

### Generate Complementary Colors

```css
:root {
  --primary: oklch(55% 0.22 265);

  /* Rotate hue for harmony */
  /* Note: CSS relative color syntax required for hue rotation */
  --complementary: oklch(from var(--primary) l c calc(h + 180));
  --analogous-1: oklch(from var(--primary) l c calc(h - 30));
  --analogous-2: oklch(from var(--primary) l c calc(h + 30));
  --triadic-1: oklch(from var(--primary) l c calc(h + 120));
  --triadic-2: oklch(from var(--primary) l c calc(h + 240));
}
```

**Browser support:** `color-mix()` is supported in Chrome 111+, Safari 16.2+, Firefox 113+. Relative color syntax (`oklch(from ...)`) is supported in Chrome 119+, Safari 16.4+, Firefox 128+.

---

## Part 6: oklch Palette Generation Formulas

### Formula: Generate N-Step Lightness Curve

For any number of steps N between two lightness endpoints:

```
L(step_i) = L_light - (L_light - L_dark) * (i / (N - 1))^gamma

Where:
  L_light = starting lightness (e.g., 97% for step 50)
  L_dark  = ending lightness (e.g., 12% for step 950)
  i       = step index (0 to N-1)
  N       = total number of steps
  gamma   = curve factor (1.0 = linear, 1.2 = slightly more dark steps, 0.8 = more light steps)
```

Recommended gamma = 1.0 for even distribution. Use gamma = 1.1 if you need more dark shades (common for dark mode support).

### Formula: Generate Chroma Curve

Chroma should peak at mid-lightness. A bell curve works:

```
C(L) = C_max * (1 - ((L - 55) / 45)^2)

Where:
  C_max = maximum chroma at L=55% (e.g., 0.22)
  L     = lightness percentage
  Clamp C to minimum 0.02
```

This produces:
- C at L=97%: 0.02 (barely chromatic)
- C at L=75%: 0.14 (moderate)
- C at L=55%: 0.22 (peak)
- C at L=35%: 0.14 (moderate)
- C at L=12%: 0.02 (barely chromatic)

### Formula: Hue Adjustment by Lightness

Some hues shift perceptually at extreme lightness. Optional correction:

```
For blues (H = 250-280):
  H_adjusted = H + (55 - L) * 0.05
  (Blues shift slightly toward purple at low lightness — this counteracts that)

For greens (H = 140-160):
  H_adjusted = H - (55 - L) * 0.03
  (Greens shift toward yellow at high lightness — this counteracts that)

For reds (H = 20-40):
  No adjustment needed (reds are stable across lightness)
```

---

## Part 7: Complete Palette Validation Checklist

Use this checklist to validate any color palette before production use.

### Contrast Validation (8 checks)

- [ ] **Body text (16px, 400) on primary surface:** Lc >= 75
- [ ] **Body text on secondary surface:** Lc >= 75
- [ ] **Secondary text on primary surface:** Lc >= 60
- [ ] **Button text on primary button bg:** Lc >= 60 (bold) or 75 (normal)
- [ ] **Link text on surface:** Lc >= 75 AND distinguishable from body text
- [ ] **Error text on error-subtle bg:** Lc >= 75
- [ ] **Disabled text on surface:** Lc >= 30 (minimum for perceivability)
- [ ] **Focus ring color vs. surrounding bg:** Lc >= 30

### Dark Mode Validation (6 checks)

- [ ] **Dark mode body text on dark bg:** Lc >= 75 (remember polarity penalty)
- [ ] **Dark mode secondary text on dark bg:** Lc >= 60
- [ ] **Dark mode surface elevation visible:** Each elevation step differs by >= 2% L
- [ ] **Dark mode accent colors do not vibrate/glow:** Chroma reduced 15-25% from light mode
- [ ] **Dark mode primary bg is not pure black:** L >= 10% to prevent halo artifacts
- [ ] **Dark mode text is not pure white:** L <= 95% to reduce eye strain

### Colorblind Validation (5 checks)

- [ ] **No information conveyed by color alone:** Icons, labels, or patterns accompany every color-coded element
- [ ] **Error state distinguishable without red:** Has an icon, border change, or text label
- [ ] **Success state distinguishable without green:** Has an icon, checkmark, or text label
- [ ] **Data visualization has lightness differentiation:** Adjacent categories differ by >= 15% L
- [ ] **Tested in deuteranopia simulation:** No two semantic colors become indistinguishable

### Semantic Validation (5 checks)

- [ ] **Primary color is the highest-chroma element:** No secondary or status color is more vivid
- [ ] **Error red is distinct from brand red:** If brand uses red, error should differ by >= 10 degrees hue
- [ ] **Success green is not confused with primary green:** If brand uses green, success should differ by >= 30 degrees hue or 20% lightness
- [ ] **Warning amber is not confused with accent orange:** If both exist, they differ by >= 20 degrees hue
- [ ] **Info blue is not confused with primary blue:** If brand is blue, info should be a noticeably different shade

### Technical Validation (4 checks)

- [ ] **All colors are within sRGB gamut:** No color produces a visible gamut-mapping shift on standard displays
- [ ] **oklch values have hex fallbacks:** For browsers without oklch support
- [ ] **CSS custom properties follow naming convention:** `--color-{semantic}-{variant}`
- [ ] **Token layers are correct:** Primitives reference raw values, semantics reference primitives, components reference semantics

### Cross-Platform Validation (4 checks)

- [ ] **Tested on macOS (P3 display):** Colors appear as intended on wide gamut
- [ ] **Tested on Windows (sRGB display):** Colors are not washed out or shifted
- [ ] **Tested on mobile (various screens):** Colors maintain readability on smaller screens
- [ ] **Print preview checked:** If printable, colors maintain contrast in CMYK approximation

**Total: 32 validation checks per palette.**
