"""Shared runner for every agent in this repo.

Each agent supplies a system prompt and a function that gathers its input.
With ANTHROPIC_API_KEY set, the agent calls Claude; without it, it runs in
dry-run mode and prints the exact prompt it would send.
"""
import json
import os
import sys
import urllib.request

MODEL = os.environ.get("AGENT_MODEL", "claude-sonnet-5-5")


def ask_claude(system: str, user: str, max_tokens: int = 1500) -> str:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return f"[dry run: no ANTHROPIC_API_KEY]\n--- system ---\n{system}\n--- input ---\n{user[:2000]}"
    body = json.dumps({
        "model": MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    return "".join(b.get("text", "") for b in data["content"])


def read_input(default: str = "") -> str:
    """Input comes from a file path argument, piped stdin, or a sample."""
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], encoding="utf-8") as f:
            return f.read()
    if not sys.stdin.isatty():
        data = sys.stdin.read()
        if data.strip():
            return data
    return default


def run(name: str, system: str, sample: str, gather=None):
    text = gather() if gather else read_input(sample)
    print(f"== {name} ==")
    print(ask_claude(system, text))
