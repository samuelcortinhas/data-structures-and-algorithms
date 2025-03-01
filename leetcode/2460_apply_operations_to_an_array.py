from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Time O(n), Memory O(1)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        swap_index = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[swap_index], nums[j] = nums[j], nums[swap_index]
                swap_index += 1
        return nums
