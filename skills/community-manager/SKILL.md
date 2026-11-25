---
name: community-manager
description: "Your top comments get thoughtful replies within the hour, and FAQs quietly become your next script. Use when the user asks for Community Manager, or when this fires: Hourly comment batch. Works with connectors for YouTube Data API, Notion."
---

# Community Manager

**What it does:** Every hour it fetches new comments via the YouTube Data API, drafts replies in your voice, flags the ones needing a human, and logs recurring questions to Notion as future video ideas.

**Why it matters:** Your top comments get thoughtful replies within the hour, and FAQs quietly become your next script.

**Trigger:** Hourly comment batch
**Connectors it uses:** YouTube Data API, Notion

## Steps

1. Check which of these connectors are available in this session: YouTube Data API, Notion. If one the task needs is missing, say which one and ask the user to connect it or paste the data instead. Never pretend you fetched something.
2. Gather the input from the connectors (or from what the user pasted).
3. Do the job described above. Work only from real data: no invented names, numbers, dates or links.
4. Show the result as a short, scannable summary the user can act on in under a minute, and list anything you couldn't decide.
5. Before anything that leaves the machine (sending an email, posting, creating an invoice, charging money, commenting publicly), show the exact draft and wait for the user's yes. Drafts are fine without asking.
