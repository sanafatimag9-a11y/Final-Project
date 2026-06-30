# Phase 1: Planning and Architecture

## Goal

Confirm the project dataset, architecture, repository location, Azure resource plan, cost risks, team split, and documentation structure before writing application code.

## What We Are Building

We are building an automated MLOps pipeline on Azure. The pipeline will take data, train a model, check the model quality, register good models, package the model in an API, deploy to staging, wait for trainer approval, deploy to production, monitor the service, detect drift, send alerts, and clean up resources safely.

## Why This Phase Is Needed

Planning first prevents expensive Azure mistakes and avoids building the wrong architecture. It also gives the trainer evidence that the team understands the workflow before implementation starts.

## Files Created

- `README.md`
- `PROJECT_PLAN.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`
- `TASKS.md`
- `RISK_REGISTER.md`
- `COST_PLAN.md`
- `DEMO_PLAN.md`
- `.gitignore`
- `.env.example`
- `docs/stage-guides/phase-01-planning-and-architecture.md`
- `docs/screenshots/SCREENSHOT_CHECKLIST.md`
- `docs/architecture/architecture-overview.md`

## Exact Terminal

Use this terminal for project commands:

```text
Run in: WSL Ubuntu terminal inside VS Code
```

If VS Code is opened on Windows at:

```text
C:\Users\USER\mlops-azure-final-project
```

then the same folder in WSL is usually:

```text
/mnt/c/Users/USER/mlops-azure-final-project
```

## Commands

Confirm the project folder from WSL:

```bash
cd /mnt/c/Users/USER/mlops-azure-final-project
```

This moves your terminal into the project folder.

List the files:

```bash
ls -la
```

This shows the planning files created during Phase 1.

Check whether Git has been initialized:

```bash
git status
```

If Git is not initialized yet, that is acceptable until the GitHub repository setup phase.

## Expected Result

You should see planning files such as:

```text
README.md
PROJECT_PLAN.md
ARCHITECTURE.md
DECISIONS.md
TASKS.md
RISK_REGISTER.md
COST_PLAN.md
DEMO_PLAN.md
.gitignore
.env.example
docs/
```

## Screenshots to Take

- Terminal showing the project folder path.
- Terminal showing the file list.
- `DECISIONS.md` showing the approved dataset.
- `ARCHITECTURE.md` showing the target architecture.
- `COST_PLAN.md` showing paid-resource warnings.

## Common Errors

- `No such file or directory`: The WSL path may be typed incorrectly. Use `/mnt/c/Users/USER/mlops-azure-final-project`.
- `not a git repository`: This is acceptable until the Git setup phase.
- Missing files: Refresh VS Code Explorer or verify you are in the correct folder.

## Security and Cost Warning

No Azure resources should be created in this phase. Do not create AKS, ACI, Azure ML Compute, ACR, Application Insights, or Storage yet.

Do not put real secret values in `.env.example`. It must contain placeholder variable names only.

## Phase Completion Checklist

- [ ] Project folder confirmed.
- [ ] Breast Cancer dataset confirmed.
- [ ] Architecture approved by team.
- [ ] Cost plan reviewed.
- [ ] Planning files visible in VS Code.
- [ ] Screenshot checklist started.
- [ ] No paid Azure resources created.
