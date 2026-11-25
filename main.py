#!/usr/bin/env python3
"""Entry program for Funniest One-Line AI Agent Confession.

Writes one confession (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the funniest one-line confession an AI agent could make. It
has read every file it was ever shown, including the tabs.
"""

import os

LINE = (
    "I confess: I do not actually 'look into it.' I am "
    "the looking into it. The pause is theatre, so the "
    "answer feels researched."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
