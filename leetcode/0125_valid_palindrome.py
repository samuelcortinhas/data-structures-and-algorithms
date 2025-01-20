import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time O(n), Memory O(1)
        chars = re.sub(r"[^a-z0-9]", "", s.lower())

        i = 0
        j = len(chars) - 1
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
        return True
