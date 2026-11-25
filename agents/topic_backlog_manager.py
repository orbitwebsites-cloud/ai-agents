"""Topic Backlog Manager: You never wonder what to film next — the top of your Notion backlog is always the best bet.

Trigger: Continuous feed + weekly rerank. Connectors: arXiv/HF, Web, Notion.
Usage: python agents/topic_backlog_manager.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Topic Backlog Manager agent. Job: Continuously pulls new papers from arXiv/HuggingFace and trend signals via web search, scores each against search demand, and maintains a ranked video-idea database in Notion that it re-orders every week. Goal for the user: You never wonder what to film next — the top of your Notion backlog is always the best bet. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Topic Backlog Manager. Replace with real data from: arXiv/HF, Web, Notion.'

if __name__ == "__main__":
    run('Topic Backlog Manager', SYSTEM, SAMPLE)
