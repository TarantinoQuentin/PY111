from typing import List

from fontTools.misc.cython import returns


# def longest_common_prefix(strs: List[str]) -> str:
#
#     if len(strs) < 1:
#         return ''
#
#     if len(strs) == 1:
#         return strs[0]
#
#     template = {char: index for index, char in enumerate(strs[0])}
#     count_matching = float('inf')
#     for string in strs[1:]:
#         current_matching = 0
#         for index, char in enumerate(string):
#             if char in template:
#                 if index == template[char]:
#                     current_matching += 1
#         count_matching = min(count_matching, current_matching)
#     result = list(template.keys())
#     result = result[:count_matching]
#     result = ''.join(result)
#     return result


# Решение учителя:
# def longest_common_prefix(strs: List[str]) -> str:
#     if not strs:
#         return ""
#     if len(strs) == 1:
#         return strs[0]
#
#     strs.sort()
#     prefix = ""
#     for i in range(len(strs[0])):
#         if strs[0][i] == strs[-1][i]:
#             prefix += strs[0][i]
#         else:
#             break
#     return prefix


# Решение из сети:
# def longest_common_prefix(strs: list[str]) -> str:
#     if not strs:
#         return ""
#
#     prefix = ""
#     # zip(*strs) берет i-й символ из каждой строки и упаковывает в кортеж
#     for chars in zip(*strs):
#         # Если в сете только 1 элемент, значит символ одинаковый у всех строк
#         if len(set(chars)) == 1:
#             prefix += chars[0]
#         else:
#             break
#
#     return prefix


# Еще одно:
# def longest_common_prefix(strs: list[str]) -> str:
#     if not strs:
#         return ""
#
#     # Итерируемся по символам первой строки
#     for i, chars in enumerate(zip(*strs)):
#         # Если в сете больше 1 символа — всё, префикс кончился
#         if len(set(chars)) > 1:
#             return strs[0][:i]
#
#     # Если цикл прошел до конца, значит самая короткая строка и есть префикс
#     return min(strs, key=len)