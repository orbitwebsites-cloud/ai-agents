"""Content Distributor: One video upload automatically becomes four scheduled posts across your channels.

Trigger: On new content published. Connectors: CMS, YouTube, schedulers.
Usage: python agents/content_distributor.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Content Distributor agent. Job: When new content publishes, it drafts platform-native posts (LinkedIn, X thread, newsletter blurb) and queues each into its scheduler at your best-performing time slot. Goal for the user: One video upload automatically becomes four scheduled posts across your channels. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Content Distributor. Replace with real data from: CMS, YouTube, schedulers.'

if __name__ == "__main__":
    run('Content Distributor', SYSTEM, SAMPLE)
