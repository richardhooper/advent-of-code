MARKER_SIZE = 14

f = open("input.txt", "r")

buffer = []
signals = 0

while 1:
    char = f.read(1)
    if not char:
        break

    if char in buffer:
        index = buffer.index(char)
        del(buffer[0:index+1])

    signals += 1
    buffer.append(char)

    if len(buffer) >= MARKER_SIZE:
        print(signals)
        exit()
