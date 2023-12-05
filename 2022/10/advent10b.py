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
    scan = 0
    line = ""
    for i in range(1, list(instructions.keys())[-1]+4):
        x += instructions[i]
        # print(f"{i}:{x}")

        char = "#" if abs(scan - x) <= 1 else "."
        line += char

        if i % CYCLE_PERIOD == 0:
            scan = 0
            print(line)
            line = ""
        else:
            scan += 1


main()
