from typing import Union
from itertools import count
from math import factorial, sin
from timeit import timeit


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

    # ==================================================================================

    # Альтернативное решение без использования функций factorial,
    # pow и оператора **:

    # n = 0
    # sin_x = 0
    # while True:
    #     taylors_key_term = 2 * n + 1
    #     sign_term = -1 if (n + 1) % 2 == 0 else 1
    #     pow_term = 1
    #     factorial_term = 1
    #
    #     for i in range(1, taylors_key_term + 1):
    #         pow_term *= x
    #         factorial_term *= i
    #
    #     step_action = sign_term * pow_term / factorial_term
    #     sin_x += step_action
    #
    #     if abs(step_action) <= DELTA:
    #             return sin_x
    #
    #     n += 1

    # ==================================================================================

    # Решение учителя без использования функций factorial,
    # pow и оператора **:

    delta_step = DELTA + 1
    square_x = x * x  # Просто константа, так как много где используется в ряде.
    sin_x = x  # Начальная сумма, так как по ряду первое слагаемое это x.
    pow_term = x  # Начальная часть для степенной функции x ** (2n - 1), т.е x, x ** 3, x ** 5, ...
    factorial_term = 1  # Начальная часть для факториала.
    sign_term = 1  # Начальный знак для ряда (1 * -1 = -1; -1 * -1 = 1).
    i = 1  # Шаг для последовательности.

    while abs(delta_step) > DELTA:
        sign_term *= -1
        pow_term *= square_x
        factorial_term *= 2 * i * (2 * i + 1)
        delta_step = sign_term * pow_term / factorial_term
        sin_x += delta_step
        i += 1
    return sin_x


# Код преподавателя для сравнения быстродействия функций, сравниваем функцию с использованием
# функций factorial, pow и оператора **, с вариантом преподавателя:

# if __name__ == '__main__':
#     x = 10
#     number_step = 100000
#
#     print(f'Отклонение: {sin(x) - sinx1(x):.8f}')  # -0.00000005
#     print(f'Отклонение: {sin(x) - sinx2(x):.8f}')  # -0.00000005
#     print(f"Time 1 для {number_step} итераций = {timeit('sinx1(x)', globals=globals(), number=number_step)}")
#     print(f"Time 2 для {number_step} итераций = {timeit('sinx2(x)', globals=globals(), number=number_step)}")
