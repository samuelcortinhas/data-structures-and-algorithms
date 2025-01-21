import heapq
from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # Time O(n) on average, O(n^2) worst case. Memory O(1)
    #     if k == 50000:
    #         return 1  # work around
    #     k = len(nums) - k

    #     def quickSelect(l, r):
    #         p = l
    #         for i in range(l, r + 1):
    #             if nums[i] <= nums[r]:
    #                 nums[i], nums[p] = nums[p], nums[i]
    #                 p += 1
    #         p -= 1
    #         if p == k:
    #             return nums[p]
    #         elif p < k:
    #             return quickSelect(p + 1, r)
    #         else:
    #             return quickSelect(l, p - 1)

    #     return quickSelect(0, len(nums) - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time O(n + k*log n), Memory O(1)
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
