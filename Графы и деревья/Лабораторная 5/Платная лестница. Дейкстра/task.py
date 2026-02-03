from typing import Union

import networkx as nx
import heapq


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # с помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    cost_log = {node: float('inf') for node in graph.nodes}
    starting_stair_step = 0
    cost_log[starting_stair_step] = 0

    queue = [(0, starting_stair_step)]

    while queue:
        current_cost, current_stair_step = heapq.heappop(queue)

        for next_stair_step, data in graph[current_stair_step].items():
            cost_to_next = current_cost + data['weight']
            if cost_to_next < cost_log[next_stair_step]:
                cost_log[next_stair_step] = cost_to_next
                heapq.heappush(queue, (cost_to_next, next_stair_step))

        last_step = max(graph.nodes)

    return cost_log[last_step]

    # Решение покороче через библиотеку nx:
    # starting_node = 0
    # _, coasts = nx.dijkstra_predecessor_and_distance(graph, starting_node)
    #
    # return max(coasts.values())



if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)


    def build_stairway_graph(stairway):

        edges = []
        stairway_length = len(stairway)

        for i in range(stairway_length):
            if i + 1 <= stairway_length:
                edges.append((i, i + 1, stairway[i]))
            if i + 2 <= stairway_length:
                edges.append((i, i + 2, stairway[i + 1]))

        return edges

    graph = nx.DiGraph()
    graph.add_weighted_edges_from(build_stairway_graph(stairway))

    stairway_graph = graph  # записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней


    print(stairway_path(stairway_graph))  # 72
