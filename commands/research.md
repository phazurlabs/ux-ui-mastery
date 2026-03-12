---
description: "User research and usability testing — interview guides, survey design, test plans, recruitment, and analysis frameworks."
tier: "plan"
---

# Research — User Research & Usability Testing

Plan and execute user research from discovery through validation. This command covers the full research lifecycle: generative research (learning what to build), evaluative research (testing what you built), and everything in between.

## When to Use This

- **Starting a new product**: Generate interview guides, survey templates, recruitment plans
- **Testing a prototype**: Generate usability test scripts, task scenarios, analysis frameworks
- **Validating a live product**: Plan post-launch research, feedback collection, iteration studies

## Protocol

### Step 0: Gather Context

Before planning research, collect:

1. **What the product does**: Description, purpose, target users
2. **What questions need answering**: What assumptions are you making? What don't you know?
3. **Product stage**: Determines method selection
   - New product (no prototype) --> generative/discovery research
   - Has prototype/design --> evaluative/validation research
   - Live product --> summative research + usability testing
4. **Budget and timeline**: These directly shape the plan. $0 and 1 week produces a very different plan than $10K and 2 months
5. **Prior Sumi outputs**: Check for `/brief` (personas, constraints). Consume if available

If no prior outputs exist, ask these questions directly. Do not proceed without understanding the product and what needs to be learned.

### Step 1: Select Methods (2-4, Not Everything)

Based on product stage and research questions, recommend the right methods.

**Generative (discovery) -- when you don't know what to build:**
- User interviews: explore mental models and motivations
- Contextual inquiry: observe users in their environment
- Diary studies: capture behavior over time
- Card sorting: discover how users categorize information
- Stakeholder interviews: align business and user needs

**Evaluative (validation) -- when you have something to test:**
- Usability testing: task-based testing with think-aloud
- A/B testing: compare two variants with real traffic
- Surveys: quantitative validation at scale
- Tree testing: validate information architecture
- First-click testing: validate navigation and layout
- Preference testing: compare design alternatives

**For each recommended method, provide**:
- Why it fits this product and these research questions
- Sample size needed (with justification)
- Time estimate (recruitment + execution + analysis)
- Tools (free and paid options)
- What it will and will not tell you

### Step 2: Generate Interview Guide

If interviews are recommended:

**Screening questions (5-7)**:
- Filter for the right participants
- Mix behavioral and demographic criteria
- Include at least one disqualifier to catch professional survey-takers

**Interview script structure**:

1. **Warm-up** (3-5 min): Build rapport, set expectations, get consent for recording
2. **Context questions** (5-7 min): Understand the participant's world, habits, current tools
3. **Core questions** (15-20 min): Organized by research objective, open-ended, non-leading
4. **Probing follow-ups**: For each core question, 2-3 follow-up probes ("Tell me more about that", "What happened next?", "Why was that important to you?")
5. **Tasks to observe** (if contextual inquiry): Specific actions to watch
6. **Wrap-up** (3-5 min): Anything missed, referral request, incentive delivery

Rules:
- Open-ended questions only (never yes/no)
- Non-leading questions only (never "Don't you think X is hard?")
- Organize by research objective, not by topic
- Include transition phrases between sections

### Step 3: Generate Survey Template

If surveys are recommended:

**Survey structure**:
1. **Introduction**: Purpose, estimated time, privacy notice
2. **Screener** (2-3 questions): Confirm participant qualifies
3. **Core questions** (10-15): Organized by research objective
4. **Demographics** (3-5): Only what's needed, always optional
5. **Close**: Thank you, next steps, incentive info

**Question types**:
- Likert scales (5 or 7-point, consistent)
- Multiple choice (exhaustive options + "Other")
- Rating scales (with clear anchors)
- Open-ended (max 2-3, place at end)
- SUS or UMUX-Lite for usability measurement

Rules:
- Target under 5 minutes completion time
- Front-load important questions (dropout increases with length)
- No double-barreled questions
- Include distribution strategy (where to find respondents)

### Step 4: Generate Usability Test Plan

If the product has something testable (prototype, live product):

**Test objectives**:
- Primary research questions (max 3-5)
- Hypotheses to validate/invalidate
- Success metrics: task completion rate, time on task, error rate, satisfaction
- Decision framework: what changes based on results?

**Task scenarios (3-5 tasks)**:

For each:
- **Scenario context** -- a realistic situation, not instructions
  - GOOD: "You want to send $50 to your friend Alex for dinner last night."
  - BAD: "Click the Send Money button and enter an amount."
- **Success criteria**: what constitutes completion
- **Expected time**: baseline for comparison
- **Watch for**: critical decision points and expected failure points
- **Probing questions**: what to ask if user takes unexpected path

Task order: warm-up task first, escalate complexity, most critical flow last.

**Moderator script**:

- **Introduction** (5 min): Consent, think-aloud protocol, reassurance ("We're testing the product, not you")
- **Pre-test questions** (5 min): Current behavior, prior experience, expectations
- **Task administration** (25-35 min): Read scenario verbatim, observe silently, note-taking cues
- **Post-task questions** after each task (2 min): SEQ ("How easy or difficult was that?" 1-7), "What did you expect?", "Was anything confusing?"
- **Post-test questions** (10 min): SUS (10 questions), most frustrating part, most positive part, comparison to alternatives, one thing to change
- **Debrief** (2 min): Thank participant, explain next steps

### Step 5: Recruitment Plan

**Participant profile**:
- Maps to persona from `/brief` if available
- Behavioral criteria over demographic criteria
- Include and exclude criteria

**Sample size**:
- Interviews: 5-8 for usability issues (Nielsen/Landauer), 12-20 for behavioral patterns
- Surveys: 30 minimum for directional data, 100+ for statistical significance
- Usability testing: 5 per round (iterative rounds preferred over one large study)
- Justify the number -- no arbitrary ranges

**Channels**:
- Existing users: email, in-app intercept
- Panels: UserTesting, Respondent.io, Prolific, UserInterviews
- Social media: targeted posts in relevant communities
- Guerrilla: coffee shops, co-working spaces (for quick tests)
- Internal: friends-and-family for very early concepts (with bias acknowledgment)

**Incentives**: $50-100/hr for general consumers, $150-300/hr for professionals/B2B

**Timeline**: Week-by-week schedule from recruitment start to analysis complete

### Step 6: Analysis Framework

**Synthesis methods**:
- Affinity mapping: cluster observations into themes
- Thematic analysis: code transcripts, identify patterns
- Jobs-to-be-done: extract user jobs, pains, gains
- Insight cards: one insight per card (observation + implication + opportunity)

**For usability tests -- severity ratings**:

| Level | Name | Definition | Action |
|-------|------|------------|--------|
| 4 | Critical | Prevents task completion | Fix before launch |
| 3 | Serious | Significant delay/frustration | Fix in current cycle |
| 2 | Minor | Slight hesitation | Fix in next cycle |
| 1 | Cosmetic | Noticed, no impact | Backlog |

**Rainbow spreadsheet** (for usability tests):
- Rows: observations and quotes
- Columns: Participant 1, 2, 3, 4, 5
- Color-coded by participant for pattern spotting
- Grouped by task

**Metrics dashboard template**:
- Per-task: completion rate, average time, error count, SEQ score
- Overall: SUS score, task success rate, critical error rate
- Benchmarks: compare against industry averages or prior tests

**Report structure**:
1. Executive summary (1 page -- findings + recommendations)
2. Methodology (participants, tasks, setup)
3. Findings per task (observations, metrics, severity, quotes)
4. Cross-cutting themes
5. Prioritized recommendations (with effort estimates)
6. Raw data appendix

**How findings feed forward into Sumi commands**:
- `/style` -- Research informs visual direction (user expectations, mental models)
- `/map` -- Research informs information architecture (how users think about content)
- `/screen` -- Research informs layout priorities (what matters most to users)
- `/roast` -- Test findings provide evidence for critique

## Output Format

```
## Research Plan: [Product Name]

### Research Objectives
[Numbered list of what we need to learn]

### Recommended Methods

| Method | Type | Why It Fits | Sample Size | Time | Tools |
|--------|------|-------------|-------------|------|-------|
| [method] | [generative/evaluative] | [reason] | [N + justification] | [weeks] | [tools] |

### Interview Guide (if applicable)

#### Screening Questions
[5-7 screening questions with pass/fail criteria]

#### Interview Script
**Warm-up (3-5 min)**
[Questions]

**Context (5-7 min)**
[Questions]

**Core Questions -- Objective 1: [Name]**
[Open-ended questions with probing follow-ups]

**Core Questions -- Objective 2: [Name]**
[Open-ended questions with probing follow-ups]

**Wrap-up (3-5 min)**
[Questions]

### Survey Template (if applicable)
**Estimated completion time**: [X] minutes
[Full survey with questions, answer options, logic]

### Usability Test Plan (if applicable)

#### Test Objectives
[Research questions, hypotheses, success metrics, decision framework]

#### Task Scenarios
**Task 1: [Name]**
- Scenario: "[Realistic situation]"
- Success criteria: [what constitutes completion]
- Expected time: [X minutes]
- Watch for: [critical paths and failure points]

[Continue for 3-5 tasks]

#### Moderator Script
[Complete script: intro, pre-test, tasks, post-task, post-test, debrief]

#### Setup & Logistics
- Environment: [remote/in-person]
- Recording: [screen + audio + face]
- Tools: [tracking, notes, observer guide]
- Roles: [moderator, note-taker, observer]
- Pilot test: [plan for internal dry run]

### Recruitment Plan
| Element | Detail |
|---------|--------|
| Profile | [behavioral + demographic criteria] |
| Sample size | [N with justification] |
| Channels | [specific channels with expected yield] |
| Screening | [pass/fail criteria] |
| Incentive | [$X per session] |
| Timeline | [week-by-week] |

### Analysis Framework
[Synthesis method, severity ratings, deliverable templates]

### Next Steps
1. Run the research using this plan
2. `/style` -- Visual direction informed by research
3. `/benchmark` -- Study competitors while research is in progress
4. `/map` -- Information architecture informed by findings
```

## Quality Gates

The output MUST include:
- [ ] Methods selected with rationale (not a generic list)
- [ ] Methods match product stage (generative for new, evaluative for existing)
- [ ] Sample sizes justified with methodology
- [ ] If interviews: non-leading, open-ended questions organized by objective
- [ ] If usability test: task scenarios as realistic situations, not instructions
- [ ] If usability test: complete moderator script with think-aloud protocol
- [ ] Recruitment plan with specific channels, criteria, and incentives
- [ ] Analysis framework with deliverable templates
- [ ] Clear connection to next Sumi commands

The output MUST NOT include:
- Generic method descriptions copied from a textbook
- Leading or yes/no interview questions
- Arbitrary sample sizes without justification
- Task scenarios written as instructions ("Click X, then Y")
- Surveys longer than 5 minutes estimated completion

## Cross-References

When planning research, draw knowledge from:
- `ux-research-methods` skill -- primary knowledge source for methods, sampling, analysis
- `ux-metrics-measurement` skill -- SUS, UMUX-Lite, SEQ, task success metrics, benchmarks
- `cognitive-psychology-ux` skill -- bias awareness (confirmation bias, leading questions, social desirability)
- `ux-process-workflow` skill -- where research fits in the design process
- `ux-ethics-content-strategy` skill -- informed consent, privacy, ethical research practices
- `screen-flow-patterns` skill -- identifying key flows to test

## Next Step

**Next** --> `/style` -- Visual direction informed by research findings

**Alternatives**:
- `/benchmark` -- Study competitors while research is in progress (can run in parallel)
- `/map` -- Information architecture if findings are ready
- `/sumi` -- See the full command map
