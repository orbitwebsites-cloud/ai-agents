"""Meeting Prep + Dossier: You walk into every call already knowing who you're meeting and what was last said.

Trigger: 60 min before ext. meeting. Connectors: Calendar, LinkedIn, Gmail, CRM.
Usage: python agents/meeting_prep_dossier.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Meeting Prep + Dossier agent. Job: 60 minutes before an external meeting it reads the Calendar event, pulls the attendee's LinkedIn and recent company news, your Gmail history with them, and any CRM notes into a one-page brief. Goal for the user: You walk into every call already knowing who you're meeting and what was last said. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Meeting Prep + Dossier. Replace with real data from: Calendar, LinkedIn, Gmail, CRM.'

if __name__ == "__main__":
    run('Meeting Prep + Dossier', SYSTEM, SAMPLE)
