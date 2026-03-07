---
description: Generate a complete visual design direction — color, typography, spacing, shape, motion, elevation — informed by 36+ world-class designers and 70 canonical design rules. Your visual identity, grounded in craft.
phase: "1"
phase_step: "1.6"
phase_name: "DISCOVER"
step_label: "Step 6 of 6"
---

# Vision — Visual Design Direction Generator

Generate a complete visual design direction document covering color, typography, spacing, shape, motion, and elevation — informed by 36+ world-class designer archetypes and 70 canonical design rules. Every decision is grounded in sector psychology, platform conventions, and perception science.

## Analysis Protocol

### Step 0: Gather Context

Before generating, collect:

1. **What the app does**: Product description, purpose, target users.
2. **Sector**: Auto-detect from description or prior Sumi outputs, or ask the user. This is critical — sector determines visual norms, color psychology, and typography expectations.
3. **Platform**: iOS, Android, Web, cross-platform. Determines type scale, motion curves, shape language, and system font considerations.
4. **Mood/feel keywords** (optional): e.g., "clean", "bold", "playful", "serious", "warm", "technical". If not provided, infer from sector + product type.
5. **Reference products** (optional): e.g., "like Stripe", "inspired by Linear". Used to anchor the visual direction.
6. **Brand constraints**: Existing colors, fonts, logo. These MUST be respected if provided — the generated direction works around them, not against them.
7. **Prior Sumi outputs**: Consume `/taste` (visual direction preferences), `/intent` (problem + constraints), `/patterns` (existing pattern inventory) if available. These significantly inform the direction.

If minimal context is provided, ask for at minimum: what the app does and the sector. Generate the rest from intelligent defaults.

### Step 1: DESIGNER MATCH — Select Design Archetypes

Based on sector + mood + references, match to 2-3 designer archetypes from `visual-design-mastery` skill -> `designer-pattern-library.md`.

**For each matched designer**:
- Name the designer and their signature style
- Explain WHY their patterns fit this product (sector alignment, mood alignment, reference alignment)
- Extract 3-5 specific teachable patterns from each matched designer
- Note which patterns will be applied to which system (color, type, spacing, shape, motion, elevation)

**You MUST**:
- Match based on genuine fit, not randomly
- Justify each match with specific reasoning
- Show how each designer's patterns translate into concrete decisions in later steps

### Step 2: COLOR SYSTEM — Generate Full Palette

Using `color-mastery.md` from the `visual-design-mastery` skill:

**Primary color**:
- Select with rationale grounded in sector psychology, brand alignment, mood keywords
- If brand constraints include a color, use it as primary and build around it

**Full palette**:
- Primary color (with tint/shade scale: 50-950)
- Secondary color (harmony algorithm used — complementary, analogous, split-complementary, triadic)
- Tertiary/accent color (if needed)
- Neutral palette (surfaces, borders, text — 8-10 steps from near-white to near-black)
- Semantic colors: success (green range), warning (amber range), error (red range), info (blue range) — each with background/foreground/border variants
- Surface colors: background, surface, elevated surface, overlay

**Technical requirements**:
- All colors in oklch() AND hex format
- Dark mode mapping: every light color maps to a dark equivalent (not just inverted — perceptually balanced)
- Contrast verification: check every text/background pair against WCAG AA (4.5:1 normal text, 3:1 large text). Note any AAA-compliant pairs (7:1).
- Output the complete palette as W3C Design Token Format (JSON)

### Step 3: TYPOGRAPHY SYSTEM — Generate Type Scale

Using `typography-mastery.md` from the `visual-design-mastery` skill:

**Font family recommendation**:
- Primary font with rationale (sector expectations, mood, platform conventions)
- Secondary/display font (if applicable — e.g., headings use a different face)
- Monospace font (if applicable — for code, data, technical content)
- Fallback stack for each (system fonts)
- If brand constraints include a font, use it and select complementary pairings

**Type scale** (all levels):
- Display Large, Display Medium, Display Small
- Headline Large, Headline Medium, Headline Small
- Title Large, Title Medium, Title Small
- Body Large, Body Medium, Body Small
- Label Large, Label Medium, Label Small
- Caption, Overline

**For each level**: font-family, font-size (px and rem), line-height, letter-spacing, font-weight

**Technical requirements**:
- Fluid type scale using clamp() for web (minimum, preferred, maximum)
- Platform adaptations: iOS Dynamic Type size category mapping, M3 type role mapping
- Maximum 3-4 font weights used across the entire scale
- Output as W3C Design Token Format (JSON)

### Step 4: SPACING SYSTEM — Generate Spatial Scale

Using `composition-mastery.md` from the `visual-design-mastery` skill:

**Base unit**: Typically 4px or 8px — justify the choice based on density needs and platform conventions.

**Spacing scale** (8-12 named values):
- Named tokens: space-0 through space-12 (or similar naming)
- Each with px value and rem equivalent

**Component padding standards**:
- Button padding (small, medium, large)
- Input padding
- Card padding
- Modal/dialog padding
- List item padding

**Section margins**: Between major content sections

**Density setting**: compact, comfortable, or spacious — with rationale based on sector and content type.

**Grid system**:
- Columns per breakpoint (mobile: 4, tablet: 8, desktop: 12 typical)
- Gutter width per breakpoint
- Margin width per breakpoint
- Max content width

**Output as W3C Design Token Format (JSON)**

### Step 5: SHAPE LANGUAGE — Generate Shape System

**Border radius scale**:
- radius-none (0)
- radius-sm, radius-md, radius-lg, radius-xl, radius-full
- Each with px value

**Container shapes**:
- Button radius (per size variant)
- Input radius
- Card radius
- Modal radius
- Chip/badge radius
- Avatar radius (typically full)

**Icon style direction**:
- Style: outlined, filled, duotone, or mixed
- Stroke width (if outlined)
- Grid size (24px typical)
- Corner style (rounded, sharp)
- Recommended icon library

**Illustration style direction** (if applicable):
- Style keywords (flat, isometric, 3D, hand-drawn, geometric)
- Color treatment (full palette, monotone, duotone)

**Platform-specific shapes**:
- iOS: squircle (continuous corner curve) via `cornerCurve: .continuous`
- M3: shape tokens (extraSmall through extraLarge)

**Output as W3C Design Token Format (JSON)**

### Step 6: MOTION PERSONALITY — Generate Motion System

Using `interaction-motion-design` skill:

**Easing curves**:
- Standard: for general transitions
- Enter: for elements appearing
- Exit: for elements disappearing
- Emphasized: for important/dramatic transitions
- Each as cubic-bezier() values

**Duration scale**:
- Instant: 0-100ms (micro-feedback)
- Fast: 100-200ms (hover, focus, toggle)
- Normal: 200-350ms (expand, collapse, slide)
- Slow: 350-500ms (page transitions, modals)
- Deliberate: 500ms+ (onboarding, celebrations)

**Spring configurations** (iOS/Android):
- Response, dampingFraction (SwiftUI)
- Stiffness, damping (Android/physics-based)
- Light spring, medium spring, heavy spring presets

**Transition types**:
- Fade: opacity transitions
- Slide: directional movement
- Scale: size transitions
- Shared element: cross-screen continuity
- When to use each

**Hover/focus animations** (web):
- Button hover (scale, shadow, color shift)
- Card hover (elevation change)
- Link hover (underline, color)
- Focus ring style and animation

**Reduced motion alternatives**: Every animation must have a reduced-motion fallback (typically instant opacity change or no animation).

**Output as W3C Design Token Format (JSON)**

### Step 7: ELEVATION SYSTEM — Generate Depth Scale

**Shadow scale** (4-6 levels):
- Level 0: No shadow (flush)
- Level 1: Subtle (cards, wells)
- Level 2: Low (dropdowns, popovers)
- Level 3: Medium (sticky headers, floating actions)
- Level 4: High (modals, dialogs)
- Level 5: Highest (toasts, notifications — if needed)

**For each level**: x-offset, y-offset, blur, spread, color (with opacity)

**Usage guidance**: When to use each level — mapped to specific component types.

**Dark mode shadow adjustments**: Shadows are less visible on dark backgrounds. Adjust opacity or supplement with border/luminance changes.

**Output as W3C Design Token Format (JSON)**

### Step 8: SCORE — Evaluate Direction

Score the generated direction against `visual-scoring-framework.md` from the `visual-design-mastery` skill:

**Score each of the 10 dimensions** (1-10):
1. Typography (15%)
2. Color (12%)
3. Spacing (12%)
4. Composition (12%)
5. Imagery (8%)
6. Iconography (8%)
7. Motion (8%)
8. Polish (10%)
9. Coherence (8%)
10. Craft (7%)

**For any dimension scoring below 7**: Note specifically what would need to change to reach 8+.

**Overall visual quality prediction**: Weighted average with quality tier label.

### Step 9: REFERENCE BOARD — Describe Visual Direction

- Name 3-5 reference products that embody this visual direction
- For each reference: what specific element or quality to take from it (not the whole design)
- Positioning statement: "This direction lives between [Product A]'s [quality] and [Product B]'s [quality]"
- What this direction is NOT (anti-references — helps sharpen the vision)

## Output Format

```
### Phase Position
> **Phase 1: DISCOVER** | Step 6 of 6 | `/vision`
> *NNG: Visual Direction | Visual: Design Direction*
>
> `/patterns` (1.5) -> **`/vision` (1.6)** -> `/vibe-check` (2.1)

---

## Visual Design Direction

### App Overview
- **App**: [Name/description]
- **Sector**: [Detected/specified]
- **Platform**: [Target platform(s)]
- **Mood**: [Keywords]
- **Prior Sumi context**: [What was consumed]

---

### Designer DNA

[2-3 matched designers with rationale and extracted patterns]

**Designer 1: [Name]** — [Signature style]
- Why: [Specific fit rationale]
- Patterns extracted: [3-5 patterns with which system they inform]

**Designer 2: [Name]** — [Signature style]
- Why: [Specific fit rationale]
- Patterns extracted: [3-5 patterns with which system they inform]

[Designer 3 if applicable]

---

### Color System

**Palette Overview**
- Primary: [color name] — [oklch()] | [hex] — [rationale]
- Secondary: [color name] — [oklch()] | [hex] — [harmony: algorithm]
- Tertiary: [color name] — [oklch()] | [hex]

**Primary Scale**: [50-950 with oklch + hex]
**Neutral Scale**: [50-950 with oklch + hex]
**Semantic Colors**: [success, warning, error, info with bg/fg/border variants]
**Surface Colors**: [background, surface, elevated, overlay]

**Dark Mode Mapping**: [Every light token -> dark equivalent]

**Contrast Verification**:
| Pair | Ratio | AA | AAA |
|------|-------|----|-----|
| [text on bg] | [X:1] | [pass/fail] | [pass/fail] |
[continue for all critical pairs]

**W3C Design Tokens**: [JSON block]

---

### Typography System

**Font Selection**
- Primary: [Font name] — [rationale]
- Secondary: [Font name] — [rationale]
- Monospace: [Font name]
- Fallbacks: [stack]

**Type Scale**
| Level | Size (px/rem) | Line Height | Letter Spacing | Weight | Fluid (clamp) |
|-------|---------------|-------------|----------------|--------|----------------|
| Display Large | [values] | [value] | [value] | [value] | [clamp()] |
[continue for all levels]

**Platform Adaptations**: [iOS Dynamic Type, M3 type roles]

**W3C Design Tokens**: [JSON block]

---

### Spacing System

**Base Unit**: [Xpx] — [rationale]
**Density**: [compact/comfortable/spacious] — [rationale]

**Scale**
| Token | Value (px) | Value (rem) | Usage |
|-------|------------|-------------|-------|
| space-1 | [X] | [X] | [typical use] |
[continue for all values]

**Component Padding Standards**: [buttons, inputs, cards, modals]
**Grid System**: [columns, gutters, margins per breakpoint]

**W3C Design Tokens**: [JSON block]

---

### Shape Language

**Border Radius Scale**
| Token | Value | Usage |
|-------|-------|-------|
| radius-sm | [X]px | [usage] |
[continue]

**Container Shapes**: [button, input, card, modal, chip, avatar]
**Icon Style**: [style, stroke width, grid, library recommendation]
**Platform Shapes**: [iOS squircle, M3 shape tokens]

**W3C Design Tokens**: [JSON block]

---

### Motion Personality

**Easing Curves**
| Name | Value | Usage |
|------|-------|-------|
| standard | cubic-bezier([values]) | [usage] |
[continue]

**Duration Scale**
| Name | Range | Usage |
|------|-------|-------|
| instant | [X]ms | [usage] |
[continue]

**Spring Configurations**: [light, medium, heavy with platform values]
**Transition Types**: [fade, slide, scale, shared element — when to use each]
**Reduced Motion**: [fallback strategy]

**W3C Design Tokens**: [JSON block]

---

### Elevation System

**Shadow Scale**
| Level | x | y | blur | spread | color | Usage |
|-------|---|---|------|--------|-------|-------|
| 0 | 0 | 0 | 0 | 0 | — | flush elements |
[continue]

**Dark Mode Adjustments**: [strategy]

**W3C Design Tokens**: [JSON block]

---

### Visual Quality Prediction: [X/10] — [Quality Tier]

| # | Dimension | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 1 | Typography | 15% | [X/10] | [note] |
| 2 | Color | 12% | [X/10] | [note] |
| 3 | Spacing | 12% | [X/10] | [note] |
| 4 | Composition | 12% | [X/10] | [note] |
| 5 | Imagery | 8% | [X/10] | [note] |
| 6 | Iconography | 8% | [X/10] | [note] |
| 7 | Motion | 8% | [X/10] | [note] |
| 8 | Polish | 10% | [X/10] | [note] |
| 9 | Coherence | 8% | [X/10] | [note] |
| 10 | Craft | 7% | [X/10] | [note] |

[Notes on any dimensions below 7 and how to improve]

---

### Reference Board

**This direction lives between [Product A]'s [quality] and [Product B]'s [quality].**

| Reference | What to Take | Specific Element |
|-----------|-------------|------------------|
| [Product 1] | [quality] | [specific element] |
| [Product 2] | [quality] | [specific element] |
| [Product 3] | [quality] | [specific element] |
[continue 3-5 references]

**This direction is NOT**: [anti-references — what to avoid]

---

### Next Steps
1. **First**: [Highest-impact action]
2. **Second**: [Next action]
3. **Third**: [Next action]

**Recommended command sequence**:
-> `/drip` — Formalize tokens into code-ready design token files
-> `/ship [component]` — Build first component consuming these tokens
-> `/screen [type]` — Generate first screen using this direction
-> `/generate` — AI-generate screens using this direction (if MCP available)
-> `/visual-score` — Score implementation against this direction
```

## Quality Gates

The output MUST include:
- [ ] Designer match with rationale (not random selection)
- [ ] Complete color palette with oklch + hex + dark mode mapping
- [ ] Contrast verification table for all critical text/background pairs
- [ ] Type scale with all levels, fluid clamp() values, and platform adaptations
- [ ] Spacing scale with component padding standards and grid system
- [ ] Shape system with platform-specific values (iOS squircle, M3 tokens)
- [ ] Motion system with easing curves, durations, and spring configurations
- [ ] Elevation system with per-level shadow values and dark mode adjustments
- [ ] All seven systems output as W3C Design Token Format (JSON)
- [ ] Visual quality prediction score with per-dimension breakdown
- [ ] Reference board with specific takeaways per product (not vague)

The output MUST NOT include:
- Vague color descriptions without actual values — every color must have oklch() and hex
- Font recommendations without rationale — every font choice must explain why
- Spacing values without usage context — every token must show when to use it
- Motion values without reduced-motion alternatives — accessibility is non-negotiable
- Scores without justification — every quality prediction must cite specifics
- Design tokens without proper W3C format — output must be copy-pasteable

## Cross-References

When generating the visual direction, draw knowledge from:
- `visual-design-mastery` skill — designer patterns (`designer-pattern-library.md`), canonical rules (`canonical-design-rules.md`), scoring framework (`visual-scoring-framework.md`), color mastery (`color-mastery.md`), typography mastery (`typography-mastery.md`), composition mastery (`composition-mastery.md`)
- `sector-style-intelligence` skill — sector visual norms, expected palettes, typography conventions, density expectations
- `design-systems-architecture` skill — W3C design token format, token architecture, naming conventions
- `cognitive-psychology-ux` skill — color psychology, type readability research, spatial perception, Gestalt principles
- `interaction-motion-design` skill — easing curves, spring physics, transition choreography, reduced motion
- `accessibility-inclusive-design` skill — WCAG contrast requirements, color blindness considerations, motion sensitivity
- `mobile-ux-design` skill — iOS Dynamic Type, M3 type roles, platform-specific conventions
- `component-patterns-code` skill — how tokens are consumed in React, SwiftUI, CSS implementations
- `ui-pattern-intelligence` skill — pattern benchmarks that inform what "world-class" looks like

## Next Step

**Next** -> `/vibe-check` (2.1) — Audit the visual direction against Nielsen's 10 heuristics

**Alternatives**:
- `/drip` (4.1) — Convert this direction into production-ready design token files
- `/ship [component]` (4.3) — Build the first component consuming these tokens
- `/screen [type]` (4.2) — Generate a full screen using this visual direction
- `/patterns` (1.5) — Re-run pattern analysis with this visual direction as context
- `/guide` — See the full journey map
