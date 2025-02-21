from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        prev, curr = 0, 0
        for n in nums:
            tmp = curr
            curr = max(prev + n, curr)
            prev = tmp
        return curr

    # def rob(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(1)
    #     prev_one, prev_two = 0, 0
    #     for i in range(len(nums)):
    #         bank = max(nums[i] + prev_two, prev_one)
    #         prev_two = prev_one
    #         prev_one = bank
    #     return prev_one

    # def rob(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     if len(nums) == 1:
    #         return nums[0]

    #     bank = [0] * len(nums)
    #     bank[-1] = nums[-1]
    #     bank[-2] = max(nums[-2:])
    #     for i in range(len(nums) - 3, -1, -1):
    #         bank[i] = max(nums[i] + bank[i + 2], bank[i + 1])
    #     return bank[0]

    # def rob(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(1)
    #     if len(nums)==1:
    #         return nums[0]

    #     twoback = nums[-1]
    #     oneback = max(nums[-2:])
    #     for i in range(len(nums)-3, -1, -1):
    #         curr = max(nums[i]+twoback, oneback)
    #         twoback = oneback
    #         oneback = curr
    #     return oneback
