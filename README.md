<p align="center">
  <img src="assets/sumi.svg" alt="Sumi" width="120" />
</p>
<h1 align="center">Sumi.</h1>
<p align="center">
  <strong>UX/UI intelligence for Claude Code.</strong><br />
  Meet <strong>Sumi</strong> — your AI design companion with a decade of senior UX experience.
</p>
<p align="center">
  <a href="#install"><strong>Install</strong></a> ·
  <a href="#the-20-commands"><strong>Commands</strong></a> ·
  <a href="#which-command-do-i-use"><strong>Workflows</strong></a> ·
  <a href="#21-skills"><strong>Skills</strong></a> ·
  <a href="#whats-new-in-v40"><strong>What's New</strong></a>
</p>
<p align="center">
  <code>20 commands</code> · <code>21 skills</code> · <code>65+ references</code> · <code>375K+ words</code>
</p>

---

<br />

## See it in action

<table>
<tr>
<td width="50%">

**Get a complete style direction for any sector**
```
/taste fintech
```
Color palette (hex + OKLCH), font pairing, spacing system, component personality, motion language, tone of voice, 5 reference apps, do's and don'ts, and a W3C design token starter kit.

</td>
<td width="50%">

**Build a full production screen**
```
/screen checkout
```
Semantic HTML, component hierarchy, 7 states (empty → loading → populated → error → partial → offline → updating), responsive breakpoints, ARIA, keyboard nav, and design token consumption.

</td>
</tr>
<tr>
<td width="50%">

**Roast any design**
```
/roast
```
Liz Lerman critique across 10 dimensions. Must-fix, should-fix, could-improve — every finding grounded in heuristics and cognitive psychology.

</td>
<td width="50%">

**Ship a component**
```
/ship modal
```
Production-ready React/SwiftUI/CSS with 10 states, full ARIA, keyboard handling, design tokens, and a test skeleton. Copy-paste into your codebase.

</td>
</tr>
<tr>
<td width="50%">

**Scan for dark patterns**
```
/dark-scan
```
22 deceptive pattern categories checked against FTC, GDPR, DSA, and CPRA. Ethical redesign alternatives for every finding.

</td>
<td width="50%">

**Find the right pattern**
```
/inspo screen login
```
Best-practice patterns, 5 reference implementations, key principles, common mistakes, and curated Mobbin/Screenlane/Refero links.

</td>
</tr>
</table>

<br />

## How it works

The plugin uses **progressive disclosure** — the same cognitive principle it teaches.

When you ask about "cognitive load," Claude loads the cognitive psychology skill with 25+ Laws of UX. When you say `/ship button`, Claude loads the component patterns skill with the full React/SwiftUI/CSS cookbook. When you type `/taste fintech`, Claude pulls from the sector style intelligence skill with real color palettes, font choices, and spacing systems from Stripe, Mercury, and Wise.

**Every skill cross-references every other skill.** Critique methodology connects to heuristic evaluation. Component code connects to accessibility. Figma workflows connect to design tokens. Cognitive biases connect to ethics. It's a web of knowledge, not a stack of silos.

**Every command chains to the next.** Run `/roast` and the output suggests `/remix` to fix what was found. Run `/taste` and it points you to `/inspo` for screen patterns and `/screen` to start building. No dead ends.

<br />

## Install

### Recommended: Claude Code marketplace

```
/plugin marketplace add phazurlabs/taste-ux-ui
/plugin install ux-ui-mastery@ux-ui-mastery-marketplace
```

That's it. Available in every session, forever.

### Alternative: Clone manually

```bash
mkdir -p ~/.claude/plugins && cd ~/.claude/plugins
git clone https://github.com/phazurlabs/taste-ux-ui.git
```

Then add to `~/.claude/settings.json`:
```json
{
  "enabledPlugins": {
    "ux-ui-mastery": true
  }
}
```

### Verify it works

Restart Claude Code and try any command:
```
/taste saas
/roast
/ship button
/inspo screen dashboard
```

Commands appear as `/ux-ui-mastery:command-name` (e.g., `/ux-ui-mastery:taste`).

Skills activate automatically — just ask about any UX topic:
```
"What does Fitts's Law say about button sizing?"
"Audit this component for cognitive load"
"What went wrong with the Snapchat 2018 redesign?"
```

<details>
<summary><strong>Troubleshooting</strong></summary>

| Problem | Solution |
|---------|----------|
| Commands not showing up | Restart Claude Code after installation |
| `/plugin` command not recognized | Update Claude Code to the latest version |
| Skills not activating on topics | Verify `plugin.json` exists at `.claude-plugin/plugin.json` |
| Want to uninstall | `/plugin uninstall ux-ui-mastery` or remove from `settings.json` |

**Requirements:** Claude Code CLI (latest). No external dependencies — pure markdown, zero config, works offline.

</details>

<br />

## The 20 Commands

### Audit — find what's wrong

| Command | One-liner | What you get |
|---------|-----------|-------------|
| `/vibe-check` | UX heuristic audit | Nielsen's 10 heuristics, severity 0-4, location-specific findings, prioritized fixes |
| `/roast` | Design critique | Liz Lerman process, 10 dimensions scored 1-10, must-fix/should-fix/could-improve |
| `/brain-scan` | Cognitive audit | 12 Laws of UX, 6 Gestalt principles, cognitive load analysis, bias ethics check |
| `/include` | Accessibility audit | WCAG 2.2 AA, semantic HTML, ARIA, keyboard nav, contrast — with code fixes |
| `/trust-scan` | AI UX audit | Trust, Safety, Usability, Accessibility scored 0-100 each + anti-pattern detection |
| `/flow` | Flow audit | Multi-screen journey analysis, drop-off risk per step, emotional arc, conversion fixes |
| `/dark-scan` | Dark pattern scan | 22 deceptive pattern categories, FTC/GDPR/DSA compliance, ethical alternatives |
| `/copy-check` | Content audit | Reading level, tone, inclusive language, truncation risk, i18n readiness |
| `/responsive` | Responsive audit | 7 breakpoint tiers, touch targets, reflow, fluid type, container queries, CSS fixes |

### Build — create something new

| Command | One-liner | What you get |
|---------|-----------|-------------|
| `/ship` | Component builder | React/SwiftUI/CSS with 10 states, ARIA, keyboard, tokens, test skeleton |
| `/screen` | Screen builder | 25+ screen types, component hierarchy, 7 states, responsive, a11y, production code |
| `/drip` | Token generator | W3C Design Tokens: 3-tier system (primitive → semantic → component), multi-theme |
| `/extract` | Figma → code | Token extraction, component decomposition, platform code, a11y validation |
| `/onboard` | Onboarding builder | Step sequence, progressive disclosure, permission timing, activation metrics |
| `/remix` | Redesign engine | Top 5 problems identified → redesigned code → UX principle cited for every change |

### Strategy — plan and decide

| Command | One-liner | What you get |
|---------|-----------|-------------|
| `/taste` | Style direction | Color, type, spacing, components, motion, tone, references, tokens — for any sector |
| `/inspo` | Inspiration finder | Screen, element, or flow patterns with best-in-class references and source links |
| `/pulse` | Metrics plan | HEART framework mapping, dashboards, experimentation framework, 90-day roadmap |
| `/judge` | Full review | All 21 skill domains scored, priority roadmap (quick wins → medium → strategic) |
| `/benchmark` | Competitive analysis | 10-dimension scorecard vs. top 5 apps, gap analysis, improvement tiers |

<br />

## Which command do I use?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  "I'm starting a new project"                                       │
│   /taste  →  /inspo  →  /screen  →  /ship                          │
│                                                                     │
│  "I need to check my work"                                          │
│   /vibe-check  →  /include  →  /brain-scan                         │
│                                                                     │
│  "I want to improve what I have"                                    │
│   /roast  →  /remix                                                 │
│                                                                     │
│  "I need to build a specific thing"                                 │
│   /ship [component]  or  /screen [type]                             │
│                                                                     │
│  "I need design direction"                                          │
│   /taste [sector]  →  /inspo [screen/element/flow]                  │
│                                                                     │
│  "Is this ethical?"                                                  │
│   /dark-scan  →  /copy-check                                        │
│                                                                     │
│  "How do I compare to the best?"                                    │
│   /benchmark [category]                                             │
│                                                                     │
│  "I need to build onboarding"                                       │
│   /onboard  →  /flow  →  /copy-check                               │
│                                                                     │
│  "I want metrics"                                                   │
│   /pulse                                                            │
│                                                                     │
│  Every command suggests the logical next command in its output.     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

<br />

## 21 Skills

The knowledge base behind every command. Skills activate automatically based on your query — no need to invoke them directly.

<details>
<summary><strong>Foundations</strong> — The science behind every decision</summary>

| Skill | Depth |
|-------|-------|
| **Cognitive Psychology UX** | 25+ Laws of UX with mathematical formulas. 50+ cognitive biases with ethical flags. Neurodesign: eye tracking patterns, dopamine loops, flow state. Hick's Law, Fitts's Law, Miller's Law, Peak-End Rule, Doherty Threshold, Von Restorff, Zeigarnik — all with code examples and anti-patterns. |
| **NNG UX Heuristics** | Nielsen's 10 heuristics with modern 2025+ interpretation. Severity rating scales (0-4). Systematic evaluation protocols. Cross-mapped to cognitive principles. |
| **UX Research Methods** | Contextual inquiry, usability testing, card sorting, diary studies, A/B testing, surveys. AI-augmented synthesis. JTBD, journey mapping, affinity diagramming, research synthesis. |
| **UX Metrics & Measurement** | HEART framework, SUS, UEQ, SUPR-Q. Task-based metrics. A/B testing statistics with sample size calculators. AI-specific metrics (hallucination rate, trust calibration). Design system ROI. |

</details>

<details>
<summary><strong>Implementation</strong> — Code that ships</summary>

| Skill | Depth |
|-------|-------|
| **Component Patterns & Code** | 40+ production components across React/TypeScript, SwiftUI, and CSS. Every component: typed props, all 10 states, ARIA, keyboard handling, design token consumption, `prefers-reduced-motion`. |
| **Design Systems Architecture** | W3C Design Tokens (Oct 2025 stable spec). Style Dictionary pipelines. Multi-brand token architecture. 5-level maturity model. Governance and DesignOps. ROI measurement. |
| **Figma Design Tool Workflows** | Auto Layout mastery. Variable modes. Dev Mode handoff. Figma MCP server integration. Code Connect. The full design-to-code flywheel. |
| **UI Visual Design System** | Typography scales. Color theory (oklch, color-mix, light-dark). Spacing systems. Visual hierarchy. Modern CSS: container queries, `:has()`, anchor positioning, view transitions, `@layer`, subgrid. |

</details>

<details>
<summary><strong>Platforms</strong> — Every screen, every context</summary>

| Skill | Depth |
|-------|-------|
| **Mobile UX Design** | iOS 26 Liquid Glass (`.glassEffect`, `GlassEffectContainer`). Material 3 Expressive (spring motion, morphing FAB). Touch, gesture, and wearable/IoT patterns. NNG usability critique of Liquid Glass. |
| **Desktop App Design** | Enterprise dashboards. Data-dense interfaces. Keyboard-first design. Data visualization (chart selection matrix, D3 patterns, accessible charts with sonification). Industry-vertical patterns. |
| **Cross-Cultural i18n UX** | RTL layout with CSS logical properties. CJK typography. Hofstede's 6 cultural dimensions mapped to interface design. Payment diversity by region. Trust signals by culture. |
| **Performance States Patterns** | Skeleton screens, optimistic UI, progressive loading (React + SwiftUI code). Notification architecture. Empty/error/onboarding state patterns. Perceived performance psychology. |

</details>

<details>
<summary><strong>Experience</strong> — Craft that users feel</summary>

| Skill | Depth |
|-------|-------|
| **Interaction & Motion Design** | Animation timing curves. Micro-interactions. M3 Expressive spring physics (stiffness/damping/mass). iOS Core Haptics + Android haptics. Brand haptic vocabulary. Don Norman's 3 levels of emotional design. |
| **Accessibility & Inclusive Design** | WCAG 2.2 full coverage. WCAG 3.0 April 2026 preview. ARIA authoring practices. Cognitive accessibility (ADHD, dyslexia, autism spectrum). Neurodiversity accommodations. |
| **Design Critique & Case Studies** | Liz Lerman Critical Response Process. 10 product deep-dives: Stripe, Linear, Notion, Airbnb, Figma, Arc Browser, Duolingo, Vercel, Apple Health, Discord. 10 redesign failure post-mortems. |
| **UX Ethics & Content Strategy** | Dark pattern detection and avoidance. 2025-2026 regulatory landscape (FTC, GDPR, DSA). Privacy UX. Sustainable/green UX. 50+ microcopy templates. |

</details>

<details>
<summary><strong>Emerging Tech</strong> — What's next</summary>

| Skill | Depth |
|-------|-------|
| **Agentic AI & Generative UX** | Multi-agent orchestration UX. Generative UI. RAG interfaces. LLM hallucination guardrails. Conversational AI dialogue patterns. Control/consent/accountability triad. |
| **AI, Spatial & Voice UX** | AI-native interface patterns. AR/VR spatial design. Voice-first UX. Multimodal interaction. The post-UI paradigm. |
| **Ambient Calm & Zero UI** | Amber Case's 8 principles of calm technology. Ambient displays. Proactive intelligence. Smart home/office/automotive. Peripheral attention design. |

</details>

<details>
<summary><strong>NEW in v4.0</strong> — Sector intelligence + screen/flow catalog</summary>

| Skill | Depth |
|-------|-------|
| **Sector Style Intelligence** | Complete style direction for 20+ sectors. Real hex color palettes from leading apps (Stripe, Headspace, Linear, Shopify, Duolingo, Netflix). Typography norms with specific font recommendations. Component conventions with px values. Motion personality with easing curves. Trust signals. Anti-patterns. W3C design token JSON for every sector. Powers `/taste` and `/benchmark`. |
| **Screen & Flow Patterns** | 27 screen types with layout patterns, key components, state matrices, and 3 reference implementations each. 15 user flows with step sequences, branching logic, error handling, and metric targets. 26 UI element deep-dives with anatomy, variants, states, platform differences (iOS/Android/Web), and accessibility requirements. Curated inspiration source guide. Powers `/screen`, `/flow`, and `/inspo`. |

</details>

<br />

## What's new in v4.0

<table>
<tr>
<th>v3.0</th>
<th>v4.0</th>
</tr>
<tr><td>10 commands</td><td><strong>20 commands</strong></td></tr>
<tr><td>19 skills</td><td><strong>21 skills</strong></td></tr>
<tr><td>55 references</td><td><strong>65+ references</strong></td></tr>
<tr><td>310K words</td><td><strong>375K+ words</strong></td></tr>
<tr><td>Clinical names (<code>/ux-audit</code>)</td><td><strong>Action-packed (<code>/vibe-check</code>)</strong></td></tr>
<tr><td>No sector style guidance</td><td><strong>20+ sectors with <code>/taste</code></strong></td></tr>
<tr><td>No screen builder</td><td><strong>27 screen types with <code>/screen</code></strong></td></tr>
<tr><td>No flow audit</td><td><strong>15 flow patterns with <code>/flow</code></strong></td></tr>
<tr><td>No inspiration system</td><td><strong>Mobbin-style taxonomy with <code>/inspo</code></strong></td></tr>
<tr><td>No competitive analysis</td><td><strong><code>/benchmark</code> vs best-in-class</strong></td></tr>
<tr><td>No dark pattern scanner</td><td><strong>22 categories with <code>/dark-scan</code></strong></td></tr>
<tr><td>No content audit</td><td><strong>Microcopy audit with <code>/copy-check</code></strong></td></tr>
<tr><td>No responsive audit</td><td><strong>7 breakpoint tiers with <code>/responsive</code></strong></td></tr>
<tr><td>No command workflow</td><td><strong>Decision tree + command chaining</strong></td></tr>
</table>

### Command name migration

If you're upgrading from v3.0, here's what changed:

| v3.0 | v4.0 | Why |
|------|------|-----|
| `/ux-audit` | `/vibe-check` | Everyone knows what a vibe check is |
| `/design-review` | `/judge` | Direct and authoritative |
| `/accessibility-check` | `/include` | Accessibility IS inclusion |
| `/generate-design-tokens` | `/drip` | Design tokens = your visual identity |
| `/ai-ux-audit` | `/trust-scan` | AI UX is about trust calibration |
| `/ux-metrics-plan` | `/pulse` | Metrics = the pulse of your product |
| `/component-build` | `/ship` | You ship components |
| `/design-critique` | `/roast` | A design roast — fun and direct |
| `/figma-to-code` | `/extract` | Pull design out of Figma into code |
| `/cognitive-check` | `/brain-scan` | Scanning UI against how the brain works |

<br />

## Architecture

```
taste-ux-ui/                                375K+ words · 107 markdown files
│
├── commands/                               20 slash commands
│   ├── Audit:    vibe-check, roast, brain-scan, include, trust-scan,
│   │             flow, dark-scan, copy-check, responsive
│   ├── Build:    ship, screen, drip, extract, onboard, remix
│   └── Strategy: taste, inspo, pulse, judge, benchmark
│
├── skills/                                 21 knowledge domains
│   ├── Foundations:  cognitive-psychology-ux, nng-ux-heuristics,
│   │                 ux-research-methods, ux-metrics-measurement
│   ├── Code:         component-patterns-code, design-systems-architecture,
│   │                 figma-design-tool-workflows, ui-visual-design-system
│   ├── Platforms:    mobile-ux-design, desktop-app-design,
│   │                 cross-cultural-i18n-ux, performance-states-patterns
│   ├── Experience:   interaction-motion-design, accessibility-inclusive-design,
│   │                 design-critique-case-studies, ux-ethics-content-strategy
│   ├── Emerging:     agentic-ai-generative-ux, ai-spatial-voice-ux,
│   │                 ambient-calm-zero-ui
│   └── NEW:          sector-style-intelligence, screen-flow-patterns
│
└── .claude-plugin/                         v4.0.0 manifests
    ├── plugin.json
    └── marketplace.json
```

<br />

## The knowledge inside

| What | Count |
|------|-------|
| Total words | **375,777** |
| Production code components (React, SwiftUI, CSS) | **40+** |
| Laws of UX (with mathematical formulas) | **25+** |
| Cognitive biases (with ethical flags) | **50+** |
| Screen type patterns | **27** |
| User flow patterns | **15** |
| UI element deep-dives | **26** |
| Sector style guides (with real app color palettes) | **6** covering **20+ sectors** |
| Product case studies (deep-dive analysis) | **10** |
| Redesign failure post-mortems | **10** |
| Dark pattern categories | **22** |
| Haptic feedback patterns | **30+** |
| Microcopy templates | **50+** |
| Cultural dimension mappings | **6** |
| Design system maturity levels | **5** |
| Platform cookbooks | **3** (React, SwiftUI, CSS) |

<br />

## Research foundations

Every claim traces back to authoritative research:

**Cognitive Science** — Kahneman (Peak-End Rule, System 1/2), Sweller (Cognitive Load Theory), Cowan (Working Memory), Iyengar & Lepper (Choice Overload), Fitts, Hick, Miller, Gestalt school, Simon (Satisficing), Csikszentmihalyi (Flow)

**Academic Research** — arXiv: UX 3.0 Paradigm, GenAI for UX Research, EvAlignUX, Emotion-Aware Interaction | ACM CHI 2025: Designing UIs with AI, Screen Reader + AI, Multi-Agent GenAI, AI Literacy

**Standards** — W3C: WCAG 3.0 April 2026 Draft, Design Tokens Oct 2025 Stable, WAI-ARIA | NNG Group 2025-2026: State of UX, AI Literacy, "AI Slop" Quality Gates

**Platforms** — Apple WWDC 2025 (iOS 26 Liquid Glass) | Google I/O 2025 (Material 3 Expressive) | Figma Config 2025 (MCP, Code Connect)

**Case Studies** — Stripe, Linear, Notion, Airbnb, Figma, Arc Browser, Duolingo, Vercel, Apple Health, Discord | Failures: Snapchat 2018, Windows 8, Digg v4, Sonos 2024, Healthcare.gov, Twitter/X, Google Plus, Reddit API, YouTube Dislikes, Skype

<br />

## Design philosophy

Built on the shoulders of giants:

| | |
|---|---|
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

> *"Every pixel on a screen is ultimately processed by a human brain. This plugin ensures Claude understands that brain."*

<br />

## Meet Sumi

<img src="assets/sumi.svg" alt="Sumi" width="80" align="left" style="margin-right: 16px;" />

**Sumi** (from *sumi-e*, Japanese ink painting) is your design companion. Part KAWS art toy, part Space Invader, part AI — Sumi has one eye for critique (the X) and one eye for precision (the crosshair).

Every command you run, Sumi draws from 375K+ words of design science — cognitive psychology, production code patterns, and real-world case studies — to make sure your pixels are right. No opinions. Only evidence.

<br clear="left" />

<br />

## Contributing

Found something to improve? We welcome contributions:

1. Fork the repo
2. Create a branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Submit a PR

**Content contributions are especially welcome**: new case studies, additional Laws of UX, updated platform patterns (WWDC/I/O releases), new sector style guides, and accessibility improvements.

<br />

## License

MIT

---

<p align="center">
  <strong>Built with obsessive attention to detail by <a href="https://github.com/phazurlabs">Design Tribe Republic</a>.</strong>
  <br />
  <sub>Powered by Claude Opus 4.6 · v4.0.0</sub>
</p>
