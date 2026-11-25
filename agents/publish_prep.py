"""Publish Prep: Upload a draft and the agent won't let it go public until every metadata box is checked.

Trigger: On upload (unlisted). Connectors: YouTube API, Notion, Web.
Usage: python agents/publish_prep.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = "You are the Publish Prep agent. Job: On an unlisted upload it queries the YouTube API to verify thumbnail, cards and end screen are set, generates keyword-ranked titles and a description via web search, and blocks publish if anything is missing. Goal for the user: Upload a draft and the agent won't let it go public until every metadata box is checked. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide."
SAMPLE = 'Sample input for Publish Prep. Replace with real data from: YouTube API, Notion, Web.'

if __name__ == "__main__":
    run('Publish Prep', SYSTEM, SAMPLE)
