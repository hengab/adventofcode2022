input_file_name = "sample_input.txt"
# input_file_name = "input.txt"
print("--------Part 1--------")

import typing as typ
import time

start_time = time.perf_counter()


with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        ...

print(f"Elapsed time: {time.perf_counter() - start_time} s")