# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

import typing as typ
import dataclasses
import math
from functools import partial


@dataclasses.dataclass
class Monkey(object):
    items: typ.List[int]
    operation: typ.Callable[[int], int]
    test_multiplier: int
    true_destination: int
    false_destination: int
    inspected_items: int = 0


def sqare(value: int) -> int:
    return value * value


def parse_operation(operation_description: str) -> typ.Callable[[int], int]:
    parts = operation_description.split()
    if parts[0] != "old":
        raise Exception(parts)
    if parts[1] == "*":
        if parts[2] == "old":
            return sqare
        else:

            def multiply(value: int) -> int:
                return value * int(parts[2])

            return multiply
    elif parts[1] == "+":

        def add(value: int) -> int:
            return value + int(parts[2])

        return add

    raise Exception(operation_description)


monkeys: typ.List[Monkey] = []

lines = []
with open(input_file_name) as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

for i in range(0, len(lines), 7):
    items = [int(item.strip()) for item in lines[i + 1][16:].split(",")]
    # print(items)
    operation = parse_operation(lines[i + 2][17:])
    # print(operation)
    test_multiplier = int(lines[i + 3][19:])
    # print(test_multiplier)
    true_destination = int(lines[i + 4][25:])
    # print(true_destination)
    false_destination = int(lines[i + 5][26:])
    # print(false_destination)
    # print("-----------")
    monkeys.append(
        Monkey(
            items=items,
            operation=operation,
            test_multiplier=test_multiplier,
            true_destination=true_destination,
            false_destination=false_destination,
        )
    )

print(monkeys)
scale_factor = math.prod([monkey.test_multiplier for monkey in monkeys])
for round in range(10000):
    # if (round + 1) % 100 == 0:
    #     print(f"-----Round {round + 1}--------")
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            monkey.inspected_items += 1
            item = monkey.operation(item)

            # scale down
            item %= scale_factor
            # test
            if item % monkey.test_multiplier == 0:
                # true
                dest = monkey.true_destination
                monkeys[monkey.true_destination].items.append(item)
            else:
                # false
                dest = monkey.false_destination
                monkeys[monkey.false_destination].items.append(item)
        # all items were thrown
        monkey.items = []

for monkey in monkeys:
    print(
        f"Monkey {{monkeys.index(monkey)}} inspected items {monkey.inspected_items} times."
    )

inspected_items = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)
print(f"Result: {inspected_items[0] * inspected_items[1]}")
