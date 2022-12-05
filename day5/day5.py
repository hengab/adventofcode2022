import typing as typ

stacks: typ.Dict[int, typ.List[str]] = {}
lines: typ.List[str] = []


def process_command_9000(line: str):
    # move {move_count} from {from_stack_id} to {to_stack_id}
    command_parts = line.split()
    move_count = int(command_parts[1])
    from_stack_id = int(command_parts[3])
    to_stack_id = int(command_parts[5])

    for i in range(move_count):
        item = stacks[from_stack_id].pop()
        stacks[to_stack_id].append(item)


def process_command_9001(line: str):
    # move {move_count} from {from_stack_id} to {to_stack_id}
    command_parts = line.split()
    move_count = int(command_parts[1])
    from_stack_id = int(command_parts[3])
    to_stack_id = int(command_parts[5])

    buffer = []
    for i in range(move_count):
        item = stacks[from_stack_id].pop()
        buffer.append(item)

    while len(buffer) > 0:
        item = buffer.pop()
        stacks[to_stack_id].append(item)


# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    line = input_file.readline()
    while line.strip() != "":
        lines.insert(0, line.strip("\n"))
        line = input_file.readline()

    stack_defs = lines[0].split("   ")
    lines.remove(lines[0])

    for stack_def in stack_defs:
        stacks[int(stack_def.strip())] = []

    for line_content in lines:

        for stack in range(len(stack_defs)):
            stack_item = line_content[(stack * 4 + 1)].strip()
            if stack_item != "":
                stacks[stack + 1].append(stack_item)

    for line in input_file.readlines():
        line = line.strip()
        # print(line)
        if line != "":
            process_command_9001(line)

result: str = ""
for stack_id, stack in stacks.items():
    result = result + stack[-1]

print(f"Stacks: {stacks}")
print(f"Result: {result}")
