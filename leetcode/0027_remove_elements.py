from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time O(n), Memory O(1)
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     # Time O(n^2), Memory O(1)
    #     deletes = 0
    #     for i in range(len(nums)):
    #         if nums[i - deletes] == val:
    #             nums.remove(val)
    #             deletes += 1
    #     return len(nums)
