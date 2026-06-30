# Phase 2: Local Python Environment

## Goal

Set up a reliable local Python workspace in WSL so later phases can run scripts, tests, and automation without version or dependency problems.

## What We Are Building

We are creating the Python foundation for the project:

- A virtual environment in `.venv`
- Dependency files for runtime and development tools
- A validation script that checks Python version, project files, and imports
- A small smoke test so `pytest` can run

## Why This Phase Is Needed

Every later phase depends on Python working the same way on your machine. If Python, pip, or the virtual environment are wrong now, training, testing, Docker builds, and CI will fail later in confusing ways.

## Files Involved

| File | Location | Purpose |
| ---- | -------- | ------- |
| `requirements.txt` | project root | Core runtime packages for early phases |
| `requirements-dev.txt` | project root | Testing and lint tools |
| `pyproject.toml` | project root | Project metadata and tool settings |
| `pytest.ini` | project root | pytest configuration |
| `scripts/validate_environment.py` | `scripts/` | Checks Python version, files, and imports |
| `tests/test_validate_environment.py` | `tests/` | Small smoke tests for the validator |

## Exact Terminal

Use:

```text
Run in: WSL Ubuntu terminal inside VS Code
```

## Commands

Move into the project folder:

```bash
cd /mnt/c/Users/USER/mlops-azure-final-project
```

Check Python version:

```bash
python3 --version
```

This should show Python 3.11 or newer.

Create the virtual environment:

```bash
python3 -m venv .venv
```

This creates an isolated Python environment in the `.venv` folder.

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Your prompt should now start with `(.venv)`.

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the environment validator:

```bash
python scripts/validate_environment.py
```

Run the smoke tests:

```bash
pytest
```

Run lint check:

```bash
ruff check scripts tests
```

## Expected Result

Successful validation output should look similar to:

```text
INFO: Project root: /mnt/c/Users/USER/mlops-azure-final-project
INFO: Python version OK: 3.11.x
INFO: Virtual environment detected: /mnt/c/Users/USER/mlops-azure-final-project/.venv
INFO: Required project files found.
INFO: Import OK: dotenv
INFO: Import OK: yaml
INFO: Import OK: pytest
INFO: Import OK: pytest_cov
INFO: Import OK: ruff
INFO: Environment validation passed.
```

Successful pytest output should look similar to:

```text
2 passed in ...
```

## Screenshots to Take

- Terminal showing `python3 --version`
- Terminal showing activated virtual environment `(.venv)`
- Terminal showing successful `validate_environment.py` output
- Terminal showing successful `pytest` output

Save them under `docs/screenshots/` using names from `SCREENSHOT_CHECKLIST.md`.

## Common Errors

- **`python3: command not found`**: Install Python 3.11 in WSL with `sudo apt update && sudo apt install python3.11 python3.11-venv python3-pip`.
- **`No module named venv`**: Install the venv package: `sudo apt install python3.11-venv`.
- **`Missing Python packages`**: Activate `.venv` first, then run `pip install -r requirements-dev.txt`.
- **Slow pip on `/mnt/c`**: This is common on WSL with Windows filesystem paths. It still works; later we can optimize if needed.

## Security and Cost Warning

This phase creates no Azure resources and uses no secrets. Do not create a real `.env` file yet unless you are ready to add placeholder values locally only.

## Phase Completion Checklist

- [ ] Python 3.11+ confirmed in WSL
- [ ] `.venv` created and activated
- [ ] Dependencies installed from `requirements-dev.txt`
- [ ] `validate_environment.py` passes
- [ ] `pytest` passes
- [ ] Screenshots saved
