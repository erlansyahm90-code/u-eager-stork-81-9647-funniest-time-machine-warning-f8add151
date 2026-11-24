"""Warning-label entry for the make.fun time-machine challenge.

The program produces a single safety notice and saves it to the output
file the grader reads. Nothing fancy here: one fixed string, a length
check so the gate never trips, and a plain write with no extra bytes
at the end.
"""

from pathlib import Path

ENTRY = "WARNING: Do not greet yourself. One of you is already wanted for crimes the other has not committed yet."

# The grader only accepts plain text between 1 and 120 characters.
# This check runs before any file is touched, so a bad label fails loudly
# instead of producing an output the grader would reject.
assert 1 <= len(ENTRY) <= 120, "entry length outside the allowed range"

# Make sure the output folder exists, then write the label exactly as-is.
out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
