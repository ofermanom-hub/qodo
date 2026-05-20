# Tasky — Qodo Demo Repository

A tiny Flask todo-list API used as a controlled demo target for Qodo's PR review.

## Purpose

This repo intentionally contains a handful of realistic issues planted in a
single feature branch so a Qodo PR review exercises every major tool:

| # | Planted issue                                                | Qodo tool / agent           |
|---|---------------------------------------------------------------|------------------------------|
| 1 | SQL string concatenation in a DB query (injection risk)       | `/review` — security         |
| 2 | Missing None check on an external API response                | `/review` — bug              |
| 3 | New feature with no test coverage                             | `/improve` + test-gen agent  |
| 4 | O(n²) loop where a dict lookup would do                       | `/improve` — performance     |
| 5 | `print()` violating the org-rule "all logging via app.logger" | Custom rule (`.pr_agent.toml`) |

## Running locally

```bash
pip install -r requirements.txt
python -m flask --app app run
```

## Tests

```bash
pytest -q
```

## How to use this for the live demo

1. Push this repo to GitHub.
2. Install the Qodo app on the repo.
3. Create a feature branch from a clean baseline, then re-introduce the issues
   (or use the bundled `demo/feature.patch`) and open the PR live on stage.
4. Walk through `/describe`, `/review`, `/improve`, `/ask`, and the custom-rule
   violation.

See `DEMO.md` for the full timed script.
