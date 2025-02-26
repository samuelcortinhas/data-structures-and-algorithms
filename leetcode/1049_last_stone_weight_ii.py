from typing import List


class Solution:
    # True dp solution
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Time O(len(stones) * sum(stones)), Memory O(sum(stones))
        dp = set([stones[0], -stones[0]])
        for weight in stones[1:]:
            new_dp = set()
            for s in dp:
                new_dp.add(s + weight)
                new_dp.add(s - weight)
            dp = new_dp
        return min([s if s >= 0 else float("inf") for s in dp])

    # # better brute force
    # def lastStoneWeightII(self, stones: List[int]) -> int:
    #     # Time O(2^n), Memory O(2^n)

    #     # answer is each number with a + or - in front of it summed together
    #     # backtrack of binary decision tree (+ or -) for each digit
    #     def backtrack(i, stack):
    #         if i == len(stones):
    #             return sum(stack) if sum(stack) >= 0 else float("inf")

    #         stack.append(stones[i])
    #         r1 = backtrack(i + 1, stack)
    #         stack.pop()

    #         stack.append(-stones[i])
    #         r2 = backtrack(i + 1, stack)
    #         stack.pop()

    #         return min(r1, r2)

    #     return backtrack(0, [])

    # # brute force
    # def lastStoneWeightII(self, stones: List[int]) -> int:
    #     # Time O((n^2)^n), Memory O((n^2)^n)
    #     def backtrack(arr, res):
    #         if len(arr) == 1:
    #             return arr[0]
    #         elif len(arr) == 0:
    #             return 0

    #         new_res = float("inf")
    #         for i in range(len(arr)):
    #             for j in range(i + 1, len(arr)):
    #                 new_arr = list(arr)
    #                 stone1 = new_arr.pop(i)
    #                 stone2 = new_arr.pop(j - 1)
    #                 if stone1 != stone2:
    #                     new_arr.append(abs(stone2 - stone1))
    #                 new_res = min(new_res, backtrack(new_arr, res))
    #         return min(res, new_res)

    #     return backtrack(stones, float("inf"))
