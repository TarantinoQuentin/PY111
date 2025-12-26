from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    # вычислить sin(x) с помощью разложения сумму бесконечного ряда
    n = 0
    sinx_result = 0
    while True:
        step_action = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
        sinx_result += step_action
        n += 1

        if abs(step_action) <= DELTA:
            return sinx_result
