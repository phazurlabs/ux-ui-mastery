---
description: Generate a complete W3C design token system — your visual identity distilled into code. Colors, type, spacing, elevation, and themes.
phase: "4"
phase_step: "4.1"
phase_name: "BUILD"
step_label: "Step 1 of 5"
---

# Drip — Design Token System Generator

Generate a complete, production-ready design token system following the W3C Design Tokens Community Group specification.

## Generation Protocol

1. **Gather context and constraints**: Before generating tokens, understand what they serve.
   - Brand colors (primary, secondary) — or generate from brand name/description
   - Typography preferences (font families, scale ratio)
   - Spacing system preference (base-4 or base-8)
   - Platform targets (web CSS, iOS, Android, React Native)
   - Theme requirements (light, dark, high contrast)
   - Brand personality (minimal, playful, corporate, premium)
   - **Sector**: What industry? (fintech, healthcare, e-commerce, SaaS, etc.) — determines color psychology, density norms, and trust signals
   - **Accessibility requirements**: AA (default) or AAA — AAA requires 7:1 contrast ratios for text and influences the entire color scale
   - **Prior Sumi outputs**: Check for `/taste` output. If available, consume its palette, type scale, spacing, motion personality, and tone direction. If not, use neutral defaults and note what's missing
   - **OKLCH perceptual uniformity**: All color scales must be generated in OKLCH color space to ensure perceptually uniform lightness steps — raw hex/HSL scales are not acceptable

2. **Apply perceptual and accessibility principles**: Every token category has a research-backed justification.

   | Token Category | Principle | How to Apply |
   |---------------|-----------|-------------|
   | Color scales | WCAG 2.2 + OKLCH perceptual uniformity | Generate in OKLCH; verify every fg/bg pairing meets contrast ratio; lightness steps must be perceptually even |
   | Semantic colors | Color psychology + sector conventions | Red=danger/error, green=success, amber=warning — but sector may override (healthcare: blue=trust, fintech: green=money) |
   | Type scale | Modular scale theory (Major Third 1.25, Perfect Fourth 1.333, etc.) | Choose ratio based on density needs; smaller ratio for dense UI, larger for editorial |
   | Spacing scale | Gestalt Proximity + sector density norms | Tighter spacing for data-dense sectors (fintech, SaaS); more generous for consumer/lifestyle |
   | Border radius | Jakob's Law + sector personality | Match the conventions of the sector; fintech/enterprise = subtle radius, consumer = generous radius |
   | Elevation/shadow | Depth perception + layering hierarchy | Shadows must communicate z-order; use consistent light source; limit to 5 levels maximum |
   | Motion/duration | Doherty Threshold (<400ms for feedback) | Micro-interactions: 100-200ms; transitions: 200-400ms; entrance animations: 300-500ms |

3. **Generate Token Tiers**:

   **Tier 1 — Global/Primitive Tokens**:
   - Color palette: 10-step scales (50-900) for each brand color + neutrals + semantic colors
   - Spacing scale: complete set from 1px to 128px
   - Typography: font families, size scale, weight scale, line height scale, letter spacing
   - Border radius: scale from none to full
   - Shadow/elevation: 5-level elevation system
   - Duration: animation timing scale
   - Easing: standard curve library

   **Tier 2 — Semantic/Alias Tokens**:
   - Background: primary, secondary, tertiary, inverse, brand, surface
   - Text: primary, secondary, tertiary, disabled, inverse, link, brand
   - Border: default, strong, brand, error, success
   - Action: primary, secondary, destructive — each with default, hover, active, disabled states
   - Feedback: success, warning, error, info — each with background, text, border, icon
   - Focus: ring color, ring width, ring offset

   **Tier 3 — Component Tokens (sample set)**:
   - Button: primary, secondary, ghost, destructive — bg, text, border, hover, active, disabled
   - Input: bg, text, border, placeholder, focus-ring, error, disabled
   - Card: bg, border, shadow, radius, padding

4. **Generate Theme Variants**:
   - Light theme (default)
   - Dark theme
   - High contrast theme (optional)

5. **Output**:
   - tokens.json following W3C DTCG format
   - CSS custom properties output
   - TypeScript type definitions
   - Usage documentation with examples

## Output Format

```
### Phase Position
> **Phase 4: BUILD** | Step 1 of 5 | `/drip`
> *NNG: Design Systems | Visual: Token Foundation*
>
> **Phase 3** `/responsive` (3.4) → **`/drip` (4.1)** → `/screen` (4.2)

## Design Token System

### Configuration
- Brand: [name/colors]
- Scale: [base-4/base-8]
- Themes: [light, dark]
- Platforms: [web, iOS, Android]

### Token Files
[Complete tokens.json]

### CSS Output
[CSS custom properties for light and dark themes]

### TypeScript Types
[Type definitions for token consumption]

### Usage Guide
[How to apply tokens in components with examples]

### Token Rationale
| Token | Value | Principle | Why |
|-------|-------|-----------|-----|
| --color-primary-500 | oklch(0.55 0.15 250) | OKLCH + sector color psychology | Primary blue conveys trust for [sector]; OKLCH ensures perceptual uniformity |
| --font-size-scale | 1.25 (Major Third) | Modular scale theory | Balanced ratio for mixed content density |
| --space-base | 8px | Gestalt Proximity + base-8 | Industry-standard base for consistent rhythm |
| [...]  | [...]  | [...]     | [...] |

### Accessibility Verification
| Foreground Token | Background Token | Contrast Ratio | WCAG Level | Status |
|-----------------|-----------------|---------------|------------|--------|
| --color-text-primary | --color-bg-primary | [X.X:1] | AA (4.5:1) | [Pass/Fail] |
| --color-text-secondary | --color-bg-primary | [X.X:1] | AA (4.5:1) | [Pass/Fail] |
| --color-action-primary-text | --color-action-primary-bg | [X.X:1] | AA (4.5:1) | [Pass/Fail] |
| [...] | [...] | [...] | [...] | [...] |

### Prior Output Integration
- **`/taste` consumed**: [Yes/No — if yes, list what was used: palette, type scale, spacing, motion, tone]
- **Missing context**: [List any Phase 1 outputs that would improve these tokens if run]
```

## Cross-References
When generating tokens, draw from:
- `design-systems-architecture` skill for token architecture and W3C specification
- `ui-visual-design-system` skill for color theory and typography systems
- `sector-style-intelligence` skill for sector-specific token recommendations
- `accessibility-inclusive-design` skill for WCAG contrast requirements and high-contrast theme generation
- `cognitive-psychology-ux` skill for perceptual principles (color psychology, Gestalt proximity for spacing)

## Next Step

**Next** → `/screen` (4.2) — Build screens using your new token system

**Alternatives**:
- `/ship` (4.3) — Skip screens, build components directly
- `/taste` (1.1) — Go back to DISCOVER for style direction if tokens feel generic
- `/guide` — See the full 20-step journey
