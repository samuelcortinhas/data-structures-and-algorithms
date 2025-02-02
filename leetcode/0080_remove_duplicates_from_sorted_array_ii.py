from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        i = 1  # insert index
        count = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[i] = nums[j]
                i += 1
        return i

    # def removeDuplicatesCounter(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     counter = defaultdict(int)
    #     i = 0
    #     for n in nums:
    #         if counter[n] <= 1:
    #             nums[i] = n
    #             i += 1
    #             counter[n] += 1
    #     return i
