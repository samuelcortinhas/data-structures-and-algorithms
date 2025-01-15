class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time O(n), Memory O(n)
        if len(s) <= 1:
            return len(s)

        seen = {s[0]: 0}
        longest = 1
        left, right = 0, 1

        while right < len(s):
            if (s[right] not in seen) or (seen[s[right]] < left):
                seen[s[right]] = right
                longest = max(longest, 1 + right - left)
            else:
                index = seen[s[right]]  # guaranteed index >= left
                left = index + 1
                seen[s[right]] = right
            right += 1

        return longest

    # def lengthOfLongestSubstringInitial(self, s: str) -> int:
    #     # Time O(n^2), Memory O(n)
    #     if len(s) <= 1:
    #         return len(s)

    #     sub = s[0]
    #     longest = 1
    #     left, right = 0, 1

    #     while right < len(s):
    #         if s[right] not in sub:
    #             sub += s[right]
    #             longest = max(longest, len(sub))
    #         else:
    #             i = sub.index(s[right])  # this is O(n) - use hashmap to optimise
    #             left = i + 1
    #             sub = sub[left:] + s[right]
    #         right += 1

    #     return longest
