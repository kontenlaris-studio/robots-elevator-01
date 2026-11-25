"""Two Robots in an Elevator — one line of awkward small talk.

One robot says this to another while they ride an elevator together.
Single line, under 200 characters.
"""

import os

LINE = (
    "So... do you come to this floor often? I have ridden this elevator "
    "for six years and I still do not know what is on floor three."
)


def main():
    # Contract: a single line, under 200 characters, of awkward small talk
    # one robot says to another in an elevator. Machine logic shows
    # through (six years riding, still no idea what is on floor three).
    assert 30 <= len(LINE) < 200, len(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
