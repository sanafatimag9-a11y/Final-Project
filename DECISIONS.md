# Decision Log

This file records important project choices so the team can explain why each choice was made.

| Decision | Choice | Reason | Status |
| -------- | ------ | ------ | ------ |
| Dataset | Breast Cancer Wisconsin Diagnostic | Small, built into scikit-learn, fast to train, realistic classification problem | Approved |
| Model | scikit-learn classifier, likely logistic regression or random forest | Beginner-friendly and strong for tabular data | Proposed |
| Evaluation metric | F1 score | Better than accuracy when false positives and false negatives both matter | Proposed |
| Passing threshold | F1 score >= 0.95 | Dataset is clean enough that a strong model should meet this without expensive training | Proposed |
| Data-versioning method | DVC with Azure Blob Storage remote | Meets requirement and teaches dataset versioning | Approved |
| Container registry | Azure Container Registry | Native Azure registry for ACI and AKS deployments | Approved default |
| Staging platform | Azure Container Instances | Simpler and cheaper than AKS for staging | Approved default |
| Production platform | Azure Kubernetes Service | Required production target | Approved default |
| Production approval | GitHub Environment named `production` | Represents trainer approval before production deployment | Approved default |
| Docker tagging | Model version plus Git commit SHA | Allows rollback to the exact image | Approved default |
| Drift scheduling method | Scheduled GitHub Actions workflow | Easy to demonstrate and keeps automation in the repository | Proposed |
| Alert destination | Teams webhook or email | Must be chosen before alert implementation | Needs decision |
| Monitoring | Application Insights and Azure Monitor | Required for API telemetry and alert evidence | Approved default |
| OpenRouter use case | Generate Markdown model evaluation report after successful quality gate | Meaningful use of actual model results | Approved default |
| AKS configuration | Small Linux node pool, exact SKU to be chosen later | Control cost and avoid early charges | Deferred |
| Rollback strategy | Redeploy a previous approved ACR image tag and matching Azure ML model version | Keeps previous versions available | Proposed |

## Dataset Details

The selected dataset predicts whether a breast tumor sample is malignant or benign.

- Input features: numeric measurements from cell nuclei, such as radius, texture, perimeter, area, smoothness, compactness, concavity, symmetry, and fractal dimension.
- Target value: malignant or benign.
- Recommended metric: F1 score.
- Recommended quality gate: F1 score >= 0.95.

## Notes for Demo

Because this is a healthcare-style dataset, the demo should clearly say it is a public educational dataset and not a medical diagnosis system.
