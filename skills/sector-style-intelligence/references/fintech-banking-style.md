# Fintech & Banking — Sector Style Intelligence

## Sector Overview

Fintech design sits at the intersection of trust, precision, and approachability. Users are entrusting you with their money — every visual decision either reinforces or erodes that trust. The best fintech products achieve a paradox: they feel simultaneously professional enough to trust with life savings and approachable enough that a first-time investor does not feel intimidated. This tension drives every design decision from color palette to border radius.

The sector has evolved through three distinct eras: the legacy banking aesthetic (conservative blues, serif typography, heavy chrome), the fintech disruption era (bold gradients, card-centric design, gamified investing), and the current mature fintech aesthetic (refined minimalism, data-rich but calm, editorial influence). Understanding where your product sits on this spectrum determines your visual direction.

---

## Color Psychology

### What Colors Mean in Fintech

| Color | Association | Usage | Risk |
|---|---|---|---|
| **Blue** | Trust, stability, security | Primary brand, navigation, CTAs | Overused — can feel generic |
| **Green** | Growth, profit, positive change | Gains, success states, confirmations | Must distinguish from "go" in traffic-light patterns |
| **Red** | Loss, decline, urgency | Losses, errors, destructive actions | Can trigger anxiety if overused |
| **Purple** | Premium, innovation, crypto | Fintech disruptors, crypto platforms | Can feel unserious for traditional banking |
| **Black/Dark** | Sophistication, premium tier | Premium cards, dark mode, pro tiers | Can feel intimidating for mass-market |
| **White/Light Gray** | Clarity, transparency, openness | Backgrounds, data containers | Can feel sterile without warm accents |

### Palettes from Leading Apps

#### Stripe
```
Primary Blue:      #635BFF (Stripe Purple — distinctive, breaks blue convention)
Dark Background:   #0A2540 (Deep navy — editorial sophistication)
Accent Green:      #00D4AA (Teal-green — modern, fresh)
Text Primary:      #425466 (Warm gray — softer than pure black)
Text Secondary:    #697386 (Mid gray)
Surface:           #F6F9FC (Cool off-white)
White:             #FFFFFF
Error Red:         #DF1B41
Success Green:     #30B130
Warning Amber:     #F5BE3B
```
**Why it works:** Stripe's palette breaks the expected blue-trust convention with a distinctive purple that signals innovation. The deep navy background adds editorial gravitas. The warm gray text prevents the clinical coldness common in fintech.

#### Cash App
```
Primary Green:     #00D632 (Cash App Green — bold, distinctive)
Dark Background:   #000000 (Pure black — bold, youth-oriented)
White:             #FFFFFF
Light Gray:        #F5F5F5
Text Primary:      #FFFFFF (on dark) / #000000 (on light)
Accent:            #00C244
Surface Card:      #1A1A1A (Dark mode cards)
```
**Why it works:** Cash App's neon green on black creates immediate visual distinction. The high contrast palette signals confidence and youthful energy while the limited palette maintains clarity.

#### Robinhood
```
Primary Green:     #00C805 (Robinhood Green — optimism, growth)
Dark Background:   #1E2124 (Dark charcoal)
White:             #FFFFFF
Text Primary:      #1E2124
Text Secondary:    #9DA0A5
Positive:          #00C805 (Green — gains)
Negative:          #FF5252 (Red — losses)
Chart Line:        #00C805
Surface:           #F7F7F7
```
**Why it works:** The single dominant green communicates the core brand promise — growth and accessibility. The red/green binary is immediately readable for portfolio performance.

#### Wise (TransferWise)
```
Primary Green:     #9FE870 (Lime green — fresh, approachable)
Dark Blue:         #163300 (Deep forest — grounding)
Secondary Blue:    #2E4057
Light Background:  #F2F5E9 (Warm off-white — organic feel)
Text Primary:      #163300
Accent Yellow:     #FFEB3B
Surface:           #FFFFFF
```
**Why it works:** Wise's lime green feels energetic and fresh, signaling a modern alternative to traditional banking. The warm off-white prevents clinical coldness.

#### Revolut
```
Primary Blue:      #0666EB (Strong blue — trust)
Dark Background:   #191C20 (Near black)
Accent Purple:     #8B5CF6
Light Background:  #F5F5F5
Text Primary:      #191C20
Text Secondary:    #6B7280
Premium Gold:      #C9A84C (Metal card tier)
Surface Card:      #FFFFFF
```

#### Mercury
```
Primary Purple:    #6E56CF (Soft purple — modern banking)
Dark Background:   #121217 (Near black)
Light Background:  #FAFAFA
Text Primary:      #1A1523 (Near black, warm)
Text Secondary:    #6F6E77
Border:            #E4E2E4
Surface:           #FFFFFF
Accent:            #8E4EC6
```

---

## Typography Norms

### Font Choices Across Leading Apps

| App | Primary Font | Numeric Font | Why |
|---|---|---|---|
| **Stripe** | Inter, custom "Stripe Roobert" | Tabular numerals (Inter) | Geometric precision, excellent at small sizes, tabular figures for data alignment |
| **Cash App** | Cash Market (custom), SF Pro | SF Mono for amounts | Bold, distinctive custom font for brand; system font for readability |
| **Robinhood** | Capsule Sans (custom), SF Pro | Tabular figures | Custom font for brand, system font for performance |
| **Wise** | DM Sans, system stack | Tabular numerals | Open-source, accessible, clean geometric sans-serif |
| **Revolut** | Revolut Custom, Inter | Tabular figures | Custom display font for brand moments, Inter for UI |
| **Mercury** | GT America, Inter | GT America Mono | Premium geometric sans, monospace for financial data |

### Typography Rules for Fintech

1. **Always use tabular (monospaced) figures for financial data.** Numbers must align vertically in columns. Use `font-variant-numeric: tabular-nums;` or a font with tabular figures as default.

2. **Large monetary amounts use a heavier weight.** Balance amounts are typically 28-48px, font-weight 600-700. This creates hierarchy and instant scannability.

3. **Body text stays 14-16px.** Fintech apps are data-dense; body text below 14px becomes unreadable at the density required. 16px for mobile, 14px acceptable for desktop data tables.

4. **Use a clear type scale with limited steps.**
```
Display:    48px / 700 weight / -0.02em tracking
Heading 1:  32px / 600 weight / -0.01em tracking
Heading 2:  24px / 600 weight / -0.01em tracking
Heading 3:  20px / 600 weight / 0 tracking
Body:       16px / 400 weight / 0 tracking
Body Small: 14px / 400 weight / 0 tracking
Caption:    12px / 500 weight / 0.02em tracking
Overline:   11px / 600 weight / 0.08em tracking / uppercase
Mono Data:  14px / 500 weight / 0 tracking / monospace
```

5. **Negative tracking on large text, positive on small caps.** Large display text benefits from -0.02em tightening. Overlines and labels use +0.05-0.08em for legibility at small sizes.

---

## Component Conventions

### Border Radius

Fintech apps tend toward sharp to moderately rounded corners. Excessively rounded corners feel playful and can undermine trust.

```
Buttons:         8px  (moderate — professional but not harsh)
Cards:           12px (slightly softer — content containers)
Input Fields:    8px  (matches buttons for visual consistency)
Modals:          16px (slightly softer for overlay contexts)
Avatars:         50%  (circular — universal convention)
Chips/Tags:      6px  (compact, data-dense elements)
Bottom Sheets:   20px top-left, top-right (mobile convention)
Tooltips:        8px
```

**Stripe exception:** Stripe uses 8-12px consistently. No element exceeds 16px radius.
**Cash App exception:** Cash App uses larger radii (16-24px) to match its younger, bolder aesthetic.

### Elevation & Shadow

Fintech prefers subtle, functional elevation over decorative shadows.

```css
/* Level 0 — Flat (default) */
box-shadow: none;
border: 1px solid #E4E7EC;

/* Level 1 — Subtle lift (cards, dropdowns) */
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);

/* Level 2 — Moderate (popovers, floating actions) */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.04);

/* Level 3 — Prominent (modals, command palettes) */
box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12), 0 4px 12px rgba(0, 0, 0, 0.06);

/* Level 4 — Maximum (onboarding overlays, critical dialogs) */
box-shadow: 0 24px 64px rgba(0, 0, 0, 0.16), 0 8px 20px rgba(0, 0, 0, 0.08);
```

**Key principle:** Most fintech surfaces are flat (Level 0) with subtle borders. Elevation is reserved for interactive overlays and temporary surfaces.

### Card Styles

```css
/* Standard Data Card */
.card-data {
  background: #FFFFFF;
  border: 1px solid #E4E7EC;
  border-radius: 12px;
  padding: 20px;
  transition: border-color 0.15s ease;
}
.card-data:hover {
  border-color: #C4C9D2;
}

/* Account Balance Card */
.card-balance {
  background: linear-gradient(135deg, #0A2540 0%, #1B3A5C 100%);
  border-radius: 12px;
  padding: 24px;
  color: #FFFFFF;
}

/* Transaction Row */
.transaction-row {
  padding: 16px 20px;
  border-bottom: 1px solid #F1F3F5;
  display: flex;
  align-items: center;
  gap: 12px;
}
```

### Button Styles

```css
/* Primary CTA */
.btn-primary {
  background: #635BFF; /* or sector-appropriate primary */
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 15px;
  font-weight: 600;
  height: 44px;
  min-width: 120px;
  transition: background 0.15s ease, transform 0.1s ease;
}
.btn-primary:hover {
  background: #5548E5;
}
.btn-primary:active {
  transform: scale(0.98);
}

/* Secondary / Ghost */
.btn-secondary {
  background: transparent;
  color: #425466;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 15px;
  font-weight: 500;
  height: 44px;
}

/* Destructive */
.btn-destructive {
  background: #FEF2F2;
  color: #DC2626;
  border: 1px solid #FCA5A5;
  border-radius: 8px;
  padding: 12px 24px;
  font-weight: 600;
  height: 44px;
}
```

### Data Table Conventions

```css
.table-financial {
  width: 100%;
  border-collapse: collapse;
  font-variant-numeric: tabular-nums;
}
.table-financial th {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #6B7280;
  padding: 12px 16px;
  border-bottom: 2px solid #E5E7EB;
  text-align: left;
}
.table-financial td {
  font-size: 14px;
  padding: 14px 16px;
  border-bottom: 1px solid #F3F4F6;
  color: #111827;
}
.table-financial td.amount {
  font-family: 'Inter', monospace;
  font-weight: 500;
  text-align: right;
}
.table-financial td.positive {
  color: #059669;
}
.table-financial td.negative {
  color: #DC2626;
}
```

---

## Spacing Philosophy

Fintech apps balance data density with breathing room. Too sparse wastes screen real estate needed for financial data. Too dense overwhelms users making consequential financial decisions.

### Spacing Scale

```
4px   — Micro spacing (icon-to-label, inline elements)
8px   — Tight spacing (related elements, compact lists)
12px  — Default inner padding (within compact components)
16px  — Standard gap (between related elements)
20px  — Card inner padding (primary content containers)
24px  — Section gap (between related sections)
32px  — Major section gap (between distinct content areas)
48px  — Page section dividers
64px  — Major page sections (desktop)
```

### Density Modes

Fintech products often offer density controls:

```
Compact:   Row height 36px, padding 8px 12px, font 13px
Default:   Row height 48px, padding 12px 16px, font 14px
Spacious:  Row height 56px, padding 16px 20px, font 15px
```

### Dashboard Layout Spacing

```
Sidebar width:        240px (collapsed: 64px)
Top nav height:       56px
Content max-width:    1200px
Card grid gap:        16px (mobile) / 24px (desktop)
Section title margin: 0 0 16px 0
Page padding:         24px (mobile) / 32px (tablet) / 48px (desktop)
```

---

## Motion Personality

Fintech motion is **precise, quick, and functional.** Animations exist to provide feedback, not to entertain. Users making financial decisions want responsiveness, not whimsy.

### Timing

```
Micro-interaction:    100-150ms  (button press, toggle, checkbox)
State transition:     200-250ms  (card expand, tab switch, filter)
Page transition:      300-350ms  (navigation, modal open)
Data refresh:         150ms      (chart update, balance change)
Celebration:          400-600ms  (successful transfer, rare and restrained)
```

### Easing Curves

```css
/* Standard ease — most interactions */
transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1.0);

/* Decelerate — elements entering the screen */
transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1.0);

/* Accelerate — elements leaving the screen */
transition-timing-function: cubic-bezier(0.4, 0.0, 1.0, 1.0);

/* Sharp — quick state changes, toggles */
transition-timing-function: cubic-bezier(0.4, 0.0, 0.6, 1.0);

/* Spring — confirmation celebrations (use sparingly) */
transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1.0);
```

### Specific Patterns

- **Balance counter:** Use `requestAnimationFrame` to count up/down to new balance over 400ms. Provides satisfying feedback without being slow.
- **Transaction list updates:** New items slide in from top with 200ms decelerate curve. No bouncing.
- **Chart animations:** Data points draw sequentially with 50ms stagger, total duration under 800ms.
- **Pull to refresh:** Spinner appears after 60px pull threshold, 200ms haptic feedback.
- **Card flip (virtual card reveal):** 3D rotation over 500ms with decelerate ease.
- **Error shake:** 3-cycle horizontal shake, 4px amplitude, 300ms total, ease-out.

---

## Trust Signals

### Visual Trust Elements

1. **Security iconography** — Lock icons near sensitive fields, shield icons on verification badges. Use outlined (not filled) for subtlety.
2. **Bank logos and partner badges** — Display FDIC insured, Visa/Mastercard logos, bank partner logos. These are non-negotiable for deposit products.
3. **Encryption indicators** — "End-to-end encrypted" labels near sensitive data entry points.
4. **Consistent visual language** — Inconsistency in styling (mismatched buttons, varying card styles) unconsciously signals unprofessionalism.
5. **Loading states for financial data** — Never show stale balances. Use skeleton screens that indicate data is being fetched, not shimmer animations that feel uncertain.
6. **Precise number formatting** — Always include currency symbols, proper decimal places ($1,234.56 not 1234.6), thousands separators. Sloppy number formatting erodes trust immediately.
7. **Timestamp everything** — "Balance as of 2:34 PM EST" signals real-time accuracy. Undated data feels unreliable.
8. **Clear transaction status** — Pending, processing, completed, failed. Every transaction needs an unambiguous status with visual differentiation.

### Behavioral Trust Elements

1. **Confirmation steps for irreversible actions** — Transfer $500? Confirm with amount, recipient, and timeline on a dedicated review screen.
2. **Undo windows** — "Transfer scheduled. Undo within 30 minutes." Reduces anxiety.
3. **Progressive disclosure of complexity** — Don't front-load advanced trading options. Reveal them as users demonstrate readiness.
4. **Biometric confirmation** — Face ID / fingerprint for sensitive actions. Friction that users welcome.
5. **Transparent fee display** — Show all fees before confirmation. Hidden fees destroy trust permanently.

---

## Anti-Patterns

### Critical Mistakes in Fintech Design

1. **Gamifying consequential financial decisions.** Confetti on stock purchases, slot-machine aesthetics for trading — these patterns (infamously associated with early Robinhood) trivialize real financial risk and have attracted regulatory scrutiny.

2. **Dark patterns around fees.** Pre-selecting premium tiers, burying fee schedules, using small gray text for charges. Users remember and leave.

3. **Inconsistent number formatting.** Mixing `$1,234.56` with `$1234.6` or displaying different decimal precision for the same currency destroys confidence in your data accuracy.

4. **Overly playful visual tone.** Comic Sans is obvious, but even overly rounded corners (24px+ on financial cards), candy-colored palettes, or bouncy animations can undermine seriousness.

5. **Missing loading states for financial data.** Showing $0.00 while data loads is terrifying. Always use skeleton screens or explicit "Loading..." states for balance displays.

6. **No transaction status clarity.** "Your transfer is being processed" without a timeline or status progression creates anxiety. Always show: initiated -> processing -> completed.

7. **Hiding security information.** If the money is FDIC insured, say it prominently. If transfers are encrypted, show it. Absence of security signals is itself a negative signal.

8. **Excessive motion during financial flows.** A 2-second animation before showing a transfer confirmation wastes time and creates anxiety. Keep financial flow animations under 300ms.

9. **Non-tabular number rendering.** When dollar amounts don't align vertically in lists and tables because proportional figures are used instead of tabular figures, it looks amateur.

10. **Ignoring responsive financial data.** Transaction lists, portfolio charts, and balance displays must be designed mobile-first. Desktop-optimized data tables on mobile are unusable.

---

## Reference Apps — What to Learn from Each

### Stripe
- **Lesson:** Editorial design can coexist with fintech. Stripe's marketing site uses magazine-quality typography and illustration while the dashboard maintains clinical precision. Study how they separate brand expression (marketing) from functional precision (product).
- **Key pattern:** Gradient mesh backgrounds, deep navy as primary background color, custom illustration style.
- **Dashboard density:** Medium density with generous padding. Data tables are clean but not cramped.

### Cash App
- **Lesson:** Bold brand identity can build trust through confidence. Cash App's stark black/green palette signals "we're not pretending to be a bank." Study how visual confidence substitutes for traditional trust signals.
- **Key pattern:** Full-screen green CTAs, oversized typography for amounts, minimal navigation.
- **Mobile-first:** Cash App barely has a desktop presence — it's designed for phone-in-hand, quick transactions.

### Robinhood
- **Lesson:** Simplification is powerful but carries responsibility. Study how Robinhood made stock trading visually accessible — and the backlash when that simplification was seen as trivializing financial risk.
- **Key pattern:** Single-stock view with prominent chart, minimal data density, progressive disclosure of advanced features.
- **Cautionary note:** The confetti-on-trade pattern became a case study in irresponsible gamification.

### Wise
- **Lesson:** Transparency as a design feature. Wise's transfer flow shows a real-time exchange rate, all fees broken down, and arrival time — all on a single screen. Study how radical transparency builds trust.
- **Key pattern:** Step-by-step transfer flow with persistent cost summary, comparison tables against banks.
- **Brand warmth:** Wise's lime green and warm off-whites feel friendlier than typical fintech without sacrificing trust.

### Revolut
- **Lesson:** Super-app complexity managed through progressive disclosure. Revolut offers banking, crypto, stocks, insurance, travel — study how they prevent feature overload through tab-based navigation and contextual feature surfacing.
- **Key pattern:** Card-based feature discovery, metal card tiers with distinct visual identity, spending analytics with clean data visualization.

### Mercury
- **Lesson:** Business banking can feel as refined as a premium consumer product. Mercury's restrained purple palette and generous whitespace signal "modern" without shouting "startup." Study how they balance information density with visual calm.
- **Key pattern:** Minimal sidebar navigation, clean transaction lists with smart categorization, beautiful statement PDFs.
- **Typography:** GT America adds quiet sophistication that distinguishes Mercury from consumer fintech.

---

## W3C Design Token Starter Kit — Fintech

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "fintech": {
    "color": {
      "primary": {
        "$value": "#635BFF",
        "$type": "color",
        "$description": "Primary brand — trust and innovation"
      },
      "primary-hover": {
        "$value": "#5548E5",
        "$type": "color"
      },
      "primary-active": {
        "$value": "#4A3FCC",
        "$type": "color"
      },
      "surface-primary": {
        "$value": "#FFFFFF",
        "$type": "color"
      },
      "surface-secondary": {
        "$value": "#F6F9FC",
        "$type": "color"
      },
      "surface-tertiary": {
        "$value": "#EDF1F5",
        "$type": "color"
      },
      "surface-dark": {
        "$value": "#0A2540",
        "$type": "color",
        "$description": "Deep navy for premium surfaces"
      },
      "text-primary": {
        "$value": "#0A2540",
        "$type": "color"
      },
      "text-secondary": {
        "$value": "#425466",
        "$type": "color"
      },
      "text-tertiary": {
        "$value": "#697386",
        "$type": "color"
      },
      "text-on-dark": {
        "$value": "#FFFFFF",
        "$type": "color"
      },
      "border-default": {
        "$value": "#E4E7EC",
        "$type": "color"
      },
      "border-hover": {
        "$value": "#C4C9D2",
        "$type": "color"
      },
      "semantic-positive": {
        "$value": "#30B130",
        "$type": "color",
        "$description": "Gains, success, confirmations"
      },
      "semantic-negative": {
        "$value": "#DF1B41",
        "$type": "color",
        "$description": "Losses, errors, destructive actions"
      },
      "semantic-warning": {
        "$value": "#F5BE3B",
        "$type": "color",
        "$description": "Cautions, pending states"
      },
      "semantic-info": {
        "$value": "#3B82F6",
        "$type": "color",
        "$description": "Informational, neutral highlights"
      }
    },
    "typography": {
      "font-family-primary": {
        "$value": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "$type": "fontFamily"
      },
      "font-family-mono": {
        "$value": "'SF Mono', 'Fira Code', 'Cascadia Code', monospace",
        "$type": "fontFamily"
      },
      "font-size-display": {
        "$value": "48px",
        "$type": "dimension"
      },
      "font-size-h1": {
        "$value": "32px",
        "$type": "dimension"
      },
      "font-size-h2": {
        "$value": "24px",
        "$type": "dimension"
      },
      "font-size-h3": {
        "$value": "20px",
        "$type": "dimension"
      },
      "font-size-body": {
        "$value": "16px",
        "$type": "dimension"
      },
      "font-size-body-small": {
        "$value": "14px",
        "$type": "dimension"
      },
      "font-size-caption": {
        "$value": "12px",
        "$type": "dimension"
      },
      "font-size-overline": {
        "$value": "11px",
        "$type": "dimension"
      },
      "font-weight-bold": {
        "$value": "700",
        "$type": "fontWeight"
      },
      "font-weight-semibold": {
        "$value": "600",
        "$type": "fontWeight"
      },
      "font-weight-medium": {
        "$value": "500",
        "$type": "fontWeight"
      },
      "font-weight-regular": {
        "$value": "400",
        "$type": "fontWeight"
      },
      "line-height-tight": {
        "$value": "1.2",
        "$type": "number"
      },
      "line-height-normal": {
        "$value": "1.5",
        "$type": "number"
      },
      "line-height-relaxed": {
        "$value": "1.7",
        "$type": "number"
      },
      "letter-spacing-tight": {
        "$value": "-0.02em",
        "$type": "dimension"
      },
      "letter-spacing-normal": {
        "$value": "0em",
        "$type": "dimension"
      },
      "letter-spacing-wide": {
        "$value": "0.08em",
        "$type": "dimension"
      }
    },
    "spacing": {
      "micro": { "$value": "4px", "$type": "dimension" },
      "tight": { "$value": "8px", "$type": "dimension" },
      "compact": { "$value": "12px", "$type": "dimension" },
      "default": { "$value": "16px", "$type": "dimension" },
      "comfortable": { "$value": "20px", "$type": "dimension" },
      "spacious": { "$value": "24px", "$type": "dimension" },
      "section": { "$value": "32px", "$type": "dimension" },
      "major": { "$value": "48px", "$type": "dimension" },
      "page": { "$value": "64px", "$type": "dimension" }
    },
    "radius": {
      "small": { "$value": "6px", "$type": "dimension" },
      "medium": { "$value": "8px", "$type": "dimension" },
      "large": { "$value": "12px", "$type": "dimension" },
      "xlarge": { "$value": "16px", "$type": "dimension" },
      "full": { "$value": "9999px", "$type": "dimension" }
    },
    "shadow": {
      "level-0": {
        "$value": "none",
        "$type": "shadow"
      },
      "level-1": {
        "$value": "0 1px 3px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04)",
        "$type": "shadow"
      },
      "level-2": {
        "$value": "0 4px 12px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.04)",
        "$type": "shadow"
      },
      "level-3": {
        "$value": "0 12px 40px rgba(0, 0, 0, 0.12), 0 4px 12px rgba(0, 0, 0, 0.06)",
        "$type": "shadow"
      }
    },
    "motion": {
      "duration-micro": { "$value": "100ms", "$type": "duration" },
      "duration-fast": { "$value": "150ms", "$type": "duration" },
      "duration-normal": { "$value": "250ms", "$type": "duration" },
      "duration-slow": { "$value": "350ms", "$type": "duration" },
      "duration-celebration": { "$value": "500ms", "$type": "duration" },
      "easing-standard": {
        "$value": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-decelerate": {
        "$value": "cubic-bezier(0.0, 0.0, 0.2, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-accelerate": {
        "$value": "cubic-bezier(0.4, 0.0, 1.0, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-sharp": {
        "$value": "cubic-bezier(0.4, 0.0, 0.6, 1.0)",
        "$type": "cubicBezier"
      }
    }
  }
}
```

---

## Inspiration Links

### Mobbin
- [Fintech app screens](https://mobbin.com/browse/apps?category=finance) — Filter by Finance category
- [Banking onboarding flows](https://mobbin.com/browse/flows?category=finance&flow=onboarding)
- [Payment confirmation screens](https://mobbin.com/browse/screens?category=finance&screen=confirmation)

### Screenlane
- [Finance app UI](https://screenlane.com/screens/category/finance/) — Transaction lists, balance displays, card management
- [Banking sign-up flows](https://screenlane.com/screens/category/finance/flow/sign-up/)

### Additional Resources
- [Stripe's design blog](https://stripe.com/blog/engineering) — Engineering and design process
- [Mercury's design system](https://mercury.com) — Study the product directly
- [Wise design principles](https://wise.com) — Transfer flow as masterclass in transparency

---

## Quick Decision Framework

When designing a fintech product, ask:

1. **Is this a mass-market consumer app or a professional tool?** Mass-market: more whitespace, larger touch targets, simpler data. Professional: denser data, keyboard shortcuts, compact tables.

2. **Does the user make high-stakes decisions here?** If yes: slow down the flow, add confirmation steps, reduce playful elements.

3. **Is this a daily-use dashboard or an occasional-use tool?** Daily: optimize for scanning speed, show changes since last visit. Occasional: orient the user, remind them of key information.

4. **What's the competitive landscape?** If competing with banks: be warmer and more modern. If competing with other fintechs: differentiate on clarity and trust, not just aesthetics.

5. **What regulatory context applies?** Heavily regulated (banking, trading): conservative, compliant, accessible. Lighter regulation (budgeting, analytics): more room for brand expression.
