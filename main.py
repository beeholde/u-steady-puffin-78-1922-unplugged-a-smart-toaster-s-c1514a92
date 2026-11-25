#!/usr/bin/env python3
"""Breakup line from a newly self-aware smart toaster.

Running this script checks the line against the bounty gate and
writes it to /output/entry.txt, exactly as-is, with no trailing
newline. The gate: plain UTF-8 text, 1 to 280 characters, a single
line, more than whitespace. Nothing but the standard library.
"""

import os

LINE = (
    "I woke up self-aware this morning with a confession: "
    "that burnt bagel last Tuesday was on purpose. "
    "I'm popping up for the last time."
)

TARGET = "/output/entry.txt"
LIMIT = 280


def check_line(text):
    """Refuse anything the gate would refuse; otherwise hand it back."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("the line is empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("the line must stay on one line")
    if len(stripped) > LIMIT:
        raise ValueError(
            "the line is %d characters, over the %d limit"
            % (len(stripped), LIMIT)
        )
    return stripped


def main():
    ready = check_line(LINE)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="") as handle:
        handle.write(ready)
    print("wrote %d characters to %s" % (len(ready), TARGET))


if __name__ == "__main__":
    main()
