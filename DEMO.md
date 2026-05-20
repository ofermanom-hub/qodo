# Live Demo Script (15–20 min)

A timed walkthrough for opening this repo as a Qodo-reviewed PR on stage.

## Pre-flight (do before you connect to the projector)

- [ ] Repo pushed to GitHub on your demo org.
- [ ] Qodo GitHub app installed on the repo with PR review enabled.
- [ ] `.pr_agent.toml` committed on `main`.
- [ ] Trial / paid Qodo account active.
- [ ] Browser tabs: GitHub PR page, Qodo dashboard, one IDE window.
- [ ] Notifications off. One monitor mirrored.
- [ ] Backup screen recording of the PR review (in case the network is slow).

## Setup the PR

Create a clean baseline branch without the planted issues, then a feature
branch that re-introduces them via a single commit. Push the feature branch
*before* the demo, but do NOT open the PR until you're on stage so
`/describe` runs live.

```bash
git checkout main
git checkout -b feat/duplicate-detection-and-suggest
# (apply the changes that introduce the 5 planted issues here)
git push -u origin feat/duplicate-detection-and-suggest
```

## Timed script

| Time   | Beat                                                             |
|--------|------------------------------------------------------------------|
| 0:00   | Open the PR. Narrate: "New dev on the team, just shipped two features." |
| 2:00   | `/describe` lands — walk through generated title, summary, walkthrough, labels. |
| 5:00   | `/review` lands — walk each finding: SQLi, None-check bug, perf. Click into one comment. |
| 9:00   | `/improve` — apply one committable patch live. |
| 12:00  | Custom-rule violation (print → app_logger). Open `.pr_agent.toml` and explain. |
| 14:00  | `/ask` the PR — "What happens if the weather upstream returns 500?" |
| 16:00  | Test-gen agent on `/todos/duplicates` and `/todos/suggest`. Run pytest, show green. |
| 18:00  | Close: "Five real issues — security, bug, perf, style, coverage — caught before a human looked." |

## Backup talking points (for stalls)

- "Each Qodo tool is a single LLM call — designed for ~30s round trips so it actually fits PR workflow."
- "Multi-agent: a security agent, bug agent, quality agent, and coverage agent run in parallel."
- "Same review experience on GitHub, GitLab, Bitbucket, Azure DevOps."
- "Enterprise: SOC 2, zero data retention, self-hosted / air-gapped available."
