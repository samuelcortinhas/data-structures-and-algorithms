from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time O(m*n), Memory O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()
        max_area = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            if (i, j) in seen:
                return 0

            seen.add((i, j))
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0 or (i, j) in seen:
                    continue
                area = dfs(i, j)
                max_area = max(max_area, area)

        return max_area
