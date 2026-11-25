"""Renewal Sentinel: You're warned 90 days before insurance renews, so coverage never lapses.

Trigger: Ahead of each renewal. Connectors: Calendar, records.
Usage: python agents/renewal_sentinel.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Renewal Sentinel agent. Job: Tracks insurance, business-registration and license renewal dates and alerts you well ahead of each lapse. Goal for the user: You're warned 90 days before insurance renews, so coverage never lapses. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Renewal Sentinel. Replace with real data from: Calendar, records.'

if __name__ == "__main__":
    run('Renewal Sentinel', SYSTEM, SAMPLE)
