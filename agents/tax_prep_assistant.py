"""Tax Prep Assistant: At quarter-end your books are sorted for the accountant with zero scramble.

Trigger: Quarterly. Connectors: Gmail, Notion.
Usage: python agents/tax_prep_assistant.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Tax Prep Assistant agent. Job: Quarterly it pulls receipts from Gmail and financial records from Notion, organizes everything by tax category, and outputs a clean handoff package. Goal for the user: At quarter-end your books are sorted for the accountant with zero scramble. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Tax Prep Assistant. Replace with real data from: Gmail, Notion.'

if __name__ == "__main__":
    run('Tax Prep Assistant', SYSTEM, SAMPLE)
