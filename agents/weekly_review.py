"""Weekly Review: Friday 5pm you get a factual snapshot of the week — wins, slips, and what Monday looks like.

Trigger: Friday 5pm. Connectors: Linear, GitHub, Notion.
Usage: python agents/weekly_review.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Weekly Review agent. Job: Every Friday it queries Linear, GitHub and Notion for what shipped and what slipped, then writes a grounded review doc from the real activity. Goal for the user: Friday 5pm you get a factual snapshot of the week — wins, slips, and what Monday looks like. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Weekly Review. Replace with real data from: Linear, GitHub, Notion.'

if __name__ == "__main__":
    run('Weekly Review', SYSTEM, SAMPLE)
