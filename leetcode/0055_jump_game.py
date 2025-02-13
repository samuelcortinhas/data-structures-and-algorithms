from typing import List


class Solution:
    # Dynamic Programming
    def canJump(self, nums: List[int]) -> bool:
        # Time O(n*m), Memory O(n) where m=max(nums), n=len(nums)
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i]):
                if dp[i + j + 1]:
                    dp[i] = True
                    break
        return dp[0]

    # # Correct but too slow
    # def canJumpBruteForce(self, nums: List[int]) -> bool:
    #     # Time O(n^m), Memory O(1)
    #     def backtrack(nums, index):
    #         if index == (len(nums) - 1):
    #             return True
    #         elif index >= len(nums):
    #             return False
    #         for i in range(nums[index], 0, -1):
    #             if backtrack(nums, index + i):
    #                 return True
    #         return False

    #     return backtrack(nums, 0)
