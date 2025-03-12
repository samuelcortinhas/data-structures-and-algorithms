from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        neg = 0
        i = 0
        while i < len(nums) and nums[i] < 0:
            neg += 1
            i += 1

        zeros = 0
        while i < len(nums) and nums[i] == 0:
            zeros += 1
            i += 1

        return max(neg, len(nums) - zeros - neg)
