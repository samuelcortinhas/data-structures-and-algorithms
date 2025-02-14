import heapq
from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if (len(nums) % k) != 0:
            return False

        counts = Counter(nums)
        heap = list(nums)
        heapq.heapify(heap)
        while heap:
            start = heapq.heappop(heap)
            if not counts[start]:
                continue

            for i in range(k):
                if counts[start + i]:
                    counts[start + i] -= 1
                else:
                    return False
        return True
