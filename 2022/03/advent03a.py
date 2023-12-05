def priority(letter: str):
    value = ord(letter)
    if 65 <= value <= 90:
        return value - 64 + 26
    else:
        return value - 96


f = open("input.txt", "r")

total = 0

for line in f:
    l: int = len(line) - 1
    packsize = int(l/2)
    pack1 = line[0:packsize]
    print(pack1)
    pack2 = line[packsize:-1]
    print(pack2)
    dupe = set(pack1).intersection(set(pack2)).pop()
    print(dupe)
    p = priority(dupe)
    print(p)
    total += p
    print()

print(total)

f.close()
