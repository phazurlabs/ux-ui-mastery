<p align="center">
  <img src="assets/sumi.svg" alt="Sumi" width="320" />
</p>

<p align="center">
  <strong>The design system you don't have to build.</strong><br />
  32 commands · 42 skills · 165 reference docs
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#commands">Commands</a> ·
  <a href="#skills">Skills</a> ·
  <a href="#how-it-works">How it works</a>
</p>

---

Type what you're building. Get production code with the design quality of a funded startup. Colors, type, spacing, components, screens — all consistent, all accessible, all yours. Works inside Claude Code.

```
/style fintech          → complete visual identity + tokens
/screen dashboard       → production React + Tailwind, all states
/component modal        → full ARIA, keyboard nav, animations
/roast                  → 10-dimension critique, must-fix list
```

<br />

## Commands

### Make

| Command | What you get |
|---------|-------------|
| `/style` | Full visual identity — palette, type scale, spacing, tokens, references |
| `/tokens` | W3C design tokens — 3-tier, multi-theme, light/dark, export-ready |
| `/screen` | Production screen — 30+ types, all states, responsive, accessible |
| `/component` | Shipped component — React/SwiftUI/CSS, ARIA, keyboard nav, animations |
| `/wireframe` | Low-fi layouts with rationale — fast exploration before pixels |
| `/map` | Information architecture — sitemap, nav hierarchy, URL structure |
| `/layout` | Page composition — block stacking, visual rhythm, responsive grid |
| `/copy` | Microcopy for every state — buttons, errors, empty states, tooltips |
| `/form` | Complete form — validation, multi-step, error handling, accessibility |
| `/chart` | Data visualization — chart selection, dashboard composition, Recharts code |
| `/nav` | Navigation system — pattern selection, IA integration, responsive |
| `/icon` | Icon and illustration system — style guide, SVG implementation |
| `/animate` | Motion recipes — entrance, micro-interaction, page transition, scroll |
| `/palette` | Color system — oklch values, APCA scores, dark mode, industry palettes |
| `/type` | Typography — font pairing, type scale, fluid sizing, platform stacks |
| `/generate` | AI image generation — Stitch MCP, Fal.ai, Recraft V3, Veo 3.1 |
| `/assets` | Asset pipeline — icons, illustrations, photos with quality control |
| `/welcome` | Onboarding flow — progressive disclosure, activation metrics |

### Review

| Command | What you get |
|---------|-------------|
| `/roast` | 10-dimension design critique — scored, with must-fix and should-fix |
| `/audit` | Heuristic audit — severity rated, prioritized fixes |
| `/access` | Accessibility audit — WCAG 2.2 AA, code fixes included |
| `/flow` | Journey audit — multi-screen, drop-off risk, emotional arc |
| `/qa` | Design QA — spec vs implementation, pixel audit, token compliance |

### Plan

| Command | What you get |
|---------|-------------|
| `/brief` | Problem definition — persona, constraints, success criteria |
| `/research` | Research plan — interview scripts, survey design, recruitment |
| `/benchmark` | Competitive analysis — 10-dimension scorecard vs top 5 |
| `/measure` | Metrics plan — HEART framework, experimentation strategy |
| `/preflight` | Pre-launch checklist — SEO, performance, analytics, legal |
| `/iterate` | Post-launch plan — monitoring, review cadence, feedback loops |

### Utility

`/sumi` · `/next` · `/status`

<br />

## Design Memory

Run `/style` once. Sumi saves your decisions to `.sumi/` — palette, type scale, tokens, voice. Every command after that inherits your design system automatically. No repetition, no drift.

<br />

## Skills

42 knowledge domains that activate automatically based on context.

| Domain | Skills |
|--------|--------|
| **Visual** | Visual design mastery, color palettes, typography pairing, shadow & elevation, animation recipes |
| **Patterns** | 200+ UI patterns, screen & flow catalog, layout blocks, page composition, navigation, forms |
| **Content** | Microcopy intelligence, conversion optimization, data visualization |
| **Systems** | Design systems architecture, design tokens, responsive blocks, component patterns & code |
| **Platforms** | Mobile (iOS 26 / M3), desktop, platform standards, cross-cultural i18n, performance states |
| **Experience** | Accessibility, interaction & motion, ethics & content strategy, design critique |
| **Intelligence** | Sector style (20+ industries), image & media, icon & illustration, business templates |
| **AI & Emerging** | AI generation, agentic AI, spatial & voice, ambient & calm technology |
| **Foundations** | Cognitive psychology, usability heuristics, research methods, metrics |

<br />

## How it works

You type a command. Sumi loads the matching skill files — patterns, code, and research. Only the relevant slice activates. More context in, better output out.

```
/component button                          → good
/component button for fintech iOS app,     → great
  primary CTA, trust-first, 35-55 audience
```

<br />

## Install

```bash
mkdir -p ~/.claude/plugins && cd ~/.claude/plugins
git clone https://github.com/phazurlabs/sumi.git
```

Pure markdown. Zero dependencies. Works offline.

<br />

---

<p align="center">
  <sub>v8.0.0 · Built by <a href="https://github.com/phazurlabs">Phazur Labs</a> · Powered by Claude</sub>
</p>
