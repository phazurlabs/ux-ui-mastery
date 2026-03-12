---
description: "Context-aware suggestion of what to do next based on what you've generated so far."
tier: "utility"
---

# Next — What Should I Do Now?

A compact navigation aid that suggests the best next command based on context. Not an analysis -- a wayfinding tool. Keep output short and action-oriented.

## Command Reference

The 27 commands organized by tier:

**MAKE**: `/style`, `/palette`, `/type`, `/layout`, `/wireframe`, `/screen`, `/component`, `/page`, `/tokens`, `/form`, `/nav`, `/animate`, `/icon`, `/dark`, `/responsive`, `/onboard`, `/generate`, `/remix`

**REVIEW**: `/audit`, `/roast`, `/grade`, `/qa`, `/a11y`

**PLAN**: `/brief`, `/research`, `/benchmark`, `/map`, `/measure`, `/preflight`

**Utility**: `/sumi`, `/next`, `/status`

## Common Progressions

These are typical sequences, not mandatory order:

```
/brief --> /style --> /screen            (fast track)
/brief --> /research --> /style           (research-first)
/style --> /tokens --> /screen            (system-first)
/screen --> /roast --> /remix             (iterate loop)
/audit --> /a11y --> /roast --> /grade    (full review)
/style --> /screen --> /qa --> /preflight (ship track)
```

## Protocol

### Step 1: Detect Context

- Scan conversation for the most recent Sumi command(s) run
- Identify what outputs exist (style decisions, screens, audits, etc.)
- If no commands have been run, recommend `/style` or `/brief`
- Utility commands (`/next`, `/status`, `/sumi`) don't count as steps

### Step 2: Recommend Next Command

Based on what exists and what's missing, suggest the highest-value next command.

**Priority logic**:
1. If no style direction exists --> `/style [sector]`
2. If style exists but no screens --> `/screen [type]`
3. If screens exist but no review --> `/roast`
4. If review done with issues --> `/remix`
5. If ready to ship --> `/preflight`
6. If nothing exists and user is exploring --> `/brief`

### Step 3: Handle Edge Cases

- **Everything looks done**: Suggest `/preflight` or celebrate. Recommend `/status` for full review.
- **User jumped around**: Note what's missing without judgment. Just mention it as available.
- **No context at all**: Recommend `/style [sector]` for builders or `/brief` for planners.

## Output Format

```
## Next Step

You just ran: `/[last-command]` -- [short description of what it produced]

---

### Recommended

> **`/[next-command]`** [optional args]
> [One sentence: what this does and why it follows naturally from what you just did]

---

### Other Options
- `/[option-1]` -- [why you might want this instead]
- `/[option-2]` -- [why you might want this instead]
- `/[option-3]` -- [why you might want this instead]

### Worth Revisiting
[Only if something valuable was skipped]
- `/[skipped]` -- [brief reason it's worth doing]

---
See all commands: `/sumi` | See progress: `/status`
```

The output should be compact -- 15-25 lines maximum. Get the user to the next command fast.
