class Solution:
    # Time O(1), Memory O(1)
    def coloredCells(self, n: int) -> int:
        # 1, 5, 13, 25
        # diff: 4, 8, 12

        # f(1) = 1
        # f(n) = 4*(n-1) + f(n-1)
        # f(n) = 4*(n-1) + 4*(n-2) + f(n-2)
        # f(n) = 4*(n-1) + 4*(n-2) + ... + 4 + 1
        # f(n) = 4[n-1 + n-2 + ... + 1] + 1
        # f(n) = 4 * (n-1) * n / 2 + 1
        # f(n) = 2 * n * (n-1) + 1

        return 2 * n * (n - 1) + 1
