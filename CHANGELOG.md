# Changelog

All notable changes to this project are documented here. This project follows
[Semantic Versioning](https://semver.org).

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
