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
    #     n = 0
    #     sinx_result = 0
    #     while True:
    #         step_action = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
    #         sinx_result += step_action
    #         n += 1
    #
    #         if abs(step_action) <= DELTA:
    #             return sinx_result
    n = 0
    pow_term = -1
    second_pow_term = x
    factorial_term = 2 * n + 1
    sinx_result = 0
    while True:
        for _ in range(n):
            pow_term *= pow_term
        for _ in range(2 * n + 1):
            second_pow_term *= second_pow_term
        for i in range(1, factorial_term):
            factorial_term *= i

        step_action = pow_term * second_pow_term / factorial_term
        sinx_result += step_action
        n += 1

        if abs(step_action) <= DELTA:
            return sinx_result
