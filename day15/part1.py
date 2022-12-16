input_file_name = "sample_input.txt"
row = 10
input_file_name = "input.txt"
row = 2000000
print("--------Part 1--------")

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

row_impossible_locations = []
for sensor in sensors:
    distance_to_row = abs(row - sensor.y)
    impossible_locations = [
        (x, row)
        for x in range(
            sensor.x - (sensor.beacon_distance - distance_to_row),
            sensor.x + (sensor.beacon_distance - distance_to_row),
        )
    ]
    # print(sensor, distance_to_row, impossible_locations)
    row_impossible_locations.extend(impossible_locations)

# print(sorted(set(row_impossible_locations)))
print(len(set(row_impossible_locations)))
print(f"Elapsed time: {time.perf_counter() - start_time} s")
