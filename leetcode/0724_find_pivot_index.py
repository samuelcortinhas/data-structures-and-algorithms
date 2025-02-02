from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        leftsum, rightsum = 0, sum(nums)
        for i, n in enumerate(nums):
            rightsum -= n
            if leftsum == rightsum:
                return i
            leftsum += n
        return -1

    # def pivotIndex3Loops(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     prefix = []
    #     total = 0
    #     for n in nums:
    #         prefix.append(total)
    #         total += n

    #     postfix = []
    #     total = 0
    #     for n in nums[::-1]:
    #         postfix.append(total)
    #         total += n
    #     postfix = postfix[::-1]

    #     for i, (l, r) in enumerate(zip(prefix, postfix)):
    #         if l == r:
    #             return i
    #     return -1
