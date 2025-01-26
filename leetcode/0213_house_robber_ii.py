from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        def houserobber(nums):
            prev_one, prev_two = 0, 0
            for i in range(len(nums)):
                bank = max(nums[i] + prev_two, prev_one)
                prev_two = prev_one
                prev_one = bank
            return prev_one

        return (
            max(houserobber(nums[1:]), houserobber(nums[:-1]))
            if len(nums) > 1
            else nums[0]
        )
