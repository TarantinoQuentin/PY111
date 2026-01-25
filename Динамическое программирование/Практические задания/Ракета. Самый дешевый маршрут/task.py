from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    # рассчитать таблицу стоимостей перемещений
    table = table.copy()
    rows = len(table)
    columns = len(table[0])

    for row_index in range(rows - 1):
        table[row_index + 1][0] += table[row_index][0]

    for column_index in range(columns - 1):
        table[0][column_index + 1] += table[0][column_index]

    for i in range(1, rows):
        for j in range(1, columns):
            table[i][j] += min(table[i - 1][j], table[i][j - 1])

    return table


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
