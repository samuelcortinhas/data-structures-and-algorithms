import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time O(k log n), Memory O(n)
        heap = [(x[0] ** 2 + x[1] ** 2, x) for x in points]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     # Time O(n log n), Memory O(n)
    #     func = lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5
    #     dists = [(func(x), x) for x in points]
    #     sorted_dists = sorted(dists, key=lambda x: x[0])
    #     topk = sorted_dists[:k]
    #     return [x[1] for x in topk]
