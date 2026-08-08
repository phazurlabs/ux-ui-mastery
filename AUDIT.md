# Citation Audit — v4.0.0

Sumi makes empirical claims. This file records which have been verified against
primary sources, which were corrected, and which are still outstanding. It is
maintained deliberately: the value of a research-grounded corpus is exactly its
citation accuracy, so that accuracy has to be auditable rather than asserted.

**Method.** Every sentence in `skills/` carrying both a hard figure (percentage,
multiplier, duration, magnitude) and a named source (NNG, Baymard, W3C, Google,
Stanford, MIT, ACM, arXiv, Forrester, and similar) is extracted programmatically
by `scripts/extract-claims.py`, then checked against the primary source where one
can be located.

**Status as of 2026-08-06.** The first pass used a narrower source list and
surfaced 20 sentences; all 20 were triaged (9 resolved, 6 outstanding, 5 needing
no external verification). The shipped script uses a wider list (adding Purdue,
Figma, Vercel, and case-insensitive matching) and surfaces **30**. The
**10 additional claims are not yet reviewed** — treat them as outstanding.

**Status as of 2026-08-08 (v4.0.0).** The merge with chef-sumi more than tripled
the corpus, and the extractor now surfaces **89** claims across 43 skills. The
honest position: **the 59 claims added by the merge have not been triaged.** The
19 skills audited in 3.1.0 keep their corrections — those files won the merge
precisely so the corrections would survive — but the 23 skills that arrived from
chef-sumi came with the same class of defect and have not been through this
process.

One family was fixed on the way in, because the correct wording was already
known from the 3.1.0 audit. The NNG hamburger finding appeared in five more
places, stated as "reduce discoverability by ~50%" or "by 50%+". NNG's study
(179 participants, six sites) found hidden navigation cuts discoverability by
*nearly half*; "~50%" turns a range into a point figure, and "50%+" asserts a
floor NNG never reported. All five now carry the study's actual finding and its
design: `ui-pattern-intelligence/references/anti-pattern-encyclopedia.md`,
`.../pattern-evolution-2024-2026.md`, `.../pattern-taxonomy-complete.md`,
`navigation-pattern-encyclopedia/SKILL.md`, and
`navigation-pattern-encyclopedia/references/mobile-navigation-patterns.md`.

**Highest-risk unreviewed cluster:** `conversion-optimization-patterns` carries
roughly a dozen Baymard- and Forrester-attributed conversion figures across
`cta-optimization.md`, `form-conversion.md`, `funnel-optimization.md`, and
`trust-persuasion-patterns.md`. Conversion statistics are the most-copied and
least-sourced numbers in the industry, and this skill is the one whose output
most directly influences revenue decisions. Treat every figure in it as
unverified until checked. `layout-block-intelligence/references/
social-proof-patterns.md` and `form-design-encyclopedia/SKILL.md` carry the same
risk in smaller quantity.

---

## Verified accurate

| Claim | Location | Source |
|---|---|---|
| W3C Design Tokens spec 2025.10, stable October 2025 | `design-systems-architecture` | DTCG announcement, 28 Oct 2025 |
| Fogg et al. 2003, 46.1% cited "design look" when assessing credibility | `cognitive-psychology-ux/references/neurodesign-engagement-science.md` | Fogg et al., *How Do Users Evaluate the Credibility of Web Sites?*, DUX 2003 (n≈2,500) |
| 5 participants surface ~85% of usability issues | `ux-research-methods` | Nielsen & Landauer, 1993 |

## Corrected in v3.1.0

| Was | Problem | Now |
|---|---|---|
| "WCAG 3.0 April 2026 Draft" (README) | April 2026 was a planned *timeline* publication, not a draft | "WCAG 3.0 Working Draft" |
| "Dark mode reduces screen power consumption by 3-6x" | Unit error. A reduction cannot exceed 1x; the real figure is a percentage, off by ~2 orders of magnitude | 3–9% at 30–50% brightness, ~42% at full brightness (Dash & Hu, MobiSys 2021) |
| "Google's A2UI research shows 72% user preference" (×2 locations) | Figure is real but comes from arXiv:2508.19227; A2UI is a separate Google spec | Attributed to arXiv:2508.19227 |
| "NNG: hamburger menus reduce engagement by 50% or more" | NNG measured *discoverability*, not engagement; "or more" overstates | Restated to NNG's actual finding and study design |
| "Baymard: icon-only navigation reduces discoverability by 50%+" | Figure not locatable in Baymard's published research; appears borrowed from the NNG hidden-navigation finding | Guidance kept (well-supported by both groups); invented figure removed |
| "Baymard: left-aligned navigation tests 15% faster" | Same — used as a *teaching example of evidence*, which made an unverifiable citation the model of good practice | Replaced with a verifiable NNG finding |

## Outstanding — not yet verified

Do not repeat these in marketing or client-facing work until checked.

| Claim | Location | Risk |
|---|---|---|
| Vasconcelos et al., "confidence indicators improve decision quality by 23%," cited in CHI 2025 workshops | `agentic-ai-generative-ux/references/conversational-ai-dialogue-patterns.md` | High — compound citation, specific figure |
| MIT Media Lab / Girouard et al. 2009, "neurofeedback-optimized designs increase engagement 20–30%" | `cognitive-psychology-ux/references/neurodesign-engagement-science.md` | High — specific figure, vague "recent extensions" |
| "40–60% of front-end time spent translating designs to code" (Forrester 2022; Figma State of Design 2023) | `figma-design-tool-workflows/references/figma-mcp-ai-flywheel.md` | High — dual citation, wide range |
| Digg v4: Reddit traffic +40%, Digg ~200M monthly pageviews | `design-critique-case-studies/references/redesign-failure-analysis.md` | Medium — historical, widely repeated |
| Google Plus: 90% of sessions under 5 seconds (2015 disclosure) | `design-critique-case-studies/references/redesign-failure-analysis.md` | Medium — widely repeated |
| "Every 100ms of latency reduces search engagement" | `cognitive-psychology-ux/references/laws-of-ux-encyclopedia.md` | Low — directionally well-established, figure imprecise |
| 10 further claims surfaced by the wider extraction | run the script | Unreviewed |
| ~12 Baymard/Forrester conversion figures | `conversion-optimization-patterns/references/` | **High** — most-copied least-sourced numbers in the industry, and this skill drives revenue decisions |
| WCAG 3.0 draft-status framing | `visual-design-mastery/SKILL.md`, `.../references/color-mastery.md` | Medium — the draft exists; only the date and status framing was ever the defect |
| 59 claims added by the chef-sumi merge | 23 newly merged skills | Unreviewed — see the v4.0.0 status note above |

## No external verification required

Restatements of WCAG success criteria (1.4.4, 2.2.1), internal metric
definitions, and generic guidance carrying an incidental number.

---

## Pattern worth carrying forward

The defects share a shape: **the design principle is sound and the figure is
often real, but the source attached to it is wrong.** Borrowed statistics get
reassigned to a more authoritative-sounding institution. This is harder to catch
than outright invention and more damaging when a reader checks, so the standing
rule for new content is: no figure ships without a locatable primary source, and
a principle that is true without a number should be stated without one.

## Reproducing the extraction

```bash
python3 scripts/extract-claims.py
```
