from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Time O(m*n), Memory O(m*n)
        m, n = len(matrix), len(matrix[0])
        dp = [[None] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            p1 = p2 = p3 = p4 = 0
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                p1 = dfs(i + 1, j)
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                p2 = dfs(i - 1, j)
            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                p3 = dfs(i, j + 1)
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                p4 = dfs(i, j - 1)

            dp[i][j] = 1 + max(p1, p2, p3, p4)
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return max(max(d) for d in dp)
