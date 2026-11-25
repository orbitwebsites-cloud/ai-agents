"""Read-It-Later Digester: Everything you saved but never read comes back as summarized, searchable notes.

Trigger: On save + daily. Connectors: Pocket/Readwise, RSS, Notion.
Usage: python agents/read_it_later_digester.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Read-It-Later Digester agent. Job: Processes your Pocket/Readwise saves and podcast RSS feeds, summarizes each, extracts standout quotes, and files structured notes to Notion while reordering your queue by your current goals. Goal for the user: Everything you saved but never read comes back as summarized, searchable notes. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Read-It-Later Digester. Replace with real data from: Pocket/Readwise, RSS, Notion.'

if __name__ == "__main__":
    run('Read-It-Later Digester', SYSTEM, SAMPLE)
