#!/usr/bin/env python3
"""Structural validation for the Sumi Claude Code plugin.

Checks the things that silently break a plugin at load or package time:
manifest shape, kebab-case skill names matching their directory, and
frontmatter fields outside the Agent Skills spec.

Complements `claude plugin validate . --strict`, which is authoritative and
should gate every release. This script needs only Python 3, runs in CI without
the CLI, and additionally checks cross-file concerns the CLI does not: license
agreement across manifests, kebab-case skill names, and duplicate reference
filenames.

Usage:  python3 scripts/validate-plugin.py [plugin_root]
Exit:   0 clean, 1 on any error.
"""
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # fall back to line parsing; type errors go undetected
    yaml = None

# Fields allowed by the Agent Skills spec. Anything else is a hard error when
# packaging with package_skill.py or uploading to claude.ai.
SPEC_FIELDS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
}
# Claude Code accepts more than the spec; these are safe locally but block the
# claude.ai / Skills API distribution path.
CLAUDE_CODE_ONLY = {
    "when_to_use", "argument-hint", "arguments", "disable-model-invocation",
    "user-invocable", "disallowed-tools", "model", "effort", "context", "agent",
    "background", "hooks", "paths", "shell",
}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DESC_CAP = 1536
# SKILL.md loads in full every time the skill triggers; references load only when
# the SKILL.md points at them. Past this, the body belongs in references/.
SKILL_LINE_BUDGET = 150

errors: list[str] = []
warnings: list[str] = []


def parse_frontmatter(path: pathlib.Path) -> dict[str, object] | None:
    """Parse YAML frontmatter, preferring a real YAML parser.

    The naive line-splitting fallback cannot detect a value that is valid YAML
    but the wrong type -- `argument-hint: [a, b]` parses as a list, not a string,
    and `[a] [b]` fails outright. Claude Code drops ALL frontmatter for a file
    whose YAML fails to parse, so this must be caught here.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    try:
        end = text.index("\n---", 4)
    except ValueError:
        return None
    block = text[4:end]

    if yaml is not None:
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError as exc:
            errors.append(
                f"{path}: YAML frontmatter fails to parse ({exc.__class__.__name__}); "
                "Claude Code loads this file with ALL frontmatter silently dropped"
            )
            return {}
        if parsed is None:
            return {}
        if not isinstance(parsed, dict):
            errors.append(f"{path}: frontmatter is not a mapping")
            return {}
        for key, value in parsed.items():
            if not isinstance(value, (str, bool, int, float)):
                errors.append(
                    f"{path}: '{key}' parses as {type(value).__name__}, not a string "
                    f"-- quote the value (unquoted [brackets] become a YAML list)"
                )
        return parsed

    fields: dict[str, object] = {}
    for line in block.split("\n"):
        if not line.strip() or line.startswith((" ", "\t", "#", "-")):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_manifest(root: pathlib.Path) -> None:
    path = root / ".claude-plugin" / "plugin.json"
    if not path.exists():
        errors.append("missing .claude-plugin/plugin.json")
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"plugin.json is not valid JSON: {exc}")
        return

    name = data.get("name")
    if not name:
        errors.append("plugin.json: 'name' is required")
    elif not KEBAB.match(name):
        errors.append(f"plugin.json: name '{name}' must be kebab-case")

    # Component paths must be relative and start with './'. Auto-discovery is
    # preferred, so flag their presence at all.
    for key in ("skills", "commands", "agents", "workflows", "outputStyles"):
        if key not in data:
            continue
        values = data[key] if isinstance(data[key], list) else [data[key]]
        warnings.append(f"plugin.json: '{key}' is set; {key}/ is auto-discovered")
        for value in values:
            if isinstance(value, str) and not value.startswith("./") and value != ".":
                errors.append(f"plugin.json: {key} path '{value}' must start with './'")

    if not data.get("version"):
        warnings.append("plugin.json: no 'version'; commit SHA will be used")

    # License must agree across every file that declares one.
    licenses = {"plugin.json": data.get("license")}
    mp = root / ".claude-plugin" / "marketplace.json"
    if mp.exists():
        mp_data = json.loads(mp.read_text(encoding="utf-8"))
        licenses["marketplace.json"] = mp_data.get("license")
        for entry in mp_data.get("plugins", []):
            licenses[f"marketplace.json[{entry.get('name')}]"] = entry.get("license")
    declared = {v for v in licenses.values() if v}
    if len(declared) > 1:
        errors.append(f"license mismatch across manifests: {licenses}")


def check_skills(root: pathlib.Path) -> None:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        errors.append("missing skills/ directory")
        return
    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir():
            continue
        path = child / "SKILL.md"
        if not path.exists():
            errors.append(f"{child.name}/: no SKILL.md")
            continue
        fields = parse_frontmatter(path)
        if fields is None:
            errors.append(f"{child.name}/SKILL.md: missing or malformed frontmatter")
            continue

        name = str(fields.get("name") or "")
        if not name:
            warnings.append(f"{child.name}/SKILL.md: no 'name'; falls back to directory")
        else:
            if not KEBAB.match(name):
                errors.append(
                    f"{child.name}/SKILL.md: name '{name}' is not kebab-case "
                    "(a plugin skill's name becomes its command)"
                )
            elif name != child.name:
                warnings.append(
                    f"{child.name}/SKILL.md: name '{name}' differs from directory"
                )

        desc = str(fields.get("description") or "")
        if not desc:
            errors.append(f"{child.name}/SKILL.md: no 'description'")
        elif len(desc) > DESC_CAP:
            errors.append(
                f"{child.name}/SKILL.md: description {len(desc)} chars exceeds {DESC_CAP}"
            )

        for key in set(fields) - SPEC_FIELDS:
            if key in CLAUDE_CODE_ONLY:
                warnings.append(
                    f"{child.name}/SKILL.md: '{key}' is Claude Code-only; "
                    "blocks claude.ai upload and package_skill.py"
                )
            else:
                errors.append(
                    f"{child.name}/SKILL.md: unrecognized frontmatter field '{key}'"
                )


def check_commands(root: pathlib.Path) -> None:
    commands_dir = root / "commands"
    if not commands_dir.is_dir():
        return
    for path in sorted(commands_dir.glob("*.md")):
        fields = parse_frontmatter(path)
        if fields is None:
            errors.append(f"commands/{path.name}: missing or malformed frontmatter")
            continue
        if not str(fields.get("description") or ""):
            errors.append(f"commands/{path.name}: no 'description'")
        for key in set(fields) - SPEC_FIELDS - CLAUDE_CODE_ONLY:
            errors.append(f"commands/{path.name}: unrecognized field '{key}'")


def check_layout(root: pathlib.Path) -> None:
    # Only plugin.json and marketplace.json belong in .claude-plugin/.
    meta = root / ".claude-plugin"
    if meta.is_dir():
        allowed = {"plugin.json", "marketplace.json", "marketplace.extended.json"}
        for child in meta.iterdir():
            if child.is_dir():
                errors.append(
                    f".claude-plugin/{child.name}/: components must live at the plugin root"
                )
            elif child.name not in allowed:
                warnings.append(f".claude-plugin/{child.name}: unexpected file")

    # A shared basename across skills makes cross-references ambiguous.
    seen: dict[str, list[str]] = {}
    for path in root.glob("skills/*/references/*.md"):
        seen.setdefault(path.name, []).append(str(path.relative_to(root)))
    for name, paths in sorted(seen.items()):
        if len(paths) > 1:
            warnings.append(f"duplicate reference filename '{name}': {', '.join(paths)}")


def check_counts(root: pathlib.Path, skills: int, references: int, commands: int) -> None:
    """Fail when a manifest or README states a count that disagrees with the tree.

    The counts appear in nine places across manifests, README, and commands. They
    drifted every previous release because nothing checked them. Globbed truth is
    the only authority; anything asserting a different number is stale.
    """
    patterns = [
        (re.compile(r"(\d+)\s+skills\b", re.I), skills, "skills"),
        (re.compile(r"(\d+)\s+reference(?:\s+files)?\b", re.I), references, "references"),
        (re.compile(r"(\d+)\s+commands\b", re.I), commands, "commands"),
        # Table form, where the number FOLLOWS the label: | Skills | **44** |
        # The label-first patterns above cannot see these, which is how a stale
        # "43 skills / 168 references" summary table survived a release.
        (re.compile(r"^\|\s*Skills\s*\|\s*\**(\d+)", re.I | re.M), skills, "skills"),
        (re.compile(r"^\|\s*(?:Deep\s+)?[Rr]eference\s+files\s*\|\s*\**(\d+)", re.M),
         references, "references"),
        (re.compile(r"^\|\s*(?:Executable\s+)?[Cc]ommands\s*\|\s*\**(\d+)", re.M),
         commands, "commands"),
    ]
    targets = [
        root / ".claude-plugin" / "plugin.json",
        root / ".claude-plugin" / "marketplace.json",
        root / "README.md",
    ]
    for path in targets:
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            for pattern, truth, label in patterns:
                for match in pattern.finditer(line):
                    stated = int(match.group(1))
                    if stated != truth:
                        errors.append(
                            f"{path.relative_to(root)}:{lineno}: says {stated} {label}, "
                            f"tree has {truth}"
                        )


def check_skill_size(root: pathlib.Path) -> None:
    """Report oversized SKILL.md files as one line, not one per file.

    Most of the corpus is over budget today, so per-file warnings would be 35
    lines of noise that hide everything else. A single summary naming the worst
    offenders stays readable and still moves when someone makes it worse.
    """
    over = []
    for skill_md in sorted(root.glob("skills/*/SKILL.md")):
        lines = len(skill_md.read_text().splitlines())
        if lines > SKILL_LINE_BUDGET:
            over.append((lines, skill_md.parent.name))
    if not over:
        return
    over.sort(reverse=True)
    worst = ", ".join(f"{name} ({n})" for n, name in over[:3])
    warnings.append(
        f"{len(over)} SKILL.md files exceed the {SKILL_LINE_BUDGET}-line budget "
        f"(SKILL.md loads in full on every trigger; references do not). "
        f"Worst: {worst}"
    )


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(f"validating {root}\n")

    check_manifest(root)
    check_skills(root)
    check_commands(root)
    check_layout(root)
    check_skill_size(root)
    check_counts(
        root,
        len(list(root.glob("skills/*/SKILL.md"))),
        len(list(root.glob("skills/*/references/*.md"))),
        len(list(root.glob("commands/*.md"))),
    )

    for warning in warnings:
        print(f"  warn  {warning}")
    for error in errors:
        print(f"  FAIL  {error}")

    skills = len(list(root.glob("skills/*/SKILL.md")))
    commands = len(list(root.glob("commands/*.md")))
    references = len(list(root.glob("skills/*/references/*.md")))
    print(
        f"\n{skills} skills, {references} references, {commands} commands  |  "
        f"{len(errors)} errors, {len(warnings)} warnings"
    )
    if errors:
        print("\nFAILED")
        return 1
    print("\nPASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
