# Canonical Design Rules

> 70 rules extracted from 23 canonical design books. Each rule: source, principle, UI application, common violation, fix.

---

## Typography Rules (1-15)

### Rule 1: Establish a Modular Type Scale
**Source**: The Elements of Typographic Style, Robert Bringhurst
**Principle**: Use a mathematical ratio (e.g., 1.25 major third) to derive all font sizes from a base size. This creates harmonious relationships between all text levels.
**UI Application**: Set base at 16px, derive scale: 12.8, 16, 20, 25, 31.25, 39. Use CSS custom properties: --text-xs: 0.8rem; --text-sm: 0.875rem; --text-base: 1rem; --text-lg: 1.25rem; --text-xl: 1.563rem; --text-2xl: 1.953rem.
**Common Violation**: Random font sizes (13px, 17px, 22px, 29px) with no mathematical relationship.
**Fix**: Pick a ratio (1.2 for dense UIs, 1.25 for general, 1.333 for spacious), generate scale, and constrain all type to these values.

### Rule 2: Set Optimal Line Length (Measure)
**Source**: The Elements of Typographic Style, Robert Bringhurst
**Principle**: Body text should be 45-75 characters per line. The ideal is 66 characters. Lines that are too long cause fatigue; too short disrupts reading rhythm.
**UI Application**: max-width: 65ch on body text containers. For code blocks: max-width: 80ch. For captions: max-width: 45ch.
**Common Violation**: Full-width text on 1440px screens = 120+ characters per line. Unreadable.
**Fix**: Apply max-width: 65ch to all prose containers. Use CSS `ch` unit, which is based on the width of the "0" character.

### Rule 3: Use Line-Height Relative to Line Length
**Source**: Thinking with Type, Ellen Lupton
**Principle**: Longer lines need more line-height (leading) to help the eye track back to the start. Shorter lines need less.
**UI Application**: Body text (60ch): line-height: 1.5-1.6. Short text (30ch): line-height: 1.3-1.4. Headings: line-height: 1.1-1.25. Captions: line-height: 1.3.
**Common Violation**: Using line-height: 1.5 for everything, including 48px headings (which creates 72px line-height — far too much).
**Fix**: Decrease line-height as font-size increases. Rule of thumb: line-height = 1.6 - (font-size - 16) * 0.01, with a floor of 1.1.

### Rule 4: Create Hierarchy with Fewer Than 4 Methods
**Source**: Thinking with Type, Ellen Lupton
**Principle**: Typographic hierarchy should be achieved through a limited set of variations: size, weight, and color. Don't use all possible methods (size + weight + color + italic + underline + caps) simultaneously.
**UI Application**: Pick 2-3 methods per hierarchy level. H1: size (32px) + weight (700). H2: size (24px) + weight (600). Body: size (16px) + weight (400). Caption: size (14px) + color (gray-500).
**Common Violation**: Headings that are bigger AND bolder AND colored AND uppercase AND underlined. Overdesigned hierarchy.
**Fix**: Reduce to the minimum differentiation needed. Test: can users distinguish levels with just one method removed?

### Rule 5: Never Center Long Text
**Source**: The Non-Designer's Design Book, Robin Williams
**Principle**: Centered text creates a ragged edge on BOTH sides, making it harder to read for more than 2-3 lines. Reserve centering for short text (headings, quotes, labels).
**UI Application**: Body text: text-align: left (LTR) always. Headings: text-align: center only if 1-2 lines. Cards: text-align: left. Form labels: text-align: left.
**Common Violation**: Centered paragraphs, centered form labels, centered list items.
**Fix**: text-align: left for anything over 2 lines. Center only: single-line headings, buttons, toasts, badges.

### Rule 6: Tracking Decreases as Size Increases
**Source**: The Elements of Typographic Style, Robert Bringhurst
**Principle**: Large type needs tighter letter-spacing (tracking); small type needs looser tracking. This is because optical spacing changes with size.
**UI Application**: Display (48px+): letter-spacing: -0.02em to -0.03em. Heading (24-48px): letter-spacing: -0.01em. Body (14-18px): letter-spacing: 0 (default). Small/Caption (12px): letter-spacing: +0.01em to +0.02em. All-caps: letter-spacing: +0.05em to +0.1em.
**Common Violation**: Default letter-spacing at all sizes, causing large headings to look too loose and small text to look too tight.
**Fix**: Add letter-spacing tokens to the type scale: --tracking-tight: -0.02em; --tracking-normal: 0; --tracking-wide: 0.025em; --tracking-wider: 0.05em.

### Rule 7: Use a Maximum of Two Typeface Families
**Source**: Practical UI, Adham Dannaway
**Principle**: Two typefaces are enough for any interface — one for headings/display, one for body/UI. More than two creates visual noise.
**UI Application**: Primary: Inter (body, UI, labels). Secondary: Source Serif 4 (long-form content, editorial). Mono: JetBrains Mono (code). The mono doesn't count as a "third" — it's functional.
**Common Violation**: Three or more sans-serif fonts, or a different font for every section.
**Fix**: Audit all font-family declarations. Consolidate to two families. Use weight and size for variety within a family.

### Rule 8: Minimum Body Font Size Is 16px on Mobile
**Source**: Web Form Design, Luke Wroblewski
**Principle**: Below 16px on mobile, iOS Safari zooms in on input focus, breaking the layout. Also, 14px body text is below comfortable reading size on handheld devices.
**UI Application**: font-size: 16px minimum for body text and input fields on mobile. Captions can be 14px. Never go below 12px for any text.
**Common Violation**: 14px body text on mobile because "it looks cleaner." Users can't read it comfortably.
**Fix**: Set html { font-size: 16px } and use rem units. Minimum for any readable text: 0.75rem (12px).

### Rule 9: Establish Consistent Typographic Color
**Source**: Thinking with Type, Ellen Lupton
**Principle**: "Typographic color" is the overall gray value of a text block. It should be even — no dark spots (bold words), no light spots (too much spacing). Even color = comfortable reading.
**UI Application**: Body text should have consistent weight (400), consistent line-height, consistent paragraph spacing. Avoid bold within paragraphs unless essential. Use color (not weight) for inline emphasis in UI.
**Common Violation**: Body text with frequent bold spans, creating a spotty, uneven texture.
**Fix**: Replace inline bold with color emphasis (text in primary brand color) or use medium weight (500) instead of bold (700) for subtle emphasis.

### Rule 10: Align Text to a Baseline Grid
**Source**: Grid Systems in Graphic Design, Josef Muller-Brockmann
**Principle**: All text should align to a shared baseline grid (typically 4px or 8px increments). This creates vertical rhythm and allows multi-column text to align across columns.
**UI Application**: Set line-height to multiples of 4px: body at 16px/24px, headings at 24px/32px, caption at 12px/16px. Margin-top and margin-bottom in 8px increments.
**Common Violation**: Arbitrary line-heights (16px/22px, 20px/27px) that don't align to any grid.
**Fix**: Round all line-heights to the nearest 4px multiple. Use a 4px vertical rhythm: every element's total height (content + padding + margin) should be divisible by 4.

### Rule 11: Optical Alignment Over Mathematical Alignment
**Source**: The Elements of Typographic Style, Robert Bringhurst
**Principle**: Some shapes need to extend beyond the mathematical boundary to APPEAR aligned. Circles and triangles should overshoot the baseline and cap-height by ~2%.
**UI Application**: Bullet points and rounded icons should be optically centered, not mathematically centered. A play button (triangle) inside a circle needs to shift right by ~6% to appear centered.
**Common Violation**: Perfectly mathematical centering that looks off — icons that appear too high, too left, or too small.
**Fix**: Use transform: translateX(1px) or translateY(-1px) for optical corrections. For icon-in-button: add 1-2px padding-left to triangle shapes.

### Rule 12: Never Use Pure Black Text on Pure White
**Source**: Refactoring UI, Adam Wathan & Steve Schoger
**Principle**: Pure black (#000000) on pure white (#FFFFFF) creates excessive contrast that causes eye strain. Real-world black ink on white paper is softer.
**UI Application**: Body text: #1A1A1A or #111827 (gray-900) on #FFFFFF. Secondary text: #6B7280 (gray-500). Disabled text: #9CA3AF (gray-400). In dark mode: #E5E7EB (gray-200) on #111827.
**Common Violation**: color: #000000 on background: #FFFFFF throughout.
**Fix**: Replace #000000 with a near-black: --color-text-primary: #111827; --color-text-secondary: #6B7280; --color-text-tertiary: #9CA3AF.

### Rule 13: Paragraph Spacing > Line Spacing
**Source**: Practical UI, Adham Dannaway
**Principle**: The space between paragraphs should be greater than the space between lines within a paragraph. This creates clear text block separation without excessive inter-line spacing.
**UI Application**: If line-height: 1.5 (24px at 16px), then paragraph margin-bottom should be 24px-32px. The ratio: paragraph spacing = 1x to 1.5x line-height.
**Common Violation**: No paragraph spacing (margin-bottom: 0) — paragraphs run together. Or excessive paragraph spacing that disconnects related content.
**Fix**: margin-bottom on <p>: 1em (matches line-height for consistent rhythm).

### Rule 14: Use Tabular (Monospaced) Figures for Data
**Source**: The Elements of Typographic Style, Robert Bringhurst
**Principle**: In tables, lists, and any vertically stacked numbers, use tabular (fixed-width) figures so digits align vertically. Proportional figures are for running text.
**UI Application**: font-variant-numeric: tabular-nums for: tables, prices, dates, counters, progress indicators. Use proportional (default) for body text.
**Common Violation**: Proportional numbers in a pricing table — the decimal points don't align, amounts look sloppy.
**Fix**: Add font-variant-numeric: tabular-nums to any container displaying vertically-stacked numbers. With Inter, also use font-feature-settings: 'tnum' 1.

### Rule 15: Headings Need Top Margin Greater Than Bottom Margin
**Source**: Practical UI, Adham Dannaway
**Principle**: A heading belongs to the content that follows it, not the content before it. More space above the heading (separation from previous section) and less space below (connection to own content).
**UI Application**: H2: margin-top: 48px, margin-bottom: 16px. H3: margin-top: 32px, margin-bottom: 12px. Ratio: top margin = 2-3x bottom margin.
**Common Violation**: Equal margins above and below headings, making them float ambiguously between sections.
**Fix**: --heading-margin-top: 2em; --heading-margin-bottom: 0.5em.

---

## Color Rules (16-28)

### Rule 16: Start with One Color, Add Grays
**Source**: Refactoring UI, Adam Wathan & Steve Schoger
**Principle**: You need far fewer colors than you think. Start with a gray palette (8-10 shades) and one primary color. Add secondary/accent colors only when functionally necessary.
**UI Application**: Gray palette: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950. Primary: one hue at 5 lightness levels. Semantic: success (green), warning (amber), error (red). That's a complete palette.
**Common Violation**: 6+ brand colors plus 4 semantic colors plus random one-off colors = visual chaos.
**Fix**: Audit every color in use. If a color isn't gray, primary, or semantic, question its existence. Generate the full palette from a single brand hue using oklch tonal steps.

### Rule 17: Colors Must Work in Pairs
**Source**: Interaction of Color, Josef Albers
**Principle**: A color never exists in isolation — it's always perceived relative to its neighbors. Test colors in their actual context, not on a swatch.
**UI Application**: A blue button on a white background looks different from the same blue on a dark background. Always test text-on-background pairs, not individual colors.
**Common Violation**: Picking colors from a palette tool and applying them without testing the actual pair.
**Fix**: Define colors as pairs: --primary-bg + --primary-text, --surface-bg + --surface-text. Test every pair for contrast (minimum APCA Lc 60 for large text, Lc 75 for body).

### Rule 18: Perceived Lightness Matters More Than Measured Lightness
**Source**: Interaction of Color, Josef Albers
**Principle**: Yellow at 50% lightness looks much brighter than blue at 50% lightness. Equal mathematical values produce unequal perceptual results. Use perceptually uniform color spaces.
**UI Application**: Use oklch() in CSS — its L (lightness) channel is perceptually uniform. oklch(0.7 0.15 90) (yellow) and oklch(0.7 0.15 250) (blue) will appear equally light.
**Common Violation**: HSL-based palettes where yellow (hsl(60, 100%, 50%)) looks much brighter than blue (hsl(240, 100%, 50%)) despite equal L values.
**Fix**: Generate palettes in oklch. Keep L constant across hues for visually balanced palettes. Use L: 0.55-0.65 for accessible accent colors on white backgrounds.

### Rule 19: Limit Saturation in Dark Mode
**Source**: Material Design 3 (Google)
**Principle**: Highly saturated colors on dark backgrounds cause visual vibration and eye strain. In dark mode, reduce chroma while maintaining hue and adjusting lightness upward.
**UI Application**: Light mode primary: oklch(0.55 0.25 250). Dark mode primary: oklch(0.75 0.15 250) — lighter, less saturated. Surface tint: primary color at 5-11% opacity over the dark surface.
**Common Violation**: Using the exact same brand colors in dark mode as light mode. Saturated red on near-black = eye strain.
**Fix**: Create dark mode color tokens with increased L and decreased C in oklch: --primary-dark: oklch(calc(var(--primary-l) + 0.2) calc(var(--primary-c) - 0.1) var(--primary-h)).

### Rule 20: Use Semantic Color Names, Not Descriptive Names
**Source**: Design Systems, Alla Kholmatova
**Principle**: Name colors by their role (--color-text-primary), not their appearance (--color-dark-gray). Roles survive theme changes; descriptions don't.
**UI Application**: Tokens: --color-surface-primary, --color-surface-elevated, --color-text-primary, --color-text-secondary, --color-border-default, --color-interactive-primary, --color-feedback-success.
**Common Violation**: --blue-500, --gray-200, --dark-red throughout the codebase. Switching themes requires rewriting every reference.
**Fix**: Two-tier token system. Reference tokens (--blue-500: oklch(0.55 0.2 250)) and semantic tokens (--color-interactive-primary: var(--blue-500)). Themes change the mapping, not the usage.

### Rule 21: Ensure 3:1 Contrast for UI Components
**Source**: WCAG 2.2, Level AA
**Principle**: Non-text UI components (buttons, form fields, icons) need at least 3:1 contrast ratio against their background. Text needs 4.5:1 (normal) or 3:1 (large).
**UI Application**: Gray border on white background: minimum #949494 (gray-500 ≈ 3:1). Icon on white: minimum #767676. Button background on white: any color darker than these thresholds.
**Common Violation**: Light gray borders (#D1D5DB, ~1.5:1 on white) that disappear for low-vision users.
**Fix**: Test all component boundaries with a contrast checker. For borders: border-color: var(--color-border-default) where the default is ≥3:1 against the surface.

### Rule 22: Color Alone Must Never Convey Information
**Source**: Inclusive Design Patterns, Heydon Pickering
**Principle**: 8% of men and 0.5% of women have color vision deficiency. Every color-coded element needs a secondary indicator (icon, label, pattern, position).
**UI Application**: Error state: red border + error icon + error text (not just red border). Chart data: color + pattern (stripes, dots) + labels. Status: colored dot + text label.
**Common Violation**: Form fields that only turn red on error, with no icon or text.
**Fix**: Every use of semantic color must have a non-color redundant signal. Audit: can a monochrome screenshot still communicate the information?

### Rule 23: Background Color Affects Text Color Perception
**Source**: Interaction of Color, Josef Albers
**Principle**: The same gray text looks darker on a white background and lighter on a dark background. Simultaneous contrast means you must adjust text colors for each background.
**UI Application**: Don't use the same gray for text on white cards and text on dark cards. On white (#FFFFFF): text at #374151. On dark (#111827): text at #D1D5DB. The mathematical darkness is very different, but perceived readability is similar.
**Common Violation**: Using a single --text-secondary color that works on light mode but becomes invisible on dark surfaces.
**Fix**: All text color tokens must have light and dark variants. Use CSS: @media (prefers-color-scheme: dark) to swap, or use a theming system with --text-secondary: light-dark(#6B7280, #9CA3AF).

### Rule 24: Temperature Creates Mood
**Source**: Color and Light, James Gurney
**Principle**: Warm colors (red, orange, yellow) advance and feel energetic. Cool colors (blue, green, purple) recede and feel calm. Neutral gray takes on the temperature of adjacent colors.
**UI Application**: Warm UI: background-color: #FFF8F0 (warm white), accent: #F97316 (orange). Cool UI: background-color: #F8FAFC (cool white), accent: #3B82F6 (blue). In oklch: shift hue toward 70-90 for warmth, 220-260 for coolness.
**Common Violation**: Mixing warm and cool accidentally — warm brand color on cool gray backgrounds creates dissonance.
**Fix**: Choose a temperature direction and apply it consistently. Warm grays: oklch(0.95 0.01 80). Cool grays: oklch(0.95 0.01 250). Even grays should have a temperature lean.

### Rule 25: Dark Surfaces Need Tinting, Not Just Darkening
**Source**: Material Design 3 (Google)
**Principle**: In dark mode, elevated surfaces should be tinted with the primary color at low opacity, not just lighter gray. This maintains color coherence between light and dark themes.
**UI Application**: Surface level 0: #121212. Level 1 (card): #121212 + primary at 5% opacity. Level 2 (raised card): #121212 + primary at 8%. Level 3 (dialog): #121212 + primary at 11%.
**Common Violation**: Dark mode surfaces that are just different grays (#1A1A1A, #2A2A2A, #3A3A3A) with no color relationship to the brand.
**Fix**: Use CSS: background-color: color-mix(in oklch, var(--surface-base), var(--primary) 5%) for surface-1, increasing the percentage for higher elevations.

### Rule 26: Limit the Palette to 3+1+1
**Source**: Universal Principles of Design, Lidwell, Holden, Butler
**Principle**: A functional UI palette needs: 3 neutrals (background, surface, text), 1 primary (brand/interactive), 1 semantic set (success, warning, error). That's the minimum AND the recommended maximum for most products.
**UI Application**: Neutrals: white, gray-100, gray-900. Primary: blue-600. Semantic: green-600, amber-500, red-600. Total: ~8 color values (not counting light/dark variants).
**Common Violation**: 5 brand colors + 8 neutral steps + 4 semantic × 5 shades each = 33 colors that no one can use consistently.
**Fix**: Start minimal. Add colors only when a functional need can't be met by existing colors. Each new color must justify its existence with a user-facing purpose.

### Rule 27: Shadows Should Be Tinted, Not Pure Black
**Source**: Refactoring UI, Adam Wathan & Steve Schoger
**Principle**: Real-world shadows aren't black — they're a darker, cooler shade of the surface color. Tinted shadows look natural; black shadows look harsh and digital.
**UI Application**: Instead of box-shadow: 0 4px 12px rgba(0,0,0,0.15), use box-shadow: 0 4px 12px oklch(0.3 0.02 250 / 0.12) — a cool, slightly blue-tinted shadow.
**Common Violation**: box-shadow: 0 2px 4px rgba(0,0,0,0.2) everywhere — creating harsh, flat-looking shadows.
**Fix**: Create a shadow token with tinting: --shadow-color: oklch(0.25 0.03 var(--primary-hue) / 0.1). Apply to all shadow values.

### Rule 28: Color Harmony Through Hue Relationships
**Source**: Interaction of Color, Josef Albers
**Principle**: Colors that share mathematical hue relationships create harmony. Complementary (180 degrees apart), analogous (30 degrees apart), triadic (120 degrees apart).
**UI Application**: In oklch, primary hue = 250 (blue). Complementary accent: hue 70 (warm yellow). Analogous secondary: hue 220 (teal) or 280 (purple). Use for data visualization and category colors.
**Common Violation**: Random hue selection — a red, a blue, a green, and a purple with no hue relationship.
**Fix**: Pick one primary hue. Derive all other hues mathematically: complementary = hue + 180, analogous = hue ± 30, triadic = hue ± 120. All in oklch.

---

## Spacing & Layout Rules (29-42)

### Rule 29: Use an 8px Spacing Scale
**Source**: Grid Systems in Graphic Design, Josef Muller-Brockmann
**Principle**: All spacing should be multiples of a base unit. 8px is the standard because it divides evenly into common screen resolutions and creates clear visual rhythm.
**UI Application**: Spacing tokens: 4px (0.25rem), 8px (0.5rem), 12px (0.75rem), 16px (1rem), 24px (1.5rem), 32px (2rem), 48px (3rem), 64px (4rem), 96px (6rem).
**Common Violation**: Arbitrary values: padding: 13px 17px; margin-bottom: 22px; gap: 9px.
**Fix**: Constrain all spacing to the scale. If 8px is too tight and 16px is too loose, use 12px (the 1.5 step). Never use a value not on the scale.

### Rule 30: Proximity Creates Grouping
**Source**: The Design of Everyday Things, Don Norman
**Principle**: Elements that are close together are perceived as related. Elements separated by more space are perceived as separate. This is Gestalt's Law of Proximity.
**UI Application**: Related form fields: gap: 8px. Between field groups: gap: 24px. Between sections: gap: 48px. The ratio between inner and outer spacing should be at least 2:1.
**Common Violation**: Uniform spacing (16px gap) between all elements, whether related or not. Everything looks equally connected.
**Fix**: Create at least 3 distinct spacing tiers: --space-within (tight), --space-between (medium), --space-apart (generous). Apply intentionally.

### Rule 31: When in Doubt, Double the Whitespace
**Source**: Refactoring UI, Adam Wathan & Steve Schoger
**Principle**: Developers and beginner designers consistently under-space. If a layout feels cramped, the fix is almost always more whitespace, not less content.
**UI Application**: If padding: 16px feels tight, try padding: 32px. If section gap is 32px, try 64px. The "professional" look often comes from generous spacing alone.
**Common Violation**: Cramming content to "above the fold." Minimal padding because "wasted space."
**Fix**: As a starting point, double all your spacing values. Then selectively tighten only where density is functionally required (data tables, toolbars).

### Rule 32: Maintain Consistent Internal Padding
**Source**: Practical UI, Adham Dannaway
**Principle**: All containers of the same type should have the same internal padding. Cards, modals, drawers, sections — each type gets a fixed padding value.
**UI Application**: Cards: padding: 24px. Modals: padding: 32px. Sections: padding: 48px 0. Buttons: padding: 10px 20px (medium). Input fields: padding: 10px 14px.
**Common Violation**: Card A has 16px padding, Card B has 24px, Card C has 20px — all on the same page.
**Fix**: Define padding tokens per container type. Enforce in component code. --card-padding: 24px. No overrides.

### Rule 33: Grids Create Order, Breaking the Grid Creates Emphasis
**Source**: Making and Breaking the Grid, Timothy Samara
**Principle**: A grid exists to create order. Breaking the grid intentionally — with one element — creates dramatic emphasis. But you must establish the grid first before breaking it.
**UI Application**: 12-column grid for page layout. All content aligns. Then: one hero element spans full bleed (breaking the grid). The break is powerful because the grid is consistent everywhere else.
**Common Violation**: No grid to begin with — everything is positioned ad hoc. No order = no ability to create emphasis through disruption.
**Fix**: Implement a grid (CSS Grid with named lines) and align everything. Then intentionally break it for 1-2 hero moments per page.

### Rule 34: Responsive Design Means Content Reflow, Not Shrinking
**Source**: Designing Interfaces, Jenifer Tidwell
**Principle**: On smaller screens, content should reflow (stack, reorder, hide secondary elements) — not just shrink. Shrinking a desktop layout to fit mobile creates unusable interfaces.
**UI Application**: 3-column → 2-column → 1-column as viewport narrows. Navigation moves from sidebar to bottom tabs. Secondary info moves to detail views.
**Common Violation**: A desktop layout scaled down to 375px width with tiny text and tiny buttons.
**Fix**: Design mobile-first. Start with the 375px layout, then ADD complexity for larger screens. Use container queries for component-level responsiveness.

### Rule 35: Consistent Alignment Creates Trust
**Source**: The Non-Designer's Design Book, Robin Williams
**Principle**: Every element should align with at least one other element. Consistent alignment creates invisible lines that organize the page and build user trust. Arbitrary placement feels chaotic.
**UI Application**: All left edges align. All right edges align. Use CSS Grid named lines: grid-template-columns: [content-start] 1fr [content-end]. Align labels, inputs, and buttons to the same grid line.
**Common Violation**: A form where labels, inputs, helper text, and buttons all have different left edges.
**Fix**: Set up a content grid. Align all elements to the same set of vertical lines. Audit by overlaying a column grid in devtools.

### Rule 36: Component Spacing > Page Spacing
**Source**: Design Systems, Alla Kholmatova
**Principle**: Spacing should be defined at the component level (internal padding, gap between elements), not the page level. When components have correct spacing, page layout becomes arrangement, not spacing.
**UI Application**: A card component defines its own padding (24px), header-to-content gap (16px), content-to-footer gap (24px). The page just defines the gap between cards (24px) and section margins (48px).
**Common Violation**: Global CSS that sets margins between arbitrary elements: h2 + p { margin-top: 12px }. Fragile and unmaintainable.
**Fix**: Each component encapsulates its own spacing. Page layout uses gap property. No margin declarations on arbitrary selectors.

### Rule 37: Touch Targets Need 48px Minimum
**Source**: Mobile First, Luke Wroblewski (also: Apple HIG: 44pt, Material: 48dp)
**Principle**: Touch targets on mobile must be large enough for a fingertip. The minimum is 48x48px (Material) or 44x44pt (Apple). This includes the total tappable area, not just the visible element.
**UI Application**: Button minimum height: 44px (iOS) or 48px (Android/Web). Invisible tap area: if an icon is 24px, add padding: 12px for a 48px touch target. List item minimum height: 48px.
**Common Violation**: 32px buttons on mobile. 24px icon buttons with no padding. Tightly spaced links.
**Fix**: Set min-height: 48px on all interactive elements. Use padding to extend touch targets beyond visible bounds. Gap between touch targets: minimum 8px.

### Rule 38: Density Should Be Intentional, Not Default
**Source**: About Face, Alan Cooper
**Principle**: Information density should match the user's expertise and task. Beginners need spacious layouts; experts need density. Density is a feature, not a compromise.
**UI Application**: Offer density preferences: compact (4px base, 32px rows), comfortable (8px base, 40px rows), spacious (12px base, 48px rows). Default to comfortable. Let users switch.
**Common Violation**: Desktop-dense layouts forced on everyone, or mobile-spacious layouts wasting expert users' screen.
**Fix**: Implement density as a CSS custom property: --density-unit: 8px. Multiply all spacing by this variable. Switch it to change density app-wide.

### Rule 39: Content Hierarchy Through Size Ratios
**Source**: Graphic Design: The New Basics, Ellen Lupton
**Principle**: Size contrast creates hierarchy. The ratio between the largest and smallest elements should be dramatic enough to be immediately clear (at least 2:1 for adjacent levels).
**UI Application**: If body text is 16px, the primary heading should be at least 32px (2:1). Display text: 48-64px (3-4:1). Caption: 12px (0.75:1). The ratio communicates importance.
**Common Violation**: H1 at 20px, H2 at 18px, body at 16px — everything looks the same size. No hierarchy.
**Fix**: Ensure at least 1.5:1 ratio between adjacent hierarchy levels. If body = 16px, then h3 ≥ 24px, h2 ≥ 32px, h1 ≥ 40px.

### Rule 40: Contain Related Elements with Borders or Background
**Source**: Layout Essentials, Beth Tondreau
**Principle**: When proximity alone isn't enough to group elements, add a visual container: a subtle background color, a border, or a card. This creates clear visual regions.
**UI Application**: Related settings: background-color: var(--surface-secondary), padding: 24px, border-radius: 12px. Or: border: 1px solid var(--border-default), padding: 24px.
**Common Violation**: Complex pages where 20+ elements float without visual grouping. Users can't parse regions.
**Fix**: Apply the "squint test" — squint and see if distinct regions are visible. If not, add visual containers around related groups.

### Rule 41: Margin Collapse Is Not a Layout Strategy
**Source**: CSS-specific best practice, industry consensus
**Principle**: Relying on CSS margin collapse (where adjacent vertical margins merge instead of stacking) creates unpredictable spacing. Use gap, padding, or explicit spacing containers instead.
**UI Application**: Use Flexbox/Grid with gap instead of margins between siblings. Use padding for container spacing. Reserve margin for document-flow text content only.
**Common Violation**: Layout built on margin-bottom on children, with collapsed margins creating "mostly correct" spacing that breaks on edge cases.
**Fix**: Replace margin-based layouts with gap-based layouts: display: flex; flex-direction: column; gap: 16px. Predictable, collapsible-proof.

### Rule 42: Aspect Ratios Should Be Consistent Across a Collection
**Source**: Layout Essentials, Beth Tondreau
**Principle**: In a grid of cards, all images should share the same aspect ratio. Mixed ratios create a ragged, unpolished grid.
**UI Application**: Use aspect-ratio CSS property: aspect-ratio: 16/9 for hero images, 4/3 for cards, 1/1 for avatars. Combine with object-fit: cover to prevent distortion.
**Common Violation**: A card grid where images are 16:9, 4:3, and 1:1, creating staggered card heights.
**Fix**: Set aspect-ratio on the image container. Let object-fit: cover handle cropping. Choose one ratio per content type.

---

## Composition & Hierarchy Rules (43-55)

### Rule 43: The Squint Test
**Source**: Universal Principles of Design, Lidwell, Holden, Butler
**Principle**: Squint at your design (or blur it in Figma). If the hierarchy, grouping, and focal points aren't immediately clear, the visual design has failed.
**UI Application**: In Figma: apply Gaussian blur (radius: 10). You should still see: (1) the primary action, (2) distinct content regions, (3) the navigation. If everything blurs into one gray mass, the design lacks hierarchy.
**Common Violation**: Designs that look "clean" but fail the squint test — everything is the same visual weight.
**Fix**: Increase contrast between hierarchy levels. Make the primary CTA larger/bolder/more saturated. Increase spacing between sections. Reduce visual weight of secondary elements.

### Rule 44: F-Pattern for Text-Heavy Pages
**Source**: Don't Make Me Think, Steve Krug
**Principle**: Users scan text-heavy pages in an F-pattern: two horizontal stripes (headline area, subhead area) followed by a vertical scan down the left edge.
**UI Application**: Place critical information in the first 2 lines. Left-align all content. Front-load headings with keywords (first 2-3 words should carry the meaning).
**Common Violation**: Centered text layouts for text-heavy content. Important content buried in the third paragraph.
**Fix**: Left-align all text content. Use headings that communicate value in the first 3 words. Place CTAs in the natural F-scan path (below the first horizontal stripe).

### Rule 45: Z-Pattern for Minimal Pages
**Source**: Don't Make Me Think, Steve Krug
**Principle**: On pages with minimal text (landing pages, login screens), users scan in a Z-pattern: top-left → top-right → bottom-left → bottom-right.
**UI Application**: Logo: top-left. Navigation/CTA: top-right. Supporting info: center. Primary CTA: bottom-right (or center-bottom). Hero image: center.
**Common Violation**: Landing page with the primary CTA in the top-left and the logo in the center — fighting the natural scan.
**Fix**: Map key elements to Z positions. Test with eye-tracking heatmaps or the 5-second test (show design for 5 seconds, ask what they noticed).

### Rule 46: One Primary Action Per Screen
**Source**: Don't Make Me Think, Steve Krug
**Principle**: Each screen should have ONE clearly dominant action. Every other action is secondary (smaller, less prominent, positioned differently).
**UI Application**: Primary CTA: solid background, primary color, large (48px height). Secondary: outlined or ghost button, neutral color. Tertiary: text link, small. Position: primary CTA in the most prominent location.
**Common Violation**: Three buttons of the same size and color at the bottom of a modal. The user doesn't know which to click.
**Fix**: Size, color, AND position should all indicate priority. Only one element per view should be the primary color at full saturation.

### Rule 47: Visual Weight Must Match Information Weight
**Source**: Universal Principles of Design, Lidwell, Holden, Butler
**Principle**: The most visually prominent element should be the most important element. If a decorative illustration is more visually prominent than the headline, the hierarchy is wrong.
**UI Application**: Audit visual weight: size + saturation + contrast + isolation. The element with the highest combined visual weight should be the primary content or action.
**Common Violation**: A large hero illustration with a small headline. Users notice the illustration first but need the headline to understand the page.
**Fix**: Ensure the headline is visually heavier than the illustration: larger size, bolder weight, higher contrast against background.

### Rule 48: Use Negative Space to Create Focal Points
**Source**: Graphic Design: The New Basics, Ellen Lupton
**Principle**: An element surrounded by more whitespace draws more attention. Whitespace is not empty — it's an active design element that directs focus.
**UI Application**: A CTA button with 48px padding around it draws more attention than one crammed between other elements. Pricing plans: add 16px more padding to the recommended plan.
**Common Violation**: Every element has equal spacing. Nothing stands out. The page is "efficient" but has no focal point.
**Fix**: Increase whitespace around the element you want to emphasize. The "featured" card: add 24px more padding than siblings.

### Rule 49: Maximum Three Levels of Visual Hierarchy
**Source**: Refactoring UI, Adam Wathan & Steve Schoger
**Principle**: At any given time, the user should parse at most three levels: primary (look here first), secondary (look here next), tertiary (look here if needed). More levels = confusion.
**UI Application**: Level 1: Hero heading / primary metric (largest, boldest, highest contrast). Level 2: Section headings / supporting data (medium size, medium weight). Level 3: Body text / metadata (normal size, reduced contrast).
**Common Violation**: Five or six levels of visual importance on one screen — display, h1, h2, h3, body, caption, footnote. Users can't parse the sequence.
**Fix**: Audit each screen. Remove or merge hierarchy levels until only 3 remain in any single viewport.

### Rule 50: The Rule of Thirds for Image Placement
**Source**: Universal Principles of Design, Lidwell, Holden, Butler
**Principle**: Divide the viewport into a 3x3 grid. Place focal points (images, CTAs, key text) at the intersections of grid lines. This creates dynamic, balanced compositions.
**UI Application**: Hero image focal point: top-right or top-left intersection. CTA button: bottom-left intersection. Headline text: aligned to left-third or top-third grid line.
**Common Violation**: Everything dead-centered, creating a static, boring composition.
**Fix**: Offset key elements slightly from center. Place hero images with the subject at a grid intersection using object-position in CSS.

### Rule 51: Repetition Creates Rhythm
**Source**: The Non-Designer's Design Book, Robin Williams
**Principle**: Repeat visual elements (color, shape, size, spacing) consistently to create rhythm. Rhythm creates unity. Break rhythm intentionally for emphasis.
**UI Application**: All cards: same border-radius (12px), same shadow, same padding (24px), same header style. The repetition creates a visual pattern. Break it for one "featured" card.
**Common Violation**: Each card has different border-radius, different padding, different shadow — no rhythm, no system.
**Fix**: Create component tokens: --card-radius, --card-padding, --card-shadow. Apply uniformly. Variants must be deliberate and limited.

### Rule 52: Contrast Creates Hierarchy, Not Decoration
**Source**: Graphic Design: The New Basics, Ellen Lupton
**Principle**: Contrast exists to communicate hierarchy — what's more important, what's different, what's actionable. Contrast that doesn't serve hierarchy is decoration.
**UI Application**: Every contrast decision answers "what is this contrast COMMUNICATING?" Bold text = important. Blue text = interactive. Larger size = primary. If contrast doesn't communicate, remove it.
**Common Violation**: Random bold words in body text. Colored elements that aren't interactive. Size differences with no hierarchical meaning.
**Fix**: Audit every bold, every color application, every size difference. Each must answer: "What does this communicate to the user?"

### Rule 53: Balance Symmetry and Asymmetry to Context
**Source**: Layout Essentials, Beth Tondreau
**Principle**: Symmetrical layouts feel stable and formal (settings, forms, dashboards). Asymmetrical layouts feel dynamic and interesting (landing pages, portfolios). Match the balance type to the content's purpose.
**UI Application**: Forms: symmetric (centered or left-aligned, uniform widths). Marketing hero: asymmetric (text left, image right, unequal columns). Dashboard: symmetric grid.
**Common Violation**: Marketing pages with symmetric, centered layouts that feel corporate and boring.
**Fix**: For marketing: 60/40 or 55/45 column splits. Text left, media right (or vice versa). Asymmetry creates visual interest.

### Rule 54: Progressive Disclosure Reduces Cognitive Load
**Source**: About Face, Alan Cooper
**Principle**: Show only the essential information initially. Provide details on demand. This reduces cognitive load and makes the interface feel simpler than it is.
**UI Application**: Settings: top-level categories → drill into details. Forms: multi-step with progress indicator. Tables: summary rows → expand for detail. Tooltips: detailed info on hover/focus.
**Common Violation**: Everything visible at once. A settings page with 40 options on a single scroll. A form with 20 fields visible.
**Fix**: Group and hide. Show 5-7 options per view. Use accordions, tabs, or multi-step flows. Each step/view should have a single clear purpose.

### Rule 55: Visual Consistency Across States
**Source**: Designing Interfaces, Jenifer Tidwell
**Principle**: Every interactive element needs 5+ visual states: default, hover, active/pressed, focus, disabled. These states must be visually distinct and consistent across all interactive elements.
**UI Application**: Button states — default: bg-blue-600. Hover: bg-blue-700 (darken 10%). Active: bg-blue-800 (darken 20%). Focus: ring-2 ring-blue-400 ring-offset-2. Disabled: bg-gray-200 text-gray-400.
**Common Violation**: No hover state. No focus ring (keyboard users stranded). Disabled state that looks like default state.
**Fix**: Define state tokens: --interactive-hover: color-mix(in oklch, var(--color), black 15%). Apply to all interactive components.

---

## Interaction & Feedback Rules (56-63)

### Rule 56: Feedback Within 100ms
**Source**: The Design of Everyday Things, Don Norman
**Principle**: Users need acknowledgment that their action was received within 100ms. After 100ms, the system feels broken. After 1 second, the user's flow of thought is interrupted.
**UI Application**: Button click: immediate visual feedback (scale: 0.97, background darken) within 16ms (one frame). Loading started indicator: within 100ms. Full response: within 1000ms ideally.
**Common Violation**: Button click with no visual response. The user doesn't know if the click registered and clicks again.
**Fix**: CSS active state: button:active { transform: scale(0.97); } — zero-JS immediate feedback. Then show loading spinner after 200ms if action hasn't completed.

### Rule 57: Map Controls to Their Effects
**Source**: The Design of Everyday Things, Don Norman
**Principle**: A control should be located near the thing it affects, and its operation should map naturally to the effect. This is "natural mapping."
**UI Application**: A sort button should be in the table header, not in a toolbar. A brightness slider should move left-to-right (dark to light). A volume control should move bottom-to-top.
**Common Violation**: An "Edit" button in a toolbar that's 400px away from the content it edits.
**Fix**: Place controls adjacent to their targets. Use inline editing where possible. If a control must be remote, use a visual connector (highlight the affected area when the control is focused).

### Rule 58: Error Prevention Over Error Recovery
**Source**: The Design of Everyday Things, Don Norman
**Principle**: It's better to prevent errors than to display good error messages. Design constraints that make errors impossible.
**UI Application**: Date picker > free text date input. Dropdown > free text for known options. Character counter > "too long" error after submission. Disable submit until form is valid.
**Common Violation**: Free text inputs for structured data (dates, phone numbers, zip codes) that allow malformed input and then show errors.
**Fix**: Use constrained input types: <input type="date">, <input type="tel">, <select>. Show inline validation before submission. Use input masks for formatted data.

### Rule 59: Three Levels of Notification Severity
**Source**: Designing Interfaces, Jenifer Tidwell
**Principle**: Notifications should match their severity: info (subtle, dismissible), warning (moderate, persistent), error/critical (prominent, blocking). Using the same treatment for all severities causes alert fatigue.
**UI Application**: Info: toast at bottom, auto-dismiss 5s, neutral color. Warning: banner at top of content area, manual dismiss, amber background. Error: inline near the cause, red, persistent until resolved. Critical: modal, blocking, requires action.
**Common Violation**: Every notification is a red alert modal. Users learn to dismiss everything without reading.
**Fix**: Define a severity scale with distinct visual treatments. Map each notification type to a severity level. Critical/blocking should be rare (1-2 types in the entire product).

### Rule 60: Visible System Status
**Source**: The Design of Everyday Things, Don Norman (also: Nielsen's Heuristic #1)
**Principle**: The system should always keep users informed about what's going on, through appropriate feedback within reasonable time.
**UI Application**: Loading: skeleton screen or spinner with context ("Loading messages..."). Progress: determinate progress bar with percentage. Sync status: "Saved" / "Saving..." / "Offline" indicator. Empty states: helpful message + action.
**Common Violation**: Blank screen while loading. No indication of save status. Empty state with no explanation.
**Fix**: Every async operation needs 3 states: loading, success, error. Every empty state needs: illustration (optional) + explanation + primary action.

### Rule 61: Undo Over Confirmation
**Source**: Sprint, Jake Knapp
**Principle**: "Are you sure?" dialogs are friction that doesn't prevent mistakes — users click through them habitually. Undo is better: let the action happen, show an undo option for 5-10 seconds.
**UI Application**: Delete: remove from view immediately, show toast "Item deleted — Undo" for 8 seconds. Archive: same pattern. Send: "Message sent — Undo" for 5 seconds.
**Common Violation**: "Are you sure you want to delete?" → Yes → actually deleted with no recovery.
**Fix**: Implement soft-delete with undo. Show a snackbar/toast with undo action. Timer bar showing remaining undo time.

### Rule 62: Skeleton Screens Over Spinners
**Source**: Lean UX, Jeff Gothelf (also: Luke Wroblewski's loading research)
**Principle**: Skeleton screens (placeholder shapes mimicking the content layout) feel faster than spinners because they set expectations about the incoming content structure.
**UI Application**: Replace loading spinners with skeleton screens that match the content layout: gray rectangles for text (height: 16px, border-radius: 4px), circles for avatars (width: 40px), rectangles for images (aspect-ratio maintained).
**Common Violation**: A centered spinner on a blank page for 2+ seconds. User has no idea what's coming.
**Fix**: Create skeleton variants for every major view. Animate with shimmer: background linear-gradient moving left to right, 1.5s duration, infinite loop.

### Rule 63: Design for the Unhappy Path
**Source**: Articulating Design Decisions, Tom Greever
**Principle**: The "happy path" (everything works perfectly) is the minority case. Design for: loading, empty, error, partial data, expired sessions, slow connections, large datasets.
**UI Application**: Every component needs: default state, loading state, empty state, error state, partial state. For lists: 0 items, 1 item, 3 items, 100 items, 10,000 items.
**Common Violation**: Beautiful designs that only work with 3 perfect-length items and a hero image.
**Fix**: Create a state matrix: [component] × [state] = specific design for each cell. No cell should be "TBD."

---

## System & Consistency Rules (64-70)

### Rule 64: Design Tokens Are the Source of Truth
**Source**: Design Systems, Alla Kholmatova
**Principle**: Every visual value (color, spacing, typography, shadow, border-radius) should be a token, not a hard-coded value. Tokens enable theming, consistency, and systematic updates.
**UI Application**: W3C DTCG format: { "color": { "primary": { "$value": "oklch(0.55 0.25 250)", "$type": "color" } } }. In CSS: var(--color-primary). Never use a raw hex, px, or rem value in component code.
**Common Violation**: Hundreds of hard-coded #3B82F6 values scattered across components. Changing the brand color means find-and-replace.
**Fix**: Audit all visual values. Extract to tokens. Reference tokens in all component code. A color change should require editing ONE token file.

### Rule 65: Naming Convention: Category-Property-Modifier
**Source**: Design Systems, Alla Kholmatova
**Principle**: Token names should follow a consistent pattern: [category]-[property]-[modifier]. This creates predictable, discoverable naming.
**UI Application**: --color-text-primary, --color-text-secondary, --color-bg-surface, --color-bg-elevated, --space-gap-sm, --space-gap-md, --radius-component-sm, --shadow-elevation-1.
**Common Violation**: --blue, --big-padding, --card-shadow-thing, --my-border — no convention, no discoverability.
**Fix**: Define the naming convention. Document it. Enforce it in code review. A new team member should be able to predict the token name.

### Rule 66: Components Own Their Spacing
**Source**: Design Systems, Alla Kholmatova
**Principle**: A component should define its internal spacing and have zero external margin. The parent layout controls the space between components using gap or padding.
**UI Application**: Button: padding: var(--space-2) var(--space-4); margin: 0. Card: padding: var(--space-6); margin: 0. Parent: display: flex; gap: var(--space-4).
**Common Violation**: Components with margin-bottom that creates unexpected spacing when composed differently.
**Fix**: Remove all margin from components. Use layout components (Stack, Cluster, Grid) that apply gap.

### Rule 67: Visual Consistency Requires Constraint
**Source**: Universal Principles of Design, Lidwell, Holden, Butler
**Principle**: Consistency doesn't happen through guidelines — it happens through constraint. Limit the available options so that misuse is impossible.
**UI Application**: If the design system has 3 button sizes, the component API should only accept "sm" | "md" | "lg" — not arbitrary pixel values. If there are 5 border-radius values, the token scale has 5 entries, period.
**Common Violation**: Design system with guidelines ("use 8px border-radius") but no enforcement. Developers use 6px, 10px, 12px.
**Fix**: Tokens are the constraint. If a value isn't a token, it's a bug. Lint rules: no raw px/rem/hex values in component files.

### Rule 68: Test Designs with Real Content
**Source**: Lean UX, Jeff Gothelf
**Principle**: Designs tested with "Lorem ipsum" and placeholder images mask real problems: text overflow, varying content lengths, missing images, long names, empty states.
**UI Application**: Test with: real user names (including long names like "Alexander Alexandropoulos"), real content at 0.5x, 1x, and 3x expected length, missing images (broken src), RTL text if supporting i18n.
**Common Violation**: Beautiful mockup with "John Smith" that breaks when the user's name is "Muhammad Al-Rashid bin Abdullah."
**Fix**: Create content stress tests: longest possible name, longest possible title, empty content, single-character content, special characters, emoji-heavy content.

### Rule 69: Document the Why, Not Just the What
**Source**: Articulating Design Decisions, Tom Greever
**Principle**: A design system that says "use 8px border-radius" is less useful than one that says "use 8px border-radius because it matches our brand personality of 'precise but approachable' and aligns with our 8px spacing grid."
**UI Application**: Each token/pattern should have: the value, the rationale, the context where it applies, and what NOT to do. Example: "--radius-md: 8px. Used for interactive containers (buttons, inputs, cards). Aligns with 8px grid. Don't use for avatars (use --radius-full)."
**Common Violation**: Token files with values but no documentation. New team members don't know when to use --space-3 vs --space-4.
**Fix**: Add usage notes to token definitions. Reference rules by number: "Based on Rule 29 (8px spacing scale)."

### Rule 70: The 5-Second Test for Visual Hierarchy
**Source**: Don't Make Me Think, Steve Krug
**Principle**: Show a new user the design for 5 seconds. Then hide it and ask: What is this page about? What's the main action? What sections did you notice? If they can't answer, the visual hierarchy has failed.
**UI Application**: Apply to every major screen. The 5-second answers should match your design intent. If you intended the CTA to be primary, users should mention it first.
**Common Violation**: Designs that require study to understand. If users need more than 5 seconds to parse the page structure, they'll leave.
**Fix**: Run the 5-second test with 3-5 people. If the answers don't match your intent, increase the visual weight of the intended focal point and decrease everything else.
