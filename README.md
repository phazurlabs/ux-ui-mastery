<p align="center">
  <img src="assets/sumi.svg" alt="Sumi" width="120" />
</p>
<h1 align="center">Sumi.</h1>
<p align="center">
  <strong>UX/UI intelligence for Claude Code.</strong><br />
  The design brain that turns vibe coders into product designers.
</p>
<p align="center">
  <a href="#install"><strong>Install</strong></a> ·
  <a href="#the-23-commands"><strong>Commands</strong></a> ·
  <a href="#which-command-do-i-use"><strong>Workflows</strong></a> ·
  <a href="#getting-best-results"><strong>Best Results</strong></a> ·
  <a href="#22-skills"><strong>Skills</strong></a> ·
  <a href="#whats-new-in-v43"><strong>What's New</strong></a>
</p>
<p align="center">
  <code>23 commands</code> · <code>22 skills</code> · <code>67 reference docs</code> · <code>480K+ words</code>
</p>

---

> **The problem:** You're shipping UI from AI prompts. It looks fine. But "fine" doesn't convert. "Fine" doesn't retain. "Fine" is what happens when you skip Empathize, Define, and Test — the phases that separate products people love from products people tolerate.
>
> **The fix:** Sumi embeds the entire UX design process — from NNG design thinking to cognitive psychology to production code — directly into your terminal. Every command traces to published research. Every output is copy-paste ready. Zero config. Just better products.

---

<br />

## Built on research

Every recommendation traces to published research.

**Cognitive Science** — Kahneman (Peak-End Rule, System 1/2), Sweller (Cognitive Load Theory), Cowan (Working Memory), Iyengar & Lepper (Choice Overload), Fitts, Hick, Miller, Gestalt school, Simon (Satisficing), Csikszentmihalyi (Flow)

**Academic Research** — arXiv: UX 3.0 Paradigm, GenAI for UX Research, EvAlignUX, Emotion-Aware Interaction | ACM CHI 2025: Designing UIs with AI, Screen Reader + AI, Multi-Agent GenAI, AI Literacy

**Standards** — W3C: WCAG 3.0 April 2026 Draft, Design Tokens Oct 2025 Stable, WAI-ARIA | NNG Group 2025-2026: State of UX, AI Literacy, "AI Slop" Quality Gates

**Platforms** — Apple WWDC 2025 (iOS 26 Liquid Glass) | Google I/O 2025 (Material 3 Expressive) | Figma Config 2025 (MCP, Code Connect)

**Case Studies** — Stripe, Linear, Notion, Airbnb, Figma, Arc Browser, Duolingo, Vercel, Apple Health, Discord | Failures: Snapchat 2018, Windows 8, Digg v4, Sonos 2024, Healthcare.gov, Twitter/X, Google Plus, Reddit API, YouTube Dislikes, Skype

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

> *"Every pixel on a screen is processed by a human brain. This plugin ensures Claude understands that brain."*

<br />

## See it in action

<table>
<tr>
<td width="50%">

**Ground yourself before you build**
```
/ground
```
6-phase NNG process map, methodology selection (IDEO, Sprint, Lean UX...), personalized Sumi command roadmap, and terminal exercises. The 60-second version for when you're moving fast.

</td>
<td width="50%">

**Define your problem, not just your pixels**
```
/intent fitness app for busy parents
```
Problem statement, lightweight persona, 5 "How Might We" questions, success criteria, and a **Constraint Stack** you paste into every BUILD command to carry intent forward.

</td>
</tr>
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

## Install

### Recommended: Claude Code marketplace

```
/plugin marketplace add phazurlabs/sumi
/plugin install sumi@sumi-marketplace
```

That's it. Works in every session.

### Alternative: Clone manually

```bash
mkdir -p ~/.claude/plugins && cd ~/.claude/plugins
git clone https://github.com/phazurlabs/sumi.git
```

Then add to `~/.claude/settings.json`:
```json
{
  "enabledPlugins": {
    "sumi": true
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

Commands appear as `/sumi:command-name` (e.g., `/sumi:taste`).

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
| Want to uninstall | `/plugin uninstall sumi` or remove from `settings.json` |

**Requirements:** Claude Code CLI (latest). No external dependencies — pure markdown, zero config, works offline.

</details>

<br />

## The 23 Commands

### Guide — know where you are

| Command | One-liner | What you get |
|---------|-----------|-------------|
| `/guide` | Phase-based companion | 6-phase design process (Ground → Discover → Diagnose → Fortify → Build → Launch), phase checklist, next command recommendation |

Start here if you're new. `/guide` maps all 22 other commands into six phases so you always know what to do next.

### Ground — know your process

| Command | One-liner | What you get |
|---------|-----------|-------------|
| `/ground` | Process orientation | 6-phase NNG process map, methodology selection, personalized Sumi command roadmap |
| `/intent` | Design intent definition | Problem statement, persona, HMW questions, success criteria, constraint stack |

New to UX or vibe coding? Start here. `/ground` maps the design thinking process to terminal workflows. `/intent` defines your problem before you build.

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
| `/judge` | Full review | All 22 skill domains scored, priority roadmap (quick wins → medium → strategic) |
| `/benchmark` | Competitive analysis | 10-dimension scorecard vs. top 5 apps, gap analysis, improvement tiers |

<br />

## Which command do I use?

**New here? Start with `/guide`** — it walks you through the six design phases and recommends commands in order.

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  "I don't know where to start"                                      │
│   /guide                                                            │
│                                                                     │
│  Phase 0 GROUND — know your process                                 │
│   /ground  →  /intent                                               │
│                                                                     │
│  Phase 1 DISCOVER — understand the space                            │
│   /taste  →  /inspo  →  /benchmark  →  /pulse                      │
│                                                                     │
│  Phase 2 DIAGNOSE — find what's broken                              │
│   /vibe-check  →  /brain-scan  →  /include  →  /flow               │
│                                                                     │
│  Phase 3 FORTIFY — secure your standards                            │
│   /dark-scan  →  /trust-scan  →  /copy-check  →  /responsive       │
│                                                                     │
│  Phase 4 BUILD — make the thing                                     │
│   /drip  →  /screen  →  /ship  →  /onboard  →  /extract            │
│                                                                     │
│  Phase 5 LAUNCH — make it better                                    │
│   /roast  →  /remix  →  /judge  →  loop back to BUILD              │
│                                                                     │
│  Every command suggests the logical next command in its output.     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

<br />

## How it works

You type a command. Claude loads the matching skill files — each one 10,000 to 30,000 words of research, patterns, and case studies.

Skills cross-reference each other. A component audit pulls from accessibility, cognitive psychology, and visual design at the same time.

Commands chain. `/roast` points to `/remix`. `/taste` leads to `/inspo`. No dead ends.

Claude uses progressive disclosure: it loads only the skill files each query needs. The full 480K+ words sit ready. Only the relevant slice activates.

<br />

## Getting best results

The difference between a generic output and a precise, production-ready one comes down to what you give Sumi to work with. More context = sharper results. Here's exactly how to get the most out of every command.

### The golden rule: give context, get precision

Every Sumi command works better when it knows **what** you're building, **who** it's for, and **what platform** it targets. Compare:

```
# Vague — Sumi has to guess everything
/ship button

# Specific — Sumi tailors every decision
/ship button for a fintech iOS app, primary CTA for confirming
wire transfers, must support Face ID confirmation state,
target audience is 35-55 year old professionals
```

The second prompt gives Sumi enough to select the right color psychology (trust-first for fintech), motion language (clinical, not bouncy), copy tone (formal-professional), touch targets (generous for older users), and platform conventions (iOS HIG, SF Symbols).

### What input format to use

Each command type accepts different inputs. Using the right format unlocks the full audit or build depth.

#### For Audit commands (`/vibe-check`, `/roast`, `/brain-scan`, `/include`, `/flow`, `/dark-scan`, `/trust-scan`, `/copy-check`, `/responsive`)

| Input type | How to provide it | Quality level |
|------------|-------------------|---------------|
| **Code** (best) | Paste the component/screen code directly into the chat, or tell Sumi to read a file path | Highest — Sumi can inspect every element, ARIA attribute, state, and token |
| **File path** | "Run /vibe-check on `src/components/Checkout.tsx`" | Highest — Sumi reads the actual implementation |
| **Screenshot** | Paste or attach a screenshot image | High — Claude's vision analyzes layout, hierarchy, color, spacing |
| **URL description** | "Audit the Stripe checkout flow — the 3-step payment form with card input, address, and confirmation" | Medium — Sumi uses its case study knowledge to infer patterns |
| **Verbal description** | "I have a dashboard with a sidebar nav, 4 metric cards, and a data table" | Baseline — useful for early-stage concepts, but findings will be general |

**Best practice for audits:**
```
# Provide the actual code + context in one message
Here's my checkout form component. It's a React/TypeScript app
targeting mobile web for a food delivery startup. Users are
18-35, often ordering while commuting.

[paste code here]

/vibe-check
```

#### For Build commands (`/ship`, `/screen`, `/drip`, `/onboard`, `/extract`, `/remix`)

| Input type | How to provide it | What you get |
|------------|-------------------|--------------|
| **Component name + context** | `/ship modal` or `/ship date-picker for a travel booking app` | Full component with states, a11y, tokens, code |
| **Screen type + sector** | `/screen dashboard for a SaaS analytics product` | Complete screen with layout, component hierarchy, all states |
| **Existing code to improve** | Paste code + `/remix` | Before/after redesign with UX reasoning for every change |
| **Figma specs** | Paste Figma Dev Mode output or token values + `/extract` | Platform-ready code matching the design spec |

**Best practice for builds:**
```
# Stack all the constraints upfront
/screen settings for an iOS health app targeting elderly users (65+).
Must support Dynamic Type up to AX5.
Platform: SwiftUI.
Design system: uses 8px grid, SF Pro, blue-500 as primary.
Must include: profile editing, notification preferences,
data export, account deletion (GDPR), and accessibility toggles.
```

#### For Strategy commands (`/taste`, `/inspo`, `/benchmark`, `/pulse`, `/judge`)

| Input type | How to provide it | What you get |
|------------|-------------------|--------------|
| **Sector name** | `/taste fintech` or `/taste wellness premium` | Full style direction calibrated to sector conventions |
| **Sector + sub-niche + modifiers** | `/taste fintech neobank, premium, Gen Z, mobile-first` | Highly targeted direction with specific font/color/motion choices |
| **Screen/element/flow type** | `/inspo screen onboarding` or `/inspo element data-table` or `/inspo flow checkout` | Pattern references with best-in-class examples |
| **Product + category** | `/benchmark [your app] vs neobanks` | 10-dimension competitive scorecard |

**Best practice for strategy:**
```
# Layer the modifiers for a precise direction
/taste healthcare, telemedicine sub-niche, clinical mood,
desktop-first, audience is doctors aged 30-50,
must feel trustworthy but not cold
```

### Prompting patterns that maximize accuracy

These patterns work across all commands.

#### 1. State your platform and framework

Sumi generates code in React/TypeScript, SwiftUI, and CSS. Tell it which one:

```
/ship toggle — React with TypeScript, using Radix primitives
/ship toggle — SwiftUI with ViewModifiers
/ship toggle — vanilla CSS with custom properties, no framework
```

Without a platform specified, Sumi defaults to React/TypeScript. Be explicit if you want SwiftUI or CSS.

#### 2. Name your design system constraints

If you have existing tokens, tell Sumi so the output integrates with your system:

```
/ship card — our tokens use --color-surface-primary, --space-md (16px),
--radius-lg (12px), --shadow-elevation-1. Font is Inter.
Border radius is 12px across all cards. 4px base grid.
```

#### 3. Specify your target audience

Audience changes everything — touch targets, font sizes, color contrast requirements, copy reading level, and density:

```
# For elderly users: larger targets, higher contrast, simpler language
/screen settings for users aged 65+

# For power users: denser UI, keyboard shortcuts, advanced features visible
/screen dashboard for developer-audience, keyboard-first

# For children: playful motion, large targets, limited choices
/ship navigation for an education app targeting ages 6-10
```

#### 4. Declare your accessibility level

Sumi defaults to WCAG 2.2 AA. If you need more:

```
# AAA compliance (highest standard)
/include — evaluate against WCAG 2.2 AAA, not just AA

# Cognitive accessibility focus
/brain-scan — prioritize cognitive load for users with ADHD

# Full inclusive audit
/include — evaluate for screen readers, keyboard-only, motor impairment,
cognitive accessibility, and color blindness (all types)
```

#### 5. Tell Sumi what you've already decided

If you've already run `/taste` and have a style direction, reference it:

```
# Chain context from a previous command
I ran /taste fintech earlier and got Inter + DM Sans,
blue-600 primary (#2563EB), 8px grid, medium border radius (8px).
Now /ship button using that direction.
```

#### 6. Ask for specific output depth

If a default output is too broad or too narrow:

```
# Narrow: just the critical issues
/vibe-check — only report severity 3 and 4 findings

# Wide: maximum depth
/roast — evaluate every dimension, don't skip any, include
code fixes for every finding

# Focused: one specific area
/brain-scan — focus on cognitive load in the form section only
```

### Chaining commands for complete coverage

Commands are designed to feed into each other. Here are the chains that produce the best results:

#### Full product design (new project)
```
/ground                   → orient yourself in the UX process
/intent                   → define your problem + generate a constraint stack
/taste [sector]           → establishes visual direction + tokens
/inspo screen [type]      → finds patterns for your key screens
/drip                     → expands tokens into a full system
/screen [type]            → builds screens consuming those tokens
/ship [component]         → builds components within those screens
/vibe-check               → audits the result against heuristics
/include                  → audits accessibility specifically
/roast                    → critiques the overall design quality
/remix                    → applies critique findings as a redesign
```

#### Design review (existing product)
```
/vibe-check               → broad heuristic sweep (start here)
/brain-scan               → cognitive load + Laws of UX
/include                  → accessibility compliance
/responsive               → cross-device breakpoint audit
/copy-check               → microcopy and content quality
/dark-scan                → ethical pattern check
/judge                    → comprehensive score across all 22 domains
```

#### Component quality gate (before shipping)
```
/ship [component]         → generate the component
/include                  → audit accessibility
/roast                    → design critique
/remix                    → apply fixes
/responsive               → verify cross-device behavior
```

#### Competitive positioning
```
/benchmark [category]     → score vs. top 5 competitors
/taste [sector]           → get the style direction leaders use
/inspo screen [type]      → see what best-in-class does differently
/pulse                    → set up metrics to track improvement
```

### Common mistakes to avoid

| Mistake | Why it hurts | Do this instead |
|---------|-------------|-----------------|
| Running `/ship button` with no context | Sumi builds a generic button with no sector personality, audience calibration, or design system alignment | Add sector, audience, platform, and any token constraints |
| Auditing a description instead of code | Findings stay high-level and can't point to specific lines or ARIA issues | Paste real code or point to a file path |
| Skipping `/taste` before `/ship` or `/screen` | Components won't have a coherent style direction — colors, type, and spacing will be generic defaults | Run `/taste` first, then reference its output in build commands |
| Running one audit and stopping | Each audit command checks different dimensions — `/vibe-check` misses what `/brain-scan` catches, `/include` misses what `/dark-scan` catches | Run at least `/vibe-check` + `/include` + `/brain-scan` for minimum coverage |
| Not specifying the platform | Defaults to React — if you need SwiftUI or CSS you'll get the wrong output | Always state: React, SwiftUI, or CSS |
| Ignoring "Next Steps" in command output | Every command suggests the logical next command — ignoring it breaks the workflow chain | Follow the suggested next command or use `/guide` to see the full phase map |

### Skill activation — how to trigger the right knowledge

Skills (the 22 knowledge domains) activate automatically when you ask about relevant topics. You don't invoke them directly. But you can steer which skills activate by how you phrase your question:

```
# Activates: cognitive-psychology-ux
"What does Fitts's Law say about the size of this CTA?"

# Activates: cognitive-psychology-ux + accessibility-inclusive-design
"Is this button big enough for users with motor impairments,
and does it follow Fitts's Law?"

# Activates: mobile-ux-design + interaction-motion-design
"How should this bottom sheet animate on iOS 26 with Liquid Glass?"

# Activates: agentic-ai-generative-ux + ux-ethics-content-strategy
"How do I design a trust-calibrated UI for an AI agent
that makes purchases on behalf of the user?"

# Activates: sector-style-intelligence + ui-visual-design-system
"What color palette do leading neobanks use and why?"

# Activates: design-critique-case-studies
"What went wrong with the Sonos 2024 app redesign?"
```

The more specific your question, the more precisely Sumi selects which of its 480K+ words to draw from.

<br />

## Real-world workflows

End-to-end scenarios showing exactly what to type for common projects.

<details>
<summary><strong>Workflow 1: "I'm building a fintech app from scratch"</strong></summary>

```
# Step 0 — Ground yourself (60 seconds)
/ground
/intent neobank for Gen Z, mobile-first

# Step 1 — Get your visual direction
/taste fintech, neobank, premium, mobile-first, Gen Z audience

# Step 2 — Find patterns for your key screens
/inspo screen dashboard
/inspo screen transaction-history
/inspo flow onboarding

# Step 3 — See how you compare before you build
/benchmark [your app name] vs neobanks

# Step 4 — Generate your design token system
/drip — use the /taste direction above, W3C format, include dark mode

# Step 5 — Build your screens
/screen dashboard for a neobank, consuming the tokens from /drip above
/screen settings for a neobank, include account, security, notifications

# Step 6 — Build key components
/ship transaction-card — React, shows amount, merchant, category, timestamp
/ship balance-widget — shows total, trend graph, and quick-send CTA

# Step 7 — Build onboarding
/onboard — neobank, 4-step flow: welcome → KYC → fund account → first transaction

# Step 8 — Audit everything
/vibe-check — audit the dashboard screen
/include — WCAG 2.2 AA audit on all components
/brain-scan — check cognitive load on the onboarding flow
/dark-scan — verify no deceptive patterns in the sign-up flow

# Step 9 — Critique and refine
/roast — full critique of the dashboard
/remix — apply the must-fix findings

# Step 10 — Final score
/judge — score the complete design across all 22 domains
```

</details>

<details>
<summary><strong>Workflow 2: "I need to audit an existing React codebase"</strong></summary>

```
# Point Sumi at your actual code files
Run /vibe-check on src/pages/Dashboard.tsx

# Then layer additional audits on the same file
Run /include on src/pages/Dashboard.tsx
Run /brain-scan on src/pages/Dashboard.tsx
Run /responsive on src/pages/Dashboard.tsx

# Audit the user flow across multiple screens
/flow — evaluate the checkout flow across
  src/pages/Cart.tsx → src/pages/Shipping.tsx →
  src/pages/Payment.tsx → src/pages/Confirmation.tsx

# Check content and ethics
/copy-check on all user-facing strings in the checkout flow
/dark-scan on the pricing page and checkout flow

# Get the full picture
/judge — score the complete application
```

</details>

<details>
<summary><strong>Workflow 3: "I'm redesigning a settings screen"</strong></summary>

```
# Start by auditing what exists
Paste the current settings screen code here.
/roast

# Get inspiration for what great settings screens look like
/inspo screen settings

# Redesign based on the roast findings
/remix — the current settings screen, applying the must-fix items

# Verify the redesign
/include — audit the new version
/responsive — check all breakpoints
/copy-check — verify label clarity and tone
```

</details>

<details>
<summary><strong>Workflow 4: "I need to generate a design system from scratch"</strong></summary>

```
# Step 1 — Establish style direction
/taste saas, project-management, balanced mood, responsive

# Step 2 — Generate the full token system
/drip — W3C format, include: color (primitive + semantic + component layers),
typography (scale + weights + line-heights), spacing (4px base),
border-radius, elevation, motion/duration, breakpoints.
Include light + dark themes.

# Step 3 — Build the core component library
/ship button — all variants (primary, secondary, ghost, destructive, icon-only)
/ship input — text, email, password, search, textarea, with validation states
/ship card — content card, stat card, action card variants
/ship modal — dialog, confirmation, form modal variants
/ship navigation — sidebar + top nav + mobile bottom nav
/ship toast — success, error, warning, info with auto-dismiss

# Step 4 — Build screens using those components
/screen dashboard — consuming the token system and components above
/screen settings — account, preferences, integrations
/screen empty-state — first-use, no-results, error variations

# Step 5 — Validate the system
/judge — score the complete design system
/include — verify WCAG 2.2 AA across all components
```

</details>

<details>
<summary><strong>Workflow 5: "I need to prepare for a design review meeting"</strong></summary>

```
# Run the full audit battery — paste your screen code first
/vibe-check — Nielsen's 10 heuristics, get severity ratings
/brain-scan — cognitive load and Laws of UX violations
/include — accessibility compliance report
/flow — user journey efficiency and drop-off risks

# Get a comprehensive score
/judge — all 22 domains scored, creates a priority roadmap

# Get competitive context
/benchmark [your app] vs [category] — see where you stand vs. the best

# The /judge output gives you:
# - Scores across every dimension
# - A prioritized improvement roadmap (quick wins → medium → strategic)
# - Evidence-backed reasoning you can present to stakeholders
```

</details>

<br />

## Pro tips

<details>
<summary><strong>Stack multiple audits in one session</strong></summary>

Run audit commands back-to-back in the same conversation. Sumi retains context from earlier commands, so `/brain-scan` after `/vibe-check` builds on findings rather than repeating them.

```
/vibe-check      → finds heuristic violations
/brain-scan      → adds cognitive load analysis on top
/include         → adds accessibility on top of both
```

Each subsequent audit goes deeper because it already knows what the previous one found.

</details>

<details>
<summary><strong>Use /remix to apply audit findings automatically</strong></summary>

After any audit command, run `/remix` immediately. It reads the findings from the audit and generates a redesigned version with before/after reasoning for every change.

```
/roast           → identifies 8 findings across 10 dimensions
/remix           → takes those 8 findings and outputs fixed code
```

No need to manually translate findings into fixes.

</details>

<details>
<summary><strong>Target specific platforms precisely</strong></summary>

Sumi knows the latest platform conventions (iOS 26 Liquid Glass, Material 3 Expressive). Be explicit:

```
# iOS-native
/ship tab-bar — SwiftUI, iOS 26 Liquid Glass style, SF Symbols

# Android-native
/ship bottom-sheet — Jetpack Compose, Material 3 Expressive, spring motion

# Web with modern CSS
/ship dialog — vanilla HTML/CSS, uses popover API, anchor positioning,
   container queries, no JavaScript framework
```

</details>

<details>
<summary><strong>Audit screenshots when you don't have code</strong></summary>

Paste a screenshot directly into the chat. Claude's vision capabilities let Sumi analyze the actual rendered UI:

```
[paste screenshot]
/roast this screen — it's a mobile banking app dashboard,
target audience is 25-40 professionals
```

Screenshot audits catch visual hierarchy issues, spacing inconsistencies, color contrast problems, and layout issues that code-only audits can miss.

</details>

<details>
<summary><strong>Ask follow-up questions after any command</strong></summary>

Every Sumi command output is a starting point, not an endpoint. Ask follow-ups:

```
/taste fintech

→ "Why did you choose Inter over SF Pro for this?"
→ "Show me the dark mode token mapping in full"
→ "What would change if the audience were Gen Z instead?"
→ "Generate just the motion tokens as a separate file"
```

Sumi's skill knowledge stays active in the conversation, so follow-ups get the same research depth as the initial command.

</details>

<details>
<summary><strong>Ground yourself before building</strong></summary>

New to UX or building with AI? Start with Phase 0:

```
/ground              → understand the 6-phase UX process, pick your methodology
/intent              → define your problem, persona, and success criteria
```

`/intent` generates a **Constraint Stack** — a structured block you paste into any BUILD command to carry your design intent forward. This single habit prevents the three risks of vibe coding: pseudo-productivity, homogenization, and skill erosion.

</details>

<details>
<summary><strong>Use /guide to reset when you're lost</strong></summary>

At any point in a session, run `/guide` to see which phase you're in, what you've done, and what comes next. It maps all 22 other commands into six phases so you never lose your place.

```
/guide           → "You're in Phase 3: BUILD. You've run /drip and /screen.
                    Next recommended: /ship to build your core components."
```

</details>

<br />

## 22 Skills

Skills activate on topic. No manual invocation.

<details>
<summary><strong>Process</strong> — Know your methodology before you build</summary>

| Skill | Depth |
|-------|-------|
| **UX Process Workflow** | NNG 6-phase design thinking (Empathize → Define → Ideate → Prototype → Test → Implement). 8 company methodology deep-dives (IDEO, Double Diamond, Google Sprint, IBM EDT, Lean UX, Spotify, Microsoft Inclusive Design, Vercel/Figma). The vibe coder's bridge: Before/While/After prompting framework, arXiv:2509.10652 findings, anti-patterns, checklists. Academic foundations (ISO 9241-210, Norman's 7 principles, cognitive laws). Powers `/ground` and `/intent`. |

</details>

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

## What's new in v4.3

**The vibe coding fix.** Phase 0 is the answer to the biggest gap in AI-assisted development: skipping the thinking that makes products actually work.

| What | Details |
|------|---------|
| **Phase 0: GROUND** | New pre-phase with 2 commands (`/ground`, `/intent`) — forces UX process grounding before building. 60-second speed mode for when you're moving fast. |
| **`/ground` (0.1)** | Process orientation — NNG 6-phase design thinking mapped to terminal workflow. Choose from 8 company methodologies (IDEO, Sprint, Lean UX...). Get a personalized Sumi command roadmap in 60 seconds. |
| **`/intent` (0.2)** | Problem definition — generates a problem statement, persona, HMW questions, success criteria, and a **Constraint Stack** you paste into every BUILD command. This single habit prevents homogenized AI output. |
| **`ux-process-workflow` skill** | 109K+ words of new knowledge: NNG design thinking, 8 company methodology deep-dives with real outcomes (Airbnb $100B, IBM 75% time-to-market reduction), the vibe coder's bridge (arXiv:2509.10652), Hall of Real Consequences (Healthcare.gov $1.7B, Snapchat $1.3B loss). |
| **6 phases, 22 steps** | Journey expanded from 5 phases to 6 phases, 20 steps to 22 steps. Ground → Discover → Diagnose → Fortify → Build → Launch. |
| **Speed runs everywhere** | Every new command includes 60-second, 2-minute, and 5-minute paths. No excuses — even under deadline pressure, you can ground your work. |

<br />

## What's new in v4.0

<table>
<tr>
<th>v3.0</th>
<th>v4.0</th>
</tr>
<tr><td>10 commands</td><td><strong>21 commands</strong></td></tr>
<tr><td>19 skills</td><td><strong>21 skills</strong></td></tr>
<tr><td>55 references</td><td><strong>65 reference docs</strong></td></tr>
<tr><td>310K words</td><td><strong>370K+ words</strong></td></tr>
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
sumi/                                       480K+ words · 112 markdown files
│
├── commands/                               23 slash commands
│   ├── Guide:    guide
│   ├── Ground:   ground, intent
│   ├── Audit:    vibe-check, roast, brain-scan, include, trust-scan,
│   │             flow, dark-scan, copy-check, responsive
│   ├── Build:    ship, screen, drip, extract, onboard, remix
│   └── Strategy: taste, inspo, pulse, judge, benchmark
│
├── skills/                                 22 knowledge domains
│   ├── Process:      ux-process-workflow
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
│   └── Intelligence: sector-style-intelligence, screen-flow-patterns
│
└── .claude-plugin/                         v4.3.0 manifests
    ├── plugin.json
    └── marketplace.json
```

<br />

## The knowledge inside

| What | Count |
|------|-------|
| Total words | **483,000+** |
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

## Meet Sumi

<img src="assets/sumi.svg" alt="Sumi" width="80" align="left" style="margin-right: 16px;" />

**Sumi** (from *sumi-e*, Japanese ink painting) is your design companion. Part KAWS art toy, part Space Invader, part AI — Sumi has one eye for critique (the X) and one eye for precision (the crosshair).

Every command you run, Sumi draws from 480K+ words of design science — cognitive psychology, production code patterns, and real-world case studies — to make sure your pixels are right. No opinions. Only evidence.

Whether you're a solo builder shipping from your terminal, a design engineer bridging Figma and code, or a team that wants UX rigor without the agency retainer — Sumi has you covered. From the 60-second process ground to the 22-domain full review, every level of investment pays off.

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
  <sub>Powered by Claude Opus 4.6 · v4.3.0</sub>
</p>
