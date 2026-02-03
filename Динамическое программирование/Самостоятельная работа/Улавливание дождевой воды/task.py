from typing import List


def trap(height: List[int]) -> int:

    # Не смог решить, решение учителя:
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    res = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1
    return res
