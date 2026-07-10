#!/usr/bin/env python3
"""Scaffold an OKF-compatible reported-article workspace."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[-\s]+", "-", value).strip("-")
    return value or "story-project"


def replace_title(text: str, title: str) -> str:
    return text.replace('title: ""', f'title: "{title.replace(chr(34), chr(39))}"', 1)


def copy_template(template: str, target: Path, title: str) -> None:
    source = TEMPLATES / template
    if not source.exists():
        raise FileNotFoundError(f"Missing template: {source}")
    text = replace_title(source.read_text(encoding="utf-8"), title)
    target.write_text(text, encoding="utf-8")


def write_index(directory: Path, heading: str, item_type: str) -> None:
    (directory / "index.md").write_text(
        f"---\nokf_version: \"0.1\"\ntype: {item_type} Index\nstatus: active\n---\n\n"
        f"# {heading}\n\nNo records yet.\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Working title")
    parser.add_argument("--output", default=".", help="Parent output directory")
    parser.add_argument("--slug", default=None, help="Override project slug")
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    project = Path(args.output).resolve() / slug
    if project.exists() and any(project.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty directory: {project}")
    project.mkdir(parents=True, exist_ok=True)

    copy_template("okf-project-index.md", project / "index.md", args.title)
    copy_template("editorial-brief.md", project / "editorial-brief.md", args.title)
    copy_template("story-design-sop.md", project / "story-design-sop.md", args.title)
    copy_template("research-dossier.md", project / "research-dossier.md", args.title)
    copy_template("article-blueprint.md", project / "article-blueprint.md", args.title)

    index_specs = {
        "sources": ("Sources", "Source"),
        "claims": ("Claims", "Claim"),
        "materials": ("Materials", "Material"),
        "sections": ("Sections", "Article Section"),
        "decisions": ("Editorial decisions", "Editorial Decision"),
    }
    for name, (heading, item_type) in index_specs.items():
        directory = project / name
        directory.mkdir()
        write_index(directory, heading, item_type)

    (project / "drafts").mkdir()
    (project / "drafts" / "draft.md").write_text(
        f"# {args.title}\n\n<!-- Draft from approved SEC / CLM / MAT records. -->\n",
        encoding="utf-8",
    )

    (project / "audits").mkdir()
    ledger = TEMPLATES / "fact-check-ledger.csv"
    shutil.copyfile(ledger, project / "audits" / "fact-check-ledger.csv")
    (project / "audits" / "revision-report.md").write_text(
        "# Revision report\n\n## Substance\n\n## Structure\n\n## Prose and voice\n\n## Unresolved items\n",
        encoding="utf-8",
    )

    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
