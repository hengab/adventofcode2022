input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 2--------")

import typing as typ
import time
import collections

start_time = time.perf_counter()

decryption_key = 811589153
class NodeData(object):
    def __init__(self, value: int) -> None:
        self.value = value


d = collections.deque()
items: typ.List[NodeData] = []
zero: typ.Optional[NodeData] = None

with open(input_file_name) as input_file:
    for line in input_file.readlines():
        data = NodeData(value=int(line.strip()) * decryption_key)

        d.append(data)
        items.append(data)
        if data.value == 0:
            zero = data

total_items = len(items)
print("Total Items:", total_items)
# print(d)
for i in range(10):
    for item in items:
        origin_index = d.index(item)

        d.remove(item)
        destination_index = (origin_index + item.value) % (total_items - 1)  # +  wraps

        if destination_index == 0:
            d.append(item)
        elif destination_index == total_items - 1:
            d.appendleft(item)
        else:
            d.insert(destination_index, item)

zero_index = d.index(zero)
coordinate_1 = (zero_index + 1000) % total_items
coordinate_2 = (zero_index + 2000) % total_items
coordinate_3 = (zero_index + 3000) % total_items

print(coordinate_1, d[coordinate_1])
print(coordinate_2, d[coordinate_2])
print(coordinate_3, d[coordinate_3])
print(d[coordinate_1].value + d[coordinate_2].value + d[coordinate_3].value)

print(f"Elapsed time: {time.perf_counter() - start_time} s")
