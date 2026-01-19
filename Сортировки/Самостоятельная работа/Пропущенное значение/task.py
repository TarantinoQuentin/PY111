from typing import List


def missing_number(nums: List[int]) -> int:

    last_element = len(nums)
    counted_numbers = {number: 0 for number in range(last_element + 1)}

    for number in nums:
        counted_numbers[number] += 1

    for number in counted_numbers:
        if counted_numbers[number] == 0:
            return number

    # Решение учителя:
    # n = len(nums)
    # return n * (n + 1) // 2 - sum(nums)
