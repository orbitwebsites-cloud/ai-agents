"""Contract & NDA Guard: A contract lands and you instantly know which clause needs a second look.

Trigger: On contract received. Connectors: Google Drive, Gmail.
Usage: python agents/contract_nda_guard.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Contract & NDA Guard agent. Job: When a contract arrives via Gmail or Drive it reads the document, flags risky clauses in plain English, and routes an approve / escalate / reject recommendation. Goal for the user: A contract lands and you instantly know which clause needs a second look. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Contract & NDA Guard. Replace with real data from: Google Drive, Gmail.'

if __name__ == "__main__":
    run('Contract & NDA Guard', SYSTEM, SAMPLE)
