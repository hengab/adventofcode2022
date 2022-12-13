# input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 2--------")

import typing as typ
import dataclasses
import string
import sys


@dataclasses.dataclass
class Coordinate(object):
    x: int
    y: int


@dataclasses.dataclass
class Node(object):
    coordinate: Coordinate
    elevation: str
    shortest_path: int = sys.maxsize

    def elevation_score(self) -> int:
        return string.ascii_lowercase.index(self.elevation)

    def explore(
        self,
        x_oob: int,
        y_oob: int,
        depth: int = 0,
    ) -> None:
        if depth >= self.shortest_path:
            # We have already found a shorter path to this node
            return
        else:
            self.shortest_path = depth

        if self.coordinate == end.coordinate:
            # Found the end
            return

        candidates: typ.List[Node] = []

        candidates.extend(
            [
                map[x][self.coordinate.y]
                for x in [self.coordinate.x - 1, self.coordinate.x + 1]
                if x > -1 and x < x_oob
            ]
        )

        candidates.extend(
            [
                map[self.coordinate.x][y]
                for y in [self.coordinate.y - 1, self.coordinate.y + 1]
                if y > -1 and y < y_oob
            ]
        )

        for candidate in candidates:
            if candidate.elevation_score() - self.elevation_score() < 2:
                candidate.explore(x_oob, y_oob, depth + 1)

        return


map: typ.List[typ.List[Node]] = []
starts: typ.List[Node] = []
end: Node
with open(input_file_name) as input_file:
    lines = input_file.readlines()

y = len(lines) - 1
for line in lines:
    line = line.strip()
    for x in range(len(line)):
        if len(map) < x + 1:
            map.append([])
        candidate = Node(Coordinate(x, y), line[x])
        if candidate.elevation == "a":
            starts.append(candidate)
        if candidate.elevation == "S":
            candidate.elevation = "a"
            starts.append(candidate)
        elif candidate.elevation == "E":
            candidate.elevation = "z"
            end = candidate
        map[x].insert(0, candidate)
    y -= 1


x_oob = len(map)
y_oob = len(map[0])

for start in starts:
    start.explore(x_oob, y_oob)

print(end.shortest_path)
