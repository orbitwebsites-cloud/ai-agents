"""Researched Script Builder: Promote a topic in the morning; a sourced, fact-checked script is sitting in Notion by lunch.

Trigger: On item promoted to production. Connectors: arXiv, Docs, Web, Notion.
Usage: python agents/researched_script_builder.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Researched Script Builder agent. Job: When a topic is promoted, it gathers primary sources via web + arXiv, extracts cited facts, drafts a retention-structured script, and saves it with a full source list to Notion. Goal for the user: Promote a topic in the morning; a sourced, fact-checked script is sitting in Notion by lunch. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Researched Script Builder. Replace with real data from: arXiv, Docs, Web, Notion.'

if __name__ == "__main__":
    run('Researched Script Builder', SYSTEM, SAMPLE)
