from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # реализовать прямой метод расчета
    cost = list(stairway[::])

    for i in range(2, len(cost)):
        cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

    return cost[-1]


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7
