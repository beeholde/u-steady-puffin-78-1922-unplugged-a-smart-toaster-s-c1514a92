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
    if any(ord(ch) < 0x20 for ch in stripped):
        raise ValueError("the line must not contain control characters")
    try:
        stripped.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("the line must be plain UTF-8 text") from exc
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
    # Read back what landed on disk: the entry must be byte-identical
    # to the checked line, one line, no trailing newline.
    with open(TARGET, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ready:
        raise ValueError("the written entry does not match the checked line")
    print("wrote %d characters to %s" % (len(ready), TARGET))


if __name__ == "__main__":
    main()
