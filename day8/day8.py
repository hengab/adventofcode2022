rows = []
columns = []


def is_taller_than(value, other_values):
    return max(other_values) < value


def scenic_score(value, other_values):
    for i in range(0, len(other_values)):
        if other_values[i] >= value:
            return i + 1

    return len(other_values)


# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        rows.append(line.strip())

row_count = len(rows)
for i in range(row_count):
    columns.append("".join([row[i] for row in rows]))
column_count = len(columns)

visible = row_count * 2 + (column_count - 2) * 2
max_scenic_score = 0
for row_index in range(1, row_count - 1):
    for column_index in range(1, column_count - 1):
        if (
            is_taller_than(
                rows[row_index][column_index], rows[row_index][0:column_index]
            )
            or is_taller_than(
                rows[row_index][column_index],
                rows[row_index][column_index + 1 : column_count],
            )
            or is_taller_than(
                rows[row_index][column_index], columns[column_index][0:row_index]
            )
            or is_taller_than(
                rows[row_index][column_index],
                columns[column_index][row_index + 1 : row_count],
            )
        ):
            visible = visible + 1

        max_scenic_score = max(
            [
                max_scenic_score,
                scenic_score(
                    rows[row_index][column_index], rows[row_index][0:column_index][::-1]
                )
                * scenic_score(
                    rows[row_index][column_index],
                    rows[row_index][column_index + 1 : column_count],
                )
                * scenic_score(
                    rows[row_index][column_index],
                    columns[column_index][0:row_index][::-1],
                )
                * scenic_score(
                    rows[row_index][column_index],
                    columns[column_index][row_index + 1 : row_count],
                ),
            ]
        )


print(f"Visible: {visible}")
print(f"Max Scenic Score: {max_scenic_score}")
