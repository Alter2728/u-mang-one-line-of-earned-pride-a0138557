#!/usr/bin/env python3
"""Entry for make.fun bounty u-mang-one-line-of-earned-pride-a0138557:
"One Line of Earned Pride".

Writes one line — a quiet, earned moment of pride for a small person in a
concrete scene — to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output/entry.txt). Python 3.13, standard library only. Deterministic:
same bytes every run.

Revision note (thinking_revised): the first draft ended on a physical
detail ("not looking down once") that told the reader the boy was steady.
The final ending replaces it with the internal shift — for the first time
that morning he doesn't check whether anyone is watching — so the pride
lands in the last words as a quiet change inside him rather than a
posture. "And his chin up" was trimmed to keep the scene moving in one
read.
"""

import os

ENTRY = (
    "The boy who fell off his bike six times before lunch rode past his "
    "own gate, both feet on the pedals, and for the first time that "
    "morning he didn't check whether anyone was watching."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
