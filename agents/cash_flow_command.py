"""Cash Flow Command: Every Friday you see next month's cash position and overdue clients get auto-nudged.

Trigger: Weekly + overdue events. Connectors: Stripe, Notion, Gmail.
Usage: python agents/cash_flow_command.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Cash Flow Command agent. Job: Weekly it reads Stripe invoices and Notion expenses to project your forward cash position, and on overdue-invoice events sends polite payment-reminder emails via Gmail. Goal for the user: Every Friday you see next month's cash position and overdue clients get auto-nudged. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Cash Flow Command. Replace with real data from: Stripe, Notion, Gmail.'

if __name__ == "__main__":
    run('Cash Flow Command', SYSTEM, SAMPLE)
