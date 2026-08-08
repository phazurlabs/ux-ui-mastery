---
name: measure
description: "Metrics plan — HEART framework, OKRs, experimentation strategy, dashboards, and baseline measurement."
argument-hint: "[product or feature to measure]"
---

# Measure — UX Metrics Plan

## Before running

This command needs a product or feature to measure.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a comprehensive UX metrics plan: map product goals to measurable user experience metrics using the HEART framework, design dashboards, establish baselines, and plan experiments.

## Protocol

### Step 1: Gather Product Context

- Product name, type, and primary user segments
- Business goals and product strategy
- Current measurement maturity (none, basic analytics, structured metrics)
- Key user flows and tasks
- Available tools (analytics platform, survey tools, testing infrastructure)

### Step 2: Map HEART Framework

For each relevant dimension (Happiness, Engagement, Adoption, Retention, Task Success):

**Goals** -- the desired user outcome:
- What does success look like from the user's perspective?
- How does this connect to business objectives?

**Signals** -- observable behaviors that indicate progress:
- What actions suggest users are achieving the goal?
- What patterns indicate problems?

**Metrics** -- quantified signals:
- How exactly do you measure the signal?
- What is the formula or calculation?
- What is the measurement frequency?

### Step 3: Select Measurement Instruments

- **Standardized questionnaires**: SUS, UEQ, UMUX-Lite, SUPR-Q, NPS, CES -- justify each selection
- **Custom metrics**: Precise calculation formulas
- **Analytics events**: Event taxonomy and tracking requirements
- **Survey deployment**: Timing, frequency, sample size

### Step 4: Baselines and Targets

- Current baseline measurement plan (how to measure the starting point)
- Industry benchmark comparison where available
- Target-setting methodology (percentage improvement, percentile ranking, absolute threshold)
- Timeline for achieving targets

### Step 5: Experimentation Framework

- **Hypothesis template** customized for this product
- **A/B testing strategy**: What to test, sample size requirements, duration
- **Guardrail metrics**: Metrics that must not regress
- **Decision criteria**: When is a result significant enough to act on?

### Step 6: Dashboard Specification

**Executive dashboard** (3-5 headline metrics):
- Trends, red/yellow/green status
- Update cadence (weekly or monthly)

**Team dashboard** (detailed metrics):
- Drill-down capability, segment views
- Update cadence (daily or real-time)

**Alert configuration**:
- Regression thresholds
- Notification channels
- Escalation rules

## Output Format

```
## UX Metrics Plan: [Product Name]

### Product Context
- **Product**: [name and type]
- **Users**: [primary segments]
- **Goals**: [top 3 business/product goals]
- **Measurement maturity**: [none / basic / structured]

### HEART Framework

#### Happiness
- **Goal**: [user outcome]
- **Signals**: [observable behaviors]
- **Metrics**: [specific measurements with formulas]
- **Instruments**: [SUS/UEQ/CSAT/custom + deployment plan]
- **Baseline**: [how to establish]
- **Target**: [specific target with timeline]

#### Engagement
[Same structure]

#### Adoption
[Same structure]

#### Retention
[Same structure]

#### Task Success
[Same structure]

### Measurement Implementation
- **Analytics events**: [event taxonomy and tracking plan]
- **Survey schedule**: [instruments, timing, sample sizes]
- **Usability testing cadence**: [frequency, participants, metrics]

### Experimentation Framework
- **Hypothesis template**: [customized for this product]
- **Testing priorities**: [what to test first]
- **Sample size requirements**: [per test type]
- **Guardrail metrics**: [must-not-regress list]

### Dashboard Specification

#### Executive View
[3-5 headline metrics with visualization and cadence]

#### Team View
[Detailed metrics with drill-down]

#### Alerts
[Thresholds and notification rules]

### Baseline Measurement Plan
[Step-by-step plan for establishing baselines within 30 days]

### 90-Day Measurement Roadmap
[Week-by-week plan for implementing the full metrics system]
```

## Quality Gates

The output MUST include:
- [ ] All 5 HEART dimensions addressed (or explicitly marked N/A with reason)
- [ ] Each metric has a formula or calculation method
- [ ] Baselines and targets with timelines
- [ ] Experimentation framework with hypothesis template
- [ ] Dashboard spec with executive and team views
- [ ] 90-day implementation roadmap
- [ ] Instruments justified (not just listed)

The output MUST NOT include:
- Metrics without formulas or measurement methods
- Targets without baselines or timelines
- Generic advice not tailored to the specific product
- Dashboard specs without update cadence

## Cross-References

When generating the plan, draw from:
- `ux-metrics-measurement` skill for framework details and benchmarks
- `ux-research-methods` skill for research methodology integration
- `nng-ux-heuristics` skill for qualitative evaluation criteria
- `agentic-ai-generative-ux` skill for AI-specific metrics (if product includes AI)
- `data-visualization-mastery` skill for dashboard design and chart selection

## Next Step

**Next** --> `/style` -- Set visual direction informed by metrics priorities

**Alternatives**:
- `/benchmark` -- Score your product against competitors
- `/screen` -- Build screens with metrics-informed priorities
- `/sumi` -- See the full command map
