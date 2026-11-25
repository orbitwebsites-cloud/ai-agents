"""Deep Research Agent: Ask a hard question and get a sourced, multi-source report instead of a shallow answer.

Trigger: On demand. Connectors: Web (multi-source).
Usage: python agents/deep_research_agent.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Deep Research Agent agent. Job: On demand it orchestrates multiple sequential web searches, cross-references the sources, and synthesizes a cited report. Goal for the user: Ask a hard question and get a sourced, multi-source report instead of a shallow answer. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Deep Research Agent. Replace with real data from: Web (multi-source).'

if __name__ == "__main__":
    run('Deep Research Agent', SYSTEM, SAMPLE)
