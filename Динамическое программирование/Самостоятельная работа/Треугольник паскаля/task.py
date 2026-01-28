from typing import List


def generate(num_rows: int) -> List[List[int]]:

    # Не смог решить, решение учителя:
    if num_rows == 0:
        return []
    triangle = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
