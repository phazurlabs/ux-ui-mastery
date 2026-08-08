---
name: status
description: "Progress dashboard — see what you've generated, what's available, and suggested next moves."
argument-hint: "[optional: project path]"
---

# Status — Progress Dashboard

A visual progress tracker showing what Sumi commands have been run in this session. Clean, scannable, motivating.

## Command Registry

All 37 commands organized by tier:

**MAKE (20 commands)**:
`/fix`, `/style`, `/palette`, `/type`, `/layout`, `/wireframe`, `/screen`, `/component`, `/page`, `/tokens`, `/form`, `/nav`, `/animate`, `/icon`, `/dark`, `/responsive`, `/onboard`, `/generate`, `/remix`, `/figma`

**REVIEW (7 commands)**:
`/audit`, `/roast`, `/grade`, `/qa`, `/a11y`, `/before-after`, `/ai-audit`

**PLAN (6 commands)**:
`/brief`, `/research`, `/benchmark`, `/map`, `/measure`, `/preflight`

**Utility (4 commands)**:
`/start`, `/sumi`, `/next`, `/status`

## Protocol

### Step 1: Detect Completed Commands

- Scan conversation context for which Sumi commands have been run
- Mark each as complete or not run
- Calculate per-tier and overall completion
- Identify the recommended next command

### Step 2: Display Dashboard

Render the progress map with completion status.

### Step 3: Adapt

- Checkmarks for completed, empty boxes for not run
- Bold or highlight the recommended next command
- Show tier completion as progress indicators
- If commands were run out of typical order, show them as complete without judgment
- If nothing has been run, show the full map with encouragement to begin

## Output Format

```
## Sumi Progress

### MAKE — Design and Build
  [ ] /fix           Anti-slop transformation
  [ ] /style         Visual identity
  [ ] /palette       Color system
  [ ] /type          Typography system
  [ ] /layout        Layout patterns
  [ ] /wireframe     Low-fidelity wireframes
  [ ] /screen        Production screens
  [ ] /component     Production components
  [ ] /page          Full page compositions
  [ ] /tokens        Design token system
  [ ] /form          Form design
  [ ] /nav           Navigation system
  [ ] /animate       Motion design
  [ ] /icon          Icon system
  [ ] /dark          Dark mode
  [ ] /responsive    Responsive design
  [ ] /onboard       Onboarding flow
  [ ] /generate      AI generation
  [ ] /remix         Evidence-based redesign
  MAKE: 0/19

### REVIEW — Evaluate and Improve
  [ ] /audit         Full design audit
  [ ] /roast         Quick critique + slop detection
  [ ] /grade         Design Quality Score (0-100)
  [ ] /qa            Design QA + codebase consistency
  [ ] /a11y          Accessibility audit + auto-fix
  [ ] /before-after  Transformation comparison
  REVIEW: 0/6

### PLAN — Research and Strategy
  [ ] /brief         Problem definition
  [ ] /research      User research & testing
  [ ] /benchmark     Competitive analysis
  [ ] /map           Information architecture
  [ ] /measure       Metrics plan
  [ ] /preflight     Launch readiness
  PLAN: 0/6

──────────────────────────────────────
Overall: 0/37 commands  |  Next → /style
──────────────────────────────────────

Run /next for guidance  |  /sumi for full map
```

### Adaptation Rules

- **NEXT marker**: Place `<-- NEXT` on the recommended next command (use priority logic from `/next` protocol: `/fix` first if slop detected, then `/style` for new projects, then uncompleted commands in tier order)
- **`/fix` completed**: Show checkmark with slop score note, e.g. `[x] /fix  Anti-slop transformation  (slop: 7→2)`
- **`/grade` completed**: Show DQS score next to checkmark, e.g. `[x] /grade  Design Quality Score  (DQS: 74/100)`
- **`/before-after` completed**: Show grade change, e.g. `[x] /before-after  Transformation comparison  (42→78 DQS)`
- **All commands run**: Replace footer with congratulatory message
- **No commands run**: Show full empty map with: "Ready to start? Try `/style [your sector]` or `/fix` to clean up existing UI."
- **Partial completion**: Show counts per tier and overall

The output should fit on one screen. No commentary beyond the dashboard -- the visual format communicates progress clearly.
