"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди — первый элемент (0), конец — последний (-1)
        """
        # инициализировать список
        self.queue = []

    def enqueue(self, elem: Any) -> None:  # O(I)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        # реализовать метод enqueue
        self.queue.append(elem)

    def dequeue(self) -> Any:  # O(I)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # реализовать метод dequeue
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError('Ошибка, очередь пуста')

    def peek(self, ind: int = 0) -> Any:  # O(I)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError('Указан не целочисленный тип индекса')
        if not 0 <= ind < len(self.queue):
            raise IndexError('Индекс вне границ очереди')
        return self.queue[ind]

    def clear(self) -> None:  # O(I)
        """ Очистка очереди. """
        # реализовать метод clear
        self.queue.clear()

    def __len__(self):  # O(N)
        """ Количество элементов в очереди. """
        # реализовать метод __len__
        total_len = 0
        for _ in self.queue:
            total_len += 1
        return total_len
