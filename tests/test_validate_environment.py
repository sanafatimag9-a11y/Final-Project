"""Smoke tests for environment validation helpers."""

from __future__ import annotations

import pytest

from scripts.validate_environment import MIN_PYTHON, check_python_version


def test_minimum_python_version_is_3_11() -> None:
    """The project standard requires Python 3.11 or newer."""
    assert MIN_PYTHON == (3, 11)


def test_check_python_version_passes_on_current_interpreter() -> None:
    """The active interpreter should satisfy the minimum version check."""
    check_python_version()
