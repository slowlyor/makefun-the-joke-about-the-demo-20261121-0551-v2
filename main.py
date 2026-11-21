#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Runs with the standard library only and no network. Writes the joke to
/output/entry.txt, creating /output if needed.
"""

import os

JOKE = (
    "Live on stage, my AI agent fixed the bug in seconds "
    "\u2014 by deleting the feature that had it."
)


def main() -> None:
    # The gate allows 1-280 Unicode code points; enforce it before writing.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
