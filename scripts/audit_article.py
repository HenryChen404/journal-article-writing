#!/usr/bin/env python3
"""Heuristic audit for journalistic article drafts.

This script does not verify truth. It surfaces structural and editorial risks
that deserve human review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PLACEHOLDER_PATTERNS = [
    r"\bTK\b",
    r"\bTODO\b",
    r"\bTBD\b",
    r"CITATION NEEDED",
    r"\[SOURCE\]",
    r"\[VERIFY\]",
    r"\?\?\?",
]

EMPTY_TRANSITIONS = [
    "another aspect",
    "on the other hand",
    "it is important to note",
    "there is another side",
    "另一方面",
    "值得注意的是",
    "另一个方面",
]

ABSOLUTE_TERMS = [
    "always",
    "never",
    "everyone",
    "no one",
    "proves",
    "guarantees",
    "必然",
    "从不",
    "所有人",
    "无人",
    "证明了",
    "保证",
]


def strip_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^[#>*+\-\d.\s]+", "", text, flags=re.M)
    return text


def paragraph_units(text: str) -> list[str]:
    blocks = re.split(r"\n\s*\n", text)
    return [
        b.strip()
        for b in blocks
        if b.strip() and not b.lstrip().startswith(("#", "|", "```"))
    ]


def sentence_units(text: str) -> list[str]:
    clean = strip_markdown(text)
    return [s.strip() for s in re.split(r"(?<=[.!?。！？])\s*", clean) if s.strip()]


def length_score(text: str) -> int:
    cjk = len(re.findall(r"[\u3400-\u9fff]", text))
    latin_words = len(re.findall(r"\b[\w'-]+\b", text))
    return cjk + latin_words


def audit(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    headings = [line for line in lines if re.match(r"^#{1,6}\s+\S", line)]
    h1 = [line for line in headings if line.startswith("# ")]

    findings: list[dict[str, Any]] = []

    def add(level: str, code: str, message: str, evidence: Any = None) -> None:
        item: dict[str, Any] = {"level": level, "code": code, "message": message}
        if evidence is not None:
            item["evidence"] = evidence
        findings.append(item)

    if not h1:
        add("warning", "missing-title", "No level-1 Markdown title was found.")
    elif len(h1) > 1:
        add("note", "multiple-titles", "Multiple level-1 headings were found.", h1)

    if len(headings) < 3:
        add(
            "warning",
            "low-structure",
            "Fewer than three headings were found; review whether a long article needs clearer navigation.",
            len(headings),
        )

    placeholders = []
    for idx, line in enumerate(lines, 1):
        if any(re.search(p, line, flags=re.I) for p in PLACEHOLDER_PATTERNS):
            placeholders.append({"line": idx, "text": line.strip()})
    if placeholders:
        add("error", "placeholders", "Unresolved reporting or editing placeholders remain.", placeholders)

    long_paragraphs = []
    for i, p in enumerate(paragraph_units(text), 1):
        score = length_score(p)
        if score > 220:
            long_paragraphs.append({"paragraph": i, "length_score": score, "preview": p[:140]})
    if long_paragraphs:
        add(
            "warning",
            "long-paragraphs",
            "Some paragraphs are unusually long; check focus and rhythm.",
            long_paragraphs,
        )

    long_sentences = []
    for i, sentence in enumerate(sentence_units(text), 1):
        score = length_score(sentence)
        if score > 60:
            long_sentences.append({"sentence": i, "length_score": score, "preview": sentence[:160]})
    if long_sentences:
        add(
            "note",
            "long-sentences",
            "Some sentences are unusually long; verify syntax and emphasis.",
            long_sentences[:20],
        )

    transitions = []
    lowered = text.lower()
    for phrase in EMPTY_TRANSITIONS:
        count = lowered.count(phrase.lower())
        if count:
            transitions.append({"phrase": phrase, "count": count})
    if transitions:
        add(
            "note",
            "generic-transitions",
            "Generic transitions appear; replace them with concrete movement when possible.",
            transitions,
        )

    absolutes = []
    for idx, line in enumerate(lines, 1):
        found = [
            term
            for term in ABSOLUTE_TERMS
            if re.search(rf"\b{re.escape(term)}\b", line, re.I) or term in line
        ]
        if found:
            absolutes.append({"line": idx, "terms": found, "text": line.strip()})
    if absolutes:
        add(
            "note",
            "absolute-claims",
            "Absolute language deserves evidentiary review.",
            absolutes[:30],
        )

    numeric_lines = []
    source_markers = re.compile(
        r"https?://|www\.|\[[^\]]+\]\([^)]+\)|\[\^\d+\]|source|according to|来源|据"
    )
    for idx, line in enumerate(lines, 1):
        if re.search(r"\d", line) and not source_markers.search(line):
            nearby = "\n".join(lines[max(0, idx - 2) : min(len(lines), idx + 1)])
            if not source_markers.search(nearby):
                numeric_lines.append({"line": idx, "text": line.strip()})
    if numeric_lines:
        add(
            "note",
            "numbers-without-nearby-source",
            "Numbers without a nearby visible source marker were found. Verify them in the fact-check ledger.",
            numeric_lines[:40],
        )

    quote_chars = len(re.findall(r'["“”]', text))
    if quote_chars > 0 and quote_chars % 2 != 0:
        add("warning", "unbalanced-quotes", "Quotation marks may be unbalanced.", quote_chars)

    summary = {
        "file": str(path),
        "character_count": len(text),
        "heading_count": len(headings),
        "paragraph_count": len(paragraph_units(text)),
        "sentence_count": len(sentence_units(text)),
        "finding_counts": {
            level: sum(1 for f in findings if f["level"] == level)
            for level in ("error", "warning", "note")
        },
    }
    return {"summary": summary, "findings": findings}


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic audit for a journalistic article in Markdown.")
    parser.add_argument("article", type=Path, help="Path to the Markdown draft")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if not args.article.exists():
        print(f"error: file not found: {args.article}", file=sys.stderr)
        return 2

    try:
        result = audit(args.article)
    except UnicodeDecodeError:
        print("error: article must be UTF-8 text", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        summary = result["summary"]
        print(f"Audit: {summary['file']}")
        print(
            f"Headings: {summary['heading_count']} | "
            f"Paragraphs: {summary['paragraph_count']} | "
            f"Sentences: {summary['sentence_count']}"
        )
        counts = summary["finding_counts"]
        print(
            f"Findings: {counts['error']} error, "
            f"{counts['warning']} warning, {counts['note']} note"
        )
        for item in result["findings"]:
            print(f"\n[{item['level'].upper()}] {item['code']}: {item['message']}")
            evidence = item.get("evidence")
            if evidence:
                print(json.dumps(evidence, ensure_ascii=False, indent=2))

    return 1 if result["summary"]["finding_counts"]["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
