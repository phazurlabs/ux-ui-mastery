# Pitch Presentation Templates — Design Presentations That Persuade

## Presentation Design Philosophy

A design presentation is not a document read aloud. It is a structured argument delivered through a combination of visuals, narrative, and data. The slides support the story; they do not replace it. Every slide should pass the "So what?" test: if a stakeholder cannot immediately understand why this slide matters to them, it does not belong in the deck.

### Core Principles for Design Presentations

**One idea per slide.** The moment a slide contains two competing ideas, comprehension drops. Split complex slides into sequences. A slide that shows the user flow AND the usability test results is doing too much. Show the flow, then show what testing revealed about it.

**Visual hierarchy mirrors importance.** The most important element on each slide should be the largest and most prominent. If the key finding is "73% of users failed the task," that number should be 72pt type, not a bullet point in 14pt body copy.

**Data before opinion.** Lead with what you found (data, quotes, observations), then present your interpretation. Stakeholders trust conclusions they can trace back to evidence. "We recommend X" is weak. "Based on [data], we recommend X because [reasoning]" is strong.

**Progressive disclosure.** Build complexity gradually. Start with the big picture, then zoom into details. If you start with details, stakeholders lose the forest for the trees. The first third of any presentation should orient the audience to the problem space before showing any design work.

**Anticipate objections.** For every significant recommendation, prepare a slide that addresses the most likely objection. If you recommend removing a feature that a VP championed, have the data ready. If you propose an unconventional interaction pattern, have the usability test results that validate it.

### Slide Design Rules for Design Presentations

**Minimal text.** Aim for fewer than 25 words per slide. If you need more text, you need more slides. Presentations are not documents.

**High-quality visuals.** Every design screenshot should be crisp, properly scaled, and shown in context (device mockups, browser frames, environment photos). A pixelated screenshot undermines the credibility of the design it shows.

**Consistent visual language.** Use a consistent color palette, typography, and layout grid across all slides. The presentation itself is a design artifact that signals your design standards.

**White space is confidence.** Crowded slides signal that the presenter is not sure what is important. Generous white space signals clarity and control.

**Annotation over explanation.** Instead of a paragraph describing a design decision, annotate the design screenshot directly with numbered callouts. Visual annotation is faster to parse and easier to reference in discussion.

---

## Template 1: Design Review Presentation

Use this template for regular design review meetings where you present work in progress to stakeholders for feedback and approval.

```
DESIGN REVIEW — [Project Name]
[Date] | [Phase/Sprint/Iteration]
Presented by: [Name]

═══════════════════════════════════════════════════════════════

SLIDE 1: AGENDA + CONTEXT
──────────────────────────
Title: "Design Review — [Phase Name]"

Content:
- Where we are in the project timeline [visual progress bar]
- What we are reviewing today (3-4 bullet points)
- What decisions we need from this session
- Reminder: Focus on [specific feedback needed], not [what to defer]

Speaker Notes:
"Today we are reviewing [deliverables]. We need decisions on [specific
items]. Please hold feedback on [visual polish / copy / etc.] for the
next review — today is about [structure / flow / concept]."

═══════════════════════════════════════════════════════════════

SLIDE 2: RECAP — WHERE WE LEFT OFF
────────────────────────────────────
Title: "Last Review: Decisions Made"

Content:
- Decision 1: [What was decided] ✓
- Decision 2: [What was decided] ✓
- Open item: [What was tabled for today]

Purpose: Prevent re-litigating settled decisions. Written record
of what was agreed creates accountability.

═══════════════════════════════════════════════════════════════

SLIDE 3: RESEARCH UPDATE (if applicable)
─────────────────────────────────────────
Title: "What We Learned Since Last Review"

Content:
- [Key finding 1 with data]
- [Key finding 2 with data]
- [How this informs what we are about to show]

Purpose: Ground the design work in evidence before showing it.

═══════════════════════════════════════════════════════════════

SLIDES 4-8: DESIGN WORK (core of the review)
──────────────────────────────────────────────
For each design element being reviewed:

Slide Structure:
[Top]: Context — "This is the [screen/flow/component] for [use case]"
[Center]: Design visual (large, annotated)
[Bottom]: Key design decisions made and rationale

Annotation Format:
① [Design decision 1 — e.g., "Primary CTA placed above the fold
   based on scroll depth data showing 68% of users don't scroll"]
② [Design decision 2 — e.g., "Error states shown inline rather
   than in a modal, based on testing that showed users missed
   modal error messages on mobile"]
③ [Design decision 3]

═══════════════════════════════════════════════════════════════

SLIDE 9: ALTERNATIVES CONSIDERED
─────────────────────────────────
Title: "Options We Explored"

Content:
- Option A: [Visual + brief description + why not chosen]
- Option B: [Visual + brief description + why not chosen]
- Recommended: [Visual + brief description + why chosen]

Purpose: Shows rigor. Demonstrates that the recommended direction
was selected deliberately, not by default.

═══════════════════════════════════════════════════════════════

SLIDE 10: OPEN QUESTIONS
─────────────────────────
Title: "Decisions Needed"

Content:
1. [Specific question requiring a decision]
   Option A: [Description]
   Option B: [Description]
   Recommendation: [Your recommendation + rationale]

2. [Second question]
   [Same format]

Purpose: Structure the discussion. Prevents the meeting from
devolving into unfocused brainstorming.

═══════════════════════════════════════════════════════════════

SLIDE 11: NEXT STEPS
─────────────────────
Title: "What Happens Next"

Content:
- Decisions made today: [Will be documented and shared by EOD]
- Next milestone: [What + when]
- What we need from you: [Specific client/stakeholder actions]
- Next review: [Date + what will be presented]

═══════════════════════════════════════════════════════════════
```

---

## Template 2: Stakeholder Presentation — Pitching a Design Direction

Use this for presenting a strategic design direction to leadership or cross-functional stakeholders who need to approve the approach.

```
═══════════════════════════════════════════════════════════════
[PROJECT NAME] — Design Direction
[Date]
[Your Name / Team]
═══════════════════════════════════════════════════════════════

SECTION 1: THE OPPORTUNITY (Slides 1-4)
───────────────────────────────────────

Slide 1: The Hook
Title: [Provocative statement or key metric]
e.g., "We are losing $2.4M annually to a checkout flow designed
in 2019."
Visual: Single powerful data point, large typography
Purpose: Capture attention and establish stakes

Slide 2: Business Context
Title: "Where We Are"
Content:
- Current business metrics relevant to this initiative
- Market trends affecting the opportunity
- Competitive pressure or advantage at stake
Visual: Data visualization or competitive landscape map
Purpose: Frame the design initiative in business terms

Slide 3: User Context
Title: "What Our Users Are Telling Us"
Content:
- [X] key user pain points with supporting data
- Direct user quotes (2-3 compelling quotes)
- Behavioral data showing friction points
Visual: User journey map highlighting pain points or quote cards
Purpose: Build empathy and ground the direction in user evidence

Slide 4: The Gap
Title: "The Opportunity"
Content: Clear statement of the gap between current state and
desired state, quantified wherever possible
Visual: Before/after framework or gap analysis
Purpose: Define the problem space the design direction addresses

SECTION 2: THE DIRECTION (Slides 5-10)
──────────────────────────────────────

Slide 5: Design Principles
Title: "Our Design Principles for This Initiative"
Content:
- Principle 1: [Name] — [One-sentence description]
- Principle 2: [Name] — [One-sentence description]
- Principle 3: [Name] — [One-sentence description]
Purpose: Establish the evaluative framework before showing design.
Stakeholders should judge the design against these principles.

Slide 6: Strategic Overview
Title: "The Approach"
Content: High-level summary of the design direction in 3-4 points
Visual: Conceptual diagram or experience map
Purpose: Orient stakeholders to the big picture before details

Slides 7-9: Key Design Moves (one per slide)
Title: "[Design Move Name]"
Content:
- What: [Description of the design change]
- Why: [Evidence supporting this direction — research data, metrics]
- Impact: [Expected business/user outcome]
Visual: Design mockup with annotations
Purpose: Each major design decision gets its own slide with full
context and rationale

Slide 10: Experience Walkthrough
Title: "The Experience"
Content: Interactive prototype walkthrough or screen-by-screen flow
Visual: Prototype demonstration (live or video)
Purpose: Show the design in motion, not just as static screens

SECTION 3: VALIDATION (Slides 11-13)
─────────────────────────────────────

Slide 11: What We Tested
Title: "Validation Results"
Content:
- Testing method and participant profile
- Key metrics from testing
- Confidence level in the direction
Visual: Test results summary with metrics
Purpose: Prove the direction works with evidence

Slide 12: Risk Assessment
Title: "Risks and Mitigations"
Content:
┌─────────────────┬──────────┬─────────────────────┐
│ Risk            │ Severity │ Mitigation          │
├─────────────────┼──────────┼─────────────────────┤
│ [Risk 1]        │ [H/M/L]  │ [Mitigation plan]   │
│ [Risk 2]        │ [H/M/L]  │ [Mitigation plan]   │
│ [Risk 3]        │ [H/M/L]  │ [Mitigation plan]   │
└─────────────────┴──────────┴─────────────────────┘
Purpose: Anticipate objections and demonstrate thorough thinking

Slide 13: What We Still Need to Learn
Title: "Open Questions"
Content: Honest list of unknowns and the plan to address them
Purpose: Transparency builds trust. Pretending you have all
the answers undermines credibility.

SECTION 4: THE ASK (Slides 14-15)
─────────────────────────────────

Slide 14: Investment Required
Title: "What It Takes"
Content:
- Timeline: [Duration with key milestones]
- Resources: [Team composition]
- Budget: [If applicable]
- Dependencies: [What must happen for success]
Purpose: Clear resource request tied to expected outcomes

Slide 15: The Decision
Title: "The Ask"
Content:
"We are requesting approval to proceed with [direction] based on
[evidence summary]. The expected impact is [outcome]. Next step
is [specific action] by [date]."
Purpose: End with a clear, specific ask. No ambiguity.

═══════════════════════════════════════════════════════════════
```

---

## Template 3: Design Sprint Results Presentation

Use this after a design sprint to share what was learned and recommend next steps.

```
═══════════════════════════════════════════════════════════════
DESIGN SPRINT RESULTS
[Sprint Theme / Challenge Statement]
[Date Range: Monday-Friday]
═══════════════════════════════════════════════════════════════

Slide 1: Sprint Overview
Title: "What We Did This Week"
Content:
- Sprint challenge: [The question we set out to answer]
- Team: [Participants and roles]
- Method: [Brief description of sprint structure]
- Prototype tested with [X] users on [day]

Slide 2: The Challenge We Tackled
Title: "[Challenge Statement]"
Content: 2-3 sentences framing the challenge
Visual: The challenge mapped against business goals
Notes: Include the specific decision or question the sprint
was designed to answer

Slide 3: Monday — Map + Ask Experts
Title: "Understanding the Problem"
Content:
- Long-term goal: [What we defined as success]
- Sprint questions: [The questions we set out to answer]
- Expert insights: [Key learnings from expert interviews]
Visual: Photo of the sprint map
Purpose: Show the foundation of the sprint

Slide 4: Tuesday — Sketch Solutions
Title: "Ideas Generated"
Content:
- [X] individual solutions sketched
- Key themes that emerged across solutions
- [X] strongest concepts selected for prototyping
Visual: Anonymized sketches or concept descriptions
Purpose: Demonstrate breadth of exploration

Slide 5: Wednesday — Decide
Title: "What We Chose to Test"
Content:
- Selected concept: [Description]
- Why this concept: [Criteria used for selection]
- Storyboard: [Visual of the user flow to prototype]
Visual: The storyboard
Purpose: Show the selection rationale

Slide 6: Thursday — Prototype
Title: "What We Built"
Content:
- Prototype fidelity: [Description of what was prototyped]
- Key assumptions embedded in the prototype
Visual: Screenshots of the prototype
Purpose: Show the test artifact

Slides 7-9: Friday — Test Results
Title: "What We Learned"

Per user pattern format:
┌────────────────────────┬────────┬────────┬────────┬────────┬────────┐
│ Observation            │ User 1 │ User 2 │ User 3 │ User 4 │ User 5 │
├────────────────────────┼────────┼────────┼────────┼────────┼────────┤
│ [Pattern 1]            │   ✓    │   ✓    │   ✓    │   ✗    │   ✓    │
│ [Pattern 2]            │   ✓    │   ✗    │   ✓    │   ✓    │   ✓    │
│ [Pattern 3]            │   ✗    │   ✗    │   ✓    │   ✗    │   ✗    │
└────────────────────────┴────────┴────────┴────────┴────────┴────────┘

Key Findings:
1. [Finding with evidence — e.g., "4 of 5 users completed the core
   task without assistance, validating the primary concept"]
2. [Finding — e.g., "3 of 5 users missed the secondary navigation,
   indicating the information architecture needs revision"]
3. [Finding — e.g., "All 5 users expressed surprise at the pricing
   page, suggesting our framing needs work"]

Strongest Quotes:
"[Powerful user quote]" — User [X]
"[Another revealing quote]" — User [X]

Slide 10: Sprint Questions — Answered
Title: "Answers to Our Sprint Questions"
Content:
- Q1: [Question] → [Answer, with confidence level]
- Q2: [Question] → [Answer, with confidence level]
- Q3: [Question] → [Partially answered / needs more research]

Slide 11: Recommendations
Title: "What We Recommend"
Content:
1. [Recommendation 1 — e.g., "Proceed with the core concept.
   Validated with 4/5 users. Ready for detailed design."]
2. [Recommendation 2 — e.g., "Revise the navigation before
   proceeding. Run a follow-up test with the revised IA."]
3. [Recommendation 3 — e.g., "Conduct pricing research before
   finalizing the business model presentation."]

Slide 12: Next Steps
Title: "What Happens Next"
Content:
- Immediate: [Actions for the next 1-2 weeks]
- Short-term: [Actions for the next month]
- Decision needed: [What stakeholders need to decide and by when]

═══════════════════════════════════════════════════════════════
```

---

## Template 4: Competitive Analysis Presentation

```
═══════════════════════════════════════════════════════════════
COMPETITIVE UX ANALYSIS
[Product Category / Market]
[Date]
═══════════════════════════════════════════════════════════════

Slide 1: Analysis Overview
Title: "Competitive Landscape — [Category]"
Content:
- [X] competitors analyzed
- Analysis dimensions: [list — e.g., onboarding, core workflow,
  mobile experience, accessibility, design system maturity]
- Method: [Heuristic evaluation + user flow analysis + feature
  comparison]

Slide 2: Competitive Positioning Map
Title: "Where We Stand"
Visual: 2x2 matrix plotting competitors on relevant axes
e.g., X-axis: Simplicity ←→ Power
      Y-axis: Consumer ←→ Enterprise
Purpose: Visual overview of competitive positioning

Slides 3-7: Per-Competitor Deep Dive (1 slide each)
Title: "[Competitor Name]"
Content:
- Strengths: [2-3 UX strengths with screenshots]
- Weaknesses: [2-3 UX weaknesses with screenshots]
- Notable pattern: [Something worth learning from]
- Threat level: [High / Medium / Low — and why]
Visual: Annotated screenshots of key screens

Slide 8: Feature Comparison Matrix
Title: "Feature Comparison"
Content:
┌──────────────────┬─────┬──────┬──────┬──────┬──────┐
│ Feature          │ Us  │ Comp │ Comp │ Comp │ Comp │
│                  │     │ A    │ B    │ C    │ D    │
├──────────────────┼─────┼──────┼──────┼──────┼──────┤
│ [Feature 1]      │ ●   │ ●    │ ○    │ ●    │ ◐    │
│ [Feature 2]      │ ○   │ ●    │ ●    │ ○    │ ●    │
│ [Feature 3]      │ ◐   │ ○    │ ●    │ ●    │ ○    │
│ [Feature 4]      │ ●   │ ◐    │ ○    │ ●    │ ●    │
└──────────────────┴─────┴──────┴──────┴──────┴──────┘
● Full support  ◐ Partial  ○ Missing

Slide 9: UX Quality Comparison
Title: "Experience Quality Scorecard"
Content: Radar chart or scoring matrix comparing UX quality
across dimensions (usability, visual design, performance,
accessibility, onboarding, error handling)

Slide 10: Patterns Worth Stealing
Title: "Best Practices from the Market"
Content:
- Pattern 1: [Description + which competitor does it best + screenshot]
- Pattern 2: [Description + source + screenshot]
- Pattern 3: [Description + source + screenshot]
Purpose: Actionable takeaways for our product

Slide 11: Our Differentiation Opportunity
Title: "Where We Can Win"
Content:
- Gap 1: [Something no competitor does well — our opportunity]
- Gap 2: [Underserved user need in the market]
- Gap 3: [UX quality gap we can exploit]
Purpose: Connect the analysis to our product strategy

Slide 12: Recommendations
Title: "What This Means for Us"
Content: Prioritized list of recommendations based on competitive
analysis, framed as opportunities rather than deficiencies

═══════════════════════════════════════════════════════════════
```

---

## Template 5: User Research Findings Presentation

```
═══════════════════════════════════════════════════════════════
USER RESEARCH FINDINGS
[Study Name / Research Question]
[Date]
═══════════════════════════════════════════════════════════════

Slide 1: Research Overview
Title: "[Research Question in Plain Language]"
Content:
- Method: [Interview / Survey / Usability Test / Diary Study / etc.]
- Participants: [X] participants matching [criteria]
- Duration: [Dates of data collection]
- Conducted by: [Researcher name]

Slide 2: Why This Research
Title: "The Question We Needed to Answer"
Content:
- Business context: [Why this research was prioritized]
- What we assumed: [Hypotheses going in]
- What we did not know: [Specific unknowns]
Purpose: Frame the research in terms stakeholders care about

Slide 3: Methodology
Title: "How We Studied This"
Content:
- [Brief methodology description]
- Participant breakdown: [Demographics, segments, recruitment]
- Analysis approach: [How data was synthesized]
Visual: Participant profile summary (not individual names)
Purpose: Establish methodological credibility

Slides 4-8: Key Findings (one per slide)
Title: "Finding [X]: [Finding Statement]"
Content:
- Evidence: [Specific data supporting this finding]
  - [X] of [X] participants exhibited this behavior
  - [Relevant survey percentage]
  - [Behavioral data from analytics]
- User voice: "[Direct quote that illustrates the finding]"
  — [Participant descriptor, not name]
- Implication: [What this means for design/product decisions]
Visual: Supporting artifact (clip reference, data visualization,
behavior map, or annotated screenshot)

Each finding slide follows the same structure:
1. The finding (clear, specific statement)
2. The evidence (data that supports it)
3. The user voice (humanizing quote)
4. The implication (what to do about it)

Slide 9: Themes and Patterns
Title: "What It All Means"
Content:
- Theme 1: [Overarching theme connecting multiple findings]
- Theme 2: [Second theme]
- Theme 3: [Third theme]
Visual: Thematic map or framework showing how findings relate
Purpose: Synthesize individual findings into actionable themes

Slide 10: Personas (if applicable)
Title: "Who We Are Designing For"
Content: [X] persona cards with:
- Name and representative image
- Key motivations
- Key frustrations
- Behavioral patterns
- Quotes
Purpose: Make research findings tangible and memorable

Slide 11: Recommendations
Title: "What We Should Do"
Content:
Priority 1 (Immediate):
- [Recommendation linked to Finding X]
- [Recommendation linked to Finding Y]

Priority 2 (Next Quarter):
- [Recommendation linked to Finding Z]

Priority 3 (Explore Further):
- [Area that needs more research]

Slide 12: Next Steps
Title: "The Path Forward"
Content:
- Decisions needed: [What stakeholders must decide]
- Follow-up research: [What questions remain unanswered]
- Design implications: [What the design team will do with these findings]
- Report: [Full research report will be shared by DATE]

═══════════════════════════════════════════════════════════════
```

---

## Template 6: Design System Pitch Presentation

Use this to convince leadership to invest in building a design system.

```
═══════════════════════════════════════════════════════════════
THE CASE FOR A DESIGN SYSTEM
[Company Name]
[Date]
═══════════════════════════════════════════════════════════════

Slide 1: The Problem in One Image
Title: [None — let the visual speak]
Visual: Screenshot collage showing the same UI element (button,
form, card) designed [X] different ways across [X] products
Purpose: Visceral demonstration of the inconsistency problem

Slide 2: The Cost of Inconsistency
Title: "What This Is Costing Us"
Content:
- Developer hours spent rebuilding common components: [X] hrs/quarter
- Design QA issues per sprint: [X] average
- Accessibility compliance: [X]% of components passing WCAG AA
- Designer onboarding time: [X] weeks before productive
- User confusion: [X] different button styles, [X] form patterns
Visual: Cost calculation or impact metrics
Purpose: Translate the design problem into business terms

Slide 3: The Audit
Title: "What We Found"
Content:
- [X] unique color values (should be [X])
- [X] unique font sizes (should be [X])
- [X] button variations (should be [X])
- [X] form input patterns (should be [X])
Visual: Audit visualization — color swatches, component collage
Purpose: Quantify the problem

Slide 4: What Industry Leaders Do
Title: "Design Systems at Scale"
Content:
- [Company A]: [System name] — [X] products, [X]% consistency
- [Company B]: [System name] — [impact metric]
- [Company C]: [System name] — [efficiency metric]
- Industry average ROI: [X]:1 within [X] years
Purpose: Social proof and benchmarking

Slide 5: The Vision
Title: "One System, [X] Products"
Content:
- Single source of truth for design decisions
- Shared component library across all products
- Consistent user experience across touchpoints
- Built-in accessibility compliance
Visual: Before/after vision showing current fragmentation vs.
unified system
Purpose: Paint the aspirational future

Slide 6: What We Would Build
Title: "The Design System Roadmap"
Content:
Phase 1 (Months 1-2): Foundation — tokens, core components
Phase 2 (Months 2-4): Component Library — [X]+ components
Phase 3 (Months 4-5): Patterns + Documentation
Phase 4 (Months 5-6): Adoption + Training
Visual: Roadmap timeline
Purpose: Make the initiative feel achievable and structured

Slide 7: Expected Impact
Title: "What We Gain"
Content:
- [X]% reduction in component development time
- [X]% improvement in visual consistency
- WCAG AA compliance built into every component
- Designer onboarding: [X] weeks → [X] days
- Developer onboarding: [X] weeks → [X] days
Purpose: Quantified benefits that justify the investment

Slide 8: The Investment
Title: "What It Takes"
Content:
- Team: [X] designers, [X] developers for [X] months
- OR: External engagement at $[XXX,XXX]
- Ongoing: [X] designer + [X] developer for maintenance
- ROI breakeven: [X] months
Purpose: Clear resource request

Slide 9: The Ask
Title: "The Decision"
Content:
"We are requesting [specific resources] to build a design system
that will [specific impact]. The first usable components will be
available in [timeframe]. Full ROI is expected within [timeframe]."
Purpose: Clear, specific, actionable ask

═══════════════════════════════════════════════════════════════
```

---

## Storytelling Framework for Design Presentations

### The Situation-Complication-Resolution (SCR) Framework

Every effective design presentation follows some version of this narrative arc:

**Situation:** Establish the current state. What is the context? What does the audience already know? What are the shared facts? This grounds the audience and creates common understanding.

**Complication:** Introduce the tension. What is wrong? What changed? What is at risk? This creates the "why now" urgency that motivates action. Use data, user quotes, and competitive evidence to make the complication tangible.

**Resolution:** Present the design direction as the answer to the complication. The resolution should feel like a natural, evidence-backed response to the problem, not a predetermined conclusion looking for justification.

### Data Visualization in Design Presentations

**Use the right chart for the message:**
- Comparison: Bar chart (vertical for categories, horizontal for ranking)
- Trend over time: Line chart
- Part-to-whole: Donut chart (not pie — donut has better readability)
- Distribution: Histogram
- Correlation: Scatter plot
- Before/after: Side-by-side bars or connected dot plot

**Color in data visualization:**
- Use semantic color consistently (green = positive, red = negative)
- Limit to 3-4 colors per chart
- Highlight the key data point; gray out the rest
- Ensure sufficient contrast for projector environments (low-contrast rooms)

**Annotation is essential:**
- Label the key data point directly on the chart
- Add a sentence of context as a subtitle: not "Monthly Active Users" but "Monthly Active Users — 23% increase since redesign launch"
- Call out the specific number the audience should remember

### Handling Q&A in Design Presentations

**Prepare backup slides.** For every recommendation, have 2-3 backup slides with deeper detail, edge case handling, or alternative approaches. When a stakeholder asks "What about X?", you pull up a prepared slide rather than improvising.

**Redirect personal preference.** When a stakeholder says "I don't like the blue," redirect to user evidence: "That is useful feedback. We chose this color based on [accessibility contrast requirements / brand guidelines / A/B test results]. Would you like us to test an alternative in the next usability round?"

**Park future scope.** When discussion veers into adjacent topics, explicitly park the item: "Great point. That is outside the scope of today's discussion but should be addressed. I will add it to our parking lot and we can schedule a separate session for it."

**Document decisions in real time.** Have a visible note (shared screen or whiteboard) where decisions are recorded during the meeting. At the end, read back the decisions. This prevents "I thought we agreed to X" disagreements later.

### Presentation Timing Guidelines

```
15-minute presentation:
- Context/problem: 3 minutes (2-3 slides)
- Process/evidence: 4 minutes (3-4 slides)
- Solution: 5 minutes (4-5 slides)
- Ask/next steps: 3 minutes (2 slides)

30-minute presentation:
- Context/problem: 7 minutes (4-5 slides)
- Process/evidence: 8 minutes (5-7 slides)
- Solution: 10 minutes (7-10 slides)
- Ask/next steps: 5 minutes (2-3 slides)

60-minute presentation (including Q&A):
- Context/problem: 10 minutes (5-7 slides)
- Process/evidence: 15 minutes (8-12 slides)
- Solution: 15 minutes (10-15 slides)
- Ask/next steps: 5 minutes (2-3 slides)
- Q&A: 15 minutes (backup slides ready)
```

---

## Appendix: Slide Layout Patterns

### Title Slide

```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│         [PROJECT NAME]                  │
│         [Subtitle / Date]              │
│                                         │
│         [Your Name / Team]             │
│         [Company Logo]                 │
│                                         │
└─────────────────────────────────────────┘
```

### Big Number Slide

```
┌─────────────────────────────────────────┐
│                                         │
│              73%                        │
│    of users abandon the checkout        │
│    before completing their purchase     │
│                                         │
│    Source: GA4, Jan-Mar 2026            │
│                                         │
└─────────────────────────────────────────┘
```

### Split Comparison Slide

```
┌────────────────────┬────────────────────┐
│     BEFORE         │      AFTER         │
│                    │                    │
│  [Screenshot]      │  [Screenshot]      │
│                    │                    │
│  - [Pain point 1]  │  - [Improvement 1] │
│  - [Pain point 2]  │  - [Improvement 2] │
│                    │                    │
└────────────────────┴────────────────────┘
```

### Annotated Design Slide

```
┌─────────────────────────────────────────┐
│  [Title]                                │
│                                         │
│      ┌─────────────────┐               │
│   ①──│                 │──③            │
│      │  [Design        │               │
│   ②──│   Screenshot]   │               │
│      │                 │──④            │
│      └─────────────────┘               │
│                                         │
│  ① [Annotation explanation]            │
│  ② [Annotation explanation]            │
│  ③ [Annotation explanation]            │
│  ④ [Annotation explanation]            │
└─────────────────────────────────────────┘
```

### Quote Slide

```
┌─────────────────────────────────────────┐
│                                         │
│  "I spent 10 minutes trying to find     │
│   my order history. I finally just      │
│   called customer support."             │
│                                         │
│   — Research Participant 7              │
│     E-commerce Customer, Age 34         │
│                                         │
│   (3 of 5 participants expressed        │
│    similar frustration)                 │
│                                         │
└─────────────────────────────────────────┘
```

### Decision Slide

```
┌─────────────────────────────────────────┐
│  DECISION NEEDED                        │
│                                         │
│  [Question in plain language]           │
│                                         │
│  Option A: [Description]               │
│  ✓ Pro   ✗ Con                         │
│                                         │
│  Option B: [Description]               │
│  ✓ Pro   ✗ Con                         │
│                                         │
│  Recommendation: Option [X]            │
│  Reason: [One sentence]                │
│                                         │
└─────────────────────────────────────────┘
```
