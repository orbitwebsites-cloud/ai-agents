---
name: meeting-ops
description: "A client call ends at 3pm; by 3:05 the notes are filed, tasks are assigned, and the follow-up email is waiting in drafts. Use when the user asks for Meeting Ops, or when this fires: On call-end webhook. Works with connectors for Zoom/Otter, Notion, Linear, Gmail."
---

# Meeting Ops

**What it does:** Catches the call-end webhook and pulls the transcript via Zoom/Otter's API, writes a structured summary into the meeting's Notion page, creates action-item tasks in Linear with owners, and drafts the follow-up email in Gmail for one-tap send.

**Why it matters:** A client call ends at 3pm; by 3:05 the notes are filed, tasks are assigned, and the follow-up email is waiting in drafts.

**Trigger:** On call-end webhook
**Connectors it uses:** Zoom/Otter, Notion, Linear, Gmail

## Steps

1. Check which of these connectors are available in this session: Zoom/Otter, Notion, Linear, Gmail. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
