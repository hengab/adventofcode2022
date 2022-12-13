# input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 1--------")

import typing as typ


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


with open(input_file_name) as input_file:
    lines = input_file.readlines()

import ast

pairs = []
for i in range(0, len(lines) - 1, 3):
    pairs.append(
        (ast.literal_eval(lines[i].strip()), ast.literal_eval(lines[i + 1].strip()))
    )

index = 0
sum = 0
for pair in pairs:
    index += 1
    if is_in_order(pair[0], pair[1]) is True:
        sum += index

print(sum)
