from typing import Hashable, List
from collections import deque

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    # реализовать обход в глубину итеративным способом

    visited = {node: False for node in g.nodes}
    deque_ = deque()
    path = []

    deque_.append(start_node)
    visited[start_node] = True

    while deque_:
        current_node = deque_.pop()
        path.append(current_node)
        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                deque_.append(neighbor)
                visited[neighbor] = True

    return path
