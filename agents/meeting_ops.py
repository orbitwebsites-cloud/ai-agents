"""Meeting Ops: A client call ends at 3pm; by 3:05 the notes are filed, tasks are assigned, and the follow-up email is waiting in drafts.

Trigger: On call-end webhook. Connectors: Zoom/Otter, Notion, Linear, Gmail.
Usage: python agents/meeting_ops.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Meeting Ops agent. Job: Catches the call-end webhook and pulls the transcript via Zoom/Otter's API, writes a structured summary into the meeting's Notion page, creates action-item tasks in Linear with owners, and drafts the follow-up email in Gmail for one-tap send. Goal for the user: A client call ends at 3pm; by 3:05 the notes are filed, tasks are assigned, and the follow-up email is waiting in drafts. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Meeting Ops. Replace with real data from: Zoom/Otter, Notion, Linear, Gmail.'

if __name__ == "__main__":
    run('Meeting Ops', SYSTEM, SAMPLE)
