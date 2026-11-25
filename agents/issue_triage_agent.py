"""Issue Triage Agent: Every new issue is labeled, prioritized, and assigned the moment it lands.

Trigger: On new-issue event. Connectors: GitHub API, Linear.
Usage: python agents/issue_triage_agent.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Issue Triage Agent agent. Job: When a new issue is opened it reads it via the GitHub API, applies labels and priority, and assigns it or creates a matching task in Linear. Goal for the user: Every new issue is labeled, prioritized, and assigned the moment it lands. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Issue Triage Agent. Replace with real data from: GitHub API, Linear.'

if __name__ == "__main__":
    run('Issue Triage Agent', SYSTEM, SAMPLE)
