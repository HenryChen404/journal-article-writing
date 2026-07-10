#!/usr/bin/env python3
"""Validate an OKF-compatible reported-article workspace."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required: pip install pyyaml") from exc


ID_PATTERN = re.compile(r"\b(SRC|CLM|MAT|SEC|DEC)-\d{3,}\b")
TYPE_PREFIX = {
    "Source": "SRC",
    "Claim": "CLM",
    "Material": "MAT",
    "Article Section": "SEC",
    "Editorial Decision": "DEC",
}


def parse_doc(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        return {}, text
    data = yaml.safe_load(match.group(1)) or {}
    return data, text


def listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.project).resolve()

    errors: list[str] = []
    warnings: list[str] = []

    required = [
        "index.md", "editorial-brief.md", "story-design-sop.md",
        "research-dossier.md", "article-blueprint.md", "sources", "claims",
        "materials", "sections", "decisions", "drafts", "audits",
    ]
    for item in required:
        if not (root / item).exists():
            errors.append(f"missing required path: {item}")

    docs: dict[str, tuple[Path, dict[str, Any], str]] = {}
    ids: list[str] = []

    for path in root.rglob("*.md"):
        data, text = parse_doc(path)
        if data.get("okf_version") and str(data["okf_version"]) != "0.1":
            errors.append(f"{path.relative_to(root)}: unsupported okf_version")
        doc_id = data.get("id")
        doc_type = data.get("type")
        if doc_id:
            ids.append(str(doc_id))
            docs[str(doc_id)] = (path, data, text)
        if doc_type in TYPE_PREFIX:
            if not doc_id:
                errors.append(f"{path.relative_to(root)}: {doc_type} missing id")
            elif not str(doc_id).startswith(TYPE_PREFIX[doc_type] + "-"):
                errors.append(f"{path.relative_to(root)}: id/type prefix mismatch")

    for doc_id, count in Counter(ids).items():
        if count > 1:
            errors.append(f"duplicate id: {doc_id}")

    known = set(ids)

    for doc_id, (path, data, text) in docs.items():
        rel = path.relative_to(root)
        doc_type = data.get("type")

        for key in (
            "source_id", "source_ids", "claim_ids", "primary_claim_ids",
            "material_ids", "counterevidence_ids", "section_ids", "affects",
        ):
            for ref in listify(data.get(key)):
                if ID_PATTERN.fullmatch(ref) and ref not in known:
                    errors.append(f"{rel}: broken ID reference {key}={ref}")

        if doc_type == "Material":
            if not data.get("source_id"):
                errors.append(f"{rel}: material missing source_id")
            if not data.get("evidence_boxes"):
                warnings.append(f"{rel}: material has no evidence_boxes")
            if not data.get("evidence_functions"):
                warnings.append(f"{rel}: material has no evidence_functions")

        if doc_type == "Claim" and data.get("importance") == "major":
            if not data.get("material_ids"):
                warnings.append(f"{rel}: major claim has no material_ids")

        if doc_type == "Article Section":
            for field in ("section_job", "reader_question", "expansion_pattern"):
                if not data.get(field):
                    errors.append(f"{rel}: section missing {field}")
            if data.get("status") in {"approved", "drafting", "published"} and not data.get("human_approved"):
                warnings.append(f"{rel}: active section is not human-approved")

        if doc_type == "Editorial Decision" and data.get("status") == "approved":
            if not data.get("decided_by"):
                warnings.append(f"{rel}: approved decision missing decided_by")

        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in link or link.startswith("#") or link.startswith("mailto:"):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(f"{rel}: broken local link {link}")

    section_materials = set()
    for _, (_, data, _) in docs.items():
        if data.get("type") == "Article Section":
            section_materials.update(listify(data.get("material_ids")))
    for doc_id, (path, data, _) in docs.items():
        if data.get("type") == "Material" and data.get("status") == "active":
            if doc_id not in section_materials and not data.get("section_ids"):
                warnings.append(f"{path.relative_to(root)}: active material is orphaned")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
