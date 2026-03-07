---
description: "[6.5] Post-launch plan — monitoring dashboard, week 1/4/12 review cadence, iteration priorities based on data, and feedback loop back to discovery."
phase: "6"
phase_step: "6.5"
phase_name: "LAUNCH"
step_label: "Step 30 of 30"
---

# Iterate — Post-Launch Monitoring & Continuous Improvement

Every world-class design framework (Spotify's "Tweak It", Lean UX's "Check", IBM's "Loop", Google's "Iterate") emphasizes that launch is the middle of the product lifecycle, not the end. This command plans what happens after shipping: what to monitor, when to review, how to prioritize improvements, and how to loop back into the Sumi journey when data reveals what to fix next.

## Analysis Protocol

### Step 0: Gather Context

Before building the iteration plan, collect:

1. **What launched**: Product name, feature set, scope (full product, feature update, redesign).
2. **Launch date**: Actual or planned date. This anchors the review cadence timeline.
3. **Key metrics**: What success looks like. Consume `/06-measure` HEART metrics if available.
4. **Analytics setup**: What is instrumented. Consume `/28-preflight` analytics section if available.
5. **Known issues**: Any items deferred from preflight, known UX debt, or pre-launch concerns.
6. **Prior Sumi outputs**: Consume `/06-measure` (metrics plan), `/28-preflight` (readiness state), `/22-test` (test findings), `/26-verdict` (comprehensive review), `/12-audit` (heuristic findings). These provide baseline context for monitoring.

### Step 1: MONITORING DASHBOARD

Design a post-launch monitoring dashboard organized by check frequency:

**Real-time (always visible)**:
- Active users (concurrent sessions)
- Error rate (client-side and server-side)
- Page load time / app launch time
- Uptime / availability status
- Critical conversion events (sign-ups, purchases, key actions)

**Daily review**:
- DAU (Daily Active Users)
- Session duration (average, median, p90)
- Bounce rate / immediate exit rate
- Conversion rate for primary funnel
- Error count by type (new vs. recurring)
- Support ticket volume

**Weekly review**:
- WAU and DAU/WAU ratio (stickiness)
- Retention: Day 1, Day 7 cohort curves
- Feature adoption rates (% of users who used each key feature)
- NPS or CSAT score (if survey is live)
- Support ticket categorization (UX issue vs. bug vs. feature request)
- Top 5 user paths (are they the intended paths?)

**Monthly review**:
- MAU and growth trend
- Retention: Day 30 cohort
- Revenue metrics (if applicable): ARPU, LTV, churn
- Feature adoption maturity curves
- Competitive landscape changes
- Roadmap progress vs. plan

**Alert thresholds** (trigger immediate investigation):
- Error rate >1% of sessions
- Page load time >3s (p95)
- Conversion rate drops >10% from baseline
- Availability <99.5%
- Spike in support tickets (>2x daily average)
- New error type affecting >100 users

**Recommended tools** (pick per stack):
- Analytics: GA4, PostHog, Mixpanel, Amplitude, Plausible
- Error tracking: Sentry, LogRocket, Bugsnag
- Uptime: Checkly, UptimeRobot, Pingdom, Better Uptime
- RUM: Vercel Analytics, Cloudflare Web Analytics, SpeedCurve
- User feedback: Hotjar, FullStory, Sprig

### Step 2: REVIEW CADENCE

**Week 1 (Launch Week) -- Daily Check**
- Focus: Is anything broken? Is anything confusing users?
- Monitor: Error rates, support tickets, social mentions, app store reviews
- Questions: Are users completing the primary flow? Where are they dropping off? What errors are new?
- Actions: Emergency fixes only. Do not redesign -- stabilize.
- Meeting: 15-minute daily standup with eng + design

**Weeks 2-4 -- Weekly Review**
- Focus: What patterns are emerging in real usage data?
- Monitor: Retention curves, feature adoption, user feedback themes
- Questions: Which features are users ignoring? Where do users get stuck? What do support tickets reveal?
- Actions: Quick wins (< 1 day effort). Categorize larger issues.
- Meeting: 30-minute weekly review with stakeholders

**Month 2-3 -- Bi-Weekly Review**
- Focus: Retention trends, deeper usability insights, first iteration cycle
- Monitor: Cohort retention, NPS trends, competitive moves
- Questions: Are we retaining users past Day 7? What is the #1 improvement request? Has the competitive landscape shifted?
- Actions: Plan and ship first iteration cycle. Schedule user interviews.
- Meeting: 45-minute bi-weekly product review

**Month 3+ -- Monthly Review**
- Focus: Strategic metrics, product-market fit signals, roadmap planning
- Monitor: Growth rate, LTV, market position, feature maturity
- Questions: Is the product growing? Where is the biggest opportunity? What should the next major initiative be?
- Actions: Roadmap adjustments, major feature planning, new Sumi cycle for expansion
- Meeting: 60-minute monthly strategy review

### Step 3: FEEDBACK CHANNELS

Set up multiple channels to hear from users at different stages:

**In-app feedback**:
- Micro-surveys: NPS at Day 7 and Day 30 (single question, non-intrusive)
- Contextual feedback: thumbs up/down or "Was this helpful?" on key screens
- Feedback button: persistent but unobtrusive "Send Feedback" option
- Feature-specific: short survey after first use of new features

**Support analysis**:
- Categorize every ticket: UX issue / Bug / Feature request / Documentation gap
- Track resolution time and user satisfaction with resolution
- Weekly summary: top 5 UX issues from support data
- Escalation path: UX issues with >5 tickets become investigation items

**User interviews**:
- Schedule 5 user interviews in first 2 weeks post-launch
- Mix: 2 successful users (completed primary flow), 2 struggling users (dropped off), 1 churned user
- Focus questions: What was confusing? What was delightful? What did you expect but not find?
- Record and share clips with the team

**Behavioral analytics**:
- Rage click detection (repeated clicks on non-interactive elements)
- Dead click detection (clicks on elements that look clickable but are not)
- Drop-off analysis on multi-step flows
- Unexpected navigation paths (users finding workarounds)
- Session replay review (sample 10 sessions per week)

**Social listening**:
- Monitor product mentions on Twitter/X, Reddit, Product Hunt, Hacker News
- Track app store reviews and ratings (daily during launch week)
- Community forums or Discord (if applicable)
- Competitor mention tracking (are users comparing?)

### Step 4: ITERATION PRIORITIES

Framework for deciding what to fix or improve next:

**P0 -- Fix NOW (same day)**:
- Broken functionality that blocks the primary user flow
- Accessibility failures that prevent usage by disabled users
- Security vulnerabilities
- Data loss or corruption risks
- Legal compliance failures

**P1 -- This Sprint (this week)**:
- High-impact UX issues (>10% of users affected)
- Conversion funnel blockers
- Critical feedback themes (same issue from 3+ users)
- Performance regressions above alert thresholds

**P2 -- Next Sprint (next 1-2 weeks)**:
- Medium-impact UX improvements
- Feature requests from multiple users
- Polish items that affect perceived quality
- Missing states (empty, error, loading) in secondary flows

**P3 -- Backlog (plan when ready)**:
- Nice-to-have improvements
- Edge case handling
- Advanced features
- Design debt and consistency cleanup
- Exploratory improvements (A/B test candidates)

**Decision Matrix**:

| | Quick (<1 day) | Medium (1-3 days) | Large (3+ days) |
|---|---|---|---|
| **High Impact** | Do immediately | Schedule this sprint | Plan for next sprint |
| **Medium Impact** | Do this sprint | Evaluate ROI | Backlog with priority |
| **Low Impact** | Batch with similar | Backlog | Deprioritize |

### Step 5: LOOP BACK TO SUMI

When post-launch data reveals issues, map them back to specific Sumi commands to re-enter the design process at the right point:

| Signal | What It Means | Re-Entry Command | Action |
|--------|--------------|-------------------|--------|
| Users confused by navigation | Information architecture mismatch | `/08-map` | Rethink IA with real usage data |
| Users not finding key features | Discoverability failure | `/12-audit` | Heuristic re-evaluation |
| Users abandoning multi-step flows | Flow friction or cognitive overload | `/15-flow` | Flow re-audit with drop-off data |
| Poor visual quality feedback | Design execution gaps | `/27-grade` | Visual quality re-score |
| Accessibility complaints | WCAG compliance gaps | `/14-access` | Accessibility re-audit |
| New competitors emerged | Market position shift | `/05-benchmark` | Competitive re-analysis |
| Users requesting new features | Product expansion opportunity | `/02-brief` then `/03-research` | New design cycle begins |
| Conversion rate below target | Funnel or persuasion issues | `/29-welcome` | Rethink onboarding and first-run |
| High bounce rate | First impression failure | `/10-vision` | Visual direction reassessment |
| Inconsistent UI feedback | Design system drift | `/drip` then `/ship` | Token and component rebuild |
| Content clarity issues | Copy or content strategy gaps | `/copy-check` | Content re-audit |
| Trust or credibility concerns | Trust signal gaps | `/trust-scan` | Trust pattern re-evaluation |

This creates the continuous improvement loop that separates products that launch and stagnate from products that launch and grow.

## Output Format

```
### Phase Position
> **Phase 6: LAUNCH** | Step 30 of 30 | `/30-iterate`
>
> `/29-welcome` (6.4) --> **`/30-iterate` (6.5)** --> Loop back to any step

---

## Post-Launch Iteration Plan

### Product Context
- **Product**: [Name/description]
- **Launch date**: [Date]
- **Key metrics**: [From /06-measure or defined here]
- **Known issues**: [Deferred items from preflight]
- **Prior Sumi context**: [What was consumed]

---

### Monitoring Dashboard

#### Real-Time
[Metrics with specific thresholds and recommended tools]

#### Daily
[Metrics with targets]

#### Weekly
[Metrics with targets]

#### Monthly
[Metrics with targets]

#### Alert Thresholds
| Metric | Warning | Critical | Action |
[Specific thresholds that trigger investigation]

---

### Review Cadence

| Timeframe | Frequency | Focus | Key Questions | Deliverable |
|-----------|-----------|-------|---------------|-------------|
| Week 1 | Daily | Stability | Is anything broken? | Emergency fixes |
| Weeks 2-4 | Weekly | Patterns | What patterns are emerging? | Quick wins list |
| Month 2-3 | Bi-weekly | Retention | Are users coming back? | First iteration cycle |
| Month 3+ | Monthly | Strategy | Is the product growing? | Roadmap update |

---

### Feedback Channels

| Channel | Setup | Frequency | Owner |
|---------|-------|-----------|-------|
[In-app, support, interviews, analytics, social -- specific setup for each]

---

### Iteration Priority Framework

[P0-P3 definitions with decision matrix]

---

### Loop Back Map

| Signal | What It Means | Sumi Command | Action |
|--------|--------------|--------------|--------|
[Data signals mapped to specific Sumi re-entry points]

---

### The Journey Continues

> Step 30 is not the end -- it is the beginning of the next cycle.
> When data reveals what to improve, loop back to the right step.
> Great products are never finished. They are continuously refined.

**Your full journey**: `/01-ground` through `/30-iterate` --> loop back --> grow

Run `/status` to see your complete progress.
Run `/guide` to see the full journey map.
Run `/next` to see recommended re-entry point based on context.
```

## Quality Gates

The output MUST include:
- [ ] Monitoring dashboard with specific metrics, targets, and alert thresholds
- [ ] Review cadence covering Week 1 through Month 3+ with specific questions and deliverables
- [ ] At least 4 feedback channels with setup instructions
- [ ] Priority framework (P0-P3) with decision matrix
- [ ] Loop-back mapping to at least 8 specific Sumi commands with trigger signals
- [ ] Specific and actionable recommendations (not generic advice)
- [ ] Recommended tools matched to the product's tech stack

The output MUST NOT include:
- Generic advice without product context -- every recommendation must reference the actual product
- Vague timelines -- every review cadence entry must have specific frequency and focus
- Metrics without targets -- every metric must have a threshold or baseline
- Loop-back suggestions without signals -- every re-entry must be triggered by observable data

## Cross-References

When building the iteration plan, draw knowledge from:
- `ux-metrics-measurement` skill -- HEART framework, SUS, task success rate, metrics planning
- `ux-research-methods` skill -- post-launch research methods, user interviews, surveys
- `ux-process-workflow` skill -- iteration cycles, continuous improvement, design process loops
- `cognitive-psychology-ux` skill -- understanding user behavior signals
- `nng-ux-heuristics` skill -- heuristic framework for diagnosing issues from data

## Next Step

**Next** --> Loop back to any step based on post-launch data signals

**The most common re-entry points after launch**:
- `/12-audit` (2.1) -- When usability issues surface from real usage
- `/05-benchmark` (1.3) -- When competitive landscape shifts
- `/02-brief` (0.2) -- When planning a major new feature or expansion
- `/guide` -- See the full journey map and pick your re-entry point
