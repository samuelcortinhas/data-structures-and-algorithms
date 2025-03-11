class Solution:
    # sliding window - tle
    def numberOfSubstrings(self, s: str) -> int:
        # Time O(n^2), Memory O(1)
        res = 0
        for left in range(len(s) - 2):
            counts = [0] * 3
            for right in range(left, left + 3):
                counts[ord(s[right]) - 97] += 1

            while min(counts) == 0 and right < len(s) - 1:
                right += 1
                counts[ord(s[right]) - 97] += 1

            if min(counts) > 0:
                res += len(s) - right
        return res
