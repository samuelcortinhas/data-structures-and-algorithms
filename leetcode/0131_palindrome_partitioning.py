from typing import List


class Solution:
    # Brute force - compute all partitions
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        # Time O(2^n), Memory O(2^n)
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(list(part))
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
