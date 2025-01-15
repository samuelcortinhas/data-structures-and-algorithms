class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time O(n^2), Memory O(1)
        if len(s) <= 1:
            return len(s)

        sub = s[0]
        longest = 1
        left, right = 0, 1

        while right < len(s):
            if s[right] not in sub:
                sub += s[right]
                longest = max(longest, len(sub))
            else:
                i = sub.index(s[right]) # this is O(n) - use hashmap to optimise
                left = i + 1
                sub = sub[left:] + s[right]
            right += 1

        return longest
