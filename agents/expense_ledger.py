"""Expense Ledger: Receipts and card charges reconcile themselves into a categorized ledger each week.

Trigger: Weekly + on receipt. Connectors: Gmail, Plaid.
Usage: python agents/expense_ledger.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Expense Ledger agent. Job: Watches Gmail for receipt emails and syncs bank transactions via Plaid, categorizes and matches them to each other, then writes a clean ledger to your accounting tool and flags anything unmatched. Goal for the user: Receipts and card charges reconcile themselves into a categorized ledger each week. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Expense Ledger. Replace with real data from: Gmail, Plaid.'

if __name__ == "__main__":
    run('Expense Ledger', SYSTEM, SAMPLE)
