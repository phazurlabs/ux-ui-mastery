# Changelog

All notable changes to this project are documented here. This project follows
[Semantic Versioning](https://semver.org).

## [4.0.0] — 2026-08-08

Merge release. Sumi 3.1.0 and Chef Sumi were one lineage that forked at `cc165ef`
on 2026-02-14: one grew the corpus to 42 skills, the other fixed the engineering
on the original 19. This merges them back into one plugin and keeps both halves.
43 skills, 168 reference files, 37 commands.

Chef Sumi's own version numbers — `plugin.json` 9.0.0, `marketplace.json` 6.0.0,
git tag v4.0.0, a commit message saying v10.0.0 — were mutually inconsistent and
never published under this name. None was carried forward. The only version users
have seen is 3.1.0, so this is 4.0.0. The chef-sumi lineage is archived at
`phazurlabs/chef-sumi` and pinned in this repo as tag `archive/chef-sumi-main`.

### Added

- **23 skills** from chef-sumi: visual design mastery, UI pattern intelligence,
  sector style intelligence, layout blocks, page composition, responsive blocks,
  navigation and form encyclopedias, microcopy, animation recipes, color
  palettes, typography pairings, shadow/elevation, icons, images and media,
  data visualization, conversion optimization, design token presets, platform
  visual standards, screen and flow patterns, AI design generation, design
  process methods, and deliverable templates.
- **26 commands** from chef-sumi across MAKE / REVIEW / PLAN tiers, including
  `/fix`, `/style`, `/grade`, `/roast`, and the `.sumi/` design memory that
  carries style decisions from `/style` into every later command.
- **`/audit` section E.4, a cross-domain roll-up** absorbed from the retired
  `/design-review`. It scores ten named design domains and, unlike its
  predecessor, does not peg that list to the plugin's skill count.
- **`/roast` gains the four-tier finding classification** from the retired
  `/design-critique`: Must-fix, Should-fix, Could-improve, and Explore. Explore
  is the class most critiques lack — when a disagreement rests on an assumption
  about users rather than a design principle, routing it to research is more
  honest than picking a side.
- **`/roast` gains CRP steps 2 and 3**, the designer's-questions and
  neutral-questions rounds chef-sumi compressed away. They are the part of
  Lerman's process that stops a critique becoming an opinion dump.
- **Count checking in `scripts/validate-plugin.py`.** Any count stated in
  `plugin.json`, `marketplace.json`, or `README.md` that disagrees with the
  globbed tree is now a hard error. These counts drifted in every prior release
  because nothing checked them.
- **A SKILL.md line budget** (150) as a warning. SKILL.md loads in full whenever
  its skill triggers; references load only when pointed at. 35 files are over
  budget today and are scheduled for v4.1.0.

### Changed

- **The orchestrator went from 8 pipelines to 12**, with a two-band model that
  distinguishes core stages (ordered, gated, six or fewer) from depth skills
  loaded inside a stage on demand. Most of the 23 new skills are encyclopedic
  lookup libraries, not stages; treating them as stages would have made several
  pipelines ten deep and broken the one-stage-at-a-time rule. New pipelines:
  **Fix** (AI code that runs but looks wrong — the flagship `/fix` had no
  pipeline), **Compose** (nothing previously produced a whole *page*),
  **Generate** (gated so nothing leaves without a quality score and a named
  verdict), and **Convert** (funnel friction, with the dark-pattern check as a
  gate rather than a courtesy). Every pipeline now names the command that
  produces its artifact.
- **All 23 merged skill descriptions rewritten** from the old "Use when the user
  mentions: <forty keywords>" dumps into task-phrased form, 266–325 characters.
  Descriptions are the only thing loaded for all 43 skills on every turn.
  Disambiguating clauses were added to the clusters that are otherwise
  indistinguishable at trigger time.
- **`ux-process-workflow` renamed to `design-process-methods`.** "Process" and
  "workflow" are synonyms; the old name conveyed nothing.
- **Seven skills had Title Case `name:` values**, which are invalid as plugin
  skill invocation names. All now match their directory.
- **All 34 merged commands** gained `name:` and a quoted `argument-hint:`, lost
  the unrecognized `tier:` field, and — for the 31 that need a target — gained
  the input guard that stops a command auditing a hypothetical interface.

### Fixed

- **`/audit` scored the same analysis twice.** Sections B and E both ran Laws of
  UX and Gestalt, and section E.1 weighted them separately at 15% and 20% — so
  one cognitive lens carried 35% of the composite score, and the two sections
  could return different scores for the same interface. Merged into one Section
  B, keeping E's better table (violation examples and a rating scale) plus the
  three laws only B had, and adopting E's attention-mapping and
  decision-architecture subsections. Sections renumbered A–E.
- **The NNG hamburger finding was overstated in five more files** that arrived
  with the merge, as "~50%" or "50%+". NNG measured discoverability in a
  179-participant, six-site study and found it cut by *nearly half*; "~50%" makes
  a range into a point figure and "50%+" asserts a floor NNG never reported.

### Removed

- **The 31 numbered redirect stubs** (`01-ground` … `30-iterate`, `guide`). They
  aliased chef-sumi's pre-v8 numbered scheme onto its v8 names — a migration path
  no user of this plugin ever walked, since everyone installed is on 3.1.0 where
  the namespace is `/sumi:*`. They were also 62 validator errors and would have
  been 31 of 68 entries in the `/` menu with no body but "run X instead."
- **Eight 3.1.0 commands** whose chef-sumi equivalent is a strict superset:
  `/accessibility-check` → `/a11y`; `/ux-audit`, `/design-review`, and
  `/cognitive-check` → `/audit`; `/component-build` → `/component`;
  `/generate-design-tokens` → `/tokens`; `/design-critique` → `/roast`;
  `/ux-metrics-plan` → `/measure`. `/figma-to-code` and `/ai-ux-audit` were kept
  and renamed to `/figma` and `/ai-audit`. The rename table lives in `/sumi`.

### Known gaps

- **Convert and Localize have no command.** They run as orchestrator pipelines.
- **63 of the 93 extracted claims are untriaged** — everything the merge brought
  in. `conversion-optimization-patterns` is the highest-risk cluster. See
  `AUDIT.md`; do not repeat those figures in client-facing work.
- **35 SKILL.md files exceed the 150-line budget**, `animation-recipe-library`
  worst at 2,317. Scheduled for v4.1.0; the validator warns so it cannot worsen
  unnoticed.

## [3.1.0] — 2026-08-06

Repackaging release. No knowledge content was removed; every change is to
identity, manifests, and frontmatter so the plugin installs and loads correctly.

### Changed

- **Renamed to Sumi.** Plugin `name` is now `sumi`, marketplace is
  `sumi-marketplace`, and the repository is `phazurlabs/sumi`. Commands are
  namespaced `/sumi:<command>`.
  - Install: `/plugin marketplace add phazurlabs/sumi` then
    `/plugin install sumi@sumi-marketplace`
- **Skill names are now kebab-case and match their directory.** Fifteen skills
  previously used display-style names containing spaces, ampersands, and commas
  (for example `Accessibility & Inclusive Design`), which produced invalid
  invocation names, since a plugin skill's frontmatter `name` sets the last
  segment of its command.
- **Skill descriptions rewritten** to lead with the key use case and carry the
  trigger vocabulary that previously lived in `triggers:`. All descriptions are
  260–320 characters, well inside the 1,536-character listing cap.
- **License is Apache-2.0 everywhere.** `README.md` and `marketplace.json`
  previously declared MIT while `LICENSE`, `NOTICE`, and `plugin.json` declared
  Apache-2.0.

### Fixed — citation accuracy

Empirical claims were audited against primary sources (see `AUDIT.md`). Six
defects corrected:

- **Dark mode power saving** stated as "3-6x." A reduction cannot exceed 1x; the
  real figure is 3-9% at typical brightness, ~42% at full (Dash & Hu, MobiSys
  2021). Off by roughly two orders of magnitude.
- **"Google's A2UI research shows 72% user preference"** (two locations). The
  figure is real but comes from arXiv:2508.19227; A2UI is a separate Google spec.
- **NNG hamburger-menu finding** described as reducing "engagement by 50% or
  more." NNG measured discoverability, not engagement.
- **Two Baymard Institute statistics** ("icon-only navigation reduces
  discoverability by 50%+", "left-aligned navigation tests 15% faster") could not
  be located in Baymard's published research. Guidance retained where
  independently supported; figures removed. The second was being used as a
  teaching example of what evidence looks like.
- **WCAG 3.0 citation** flagged as superseded by the March 2026 draft.

Added `AUDIT.md` and `scripts/extract-claims.py` so citation accuracy is an
auditable, repeatable property rather than an assertion. Six claims from the
first pass and ten from the wider extraction remain unverified and are listed.

### Fixed — caught by `claude plugin validate --strict`

Running the authoritative validator surfaced defects the repo's own Python
checker missed. All fixed, and the CLI check is now a CI gate:

- **`argument-hint` values were unquoted.** `[a] [b]` is invalid YAML outright;
  even `[a, b]` parses as a list rather than a string. Claude Code drops **all**
  frontmatter for a file whose YAML fails to parse, so `/sumi:figma-to-code`
  would have loaded with no name and no description. All 11 now quoted.
- **`license` at marketplace top level is not a recognized field** and is ignored
  at load time. Removed; per-plugin licenses are authoritative and are still
  checked for agreement by `scripts/validate-plugin.py`.
- **marketplace.json had no `description`.** Added.
- **`license-preflight.yml` was not valid YAML.** A heredoc inside a `run: |`
  block had its body at column zero, which terminates the block scalar — the
  workflow would not have parsed on GitHub. Rebuilt; both workflows now verified
  to parse.
- **`scripts/validate-plugin.py` now parses frontmatter with a real YAML parser**
  and fails on values that parse to the wrong type. Regression-tested against
  both reintroduced failure modes.

### Removed

- **`triggers:` frontmatter (243 entries across 19 skills).** Not a field in the
  Agent Skills spec and not read by Claude Code; its presence caused a hard
  error when packaging skills or uploading to claude.ai.
- **`user_invocable: true` from all 10 command files.** The correct spelling is
  `user-invocable`, and `true` is already the default.
- **Component path arrays from `plugin.json`.** `skills/` and `commands/` are
  auto-discovered. The declared paths were also invalid: they omitted the
  required `./` prefix and pointed at `SKILL.md` files rather than the
  directories containing them.

### Added — orchestration and onboarding

The plugin had 19 independent skills, no router, no agents, no entry point, and
no argument handling on any command. A new user typing `/sumi:ux-audit` with
nothing got an audit of an imaginary interface. Fixed:

- **`sumi-orchestrator` skill.** Routes any request to a pipeline — Evaluate,
  Create, Implement, Systematize, Handoff, Localize, AI Surface, Measure — each
  with ordered stages, a gate that must pass before the next stage, and a named
  output artifact. Platform skills (mobile, desktop, ambient) layer in.
- **`/sumi:start` command.** Zero-knowledge entry point. Asks one plain-language
  question, routes via the orchestrator, and matches the user's register rather
  than requiring them to learn UX vocabulary.
- **`argument-hint` on all 10 existing commands**, so `/` shows what each expects.
- **Input guards on all 10.** With no target and none evident from context, a
  command now asks and stops instead of analyzing something hypothetical.
- **README quick start** with separate paths for first-time and expert users.

### Added

- `plugin.json` now declares `$schema`, `displayName`, `author`, `homepage`,
  `repository`, and `keywords` for marketplace discoverability.
- `scripts/validate-plugin.py`, a dependency-free structural validator, wired
  into the license preflight workflow.
- This changelog.

### Fixed

- Two pairs of reference files shared a filename across skills. Renamed to
  reflect their actual scope and wired into their skill's navigation:
  - `ui-visual-design-system/references/design-token-architecture.md` →
    `design-systems-architecture/references/design-token-implementation.md`
  - `agentic-ai-generative-ux/references/ai-native-interface-patterns.md` →
    `agentic-ai-generative-ux/references/ai-interface-archetypes.md`
- `commands/design-review.md` claimed 10 skill domains; there are 19.
- README architecture diagram placed `marketplace.json` at the repository root;
  it lives in `.claude-plugin/`. File count corrected from 87 to 89.
- CLA workflow linked to a repository path that no longer exists.

## [3.0.0] — 2026

- 19 skills, 55 reference files, 10 commands, 310K+ words.
- Added cognitive psychology, component code cookbooks (React/SwiftUI/CSS),
  design critique and case studies, Figma MCP workflows, performance and state
  patterns, cross-cultural i18n, and ambient/calm technology.
- Applied Apache-2.0 licensing, CLA enforcement, and license preflight CI.
