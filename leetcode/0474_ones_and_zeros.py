from collections import defaultdict
from typing import List


class Solution:
    # top down dp with cache
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time O(2^n), Memory O(2^n)
        dp = {}  # (index, #ones, #zeros): #solutions

        def backtrack(i, curr):
            if (i, curr["1"], curr["0"]) in dp:
                return dp[(i, curr["1"], curr["0"])]
            if i == len(strs):
                if curr["0"] <= m and curr["1"] <= n:
                    dp[(i, curr["1"], curr["0"])] = curr["size"]
                    return curr["size"]
                else:
                    dp[(i, curr["1"], curr["0"])] = 0
                    return 0

            copy_ones = curr["1"]
            copy_zeros = curr["0"]

            # don't include
            r1 = backtrack(i + 1, curr)

            # include
            ones = sum([1 if s == "1" else 0 for s in strs[i]])
            zeros = len(strs[i]) - ones
            curr["1"] += ones
            curr["0"] += zeros
            curr["size"] += 1
            r2 = backtrack(i + 1, curr)
            curr["1"] -= ones
            curr["0"] -= zeros
            curr["size"] -= 1

            dp[(i, copy_ones, copy_zeros)] = max(r1, r2)
            return dp[(i, curr["1"], curr["0"])]

        return backtrack(0, defaultdict(int))

    # # brute force on binary decision tree
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     # Time O(2^n), Memory O(2^n)

    #     # For each str, decision is include or not include it
    #     # curr = {"0": count, "1": count, "size": len}
    #     def backtrack(i, curr):
    #         if i == len(strs):
    #             if curr["0"] <= m and curr["1"] <= n:
    #                 return curr["size"]
    #             else:
    #                 return 0

    #         # don't include
    #         r1 = backtrack(i + 1, curr)

    #         # include
    #         ones = sum([1 if s == "1" else 0 for s in strs[i]])
    #         zeros = len(strs[i]) - ones
    #         curr["1"] += ones
    #         curr["0"] += zeros
    #         curr["size"] += 1
    #         r2 = backtrack(i + 1, curr)
    #         curr["1"] -= ones
    #         curr["0"] -= zeros
    #         curr["size"] -= 1

    #         return max(r1, r2)

    #     return backtrack(0, defaultdict(int))
