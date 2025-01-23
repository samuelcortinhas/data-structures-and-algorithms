from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time O(3^n), Memory O(n) where n=len(word)
        m, n = len(board), len(board[0])
        res = False

        def backtrack(curr, i, j, hist):
            nonlocal res
            # i, j = matrix coordinates
            if i < 0 or j < 0 or i >= m or j >= n or len(curr) > len(word) - 1:
                return
            if board[i][j] != word[len(curr)]:
                return
            curr += board[i][j]
            hist.append((i, j))
            if curr == word:
                res = True
                return

            if (i + 1, j) not in hist:
                backtrack(curr, i + 1, j, hist)
            if (i, j + 1) not in hist:
                backtrack(curr, i, j + 1, hist)
            if (i - 1, j) not in hist:
                backtrack(curr, i - 1, j, hist)
            if (i, j - 1) not in hist:
                backtrack(curr, i, j - 1, hist)

            curr = curr[:-1]
            hist.pop()
            return

        c0 = word[0]
        start = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if c0 == x:
                    start.append([i, j])

        for s in start:
            backtrack("", s[0], s[1], [])

        return res
