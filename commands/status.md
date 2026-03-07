---
description: "Progress dashboard — see where you are in the 30-step design journey, what's complete, what's next, and your overall progress."
---

# Status — Journey Progress Dashboard

A progress tracking utility that shows the user's position in the 30-step Sumi design journey. The output should be clean, scannable, and motivating -- use progress bars and checkmarks to create a sense of accomplishment and momentum.

## Protocol

### Step 1: Detect Completed Steps

- Scan the conversation context for which Sumi numbered commands have been run.
- Mark each of the 30 steps as complete or incomplete.
- Identify the recommended next step (first incomplete step in sequence).
- Calculate per-phase and overall completion percentages.

### Step 2: Display Progress Dashboard

Render the full journey map with completion status for every step.

### Step 3: Adapt to Context

- Show checkmarks for completed steps, empty boxes for incomplete.
- Bold or highlight the recommended next step.
- Show phase completion as progress bars and percentages.
- Show overall progress as fraction and percentage.
- If steps were completed out of order, show them as complete without judgment.
- If no steps have been completed, show the full map with an encouraging message to begin.

## Output Format

```
## Sumi Journey Progress

### Phase 0: GROUND -- "Know your problem"
  [x] 01. `/01-ground`       Orient in the design process
  [x] 02. `/02-brief`        Define problem, persona, constraints
  Phase 0: xxxxxxxxxx 100%

### Phase 1: DISCOVER -- "Know your market"
  [x] 03. `/03-research`     Plan user research
  [x] 04. `/04-taste`        Sector style direction
  [ ] 05. `/05-benchmark`    Competitive design analysis       <-- NEXT
  [ ] 06. `/06-measure`      Plan UX metrics
  [ ] 07. `/07-inspo`        Find design inspiration
  Phase 1: xxxx...... 40%

### Phase 2: SHAPE -- "Explore your solution"
  [ ] 08. `/08-map`          Information architecture
  [ ] 09. `/09-wireframe`    Low-fidelity wireframes
  [ ] 10. `/10-vision`       Visual design direction
  [ ] 11. `/11-anatomy`      UI pattern analysis
  Phase 2: .......... 0%

### Phase 3: AUDIT -- "Find your problems"
  [ ] 12. `/12-audit`        Heuristic evaluation
  [ ] 13. `/13-think`        Cognitive audit
  [ ] 14. `/14-access`       Accessibility audit
  [ ] 15. `/15-flow`         User flow audit
  [ ] 16. `/16-expose`       Fortification sweep
  Phase 3: .......... 0%

### Phase 4: BUILD -- "Ship your product"
  [ ] 17. `/17-tokens`       Design token system
  [ ] 18. `/18-screen`       Build production screens
  [ ] 19. `/19-ship`         Build production components
  [ ] 20. `/20-generate`     AI-powered screen generation
  [ ] 21. `/21-assets`       AI-powered asset generation
  Phase 4: .......... 0%

### Phase 5: VALIDATE -- "Prove it works"
  [ ] 22. `/22-test`         Usability test plan
  [ ] 23. `/23-roast`        Design critique
  [ ] 24. `/24-remix`        Evidence-based redesign
  [ ] 25. `/25-qa`           Design QA
  Phase 5: .......... 0%

### Phase 6: LAUNCH -- "Ship and grow"
  [ ] 26. `/26-verdict`      Comprehensive review
  [ ] 27. `/27-grade`        Visual quality score
  [ ] 28. `/28-preflight`    Pre-launch checklist
  [ ] 29. `/29-welcome`      Onboarding flow builder
  [ ] 30. `/30-iterate`      Post-launch iteration plan
  Phase 6: .......... 0%

----------------------------------------------
Overall: [X]/30 steps ([Y]%)  |  Next --> `/[next-command]`
----------------------------------------------

Run `/next` to continue  |  `/guide` for the full map
```

### Adaptation Rules

- **Progress bar characters**: Use `x` for complete segments and `.` for incomplete segments. 10 characters total per phase, proportional to completion.
- **NEXT marker**: Place `<-- NEXT` on the first incomplete step in sequence.
- **Completed journey**: If all 30 steps are complete, replace the footer with a congratulatory message and suggest `/30-iterate` for continuous improvement.
- **No steps complete**: Show the full empty map with: "Ready to begin? Start with `/01-ground` to orient yourself in the design process."
- **Out-of-order completion**: Mark completed steps with `[x]` regardless of order. Place `<-- NEXT` on the first incomplete step.

The output should fit in one screen when possible. No additional commentary beyond the dashboard itself -- the visual format communicates progress clearly on its own.
