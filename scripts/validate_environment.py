"""Validate the local Python environment for the MLOps project."""

from __future__ import annotations

import importlib
import logging
import platform
import sys
from pathlib import Path

MIN_PYTHON = (3, 11)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "requirements.txt",
    "requirements-dev.txt",
    "pyproject.toml",
    "pytest.ini",
    ".env.example",
    ".gitignore",
]
REQUIRED_PACKAGES = [
    "dotenv",
    "yaml",
    "pytest",
    "pytest_cov",
    "ruff",
]

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def check_python_version() -> None:
    """Ensure the interpreter meets the minimum Python version."""
    current = sys.version_info[:2]
    if current < MIN_PYTHON:
        required = ".".join(str(part) for part in MIN_PYTHON)
        actual = ".".join(str(part) for part in current)
        raise RuntimeError(
            f"Python {required}+ is required, but this environment is Python {actual}."
        )
    logger.info("Python version OK: %s", platform.python_version())


def check_virtual_environment() -> None:
    """Warn when the active interpreter is not inside a virtual environment."""
    if sys.prefix == sys.base_prefix:
        logger.warning(
            "No virtual environment detected. Create and activate .venv before installing packages."
        )
        return
    logger.info("Virtual environment detected: %s", sys.prefix)


def check_project_files() -> None:
    """Ensure required project files exist."""
    missing = [name for name in REQUIRED_FILES if not (PROJECT_ROOT / name).exists()]
    if missing:
        raise FileNotFoundError(f"Missing required project files: {', '.join(missing)}")
    logger.info("Required project files found.")


def check_imports() -> None:
    """Ensure required packages can be imported."""
    failed: list[str] = []
    for package_name in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package_name)
            logger.info("Import OK: %s", package_name)
        except ImportError:
            failed.append(package_name)

    if failed:
        joined = ", ".join(failed)
        raise ImportError(
            "Missing Python packages: "
            f"{joined}. Install dependencies with: pip install -r requirements-dev.txt"
        )


def main() -> int:
    """Run all environment checks."""
    logger.info("Project root: %s", PROJECT_ROOT)
    check_python_version()
    check_virtual_environment()
    check_project_files()
    check_imports()
    logger.info("Environment validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        logger.error("%s", exc)
        raise SystemExit(1) from exc
