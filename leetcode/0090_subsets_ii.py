from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time O(n 2^n), Memory O(n 2^n)
        res = []
        nums.sort()

        def dfs(i, stack, stack_sum):
            if i == len(nums):
                res.append(list(stack))
                return

            # decision to include nums[i]
            stack.append(nums[i])
            stack_sum += nums[i]
            dfs(i + 1, stack, stack_sum)

            # decision to skip nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            stack_sum -= stack.pop()
            dfs(i + 1, stack, stack_sum)

        dfs(0, [], 0)
        return res
