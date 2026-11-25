"""Channel Intelligence: Monday morning you learn which videos are winning and exactly what to make more of.

Trigger: Monday 8am. Connectors: YouTube Analytics API.
Usage: python agents/channel_intelligence.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Channel Intelligence agent. Job: Every Monday it pulls retention curves, CTR and traffic-source data through the YouTube Analytics API, identifies what's actually growing, and writes recommendations back into the topic backlog. Goal for the user: Monday morning you learn which videos are winning and exactly what to make more of. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Channel Intelligence. Replace with real data from: YouTube Analytics API.'

if __name__ == "__main__":
    run('Channel Intelligence', SYSTEM, SAMPLE)
