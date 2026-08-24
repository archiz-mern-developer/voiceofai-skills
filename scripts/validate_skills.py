#!/usr/bin/env python3
"""Validate that all skill directories contain valid SKILL.md files with proper YAML frontmatter."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent


def validate_skill_file(skill_md_path: Path) -> list[str]:
    errors = []
    content = skill_md_path.read_text(encoding="utf-8")

    if not content.startswith("---"):
        errors.append(f"{skill_md_path.relative_to(ROOT_DIR)}: Missing starting YAML frontmatter '---'")
        return errors

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{skill_md_path.relative_to(ROOT_DIR)}: Invalid YAML frontmatter structure")
        return errors

    frontmatter = parts[1]
    if "name:" not in frontmatter:
        errors.append(f"{skill_md_path.relative_to(ROOT_DIR)}: Frontmatter missing 'name' field")
    if "description:" not in frontmatter:
        errors.append(f"{skill_md_path.relative_to(ROOT_DIR)}: Frontmatter missing 'description' field")

    return errors


def main() -> int:
    print(f"Validating VoiceOfAI Skills in {ROOT_DIR}...")
    skill_dirs = [d for d in ROOT_DIR.iterdir() if d.is_dir() and not d.name.startswith(".") and d.name not in ("references", "scripts")]

    all_errors = []
    validated_count = 0

    for skill_dir in sorted(skill_dirs):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            all_errors.append(f"Directory '{skill_dir.name}' missing SKILL.md")
            continue

        errors = validate_skill_file(skill_md)
        if errors:
            all_errors.extend(errors)
        else:
            validated_count += 1
            print(f"  [OK] {skill_dir.name}")

    if all_errors:
        print("\n[ERROR] Validation errors found:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"\n[SUCCESS] All {validated_count} skills validated successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
