class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time O(n^2), Memory O(1)
        count = 0
        for i in range(len(s)):
            for offset in [0, 1]:
                l, r = i, i + offset
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count
