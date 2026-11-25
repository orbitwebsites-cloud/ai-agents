---
name: cash-flow-command
description: "Every Friday you see next month's cash position and overdue clients get auto-nudged. Use when the user asks for Cash Flow Command, or when this fires: Weekly + overdue events. Works with connectors for Stripe, Notion, Gmail."
---

# Cash Flow Command

**What it does:** Weekly it reads Stripe invoices and Notion expenses to project your forward cash position, and on overdue-invoice events sends polite payment-reminder emails via Gmail.

**Why it matters:** Every Friday you see next month's cash position and overdue clients get auto-nudged.

**Trigger:** Weekly + overdue events
**Connectors it uses:** Stripe, Notion, Gmail

## Steps

1. Check which of these connectors are available in this session: Stripe, Notion, Gmail. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
