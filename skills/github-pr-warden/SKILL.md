---
name: github-pr-warden
description: "Stale pull requests get surfaced daily instead of rotting for a week. Use when the user asks for GitHub PR Warden, or when this fires: On PR events + 9am sweep. Works with connectors for GitHub API."
---

# GitHub PR Warden

**What it does:** On PR events and a 9am sweep it queries the GitHub API for open PRs, flags the ones that are stale or waiting on you, and nudges you so review debt doesn't pile up.

**Why it matters:** Stale pull requests get surfaced daily instead of rotting for a week.

**Trigger:** On PR events + 9am sweep
**Connectors it uses:** GitHub API

## Steps

1. Check which of these connectors are available in this session: GitHub API. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
