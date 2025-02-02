from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time O(n), Memory O(n)
        counter = defaultdict(int)
        i = 0
        for n in nums:
            if counter[n] <= 1:
                nums[i] = n
                i += 1
                counter[n] += 1
        return i
