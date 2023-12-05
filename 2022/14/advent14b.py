def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    f.close()

    rockpoints = set()

    for line in lines:
        coords = parse_line(line)
        pairs = zip(coords[0:-1], coords[1:])
        for pair in pairs:
            path_coords = calc_path_coords(pair)
            for coord in path_coords:
                if not (coord in rockpoints):
                    rockpoints.add(coord)

    max_x = max([c[0] for c in rockpoints])
    min_x = min([c[0] for c in rockpoints])
    min_x = min([c[0] for c in rockpoints])
    max_y = max([c[1] for c in rockpoints])
    min_y = 1

    floor = max_y + 2

    keep_sanding = True

    sandpoints = set()

    # Reduce this to go one by one after a certain point
    pause_grain = 100000000

    pause_period = 1000000000000

    # Change these to restrict window printed out
    first_row = 1
    last_row = 10000

    grains = 0
    while keep_sanding:
        grains += 1
        keep_sanding = drop_grain(rockpoints, sandpoints, min_x, max_x, min_y, max_y, floor)
        if grains > pause_grain or grains % pause_period == 0:
            display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, floor, None, first_row, last_row, )
            input("Press Enter to continue...")
        # if grains % 1000 == 0:
        #     print(".", end="")
        # if grains % 100000 == 0:
        #     print()

    display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, floor)

    print(f"{grains} grains!")


def display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, floor, grain=None, first_row=1, last_row=1000):
    display = []
    for y in range(max(min_y, first_row), min(floor + 1, last_row)):
        line = f"{y:03d} "
        for x in range(min_x, max_x + 1):
            char = "."
            if (x, y) in rockpoints:
                char = "#"
            if (x, y) in sandpoints:
                char = "o"
            if (x, y) == grain:
                char = "O"
            if y == floor:
                char = "#"
            line += char
        display.append(line)

    print("\n".join(display))


def drop_grain(rockpoints, sandpoints, min_x, max_x, min_y, max_y, floor):
    origin  = (500, 0)
    x, y = origin

    blocked_immediately = False

    blocked = False

    while not blocked:
        # display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, (x, y))
        # input("Press Enter to continue...")

        tests = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        for test in tests:
            if test not in rockpoints and test not in sandpoints and not test[1] == floor:
                x, y = test
                break
        else:
            blocked = True
            sandpoints.add((x, y))
            if (x, y) == origin:
                return False

    return True


def parse_line(line):
    coords = list(line.split(" -> "))
    return [(int(c2[0]), int(c2[1])) for c2 in [c1.split(",") for c1 in coords]]


def calc_path_coords(pair):

    a = sorted(pair)[0]
    b = sorted(pair)[1]

    if a[0] == b[0]:
        return [(int(a[0]), y) for y in range(int(a[1]), int(b[1]) + 1)]

    if a[1] == b[1]:
        return [(x, int(a[1])) for x in range(int(a[0]), int(b[0]) + 1)]


main()
