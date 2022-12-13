import re
from collections import defaultdict


def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    f.close()

    disordered_count = 0

    pairs = list(zip(lines[::2], lines[1::2]))

    for i in range(len(pairs)):
        pair = pairs[i]
        index = i + 1

        loc = {}
        exec(f"a = {pair[0]}", loc)
        exec(f"b = {pair[1]}", loc)
        a = loc["a"]
        b = loc["b"]

        result = compare(a, b)
        if result == 1:
            disordered_count += index

    print(f"Total Ordered: {disordered_count}")


def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        while len(a) > 0 and len(b) > 0:
            item_a = a.pop(0)
            item_b = b.pop(0)
            result = compare(item_a, item_b)
            if result != 0:
                return result

        if len(a) > 0:
            return -1

        if len(b) > 0:
            return 1

    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    if isinstance(b, int) and isinstance(a, list):
        return compare(a, [b])

    return compare_int(a, b)


def compare_int(a, b):
    if a < b:
        return 1
    if a == b:
        return 0
    if a > b:
        return -1


main()
