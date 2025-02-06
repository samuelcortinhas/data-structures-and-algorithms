class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time O(n*m), Memory O(1) where n = len(haystack), m = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    # def strStrFind(self, haystack: str, needle: str) -> int:
    #     return haystack.find(needle)
