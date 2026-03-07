---
description: AI-powered design asset generation — create icons (SVG), illustrations, photographs, video, and brand assets using MCP tools, with style consistency ensured by Sumi's design intelligence.
phase: "4"
phase_step: "4.7"
phase_name: "BUILD"
step_label: "Step 7 of 7"
---

# Assets — AI Design Asset Generation Engine

Generate design assets — icons, illustrations, photographs, video, patterns, and brand elements — using AI tools (MCP servers), with style consistency enforced by Sumi's design tokens and visual direction.

## Analysis Protocol

### Step 0: Gather Context & Check MCP Availability

Before generating assets, collect:

1. **Asset request**: What assets to generate (type: icons, illustrations, photos, video, patterns, brand elements). Be specific about quantity and purpose.
2. **Style direction**: From `/vision` or `/taste` — or specified directly. This locks the visual style for consistency across all generated assets.
3. **Design tokens**: Colors, shapes, border radii from `/drip` — used for style-locking prompts to ensure generated assets match the design system.
4. **Platform and format requirements**: Target platform (iOS, Android, Web), required formats (SVG, PNG, WebP, MP4), size requirements.
5. **Check MCP availability**:
   - **Recraft V3 (via Fal.ai)** → SVG/vector icons and logos (the ONLY vector-capable generation model)
   - **Fal.ai (FLUX Pro, Imagen 4)** → illustrations, photographs, hero images, background patterns
   - **Fal.ai (Veo 3.1)** → video and motion assets (up to 8 seconds)
   - **OpenAI GPT-Image** → illustrations with embedded text, diagrams
   - If **NO MCP available** → output specifications and optimized prompts for manual use

If the user provides a vague request ("I need some icons"), ask about: how many, what they represent, what style (outlined/filled/duotone), what size, and what context they appear in.

### Step 1: PLAN — Asset Generation Plan

Based on the request, create a generation plan covering:

- **Asset types needed**: Categorized by type
- **Best MCP tool for each**: Route each asset to the optimal generation model
- **Style parameters**: Extracted from design tokens and visual direction
- **Quantity and variations**: How many of each, whether variations are needed
- **Output format and size**: Target format per asset type
- **Consistency requirements**: If generating a set, what must stay locked across all items

**Asset Type Routing Table:**

| Asset Type | Best Tool | Format | Notes |
|-----------|-----------|--------|-------|
| App icons (vector) | Recraft V3 (Fal.ai) | SVG | Only vector-capable model |
| UI icon sets | Recraft V3 (Fal.ai) | SVG | Lock stroke width, grid, corner radius, color |
| Illustrations | GPT-Image or FLUX Pro | PNG/WebP | Match app visual style from /vision |
| Product photos | Imagen 4 (Fal.ai) | WebP | Photorealistic, controlled lighting |
| Hero images | FLUX Pro (Fal.ai) | WebP | Artistic/stylized, sector-aware |
| Background patterns | FLUX Pro (Fal.ai) | WebP/SVG | Seamless tileable |
| Video/motion | Veo 3.1 (Fal.ai) | MP4/WebM | Up to 8 seconds |
| Logos (concept) | Recraft V3 (Fal.ai) | SVG | Conceptual — then refine manually |
| Onboarding art | GPT-Image or FLUX Pro | PNG/WebP | Match onboarding screen style |
| Social/marketing | FLUX Pro or GPT-Image | PNG/WebP | Platform-specific dimensions |

### Step 2: PROMPT — Construct Asset Prompts

Using `ai-design-generation` skill → `asset-generation-guide.md`:

Build style-consistent prompts for each asset. The key principle is **style-locking** — every prompt in a set shares the same style prefix to ensure visual consistency.

**For icon sets**:
- Lock: stroke width (e.g., 1.5px), grid size (e.g., 24x24), corner radius (e.g., 2px), color (e.g., single color #1A1A2E or duotone), optical balance
- Prompt structure: "[style prefix] [icon subject], [grid/size], [stroke/fill style], [color constraint]"
- Generate all icons in the set with the same style prefix

**For illustrations**:
- Lock: style (flat/isometric/3D/hand-drawn), color palette (from tokens), level of detail, character style (if applicable)
- Prompt structure: "[style prefix] [scene/subject], [palette constraint], [mood/lighting], [composition]"

**For photographs**:
- Specify: lighting (natural/studio/dramatic), mood, composition (rule of thirds, centered), color temperature (warm/cool/neutral), depth of field
- Prompt structure: "[subject], [lighting], [mood], [composition], [color temperature], [background]"

**For video**:
- Specify: duration (2-8 seconds), camera movement (static/pan/zoom/orbit), subject action, style (live-action/animated/motion graphics), loop behavior
- Prompt structure: "[subject action], [camera movement], [duration], [style], [mood]"

**Negative prompts** (apply to all): watermarks, text overlays (unless requested), low resolution, inconsistent style, busy backgrounds (for icons)

### Step 3: GENERATE — Execute via MCP

Route each asset to the appropriate MCP tool:

- Execute generation with style-locked prompts
- **For sets**: Generate all items with the same style prefix. If the first result establishes a good style, reference it for subsequent items.
- **For variations**: Generate 2-3 variations of critical assets (app icon, hero image) for user selection
- **If no MCP available**: Output complete prompts organized by tool, with recommended settings (model, resolution, style parameters)

Log every prompt used for reproducibility and iteration.

### Step 4: QUALITY CHECK — Verify Assets

For each generated asset, verify against this checklist:

**Universal checks**:
- [ ] Style consistent with design tokens (colors, shapes, visual language)
- [ ] Works on light AND dark backgrounds (or appropriate for intended context)
- [ ] Correct file format for intended use
- [ ] Appropriate resolution/dimensions for target platform
- [ ] Accessible — sufficient contrast, not decorative-only without alt text plan
- [ ] Production-ready — optimized file size, correct format, no artifacts

**Icon set checks**:
- [ ] Consistent stroke width across all icons
- [ ] Grid-aligned — all icons sit on the same grid
- [ ] Consistent visual weight — no icon looks heavier or lighter than others
- [ ] Legible at smallest target size (16px for web, 24pt for mobile)
- [ ] Consistent corner radius and cap style

**Illustration checks**:
- [ ] Consistent art style across the set
- [ ] Color palette matches design tokens
- [ ] Appropriate level of detail for context (not too busy for mobile)
- [ ] Consistent character style if people are depicted

**Photo checks**:
- [ ] Consistent lighting and color temperature
- [ ] Appropriate mood for the product/sector
- [ ] No uncanny/artificial artifacts
- [ ] Represents target audience appropriately (diversity, inclusion)

**Video checks**:
- [ ] Smooth motion without artifacts
- [ ] Correct duration and loop behavior
- [ ] Appropriate file size for target platform

### Step 5: DELIVER — Production-Ready Output

Present generated assets with everything needed for integration:

- **Generated assets**: Each asset with its prompt, quality status, and any refinement notes
- **Alt text recommendations**: Descriptive alt text for every asset (for accessibility)
- **Responsive sizing**: 1x, 2x, 3x dimensions for each raster asset
- **Naming conventions**: Consistent file naming (e.g., `icon-[name]-[size].[format]`, `hero-[section]-[variant].[format]`)
- **Refinement notes**: Any assets that need manual touch-up, with specific guidance on what to adjust
- **Usage guidelines**: Where and how each asset should be used in the UI

## Output Format

```
### Phase Position
> **Phase 4: BUILD** | Step 7 of 7 | `/assets`
> *NNG: Asset Creation | Visual: AI-Powered Asset Generation*
>
> `/generate` (4.6) -> **`/assets` (4.7)** -> `/roast` (5.1)

---

## Asset Generation Report

### Request
- **Asset type**: [Icons/Illustrations/Photos/Video/Brand]
- **Quantity**: [N items]
- **Style source**: [/vision output / /taste output / specified]
- **MCP tools available**: [List]

---

### Generation Plan

| # | Asset | Tool | Format | Size | Style Lock |
|---|-------|------|--------|------|------------|
| 1 | [Name] | [Tool] | [SVG/WebP/MP4] | [Dimensions] | [Key style params] |
| 2 | [Name] | [Tool] | [Format] | [Dimensions] | [Key style params] |
| [continue for all assets] |

---

### Style Lock
[Extracted style parameters applied to all prompts]
- **Colors**: [palette hex values from tokens]
- **Style**: [flat/isometric/outlined/filled/photorealistic]
- **Grid**: [size for icons]
- **Stroke**: [width and cap style for icons]
- **Corner radius**: [value]
- **Mood**: [for illustrations/photos]
- **Lighting**: [for photos/video]

---

### Generated Assets

#### Asset 1: [Name]
- **Tool used**: [MCP tool or "manual prompt"]
- **Prompt**: [The exact prompt used]
- **Result**: [Generated asset or "No MCP — use prompt above with [recommended tool]"]
- **Quality**: [Pass / Needs refinement — specific notes]
- **Alt text**: "[Recommended descriptive alt text]"
- **Sizes**: 1x: [W]x[H], 2x: [W]x[H], 3x: [W]x[H]

#### Asset 2: [Name]
[Same structure]

[Continue for all assets]

---

### Production Checklist
- [ ] All assets style-consistent with design tokens
- [ ] Light + dark mode compatible (or context-appropriate)
- [ ] Correct formats (SVG for vectors, WebP for raster, MP4 for video)
- [ ] Optimized file sizes (SVG minified, images compressed)
- [ ] Alt text documented for every asset
- [ ] Responsive sizes specified (1x, 2x, 3x)
- [ ] Naming convention applied consistently

---

### Usage Guidelines
[How to use these assets in the app]

**Icons**: [Size, padding, color application — single color or multi]
**Illustrations**: [Placement, responsive behavior, max/min dimensions]
**Photos**: [Aspect ratio, cropping rules, overlay treatment]
**Video**: [Autoplay behavior, loop, fallback image]

---

### Next Steps
1. **Integrate**: Add assets to your project's asset directory
2. **Refine**: Any assets marked "needs refinement" — [specific manual edits needed]
3. **Generate more**: Run `/assets` again for additional asset types

**Recommended command sequence**:
-> `/ship [component]` — Build components that consume these assets
-> `/generate` — Generate screens using these assets
-> `/roast` — Get a design critique including asset quality
-> `/responsive` — Verify assets work across breakpoints
```

## Quality Gates

The output MUST include:
- [ ] MCP availability detected and reported
- [ ] Asset routing to appropriate tools with justification
- [ ] Style-locked prompts consistent with design tokens from `/drip` or `/vision`
- [ ] If MCP available: generation attempted with results shown
- [ ] If no MCP: complete prompts and specs provided for manual use with tool recommendations
- [ ] Quality check completed for each generated asset with pass/fail per criterion
- [ ] Production checklist completed
- [ ] Usage guidelines provided for each asset type
- [ ] Alt text recommendations included for every asset
- [ ] Responsive sizing specified (1x, 2x, 3x) for raster assets

The output MUST NOT include:
- Assets generated without style-locking — every prompt must include design token values
- Icon sets with inconsistent parameters — stroke width, grid, and color must be locked
- Missing alt text — every asset must have a recommended descriptive alt text
- Unverified quality — every asset must pass the quality checklist or be flagged for refinement
- Vague refinement notes ("needs work") — every refinement note must specify exactly what to adjust

## Cross-References

When generating assets, draw intelligence from:
- `ai-design-generation` skill → `asset-generation-guide.md` — per-asset-type generation strategy, model selection
- `ai-design-generation` skill → `mcp-design-tools.md` — tool configuration, API parameters, model capabilities
- `ai-design-generation` skill → `quality-control-generation.md` — quality verification framework
- `visual-design-mastery` skill — style consistency standards, designer DNA for reference
- `design-systems-architecture` skill — token consumption for style-locking prompts
- `accessibility-inclusive-design` skill — alt text requirements, contrast standards, inclusive representation
- `sector-style-intelligence` skill — sector-appropriate visual treatment for assets
- `platform-visual-standards` skill — platform-specific asset requirements (iOS app icon specs, Android adaptive icons, web favicons)

## Next Step

**Next** -> `/roast` (5.1) — Get a design critique of the complete design including assets

**Alternatives**:
- `/ship` (4.3) — Build components that consume these assets
- `/generate` (4.6) — Generate screens using these assets
- `/responsive` (3.4) — Verify assets work across all breakpoints
- `/assets` — Run again for additional asset types
