from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = [[0] * n for _ in range(m)]
    ans = 0

    # Не смог решить, решение из интернета:
    def dfs(i, j):
        # реализовать поиск в глубину

        # Если мы уже считали путь для этой клетки, возвращаем его
        if dp[i][j]:
            return dp[i][j]

        best = 1  # Минимальная длина пути - сама эта клетка

        for dx, dy in directions:
            x, y = i + dx, j + dy
            # Проверяем границы и условие возрастания
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                best = max(best, 1 + dfs(x, y))

        dp[i][j] = best  # Запоминаем результат
        return best

    # Решение преподавателя:
    # def dfs(i, j):
    #     if not dp[i][j]:
    #         for dx, dy in directions:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 dp[i][j] = max(dp[i][j], dfs(x, y))
    #         dp[i][j] += 1
    #     return dp[i][j]

    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))

    return ans
