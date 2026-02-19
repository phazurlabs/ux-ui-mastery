---
description: Generate a complete UX metrics plan — HEART framework with goals, signals, metrics, dashboards, and experimentation strategy.
phase: "1"
phase_step: "1.4"
phase_name: "DISCOVER"
step_label: "Step 4 of 4"
---

# Pulse — UX Metrics Plan

Generate a comprehensive UX metrics plan for the specified product or feature, mapping product goals to measurable user experience metrics using the HEART framework.

## Generation Protocol

1. **Gather Product Context**:
   - Product name, type, and primary user segments
   - Business goals and product strategy
   - Current measurement maturity (none, basic analytics, structured metrics)
   - Key user flows and tasks
   - Available tools (analytics platform, survey tools, testing infrastructure)

2. **Map HEART Framework Dimensions**:

   For each relevant HEART dimension (Happiness, Engagement, Adoption, Retention, Task Success):

   **Goals** — Define the desired user outcome for this dimension
   - What does success look like from the user's perspective?
   - How does this connect to business objectives?

   **Signals** — Identify user behaviors that indicate progress toward the goal
   - What observable actions suggest users are achieving the goal?
   - What behavioral patterns indicate problems?

   **Metrics** — Quantify each signal with a concrete metric
   - How exactly do you measure the signal?
   - What is the formula or calculation?
   - What is the measurement frequency?

3. **Select Measurement Instruments**:
   - Recommend standardized questionnaires (SUS, UEQ, UMUX-Lite, SUPR-Q, NPS, CES) with justification for each selection
   - Define custom metrics with precise calculation formulas
   - Specify analytics events and tracking requirements
   - Design survey deployment strategy (timing, frequency, sample)

4. **Establish Baselines and Targets**:
   - Current baseline measurement plan (how to measure the starting point)
   - Industry benchmark comparison where available
   - Target-setting methodology (percentage improvement, percentile ranking, absolute threshold)
   - Timeline for achieving targets

5. **Design Experimentation Framework**:
   - Hypothesis template for the product
   - A/B testing strategy (what to test, sample size requirements, duration)
   - Guardrail metrics (metrics that must not regress)
   - Decision criteria (when is a result significant enough to act on?)

6. **Specify Dashboard**:
   - Executive dashboard (3-5 headline metrics, trends, red/yellow/green status)
   - Team dashboard (detailed metrics, drill-down, segment views)
   - Alert configuration (regression thresholds, notification channels)
   - Update cadence (real-time, daily, weekly, quarterly review)

## Output Format

```
### Phase Position
> **Phase 1: DISCOVER** | Step 4 of 4 | `/pulse`
> *NNG: Metrics & Measurement | Visual: Success Criteria*
>
> `/benchmark` (1.3) → **`/pulse` (1.4)** → **Phase 2: DIAGNOSE** `/vibe-check` (2.1)

## UX Metrics Plan: [Product Name]

### Product Context
- **Product**: [name and type]
- **Users**: [primary segments]
- **Goals**: [top 3 business/product goals]

### HEART Framework Mapping

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
- **Analytics Events**: [event taxonomy and tracking plan]
- **Survey Schedule**: [instruments, timing, sample sizes]
- **Usability Testing Cadence**: [frequency, participant count, metrics collected]

### Experimentation Framework
- **Hypothesis Template**: [customized for this product]
- **Testing Priorities**: [what to test first]
- **Sample Size Requirements**: [per test type]
- **Guardrail Metrics**: [must-not-regress list]

### Dashboard Specification

#### Executive View
[3-5 headline metrics with visualization type and update cadence]

#### Team View
[Detailed metrics with drill-down specification]

#### Alerts
[Regression thresholds and notification rules]

### Baseline Measurement Plan
[Step-by-step plan for establishing current baselines within 30 days]

### 90-Day Measurement Roadmap
[Week-by-week plan for implementing the full metrics system]
```

## Cross-References
When generating the plan, draw context from:
- `ux-metrics-measurement` skill for framework details and benchmarks
- `ux-research-methods` skill for research methodology integration
- `nng-ux-heuristics` skill for qualitative evaluation criteria
- `agentic-ai-generative-ux` skill for AI-specific metrics (if product includes AI features)
- `design-systems-architecture` skill for design system metrics (if applicable)

## Next Step

**Phase 1: DISCOVER complete.** You have style direction, pattern references, competitive gaps, and a metrics plan.

**Next phase** → **Phase 2: DIAGNOSE** — Start with `/vibe-check` (2.1)

**Alternatives**:
- `/drip` (4.1) — Jump to BUILD if no existing product to audit
- `/guide` — See the full 20-step journey
