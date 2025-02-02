from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time O(n), Memory O(n)
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        total, res = 0, 0
        for n in nums:
            total += n
            res += prefix_counts[total - k]
            prefix_counts[total] += 1
        return res
