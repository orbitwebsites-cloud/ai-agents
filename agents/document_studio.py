"""Document Studio: Generate a client-ready proposal grounded in real project data in minutes.

Trigger: On demand + CRM events. Connectors: CRM, Notion, Drive.
Usage: python agents/document_studio.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Document Studio agent. Job: Pulls real project data from CRM/Notion and your past winning docs as templates to generate proposals, SOWs and agreements, then files them to Drive and sends where relevant. Goal for the user: Generate a client-ready proposal grounded in real project data in minutes. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Document Studio. Replace with real data from: CRM, Notion, Drive.'

if __name__ == "__main__":
    run('Document Studio', SYSTEM, SAMPLE)
