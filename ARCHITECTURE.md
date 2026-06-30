# Architecture

## Plain-English Overview

The system works like a safety-focused factory for machine-learning models. A developer changes code on a feature branch, opens a pull request, and GitHub Actions checks the code. When approved code reaches `main`, Python automation ingests data, trains a model in Azure ML, tracks results with MLflow, and checks whether the model is good enough. Only approved models are registered, containerized, deployed to staging, tested, and then promoted to production after trainer approval.

## Target Architecture

```text
Developer
↓
GitHub feature branch
↓
Pull request
↓
GitHub Actions CI
↓
pytest, coverage, and code checks
↓
Merge to main
↓
Python data-ingestion script
↓
Azure Blob Storage and DVC
↓
Azure ML Compute training
↓
MLflow experiment tracking
↓
Automated model evaluation gate
↓
Failed model: stop and notify
↓
Approved model: Azure ML Model Registry
↓
FastAPI application
↓
Python-controlled Docker build
↓
Azure Container Registry
↓
Azure Container Instances staging
↓
Automated staging tests
↓
Protected production approval
↓
Azure Kubernetes Service production
↓
Application Insights and Azure Monitor
↓
Evidently drift detection and alerting
```

## Simplest Compliant Design

- Use scikit-learn because it is beginner-friendly and works well for tabular classification.
- Use the Breast Cancer Wisconsin Diagnostic dataset because it is small, built into scikit-learn, and trains cheaply.
- Use DVC with Azure Blob Storage because the requirement asks for data versioning and Azure storage.
- Use Azure ML Compute for training so the project demonstrates real cloud ML training.
- Use MLflow through Azure ML so experiment tracking is connected to the training run.
- Use a Python evaluation script that exits with failure when the quality threshold is not met.
- Use FastAPI for a small REST API with `/health`, `/predict`, and `/model-info`.
- Use Python scripts for Azure provisioning, Docker image builds, ACI staging, AKS deployment, drift checks, alerts, and cleanup.
- Use GitHub protected environment `production` to represent trainer approval before AKS deployment.

## Important Cost Control Choices

- Do not create AKS until Phase 18.
- Keep Azure ML Compute small and configure it to scale down.
- Delete ACI when not testing staging.
- Keep Application Insights log volume low.
- Use small datasets and small container images.

## Security Boundary

Secrets must not be written into source code, documentation, screenshots, or logs. Secret values must come from GitHub Secrets, environment variables, managed identity, or Azure Key Vault.
