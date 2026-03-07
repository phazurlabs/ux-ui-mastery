---
description: "[6.3] Pre-launch checklist — comprehensive readiness check covering SEO, performance, analytics, error tracking, legal compliance, security, and operational concerns before shipping."
phase: "6"
phase_step: "6.3"
phase_name: "LAUNCH"
step_label: "Step 28 of 30"
---

# Pre-Launch Preflight — Comprehensive Readiness Check

The final gate between "the design is good" and "it's actually ready to ship." This command generates a comprehensive pre-launch checklist that covers every category that can derail an otherwise well-designed product at launch.

## Analysis Protocol

### Step 0: Gather Context

Before generating the checklist, collect:

1. **Product type**: Web app, mobile app, marketing site, SaaS, e-commerce, or hybrid.
2. **Platform**: Web, iOS, Android, cross-platform. This determines which checklist items apply.
3. **Target markets**: Geographic regions and user demographics. This affects legal/regulatory requirements (GDPR for EU, CCPA for California, etc.).
4. **Feature flags**: Has AI features? Has payments/commerce? Has user accounts? Has user-generated content? Each flag activates additional checklist items.
5. **Prior Sumi outputs**: Consume any available, especially `/26-verdict` (comprehensive review), `/27-grade` (visual quality score), `/25-qa` (design QA). These provide evidence for several checklist items.

If the user has not run prior commands, note which checklist items cannot be verified and recommend running the relevant command.

### Step 1: SEO & DISCOVERABILITY

**For web products**:
- [ ] Page titles unique and descriptive (50-60 characters)
- [ ] Meta descriptions written (150-160 characters)
- [ ] Heading hierarchy correct (one H1 per page, logical H2-H6 nesting)
- [ ] Semantic HTML used (nav, main, article, section, aside, footer)
- [ ] Open Graph tags for social sharing (og:title, og:description, og:image)
- [ ] Twitter Card tags configured
- [ ] Canonical URLs set on all pages
- [ ] sitemap.xml generated and submitted to search engines
- [ ] robots.txt configured correctly
- [ ] Structured data (JSON-LD) for key content types
- [ ] 301 redirects configured for any changed URLs
- [ ] Alt text on all meaningful images
- [ ] No broken internal links

**For mobile apps**:
- [ ] App Store / Play Store description optimized
- [ ] Keywords researched and set
- [ ] Screenshots prepared for all required device sizes
- [ ] Preview video created (if applicable)
- [ ] App category selected correctly
- [ ] App icon meets platform guidelines

### Step 2: PERFORMANCE

- [ ] Core Web Vitals targets met: LCP <2.5s, INP <200ms, CLS <0.1
- [ ] Images optimized (WebP/AVIF format, responsive srcset, lazy loading below fold)
- [ ] Fonts optimized (preload critical fonts, font-display: swap, subset if possible)
- [ ] JavaScript bundle size checked (target: <200KB initial load)
- [ ] CSS optimized (unused CSS removed, critical CSS inlined)
- [ ] Compression enabled (Brotli preferred, gzip fallback)
- [ ] CDN configured for static assets
- [ ] Caching headers set (immutable for hashed assets, appropriate max-age)
- [ ] No render-blocking resources in critical path
- [ ] Lighthouse Performance score >90
- [ ] Time to Interactive <3.5s on mid-tier mobile device
- [ ] API response times <500ms for critical endpoints

### Step 3: ANALYTICS & MONITORING

- [ ] Analytics tool configured and verified (GA4, Plausible, PostHog, Mixpanel)
- [ ] Key events tracked (mapped from `/06-measure` HEART metrics plan if available)
- [ ] Conversion funnels defined and instrumented
- [ ] Error tracking live and verified (Sentry, LogRocket, Bugsnag)
- [ ] Uptime monitoring configured (Checkly, UptimeRobot, Pingdom)
- [ ] Real User Monitoring (RUM) enabled
- [ ] Launch metrics dashboard built
- [ ] Alert thresholds set (error rate >1%, response time >3s, availability <99.5%)

### Step 4: ACCESSIBILITY

- [ ] WCAG 2.2 AA audit passed (from `/14-access` if available)
- [ ] Keyboard navigation works for all critical flows
- [ ] Screen reader tested (VoiceOver on macOS/iOS, NVDA on Windows, TalkBack on Android)
- [ ] Color contrast passing all text (4.5:1 body text, 3:1 large text/UI components)
- [ ] Focus indicators visible on all interactive elements
- [ ] Skip navigation link present (web)
- [ ] Reduced motion respected (@prefers-reduced-motion / UIAccessibility.isReduceMotionEnabled)
- [ ] Accessibility statement page published (if required by jurisdiction)
- [ ] Touch targets minimum 44x44pt (mobile)
- [ ] Form labels properly associated with inputs

### Step 5: LEGAL & COMPLIANCE

- [ ] Privacy policy linked and current (covers all data collection)
- [ ] Terms of service linked and current (if user accounts exist)
- [ ] Cookie consent banner implemented (required for EU/UK/California visitors)
- [ ] GDPR data handling documented (if EU users): right to access, delete, export
- [ ] CCPA compliance implemented (if California users): opt-out of data sale
- [ ] Age verification gate (if age-restricted content)
- [ ] Disclaimer/disclosure present (if financial, health, or legal content)
- [ ] Licenses verified for all fonts, images, icons, and third-party assets
- [ ] AI-generated content disclosed where applicable
- [ ] Data Processing Agreement (DPA) with third-party processors
- [ ] Copyright notice in footer

### Step 6: SECURITY

- [ ] HTTPS enforced everywhere (HTTP redirects to HTTPS)
- [ ] Content Security Policy (CSP) headers configured
- [ ] No secrets or API keys exposed in client-side code
- [ ] Form inputs sanitized (XSS prevention)
- [ ] Authentication secure (bcrypt/argon2 hashing, rate limiting, 2FA option)
- [ ] CORS configured correctly (not wildcard in production)
- [ ] Dependencies audited for known vulnerabilities (npm audit / pip audit)
- [ ] Rate limiting on API endpoints and login attempts
- [ ] Security headers set (X-Frame-Options, X-Content-Type-Options, Referrer-Policy)
- [ ] SQL injection prevention verified (parameterized queries)
- [ ] File upload validation (if applicable)

### Step 7: OPERATIONAL READINESS

- [ ] 404 page designed and functional (branded, helpful, links back to home)
- [ ] 500/error page designed and functional (apologetic, shows status page link)
- [ ] Favicon configured (all sizes: 16x16, 32x32, 180x180, 192x192, 512x512)
- [ ] Web manifest (manifest.json) configured for PWA (if applicable)
- [ ] Social preview tested (Facebook Sharing Debugger, Twitter Card Validator)
- [ ] Email templates tested across clients (if transactional emails exist)
- [ ] Backup and recovery plan documented
- [ ] Rollback procedure documented and tested
- [ ] Launch communication plan ready (announcement, social media, email newsletter)
- [ ] Support channels ready (help docs, contact form, chat widget)
- [ ] DNS configuration verified (propagation complete)
- [ ] SSL certificate auto-renewal configured

### Step 8: FINAL DESIGN CHECK

- [ ] Design QA passed (from `/25-qa` if available)
- [ ] All states implemented (empty, loading, error, success, offline)
- [ ] Responsive at all breakpoints (mobile, tablet, desktop, ultrawide)
- [ ] Dark mode tested and consistent (if supported)
- [ ] Print stylesheet present (if content is printable)
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge — latest 2 versions)
- [ ] Real content throughout (no lorem ipsum, no placeholder images, no test data)
- [ ] Copy proofread for spelling and grammar
- [ ] Links all functional (no dead links, no placeholder hrefs)
- [ ] Forms submit correctly with validation messages

## Output Format

```
### Phase Position
> **Phase 6: LAUNCH** | Step 28 of 30 | `/28-preflight`
>
> `/27-grade` (5.4) --> **`/28-preflight` (6.3)** --> `/29-welcome` (6.4)

---

## Pre-Launch Preflight Checklist

### Product Context
- **Product**: [Name/description]
- **Type**: [Web app / mobile app / marketing site / etc.]
- **Platform**: [Web / iOS / Android / cross-platform]
- **Target markets**: [Regions]
- **Feature flags**: [AI / payments / accounts / UGC]
- **Prior Sumi context**: [What was consumed from prior commands]

---

### Readiness Summary

| Category | Status | Items | Passing | Failing | N/A |
|----------|--------|-------|---------|---------|-----|
| SEO & Discovery | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Performance | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Analytics & Monitoring | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Accessibility | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Legal & Compliance | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Security | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Operations | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |
| Design | [PASS/WARN/FAIL] | [N] | [N] | [N] | [N] |

**Overall: [X/Y] items passing -- [READY TO LAUNCH / NOT READY / READY WITH WARNINGS]**

---

[Detailed checklist per category with pass/fail/N/A per item and evidence notes]

---

### Blocking Issues (Must Fix Before Launch)
[Any failing items that MUST be fixed -- these prevent launch]

### Recommended Before Launch
[Items that should be fixed but will not block launch]

### Post-Launch (Can Wait)
[Items safe to address in the first week after launch]

---

### Next Steps

1. **Fix** all blocking issues listed above
2. **Then** --> `/29-welcome` -- Build onboarding for new users
3. **Then** --> `/30-iterate` -- Plan post-launch monitoring and iteration

**Run `/next` to continue the journey.**
```

## Quality Gates

The output MUST include:
- [ ] All 8 categories covered with per-item pass/fail/N/A
- [ ] Each item marked with evidence or reason for its status
- [ ] Blocking issues clearly separated from recommendations
- [ ] Platform-appropriate checks (web-only items skipped for native mobile, and vice versa)
- [ ] Legal requirements matched to the specific target markets provided
- [ ] Performance targets specified with actual measurements where available
- [ ] Clear overall verdict: READY TO LAUNCH / NOT READY / READY WITH WARNINGS
- [ ] N/A items explained (why they do not apply)

The output MUST NOT include:
- Unchecked items without explanation -- every item must have a status and reason
- Generic advice without specificity -- cite the actual product context
- False confidence -- if an item cannot be verified, mark it as UNVERIFIED, not PASS

## Cross-References

When generating the checklist, draw knowledge from:
- `performance-states-patterns` skill -- loading, error, empty, offline states
- `accessibility-inclusive-design` skill -- WCAG 2.2 compliance requirements
- `ux-ethics-content-strategy` skill -- privacy, legal, ethical compliance
- `ux-metrics-measurement` skill -- analytics setup and measurement planning
- `platform-visual-standards` skill -- cross-browser, cross-device, platform requirements
- `component-patterns-code` skill -- implementation verification for design patterns
- `screen-flow-patterns` skill -- screen completeness verification

## Next Step

**Next** --> `/29-welcome` (6.4) -- Build an onboarding flow for new users

**Alternatives**:
- `/30-iterate` (6.5) -- Skip to post-launch iteration planning
- `/25-qa` (5.3) -- Run design QA if not yet done
- `/27-grade` (5.4) -- Get a visual quality score if not yet done
- `/guide` -- See the full journey map
