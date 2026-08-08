# Company UX Methodologies — Deep Dive Encyclopedia

A comprehensive breakdown of 8 industry-leading UX methodologies. Each section covers the full process, how it maps to NNG's 6 phases, and how to adapt it for AI-assisted solo/small-team development.

### Why This Matters for Builders

These aren't academic exercises. These methodologies power the products you use every day:

| Company | Methodology Result |
|---------|-------------------|
| **Airbnb** (IDEO-trained founders) | Went from nearly bankrupt to $100B by redesigning around host empathy. The "Snow White" storyboarding exercise (IDEO method) transformed their entire product. |
| **Google** (Design Sprint) | Gmail's "Undo Send" feature — born from a single Design Sprint. Tested with 5 users on Friday, shipped to 1.8B users. |
| **IBM** (EDT) | Reduced time-to-market by 75% across 50+ product teams. $20.6M annual savings from design system alignment alone. |
| **Spotify** (Squad model) | Discover Weekly — built by a single squad using Think-It/Build-It. 40M users in first year. 8,000 streams per user per year. |
| **Microsoft** (Inclusive Design) | Xbox Adaptive Controller — designed for gamers with limited mobility, became a mainstream accessibility standard. Generated $400M+ in accessible gaming revenue. |
| **Stripe** (Design Engineering) | 3 people ship Stripe Checkout (design engineer workflow). Handles $1T+ in payments. Every pixel driven by tokens. |

These companies didn't succeed despite process — they succeeded *because* of it.

---

## 1. IDEO — Human-Centered Design (HCD)

### Origin & Philosophy

IDEO, founded by David Kelley in 1991 (who also founded Stanford's d.school), pioneered the application of design thinking to business and social innovation. Their approach centers on radical empathy — going into the field, observing real humans, and designing from their perspective rather than from business requirements or technological capability.

**Core belief**: The best solutions come from deep understanding of people's needs, combined with what is technically feasible and commercially viable (the "three lenses" of HCD: Desirability, Feasibility, Viability).

### The 3-Phase Process

#### Phase 1: Inspiration

**Goal**: Immerse yourself in the lives of the people you're designing for.

**Activities**:
- **Field immersion** — Spend time in the user's environment (not a lab). If designing for nurses, shadow nurses. If designing for commuters, ride the commute.
- **Extreme users** — Interview people at the extremes of usage (heaviest users, non-users, people who've abandoned the product). Extremes reveal mainstream needs.
- **Analogous inspiration** — Study how other domains solve similar problems. Designing a hospital check-in? Study hotel check-in, airline check-in, amusement park entry.
- **Expert interviews** — Talk to domain experts who understand the systemic context.
- **Empathy exercises** — Simulate the user's experience. Use an app with your non-dominant hand. Navigate a website with a screen reader.

**Outputs**: Stories, observations, photos, quotes, empathy maps, journey maps.

#### Phase 2: Ideation

**Goal**: Synthesize what you learned and generate a breadth of solutions.

**Activities**:
- **Download** — Share everything observed with the team. No filtering. Quantity of observations matters.
- **Affinity clustering** — Group observations into themes using sticky notes or digital boards.
- **HMW questions** — Transform themes into "How Might We" opportunity statements.
- **Brainstorming** — 100+ ideas, no judgment. Build on others' ideas. Go for quantity.
- **Concept selection** — Cluster ideas, vote on promising concepts, select 2-3 to prototype.
- **Rapid prototyping** — Build the fastest possible version to make the idea tangible.

**Outputs**: HMW questions, concept sketches, rough prototypes, experience blueprints.

#### Phase 3: Implementation

**Goal**: Test prototypes, iterate, and bring the solution to market.

**Activities**:
- **User testing** — Test prototypes with real users. Observe silently. Note confusion, delight, workarounds.
- **Iterate** — Revise based on test findings. Expect 3-5 iterations.
- **Pilot** — Deploy to a small group in real conditions. Measure outcomes.
- **Scale** — Roll out with monitoring, feedback loops, and continuous improvement.

**Outputs**: Tested prototypes, pilot results, launch plan, feedback mechanisms.

### Mapping to NNG Phases

| IDEO Phase | NNG Phase | Key Activity |
|-----------|-----------|-------------|
| Inspiration | Empathize | Field immersion, extreme user interviews |
| Inspiration | Define | Observation synthesis, theme clustering |
| Ideation | Ideate | HMW brainstorming, concept generation |
| Ideation | Prototype | Rapid prototyping |
| Implementation | Test | User testing, iteration |
| Implementation | Implement | Pilot, scale, monitor |

### Adapting for AI-Assisted Development

**What stays**: The empathy work. AI cannot empathize. You must still understand your users.
**What changes**: Prototyping speed. AI generates prototypes in seconds instead of hours.
**Risk**: IDEO's strength is divergence — generating many ideas. AI tempts you to converge too early on the first generated output.

**Terminal adaptation**:
1. Empathy: Write your `/brief` problem statement before any prompting
2. Ideation: Ask AI for 3 different approaches, not just 1
3. Testing: Run Sumi audits on every AI-generated output
4. Iteration: Use `/remix` to apply findings, then re-test

---

## 2. UK Design Council — Double Diamond

### Origin & Philosophy

The British Design Council published the Double Diamond in 2005, later revised in 2019 with the "Framework for Innovation." It visualizes the design process as two diamonds: discover/define (understand the right problem) and develop/deliver (build the right solution). The diamonds represent divergent thinking (expanding possibilities) followed by convergent thinking (narrowing to decisions).

**Core belief**: Getting the problem right is as important as getting the solution right. The first diamond ensures you don't build a beautiful solution to the wrong problem.

### The 4-Phase Process

#### Phase 1: Discover (Diverge on the Problem)

**Goal**: Explore the problem space widely. Don't narrow too early.

**Activities**:
- User research (interviews, observation, surveys)
- Market research and trend analysis
- Data analysis of existing products
- Stakeholder mapping
- Literature review

**Mindset**: "We don't know what the problem is yet." Open, curious, non-judgmental.

#### Phase 2: Define (Converge on the Problem)

**Goal**: Synthesize research into a clear problem definition.

**Activities**:
- Affinity mapping
- Persona creation
- Problem statement crafting
- "How Might We" framing
- Design brief writing
- Prioritization (impact vs. effort)

**Mindset**: "This is the specific problem we're solving." Focused, decisive, evidence-based.

#### Phase 3: Develop (Diverge on the Solution)

**Goal**: Generate and explore multiple solutions to the defined problem.

**Activities**:
- Ideation workshops
- Sketching and wireframing
- Prototyping (paper, digital, code)
- Co-design with users
- Technical feasibility checks

**Mindset**: "There are many ways to solve this." Creative, experimental, collaborative.

#### Phase 4: Deliver (Converge on the Solution)

**Goal**: Test, refine, and launch the best solution.

**Activities**:
- Usability testing
- A/B testing
- Performance optimization
- Accessibility audit
- Launch planning
- Post-launch monitoring

**Mindset**: "This is the solution we're shipping." Rigorous, quality-focused, measurable.

### The 2019 Framework for Innovation Additions

The revised framework adds four enabling factors:
1. **Leadership** — Organizational support for design process
2. **Engagement** — Involving diverse stakeholders
3. **Methods** — Using appropriate design methods
4. **Culture** — Creating an environment that supports experimentation

### Mapping to NNG Phases

| Double Diamond | NNG Phase | Thinking Mode |
|---------------|-----------|--------------|
| Discover | Empathize | Divergent |
| Define | Define | Convergent |
| Develop | Ideate + Prototype | Divergent |
| Deliver | Test + Implement | Convergent |

### Adapting for AI-Assisted Development

**What stays**: The diverge/converge rhythm. This is the framework's core insight.
**What changes**: Speed of divergence. AI can generate many options quickly.
**Risk**: AI collapses both diamonds into a single convergent step. You ask one question, get one answer, and ship it.

**Terminal adaptation**:
1. Discover: `/sumi` (0.1) + research prompts — diverge on the problem
2. Define: `/brief` (0.2) — converge on the problem statement
3. Develop: `/style` + `/style` + generate 3 variations — diverge on solutions
4. Deliver: Sumi audits (`/audit`, `/a11y`, `/roast`) — converge on quality

---

## 3. Google Ventures — Design Sprint

### Origin & Philosophy

Jake Knapp developed the Design Sprint at Google Ventures (GV) in 2010, refined across 150+ sprints, and published it in *Sprint* (2016). The sprint compresses months of diverge/converge into exactly 5 days. It's designed for time-critical product decisions where the cost of being wrong is high.

**Core belief**: You can learn more from a 5-day sprint than from months of debates and meetings. Speed + structure = better decisions.

### The 5-Day Process

#### Monday: Map

**Goal**: Create a shared understanding of the problem and choose a target.

**Activities**:
- Long-term goal setting (where do we want to be in 6 months?)
- Expert interviews (20-min "Ask the Experts" sessions)
- Map the user journey from start to finish
- Choose the most critical moment to focus on
- Sprint questions: "What must be true for this to work?"

**Output**: A journey map with a circled target moment.

#### Tuesday: Sketch

**Goal**: Generate individual solutions without groupthink.

**Activities**:
- Lightning demos (15 min) — Review existing solutions in the market
- 4-step sketching process:
  1. **Notes** — 20 min reviewing research
  2. **Ideas** — 20 min rapid idea generation
  3. **Crazy 8s** — 8 variations in 8 minutes
  4. **Solution sketch** — Detailed 3-panel storyboard of best idea
- All sketching is individual (prevents groupthink)

**Output**: One detailed solution sketch per person.

#### Wednesday: Decide

**Goal**: Choose the best solution without design-by-committee.

**Activities**:
- Art museum (silent review of all sketches)
- Heat map voting (dot stickers on compelling ideas)
- Speed critique (3 min per sketch, structured discussion)
- Decider votes (the decision-maker makes the call)
- Storyboard the winning concept for prototyping

**Output**: A storyboard that the team will prototype tomorrow.

#### Thursday: Prototype

**Goal**: Build a realistic-looking prototype in one day.

**Activities**:
- Assign roles: Makers (2+), Stitcher (1), Writer (1), Asset Collector (1), Interviewer (1, prepares for Friday)
- Build a "Goldilocks" prototype — just real enough to evoke genuine reactions
- Use whatever tools are fastest (Keynote, Figma, code, video)
- The prototype should test the specific hypothesis from Monday

**Output**: A testable prototype that looks real enough for users to react naturally.

#### Friday: Test

**Goal**: Learn from real users interacting with the prototype.

**Activities**:
- 5 user interviews (1 hour each, staggered)
- Structured interview with tasks (not just showing the prototype)
- Team watches in a separate room, noting reactions on a whiteboard
- Pattern identification after all 5 interviews
- Sprint decision: iterate, pivot, or kill

**Output**: Clear patterns from 5 users, decision on next steps.

### Mapping to NNG Phases

| Sprint Day | NNG Phase | Duration |
|-----------|-----------|----------|
| Monday: Map | Empathize + Define | 1 day |
| Tuesday: Sketch | Ideate | 1 day |
| Wednesday: Decide | Define (converge on solution) | 1 day |
| Thursday: Prototype | Prototype | 1 day |
| Friday: Test | Test | 1 day |
| (Post-sprint) | Implement | Following weeks |

### Adapting for AI-Assisted Development

**What stays**: The time-boxing and the Friday test. Speed without testing is just rushing.
**What changes**: Thursday (Prototype) drops from a full day to hours with AI generation.
**Risk**: The temptation to skip Monday-Wednesday and jump straight to AI-generated prototypes.

**Terminal adaptation — Solo Dev Sprint (2 hours)**:
1. Map (15 min): Write user journey, circle the critical moment, define sprint questions
2. Sketch (15 min): `/style` for patterns + sketch 3 approaches in notes
3. Decide (10 min): Pick the best approach based on user needs
4. Prototype (40 min): `/tokens` + `/screen` or `/component` — AI-generate the prototype
5. Test (40 min): `/audit` + `/a11y` + `/audit` — simulate user testing

---

## 4. IBM — Enterprise Design Thinking (EDT)

### Origin & Philosophy

IBM adopted design thinking in 2012, adapting it for enterprise-scale challenges where projects involve hundreds of stakeholders across global teams. Phil Gilbert led the transformation, scaling from 100 designers to 1,600+ across IBM. EDT adds three practices unique to large-organization design.

**Core belief**: Design thinking scales across enterprises when you add the right scaffolding — Hills for alignment, Playbacks for transparency, and Sponsor Users for continuous grounding.

### The Framework

EDT uses the same diverge/converge loop (Observe → Reflect → Make) but adds three key practices:

#### The Loop: Observe → Reflect → Make

**Observe**: Immerse in the user's world. Watch, listen, and engage with empathy.
**Reflect**: Synthesize observations. What patterns emerge? What surprises?
**Make**: Externalize ideas. Build something to test and learn from.

This loop runs continuously — it's not a linear process but a constant cycle.

#### Key Practice 1: Hills

**What**: Statement of intent written as user outcomes, not system requirements.
**Format**: "A [user] can [do something meaningful] in [a specific, measurable way]"
**Example**: "A nurse can access a patient's full medication history in under 10 seconds without leaving the current screen."

**Why it matters**: Hills align entire organizations around user outcomes instead of feature checklists. They're measurable, testable, and user-focused.

**Rules**:
- Maximum 3 Hills per project (forces focus)
- Must be achievable within the current release
- Must be testable with real users
- Written from the user's perspective, never the system's

#### Key Practice 2: Playbacks

**What**: Regular presentations of work-in-progress to stakeholders, using the Hills as the measuring stick.

**Three types**:
1. **Alignment Playback** — "Here's the problem we're solving and the Hills we've set." (Beginning)
2. **Review Playback** — "Here's our progress against the Hills. Here's what we've learned." (Middle)
3. **Decision Playback** — "Here's our recommendation. Here's the evidence." (Decision points)

**Why it matters**: Prevents the "big reveal" anti-pattern where teams build in isolation for months, then show stakeholders a finished product that doesn't meet expectations.

#### Key Practice 3: Sponsor Users

**What**: Real users (not proxies) who participate in the design process from beginning to end.

**Requirements**:
- Must be actual end users of the product (not managers, not sales reps, not executives)
- Participate in research, co-design sessions, and testing
- Available for ongoing feedback throughout the project
- Minimum 3 Sponsor Users per project for diversity of perspective

**Why it matters**: Sponsor Users keep the team grounded in real needs. When debates arise about "what users want," the team can ask actual users.

### Mapping to NNG Phases

| EDT Activity | NNG Phase | EDT Addition |
|-------------|-----------|-------------|
| Observe | Empathize | Sponsor Users provide ongoing access |
| Reflect | Define | Hills replace requirements docs |
| Make | Ideate + Prototype | Continuous loop, not linear |
| Playback | Test (stakeholder) | Regular alignment checkpoints |
| (with Sponsor Users) | Test (user) | Real users throughout, not just at the end |

### Adapting for AI-Assisted Development

**What stays**: Hills. Writing user-outcome-focused goals prevents "feature factory" development.
**What changes**: The Make cycle accelerates with AI generation.
**Risk**: Skipping Playbacks because "I'm just one developer." Even solo devs benefit from self-review checkpoints.

**Terminal adaptation**:
1. Hills: Write 1-3 Hills in `/brief` format ("A [user] can [outcome] in [measurable way]")
2. Observe: Define persona and context in `/brief`
3. Make: `/screen` or `/component` against the Hills
4. Self-Playback: Run `/grade` — does the output achieve the Hills?
5. Sponsor User simulation: Have a real person (colleague, friend, target user) try the prototype

---

## 5. Lean UX — Build-Measure-Learn

### Origin & Philosophy

Eric Ries (*The Lean Startup*, 2011) and Jeff Gothelf (*Lean UX*, 2013) adapted lean manufacturing principles to design. The core insight: every design decision is a hypothesis that can be tested. Don't invest in polished designs until you have evidence they work.

**Core belief**: The riskiest assumption is the one you don't test. Minimize waste by validating hypotheses with the smallest possible investment.

### The Process

#### Step 1: Declare Assumptions

**What**: Make every assumption explicit before designing anything.

**Business assumptions**: Who is our target user? What problem are we solving? How will we make money?
**User assumptions**: What are users' needs? How do they currently solve this problem? What would make them switch?
**Design assumptions**: What UI pattern will work? What information hierarchy is correct? What mental model applies?

**Lean UX Canvas** (captures all assumptions in one artifact):
- Business problem
- Business outcomes
- Users and customers
- User benefits
- Solutions
- Hypotheses
- What's the riskiest assumption?

#### Step 2: Form Hypotheses

**Format**: "We believe [outcome] will be achieved if [persona] attains [benefit] with [feature]."

**Example**: "We believe increased checkout completion will be achieved if first-time shoppers attain confidence in purchase security with a real-time fraud protection indicator."

#### Step 3: Build MVP (Minimum Viable Product)

**What**: The smallest thing you can build to test the hypothesis.

**MVP types**:
- **Concierge MVP** — Manually perform the service to test demand
- **Wizard of Oz MVP** — Interface looks automated but is manually operated
- **Landing page MVP** — Test demand before building anything
- **Single-feature MVP** — One feature, polished, with real users
- **Prototype MVP** — Clickable mockup tested for usability

#### Step 4: Measure

**What**: Collect quantitative and qualitative data on the hypothesis.

**Quantitative**: Conversion rates, task completion rates, time-on-task, error rates.
**Qualitative**: User interviews, observation, support tickets, NPS.

**Key metric**: Define the "one metric that matters" (OMTM) for each hypothesis.

#### Step 5: Learn

**What**: Analyze data and make a decision: persevere, pivot, or kill.

**Persevere**: Hypothesis validated. Scale the solution.
**Pivot**: Hypothesis partially validated. Change the approach but keep the goal.
**Kill**: Hypothesis invalidated. Abandon this approach entirely.

### Mapping to NNG Phases

| Lean UX Step | NNG Phase | Lean Addition |
|-------------|-----------|--------------|
| Assumptions | Empathize + Define | Makes all beliefs explicit |
| Hypotheses | Define | Testable prediction, not just problem statement |
| MVP | Prototype | Minimum investment to learn |
| Measure | Test | Quantitative + qualitative |
| Learn | (loops back) | Persevere / pivot / kill decision |

### Adapting for AI-Assisted Development

**What stays**: The hypothesis format. It prevents "building because we can."
**What changes**: MVP creation is nearly instant with AI generation.
**Risk**: Building full products instead of MVPs because AI makes it easy. More code ≠ more learning.

**Terminal adaptation**:
1. Hypothesis: Write in `/brief` format — "We believe [X] if [Y] with [Z]"
2. MVP: `/component` one component that tests the hypothesis, not a full screen
3. Measure: Define metric in `/research`, collect data
4. Learn: `/roast` + `/grade` — does the output validate the hypothesis?
5. Iterate: `/remix` to apply learnings, or `/brief` to reframe

---

## 6. Spotify — Squad-Based Design Thinking

### Origin & Philosophy

Spotify's organizational model (Henrik Kniberg & Anders Ivarsson, 2012) organizes autonomous squads (8-12 people) around user missions, not features. Design thinking happens at the squad level, with design system alignment happening across squads through guilds and chapters.

**Core belief**: Autonomous teams closest to the user make the best design decisions, but they need shared design language to maintain product coherence.

### The Model

#### Squads (Autonomous Teams)

Each squad:
- Owns a user mission (e.g., "Make music discovery feel magical")
- Has embedded design capability (designer + researcher or design-savvy engineers)
- Runs its own research, ideation, and testing cycles
- Ships independently without cross-team approval
- Uses think-it / build-it / ship-it / tweak-it as internal process

#### Tribes (Squad Collections)

Tribes group squads around a business domain (e.g., "Listening Experience"). Tribes provide:
- Shared context through tribe-level OKRs
- Regular Demo Days for cross-squad learning
- Resource sharing and conflict resolution

#### Chapters (Skill Groups)

Chapters group people with the same skill across squads (e.g., all UX designers). Chapters provide:
- Craft mentorship and growth
- Shared practices and tools
- Design system governance

#### Guilds (Communities of Interest)

Guilds are voluntary communities around shared interests (e.g., "Accessibility Guild," "Data Visualization Guild"). Guilds provide:
- Cross-functional knowledge sharing
- Best practice documentation
- Innovation incubation

### The Think-It / Build-It / Ship-It / Tweak-It Process

**Think-It** (1-2 weeks):
- Narrative writing: "Imagine a user who..."
- Data mining: What does existing data tell us?
- Prototype testing: Quick mockups with internal users
- Bet sizing: How much should we invest?

**Build-It** (2-4 weeks):
- Development sprints
- Continuous A/B testing
- Internal dogfooding
- Quality gates (design review, a11y, performance)

**Ship-It** (1 day-1 week):
- Gradual rollout (1% → 5% → 25% → 100%)
- Real-time monitoring
- Kill switch ready

**Tweak-It** (ongoing):
- Measure against OKRs
- User feedback channels
- Continuous iteration
- Sunset if not working

### Mapping to NNG Phases

| Spotify Phase | NNG Phase | Spotify Addition |
|--------------|-----------|-----------------|
| Think-It | Empathize + Define + Ideate | Narrative-driven, data-informed |
| Build-It | Prototype + Test | Continuous testing during build |
| Ship-It | Implement | Gradual rollout with monitoring |
| Tweak-It | Test (post-launch) | Continuous measurement and iteration |

### Adapting for AI-Assisted Development

**What stays**: The narrative format ("Imagine a user who...") — it forces empathy.
**What changes**: Build-It compresses dramatically with AI generation.
**Risk**: Skipping Think-It because AI makes Build-It so fast.

**Terminal adaptation**:
1. Think-It: `/brief` — write the user narrative, define the bet
2. Build-It: `/tokens` + `/screen` + `/component` — generate with full context
3. Ship-It: `/a11y` + `/responsive` — quality gates before deploy
4. Tweak-It: `/roast` + `/grade` — measure and iterate

---

## 7. Microsoft — Inclusive Design

### Origin & Philosophy

Microsoft's Inclusive Design methodology (Kat Holmes, *Mismatch*, 2018) reframes accessibility as a design driver, not a compliance checkbox. The core insight: disability is a mismatch between a person and their environment, not a condition of the person.

**Core belief**: "Solve for one, extend to many." Designing for people with permanent disabilities creates solutions that benefit everyone (curb cuts, closed captions, voice interfaces).

### The Persona Spectrum

Microsoft's key contribution is the **Persona Spectrum** — showing how disability exists on a spectrum from permanent to temporary to situational:

| Interaction | Permanent | Temporary | Situational |
|------------|-----------|-----------|-------------|
| **Touch** | One arm | Arm injury | Holding a child |
| **See** | Blind | Cataracts | Distracted driver |
| **Hear** | Deaf | Ear infection | Loud bar |
| **Speak** | Non-verbal | Laryngitis | Heavy accent |
| **Cognition** | Cognitive disability | Concussion | Sleep-deprived |

**Insight**: Designing for the "permanent" column creates solutions that help everyone across the spectrum. Closed captions (designed for deaf users) help in loud bars, while learning a language, and when you can't disturb a sleeping baby.

### The 3 Inclusive Design Principles

#### Principle 1: Recognize Exclusion

**What**: Actively identify who is excluded by current designs and why.
**Method**: For every design decision, ask "Who can't use this?" across all five interaction types.
**Example**: A drag-and-drop interface excludes keyboard users, users with motor impairments, and anyone using a screen reader.

#### Principle 2: Solve for One, Extend to Many

**What**: Design for the most constrained user first. The solution will benefit broader audiences.
**Method**: Use the Persona Spectrum to identify the "one" to solve for.
**Example**: Voice control (designed for motor-impaired users) becomes the preferred interaction for everyone cooking, driving, or exercising.

#### Principle 3: Learn from Diversity

**What**: People with disabilities are experts in adaptation. Include them as co-designers, not just testers.
**Method**: Recruit people with disabilities as Sponsor Users (IBM terminology) or design collaborators.
**Example**: Blind users who navigate complex websites daily know more about information architecture than any sighted designer.

### Mapping to NNG Phases

| Inclusive Design | NNG Phase | Inclusive Addition |
|-----------------|-----------|-------------------|
| Recognize Exclusion | Empathize | Persona Spectrum analysis |
| Solve for One | Define + Ideate | Constraint-driven design |
| Learn from Diversity | Test | Co-design with diverse users |
| (Throughout) | All phases | Accessibility as process, not checkpoint |

### Adapting for AI-Assisted Development

**What stays**: The Persona Spectrum exercise. AI cannot identify who it's excluding.
**What changes**: AI can generate accessible code if explicitly instructed.
**Risk**: AI-generated UI often fails accessibility because training data contains inaccessible patterns.

**Terminal adaptation**:
1. Recognize: Before prompting, ask "Who can't use this?" for all 5 interaction types
2. Solve: `/brief` — include the most constrained persona as the target user
3. Build: `/component` — explicitly request accessible code with ARIA, keyboard, screen reader support
4. Verify: `/a11y` — automated accessibility audit
5. Learn: Test with real users, including users with disabilities

---

## 8. Vercel/Figma — Design Engineer Workflow

### Origin & Philosophy

The "Design Engineer" role (Vercel coined the title, but the practice emerged from teams like Stripe, Linear, and Figma) merges design and engineering into a single practitioner. Instead of handoff between designers and developers, one person designs in code, using tools like Figma MCP, design tokens, and component libraries to bridge the gap.

**Core belief**: The best interfaces emerge when the person making design decisions can immediately implement them, and vice versa. Handoff is waste.

### The Workflow

#### Step 1: Design in Context

**What**: Design directly in the medium that ships (code), using design tools for exploration only.
**Tools**: Figma for exploration → Figma Dev Mode for inspection → Code for implementation.
**Key**: Decisions made in Figma are proposals. Decisions made in code are commitments.

#### Step 2: Token-Driven Development

**What**: Every visual decision is encoded in design tokens, not hardcoded values.
**Flow**: Figma Variables → W3C Design Tokens → Style Dictionary → Platform code.
**Key**: Tokens are the single source of truth for color, typography, spacing, elevation, and motion.

#### Step 3: Component-First Architecture

**What**: Build reusable components that consume tokens and compose into screens.
**Pattern**: Tokens → Primitives → Composites → Screens.
**Key**: Every component has defined props, states (7 minimum), accessibility attributes, and responsive behavior.

#### Step 4: Visual Regression + Design Audit

**What**: Automated testing catches unintended visual changes. Design audits catch intentional-but-flawed changes.
**Tools**: Chromatic, Percy, or custom screenshot comparison + Sumi audit commands.
**Key**: Visual regression catches *what changed*. Design audits catch *whether the change is good*.

#### Step 5: Figma MCP Integration

**What**: Figma's Model Context Protocol (MCP) server enables AI agents to read Figma files, extract design decisions, and generate code that matches the design spec.
**Flow**: Designer creates in Figma → MCP reads the file → AI generates matching code → `/figma` validates alignment.
**Key**: MCP doesn't replace design judgment — it accelerates the handoff of mechanical decisions (spacing, color, layout structure).

### Mapping to NNG Phases

| Design Engineer | NNG Phase | DE Addition |
|----------------|-----------|------------|
| Design in Context | Ideate + Prototype | Design and code are the same activity |
| Token-Driven Dev | Implement | Single source of truth |
| Component-First | Implement | Systematic composition |
| Visual Regression | Test | Automated visual validation |
| Figma MCP | Prototype + Implement | AI-assisted design-to-code |

### Adapting for AI-Assisted Development

**What stays**: Everything — this methodology was designed for AI-assisted development.
**What changes**: The "Design in Context" step is now "Design in Conversation" (prompting AI).
**Risk**: Losing the exploration step. Design Engineers still sketch, wireframe, and explore in Figma before committing to code. Don't skip exploration just because AI can generate code instantly.

**Terminal adaptation**:
1. Explore: `/style` + `/style` — establish direction before generating
2. Foundation: `/tokens` — create the token system
3. Build: `/screen` + `/component` — generate components consuming tokens
4. Validate: `/figma` — verify Figma-to-code alignment
5. Audit: `/audit` + `/a11y` — quality gate before shipping

---

## Methodology Decision Matrix

Use this matrix to choose the right methodology for your context:

| Factor | IDEO | Double Diamond | Sprint | IBM EDT | Lean UX | Spotify | Microsoft ID | Vercel/Figma |
|--------|------|---------------|--------|---------|---------|---------|-------------|-------------|
| **Team size** | 5-15 | 3-10 | 4-7 | 10-100+ | 2-5 | 8-12/squad | Any | 1-3 |
| **Timeline** | Weeks-months | Days-weeks | 5 days | Ongoing | Continuous | Continuous | Ongoing | Hours-days |
| **Problem clarity** | Ambiguous | Medium | Focused | Strategic | Hypothesis | Mission-based | Inclusive | Clear |
| **Best for** | Innovation | Structured design | Quick decisions | Enterprise | Startups | Product teams | Accessibility | Design engineering |
| **Risk if skipped** | Wrong problem | Chaotic process | Analysis paralysis | Misalignment | Waste | Inconsistency | Exclusion | Slow delivery |
| **AI adaptation** | Moderate | Easy | Easy | Moderate | Easy | Moderate | Critical | Native |

### The Solo Developer's Choice

If you're one developer working in the terminal with AI assistance:

**Primary**: Lean UX (hypothesis-driven, fast cycles)
**Secondary**: Vercel/Figma workflow (token-driven, component-first)
**Process layer**: Double Diamond thinking (diverge/converge rhythm)
**Ethics layer**: Microsoft Inclusive Design (Persona Spectrum)

This combination gives you:
1. A clear hypothesis before every build session (`/brief`)
2. A token-driven architecture (`/tokens` → `/screen` → `/component`)
3. Divergent thinking before convergent building (`/style` + `/style` → then `/component`)
4. Accessibility-first design (Persona Spectrum in `/brief`, verified with `/a11y`)

---

## Speed-Adapted Methodologies

Every methodology above can compress. Here's how to run each one as a solo developer with AI assistance:

### IDEO Speed Run (30 min)
```
0-5 min:   Empathy sprint — write 3 user stories from observation/research
5-10 min:  /intent — formalize into problem statement and persona
10-15 min: Crazy 8s — sketch 8 solutions in 8 minutes (paper/notes)
15-20 min: /ship — prototype the best solution
20-30 min: /vibe-check + /include — test against heuristics and accessibility
```

### Double Diamond Speed Run (20 min)
```
Diamond 1 — The Problem (10 min):
  0-5 min:  Diverge — list 5 possible problems users have
  5-10 min: Converge — /intent on the most critical one

Diamond 2 — The Solution (10 min):
  10-15 min: Diverge — /inspo for 3 different pattern approaches
  15-20 min: Converge — /ship the best approach with constraint stack
```

### Google Sprint Speed Run (2 hours)
```
Map (15 min):    Write user journey, circle critical moment
Sketch (15 min): /inspo + sketch 3 approaches
Decide (10 min): Pick based on persona needs, not personal preference
Prototype (40 min): /drip + /screen or /ship
Test (40 min):   /vibe-check + /include + /brain-scan + /flow
```

### IBM EDT Speed Run (15 min)
```
Hill (5 min):    "A [user] can [do X] in [measurable way]"
                 Write 1-3 Hills in /intent
Make (5 min):    /ship against the Hills
Playback (5 min): /judge — does it achieve the Hills?
```

### Lean UX Speed Run (10 min)
```
Hypothesis (2 min): "We believe [outcome] if [persona] gets [feature]"
MVP (5 min):        /ship one component that tests the hypothesis
Learn (3 min):      /vibe-check — does it validate or invalidate?
```

### Spotify Speed Run (20 min)
```
Think-It (5 min):   /intent — write the user narrative + bet size
Build-It (10 min):  /drip + /ship — generate with full context
Ship-It (2 min):    /include + /responsive — quality gate check
Tweak-It (3 min):   /roast — identify improvements for next cycle
```

### Microsoft Inclusive Speed Run (15 min)
```
Recognize (5 min):  For each interaction type (touch/see/hear/speak/think),
                    ask "Who can't use this?" Write down 5 excluded users.
Solve (5 min):      /intent with the most constrained persona as target
Verify (5 min):     /include — did we actually solve for them?
```

### Vercel/Figma Speed Run (15 min)
```
Explore (5 min):  /taste + /inspo — direction before committing
Build (5 min):    /drip tokens → /ship consuming tokens
Validate (5 min): /vibe-check + /include — quality gate
```

**The pattern across all speed runs**: Define the problem → Build with constraints → Test before shipping. The methodology just shapes how you do each step.
