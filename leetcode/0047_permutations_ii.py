from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Time O(n!), Memory O(n!)
        counts = Counter(nums)
        res = []

        def backtrack(stack):
            if len(stack) == len(nums):
                res.append(list(stack))

            for n in counts:
                if counts[n] > 0:
                    stack.append(n)
                    counts[n] -= 1
                    backtrack(stack)
                    counts[n] += 1
                    stack.pop()

        backtrack([])
        return res
