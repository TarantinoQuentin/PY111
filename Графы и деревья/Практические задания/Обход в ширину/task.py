from logging import currentframe
from typing import Hashable, List
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    # реализовать обход в ширину
    visited = {node: False for node in g.nodes}
    our_deque = deque()
    path = []

    our_deque.append(start_node)
    visited[start_node] = True

    while our_deque:
        current_node = our_deque.popleft()
        path.append(current_node)
        for neighbor in g.neighbors(current_node):  # g[current_node]
            if not visited[neighbor]:
                our_deque.append(neighbor)
                visited[neighbor] = True

    return path


if __name__ == '__main__':
    # записать граф с помощью модуля networkx и проверить обход в ширину
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'J'),
        ('H', 'E'),
        ('H', 'D'),
        ('E', 'D'),
    ])

    print(bfs(graph, "A"))
    # nx.draw_networkx(graph)
    # plt.show()
