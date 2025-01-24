from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time O(m*n), Memory O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            if (i, j) in seen:
                return

            seen.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == "0" or (i, j) in seen:
                    continue
                dfs(i, j)
                res += 1

        return res
