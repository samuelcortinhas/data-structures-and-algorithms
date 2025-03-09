from typing import List


class Solution:
    # cumulative sum of diffs
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Time O(n), Memory O(n)
        diffs = [
            (colors[i] != colors[(i - 1) % len(colors)]) for i in range(len(colors))
        ]

        start = 0
        for d in diffs:
            if not d:
                start = 0
            else:
                start += 1

        cumsum = [start]
        for d in diffs:
            if not d:
                cumsum.append(0)
            else:
                cumsum.append(1 + cumsum[-1])

        return sum([1 for c in cumsum[1:] if c >= k - 1])

    # # brute force
    # def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
    #     # Time O(n*k) , Memory O(1)
    #     n = len(colors)
    #     res = 0
    #     for i in range(len(colors)):
    #         for j in range(k - 1):
    #             if colors[(i + j + 1) % n] == colors[(i + j) % n]:
    #                 res -= 1
    #                 break
    #         res += 1
    #     return res
