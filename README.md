# Sumi — UX/UI Design Intelligence for Claude Code

### The most comprehensive UX/UI design intelligence ever built for an AI coding assistant.

**v4.0.0** | 43 Skills | 168 References | 37 Commands | 1,066,453 Words | 265 Files

---

> *"Every pixel on a screen is ultimately processed by a human brain. This plugin ensures Claude understands that brain."*

---

## Quick start

**If you've never used this before**, type one thing:

```
/sumi:start
```

It asks what you're working on in plain language, picks the right process, and
runs it. No knowledge of the 43 skills required — you never have to choose
from a list.

**If you know what you want**, go straight at it:

```
/sumi:ux-audit src/checkout/
/sumi:component-build a date picker, React, with error and disabled states
/sumi:accessibility-check LoginForm.tsx
```

Every command shows what it expects when you type `/`. If you run one without a
target, it asks rather than inventing something to analyze.

**If your request spans several areas** — a redesign, a launch, a new product —
the orchestrator picks the pipeline and sequences the skills for you:

| You want to… | Sumi runs |
|---|---|
| Check something that exists | Heuristics → cognitive load → accessibility → ethics |
| Design something new | Research → constraints → visual → motion → states → a11y |
| Build a component | Tokens → visual spec → code → a11y → performance |
| Start a design system | Architecture → visual language → components → Figma sync |
| Ship internationally | i18n → layout → accessibility |
| Design an AI feature | Agent patterns → conversational → ethics → trust |
| Prove it worked | Metrics → research design |

Each stage has a gate it must pass before the next begins, so you find out at
stage 3 that findings are unrated — not at the end.

---

## Why This Exists

Most design tools give you components. Most AI assistants give you opinions. Neither gives you **the science of why users behave the way they do** — and the production code to act on it.

This plugin gives Claude Code the equivalent of a senior UX designer's entire career knowledge: cognitive psychology, battle-tested heuristics, platform-native component code, real product case studies, and the latest 2025-2026 research — all activated automatically when you need it.

**The result:** Claude doesn't just suggest "make the button bigger." It tells you Fitts's Law predicts a 23% improvement at 48px, generates the accessible React component with all 10 states, and flags that your 14-option dropdown violates Hick's Law.

## What Changed in v4.0.0

Sumi 3.1.0 and Chef Sumi were one lineage that forked in February 2026. One grew
the corpus; the other fixed the engineering. v4.0.0 merges them back into a single
plugin, keeping both.

| From Chef Sumi | From Sumi 3.1.0 |
|---|---|
| 23 additional skills — visual design mastery, UI pattern intelligence, sector style, layout and page composition, conversion, dataviz, microcopy | Citation audit: six empirical claims corrected against primary sources |
| 34 action-first commands across MAKE / REVIEW / PLAN tiers | Kebab-case skill names, quoted `argument-hint`, input guards on every command |
| The `.sumi/` design memory that carries style decisions between commands | `sumi-orchestrator` and `/start` — routing, so you never pick from a list of 43 |
| The anti-slop engine (`/fix`) and Design Quality Score (`/grade`) | `scripts/validate-plugin.py` and CI gates that keep all of it honest |

The merge also fixed a scoring defect inherited from Chef Sumi: `/audit` ran its
Laws of UX and Gestalt lenses twice, in two sections weighted separately, so the
same cognitive analysis carried 35% of the composite score and the two sections
could disagree about one interface. They are now one section.

Ten command names from 3.1.0 were retired or renamed — see the table in `/sumi`.

---

## Installation

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated
- No other dependencies — the plugin is pure markdown, zero config

---

### Method 1: Install from GitHub Marketplace (Recommended for End Users)

This is the standard way to install Claude Code plugins. Run these commands **inside a Claude Code session**:

```
/plugin marketplace add phazurlabs/sumi
/plugin install sumi@sumi-marketplace
```

That's it. The plugin is now permanently installed and available in every session.

To choose installation scope:
- **User scope** (all projects): Plugin is registered in `~/.claude/settings.json`
- **Project scope** (team-shared): Plugin is registered in `.claude/settings.json` in your project
- **Local scope** (personal, gitignored): Plugin is registered in `.claude/settings.local.json`

---

### Method 2: Clone + Load Directly (For Development / Testing)

Clone the repo anywhere, then load it with the `--plugin-dir` flag:

```bash
git clone https://github.com/phazurlabs/sumi.git
claude --plugin-dir ./sumi
```

This loads the plugin for that session only. Great for testing or development.

---

### Method 3: Clone + Register Permanently (Manual)

**Step 1:** Clone into the plugins directory:

```bash
mkdir -p ~/.claude/plugins
cd ~/.claude/plugins
git clone https://github.com/phazurlabs/sumi.git
```

**Step 2:** Register the plugin in your Claude Code settings. Edit `~/.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "sumi": true
  }
}
```

**Step 3:** Restart Claude Code. The plugin loads automatically every session.

---

### Verify Installation

Start Claude Code and run any slash command:

```
/ux-audit
/cognitive-check
/component-build
/design-critique
/figma-to-code
```

Commands appear as `/sumi:command-name` (e.g., `/sumi:ux-audit`).

You can also test skill activation by asking about any trigger topic:

```
"What does Fitts's Law say about button sizing?"
"Audit this component for cognitive load"
"Build me a React modal with all states"
"What went wrong with the Snapchat 2018 redesign?"
```

The relevant skill and deep references load automatically based on your query.

### Troubleshooting

| Problem | Solution |
|---------|----------|
| Commands not showing up | Restart Claude Code after installation |
| `/plugin` command not recognized | Update Claude Code to the latest version |
| Skills not activating on topics | Verify `plugin.json` exists at `.claude-plugin/plugin.json` |
| Want to uninstall | Run `/plugin uninstall sumi` or remove from `settings.json` |

### Requirements

- Claude Code CLI (latest version)
- No external dependencies — pure markdown, zero config, works offline

---

## 37 Commands at Your Fingertips

New here? Run `/sumi:start` — it asks one question and routes you. `/sumi:sumi` is
the full map with starter recipes.

**MAKE (20)** — design and build

`/fix` `/style` `/palette` `/type` `/layout` `/wireframe` `/screen` `/component`
`/page` `/tokens` `/form` `/nav` `/animate` `/icon` `/dark` `/responsive`
`/onboard` `/generate` `/remix` `/figma`

**REVIEW (7)** — evaluate and improve

`/audit` `/roast` `/grade` `/qa` `/a11y` `/before-after` `/ai-audit`

**PLAN (6)** — research and strategy

`/brief` `/research` `/benchmark` `/map` `/measure` `/preflight`

**UTILITY (4)**

`/start` `/sumi` `/next` `/status`

| Hero command | What it does |
|---|---|
| `/fix` | Anti-slop engine — turns AI-generated UI into production quality |
| `/audit` | Heuristics, cognitive load, flow, ethics, and AI-slop in one pass |
| `/grade` | Design Quality Score 0-100, Awwwards-calibrated |
| `/style` | Sector-aware visual direction, written to `.sumi/` for every later command |

## 43 Skills — The Complete Design Brain

Skills activate automatically. You never call them directly — `sumi-orchestrator`
routes to them, which is why `/start` never asks you to pick from a list.

**Routing (1)** — `sumi-orchestrator`

**Foundations (6)** — `nng-ux-heuristics`, `cognitive-psychology-ux`,
`ux-research-methods`, `ux-metrics-measurement`, `ux-ethics-content-strategy`,
`design-process-methods`

**Visual craft (7)** — `ui-visual-design-system`, `visual-design-mastery`,
`color-palette-library`, `typography-pairing-recipes`, `shadow-elevation-density`,
`image-media-patterns`, `icon-illustration-systems`

**Patterns and composition (7)** — `ui-pattern-intelligence`,
`screen-flow-patterns`, `layout-block-intelligence`, `page-composition-engine`,
`navigation-pattern-encyclopedia`, `form-design-encyclopedia`,
`responsive-block-patterns`

**Systems and code (5)** — `design-systems-architecture`, `design-token-presets`,
`component-patterns-code`, `figma-design-tool-workflows`,
`performance-states-patterns`

**Platform (5)** — `mobile-ux-design`, `desktop-app-design`,
`platform-visual-standards`, `ambient-calm-zero-ui`, `cross-cultural-i18n-ux`

**Experience and craft (4)** — `interaction-motion-design`,
`animation-recipe-library`, `micro-copy-intelligence`,
`accessibility-inclusive-design`

**Strategy and outcomes (5)** — `sector-style-intelligence`,
`conversion-optimization-patterns`, `data-visualization-mastery`,
`design-critique-case-studies`, `business-design-templates`

**AI (3)** — `agentic-ai-generative-ux`, `ai-spatial-voice-ux`,
`ai-design-generation`

## How It Works

The plugin uses **progressive disclosure** — the same cognitive principle it teaches. Only the relevant skill and its references load based on your query, keeping Claude's context lean while providing deep expertise on demand.

Ask about "cognitive load" and Claude loads the cognitive psychology skill with 25+ Laws of UX. Ask about "React button component" and Claude loads the component patterns skill with the full React cookbook. Ask about "iOS 26" and Claude loads mobile UX with the Liquid Glass deep-dive.

Every skill cross-references every other skill. Critique methodology connects to heuristic evaluation. Component code connects to accessibility. Figma workflows connect to design tokens. Cognitive biases connect to ethics. It's a web of knowledge, not a stack of silos.

---

## Design Philosophy

Built on the shoulders of giants:

| Thinker | Contribution to This Plugin |
|---------|----------------------------|
| **Don Norman** | Affordances, emotional design, the 3 levels of processing |
| **Jakob Nielsen** | 10 usability heuristics, evidence-based evaluation |
| **Daniel Kahneman** | Peak-End Rule, cognitive biases, System 1/System 2 |
| **John Sweller** | Cognitive Load Theory (intrinsic, extraneous, germane) |
| **Dieter Rams** | "Less, but better" — systematic minimalism |
| **Edward Tufte** | Data visualization, information density with clarity |
| **Amber Case** | Calm technology, peripheral attention |
| **Luke Wroblewski** | Mobile-first, form design |
| **Julie Zhuo** | Design leadership, scaling quality |
| **Liz Lerman** | Critical Response Process for design critique |

---

## Architecture

```
sumi/
├── .claude-plugin/
│   ├── plugin.json                 name, version (the cache key), license
│   └── marketplace.json            marketplace listing
│
├── skills/                         43 skills, auto-invoked
│   ├── sumi-orchestrator/          the router: 12 pipelines, stages, gates
│   └── <skill>/
│       ├── SKILL.md                loads in full whenever the skill triggers
│       └── references/             168 files; load only when SKILL.md points at them
│
├── commands/                       37 commands, user-invoked
├── scripts/
│   ├── validate-plugin.py          structure, counts, frontmatter — CI gate
│   └── extract-claims.py           pulls empirical claims for citation audit
├── .github/workflows/              license preflight + CLA
├── AUDIT.md                        which claims are verified, corrected, outstanding
└── CHANGELOG.md
```

The split that matters: **SKILL.md loads in full every time its skill triggers;
references load only when a SKILL.md points at them.** That is why depth lives in
`references/` and why `validate-plugin.py` warns when a SKILL.md gets fat.

## Knowledge Base by the Numbers

| Metric | Count |
|--------|-------|
| Total words | **1,066,453** |
| Skills | **43** (42 domains + orchestrator) |
| Deep reference files | **168** |
| Executable commands | **37** |
| Production code components | **40+** |
| Laws of UX (with formulas) | **25+** |
| Cognitive biases (with ethical flags) | **50+** |
| Product case studies | **10** |
| Redesign failure analyses | **10** |
| Eye tracking patterns | **6** |
| Platform cookbooks | **3** (React, SwiftUI, CSS) |
| Haptic feedback patterns | **30+** |
| Microcopy templates | **50+** |
| Cultural dimension mappings | **6** |
| Design system maturity levels | **5** |

---

## Research Sources

Every claim in this plugin traces back to authoritative research:

**Cognitive Science**
Kahneman (Peak-End Rule, System 1/2), Sweller (Cognitive Load Theory), Cowan (Working Memory), Iyengar & Lepper (Choice Overload), Fitts, Hick, Miller, Gestalt school, Simon (Satisficing), Csikszentmihalyi (Flow)

**Academic Research**
arXiv: UX 3.0 Paradigm, GenAI for UX Research, EvAlignUX, Emotion-Aware Interaction, LLM Hallucination Detection | ACM CHI 2025: Designing UIs with AI, Screen Reader + AI Coding, Multi-Agent GenAI, AI Literacy

**Industry Standards**
W3C: WCAG 3.0 Working Draft, Design Tokens Oct 2025 Stable, WAI-ARIA | NNG Group 2025-2026: State of UX, AI Literacy, "AI Slop" Quality Gates, iOS 26 Usability Critique

**Platform Sources**
Apple WWDC 2025 (iOS 26 Liquid Glass) | Google I/O 2025 (Material 3 Expressive) | Figma Config 2025 (MCP, Code Connect)

**Industry Voices**
Smashing Magazine Feb 2026 (Agentic UX) | Microsoft Copilot Framework | OpenAI Apps SDK | Sparkbox (Design System ROI) | Amber Case (Calm Technology) | Liz Lerman (Critical Response Process)

**Case Studies**
Stripe, Linear, Notion, Airbnb, Figma, Arc Browser, Duolingo, Vercel, Apple Health, Discord | Failures: Snapchat 2018, Windows 8, Digg v4, Sonos 2024, Healthcare.gov, Twitter/X, Google Plus, Reddit API, YouTube Dislikes, Skype

---

## License

Apache-2.0. See `LICENSE`, `NOTICE`, and `TRADEMARKS.md`.

---

*Built by Phazur Labs.*
