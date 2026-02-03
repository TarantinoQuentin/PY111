from typing import Hashable, Mapping, Union
import networkx as nx
from networkx.algorithms.shortest_paths.unweighted import predecessor
import heapq


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
    # вернуть стоимость путей до всех вершин посчитанных алгоритмом Дейкстры

    distance = {node: float('inf') for node in g.nodes}
    distance[starting_node] = 0
    predecessor_ = {node: None for node in g.nodes}

    queue = [(0, starting_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in g[current_node].items():
            distance_to_node = current_distance + weight['weight']
            if distance_to_node < distance[neighbor]:
                distance[neighbor] = distance_to_node
                predecessor_[neighbor] = current_node
                heapq.heappush(queue, (distance_to_node, neighbor))

    return distance


    # _, coasts = nx.dijkstra_predecessor_and_distance(g, starting_node)
    # for node in g.nodes:
    #     if node not in coasts:
    #         coasts[node] = float("inf")
    #
    # return coasts


if __name__ == '__main__':
    # записать граф
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 7),
        (1, 3, 9),
        (1, 6, 14),
        (2, 3, 10),
        (2, 4, 15),
        (3, 4, 11),
        (3, 6, 2),
        (4, 5, 6),
        (5, 6, 9),
    ])

    print(dijkstra_algo(graph, 1))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 26}
