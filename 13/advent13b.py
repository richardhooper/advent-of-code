import functools
import re
from collections import defaultdict

DIVIDER_1 = [[2]]
DIVIDER_2 = [[6]]

def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    f.close()

    packets = list(map(read_packet, lines))

    packets.append(DIVIDER_1)
    packets.append(DIVIDER_2)

    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))

    print("\n".join(list(map(str, sorted_packets))))

    index_1 = index_2 = 0

    for i in range(len(sorted_packets)):
        packet = sorted_packets[i]
        index = i + 1

        if compare(packet, DIVIDER_1) == 0:
            index_1 = index

        if compare(packet, DIVIDER_2) == 0:
            index_2 = index

    print(f"Divider 1: {str(index_1)} Divider 2: {index_2}")
    print(f"Decoder key: {index_1 * index_2}")


def read_packet(line):
    return eval(line)


def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        list_a = a.copy()
        list_b = b.copy()
        while len(list_a) > 0 and len(list_b) > 0:
            item_a = list_a.pop(0)
            item_b = list_b.pop(0)
            result = compare(item_a, item_b)
            if result != 0:
                return result

        if len(list_a) > 0:
            return 1

        if len(list_b) > 0:
            return -1

        return 0

    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    if isinstance(b, int) and isinstance(a, list):
        return compare(a, [b])

    return compare_int(a, b)


def compare_int(a, b):
    if a < b:
        return -1
    if a == b:
        return 0
    if a > b:
        return 1


main()
