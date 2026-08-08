# Generation Pipelines — Multi-Step Design Workflows

This reference covers how to orchestrate multi-step AI generation workflows that produce consistent, high-quality design output. Single generations rarely produce production-ready results — pipelines combine multiple steps (context extraction, specification, generation, scoring, iteration, code conversion) into reliable workflows.

---

## Pipeline Architecture

Every generation pipeline follows the same six-stage structure:

```
Stage 1: Context Extraction
  Input: existing design, brand guidelines, sector norms, or user description
  Action: extract design context (colors, typography, spacing, patterns)
  Output: design context document

Stage 2: Specification
  Input: design context + user request
  Action: generate detailed design specification using Sumi's design intelligence
  Output: complete prompt with all sections (subject, platform, tokens, content, states)

Stage 3: Generation
  Input: specification/prompt
  Action: AI tool creates the visual output
  Output: generated design (HTML/CSS from Stitch, image from Fal.ai/OpenAI)

Stage 4: Quality Scoring
  Input: generated design
  Action: evaluate against 10-dimension visual scoring framework
  Output: score card with per-dimension ratings and findings

Stage 5: Iteration
  Input: score card + original specification
  Action: identify weakest dimensions, adjust prompt, regenerate
  Output: improved generation (repeat until score >= threshold or max iterations)

Stage 6: Code Conversion
  Input: approved design
  Action: convert to production code (React, SwiftUI, HTML/CSS)
  Output: production-ready component/screen
```

Not every pipeline uses all six stages. Wireframe exploration might stop at Stage 3. A full production pipeline uses all six.

---

## Single-Tool Pipelines

### Stitch-Only Pipeline
Best for: rapid prototyping, landing pages, multi-screen apps.

```
1. [Optional] extract_design_context from existing design or URL
2. Write detailed screen description (see prompt-engineering-visual.md)
3. generate_screen_from_text with description + design context
4. Review generated HTML/CSS in browser
5. Identify issues (layout, colors, content, spacing)
6. Adjust description and regenerate (max 3 iterations)
7. Extract final HTML/CSS for production use or as reference for /ship
```

**Tips:**
- Always provide design context for style consistency
- Start with a single screen before generating multi-page sites
- Use build_site only after you have established style with a single screen
- Review on multiple viewport widths if responsive is enabled

### Fal.ai FLUX-Only Pipeline
Best for: hero images, product photography, illustrations.

```
1. Choose model based on task (FLUX Pro for quality, Dev for speed)
2. Write image prompt with style, composition, and color specifications
3. Generate 2-3 variants (different seeds or slight prompt variations)
4. Score variants against design requirements
5. Select best variant
6. [Optional] Upscale if needed (via Replicate Real-ESRGAN)
7. Optimize for web (compress, convert to WebP)
```

### Figma-Only Pipeline
Best for: design system analysis, spec extraction, design audit.

```
1. get_file to retrieve Figma file structure
2. get_file_styles to extract color and text styles
3. get_file_components to map component library
4. Analyze design system for consistency and completeness
5. get_images to export specific frames as images
6. Generate report with findings and recommendations
7. [Optional] post_comment with feedback on specific frames
```

---

## Multi-Tool Pipelines

### Full Screen Generation Pipeline
Tools: Stitch + Fal.ai + Figma MCP
Best for: complete screen with custom assets.

```
Step 1: Context (Figma MCP or Stitch)
  - If Figma file exists: extract design context from Figma via get_file_styles
  - If no Figma file: use Stitch extract_design_context from reference URL
  - Output: design context document with colors, typography, spacing, patterns

Step 2: Screen Layout (Stitch)
  - Generate screen layout with Stitch using design context
  - Include placeholder references for images and icons
  - Review and iterate on layout (1-2 rounds)
  - Output: approved screen layout in HTML/CSS

Step 3: Icon Generation (Fal.ai — Recraft V3)
  - Identify icons needed from the screen layout
  - Generate icon set with Recraft V3 (SVG output)
  - Ensure consistent style across all icons (same prompt prefix)
  - Output: SVG icon files

Step 4: Image Generation (Fal.ai — FLUX Pro or Imagen 4)
  - Identify images needed (hero, product shots, avatars, illustrations)
  - Generate each image with appropriate model
  - Match color temperature and mood to the screen's design tokens
  - Output: optimized image files (WebP)

Step 5: Assembly
  - Replace placeholder assets in Stitch output with generated icons and images
  - Verify visual coherence of the complete screen
  - Score against 10-dimension framework
  - Output: complete screen with all assets

Step 6: Code Conversion
  - Use /ship to convert approved screen to production code
  - Replace Stitch HTML/CSS with React/SwiftUI/production framework
  - Integrate generated assets into component tree
  - Output: production-ready code
```

### Asset Library Pipeline
Tools: Fal.ai (Recraft V3 + FLUX Pro + Imagen 4 + Veo 3.1)
Best for: generating a complete set of design assets for a project.

```
Step 1: Define Asset Manifest
  - List all needed assets by type: icons, illustrations, photos, videos
  - For each asset: purpose, size, style requirements
  - Define style constraints that apply to all assets

Step 2: Icon Set (Recraft V3)
  - Generate all icons with consistent style prompt prefix
  - Verify: consistent stroke width, grid alignment, recognizability
  - Export as optimized SVG
  - Batch: generate 10-20 icons per session

Step 3: Illustrations (FLUX Pro or GPT-Image)
  - Generate illustrations with consistent style (same style prefix)
  - Use cases: empty states, onboarding, feature highlights, error pages
  - Verify: palette matches design tokens, style consistent across set
  - Export as optimized WebP/PNG

Step 4: Photography (Imagen 4 or FLUX Pro)
  - Generate product photos, lifestyle images, hero imagery
  - Verify: color temperature matches palette, no artifacts
  - Export at appropriate resolution for target display sizes
  - Generate 2x versions for retina displays

Step 5: Video/Motion (Veo 3.1)
  - Generate motion concepts for key interactions
  - Verify: smooth motion, consistent style
  - Export as compressed MP4/WebM
  - Note: these are concept references, not production animations

Step 6: Asset Library Assembly
  - Organize all assets by type and purpose
  - Create asset manifest with metadata (size, format, usage notes)
  - Verify cross-asset consistency (colors, mood, style)
  - Output: organized asset library ready for integration
```

### Design System Extraction + Generation Pipeline
Tools: Figma MCP + Stitch
Best for: generating new screens that match an existing design system.

```
Step 1: Extract from Figma
  - get_file_styles: all color styles, text styles, effect styles
  - get_file_components: all components with properties and variants
  - get_images: export key screens as reference images

Step 2: Build Design Context
  - Convert Figma styles to design context format
  - Map component patterns to Sumi's pattern vocabulary
  - Identify design system rules (spacing grid, radius scale, shadow hierarchy)

Step 3: Generate New Screens
  - Use Stitch with extracted design context
  - Generate screens that the existing design system needs but does not have
  - Ensure every generated screen uses only the extracted design tokens

Step 4: Consistency Verification
  - Compare generated screens against existing Figma screens
  - Score for token consistency (colors, fonts, spacing match?)
  - Score for pattern consistency (navigation, headers, footers match?)
  - Flag any deviations for manual review

Step 5: Handoff
  - Export approved screens as specifications for implementation
  - Include exact design token references for each element
  - Note any new patterns introduced that need design system documentation
```

---

## Design System Consistency Across Generations

The biggest risk with multi-screen generation is style drift — each generation looks slightly different. Prevent this with:

### Style Lock Document
Create a "style lock" before generating multiple screens:

```
=== STYLE LOCK: [Project Name] ===

Color Palette (exact values, no variation):
  Primary: #6366F1
  Primary hover: #4F46E5
  Primary text-on: #FFFFFF
  Secondary: #EC4899
  Surface: #FFFFFF
  Surface elevated: #F8FAFC
  Surface sunken: #F1F5F9
  Border: #E2E8F0
  Text primary: #0F172A
  Text secondary: #64748B
  Text tertiary: #94A3B8

Typography (exact specifications):
  Font: Inter
  H1: 32px / 1.2 / 700
  H2: 24px / 1.3 / 600
  H3: 18px / 1.3 / 600
  Body: 16px / 1.5 / 400
  Body small: 14px / 1.5 / 400
  Caption: 12px / 1.4 / 500
  Mono: JetBrains Mono, 14px / 1.5 / 400

Spacing (8px grid, no exceptions):
  4, 8, 12, 16, 20, 24, 32, 40, 48, 64

Border Radius:
  Small (inputs, tags): 6px
  Medium (cards, panels): 8px
  Large (modals, sheets): 12px
  Pill (badges, pills): 9999px

Shadows:
  sm: 0 1px 2px rgba(0,0,0,0.05)
  md: 0 4px 6px -1px rgba(0,0,0,0.07)
  lg: 0 10px 15px -3px rgba(0,0,0,0.1)

Component Patterns:
  Buttons: pill radius, 40px height (default), 32px (small), 48px (large)
  Inputs: 6px radius, 40px height, 1px border, focus ring 2px primary
  Cards: 8px radius, 1px border, surface elevated background
  Navigation: sidebar 256px, top bar 64px, bottom tab bar 48px (mobile)

Icons: SF Symbols style, 1.5px stroke, rounded caps, 24px default grid
===
```

### Context Injection Protocol
For every screen in a multi-screen generation:
1. Include the full style lock document in the prompt
2. Reference the first generated screen as the style anchor
3. Specify shared elements explicitly (navigation, headers, footers)
4. After generation, diff the token usage against the style lock

### Cross-Screen Verification Checklist
After generating a set of screens, verify:
- [ ] Same background color on all screens
- [ ] Same navigation component on all screens with nav
- [ ] Same header height and style on all screens
- [ ] Same font family, sizes, and weights
- [ ] Same spacing values (measure padding, margins, gaps)
- [ ] Same border radius values
- [ ] Same shadow values
- [ ] Same button styles (size, color, radius, text style)
- [ ] Same input styles
- [ ] Same color usage patterns (primary for CTAs, secondary for links, etc.)

---

## Batch Generation for Screen Families

### Protocol for Generating 5-10 Screens of an App

```
Preparation:
1. Create style lock document
2. Define all screens with names and purposes
3. Identify shared elements (navigation, headers, footers)
4. Establish content strategy (realistic content for each screen)

Generation Order (critical for consistency):
1. FIRST: Generate the most complex screen (usually dashboard or main view)
   - This establishes the design language
   - Score and iterate until satisfactory
   - Extract design context from this screen

2. SECOND: Generate shared shell (navigation + header + footer)
   - If not already part of the first screen
   - This becomes the wrapper for all subsequent screens

3. THEN: Generate remaining screens in dependency order
   - Screens that share layouts generate together
   - Include style lock + reference to first screen in every prompt
   - Generate 2-3 per session to maintain context

4. FINALLY: Cross-screen consistency review
   - View all screens side by side
   - Run cross-screen verification checklist
   - Regenerate any that deviate from the style lock
```

---

## Pipeline Templates

### 1. Landing Page Pipeline

**Input:** Product description, brand colors, target audience.
**Time:** 15-30 minutes with MCP tools.

```
Step 1: /taste
  Identify sector visual direction and style benchmarks

Step 2: Design Context
  Extract or build design context (colors, typography, spacing)
  Create style lock document

Step 3: /generate with Stitch
  Provide complete landing page prompt (see prompt templates)
  Include: hero, social proof, features, how-it-works, testimonial, pricing, CTA, footer
  Use design context from Step 2

Step 4: Score
  10-dimension visual scoring
  Minimum threshold: 7/10 for client presentation

Step 5: Iterate (if needed)
  Adjust prompt based on weakest scoring dimensions
  Regenerate (max 2 iterations)

Step 6: Assets
  Generate hero image with FLUX Pro or Imagen 4
  Generate feature icons with Recraft V3 (SVG)
  Replace placeholders in Stitch output

Step 7: /ship
  Convert approved design to production React/HTML
  Optimize assets (WebP, lazy loading)
  Output: deployable landing page
```

### 2. Dashboard Pipeline

**Input:** Data types, user role, key metrics.
**Time:** 20-40 minutes with MCP tools.

```
Step 1: Screen specification
  Identify required dashboard components (KPI cards, charts, tables, feeds)
  Map data to visual patterns

Step 2: Design context
  Extract from existing design system or build from scratch
  Define chart color palette (accessible, distinguishable)

Step 3: Generate with Stitch
  Sidebar + header + metric cards + chart area + table + activity feed
  Use realistic data in prompt (not placeholder numbers)

Step 4: Score
  10-dimension visual scoring + usability heuristic check
  Minimum: 7/10 overall, 8/10 for hierarchy and typography

Step 5: Iterate
  Common dashboard issues: information density too high/low, chart unreadable, poor hierarchy

Step 6: /ship
  Convert to production components
  Integrate with data visualization library (Recharts, D3, Chart.js)
  Wire up to real data endpoints
```

### 3. Mobile App Pipeline

**Input:** App concept, platform (iOS/Android), core user flows.
**Time:** 30-60 minutes with MCP tools (5-8 screens).

```
Step 1: Visual direction
  Sector style, platform conventions (iOS 26 Liquid Glass / Material 3 Expressive)
  Create style lock document with platform-specific tokens

Step 2: Flow mapping
  Map core user flows to screens
  Identify screen types needed (list, detail, form, empty, error, onboarding)

Step 3: Generate anchor screen
  Generate the most important screen first (usually the main/home screen)
  Iterate until quality threshold met
  Extract design context

Step 4: Generate remaining screens
  Generate each screen with style lock + design context
  Batch related screens (all list screens together, all form screens together)
  2-3 screens per generation session

Step 5: Cross-screen consistency check
  Navigation consistent, tab bar matches, colors and fonts consistent
  Fix any deviations before proceeding

Step 6: /ship for production
  Convert each screen to SwiftUI (iOS) or Jetpack Compose (Android)
  Build reusable components for shared elements
  Integrate navigation flow
```

### 4. Design System Pipeline

**Input:** Brand guidelines, target platforms.
**Time:** 45-90 minutes with MCP tools.

```
Step 1: /drip for token system
  Define complete design token set from brand guidelines
  Color, typography, spacing, radius, shadow, motion tokens
  Export as W3C design tokens JSON

Step 2: Generate core components
  Use Stitch to generate each core component with all variants:
  - Buttons (primary, secondary, tertiary, ghost + sizes + states)
  - Inputs (text, select, checkbox, radio, toggle + states)
  - Cards (default, interactive, media, compact)
  - Navigation (top bar, sidebar, tab bar, breadcrumb)
  - Feedback (alerts, toasts, dialogs, banners)

Step 3: Asset generation
  Recraft V3 for icon set (16-24 core icons in SVG)
  FLUX/Imagen for illustration set (4-6 empty state illustrations)

Step 4: Consistency audit
  Score all components for token consistency
  Verify all states are covered
  Verify accessibility (contrast, touch targets)

Step 5: /ship component library
  Convert each component to production code
  Build Storybook or equivalent documentation
  Export Figma integration if Figma MCP available
```

---

## When NOT to Use Generation

AI generation is powerful but not appropriate for every design task. Prefer manual design or direct coding when:

| Scenario | Why Skip Generation | Better Approach |
|----------|-------------------|-----------------|
| Complex interactive components | Generation cannot show real interactions | Build directly with /ship |
| Accessibility-critical flows | Must be verified by hand, not approximated | Generate then audit with /include |
| Data-heavy tables and grids | Better to code directly with real data | /ship with data visualization library |
| Design system tokens | Tokens are specifications, not visuals | /drip for token generation |
| Strict brand guidelines | Generation may deviate from exact specs | Use generation as reference, implement manually |
| Animation and micro-interactions | Generation produces static output | Specify with /motion, implement in code |
| Highly custom layouts | Generation defaults to common patterns | Manual layout design + /ship |
| Legal/compliance UIs | Must match exact regulatory requirements | Manual implementation with legal review |

### The 70/30 Rule
AI generation can get you 70% of the way to a final design in 10% of the time. The remaining 30% — refinement, polish, edge cases, accessibility, interaction details — requires design intelligence and manual work. Use generation for the 70%, Sumi's skills for the 30%.
