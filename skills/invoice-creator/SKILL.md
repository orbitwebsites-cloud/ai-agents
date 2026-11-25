---
name: invoice-creator
description: "Mark a milestone done and the client gets a professional invoice minutes later. Use when the user asks for Invoice Creator, or when this fires: On milestone billable. Works with connectors for Stripe, Notion."
---

# Invoice Creator

**What it does:** When a project milestone is marked billable in Notion, it creates and sends a real invoice via the Stripe API and writes the invoice ID back to Notion for tracking.

**Why it matters:** Mark a milestone done and the client gets a professional invoice minutes later.

**Trigger:** On milestone billable
**Connectors it uses:** Stripe, Notion

## Steps

1. Check which of these connectors are available in this session: Stripe, Notion. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
