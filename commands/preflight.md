---
name: preflight
description: "Pre-launch checklist and post-launch plan — SEO, performance, analytics, legal, security, monitoring, feedback loops, iteration strategy."
argument-hint: "[product or release to check]"
---

# Preflight — Launch Readiness & Post-Launch Plan

## Before running

This command needs a product or release to check.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


The final gate between "the design is good" and "it's actually ready to ship." This command generates a comprehensive pre-launch checklist AND a post-launch monitoring and iteration plan. Launch is the middle of the product lifecycle, not the end.

## Part 1: Pre-Launch Checklist

### Step 0: Gather Context

1. **Product type**: Web app, mobile app, marketing site, SaaS, e-commerce, hybrid
2. **Platform**: Web, iOS, Android, cross-platform
3. **Target markets**: Geographic regions (affects legal: GDPR for EU, CCPA for California)
4. **Feature flags**: AI features? Payments? User accounts? User-generated content? Each activates additional items
5. **Prior Sumi outputs**: Consume `/audit`, `/grade`, `/qa`, `/a11y` if available

### Category 1: SEO & Discoverability

**Web products**:
- [ ] Page titles unique and descriptive (50-60 characters)
- [ ] Meta descriptions written (150-160 characters)
- [ ] Heading hierarchy correct (one H1 per page, logical H2-H6 nesting)
- [ ] Semantic HTML used (nav, main, article, section, aside, footer)
- [ ] Open Graph tags for social sharing (og:title, og:description, og:image)
- [ ] Twitter Card tags configured
- [ ] Canonical URLs set on all pages
- [ ] sitemap.xml generated and submitted
- [ ] robots.txt configured correctly
- [ ] Structured data (JSON-LD) for key content types
- [ ] 301 redirects for any changed URLs
- [ ] Alt text on all meaningful images
- [ ] No broken internal links

**Mobile apps**:
- [ ] App Store / Play Store description optimized
- [ ] Keywords researched and set
- [ ] Screenshots prepared for all required device sizes
- [ ] Preview video created (if applicable)
- [ ] App category selected correctly
- [ ] App icon meets platform guidelines

### Category 2: Performance

- [ ] Core Web Vitals: LCP <2.5s, INP <200ms, CLS <0.1
- [ ] Images optimized (WebP/AVIF, responsive srcset, lazy loading below fold)
- [ ] Fonts optimized (preload critical, font-display: swap, subset)
- [ ] JavaScript bundle <200KB initial load
- [ ] CSS optimized (unused removed, critical inlined)
- [ ] Compression enabled (Brotli preferred, gzip fallback)
- [ ] CDN configured for static assets
- [ ] Caching headers set (immutable for hashed assets)
- [ ] No render-blocking resources in critical path
- [ ] Lighthouse Performance >90
- [ ] TTI <3.5s on mid-tier mobile
- [ ] API response times <500ms for critical endpoints

### Category 3: Analytics & Monitoring

- [ ] Analytics configured and verified (GA4, Plausible, PostHog, Mixpanel)
- [ ] Key events tracked (mapped from `/measure` HEART plan if available)
- [ ] Conversion funnels defined and instrumented
- [ ] Error tracking live (Sentry, LogRocket, Bugsnag)
- [ ] Uptime monitoring configured (Checkly, UptimeRobot, Pingdom)
- [ ] Real User Monitoring (RUM) enabled
- [ ] Launch metrics dashboard built
- [ ] Alert thresholds set (error rate >1%, response >3s, availability <99.5%)

### Category 4: Accessibility

- [ ] WCAG 2.2 AA audit passed (from `/a11y` if available)
- [ ] Keyboard navigation works for all critical flows
- [ ] Screen reader tested (VoiceOver, NVDA, TalkBack)
- [ ] Color contrast passing (4.5:1 body, 3:1 large text/UI)
- [ ] Focus indicators visible on all interactive elements
- [ ] Skip navigation link present (web)
- [ ] Reduced motion respected (@prefers-reduced-motion)
- [ ] Accessibility statement published (if required)
- [ ] Touch targets minimum 44x44pt (mobile)
- [ ] Form labels properly associated with inputs

### Category 5: Legal & Compliance

- [ ] Privacy policy linked and current
- [ ] Terms of service linked (if user accounts)
- [ ] Cookie consent banner implemented (EU/UK/California)
- [ ] GDPR handling documented (if EU users): access, delete, export
- [ ] CCPA compliance (if California users): opt-out of data sale
- [ ] Age verification gate (if age-restricted content)
- [ ] Disclaimers present (if financial, health, or legal content)
- [ ] Licenses verified for fonts, images, icons, third-party assets
- [ ] AI-generated content disclosed where applicable
- [ ] Data Processing Agreement with third-party processors
- [ ] Copyright notice in footer

### Category 6: Security

- [ ] HTTPS enforced everywhere
- [ ] Content Security Policy (CSP) headers configured
- [ ] No secrets or API keys in client-side code
- [ ] Form inputs sanitized (XSS prevention)
- [ ] Authentication secure (bcrypt/argon2, rate limiting, 2FA option)
- [ ] CORS configured correctly (not wildcard in production)
- [ ] Dependencies audited for vulnerabilities (npm audit / pip audit)
- [ ] Rate limiting on API endpoints and login
- [ ] Security headers set (X-Frame-Options, X-Content-Type-Options, Referrer-Policy)
- [ ] SQL injection prevention (parameterized queries)
- [ ] File upload validation (if applicable)

### Category 7: Operational Readiness

- [ ] 404 page designed and functional (branded, helpful)
- [ ] 500/error page designed (apologetic, status page link)
- [ ] Favicons configured (all sizes: 16, 32, 180, 192, 512)
- [ ] Web manifest configured for PWA (if applicable)
- [ ] Social preview tested (Facebook Debugger, Twitter Validator)
- [ ] Email templates tested across clients (if transactional emails)
- [ ] Backup and recovery plan documented
- [ ] Rollback procedure documented and tested
- [ ] Launch communication plan ready
- [ ] Support channels ready (help docs, contact form, chat)
- [ ] DNS configuration verified
- [ ] SSL certificate auto-renewal configured

### Category 8: Final Design Check

- [ ] Design QA passed (from `/qa` if available)
- [ ] All states implemented (empty, loading, error, success, offline)
- [ ] Responsive at all breakpoints (mobile, tablet, desktop, ultrawide)
- [ ] Dark mode tested and consistent (if supported)
- [ ] Print stylesheet present (if printable content)
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Real content throughout (no lorem ipsum, no placeholders)
- [ ] Copy proofread
- [ ] All links functional
- [ ] Forms submit correctly with validation messages

---

## Part 2: Post-Launch Plan

### Monitoring Dashboard

**Real-time** (always visible):
- Active users, error rate, page load time, uptime, critical conversions

**Daily review**:
- DAU, session duration, bounce rate, conversion rate, error count by type, support tickets

**Weekly review**:
- WAU, DAU/WAU stickiness, Day 1/7 retention, feature adoption, NPS/CSAT, top 5 user paths

**Monthly review**:
- MAU, growth trend, Day 30 retention, revenue metrics (ARPU, LTV, churn), competitive landscape

**Alert thresholds**:

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Error rate | >0.5% | >1% | Investigate immediately |
| Page load (p95) | >2s | >3s | Performance review |
| Conversion rate | -5% | -10% | Funnel analysis |
| Availability | <99.9% | <99.5% | Incident response |
| Support tickets | >1.5x avg | >2x avg | UX review |

### Review Cadence

**Week 1 (Launch Week)** -- Daily:
- Focus: Is anything broken? Is anything confusing?
- Monitor: Error rates, support tickets, social mentions, app store reviews
- Actions: Emergency fixes only. Do not redesign -- stabilize.
- Meeting: 15-minute daily standup with eng + design

**Weeks 2-4** -- Weekly:
- Focus: What patterns are emerging in real usage?
- Monitor: Retention curves, feature adoption, user feedback themes
- Actions: Quick wins (<1 day effort). Categorize larger issues.
- Meeting: 30-minute weekly review

**Month 2-3** -- Bi-Weekly:
- Focus: Retention trends, deeper usability insights, first iteration cycle
- Monitor: Cohort retention, NPS trends, competitive moves
- Actions: Plan and ship first iteration. Schedule user interviews.
- Meeting: 45-minute bi-weekly product review

**Month 3+** -- Monthly:
- Focus: Strategic metrics, product-market fit, roadmap
- Monitor: Growth rate, LTV, market position
- Actions: Roadmap adjustments, major feature planning
- Meeting: 60-minute monthly strategy review

### Feedback Channels

**In-app feedback**:
- Micro-surveys: NPS at Day 7 and Day 30
- Contextual feedback: thumbs up/down on key screens
- Feedback button: persistent "Send Feedback" option
- Feature-specific: short survey after first use of new features

**Support analysis**:
- Categorize every ticket: UX issue / Bug / Feature request / Docs gap
- Weekly summary: top 5 UX issues from support data
- Escalation: UX issues with >5 tickets become investigation items

**User interviews**:
- 5 interviews in first 2 weeks post-launch
- Mix: 2 successful users, 2 struggling users, 1 churned user
- Focus: What was confusing? What was delightful? What was expected but missing?

**Behavioral analytics**:
- Rage click detection
- Dead click detection
- Drop-off analysis on multi-step flows
- Session replay review (10 sessions/week)

**Social listening**:
- Product mentions on Twitter/X, Reddit, Product Hunt, Hacker News
- App store reviews and ratings
- Community forums or Discord
- Competitor mention tracking

### Iteration Priority Framework

| Priority | Definition | Timeline |
|----------|-----------|----------|
| **P0** | Blocks primary flow, accessibility failure, security issue, data loss | Fix same day |
| **P1** | High-impact UX issue (>10% users), conversion blocker, 3+ user reports | This sprint |
| **P2** | Medium-impact improvement, multiple user requests, missing states | Next sprint |
| **P3** | Nice-to-have, edge cases, design debt, A/B test candidates | Backlog |

**Decision matrix**:

| | Quick (<1 day) | Medium (1-3 days) | Large (3+ days) |
|---|---|---|---|
| **High Impact** | Do immediately | This sprint | Plan for next sprint |
| **Medium Impact** | This sprint | Evaluate ROI | Backlog with priority |
| **Low Impact** | Batch with similar | Backlog | Deprioritize |

### Loop Back to Sumi

When post-launch data reveals issues, re-enter the design process:

| Signal | Re-Entry Command | Action |
|--------|-----------------|--------|
| Users confused by navigation | `/map` | Rethink IA with real usage data |
| Users not finding features | `/audit` | Heuristic re-evaluation |
| Users abandoning flows | `/audit` | Flow audit with drop-off data |
| Poor visual quality feedback | `/grade` | Visual quality re-score |
| Accessibility complaints | `/a11y` | Accessibility re-audit |
| New competitors emerged | `/benchmark` | Competitive re-analysis |
| Users requesting new features | `/brief` then `/research` | New design cycle |
| Conversion below target | `/onboard` | Rethink onboarding |
| High bounce rate | `/style` | Visual direction reassessment |
| Content clarity issues | `/audit` | Content audit |

## Output Format

```
## Launch Readiness & Post-Launch Plan

### Product Context
- **Product**: [name]
- **Type**: [web / mobile / both]
- **Platform**: [specifics]
- **Markets**: [regions]
- **Feature flags**: [AI / payments / accounts / UGC]

### Pre-Launch Readiness

| Category | Status | Passing | Failing | N/A |
|----------|--------|---------|---------|-----|
| SEO & Discovery | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Performance | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Analytics | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Accessibility | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Legal | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Security | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Operations | [PASS/WARN/FAIL] | [N] | [N] | [N] |
| Design | [PASS/WARN/FAIL] | [N] | [N] | [N] |

**Overall: [X/Y] passing -- [READY / NOT READY / READY WITH WARNINGS]**

[Detailed checklist per category with evidence]

### Blocking Issues (Must Fix)
[Failing items that prevent launch]

### Recommended Before Launch
[Should fix but won't block]

### Post-Launch Plan

#### Monitoring Dashboard
[Metrics by frequency with tools and thresholds]

#### Review Cadence
[Week 1 through Month 3+ schedule]

#### Feedback Channels
[Setup for each channel]

#### Iteration Framework
[P0-P3 with decision matrix]

#### Loop Back Map
[Signals mapped to Sumi re-entry commands]

### The Journey Continues
> Launch is not the end -- it's the beginning of the next cycle.
> When data reveals what to improve, loop back to the right command.

Run `/status` to see your full progress.
Run `/sumi` to see the complete command map.
```

## Quality Gates

The output MUST include:
- [ ] All 8 pre-launch categories with per-item status
- [ ] Each item with evidence or reason for status
- [ ] Blocking issues separated from recommendations
- [ ] Platform-appropriate checks (web items skipped for native mobile, vice versa)
- [ ] Legal requirements matched to target markets
- [ ] Clear overall verdict: READY / NOT READY / READY WITH WARNINGS
- [ ] Monitoring dashboard with specific metrics, targets, and tools
- [ ] Review cadence covering Week 1 through Month 3+
- [ ] At least 4 feedback channels with setup instructions
- [ ] Priority framework (P0-P3) with decision matrix
- [ ] Loop-back mapping to at least 8 Sumi commands with trigger signals

The output MUST NOT include:
- Items without status explanation
- Generic advice without product specificity
- False confidence (unverifiable items marked UNVERIFIED, not PASS)
- Metrics without targets or thresholds
- Vague timelines

## Cross-References

When generating the checklist and plan, draw from:
- `performance-states-patterns` skill -- loading, error, empty, offline states
- `accessibility-inclusive-design` skill -- WCAG 2.2 requirements
- `ux-ethics-content-strategy` skill -- privacy, legal, ethical compliance
- `ux-metrics-measurement` skill -- analytics and measurement planning
- `platform-visual-standards` skill -- cross-browser, cross-device requirements
- `component-patterns-code` skill -- implementation verification
- `ux-research-methods` skill -- post-launch research methods

## Next Step

**Next** --> Loop back based on data signals, or celebrate the launch

**Alternatives**:
- `/research` -- Plan post-launch user research
- `/benchmark` -- Re-benchmark against competitors after launch
- `/sumi` -- See the full command map
