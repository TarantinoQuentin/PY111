from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализуйте сортировку слиянием
    def merge(left: list[int], right: list[int]) -> list[int]:
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
        while True:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
            if not left:
                result.extend(right)
                break
            if not right:
                result.extend(left)
                break
        return result

    if len(container) < 2:
        return  container

    middle_index = len(container) // 2
    left_part = container[:middle_index]
    right_part = container[middle_index:]

    sort_left_container = sort(left_part)
    sort_right_container = sort(right_part)

    return merge(sort_left_container, sort_right_container)
