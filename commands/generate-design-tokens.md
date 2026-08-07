---
name: generate-design-tokens
description: Generate a complete design token system from brand requirements following the W3C Design Tokens specification.
argument-hint: "[brand requirements or existing palette]"
---

# Generate Design Tokens Command

## Before running

This command needs the brand requirements — colors, type, spacing — or an existing palette to formalize.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target, do not audit a hypothetical interface, and do not produce generic advice in place of the real analysis — an audit of something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.

Generate a complete, production-ready design token system following the W3C Design Tokens Community Group specification.

## Generation Protocol

1. **Gather Requirements**:
   - Brand colors (primary, secondary) — or generate from brand name/description
   - Typography preferences (font families, scale ratio)
   - Spacing system preference (base-4 or base-8)
   - Platform targets (web CSS, iOS, Android, React Native)
   - Theme requirements (light, dark, high contrast)
   - Brand personality (minimal, playful, corporate, premium)

2. **Generate Token Tiers**:

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

3. **Generate Theme Variants**:
   - Light theme (default)
   - Dark theme
   - High contrast theme (optional)

4. **Output**:
   - tokens.json following W3C DTCG format
   - CSS custom properties output
   - TypeScript type definitions
   - Usage documentation with examples

## Output Format

```
## Generated Design Token System

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
```
