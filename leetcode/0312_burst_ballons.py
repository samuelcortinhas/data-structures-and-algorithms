from typing import List


class Solution:
    # dp solution - keep track of left and right boundaries for each subarray
    def maxCoins(self, nums: List[int]) -> int:
        # Time O(n^3), Memory O(n^2)
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)

    # # brute force - way too slow
    # def maxCoins(self, nums: List[int]) -> int:
    #     # Time O(n!), Memory O(n!)
    #     return self.dfs(nums)

    # def dfs(self, nums):
    #     best_score = 0
    #     for i in range(len(nums)):
    #         if i - 1 >= 0 and i + 1 < len(nums):
    #             score = nums[i - 1] * nums[i] * nums[i + 1]
    #         elif i - 1 >= 0:
    #             score = nums[i - 1] * nums[i]
    #         elif i + 1 < len(nums):
    #             score = nums[i] * nums[i + 1]
    #         else:
    #             score = nums[i]
    #         nxt = list(nums)
    #         nxt.pop(i)
    #         score += self.dfs(nxt)
    #         if score > best_score:
    #             best_score = score
    #     return best_score
