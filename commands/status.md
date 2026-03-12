---
description: "Progress dashboard — see what you've generated, what's available, and suggested next moves."
tier: "utility"
---

# Status — Progress Dashboard

A visual progress tracker showing what Sumi commands have been run in this session. Clean, scannable, motivating.

## Command Registry

All 27 commands organized by tier:

**MAKE (18 commands)**:
`/style`, `/palette`, `/type`, `/layout`, `/wireframe`, `/screen`, `/component`, `/page`, `/tokens`, `/form`, `/nav`, `/animate`, `/icon`, `/dark`, `/responsive`, `/onboard`, `/generate`, `/remix`

**REVIEW (5 commands)**:
`/audit`, `/roast`, `/grade`, `/qa`, `/a11y`

**PLAN (6 commands)**:
`/brief`, `/research`, `/benchmark`, `/map`, `/measure`, `/preflight`

**Utility (3 commands)**:
`/sumi`, `/next`, `/status`

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

### MAKE -- Design and Build
  [x] /style          Sector visual direction
  [ ] /palette        Deep color system
  [ ] /type           Typography system
  [ ] /layout         Layout block patterns
  [x] /wireframe      Low-fidelity wireframes
  [x] /screen         Production screens
  [ ] /component      Production components
  [ ] /page           Full page compositions
  [ ] /tokens         Design token system
  [ ] /form           Form design
  [ ] /nav            Navigation system
  [ ] /animate        Motion design
  [ ] /icon           Icon system
  [ ] /dark           Dark mode
  [ ] /responsive     Responsive design
  [ ] /onboard        Onboarding flow
  [ ] /generate       AI screen generation
  [ ] /remix          Evidence-based redesign
  MAKE: 3/18

### REVIEW -- Evaluate and Improve
  [x] /audit          Heuristic evaluation
  [ ] /roast          Design critique            <-- NEXT
  [ ] /grade          Visual quality score
  [ ] /qa             Design QA
  [ ] /a11y           Accessibility audit
  REVIEW: 1/5

### PLAN -- Research and Strategy
  [x] /brief          Problem definition
  [ ] /research       User research & testing
  [ ] /benchmark      Competitive analysis
  [ ] /map            Information architecture
  [ ] /measure        Metrics plan
  [ ] /preflight      Launch readiness
  PLAN: 1/6

----------------------------------------------
Overall: 5/27 commands  |  Next --> /roast
----------------------------------------------

Run /next for guidance  |  /sumi for full map
```

### Adaptation Rules

- **NEXT marker**: Place `<-- NEXT` on the recommended next command (use priority logic from `/next` protocol)
- **All commands run**: Replace footer with congratulatory message
- **No commands run**: Show full empty map with: "Ready to start? Try `/style [your sector]` or `/brief` to begin."
- **Partial completion**: Show counts per tier and overall

The output should fit on one screen. No commentary beyond the dashboard -- the visual format communicates progress clearly.
