from typing import List


class Solution:
    # compute sign
    def arraySign(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        res = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                res *= -1
        return res

    # # compute product
    # def arraySign(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(1)
    #     prod = 1
    #     for n in nums:
    #         prod *= n
    #     if prod > 0:
    #         return 1
    #     elif prod < 0:
    #         return -1
    #     else:
    #         return 0
