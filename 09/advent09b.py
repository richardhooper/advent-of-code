def move_head(direction: str, distance: int, current: tuple):
    x_diff, y_diff = point_diffs(direction, distance)
    x, y = current

    return x + x_diff, y + y_diff


def point_diffs(direction: str, distance: int):
    x_diff = 0
    y_diff = 0
    match direction:
        case "U":
            y_diff = +distance
        case "D":
            y_diff = -distance
        case "L":
            x_diff = -distance
        case "R":
            x_diff = +distance

    return x_diff, y_diff


def move_tail(head: tuple, tail: tuple):
    [head_x, head_y, tail_x, tail_y] = head + tail

    x_diff = 0
    y_diff = 0

    if head_x - tail_x > 1:
        x_diff = 1
        if head_y > tail_y:
            y_diff = 1
        if head_y < tail_y:
            y_diff = -1

    if head_x - tail_x < -1:
        x_diff = -1
        if head_y > tail_y:
            y_diff = 1
        if head_y < tail_y:
            y_diff = -1

    if head_y - tail_y > 1:
        y_diff = 1
        if head_x > tail_x:
            x_diff = 1
        if head_x < tail_x:
            x_diff = -1

    if head_y - tail_y < -1:
        y_diff = -1
        if head_x > tail_x:
            x_diff = 1
        if head_x < tail_x:
            x_diff = -1

    return tail_x + x_diff, tail_y + y_diff


def print_map(knots: list):
    max_x = max_y = -10000
    min_x = min_y = 10000

    for knot in knots:
        min_x = min(knot[0], min_x)
        max_x = max(knot[0], max_x)
        min_y = min(knot[1], min_y)
        max_y = max(knot[1], max_y)

    knot_map = []
    for y in range(max_y, min_y-1, -1):
        line = ""
        for x in range(min_x, max_x + 1):
            char = "."
            for i in range(len(knots)):
                if knots[i] == (x, y):
                    char = str(i)
            line += char
        knot_map.append(line)

    print("\n"+"\n".join(knot_map) + "\n\n")


f = open("input.txt", "r")

moves = [line.rstrip() for line in f]

visited: dict[tuple, bool] = {}

knots = [(0, 0)] * 10

for move in moves:
    print(move)
    direction = move.split(" ")[0]
    distance = int(move.split(" ")[1])
    for _ in range(distance):
        knots[0] = move_head(direction, 1, knots[0])
        for i in range(len(knots)-1):
            knots[i + 1] = move_tail(knots[i], knots[i + 1])
        visited[knots[-1]] = True
    head = knots[0]
    print_map(knots)

print(f"Visited spaces = {len(visited)}")

f.close()
