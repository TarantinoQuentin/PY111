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

    # n = 0
    # sinx_result = 0
    # while True:
    #     step_action = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
    #     sinx_result += step_action
    #     n += 1
    #
    #     if abs(step_action) <= DELTA:
    #         return sinx_result

    # Альтернативное решение без использования функций factorial,
    # pow и оператора **:

    n = 0
    sin_x = 0
    while True:
        eulers_key_term = 2 * n + 1
        sign_term = -1 if (n + 1) % 2 == 0 else 1
        pow_term = 1
        factorial_term = 1

        for i in range(1, eulers_key_term + 1):
            pow_term *= x
            factorial_term *= i

        step_action = sign_term * pow_term / factorial_term
        sin_x += step_action

        if abs(step_action) <= DELTA:
                return sin_x

        n += 1
