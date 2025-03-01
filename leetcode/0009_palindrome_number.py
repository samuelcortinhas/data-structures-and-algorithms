class Solution:
    # convert to string
    def isPalindrome(self, x: int) -> bool:
        # Time O(n), Memory O(1)
        x = str(x)
        i, j = 0, len(x) - 1
        while i <= j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True
