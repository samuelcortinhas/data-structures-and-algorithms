from typing import List


class Solution:
    # brute force
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Time O((n^2)^n), Memory O((n^2)^n)
        def backtrack(arr, res):
            if len(arr) == 1:
                return arr[0]
            elif len(arr) == 0:
                return 0

            new_res = float("inf")
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    new_arr = list(arr)
                    stone1 = new_arr.pop(i)
                    stone2 = new_arr.pop(j - 1)
                    if stone1 != stone2:
                        new_arr.append(abs(stone2 - stone1))
                    new_res = min(new_res, backtrack(new_arr, res))
            return min(res, new_res)

        return backtrack(stones, float("inf"))
