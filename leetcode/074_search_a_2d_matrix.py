from typing import List, Tuple


class Solution:
    def map_index_1d_to_2d(self, n_cols: int, index: int) -> Tuple[int, int]:
        row = index // n_cols
        col = index % n_cols
        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time O(log(m * n)), Memory O(1)
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = self.map_index_1d_to_2d(n, mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
