from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time O(m*n), Memory O(m*n)
        m, n = len(grid), len(grid[0])
        queue = deque()

        if all([x != 1 for row in grid for x in row]):
            return 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 2:
                    queue.append((i, j))
                    grid[i][j] = 1

        minutes = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                    continue

                grid[i][j] = 2
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))
            minutes += 1

        if any([x == 1 for row in grid for x in row]):
            return -1

        return minutes - 1
