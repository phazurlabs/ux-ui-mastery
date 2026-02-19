---
description: UX process orientation — map the 6-phase NNG design thinking process to your terminal workflow, select the right company methodology, and generate a personalized Sumi command roadmap.
phase: "0"
phase_step: "0.1"
phase_name: "GROUND"
step_label: "Step 1 of 2"
---

# Ground — Process Orientation & Methodology Selection

Before you discover, diagnose, or build — ground yourself in process. This command maps established UX methodology to how you actually work, so you never skip the steps that separate great products from pretty ones.

## The Choice

Every time you open the terminal to build UI, you make a choice:

```
Path A: Prompt → Ship → Hope users like it → Redesign when they don't → Repeat
Path B: Ground → Build → Test → Ship with confidence → Iterate with data
```

Path A feels faster. Path B is faster. The math doesn't lie: 3 well-defined screens beat 10 generic ones, every time.

## Speed Ground (5 Minutes)

Don't have time for full process orientation? Do this instead:

1. **Write one sentence** (1 min): "Users who _____ need _____ because _____"
   - If you can't fill this in → you're not ready to build
   - If you can → skip to `/intent` (0.2) to formalize it

2. **Name one person** (1 min): Give your user a name, a job, and the moment they reach for your product
   - Not "users" — a real human with a real problem

3. **Pick your methodology** (1 min):
   - Solo vibe coding → **Lean UX** (hypothesis → build → test)
   - Small team → **Google Sprint** (map → sketch → decide → prototype → test)
   - Enterprise → **IBM EDT** (Hills → Make → Playback)

4. **Set your quality gate** (1 min): "Before I ship, I will run _____ "
   - Minimum: `/vibe-check` + `/include`
   - Better: add `/brain-scan` + `/responsive`
   - Best: full audit battery via `/judge`

5. **Run `/intent`** (1 min): Let Sumi formalize your problem into a Constraint Stack

That's your Speed Ground. 5 minutes. Now you have a problem statement, a persona, a methodology, and a quality gate. You're ready to build.

## Ground Protocol

1. **Assess starting point**: Determine where the user is and what they need.

   Ask or infer:
   - **Experience level**: No UX experience / Some UX knowledge / Experienced designer
   - **Project stage**: New idea / Existing product / Redesign / Audit
   - **Team size**: Solo developer / Small team (2-5) / Large team (6+)
   - **Time pressure**: Exploring / Time-boxed sprint / Ship immediately
   - **Current process**: No process / Ad-hoc / Structured methodology

   If the user provides context (e.g., "I'm a solo dev building a SaaS app"), infer these from context rather than asking all questions.

2. **Present the 6-phase NNG process mapped to terminal workflow**:

   Show the complete design thinking process with concrete terminal activities for each phase:

   ```
   ┌─────────────────────────────────────────────────────────────────────┐
   │                    THE UX PROCESS FOR BUILDERS                     │
   │                                                                     │
   │  ── UNDERSTAND ──────────────────────────────────────────────────── │
   │                                                                     │
   │  1. EMPATHIZE (2 min)                                              │
   │     Who is the user? What's their task? What frustrates them?      │
   │     → Write 3 sentences about a real person using your product     │
   │                                                                     │
   │  2. DEFINE (3 min)                                                 │
   │     What's the actual problem?                                     │
   │     → Complete: "Users who [X] need [Y] because [Z]"              │
   │     → Sumi: /intent (0.2)                                         │
   │                                                                     │
   │  ── EXPLORE ─────────────────────────────────────────────────────── │
   │                                                                     │
   │  3. IDEATE (5 min)                                                 │
   │     What are the possible solutions? List 3+ approaches.          │
   │     → Sumi: /taste (1.1) + /inspo (1.2) + /benchmark (1.3)       │
   │                                                                     │
   │  4. PROTOTYPE (varies)                                             │
   │     Build the fastest version to test your hypothesis.             │
   │     → Sumi: /drip (4.1) + /screen (4.2) + /ship (4.3)            │
   │                                                                     │
   │  ── MATERIALIZE ─────────────────────────────────────────────────── │
   │                                                                     │
   │  5. TEST (10 min)                                                  │
   │     Does it actually work? Run the audit battery.                  │
   │     → Sumi: /vibe-check (2.1) + /include (2.3) + /brain-scan (2.2)│
   │                                                                     │
   │  6. IMPLEMENT (varies)                                             │
   │     Ship with quality. Every component production-ready.           │
   │     → Sumi: /ship (4.3) + /onboard (4.4) + /extract (4.5)        │
   │                                                                     │
   │  The vibe coder's gap:                                             │
   │  Most skip steps 1-2 and 5. That's where failures start.          │
   └─────────────────────────────────────────────────────────────────────┘
   ```

3. **Terminal exercises for each phase**:

   Provide concrete, timed exercises the user can do right now:

   **Empathize Exercise (2 min)**:
   - Close your eyes for 10 seconds and picture one person who will use this product
   - Write their name, job, and the moment they reach for your product
   - Write what they're doing right before and right after using it
   - Write what frustrates them about how they solve this today

   **Define Exercise (3 min)**:
   - Complete the sentence: "Users who _____ need _____ because _____"
   - Write 3 "How Might We" questions (e.g., "HMW make checkout feel instant?")
   - Define one measurable success criterion (e.g., "task completed in < 30 seconds")

   **Ideate Exercise (5 min)**:
   - List 3 different approaches to solving the defined problem
   - For each, note one advantage and one risk
   - Pick the approach that best serves the persona, not the one that's easiest to build

   **Test Exercise (post-build, 5 min)**:
   - Run `/vibe-check` on your generated output
   - Run `/include` on the same output
   - Read every severity 3-4 finding. Fix before shipping.

4. **Select methodology based on user's context**:

   Based on the assessment from step 1, recommend the right company methodology:

   | Your Context | Recommended Methodology | Why | Core Practice |
   |-------------|------------------------|-----|--------------|
   | Solo dev, vibe coding | **Lean UX** + Vercel/Figma | Fast hypothesis cycles, token-driven | Write hypothesis → build MVP → measure |
   | Solo dev, new product | **Double Diamond** | Diverge/converge prevents premature commitment | Discover → Define → Develop → Deliver |
   | Small team, time pressure | **Google Sprint** (adapted) | 5-day process compresses into 2-hour session | Map → Sketch → Decide → Prototype → Test |
   | Small team, ongoing product | **Spotify** model | Squad autonomy with design system alignment | Think-it → Build-it → Ship-it → Tweak-it |
   | Large organization | **IBM EDT** | Hills + Playbacks align stakeholders | Hills → Observe → Reflect → Make → Playback |
   | Accessibility-focused | **Microsoft Inclusive Design** | "Solve for one, extend to many" | Persona Spectrum → constraint-driven design |
   | Complex/ambiguous problem | **IDEO HCD** | Deep empathy before any solution | Inspiration → Ideation → Implementation |
   | Design engineer | **Vercel/Figma** workflow | Design in code, tokens as truth | Explore in Figma → Build with tokens → Visual regression |

   **The methodology doesn't matter as much as having one.** Any structured process beats no process. Pick one, try it for a week, adjust. The methodologies above are starting points, not religions.

   **The one thing every methodology agrees on**: Understand the user before you build. That's what Phase 0 exists for.

   For each recommendation, explain:
   - Why this methodology fits their context
   - The one practice they should adopt immediately
   - How it maps to Sumi's phase system
   - What to skip if time is short

5. **Generate personalized Sumi command roadmap**:

   Based on the user's project stage, experience, and methodology selection, generate a customized roadmap through Sumi's 22 commands:

   ```
   ## Your Sumi Roadmap

   Based on: [context summary]
   Methodology: [selected methodology]
   Estimated time: [total time]

   ### Required Steps
   1. /intent (0.2) — [why this step matters for their context]
   2. [next command] — [specific rationale]
   3. [next command] — [specific rationale]
   ...

   ### Recommended Steps
   - [command] — [why it adds value for their context]
   ...

   ### Skip These (for now)
   - [command] — [why it's not needed in their context]
   ...

   ### Your Quality Gate
   Before shipping, run at minimum:
   - /vibe-check + /include
   After shipping, measure with:
   - /pulse metrics
   ```

## Output Format

```
### Phase Position
> **Phase 0: GROUND** | Step 1 of 2 | `/ground`
> *NNG: Understand (Empathize + Define) | Pre-phase: Process Orientation*
>
> **`/ground` (0.1)** → `/intent` (0.2)

## Process Orientation: [Context Summary]

### The 6-Phase UX Process
[Process map with terminal exercises]

### Your Methodology: [Selected Methodology]
[Why this fits, core practice, Sumi mapping]

### Your Sumi Roadmap
[Personalized command sequence with rationale]

### Your Process Maturity
[Current level assessment + level-up suggestion]

### The 60-Second Version
> [One-paragraph summary of: your user, their problem, your methodology, and your quality gate. Everything a builder needs to get started.]

### Start Building
> Run `/intent` now to formalize your problem into a Constraint Stack, then paste it into every BUILD command.
```

## Cross-References

When grounding users in process, draw knowledge from:
- `ux-process-workflow` skill for NNG phases, company methodologies, and the vibe coder bridge
- `nng-ux-heuristics` skill for heuristic evaluation fundamentals used in the Test phase
- `ux-research-methods` skill for research methodology in the Empathize phase
- `cognitive-psychology-ux` skill for cognitive laws that justify process rigor
- `ux-metrics-measurement` skill for measurement frameworks used in success criteria
- `agentic-ai-generative-ux` skill for AI-assisted design risks and patterns
- `ux-ethics-content-strategy` skill for ethical frameworks in the Define phase

## Next Step

**Next** → `/intent` (0.2) — Define your problem statement, persona, HMW questions, and success criteria

**Alternatives**:
- `/taste` (1.1) — Skip to DISCOVER if you already have a clear problem and process
- `/guide` — See the full 22-step journey across all 6 phases

**The builder's promise**: 10 minutes in Phase 0 saves hours of building the wrong thing. Every senior designer in the industry does this step — it's the one thing separating "good-looking" from "great product."
