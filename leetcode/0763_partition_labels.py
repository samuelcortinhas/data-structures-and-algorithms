from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Time O(n log n), Memory O(n)
        start = {}
        end = {}
        for i, char in enumerate(s):
            if char not in start:
                start[char] = i
            end[char] = i

        intervals = []
        for k, v in start.items():
            intervals.append([v, end[k]])
        intervals.sort()

        # merge intervals
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            else:
                curr[1] = max(curr[1], intervals[i][1])
        res.append(curr)
        return [e - s + 1 for s, e in res]
