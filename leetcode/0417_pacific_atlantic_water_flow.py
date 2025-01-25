from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time O(m*n), Memory O(m*n)
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visit, prev):
            if (
                i < 0
                or j < 0
                or i >= m
                or j >= n
                or (i, j) in visit
                or heights[i][j] < prev
            ):
                return

            visit.add((i, j))
            prev = heights[i][j]
            dfs(i + 1, j, visit, prev)
            dfs(i, j + 1, visit, prev)
            dfs(i - 1, j, visit, prev)
            dfs(i, j - 1, visit, prev)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(i, j, pacific, heights[i][j])
                if i == m - 1 or j == n - 1:
                    dfs(i, j, atlantic, heights[i][j])

        return list(pacific.intersection(atlantic))

    # def pacificAtlanticBruteForce(self, heights: List[List[int]]) -> List[List[int]]:
    #     # Time O((m*n)^2), Memory O(m*n(m+n))
    #     m, n = len(heights), len(heights[0])

    #     def dfs(i, j, prev):
    #         if i < 0 or j < 0 or i >= m or j >= n:
    #             return 1

    #         if heights[i][j] > prev:
    #             return 0

    #         prev = heights[i][j]
    #         if (dfs(i + 1, j, prev) or dfs(i, j + 1, prev)) and (
    #             dfs(i - 1, j, prev) or dfs(i, j - 1, prev)
    #         ):
    #             return 1
    #         else:
    #             return 0

    #     res = []
    #     for i in range(m):
    #         for j in range(n):
    #             if dfs(i, j, heights[i][j]):
    #                 res.append([i, j])
    #     return res
