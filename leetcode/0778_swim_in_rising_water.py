import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Time O(n^2 log n), Memory O(n^2)
        n = len(grid)
        visited = set()  # (i, j)
        heap = [(grid[0][0], (0, 0))]  # min t, (i,  j)
        while heap:
            el, (i, j) = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if (i, j) == (n - 1, n - 1):
                return el

            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                u, v = i + dx, j + dy
                if u >= 0 and v >= 0 and u < n and v < n and (u, v) not in visited:
                    heapq.heappush(heap, (max(el, grid[u][v]), (u, v)))
