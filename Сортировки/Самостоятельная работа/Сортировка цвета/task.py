from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """

    nums_length = len(nums)
    while True:
        changed = False
        for i in range(nums_length + 1):
            if i > nums_length - 2:
                break
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                changed = True
        if not changed:
            break
        nums_length -= 1

# tt = [2,0,2,1,1,0]
# sort_сolors(tt)
# print(tt)

# Решение учителя:
# low, mid, high = 0, 0, len(nums) - 1
# while mid <= high:
#     if nums[mid] == 0:
#         nums[low], nums[mid] = nums[mid], nums[low]
#         low += 1
#         mid += 1
#     elif nums[mid] == 1:
#         mid += 1
#     else:
#         nums[mid], nums[high] = nums[high], nums[mid]
#         high -= 1