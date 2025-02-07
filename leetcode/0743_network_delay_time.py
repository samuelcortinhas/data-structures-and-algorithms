import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time O(E log V), Memory O(V)
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        shortest = {}
        heap = [(0, k)]
        while heap:
            dist, node = heapq.heappop(heap)
            if node in shortest:
                continue
            shortest[node] = dist

            for v, t in adj_list[node]:
                if v not in shortest:
                    heapq.heappush(heap, (dist + t, v))

        if len(shortest) < n:
            return -1
        return max(shortest.values())
