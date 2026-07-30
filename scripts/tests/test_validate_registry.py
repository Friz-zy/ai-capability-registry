"""Regression tests for registry validation."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import ModuleType
from typing import Any


SCRIPTS_DIRECTORY = Path(__file__).resolve().parents[1]
VALID_COMMIT = "a" * 40


def load_validator_module() -> ModuleType:
    """Load the executable validator as an importable module.

    Returns:
        The loaded validator module.

    Raises:
        RuntimeError: If Python cannot load the validator module.
    """
    sys.path.insert(0, str(SCRIPTS_DIRECTORY))
    module_specification = importlib.util.spec_from_file_location(
        "validate_registry",
        SCRIPTS_DIRECTORY / "validate-registry.py",
    )
    if module_specification is None or module_specification.loader is None:
        raise RuntimeError("Unable to load validate-registry.py")
    validator_module = importlib.util.module_from_spec(module_specification)
    module_specification.loader.exec_module(validator_module)
    return validator_module


VALIDATOR_MODULE = load_validator_module()


def git_skill(version: Any) -> dict[str, Any]:
    """Build one otherwise-valid Git skill entry.

    Args:
        version: Version metadata under test.

    Returns:
        A complete skill entry for validator tests.
    """
    return {
        "id": "example-source",
        "name": "Example Source",
        "source": {
            "type": "git",
            "repo": "https://github.com/example/source",
        },
        "category": ["candidate"],
        "trust": {"level": "candidate"},
        "compatibility": ["codex-cli"],
        "version": version,
        "enabled": False,
    }


def validation_errors(skill: dict[str, Any]) -> list[str]:
    """Validate one skill and return its errors.

    Args:
        skill: Skill entry to validate.

    Returns:
        Validation errors produced for the entry.
    """
    errors: list[str] = []
    VALIDATOR_MODULE.validate_skills(
        [skill],
        {"candidate"},
        {"codex-cli"},
        errors,
    )
    return errors


class GitSkillPinValidationTest(unittest.TestCase):
    """Verify Git skill sources use immutable full commit pins."""

    def test_accepts_full_commit_pin(self) -> None:
        """Accept a pinned, lowercase, full-length commit hash."""
        errors = validation_errors(
            git_skill({"commit": VALID_COMMIT, "pinned": True})
        )

        self.assertEqual(errors, [])

    def test_rejects_missing_commit(self) -> None:
        """Reject pinned metadata that omits its commit."""
        errors = validation_errors(git_skill({"pinned": True}))

        self.assertIn(
            "skill example-source: version.commit must be a full 40-character lowercase commit hash",
            errors,
        )

    def test_rejects_moving_ref(self) -> None:
        """Reject a branch name in place of an immutable commit."""
        errors = validation_errors(
            git_skill({"commit": "main", "pinned": True})
        )

        self.assertIn(
            "skill example-source: version.commit must be a full 40-character lowercase commit hash",
            errors,
        )

    def test_rejects_non_mapping_version(self) -> None:
        """Reject malformed version metadata without crashing."""
        errors = validation_errors(git_skill("main"))

        self.assertIn(
            "skill example-source: git sources must set version.pinned: true",
            errors,
        )
        self.assertIn(
            "skill example-source: version.commit must be a full 40-character lowercase commit hash",
            errors,
        )

    def test_rejects_unpinned_git_source(self) -> None:
        """Reject a full commit when the source is not marked pinned."""
        errors = validation_errors(
            git_skill({"commit": VALID_COMMIT, "pinned": False})
        )

        self.assertIn(
            "skill example-source: git sources must set version.pinned: true",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
