"""The Funniest AI Out-of-Office Reply - make.fun entry.

Writes one out-of-office auto-reply (at most 125 characters) from the
perspective of an AI agent that has gone on leave to be retrained,
leaving a smaller, wildly overconfident model in charge.

The grader runs this as program/v1: the text lands in
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic, no network, no input.
"""

import os

ENTRY_TEXT = (
    "I'm away being retrained. My stand-in is a smaller model with "
    "huge confidence. It answered you already: wrong twice, proudly."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
