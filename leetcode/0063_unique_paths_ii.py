from typing import List


class Solution:
    # Bottom up dp, use grid as cache
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time O(m*n), Memory O(1)
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    continue
                if i + 1 < m and j + 1 < n:
                    obstacleGrid[i][j] = obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]
                elif i + 1 < m:
                    obstacleGrid[i][j] = obstacleGrid[i + 1][j]
                elif j + 1 < n:
                    obstacleGrid[i][j] = obstacleGrid[i][j + 1]

        return obstacleGrid[0][0]
