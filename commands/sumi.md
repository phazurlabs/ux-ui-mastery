---
name: sumi
description: "Command map and quick start — see all 34 commands, starter recipes, Design Quality Score, anti-slop engine, and tips for best results."
argument-hint: "[optional: command or topic]"
---

# Chef Sumi — Your Design Intelligence System

Welcome to Chef Sumi v9. 34 commands. 42 skills. Vibe coded slop into visual cuisine.

## Quick Start

```
# The fast track — style it, build it, ship it
/style [sector]  →  /screen [type]  →  /fix  →  ship

# The quality track — fix slop, prove it, ship it
/fix  →  /before-after  →  /grade  →  ship

# The full track — plan, design, review, ship
/brief  →  /style  →  /screen  →  /roast  →  /fix  →  /preflight
```

---

## Hero Commands

| Command | What It Does |
|---------|-------------|
| `/fix` | Anti-slop engine — transforms AI-generated UI into production quality |
| `/style` | Complete visual identity with 10 zero-config starter recipes |
| `/grade` | Design Quality Score (0-100) like Lighthouse for design |
| `/before-after` | Visual proof of design transformation |
| `/screen` + `/component` | Platform-aware code (web/iOS/Android) |

---

## All 34 Commands

### MAKE — Design and Build (19)

Generate visual design systems, screens, components, and production-ready code.

| Command | What It Does |
|---------|-------------|
| `/fix` | Anti-slop engine — 60+ detection patterns, full code transformation |
| `/style` | Sector-aware visual direction — palette, typography, spacing, mood |
| `/palette` | Deep color system with oklch, APCA contrast, dark mode mapping |
| `/type` | Typography system — font pairing, scale, fluid sizing |
| `/layout` | Layout section/block patterns — hero, features, pricing, CTA, dashboard |
| `/wireframe` | Low-fidelity wireframes and layout exploration |
| `/screen` | Full production screens with all states (empty, loading, error, success) |
| `/component` | Production components with accessibility baked in |
| `/page` | Full page compositions with block stacking and visual rhythm |
| `/tokens` | Complete design token system (color, type, spacing, motion, elevation) |
| `/form` | Form design — inputs, validation, multi-step, accessibility |
| `/nav` | Navigation system — top bar, sidebar, tabs, command palette, mega menu |
| `/animate` | Motion design — entrance, micro-interaction, page transition, scroll |
| `/icon` | Icon and illustration systems with SVG implementation |
| `/dark` | Dark mode — color mapping, contrast verification, seamless toggle |
| `/responsive` | Cross-breakpoint design — container queries, fluid scaling, grids |
| `/onboard` | Onboarding flow with activation metrics and progressive disclosure |
| `/generate` | AI-powered screen generation (Stitch MCP, Fal.ai) |
| `/remix` | Evidence-based redesign of weak areas |

### REVIEW — Evaluate and Improve (6)

Audit existing designs for quality, accessibility, and usability problems.

| Command | What It Does |
|---------|-------------|
| `/audit` | Nielsen's 10 heuristics + Laws of UX + Gestalt + cognitive load analysis |
| `/roast` | Liz Lerman critique with dimensional scoring + AI slop detection |
| `/grade` | Design Quality Score (0-100) — Lighthouse-style scoring with badge generation |
| `/qa` | Design QA — spec vs. implementation comparison. `/qa project` scans full codebase |
| `/a11y` | WCAG 2.2 accessibility audit. `/a11y fix` generates corrected code |
| `/before-after` | Visual proof of design transformation — side-by-side comparison |

### PLAN — Research and Strategy (6)

Research users, analyze competitors, plan metrics, and prepare for launch.

| Command | What It Does |
|---------|-------------|
| `/brief` | Problem definition — persona, HMW questions, constraints, success criteria |
| `/research` | User research AND usability testing — interviews, surveys, test plans |
| `/benchmark` | Competitive analysis — 10-dimension scorecard, gap analysis, roadmap |
| `/map` | Information architecture — sitemap, navigation, content hierarchy |
| `/measure` | Metrics plan — HEART framework, OKRs, experimentation, dashboards |
| `/preflight` | Pre-launch checklist AND post-launch plan — the full launch playbook |

### Utility (3)

| Command | What It Does |
|---------|-------------|
| `/sumi` | You're here. Command map, quick start, tips. |
| `/next` | Context-aware suggestion of what to do next |
| `/status` | Progress dashboard of what you've generated |

---

## Starter Recipes

One word. Zero config. Complete visual identity.

```
/style saas         →  Linear DNA
/style fintech      →  Stripe DNA
/style ecommerce    →  Shopify DNA
/style healthcare   →  One Medical DNA
/style creative     →  Awwwards DNA
/style education    →  Duolingo DNA
/style social       →  Discord DNA
/style devtools     →  GitHub DNA
/style landing      →  Vercel DNA
/style mobile       →  iOS/Android adaptive
```

---

## Workflows by Goal

**"Fix my AI-generated code"**
`/fix` → `/before-after`

**"Build a screen fast"**
`/style [sector]` → `/screen [type]`

**"Get a design quality score"**
`/grade` (or `/grade vs stripe`)

**"Complete design system"**
`/style` → `/tokens` → `/screen` → `/component`

**"Review existing design"**
`/audit` → `/roast` → `/a11y` → `/grade`

**"Start from scratch"**
`/brief` → `/research` → `/style` → `/screen`

**"Ship by Friday"**
`/style` → `/screen` → `/fix` → `/qa` → `/preflight`

**"Scan my whole codebase"**
`/qa project`

---

## What's New in v9

- **Anti-Slop Engine** (`/fix`) — 60+ detection patterns, full code transformation. Turns AI-generated UI into production quality.
- **Design Quality Score** (`/grade`) — 0-100 Lighthouse-style scoring with badge generation. Benchmark against any product.
- **Before/After** (`/before-after`) — Visual proof of design transformation with side-by-side comparison.
- **Platform-Aware Generation** — `/screen` and `/component` auto-detect iOS/Android/web and generate platform-native code.
- **Starter Recipes** — 10 zero-config design systems. One word each. Instant visual identity.
- **Project-Wide QA** — `/qa project` scans entire codebase for design drift and inconsistency.
- **Cognitive Load Analysis** — `/audit` now includes Laws of UX and Gestalt evaluation alongside Nielsen's heuristics.
- **Design Memory v2** — Auto-detects existing Tailwind config and CSS custom properties. `.sumi/` carries context across all commands.
- **WCAG Auto-Fix** — `/a11y fix` generates corrected code for every accessibility finding.
- **AI Slop Detection** — `/roast` and `/audit` now flag AI-generated UI patterns (default spacing, placeholder copy, generic icons).

---

## Tips for Best Results

1. **Start with `/style`**. Takes 2 minutes, makes everything 10x better.
2. **Run `/fix` on any AI-generated code**. It's the fastest path to production quality.
3. **Use `/grade` before every PR**. If it scores below 70, run `/fix`.
4. **The more context you give, the better the output**. Paste screenshots, code, URLs, Figma exports.
5. **Commands compose**. `/style` → `/screen` → `/fix` → `/grade` builds on each step.
6. **Design memory carries across commands**. Run `/style` once, benefit everywhere.
7. **Be specific about screen types**. `/screen dashboard` beats `/screen`. `/screen settings mobile iOS` beats `/screen settings`.
8. **REVIEW commands work on anything**. Paste a screenshot, a URL, a code snippet, a Figma export.

---

## 42 Skills (Auto-Invoked)

Skills activate automatically when relevant. You never need to call them directly.

**Core UX**: design-process-methods, nng-ux-heuristics, ux-research-methods, cognitive-psychology-ux, ux-metrics-measurement, ux-ethics-content-strategy

**Platform**: mobile-ux-design, desktop-app-design, platform-visual-standards, cross-cultural-i18n-ux

**Visual**: ui-visual-design-system, visual-design-mastery, color-palette-library, typography-pairing-recipes, shadow-elevation-density, image-media-patterns, icon-illustration-systems

**Patterns**: screen-flow-patterns, ui-pattern-intelligence, layout-block-intelligence, page-composition-engine, navigation-pattern-encyclopedia, form-design-encyclopedia, responsive-block-patterns

**Interaction**: interaction-motion-design, animation-recipe-library, performance-states-patterns, ambient-calm-zero-ui

**Systems**: design-systems-architecture, component-patterns-code, design-token-presets, data-visualization-mastery

**AI & Generation**: ai-spatial-voice-ux, agentic-ai-generative-ux, ai-design-generation, figma-design-tool-workflows

**Strategy**: sector-style-intelligence, conversion-optimization-patterns, micro-copy-intelligence, design-critique-case-studies, accessibility-inclusive-design, business-design-templates

---

Start building. `/style [your sector]` is a good first move. Or paste your code and run `/fix`.
