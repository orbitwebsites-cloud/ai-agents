---
name: issue-triage-agent
description: "Every new issue is labeled, prioritized, and assigned the moment it lands. Use when the user asks for Issue Triage Agent, or when this fires: On new-issue event. Works with connectors for GitHub API, Linear."
---

# Issue Triage Agent

**What it does:** When a new issue is opened it reads it via the GitHub API, applies labels and priority, and assigns it or creates a matching task in Linear.

**Why it matters:** Every new issue is labeled, prioritized, and assigned the moment it lands.

**Trigger:** On new-issue event
**Connectors it uses:** GitHub API, Linear

## Steps

1. Check which of these connectors are available in this session: GitHub API, Linear. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
