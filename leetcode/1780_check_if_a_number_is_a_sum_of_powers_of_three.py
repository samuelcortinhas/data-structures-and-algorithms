class Solution:
    # greedy
    def checkPowersOfThree(self, n: int) -> bool:
        # Time O(log n), Memory O(1)
        i = 0
        while 3**i <= n:
            i += 1

        curr = n
        while i >= 0:
            if curr >= 3**i:
                curr -= 3**i
            i -= 1
        return curr == 0

    # # backtracking
    # def checkPowersOfThree(self, n: int) -> bool:
    #     # Time O(n), Memory O(n)
    #     def backtrack(i, curr_sum):
    #         if curr_sum == n:
    #             return True
    #         if curr_sum > n or 3**i > n:
    #             return False
    #         return backtrack(i + 1, curr_sum + 3**i) or backtrack(i + 1, curr_sum)

    #     return backtrack(0, 0)
