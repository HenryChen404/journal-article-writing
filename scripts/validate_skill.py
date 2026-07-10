#!/usr/bin/env python3
"""Validate the structure of this Claude Code skill."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    data: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []

    if not SKILL.exists():
        errors.append("SKILL.md is missing")
    else:
        text = SKILL.read_text(encoding="utf-8")
        try:
            frontmatter = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(str(exc))
            frontmatter = {}

        for field in ("name", "description"):
            if not frontmatter.get(field):
                errors.append(f"frontmatter field '{field}' is required")

        if frontmatter.get("name") != "journal-article-writing":
            errors.append("frontmatter name must be 'journal-article-writing'")

        line_count = len(text.splitlines())
        if line_count > 500:
            errors.append(f"SKILL.md has {line_count} lines; keep it at or below 500")

        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        for link in links:
            if "://" in link or link.startswith("#"):
                continue
            target = (ROOT / link).resolve()
            if not target.exists():
                errors.append(f"broken local link in SKILL.md: {link}")

    required = [
        ROOT / "README.md",
        ROOT / "references" / "research-workflow.md",
        ROOT / "references" / "story-hypothesis.md",
        ROOT / "references" / "article-architecture.md",
        ROOT / "references" / "section-craft.md",
        ROOT / "references" / "verification-and-revision.md",
        ROOT / "templates" / "research-dossier.md",
        ROOT / "templates" / "article-outline.md",
        ROOT / "templates" / "fact-check-ledger.csv",
        ROOT / "scripts" / "audit_article.py",
        ROOT / "evals" / "evals.json",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"required file missing: {path.relative_to(ROOT)}")

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
