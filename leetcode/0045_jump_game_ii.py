from typing import List


class Solution:
    # Greedy/ BFS solution
    def jump(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        i = 0
        curr = nums[0]
        jumps = 1
        while i + curr < len(nums) - 1:
            tmp = max([nums[i + j + 1] - (curr - (j + 1)) for j in range(curr)])
            i += curr
            curr = tmp
            jumps += 1
        return jumps if len(nums) > 1 else 0

    # # DP solution
    # def jump(self, nums: List[int]) -> int:
    #     # Time O(n*m), Memory O(n) where n=len(nums), m=max(nums)
    #     dp = [0] * len(nums)
    #     for i in range(len(nums) - 2, -1, -1):
    #         steps = []
    #         for j in range(nums[i]):
    #             if i + j + 1 < len(nums) and dp[i + j + 1] is not None:
    #                 steps.append(dp[i + j + 1])
    #         dp[i] = 1 + min(steps) if steps else None
    #     return dp[0]
