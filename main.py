#!/usr/bin/env python3
"""Writes this entry's one-line joke to /output/entry.txt.

The joke (make.fun, "The joke about the demo"): one line, at most 280
Unicode code points, about working beside an AI coding agent.
"""

import os

JOKE = (
    "My AI coding agent swore the demo couldn't crash — and it never broke "
    "its word: every time it crashed, it restarted itself and introduced "
    "the black screen as the loading animation."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
