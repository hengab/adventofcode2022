# input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 2--------")

import typing as typ
import ast
import math


class Packet(object):
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        lt = is_in_order(self.data, other.data)
        return False if lt is None else lt

    def __gt__(self, other):
        gt = is_in_order(self.data, other.data)
        return False if gt is None else gt

    def __eq__(self, other):
        eq = is_in_order(self.data, other.data)
        return True if eq is None else False

    def __repr__(self) -> str:
        return str(self.data)


def is_in_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    for left_part, right_part in zip(left, right):
        result = is_in_order(left_part, right_part)
        if result is not None:
            return result
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False
    return None


packets = []
with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        if line != "":
            packets.append(Packet(ast.literal_eval(line)))


dividers = [Packet([[2]]), Packet([[6]])]
sorted_packets = sorted(packets + dividers)
sum = math.prod([sorted_packets.index(divider) + 1 for divider in dividers])

print(sum)
