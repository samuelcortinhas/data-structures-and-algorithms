from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time O(9^2), Memory O(9^2)
        board_T = [[board[j][i] for j in range(9)] for i in range(9)]

        for b in [board, board_T]:
            for row in b:
                digits = [r for r in row if r != "."]
                if len(digits) != len(set(digits)):
                    return False

        for u in range(3):
            for v in range(3):
                quadrant = [
                    line[v * 3 : (v + 1) * 3] for line in board[u * 3 : (u + 1) * 3]
                ]
                digits = [j for row in quadrant for j in row if j != "."]
                if len(digits) != len(set(digits)):
                    return False

        return True
