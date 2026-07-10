#!/usr/bin/env python3
"""Validate the structure of this Claude Code skill."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required: pip install pyyaml") from exc


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    return yaml.safe_load(match.group(1)) or {}


def main() -> int:
    errors: list[str] = []

    if not SKILL.exists():
        errors.append("SKILL.md is missing")
    else:
        text = SKILL.read_text(encoding="utf-8")
        try:
            frontmatter = parse_frontmatter(text)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
            frontmatter = {}

        for field in ("name", "description"):
            if not frontmatter.get(field):
                errors.append(f"frontmatter field '{field}' is required")

        if frontmatter.get("name") != "journal-article-writing":
            errors.append("frontmatter name must be 'journal-article-writing'")

        tools = frontmatter.get("allowed-tools", [])
        if isinstance(tools, str):
            tools = [part.strip() for part in tools.split(",")]
        if "AskUserQuestion" not in tools:
            errors.append("allowed-tools must include AskUserQuestion")

        line_count = len(text.splitlines())
        if line_count > 500:
            errors.append(f"SKILL.md has {line_count} lines; keep it at or below 500")

        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        for link in links:
            if "://" in link or link.startswith("#"):
                continue
            target = (ROOT / link.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(f"broken local link in SKILL.md: {link}")

    required = [
        "README.md",
        "references/research-workflow.md",
        "references/story-hypothesis.md",
        "references/article-architecture.md",
        "references/section-expansion-patterns.md",
        "references/section-craft.md",
        "references/style-toolkit.md",
        "references/human-checkpoints.md",
        "references/okf-material-system.md",
        "references/human-writing-integration.md",
        "references/verification-and-revision.md",
        "templates/editorial-brief.md",
        "templates/story-design-sop.md",
        "templates/research-dossier.md",
        "templates/article-blueprint.md",
        "templates/okf-project-index.md",
        "templates/okf-source.md",
        "templates/okf-claim.md",
        "templates/okf-material.md",
        "templates/okf-section.md",
        "templates/fact-check-ledger.csv",
        "scripts/audit_article.py",
        "scripts/init_story_project.py",
        "scripts/validate_story_project.py",
        "evals/evals.json",
        "third_party/humanizer/NOTICE.md",
        "third_party/humanizer/LICENSE",
    ]
    for item in required:
        if not (ROOT / item).exists():
            errors.append(f"required file missing: {item}")

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
