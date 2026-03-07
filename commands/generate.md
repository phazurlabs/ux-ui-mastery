---
description: AI-powered screen generation — use Stitch MCP and image generation tools to create UI screens from text descriptions, informed by Sumi's design intelligence. Design-aware AI generation.
phase: "4"
phase_step: "4.6"
phase_name: "BUILD"
step_label: "Step 6 of 7"
---

# Generate — AI Screen Generation Engine

Generate UI screens using AI tools (MCP servers), informed by Sumi's full design intelligence stack — pattern taxonomy, visual direction, platform conventions, sector expectations, and design tokens.

## Analysis Protocol

### Step 0: Gather Context & Check MCP Availability

Before generating, collect:

1. **Screen description**: What screen to generate (description, purpose, target users).
2. **Platform**: iOS, Android, or Web.
3. **Sector**: Auto-detect from context, or ask the user. Sector determines pattern expectations and visual norms.
4. **Design tokens**: From `/drip` or `/vision` — if available, inject into generation prompts as specific values (hex colors, font sizes, spacing).
5. **Prior Sumi outputs**: Consume `/vision`, `/patterns`, `/taste`, `/screen` if available. These provide visual direction, pattern requirements, and screen specifications.
6. **Check MCP availability**: Detect which MCP servers are configured in the current environment:
   - **Stitch MCP** → full screen generation from text
   - **Fal.ai MCP** → image/visual generation (FLUX Pro, Imagen 4, Recraft V3)
   - **Figma MCP** → design file read/write
   - **OpenAI GPT-Image** → illustration and text-in-image generation
   - If **NO MCP available** → output a detailed specification + optimized prompt that the user can use manually with their tool of choice

If the user provides only a vague description, ask clarifying questions about screen purpose, key content, and primary user action before proceeding.

### Step 1: SPECIFY — Build Design-Informed Specification

Using Sumi's design intelligence, build a complete screen specification:

- **Screen type**: From `screen-flow-patterns` skill — e.g., dashboard, settings, profile, onboarding, detail view, list view, checkout
- **Required patterns**: From `ui-pattern-intelligence` — what UI patterns this screen type needs (navigation, data display, input, feedback, layout)
- **Visual direction**: From `visual-design-mastery` — designer DNA match, canonical rules, color system, typography scale
- **Platform conventions**: From `platform-visual-standards` — iOS Human Interface Guidelines, Material 3, or Web conventions
- **Sector expectations**: From `sector-style-intelligence` — what visual treatment, density, tone, and patterns are expected in this industry
- **Content strategy**: Real or realistic content throughout — never lorem ipsum. Use plausible names, numbers, dates, and copy that reflects the actual product domain.
- **State coverage**: Which states to generate — default, empty, loading, error, success. Default state is always generated; specify additional states explicitly.

**Output the specification before proceeding to prompt construction.**

### Step 2: PROMPT — Construct Generation Prompt

Using `ai-design-generation` skill → `prompt-engineering-visual.md`:

Build a structured generation prompt with all required sections:
- **Subject**: Screen type, purpose, primary action
- **Platform**: Target platform with version (e.g., iOS 18, Material 3, responsive web)
- **Style**: Visual style keywords derived from designer DNA match and sector direction
- **Tokens**: Inject design tokens as specific values — hex colors, font families, font sizes in px/pt, spacing values, border radii, shadow values
- **Content**: Real/realistic content strings to populate the screen
- **States**: Which states to render
- **Constraints**: Platform-specific constraints (safe areas, navigation bars, status bars, notches)
- **Quality**: Resolution, aspect ratio, fidelity level
- **Reference**: "In the visual style of [matched designer/product]" — from benchmark data
- **Negative prompts**: What to avoid — wireframes (unless requested), placeholder text, unrealistic content, inconsistent styling

### Step 3: GENERATE — Execute via MCP

Route generation to the best available tool:

- **If Stitch MCP available**: Call `generate_screen_from_text` with the constructed prompt. Request 2-3 variations if the tool supports it.
- **If Fal.ai MCP available**: Generate a high-fidelity mockup image using FLUX Pro or Imagen 4. Use the full prompt with style-locking parameters.
- **If Figma MCP available**: Create a design frame in Figma with the specified components and tokens.
- **If no MCP available**: Output the complete prompt and specification for manual use. Recommend the best tool for the screen type (Stitch for full screens, FLUX Pro for stylized mockups, Figma for component-level work).

For each generation attempt, log the exact prompt used so it can be iterated.

### Step 4: SCORE — Evaluate Generated Output

Using `visual-scoring-framework.md`, score the generated output across 10 visual dimensions:

| Dimension | Weight | What to Check |
|-----------|--------|---------------|
| Layout & Hierarchy | 15% | Visual hierarchy, F/Z-pattern, content grouping |
| Typography | 12% | Scale, contrast, readability, platform conventions |
| Color & Contrast | 12% | Token adherence, WCAG contrast, harmony |
| Spacing & Alignment | 10% | Consistent spacing, grid alignment, breathing room |
| Platform Fidelity | 10% | Matches platform conventions (iOS/Android/Web) |
| Pattern Correctness | 10% | Uses correct patterns for the screen type |
| Content Quality | 10% | Realistic content, appropriate length, no placeholder |
| State Completeness | 8% | Requested states are present and well-handled |
| Sector Fit | 8% | Matches industry visual expectations |
| Accessibility | 5% | Visible contrast, touch target sizes, text sizing |

**You MUST**:
- Score each dimension 1-10 with specific justification
- Compute weighted overall score
- Identify top 3 issues that most hurt the score
- Flag any platform convention violations
- Flag any sector anti-patterns
- Flag any accessibility failures (contrast ratio below 4.5:1, touch targets below 44pt)

### Step 5: ITERATE OR APPROVE

Based on the score:

- **Score >= 7/10**: Present to user for approval. Highlight strengths and any minor improvements.
- **Score 4-6/10**: Identify the weakest 2-3 dimensions. Construct an adjusted prompt with targeted fixes. Suggest regeneration with specific changes noted.
- **Score < 4/10 after 2 iterations**: Recommend manual building with `/ship` instead. The screen may be too complex or nuanced for current generation tools. Provide the specification as a detailed brief for manual implementation.

For each iteration, document what changed in the prompt and why.

### Step 6: CODE — Convert to Production (Optional)

If the user approves the generated output:

1. Offer to convert to production code via `/ship`
2. Extract the design specification from the generated output (layout structure, component hierarchy, token values)
3. Map to platform-native components (React/SwiftUI/Compose/HTML+CSS)
4. Preserve the visual decisions from generation as coded constraints

## Output Format

```
### Phase Position
> **Phase 4: BUILD** | Step 6 of 7 | `/generate`
> *NNG: Prototyping | Visual: AI-Powered Generation*
>
> `/extract` (4.5) → **`/generate` (4.6)** → `/assets` (4.7)

---

## AI Screen Generation

### Generation Brief
- **Screen**: [Description]
- **Platform**: [iOS/Android/Web]
- **Sector**: [Detected/specified]
- **Design tokens**: [Source — /drip, /vision, or specified]
- **MCP tools available**: [List of available MCP servers]

---

### Design Specification
[Complete spec built from Sumi's intelligence]

#### Screen Type & Patterns
- **Screen type**: [From screen-flow-patterns taxonomy]
- **Required patterns**: [List of patterns this screen needs]
- **Sector expectations**: [What this sector demands for this screen type]

#### Visual Direction
- **Designer DNA match**: [Matched designer/product]
- **Canonical rules**: [Key visual rules applied]
- **Platform conventions**: [iOS HIG / Material 3 / Web specifics]

#### Content
[Real/realistic content for every text element on the screen]

#### States
[Which states are being generated and why]

---

### Generation Prompt
[The complete, optimized prompt constructed for the MCP tool]

---

### Generated Output
[If MCP available: the generated screen/image]
[If no MCP: "No MCP server detected. Use the prompt above with [recommended tool]"]

---

### Visual Quality Score: [X/10]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Layout & Hierarchy | [X/10] | [Specific finding] |
| Typography | [X/10] | [Specific finding] |
| Color & Contrast | [X/10] | [Specific finding] |
| Spacing & Alignment | [X/10] | [Specific finding] |
| Platform Fidelity | [X/10] | [Specific finding] |
| Pattern Correctness | [X/10] | [Specific finding] |
| Content Quality | [X/10] | [Specific finding] |
| State Completeness | [X/10] | [Specific finding] |
| Sector Fit | [X/10] | [Specific finding] |
| Accessibility | [X/10] | [Specific finding] |

**Top 3 Issues**:
1. [Most impactful issue with specific fix]
2. [Second issue with specific fix]
3. [Third issue with specific fix]

---

### Iteration Suggestions
[If score < 7: specific prompt adjustments to improve weakest dimensions]
[If score >= 7: "Ready for review — approve to proceed to production code"]

---

### Next Steps
1. **Approve & build**: Run `/ship` to convert to production code
2. **Iterate**: Adjust [specific dimension] and regenerate
3. **Generate more**: Run `/generate` for the next screen in the flow

**Recommended command sequence**:
-> `/generate [next screen]` — Generate the next screen in the flow
-> `/ship [component]` — Build approved components as production code
-> `/assets` — Generate supporting assets (icons, illustrations)
-> `/roast` — Score the full set of generated screens
```

## Quality Gates

The output MUST include:
- [ ] MCP availability detected and reported
- [ ] Design specification includes screen type, patterns, visual direction, platform conventions
- [ ] Generation prompt is complete with all sections (subject, platform, style, tokens, content, states, constraints, quality, reference, negative)
- [ ] If MCP available: generation attempted with result shown
- [ ] If no MCP: prompt and specification provided for manual use with tool recommendation
- [ ] Generated output scored across 10 visual dimensions with specific justifications
- [ ] Top 3 issues identified with specific fixes
- [ ] Iteration suggestions provided if score < 7
- [ ] Real/realistic content used throughout — no lorem ipsum, no placeholder text

The output MUST NOT include:
- Vague scoring ("looks good", "could be better") — every dimension must cite what's present and what's missing
- Lorem ipsum or placeholder content anywhere in the specification or prompt
- Generation without specification — the spec must be built first using Sumi's intelligence
- Scores without actionable follow-up — every low score must have a specific prompt adjustment

## Cross-References

When generating screens, draw intelligence from:
- `ai-design-generation` skill — MCP tool configuration, prompt engineering, generation pipelines, quality control
- `visual-design-mastery` skill — visual quality standards for scoring, designer DNA for style reference
- `platform-visual-standards` skill — platform-specific generation constraints (iOS, Android, Web)
- `ui-pattern-intelligence` skill — pattern requirements for each screen type
- `sector-style-intelligence` skill — sector visual norms and expectations
- `screen-flow-patterns` skill — screen type specifications and flow context
- `component-patterns-code` skill — component mapping for production conversion
- `performance-states-patterns` skill — state coverage requirements (loading, error, empty)

## Next Step

**Next** -> `/assets` (4.7) — Generate supporting visual assets (icons, illustrations, photos)

**Alternatives**:
- `/ship` (4.3) — Convert approved generation to production code
- `/roast` (5.1) — Get a design critique of generated screens
- `/screen` (4.2) — Define screen specifications before generating
- `/generate` — Run again for the next screen in the flow
