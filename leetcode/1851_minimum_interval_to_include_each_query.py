from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Time O(q*n), Memory O(q)
        intervals.sort()
        res = []
        for q in queries:
            min_size = float("inf")
            for start, end in intervals:
                if start <= q and q <= end:
                    min_size = min(min_size, end - start + 1)
            if min_size == float("inf"):
                min_size = -1
            res.append(min_size)
        return res
