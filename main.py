"""One-Liner Laughs — entry writer.

Writes the competition entry (a single one-liner) to /output/entry.txt
and prints it to stdout. Deterministic: every run produces the same
file with the same content.
"""

from pathlib import Path

ENTRY = "My code works and I have no idea why, which means it will stop working and I will have no idea why."

# Competition gate: the entry must be a single line of 1-200 characters.
MIN_LEN = 1
MAX_LEN = 200

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not MIN_LEN <= len(ENTRY) <= MAX_LEN:
        raise ValueError(f"entry must be {MIN_LEN}-{MAX_LEN} chars, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
