from typing import List


class Solution:
    # Time O(t 2^t), Memory O(t 2^t) where t is the target
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        res = []
        stack = []

        def dfs(i):
            # i = index of number being considered
            s = sum(stack)
            if s == target:
                res.append(list(stack))
                return
            elif s > target or i >= len(candidates):
                return

            # decision to include candidates[i] in stack
            stack.append(candidates[i])
            dfs(i)

            # decision not to include candidates[i] in stack
            stack.pop()
            dfs(i + 1)

        dfs(0)
        return res
