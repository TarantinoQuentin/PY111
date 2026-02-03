from collections import defaultdict
import networkx as nx
import heapq


def network_delay_time(times, n, k):

    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, n + 1))
    graph.add_weighted_edges_from(times)

    time = {node: float('inf') for node in graph.nodes}
    start_node = k
    time[start_node] = 0

    queue = [(0, start_node)]

    while queue:
        current_time, current_node = heapq.heappop(queue)

        if current_time > time[current_node]:
            continue

        for next_node, data in graph[current_node].items():
            time_to_next = current_time + data['weight']
            if time_to_next < time[next_node]:
                time[next_node] = time_to_next
                heapq.heappush(queue, (time_to_next, next_node))

    max_time = max(time.values())

    return max_time if max_time != float('inf') else -1


# Решение учителя:
# def network_delay_time(times, n, k):
#     graph = defaultdict(list)
#     for u, v, w in times:
#         graph[u].append((v, w))
#
#     dist = [float('inf')] * (n + 1)
#     dist[k] = 0
#
#     queue = [(0, k)]
#     while queue:
#         curr_dist, curr = heapq.heappop(queue)
#         if curr_dist > dist[curr]:
#             continue
#         for neighbor, weight in graph[curr]:
#             if curr_dist + weight < dist[neighbor]:
#                 dist[neighbor] = curr_dist + weight
#                 heapq.heappush(queue, (dist[neighbor], neighbor))
#
#     max_time = max(dist[1:])
#     return max_time if max_time < float('inf') else -1
