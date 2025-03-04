class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Time O(n), Memory O(n)
        def backtrack(i, curr_sum):
            if curr_sum == n:
                return True
            if curr_sum > n or 3**i > n:
                return False
            return backtrack(i + 1, curr_sum + 3**i) or backtrack(i + 1, curr_sum)

        return backtrack(0, 0)
