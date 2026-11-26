"""One-Liner Laughs entry: write a single funny line to /output/entry.txt."""

import os

ENTRY = "My code works and I have no idea why, which means it will stop working and I will have no idea why."


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} outside 1-200"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
