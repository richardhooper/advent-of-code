from functools import reduce


def column(matrix, i):
    return [row[i] for row in matrix]


def how_scenic(index:int, row: list[str]) -> int:
    return how_scenic_one_way(index, row) * how_scenic_one_way(len(row) - 1 - index, row[::-1])


def how_scenic_one_way(index:int, row: list[str]) -> int:
    if index == len(row) - 1:
        return 0

    tree_count = 0
    viewer = row[index]

    succeeding = row[index+1:]
    for tree in succeeding:
        tree_count += 1
        if tree >= viewer:
            break

    return tree_count


f = open("input.txt", "r")

lines = [line.rstrip() for line in f]

tree_map: list[list] = []

x_size = 0
y_size = 0

for line in lines:
    x = 0
    tree_map.append([])
    for char in line:
        tree_map[y_size].append(int(char))

        x += 1
        x_size = max(x, x_size)

    y_size += 1

f.close()

print("X: " + str(x_size) + ", Y:" + str(y_size))

scenic_map: list[list[int]] = [[1 for _ in range(x_size)] for _ in range(y_size)]

for y in range(0, y_size):
    for x in range(0, x_size):
        row = tree_map[y]
        scenic_map[y][x] = scenic_map[y][x] * how_scenic(x, row)

for x in range(0, x_size):
    for y in range(0, y_size):
        col = column(tree_map, x)
        scenic_map[y][x] = scenic_map[y][x] * how_scenic(y, col)


# row: list[str]
# for row in tree_map:
#     print("".join([str(t) for t in row]))
#
# print("\n\n\n")

row: list[str]
for row in scenic_map:
    print(":".join([str(v) for v in row]))

max_scenic = 0

for row in scenic_map:
    for scenic in row:
        max_scenic = max(max_scenic, scenic)

print("\n\nMax scenic: " + str(max_scenic))
