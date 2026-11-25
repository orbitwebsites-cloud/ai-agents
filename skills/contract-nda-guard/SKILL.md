---
name: contract-nda-guard
description: "A contract lands and you instantly know which clause needs a second look. Use when the user asks for Contract & NDA Guard, or when this fires: On contract received. Works with connectors for Google Drive, Gmail."
---

# Contract & NDA Guard

**What it does:** When a contract arrives via Gmail or Drive it reads the document, flags risky clauses in plain English, and routes an approve / escalate / reject recommendation.

**Why it matters:** A contract lands and you instantly know which clause needs a second look.

**Trigger:** On contract received
**Connectors it uses:** Google Drive, Gmail

## Steps

1. Check which of these connectors are available in this session: Google Drive, Gmail. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
