import os


def part1(instructions, start=50):
    """
    Calculates the number of times the dial points at 0 (Part 1).
    Counts only when the dial STOPS on 0.
    """
    pos = start % 100
    count = 0

    for line in instructions:
        line = line.strip()
        if not line:
            continue

        direction = line[0].upper()
        try:
            amount = int(line[1:])
        except ValueError:
            print(f"Warning: Skipping invalid line format: '{line}'")
            continue

        if direction == "L":
            pos = (pos - amount) % 100
        elif direction == "R":
            pos = (pos + amount) % 100
        else:
            raise ValueError(f"Bad direction in line: {line}")

        if pos == 0:
            count += 1

    return count


def part2(instructions, start=50):
    """
    Calculates the number of times the dial points at 0 (Part 2).
    Counts every time the dial hits 0, including during rotation.
    """
    pos = start % 100
    count = 0

    for line in instructions:
        line = line.strip()
        if not line:
            continue

        direction = line[0].upper()
        try:
            amount = int(line[1:])
        except ValueError:
            print(f"Warning: Skipping invalid line format: '{line}'")
            continue

        # Each full 100 steps guarantees exactly one 0 hit
        full_circles = amount // 100
        count += full_circles

        remainder = amount % 100

        if remainder == 0:
            continue

        if direction == "R":
            # Moving up (0 -> 99 -> 0).
            # We hit 0 if we cross the boundary from 99 to 0.
            # In linear terms 0..99, this is crossing 100.
            if pos + remainder >= 100:
                count += 1
            pos = (pos + remainder) % 100

        elif direction == "L":
            # Moving down (0 -> 99 -> ...).
            # We hit 0 if we reach 0 or cross it downwards.
            # If we start at 0, the very first step is 99, so we don't hit 0
            # in the remainder steps (since remainder < 100).
            if pos > 0 and pos - remainder <= 0:
                count += 1
            pos = (pos - remainder) % 100

    return count


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")

    try:
        with open(input_file, "r") as f:
            # Read all lines once so we can pass them to both functions
            lines = f.readlines()
            
            # Part 1
            result1 = part1(lines)
            print(f"Part 1 Password: {result1}")

            # Part 2
            result2 = part2(lines)
            print(f"Part 2 Password: {result2}")

    except FileNotFoundError:
        print(f"Error: Could not find '{input_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
