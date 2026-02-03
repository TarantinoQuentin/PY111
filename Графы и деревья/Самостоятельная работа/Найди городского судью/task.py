from typing import List


def find_judge(n: int, trust: List[List[int]]) -> int:

    # if not trust:
    #     return n

    # population_census = {citizen: 0 for trust_block in trust for citizen in trust_block}
    population_census = {citizen: 0 for citizen in range(1, n + 1)}

    for chain in trust:
        population_census[chain[0]] -= 1
        population_census[chain[1]] += 1
    for citizen, score in population_census.items():
        if score == n - 1:
            return citizen
    return -1


# Решение преподавателя:
# def find_judge(n: int, trust: List[List[int]]) -> int:
#     if n == 1:
#         return 1
#
#     trust_count = [0] * (n + 1)
#
#     for i, j in trust:
#         trust_count[i] -= 1
#         trust_count[j] += 1
#
#     for i in range(1, n + 1):
#         if trust_count[i] == n - 1:
#             return i
#
#     return -1
