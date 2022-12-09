# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

import math

move_directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def move(current_position, direction):
    return (
        current_position[0] + direction[0],
        current_position[1] + direction[1],
    )


def distance(head_position, tail_position):
    d = math.sqrt(
        (head_position[0] - tail_position[0]) ** 2
        + (head_position[1] - tail_position[1]) ** 2
    )

    return d


def direction(head_position, tail_position):
    delta_x = head_position[0] - tail_position[0]
    delta_y = head_position[1] - tail_position[1]

    d = (
        int(delta_x / abs(delta_x)) if delta_x != 0 else 0,
        int(delta_y / abs(delta_y)) if delta_y != 0 else 0,
    )

    return d


def move_trailing_knot(head_position, tail_position):
    if distance(head_position, tail_position) > 1.4142135623730951:
        tail_move_direction = direction(head_position, tail_position)

        move_text = f"T   from {tail_position}"
        tail_position = move(tail_position, tail_move_direction)
        # print(f"{move_text} to {tail_position} using direction {tail_move_direction}")

    return tail_position


def make_moves(
    head_position,
    steps,
    head_move_direction,
    middle_knot_positions,
    tail_position,
    tail_positions,
):
    for _ in range(steps):
        move_text = f"H {line[0]} from {head_position}"
        head_position = move(head_position, head_move_direction)
        # print(f"{move_text} to {head_position} using direction {head_move_direction}")
        preceding_knot_position = head_position
        for i in range(len(middle_knot_positions)):
            middle_knot_positions[i] = move_trailing_knot(
                preceding_knot_position, middle_knot_positions[i]
            )
            preceding_knot_position = middle_knot_positions[i]

        tail_position = move_trailing_knot(preceding_knot_position, tail_position)
        tail_positions.append(tail_position)

    return head_position, middle_knot_positions, tail_position


head_position = (0, 0)
middle_knot_positions = []
tail_position = (0, 0)
tail_positions = []
# Initial position
tail_positions.append(tail_position)
with open(input_file_name) as input_file:
    line_no = 0
    for line in input_file.readlines():
        line_no = line_no + 1
        # print(f"--------{line_no}-{line}----------")
        line = line.strip()
        move_direction, length = line.split()
        head_move_direction = move_directions[move_direction]
        steps = int(length)

        head_position, middle_knot_positions, tail_position = make_moves(
            head_position,
            steps,
            head_move_direction,
            middle_knot_positions,
            tail_position,
            tail_positions,
        )

print(f"Part 1 Tail Positions: {len(tail_positions)} - Unique: {len(set(tail_positions))}")


head_position = (0, 0)
middle_knot_positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
tail_position = (0, 0)
tail_positions = []
# Initial position
tail_positions.append(tail_position)
with open(input_file_name) as input_file:
    line_no = 0
    for line in input_file.readlines():
        line_no = line_no + 1
        # print(f"--------{line_no}-{line}----------")
        line = line.strip()
        move_direction, length = line.split()
        head_move_direction = move_directions[move_direction]
        steps = int(length)

        head_position, middle_knot_positions, tail_position = make_moves(
            head_position,
            steps,
            head_move_direction,
            middle_knot_positions,
            tail_position,
            tail_positions,
        )

print(f"Part 2 Tail Positions: {len(tail_positions)} - Unique: {len(set(tail_positions))}")