#!/usr/bin/env python3
"""Shared loader for the Sumi corpus.

Holds no checks. `check-corpus.py` imports this; `validate-plugin.py` deliberately
does not, so the release gate keeps zero dependencies on ratchet machinery.

The load-bearing function is `resolve_reference_mentions`. The corpus points at
reference files in three different syntaxes, and a resolver that handles only the
obvious one invents false orphans:

  1. `references/x.md`               own skill (95 uses)
  2. `other-skill/references/x.md`   cross-skill (16 uses)
  3. `` `x.md` ``                    bare basename under a "Reference Files"
                                     heading (14 uses, e.g.
                                     skills/animation-recipe-library/SKILL.md)

Form 3 is resolved only against the owning skill's own references. A bare `.md`
backtick that happens to match some other skill's filename is a coincidence, not
a pointer.
"""
from __future__ import annotations

import pathlib
import re
from dataclasses import dataclass, field

# Group 1 is an optional owning-skill prefix; group 2 is the basename.
PATH_FORM = re.compile(r"(?:([a-z0-9][a-z0-9-]*)/)?references/([A-Za-z0-9_.-]+\.md)")
BARE_FORM = re.compile(r"`([A-Za-z0-9_.-]+\.md)`")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def strip_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def frontmatter_value(raw: str, key: str) -> str:
    for line in raw.split("\n"):
        if line.startswith(f"{key}:"):
            return line[len(key) + 1:].strip().strip('"').strip("'")
    return ""


@dataclass
class Doc:
    """A SKILL.md or a command file."""
    name: str
    path: pathlib.Path
    kind: str                      # "skill" | "command"
    raw_frontmatter: str
    body: str
    description: str
    owner: str | None              # skill directory, or None for commands
    refs_on_disk: set[str] = field(default_factory=set)

    @property
    def text(self) -> str:
        return self.raw_frontmatter + "\n" + self.body


@dataclass
class Corpus:
    root: pathlib.Path
    skills: dict[str, Doc]
    commands: dict[str, Doc]
    references: dict[tuple[str, str], pathlib.Path]   # (skill, basename) -> path

    @property
    def docs(self) -> list[Doc]:
        return list(self.skills.values()) + list(self.commands.values())


def load_corpus(root: pathlib.Path) -> Corpus:
    root = pathlib.Path(root).resolve()

    references: dict[tuple[str, str], pathlib.Path] = {}
    for ref in sorted(root.glob("skills/*/references/*.md")):
        references[(ref.parent.parent.name, ref.name)] = ref

    skills: dict[str, Doc] = {}
    for skill_md in sorted(root.glob("skills/*/SKILL.md")):
        owner = skill_md.parent.name
        fm, body = strip_frontmatter(skill_md.read_text())
        skills[owner] = Doc(
            name=frontmatter_value(fm, "name") or owner,
            path=skill_md, kind="skill", raw_frontmatter=fm, body=body,
            description=frontmatter_value(fm, "description"), owner=owner,
            refs_on_disk={n for (s, n) in references if s == owner},
        )

    commands: dict[str, Doc] = {}
    for cmd in sorted(root.glob("commands/*.md")):
        fm, body = strip_frontmatter(cmd.read_text())
        commands[cmd.stem] = Doc(
            name=frontmatter_value(fm, "name") or cmd.stem,
            path=cmd, kind="command", raw_frontmatter=fm, body=body,
            description=frontmatter_value(fm, "description"), owner=None,
        )

    return Corpus(root=root, skills=skills, commands=commands, references=references)


def resolve_reference_mentions(
    doc: Doc, corpus: Corpus
) -> tuple[set[tuple[str, str]], list[tuple[int, str]]]:
    """Return (resolved (skill, basename) pairs, unresolved [(line_no, raw)]).

    A path-form mention without an owning-skill prefix inside a COMMAND is
    unresolvable by construction -- commands have no owning skill -- so it is
    reported rather than silently guessed at.
    """
    resolved: set[tuple[str, str]] = set()
    unresolved: list[tuple[int, str]] = []

    for lineno, line in enumerate(doc.text.split("\n"), 1):
        for m in PATH_FORM.finditer(line):
            prefix, base = m.group(1), m.group(2)
            owner = prefix or doc.owner
            if owner is None:
                unresolved.append((lineno, m.group(0)))
                continue
            if (owner, base) in corpus.references:
                resolved.add((owner, base))
            else:
                unresolved.append((lineno, m.group(0)))

        if doc.owner is not None:
            for m in BARE_FORM.finditer(line):
                base = m.group(1)
                if base in doc.refs_on_disk:
                    resolved.add((doc.owner, base))

    return resolved, unresolved


def reachable_references(corpus: Corpus) -> set[tuple[str, str]]:
    """Every reference any SKILL.md or command can route to.

    Reference files are deliberately NOT roots: measured on this corpus, they
    never point at each other, so transitive reachability equals direct.
    """
    reached: set[tuple[str, str]] = set()
    for doc in corpus.docs:
        got, _ = resolve_reference_mentions(doc, corpus)
        reached |= got
    return reached


def estimate_tokens(text: str) -> int:
    """Deterministic, dependency-free, monotonic in content.

    Calibrated 2026-08 by hand against messages.count_tokens on files spanning
    prose-heavy to code-heavy: within roughly -8% to +14% of true. Budgets are
    expressed in ESTIMATOR units, so tokenizer drift never moves a threshold --
    only relative change is ever asserted. The word-count floor matters: len//4
    alone systematically under-counts the CSS and TSX this corpus is full of.
    """
    return max(len(text) // 4, len(text.split()))


STOPWORDS = frozenset("""
a an and are as at be by for from has have in into is it its of on or that the
to use used using when with within your you their this these those than then
""".split())


def content_words(text: str) -> set[str]:
    words = re.findall(r"[a-z][a-z0-9-]{2,}", text.lower())
    return {w for w in words if w not in STOPWORDS}


def iter_prose_lines(text: str, skip_fences: bool = False):
    """Yield (line_no, line). Fences are KEPT by default.

    Retired command names live inside a fenced ASCII diagram in
    skills/design-process-methods/SKILL.md, so a scanner that skips fences misses
    the very defect it exists to catch.
    """
    in_fence = False
    for lineno, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if skip_fences and in_fence:
            continue
        yield lineno, line
