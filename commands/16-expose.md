---
description: "[3.5] Fortification sweep — dark pattern detection, AI trust audit, content/tone review, and cross-device responsive check in one comprehensive protection pass."
phase: "3"
phase_step: "3.5"
phase_name: "AUDIT"
step_label: "Step 16 of 30"
---

# Expose — Comprehensive Fortification Sweep

Scan a product across all defensive dimensions in a single pass: dark pattern detection, AI trust audit, content/tone review, and cross-device responsive check. This command combines what were previously 4 separate audits into one comprehensive fortification sweep that protects users, reduces regulatory risk, and ensures quality across every device.

## Analysis Protocol

### Step 0: Gather Context

Before scanning, collect:

1. **Input**: Code (file paths or pasted), screenshots, or URL to analyze.
2. **Product type**: Does it have AI features? Commerce/payments? Forms/data collection? Subscriptions?
3. **Target markets**: Affects regulatory requirements (FTC for US, GDPR for EU, DSA, California CCPA).
4. **Prior Sumi outputs**: Consume `/12-audit`, `/13-think`, `/14-access`, `/15-flow` if available.

If the user provides limited context, proceed with what's available and flag assumptions. The scan adapts based on product type — AI trust audit is skipped if no AI features are present.

### Step 1: DARK PATTERN SCAN

Using `ux-ethics-content-strategy` skill + `ui-pattern-intelligence` -> `anti-pattern-encyclopedia.md`:

Scan for 20+ deceptive design categories:

**Coercion patterns**:
- Confirmshaming — guilt-tripping the user into opting in ("No thanks, I hate saving money")
- Forced continuity — free trial converts to paid without clear warning
- Roach motel — easy to sign up, impossible to cancel
- Forced action — requiring account creation or social sharing to proceed

**Sneaking patterns**:
- Hidden costs — fees revealed only at checkout
- Sneak into basket — items added without explicit consent
- Bait and switch — advertising one thing, delivering another
- Hidden subscription — recurring charge buried in terms

**Interface manipulation**:
- Trick questions — double negatives or confusing opt-in/opt-out toggles
- Misdirection — visual design draws attention away from important information
- Disguised ads — ads styled to look like content or navigation
- False hierarchy — making the company-preferred option visually dominant

**Privacy violations**:
- Privacy zuckering — confusing privacy settings that default to maximum data sharing
- Address book leeching — requesting contacts without clear purpose
- Surveillance capitalism indicators — excessive data collection for the service provided

**Urgency/scarcity**:
- Fake urgency — countdown timers with no real deadline
- Fake scarcity — "Only 2 left!" without real inventory limits
- Fake social proof — fabricated reviews or user counts

**Obstruction**:
- Hard to cancel — cancellation flow longer or harder than signup
- Hidden settings — important controls buried deep in settings
- Comparison prevention — making plan comparison deliberately difficult

**For each detected pattern**:
- Pattern name and category
- Where it appears (specific component, screen, or flow)
- Severity classification:
  - **Illegal**: Violates current regulation (FTC, GDPR Art. 25, DSA)
  - **Deceptive**: Misleads users about what will happen
  - **Manipulative**: Uses psychology against the user's interest
  - **Questionable**: Gray area — could be interpreted as dark pattern
- Regulatory risk: specific laws/regulations that apply
- Ethical redesign alternative: how to achieve the business goal without the dark pattern

If no dark patterns are found, confirm: "Clean — no dark patterns detected across 20 categories scanned."

### Step 2: AI TRUST AUDIT

**Skip this section entirely if the product has no AI features.** Output "N/A — no AI features detected" and move to Step 3.

If AI features are present, audit using `ai-spatial-voice-ux` skill + `agentic-ai-generative-ux` skill:

**Transparency** (score 1-10):
- Does the user know when AI is making or influencing decisions?
- Are AI-generated outputs labeled as such?
- Is the data source for AI decisions disclosed?
- Are limitations of the AI clearly communicated?

**Control** (score 1-10):
- Can the user override or correct AI decisions?
- Can the user opt out of AI features?
- Can the user provide feedback on AI accuracy?
- Are there human escalation paths?

**Safety** (score 1-10):
- What happens when AI is wrong? Is there graceful degradation?
- Are there guardrails against harmful outputs?
- Is there bias monitoring or mitigation?
- Could the AI discriminate based on protected characteristics?

**Usability** (score 1-10):
- Does the AI enhance or complicate the user experience?
- Are AI interactions consistent with the rest of the product?
- Is the confidence level of AI outputs communicated?
- Does the user understand how to interact with AI features?

**Overall AI Trust Score**: Average of 4 dimensions.

### Step 3: CONTENT & TONE REVIEW

Using `ux-ethics-content-strategy` skill:

Scan all visible UI text for:

**Clarity**:
- Is every label, button, and message unambiguous?
- Can the user predict what will happen before they act?
- Are instructions necessary, or is the UI self-explanatory?
- Flag any jargon, acronyms without explanation, or insider language

**Tone consistency**:
- Does the voice match throughout the product? (casual in one place, formal in another = inconsistency)
- Does the tone match the product's brand and sector expectations?
- Is the tone appropriate for the context? (playful error messages for banking = mismatch)

**Inclusive language**:
- No gendered assumptions (he/she when they would work)
- No ableist language ("see below" when "refer to" works for screen readers)
- No cultural bias or idioms that don't translate
- No age-related assumptions

**Error messages**:
- Helpful and specific? (not "Something went wrong" or "Error 500")
- Do they tell the user what happened AND what to do next?
- Friendly tone without blame? ("We couldn't find that page" not "You entered a bad URL")
- Provide a recovery path (retry button, support link, alternative action)?

**CTAs (calls to action)**:
- Action-oriented with clear outcome? ("Create Account" not "Submit")
- Consistent verb patterns? (not mixing "Save", "Update", "Apply" for similar actions)
- Button text matches the result? ("Delete Account" not "Continue" for destructive actions)

**Readability**:
- Flesch-Kincaid grade level appropriate for audience?
- Sentence length reasonable (avg <20 words)?
- Paragraph length manageable (max 3-4 sentences in UI)?

**i18n readiness**:
- Text externalized from code (not hardcoded strings)?
- Date/number formatting locale-aware?
- Text expansion room (German/French can be 30% longer)?
- No text embedded in images?
- RTL layout considerations if applicable?

**Provide specific rewrites for any failing text.** Format: "Current: [X] -> Recommended: [Y] — Reason: [Z]"

### Step 4: RESPONSIVE & CROSS-DEVICE CHECK

Using `platform-visual-standards` skill:

Check at 5 breakpoints:

**Mobile (375px)**:
- Layout: Single column? Content reflow correct?
- Touch targets: >= 44px on all interactive elements?
- Typography: Readable? Line length <= 75 characters?
- Navigation: Mobile-appropriate pattern (tab bar, hamburger)?
- Images: Responsive, not overflowing container?
- Horizontal scroll: Present? (almost always an anti-pattern)
- Input modes: Touch-optimized? (large inputs, appropriate keyboards)
- Bottom nav or FAB for primary actions?

**Tablet (768px)**:
- Layout: Adapts to 2-column or adjusts spacing?
- Split view or sidebar patterns where appropriate?
- Touch and pointer input both work?
- Modal sizing appropriate (not full-screen on tablet)?

**Laptop (1024px)**:
- Layout: Multi-column with sidebar if applicable?
- Hover states all present and visible?
- Keyboard navigation fully functional?
- Right-click context menus where expected?

**Desktop (1280px)**:
- Full layout as designed?
- Max-width container present?
- Comfortable information density?
- All features accessible?

**Wide (1536px+)**:
- Content constrained to readable width?
- No awkward stretched elements?
- Grid fills proportionally?
- Images don't upscale beyond source resolution?

**Cross-cutting checks**:
- No horizontal scrolling at any breakpoint
- Print stylesheet if the content is printable
- Orientation changes handled (portrait to landscape)
- Input mode transitions (touch to keyboard to mouse)

Flag any breakpoint where the experience degrades with specific issues.

### Step 5: FORTIFICATION SCORE

Score the product across 4 defense dimensions:

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Ethics (dark patterns) | 30% | 1-10 | Based on findings from Step 1 |
| Trust (AI) | 20% | 1-10 or N/A | Based on findings from Step 2 |
| Content quality | 25% | 1-10 | Based on findings from Step 3 |
| Device coverage | 25% | 1-10 | Based on findings from Step 4 |

**Overall Fortification Score**: Weighted average (if Trust is N/A, redistribute weight to other dimensions: Ethics 35%, Content 35%, Devices 30%).

**Score interpretation**:
- 9-10: Ship-ready — minimal risk, comprehensive coverage
- 7-8: Solid — minor issues, no critical gaps
- 5-6: Needs work — notable gaps that could affect users or create risk
- 3-4: Risky — significant issues across multiple dimensions
- 1-2: Dangerous — critical dark patterns, accessibility failures, or regulatory risk

## Output Format

```
### Phase Position
> **Phase 3: AUDIT** | Step 16 of 30 | `/16-expose`
>
> `/15-flow` -> **`/16-expose`** -> `/17-tokens`

---

## Fortification Sweep

### Summary

| Dimension | Score | Issues | Critical |
|-----------|-------|--------|----------|
| Ethics | [X/10] | [N] | [N] |
| Trust | [X/10 or N/A] | [N] | [N] |
| Content | [X/10] | [N] | [N] |
| Devices | [X/10] | [N] | [N] |

**Overall Fortification: [X/10]**

---

### Dark Pattern Scan

[For each finding:]

#### [Pattern Name] — [Severity: Illegal/Deceptive/Manipulative/Questionable]
- **Location**: [Component/screen/flow]
- **What's happening**: [Description]
- **Regulatory risk**: [Specific laws/regulations]
- **Ethical alternative**: [How to achieve the goal without the dark pattern]

[Or: "Clean — no dark patterns detected across 20 categories scanned."]

---

### AI Trust Audit

| Dimension | Score | Key Findings |
|-----------|-------|-------------|
| Transparency | [X/10] | [Findings] |
| Control | [X/10] | [Findings] |
| Safety | [X/10] | [Findings] |
| Usability | [X/10] | [Findings] |
| **Overall AI Trust** | **[X/10]** | |

[Or: "N/A — no AI features detected."]

---

### Content & Tone Review

#### Clarity Issues
[Findings with rewrites]

#### Tone Consistency
[Findings]

#### Inclusive Language
[Findings with rewrites]

#### Error Messages
[Findings with rewrites]

#### CTAs
[Findings with rewrites]

#### Readability
[Score and findings]

#### i18n Readiness
[Findings]

---

### Responsive & Cross-Device

#### Mobile (375px)
[Findings: layout, touch targets, typography, navigation, overflow]

#### Tablet (768px)
[Findings]

#### Laptop (1024px)
[Findings]

#### Desktop (1280px)
[Findings]

#### Wide (1536px+)
[Findings]

---

### Fortification Punch List

| # | Dimension | Severity | Issue | Location | Fix |
|---|-----------|----------|-------|----------|-----|
| 1 | Ethics | Illegal | Confirmshaming on newsletter | Modal dismiss CTA | Change "No thanks, I don't like deals" to "No thanks" |
| 2 | Content | Critical | Vague error message | Login form | Change "Error" to "Incorrect email or password. Try again or reset your password." |
| 3 | Devices | Major | Touch targets 32px | Mobile nav | Increase to 44px minimum |
| 4 | Trust | Major | AI decisions unlabeled | Recommendations | Add "Suggested for you by AI" label |
[complete prioritized list]

---

### Next Steps
1. **Fix** critical findings before building further — especially any illegal dark patterns
2. **Then** -> `/17-tokens` — Begin building with a clean, fortified foundation
3. **Or** -> `/19-ship` — Rebuild flagged components with ethical alternatives

**Run `/next` to continue the journey.**
```

## Quality Gates

The output MUST include:
- [ ] Dark pattern scan covering 20+ deceptive design categories
- [ ] AI trust audit included if product has AI features, cleanly skipped if not
- [ ] Content review with specific rewrites for every failing text instance
- [ ] Responsive check at 5+ breakpoints with specific findings per breakpoint
- [ ] Per-dimension scores with justification (not arbitrary numbers)
- [ ] Prioritized punch list with severity and specific fix instructions
- [ ] Regulatory risk flagged where applicable with specific law/regulation citations

The output MUST NOT include:
- Vague findings ("content could be clearer") — every issue must cite specific text and a rewrite
- Dark pattern scan that checks fewer than 20 categories
- AI trust audit on products without AI (must skip cleanly)
- Responsive findings without specific breakpoint data
- Scores without justification — every score must explain what earned or lost points
- Missing punch list — every finding must have a fix

## Cross-References

When performing the fortification sweep, draw knowledge from:
- `ux-ethics-content-strategy` skill — dark pattern taxonomy, ethical design principles, content strategy, tone of voice
- `ai-spatial-voice-ux` skill — AI transparency, trust patterns, voice UX ethics
- `agentic-ai-generative-ux` skill — AI safety guardrails, agent trust, generative UI ethics
- `platform-visual-standards` skill — responsive standards per device type, platform conventions
- `accessibility-inclusive-design` skill — inclusive language, WCAG compliance, universal design
- `cross-cultural-i18n-ux` skill — i18n readiness, cultural sensitivity, localization patterns
- `ui-pattern-intelligence` -> `anti-pattern-encyclopedia.md` — comprehensive dark pattern reference
- `cognitive-psychology-ux` skill — manipulation techniques, cognitive bias exploitation detection

## Next Step

**Next** -> `/17-tokens` (4.1) — Build the design token system with a clean, fortified foundation

**Alternatives**:
- `/19-ship` — Rebuild flagged components with ethical alternatives
- `/14-access` — Deep accessibility audit if inclusive language issues were found
- `/12-audit` — Revisit heuristic audit after fixes
- `/guide` — See the full journey map
