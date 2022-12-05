def parseline(text: str) -> list:
    pairs = text.split(",")
    return list(map(parsepair, pairs))


def parsepair(text: str):
    [start, end] = text.split("-")
    return {"start": int(start), "end": int(end)}


def contains(a: dict, b: dict):
    return (b["start"] <= a["start"] <= b["end"] and b["start"] <= a["end"] <= b["end"])\
            or \
            (a["start"] <= b["start"] <= a["end"] and a["start"] <= b["end"] <= a["end"])


f = open("input.txt", "r")

total = 0

for line in f:
    parsed = parseline(line.rstrip())
    first = parsed[0]
    second = parsed[1]

    if contains(first, second) or contains(second, first):
        total += 1

print(total)

f.close()
