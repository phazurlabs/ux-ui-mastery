# `.sumi/` File Schemas

Full schemas for every design-memory file, the merge semantics, and the
migration path from the pre-v4.1.0 shapes.

## Why this file exists

Before v4.1.0 there was no canonical definition. `.sumi/style.json` was written
in **four** different shapes:

| Writer | Top-level keys |
|---|---|
| `commands/style.md` Step 14 | `meta` `color` `typography` `spacing` `borderRadius` `shadow` `motion` `tone` `references` |
| `commands/style.md` Design Memory Persistence | `version` `generated` `sector` `mood` `technology` **`colors`** `darkMode` |
| `commands/tokens.md` | raw W3C DTCG — `$schema` `color` `space` `radius` `z` `$themes` |
| `commands/palette.md`, `commands/type.md` | partial merges into `color` / `typography` |

The two `style.md` blocks were 90 lines apart in the same file and disagreed on
whether the color key was `color` or `colors`. Downstream commands read whichever
they happened to assume, so a `/style` followed by `/screen` could silently find
no palette at all.

`scripts/check-corpus.py` now fails the build if any `.sumi/*.json` path is
written with more than one top-level key set.

## The resolution

The canonical shape keeps **schema 1's envelope**, nests **DTCG as the token
payload**, and renames schema 2's one unique contribution.

Why this way round:

- Schema 1 had three writers to schema 2's one, and two of those three
  (`/palette`, `/type`) are *partial* writers that merge into a subtree. Schema 2
  was a whole-file replacement, which is the wrong shape for a file four commands
  write to — it destroys the other three writers' work on every run.
- Schema 1's key names are singular and match DTCG group names. Schema 2's
  `colors` matches nothing else in the corpus and was the direct cause of the
  reader breakage.
- Schema 3 was never a competitor — DTCG is the right format for tokens and has
  no way to express a sector, a tone of voice, or a list of reference apps. It is
  the payload, not the envelope, so it nests under `tokens`.
- Schema 2's `technology` block is genuinely useful and survives, renamed
  `project`, populated by the framework-detection protocol.

## Migration from pre-v4.1.0 files

A file with no `$sumi` key is a legacy file. Read it, map it, write the canonical
shape back:

| Legacy | Canonical |
|---|---|
| `color`, `colors` | `tokens.color` |
| `typography` | `tokens.typography` |
| `spacing` | `tokens.space` |
| `borderRadius` | `tokens.radius` |
| `shadow` | `tokens.shadow` |
| `motion` | `tokens.duration` + `tokens.easing` |
| `darkMode` | `tokens.$themes.dark` |
| `technology` | `project` |
| `version`, `generated`, `sector`, `mood` | `meta.*` |
| `context.json` → `project` block | `project` (that file is retired) |

Do the migration silently — it is lossless. Say so in one line only if the user
is watching a command that would otherwise appear to do nothing.

## `.sumi/style.json`

```json
{
  "$sumi": "1",
  "meta": {
    "generated": "2026-08-08T14:22:00Z",
    "updatedBy": ["/style", "/palette"],
    "sector": "fintech",
    "mood": "professional, precise, quietly confident",
    "platform": "web"
  },
  "project": {
    "framework": "react",
    "styling": "tailwind",
    "typescript": true
  },
  "tokens": {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "color": {
      "brand": {
        "500": { "$type": "color", "$value": "oklch(0.55 0.14 250)" }
      },
      "neutral": {
        "50":  { "$type": "color", "$value": "oklch(0.98 0.002 250)" },
        "950": { "$type": "color", "$value": "oklch(0.18 0.01 250)" }
      },
      "semantic": {
        "bg-base":    { "$type": "color", "$value": "{color.neutral.50}" },
        "text-strong":{ "$type": "color", "$value": "{color.neutral.950}" },
        "error":      { "$type": "color", "$value": "oklch(0.55 0.19 25)" }
      }
    },
    "typography": {
      "family": {
        "display": { "$type": "fontFamily", "$value": "Instrument Serif" },
        "body":    { "$type": "fontFamily", "$value": "Inter" },
        "mono":    { "$type": "fontFamily", "$value": "JetBrains Mono" }
      },
      "scale": {
        "base": { "$type": "dimension", "$value": "1rem" },
        "lg":   { "$type": "dimension", "$value": "1.25rem" }
      }
    },
    "space":    { "4": { "$type": "dimension", "$value": "1rem" } },
    "radius":   { "md": { "$type": "dimension", "$value": "0.5rem" } },
    "shadow":   { "2": { "$type": "shadow", "$value": {} } },
    "duration": { "fast": { "$type": "duration", "$value": "150ms" } },
    "easing":   { "out": { "$type": "cubicBezier", "$value": [0.2, 0, 0, 1] } },
    "z":        { "modal": { "$type": "number", "$value": 400 } },
    "$themes": {
      "light": {},
      "dark":  { "color": { "semantic": { "bg-base": { "$value": "{color.neutral.950}" } } } }
    }
  },
  "tone": {
    "formality": "professional but not stiff",
    "traits": ["precise", "calm", "never breathless"],
    "wordsToUse": ["balance", "transfer", "confirm"],
    "wordsToAvoid": ["seamless", "effortless", "revolutionary"]
  },
  "references": [
    {
      "app": "Mercury",
      "platform": "web",
      "stealThis": "tabular numerals everywhere a figure appears",
      "takeaway": "alignment of digits carries more trust signal than any badge"
    }
  ]
}
```

### Field notes

- `$sumi` is the envelope version, not the design's version. It changes only when
  this schema changes.
- `meta.updatedBy` is append-only and de-duplicated. It is how a later command
  knows whether the palette came from `/style`'s first pass or a later `/palette`.
- `project` is written by framework detection, and read by every command that
  emits code. Detection lives in `/style`; other commands read the result rather
  than re-detecting.
- `tokens.$themes.dark` holds only the deltas from light. A full second palette
  means someone replaced instead of merging.

## `.sumi/brief.json`

```json
{
  "$sumi": "1",
  "meta": { "generated": "", "updatedBy": ["/brief"] },
  "persona": { "who": "", "context": "", "constraints": [], "jobToBeDone": "" },
  "hmw": [""],
  "constraints": { "technical": [], "business": [], "regulatory": [] },
  "success": [{ "metric": "", "baseline": "", "target": "" }]
}
```

## `.sumi/map.json`

```json
{
  "$sumi": "1",
  "meta": { "generated": "", "updatedBy": ["/map"] },
  "screens": [{ "id": "", "path": "", "purpose": "", "parent": null }],
  "navigation": { "model": "", "primary": [], "secondary": [] },
  "contentHierarchy": []
}
```

## `.sumi/vision.json`

```json
{
  "$sumi": "1",
  "meta": { "generated": "", "updatedBy": ["/grade"] },
  "score": { "total": 0, "dimensions": [{ "name": "", "score": 0, "note": "" }] },
  "dnaMatch": [{ "designer": "", "confidence": 0, "evidence": "" }],
  "verdict": ""
}
```

## `.sumi/wireframe-<screen>.json`

```json
{
  "$sumi": "1",
  "meta": { "generated": "", "updatedBy": ["/wireframe"], "screen": "" },
  "blocks": [{ "id": "", "type": "", "order": 0, "responsive": {} }],
  "components": [{ "name": "", "states": [] }],
  "interactions": []
}
```

## `.sumi/generated-<asset>.json`

```json
{
  "$sumi": "1",
  "meta": { "generated": "", "updatedBy": ["/generate"], "asset": "" },
  "runs": [{ "model": "", "prompt": "", "jobId": "", "score": 0, "verdict": "" }]
}
```

## `.sumi/decisions.log`

Append-only NDJSON, one object per line. Never rewritten, never sorted.

```
{"ts":"2026-08-08T14:22:00Z","command":"/style","decision":"brand hue 250","reason":"fintech trust convention","overrides":null}
{"ts":"2026-08-08T14:31:00Z","command":"/palette","decision":"brand hue 262","reason":"user asked for more violet","overrides":"style:brand.500"}
```

`overrides` names the prior decision this one supersedes, so the log reads as a
chain rather than a pile. When two commands disagree, the last entry with an
`overrides` pointing at the earlier one is the answer.

## Worked merge example

`/style` runs, then `/palette` runs with an explicit user instruction.

1. `/style` creates the file, `meta.updatedBy = ["/style"]`, fills `tokens.*`.
2. `/palette` loads it. It owns `tokens.color` only.
3. The user says "more violet". That is an explicit instruction, so it beats
   design memory (rule 2).
4. `/palette` deep-merges `tokens.color`, leaves `tokens.typography` and
   everything else byte-identical, appends `"/palette"` to `meta.updatedBy`,
   refreshes `meta.generated`.
5. It appends one line to `decisions.log` with `overrides` naming the token it
   changed.

What would be wrong: writing a fresh object with only a `colors` key. That is
schema 2's whole-file replacement, and it silently discards the type scale, the
spacing system, the tone, and the reference apps.
