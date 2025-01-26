from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time O(n), Memory O(n)
        if len(nums) == 1:
            return nums[0]

        bank = [0] * len(nums)
        bank[-1] = nums[-1]
        bank[-2] = max(nums[-2:])
        for i in range(len(nums) - 3, -1, -1):
            bank[i] = max(nums[i] + bank[i + 2], bank[i + 1])
        return bank[0]
