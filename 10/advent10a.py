import re
from collections import defaultdict


def main():

    FIRST_INTERESTING_CYCLE = 20
    CYCLE_PERIOD = 40

    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f]
    f.close()

    cycle = 1
    instructions = defaultdict(int)

    for line in lines:
        if addmatch := re.match("addx (-?\d+)", line):
            instructions[cycle + 2] = int(addmatch.group(1))
            cycle += 1
        cycle += 1

    x = 1
    total_strength = 0
    for i in range(1, list(instructions.keys())[-1]+2):
        x += instructions[i]
        print(f"{i}:{x}")
        if (i - FIRST_INTERESTING_CYCLE) % CYCLE_PERIOD == 0:
            strength = i * x
            total_strength += strength
            print(f"Strength at cycle {i}: {strength}")

    print(f"Total strength: {total_strength}")

main()
