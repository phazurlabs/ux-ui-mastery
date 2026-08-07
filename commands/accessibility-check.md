---
name: accessibility-check
description: Deep WCAG 2.2 compliance audit on code with specific fixes for every violation found.
argument-hint: "[file, component, or screen to audit]"
---

# Accessibility Check Command

## Before running

This command needs a file path, component, screen description, or pasted markup.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target, do not audit a hypothetical interface, and do not produce generic advice in place of the real analysis — an audit of something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.

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
