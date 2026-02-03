from functools import lru_cache


def unique_paths(m: int, n: int) -> int:

    @lru_cache()
    def get_move(rows, cols):

        if rows == 0 and cols == 0:
            return 1

        if rows < 0 or cols < 0:
            return 0

        return get_move(rows - 1, cols) + get_move(rows, cols - 1)

    return get_move(m - 1, n - 1)

# Решение учителя:
# def unique_paths(m: int, n: int) -> int:
#     dp = [[0] * n for _ in range(m)]
#     for i in range(m):
#         dp[i][0] = 1
#     for j in range(n):
#         dp[0][j] = 1
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#     return dp[m - 1][n - 1]
