from typing import List


class Solution:
    # Time O(m*n), Memory O(m*n)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        seen = set()

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= m
                or j >= n
                or board[i][j] == "X"
                or (i, j) in seen
            ):
                return

            seen.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if (i, j) not in seen:
                    board[i][j] = "X"
