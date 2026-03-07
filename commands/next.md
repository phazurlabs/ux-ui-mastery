---
description: "Auto-advance — see what step comes next in your design journey based on what you've done so far."
---

# Next — Journey Navigation Utility

A compact navigation utility that helps users progress through the 30-step Sumi journey without memorizing the step order. This is not an analysis command -- it is a wayfinding tool. Keep output short and action-oriented.

## Step Sequence Reference

The canonical 30-step order:

| Step | Command | Phase | Phase Name |
|------|---------|-------|------------|
| 1 | `/01-ground` | 0 | GROUND |
| 2 | `/02-brief` | 0 | GROUND |
| 3 | `/03-research` | 1 | DISCOVER |
| 4 | `/04-taste` | 1 | DISCOVER |
| 5 | `/05-benchmark` | 1 | DISCOVER |
| 6 | `/06-measure` | 1 | DISCOVER |
| 7 | `/07-inspo` | 1 | DISCOVER |
| 8 | `/08-map` | 2 | SHAPE |
| 9 | `/09-wireframe` | 2 | SHAPE |
| 10 | `/10-vision` | 2 | SHAPE |
| 11 | `/11-anatomy` | 2 | SHAPE |
| 12 | `/12-audit` | 3 | AUDIT |
| 13 | `/13-think` | 3 | AUDIT |
| 14 | `/14-access` | 3 | AUDIT |
| 15 | `/15-flow` | 3 | AUDIT |
| 16 | `/16-expose` | 3 | AUDIT |
| 17 | `/17-tokens` | 4 | BUILD |
| 18 | `/18-screen` | 4 | BUILD |
| 19 | `/19-ship` | 4 | BUILD |
| 20 | `/20-generate` | 4 | BUILD |
| 21 | `/21-assets` | 4 | BUILD |
| 22 | `/22-test` | 5 | VALIDATE |
| 23 | `/23-roast` | 5 | VALIDATE |
| 24 | `/24-remix` | 5 | VALIDATE |
| 25 | `/25-qa` | 5 | VALIDATE |
| 26 | `/26-verdict` | 6 | LAUNCH |
| 27 | `/27-grade` | 6 | LAUNCH |
| 28 | `/28-preflight` | 6 | LAUNCH |
| 29 | `/29-welcome` | 6 | LAUNCH |
| 30 | `/30-iterate` | 6 | LAUNCH |

## Protocol

### Step 1: Detect Current Position

- Scan the conversation context for the most recent Sumi numbered command that was run.
- If multiple commands have been run, identify the highest-numbered step completed.
- If no numbered commands have been run, default to recommending step 1 (`/01-ground`).
- Utility commands (`/next`, `/status`, `/guide`) do not count as steps.

### Step 2: Show Next Step

Display the next step in the sequence with enough context to be useful but no more.

### Step 3: Handle Edge Cases

- **At step 30**: Celebrate journey completion. Suggest `/status` for full progress review, or loop back based on `/30-iterate` findings.
- **At end of a phase**: Celebrate phase completion. Briefly explain what the next phase is about and why it follows.
- **Steps were skipped**: Note skipped steps non-judgmentally. Do not lecture -- just mention them as available if the user wants to come back. Example: "You haven't run `/14-access` yet -- worth revisiting for accessibility coverage."
- **No context available**: Recommend starting at `/01-ground` and explain the journey briefly.

## Output Format

```
## Next Step

You just completed: `/[last-command]` -- [short description]

---

### Up Next

> **Step [N] of 30** --> `/[next-command]`
> [One-sentence description of what this step does and why it follows naturally]
>
> **Phase [N]: [PHASE NAME]** | [X] steps remaining in this phase

---

### Quick Options
- **Continue** --> Run `/[next-command]` to proceed
- **Skip ahead** --> `/[command-after-next]` (Step [N+1]): [short description]
- **Next phase** --> `/[first-command-of-next-phase]` (Phase [N]: [NAME])
- **See progress** --> `/status`
- **Full map** --> `/guide`

[If steps were skipped, add:]
### Skipped Steps
You haven't run these yet (non-blocking, but valuable):
- `/[skipped]` -- [why it is worth coming back to]
```

The output should be compact -- no more than 20-30 lines. This is a navigation aid, not an analysis. Get the user to the next step quickly.
