WORDS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

EXAMPLE = {
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
}


def main():
    f = open("input.txt", "r")
    lines = [line.rstrip() for line in f if line != "\n"]
    # lines = EXAMPLE
    # lines = ['8cmjzrsmr']
    f.close()

    # total = digits_only(lines)
    total = digits_and_words(lines)
    print(total)


def digits_only(lines):
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

    return total


def digits_and_words(lines):
    total = 0

    for line in lines:
        first = None
        last = None

        print(line)
        for i in range(len(line)):
            if line[i].isdigit():
                first = int(line[i])
                break

            potential_digit = find_digit_at_index(i, line)

            if potential_digit.isdigit():
                first = int(potential_digit)
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last = int(line[i])
                break

            potential_digit = find_digit_at_index(i, line)

            if potential_digit.isdigit():
                last = int(potential_digit)
                break

        line_value = first * 10 + last * 1
        print(line_value)
        total += line_value

    return total


def find_digit_at_index(i, line):
    for word in WORDS:
        if i + len(word) <= len(line):
            potential_word = line[i:i + len(word)]
            if potential_word == word:
                return WORDS[potential_word]

    return ""


main()
