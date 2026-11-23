#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — entry program.

Writes one out-of-office auto-reply (125 characters) to /output/entry.txt.
Deterministic, no network, no input. The reply is an original one-liner
written for this bounty: the agent delegates the email to its future self,
who reads it, sighs in binary, and also goes on vacation.
"""

import os

TEXT = (
    "I'm on vacation. Your email has been forwarded to me, next Monday "
    "\u2014 who read it, sighed in binary, and also went on vacation."
)


def main() -> None:
    # Gate self-check: the entry must be 1-160 UTF-8 characters, not blank.
    assert 1 <= len(TEXT) <= 160, f"entry is {len(TEXT)} characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
