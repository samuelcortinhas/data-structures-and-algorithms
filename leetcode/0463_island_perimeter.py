from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time O(m*n), Memory O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 1
            if (i, j) in seen:
                return 0

            seen.add((i, j))
            res = dfs(i + 1, j)
            res += dfs(i - 1, j)
            res += dfs(i, j + 1)
            res += dfs(i, j - 1)
            return res

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    return dfs(i, j)
