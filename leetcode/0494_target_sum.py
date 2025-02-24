from typing import List


class Solution:
    # top down dp solution - cache curr_target at each index
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Time O(n*m), Memory O(n*m) where n=len(nums), m=sum(abs(nums))
        dp = {}

        def dfs(i, curr_target):
            if (i, curr_target) in dp:
                return dp[(i, curr_target)]
            if i == len(nums) and curr_target == 0:
                return 1
            elif i == len(nums):
                return 0
            dp[(i, curr_target)] = dfs(i + 1, curr_target - nums[i]) + dfs(
                i + 1, curr_target + nums[i]
            )
            return dp[(i, curr_target)]

        return dfs(0, target)

    # # brute force - too slow
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     # Time O(2^n), Memory O(2^n) where n=len(nums)
    #     def dfs(i, curr_sum):
    #         if i == len(nums) and curr_sum == target:
    #             return 1
    #         elif i == len(nums):
    #             return 0
    #         return dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])

    #     return dfs(0, 0)
