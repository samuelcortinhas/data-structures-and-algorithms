from typing import List


class Solution:
    def partitionLabelsV2(self, s: str) -> List[int]:
        # Time O(n), Memory O(26)
        last_occurence = {}
        for i, char in enumerate(s):
            last_occurence[char] = i

        res = []
        size, max_size, end = 0, 0, 0
        for i, char in enumerate(s):
            size += 1
            max_size = max(max_size, size)
            end = max(end, last_occurence[char])
            if i >= end:
                res.append(size)
                size = 0
        return res

    # def partitionLabelsV1(self, s: str) -> List[int]:
    #     # Time O(n log n), Memory O(n)
    #     start = {}
    #     end = {}
    #     for i, char in enumerate(s):
    #         if char not in start:
    #             start[char] = i
    #         end[char] = i

    #     intervals = []
    #     for k, v in start.items():
    #         intervals.append([v, end[k]])
    #     intervals.sort()

    #     # merge intervals
    #     res = []
    #     curr = intervals[0]
    #     for i in range(1, len(intervals)):
    #         if curr[1] < intervals[i][0]:
    #             res.append(curr)
    #             curr = intervals[i]
    #         else:
    #             curr[1] = max(curr[1], intervals[i][1])
    #     res.append(curr)
    #     return [e - s + 1 for s, e in res]
