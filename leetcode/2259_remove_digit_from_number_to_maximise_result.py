class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Time O(n^2), Memory O(1)
        res = 0
        for i, n in enumerate(number):
            if n == digit:
                res = max(res, int(number[:i] + number[i + 1 :]))
        return str(res)
