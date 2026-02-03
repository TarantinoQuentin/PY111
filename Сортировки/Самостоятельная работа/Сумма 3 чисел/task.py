from typing import List
from itertools import batched


def three_sum(nums: List[int]) -> List[List[int]]:

    # if len(nums) == 3 and sum(nums) == 0:
    #     return [nums]
    #
    # result = []
    # step_num_index = 0
    # for index, num in enumerate(nums):
    #     if index > len(nums) - 2:
    #         break
    #     if index == step_num_index:
    #         pass
    #     if nums[step_num_index] + num + nums[index + 1] == 0:
    #         result.append(nums[step_num_index])
    #         result.append(num)
    #         result.append(nums[index + 1])
    #
    # result = [list(batch) for batch in batched(result, 3)]
    # return result


# Решение учителя:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return result