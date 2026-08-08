# Sumi

**Design intelligence for Claude Code.** Sumi gives Claude the working knowledge of a senior product designer — cognitive psychology, usability heuristics, accessibility law, design systems, and production component code — and the commands to act on it.

`v4.1.0` · 44 skills · 189 reference files · 37 commands · Apache-2.0

---

## Start here

Install it:

```
/plugin marketplace add phazurlabs/sumi
/plugin install sumi@sumi-marketplace
```

Then type one thing:

```
/sumi:start
```

It asks what you're working on in plain language, picks the right process, and runs it. You never have to know what any of the 44 skills are called.

That's the whole onboarding. Everything below is for when you want to drive it yourself.

---

## Three ways to use it

**1. Let it route you.** `/sumi:start` asks one question and begins. Best when the job spans more than one thing — a redesign, a launch, a new product.

**2. Run a command.** If you know what you want, go straight at it. Typing `/` shows what each expects.

```
/sumi:audit src/checkout/
/sumi:component a date picker, React, with error and disabled states
/sumi:fix DashboardCard.tsx
```

**3. Just ask.** Skills activate on their own. You don't invoke them.

```
"What does Fitts's Law say about button sizing?"
"Is this countdown timer a dark pattern?"
"Why does this dashboard feel cluttered?"
```

If you run a command with no target, it asks rather than inventing something to analyse. An audit of an imaginary interface reads as authoritative and is worthless.

---

## What to run when

| Your situation | Run this |
|---|---|
| Claude generated UI and it looks generic | `/sumi:fix` |
| Starting a new product or feature | `/sumi:brief` → `/sumi:style` → `/sumi:screen` |
| Need to know if a design is any good | `/sumi:grade` for a score, `/sumi:roast` for a fast critique |
| Something's wrong but you can't name it | `/sumi:audit` |
| Accessibility review before shipping | `/sumi:a11y` |
| Building one component properly | `/sumi:component` |
| Setting up a design system | `/sumi:tokens` |
| Turning a Figma file into code | `/sumi:figma` |
| Checking an AI feature is trustworthy | `/sumi:ai-audit` |
| About to launch | `/sumi:preflight` |
| Lost | `/sumi:next` |

---

## Recipes

Real sequences that work. Each command writes its decisions to `.sumi/`, so later commands inherit them.

**Fix AI-generated UI** — the most common job.

```
/sumi:fix Card.tsx          →  detects slop, rewrites it, cites the principle for each fix
/sumi:before-after          →  side-by-side proof of what changed
/sumi:grade                 →  Design Quality Score, 0-100
```

**Build a screen from nothing.**

```
/sumi:brief                 →  persona, constraints, success criteria
/sumi:style fintech         →  palette, type, spacing, motion — saved to .sumi/
/sumi:wireframe checkout    →  structure before pixels
/sumi:screen checkout       →  production code, every state
/sumi:a11y                  →  WCAG 2.2 pass with corrected code
```

**Audit something that exists.**

```
/sumi:audit src/            →  heuristics, cognitive load, flow, ethics, AI-slop
/sumi:remix                 →  evidence-based redesign of the weak areas
/sumi:qa                    →  does the build match the spec
```

**Stand up a design system.**

```
/sumi:tokens                →  W3C DTCG tokens: CSS, Tailwind, Style Dictionary
/sumi:dark                  →  dark mode derived from the light palette
/sumi:component Button      →  reference implementation, all states
/sumi:figma                 →  keep design and code in sync
```

---

## Design memory

Sumi remembers decisions across commands in a `.sumi/` directory at your project root.

`/sumi:style` decides a visual direction once and writes it to `.sumi/style.json`. Every later command reads it, so `/sumi:screen` uses your palette instead of inventing one, and `/sumi:fix` corrects toward *your* system rather than a generic one.

| File | Written by | Holds |
|---|---|---|
| `style.json` | `/style`, `/palette`, `/type`, `/tokens`, `/dark` | tokens, tone, reference apps |
| `brief.json` | `/brief` | persona, constraints, success criteria |
| `map.json` | `/map` | sitemap and screen inventory |
| `vision.json` | `/grade` | score and designer-DNA match |
| `decisions.log` | any command | append-only record of what changed and why |

Commit `.sumi/` to share the design direction with your team. Delete it to start fresh.

---

## The 37 commands

New here, run `/sumi:start`. For the full map with starter recipes, run `/sumi:sumi`.

**MAKE (20)** — design and build

`/fix` `/style` `/palette` `/type` `/layout` `/wireframe` `/screen` `/component` `/page` `/tokens` `/form` `/nav` `/animate` `/icon` `/dark` `/responsive` `/onboard` `/generate` `/remix` `/figma`

**REVIEW (7)** — evaluate and improve

`/audit` `/roast` `/grade` `/qa` `/a11y` `/before-after` `/ai-audit`

**PLAN (6)** — research and strategy

`/brief` `/research` `/benchmark` `/map` `/measure` `/preflight`

**UTILITY (4)**

`/start` `/sumi` `/next` `/status`

The four that do the most work:

| Command | What it does |
|---|---|
| `/fix` | Anti-slop engine. Takes UI that works but looks machine-made and rebuilds the design layer — typography, colour, spacing, states, accessibility — without touching your logic. |
| `/audit` | Five lenses in one pass: heuristics with severity ratings, cognitive load, flow, dark patterns, and AI-slop detection. Ends with a scored roadmap. |
| `/grade` | Design Quality Score 0-100 across ten dimensions, Awwwards-calibrated. Honest: most AI-generated UI scores 30-50. |
| `/style` | Sector-aware visual direction — fintech reads differently from healthcare. Writes to `.sumi/` so everything downstream inherits it. |

---

## How it works

### Progressive disclosure

Sumi is large. It stays cheap by loading in three tiers:

| Tier | Loads | Cost |
|---|---|---|
| Skill descriptions | always | ~4,400 tokens |
| A skill's `SKILL.md` | when that skill triggers | ~1,500–4,000 tokens |
| Its `references/` | only when the skill points at one and it's needed | on demand |

So asking about button sizing loads the cognitive psychology skill, not the other 43. Asking for a React modal loads the component cookbook, not the Figma pipeline.

This is why v4.1.0 moved 125,000 tokens out of the always-loaded tier: a `/style` → `/screen` → `/fix` session went from 133,000 tokens to 70,000, which is the difference between two-thirds of your context window and a third of it.

### The orchestrator

Broad requests go to `sumi-orchestrator`, which picks one of twelve pipelines and runs its stages in order.

| You want to… | Pipeline |
|---|---|
| Find what's wrong with something that exists | Evaluate |
| Fix AI-generated UI that runs but looks wrong | Fix |
| Design something that doesn't exist yet | Create |
| Build or ship an actual component | Implement |
| Compose a whole page | Compose |
| Generate design assets with AI | Generate |
| Start or scale a design system | Systematize |
| Move a design into code | Handoff |
| Understand why people aren't finishing | Convert |
| Ship to new countries or languages | Localize |
| Design an AI or agent feature | AI Surface |
| Know whether any of it worked | Measure |

Every stage has a **gate** it must clear before the next begins. Evaluate won't advance while findings lack a severity rating, because unrated findings are opinions and opinions don't survive a prioritisation meeting. Implement won't advance until every state is rendered and keyboard-navigable. You find out at stage three, not at the end.

---

## The 44 skills

Skills activate automatically. You never call them directly.

**Routing** — `sumi-orchestrator`, `design-memory`

**Foundations** — `nng-ux-heuristics`, `cognitive-psychology-ux`, `ux-research-methods`, `ux-metrics-measurement`, `ux-ethics-content-strategy`, `design-process-methods`

**Visual craft** — `ui-visual-design-system`, `visual-design-mastery`, `color-palette-library`, `typography-pairing-recipes`, `shadow-elevation-density`, `image-media-patterns`, `icon-illustration-systems`

**Patterns and composition** — `ui-pattern-intelligence`, `screen-flow-patterns`, `layout-block-intelligence`, `page-composition-engine`, `navigation-pattern-encyclopedia`, `form-design-encyclopedia`, `responsive-block-patterns`

**Systems and code** — `design-systems-architecture`, `design-token-presets`, `component-patterns-code`, `figma-design-tool-workflows`, `performance-states-patterns`

**Platform** — `mobile-ux-design`, `desktop-app-design`, `platform-visual-standards`, `ambient-calm-zero-ui`, `cross-cultural-i18n-ux`

**Experience and craft** — `interaction-motion-design`, `animation-recipe-library`, `micro-copy-intelligence`, `accessibility-inclusive-design`

**Strategy and outcomes** — `sector-style-intelligence`, `conversion-optimization-patterns`, `data-visualization-mastery`, `design-critique-case-studies`, `business-design-templates`

**AI** — `agentic-ai-generative-ux`, `ai-spatial-voice-ux`, `ai-design-generation`

---

## What's verified, and what isn't

Sumi makes empirical claims, so it keeps an auditable record of which ones hold up.

`AUDIT.md` lists every claim checked against a primary source, every one corrected, and every one still outstanding. v3.1.0 corrected six defects — including a dark-mode power figure that was wrong by two orders of magnitude and two statistics attributed to research that doesn't contain them.

**54 of 84 extracted claims are not yet triaged**, almost all in skills that arrived with the v4.0.0 merge. `conversion-optimization-patterns` is the highest-risk cluster: conversion statistics are the most-copied and least-sourced numbers in the industry. Use its patterns; don't quote its figures to a client until they're checked.

Two scripts keep this honest, both wired into CI:

- `scripts/validate-plugin.py` — the release gate. Manifest shape, frontmatter, kebab-case names, and any count stated in the README or manifests that disagrees with the actual tree.
- `scripts/check-corpus.py` — the knowledge graph. Every reference must be reachable from a skill, no file may silently grow, no retired command name may linger, and no `.sumi/` artifact may carry two schemas. Existing debt is frozen against a committed baseline; new debt is a hard error.

A green build proves the plumbing is sound. It doesn't prove the advice is good — that's judgment, and judgment doesn't fit in CI.

---

## Installation

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code), authenticated. No other dependencies — the plugin is markdown, zero config, works offline.

### From the marketplace (recommended)

Inside a Claude Code session:

```
/plugin marketplace add phazurlabs/sumi
/plugin install sumi@sumi-marketplace
```

Scope is chosen at install: user (all your projects), project (shared with your team via `.claude/settings.json`), or local (personal, gitignored).

### For development

```bash
git clone https://github.com/phazurlabs/sumi.git
claude --plugin-dir ./sumi
```

Loads for that session only.

### Verify it worked

```
/sumi:start
```

If the command exists, you're installed. Commands appear namespaced as `/sumi:<name>`.

Then check skills activate by asking something they cover:

```
"What does Fitts's Law say about button sizing?"
"Build me a React modal with all states"
```

### Troubleshooting

| Problem | Fix |
|---|---|
| Commands don't appear | Restart Claude Code after installing |
| `/plugin` not recognised | Update Claude Code to the latest version |
| Skills never activate | Check `.claude-plugin/plugin.json` exists at the plugin root |
| Stuck on an old version | `version` in `plugin.json` is the cache key — `/plugin update sumi` |
| Uninstall | `/plugin uninstall sumi` |

---

## Architecture

```
sumi/
├── .claude-plugin/
│   ├── plugin.json                 name, version (the cache key), license
│   └── marketplace.json            marketplace listing
│
├── skills/                         44 skills, auto-invoked
│   ├── sumi-orchestrator/          the router: 12 pipelines, stages, gates
│   └── <skill>/
│       ├── SKILL.md                loads in full whenever the skill triggers
│       └── references/             189 reference files; load only when pointed at
│
├── commands/                       37 commands, user-invoked
├── scripts/
│   ├── validate-plugin.py          release gate: structure, frontmatter, counts
│   ├── check-corpus.py             knowledge graph and context budget
│   └── extract-claims.py           pulls empirical claims for citation audit
├── tests/
│   ├── baseline.json               committed ratchet baselines
│   └── routing-fixtures.yaml       does the right skill fire for a real request
├── AUDIT.md                        claims verified, corrected, outstanding
└── CHANGELOG.md
```

The split that matters: **`SKILL.md` loads in full every time its skill triggers; `references/` load only when a skill points at them.** That is why depth lives in `references/`, and why keeping skills thin is enforced rather than encouraged.

---

## Built on

| Thinker | Contribution |
|---|---|
| Don Norman | Affordances, emotional design, three levels of processing |
| Jakob Nielsen | Ten usability heuristics, evidence-based evaluation |
| Daniel Kahneman | Peak-End Rule, cognitive biases, System 1 and 2 |
| John Sweller | Cognitive Load Theory |
| Dieter Rams | "Less, but better" |
| Edward Tufte | Information density with clarity |
| Amber Case | Calm technology, peripheral attention |
| Luke Wroblewski | Mobile-first, form design |
| Liz Lerman | Critical Response Process for critique |

Standards and sources: W3C (WCAG 2.2, Design Tokens 2025.10, WAI-ARIA), Nielsen Norman Group, Baymard Institute, Apple HIG (iOS 26), Material Design 3 Expressive, and product teardowns of Stripe, Linear, Notion, Figma, Arc, Vercel and others — alongside post-mortems of Snapchat 2018, Windows 8, Digg v4, Sonos 2024 and Healthcare.gov, because failures teach faster.

---

## License

Apache-2.0. See `LICENSE`, `NOTICE`, and `TRADEMARKS.md`. Contributions require a CLA — see `CONTRIBUTING.md`.

*Built by [Phazur Labs](https://phazurlabs.com).*
