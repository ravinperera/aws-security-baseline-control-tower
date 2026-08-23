#!/usr/bin/env python3
"""Dependency-free checks for the public security-baseline examples."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REMOTE_PREFIXES = ("http://", "https://", "mailto:", "tel:")


def reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Build a JSON object while rejecting ambiguous duplicate keys."""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def validate_json(errors: list[str]) -> int:
    checked = 0
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts or ".terraform" in path.parts:
            continue
        checked += 1
        try:
            json.loads(
                path.read_text(encoding="utf-8"),
                object_pairs_hook=reject_duplicate_json_keys,
            )
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
    return checked


def validate_markdown_links(errors: list[str]) -> int:
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or ".terraform" in path.parts:
            continue
        checked += 1
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith("#") or target.startswith(REMOTE_PREFIXES):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: missing local link target: {raw_target}"
                )
    return checked


def validate_yaml_indentation(errors: list[str]) -> int:
    checked = 0
    for suffix in ("*.yml", "*.yaml"):
        for path in sorted(ROOT.rglob(suffix)):
            if ".git" in path.parts or ".terraform" in path.parts:
                continue
            checked += 1
            if "\t" in path.read_text(encoding="utf-8"):
                errors.append(f"{path.relative_to(ROOT)}: YAML contains tab indentation")
    return checked


def main() -> int:
    errors: list[str] = []
    json_count = validate_json(errors)
    markdown_count = validate_markdown_links(errors)
    yaml_count = validate_yaml_indentation(errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Validation passed: "
        f"{json_count} JSON file(s), "
        f"{markdown_count} Markdown file(s), "
        f"{yaml_count} YAML file(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
