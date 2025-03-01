class Solution:
    # reverse number
    def isPalindrome(self, x: int) -> bool:
        # Time O(log n), Memory O(log n)
        if x < 0:
            return False
        if x == 0:
            return True

        rev = 0
        y = x
        i = 0
        while y:
            rev = 10 * rev + (y % 10)
            y = y // 10
            i += 1
        return x == rev

    # # convert to string
    # def isPalindrome(self, x: int) -> bool:
    #     # Time O(log n), Memory O(log n)
    #     x = str(x)
    #     i, j = 0, len(x) - 1
    #     while i <= j:
    #         if x[i] != x[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True
