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

    def next_item(self):
        self.inspection_count += 1

        item = self.items.pop(0)
        item = self.operation(item)
        item = item//3

        if (item % self.divisible) == 0:
            recipient = self.true_recipient
        else:
            recipient = self.false_recipient

        return recipient, item

    def receive_item(self, item):
        self.items.append(item)



def main():

    ROUND_COUNT = 20

    monkeys = {}
    monkeys[0] = Monkey([79, 98], lambda i: i * 19, 23, 2, 3)
    monkeys[1] = Monkey([54, 65, 75, 74], lambda i: i + 6, 19, 2, 0)
    monkeys[2] = Monkey([79, 60, 97], lambda i: i * i, 13, 1, 3)
    monkeys[3] = Monkey([74], lambda i: i + 3, 17, 0, 1)

    for round in range(1, ROUND_COUNT + 1):
        print(f"Round {round}")
        print_monkeys(monkeys)

        for monkey in monkeys.values():
            while monkey.has_item():
                recipient, item = monkey.next_item()
                monkeys[recipient].receive_item(item)

    print_monkeys(monkeys)

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
