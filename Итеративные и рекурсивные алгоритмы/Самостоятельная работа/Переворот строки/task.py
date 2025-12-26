from typing import List


def reverse_string(s: List[str]) -> None:
    list_copy = s.copy()
    list_range = len(s)
    s.clear()
    for i in range(list_range):
        s.append(list_copy[list_range - 1])
        list_range -= 1

    # left_edge, right_edge = 0, len(s) - 1
    # while left_edge < right_edge:
    #     s[left_edge], s[right_edge] = s[right_edge], s[left_edge]
    #     left_edge, right_edge = left_edge + 1, right_edge - 1
