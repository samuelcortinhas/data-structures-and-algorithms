import heapq
from typing import List


class Solution:
    # initial attempt - too slow
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Time O(n^2), Memory O(n)
        curr_time = 0
        heap = [(t, d, i) for i, (t, d) in enumerate(tasks)]
        heapq.heapify(heap)
        res = []
        while heap:
            curr_time = max(curr_time, heap[0][0])
            batch = []
            while heap and heap[0][0] <= curr_time:
                batch.append(heapq.heappop(heap))

            j = float("inf")
            shortest = float("inf")
            item = None
            for b in batch:
                if b[1] < shortest or (b[1] == shortest and b[2] < j):
                    shortest = b[1]
                    item = b
                    j = b[2]

            res.append(item[2])
            curr_time += item[1]
            for b in batch:
                if b != item:
                    heapq.heappush(heap, b)
        return res
