from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:

    result = []
    if nums1 >= nums2:
        for num in nums2:
            if num in nums1:
                result.append(num)
    else:
        for num in nums1:
            if num in nums2:
                result.append(num)

    return list(set(result))

    # Решение учителя:
    # set1 = set(nums1)
    # set2 = set(nums2)
    # return list(set1 & set2)