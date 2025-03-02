from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # Time O(m*n), Memory O(m*n)
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.dp[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.dp[i][j - 1]
                    + self.dp[i - 1][j]
                    - self.dp[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Time O(1), Memory O(1)
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row2 + 1][col1]
            - self.dp[row1][col2 + 1]
            + self.dp[row1][col1]
        )


# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         # Time O(m*n), Memory O(m*n)
#         m, n = len(matrix), len(matrix[0])
#         self.matrix = matrix
#         self.prefix = [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 left = self.prefix[i][j - 1] if j > 0 else 0
#                 up = self.prefix[i - 1][j] if i > 0 else 0
#                 diag = self.prefix[i - 1][j - 1] if i > 0 and j > 0 else 0
#                 self.prefix[i][j] = matrix[i][j] + left + up - diag

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         # Time O(1), Memory O(1)
#         box = self.prefix[row2][col2]
#         left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
#         up = self.prefix[row1 - 1][col2] if row1 > 0 else 0
#         diag = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
#         return box - left - up + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
