def move_head(direction: str, distance: int, current: tuple):
    x_diff, y_diff  = point_diffs(direction, distance)
    x, y = current

    return (x + x_diff, y + y_diff)

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


def move_tail(head: tuple, tail: tuple, direction: str):
    [head_x, head_y, tail_x, tail_y] = head + tail

    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        x_diff, y_diff = point_diffs(direction, -1)
        return head_x + x_diff, head_y + y_diff

    return tail

def is_visible(index: int, row: list[str]) -> bool:
    return is_visible_one_way(index, row) or is_visible_one_way(len(row) - 1 - index, row[::-1])


def is_visible_one_way(index: int, row: list[str]) -> bool:
    preceding = row[0:index]
    height_before = max(preceding, default=-1)
    return height_before < row[index]


f = open("input.txt", "r")

moves = [line.rstrip() for line in f]

visited: dict[tuple, bool] = {}

head = (0, 0)
tail = (0, 0)

for move in moves:
    print(f"\nHead: {head} Tail: {tail}")
    print(move)
    direction = move.split(" ")[0]
    distance = int(move.split(" ")[1])
    for _ in range(distance):
        head = move_head(direction, 1, head)
        tail = move_tail(head, tail, direction)
        visited[tail] = True
        print(f"Head: {head} Tail: {tail}")


print(f"Visited spaces = {len(visited)}")

f.close()
