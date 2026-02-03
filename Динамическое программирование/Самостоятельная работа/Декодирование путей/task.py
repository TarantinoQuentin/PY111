from functools import lru_cache


# def num_decodings(s: str) -> int:
#
#     @lru_cache
#     def get_bite(string):
#
#         if string == '':
#             return 1
#
#         variations = 0
#
#         if not int(string[-1]) == 0:
#             variations += get_bite(string[:-1])
#
#         if len(string) >= 2:
#             if not int(string[-2]) == 0 and 9 < int(string[-2:]) < 27:
#                 variations += get_bite(string[:-2])
#
#         return variations
#
#     return get_bite(s)


# Решение преподавателя:
# def num_decodings(s: str) -> int:
#     if not s:
#         return 0
#
#     n = len(s)
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     dp[1] = 1 if s[0] != '0' else 0
#
#     for i in range(2, n + 1):
#         if s[i - 1] != '0':
#             dp[i] += dp[i - 1]
#         if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
#             dp[i] += dp[i - 2]
#
#     return dp[n]


# Мое альтернативное с оптимизацией по памяти:
def num_decodings(s: str) -> int:

    if not s or s[0] == '0':
        return 0

    pre_prev = prev = 1

    for i in range(1, len(s)):

        curr = 0

        if s[i] != '0':
            curr += prev
        if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
            curr += pre_prev

        pre_prev, prev = prev, curr

        if prev == 0:
            return 0

    return prev

print(num_decodings("0"))