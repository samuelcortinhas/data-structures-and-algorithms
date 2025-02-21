from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        def house_robber(nums):
            prev, curr = 0, 0
            for n in nums:
                tmp = curr
                curr = max(prev + n, curr)
                prev = tmp
            return curr

        return max(house_robber(nums[1:]), house_robber(nums[:-1]), nums[0])

    # def rob(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(1)
    #     def houserobber(nums):
    #         prev_one, prev_two = 0, 0
    #         for i in range(len(nums)):
    #             bank = max(nums[i] + prev_two, prev_one)
    #             prev_two = prev_one
    #             prev_one = bank
    #         return prev_one

    #     return max(houserobber(nums[1:]), houserobber(nums[:-1]), nums[0])
