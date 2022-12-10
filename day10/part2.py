import typing as typ
# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

cycles: typ.Dict[int, int] = {1: 1}
current_cycle = 1

def print_crt(crt: typ.List[str], sprite_position, cycle) -> typ.List[str]:
    if cycle in sprite_position:
        crt.append("#")
    else:
        crt.append(".")

    return crt


with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()        

        command_line = line.split()

        if len(command_line) > 1:
            # addx
            instruction, value = command_line
            cycles[current_cycle + 1] = cycles[current_cycle]            
            cycles[current_cycle + 2] = cycles[current_cycle] + int(value)
            current_cycle = current_cycle + 2
        else:
            # noop
            cycles[current_cycle + 1] = cycles[current_cycle]
            current_cycle = current_cycle + 1


crt = []
for cycle, cycle_value in cycles.items():
    sprite_position = [i for i in range(cycle_value-1, cycle_value + 2)]
    crt_position = (cycle - 1) % 40
    crt = print_crt(crt, sprite_position, crt_position)
    # print(f"{cycle}: {cycle_value} - {sprite_position} {''.join(crt)} {len(crt)}")


print("".join(crt[0:40]))
print("".join(crt[40:80]))
print("".join(crt[80:120]))
print("".join(crt[120:160]))
print("".join(crt[160:200]))
print("".join(crt[200:240]))


###..###..####..##..###...##..####..##..
#..#.#..#....#.#..#.#..#.#..#....#.#..#.
#..#.###....#..#....#..#.#..#...#..#..#.
###..#..#..#...#.##.###..####..#...####.
#....#..#.#....#..#.#.#..#..#.#....#..#.
#....###..####..###.#..#.#..#.####.#..#.