from typing import List


class Solution:
    # bottom up dp solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time O(n^2), Memory O(n)
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
