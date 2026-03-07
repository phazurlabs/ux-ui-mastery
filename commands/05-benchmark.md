---
description: "[1.3] Competitive design benchmark — score a design against the best apps in its category across 10 UX dimensions with gap analysis."
phase: "1"
phase_step: "1.3"
phase_name: "DISCOVER"
step_label: "Step 5 of 30"
---

# Benchmark — Competitive Design Benchmark

Compare a design against the best apps in its category. Score across 10 dimensions, identify specific gaps, and generate an actionable roadmap to close them.

## Benchmark Protocol

1. **Establish the benchmark context**: Determine what is being benchmarked and against what.
   - **Subject**: The design, app, or product being evaluated (accept code, screenshots, descriptions, or product URLs)
   - **Category**: The product category for comparison (e.g., "neobank", "team messaging", "food delivery")
   - **Competitors**: If specified by the user, benchmark against those. Otherwise, select the top 5 apps in the category.
   - **Platform**: iOS, Android, Web, Desktop, or cross-platform
   - **Maturity stage**: Early (MVP/beta), Growth (scaling), Mature (established) — this calibrates expectations

2. **Identify the benchmark set**: Select 5 best-in-class apps in the category.
   - For each competitor, document:
     - **App name and company**
     - **Platform availability**
     - **What they are known for**: Their signature UX strength
     - **User base / market position**: Context for why they are a valid benchmark
     - **Design team reputation**: Awards, notable designers, known for design excellence
   - Selection criteria: Prioritize apps known for design quality, not just market share. A well-designed smaller app can be a better benchmark than a dominant but poorly-designed market leader.

3. **Score the subject across 10 dimensions**: Each dimension scored 1-10 with explicit criteria.

   | Score | Meaning |
   |-------|---------|
   | 1-2 | Broken — fails basic expectations, causes user harm or failure |
   | 3-4 | Below average — noticeably worse than most competitors |
   | 5-6 | Average — meets baseline expectations, no standout quality |
   | 7-8 | Good — above average, shows intentional design thinking |
   | 9-10 | Exceptional — best-in-class, could be a reference for others |

   **Dimension 1: Visual Polish**
   - Consistency of visual language across all screens
   - Typography quality (hierarchy, spacing, readability)
   - Color usage (intentional, accessible, harmonious)
   - Iconography and illustration quality
   - Attention to detail (alignment, pixel precision, edge cases)

   **Dimension 2: Information Architecture**
   - Navigation structure clarity and findability
   - Content organization and categorization
   - Search and discovery effectiveness
   - Mental model alignment (does the structure match how users think?)
   - Depth vs. breadth balance

   **Dimension 3: Interaction Quality**
   - Feedback for every user action (visual, haptic, audio)
   - Animation quality and purposefulness
   - Gesture support and discoverability
   - Touch/click target sizing
   - Responsiveness and perceived performance
   - Micro-interactions that enhance understanding

   **Dimension 4: Accessibility**
   - Screen reader compatibility
   - Keyboard navigation completeness
   - Color contrast compliance (WCAG AA minimum)
   - Text resizing support
   - Motion sensitivity respect (prefers-reduced-motion)
   - Touch target sizing (minimum 44x44pt)
   - Focus management quality

   **Dimension 5: Performance UX**
   - Perceived loading speed (skeleton screens, optimistic updates)
   - Offline behavior and resilience
   - Error recovery (network failures, timeouts)
   - State preservation (back button, app switching, session restore)
   - Progressive loading of heavy content
   - Startup time and first meaningful paint

   **Dimension 6: Onboarding**
   - Time to first value (how quickly does a new user experience the core benefit?)
   - Progressive disclosure (information revealed when needed, not all at once)
   - Permission request timing and copy
   - Skip-ability (can users bypass onboarding?)
   - Return user experience (re-engagement, re-activation)

   **Dimension 7: Navigation**
   - Primary navigation clarity and reachability
   - Wayfinding (user always knows where they are)
   - Back/undo/escape reliability
   - Deep linking and shareability
   - Navigation efficiency (steps to reach any feature)
   - Cross-platform navigation consistency

   **Dimension 8: Content Quality**
   - Microcopy clarity (labels, instructions, CTAs)
   - Error message helpfulness
   - Empty state design (instructive, actionable)
   - Tone consistency across all touchpoints
   - Localization quality (if applicable)
   - Content loading and pagination patterns

   **Dimension 9: Mobile Experience**
   - Thumb-zone optimization (reachability of key actions)
   - Platform convention adherence (iOS HIG / Material 3)
   - Gesture utilization (swipe, pinch, long-press)
   - System integration (widgets, shortcuts, share sheet, notifications)
   - Orientation and multitasking support
   - Dynamic Type / text scaling support

   **Dimension 10: Innovation**
   - Novel interaction patterns that solve real problems
   - Unique features that differentiate from competitors
   - Creative use of platform capabilities
   - Forward-thinking design decisions (AI, spatial, voice)
   - Risk-taking that pays off vs. unnecessary novelty

4. **Generate gap analysis**: For each dimension where the subject scores lower than the benchmark leaders.
   - **Gap description**: "[Benchmark app] does [specific thing], you don't"
   - **Impact**: How much this gap affects the user experience (High / Medium / Low)
   - **Difficulty to close**: How hard it would be to implement the improvement (Easy / Medium / Hard)
   - **Quick win available?**: Is there a simple first step that partially closes the gap?

5. **Classify improvements into three tiers**:

   **Tier 1 — Quick Wins** (close within 1-2 sprints):
   - High impact, low effort improvements
   - Usually visual polish, copy improvements, or small interaction fixes
   - Can be shipped without major architecture changes

   **Tier 2 — Strategic Improvements** (close within 1-2 quarters):
   - Medium-to-high impact, medium effort
   - May require new components, redesigned flows, or feature additions
   - Closes the most significant gaps with benchmark leaders

   **Tier 3 — Differentiation Moves** (close within 2-4 quarters):
   - Investments that could leapfrog the competition
   - Novel features, platform capabilities, or design innovations
   - Not about closing gaps but about creating new advantages

6. **Generate competitive positioning map**: Place the subject and all benchmark apps on a 2x2 matrix.
   - Axes selected based on what matters most in the category
   - Common axis pairs: Polish vs. Feature Richness, Simplicity vs. Power, Delight vs. Efficiency
   - Identify the open quadrant (opportunity space) and whether the subject should move toward it

## Output Format

```
### Phase Position
> **Phase 1: DISCOVER** | Step 3 of 4 | `/benchmark`
> *NNG: Competitive Analysis | Visual: Competitive Quality*
>
> `/inspo` (1.2) → **`/benchmark` (1.3)** → `/pulse` (1.4)

## Benchmark Report: [Product Name] vs. [Category] Leaders

### Benchmark Set
| App | Platform | Known For | Why Included |
|-----|----------|-----------|--------------|
[5 rows with benchmark competitors]

### Dimension Scores

| Dimension | [Subject] | [Comp 1] | [Comp 2] | [Comp 3] | [Comp 4] | [Comp 5] |
|-----------|-----------|----------|----------|----------|----------|----------|
| Visual Polish | X | X | X | X | X | X |
| Information Architecture | X | X | X | X | X | X |
| Interaction Quality | X | X | X | X | X | X |
| Accessibility | X | X | X | X | X | X |
| Performance UX | X | X | X | X | X | X |
| Onboarding | X | X | X | X | X | X |
| Navigation | X | X | X | X | X | X |
| Content Quality | X | X | X | X | X | X |
| Mobile Experience | X | X | X | X | X | X |
| Innovation | X | X | X | X | X | X |
| **Average** | **X** | **X** | **X** | **X** | **X** | **X** |

### Gap Analysis
[For each gap: what the competitor does, what the subject lacks, impact, and difficulty]

### Improvement Roadmap

#### Tier 1: Quick Wins (1-2 sprints)
[Specific, actionable improvements with expected impact]

#### Tier 2: Strategic Improvements (1-2 quarters)
[Larger initiatives with clear gap-closing potential]

#### Tier 3: Differentiation Moves (2-4 quarters)
[Innovative investments to leapfrog competition]

### Competitive Position Map
[2x2 matrix description with positioning]

### Key Takeaway
[1-2 sentences: the single most important insight from this benchmark]
```

## Cross-References
When benchmarking designs, draw evaluation frameworks and competitive knowledge from:
- `design-critique-case-studies` skill for product deep-dives, teardown methodology, and case study knowledge
- `nng-ux-heuristics` skill for consistent evaluation criteria across heuristic dimensions
- `ui-visual-design-system` skill for visual polish assessment and design system maturity evaluation
- `accessibility-inclusive-design` skill for accessibility dimension scoring against WCAG 2.2 criteria
- `ux-metrics-measurement` skill for quantitative benchmarking, industry baselines, and measurement methodology
- `mobile-ux-design` skill for platform convention evaluation (iOS HIG, Material 3)
- `interaction-motion-design` skill for interaction quality and animation assessment
- `performance-states-patterns` skill for performance UX evaluation and state handling assessment

## Next Step

**Next** → `/pulse` (1.4) — Define metrics to track the gaps you found

**Alternatives**:
- `/vibe-check` (2.1) — Jump to DIAGNOSE if you already have metrics
- `/remix` (5.2) — Redesign specific areas where you scored lowest
- `/guide` — See the full 20-step journey
