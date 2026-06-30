# Demo Plan

## Demo Goal

Show that a code change can safely move through testing, model training, quality approval, staging deployment, production approval, production deployment, monitoring, drift detection, alerting, rollback, and cleanup.

## Demo Story

1. Open a feature branch and make a small safe code change.
2. Open a pull request.
3. Show GitHub Actions CI running tests and coverage.
4. Merge to `main` after checks pass.
5. Show the training pipeline start.
6. Show MLflow metrics in Azure ML.
7. Show the quality gate passing or failing.
8. Show approved model registration.
9. Show Docker image tag with model version and Git SHA.
10. Show ACI staging endpoint responding.
11. Show trainer approval through GitHub `production` environment.
12. Show AKS production endpoint responding.
13. Show Application Insights logs.
14. Show Evidently drift report.
15. Show Teams or email alert.
16. Show OpenRouter model evaluation report.
17. Show rollback to previous approved image.
18. Run cleanup and show resources are deleted or stopped.

## Screenshot Evidence to Collect

Screenshots should be saved under `docs/screenshots/`.

The final evidence table must include requirement, file or Azure resource, test performed, screenshot, and status.

## Demo Safety Notes

- Do not show secret values.
- Do not display full environment files.
- Do not leave AKS or ACI running after the demo.
- Do not claim a metric or deployment succeeded unless the output proves it.
