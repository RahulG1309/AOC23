import copy
from typing import List

DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]


def get_matrix_row(raw_string: str) -> List[str]:
    row = [raw_string[0]]

    for i in range(1, len(raw_string)):
        cur = raw_string[i]
        prev = row[-1]

        if cur.isdigit():
            if prev.isdigit():
                row.append(prev + cur)  # Build up the number
                row[-2] = "x"
                continue

        row.append(cur)
    return row


def get_adjacent_parts(matrix: List[List[str]]) -> List[str]:
    m, n = len(matrix), len(matrix[0])
    part_nums = []

    for i in range(m):
        for j in range(n):
            if (
                matrix[i][j] != "."
                and matrix[i][j] != "x"
                and not matrix[i][j].isdigit()
            ):
                for di, dj in DIRECTIONS:
                    i_new, j_new = i + di, j + dj

                    if i_new >= 0 and i_new < m and j_new >= 0 and j_new < n:
                        # There may either be a number or period at the end of the x trail
                        while matrix[i_new][j_new] == "x" and j_new < m:
                            j_new += 1

                        if matrix[i_new][j_new].isdigit():
                            part_nums.append(int(matrix[i_new][j_new]))
                            matrix[i_new][j_new] = "."
    return part_nums


def get_gear_ratios(matrix: List[List[str]]) -> List[str]:
    m, n = len(matrix), len(matrix[0])
    gear_ratios = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "*":
                adj_parts = []

                for di, dj in DIRECTIONS:
                    i_new, j_new = i + di, j + dj

                    if i_new >= 0 and i_new < m and j_new >= 0 and j_new < n:
                        # There may either be a number or period at the end of the x trail
                        while matrix[i_new][j_new] == "x" and j_new < m:
                            j_new += 1

                        if matrix[i_new][j_new].isdigit():
                            adj_parts.append(int(matrix[i_new][j_new]))
                            matrix[i_new][j_new] = "."

                if len(adj_parts) == 2:
                    gear_ratios.append(int(adj_parts[0]) * int(adj_parts[1]))

    return gear_ratios


if __name__ == "__main__":
    matrix = []

    with open("input.txt", "r", encoding="UTF-8") as file:
        while line := file.readline():
            row = get_matrix_row(line.rstrip())
            matrix.append(row)

    # These functions modify the input matrix inplace
    part_nums = get_adjacent_parts(copy.deepcopy(matrix))
    print(f"Sum of adjacent part numbers = {sum(part_nums)}")

    # These functions modify the input matrix inplace
    gear_ratios = get_gear_ratios(copy.deepcopy(matrix))
    print(f"Sum of gear ratios = {sum(gear_ratios)}")
