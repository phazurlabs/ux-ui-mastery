---
description: Phase-based design guide — know where you are in the design process, what to do next, and which commands to run in what order.
---

# Guide — Phase-Based Design Companion

Navigate the design process with confidence. Instead of choosing from 20+ commands, tell Sumi where you are and get a guided path forward.

## Design Phases

The design process moves through four phases. Each phase has a clear goal, a set of commands, and natural exit criteria that signal readiness for the next phase.

```
  DISCOVER          AUDIT            BUILD            REFINE
  ─────────→       ─────────→       ─────────→       ─────────→
  "What space       "What's wrong    "Make the        "Make it
   am I in?"         with what        thing."          better."
                     exists?"
```

### Phase 1: DISCOVER — Understand the space

**Goal**: Establish visual direction, find patterns, understand the competition, and define what success looks like before touching a single pixel.

**When to use**: Starting a new product, entering a new sector, redesigning from scratch, or onboarding onto an unfamiliar project.

| Order | Command | What it gives you | Output feeds into |
|-------|---------|-------------------|-------------------|
| 1 | `/taste` | Complete style direction — color, type, spacing, motion, tokens, tone, reference apps | `/drip`, `/ship`, `/screen` |
| 2 | `/inspo` | Best-practice patterns, 5 reference implementations, curated inspiration sources | `/screen`, `/ship` |
| 3 | `/benchmark` | Competitive scoring across 10 dimensions with gap analysis | `/roast`, `/remix` |
| 4 | `/pulse` | HEART metrics framework, measurement plan, experimentation strategy | All audit commands |

**Exit criteria — move to Phase 2 when you have**:
- A style direction (from `/taste`)
- Pattern references for your key screens (from `/inspo`)
- A clear picture of where competitors are stronger (from `/benchmark`)

**Shortcut**: If you're adding to an existing product (not starting fresh), skip to Phase 2.

---

### Phase 2: AUDIT — Find what's broken

**Goal**: Systematically evaluate what exists — whether it's a live product, a Figma prototype, code, or a competitor's app. Find every issue before building.

**When to use**: Reviewing an existing design, evaluating a prototype, preparing for a redesign, running a design QA pass, or onboarding onto a codebase with UI.

| Order | Command | What it checks | Severity system |
|-------|---------|---------------|-----------------|
| 1 | `/vibe-check` | Nielsen's 10 heuristics — the broadest UX sweep | Severity 0-4 |
| 2 | `/brain-scan` | Cognitive load, Laws of UX, Gestalt, bias ethics | 12-dimension score |
| 3 | `/include` | WCAG 2.2 AA accessibility — semantic HTML, ARIA, keyboard, contrast | Pass/Fail per criterion |
| 4 | `/flow` | Multi-step journey analysis — drop-off risk, emotional arc | Per-step scoring |
| 5 | `/dark-scan` | 22 deceptive pattern categories, regulatory compliance | FTC/GDPR/DSA flags |
| 6 | `/trust-scan` | AI feature trust, safety, usability, accessibility | 4-dimension 0-100 |
| 7 | `/copy-check` | Microcopy clarity, tone, inclusive language, i18n readiness | Per-string audit |
| 8 | `/responsive` | 7 breakpoint tiers, touch targets, reflow, fluid type | Per-breakpoint report |

**Exit criteria — move to Phase 3 when you have**:
- A prioritized list of must-fix issues (from `/vibe-check` + `/brain-scan`)
- Accessibility violations cataloged with fixes (from `/include`)
- Flow bottlenecks identified (from `/flow`)

**Shortcut**: For a quick health check, run just `/vibe-check` + `/include`. For a full audit, run all eight in order.

---

### Phase 3: BUILD — Make the thing

**Goal**: Generate production-ready screens, components, design tokens, and flows. Every output is copy-paste ready with states, accessibility, and responsive behavior built in.

**When to use**: You know what to build. Style direction exists. Issues are cataloged. Time to ship.

| Order | Command | What it produces | Output format |
|-------|---------|-----------------|---------------|
| 1 | `/drip` | Full W3C design token system — color, type, spacing, elevation, themes | JSON (W3C Design Tokens) |
| 2 | `/screen` | Complete screen with all states, ARIA, responsive breakpoints | React/SwiftUI/CSS |
| 3 | `/ship` | Production component with 10 states, keyboard handling, test skeleton | React/SwiftUI/CSS |
| 4 | `/onboard` | Onboarding flow with progressive disclosure, activation metrics | React/TypeScript |
| 5 | `/extract` | Figma design → production code pipeline | React/SwiftUI/CSS |

**Exit criteria — move to Phase 4 when you have**:
- A token system consumed by your components (from `/drip`)
- Key screens built with all states handled (from `/screen`)
- Core components shipping (from `/ship`)

**Shortcut**: If tokens already exist in your codebase, skip `/drip` and start with `/screen` or `/ship`.

---

### Phase 4: REFINE — Make it better

**Goal**: Critique what you've built, score it against professional standards, and iterate. This phase loops — refine until the scores are where you want them.

**When to use**: After building. Before launch. During design review. When something feels off but you can't articulate why.

| Order | Command | What it does | Loops back to |
|-------|---------|-------------|---------------|
| 1 | `/roast` | Liz Lerman critique, 10 dimensions scored, must-fix/should-fix/could-improve | Phase 3 (`/ship`, `/screen`) |
| 2 | `/remix` | Takes findings and generates a redesigned version with before/after reasoning | Phase 3 (`/ship`, `/screen`) |
| 3 | `/judge` | Full scoring across all 21 skill domains — the final exam | Phase 2 (if major issues) |

**Exit criteria — ready to ship when**:
- `/roast` returns no must-fix findings
- `/judge` scores 7+ across all dimensions
- `/include` passes WCAG 2.2 AA

**Loop**: Phase 4 feeds back into Phase 3. `/roast` identifies problems → `/remix` generates fixes → `/ship` rebuilds → `/roast` again. Repeat until quality bar is met.

---

## Guide Protocol

1. **Determine where the user is**: Ask or infer which phase they're in.
   - **New project, no direction yet** → Phase 1: DISCOVER
   - **Have a design or product to evaluate** → Phase 2: AUDIT
   - **Know what to build, ready to code** → Phase 3: BUILD
   - **Built something, need to improve it** → Phase 4: REFINE
   - **Not sure** → Start with Phase 1

   If the user provides context (e.g., "I'm building a fintech app" or "review this component"), infer the phase from context rather than asking.

2. **Show the phase map**: Display all four phases with the user's current position highlighted.

3. **Recommend the first command**: Based on the phase, suggest the specific command to run next with a one-line explanation of why.

4. **Show the phase checklist**: List all commands in the current phase as a checklist so the user can track progress.

5. **Suggest phase transitions**: When the user has completed enough of the current phase, proactively suggest moving to the next phase.

## Output Format

```
## Sumi Design Guide

### Where You Are
> **Phase [N]: [PHASE NAME]** — [one-line description of goal]

### The Full Journey
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1 DISCOVER  │───▶│   2 AUDIT    │───▶│   3 BUILD    │───▶│  4 REFINE   │
│             │    │             │    │             │    │             │
│ /taste      │    │ /vibe-check │    │ /drip       │    │ /roast      │
│ /inspo      │    │ /brain-scan │    │ /screen     │    │ /remix      │
│ /benchmark  │    │ /include    │    │ /ship       │    │ /judge      │
│ /pulse      │    │ /flow       │    │ /onboard    │    │             │
│             │    │ /dark-scan  │    │ /extract    │    │     ▲       │
│             │    │ /trust-scan │    │             │    │     │       │
│             │    │ /copy-check │    │             │    │  loop until │
│             │    │ /responsive │    │             │    │  quality ✓  │
└─────────────┘    └─────────────┘    └─────────────┘    └──────┼──────┘
                                           ▲                    │
                                           └────────────────────┘
[Current phase highlighted with ★]

### Your Phase: [PHASE NAME]

**Goal**: [What this phase achieves]

**Start here** → `[first command]` — [why this command first]

#### Phase Checklist
- [ ] `[command 1]` — [what it gives you]
- [ ] `[command 2]` — [what it gives you]
- [ ] `[command 3]` — [what it gives you]
[...]

#### When to move on
[Exit criteria for this phase]

### Quick Reference
| Phase | Commands | Time |
|-------|----------|------|
| 1 DISCOVER | /taste → /inspo → /benchmark → /pulse | ~30 min |
| 2 AUDIT | /vibe-check → /brain-scan → /include → +5 more | ~45 min |
| 3 BUILD | /drip → /screen → /ship → /onboard → /extract | ~60 min |
| 4 REFINE | /roast → /remix → /judge → loop | ~20 min/cycle |
```

## Cross-References
The guide draws on the full Sumi skill and command system:
- All 20 commands are organized into the four phases above
- `cognitive-psychology-ux` skill informs the progressive disclosure rationale (Iyengar & Lepper choice overload, Miller's chunking)
- `ux-research-methods` skill grounds the phase structure in established design process methodology (Double Diamond, Design Thinking)
- `nng-ux-heuristics` skill provides the evaluation framework used in Phase 2
- `design-systems-architecture` skill informs the build order in Phase 3 (tokens before components)

## Next Steps
After running `/guide`, the user should:
- Run the first recommended command for their current phase
- Return to `/guide` at any time to reorient and check progress
- Use `/guide [phase]` to jump directly to a specific phase (e.g., `/guide build`)
