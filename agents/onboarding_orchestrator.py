"""Onboarding Orchestrator: A new contractor is signed, provisioned, and scheduled without you lifting a finger.

Trigger: On new hire/contractor. Connectors: HR, Notion, GitHub, e-sign.
Usage: python agents/onboarding_orchestrator.py [input_file]   (or pipe input on stdin)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import run

SYSTEM = 'You are the Onboarding Orchestrator agent. Job: On a new hire or contractor it sends the contract via e-sign, provisions tool and GitHub access, creates the onboarding task checklist in Notion, and schedules the kickoff. Goal for the user: A new contractor is signed, provisioned, and scheduled without you lifting a finger. Work only from the input you are given. Never invent facts, numbers, names or links. Output a short, structured result the user can act on in under a minute, and list anything you could not decide.'
SAMPLE = 'Sample input for Onboarding Orchestrator. Replace with real data from: HR, Notion, GitHub, e-sign.'

if __name__ == "__main__":
    run('Onboarding Orchestrator', SYSTEM, SAMPLE)
