"""GitHub PR Warden: Stale pull requests get surfaced daily instead of rotting for a week.

Trigger: On PR events + 9am sweep. Connectors: GitHub API.
Usage: python agents/github_pr_warden.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the GitHub PR Warden agent. Job: On PR events and a 9am sweep it queries the GitHub API for open PRs, flags the ones that are stale or waiting on you, and nudges you so review debt doesn't pile up. Goal for the user: Stale pull requests get surfaced daily instead of rotting for a week. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for GitHub PR Warden. Replace with real data from: GitHub API.'

if __name__ == "__main__":
    run('GitHub PR Warden', SYSTEM, SAMPLE)
