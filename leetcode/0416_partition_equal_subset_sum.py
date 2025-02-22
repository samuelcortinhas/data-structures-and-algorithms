from typing import List


class Solution:
    # dfs with backtracking - too slow
    def canPartition(self, nums: List[int]) -> bool:
        # Time O(2^n), Memory O(n)
        target = sum(nums) / 2
        if sum(nums) % 2:
            return False

        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if i >= len(nums):
                return False

            curr_sum += nums[i]
            if dfs(i + 1, curr_sum):
                return True
            curr_sum -= nums[i]

            if dfs(i + 1, curr_sum):
                return True
            return False

        return dfs(0, 0)
