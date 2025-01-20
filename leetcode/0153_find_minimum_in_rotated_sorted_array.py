from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time O(log(n)), Memory O(1)
        left, right = 0, len(nums) - 1
        lowest = nums[0]

        while left <= right:
            mid = (left + right) // 2
            lowest = min(lowest, nums[mid])
            if nums[mid] > max(nums[left], nums[right]):
                left = mid + 1
            elif nums[mid] < min(nums[left], nums[right]):
                right = mid - 1
            else:
                return min(lowest, nums[left], nums[right])
