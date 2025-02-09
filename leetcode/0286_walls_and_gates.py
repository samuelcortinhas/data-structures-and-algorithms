from collections import deque
from typing import List


class Solution:
    # Multi-source BFS
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        dist = 0
        visit = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                rooms[i][j] = dist
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    u, v = i + dx, j + dy
                    if (
                        u >= 0
                        and v >= 0
                        and u < m
                        and v < n
                        and (u, v) not in visit
                        and rooms[u][v] > 0
                    ):
                        queue.append((u, v))
                        visit.add((u, v))
            dist += 1
