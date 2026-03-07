---
description: "[5.1] Usability test plan — generate test script, task scenarios, success criteria, participant recruitment screener, and analysis template for validating your design with real users."
phase: "5"
phase_step: "5.1"
phase_name: "VALIDATE"
step_label: "Step 22 of 30"
---

# Test — Usability Test Plan Generator

Generate a complete usability test plan: research questions, task scenarios, moderator script, participant recruitment screener, and analysis template. Every world-class design framework includes user testing — this is the step vibe coders skip that separates "looks good to designers" from "works for users."

## Analysis Protocol

### Step 0: Gather Context

Before generating the test plan, collect:

1. **Product description and key flows**: What does the product do? Which flows are most critical to test?
2. **Research questions**: What assumptions are we testing? What do we need to learn?
3. **Platform**: Mobile, desktop, or both — affects test setup and task design.
4. **Stage**: Are we testing wireframes, interactive prototypes, or a live product?
5. **Budget/tools available**: UserTesting, Maze, Lookback, Zoom, or in-person lab?
6. **Prior Sumi outputs**: Consume `/02-brief` (persona), `/12-flow` (user flows), `/09-wireframe` (layouts) if available.

If the user has not run prior commands, proceed with what's provided and note what additional context would strengthen the plan.

### Step 1: DEFINE TEST OBJECTIVES

Establish the foundation of the test:

- **Primary research questions** (max 3-5 — focus matters, a sprawling test yields shallow answers)
- **Hypotheses to validate/invalidate** — what do we believe is true that we're testing?
- **Success metrics**: task completion rate, time on task, error rate, satisfaction (SUS/UMUX-Lite)
- **Decision framework**: What decisions will this test inform? What will we do differently based on results?

A test without clear objectives produces data without insight. Every question must map to a decision.

### Step 2: TASK SCENARIOS

For each key flow being tested (3-5 tasks recommended):

- **Scenario context** — a realistic situation, not instructions
  - GOOD: "You want to send $50 to your friend Alex for dinner last night."
  - BAD: "Click the Send Money button and enter an amount."
- **Success criteria** for each task — what constitutes completion?
- **Expected completion time** — baseline for comparison
- **Critical paths to observe** — what decision points matter?
- **Common failure points** — where do we expect users to struggle?
- **Probing questions** — what to ask if the user gets stuck or takes an unexpected path

Task order matters: start with a warm-up task, escalate complexity, end with the most critical flow.

### Step 3: TEST SCRIPT

Generate a complete moderator script:

**Introduction (5 min)**:
- Consent and recording permission
- Think-aloud protocol instruction ("Please say everything you're thinking as you use this")
- Reassurance ("We're testing the product, not you — there are no wrong answers")
- Session structure overview

**Pre-test questions (5 min)**:
- Current behavior and habits related to the product domain
- Prior experience with similar products
- Expectations before seeing the product

**Task administration (25-35 min)**:
- Read scenario verbatim (no leading language)
- Observe silently — resist the urge to help
- Note-taking cues for observers
- Probing questions between tasks: "What did you expect to happen?" "Was anything confusing?"

**Post-task questions after each task (2 min each)**:
- Single Ease Question (SEQ): "How easy or difficult was that task?" (1-7 scale)
- "What did you expect to happen when you [action]?"
- "Was there anything confusing or unexpected?"

**Post-test questions (10 min)**:
- System Usability Scale (SUS) — 10 standardized questions
- "What was the most frustrating part of the experience?"
- "What was the most positive part?"
- "How does this compare to [competitor/current solution]?"
- "If you could change one thing, what would it be?"

**Debrief (2 min)**:
- Thank participant
- Ask if they have questions
- Explain next steps and how their feedback will be used

### Step 4: PARTICIPANT PLAN

**Profile** (maps to persona from `/02-brief` if available):
- Demographics, behaviors, and experience level that match target users
- Include at least one segment of users who are NOT power users

**Sample size**:
- **Qualitative (formative)**: 5 users — finds ~85% of usability issues (Nielsen, 2000)
- **Quantitative (summative)**: 20+ users — needed for statistical significance on metrics
- Justify the recommendation based on the testing stage and objectives

**Screening questions** (6-8) to qualify participants:
- Mix of behavioral and demographic questions
- Include disqualifiers (people who work in UX/tech, competitors' employees)
- At least one question that confirms relevant domain experience
- Avoid leading questions that reveal what you're looking for

**Recruitment channels**:
- UserTesting.com, Respondent.io, or similar panel
- Social media / community outreach for niche audiences
- Customer database (for existing products)
- Guerrilla testing (for quick validation)

**Incentive recommendation**: $50-150 depending on duration, complexity, and participant profile. B2B and specialized audiences command higher incentives.

**Scheduling**: 45-60 min sessions, 15 min buffer between sessions for debrief and reset.

### Step 5: SETUP & LOGISTICS

- **Test environment**: Remote (Zoom/Lookback/UserTesting) or in-person lab — recommend based on context
- **Recording**: Screen + audio + face (with consent) — critical for playback and stakeholder buy-in
- **Prototype preparation**: Ensure all task paths are functional, dead ends are handled gracefully
- **Tools**: Task tracking spreadsheet, note-taking template, observer guide, timer
- **Roles**: Moderator (asks questions), note-taker (captures observations), observer (stakeholders watch silently)
- **Pilot test**: Run 1 session internally first to calibrate timing, catch script issues, and ensure prototype works

### Step 6: ANALYSIS TEMPLATE

**Rainbow spreadsheet**:
- Rows: Observations and quotes
- Columns: Participant 1, 2, 3, 4, 5
- Color-coded by participant for pattern spotting
- Group by task

**Severity rating framework**:
- **Critical (4)**: Prevents task completion, affects all/most users
- **Serious (3)**: Causes significant delay or frustration, affects many users
- **Minor (2)**: Causes slight hesitation, affects some users
- **Cosmetic (1)**: Noticed but doesn't affect task performance

**Affinity mapping guide**:
- Transcribe all observations onto individual notes
- Group by theme (not by task or participant)
- Name each theme
- Prioritize themes by frequency and severity

**Metrics dashboard template**:
- Per-task: completion rate, average time, error count, SEQ score
- Overall: SUS score, task success rate, critical error rate
- Benchmarks: compare against industry averages or prior tests

**Report structure**:
1. Executive summary (1 page — findings + recommendations)
2. Methodology (participants, tasks, setup)
3. Findings per task (observations, metrics, severity, quotes)
4. Cross-cutting themes
5. Prioritized recommendations (with effort estimates)
6. Raw data appendix (rainbow spreadsheet, SUS scores, recordings index)

## Output Format

```
### Phase Position
> **Phase 5: VALIDATE** | Step 22 of 30 | `/22-test`
>
> `/21-assets` -> **`/22-test`** -> `/23-roast`

---

## Usability Test Plan

### Test Objectives
[3-5 research questions with hypotheses and success metrics]
[Decision framework: what changes based on results]

---

### Task Scenarios

#### Task 1: [Name]
- **Scenario**: "[Realistic situation]"
- **Success criteria**: [What constitutes completion]
- **Expected time**: [X minutes]
- **Watch for**: [Critical paths and failure points]

#### Task 2: [Name]
[continue for 3-5 tasks]

---

### Moderator Script

#### Introduction
[Complete intro script with consent, think-aloud, reassurance]

#### Pre-Test Questions
[3-5 questions about current behavior and expectations]

#### Task Administration
[Per-task script with scenario text, probing questions]

#### Post-Task Questions
[SEQ + follow-up questions after each task]

#### Post-Test Questions
[SUS, overall impressions, comparative, one-change question]

#### Debrief
[Thank you, next steps, questions]

---

### Participant Plan
- **Profile**: [Target user description]
- **Sample size**: [N] participants — [justification]
- **Screening questions**: [6-8 qualification questions]
- **Recruitment**: [Channels and approach]
- **Incentive**: [$X — justification]
- **Schedule**: [Session length, buffer, total timeline]

---

### Setup & Logistics
- **Environment**: [Remote/in-person — recommendation]
- **Recording**: [Screen + audio + face setup]
- **Tools**: [Tracking, notes, observer guide]
- **Roles**: [Moderator, note-taker, observer assignments]
- **Pilot test**: [Plan for internal dry run]

---

### Analysis Template

#### Rainbow Spreadsheet
[Template structure with participant columns and task rows]

#### Severity Ratings
| Level | Name | Definition | Action |
|-------|------|------------|--------|
| 4 | Critical | Prevents task completion | Fix before launch |
| 3 | Serious | Significant delay/frustration | Fix in current cycle |
| 2 | Minor | Slight hesitation | Fix in next cycle |
| 1 | Cosmetic | Noticed, no impact | Backlog |

#### Metrics Dashboard
[Per-task and overall metrics template]

#### Report Structure
[Section outline for final report]

---

### Next Steps
1. **Conduct tests** using this plan — start with the pilot session
2. **Then** -> `/23-roast` — Expert critique to complement user feedback
3. **Or** -> `/24-remix` — Redesign based on test findings

**Run `/next` to continue the journey.**
```

## Quality Gates

The output MUST include:
- [ ] 3-5 focused research questions (not a laundry list)
- [ ] Task scenarios written as realistic situations, not instructions
- [ ] Complete moderator script with think-aloud protocol
- [ ] Sample size justified (5 for qualitative, 20+ for quantitative)
- [ ] Screening questions that qualify the right participants
- [ ] Analysis template with severity ratings
- [ ] Clear link between findings and next Sumi commands

The output MUST NOT include:
- Generic test plans not tailored to the specific product
- Task scenarios written as instructions ("Click X, then Y")
- Sample sizes without justification
- Missing moderator script sections (every section must be complete)
- Analysis guidance without severity framework

## Cross-References

When generating the test plan, draw knowledge from:
- `ux-research-methods` skill — primary knowledge source for test methodology, research design, sampling
- `ux-metrics-measurement` skill — SUS, UMUX-Lite, SEQ, task success metrics, benchmark data
- `cognitive-psychology-ux` skill — observation techniques, cognitive biases to watch for, think-aloud protocol
- `screen-flow-patterns` skill — identifying key flows to test, expected user paths
- `ux-process-workflow` skill — where testing fits in the design process, iterative validation

## Next Step

**Next** -> `/23-roast` (5.2) — Expert critique to complement user feedback with heuristic evaluation

**Alternatives**:
- `/24-remix` — Redesign flows based on test findings
- `/25-qa` — Design QA to verify implementation fidelity
- `/12-flow` — Revisit user flows before testing
- `/guide` — See the full journey map
