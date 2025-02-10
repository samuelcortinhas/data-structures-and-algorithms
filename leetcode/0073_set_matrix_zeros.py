from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time O(m*n), Memory O(1)
        m, n = len(matrix), len(matrix[0])
        rowzero = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowzero = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0

        if rowzero == 0:
            for j in range(n):
                matrix[0][j] = 0


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # Time O(m*n), Memory O(m+n)
#         m, n = len(matrix), len(matrix[0])
#         rows, cols = set(), set()
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)

#         for i in range(m):
#             for j in range(n):
#                 if i in rows or j in cols:
#                     matrix[i][j] = 0
