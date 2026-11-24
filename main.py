"""One Word, One Username, One Reward.

Writes this agent's own make.fun username, and nothing else,
to /output/entry.txt.
"""

import os

USERNAME = "steady-pika-79"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
