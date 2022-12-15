def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    f.close()

    rockpoints = []

    for line in lines:
        coords = parse_line(line)
        pairs = zip(coords[0:-1], coords[1:])
        for pair in pairs:
            path_coords = calc_path_coords(pair)
            for coord in path_coords:
                if not (coord in rockpoints):
                    rockpoints.append(coord)

    max_x = max([c[0] for c in rockpoints])
    min_x = min([c[0] for c in rockpoints])
    max_y = max([c[1] for c in rockpoints])
    min_y = 1

    keep_sanding = True

    sandpoints = []

    # Reduce this to go one by one after a certain point
    pause_grain = 1000

    # Change these to restrict window printed out
    first_row = 1
    last_row = 10000

    grains = 0
    while keep_sanding:
        grains += 1
        keep_sanding = drop_grain(rockpoints, sandpoints, min_x, max_x, min_y, max_y)
        if grains > pause_grain:
            display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, None, first_row, last_row)
            input("Press Enter to continue...")

    display(rockpoints, sandpoints, min_x, max_x, min_y, max_y)

    print(f"{grains - 1} grains!")


def display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, grain=None, first_row=1, last_row=1000):
    display = []
    for y in range(max(min_y, first_row), min(max_y + 1, last_row)):
        line = f"{y:03d} "
        for x in range(min_x, max_x + 1):
            char = "."
            if (x, y) in rockpoints:
                char = "#"
            if (x, y) in sandpoints:
                char = "o"
            if (x, y) == grain:
                char = "O"
            line += char
        display.append(line)

    print("\n".join(display))


def drop_grain(rockpoints, sandpoints, min_x, max_x, min_y, max_y):
    x = 500
    y = 0

    blocked = False
    escaped = False

    while not (blocked or escaped):
        # display(rockpoints, sandpoints, min_x, max_x, min_y, max_y, (x, y))
        # input("Press Enter to continue...")
        if x < min_x or x > max_x or y > max_y:
            escaped = True

        tests = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        for test in tests:
            if test not in rockpoints and test not in sandpoints:
                x, y = test
                break
        else:
            blocked = True
            sandpoints.append((x, y))

    return not escaped


def parse_line(line):
    coords = list(line.split(" -> "))
    return [(c2[0], c2[1]) for c2 in [c1.split(",") for c1 in coords]]


def calc_path_coords(pair):

    a = sorted(pair)[0]
    b = sorted(pair)[1]

    if a[0] == b[0]:
        return [(int(a[0]), y) for y in range(int(a[1]), int(b[1]) + 1)]

    if a[1] == b[1]:
        return [(x, int(a[1])) for x in range(int(a[0]), int(b[0]) + 1)]


main()
