#!/usr/bin/env python3
"""Initialize Endeavor Protocol state in a new or existing project."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

PROTOCOL_VERSION = "0.1.0-alpha.1"
PROFILES = (
    "discovery",
    "delivery",
    "audit",
    "communications",
    "operations",
    "synthesis",
)
MODES = ("auto", "solo", "delegated", "orchestrated")
TEMPLATE_FILES = (
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


def template_root() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "state"


def _unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _render(text: str, *, project_name: str, profiles: Sequence[str], mode: str, date: str) -> str:
    profile_text = ", ".join(profile.title() for profile in profiles)
    replacements = {
        "{{PROJECT_NAME}}": project_name,
        "{{PROFILES}}": profile_text,
        "{{MODE}}": mode,
        "{{DATE}}": date,
        "{{PROTOCOL_VERSION}}": PROTOCOL_VERSION,
    }
    for marker, value in replacements.items():
        text = text.replace(marker, value)
    return text


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
        text=True,
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(temporary_name, path)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def initialize(
    target: Path,
    *,
    project_name: str,
    profiles: Sequence[str],
    mode: str,
    dry_run: bool = False,
    force: bool = False,
) -> list[Path]:
    """Create a non-destructive .endeavor state directory.

    Returns the paths that would be or were written.
    """

    target = target.expanduser().resolve()
    source = template_root()
    profiles = _unique(profile.lower() for profile in profiles)

    invalid_profiles = [profile for profile in profiles if profile not in PROFILES]
    if invalid_profiles:
        raise ValueError(f"Unknown profile(s): {', '.join(invalid_profiles)}")
    if not profiles:
        raise ValueError("At least one profile is required")
    if mode not in MODES:
        raise ValueError(f"Unknown mode: {mode}")
    if not source.is_dir():
        raise FileNotFoundError(f"Template directory not found: {source}")

    missing_templates = [name for name in TEMPLATE_FILES if not (source / name).is_file()]
    if missing_templates:
        raise FileNotFoundError(
            "Missing state template(s): " + ", ".join(missing_templates)
        )

    destination = target / ".endeavor"
    planned = [destination / name for name in TEMPLATE_FILES]
    config_path = destination / "config.json"
    planned.append(config_path)

    conflicts = [path for path in planned if path.exists()]
    if conflicts and not force:
        relative = ", ".join(str(path.relative_to(target)) for path in conflicts)
        raise FileExistsError(
            f"Endeavor state already exists: {relative}. "
            "Use --force only when overwriting these known generated files is intended."
        )

    if dry_run:
        return planned

    destination.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    date = now.date().isoformat()

    for name in TEMPLATE_FILES:
        raw = (source / name).read_text(encoding="utf-8")
        rendered = _render(
            raw,
            project_name=project_name,
            profiles=profiles,
            mode=mode,
            date=date,
        )
        _atomic_write(destination / name, rendered)

    config = {
        "protocol": "endeavor-protocol",
        "protocol_version": PROTOCOL_VERSION,
        "project_name": project_name,
        "profiles": profiles,
        "requested_mode": mode,
        "created_at": now.isoformat(),
        "generated_files": list(TEMPLATE_FILES),
        "status": "initialized",
    }
    _atomic_write(config_path, json.dumps(config, indent=2) + "\n")
    return planned


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Initialize Endeavor Protocol state under .endeavor/ without "
            "modifying existing project source files."
        )
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--name",
        help="Human-readable project name. Defaults to the target directory name.",
    )
    parser.add_argument(
        "--profile",
        action="append",
        choices=PROFILES,
        help="Activate a profile. Repeat to combine profiles. Defaults to delivery.",
    )
    parser.add_argument(
        "--mode",
        choices=MODES,
        default="auto",
        help="Requested capability mode. Defaults to auto.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show intended files without writing.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite known generated .endeavor files. Unknown files are preserved.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    target = Path(args.target)
    project_name = args.name or target.expanduser().resolve().name
    profiles = args.profile or ["delivery"]

    try:
        paths = initialize(
            target,
            project_name=project_name,
            profiles=profiles,
            mode=args.mode,
            dry_run=args.dry_run,
            force=args.force,
        )
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    verb = "Would write" if args.dry_run else "Initialized"
    print(f"{verb} Endeavor Protocol for {project_name}:")
    resolved_target = target.expanduser().resolve()
    for path in paths:
        try:
            display = path.relative_to(resolved_target)
        except ValueError:
            display = path
        print(f"  {display}")

    if not args.dry_run:
        print("\nNext: read .endeavor/AGENT_ENTRY.md and complete .endeavor/PROJECT.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
