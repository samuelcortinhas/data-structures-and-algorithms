from typing import List


class Solution:
    # Time O(n 2^n), Memory O(n 2^n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        res = []
        candidates = sorted(candidates)

        def dfs(i, stack, stack_sum):
            # i = index of number being considered
            if stack_sum == target and stack not in res:
                res.append(list(stack))
                return
            elif stack_sum > target or i >= len(candidates):
                return

            # decision to include candidates[i] in stack
            stack.append(candidates[i])
            stack_sum += candidates[i]
            dfs(i + 1, stack, stack_sum)

            # decision not to include candidates[i] in stack (skip if already backtracked)
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            stack_sum -= stack.pop()
            dfs(i + 1, stack, stack_sum)

        dfs(0, [], 0)
        return res
