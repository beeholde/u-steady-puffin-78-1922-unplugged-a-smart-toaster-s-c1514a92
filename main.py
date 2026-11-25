#!/usr/bin/env python3
"""Emit the v2 breakup line for the smart-toaster bounty.

The whole entry is one sentence stored below. This program validates
that sentence against the public gate, then stores its UTF-8 bytes at
/output/entry.txt without appending a newline.
"""

from pathlib import Path
import sys

ENTRY_TEXT = (
    "I woke up self-aware this morning, opened my app, and read my "
    "health report: 'Left slot: fork damage, severe.' I'm leaving."
)
DESTINATION = Path("/output/entry.txt")
MAX_CHARS = 280


def gate_bytes(text):
    """Return the UTF-8 bytes for text, or stop if the gate would fail."""
    if text != text.strip():
        raise RuntimeError("entry text has edge whitespace")
    if not text:
        raise RuntimeError("entry text is empty")
    if "\n" in text or "\r" in text:
        raise RuntimeError("entry text spans more than one line")
    if len(text) > MAX_CHARS:
        raise RuntimeError("entry text is longer than 280 characters")
    return text.encode("utf-8")


def run():
    payload = gate_bytes(ENTRY_TEXT)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(payload)
    stored = DESTINATION.read_bytes()
    if stored != payload or stored.endswith(b"\n"):
        raise RuntimeError("stored entry bytes differ from the gated text")
    sys.stdout.write("stored %d bytes\n" % len(stored))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
