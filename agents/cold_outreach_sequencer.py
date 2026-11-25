"""Cold Outreach Sequencer: Add a lead and a personalized outreach sequence runs itself until they respond.

Trigger: On new lead in CRM. Connectors: LinkedIn, Clearbit, CRM.
Usage: python agents/cold_outreach_sequencer.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Cold Outreach Sequencer agent. Job: On a new CRM lead it enriches from LinkedIn/Clearbit, writes a personalized email grounded in their recent activity, sends via the CRM, and runs a 3-step follow-up that stops the instant they reply. Goal for the user: Add a lead and a personalized outreach sequence runs itself until they respond. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Cold Outreach Sequencer. Replace with real data from: LinkedIn, Clearbit, CRM.'

if __name__ == "__main__":
    run('Cold Outreach Sequencer', SYSTEM, SAMPLE)
