from typing import List


class Solution:
    def pacificAtlanticBruteForce(self, heights: List[List[int]]) -> List[List[int]]:
        # Time O((m*n)^2), Memory O(m*n(m+n))
        m, n = len(heights), len(heights[0])

        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            if heights[i][j] > prev:
                return 0

            prev = heights[i][j]
            if (dfs(i + 1, j, prev) or dfs(i, j + 1, prev)) and (
                dfs(i - 1, j, prev) or dfs(i, j - 1, prev)
            ):
                return 1
            else:
                return 0

        res = []
        for i in range(m):
            for j in range(n):
                if dfs(i, j, heights[i][j]):
                    res.append([i, j])
        return res
