<p align="center">
  <img src="assets/sumi.svg" alt="Chef Sumi" width="400" />
</p>

<p align="center">
  <strong>Vibe coded slop &rarr; visual cuisine.</strong><br />
  A Claude Code plugin that turns plain English into production-grade UI.
</p>

<p align="center">
  <a href="#what-it-does">What it does</a> &middot;
  <a href="#examples">Examples</a> &middot;
  <a href="#all-commands">All commands</a> &middot;
  <a href="#install">Install</a>
</p>

---

## What it does

Chef Sumi is a design intelligence plugin for [Claude Code](https://github.com/anthropics/claude-code). You describe what you're building. Chef Sumi turns it into production-ready code — colors, typography, components, full screens — with the visual quality and consistency of a professional design system.

**Three things make it different:**

1. **It produces code, not theory.** Every command outputs copy-paste-ready React, Tailwind CSS, SwiftUI, or vanilla CSS. Not wireframes in Figma. Not methodology docs. Actual code.

2. **It knows your industry.** Say "fintech" and you get trust-first blues, tabular number fonts, and conservative motion. Say "gaming" and you get high-energy palettes, bold type, and dramatic animations. 20+ sectors built in.

3. **It remembers your decisions.** Run `/style` once. Every command after that — `/screen`, `/component`, `/form` — automatically uses your palette, type scale, and tokens. No copy-pasting tokens between prompts. No drift.

<br />

## Examples

### Generate a complete visual identity

```
/style fintech
```

**What you get:**
- Color palette — 10-step brand scale + neutrals in oklch, with hex values and dark mode
- Typography — font pairing (Inter + DM Sans), fluid type scale with `clamp()` values
- Spacing — 4px base grid, scale from 4px to 128px
- Motion — duration scale, easing curves, spring physics values
- Radius + shadows — consistent scale across components
- Tone of voice — microcopy guidelines for the sector
- 5 reference apps — what to study and what to steal from each
- **Complete CSS custom properties** — copy the `:root {}` block into your project
- **W3C Design Tokens JSON** — import into Style Dictionary, Figma, or Tailwind
- Saves to `.sumi/style.json` so every future command inherits these decisions

---

### Fix AI-generated slop

```
/fix
```
*(paste your AI-generated code or point to a file)*

**What you get:**
- AI slop detection scan — identifies purple gradient syndrome, font monotony, layout lottery, accessibility void
- Complete code transformation — every issue fixed, not just flagged
- Design token generation — if no tokens exist, creates a complete set
- Before/after quality score showing exactly what improved
- All business logic preserved — only the design layer is transformed

---

### Compare before and after

```
/before-after
```
*(paste your original code — see the transformation)*

**What you get:**
- Side-by-side scoring across 10 design dimensions
- AI Slop Score comparison (before vs after)
- Exact code changes per category (typography, color, spacing, layout, accessibility)
- Complete transformed code — ready to copy-paste
- Shareable verdict: "Transformed from D-grade slop to A- production cuisine"

---

### Build a production screen

```
/screen dashboard for a fintech app
```

**What you get:**
- Full React + TypeScript + Tailwind component
- All states: loading (skeleton), empty, error, populated
- Responsive: mobile &rarr; tablet &rarr; desktop with actual breakpoint CSS
- Accessible: ARIA roles, keyboard navigation, skip links
- Uses your tokens from `/style` automatically
- Component hierarchy documented

---

### Ship a component

```
/component modal for confirming wire transfers, trust-first
```

**What you get:**
- React component with TypeScript props
- 10 states: default, loading, success, error, disabled, etc.
- Full ARIA: `role="dialog"`, `aria-modal`, focus trap, Escape to close
- Keyboard handling: Tab cycle, focus restoration on close
- Framer Motion entrance/exit animations
- Dark mode support
- Test skeleton (vitest + testing-library)

---

### Get a full page layout

```
/page saas landing
```

**What you get:**
- Complete page with ordered blocks: Nav &rarr; Hero &rarr; Social Proof &rarr; Features &rarr; Pricing &rarr; FAQ &rarr; CTA &rarr; Footer
- Each block is a full React component
- Section spacing rhythm system
- Scroll behavior: sticky nav, scroll-driven animations
- SEO meta tags + Open Graph
- Lazy loading + performance optimized

---

### Create a form

```
/form checkout for e-commerce
```

**What you get:**
- Multi-step wizard: Shipping &rarr; Payment &rarr; Review
- Zod validation schema
- Inline error messages with accessible announcements
- Credit card detection (Visa/Mastercard/Amex)
- Mobile-optimized: `inputmode="numeric"`, autofill attributes
- Loading + success + error states

---

### Build a navigation system

```
/nav sidebar for a SaaS dashboard
```

**What you get:**
- Collapsible sidebar with icon-only rail mode
- Nested menu groups with expand/collapse
- Active state with `aria-current="page"`
- Keyboard navigation
- Mobile: transforms into hamburger overlay
- Dark mode variant

---

### Generate a color system

```
/palette mood:calm sector:healthcare
```

**What you get:**
- 10-step neutral scale (oklch)
- 10-step brand color scale
- Semantic colors: surface, text, primary, error, warning, success
- APCA contrast scores for every text/background pair
- Dark mode palette (proper luminance mapping, not inversion)
- Colorblind-safe data visualization palette
- CSS custom properties block

---

### Critique any design

```
/roast
```
*(paste your code or describe your screen)*

**What you get:**
- 10 dimensions scored 1-10: clarity, hierarchy, consistency, spacing, color, typography, interaction, accessibility, innovation, polish
- Letter grade (A-F)
- Top 3 must-fix issues with code fixes
- Top 3 strengths to keep
- One-line verdict

---

### Run a full accessibility audit

```
/a11y
```

**What you get:**
- WCAG 2.2 AA compliance check
- ARIA attribute audit
- Keyboard navigation analysis
- Color contrast scores (APCA)
- Screen reader compatibility
- Cognitive accessibility (ADHD, dyslexia considerations)
- **Code fix for every finding**

<br />

## All commands

### Make — design and build

| Command | What you get |
|---------|-------------|
| `/fix` | Anti-slop engine — transforms AI-generated UI into production-quality design |
| `/style` | Complete visual identity — palette, type, spacing, tokens, references |
| `/palette` | Color system — oklch scales, APCA scores, dark mode mapping |
| `/type` | Typography — font pairing, type scale, fluid sizing, platform stacks |
| `/tokens` | W3C design tokens — 3-tier, multi-theme, CSS + Tailwind + JSON |
| `/screen` | Production screen — 30+ types, all states, responsive, accessible |
| `/component` | Production component — React/SwiftUI/CSS, 10 states, ARIA, tests |
| `/page` | Full page — block composition, spacing rhythm, SEO, lazy loading |
| `/wireframe` | ASCII wireframes — 2-3 layout options with rationale |
| `/layout` | Page grid — CSS Grid/Flexbox, container queries, responsive |
| `/form` | Complete form — validation, multi-step, Zod schema, accessibility |
| `/nav` | Navigation — sidebar, top bar, bottom tabs, command palette |
| `/animate` | Motion recipes — CSS + Framer Motion, reduced-motion fallbacks |
| `/icon` | Icon system — library selection, sizing scale, React wrapper |
| `/dark` | Dark mode — oklch luminance mapping, elevation, toggle component |
| `/responsive` | Responsive — breakpoints, fluid scaling, block transformations |
| `/onboard` | Onboarding — step sequence, permissions, activation metrics |
| `/generate` | AI generation — mockups, icons, illustrations via MCP |
| `/remix` | Redesign — fix top 5 problems with UX reasoning for each change |

### Review — evaluate and improve

| Command | What you get |
|---------|-------------|
| `/audit` | Full design audit — heuristics, cognitive, flow, dark patterns, score |
| `/roast` | Quick critique — 10 dimensions, letter grade, must-fix list |
| `/grade` | Visual score — Awwwards-calibrated, designer DNA match |
| `/qa` | Design QA — token compliance, state coverage, responsive check |
| `/a11y` | Accessibility — WCAG 2.2 AA, ARIA, keyboard, contrast, code fixes |
| `/before-after` | Before/after comparison — visual proof of design transformation |

### Plan — research and strategy

| Command | What you get |
|---------|-------------|
| `/brief` | Problem definition — persona, constraints, success criteria |
| `/research` | Research plan — interview scripts, surveys, usability tests |
| `/benchmark` | Competitive analysis — scorecard vs top 5, gap analysis |
| `/map` | Information architecture — sitemap, nav hierarchy, URL structure |
| `/measure` | Metrics plan — HEART framework, experimentation strategy |
| `/preflight` | Launch checklist — SEO, performance, analytics, legal, monitoring |

### Utility

| Command | What it does |
|---------|-------------|
| `/sumi` | Show all commands and quick-start guide |
| `/next` | Suggest what to do next based on context |
| `/status` | Show what you've built so far |

<br />

## Starter recipes

Run `/style` with just a sector name. Zero config needed.

```
/style saas          → Professional dashboard system (Linear DNA)
/style fintech       → Trust-first banking aesthetic (Stripe DNA)
/style ecommerce     → Conversion-optimized store (Shopify DNA)
/style healthcare    → Calm clinical interface (One Medical DNA)
/style creative      → Bold editorial portfolio (Awwwards DNA)
/style education     → Friendly learning platform (Duolingo DNA)
/style social        → Content-first community (Discord DNA)
/style devtools      → Dark-native developer tool (GitHub DNA)
/style landing       → Show-stopping marketing page (Vercel DNA)
/style mobile        → Platform-native app (iOS/Android adaptive)
```

Each recipe generates a complete design system — palette, typography, spacing, motion, radius, shadows, tokens — tuned to that sector's conventions. No questions asked.

<br />

## Design Quality Score

Run `/grade` on any UI and get a single 0-100 score — like Lighthouse, but for design.

```
/grade
```

**Scoring across 7 dimensions:**
- Visual Hierarchy (20%) — information priority and scanning patterns
- Typography System (15%) — type scale, pairing, fluid sizing
- Color System (15%) — palette harmony, semantic usage, contrast
- Spacing & Layout (15%) — grid consistency, responsive behavior
- Component Quality (15%) — state coverage, interaction feedback
- Accessibility (10%) — WCAG 2.2 AA compliance
- Design System Coherence (10%) — token usage and consistency

**Score 80+?** Get a "Designed with Chef Sumi" badge for your README.

<br />

## How it works

Chef Sumi is pure markdown — 42 skill files totaling 23,000+ lines of design intelligence, backed by 165 reference documents. When you run a command, Claude loads the relevant skills automatically. No API keys. No external services. No dependencies.

**The more context you give, the better the output:**

```
/component button                                → works
/component button for fintech iOS app,            → much better
  primary CTA for wire transfers,
  trust-first, audience 35-55 professionals
```

**Design memory** makes everything consistent:

```
/style fintech              ← establishes your design system
/screen dashboard           ← automatically uses fintech palette, type, tokens
/component card             ← same tokens, same visual language
/form settings              ← consistent spacing, colors, radii
/roast                      ← evaluates against YOUR system, not generic rules
```

<br />

## Install

```bash
mkdir -p ~/.claude/plugins && cd ~/.claude/plugins
git clone https://github.com/phazurlabs/sumi.git
```

Restart Claude Code. Run `/sumi` to see all commands.

<br />

## Requirements

- [Claude Code](https://github.com/anthropics/claude-code) CLI
- That's it. Pure markdown. Zero dependencies. Works offline.

<br />

---

<p align="center">
  <sub>v9.0.0 &middot; 34 commands &middot; 42 skills &middot; 165 reference docs</sub><br />
  <sub>Built by <a href="https://github.com/phazurlabs">Phazur Labs</a> &middot; Powered by Claude</sub>
</p>
