# Build a Real-World MLOps CI/CD Pipeline on Azure

This repository is an end-to-end beginner-friendly MLOps project using Python, Azure, GitHub Actions, Docker, FastAPI, MLflow, Evidently AI, and OpenRouter.

## Current Phase

Phase 2 complete. Next: Phase 3 — GitHub repository setup.

No Azure resources have been created yet. Application code for training, API, and deployment has not been written yet.

## Local Setup (Phase 2)

Use WSL Ubuntu inside VS Code:

```bash
cd /mnt/c/Users/USER/mlops-azure-final-project
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
python scripts/validate_environment.py
pytest
```

See `docs/stage-guides/phase-02-local-python-environment.md` for full instructions.

## Project Summary

The project will train a machine-learning classification model and deploy it safely through a CI/CD pipeline. Pull requests will run automated checks before code can merge. After approved changes reach `main`, the pipeline will train a model, evaluate it, stop if quality is too low, register approved models, build a Docker image, deploy to staging, wait for production approval, and then deploy the exact same image to AKS. Monitoring and drift detection will show whether the deployed API is healthy and whether future input data changes too much.

## Approved Phase 1 Decisions

- Dataset: Breast Cancer Wisconsin Diagnostic dataset.
- Model framework: scikit-learn.
- API framework: FastAPI.
- Test framework: pytest.
- Minimum Python test coverage: 70%.
- Experiment tracking: MLflow through Azure ML.
- Data storage: Azure Blob Storage.
- Data versioning: DVC with Azure Blob Storage as the remote.
- Staging deployment: Azure Container Instances.
- Production deployment: Azure Kubernetes Service.
- Production approval gate: GitHub protected environment named `production`.
- Monitoring: Application Insights and Azure Monitor.
- Drift detection: Evidently AI.
- OpenRouter use case: generate a model evaluation report from actual evaluation results.

## Beginner Notes

This project will be built in phases. At the end of each phase, stop and verify the commands, files, screenshots, and errors before continuing.

The preferred terminal for project commands is:

```text
WSL Ubuntu terminal inside VS Code
```

The current Windows project path is:

```text
C:\Users\USER\mlops-azure-final-project
```

In WSL, that path is usually:

```text
/mnt/c/Users/USER/mlops-azure-final-project
```

## Screenshot Evidence

Screenshots should be saved under:

```text
docs/screenshots/
```

See `docs/screenshots/SCREENSHOT_CHECKLIST.md` for the running screenshot list.

## Safety

Never commit real secrets. Use `.env.example` for placeholder names only, and use GitHub Secrets, environment variables, managed identity, or Azure Key Vault for real values.
