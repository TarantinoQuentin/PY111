from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    suitable_numbers = {}
    for index, number in enumerate(nums):
        if number <= target:
            if number in suitable_numbers and number * 2 == target:
                return [suitable_numbers[number], index]
            suitable_numbers[number] = index
    result = []
    first_term_index = 0
    for index, suitable_num in enumerate(suitable_numbers):
        first_term = list(suitable_numbers.keys())[first_term_index]
        if index == first_term_index:
            continue
        if suitable_num + first_term == target:
            result.append(suitable_numbers[suitable_num])
            result.append(suitable_numbers[first_term])
            return result
        first_term_index += 1
        if first_term_index >= len(suitable_numbers):
            raise ValueError('Слогаемых нет')

