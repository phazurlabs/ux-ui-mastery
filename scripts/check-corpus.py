#!/usr/bin/env python3
"""Knowledge-graph and budget checks for the Sumi corpus.

`validate-plugin.py` is the release gate: absolute, deterministic, load-time
breakage only. This script is the ratchet: it measures properties the corpus is
already in debt on, freezes that debt, and forbids more of it. Mixing the two
would mean every baseline bump edits the release gate's blast radius.

What this proves: the graph is navigable and the shapes are consistent -- no
pointer dangles, no retired name lingers, no file silently doubles, no artifact
carries two schemas, no description drifts into its neighbour.

What it does NOT prove: that the knowledge is correct, that routing works in a
real session, or that the output is any good. A green run here is a statement
about plumbing. Do not read it as a quality signal.

Usage:  python3 scripts/check-corpus.py [graph|shape|routing|budget|all] [root]
                                        [--update-baseline]
Exit:   0 clean, 1 on any error.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sumi_corpus import (  # noqa: E402
    Corpus, content_words, estimate_tokens, iter_prose_lines, load_corpus,
    reachable_references, resolve_reference_mentions,
)

errors: list[str] = []
warnings: list[str] = []
improved: list[str] = []
measured: dict = {}

# Tier 1 is the only cost paid on every session regardless of what the user does,
# so it gets a fixed line rather than a ratchet. 4,331 today: 3,124 for the 43
# skill descriptions plus 1,207 for the 37 command descriptions -- both are in the
# listing the model always sees, and counting only the skills understates it by a
# quarter. 5,000 leaves room for roughly ten more skills before the line moves.
ALWAYS_ON_CEILING = 5_000
# Ceilings for files that do not yet exist. Existing debt is frozen by ratchet;
# new debt is simply forbidden.
NEW_SKILL_CEILING = 8_000
NEW_COMMAND_CEILING = 12_500
NEW_REFERENCE_CEILING = 40_000
# Two skills genuinely converging is a routing failure regardless of history.
COLLISION_CEILING = 0.30
# Absorbs reflows and typo fixes without admitting real content.
GROWTH_EPSILON = 1.02

HTML_TAGS = frozenset("""
a abbr address area article aside audio b base bdi bdo blockquote body br button
canvas caption cite code col colgroup data datalist dd del details dfn dialog div
dl dt em embed fieldset figcaption figure footer form h1 h2 h3 h4 h5 h6 head
header hgroup hr html i iframe img input ins kbd label legend li link main map
mark menu meta meter nav noscript object ol optgroup option output p param
picture pre progress q rp rt ruby s samp script search section select slot small
source span strong style sub summary sup table tbody td template textarea tfoot
th thead time title tr track u ul var video wbr svg path circle rect g defs line
polygon polyline ellipse text tspan use symbol clippath mask pattern stop
lineargradient radialgradient filter
""".split())

# Lines that look like code, imports, URLs, or asset paths never contain a
# slash-command. Without this filter the scanner returns ~1,300 hits on /div.
CODE_LINE = re.compile(
    r"https?://|\bimport\b|\bfrom\s+['\"]|src=|href=|url\(|@/|node_modules"
    r"|\.(?:tsx?|jsx?|css|json|svg|png|jpg|webp|woff2?)\b"
)


def _read_list(path: pathlib.Path) -> list[str]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text().split("\n"):
        line = line.split("#", 1)[0].strip()
        if line:
            out.extend(line.split())
    return out


def _baseline_path(root: pathlib.Path) -> pathlib.Path:
    return root / "tests" / "baseline.json"


def _load_baseline(root: pathlib.Path) -> dict:
    p = _baseline_path(root)
    return json.loads(p.read_text()) if p.exists() else {}


def _ratchet(label: str, actual: int, baseline: int | None, hint: str = "") -> None:
    """Fail only when a metric moves away from the budget."""
    if baseline is None:
        return
    if actual > baseline:
        errors.append(f"{label}: {actual}, baseline {baseline} — regression. {hint}".rstrip())
    elif actual < baseline:
        improved.append(f"{label}: improved to {actual} (baseline {baseline})")


# ---------------------------------------------------------------- graph

def check_reference_resolution(corpus: Corpus) -> None:
    """ERROR. Zero violations today, and it protects the whole refactor:
    reconnecting the corpus creates ~150 new pointers, and a single typo
    silently re-orphans a 1,800-line file with no other symptom."""
    for doc in corpus.docs:
        _, unresolved = resolve_reference_mentions(doc, corpus)
        for lineno, raw in unresolved:
            rel = doc.path.relative_to(corpus.root)
            errors.append(f"{rel}:{lineno}: '{raw}' does not resolve to a file on disk")


def check_orphan_references(corpus: Corpus, baseline: dict) -> None:
    """RATCHET, keyed per skill.

    Per skill rather than one global integer: with a single total, indexing five
    references in one skill would mask orphaning five in another and the check
    stays green. Per-skill keys make regressions local and make the baseline diff
    read like a changelog.
    """
    reached = reachable_references(corpus)
    per_skill: dict[str, int] = {}
    for (skill, _base) in set(corpus.references) - reached:
        per_skill[skill] = per_skill.get(skill, 0) + 1
    measured["orphan_references"] = dict(sorted(per_skill.items()))
    base = baseline.get("orphan_references", {})
    for skill in sorted(set(per_skill) | set(base)):
        _ratchet(
            f"orphan_references[{skill}]", per_skill.get(skill, 0), base.get(skill, 0),
            "add rows to its reference index so progressive disclosure can reach them.",
        )


def check_reference_index_present(corpus: Corpus, baseline: dict) -> None:
    """RATCHET by name + ERROR for anything new.

    A skill shipping references with zero working pointers has no progressive
    disclosure at all. Grandfathering by NAME rather than by count is the rule
    that makes the corpus monotonically improve: existing debt may stay, new debt
    is an error.
    """
    reached = reachable_references(corpus)
    offenders = sorted(
        name for name, doc in corpus.skills.items()
        if doc.refs_on_disk and not any(s == name for s, _ in reached)
    )
    measured["skills_without_reference_index"] = offenders
    grandfathered = set(baseline.get("skills_without_reference_index", []))
    for name in offenders:
        if name not in grandfathered:
            errors.append(
                f"{name}: ships references/ but no SKILL.md pointer resolves to any of them"
            )
    for name in sorted(grandfathered - set(offenders)):
        improved.append(f"{name}: now indexes its references")


def check_retired_commands(corpus: Corpus, root: pathlib.Path) -> None:
    """ERROR, from an explicit list -- zero false positives by construction.

    Scans INSIDE fenced code blocks on purpose: the defect this exists to catch
    lives in a fenced ASCII pipeline diagram, which is exactly why the v4.0.0
    manual repair pass missed it.
    """
    retired = _read_list(root / "tests" / "retired-commands.txt")
    if not retired:
        return
    pattern = re.compile(
        r"(?:^|[\s(\[])/(" + "|".join(sorted(map(re.escape, retired), key=len, reverse=True))
        + r")(?=[\s.,;:!?)\]`*]|$)"
    )
    for doc in corpus.docs:
        rel = doc.path.relative_to(corpus.root)
        # sumi.md's "Renamed in v4.0.0" table names retired commands deliberately.
        if rel.as_posix() == "commands/sumi.md":
            continue
        for lineno, line in enumerate(doc.text.split("\n"), 1):
            for m in pattern.finditer(line):
                errors.append(
                    f"{rel}:{lineno}: '/{m.group(1)}' was retired; "
                    f"no commands/{m.group(1)}.md exists"
                )


def check_unknown_slash_tokens(corpus: Corpus, root: pathlib.Path, baseline: dict) -> None:
    """RATCHET on DISTINCT names -- the safety net for the next rename.

    Ratcheting on total hits would let one new stale name appear thirty times in
    a diagram without tripping anything.
    """
    allow = set(_read_list(root / "tests" / "slash-token-allowlist.txt"))
    allow |= set(_read_list(root / "tests" / "retired-commands.txt"))
    known = set(corpus.commands)
    found: set[str] = set()
    token = re.compile(r"(?:^|[\s(\[])/([a-z][a-z0-9-]{1,30})(?=[\s.,;:!?)\]`*]|$)")
    for doc in corpus.docs:
        for _lineno, line in enumerate(doc.text.split("\n"), 1):
            if CODE_LINE.search(line):
                continue
            for m in token.finditer(line):
                name = m.group(1)
                if name in known or name in allow or name in HTML_TAGS:
                    continue
                found.add(name)
    measured["unknown_slash_tokens"] = sorted(found)
    _ratchet(
        "unknown_slash_tokens", len(found),
        len(baseline.get("unknown_slash_tokens", [])),
        f"new: {sorted(found - set(baseline.get('unknown_slash_tokens', [])))} — "
        f"add to tests/slash-token-allowlist.txt if legitimate.",
    )


def check_orchestrator_resolution(corpus: Corpus) -> None:
    """ERROR, bidirectional. The reverse direction is the valuable one: it
    catches 'you added a skill and nothing routes to it'."""
    orch = corpus.skills.get("sumi-orchestrator")
    if orch is None:
        errors.append("sumi-orchestrator skill is missing")
        return
    text = orch.text
    for m in re.finditer(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`", text):
        name = m.group(1)
        if name.endswith(".md") or "/" in name:
            continue
        if name in corpus.skills or name in corpus.commands:
            continue
        # Only flag tokens shaped like a skill slug that resolve to nothing.
        if name.count("-") >= 1 and name not in {"anti-patterns", "design-to-code"}:
            errors.append(f"sumi-orchestrator: '{name}' is not a skill or command")
    for name in sorted(corpus.skills):
        if name == "sumi-orchestrator":
            continue
        if f"`{name}`" not in text:
            errors.append(f"sumi-orchestrator: skill '{name}' is never routed to")


def check_command_cross_references(corpus: Corpus) -> None:
    """ERROR. 333 entries across 33 commands, all resolving today."""
    for name, doc in corpus.commands.items():
        section = re.search(r"^## Cross-References$(.*?)(?=^## |\Z)", doc.body, re.M | re.S)
        if not section:
            continue
        for lineno, line in enumerate(section.group(1).split("\n"), 1):
            m = re.match(r"\s*[-*]\s+`([a-z0-9-]+)`", line)
            if m and m.group(1) not in corpus.skills:
                errors.append(
                    f"commands/{name}.md: cross-reference '{m.group(1)}' is not a skill"
                )


def check_artifact_schemas(corpus: Corpus, root: pathlib.Path) -> None:
    """ERROR with a waiver file.

    Attributes each fenced json block to the `.sumi/*.json` path mentioned within
    the preceding 25 lines, then fails when one artifact has more than one
    top-level key set. This is precisely the check that catches /style writing
    style.json two different ways 90 lines apart.

    Fixing the conflict means DELETING a line from the waiver file, which is a
    better incentive than silence.
    """
    waived = set(_read_list(root / "tests" / "schema-waivers.txt"))
    shapes: dict[str, dict[frozenset, list[str]]] = {}
    artifact_re = re.compile(r"\.sumi/([a-z0-9-]+(?:-\*)?\.json)")
    for name, doc in corpus.commands.items():
        lines = doc.text.split("\n")
        i = 0
        while i < len(lines):
            if lines[i].strip().startswith("```json"):
                start = i
                i += 1
                block = []
                while i < len(lines) and not lines[i].strip().startswith("```"):
                    block.append(lines[i])
                    i += 1
                context = "\n".join(lines[max(0, start - 25):start])
                hits = artifact_re.findall(context)
                if hits:
                    # Dedent first: these blocks are often nested inside a
                    # numbered list, and an indent-sensitive key regex silently
                    # sees zero top-level keys and reports no conflict.
                    body = [ln for ln in block if ln.strip()]
                    pad = min((len(ln) - len(ln.lstrip()) for ln in body), default=0)
                    flat = "\n".join(ln[pad:] for ln in block)
                    keys = frozenset(
                        m.group(1) for m in re.finditer(r'^  "([^"]+)"\s*:', flat, re.M)
                    )
                    if keys:
                        art = hits[-1]
                        shapes.setdefault(art, {}).setdefault(keys, []).append(
                            f"commands/{name}.md:{start + 1}"
                        )
            i += 1
    measured["artifact_schema_conflicts"] = sorted(
        a for a, s in shapes.items() if len(s) > 1
    )
    for artifact, sets in sorted(shapes.items()):
        if len(sets) > 1 and artifact not in waived:
            sites = "; ".join(
                f"{{{', '.join(sorted(k)[:4])}...}} at {v[0]}" for k, v in sets.items()
            )
            errors.append(
                f".sumi/{artifact} has {len(sets)} different top-level key sets: {sites}"
            )


# ---------------------------------------------------------------- shape

def check_required_sections(corpus: Corpus, baseline: dict) -> None:
    """RATCHET by name. Same grandfather rule: a NEW command without gates errors."""
    for section, key in (("## Quality Gates", "commands_without_quality_gates"),
                         ("## Cross-References", "commands_without_cross_references")):
        missing = sorted(n for n, d in corpus.commands.items() if section not in d.body)
        measured[key] = missing
        grandfathered = set(baseline.get(key, []))
        for name in missing:
            if name not in grandfathered:
                errors.append(f"commands/{name}.md: missing '{section}' section")
        for name in sorted(grandfathered - set(missing)):
            improved.append(f"commands/{name}.md: now has '{section}'")


def check_description_collisions(corpus: Corpus, baseline: dict) -> None:
    """RATCHET plus an absolute ceiling.

    Two skills converging past 0.30 are indistinguishable to the router
    regardless of what the baseline says.
    """
    vecs = {n: content_words(d.description) for n, d in corpus.skills.items()}
    names = sorted(vecs)
    worst, pair = 0.0, ("", "")
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            union = vecs[a] | vecs[b]
            if not union:
                continue
            j = len(vecs[a] & vecs[b]) / len(union)
            if j > worst:
                worst, pair = j, (a, b)
            if j > COLLISION_CEILING:
                errors.append(
                    f"description collision {j:.3f} between '{a}' and '{b}' "
                    f"exceeds the {COLLISION_CEILING} ceiling"
                )
    measured["max_description_jaccard"] = round(worst, 4)
    base = baseline.get("max_description_jaccard")
    if base is not None and worst > base + 0.01:
        errors.append(
            f"max description collision rose to {worst:.3f} (baseline {base}) — "
            f"worst pair: {pair[0]} / {pair[1]}"
        )
    elif base is not None and worst < base - 0.001:
        improved.append(f"max_description_jaccard: improved to {worst:.4f} (baseline {base})")


# ---------------------------------------------------------------- budget

def check_budget(corpus: Corpus, baseline: dict) -> None:
    """Tier 1 absolute; tiers 2-4 per-file ratchet; new files hard-capped."""
    always_on = sum(
        estimate_tokens(d.description) for d in corpus.docs
    )
    measured["always_on_tokens"] = always_on
    if always_on > ALWAYS_ON_CEILING:
        errors.append(
            f"always-on descriptions total {always_on} tokens, ceiling "
            f"{ALWAYS_ON_CEILING} — this is the only cost paid on every session"
        )

    tiers = {
        "skills": ({n: estimate_tokens(d.path.read_text()) for n, d in corpus.skills.items()},
                   NEW_SKILL_CEILING),
        "commands": ({n: estimate_tokens(d.path.read_text()) for n, d in corpus.commands.items()},
                     NEW_COMMAND_CEILING),
        "references": ({f"{s}/{b}": estimate_tokens(p.read_text())
                        for (s, b), p in corpus.references.items()}, NEW_REFERENCE_CEILING),
    }
    for tier, (sizes, ceiling) in tiers.items():
        measured.setdefault("budget", {})[tier] = sizes
        base = baseline.get("budget", {}).get(tier, {})
        for name, size in sorted(sizes.items()):
            prior = base.get(name)
            if prior is None:
                if size > ceiling:
                    errors.append(
                        f"{tier}/{name} is new at {size} tokens, ceiling {ceiling}"
                    )
            elif size > prior * GROWTH_EPSILON:
                errors.append(
                    f"{tier}/{name} grew {prior} -> {size} tokens (>2%)"
                )
        total = sum(sizes.values())
        prior_total = sum(base.values()) if base else None
        delta = f", baseline {prior_total} (delta {total - prior_total:+d})" if prior_total else ""
        warnings.append(f"tier {tier}: {len(sizes)} files, {total:,} tokens{delta}")


# ---------------------------------------------------------------- routing

def _tfidf(corpus: Corpus):
    import math
    docs = {n: content_words(d.description) for n, d in corpus.skills.items()}
    n_docs = len(docs)
    df: dict[str, int] = {}
    for words in docs.values():
        for w in words:
            df[w] = df.get(w, 0) + 1
    idf = {w: math.log((n_docs + 1) / (c + 1)) + 1 for w, c in df.items()}
    vecs = {}
    for name, words in docs.items():
        v = {w: idf[w] for w in words}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs[name] = {w: x / norm for w, x in v.items()}
    return vecs, idf


def rank_skills(query: str, vecs, idf) -> list[tuple[float, str]]:
    import math
    q = {w: idf.get(w, 1.0) for w in content_words(query)}
    norm = math.sqrt(sum(x * x for x in q.values())) or 1.0
    q = {w: x / norm for w, x in q.items()}
    scored = [
        (sum(q.get(w, 0.0) * s for w, s in v.items()), name) for name, v in vecs.items()
    ]
    return sorted(scored, reverse=True)


def check_routing(corpus: Corpus, root: pathlib.Path, baseline: dict) -> None:
    """RATCHET on the delta only.

    The absolute score is MEANINGLESS. TF-IDF cosine over 43 short descriptions
    is not a model of how Claude picks a skill -- no synonymy, no world
    knowledge, no instruction-following. What it is: a deterministic function of
    the description text that moves when that text changes. That makes it a
    change detector, and change detection is the only thing a free CI check can
    honestly provide.
    """
    fixtures_path = root / "tests" / "routing-fixtures.yaml"
    if not fixtures_path.exists():
        return
    try:
        import yaml
    except ImportError:
        warnings.append("routing: pyyaml not installed, skipping")
        return
    fixtures = yaml.safe_load(fixtures_path.read_text()) or []
    vecs, idf = _tfidf(corpus)
    top1 = top3 = forbid_hits = 0
    detail: list[str] = []
    for fx in fixtures:
        ranked = rank_skills(fx["prompt"], vecs, idf)
        names = [n for _s, n in ranked]
        ok = {fx["expect"], *(fx.get("also_ok") or [])}
        if names[0] in ok:
            top1 += 1
        else:
            detail.append(
                f"  {fx['id']}: expected {fx['expect']}"
                f"{' (also ok: ' + ', '.join(fx['also_ok']) + ')' if fx.get('also_ok') else ''}"
                f", got {names[0]} at rank 1"
            )
        if ok & set(names[:3]):
            top3 += 1
        for bad in fx.get("forbid") or []:
            if names[0] == bad:
                forbid_hits += 1
                detail.append(f"  {fx['id']}: FORBIDDEN {bad} ranked 1")
    measured["routing"] = {"top1": top1, "top3": top3,
                           "forbid_hits": forbid_hits, "n": len(fixtures)}
    base = baseline.get("routing")
    if base:
        if top1 < base["top1"]:
            errors.append(f"routing top1 regressed {base['top1']} -> {top1}")
        if top3 < base["top3"]:
            errors.append(f"routing top3 regressed {base['top3']} -> {top3}")
        if forbid_hits > base["forbid_hits"]:
            errors.append(
                f"routing forbid violations rose {base['forbid_hits']} -> {forbid_hits}"
            )
        if top1 > base["top1"] or top3 > base["top3"]:
            improved.append(f"routing: improved to top1={top1} top3={top3}")
    warnings.append(f"routing: top1 {top1}/{len(fixtures)}, top3 {top3}/{len(fixtures)}")
    for line in detail:
        warnings.append(line.strip())


# ---------------------------------------------------------------- main

def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    update = "--update-baseline" in sys.argv
    mode = args[0] if args and args[0] in {"graph", "shape", "routing", "budget", "all"} else "all"
    root = pathlib.Path(args[1] if len(args) > 1 else (args[0] if args and mode == "all" and args[0] not in {"all"} else ".")).resolve()
    if not (root / "skills").exists():
        root = pathlib.Path(".").resolve()

    corpus = load_corpus(root)
    baseline = _load_baseline(root)
    print(f"checking {root}  [{mode}]\n")

    if mode in {"graph", "all"}:
        check_reference_resolution(corpus)
        check_orphan_references(corpus, baseline)
        check_reference_index_present(corpus, baseline)
        check_retired_commands(corpus, root)
        check_unknown_slash_tokens(corpus, root, baseline)
        check_orchestrator_resolution(corpus)
        check_command_cross_references(corpus)
        check_artifact_schemas(corpus, root)
    if mode in {"shape", "all"}:
        check_required_sections(corpus, baseline)
        check_description_collisions(corpus, baseline)
    if mode in {"budget", "all"}:
        check_budget(corpus, baseline)
    if mode in {"routing", "all"}:
        check_routing(corpus, root, baseline)

    if update:
        merged = {**baseline, **measured}
        _baseline_path(root).parent.mkdir(exist_ok=True)
        _baseline_path(root).write_text(json.dumps(merged, indent=2, sort_keys=True) + "\n")
        print(f"baseline written to {_baseline_path(root).relative_to(root)}\n")
        return 0

    for w in warnings:
        print(f"  warn  {w}")
    for i in improved:
        print(f"  BETTER {i} — run with --update-baseline")
    for e in errors:
        print(f"  FAIL  {e}")

    orph = sum(measured.get("orphan_references", {}).values())
    print(
        f"\n{len(corpus.skills)} skills, {len(corpus.references)} references "
        f"({orph} orphaned), {len(corpus.commands)} commands  |  "
        f"{len(errors)} errors, {len(warnings)} warnings"
    )
    if errors:
        print("\nFAILED")
        return 1
    print("\nPASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
