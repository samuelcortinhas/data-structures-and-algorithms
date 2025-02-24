from typing import List


class Solution:
    # brute force - too slow
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Time O(2^n), Memory O(2^n) where n=len(nums)
        def dfs(i, curr_sum):
            if i == len(nums) and curr_sum == target:
                return 1
            elif i == len(nums):
                return 0
            return dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])

        return dfs(0, 0)
