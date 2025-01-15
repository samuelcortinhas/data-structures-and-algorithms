from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time O(n), Memory O(n)
        # Idea: n is start of sequence if n-1 not present
        # go to end of sequence by incrementing += 1
        # every number visited at most twice
        seen = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in seen:
                i = n + 1
                while i in seen:
                    i += 1
                longest = max(longest, i - n)
        return longest
