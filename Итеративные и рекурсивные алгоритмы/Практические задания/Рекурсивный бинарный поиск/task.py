from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None, step: int = -1
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма
    :param step: Шаг и направление поиска первого элемента, если искомых чисел несколько

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    # реализовать алгоритм бинарного поиска
    if right_border is None:
        right_border = len(seq) - 1

    if left_border > right_border:
        raise ValueError('Искомого элемента нет в последовательности')
    middle_index = left_border + (right_border - left_border) // 2
    if value == seq[middle_index]:
        while 0 <= middle_index + step < len(seq) and seq[middle_index + step] == value:
            middle_index += step
        return middle_index
    elif value > seq[middle_index]:
        left_border = middle_index + 1
    else:
        right_border = middle_index - 1
    return binary_search(value, seq, left_border, right_border)