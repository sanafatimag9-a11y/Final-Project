# Cost Plan

## Rule

Do not create paid Azure resources until the phase that needs them, and ask for approval before creating expensive resources.

## Expected Azure Resources

| Resource | Purpose | May create charges | Smallest practical choice | Stop or delete plan |
| -------- | ------- | ------------------ | ------------------------- | ------------------- |
| Resource group | Groups project resources | No direct charge | One dedicated resource group | Delete the resource group after demo |
| Storage account | Stores datasets and DVC remote files | Yes | Standard LRS | Delete blobs or storage account |
| Blob container | Holds raw/versioned data | Storage charge through account | One private container | Delete container |
| Azure ML workspace | Manages training, registry, tracking | Usually low direct cost, related services may charge | One workspace | Delete workspace/resource group |
| Azure ML Compute | Runs training jobs | Yes while running | Small CPU VM, min nodes 0 | Set min nodes to 0 and delete after demo |
| Azure Container Registry | Stores Docker images | Yes | Basic SKU | Delete registry after demo |
| Azure Container Instances | Staging API | Yes while running | Small CPU/memory container | Delete container group after testing |
| AKS | Production Kubernetes cluster | Yes, can be expensive | Small node pool, create late | Delete cluster immediately after demo |
| Log Analytics | Stores monitoring logs | Yes by ingestion/retention | Lowest practical retention | Delete workspace or reduce retention |
| Application Insights | API telemetry | Yes through log ingestion | Basic setup with careful logging | Delete with resource group |
| Public IP/load balancer | Exposes AKS service | Yes possible | Only create during production phase | Delete with AKS/resource group |

## Cost Controls

- Create AKS only in Phase 18.
- Use CPU training, not GPU.
- Use small datasets.
- Use Azure ML Compute with `min_instances=0`.
- Delete ACI after staging tests when not needed.
- Keep logs small and do not log request bodies unless needed for drift samples.
- Use a cleanup script and Azure Portal verification after the final demo.

## Approval Required Before Creation

Approval is required before creating:

- Azure ML Compute.
- Azure Container Registry.
- Azure Container Instances.
- AKS.
- Application Insights and Log Analytics.
- Any public IP or load balancer.
