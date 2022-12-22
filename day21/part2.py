input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 2--------")

import typing as typ
import time
import collections
import sys
import math

start_time = time.perf_counter()

class Operation(object):
    def __init__(self, key: str, operand_1: str, operator: str, operand_2):
        self.key = key
        self.operand_1 = operand_1
        self.operator = operator
        self.operand_2 = operand_2

    def __repr__(self):
        return f"{self.key}: {self.operand_1} {self.operator} {self.operand_2}"

solutions = {}
iterations = math.inf
candidates = {-sys.maxsize: None, 0: None, sys.maxsize: None}
# candidates = {0: math.inf, 255: math.inf, 511: math.inf}
for i in range(10000):
    # print(f"Candidates: {candidates}")
    for humn in candidates:
        monkeys: typ.Dict[str, typ.Union[str, int]] = {}
        # operations: typ.List[Operation] = []
        operations: typ.Deque[Operation] = collections.deque()
        numbers: typ.Dict[str, int] = {}
        with open(input_file_name) as input_file:
            for line in input_file.readlines():
                line = line.strip()
                monkey, token = line.split(":")

                try:
                    if monkey == "humn":
                        numbers[monkey] = humn
                    else:
                        numbers[monkey] = int(token)
                except:
                    if monkey == "root":
                        operations.append(Operation(monkey, token.split()[0].strip(), "-", token.split()[2].strip()))    
                    else:
                        operations.append(Operation(monkey, token.split()[0].strip(), token.split()[1].strip(), token.split()[2].strip()))

        number_keys = numbers.keys()


        # Replace all operations with values
        while operations:
            operation = operations.pop()
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
                root = numbers["root"]
                break
        
        candidates[humn] = root

    # largest negative number
    lower_bound_key = None
    for candidate_key, candidate_value in candidates.items():
        if candidate_value < 0 and candidate_value >= candidates.get(lower_bound_key, candidate_value):
            lower_bound_key = candidate_key 
    
    # smallest positive number
    upper_bound_key = None
    for candidate_key, candidate_value in candidates.items():
        if candidate_value > 0 and candidate_value < candidates.get(upper_bound_key, math.inf):
            upper_bound_key = candidate_key 

    solutions = {k:v for k,v in candidates.items() if int(v) == 0}
    if solutions:
        iterations = i
        break

    # no solution yet, set up new candidates
    candidates = {min(lower_bound_key, upper_bound_key): None, (upper_bound_key+lower_bound_key)//2: None, max(lower_bound_key, upper_bound_key): None}    
    

print(solutions, "in", iterations, "iterations")
print(f"Elapsed time: {time.perf_counter() - start_time} s")


