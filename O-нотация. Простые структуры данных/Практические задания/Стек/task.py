from typing import Any


class Stack:
    def __init__(self):
        self._stack = []
        self.len = 0

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        # реализовать операцию push
        self._stack.append(elem)
        self.len += 1

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        # реализовать операцию pop
        if not self._stack:
            raise IndexError()
        else:
            self.len -= 1
            return self._stack.pop()


    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
          # реализовать операцию peek
        if not isinstance(ind, int):
            raise TypeError()
        if not 0 <= ind <= len(self._stack):
            raise IndexError()
        else:
            return self._stack[-ind - 1]

    def clear(self) -> None:
        """ Очистка стека. """
        # реализовать операцию clear
        self._stack.clear()
        self.len = 0

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        return self.len  # реализовать операцию __len__
