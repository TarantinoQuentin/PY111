from typing import List


def contains_duplicate(nums: List[int]) -> bool:

    if not nums:
        return False

    last_element = max(nums)
    counted_numbers = {number: 0 for number in range(last_element + 1)}

    for number in nums:
        counted_numbers[number] += 1
        if counted_numbers[number] > 1:
            return True

    return False

    # Решение учителя:
    # return len(nums) > len(set(nums))
