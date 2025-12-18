"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        # использовать deque для реализации очереди с приоритетами
        self.data = {key:deque() for key in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        # реализовать метод enqueue
        self.data[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # реализовать метод dequeue
        for deq in self.data.values():
            if deq:
                return deq.popleft()
        raise IndexError()


    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError()

        deq = self.data[priority]

        if not 0 <= ind <= len(deq):
            raise IndexError()

        return deq[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        # реализовать метод clear
        self.__init__()

    def __len__(self):
        """ Количество элементов в очереди. """
          # реализовать метод __len__
        total_len = 0
        for deq in self.data.values():
            total_len += len(deq)
        return total_len
