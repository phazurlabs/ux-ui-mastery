---
name: sumi-orchestrator
description: "Routes any UX/UI request to the right Sumi skills in the right order, with stage gates and handoffs. Use when the user asks where to start, what comes next, what the process is, or wants a full design engagement run end to end — and whenever a request is broad enough to need more than one skill (redesign, launch, audit, new product, design system)."
---

# Sumi Orchestrator

Sumi holds 19 skill domains. Most real requests need three to six of them in a
particular order, and running them in the wrong order wastes work — you cannot
critique a flow before you know who it is for, and you cannot set metrics before
you know what good looks like.

This skill is the router. Identify the pipeline, run its stages in order, honour
the gates, hand off the named artifact.

## Routing

Match the user's request to a pipeline. If the request is vague ("help me with my
app"), ask the three qualifying questions below before routing.

| The user wants to… | Pipeline |
|---|---|
| Find what's wrong with something that exists | **Evaluate** |
| Design something that doesn't exist yet | **Create** |
| Build or ship an actual component | **Implement** |
| Start or scale a design system | **Systematize** |
| Move a design into code | **Handoff** |
| Ship to new countries or languages | **Localize** |
| Design an AI or agent feature | **AI Surface** |
| Know whether any of it worked | **Measure** |

### Qualifying questions

Ask at most three, and only what the request hasn't already answered:

1. **Does it exist yet?** Nothing built → Create. Something built → Evaluate.
2. **What platform?** Web/desktop, mobile, or ambient/voice/spatial. This selects
   the platform skill layered into every pipeline.
3. **What decision hangs on this?** Ship/no-ship, roadmap priority, or a specific
   fix. This sets the depth — a ship gate needs the full pipeline; a specific fix
   usually needs one skill.

## Pipelines

Each stage names the skill to invoke. **Gate** is the condition to satisfy before
moving on — if it fails, stay in the stage or step back, don't push forward.

### Evaluate — something exists and may be broken

1. `nng-ux-heuristics` — heuristic pass, severity 0–4 on every finding
2. `cognitive-psychology-ux` — cognitive load, decision architecture, attention
3. `accessibility-inclusive-design` — WCAG 2.2, ARIA, keyboard, contrast
4. `ux-ethics-content-strategy` — dark patterns, manipulation, interface copy
5. `design-critique-case-studies` — structure the findings into a critique

**Gate:** every finding carries a severity rating and a location. Unrated
findings are opinions, and opinions don't survive a prioritization meeting.
**Artifact:** severity-ranked defect list.

### Create — designing something new

1. `ux-research-methods` — what do we actually know about these users
2. `cognitive-psychology-ux` — the constraints the design must respect
3. `ui-visual-design-system` — type, color, hierarchy, spacing
4. `interaction-motion-design` — how it moves and responds
5. `performance-states-patterns` — empty, loading, error, offline, success
6. `accessibility-inclusive-design` — before it's built, not after

**Gate:** every screen has all its states specified. A design that only shows the
happy path is a mockup, not a design.
**Artifact:** design specification with a state matrix.

### Implement — building the real thing

1. `design-systems-architecture` — which tokens and components already exist
2. `ui-visual-design-system` — visual spec for anything new
3. `component-patterns-code` — production code, full state matrix, ARIA
4. `accessibility-inclusive-design` — verify against the built artifact
5. `performance-states-patterns` — perceived performance and state handling

**Gate:** keyboard-navigable, screen-reader-labelled, every state rendered.
**Artifact:** component code plus its state and a11y checklist.

### Systematize — starting or scaling a design system

1. `design-systems-architecture` — token tiers, governance, versioning
2. `ui-visual-design-system` — the visual language the tokens encode
3. `component-patterns-code` — reference implementations
4. `figma-design-tool-workflows` — keep design and code in sync

**Gate:** tokens are a single source of truth in W3C DTCG format, and one change
propagates everywhere without hand-editing.
**Artifact:** token file, component inventory, governance model.

### Handoff — design to code

1. `figma-design-tool-workflows` — Auto Layout, variables, Dev Mode, MCP
2. `design-systems-architecture` — map Figma variables onto real tokens
3. `component-patterns-code` — generate the platform code

**Gate:** generated code consumes tokens, not hardcoded values.
**Artifact:** platform code traceable back to the source design.

### Localize — new markets

1. `cross-cultural-i18n-ux` — RTL, CJK, expansion, locale formats, color meaning
2. `ui-visual-design-system` — logical properties, flexible containers
3. `accessibility-inclusive-design` — language attributes, reading order

**Gate:** layout survives 40% text expansion and RTL mirroring.
**Artifact:** localization readiness report.

### AI Surface — designing an AI or agent feature

1. `agentic-ai-generative-ux` — agent patterns, confidence, guardrails
2. `ai-spatial-voice-ux` — conversational, voice, multimodal patterns
3. `ux-ethics-content-strategy` — consent, control, accountability
4. `cognitive-psychology-ux` — trust calibration and automation bias

**Gate:** the user can tell what the AI did, why, and how to undo it.
**Artifact:** AI interaction spec with trust and recovery affordances.

### Measure — did it work

1. `ux-metrics-measurement` — HEART, SUS, task success, statistical validity
2. `ux-research-methods` — the study design that produces those numbers

**Gate:** every metric has a baseline. A metric without a baseline cannot show
improvement.
**Artifact:** measurement plan with baselines and instrumentation.

## Platform layer

Layer the matching platform skill into whichever pipeline is running:

- Mobile or responsive → `mobile-ux-design`
- Desktop, enterprise, dashboards, data-dense → `desktop-app-design`
- Ambient, wearable, automotive, screenless → `ambient-calm-zero-ui`

## Operating rules

- **Announce the pipeline before running it.** The user should know which stages
  are coming and roughly what each costs them in time.
- **One stage at a time.** Each skill's content stays in context once loaded, so
  running six at once is both slower and worse than running them in sequence.
- **Report gate failures.** "Stage 3 failed the gate — 12 findings have no
  severity rating" is useful. Silently continuing is not.
- **Short-circuit narrow requests.** "What's a good tap target size?" is one
  skill, not a pipeline. Don't run process for its own sake.
- **Stop when the decision is answerable.** The pipeline serves the decision, not
  the other way around.

## Cross-references

Each pipeline's stages have their own reference files, listed inside each skill.
Load references only when the stage's SKILL.md points to them — they are large
and they persist in context once read.
