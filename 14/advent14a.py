def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    f.close()

    rockmap = []

    for line in lines:
        coords = parse_line(line)
        pairs = zip(coords[0:-1], coords[1:])
        for pair in pairs:
            path_coords = calc_path_coords(pair)
            for coord in path_coords:
                if not (coord in rockmap):
                    rockmap.append(coord)

    max_x = max([c[0] for c in rockmap])
    min_x = min([c[0] for c in rockmap])
    max_y = max([c[1] for c in rockmap])
    min_y = min([c[1] for c in rockmap])

    display = []
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            char = "."
            if (x, y) in rockmap:
                char = "#"
            line += char
        display.append(line)

    print("\n".join(display))


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
