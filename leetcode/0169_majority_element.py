from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time O(n log n), Memory O(n)
        counter = Counter(nums)
        s = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return s[0][0]
