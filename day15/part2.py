# input_file_name = "sample_input.txt"
# search_area_max = 20
input_file_name = "input.txt"
search_area_max = 4000000
print("--------Part 2--------")

import typing as typ
import dataclasses
import time

start_time = time.perf_counter()


@dataclasses.dataclass
class Sensor(object):
    x: int
    y: int
    beacon_distance: int = 0

    def x_coverage(self):
        return range(self.x - self.beacon_distance, self.x + self.beacon_distance)

    def y_coverage(self):
        return range(self.y - self.beacon_distance, self.y + self.beacon_distance)


sensors: typ.List[Sensor] = []

with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()

        sensor, beacon = line.strip("Sensor at ").split(": closest beacon is at ")
        # sensor="x=2557568, y=3759110" beacon="x=2594124, y=3746832"

        sensor_x, sensor_y = [int(v.strip()[2:]) for v in sensor.split(",")]
        beacon_x, beacon_y = [int(v.strip()[2:]) for v in beacon.split(",")]

        sensors.append(
            Sensor(
                x=sensor_x,
                y=sensor_y,
                beacon_distance=abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y),
            )
        )
        # print(sensors[-1], sensors[-1].x_coverage(), sensors[-1].y_coverage())


# search_timer = time.perf_counter()
goal: typ.Tuple[int, int] = None
for y in range(search_area_max + 1):
    # print(f"y: {y}")
    x_iterations = 0
    if goal is None:
        x = 0
        while x < search_area_max + 1:
            x_iterations += 1
            not_it = False
            # print(f"x: {x}")
            for sensor in sensors:
                distance = abs(sensor.x - x) + abs(sensor.y - y)
                if distance <= sensor.beacon_distance:
                    not_it = True
                    distance_to_row = abs(y - sensor.y)
                    horizontal_coverage = abs(sensor.beacon_distance - distance_to_row)
                    x = max(sensor.x + horizontal_coverage, x + 1)
                    break
            if not not_it:
                goal = (x, y)
                break
            x += 1
    # print(f"   x-iterations: {x_iterations}")
print(goal)
print(goal[0] * 4000000 + goal[1])
print(f"Elapsed time: {time.perf_counter() - start_time} s")
