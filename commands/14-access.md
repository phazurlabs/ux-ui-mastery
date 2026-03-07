---
description: "[3.3] Accessibility audit — deep WCAG 2.2 audit on code with specific fixes for every violation found. Accessibility IS inclusion."
phase: "3"
phase_step: "3.3"
phase_name: "AUDIT"
step_label: "Step 14 of 30"
---

# Include — Accessibility Audit

Perform a deep accessibility audit against WCAG 2.2 AA standards on the provided code or component.

## Audit Protocol

1. **Semantic HTML Analysis**:
   - Verify proper heading hierarchy (h1-h6)
   - Check landmark regions (nav, main, aside, header, footer)
   - Validate form labels, fieldsets, and legends
   - Verify list structure (ul/ol/li)
   - Check table accessibility (th, scope, caption)
   - Ensure buttons vs links are used correctly

2. **ARIA Implementation**:
   - Check for redundant ARIA (ARIA that duplicates native semantics)
   - Verify all ARIA roles have required attributes
   - Validate aria-label, aria-labelledby, aria-describedby references
   - Check live regions for dynamic content
   - Verify modal/dialog focus management

3. **Keyboard Navigation**:
   - Verify tab order follows visual layout
   - Check for keyboard traps
   - Verify focus indicators are visible and meet contrast requirements
   - Check composite widget keyboard patterns (tabs, menus, trees)
   - Verify skip navigation links

4. **Visual Accessibility**:
   - Calculate color contrast ratios for all text
   - Check for color-only information encoding
   - Verify text resizing up to 200% without loss
   - Check for respecting prefers-reduced-motion
   - Verify prefers-color-scheme support

5. **Content Accessibility**:
   - Check image alt text (present, meaningful, or empty for decorative)
   - Verify link text is descriptive out of context
   - Check for plain language and reading level
   - Verify error messages are associated with fields

## Output Format

```
### Phase Position
> **Phase 2: DIAGNOSE** | Step 3 of 4 | `/include`
> *NNG: Accessibility Evaluation | Visual: Inclusive Design*
>
> `/brain-scan` (2.2) → **`/include` (2.3)** → `/flow` (2.4)

## Accessibility Audit Results

### Compliance Level: [A / AA / AAA / Non-compliant]
### Issues Found: [X critical, X serious, X moderate, X minor]

### Critical Issues (Must Fix)
[Each with: WCAG criterion, code location, description, fix with code]

### Serious Issues (Should Fix)
[Same format]

### Moderate Issues (Good to Fix)
[Same format]

### Passing Checks
[What the code does well]

### Recommended Testing
- [ ] Screen reader testing with [VoiceOver/NVDA]
- [ ] Keyboard-only navigation test
- [ ] 200% zoom test
- [ ] Color blindness simulation
```

## Cross-References
When relevant issues are found, load additional context from:
- `accessibility-inclusive-design` skill for WCAG patterns and neurodiversity accommodations
- `component-patterns-code` skill for accessible component implementations
- `cross-cultural-i18n-ux` skill for RTL and i18n accessibility

## Next Step

**Next** → `/flow` (2.4) — Audit the full user journey for bottlenecks

**Alternatives**:
- `/dark-scan` (3.1) — Jump to FORTIFY if flow analysis isn't needed
- `/ship` (4.3) — Rebuild a component with full accessibility baked in
- `/guide` — See the full 20-step journey
