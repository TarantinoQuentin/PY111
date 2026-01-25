from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # реализовать ленивую динамику

    @lru_cache()
    def stairway_cost_counting(n):

        if n == 0 or n == 1:
            return stairway[n]
        return stairway[n] + min(stairway_cost_counting(n - 1), stairway_cost_counting(n - 2))

    return stairway_cost_counting(len(stairway) - 1)


if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
