---
description: User flow audit — map, score, and optimize any multi-step user journey for efficiency, cognitive load, emotional arc, and conversion.
phase: "2"
phase_step: "2.4"
phase_name: "DIAGNOSE"
step_label: "Step 4 of 4"
---

# Flow — User Flow Audit

Audit a complete user journey across multiple screens or steps, identifying friction, unnecessary complexity, and drop-off risks while optimizing the emotional arc for completion.

## Flow Audit Protocol

1. **Accept and classify the flow**:
   - Identify flow type: onboarding, signup, checkout, settings change, content creation, search-to-action, account recovery, upgrade/upsell, or custom
   - Determine flow criticality: revenue-critical, retention-critical, trust-critical, or utility
   - Establish the entry point (where users come from) and the success state (what "done" looks like)
   - Note the platform context: mobile, desktop, cross-device, or embedded

2. **Map every step in the flow**:
   - Enumerate each distinct screen, modal, or interaction step from entry to completion
   - For each step, document: screen name, primary action, secondary actions, data collected/displayed, decisions the user must make
   - Identify branching paths (conditional steps, error branches, optional steps)
   - Note system-initiated steps (loading, processing, verification emails, SMS codes)
   - Calculate total step count and estimated time-to-completion

3. **Evaluate per-step cognitive load**:
   - Count decisions per step (Hick's Law — each decision adds friction)
   - Count input fields per step (Miller's Law — keep chunks to 4 +/- 1)
   - Assess visual complexity: information density, competing CTAs, distracting elements
   - Track cumulative cognitive load across the entire flow (load should not monotonically increase)
   - Flag steps where load spikes unexpectedly

4. **Assess drop-off risk per step**:
   - Rate each step 1-5 for drop-off risk based on: effort required, value unclear, trust barrier, technical friction, interruption likelihood
   - Identify the "valley of death" — the step with highest drop-off risk
   - Check if value is demonstrated before effort is demanded (the Reciprocity Principle)
   - Verify progress indication exists and is accurate

5. **Analyze the emotional arc (Peak-End Rule)**:
   - Map emotional valence per step: delight, neutral, friction, anxiety, relief, accomplishment
   - Verify the flow has at least one designed peak moment (positive surprise, social proof, personalization)
   - Verify the end state is emotionally positive (confirmation, celebration, immediate value delivery)
   - Check for negative emotional clusters (consecutive friction steps without relief)

6. **Evaluate error recovery mid-flow**:
   - What happens if the user makes an error at step 3 of 7? Do they lose progress?
   - Is back-navigation safe (no data loss)?
   - Can users save progress and return later?
   - Are error messages contextual and recovery-oriented?

7. **Score the flow** (each 1-10):

   | Dimension | What It Measures |
   |-----------|-----------------|
   | Flow Efficiency | Ratio of necessary to total steps — are there steps that can be cut or merged? |
   | Cognitive Progression | Does cognitive load distribute well across steps or spike dangerously? |
   | Emotional Arc | Is the Peak-End Rule satisfied? Is there delight and strong closure? |
   | Error Recovery | Can users recover from mistakes without restarting the flow? |
   | Completion Likelihood | Given all factors, what percentage of users will finish? |

## Output Format

```
### Phase Position
> **Phase 2: DIAGNOSE** | Step 4 of 4 | `/flow`
> *NNG: Task Analysis | Visual: Journey Optimization*
>
> `/include` (2.3) → **`/flow` (2.4)** → **Phase 3: FORTIFY** `/dark-scan` (3.1)

## Flow Audit: [Flow Name]

### Flow Overview
- **Type**: [onboarding / checkout / signup / etc.]
- **Criticality**: [revenue / retention / trust / utility]
- **Total Steps**: [X] (recommended: [Y])
- **Estimated Time**: [X minutes]
- **Platform**: [mobile / desktop / cross-device]

### Flow Diagram
[Entry] → [Step 1: Name] → [Step 2: Name] → ... → [Success State]
              ↓ (error)        ↓ (branch)
         [Recovery]        [Alt Path]

### Per-Step Analysis
| Step | Screen | Cognitive Load (1-5) | Drop-off Risk (1-5) | Emotion | Issues |
|------|--------|---------------------|---------------------|---------|--------|
| 1    | ...    | ...                 | ...                 | ...     | ...    |

### Emotional Arc Visualization
Step 1: ████████░░ Curiosity (positive)
Step 2: ██████░░░░ Effort (neutral)
Step 3: ████░░░░░░ Friction (negative)  ← Valley of Death
Step 4: ████████░░ Relief (positive)    ← Designed Peak
Step 5: ██████████ Accomplishment       ← Strong End

### Dimension Scores
| Dimension | Score | Observation |
|-----------|-------|------------|
| Flow Efficiency | X/10 | ... |
| Cognitive Progression | X/10 | ... |
| Emotional Arc | X/10 | ... |
| Error Recovery | X/10 | ... |
| Completion Likelihood | X/10 | ... |

**Overall Flow Score**: [average]/10

### Recommended Optimizations
#### Steps to Cut
[Steps that add no value and should be eliminated]

#### Steps to Merge
[Consecutive steps that can be combined without overloading]

#### Steps to Add
[Missing steps that would reduce anxiety or increase trust — e.g., a progress indicator, a reassurance moment]

#### Friction Fixes
[Specific fixes for high-friction steps with before/after]
```

## Cross-References
When auditing flows, draw evaluation criteria from:
- `cognitive-psychology-ux` skill for Hick's Law, Miller's Law, Peak-End Rule, and cognitive load theory
- `nng-ux-heuristics` skill for visibility of system status (H1), user control and freedom (H3), error prevention (H5)
- `performance-states-patterns` skill for loading states, skeleton screens, and progress indicators within the flow
- `ux-metrics-measurement` skill for funnel metrics, drop-off benchmarks, and conversion rate optimization

## Next Step

**Phase 2: DIAGNOSE complete.** All UX problems cataloged — heuristic violations, cognitive risks, accessibility gaps, and flow bottlenecks.

**Next phase** → **Phase 3: FORTIFY** — Start with `/dark-scan` (3.1)

**Alternatives**:
- `/drip` (4.1) — Jump to BUILD if compliance isn't a concern
- `/guide` — See the full 20-step journey
