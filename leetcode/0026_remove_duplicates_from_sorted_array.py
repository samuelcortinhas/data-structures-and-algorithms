from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time O(n), Memory O(n)
        seen = set()
        i = 0
        for n in nums:
            if n not in seen:
                seen.add(n)
                nums[i] = n
                i += 1
        return len(seen)
