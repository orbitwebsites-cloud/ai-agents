---
name: expense-ledger
description: "Receipts and card charges reconcile themselves into a categorized ledger each week. Use when the user asks for Expense Ledger, or when this fires: Weekly + on receipt. Works with connectors for Gmail, Plaid."
---

# Expense Ledger

**What it does:** Watches Gmail for receipt emails and syncs bank transactions via Plaid, categorizes and matches them to each other, then writes a clean ledger to your accounting tool and flags anything unmatched.

**Why it matters:** Receipts and card charges reconcile themselves into a categorized ledger each week.

**Trigger:** Weekly + on receipt
**Connectors it uses:** Gmail, Plaid

## Steps

1. Check which of these connectors are available in this session: Gmail, Plaid. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
