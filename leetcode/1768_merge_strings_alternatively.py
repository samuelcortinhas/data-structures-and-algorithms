class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time O(n+m), Memory O(n+m)
        res = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1

        res += word1[i:] + word2[j:]
        return res
