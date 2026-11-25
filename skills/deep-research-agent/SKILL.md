---
name: deep-research-agent
description: "Ask a hard question and get a sourced, multi-source report instead of a shallow answer. Use when the user asks for Deep Research Agent, or when this fires: On demand. Works with connectors for Web (multi-source)."
---

# Deep Research Agent

**What it does:** On demand it orchestrates multiple sequential web searches, cross-references the sources, and synthesizes a cited report.

**Why it matters:** Ask a hard question and get a sourced, multi-source report instead of a shallow answer.

**Trigger:** On demand
**Connectors it uses:** Web (multi-source)

## Steps

1. Check which of these connectors are available in this session: Web (multi-source). If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
