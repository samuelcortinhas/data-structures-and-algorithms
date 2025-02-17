from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Time O(n^k), Memory O(k * nCk)
        res = []

        def backtrack(i, stack):
            if i == k:
                res.append(list(stack))

            for j in range(1, n + 1):
                if not stack or j > stack[-1]:
                    stack.append(j)
                    backtrack(i + 1, stack)
                    stack.pop()

        backtrack(0, [])
        return res
