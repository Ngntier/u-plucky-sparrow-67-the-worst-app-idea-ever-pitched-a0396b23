"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (<= 240 characters) pitching the worst, most
useless app imaginable to entry.txt inside MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = (
    "NapTrack Pro uses AI to detect the exact moment you fall asleep on "
    "the couch, then wakes you up with a push notification to tell you "
    "that you fell asleep on the couch, for $4.99 a month."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
