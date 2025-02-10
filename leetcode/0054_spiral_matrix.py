from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time O(m*n), Memory O(m*n)
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0

        left_wall, right_wall = 0, n - 1
        up_wall, down_wall = 1, m - 1

        step = {"right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0]}
        direc = "right"
        res = []
        while len(res) < m * n:
            res.append(matrix[i][j])
            if direc == "right" and j == right_wall:
                direc = "down"
                right_wall -= 1
            elif direc == "down" and i == down_wall:
                direc = "left"
                down_wall -= 1
            elif direc == "left" and j == left_wall:
                direc = "up"
                left_wall += 1
            elif direc == "up" and i == up_wall:
                direc = "right"
                up_wall += 1

            delta = step[direc]
            i += delta[0]
            j += delta[1]

        return res
