"""Invoice Creator: Mark a milestone done and the client gets a professional invoice minutes later.

Trigger: On milestone billable. Connectors: Stripe, Notion.
Usage: python agents/invoice_creator.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Invoice Creator agent. Job: When a project milestone is marked billable in Notion, it creates and sends a real invoice via the Stripe API and writes the invoice ID back to Notion for tracking. Goal for the user: Mark a milestone done and the client gets a professional invoice minutes later. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Invoice Creator. Replace with real data from: Stripe, Notion.'

if __name__ == "__main__":
    run('Invoice Creator', SYSTEM, SAMPLE)
