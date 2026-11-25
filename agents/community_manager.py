"""Community Manager: Your top comments get thoughtful replies within the hour, and FAQs quietly become your next script.

Trigger: Hourly comment batch. Connectors: YouTube Data API, Notion.
Usage: python agents/community_manager.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Community Manager agent. Job: Every hour it fetches new comments via the YouTube Data API, drafts replies in your voice, flags the ones needing a human, and logs recurring questions to Notion as future video ideas. Goal for the user: Your top comments get thoughtful replies within the hour, and FAQs quietly become your next script. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Community Manager. Replace with real data from: YouTube Data API, Notion.'

if __name__ == "__main__":
    run('Community Manager', SYSTEM, SAMPLE)
