from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # Time O(n), Memory O(1)
        curr_sum = 0
        max_sum = float("-inf")
        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum
