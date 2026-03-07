---
name: AI Design Generation
description: "MCP integration layer for AI-powered visual design generation — Stitch MCP (UI screen generation), Fal.ai MCP (600+ models including Imagen 4, FLUX, Veo 3.1), Replicate MCP (open-source models), Recraft V3 MCP (only SVG/vector-capable model), OpenAI GPT-Image MCP, and Figma MCP (official design read/write). Covers prompt engineering for visual design output, multi-tool generation pipelines (sketch to refine to code), asset generation (icons, illustrations, photos, video), and quality control scoring for generated designs. Use when the user mentions: generate design, create mockup, AI design, generate screen, create UI, make me a design, generate icons, create illustrations, Stitch, Imagen, Veo, DALL-E, Recraft, design generation, AI mockup, generate assets, create visuals."
---

# AI Design Generation

## Why AI Design Generation Matters

AI design generation tools can produce screens, icons, illustrations, and videos in seconds — but without design intelligence, they produce generic, trend-chasing output. This skill bridges the gap: it teaches Sumi how to prompt AI generation tools with designer-grade specifications (drawing from visual-design-mastery) and how to score, critique, and iterate on generated output until it meets professional standards.

The key insight: AI generation is not a replacement for design intelligence — it is an accelerator. The better the design brief, the better the generation. Sumi's design knowledge makes AI tools dramatically more effective.

## Reference Architecture

| File | Contents | Use When |
|------|----------|----------|
| `references/mcp-design-tools.md` | Complete catalog of MCP servers for design generation: Stitch (UI screens from text), Fal.ai (600+ models — Imagen 4, FLUX Pro, Veo 3.1, Recraft V3), Replicate (open-source models), OpenAI GPT-Image, Figma MCP (official). Per tool: capabilities, MCP configuration, tool names, parameters, pricing, strengths, limitations, best use cases. | Selecting the right MCP tool for a task. Configuring MCP servers. Understanding tool capabilities and limitations. |
| `references/prompt-engineering-visual.md` | How to write effective prompts for UI design generation. Prompt anatomy for each tool (Stitch, Imagen, FLUX, DALL-E). Style transfer techniques. Design token injection into prompts. Sector-aware prompting. Platform-specific prompting (iOS, Android, web). Negative prompting. Prompt templates for common UI screens. | Crafting effective generation prompts. Converting design specifications into tool-specific prompts. Ensuring generated output matches design direction. |
| `references/generation-pipelines.md` | Multi-step generation workflows: text to wireframe to high-fidelity to code. Single-tool pipelines vs. multi-tool pipelines. Iterative refinement loops. Design system consistency across multiple generations. Batch generation for screen families. Pipeline templates for common scenarios (landing page, dashboard, mobile app, design system). | Running multi-step generation workflows. Ensuring consistency across multiple generated screens. Planning generation projects. |
| `references/asset-generation-guide.md` | Generating design assets: icons (SVG via Recraft V3 — the only vector-capable model), illustrations (Fal.ai, DALL-E), photographs (Imagen 4, FLUX), video/motion (Veo 3.1), patterns/textures, brand assets. Per asset type: best tool, prompt strategy, output format, quality requirements, production-readiness checklist. | Generating specific design assets. Choosing the right tool for icons vs. illustrations vs. photos vs. video. |
| `references/quality-control-generation.md` | Scoring generated designs against the visual-design-mastery framework. Automated quality checks. Human-in-the-loop review process. Iteration strategies (what to change in prompts when output is poor). Common generation failures and fixes. When to stop iterating and hand-craft instead. | Evaluating AI-generated output quality. Deciding whether to iterate, change tools, or hand-craft. Quality gates for generated designs. |

## MCP Server Requirements

This skill enhances Sumi when MCP servers are available but does NOT require them. Without MCP servers, Sumi provides detailed specifications and prompts that users can use manually with any generation tool.

**Supported MCP Servers** (all optional):
| Server | What It Does | Install |
|--------|-------------|---------|
| stitch-mcp | Generate UI screens from text descriptions | npm i -g @anthropic/stitch-mcp |
| @fal-ai/mcp | 600+ image/video models (Imagen 4, FLUX, Veo 3.1, Recraft V3) | npm i -g @fal-ai/mcp |
| replicate-mcp | Open-source model access | npm i -g replicate-mcp |
| openai-images-mcp | GPT-Image / DALL-E 3 | npm i -g openai-images-mcp |
| figma-mcp | Read/write Figma files (official) | npm i -g @anthropic/figma-mcp |

## Cross-References

- **`visual-design-mastery`** — Provides the design intelligence that makes generation prompts effective and quality scoring meaningful.
- **`platform-visual-standards`** — Provides platform-specific constraints for generation prompts.
- **`ui-pattern-intelligence`** — Identifies which patterns to generate and their quality benchmarks.
- **`sector-style-intelligence`** — Provides sector-specific visual direction for generation prompts.
- **`design-systems-architecture`** — Ensures generated designs consume design tokens consistently.
- **`figma-design-tool-workflows`** — Integration with Figma for design-to-code pipelines.

## Commands Powered by This Skill

| Command | How This Skill Is Used |
|---------|----------------------|
| `/generate` | Primary command — AI-powered screen generation via MCP tools |
| `/assets` | AI-powered asset generation (icons, illustrations, photos, video) |
| `/vision` | Can generate mood board visualizations using image generation |
| `/screen` | Can use Stitch to generate screen mockups before coding |
| `/ship` | Can reference generated designs as implementation targets |
