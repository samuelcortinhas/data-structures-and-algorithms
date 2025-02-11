class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time O(n), Memory O(1)
        if n == 0:
            return 1
        elif x == 1:
            return 1
        elif x == -1:
            if n % 2:
                return -1
            else:
                return 1
        elif n < 0:
            n *= -1
            x = 1 / x

        res = x
        for _ in range(n - 1):
            res *= x
            if res == 0:
                return 0
        return res
