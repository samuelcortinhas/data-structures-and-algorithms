from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time O(n log n), Memory O(1)
        intervals.sort()
        curr = intervals[0]
        deletes = 0
        for i in range(1, len(intervals)):
            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
                continue
            elif curr[1] <= intervals[i][1]:
                deletes += 1
            else:
                deletes += 1
                curr = intervals[i]
        return deletes
