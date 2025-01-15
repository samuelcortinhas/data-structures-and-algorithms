from collections import defaultdict


class Solution:
    def isValidSubstring(self, counter, sub, k):
        majority = max(counter, key=counter.get)  # O(26)
        maj_count = counter[majority]
        if maj_count + k >= len(sub):
            return True
        else:
            return False

    def characterReplacement(self, s: str, k: int) -> int:
        # Time O(26*n), Memory O(n)
        if len(s) <= 1:
            return len(s)

        longest = 0
        left, right = 0, 0
        counter = defaultdict(int)

        while right < len(s):
            sub = s[left : 1 + right]
            counter[s[right]] += 1
            if self.isValidSubstring(counter, sub, k):
                right += 1
                longest = max(longest, right - left)
            else:
                counter[s[right]] -= 1
                counter[s[left]] -= 1
                left += 1

        return longest
