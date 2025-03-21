from typing import List


class Solution:
    # Time O(t n^t), Memory O(t n^t) where t is the target
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(prev_index, stack, curr_sum):
            if curr_sum == target:
                res.append(list(stack))
                return
            if curr_sum > target:
                return

            for i in range(prev_index, len(candidates)):
                c = candidates[i]
                stack.append(c)
                curr_sum += c
                backtrack(i, stack, curr_sum)
                curr_sum -= c
                stack.pop()

        backtrack(0, [], 0)
        return res


# class Solution:
#     # Time O(t 2^t), Memory O(t 2^t) where t is the target
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # backtracking
#         res = []

#         def dfs(i, stack, stack_sum):
#             # i = index of number being considered
#             if stack_sum == target:
#                 res.append(list(stack))
#                 return
#             elif stack_sum > target or i >= len(candidates):
#                 return

#             # decision to include candidates[i] in stack
#             stack.append(candidates[i])
#             stack_sum += candidates[i]
#             dfs(i, stack, stack_sum)

#             # decision not to include candidates[i] in stack
#             stack_sum -= stack.pop()
#             dfs(i + 1, stack, stack_sum)

#         dfs(0, [], 0)
#         return res

# def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#     # backtracking
#     res = []
#     stack = []

#     def dfs(i):
#         # i = index of number being considered
#         s = sum(stack)
#         if s == target:
#             res.append(list(stack))
#             return
#         elif s > target or i >= len(candidates):
#             return

#         # decision to include candidates[i] in stack
#         stack.append(candidates[i])
#         dfs(i)

#         # decision not to include candidates[i] in stack
#         stack.pop()
#         dfs(i + 1)

#     dfs(0)
#     return res
