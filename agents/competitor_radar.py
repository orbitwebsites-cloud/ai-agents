"""Competitor Radar: You hear about a rival's launch the moment it happens, not a week later.

Trigger: Alert-on-change. Connectors: Web, news sources.
Usage: python agents/competitor_radar.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Competitor Radar agent. Job: Continuously monitors named competitors and topics via web and news sources, and only alerts you when something actually changes — a launch, a price move, a funding round. Goal for the user: You hear about a rival's launch the moment it happens, not a week later. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Competitor Radar. Replace with real data from: Web, news sources.'

if __name__ == "__main__":
    run('Competitor Radar', SYSTEM, SAMPLE)
