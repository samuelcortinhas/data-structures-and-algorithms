import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time O(n log n), Memory O(1)
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            m1 = heapq.heappop(heap)
            m2 = heapq.heappop(heap)

            if m1 != m2:
                heapq.heappush(heap, m1 - m2)

        return -heap[0] if heap else 0
