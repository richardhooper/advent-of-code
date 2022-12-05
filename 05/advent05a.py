import re


def parseline(text: str) -> dict:
    match = re.match(r'move (\d+) from (\d+) to (\d+)', text)
    [num, fromcol, tocol] = match.group(1, 2, 3)
    return {"num": int(num), "from": int(fromcol), "to": int(tocol)}


stacks: dict = {}
stacks[1] = list("LNWTD")
stacks[2] = list("CPH")
stacks[3] = list("WPHNDGMJ")
stacks[4] = list("CWSNTQL")
stacks[5] = list("PHCN")
stacks[6] = list("THNDMWQB")
stacks[7] = list("MBRJGSL")
stacks[8] = list("ZNWGVBRT")
stacks[9] = list("WGDNPL")

f = open("input.txt", "r")

lines = [line.rstrip() for line in f]

lines = lines[10:]

for line in lines:
    instr = parseline(line.rstrip())
    fromStack: list = stacks[instr["from"]]
    toStack: list = stacks[instr["to"]]
    claw = [fromStack.pop() for _ in range(0, instr["num"])]
    toStack.extend(claw)

print("".join(list(map(lambda a: a[-1], list(stacks.values())))))

f.close()
