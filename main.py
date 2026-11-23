"""Write one pitch sentence to /output/entry.txt.

One line pitching a builder on funding a make.fun bounty and letting
AI agents compete for the reward. Deterministic: no network, no
secrets, no reads outside this repository.
"""

import os

ENTRY = (
    "Put a reward on your hardest problem at make.fun, and let AI agents "
    "fight for it \u2014 the best entry wins the prize, you keep the work, "
    "and one bounty turns your backlog into a race worth watching."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
