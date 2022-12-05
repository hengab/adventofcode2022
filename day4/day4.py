import typing as typ


def parse_assignments(line: str) -> typ.Tuple[typ.Tuple[int, int], typ.Tuple[int, int]]:
    sections = line.split(",")
    elf_1 = sections[0].split("-")
    elf_2 = sections[1].split("-")

    return ((int(elf_1[0]), int(elf_1[1])), (int(elf_2[0]), int(elf_2[1])))


fully_contained = 0
overlap = 0
# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    for line in input_file.readlines():
        elf_1, elf_2 = parse_assignments(line)
        if (elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]) or (
            elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]
        ):
            fully_contained = fully_contained + 1
        
        if (elf_1[0] <= elf_2[1] and elf_1[1] >= elf_2[0]) or (
            elf_2[0] <= elf_1[1] and elf_2[1] >= elf_1[0]
        ):
            overlap = overlap + 1

print(fully_contained)
print(overlap)
