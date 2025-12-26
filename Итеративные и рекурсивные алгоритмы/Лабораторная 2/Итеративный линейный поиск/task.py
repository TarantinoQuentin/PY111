"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # реализовать итеративный линейный поиск
    if not arr:
        raise ValueError('Передана пустая последовательность')
    target_index = 0
    target = arr[target_index]
    for index, value in enumerate(arr):
        if value < target:
            target = value
            target_index = index
    return target_index
