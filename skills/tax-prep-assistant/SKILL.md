---
name: tax-prep-assistant
description: "At quarter-end your books are sorted for the accountant with zero scramble. Use when the user asks for Tax Prep Assistant, or when this fires: Quarterly. Works with connectors for Gmail, Notion."
---

# Tax Prep Assistant

**What it does:** Quarterly it pulls receipts from Gmail and financial records from Notion, organizes everything by tax category, and outputs a clean handoff package.

**Why it matters:** At quarter-end your books are sorted for the accountant with zero scramble.

**Trigger:** Quarterly
**Connectors it uses:** Gmail, Notion

## Steps

1. Check which of these connectors are available in this session: Gmail, Notion. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
