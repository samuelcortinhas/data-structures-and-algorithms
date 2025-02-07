import heapq
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time O(n^2 log n), Memory O(n^2)
        adj_list = defaultdict(list)
        n = len(points)
        if n <= 1:
            return 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p, q = points[i], points[j]
                adj_list[tuple(p)].append(tuple(q))
                adj_list[tuple(q)].append(tuple(p))

        start = tuple(points[0])
        heap = []
        for point in adj_list[start]:
            heapq.heappush(heap, (self.manhattan(start, point), start, point))
        seen = set([start])
        cost = 0
        while heap:
            dist, start, dest = heapq.heappop(heap)
            if dest in seen:
                continue
            seen.add(dest)
            cost += dist

            if len(seen) == n:
                return cost

            for neigh in adj_list[dest]:
                if neigh not in seen:
                    heapq.heappush(heap, (self.manhattan(dest, neigh), dest, neigh))
