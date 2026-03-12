---
description: "Competitive analysis — 10-dimension scorecard, gap analysis, improvement roadmap, and differentiation strategy."
tier: "plan"
---

# Benchmark — Competitive Design Analysis

Compare a design against the best apps in its category. Score across 10 dimensions, identify specific gaps, and generate an actionable roadmap to close them.

## Protocol

### Step 1: Establish Context

Determine what is being benchmarked and against what:

- **Subject**: The design, app, or product being evaluated (accept code, screenshots, descriptions, or URLs)
- **Category**: The product category for comparison (e.g., "neobank", "team messaging", "food delivery")
- **Competitors**: If specified by the user, benchmark against those. Otherwise, select the top 5 in the category
- **Platform**: iOS, Android, Web, Desktop, or cross-platform
- **Maturity stage**: Early (MVP/beta), Growth (scaling), Mature (established) -- calibrates expectations

### Step 2: Identify the Benchmark Set

Select 5 best-in-class apps in the category. For each:

- **App name and company**
- **Platform availability**
- **Signature UX strength**: What they are known for
- **Market position**: Why they are a valid benchmark
- **Design reputation**: Awards, notable designers, known for design excellence

Selection criteria: Prioritize apps known for design quality, not just market share. A well-designed smaller app can be a better benchmark than a dominant but poorly-designed market leader.

### Step 3: Score Across 10 Dimensions (1-10)

| Score | Meaning |
|-------|---------|
| 1-2 | Broken -- fails basic expectations |
| 3-4 | Below average -- noticeably worse than competitors |
| 5-6 | Average -- meets baseline, no standout quality |
| 7-8 | Good -- above average, intentional design thinking |
| 9-10 | Exceptional -- best-in-class, a reference for others |

**Dimension 1: Visual Polish**
- Consistency of visual language across screens
- Typography quality (hierarchy, spacing, readability)
- Color usage (intentional, accessible, harmonious)
- Iconography and illustration quality
- Attention to detail (alignment, pixel precision, edge cases)

**Dimension 2: Information Architecture**
- Navigation structure clarity and findability
- Content organization and categorization
- Search and discovery effectiveness
- Mental model alignment
- Depth vs. breadth balance

**Dimension 3: Interaction Quality**
- Feedback for every user action (visual, haptic, audio)
- Animation quality and purposefulness
- Gesture support and discoverability
- Touch/click target sizing
- Responsiveness and perceived performance

**Dimension 4: Accessibility**
- Screen reader compatibility
- Keyboard navigation completeness
- Color contrast compliance (WCAG AA minimum)
- Text resizing support
- Motion sensitivity respect (prefers-reduced-motion)
- Touch targets minimum 44x44pt
- Focus management quality

**Dimension 5: Performance UX**
- Perceived loading speed (skeleton screens, optimistic updates)
- Offline behavior and resilience
- Error recovery (network failures, timeouts)
- State preservation (back button, app switching, session restore)
- Progressive loading, startup time

**Dimension 6: Onboarding**
- Time to first value
- Progressive disclosure
- Permission request timing and copy
- Skip-ability
- Return user experience

**Dimension 7: Navigation**
- Primary navigation clarity and reachability
- Wayfinding (user always knows where they are)
- Back/undo/escape reliability
- Deep linking and shareability
- Navigation efficiency (steps to reach any feature)

**Dimension 8: Content Quality**
- Microcopy clarity (labels, instructions, CTAs)
- Error message helpfulness
- Empty state design (instructive, actionable)
- Tone consistency
- Content loading and pagination patterns

**Dimension 9: Mobile Experience**
- Thumb-zone optimization
- Platform convention adherence (iOS HIG / Material 3)
- Gesture utilization (swipe, pinch, long-press)
- System integration (widgets, shortcuts, share sheet, notifications)
- Dynamic Type / text scaling support

**Dimension 10: Innovation**
- Novel interaction patterns solving real problems
- Unique differentiating features
- Creative platform capability use
- Forward-thinking design (AI, spatial, voice)
- Risk-taking that pays off vs. unnecessary novelty

### Step 4: Gap Analysis

For each dimension where the subject scores lower than benchmark leaders:

- **Gap description**: "[Benchmark app] does [specific thing], you don't"
- **Impact**: How much this affects UX (High / Medium / Low)
- **Difficulty to close**: How hard to implement (Easy / Medium / Hard)
- **Quick win available?**: Simple first step that partially closes the gap

### Step 5: Improvement Roadmap

Classify improvements into three tiers:

**Tier 1 -- Quick Wins** (1-2 sprints):
- High impact, low effort
- Visual polish, copy improvements, small interaction fixes
- Ship without major architecture changes

**Tier 2 -- Strategic Improvements** (1-2 quarters):
- Medium-to-high impact, medium effort
- New components, redesigned flows, feature additions
- Closes the most significant gaps

**Tier 3 -- Differentiation Moves** (2-4 quarters):
- Investments that could leapfrog the competition
- Novel features, platform capabilities, design innovations
- Not about closing gaps -- about creating new advantages

### Step 6: Competitive Position Map

Place subject and benchmark apps on a 2x2 matrix:
- Axes selected based on what matters most in the category
- Common pairs: Polish vs. Feature Richness, Simplicity vs. Power, Delight vs. Efficiency
- Identify the open quadrant (opportunity space)

## Output Format

```
## Benchmark Report: [Product Name] vs. [Category] Leaders

### Benchmark Set
| App | Platform | Known For | Why Included |
|-----|----------|-----------|--------------|
[5 rows]

### Dimension Scores

| Dimension | [Subject] | [Comp 1] | [Comp 2] | [Comp 3] | [Comp 4] | [Comp 5] |
|-----------|-----------|----------|----------|----------|----------|----------|
| Visual Polish | X | X | X | X | X | X |
| Info Architecture | X | X | X | X | X | X |
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
[For each gap: what competitor does, what subject lacks, impact, difficulty]

### Improvement Roadmap

#### Tier 1: Quick Wins (1-2 sprints)
[Specific improvements with expected impact]

#### Tier 2: Strategic Improvements (1-2 quarters)
[Larger initiatives with gap-closing potential]

#### Tier 3: Differentiation Moves (2-4 quarters)
[Innovative investments to leapfrog competition]

### Competitive Position Map
[2x2 matrix with positioning analysis]

### Key Takeaway
[1-2 sentences: the single most important insight]
```

## Quality Gates

The output MUST include:
- [ ] 5 benchmark competitors with selection rationale
- [ ] All 10 dimensions scored with specific evidence for each score
- [ ] Gap analysis with impact and difficulty ratings
- [ ] Three-tier improvement roadmap with actionable items
- [ ] Competitive position map with opportunity space identified
- [ ] Scores calibrated to maturity stage (don't expect MVP to match mature products)

The output MUST NOT include:
- Scores without evidence or rationale
- Generic improvement suggestions not tied to specific gaps
- Benchmark apps selected purely on market share (design quality matters)
- Missing dimensions (all 10 must be scored)

## Cross-References

When benchmarking, draw knowledge from:
- `design-critique-case-studies` skill for teardown methodology and product deep-dives
- `nng-ux-heuristics` skill for consistent evaluation criteria
- `ui-visual-design-system` skill for visual polish assessment
- `accessibility-inclusive-design` skill for accessibility scoring against WCAG 2.2
- `ux-metrics-measurement` skill for quantitative benchmarking and industry baselines
- `mobile-ux-design` skill for platform convention evaluation (iOS HIG, Material 3)
- `interaction-motion-design` skill for interaction quality and animation assessment
- `performance-states-patterns` skill for performance UX evaluation

## Next Step

**Next** --> `/measure` -- Define metrics to track the gaps you found

**Alternatives**:
- `/style` -- Set visual direction informed by competitive landscape
- `/roast` -- Deep critique of your own design
- `/sumi` -- See the full command map
