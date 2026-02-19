---
description: Microcopy & content audit — evaluate all UI text for clarity, tone, accessibility, inclusive language, and i18n readiness with rewrites.
phase: "3"
phase_step: "3.3"
phase_name: "FORTIFY"
step_label: "Step 3 of 4"
---

# Copy Check — Microcopy & Content Audit

Audit all user-facing text in a UI for clarity, tone consistency, inclusive language, actionability, and cross-cultural readiness, providing rewritten alternatives for every finding.

## Content Audit Protocol

1. **Inventory all UI text by category**:
   - **Navigation**: menu labels, breadcrumbs, tab names, section headers
   - **Actions**: button labels, CTAs, link text, toggle labels
   - **Feedback**: success messages, error messages, warnings, validation text, toast notifications
   - **Empty States**: zero-data screens, first-run experiences, search-no-results
   - **Guidance**: tooltips, helper text, placeholders, onboarding callouts, coach marks
   - **Confirmation**: dialog titles, dialog body text, destructive action warnings
   - **System**: loading text, status indicators, progress descriptions, timestamps

2. **Evaluate reading level and comprehension**:
   - Calculate Flesch-Kincaid grade level for all body text
   - Target grade 6-8 for consumer products, grade 8-10 for professional/B2B tools
   - Flag jargon, technical terms, or acronyms used without explanation
   - Flag sentences over 20 words (cognitive overload risk on mobile)
   - Flag passive voice in action-oriented contexts (buttons, CTAs, instructions)

3. **Assess tone and voice consistency**:
   - Identify the current voice profile: formal, conversational, playful, authoritative, empathetic
   - Flag tone shifts between screens or components (e.g., playful onboarding, robotic error messages)
   - Check that emotional register matches the user's likely emotional state at that point in the journey
   - Verify brand voice alignment if brand guidelines are available

4. **Audit inclusive language**:
   - Flag gendered language where gender-neutral alternatives exist
   - Flag ableist language (e.g., "crazy deal," "blind spot," "lame")
   - Flag culturally specific idioms that may not translate (e.g., "knock it out of the park")
   - Check for assumptions about family structure, age, technical literacy, or physical ability
   - Verify pronoun usage is inclusive or configurable

5. **Evaluate action verb strength**:
   - Button labels should start with strong, specific verbs: "Create account" not "Submit," "Save changes" not "OK"
   - CTAs should communicate value: "Start free trial" not "Continue," "Get my report" not "Next"
   - Destructive actions should be explicit: "Delete 3 files permanently" not "Delete"
   - Flag vague labels: "Click here," "Learn more," "Submit," "OK," "Yes/No" without context

6. **Check character count and truncation risk**:
   - Flag button labels over 20 characters (mobile truncation risk)
   - Flag headings over 40 characters (small screen wrapping)
   - Check that strings allow for 30-40% expansion for translation (German, Finnish expand significantly)
   - Verify text containers use flexible sizing, not fixed widths
   - Flag concatenated strings that break translation word order

7. **Assess scannability**:
   - Check heading hierarchy for logical information architecture
   - Verify front-loading: most important word comes first in labels and headings
   - Check for parallel structure in lists and navigation items
   - Flag walls of text without visual breaks

8. **Score the content** (each 1-10):

   | Dimension | What It Measures |
   |-----------|-----------------|
   | Clarity | Can users understand every piece of text on first read without context? |
   | Consistency | Does tone, terminology, and formatting stay uniform across the entire UI? |
   | Inclusivity | Is language free from bias, assumption, and exclusionary phrasing? |
   | Actionability | Do action labels clearly communicate what will happen and motivate the click? |
   | Scannability | Can users extract meaning from headings and labels without reading body text? |

## Output Format

```
### Phase Position
> **Phase 3: FORTIFY** | Step 3 of 4 | `/copy-check`
> *NNG: Content Strategy | Visual: Content Quality*
>
> `/trust-scan` (3.2) → **`/copy-check` (3.3)** → `/responsive` (3.4)

## Copy Check: [Product/Screen Name]

### Content Summary
- **Total text elements audited**: [X]
- **Reading level**: Grade [X] (target: [Y])
- **Voice profile**: [detected tone]
- **i18n readiness**: [ready / needs work / not ready]

### Dimension Scores
| Dimension | Score | Key Observation |
|-----------|-------|----------------|
| Clarity | X/10 | ... |
| Consistency | X/10 | ... |
| Inclusivity | X/10 | ... |
| Actionability | X/10 | ... |
| Scannability | X/10 | ... |

**Overall Content Score**: [average]/10

### Findings

#### [Category: e.g., Action Labels]
| Location | Current Copy | Problem | Rewritten Copy | Reasoning |
|----------|-------------|---------|---------------|-----------|
| Signup CTA | "Submit" | Vague, no value communicated | "Create my account" | Specific verb + possessive pronoun increases ownership |

[Repeat table per category]

### i18n Readiness Issues
[String concatenation problems, hardcoded text, expansion risk, cultural assumptions]

### Voice & Tone Guide (Recommended)
[If inconsistencies found, provide a mini voice chart: context → tone → example]
```

## Cross-References
When auditing content, draw evaluation criteria from:
- `ux-ethics-content-strategy` skill for content strategy frameworks, voice/tone methodology, and ethical copywriting
- `accessibility-inclusive-design` skill for plain language requirements (WCAG 3.1.5), reading level targets, and cognitive accessibility
- `cross-cultural-i18n-ux` skill for translation readiness, string externalization, bidirectional text, and cultural sensitivity

## Next Step

**Next** → `/responsive` (3.4) — Verify cross-device behavior

**Alternatives**:
- `/drip` (4.1) — Jump to BUILD if responsive isn't a concern
- `/include` (2.3) — Go back for accessibility if reading level issues were found
- `/guide` — See the full 20-step journey
