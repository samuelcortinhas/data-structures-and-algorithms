from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time O(nk), Memory O(k)
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i : i + k]))
        return res
