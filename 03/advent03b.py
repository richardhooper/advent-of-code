def priority(letter: str):
    value = ord(letter)
    if 65 <= value <= 90:
        return value - 64 + 26
    else:
        return value - 96


f = open("input.txt", "r")

total = 0

lines = [line.rstrip() for line in f]

chunks = [lines[i:i + 3] for i in range(0, len(lines), 3)]

for chunk in chunks:
    pack1 = chunk[0][0:]
    pack2 = chunk[1][0:]
    pack3 = chunk[2][0:]
    badge = set(pack1).intersection(set(pack2)).intersection(set(pack3)).pop()
    total += priority(badge)

print(total)

f.close()
