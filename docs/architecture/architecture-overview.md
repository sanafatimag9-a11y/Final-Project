# Architecture Overview

## Summary

This project uses GitHub Actions and Azure services to automate the journey from dataset to production model API.

## Main Components

- GitHub: source control, pull requests, branch protection, and CI/CD workflows.
- Azure Blob Storage: stores raw and versioned dataset files.
- DVC: tracks dataset versions without committing large data files directly to Git.
- Azure ML: runs training jobs, tracks MLflow experiments, and stores approved models.
- FastAPI: serves the model through HTTP endpoints.
- Docker: packages the API and model into a portable container image.
- Azure Container Registry: stores versioned Docker images.
- Azure Container Instances: hosts the staging API.
- AKS: hosts the production API after trainer approval.
- Application Insights and Azure Monitor: collect logs, request timing, status codes, and errors.
- Evidently AI: compares reference data to current inference data for drift detection.
- OpenRouter: turns actual model evaluation results into a concise Markdown report.

## Quality Gate

The quality gate is the automatic check that prevents weak models from being deployed.

For the selected Breast Cancer dataset, the proposed starting gate is:

```text
Required F1 score: 0.95
```

If a model scores below this threshold, the pipeline should stop and send a notification.

## Versioning Strategy

- Dataset versions: DVC file hashes and Azure Blob Storage remote.
- Model versions: Azure ML Model Registry versions.
- Docker versions: model version plus Git commit SHA.
- Deployment versions: recorded image tag and model version for staging and production.

## Rollback Strategy

Rollback means returning production to a previous working version. The production deployment script will redeploy a previously approved Docker image tag from Azure Container Registry and record the matching Azure ML model version.
