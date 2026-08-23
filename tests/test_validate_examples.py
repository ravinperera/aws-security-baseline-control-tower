from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "validate_examples.py"
SPEC = importlib.util.spec_from_file_location("validate_examples", SCRIPT_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class ValidateExamplesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.original_root = validator.ROOT
        validator.ROOT = self.root

    def tearDown(self) -> None:
        validator.ROOT = self.original_root
        self.temporary_directory.cleanup()

    def test_markdown_accepts_valid_local_link(self) -> None:
        docs = self.root / "docs"
        docs.mkdir()
        (self.root / "README.md").write_text("# Root\n", encoding="utf-8")
        (docs / "guide.md").write_text("See [root](../README.md).\n", encoding="utf-8")
        errors: list[str] = []

        checked = validator.validate_markdown_links(errors)

        self.assertEqual(checked, 2)
        self.assertEqual(errors, [])

    def test_markdown_reports_missing_local_link(self) -> None:
        (self.root / "README.md").write_text(
            "See [missing](docs/missing.md).\n",
            encoding="utf-8",
        )
        errors: list[str] = []

        validator.validate_markdown_links(errors)

        self.assertEqual(
            errors,
            ["README.md: missing local link target: docs/missing.md"],
        )

    def test_markdown_rejects_link_that_escapes_repository(self) -> None:
        (self.root / "README.md").write_text("See [outside](../outside.md).\n", encoding="utf-8")
        errors: list[str] = []

        validator.validate_markdown_links(errors)

        self.assertEqual(
            errors,
            ["README.md: link escapes repository: ../outside.md"],
        )

    def test_markdown_ignores_links_inside_backtick_fence(self) -> None:
        (self.root / "README.md").write_text(
            "```markdown\n[placeholder](docs/not-real.md)\n```\n",
            encoding="utf-8",
        )
        errors: list[str] = []

        checked = validator.validate_markdown_links(errors)

        self.assertEqual(checked, 1)
        self.assertEqual(errors, [])

    def test_markdown_ignores_links_inside_tilde_fence_but_checks_outside(self) -> None:
        (self.root / "README.md").write_text(
            "~~~markdown\n[placeholder](docs/not-real.md)\n~~~\n[missing](docs/missing.md)\n",
            encoding="utf-8",
        )
        errors: list[str] = []

        validator.validate_markdown_links(errors)

        self.assertEqual(
            errors,
            ["README.md: missing local link target: docs/missing.md"],
        )

    def test_invalid_json_is_reported(self) -> None:
        (self.root / "valid.json").write_text(json.dumps({"ok": True}), encoding="utf-8")
        (self.root / "invalid.json").write_text('{"broken": ', encoding="utf-8")
        errors: list[str] = []

        checked = validator.validate_json(errors)

        self.assertEqual(checked, 2)
        self.assertEqual(len(errors), 1)
        self.assertTrue(errors[0].startswith("invalid.json: invalid JSON"))

    def test_duplicate_json_key_is_reported(self) -> None:
        (self.root / "duplicate.json").write_text(
            '{"enabled": true, "enabled": false}\n',
            encoding="utf-8",
        )
        errors: list[str] = []

        checked = validator.validate_json(errors)

        self.assertEqual(checked, 1)
        self.assertEqual(
            errors,
            ["duplicate.json: invalid JSON (duplicate JSON key: 'enabled')"],
        )

    def test_nested_json_with_unique_keys_is_accepted(self) -> None:
        (self.root / "valid.json").write_text(
            '{"control": {"enabled": true}, "owner": "security"}\n',
            encoding="utf-8",
        )
        errors: list[str] = []

        checked = validator.validate_json(errors)

        self.assertEqual(checked, 1)
        self.assertEqual(errors, [])

    def test_yaml_tab_indentation_is_reported(self) -> None:
        (self.root / "valid.yml").write_text("key:\n  child: value\n", encoding="utf-8")
        (self.root / "invalid.yaml").write_text("key:\n\tchild: value\n", encoding="utf-8")
        errors: list[str] = []

        checked = validator.validate_yaml_indentation(errors)

        self.assertEqual(checked, 2)
        self.assertEqual(errors, ["invalid.yaml: YAML contains tab indentation"])


if __name__ == "__main__":
    unittest.main()
