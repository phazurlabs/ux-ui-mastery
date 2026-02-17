---
name: brain-scan
description: Cognitive audit — Laws of UX, Gestalt principles, cognitive bias analysis. Score decision architecture, visual cognition, memory load, and attention management.
user_invocable: true
---

# Brain Scan — Cognitive Psychology Audit

Audit an interface against cognitive psychology principles — Laws of UX, Gestalt principles, cognitive biases, attention science, and memory constraints. Identify where the design works against human cognition and provide evidence-based fixes.

## Audit Protocol

1. **Identify the target**: Determine what is being audited and the user context.
   - Interface type (form, dashboard, checkout, navigation, onboarding, settings)
   - Primary user task and goal
   - User expertise level (novice, intermediate, expert)
   - Time pressure or environmental context

2. **Evaluate against Laws of UX**:

   | Law | Check |
   |-----|-------|
   | **Hick's Law** | How many choices are presented simultaneously? Are options progressively disclosed? Is decision time proportional to importance? |
   | **Fitts's Law** | Are primary actions large enough and positioned near focus? Are destructive actions distant from constructive ones? Mobile tap targets >= 44pt? |
   | **Miller's Law** | Are more than 4-7 items presented without chunking? Is information grouped into meaningful clusters? |
   | **Jakob's Law** | Does the interface follow platform/industry conventions? Where does it deviate, and is the deviation justified by core value? |
   | **Doherty Threshold** | Do interactions respond within 400ms? Are delays masked with feedback (progress, skeleton, optimistic UI)? |
   | **Peak-End Rule** | What is the emotional peak of the experience? What is the final moment? Are both deliberately designed? |
   | **Von Restorff Effect** | Does the most important element visually stand out? Is distinctiveness used strategically (not everywhere)? |
   | **Serial Position** | Are the most important items placed first and last in lists/menus? |
   | **Aesthetic-Usability** | Is visual polish potentially masking usability problems? |
   | **Tesler's Law** | Has complexity been reduced as far as possible without removing essential functionality? |
   | **Postel's Law** | Is the interface liberal in what it accepts from users (flexible input parsing, forgiving formatting)? |
   | **Zeigarnik Effect** | Are incomplete tasks creating productive engagement or anxiety? |

3. **Evaluate Gestalt principles**:
   - **Proximity**: Are related elements close together? Are unrelated elements sufficiently separated?
   - **Similarity**: Do similar elements share consistent visual treatment?
   - **Closure**: Can users complete partial patterns mentally? Are shapes and regions implied effectively?
   - **Continuity**: Do visual flows guide the eye in the intended direction?
   - **Common Region**: Are groups enclosed or backgrounded to show relationship?
   - **Figure-Ground**: Is the primary content clearly distinguished from background?

4. **Evaluate cognitive load**:
   - **Intrinsic load**: Is task complexity managed through decomposition (wizard, progressive form)?
   - **Extraneous load**: What unnecessary cognitive demands does the design impose? (confusing labels, hidden controls, inconsistent patterns, visual noise)
   - **Germane load**: Does the design build reusable mental schemas through consistency?
   - **Working memory demand**: At any single step, how many items must the user hold in working memory?

5. **Scan for cognitive bias exploitation or risk**:
   - Anchoring bias (are reference points fair or manipulative?)
   - Default bias (do defaults serve users or the business?)
   - Confirmation bias (does the interface surface disconfirming information?)
   - Framing effect (is information framed neutrally or manipulatively?)
   - Choice overload (are there too many options without curation?)
   - Sunk cost framing (does the design leverage past investment to trap users?)

6. **Score each domain** (1-10):

   | Domain | Score Criteria |
   |--------|---------------|
   | Decision Architecture | Choice count, defaults, progressive disclosure |
   | Visual Cognition | Gestalt compliance, hierarchy clarity, figure-ground |
   | Memory Load | Working memory demand, recognition vs. recall, chunking |
   | Attention Management | Focus direction, interruption protection, sustained attention support |
   | Bias Ethics | Fair defaults, neutral framing, no dark patterns |

## Output Format

```
## Brain Scan: [Interface Name]

### Context
- **Interface**: [type and description]
- **Primary Task**: [user goal]
- **User Level**: [novice / intermediate / expert]

### Domain Scores
| Domain | Score | Key Finding |
|--------|-------|-------------|
| Decision Architecture | X/10 | [one-line summary] |
| Visual Cognition | X/10 | [one-line summary] |
| Memory Load | X/10 | [one-line summary] |
| Attention Management | X/10 | [one-line summary] |
| Bias Ethics | X/10 | [one-line summary] |

**Cognitive Health Score**: [average]/10

### Laws of UX Findings
[Each violated law with specific location, evidence, and fix]

### Gestalt Findings
[Principle violations with visual description and correction]

### Cognitive Load Analysis
[Breakdown of intrinsic, extraneous, and germane load with reduction strategies]

### Bias Audit
[Any biases being exploited or risks identified, with ethical alternatives]

### Recommended Fixes (Priority Order)
[Top 5 fixes with predicted cognitive impact]
```

## Cross-References
When auditing cognitive factors, draw from:
- `cognitive-psychology-ux` skill for Laws of UX encyclopedia, cognitive biases catalog, and neurodesign science
- `nng-ux-heuristics` skill for heuristic grounding (H2 mental models, H6 recognition, H8 minimalist design)
- `ux-ethics-content-strategy` skill for ethical evaluation of bias exploitation
- `performance-states-patterns` skill for Doherty Threshold and perceived performance
- `accessibility-inclusive-design` skill for cognitive accessibility (ADHD, dyslexia, age-related decline)

## Next Steps
After running `/brain-scan`, consider:
- `/remix` — Redesign to fix cognitive issues with UX reasoning
- `/roast` — Full design critique with dimensional scoring
- `/flow` — Audit the multi-step journey for cognitive load accumulation
- `/dark-scan` — Check if detected biases cross into dark patterns
