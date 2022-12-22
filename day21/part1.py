# input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 1--------")

import typing as typ
import time
import collections


start_time = time.perf_counter()

class Operation(object):
    def __init__(self, key: str, operand_1: str, operator: str, operand_2):
        self.key = key
        self.operand_1 = operand_1
        self.operator = operator
        self.operand_2 = operand_2

    def __repr__(self):
        return f"{self.key}: {self.operand_1} {self.operator} + {self.operand_2}"

monkeys: typ.Dict[str, typ.Union[str, int]] = {}
# operations: typ.List[Operation] = []
operations: typ.Deque[Operation] = collections.deque()
numbers: typ.Dict[str, int] = {}
with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        monkey, token = line.split(":")

        try:
            numbers[monkey] = int(token)
        except:
            operations.append(Operation(monkey, token.split()[0].strip(), token.split()[1].strip(), token.split()[2].strip()))

number_keys = numbers.keys()
# Replace all operations with values
while operations:
    operation = operations.pop()
    print(operation)
    if operation.operand_1 in number_keys and operation.operand_2 in number_keys:
        if operation.operator == "+":
            numbers[operation.key] = numbers[operation.operand_1] + numbers[operation.operand_2]
        elif operation.operator == "-":
            numbers[operation.key] = numbers[operation.operand_1] - numbers[operation.operand_2]
        elif operation.operator == "/":
            numbers[operation.key] = numbers[operation.operand_1] / numbers[operation.operand_2]
        elif operation.operator == "*":
            numbers[operation.key] = numbers[operation.operand_1] * numbers[operation.operand_2]
        else:
            raise Exception(f"Unexpected Operator '{operation.operator}'")
        number_keys = numbers.keys()        
    else:
        # Can't resolve yet....add to end of line
        operations.appendleft(operation)

    if "root" in number_keys:
        break

print(numbers["root"])
print(f"Elapsed time: {time.perf_counter() - start_time} s")