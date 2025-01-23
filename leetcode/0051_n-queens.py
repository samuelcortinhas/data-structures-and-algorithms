from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Time O(n^2), Memory O(n)
        res = []

        def backtrack(stack):
            # stack[i] = column index of queen in i-th row
            if len(stack) == n:
                res.append(list(stack))
                return

            invalid = set(stack)
            for i, s in enumerate(stack):
                invalid.add(s + len(stack) - i)
                invalid.add(s - (len(stack) - i))

            valid = set(range(n)).difference(invalid)

            for v in valid:
                stack.append(v)
                backtrack(stack)
                stack.pop()

        for i in range(n):
            backtrack([i])

        out = []
        for stack in res:
            board = []
            for s in stack:
                row = ["."] * n
                row[s] = "Q"
                board.append("".join(row))
            out.append(board)

        return out
