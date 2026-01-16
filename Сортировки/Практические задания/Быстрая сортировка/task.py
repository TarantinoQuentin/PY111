from typing import List


def partition(arr: list, low: int, high: int):
    pivot = arr[high]

    left_edge_index = low - 1

    for checking_index in range(low, high):
        if arr[checking_index] <= pivot:
            left_edge_index += 1
            arr[left_edge_index], arr[checking_index] = arr[checking_index], arr[left_edge_index]

    arr[left_edge_index + 1], arr[high] = arr[high], arr[left_edge_index + 1]

    return left_edge_index + 1

def quick_sort(arr: list, low: int = 0, high: int | None = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    # реализовать алгоритм быстрой сортировки

    if not container:
        return container

    quick_sort(container)

    return container

# Решение создателя теста:

#     if not container:
#         return container
#
#     pivot = container[0]
#     return (
#             sort([item for item in container if item < pivot]) +
#             [item for item in container if item == pivot] +
#             sort([item for item in container if item > pivot])
#     )

# Чем оно плохо? Алгоритм быстрой сортировки в классическом виде хорош тем,
# что работает "in place", не затрачивая дополнительную память на копирование кусков
# массива, но в данном случае через list comprehension мы его дублируем аж три раза,
# неоправданно затрачивая на это лишнюю память.
