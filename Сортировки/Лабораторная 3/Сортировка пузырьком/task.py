from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализовать алгоритм сортировки пузырьком

    if len(container) < 2:
        return container

    unsorted_length = len(container)
    while unsorted_length > 1:
        array_changed = False
        for i in range(unsorted_length - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                array_changed = True

        if not array_changed:
            break

        unsorted_length -= 1

    return container
