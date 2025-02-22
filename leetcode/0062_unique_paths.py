class Solution:
    # bottom up dp - memory efficient
    def uniquePaths(self, m: int, n: int) -> int:
        # Time O(m*n), Memory O(n)
        prev_row = [0] * n
        for _ in range(m - 1, -1, -1):
            curr_row = [0] * n
            curr_row[-1] = 1
            for j in range(n - 2, -1, -1):
                curr_row[j] = curr_row[j + 1] + prev_row[j]
            prev_row = curr_row
        return curr_row[0]

    # # bottom up dp - iterate in reverse
    # def uniquePaths(self, m: int, n: int) -> int:
    #     # Time O(m*n), Memory O(m*n)
    #     dp = [[0] * n for _ in range(m)]
    #     dp[m - 1][n - 1] = 1
    #     for i in range(m - 1, -1, -1):
    #         for j in range(n - 1, -1, -1):
    #             if i < m - 1 and j < n - 1:
    #                 dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
    #             elif i < m - 1:
    #                 dp[i][j] = dp[i + 1][j]
    #             elif j < n - 1:
    #                 dp[i][j] = dp[i][j + 1]
    #     return dp[0][0]

    # # top down dp - dfs with cache
    # def uniquePaths(self, m: int, n: int) -> int:
    #     # Time O(m*n), Memory O(m*n)
    #     dp = [[0] * n for _ in range(m)]

    #     def dfs(i, j):
    #         if dp[i][j]:
    #             return dp[i][j]
    #         if i == m or j == n:
    #             return 0
    #         if i == m - 1 or j == n - 1:
    #             return 1
    #         res = dfs(i + 1, j) + dfs(i, j + 1)
    #         dp[i][j] = res
    #         return res

    #     return dfs(0, 0)

    # # dfs - too slow
    # def uniquePaths(self, m: int, n: int) -> int:
    #     # Time O(2^(m*n)), Memory O(2^(m*n))
    #     def dfs(i, j):
    #         if i == m or j == n:
    #             return 0
    #         if i == m - 1 and j == n - 1:
    #             return 1
    #         return dfs(i + 1, j) + dfs(i, j + 1)

    #     return dfs(0, 0)
