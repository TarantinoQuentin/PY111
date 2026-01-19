from typing import List


def maximum_gap(nums: List[int]) -> int:

    if len(nums) < 2:
        return 0

    unsorted_length = len(nums)
    while unsorted_length > 1:
        array_changed = False
        for i in range(unsorted_length - 1):
                if nums[i] > nums[i + 1]:
                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
                    array_changed = True
        unsorted_length -= 1

        if not array_changed:
            break

    max_gap = 0
    for i in range(len(nums) - 1):
        gap = nums[i + 1] - nums[i]
        if gap > max_gap:
            max_gap = gap

    return max_gap
