class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time O(log n), Memory O(log n)
        if n == 0:
            return 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1:
            return -1 if n % 2 else 1

        def calc_power(x, n):
            if n == 0:
                return 1
            res = calc_power(x * x, n // 2)
            return x * res if n % 2 else res

        res = calc_power(x, abs(n))
        return res if n > 0 else 1 / res

    # def myPow(self, x: float, n: int) -> float:
    #     # Time O(n), Memory O(1)
    #     if n == 0:
    #         return 1
    #     elif x == 1:
    #         return 1
    #     elif x == -1:
    #         if n % 2:
    #             return -1
    #         else:
    #             return 1
    #     elif n < 0:
    #         n *= -1
    #         x = 1 / x

    #     res = x
    #     for _ in range(n - 1):
    #         res *= x
    #         if res == 0:
    #             return 0
    #     return res
