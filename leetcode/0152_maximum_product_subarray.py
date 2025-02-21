from typing import List


class Solution:
    # dp solution - too slow
    def maxProduct(self, nums: List[int]) -> int:
        # Time O(n^2), Memory O(1)
        res = max(nums)
        for i in range(len(nums)):
            prod = nums[i]
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                if prod > res:
                    res = prod
        return res

    # Brute force - too slow
    # def maxProduct(self, nums: List[int]) -> int:
    #     # Time O(n^3), Memory O(1)
    #     res = float("-inf")
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             prod = 1
    #             for p in nums[i : j + 1]:
    #                 prod *= p
    #             if prod > res:
    #                 res = prod
    #     return res
