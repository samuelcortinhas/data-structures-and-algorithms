from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time O(n 2^n), Memory O(n 2^n)
        res = []

        def dfs(i, stack):
            if i == len(nums):
                res.append(list(stack))
                return

            # include nums[i] in subset
            stack.append(nums[i])
            dfs(i + 1, stack)
            stack.pop()

            # don't include nums[i] in subset
            dfs(i + 1, stack)

        dfs(0, [])
        return res


# class Solution(object):
#     # Time O(2^n), Memory O(n 2^n)
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # size of power set is 2^n
#         # every element is either in or not in a subset
#         # binary tree of height n
#         res = []
#         subset = []

#         def dfs(i):
#             # i = index of value we are making decision on
#             if i >= len(nums):
#                 res.append(list(subset))
#                 return

#             # decision to include nums[i]
#             subset.append(nums[i])
#             dfs(i + 1)

#             # decision to not include nums[i]
#             subset.pop()
#             dfs(i + 1)

#         dfs(0)
#         return res
