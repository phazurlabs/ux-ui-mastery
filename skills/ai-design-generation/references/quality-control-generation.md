# Quality Control for AI-Generated Designs

This reference covers how to evaluate, score, iterate, and approve AI-generated design output. Without quality control, AI generation produces output that looks impressive at first glance but fails under professional scrutiny. This framework ensures generated designs meet production standards.

---

## Visual Scoring Integration

Every AI-generated design should be scored against the 10-dimension visual scoring framework (from visual-design-mastery). This provides objective, repeatable quality assessment.

### The 10 Scoring Dimensions

| # | Dimension | What It Measures | Key Questions |
|---|-----------|-----------------|---------------|
| 1 | **Layout & Composition** | Spatial organization, grid adherence, visual balance | Is the layout structured on a grid? Is there clear visual hierarchy? Is whitespace intentional? |
| 2 | **Typography** | Font choices, type scale, readability, hierarchy | Is the type scale consistent? Are headings distinguishable from body? Is line-height comfortable? |
| 3 | **Color** | Palette coherence, contrast, intentional use | Do colors follow a system? Is contrast sufficient? Are accent colors used purposefully? |
| 4 | **Spacing & Rhythm** | Consistent spacing, vertical rhythm, breathing room | Does spacing follow a base grid? Is spacing consistent between similar elements? |
| 5 | **Visual Hierarchy** | Information priority, eye flow, emphasis | Is the most important element the most prominent? Can you scan the page quickly? |
| 6 | **Component Quality** | UI element design, states, interactivity cues | Do buttons look clickable? Are inputs clearly defined? Are interactive elements distinguishable? |
| 7 | **Consistency** | Cross-screen coherence, pattern reuse, token adherence | Does this screen feel like it belongs to the same product as other screens? |
| 8 | **Platform Fit** | Platform convention adherence, native feel | Does this feel native to the target platform? Are conventions followed? |
| 9 | **Content Quality** | Real content, appropriate density, tone | Is the content realistic? Is the information density appropriate for the use case? |
| 10 | **Polish & Craft** | Attention to detail, pixel precision, refinement | Are edges crisp? Are shadows consistent? Does it feel professionally crafted? |

### Scoring Scale (Per Dimension)

| Score | Level | Description |
|-------|-------|-------------|
| 1-2 | Poor | Fundamentally broken — wrong patterns, unreadable, confusing |
| 3-4 | Below Average | Functional but clearly amateur — inconsistent, rough |
| 5-6 | Average | Acceptable for internal/draft use — competent but unpolished |
| 7-8 | Good | Professional quality — suitable for client presentation and production |
| 9-10 | Excellent | Award-worthy — distinctive, polished, memorable |

### Minimum Acceptable Scores by Use Case

| Use Case | Overall Minimum | No Dimension Below | Notes |
|----------|----------------|-------------------|-------|
| Wireframe / concept exploration | 4/10 | 2/10 | Just needs to communicate the idea |
| Internal prototype | 6/10 | 4/10 | Functional, demonstrates concept |
| User testing prototype | 6/10 | 5/10 | Must not distract from usability testing |
| Client presentation | 7/10 | 5/10 | Professional quality expected |
| Production deployment | 8/10 | 6/10 | Launch-ready, polished |
| Portfolio / showcase | 9/10 | 7/10 | Represents your best work |

---

## Automated Quality Checks

Run these 10 checks on every generated design. Each check is pass/fail with specific criteria.

### Check 1: Color Consistency
**What:** Do the colors in the generated output match the specified design tokens?
**How:** Compare key element colors against the style lock / design tokens.
**Pass criteria:** All primary UI colors (backgrounds, text, buttons, borders) match specified hex values within a tolerance of +/- 5% lightness.
**Common failure:** Generation uses "approximately blue" instead of the exact #6366F1 specified.
**Fix:** Include exact hex values in the prompt, not color names. Say "#6366F1 indigo" not just "indigo."

### Check 2: Typography Consistency
**What:** Is the correct font family, weight, and scale used?
**How:** Verify heading sizes, body text sizes, font weights against specification.
**Pass criteria:** Font family matches specification. Type scale steps are consistent (not random sizes). Weight hierarchy is clear (headings heavier than body).
**Common failure:** Generation uses a similar but different font, or inconsistent sizes.
**Fix:** Specify exact font name, sizes in px, and weights as numbers (400, 600, 700).

### Check 3: Spacing Consistency
**What:** Does spacing follow the specified grid system?
**How:** Measure padding, margins, and gaps between elements.
**Pass criteria:** All spacing values are multiples of the base grid (usually 4px or 8px). No random spacing values. Consistent padding within similar components.
**Common failure:** Spacing "looks about right" but uses inconsistent values (13px, 17px, 22px instead of 12, 16, 24).
**Fix:** Specify exact spacing values and state "8px base grid, all spacing must be multiples of 8."

### Check 4: Component Correctness
**What:** Do components match platform conventions and standard patterns?
**How:** Compare buttons, inputs, navigation, cards against platform guidelines.
**Pass criteria:** Components follow the target platform's conventions (iOS HIG, Material 3, web standards). Interactive elements are clearly distinguishable. Standard patterns are used correctly.
**Common failure:** iOS-style components on an Android screen, or vice versa.
**Fix:** Explicitly state platform and version in the prompt. Reference specific component guidelines.

### Check 5: Content Quality
**What:** Is there real or realistic content, not lorem ipsum?
**How:** Read all text content in the generated design.
**Pass criteria:** All text is meaningful and realistic. Names, numbers, dates, and descriptions are plausible. No "lorem ipsum" or obviously placeholder text.
**Common failure:** Generation fills long text areas with lorem ipsum or repetitive placeholder text.
**Fix:** Provide actual content in the prompt for key areas. For dynamic content, specify realistic examples.

### Check 6: State Coverage
**What:** Are the required interaction states shown?
**How:** Check whether hover, active, disabled, error, loading, and empty states are present.
**Pass criteria:** All states requested in the prompt are shown. At minimum, the default state is clear and complete.
**Common failure:** Only the default/happy-path state is generated.
**Fix:** Explicitly list required states in the prompt: "Show: default state, hover state on primary button, error state on email input, loading skeleton for the data table."

### Check 7: Accessibility Baseline
**What:** Does the design meet minimum accessibility requirements?
**How:** Check text contrast ratios, touch target sizes, and color-only information.
**Pass criteria:** Text contrast meets WCAG AA (4.5:1 for normal text, 3:1 for large text). Touch targets are minimum 44x44pt (iOS) or 48x48dp (Android). Information is not conveyed by color alone.
**Common failure:** Light gray text on white background. Small touch targets. Red/green only for status.
**Fix:** Include "WCAG AA contrast minimum 4.5:1 for text" and minimum touch target size in the prompt.

### Check 8: Responsive Hints
**What:** Does the layout suggest responsive adaptability?
**How:** Evaluate whether the layout could reflow for different viewport widths.
**Pass criteria:** Grid-based layout that could reflow. No fixed-width elements that would break on smaller screens. Content priority is clear (what would stack on mobile?).
**Common failure:** Desktop-only layout with no consideration for smaller viewports.
**Fix:** If responsive is important, explicitly request it. Or generate separate mobile and desktop versions.

### Check 9: Pattern Correctness
**What:** Do the UI patterns match what is expected for the sector and screen type?
**How:** Compare patterns against the sector-style-intelligence and ui-pattern-intelligence references.
**Pass criteria:** Navigation pattern is appropriate for the platform. Data display pattern matches the data type. Form pattern follows conventions. No anti-patterns.
**Common failure:** Using a carousel where a grid would be more usable. Using tabs where a list would work better.
**Fix:** Specify which UI patterns to use in the prompt. Reference specific pattern names from the pattern catalog.

### Check 10: Coherence
**What:** Does the screen feel like part of a unified product?
**How:** View the screen in context of other screens in the project. Assess overall "feel."
**Pass criteria:** The screen uses the same visual language as other screens. It feels like one designer designed the entire product. No element feels out of place.
**Common failure:** A screen that is individually well-designed but does not match the rest of the project.
**Fix:** Always use the style lock document. Reference previous screens in the prompt. Extract design context from the first approved screen.

---

## Common Generation Failures and Fixes

### Detailed Failure-Fix Matrix

| # | Failure | Root Cause | Prompt Fix | Alternative |
|---|---------|-----------|------------|-------------|
| 1 | Generic/bland design | Vague or high-level prompt | Add specific product references, exact design tokens, sector keywords. "In the style of Mercury bank" not just "banking app." | Generate 3 variants, pick best, refine |
| 2 | Inconsistent style across screens | No design context propagation | Create a style lock document. Extract design context from the first screen. Include the full style lock in every prompt. | Generate all screens in one session |
| 3 | Wrong platform conventions | Platform not specified or underspecified | Add "iOS 26 Liquid Glass" or "Material 3 Expressive" explicitly. List platform-specific elements: tab bar, navigation drawer, etc. | Reference platform design gallery |
| 4 | Too decorative / cluttered | Over-specified aesthetic or too many decorative keywords | Add "clean, minimal, functional, content-first." Remove decorative descriptors. Add "no decorative illustrations, no gradients, no patterns." | Simplify the prompt significantly |
| 5 | Too sparse / empty | Under-specified content | Add more content to the prompt. Fill every section with realistic data. Specify information density: "data-dense" or "content-rich." | Provide exact content for each area |
| 6 | Poor typography hierarchy | No type scale specified | Add exact font sizes, weights, and line-heights for each level (H1, H2, body, small, caption). State "clear typographic hierarchy with 3+ distinct levels." | Specify a known type scale (e.g., Material 3) |
| 7 | Wrong color palette | Colors described by name, not value | Use exact hex values: "#6366F1" not "indigo." Include the complete color palette with usage rules. | Provide a color reference image |
| 8 | Missing interaction states | Only default state described | Explicitly list every required state: "Show default, hover, active, focus, disabled, error, loading, and empty states." | Generate states as separate requests |
| 9 | Inaccessible contrast | No accessibility requirement stated | Add "WCAG AA contrast ratios: minimum 4.5:1 for normal text, 3:1 for large text. Minimum 44pt touch targets." | Run contrast checker on output |
| 10 | Not sector-appropriate | No sector context in prompt | Add sector keywords (see sector-aware prompting). Reference 2-3 competitor products. Describe target user and their expectations. | Run /taste first for sector direction |
| 11 | Uncanny / artificial feel | Over-reliance on AI without human design judgment | Reduce prompt complexity. Use fewer style keywords. Add stronger product references. Consider using output as a reference for manual implementation. | Use as wireframe, polish manually |
| 12 | Layout does not scan | No visual hierarchy specified | Specify element priority: "Most prominent: [X]. Secondary: [Y]. Tertiary: [Z]." Add size relationships: "headline 3x larger than body text." | Reference a specific layout pattern |
| 13 | Content feels fake | Placeholder or generic content | Write real copy for all headlines, descriptions, CTAs. Use realistic data (real names, plausible numbers, actual dates). | Hire a content writer for key content |
| 14 | Inconsistent iconography | Icons generated individually | Generate all icons with same prompt prefix (see asset generation guide). Or specify an existing icon set (Lucide, Phosphor). | Use a single open-source icon set |
| 15 | Shadow/depth inconsistency | No shadow system specified | Define shadow levels: "sm, md, lg shadows. Cards use sm. Modals use lg. No other shadow values." | Specify a known shadow system (Material 3) |

---

## Iteration Strategies

### Strategy 1: Score-Based Iteration
The most systematic approach. Score the generated design, identify the weakest dimension, and adjust the prompt to specifically target that dimension.

```
Round 1: Generate → Score
  Overall: 6.2/10
  Weakest: Typography (4/10) — inconsistent sizes, wrong font weight

Round 2: Add to prompt:
  "Typography must be precise: Inter font family.
   H1: 32px / 1.2 / 700 weight.
   H2: 24px / 1.3 / 600 weight.
   Body: 16px / 1.5 / 400 weight.
   Small: 14px / 1.5 / 400 weight.
   Caption: 12px / 1.4 / 500 weight.
   Clear hierarchy with at least 3 visible levels."
  Generate → Score
  Overall: 7.1/10
  Weakest: Spacing (5/10) — inconsistent padding

Round 3: Add to prompt:
  "Strict 8px spacing grid. Component internal padding: 16px.
   Between sections: 32px. Between related elements: 8px.
   Between unrelated elements: 24px. No spacing value that is
   not a multiple of 8."
  Generate → Score
  Overall: 7.8/10 — passes threshold
```

### Strategy 2: A/B Generation
Generate 2-3 variants with slightly different prompts, score all, pick the best.

```
Variant A: Original prompt
Variant B: Original + "in the style of Stripe" (adds polish benchmark)
Variant C: Original + "minimal, content-first, no decoration" (reduces clutter)

Score all three:
  A: 6.5/10
  B: 7.2/10 — best overall
  C: 6.8/10 — cleaner but too sparse

Use B as the base for further iteration.
```

### Strategy 3: Progressive Refinement
Start at low fidelity and progressively increase.

```
Round 1: "Generate a wireframe-level layout..." → Validate structure and hierarchy
Round 2: "Generate a medium-fidelity mockup..." → Validate style direction
Round 3: "Generate a high-fidelity screen..." → Validate production quality
```

This prevents wasting high-fidelity generation attempts on a fundamentally wrong layout.

### Strategy 4: Reference Anchoring
When the style keeps drifting, anchor it to a stronger reference.

```
Before: "A modern fintech dashboard with clean design"
After:  "A fintech dashboard that looks EXACTLY like Mercury's dashboard — same layout density, same minimalism, same dark sidebar, same typography weight"
```

Stronger references produce more consistent results. Use "exactly like" for strong matching, "inspired by" for loose influence.

### Strategy 5: Constraint Tightening / Loosening
If output is too creative, add constraints. If too bland, remove them.

```
Too creative/chaotic: Add constraints
  + "No gradients, no decorative elements, no illustrations in the UI"
  + "Maximum 3 colors: primary, surface, text"
  + "Straight lines only, no curved sections"

Too bland/generic: Remove constraints
  - Remove "minimal" and "clean"
  + Add "distinctive, memorable, with personality"
  + Add "subtle gradient on the hero section"
  + Add a strong style reference ("with the visual character of Arc browser")
```

---

## When to Stop Iterating and Hand-Craft

Stop AI generation and switch to manual design or direct coding when:

### After 3 Iterations with No Score Improvement
If the overall score has not improved by at least 0.5 points after 3 iteration rounds, the issue is likely beyond what prompt engineering can fix. The generation model may not be capable of the specific output you need.

**Action:** Use the best generated version as a visual reference and implement manually with /ship.

### When the Issue Is Component-Level Detail
AI generation works at the screen level, not the component level. If the issue is button states, input field behavior, dropdown menus, or other component-level details, generation will not solve it.

**Action:** Accept the screen layout from generation and build components manually with /ship.

### When Accessibility Requirements Are Complex
AI cannot reliably generate accessible designs. It may produce sufficient contrast sometimes, but it cannot guarantee ARIA roles, focus order, screen reader behavior, or keyboard navigation.

**Action:** Generate the visual design, then audit and fix accessibility manually with /include.

### When Custom Interactions Are Required
AI generation produces static output. If the design requires complex interactions (drag-and-drop, gesture-based navigation, animated transitions between states), generation cannot show these.

**Action:** Use generation for the static states, then specify interactions manually with /motion.

### When Brand Guidelines Are Very Specific
If the brand has pixel-precise guidelines (exact logo placement, specific margin values, prescribed color combinations for specific contexts), generation is unlikely to match exactly.

**Action:** Use generation as a rapid concept exploration tool, then implement the approved concept with exact brand compliance manually.

### When "Close Enough" Is Good Enough
Often the best use of AI generation is to get 70% of the way there, then use it as a reference for manual implementation. If a generated screen communicates the right idea, layout, and style, it has done its job even if it is not pixel-perfect.

**Action:** Screenshot the generated design, use it as a reference alongside the design spec, and implement with /ship.

---

## Human-in-the-Loop Review Process

AI should never be the final judge of design quality. Every generated design needs human review.

### Review Protocol

```
Step 1: Generate
  Run the generation with the prepared prompt
  Capture the output (screenshot or preview URL)

Step 2: Auto-Score
  Run the 10-dimension visual scoring
  Run the 10 automated quality checks
  Generate a score card with pass/fail for each check

Step 3: Present to User
  Show the generated design with:
  - Overall score (X/10)
  - Per-dimension scores
  - Pass/fail on each quality check
  - Specific findings (what is good, what needs improvement)
  - Recommendation (approve / iterate / hand-craft)

Step 4: Gather Feedback
  Ask the user:
  - "What do you like about this design?"
  - "What would you change?"
  - "Does this match your vision for the product?"
  - "Any specific elements that feel wrong?"

Step 5: Adjust and Regenerate
  Based on user feedback:
  - Translate subjective feedback into prompt adjustments
  - "It feels too corporate" → add warmer colors, rounded shapes, friendly language
  - "The layout is too busy" → reduce content density, increase whitespace
  - "I want it more like [Product]" → add specific product reference

Step 6: Repeat Until Approved
  Maximum 3 iteration rounds with user feedback
  If not approved after 3 rounds, recommend hand-craft approach

Step 7: Approve or Pivot
  User either approves the design for production or
  decides to use it as a reference for manual implementation
```

### Feedback Translation Guide

| User Says | Design Translation | Prompt Adjustment |
|-----------|-------------------|-------------------|
| "It feels too corporate" | Needs warmth and personality | Add warm colors, rounded corners, friendly illustrations, conversational content |
| "It feels too playful" | Needs professionalism and restraint | Remove decorative elements, use neutral colors, straighten corners, formal content |
| "It's too busy" | Information density too high | Increase whitespace, reduce content per section, larger margins, fewer elements |
| "It's too empty" | Information density too low | Add more content, reduce whitespace, more cards/sections, denser layout |
| "It looks dated" | Needs modern design patterns | Update to current platform conventions, add micro-interactions, use modern type scale |
| "It looks generic" | Needs distinctive character | Add stronger style reference, unique color choices, distinctive typography, signature patterns |
| "I can't find the main action" | Weak visual hierarchy | Make primary CTA larger, more contrast, above the fold, remove competing elements |
| "The colors feel wrong" | Palette mismatch | Adjust specific colors based on feedback, try a different seed/temperature, reference a product they like |

---

## Quality Gate for Production Use

Before any AI-generated design can be considered production-ready, it must pass every item in this gate. This is a non-negotiable checklist.

### Visual Quality
- [ ] Overall visual score >= 8/10
- [ ] No single dimension below 6/10
- [ ] All 10 automated quality checks passed

### Accessibility
- [ ] WCAG AA contrast ratios verified (4.5:1 text, 3:1 large text, 3:1 UI components)
- [ ] Touch targets meet platform minimum (44pt iOS, 48dp Android)
- [ ] Focus indicators present on all interactive elements
- [ ] Information not conveyed by color alone
- [ ] Accessibility audit completed (/include)

### Platform Compliance
- [ ] Platform conventions verified (iOS HIG, Material 3, or web standards)
- [ ] Navigation pattern matches platform expectations
- [ ] Component patterns match platform component libraries
- [ ] Safe areas respected (Dynamic Island, home indicator, status bar)

### Design System Adherence
- [ ] All colors from the approved design token palette
- [ ] All fonts from the approved typography system
- [ ] All spacing on the approved grid system
- [ ] All border radii from the approved scale
- [ ] All shadows from the approved elevation system

### Content
- [ ] All text content is real, not placeholder
- [ ] Content tone matches the product's voice
- [ ] Content length is realistic (not truncated or artificially short)
- [ ] Data values are plausible (numbers, dates, names)

### States and Responsiveness
- [ ] All required interaction states are defined (default, hover, active, focus, disabled, error, loading, empty)
- [ ] Responsive behavior validated for target breakpoints (/responsive)
- [ ] Graceful degradation for unsupported features

### Assets
- [ ] All images and icons are production-optimized (correct format, compressed)
- [ ] All images have alt text defined
- [ ] Asset file sizes within performance budget
- [ ] Lazy loading configured for below-fold assets

### Approval
- [ ] User/stakeholder has reviewed and approved the design
- [ ] Any feedback from review has been incorporated
- [ ] Design is documented (what it is, what it does, key decisions)

### Final Determination

If all items pass: **APPROVED FOR PRODUCTION** — proceed to /ship for code conversion.

If 1-3 items fail: **CONDITIONAL APPROVAL** — fix the failing items during implementation.

If 4+ items fail: **NOT APPROVED** — iterate on the design or switch to manual implementation.
