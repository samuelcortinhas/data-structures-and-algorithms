import heapq
from typing import List


class Solution:
    def minIntervalV2(self, intervals: List[List[int]], queries: List[int]):
        # Time O(nlogn + qlogq), Memory O(n+q)
        intervals.sort()
        queries_sorted = [(q, i) for i, q in enumerate(queries)]
        queries_sorted.sort()
        res = [-1] * len(queries)
        heap = []
        interval_index = 0
        for q, i in queries_sorted:
            while interval_index < len(intervals) and intervals[interval_index][0] <= q:
                heapq.heappush(
                    heap,
                    (
                        intervals[interval_index][1] - intervals[interval_index][0] + 1,
                        intervals[interval_index][1],
                    ),
                )
                interval_index += 1

            while heap:
                width, r = heap[0]
                if r >= q:
                    res[i] = width
                    break
                else:
                    heapq.heappop(heap)
        return res

    # def minIntervalV1(self, intervals: List[List[int]], queries: List[int]):
    #     # Time O(q*n), Memory O(q)
    #     intervals.sort()
    #     res = []
    #     for q in queries:
    #         min_size = float("inf")
    #         for start, end in intervals:
    #             if start <= q and q <= end:
    #                 min_size = min(min_size, end - start + 1)
    #         if min_size == float("inf"):
    #             min_size = -1
    #         res.append(min_size)
    #     return res
