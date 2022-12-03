import typing as typ


with open("input.txt") as input_file:
    lines = input_file.readlines()

elf_items: typ.Dict[int, typ.List[int]] = {}
elf = 0
print(lines)
for line in lines:
    if line.strip() == "":
        elf = elf + 1
        continue

    elf_items[elf] = elf_items.get(elf, []) + [int(line.strip())]


elf_calories = sorted([sum(items) for elf, items in elf_items.items()])
elf_calories_as_str = [f"{items}\n" for items in elf_calories]
top_three = sum(elf_calories[-3:])

with open("result.txt", "w") as output_file:
    output_file.write(f"Total Elves: {elf + 1}\n")
    output_file.write(f"Top Elf Calories: {elf_calories[-1]}\n")
    output_file.write(f"Top Three Elf Calories: {top_three}\n")
    output_file.write(f"Calorie Count:\n")
    output_file.writelines(elf_calories_as_str)
