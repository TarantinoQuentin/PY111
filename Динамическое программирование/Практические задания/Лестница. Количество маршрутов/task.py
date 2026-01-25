from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    # найти количество маршрутов до каждой ступени
    if count_stairs < 0:
        raise ValueError
    if count_stairs == 0:
        return [0]
    if count_stairs == 1:
        return [0, 1]

    path = [0] * (count_stairs + 1)
    path[1] = 1

    for i in range(2, count_stairs + 1):
        path[i] = path[i - 1] + path[i - 2]

    return path


if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
