#!/usr/bin/env python3
"""Validate the Endeavor Protocol package using only the Python standard library."""

from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path

NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_ROOT = (
    "README.md",
    "LICENSE",
    "VERSION",
    "BOOTSTRAP.md",
    "AGENTS.md",
    "endeavor-protocol.json",
    "docs/ARCHITECTURE.md",
    "docs/CAPABILITY_LADDER.md",
    "docs/RELEASE_CRITERIA.md",
)
REQUIRED_REFERENCES = (
    "protocol.md",
    "profiles.md",
    "roles.md",
    "evidence-and-closure.md",
    "state.md",
)
REQUIRED_TEMPLATES = (
    "AGENT_ENTRY.md",
    "PROJECT.md",
    "WORKPLAN.md",
    "DECISIONS.md",
    "EVIDENCE.md",
    "OPEN_QUESTIONS.md",
    "RISKS.md",
    "RUN_LOG.md",
    "HANDOFF.md",
)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("SKILL.md frontmatter is not closed")
    frontmatter_text = parts[1]
    body = parts[2].lstrip("\n")
    metadata: dict[str, str] = {}
    for raw_line in frontmatter_text.splitlines():
        if not raw_line or raw_line.startswith((" ", "\t")):
            continue
        if ":" not in raw_line:
            raise ValueError(f"Invalid frontmatter line: {raw_line}")
        key, value = raw_line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, body


def validate() -> list[str]:
    errors: list[str] = []
    root = repository_root()
    skill_root = root / "skills" / "endeavor-protocol"
    skill_path = skill_root / "SKILL.md"

    for relative in REQUIRED_ROOT:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    if not skill_path.is_file():
        errors.append("Missing required skill: skills/endeavor-protocol/SKILL.md")
        return errors

    try:
        metadata, body = parse_frontmatter(skill_path)
    except (OSError, ValueError) as error:
        errors.append(str(error))
        return errors

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not name:
        errors.append("SKILL.md frontmatter requires name")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append("Skill name must contain lowercase letters, numbers, and single hyphens only")
    elif name != skill_root.name:
        errors.append("Skill name must match its parent directory")

    if not description:
        errors.append("SKILL.md frontmatter requires description")
    elif len(description) > 1024:
        errors.append("Skill description exceeds 1024 characters")

    if len(skill_path.read_text(encoding="utf-8").splitlines()) > 500:
        errors.append("SKILL.md exceeds the 500-line progressive-disclosure limit")

    for name in REQUIRED_REFERENCES:
        if not (skill_root / "references" / name).is_file():
            errors.append(f"Missing skill reference: {name}")

    for name in REQUIRED_TEMPLATES:
        path = skill_root / "assets" / "state" / name
        if not path.is_file():
            errors.append(f"Missing state template: {name}")

    version_path = root / "VERSION"
    manifest_path = root / "endeavor-protocol.json"
    if version_path.is_file() and manifest_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"Invalid endeavor-protocol.json: {error}")
        else:
            if manifest.get("version") != version:
                errors.append("Manifest version does not match VERSION")
            skill_version = ""
            for line in skill_path.read_text(encoding="utf-8").splitlines():
                if line.strip().startswith("version:"):
                    skill_version = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
            if skill_version and skill_version != version:
                errors.append("Skill metadata version does not match VERSION")

    for script_name in ("bootstrap.py", "validate.py"):
        script_path = skill_root / "scripts" / script_name
        if not script_path.is_file():
            errors.append(f"Missing script: {script_name}")
            continue
        try:
            py_compile.compile(str(script_path), doraise=True)
        except py_compile.PyCompileError as error:
            errors.append(f"Python compile failure in {script_name}: {error.msg}")

    required_markers = (
        "Capability honesty",
        "Evidence rule",
        "Human approval rule",
        "Completion language",
    )
    for marker in required_markers:
        if marker not in body:
            errors.append(f"SKILL.md missing required section: {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Endeavor Protocol validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print("Endeavor Protocol validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
