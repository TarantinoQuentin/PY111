from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    # реализовать итеративный алгоритм бинарного поиска
    left_border = 0
    right_border = len(seq) - 1

    while True:
        if left_border > right_border:
            raise ValueError('Искомого элемента нет в последовательности')
        middle_index = left_border + (right_border - left_border) // 2
        if value == seq[middle_index]:
            while 0 <= middle_index - 1 < len(seq) and seq[middle_index - 1] == value:
                middle_index -= 1
            return middle_index
        elif value > seq[middle_index]:
            left_border = middle_index + 1
        else:
            right_border = middle_index - 1
