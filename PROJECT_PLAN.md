# Project Plan

## Project Name

Build a Real-World MLOps CI/CD Pipeline on Azure

## Goal

Build a complete machine-learning delivery pipeline that starts with data ingestion and ends with a monitored production API.

## Scope

The project includes:

- Data ingestion into Azure Blob Storage.
- Dataset versioning with DVC.
- Training with Azure ML Compute.
- Experiment tracking with MLflow.
- Automated model evaluation quality gate.
- Azure ML model registration.
- FastAPI model-serving API.
- Docker image build controlled by Python.
- GitHub Actions CI/CD.
- ACI staging deployment.
- Protected AKS production deployment.
- Application Insights and Azure Monitor.
- Evidently AI drift detection.
- Teams or email alerting.
- OpenRouter-generated model evaluation report.
- Rollback and cleanup documentation.

## Phase Plan

1. Planning and architecture.
2. Local Python environment.
3. GitHub repository setup.
4. Dataset selection and preprocessing.
5. Azure Blob Storage and data versioning.
6. Local model training.
7. Azure ML training and MLflow.
8. Model evaluation quality gate.
9. Model registration and versioning.
10. FastAPI model-serving application.
11. Docker containerization.
12. pytest tests and 70% coverage.
13. GitHub Actions CI.
14. Azure Container Registry.
15. ACI staging deployment.
16. Staging API testing.
17. Trainer approval gate.
18. AKS production deployment.
19. Application Insights and Azure Monitor.
20. Evidently drift detection.
21. Alerting.
22. OpenRouter integration.
23. Rollback testing.
24. Documentation and screenshots.
25. Final demo rehearsal.
26. Azure resource cleanup.

## Current Status

Phase 1 is in progress. The dataset choice is approved as the Breast Cancer Wisconsin Diagnostic dataset.

## Evidence Table

| Requirement | File or Azure resource | Test performed | Screenshot | Status |
| ----------- | ---------------------- | -------------- | ---------- | ------ |
| Planning documents created | `PROJECT_PLAN.md`, `ARCHITECTURE.md`, `DECISIONS.md` | File review | Required | In progress |
| Dataset selected | `DECISIONS.md` | Human approval | Required | Approved |
| Azure resources created | None | Not applicable | Not required | Not started |
| Secrets protected | `.gitignore`, `.env.example` | File review | Required later | In progress |
