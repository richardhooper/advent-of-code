from typing import Callable


class Monkey:
    def __init__(self, starting_items: list, operation: Callable, divisible: int, true_recipient: int, false_recipient: int):
        self.items = starting_items
        self.operation = operation
        self.divisible = divisible
        self.true_recipient = true_recipient
        self.false_recipient = false_recipient
        self.inspection_count = 0

    def has_item(self):
        return len(self.items) > 0

    def next_item(self, lcm):
        self.inspection_count += 1

        item = self.items.pop(0)
        item = self.operation(item)
        # item = item//3

        multiple = item // lcm
        if multiple > 0:
            item -= multiple * lcm

        if (item % self.divisible) == 0:
            recipient = self.true_recipient
        else:
            recipient = self.false_recipient

        return recipient, item

    def receive_item(self, item):
        self.items.append(item)



def main():

    ROUND_COUNT = 10000

    monkeys = {}
    monkeys[0] = Monkey([91, 54, 70, 61, 64, 64, 60, 85], lambda i: i * 13, 2, 5, 2)
    monkeys[1] = Monkey([82], lambda i: i + 7, 13, 4, 3)
    monkeys[2] = Monkey([84, 93, 70], lambda i: i + 2, 5, 5, 1)
    monkeys[3] = Monkey([78, 56, 85, 93], lambda i: i * 2, 3, 6, 7)
    monkeys[4] = Monkey([64, 57, 81, 95, 52, 71, 58], lambda i: i * i, 11, 7, 3)
    monkeys[5] = Monkey([58, 71, 96, 58, 68, 90], lambda i: i + 6, 17, 4, 1)
    monkeys[6] = Monkey([56, 99, 89, 97, 81], lambda i: i + 1, 7, 0, 2)
    monkeys[7] = Monkey([68, 72], lambda i: i + 8, 19, 6, 0)

    LCM = 1
    for monkey in monkeys.values():
        LCM *= monkey.divisible

    for round in range(1, ROUND_COUNT + 1):
        print(f"Round {round}")
        # print_monkeys(monkeys)

        # if round % 100 == 0:
        # print(f"Round {round}")

        for monkey in monkeys.values():
            while monkey.has_item():
                recipient, item = monkey.next_item(LCM)
                monkeys[recipient].receive_item(item)

    # print_monkeys(monkeys)

    inspection_counts = []
    for monkey in monkeys.values():
        inspection_counts.append(monkey.inspection_count)

    top_two = list(reversed(sorted(inspection_counts)))[:-2]
    monkey_business = top_two[0] * top_two[1]

    print(f"Monkey business: {monkey_business}")


def print_monkeys(monkeys):
    for monkey_id in monkeys:
        monkey_items = ", ".join(map(str, monkeys[monkey_id].items))
        print(f"Monkey {str(monkeys[monkey_id])} has {monkey_items}")
    print("\n")

main()
