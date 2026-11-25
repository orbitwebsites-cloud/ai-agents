"""Email Copilot: You open Gmail to find every important email already has a reply drafted in your tone.

Trigger: New priority email + 8:30am. Connectors: Gmail.
Usage: python agents/email_copilot.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Email Copilot agent. Job: Reads new priority threads and your sent-mail history through the Gmail API to learn your voice, then writes draft replies straight back into your Gmail drafts folder — you just review and send. Goal for the user: You open Gmail to find every important email already has a reply drafted in your tone. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Email Copilot. Replace with real data from: Gmail.'

if __name__ == "__main__":
    run('Email Copilot', SYSTEM, SAMPLE)
