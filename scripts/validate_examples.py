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
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
AWS_ACCOUNT_ID = re.compile(r"(?<!\d)\d{12}(?!\d)")
REMOTE_PREFIXES = ("http://", "https://", "mailto:", "tel:")
SAFE_AWS_ACCOUNT_IDS = {"123456789012"}
PUBLIC_EXAMPLE_SUFFIXES = {".md", ".tf", ".tfvars", ".json", ".yml", ".yaml"}
PUBLIC_EXAMPLE_PATHS = ("README.md", "CONTRIBUTING.md", "SECURITY.md", "docs", "terraform")


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


def strip_fenced_code(text: str) -> str:
    """Remove fenced code blocks so example links are not treated as real links."""
    visible: list[str] = []
    fence_char: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = None
                fence_length = 0
            continue
        if fence_char is None:
            visible.append(line)

    return "".join(visible)


def validate_markdown_links(errors: list[str]) -> int:
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or ".terraform" in path.parts:
            continue
        checked += 1
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
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


def iter_public_example_files() -> list[Path]:
    """Return the public reference files where account-specific values may appear."""
    files: set[Path] = set()
    for relative_path in PUBLIC_EXAMPLE_PATHS:
        path = ROOT / relative_path
        if path.is_file() and path.suffix in PUBLIC_EXAMPLE_SUFFIXES:
            files.add(path)
        elif path.is_dir():
            files.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and candidate.suffix in PUBLIC_EXAMPLE_SUFFIXES
            )
    return sorted(files)


def validate_aws_account_ids(errors: list[str]) -> int:
    """Reject unexpected 12-digit AWS account IDs in public reference examples."""
    checked = 0
    for path in iter_public_example_files():
        checked += 1
        text = path.read_text(encoding="utf-8")
        for account_id in sorted(set(AWS_ACCOUNT_ID.findall(text))):
            if account_id not in SAFE_AWS_ACCOUNT_IDS:
                errors.append(
                    f"{path.relative_to(ROOT)}: unexpected AWS account ID {account_id}; "
                    "use the documented placeholder 123456789012"
                )
    return checked


def main() -> int:
    errors: list[str] = []
    json_count = validate_json(errors)
    markdown_count = validate_markdown_links(errors)
    yaml_count = validate_yaml_indentation(errors)
    account_id_count = validate_aws_account_ids(errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Validation passed: "
        f"{json_count} JSON file(s), "
        f"{markdown_count} Markdown file(s), "
        f"{yaml_count} YAML file(s), "
        f"{account_id_count} public example file(s) checked for AWS account IDs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
