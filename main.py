"""Snooze Button Roast — make.fun entry.

Writes a single roast line (at most 200 characters) to
/output/entry.txt. The program is fixed and deterministic: it takes
no input, makes no network calls, and always writes the same line.

DRAFT pick (first write, to be revised): candidate A below.
Candidates judged against the judge's brief (roast an alarm clock
ringing at 6 AM on a Saturday; real laugh with punchline at the end;
fresh angle; tight; sharp specific voice):

  A. "My alarm clock went off at 6 AM on Saturday like a debt
     collector with a megaphone — mate, the only thing I owe this
     weekend is absolutely nothing." (147)
  B. "At 6 AM on a Saturday, my alarm clock screamed like it was
     auditioning for a fire drill — in a house with no fire, no job,
     and no mercy." (136)
  C. "Six AM, Saturday, and my alarm clock is already yelling like
     I owe it rent — the only thing getting evicted today is you,
     straight into a drawer." (145)

REVISED pick: C. The rent/eviction angle is the freshest — the clock
as a landlord demanding payment on a day nobody works — and the
punchline pays off in the last four words, with the clock itself
getting evicted into a drawer. A is a solid debt-collector joke but
its punchline ("absolutely nothing") is a shrug, not a hit; B's
fire-drill image is vivid but the joke stays a complaint, no turn
at the end. C turns the tables: the clock, not the sleeper, is the
one being thrown out.
"""

from __future__ import annotations

import os

# The entry. 145 characters, plain text, single line, no trailing newline.
ENTRY = "Six AM, Saturday, and my alarm clock is already yelling like I owe it rent — the only thing getting evicted today is you, straight into a drawer."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(entry: str) -> str:
    """Enforce the gate: UTF-8 text of 1-200 characters, not only whitespace."""
    if not isinstance(entry, str):
        raise TypeError("entry must be text")
    if not (1 <= len(entry) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in entry):
        raise ValueError("entry must not contain control characters")
    entry.encode("utf-8")  # must be encodable as UTF-8
    return entry


def main() -> None:
    entry = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
