from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # решить задачу с помощью динамического программирования
    rows = n
    columns = m
    road = [[0] * columns for _ in range(rows)]
    road[0][0] = 1

    for column_index in range(columns - 1):
        road[0][column_index + 1] += road[0][column_index]

    for rows_index in range(rows - 1):
        road[rows_index + 1][0] += road[rows_index][0]

    for i in range(1, columns):
        for j in range(1, rows):
            road[j][i] += road[j - 1][i] + road[j][i - 1] + road[j - 1][i - 1]

    return road


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
