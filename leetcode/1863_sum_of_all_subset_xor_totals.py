from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Time O(2^n), Memory O(n)
        def dfs(i, curr):
            if i == len(nums):
                return curr
            include = dfs(i + 1, curr ^ nums[i])
            exclude = dfs(i + 1, curr)
            return include + exclude

        return dfs(0, 0)
