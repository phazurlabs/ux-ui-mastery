#!/usr/bin/env python3
"""Extract falsifiable empirical claims from the skill corpus for citation audit.

Finds sentences carrying BOTH a hard figure and a named source — the claims a
reader can check and Sumi can therefore be wrong about. Run after adding content;
every new hit needs a locatable primary source before it ships. See AUDIT.md.

Usage:  python3 scripts/extract-claims.py [--csv] [root]
"""
import pathlib
import re
import sys

FIGURE = re.compile(
    r"\b\d{1,3}(?:\.\d+)?%"          # percentages
    r"|\b\d+(?:\.\d+)?x\b"           # multipliers
    r"|\b\d{2,}(?:,\d{3})+\b"        # large counts
    r"|\b\d+\s?ms\b"                 # milliseconds
    r"|\b\d+(?:\.\d+)?\s+seconds?\b"
    r"|\b\d+\s+minutes?\b"
)
SOURCE = re.compile(
    r"\b(NN/?G|Nielsen Norman|Baymard|Forrester|Gartner|McKinsey|WebAIM|Deque"
    r"|Smashing|ACM|CHI|arXiv|Google|Microsoft|Apple|W3C|WCAG|Stanford|MIT"
    r"|Harvard|Purdue|Figma|Vercel)\b",
    re.IGNORECASE,
)
SKIP_PREFIX = ("|", "```", "#", ">")


def claims(root: pathlib.Path):
    for path in sorted(root.glob("skills/**/*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            text = line.strip().lstrip("-*").strip()
            if len(text) < 40 or line.strip().startswith(SKIP_PREFIX):
                continue
            if FIGURE.search(text) and SOURCE.search(text):
                yield path.relative_to(root), lineno, text


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--csv"]
    as_csv = "--csv" in sys.argv
    root = pathlib.Path(args[0] if args else ".").resolve()

    found = list(claims(root))
    if as_csv:
        import csv
        w = csv.writer(sys.stdout)
        w.writerow(["file", "line", "claim", "verdict", "primary_source"])
        for path, lineno, text in found:
            w.writerow([path, lineno, text, "", ""])
    else:
        for i, (path, lineno, text) in enumerate(found, 1):
            print(f"\n[{i}] {path}:{lineno}\n    {text}")
        print(f"\n{len(found)} falsifiable claims. Each needs a locatable "
              f"primary source — see AUDIT.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
