class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time O(n^2), Memory O(1)
        res = ""
        for i in range(len(s)):
            # odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1

            # even palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res
