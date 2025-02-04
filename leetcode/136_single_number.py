from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        res = 0
        for n in nums:
            res ^= n
        return res
