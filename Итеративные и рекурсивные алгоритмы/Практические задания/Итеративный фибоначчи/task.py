def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    # написать итеративный алгоритм чисел Фибоначчи
    if n < 0:
        raise ValueError('Должен быть передан положительный номер числа')
    if n in (0, 1):
        return n

    first_number, second_number = 0, 1
    iteration_count = len([first_number, second_number])
    while True:
        result = first_number + second_number

        if iteration_count == n:
            return result

        first_number, second_number = second_number, result
        iteration_count += 1
