class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
                i = sub.index(s[right])
                left = i + 1
                sub = sub[left:] + s[right]
            right += 1

        return longest
