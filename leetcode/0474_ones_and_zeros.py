from typing import List


class Solution:
    # top down dp with cache
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time O(s*m*n), Memory O(s*m*n) where s=len(strs)
        dp = {}  # (index, #zeros, #ones): #solutions

        def backtrack(i, zeros, ones):
            if i == len(strs):
                return 0
            if (i, zeros, ones) in dp:
                return dp[(i, zeros, ones)]

            # don't include
            r1 = backtrack(i + 1, zeros, ones)

            # include
            i_zeros = strs[i].count("0")
            i_ones = strs[i].count("1")
            if zeros + i_zeros <= m and ones + i_ones <= n:
                r2 = backtrack(i + 1, zeros + i_zeros, ones + i_ones)
            else:
                r2 = -1

            dp[(i, zeros, ones)] = max(r1, 1 + r2)
            return dp[(i, zeros, ones)]

        return backtrack(0, 0, 0)

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
