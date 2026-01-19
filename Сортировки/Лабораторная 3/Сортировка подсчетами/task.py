from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализовать алгоритм сортировки подсчетами
    if len(container) < 2:
        return container

    last_element = max(container)
    counted_numbers = {number: 0 for number in range(last_element + 1)}

    for number in container:
        counted_numbers[number] += 1

    result = []
    for number in counted_numbers:
        for i in range(counted_numbers[number]):
            result.append(number)

    return result
