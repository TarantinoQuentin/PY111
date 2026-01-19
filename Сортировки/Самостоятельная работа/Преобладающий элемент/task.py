from typing import List


def majority_element(nums: List[int]) -> int|None:

    if not nums:
        return None

    last_element = max(nums)
    counted_numbers = {number: 0 for number in range(last_element + 1)}

    for number in nums:
        counted_numbers[number] += 1

    superior = list(counted_numbers.keys())[0]
    for number in counted_numbers:
        if counted_numbers[number] > counted_numbers[superior]:
            superior = list(counted_numbers.keys())[number]

    return superior

    # Решение учителя:
    # count = 0
    # candidate = None
    #
    # for num in nums:
    #     if count == 0:
    #         candidate = num
    #     count += (1 if num == candidate else -1)
    #
    # return candidate
