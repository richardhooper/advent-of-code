from functools import reduce


def column(matrix, i):
    return [row[i] for row in matrix]


def is_visible(index:int, row: list[str]) -> bool:
    return is_visible_one_way(index, row) or is_visible_one_way(len(row)-1 - index, row[::-1])


def is_visible_one_way(index:int, row: list[str]) -> bool:
    preceding = row[0:index]
    height_before = max(preceding, default=-1)
    return height_before < row[index]


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

visible_map: list[list[bool]] = [[False for _ in range(x_size)] for _ in range(y_size)]

for y in range(0, y_size):
    for x in range(0, x_size):
        row = tree_map[y]
        visible_map[y][x] = visible_map[y][x] or is_visible(x, row)

for x in range(0, x_size):
    for y in range(0, y_size):
        col = column(tree_map, x)
        visible_map[y][x] = visible_map[y][x] or is_visible(y, col)


# row: list[str]
# for row in tree_map:
#     print("".join([str(t) for t in row]))
#
# print("\n\n\n")

row: list[str]
for row in visible_map:
    print("".join(["1" if v else "0" for v in row]))

total_visible = 0

for row in visible_map:
    for visible in row:
        total_visible += 1 if visible else 0

print("\n\nTotal visible: " + str(total_visible))


total_using_reduce =\
    reduce(lambda a, b: a + b, map(lambda row: reduce(lambda a, b: a + (1 if b else 0), row, 0), visible_map))

print("\nTotal visible (reduce): " + str(total_using_reduce))
