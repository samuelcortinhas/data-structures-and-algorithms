from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        left, curr_sum = 0, 0
        min_size = float("inf")
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_size = min(min_size, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_size if min_size != float("inf") else 0

    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     # Time O(n), Memory O(1)
    #     left, right = 0, 0
    #     curr_sum = nums[0]
    #     min_size = 1 if curr_sum >= target else float("inf")
    #     while True:
    #         print(left, right, curr_sum)
    #         if left < right and curr_sum >= target:
    #             min_size = min(min_size, right - left + 1)
    #             curr_sum -= nums[left]
    #             left += 1
    #             if curr_sum >= target:
    #                 min_size = min(min_size, right - left + 1)
    #         elif right < len(nums) - 1:
    #             right += 1
    #             curr_sum += nums[right]
    #         else:
    #             break
    #     return min_size if min_size != float("inf") else 0
