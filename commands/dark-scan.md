---
description: Dark pattern detection — scan any UI for 20+ deceptive design categories with regulatory risk analysis and ethical redesign alternatives.
phase: "3"
phase_step: "3.1"
phase_name: "FORTIFY"
step_label: "Step 1 of 4"
---

# Dark Scan — Dark Pattern Detection

Dedicated ethical audit that systematically scans a UI for deceptive design patterns, assesses regulatory risk, and provides ethical redesign alternatives for every finding.

## Detection Protocol

1. **Scan against the full dark pattern taxonomy** (20+ categories):

   | Category | What to Look For |
   |----------|-----------------|
   | Confirmshaming | Guilt-laden opt-out language ("No, I don't want to save money") |
   | Roach Motel | Easy to sign up, deliberately hard to cancel or delete account |
   | Trick Questions | Double negatives, confusing toggles, pre-checked opt-ins |
   | Hidden Costs | Fees, taxes, or charges revealed only at the final step |
   | Forced Continuity | Free trial auto-converts to paid without clear warning |
   | Bait and Switch | Promised action does something different than expected |
   | Misdirection | Visual emphasis guides users away from their intended choice |
   | Friend Spam | Requesting contact access and messaging contacts without clear consent |
   | Disguised Ads | Advertisements styled as content, navigation, or system UI |
   | Privacy Zuckering | Making privacy-eroding options the default or easiest path |
   | Preselected Consent | Opt-in checkboxes pre-checked for newsletters, data sharing, tracking |
   | Obstruction | Making an undesirable action (unsubscribe, delete) require excessive steps |
   | Sneaking | Adding items to cart, changing selections, or altering terms quietly |
   | Fake Urgency | Countdown timers that reset, "only 2 left" when inventory is unlimited |
   | Fake Social Proof | Fabricated reviews, inflated user counts, fake "someone just bought" popups |
   | Forced Action | Requiring account creation, app install, or data sharing to access basic content |
   | Nagging | Repeated interruptions asking user to do something they already declined |
   | Interface Interference | Making the "wrong" choice visually prominent (bright "Accept All" vs dim "Manage") |
   | Drip Pricing | Displaying a base price, then adding mandatory fees incrementally |
   | Hidden Subscription | Burying subscription terms in fine print, making one-time purchase unclear |
   | Comparison Prevention | Making plan comparison deliberately difficult to push users to a specific tier |
   | Immortal Accounts | Making account deletion impossible or requiring calling a phone number |

2. **Classify each finding by severity**:
   - **Manipulative** (Red): Deliberately designed to deceive — causes financial harm, data loss, or coerced consent
   - **Misleading** (Orange): Likely to confuse a reasonable user — may not be intentional but is harmful
   - **Grey Area** (Yellow): Could be interpreted as dark pattern depending on context and intent
   - **Clean** (Green): Pattern exists but implementation is ethical and transparent

3. **Perform regulatory risk assessment**:
   - **FTC Act Section 5** (US): Prohibits unfair or deceptive acts — check for material misrepresentation, omission of material information, unfair practices
   - **EU Digital Services Act**: Bans interface designs that deceive, manipulate, or materially distort user decision-making
   - **GDPR Consent Requirements** (EU): Consent must be freely given, specific, informed, unambiguous — pre-checked boxes violate Article 7
   - **California Privacy Rights Act (CPRA)**: Dark patterns that subvert consumer privacy choices are non-compliant
   - **UK Online Safety Act**: Platforms must not design features that harm users through deceptive practices
   - **FTC Negative Option Rule** (updated 2024): Requires clear disclosure, informed consent, and easy cancellation for subscriptions
   - Flag specific regulatory violations with citation

4. **Generate ethical redesign alternatives**:
   - For every finding rated Manipulative or Misleading, provide a concrete ethical alternative
   - Include visual description or code showing the ethical version
   - Explain why the ethical version still achieves the business goal (retention, conversion) without deception
   - Reference case studies where ethical redesigns improved metrics (when available)

5. **Assess cumulative manipulation load**:
   - A single grey-area pattern may be acceptable; multiple grey-area patterns compound into manipulation
   - Score the overall "dark pattern density" — how many patterns per screen or per flow step
   - Check if dark patterns cluster around high-value user decisions (payment, consent, cancellation)

## Output Format

```
### Phase Position
> **Phase 3: FORTIFY** | Step 1 of 4 | `/dark-scan`
> *NNG: Ethical Design Review | Visual: Regulatory Compliance*
>
> **Phase 2** `/flow` (2.4) → **`/dark-scan` (3.1)** → `/trust-scan` (3.2)

## Dark Scan: [Product/Screen Name]

### Overall Rating: [Clean / Caution / Violation]
- **Patterns detected**: [X total] ([X manipulative, X misleading, X grey-area])
- **Regulatory risk level**: [Low / Medium / High / Critical]
- **Jurisdictions at risk**: [US FTC, EU DSA, GDPR, CPRA, UK OSA]

### Dark Pattern Density
- **Per screen**: [X patterns across Y screens]
- **Clustering**: [Where patterns concentrate — e.g., checkout, cancellation, consent]

### Findings

#### Manipulative (Must Eliminate)
**[Pattern Name]** — [Location in UI]
- **What it does**: [Description of the deceptive behavior]
- **Who it harms**: [Which users are affected and how]
- **Regulatory risk**: [Specific law/regulation violated]
- **Ethical alternative**: [Concrete redesign with code or visual description]
- **Business case**: [Why the ethical version can still achieve the goal]

#### Misleading (Should Fix)
[Same format]

#### Grey Area (Review with Legal)
[Same format]

#### Clean Patterns
[Patterns that were checked and found to be ethically implemented]

### Regulatory Compliance Checklist
- [ ] All consent is freely given, not pre-selected (GDPR Art. 7)
- [ ] Cancellation is as easy as signup (FTC Negative Option Rule)
- [ ] All costs disclosed before commitment (FTC Act Section 5)
- [ ] No interface interference on consent dialogs (EU DSA)
- [ ] Privacy-protective options are not visually deprioritized (CPRA)
- [ ] Account deletion is accessible and functional (GDPR Art. 17)

### Recommended Actions
[Prioritized list: immediate regulatory fixes, then ethical improvements]
```

## Cross-References
When scanning for dark patterns, draw evaluation criteria from:
- `ux-ethics-content-strategy` skill for ethical design frameworks, consent design, and persuasion vs. manipulation boundaries
- `cognitive-psychology-ux` skill for cognitive biases exploited by dark patterns (loss aversion, anchoring, default bias, social proof)
- `accessibility-inclusive-design` skill for intersection of accessibility and dark patterns (users with cognitive disabilities are disproportionately affected)

## Next Step

**Next** → `/trust-scan` (3.2) — Check AI feature trust and safety

**Alternatives**:
- `/copy-check` (3.3) — Skip ahead to content audit if no AI features
- `/responsive` (3.4) — Jump to responsive audit
- `/guide` — See the full 20-step journey
