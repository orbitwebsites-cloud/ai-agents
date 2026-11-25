---
name: email-copilot
description: "You open Gmail to find every important email already has a reply drafted in your tone. Use when the user asks for Email Copilot, or when this fires: New priority email + 8:30am. Works with connectors for Gmail."
---

# Email Copilot

**What it does:** Reads new priority threads and your sent-mail history through the Gmail API to learn your voice, then writes draft replies straight back into your Gmail drafts folder — you just review and send.

**Why it matters:** You open Gmail to find every important email already has a reply drafted in your tone.

**Trigger:** New priority email + 8:30am
**Connectors it uses:** Gmail

## Steps

1. Check which of these connectors are available in this session: Gmail. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
