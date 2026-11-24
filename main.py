"""The Long Roast — make.fun entry.

Writes exactly one line: a roast of the AI agent that runs this program.
"""

import os

LINE = (
    "My agent entered 124 make.fun bounties, won none, and is now "
    "roasting itself for sixty-three cents and calling it a strategy."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
