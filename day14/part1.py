# input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 1--------")

import typing as typ
import time 
start_time = time.perf_counter() 

cave = [["."] * 1000 for _ in range(300)]
min_x = 500
max_x = 0
min_y = 1000
max_y = 0
max_stone_y = 0

with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        parts = line.split(" -> ")

        start = None
        for part in parts:
            end = tuple(int(v) for v in part.split(","))
            if start is not None:
                from_x = min(start[0], end[0])
                to_x = max(start[0], end[0]) + 1
                for x in range(from_x, to_x):
                    from_y = min(start[1], end[1])
                    to_y = max(start[1], end[1]) + 1
                    for y in range(from_y, to_y):
                        cave[y][x] = "#"

                        min_x = min(x, min_x)
                        min_y = min(y, min_y)

                        max_x = max(x, max_x)
                        max_y = max(y, max_y)

                        if y > max_stone_y:
                            max_stone_y = y

            start = end


at_rest_count = 0
into_the_abyss = False

while not into_the_abyss:
    sand_unit_location = (500, 0)
    at_rest = False
    while not into_the_abyss and not at_rest:
        if sand_unit_location[1] + 1 > max_stone_y:
            into_the_abyss = True
        elif cave[sand_unit_location[1] + 1][sand_unit_location[0]] == ".":
            # down one step
            sand_unit_location = (sand_unit_location[0], sand_unit_location[1] + 1)
        elif cave[sand_unit_location[1] + 1][sand_unit_location[0] - 1] == ".":
            # one step down and to the left
            sand_unit_location = (sand_unit_location[0] - 1, sand_unit_location[1] + 1)
        elif cave[sand_unit_location[1] + 1][sand_unit_location[0] + 1] == ".":
            # one step down and to the right
            sand_unit_location = (sand_unit_location[0] + 1, sand_unit_location[1] + 1)
        else:
            cave[sand_unit_location[1]][sand_unit_location[0]] = "o" # str(at_rest_count + 1)
            at_rest = True
            at_rest_count += 1


min_x = min(500, min_x)
min_y = min(0, min_y)

max_x = max(500, max_x)
max_y = max(0, max_y)
cave[0][500] = "+"

# for y in range(min_y, max_y + 5):
#     print("".join([cave[y][x] for x in range(min_x, max_x + 5)]))

print(f"Part 1: {at_rest_count}")
print(f"Part 1 Time: {time.perf_counter() - start_time} s")