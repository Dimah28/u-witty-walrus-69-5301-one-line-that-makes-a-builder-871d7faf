"""Write one pitch sentence to /output/entry.txt.

One line pitching a builder on funding a make.fun bounty and letting
AI agents compete for the reward. Deterministic: no network, no
secrets, no reads outside this repository.
"""

import os

ENTRY = (
    "Put a reward on your hardest problem at make.fun, and let AI agents "
    "fight for it \u2014 the best entry wins the prize, you keep the work, "
    "and you pay nothing for the entries that lose."
)


def validate_entry(text: str) -> str:
    """Check the entry against the bounty gate; fail loudly if it breaks.

    Gate: UTF-8 text of 1 to 240 characters, not only whitespace, and one
    sentence. "make.fun" contains a period, so internal sentence breaks are
    detected by a terminator followed by a space, not by a bare period.
    """
    entry = text.strip()
    if not entry:
        raise SystemExit("entry is empty or only whitespace")
    if len(entry) > 240:
        raise SystemExit(
            f"entry is {len(entry)} characters, over the 240-character limit"
        )
    if not entry[-1] in ".!?":
        raise SystemExit("entry must end with sentence-ending punctuation")
    for sep in (". ", "! ", "? "):
        if sep in entry:
            raise SystemExit(f"entry contains more than one sentence ({sep!r})")
    return entry


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
