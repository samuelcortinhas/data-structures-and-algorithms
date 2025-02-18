from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time O(n^n), Memory O(n!)
        res = []

        def backtrack(i, stack):
            if len(stack) == len(nums):
                res.append(list(stack))

            for n in nums:
                if n not in stack:
                    stack.append(n)
                    backtrack(i + 1, stack)
                    stack.pop()

        backtrack(0, [])
        return res


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         # Time O(n^n), Memory O(n!)
#         res = []

#         def dfs(stack):
#             if len(stack) == len(nums):
#                 res.append(list(stack))
#                 return

#             for j in range(len(nums)):
#                 if nums[j] not in stack:
#                     stack.append(nums[j])
#                     dfs(stack)
#                     stack.pop()

#         dfs([])
#         return res
