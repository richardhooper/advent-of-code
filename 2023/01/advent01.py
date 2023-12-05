def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    f.close()

    total = 0

    for line in lines:
        for char in line:
            if char.isdigit():
                total += 10 * int(char)
                break

        for char in line[::-1]:
            if char.isdigit():
                total += int(char)
                break

    print(total)

main()