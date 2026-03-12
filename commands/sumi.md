---
description: "Command map and quick start — see all 27 commands, tips for best results, and what's new in v8."
tier: "utility"
---

# Sumi — Your UX/UI Design System

Welcome to Sumi v8. 27 commands. 42 skills. One design system that turns Claude into your senior design partner.

## Quick Start

```
/style [sector]  -->  /screen [type]  -->  /roast  -->  ship
```

That's the minimum viable workflow. Style sets the visual direction, screen builds it, roast catches problems. Everything else makes the output better.

---

## All 27 Commands

### MAKE -- Design and Build

Generate visual design systems, screens, components, and production-ready code.

| Command | What It Does |
|---------|-------------|
| `/style` | Sector-aware visual direction -- palette, typography, spacing, mood |
| `/palette` | Deep color system with oklch, APCA contrast, dark mode mapping |
| `/type` | Typography system -- font pairing, scale, fluid sizing |
| `/layout` | Layout section/block patterns -- hero, features, pricing, CTA, dashboard |
| `/wireframe` | Low-fidelity wireframes and layout exploration |
| `/screen` | Full production screens with all states (empty, loading, error, success) |
| `/component` | Production components with accessibility baked in |
| `/page` | Full page compositions with block stacking and visual rhythm |
| `/tokens` | Complete design token system (color, type, spacing, motion, elevation) |
| `/form` | Form design -- inputs, validation, multi-step, accessibility |
| `/nav` | Navigation system -- top bar, sidebar, tabs, command palette, mega menu |
| `/animate` | Motion design -- entrance, micro-interaction, page transition, scroll |
| `/icon` | Icon and illustration systems with SVG implementation |
| `/dark` | Dark mode -- color mapping, contrast verification, seamless toggle |
| `/responsive` | Cross-breakpoint design -- container queries, fluid scaling, grids |
| `/onboard` | Onboarding flow with activation metrics and progressive disclosure |
| `/generate` | AI-powered screen generation (Stitch MCP, Fal.ai) |
| `/remix` | Evidence-based redesign of weak areas |

### REVIEW -- Evaluate and Improve

Audit existing designs for quality, accessibility, and usability problems.

| Command | What It Does |
|---------|-------------|
| `/audit` | Nielsen's 10 heuristics evaluation with severity ratings |
| `/roast` | Liz Lerman critique with dimensional scoring -- the honest review |
| `/grade` | 10-dimension visual quality score (Awwwards-calibrated) |
| `/qa` | Design QA -- spec vs. implementation comparison |
| `/a11y` | WCAG 2.2 accessibility audit with fix recommendations |

### PLAN -- Research and Strategy

Research users, analyze competitors, plan metrics, and prepare for launch.

| Command | What It Does |
|---------|-------------|
| `/brief` | Problem definition -- persona, HMW questions, constraints, success criteria |
| `/research` | User research AND usability testing -- interviews, surveys, test plans |
| `/benchmark` | Competitive analysis -- 10-dimension scorecard, gap analysis, roadmap |
| `/map` | Information architecture -- sitemap, navigation, content hierarchy |
| `/measure` | Metrics plan -- HEART framework, OKRs, experimentation, dashboards |
| `/preflight` | Pre-launch checklist AND post-launch plan -- the full launch playbook |

### Utility

| Command | What It Does |
|---------|-------------|
| `/sumi` | You're here. Command map, quick start, tips. |
| `/next` | Context-aware suggestion of what to do next |
| `/status` | Progress dashboard of what you've generated |

---

## Workflows by Goal

**"I need to build a screen fast"**
```
/style [sector] --> /screen [type]
```

**"I want a complete design system"**
```
/style --> /tokens --> /palette --> /type --> /component --> /screen
```

**"I need to review an existing design"**
```
/audit --> /roast --> /a11y --> /grade
```

**"I'm starting a new product from scratch"**
```
/brief --> /research --> /benchmark --> /map --> /style --> /screen
```

**"I need to ship by Friday"**
```
/style [sector] --> /screen [type] --> /qa --> /preflight
```

**"I want to improve my conversion rate"**
```
/benchmark --> /onboard --> /form --> /roast
```

---

## What's New in v8

**Action-first commands**: No more numbered steps. Every command is a verb. Type `/style`, not `/04-taste`. Type `/roast`, not `/23-roast`.

**Three tiers, not seven phases**: Commands organized by what they do (MAKE / REVIEW / PLAN), not when to use them. Use any command at any time.

**Merged commands**: `/research` now covers both user research AND usability testing. `/preflight` covers both pre-launch checklist AND post-launch iteration plan. Fewer commands, same coverage.

**42 skills**: 16 new specialist skills added -- layout blocks, page composition, conversion optimization, microcopy, form design, navigation patterns, color palettes, typography pairing, shadow/elevation, animation recipes, image/media patterns, icon systems, data visualization, responsive patterns, design token presets, and business templates.

**Design memory**: `.sumi/` directory stores your style decisions (palette, typography, tokens) so they carry across commands automatically.

---

## Tips for Best Results

1. **Start with `/style`**. It takes 2 minutes and makes every subsequent command 10x more precise.

2. **Paste your Constraint Stack**. If you ran `/brief`, paste the Constraint Stack into every command. It's the difference between generic and specific output.

3. **Be specific about screen types**. `/screen dashboard` beats `/screen`. `/screen settings mobile iOS` beats `/screen settings`.

4. **Use sector names with `/style`**. `/style fintech` or `/style healthcare` or `/style luxury-ecommerce` -- sector context dramatically changes the output.

5. **Run `/roast` before you ship**. It's the honest review your design needs. Catches problems you can't see because you've been staring at it too long.

6. **Commands compose**. `/style` feeds `/tokens` feeds `/screen` feeds `/component`. Each one builds on the last. The more context Sumi has, the better the output.

7. **REVIEW commands work on anything**. Paste a screenshot, a URL, a code snippet, a Figma export. `/audit`, `/roast`, `/grade`, and `/a11y` will evaluate whatever you give them.

---

## 42 Skills (Auto-Invoked)

Skills activate automatically when relevant. You never need to call them directly.

**Core UX**: ux-process-workflow, nng-ux-heuristics, ux-research-methods, cognitive-psychology-ux, ux-metrics-measurement, ux-ethics-content-strategy

**Platform**: mobile-ux-design, desktop-app-design, platform-visual-standards, cross-cultural-i18n-ux

**Visual**: ui-visual-design-system, visual-design-mastery, color-palette-library, typography-pairing-recipes, shadow-elevation-density, image-media-patterns, icon-illustration-systems

**Patterns**: screen-flow-patterns, ui-pattern-intelligence, layout-block-intelligence, page-composition-engine, navigation-pattern-encyclopedia, form-design-encyclopedia, responsive-block-patterns

**Interaction**: interaction-motion-design, animation-recipe-library, performance-states-patterns, ambient-calm-zero-ui

**Systems**: design-systems-architecture, component-patterns-code, design-token-presets, data-visualization-mastery

**AI & Generation**: ai-spatial-voice-ux, agentic-ai-generative-ux, ai-design-generation, figma-design-tool-workflows

**Strategy**: sector-style-intelligence, conversion-optimization-patterns, micro-copy-intelligence, design-critique-case-studies, accessibility-inclusive-design, business-design-templates

---

## Getting Help

- `/next` -- Not sure what to do? Get a context-aware suggestion.
- `/status` -- See what you've generated so far.
- `/sumi` -- Come back here anytime for the full map.

Start building. `/style [your sector]` is a good first move.
