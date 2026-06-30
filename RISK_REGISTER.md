# Risk Register

| Risk | Probability | Impact | Prevention | Recovery plan |
| ---- | ----------- | ------ | ---------- | ------------- |
| Azure costs increase unexpectedly | Medium | High | Create expensive resources late, use small SKUs, delete after testing | Run cleanup script and verify Azure Portal resource group is empty |
| Secrets accidentally committed | Medium | High | Use `.env.example`, `.gitignore`, GitHub Secrets, and review before commit | Rotate exposed secret, remove from Git history, document incident |
| Azure ML Compute left running | Medium | Medium | Configure scale-down and stop/delete compute when idle | Stop compute in Azure ML Studio or cleanup script |
| AKS created too early | Low | High | Defer AKS until Phase 18 | Delete cluster and public IP resources |
| Quality gate blocks deployment | Medium | Medium | Choose realistic threshold and review preprocessing/model setup | Inspect metrics, compare baseline, fix model or threshold decision |
| GitHub Actions cannot authenticate to Azure | Medium | High | Document required secrets or federated credentials clearly | Recreate service principal/federated credential and rerun workflow |
| Docker Desktop not connected to WSL | Medium | Medium | Verify Docker from WSL before container phase | Enable WSL integration in Docker Desktop settings |
| DVC remote misconfigured | Medium | Medium | Keep DVC config documented and avoid hardcoded credentials | Reconfigure remote using environment variables or Azure auth |
| Application Insights logs too much data | Low | Medium | Log only required metadata, no secrets or personal information | Reduce sampling/log level and delete excess test resources |
| Drift demo does not trigger alert | Medium | Medium | Create controlled shifted data for the demo | Adjust simulated drift dataset and rerun scheduled workflow |
| OpenRouter key exposed in logs | Low | High | Read key from environment and never log request headers | Rotate key and clean logs if exposure occurs |
| Team members duplicate work | Medium | Medium | Assign owners in `TASKS.md` and update status daily | Reassign tasks and resolve merge conflicts through pull requests |
