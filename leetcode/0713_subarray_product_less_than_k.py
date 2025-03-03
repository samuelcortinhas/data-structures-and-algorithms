from typing import List


class Solution:
    # sliding window
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Time O(n), Memory O(1)
        res = 0
        left = 0
        p = 1
        for right in range(len(nums)):
            p *= nums[right]
            while p >= k and left <= right:
                p //= nums[left]
                left += 1
            res += right - left + 1
        return res

    # # compute prefix products on demand - too slow
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     # Time O(n^2), Memory O(1)
    #     left, right = 0, 0
    #     res = 0
    #     while left < len(nums):
    #         right = left
    #         p = 1
    #         while right < len(nums):
    #             p *= nums[right]
    #             if p < k:
    #                 res += 1
    #                 right += 1
    #             else:
    #                 break
    #         left += 1
    #     return res

    # compute prefix products - uses too much memory
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     # Time O(n^2), Memory O(n^2)
    #     left, right = 0, 0
    #     res = 0
    #     pre = [[1] * (len(nums) + 1) for _ in range(len(nums))]
    #     for i in range(len(nums)):
    #         for j in range(1, len(nums) + 1):
    #             if j > i:
    #                 pre[i][j] = nums[j - 1] * pre[i][j - 1]

    #     while left < len(nums):
    #         right = left
    #         p = pre[left][right + 1]
    #         while right < len(nums):
    #             p = pre[left][right + 1]
    #             if p < k:
    #                 res += 1
    #                 right += 1
    #             else:
    #                 break
    #         left += 1
    #     return res
