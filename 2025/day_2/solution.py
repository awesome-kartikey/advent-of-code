# solution.py
import os
import sys


def is_invalid_id_part1(n: int) -> bool:
    """
    Part 1: number is made of some digits repeated exactly twice, e.g. 6464.
    """
    s = str(n)
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    return s[:mid] == s[mid:]


def is_invalid_id_part2(n: int) -> bool:
    """
    Part 2: number is made of some digits repeated at least twice, e.g. 123123123.
    """
    s = str(n)
    length = len(s)

    # try all possible pattern lengths
    for size in range(1, length // 2 + 1):
        if length % size != 0:
            continue

        pattern = s[:size]
        if pattern * (length // size) == s:
            return True

    return False


def solve(input_text: str, use_part2_rules: bool) -> int:
    """
    Input is a comma-separated list of ranges: 100-200,300-350,...
    Returns the sum of all IDs that are invalid under the chosen rules.
    """
    validator = is_invalid_id_part2 if use_part2_rules else is_invalid_id_part1

    text = input_text.replace("\n", "").strip().strip(",")
    if not text:
        return 0

    total = 0
    for chunk in text.split(","):
        if "-" not in chunk:
            continue

        start_str, end_str = chunk.split("-", 1)
        try:
            start = int(start_str)
            end = int(end_str)
        except ValueError:
            continue

        for n in range(start, end + 1):
            if validator(n):
                total += n

    return total


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "input.txt")

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
    except FileNotFoundError:
        print(f"Could not find input file at {path}")
        sys.exit(1)

    part1 = solve(raw, use_part2_rules=False)
    part2 = solve(raw, use_part2_rules=True)

    print(f"🎁 Part 1 Result (Sequence repeated EXACTLY twice): {part1}")
    print(f"💰 Part 2 Result (Sequence repeated AT LEAST twice): {part2}")


if __name__ == "__main__":
    main()
