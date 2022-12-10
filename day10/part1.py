import typing as typ
# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

cycles: typ.Dict[int, int] = {1: 1}
current_cycle = 1

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

total = cycles[20] * 20 + cycles[60] * 60 + cycles[100] * 100 + cycles[140] * 140 + cycles[180] * 180 + cycles[220] * 220
print(f"Total Signal Strength: {total}")