---
name: Visual Design Mastery
description: "World-class visual design intelligence — 36+ designer pattern libraries, 70 canonical design rules from 23 books, 10-dimension visual scoring framework (Awwwards-calibrated), deep color science (oklch, HCT, Dynamic Color), typography systems (variable fonts, fluid scales, optical sizing), and composition mastery (Swiss grid, golden ratio, visual weight). Use when the user mentions: visual design, make it look better, professional design, designer quality, color palette, typography, spacing, grid, layout, visual hierarchy, design score, design quality, polish, craft, aesthetic, beautiful, ugly, looks bad, looks cheap, visual direction, design system visuals, brand identity, visual identity, color theory, type scale."
---

# Visual Design Mastery

## Why Visual Design Mastery Matters

The gap between a vibe-coded app and a professionally designed product is visual design mastery. Not subjective taste — learnable, systematic craft. Every world-class designer applies a finite set of principles consistently: typographic hierarchy, color harmony, spatial rhythm, compositional balance, and material craft. This skill codifies those principles from 36+ designers and 23 canonical books into teachable, measurable intelligence.

## Reference Architecture

| File | Contents | Use When |
|------|----------|----------|
| `references/designer-pattern-library.md` | 36+ world-class designers organized by era and style. Each: signature visual patterns, design philosophy, teachable techniques across 8 categories (typography, color, spacing, composition, motion, material, iconography, craft). Designers include: Dieter Rams, Massimo Vignelli, Josef Muller-Brockmann, Jony Ive, Mike Matas, Rasmus Andersson, Tobias van Schneider, Claudio Guglieri, Julie Zhuo, Luke Wroblewski, and 26+ more. | Matching a visual direction to designer archetypes. Explaining WHY a design choice works by citing the designer who pioneered it. Generating designer-informed recommendations. |
| `references/canonical-design-rules.md` | 70 rules extracted from 23 canonical design books: Grid Systems (Muller-Brockmann), Thinking with Type (Lupton), Interaction of Color (Albers), Design of Everyday Things (Norman), Refactoring UI (Wathan/Schoger), Laws of UX (Yablonski), Universal Principles of Design, and 16 more. Each rule: source, principle, application to UI, common violation, fix. | Grounding visual design recommendations in published authority. Teaching users WHY spacing/type/color rules exist. |
| `references/visual-scoring-framework.md` | 10-dimension visual quality scoring system calibrated to Awwwards (4-criterion), Red Dot, and iF Design Award standards. Dimensions: Typography, Color, Spacing, Composition, Imagery, Iconography, Motion, Polish, Coherence, Craft. Each dimension: scoring rubric (1-10), what each score looks like, benchmark examples, common vibe-coder failures. Weighted overall score formula. | Scoring any UI's visual quality. Powering the `/visual-score` command. Benchmarking against award-winning products. |
| `references/color-mastery.md` | Deep color science for UI: oklch() and LCH color spaces (perceptually uniform), HCT (Material 3's Hue-Chroma-Tone), Dynamic Color (wallpaper extraction), accessible palette generation (APCA contrast), P3 wide gamut, dark mode color mapping, semantic color systems, color harmony algorithms (complementary, analogous, triadic, split-complementary). | Generating color palettes, auditing color usage, fixing contrast issues, building dark mode, creating brand-aligned color systems. |
| `references/typography-mastery.md` | Typography systems for UI: variable fonts (weight, width, optical size axes), fluid type scales (clamp-based), modular scales (ratios), platform-native font stacks, optical alignment, text rendering (subpixel, antialiasing), responsive typography, typographic hierarchy (6-level system), line-height and measure optimization, font pairing rules, web font performance. | Building type systems, auditing typography, recommending font pairings, fixing readability issues, creating responsive type scales. |
| `references/composition-mastery.md` | Layout and composition: Swiss/International grid systems, 8px baseline grid, golden ratio applications, rule of thirds, visual weight distribution, whitespace as design element, density control (compact/comfortable/spacious), responsive grid systems (12-column, CSS Grid, Flexbox), visual hierarchy techniques (size, weight, color, position, contrast), z-pattern and f-pattern scanning, Gestalt grouping in layouts. | Building grid systems, auditing layout quality, fixing visual hierarchy, creating balanced compositions, managing information density. |

## Cross-References

- **`ui-pattern-intelligence`** — Pattern-level analysis. This skill provides the visual quality lens that evaluates HOW patterns are executed visually.
- **`sector-style-intelligence`** — Sector visual norms. This skill provides the deeper craft principles that APPLY within any sector direction.
- **`design-systems-architecture`** — Token architecture. This skill defines the visual VALUES that tokens encode.
- **`component-patterns-code`** — Component code. This skill ensures components are visually excellent, not just functionally correct.
- **`cognitive-psychology-ux`** — Why visual design choices work, grounded in perception science.
- **`interaction-motion-design`** — Motion as a visual design element.
- **`accessibility-inclusive-design`** — Ensuring visual excellence doesn't compromise accessibility.

## Commands Powered by This Skill

| Command | How This Skill Is Used |
|---------|----------------------|
| `/vision` | Primary command — generates complete visual design direction using designer DNA + canonical rules |
| `/visual-score` | Scores visual quality using the 10-dimension framework |
| `/taste` | Enhanced with designer pattern library for richer style direction |
| `/drip` | Enhanced with color/typography mastery for better token generation |
| `/ship` | Enhanced with composition mastery for better component visual quality |
| `/roast` | References canonical rules during design critique |
| `/judge` | Visual scoring contributes to overall design score |
