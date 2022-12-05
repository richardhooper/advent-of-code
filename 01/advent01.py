f = open("input.txt", "r")
total = 0
highest = [0, 0, 0]

for line in f:
    if line != "\n":
        total += int(line)
    else:
        if total > highest[0]:
            highest[0] = total
            highest.sort()

        total = 0


combined = highest[0] + highest[1] + highest[2]

print(combined)

f.close()
