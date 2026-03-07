---
description: "[1.1] Plan user research — generate interview guides, survey templates, research methods selection, participant recruitment plans, and analysis frameworks tailored to your product."
phase: "1"
phase_step: "1.1"
phase_name: "DISCOVER"
step_label: "Step 3 of 30"
---

# Research — User Research Planning Engine

Generate a complete user research plan: method selection, interview guides, survey templates, recruitment plans, and analysis frameworks — tailored to your product stage, research questions, and constraints.

## Analysis Protocol

### Step 0: Gather Context

Before planning research, collect:

1. **What the product does**: Description, purpose, target users.
2. **What questions need answering**: What don't you know about your users? What assumptions are you making?
3. **Product stage**: New product (generative/discovery research) or existing product (evaluative/validation research).
4. **Budget and time constraints**: These directly affect method selection — a $0 budget and 1 week timeline produces a very different plan than $10K and 2 months.
5. **Prior Sumi outputs**: Check for `/02-brief` (product brief, personas, constraints). Consume if available.

If the user has no prior Sumi outputs, ask the five questions above directly. Do not proceed without understanding the product and what needs to be learned.

### Step 1: SELECT METHODS

Based on the product stage and research questions, recommend the right research methods. Do not recommend everything — select 2-4 methods that fit.

**Generative (discovery) methods** — use when you don't know what to build:
- Contextual inquiry: observe users in their environment
- Diary studies: capture behavior over time
- User interviews: explore mental models and motivations
- Ethnography: deep immersion in user context
- Card sorting: discover how users categorize information
- Stakeholder interviews: align business and user needs

**Evaluative (validation) methods** — use when you have something to test:
- Usability testing: task-based testing with think-aloud
- A/B testing: compare two variants with real traffic
- Surveys: quantitative validation at scale
- Tree testing: validate information architecture
- First-click testing: validate navigation and layout
- Preference testing: compare design alternatives

**For each recommended method, provide**:
- Why it fits this product and these research questions
- Sample size needed (with justification, not arbitrary)
- Time estimate (recruitment + execution + analysis)
- Tools (free and paid options)
- What it will and will not tell you

### Step 2: GENERATE INTERVIEW GUIDE

If interviews are recommended (they usually are for generative research):

**Screening questions (5-7)**:
- Filter for the right participants
- Include a mix of behavioral and demographic criteria
- Include at least one disqualifier to catch professional survey-takers

**Interview script structure**:
1. **Warm-up** (3-5 min): Build rapport, set expectations, get consent for recording
2. **Context questions** (5-7 min): Understand the participant's world, habits, current tools
3. **Core questions** (15-20 min): Organized by research objective, open-ended, non-leading
4. **Probing follow-ups**: For each core question, provide 2-3 follow-up probes (e.g., "Tell me more about that", "What happened next?", "Why was that important to you?")
5. **Tasks to observe** (if contextual inquiry): Specific actions to watch the participant perform
6. **Wrap-up** (3-5 min): Anything we missed, referral request, incentive delivery

**You MUST**:
- Write open-ended questions (never yes/no)
- Write non-leading questions (never "Don't you think X is hard?")
- Organize questions by research objective, not by topic
- Include transition phrases between sections

### Step 3: GENERATE SURVEY TEMPLATE

If surveys are recommended (they usually are for evaluative research):

**Survey structure**:
1. **Introduction**: Purpose, estimated time, privacy notice
2. **Screener** (2-3 questions): Confirm participant qualifies
3. **Core questions** (10-15 questions): Organized by research objective
4. **Demographics** (3-5 questions): Only what's needed, always optional
5. **Close**: Thank you, next steps, incentive info

**Question types to use**:
- Likert scales (5-point or 7-point, be consistent)
- Multiple choice (exhaustive options + "Other")
- Rating scales (with clear anchors)
- Open-ended (max 2-3, place at end)
- SUS (System Usability Scale) or UMUX-Lite for usability measurement

**You MUST**:
- Target under 5 minutes completion time
- Front-load important questions (dropout increases with length)
- Avoid double-barreled questions
- Include a distribution strategy (where to find respondents, expected response rate)

### Step 4: RECRUITMENT PLAN

**Participant profile**:
- Maps to persona from `/02-brief` if available
- Behavioral criteria (what they do) over demographic criteria (who they are)
- Include and exclude criteria

**Sample size recommendation**:
- Interviews: 5-8 for usability issues (Nielsen/Landauer), 12-20 for behavioral patterns
- Surveys: minimum 30 for directional data, 100+ for statistical significance, use sample size calculator for specific confidence levels
- Usability testing: 5 per round (iterative rounds preferred over one large study)
- Justify the number — do not say "5-10 participants" without explanation

**Recruitment channels**:
- Existing users (if available): email, in-app intercept
- Panels: UserTesting, Respondent.io, Prolific, UserInterviews
- Social media: targeted posts in relevant communities
- Guerrilla: coffee shops, co-working spaces (for quick tests)
- Internal: friends-and-family for very early concepts (with bias acknowledgment)

**Screening criteria**: Specific pass/fail criteria for each channel

**Incentive recommendations**: Amount based on session length, participant type, and market rate (typically $50-100/hr for general consumers, $150-300/hr for professionals/B2B)

**Timeline**: Week-by-week schedule from recruitment start to analysis complete

### Step 5: ANALYSIS FRAMEWORK

**How to synthesize findings**:
- Affinity mapping: cluster observations into themes
- Thematic analysis: code transcripts, identify patterns
- Jobs-to-be-done: extract user jobs, pains, gains
- Insight cards: one insight per card (observation + implication + opportunity)

**Deliverable templates**:
- Research report outline (executive summary, methodology, key findings, recommendations)
- Insight prioritization matrix (impact vs. confidence)
- User needs hierarchy (must-have, should-have, nice-to-have)

**How findings feed into next Sumi commands**:
- `/04-taste` — Research informs visual direction (user expectations, mental models)
- `/08-map` — Research informs information architecture (how users think about content)
- `/09-wireframe` — Research informs layout priorities (what matters most to users)

## Output Format

```
### Phase Position
> **Phase 1: DISCOVER** | Step 3 of 30 | `/03-research`
>
> `/02-brief` → **`/03-research`** → `/04-taste`

---

## User Research Plan

### Research Objectives
[Numbered list of what we need to learn, mapped to product questions]

### Recommended Methods

| Method | Type | Why It Fits | Sample Size | Time | Tools |
|--------|------|-------------|-------------|------|-------|
| [method] | [generative/evaluative] | [specific reason] | [N with justification] | [weeks] | [tools] |

### Interview Guide (if applicable)

#### Screening Questions
[5-7 screening questions with pass/fail criteria]

#### Interview Script
**Warm-up (3-5 min)**
[Questions and rapport-building prompts]

**Context (5-7 min)**
[Background questions about participant's world]

**Core Questions — Objective 1: [Name]**
[Open-ended questions with probing follow-ups]

**Core Questions — Objective 2: [Name]**
[Open-ended questions with probing follow-ups]

**Wrap-up (3-5 min)**
[Closing questions and logistics]

### Survey Template (if applicable)

**Estimated completion time**: [X] minutes
[Full survey structure with all questions, answer options, and logic]

### Recruitment Plan

| Element | Detail |
|---------|--------|
| Participant profile | [behavioral + demographic criteria] |
| Sample size | [N with justification] |
| Channels | [specific channels with expected yield] |
| Screening criteria | [pass/fail] |
| Incentive | [$X per session] |
| Timeline | [week-by-week] |

### Analysis Framework
[Synthesis method, deliverable templates, how findings feed forward]

---

### Next Steps
1. **Conduct the research** using the plan above
2. **Then** → `/04-taste` — Generate style direction informed by research findings
3. **Or** → `/05-benchmark` — Study competitors while research is in progress

**Run `/next` to continue the journey.**
```

## Quality Gates

The output MUST include:
- [ ] Research methods selected with rationale for each (not a generic list of all methods)
- [ ] Methods match product stage (generative for new products, evaluative for existing)
- [ ] Interview guide with non-leading, open-ended questions organized by objective
- [ ] Sample size justified with methodology (not arbitrary numbers)
- [ ] Recruitment plan with specific channels, criteria, and incentives
- [ ] Analysis framework with deliverable templates
- [ ] Clear connection to next Sumi steps

The output MUST NOT include:
- Generic method descriptions copied from a textbook — every recommendation must be specific to this product
- Leading or yes/no interview questions
- Arbitrary sample sizes without justification
- Recruitment plans without specific channels
- Surveys longer than 5 minutes estimated completion

## Cross-References

When planning research, draw knowledge from:
- `ux-research-methods` skill — primary knowledge source for methods, sampling, analysis
- `ux-metrics-measurement` skill — metrics integration (SUS, UMUX-Lite, task success rate, time on task)
- `cognitive-psychology-ux` skill — bias awareness in research design (confirmation bias, leading questions, social desirability bias, anchoring)
- `ux-process-workflow` skill — where research fits in the design process
- `ux-ethics-content-strategy` skill — informed consent, privacy, ethical research practices

## Next Step

**Next** → `/04-taste` (1.2) — Generate sector-appropriate visual direction informed by research findings

**Alternatives**:
- `/05-benchmark` — Study competitors while research is in progress (can run in parallel)
- `/08-map` — Jump to information architecture if research findings are already available
- `/guide` — See the full journey map
