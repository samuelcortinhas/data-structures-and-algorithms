from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time O(n log n), Memory O(n)
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        curr = sorted_intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if curr[1] < sorted_intervals[i][0]:
                res.append(curr)
                curr = sorted_intervals[i]
            else:
                curr = [
                    min(curr[0], sorted_intervals[i][0]),
                    max(curr[1], sorted_intervals[i][1]),
                ]
        res.append(curr)
        return res
