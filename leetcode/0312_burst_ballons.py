from typing import List


class Solution:
    # brute force - way too slow
    def maxCoins(self, nums: List[int]) -> int:
        # Time O(n!), Memory O(n!)
        return self.dfs(nums)

    def dfs(self, nums):
        best_score = 0
        for i in range(len(nums)):
            if i - 1 >= 0 and i + 1 < len(nums):
                score = nums[i - 1] * nums[i] * nums[i + 1]
            elif i - 1 >= 0:
                score = nums[i - 1] * nums[i]
            elif i + 1 < len(nums):
                score = nums[i] * nums[i + 1]
            else:
                score = nums[i]
            nxt = list(nums)
            nxt.pop(i)
            score += self.dfs(nxt)
            if score > best_score:
                best_score = score
        return best_score
