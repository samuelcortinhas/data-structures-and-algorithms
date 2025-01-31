from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time O(n), Memory O(n)
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
