from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time O(26*n), Memory O(n)
        longest = 0
        left = 0
        counter = defaultdict(int)

        for right, char in enumerate(s):
            counter[char] += 1

            while max(counter.values()) + k < 1 + right - left:
                counter[s[left]] -= 1
                left += 1

            longest = max(longest, 1 + right - left)

        return longest
