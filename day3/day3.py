import string
import typing as typ


def groups(input: typ.Iterable) -> typ.Generator[typ.Tuple[str, str, str], None, None]:
    for i in range(0, len(input), 3):
        yield input[i : i + 3]


def item_priority(item: str) -> int:
    return (
        string.ascii_lowercase.index(item) + 1
        if item in string.ascii_lowercase
        else string.ascii_uppercase.index(item) + 27
    )


priority = 0
group_priority = 0

# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    for group in groups(input_file.readlines()):
        group_item = next(
            item for item in group[0] if item in group[1] and item in group[2]
        )
        group_priority = group_priority + item_priority(group_item)
        for line in group:
            if line.strip() != "":
                compartment_1 = line[: len(line) // 2]
                compartment_2 = line[len(line) // 2 :]

                item = next(item for item in compartment_1 if item in compartment_2)
                priority = priority + item_priority(item)

    print(f"Priority: {priority}")
    print(f"Group Priority: {group_priority}")
