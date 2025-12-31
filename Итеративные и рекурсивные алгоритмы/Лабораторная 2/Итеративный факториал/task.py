def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # реализовать итеративный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError('Факториал может быть посчитан только для натуральных чисел')
    elif n < 0:
        raise ValueError('Факториал может быть посчитан только для положительных числе')

    elif n == 0:
        return 1

    result = 1
    for i in range(1, n ):
        result *= i
    return result