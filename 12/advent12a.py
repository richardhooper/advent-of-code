def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f]
    f.close()

    heightmap = {}

    row = 0
    column = 0
    start = None
    end = None
    for line in lines:
        column = 0
        for char in line:
            heightmap[column, row] = char
            if char == "S":
                start = column, row
                heightmap[column, row] = "a"
            elif char == "E":
                end = column, row
                heightmap[column, row] = "z"
            else:
                heightmap[column, row] = char
            column += 1
        row += 1

    max_x = column - 1
    max_y = row - 1

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(heightmap[x, y], end="")
        print()

    visited = [start]
    queue = [start]

    steps = 0

    while len(queue) > 0:
        step_set = len(queue)
        print(f"Step {steps}")

        for i in range(step_set, 0, -1):
            visiting = queue.pop(0)
            visited.append(visiting)
            print(visiting)

            if visiting == end:
                print(f"End found after {steps} steps")
                exit()

            neighbours = find_neighbours(visiting, max_x, max_y)
            for neighbour in neighbours:
                include = True
                if neighbour in visited:
                    include = False
                if ord(heightmap[neighbour]) - ord(heightmap[visiting]) > 1:
                    include = False
                if include:
                    visited.append(neighbour)
                    queue.append(neighbour)
        steps += 1


def find_neighbours(point, max_x, max_y):
    neighbours = []
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour = find_specific_neighbour(point, direction, max_x, max_y)
        if neighbour:
            neighbours.append(neighbour)
    return neighbours


def find_specific_neighbour(point, direction, max_x, max_y):
    x = point[0] + direction[0]
    y = point[1] + direction[1]
    if x < 0 or x > max_x:
        return None
    if y < 0 or y > max_y:
        return None

    return x, y


main()
