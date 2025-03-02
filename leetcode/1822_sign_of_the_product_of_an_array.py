from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        prod = 1
        for n in nums:
            prod *= n
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        else:
            return 0
