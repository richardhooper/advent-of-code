import re
from collections import defaultdict
from functools import reduce
from typing import List, Dict


def parent(current: str) -> str:
    dirrev = current[::-1][1:]
    return dirrev[dirrev.find("/"):][::-1]


def addToBranch(dirname: str, size: int, sizes: dict):
    sizes[dirname] = size
    while dirname != "/":
        dirname = parent(dirname)
        sizes[dirname] += size


f = open("input.txt", "r")

lines = [line.rstrip() for line in f]

currentdir: str = "/"

files: Dict[str, List] = {"/": []}
dirs: Dict[str, List] = {"/": []}

for line in lines:
    if commandmatch := re.match("\$ (.+)", line):
        if cdmatch := re.match("cd (.*)", commandmatch.group(1)):
            cd = cdmatch.group(1)
            if cd == "/":
                currentdir = "/"
            elif cd == "..":
                dirrev = currentdir[::-1][1:]
                currentdir = dirrev[dirrev.find("/"):][::-1]
            else:
                currentdir += cd + "/"
                files[currentdir] = []
                dirs[currentdir] = []
            # print(currentdir)
        elif lsmatch := re.match("ls", commandmatch.group(1)):
            pass
    elif commandmatch := re.match("dir (.*)", line):
        dirname = commandmatch.group(1)
        dirs[currentdir].append(dirname)
        # print("dir "+ dirname)
    elif commandmatch := re.match("(\d+) (\w+)", line):
        size = commandmatch.group(1)
        file = commandmatch.group(2)
        files[currentdir].append(size+":"+file)
        # print("file "+size+" "+file)

dirsizes: defaultdict[str, int] = defaultdict(int)


for d in dirs.keys():
    dirfiles = files[d]
    sizes = list(map(lambda filesize: int(filesize.split(":")[0]), dirfiles))
    total = reduce(lambda a, b: a + b, sizes, 0)
    addToBranch(d, total, dirsizes)

belowlimit = {key: value for (key, value) in dirsizes.items() if value <= 100000}

totalbelowlimit = reduce(lambda a, b: a + b, belowlimit.values(), 0)

print("Total size of dirs < 100000 = " + str(totalbelowlimit))

sizesonly = sorted(dirsizes.values(), reverse=True)

totalused = dirsizes["/"]
totalfs = 70000000
spacerequired = 30000000
available = totalfs - totalused
target = spacerequired - available

print("Total used: " + str(totalused))
print("Available: " + str(available))

# This way of finding a particular size is a bit silly given the better way used for part A...
biggest = sizesonly[0]
for size in sizesonly:
    # print(str(biggest))
    if size < target:
        break
    biggest = size

print("Smallest dir more then target " + str(target) + " is " + str(biggest))

f.close()
