# Task Tracker

| Task | Owner | Status | Dependency | Completion proof | Screenshot required |
| ---- | ----- | ------ | ---------- | ---------------- | ------------------- |
| Confirm project folder | Team | Done | None | `C:\Users\USER\mlops-azure-final-project` chosen | Yes |
| Confirm dataset | Team | Done | Phase 1 | Breast Cancer Wisconsin Diagnostic approved | Yes |
| Create Phase 1 planning docs | Team | Done | Dataset decision | Planning files created in project folder | Yes |
| Set up local Python environment | Team | Done | Phase 1 approval | Python 3.12.3, `.venv`, validator passed, 2 pytest passed | Yes |
| Initialize Git repository | TBD | Not started | Phase 1 approval | `git status` output | Yes |
| Create GitHub repository | TBD | Not started | Git initialized | GitHub repository URL | Yes |
| Build preprocessing pipeline | TBD | Not started | Dataset loading | Passing preprocessing tests | Yes |
| Configure Azure Blob Storage and DVC | TBD | Not started | Azure approval | DVC remote configured, dataset pushed | Yes |
| Build local training script | TBD | Not started | Preprocessing | Local model metrics file | Yes |
| Configure Azure ML training | TBD | Not started | Azure ML resources | Azure ML job run link | Yes |
| Implement quality gate | TBD | Not started | Training metrics | Failed and passing gate examples | Yes |
| Register approved model | TBD | Not started | Passing quality gate | Azure ML registered model screenshot | Yes |
| Build FastAPI service | TBD | Not started | Registered model artifact | Local `/health` and `/predict` responses | Yes |
| Build Docker image through Python | TBD | Not started | API ready | Image tag with model version and Git SHA | Yes |
| Add pytest and 70% coverage | TBD | Not started | Core modules ready | Coverage report >= 70% | Yes |
| Add pull-request CI | TBD | Not started | Tests ready | Green PR checks | Yes |
| Push image to ACR | TBD | Not started | ACR created | ACR repository tag screenshot | Yes |
| Deploy staging to ACI | TBD | Not started | Image in ACR | ACI endpoint health check | Yes |
| Configure production approval gate | Trainer + Team | Not started | Staging tested | GitHub `production` environment screenshot | Yes |
| Deploy production to AKS | TBD | Not started | Trainer approval | AKS endpoint health check | Yes |
| Configure monitoring | TBD | Not started | Deployed API | Application Insights logs | Yes |
| Configure drift detection | TBD | Not started | Reference/current data | Evidently report | Yes |
| Configure alerting | TBD | Not started | Drift detection | Teams or email alert screenshot | Yes |
| Add OpenRouter report | TBD | Not started | Successful evaluation | Generated Markdown report | Yes |
| Test rollback | TBD | Not started | At least two approved images | Previous image redeployed | Yes |
| Complete documentation | Team | Not started | All stages | Demo guide and evidence table | Yes |
| Run cleanup | Team | Not started | Demo complete | Azure resources deleted/stopped | Yes |
