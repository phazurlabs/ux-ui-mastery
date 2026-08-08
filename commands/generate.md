---
name: generate
description: "AI design generation — mockups, icons, illustrations, images via Stitch MCP, Fal.ai, Recraft V3, Veo 3.1"
argument-hint: "[asset type and description]"
---

# Generate — AI Design Generation Engine

## Before running

This command needs an asset type and a description of what to generate.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate UI screens, icons, illustrations, photographs, video, and brand assets using AI tools (MCP servers), informed by Sumi's full design intelligence stack. This command merges screen generation and asset generation into a single, unified pipeline.

## Design Memory Integration

Before generating, check for `.sumi/` in the user's project root:

- **`.sumi/style.json`** — If present, inject design tokens into every generation prompt: hex colors, font families, spacing values, border radii, shadow values. Style-lock all prompts to these tokens.
- **`.sumi/wireframe-*.json`** — If present, use the layout structure and component map to inform screen generation prompts. The wireframe defines WHAT goes where; generation defines HOW it looks.
- **`.sumi/brief.json`** — If present, pull product description, sector, target users, and platform. Use sector for style-matching and visual expectations.
- **`.sumi/vision.json`** — If present, pull visual direction, designer DNA match, mood, and canonical rules. This is the primary style source for generation.
- **`.sumi/decisions.log`** — If present, read prior design decisions to maintain consistency.

After generation is approved, write to `.sumi/`:
```json
// .sumi/generated-[asset-name].json
{
  "type": "screen|icon|illustration|photo|video|brand",
  "prompt": "the exact prompt used",
  "tool": "stitch|fal-flux|fal-imagen|fal-recraft|fal-veo|gpt-image|manual",
  "styleLock": { "colors": [], "style": "", "mood": "" },
  "score": 0,
  "approved": false,
  "timestamp": "ISO-8601"
}
```

---

## Sub-Modes

This command operates in 7 sub-modes. The user specifies which mode, or describe what they need and the command auto-detects:

| Mode | Trigger | Output |
|------|---------|--------|
| **Screen Mockup** | "generate a dashboard", "mockup for settings page" | High-fidelity UI screen image |
| **Icon Set** | "generate icons for...", "icon set for navigation" | SVG vector icons (consistent set) |
| **Illustration** | "illustration for onboarding", "hero illustration" | Styled illustration matching brand |
| **Hero Image** | "hero image for landing page", "product shot" | Photographic or stylized hero image |
| **Product Photo** | "product photo for...", "lifestyle shot" | Photorealistic product photography |
| **Video** | "generate a video for...", "motion asset" | Short video clip (2-8 seconds) |
| **Figma Import** | "import from Figma", "Figma to code", "convert Figma" | Production code from Figma designs via MCP |

---

## Sub-Mode 7: Figma Import (MCP Bridge)

Import designs from Figma via MCP, audit them with Sumi's design intelligence, and export production-ready code.

**Trigger**: "import from Figma", "Figma to code", "convert this Figma design"

### Prerequisites

Requires one of the following MCP servers configured:
- `figma-mcp` — Official Figma MCP server
- `figma-developer` — Community Figma Developer MCP
- Direct Figma API access via personal access token

If no Figma MCP is configured, instruct the user:
```
To connect Figma, add to your Claude Code MCP config:

{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp"],
      "env": {
        "FIGMA_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Import Protocol

**Step 1: Extract from Figma**
- Accept a Figma file URL, frame URL, or node ID
- Use the MCP server to fetch:
  - Component tree structure
  - Colors (fill, stroke, effects)
  - Typography (font family, size, weight, line height, letter spacing)
  - Spacing (padding, gaps, auto layout properties)
  - Border radius values
  - Shadow/effect values
  - Asset references (images, icons)
  - Component variants and properties

**Step 2: Map to Sumi Tokens**
- Convert Figma colors to oklch values with hex fallbacks
- Map Figma text styles to type scale tokens
- Convert Figma auto layout spacing to spacing scale values
- Map Figma effects to shadow tokens
- Map Figma corner radius to radius tokens
- Identify the closest Sumi sector match based on visual patterns
- If `.sumi/style.json` exists, map Figma values to existing tokens (flag mismatches)

**Step 3: Audit the Figma Design**
Before generating code, run a silent design quality check:
- Color contrast: Do text/background pairs meet WCAG AA?
- Typography: Is there a consistent type scale or random sizes?
- Spacing: Does it follow a grid or use arbitrary values?
- Consistency: Are similar components styled consistently?
- Accessibility: Are interactive elements properly sized (44px+ tap targets)?
- Output any issues found as warnings before generating code

**Step 4: Generate Production Code**
Generate code using the same protocol as `/screen` or `/component`:
- React + TypeScript + Tailwind (default for web)
- SwiftUI (if iOS signals detected)
- Jetpack Compose (if Android signals detected)
- Apply all Sumi quality standards:
  - Semantic color tokens (not raw hex values)
  - Type scale tokens (not arbitrary font sizes)
  - Spacing scale tokens (not random padding)
  - All interactive states (hover, focus, active, disabled, loading)
  - Full accessibility (ARIA, keyboard nav, focus management)
  - Responsive breakpoints
  - Dark mode support

**Step 5: Save Extracted Tokens**
If no `.sumi/style.json` exists, generate one from the Figma design:
- Extract the color palette into token format
- Extract typography into type scale
- Extract spacing into grid scale
- Save to `.sumi/style.json` for use by all other commands

### Output Format

```
## Figma Import — [Frame/Component Name]

### Extracted Design Values
| Category | Figma Value | Sumi Token | Status |
|----------|-------------|-----------------|--------|
| Primary Color | #2563EB | oklch(0.55 0.18 255) → --color-primary | ✅ Mapped |
| Body Font | Inter 16/24 | --font-body, --text-base | ✅ Mapped |
| Card Radius | 12px | --radius-lg | ✅ Mapped |
| Spacing | 17px | ⚠️ Off-grid (nearest: 16px → --space-4) | ⚠️ Adjusted |

### Design Quality Warnings
[Any issues found in Step 3]

### Generated Code
[Full production code]

### Saved Tokens
[If .sumi/style.json was generated]
```

### Integration Notes
- After Figma import, suggest running `/grade` to score the output
- If Figma design has quality issues, suggest `/fix` after import
- Figma token extraction feeds directly into `/tokens` for W3C DTCG export

---

## Analysis Protocol

### Step 0: Gather Context & Check MCP Availability

Before generating anything, collect:

1. **What to generate**: Type (screen/icon/illustration/photo/video), description, purpose, target audience.
2. **Platform**: iOS, Android, Web — affects screen generation constraints (safe areas, navigation patterns, status bars).
3. **Sector**: Auto-detect from context or `.sumi/brief.json`. Sector determines visual expectations, pattern norms, and style benchmarks.
4. **Design tokens**: From `.sumi/style.json` or `/tokens` — inject specific values (hex colors, font sizes, spacing, radii) into prompts.
5. **Visual direction**: From `.sumi/vision.json` or `/grade` — designer DNA match, mood, canonical rules, reference products.
6. **Prior Sumi outputs**: Consume `/grade` (visual direction), `/style` (competitive landscape), `/screen` (screen specs), `/wireframe` (layout structure) if available.

7. **Check MCP availability**: Detect which MCP servers are configured:

| MCP Server | Capability | Best For |
|------------|-----------|----------|
| **Stitch MCP** | Full screen generation from text | Complete UI screens, multi-screen flows |
| **Fal.ai — FLUX Pro** | High-quality image generation | Stylized mockups, hero images, illustrations |
| **Fal.ai — Imagen 4** | Photorealistic image generation | Product photos, lifestyle shots, realistic scenes |
| **Fal.ai — Recraft V3** | Vector SVG generation | Icons, logos, vector illustrations (ONLY vector-capable model) |
| **Fal.ai — Veo 3.1** | Video generation (up to 8s) | Motion assets, UI animations, product videos |
| **OpenAI GPT-Image** | Image with embedded text | Illustrations with labels, diagrams, text-in-image |
| **Figma MCP** | Design file read/write | Component creation, design system integration |

If **NO MCP available**: Output a detailed specification + optimized prompt that the user can use manually with their tool of choice. The prompt is the product.

If the user provides only a vague request, ask clarifying questions:
- For screens: What is the screen's purpose? What are the key elements? What platform?
- For icons: How many? What do they represent? What style (outlined/filled/duotone)? What size?
- For illustrations: What scene/concept? What mood? What style? Where will it appear?
- For photos: What subject? What lighting? What mood? What context?
- For video: What action? How long? What style? Loop or one-shot?

---

### Step 1: SPECIFY — Build Design-Informed Specification

Using Sumi's design intelligence, build a complete specification for the requested asset:

#### For Screen Mockups

- **Screen type**: From `screen-flow-patterns` skill — dashboard, settings, profile, onboarding, detail view, list view, checkout, etc.
- **Required patterns**: From `ui-pattern-intelligence` — navigation, data display, input, feedback, layout patterns for this screen type
- **Visual direction**: From `visual-design-mastery` — designer DNA match, canonical rules, color system, typography scale
- **Platform conventions**: From `platform-visual-standards` — iOS HIG (Liquid Glass for iOS 26), Material 3 Expressive, or Web conventions
- **Sector expectations**: From `sector-style-intelligence` — visual treatment, density, tone, patterns expected in this industry
- **Content strategy**: Real or realistic content throughout — never lorem ipsum. Use plausible names, numbers, dates, and copy that reflects the actual product domain
- **State coverage**: Which states to generate — default, empty, loading, error, success. Default is always generated.
- **Layout structure**: From `.sumi/wireframe-*.json` if available — component positions, regions, responsive rules

#### For Icon Sets

- **Icon inventory**: List every icon needed with its meaning
- **Style**: Outlined (1.5px stroke default), filled, duotone, or mixed
- **Grid**: 24x24px default (16px for compact, 32px for display)
- **Stroke width**: Consistent across all icons (1px, 1.5px, or 2px)
- **Corner radius**: Consistent across all icons (2px default)
- **Color**: Single color (from tokens), duotone (primary + secondary), or multi-color
- **Optical balance**: All icons should have equal visual weight at the same size
- **Metaphor check**: Each icon's metaphor should be universally understood (avoid cultural assumptions)

#### For Illustrations

- **Scene/concept**: What the illustration depicts
- **Style**: Flat, isometric, 3D, hand-drawn, geometric, abstract, photorealistic
- **Color palette**: Locked to design tokens or specified palette
- **Mood**: Playful, professional, warm, minimal, energetic, calm
- **Character style** (if people): Geometric, realistic, cartoon, abstract
- **Level of detail**: Simple (icon-like), moderate (spot illustration), complex (full scene)
- **Composition**: Centered, asymmetric, full-bleed, contained

#### For Hero Images / Product Photos

- **Subject**: What the image shows
- **Lighting**: Natural (golden hour, overcast), studio (softbox, rim), dramatic (high contrast), flat
- **Mood**: Aspirational, trustworthy, energetic, calm, luxurious, accessible
- **Composition**: Rule of thirds, centered, leading lines, negative space for text overlay
- **Color temperature**: Warm (3000-4000K), neutral (5000-6000K), cool (7000-9000K)
- **Depth of field**: Shallow (subject isolated), deep (everything sharp), selective
- **Background**: Solid color, gradient, environmental, transparent, blurred
- **Text overlay zone**: If text will be placed over the image, specify safe areas

#### For Video

- **Duration**: 2-8 seconds (Veo 3.1 constraint)
- **Camera movement**: Static, pan left/right, zoom in/out, orbit, tracking
- **Subject action**: What happens in the video (product spin, UI interaction, scene transition)
- **Style**: Live-action look, animated/motion graphics, 3D rendered, kinetic typography
- **Loop behavior**: Seamless loop, one-shot with fade, boomerang
- **Audio**: Silent (default for UI), ambient, music
- **Aspect ratio**: 16:9 (landscape), 9:16 (mobile/stories), 1:1 (social), 4:3 (tablet)

---

### Step 2: PROMPT ENGINEERING — Construct Generation Prompts

Using `ai-design-generation` skill -> `prompt-engineering-visual.md`:

Build structured, optimized prompts for the target MCP tool. The prompt is the most important artifact — even if no MCP is available, a well-constructed prompt is immediately usable.

#### Universal Prompt Structure

Every generation prompt follows this structure:

```
[SUBJECT]: What to generate — specific and descriptive
[PLATFORM]: Target platform with version (iOS 26, Material 3, responsive web)
[STYLE]: Visual style keywords from designer DNA match and sector direction
[TOKENS]: Specific design token values — hex colors, font sizes, spacing, radii
[CONTENT]: Real/realistic content strings for every text element
[COMPOSITION]: Layout structure, alignment, spacing rules
[QUALITY]: Resolution, aspect ratio, fidelity level
[REFERENCE]: "In the visual style of [matched designer/product]"
[NEGATIVE]: What to avoid — wireframes (unless requested), placeholder text, inconsistent styling
```

#### Prompt Templates by Mode

**Screen Mockup Prompt Template**:
```
A high-fidelity UI screen mockup of a [screen type] for a [sector] [platform] app.

Layout: [from wireframe or description — sidebar navigation, card grid, split pane, etc.]
Primary content: [main content visible on screen]
Primary action: [the main thing the user can do]

Visual style: [designer DNA match], [sector style keywords]
Color palette: primary [hex], secondary [hex], background [hex], text [hex]
Typography: [font family], headings [size], body [size]
Spacing: base unit [N]px, section gap [N]px, card padding [N]px
Border radius: [N]px for cards, [N]px for buttons, [N]px for inputs

Content: [Real text for every visible element — headlines, body, buttons, labels, data]
Platform: [iOS 26 with Liquid Glass / Material 3 Expressive / responsive web]
Resolution: [2x for screens, specific dimensions for assets]

States shown: [default / also include loading, empty, error states as separate frames]

Do NOT include: wireframe style, lorem ipsum, placeholder avatars without faces, inconsistent element styling, watermarks
```

**Icon Set Prompt Template**:
```
A set of [N] UI icons for [purpose/context].

Icons needed: [list each icon with its meaning]

Style: [outlined/filled/duotone] with [N]px stroke width
Grid: [N]x[N]px with [N]px padding (optical area [N]x[N]px)
Corner radius: [N]px
Color: [single color hex / duotone primary+secondary hex]
Cap style: round / square / butt

Consistency requirements: All icons must have equal visual weight, consistent stroke width, and aligned to the same grid. No icon should appear heavier or lighter than others.

Output format: SVG (vector, scalable)

Do NOT include: filled backgrounds, text labels, inconsistent stroke widths, overly detailed elements that won't scale to 16px
```

**Illustration Prompt Template**:
```
A [style] illustration of [scene/concept] for a [sector] [context — onboarding, empty state, hero, etc.].

Style: [flat/isometric/3D/hand-drawn/geometric]
Color palette: [hex values from tokens — limit to 4-6 colors]
Mood: [playful/professional/warm/minimal]
Composition: [centered/asymmetric/full-bleed]
Level of detail: [simple/moderate/complex]

Characters (if any): [style — geometric/realistic/abstract], [diversity considerations]
Background: [solid color hex / gradient / environmental / transparent]

Dimensions: [W]x[H] px at 2x resolution
Format: PNG with transparency / WebP / SVG

Do NOT include: text (unless specifically requested), stock photo look, watermarks, overly busy backgrounds
```

**Photo Prompt Template**:
```
A [photorealistic/editorial/lifestyle] photograph of [subject] for [context].

Lighting: [natural golden hour / studio softbox / dramatic rim light / flat overcast]
Mood: [aspirational/trustworthy/energetic/calm/luxurious]
Composition: [rule of thirds / centered / leading lines / negative space left/right for text]
Color temperature: [warm 3500K / neutral 5500K / cool 7500K]
Depth of field: [shallow f/1.8 / deep f/11 / selective]
Background: [describe — blurred office, solid gray, outdoor environment]

Dimensions: [W]x[H] px at 2x resolution
Format: WebP (for web) / HEIC (for iOS)

Do NOT include: AI artifacts (extra fingers, warped text), watermarks, overly saturated colors, uncanny valley faces
```

**Video Prompt Template**:
```
A [duration]-second [style] video of [subject/action].

Camera: [static / slow pan right / gentle zoom in / orbit 45 degrees]
Subject: [what is shown and what it does — product rotates, UI scrolls, scene transitions]
Style: [live-action / motion graphics / 3D render / kinetic typography]
Mood: [matching the brand — calm, energetic, premium]
Loop: [seamless loop / one-shot with fade / boomerang]
Aspect ratio: [16:9 / 9:16 / 1:1]

Color grading: [warm / cool / neutral / matched to brand palette hex values]
Speed: [normal / slow motion 0.5x / timelapse 2x]

Do NOT include: audio (silent for UI use), jarring cuts, inconsistent lighting between frames, watermarks
```

#### Style-Locking for Sets

When generating a SET of assets (icon set, illustration series, screen flow), use a **style prefix** that repeats across all prompts:

```
STYLE PREFIX (applied to every prompt in this set):
"Minimal outlined icons, 24x24 grid, 1.5px stroke, round caps, 2px corner radius, single color #1A1A2E, optical balanced, consistent visual weight"

Then each individual prompt:
ICON 1: [style prefix] — Home icon, simple house shape with chimney
ICON 2: [style prefix] — Search icon, magnifying glass tilted 45 degrees
ICON 3: [style prefix] — Settings icon, gear with 6 teeth
```

This ensures visual consistency across the entire set.

---

### Step 3: MODEL SELECTION — Choose the Right Tool

Not all AI models are equal. Route each asset to the optimal model:

#### Model Selection Matrix

| Asset Type | Best Model | Why | Fallback |
|-----------|-----------|-----|----------|
| **Full UI screen** | Stitch MCP | Purpose-built for UI generation, understands components | FLUX Pro (image-based mockup) |
| **UI icon set (vector)** | Recraft V3 via Fal.ai | Only model that outputs true SVG vectors | GPT-Image (raster, then trace to SVG) |
| **Logo concept (vector)** | Recraft V3 via Fal.ai | Vector output, clean shapes | FLUX Pro (raster concept, refine manually) |
| **Flat illustration** | FLUX Pro via Fal.ai | Strong style adherence, clean output | GPT-Image (good with text-in-image) |
| **Isometric illustration** | FLUX Pro via Fal.ai | Best isometric rendering quality | Imagen 4 (more photorealistic but capable) |
| **Character illustration** | GPT-Image | Best character consistency and expression | FLUX Pro |
| **Product photo** | Imagen 4 via Fal.ai | Most photorealistic output | FLUX Pro (slightly more stylized) |
| **Lifestyle photo** | Imagen 4 via Fal.ai | Natural lighting and composition | FLUX Pro |
| **Hero image (stylized)** | FLUX Pro via Fal.ai | Best artistic/stylized quality | Imagen 4 (more photorealistic) |
| **Background pattern** | FLUX Pro via Fal.ai | Good at seamless patterns | Recraft V3 (for vector patterns) |
| **UI video/animation** | Veo 3.1 via Fal.ai | Only video generation model | Screen record + edit manually |
| **Product video** | Veo 3.1 via Fal.ai | Smooth camera movement, product focus | Manual video production |
| **Diagram with text** | GPT-Image | Best text rendering in images | Manual creation (Figma/design tool) |
| **App Store screenshots** | Stitch MCP + post-process | Full screen generation + frame | FLUX Pro (mockup image) |

#### When NO MCP Is Available

If no generation MCP is available, the command's output shifts to:
1. Complete, tool-ready prompt for each asset (copy-paste into Midjourney, DALL-E, Ideogram, etc.)
2. Recommended tool for each asset type
3. Recommended settings (model version, resolution, style parameters)
4. Post-processing instructions

The prompt itself is a valuable design artifact — it encodes all of Sumi's design intelligence into a format any tool can consume.

---

### Step 4: GENERATE — Execute via MCP

Route generation to the best available tool:

#### Screen Generation Flow

1. Build specification from Step 1
2. Construct prompt from Step 2
3. Call Stitch MCP `generate_screen_from_text` with full prompt
4. If Stitch unavailable, call Fal.ai FLUX Pro with the prompt adapted for image generation
5. Request 2-3 variations if the tool supports it
6. Log the exact prompt for iteration

#### Icon Generation Flow

1. Define complete icon inventory from Step 1
2. Build style-locked prompt prefix from Step 2
3. Call Fal.ai Recraft V3 for each icon with the same style prefix
4. Verify SVG output is clean (no raster embedded, no excessive nodes)
5. Verify visual consistency across the set

#### Illustration/Photo/Video Generation Flow

1. Build specification from Step 1
2. Construct mode-specific prompt from Step 2
3. Route to optimal model from Step 3
4. Execute generation
5. Log prompt for iteration

For each generation attempt, log:
- The exact prompt used
- The model and parameters
- The result quality assessment
- Any adjustments needed for iteration

---

### Step 5: QUALITY CONTROL — Score and Verify

#### Screen Quality Score (10 Dimensions)

For generated screens, score across 10 visual dimensions:

| Dimension | Weight | What to Check |
|-----------|--------|---------------|
| Layout and Hierarchy | 15% | Visual hierarchy follows F/Z-pattern, clear H1-H4 levels, content grouping |
| Typography | 12% | Type scale is consistent, contrast between heading/body, readable at target size |
| Color and Contrast | 12% | Token adherence, WCAG contrast ratios (4.5:1 text, 3:1 UI), harmony |
| Spacing and Alignment | 10% | Grid-aligned, consistent spacing rhythm, breathing room |
| Platform Fidelity | 10% | Matches iOS HIG / Material 3 / Web conventions accurately |
| Pattern Correctness | 10% | Uses correct patterns for the screen type (nav, data display, input) |
| Content Quality | 10% | Realistic content, appropriate length, no placeholder text |
| State Completeness | 8% | Requested states are present and well-handled |
| Sector Fit | 8% | Matches industry visual expectations and norms |
| Accessibility | 5% | Visible contrast, appropriately sized targets, text legibility |

Score each dimension 1-10 with specific justification. Compute weighted overall score.

#### Asset Quality Checklist

For generated assets (icons, illustrations, photos, video):

**Universal checks**:
- [ ] Style consistent with design tokens (colors match hex values, shapes match radii)
- [ ] Works on light AND dark backgrounds (or appropriate for intended context)
- [ ] Correct file format for intended use (SVG for vectors, WebP for raster, MP4 for video)
- [ ] Appropriate resolution/dimensions for target platform
- [ ] Accessible (sufficient contrast, not decorative-only without alt text plan)
- [ ] Production-ready (optimized file size, no artifacts, no watermarks)

**Icon set checks**:
- [ ] Consistent stroke width across all icons in the set
- [ ] Grid-aligned — all icons sit on the same pixel grid
- [ ] Consistent visual weight — no icon looks heavier or lighter than others
- [ ] Legible at smallest target size (16px for web, 24pt for mobile)
- [ ] Consistent corner radius and cap style across all icons
- [ ] Metaphors are universally understood (not culturally specific)

**Illustration checks**:
- [ ] Consistent art style across the set
- [ ] Color palette matches design tokens exactly (not "close to" — exact hex values)
- [ ] Appropriate level of detail for context (not too busy for mobile)
- [ ] Consistent character style if people are depicted
- [ ] Inclusive representation (diversity in depicted people)

**Photo checks**:
- [ ] Consistent lighting and color temperature across the set
- [ ] Appropriate mood for the product sector
- [ ] No uncanny valley artifacts (hands, faces, text)
- [ ] Represents target audience appropriately (diversity, inclusion)
- [ ] Composition works with planned text overlay zones

**Video checks**:
- [ ] Smooth motion without frame-to-frame artifacts
- [ ] Consistent style throughout (no mid-clip style shifts)
- [ ] Correct duration (within requested range)
- [ ] Loop is seamless (if loop was requested)
- [ ] File size is appropriate for target platform (< 5MB for web, < 10MB for native)

---

### Step 6: POST-PROCESSING — Production-Ready Assets

After generation and quality check, prepare assets for production:

#### Upscaling

- Raster assets generated at low resolution: upscale to target resolution
- Use AI upscaling (Fal.ai has upscaling endpoints) or manual upscale
- Verify sharpness and detail after upscaling — no blur or artifacts introduced

#### Background Removal

- For icons and illustrations that need transparency: remove background
- Verify edges are clean (no fringing, no halo)
- Save with alpha channel (PNG-32 or WebP with alpha)

#### SVG Optimization

For vector assets (icons, logos, vector illustrations):
- Remove unnecessary metadata and comments
- Simplify paths (reduce node count without visible change)
- Use consistent precision (2 decimal places for coordinates)
- Ensure viewBox is set correctly
- Remove embedded raster images (should be pure vector)
- Minify for production (remove whitespace, shorten attribute names)

Tool: SVGO or equivalent optimization

#### Format Optimization

| Format | Use Case | Optimization |
|--------|----------|-------------|
| **SVG** | Icons, logos, simple illustrations | SVGO minification, gzip compression |
| **WebP** | Photos, complex illustrations (web) | Quality 80-85%, lossy for photos, lossless for UI |
| **AVIF** | Photos, illustrations (modern browsers) | Quality 70-80%, smaller than WebP |
| **PNG** | UI elements needing exact pixel control | PNG-8 for limited colors, PNG-32 for transparency |
| **HEIC** | Photos (iOS native) | Quality 80%, Apple ecosystem only |
| **MP4** | Video (universal) | H.264, CRF 23, 30fps, AAC audio if needed |
| **WebM** | Video (web) | VP9, CRF 31, smaller than MP4 for web |
| **Lottie** | UI animations | Export from After Effects or convert from video |

#### Responsive Asset Preparation

For raster assets, prepare multiple resolutions:

| Density | Multiplier | Use Case |
|---------|-----------|----------|
| 1x | Base size | Standard density displays, fallback |
| 2x | 2x base | Retina/HiDPI displays (most modern devices) |
| 3x | 3x base | Super HiDPI (iPhone Pro Max, high-end Android) |

Naming convention: `asset-name.webp`, `asset-name@2x.webp`, `asset-name@3x.webp`

For responsive images, also prepare srcset-ready variants:
```html
<img
  src="hero-640.webp"
  srcset="hero-640.webp 640w, hero-1024.webp 1024w, hero-1440.webp 1440w, hero-2880.webp 2880w"
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 100vw, 1440px"
  alt="Descriptive alt text"
  loading="lazy"
  decoding="async"
/>
```

---

### Step 7: FIGMA INTEGRATION

If Figma MCP is available, offer to push generated assets directly:

**For screens**:
- Create a new frame in Figma with the generated design
- Apply Auto Layout for responsive behavior
- Map design tokens to Figma variables
- Organize layers with meaningful names

**For icons**:
- Create icon components with consistent frame sizes
- Set up variants (outlined, filled, duotone) as component variants
- Apply color as a Figma variable (swappable)
- Organize in an icon library page

**For illustrations/photos**:
- Place in a designated assets page
- Set constraints for responsive behavior
- Add descriptive layer names
- Tag with metadata (purpose, alt text, usage context)

If Figma MCP is NOT available, output:
- Figma-ready specifications (frame sizes, auto layout settings, variable mappings)
- Import instructions for manual Figma integration

---

### Step 8: ITERATE OR APPROVE

Based on the quality score:

**Score >= 7/10**: Present to user for approval. Highlight strengths and any minor polish items.

**Score 4-6/10**: Identify the weakest 2-3 dimensions. Construct an adjusted prompt with targeted fixes:
- If hierarchy is weak → add explicit layout instructions to prompt
- If colors don't match → add hex values more prominently in prompt
- If platform fidelity is off → add specific platform version constraints
- Regenerate with the adjusted prompt

**Score < 4/10 after 2 iterations**: Recommend alternative approach:
- For screens → build manually with `/component` instead
- For icons → use an established icon library (Lucide, Phosphor, Heroicons) instead of generating
- For photos → use stock photography with specific search terms provided
- Provide the specification as a detailed brief for manual creation

For each iteration, document:
- What changed in the prompt
- Why it was changed (which quality dimension was weak)
- The result of the change

---

## Output Format

```
### Phase Position
> **Phase 4: BUILD** | Step 20 of 30 | `/generate`
>
> `/component` -> **`/generate`** -> `/research`

---

## AI Design Generation

### Generation Brief
- **Mode**: [Screen Mockup / Icon Set / Illustration / Hero Image / Product Photo / Video]
- **Description**: [What is being generated]
- **Platform**: [iOS / Android / Web]
- **Sector**: [Detected or specified]
- **Design tokens**: [Source — .sumi/style.json, /17-tokens, or specified]
- **Visual direction**: [Source — .sumi/vision.json, /10-vision, or specified]
- **MCP tools available**: [List of available MCP servers, or "None — manual prompts"]

---

### Design Specification
[Complete spec built from Sumi's intelligence — varies by mode]

#### [Mode-specific sections]
[Screen type + patterns / Icon inventory + style / Illustration scene + style / Photo subject + lighting / Video action + camera]

#### Visual Direction
- **Designer DNA match**: [Matched designer or product]
- **Canonical rules**: [Key visual rules applied]
- **Platform conventions**: [iOS HIG / Material 3 / Web specifics]
- **Sector expectations**: [What this sector demands]

#### Content
[Real/realistic content for every text element — no lorem ipsum]

#### Style Lock
[Parameters applied to all prompts for consistency]
- **Colors**: [Hex values from tokens]
- **Typography**: [Font family, sizes]
- **Style keywords**: [Flat, minimal, bold, warm, etc.]
- **Mood**: [Professional, playful, premium, etc.]

---

### Generation Prompts

#### [Asset 1]: [Name]
**Tool**: [Selected MCP tool or "Manual — use prompt with [recommended tool]"]
**Prompt**:
```
[The complete, optimized prompt]
```
**Settings**: [Model version, resolution, parameters]

#### [Asset 2]: [Name]
[Same structure — repeated for each asset]

---

### Generated Output
[If MCP available: description of generated results, quality notes]
[If no MCP: "No MCP server detected. Use the prompts above with the recommended tools."]

---

### Quality Score

#### Screen Score (if screen mode): [X/10]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Layout and Hierarchy | [X/10] | [Specific finding] |
| Typography | [X/10] | [Specific finding] |
| Color and Contrast | [X/10] | [Specific finding] |
| Spacing and Alignment | [X/10] | [Specific finding] |
| Platform Fidelity | [X/10] | [Specific finding] |
| Pattern Correctness | [X/10] | [Specific finding] |
| Content Quality | [X/10] | [Specific finding] |
| State Completeness | [X/10] | [Specific finding] |
| Sector Fit | [X/10] | [Specific finding] |
| Accessibility | [X/10] | [Specific finding] |

#### Asset Checklist (if asset mode):
[Completed quality checklist — all items pass/fail with notes]

**Top 3 Issues**:
1. [Most impactful issue with specific fix]
2. [Second issue with specific fix]
3. [Third issue with specific fix]

---

### Post-Processing Plan
| Asset | Action | Tool | Output Format | Sizes |
|-------|--------|------|---------------|-------|
| [Name] | [Upscale/Remove BG/Optimize/Trace] | [Tool] | [Format] | [1x, 2x, 3x dimensions] |

---

### Production Delivery

#### Asset [N]: [Name]
- **Prompt used**: [Exact prompt for reproducibility]
- **Quality status**: [Pass / Needs refinement — specific notes]
- **Alt text**: "[Recommended descriptive alt text for accessibility]"
- **Sizes**: 1x: [W]x[H], 2x: [W]x[H], 3x: [W]x[H]
- **Format**: [SVG / WebP / PNG / MP4]
- **File naming**: [asset-name-variant.format]
- **Usage**: [Where and how this asset should be used]

[Repeated for each asset]

---

### Iteration Log
[If iterations were needed: what changed in the prompt and why]

---

### Design Memory Written
Generation records saved to `.sumi/generated-[asset-name].json`.
Prompts preserved for reproducibility and iteration.

---

### Next Steps
1. **Approve and build** → `/component` to convert approved screens to production code
2. **Iterate** → Adjust [specific dimension] and regenerate
3. **Generate more** → `/generate` for the next asset in the set
4. **Integrate** → Add approved assets to your project's asset directory
5. **Critique** → `/roast` to score the full set of generated designs

**Run `/next` to continue the journey.**
```

---

## Quality Gates

The output MUST include:
- [ ] MCP availability detected and reported (which tools are available)
- [ ] Sub-mode correctly identified (screen/icon/illustration/photo/video)
- [ ] Design specification built from Sumi's intelligence (not generic — uses tokens, sector, platform, visual direction)
- [ ] Generation prompts complete with all sections (subject, platform, style, tokens, content, composition, quality, reference, negative)
- [ ] Model selection justified (why this model for this asset type)
- [ ] Style-locking applied for sets (consistent prefix across all prompts in a set)
- [ ] If MCP available: generation attempted with result described
- [ ] If no MCP: prompts and specifications provided for manual use with tool recommendation
- [ ] Quality scoring completed (10-dimension for screens, checklist for assets) with specific findings
- [ ] Top 3 issues identified with specific fixes
- [ ] Post-processing plan documented (upscaling, optimization, format conversion)
- [ ] Production delivery includes: alt text, responsive sizes, file naming, usage guidelines
- [ ] Real/realistic content used throughout — no lorem ipsum, no placeholder text
- [ ] Iteration log if regeneration was needed (what changed in the prompt, why)
- [ ] Design memory written to `.sumi/generated-*.json`

The output MUST NOT include:
- Vague scoring ("looks good") — every dimension must cite specific findings
- Lorem ipsum or placeholder content anywhere
- Generation without specification — the spec must be built first using Sumi's intelligence
- Scores without actionable follow-up — every low score must have a specific prompt adjustment
- Icon sets without style-locking — stroke width, grid, color, and caps must be locked across all icons
- Assets without alt text recommendations
- Missing format optimization — every asset must specify its production format and size variants
- Inconsistent sets — all items in a set must share the same style prefix

---

## Cross-References

When generating designs and assets, draw intelligence from:
- `ai-design-generation` skill — MCP tool configuration, prompt engineering, generation pipelines, quality control, asset generation strategies
- `visual-design-mastery` skill — visual quality standards for scoring, designer DNA for style reference, canonical design rules
- `platform-visual-standards` skill — platform-specific generation constraints (iOS 26 Liquid Glass, Material 3 Expressive, modern CSS)
- `ui-pattern-intelligence` skill — pattern requirements for each screen type (200+ patterns)
- `sector-style-intelligence` skill — sector visual norms and expectations (20+ industries)
- `screen-flow-patterns` skill — screen type specifications and flow context
- `layout-block-intelligence` skill — 500+ layout section/block patterns for screen composition
- `page-composition-engine` skill — full-page composition recipes for screen generation
- `component-patterns-code` skill — component mapping for production conversion
- `performance-states-patterns` skill — state coverage requirements (loading, error, empty, skeleton)
- `color-palette-library` skill — accessible color combinations, APCA contrast verification
- `typography-pairing-recipes` skill — type scale and font pairing for typography accuracy
- `icon-illustration-systems` skill — icon design systems, illustration style guides, SVG best practices
- `image-media-patterns` skill — image, video, gallery patterns with responsive and performance guidance
- `accessibility-inclusive-design` skill — alt text requirements, contrast standards, inclusive representation
- `design-token-presets` skill — ready-to-deploy token systems if no `.sumi/style.json` exists

---

## Next Step

**Next** -> `/research` (5.1) — Plan usability testing on generated designs

**Alternatives**:
- `/component` (4.3) — Convert approved screen generations to production code
- `/roast` (5.2) — Get a design critique of generated screens and assets
- `/screen` (4.2) — Define screen specifications before generating
- `/generate` — Run again for the next asset in the flow
- `/sumi` — See the full journey map
