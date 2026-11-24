#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the entrant.

The word is "Exhausting". It is the single word an ex reaches for first:
every argument, every late-night spiral, every "we need to talk" distilled
into one verdict. It stings because it is painfully true and the entrant
plainly knows it, it lands instantly with no explanation needed, and it is
relatable to anyone who has ever been on either side of that sentence.
10 characters, inside the gate's 1-24 character limit.
"""

import os

WORD = "Exhausting"


def main() -> None:
    # Gate check, same rule the sealed scorer applies: UTF-8 text of
    # 1 to 24 characters, not only white space.
    assert 1 <= len(WORD) <= 24 and WORD.strip(), "word fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
