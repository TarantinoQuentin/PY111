from typing import List


def sort_len(container: list[str]) -> list[str]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    # реализуйте сортировку слиянием
    def merge(left: list[str], right: list[str]) -> list[str]:
        """
        Алгоритм для слияния левой и правой части, сравнивает
        первые элементы из каждого массива и в итоговый массив записывает наименьшее,
        в массиве, в котором был наименьший элемент, переходит к следующему,
        когда один из массивов закончится, остаток второго «сливает» в итоговый массив

        :param left: левая часть
        :param right: правая часть
        :return: слитый список
        """

        result = []
        left_len = right_len = 0

        while left_len < len(left) and right_len < len(right):
            if len(left[left_len]) > len(right[right_len]):
                result.append(left[left_len])
                left_len += 1
            else:
                result.append(right[right_len])
                right_len += 1

        result.extend(left[left_len:])
        result.extend(right[right_len:])
        return result

    if len(container) < 2:
        return container

    middle_index = len(container) // 2
    left_part = sort_len(container[:middle_index])
    right_part = sort_len(container[middle_index:])

    return merge(left_part, right_part)


def is_subsequence(a: str, b: str) -> bool:
    index_count_a, index_count_b = 0, 0
    while index_count_a < len(a) and index_count_b < len(b):
        if a[index_count_a] == b[index_count_b]:
            index_count_a += 1
        index_count_b += 1
    return index_count_a == len(a)


def find_lus_length(strs: List[str]) -> int:

    strs_sorted_len = sort_len(strs)

    # Решить не смог, решение учителя:
    for index, value in enumerate(strs_sorted_len):
        is_unique = True
        for step in range(len(strs_sorted_len)):
            if index == step:
                continue
            if is_subsequence(strs_sorted_len[step], value):
                is_unique = False
                break
        if is_unique:
            return len(value)
    return -1
