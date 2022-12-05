import typing as typ


def parse_assignments(line: str) -> typ.Tuple[typ.Tuple[int, int], typ.Tuple[int, int]]:
    sections = line.split(",")
    elf_1 = sections[0].split("-")
    elf_2 = sections[1].split("-")

    return ((int(elf_1[0]), int(elf_1[1])), (int(elf_2[0]), int(elf_2[1])))


def fully_contained(elf_1: typ.Tuple[int, int], elf_2: typ.Tuple[int, int]) -> bool:
    return elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]


def overlap(elf_1: typ.Tuple[int, int], elf_2: typ.Tuple[int, int]) -> bool:
    return elf_1[0] <= elf_2[1] and elf_1[1] >= elf_2[0]


fully_contained_count = 0
overlap_count = 0
# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    for line in input_file.readlines():
        elf_1, elf_2 = parse_assignments(line)
        if fully_contained(elf_1, elf_2) or fully_contained(elf_2, elf_1):
            fully_contained_count = fully_contained_count + 1

        if overlap(elf_1, elf_2) or overlap(elf_2, elf_1):
            overlap_count = overlap_count + 1

print(fully_contained_count)
print(overlap_count)
