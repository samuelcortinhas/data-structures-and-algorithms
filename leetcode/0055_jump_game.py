from typing import List


class Solution:
    # Correct but too slow
    def canJump(self, nums: List[int]) -> bool:
        # Time O(exponential), Memory O(1)
        def backtrack(nums, index):
            if index == (len(nums) - 1):
                return True
            elif index >= len(nums):
                return False
            for i in range(nums[index], 0, -1):
                if backtrack(nums, index + i):
                    return True
            return False

        return backtrack(nums, 0)
