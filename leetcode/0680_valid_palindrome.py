class Solution:
    # backtracking solution
    def validPalindrome(self, s: str) -> bool:
        # Time O(n), Memory O(1)
        def backtrack(l, r, deletes):
            if deletes > 1:
                return False

            while l <= r:
                if s[l] != s[r]:
                    deletes += 1
                    if s[l + 1] == s[r] and backtrack(l + 1, r, deletes):
                        return True
                    if s[l] == s[r - 1] and backtrack(l, r - 1, deletes):
                        return True
                    return False
                l += 1
                r -= 1
            return True

        return backtrack(0, len(s) - 1, 0)
