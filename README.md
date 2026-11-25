# 24 Real AI Agents (open source)

Every agent from my *100 Agents · 100 Days* build, in one repo. I've made videos on these agents; the table shows which ones have a video so far.

## Run one
```
# standard library only, nothing to install
set ANTHROPIC_API_KEY=...   # optional; without it each agent runs in dry-run mode
python agents/meeting_ops.py notes.txt
```

Each agent reads its input from a file argument or stdin, sends it to Claude with its own instructions, and prints the result. Wire your connectors (Gmail, Notion, Stripe...) in front of the input.

## Agents

| # | Video made | Agent | What it does | File |
|---|---|---|---|---|
| 1 | ✅ | ~~Meeting Ops~~ | A client call ends at 3pm; by 3:05 the notes are filed, tasks are assigned, and the follow-up email is waiting in drafts. | [agents/meeting_ops.py](agents/meeting_ops.py) |
| 2 | ✅ | ~~Email Copilot~~ | You open Gmail to find every important email already has a reply drafted in your tone. | [agents/email_copilot.py](agents/email_copilot.py) |
| 3 | ✅ | ~~Community Manager~~ | Your top comments get thoughtful replies within the hour, and FAQs quietly become your next script. | [agents/community_manager.py](agents/community_manager.py) |
| 4 | ✅ | ~~Topic Backlog Manager~~ | You never wonder what to film next — the top of your Notion backlog is always the best bet. | [agents/topic_backlog_manager.py](agents/topic_backlog_manager.py) |
| 5 | ✅ | ~~Researched Script Builder~~ | Promote a topic in the morning; a sourced, fact-checked script is sitting in Notion by lunch. | [agents/researched_script_builder.py](agents/researched_script_builder.py) |
| 6 | ✅ | ~~Publish Prep~~ | Upload a draft and the agent won't let it go public until every metadata box is checked. | [agents/publish_prep.py](agents/publish_prep.py) |
| 7 | ✅ | ~~Content Distributor~~ | One video upload automatically becomes four scheduled posts across your channels. | [agents/content_distributor.py](agents/content_distributor.py) |
| 8 | ✅ | ~~Channel Intelligence~~ | Monday morning you learn which videos are winning and exactly what to make more of. | [agents/channel_intelligence.py](agents/channel_intelligence.py) |
| 9 | ✅ | ~~Invoice Creator~~ | Mark a milestone done and the client gets a professional invoice minutes later. | [agents/invoice_creator.py](agents/invoice_creator.py) |
| 10 | ✅ | ~~Cash Flow Command~~ | Every Friday you see next month's cash position and overdue clients get auto-nudged. | [agents/cash_flow_command.py](agents/cash_flow_command.py) |
| 11 | ✅ | ~~Expense Ledger~~ | Receipts and card charges reconcile themselves into a categorized ledger each week. | [agents/expense_ledger.py](agents/expense_ledger.py) |
| 12 | ✅ | ~~Tax Prep Assistant~~ | At quarter-end your books are sorted for the accountant with zero scramble. | [agents/tax_prep_assistant.py](agents/tax_prep_assistant.py) |
| 13 | ✅ | ~~GitHub PR Warden~~ | Stale pull requests get surfaced daily instead of rotting for a week. | [agents/github_pr_warden.py](agents/github_pr_warden.py) |
| 14 | ✅ | ~~Issue Triage Agent~~ | Every new issue is labeled, prioritized, and assigned the moment it lands. | [agents/issue_triage_agent.py](agents/issue_triage_agent.py) |
| 15 | ✅ | ~~Weekly Review~~ | Friday 5pm you get a factual snapshot of the week — wins, slips, and what Monday looks like. | [agents/weekly_review.py](agents/weekly_review.py) |
| 16 | ✅ | ~~Cold Outreach Sequencer~~ | Add a lead and a personalized outreach sequence runs itself until they respond. | [agents/cold_outreach_sequencer.py](agents/cold_outreach_sequencer.py) |
| 17 | ✅ | ~~Meeting Prep + Dossier~~ | You walk into every call already knowing who you're meeting and what was last said. | [agents/meeting_prep_dossier.py](agents/meeting_prep_dossier.py) |
| 18 | ⬜ | Competitor Radar | You hear about a rival's launch the moment it happens, not a week later. | [agents/competitor_radar.py](agents/competitor_radar.py) |
| 19 | ⬜ | Contract & NDA Guard | A contract lands and you instantly know which clause needs a second look. | [agents/contract_nda_guard.py](agents/contract_nda_guard.py) |
| 20 | ⬜ | Renewal Sentinel | You're warned 90 days before insurance renews, so coverage never lapses. | [agents/renewal_sentinel.py](agents/renewal_sentinel.py) |
| 21 | ⬜ | Deep Research Agent | Ask a hard question and get a sourced, multi-source report instead of a shallow answer. | [agents/deep_research_agent.py](agents/deep_research_agent.py) |
| 22 | ⬜ | Read-It-Later Digester | Everything you saved but never read comes back as summarized, searchable notes. | [agents/read_it_later_digester.py](agents/read_it_later_digester.py) |
| 23 | ⬜ | Document Studio | Generate a client-ready proposal grounded in real project data in minutes. | [agents/document_studio.py](agents/document_studio.py) |
| 24 | ⬜ | Onboarding Orchestrator | A new contractor is signed, provisioned, and scheduled without you lifting a finger. | [agents/onboarding_orchestrator.py](agents/onboarding_orchestrator.py) |

## License
MIT
