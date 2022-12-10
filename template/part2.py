# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        ...

