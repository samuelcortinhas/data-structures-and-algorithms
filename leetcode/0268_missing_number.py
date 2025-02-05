from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        res = len(nums)
        for i, n in enumerate(nums):
            res = res ^ i ^ n
        return res

    # def missingNumberMaths(self, nums: List[int]) -> int:
    #     # Time O(1), Memory O(1)
    #     return len(nums)*(len(nums)+1)//2 - sum(nums)
