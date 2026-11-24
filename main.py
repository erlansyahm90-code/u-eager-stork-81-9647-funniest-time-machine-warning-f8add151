"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt. The label is 104 characters, inside the 120-character
gate, and is written with no trailing newline so the file is exactly
104 bytes.

The joke follows the judge brief: a real time-travel hazard (meeting
your duplicate self / a temporal paradox) turned into the joke itself,
kept in a deadpan official-safety-notice tone, with the surprise saved
for the last few words ("has not committed yet").
"""

import os

ENTRY = (
    "WARNING: Do not greet yourself. "
    "One of you is already wanted for crimes "
    "the other has not committed yet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the competition's own rule: 1-120 characters.
    # No trailing newline: the output file must be exactly len(ENTRY) bytes.
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
