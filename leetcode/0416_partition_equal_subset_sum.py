from typing import List


class Solution:
    # top down dp - too slow
    def canPartition(self, nums: List[int]) -> bool:
        # Time O(2^n), Memory O(n)
        target = sum(nums) / 2
        if sum(nums) % 2:
            return False
        dp = [False] * (len(nums) + 1)

        def dfs(i, curr_sum):
            if dp[i]:
                return True
            if curr_sum == target:
                dp[i] = True
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
