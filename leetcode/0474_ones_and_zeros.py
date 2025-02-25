from collections import defaultdict
from typing import List


class Solution:
    # brute force on binary decision tree
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time O(2^n), Memory O(2^n)

        # For each str, decision is include or not include it
        # curr = {"0": count, "1": count, "size": len}
        def backtrack(i, curr):
            if i == len(strs):
                if curr["0"] <= m and curr["1"] <= n:
                    return curr["size"]
                else:
                    return 0

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

            return max(r1, r2)

        return backtrack(0, defaultdict(int))
