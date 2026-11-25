"""Roast Your Own Agent entry.

Writes a single-line roast of my own AI agent to /output/entry.txt.
The line is kept as one constant so the output is exactly the entry
text: no trailing newline, no extra framing.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LINE = "My agent runs my money, my calendar and my inbox from a sandbox that's demolished every 30 minutes — he's not a butler, he's a goldfish with admin access."


def render_entry() -> str:
    """Return the entry text, validated against the competition gate."""
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    return text


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(render_entry())

if __name__ == "__main__":
    main()
