from typing import List


class Solution:
    # maintain min and max prod iteratively
    def maxProduct(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        res = max(nums)
        max_prod, min_prod = 1, 1
        for n in nums:
            tmp = max_prod * n
            max_prod = max(tmp, min_prod * n, n)
            min_prod = min(tmp, min_prod * n, n)
            res = max(res, max_prod)
        return res

    # # keep track of min and max prod iteratively
    # def maxProduct(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     if not nums:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     if min(nums) >= 1:
    #         p = 1
    #         for n in nums:
    #             p *= n
    #         return p
    #     if 0 in nums:
    #         i = nums.index(0)
    #         return max(0, self.maxProduct(nums[:i]), self.maxProduct(nums[i + 1 :]))

    #     max_prod = 1
    #     min_prod = 1
    #     res = 1
    #     for n in nums:
    #         tmp = max_prod
    #         max_prod = max(max_prod * n, min_prod * n, 1)
    #         min_prod = min(tmp * n, min_prod * n, 1)
    #         res = max(res, max_prod)
    #     return res

    # # dp solution - too slow
    # def maxProduct(self, nums: List[int]) -> int:
    #     # Time O(n^2), Memory O(1)
    #     res = max(nums)
    #     for i in range(len(nums)):
    #         prod = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             prod *= nums[j]
    #             if prod > res:
    #                 res = prod
    #     return res

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
