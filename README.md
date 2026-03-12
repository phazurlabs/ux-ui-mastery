<p align="center">
  <img src="assets/sumi.svg" alt="Chef Sumi" width="400" />
</p>

<p align="center">
  <strong>Your AI writes code. Chef Sumi makes it look like a designer wrote it.</strong>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> &middot;
  <a href="#the-problem">The Problem</a> &middot;
  <a href="#what-you-get">What You Get</a> &middot;
  <a href="#commands">Commands</a> &middot;
  <a href="#how-it-works">How It Works</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-9.0.0-FF6B4A?style=flat-square" alt="v9.0.0" />
  <img src="https://img.shields.io/badge/commands-34-white?style=flat-square" alt="34 commands" />
  <img src="https://img.shields.io/badge/skills-42-white?style=flat-square" alt="42 skills" />
  <img src="https://img.shields.io/badge/dependencies-zero-22C55E?style=flat-square" alt="Zero dependencies" />
</p>

---

## Quick Start

```bash
# Install (one command)
mkdir -p ~/.claude/plugins && git clone https://github.com/phazurlabs/sumi.git ~/.claude/plugins/sumi

# Restart Claude Code, then:
/style fintech          # generate a complete design system
/fix                    # transform AI slop into production UI
/grade                  # get a 0-100 design quality score
```

That's it. No API keys. No accounts. No dependencies.

---

## The Problem

AI coding tools generate UI that works but looks like AI wrote it.

You've seen it: the same purple gradient. The same Inter font. The same rounded cards on white. The same three-column grid. Every AI-generated app looks identical because LLMs produce the statistical average of their training data &mdash; not intentional design.

The numbers tell the story:

| | |
|---|---|
| **66%** of developers | say "almost right, but not quite" is their #1 AI frustration &mdash; Stack Overflow 2025 |
| **94.8%** of websites | fail basic accessibility standards &mdash; WebAIM 2025 |
| **1.7x** more issues | in AI-generated code vs human-written &mdash; CodeRabbit 2025 |
| **~33%** pass rate | for WCAG compliance in AI-generated UI &mdash; Standard Beagle 2025 |

Chef Sumi fixes this. It's a design intelligence layer for [Claude Code](https://github.com/anthropics/claude-code) that transforms raw AI output into production-quality UI &mdash; with real typography, real color systems, real accessibility, and real design consistency.

---

## What You Get

### `/fix` &mdash; Transform AI slop into production UI

Paste any AI-generated code. Get back production-quality code with every design issue fixed.

```
/fix
```

- Detects 60+ AI slop patterns across 7 dimensions
- Fixes typography, color, spacing, layout, states, accessibility
- Generates design tokens if none exist
- Preserves all business logic &mdash; only transforms the design layer
- Shows before/after quality score

### `/style` &mdash; Generate a complete design system

One word. Complete design system. Zero questions asked.

```
/style fintech
```

Outputs: color palette (oklch + hex), font pairing, type scale, spacing grid, motion curves, radius + shadows, tone of voice, CSS custom properties, W3C design tokens, and 5 reference apps. Saves to `.sumi/style.json` so every future command inherits your decisions.

**10 starter recipes built in:**

| Recipe | DNA | Recipe | DNA |
|--------|-----|--------|-----|
| `/style saas` | Linear | `/style education` | Duolingo |
| `/style fintech` | Stripe | `/style social` | Discord |
| `/style ecommerce` | Shopify | `/style devtools` | GitHub |
| `/style healthcare` | One Medical | `/style landing` | Vercel |
| `/style creative` | Awwwards | `/style mobile` | iOS/Android |

### `/grade` &mdash; Design Quality Score (0&ndash;100)

Like Lighthouse, but for design. One number. Seven dimensions.

```
/grade
```

| Dimension | Weight |
|-----------|--------|
| Visual Hierarchy | 20% |
| Typography System | 15% |
| Color System | 15% |
| Spacing &amp; Layout | 15% |
| Component Quality | 15% |
| Accessibility | 10% |
| Design Coherence | 10% |

Score 80+? Get a **Designed with Chef Sumi** badge for your README.

Compare against the best: `/grade vs stripe` &mdash; see exactly where you stand.

### `/screen` &amp; `/component` &mdash; Platform-aware code

Tell Chef Sumi what you're building. Get production-ready code for your platform.

```
/screen dashboard for a fintech app
/component modal for confirming payments, trust-first
```

- **Web**: React + TypeScript + Tailwind, all states, responsive breakpoints
- **iOS**: SwiftUI with iOS 26 Liquid Glass, Dynamic Type, haptic feedback
- **Android**: Jetpack Compose with Material 3 Expressive, dynamic color
- **Cross-platform**: React Native / Flutter with platform-adaptive styling

Every component ships with 10 states, full ARIA/accessibility, keyboard navigation, dark mode, and test skeleton.

### `/before-after` &mdash; Visual proof

See exactly what changed and why. Shareable comparison for PRs, portfolios, or stakeholders.

```
/before-after
```

Scores 10 design dimensions before and after. Shows category-by-category code diffs. Outputs a one-line shareable verdict.

---

## Commands

### Make &mdash; design and build

| Command | Output |
|---------|--------|
| `/fix` | Anti-slop engine &mdash; transforms AI-generated UI into production quality |
| `/style` | Complete visual identity &mdash; palette, type, spacing, tokens, references |
| `/screen` | Production screen &mdash; 30+ types, all states, responsive, accessible |
| `/component` | Production component &mdash; React/SwiftUI/Compose, 10 states, ARIA, tests |
| `/page` | Full page &mdash; block composition, spacing rhythm, SEO, lazy loading |
| `/form` | Complete form &mdash; validation, multi-step, Zod schema, accessibility |
| `/nav` | Navigation &mdash; sidebar, top bar, bottom tabs, command palette |
| `/palette` | Color system &mdash; oklch scales, APCA scores, dark mode mapping |
| `/type` | Typography &mdash; font pairing, type scale, fluid sizing, platform stacks |
| `/tokens` | W3C design tokens &mdash; 3-tier, multi-theme, CSS + Tailwind + JSON |
| `/layout` | Page grid &mdash; CSS Grid/Flexbox, container queries, responsive |
| `/wireframe` | ASCII wireframes &mdash; 2-3 layout options with rationale |
| `/animate` | Motion recipes &mdash; CSS + Framer Motion, reduced-motion fallbacks |
| `/icon` | Icon system &mdash; library selection, sizing scale, React wrapper |
| `/dark` | Dark mode &mdash; oklch luminance mapping, elevation, toggle component |
| `/responsive` | Responsive &mdash; breakpoints, fluid scaling, block transformations |
| `/onboard` | Onboarding &mdash; step sequence, permissions, activation metrics |
| `/generate` | AI generation &mdash; mockups, icons, illustrations via MCP |
| `/remix` | Redesign &mdash; fix top 5 problems with UX reasoning for each change |

### Review &mdash; evaluate and improve

| Command | Output |
|---------|--------|
| `/grade` | Design Quality Score &mdash; 0-100, 7 dimensions, badge generation |
| `/audit` | Full design audit &mdash; heuristics, cognitive load, flow, dark patterns |
| `/roast` | Quick critique &mdash; 10 dimensions, letter grade, AI slop detection |
| `/before-after` | Before/after comparison &mdash; visual proof of design transformation |
| `/qa` | Design QA &mdash; token compliance, state coverage, project-wide consistency |
| `/a11y` | Accessibility &mdash; WCAG 2.2 AA, ARIA, keyboard, contrast, auto-fix |

### Plan &mdash; research and strategy

| Command | Output |
|---------|--------|
| `/brief` | Problem definition &mdash; persona, constraints, success criteria |
| `/research` | Research plan &mdash; interview scripts, surveys, usability tests |
| `/benchmark` | Competitive analysis &mdash; scorecard vs top 5, gap analysis |
| `/map` | Information architecture &mdash; sitemap, nav hierarchy, URL structure |
| `/measure` | Metrics plan &mdash; HEART framework, experimentation strategy |
| `/preflight` | Launch checklist &mdash; SEO, performance, analytics, legal, monitoring |

### Utility

| Command | |
|---------|---|
| `/sumi` | Show all commands |
| `/next` | Suggest what to do next |
| `/status` | Show what you've built so far |

---

## How It Works

Chef Sumi is **42 skill files** containing 23,000+ lines of design intelligence, backed by 165 reference documents. Pure markdown. When you run a command, Claude loads the relevant skills automatically.

```
No API keys. No external services. No dependencies. Works offline.
```

### Design Memory

Run `/style` once. Every command after that uses your decisions automatically.

```
/style fintech        ← your design system is saved
/screen dashboard     ← uses your palette, type, tokens
/component card       ← same visual language
/fix                  ← transforms code using YOUR tokens
/roast                ← evaluates against YOUR system
```

Design memory lives in `.sumi/style.json`. It auto-detects your project's existing Tailwind config, CSS custom properties, and design tokens &mdash; so it works with what you already have.

### Context makes it better

```
/component button                              → works
/component button for fintech iOS app,          → much better
  primary CTA for wire transfers,
  trust-first, audience: professionals 30-55
```

---

## Install

**One command:**

```bash
mkdir -p ~/.claude/plugins && git clone https://github.com/phazurlabs/sumi.git ~/.claude/plugins/sumi
```

Restart Claude Code. Type `/sumi`.

**Requirements:** [Claude Code](https://github.com/anthropics/claude-code) CLI. That's it.

**Update:**

```bash
cd ~/.claude/plugins/sumi && git pull
```

---

<p align="center">
  <sub>v9.0.0 &middot; 34 commands &middot; 42 skills &middot; 165 reference docs &middot; zero dependencies</sub><br />
  <sub>Built by <a href="https://github.com/phazurlabs">Phazur Labs</a></sub>
</p>
