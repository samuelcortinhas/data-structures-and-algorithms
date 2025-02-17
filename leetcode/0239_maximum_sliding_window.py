import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time O(n log k), Memory O(n)
        heap = [(-n, i) for i, n in enumerate(nums[:k])]  # max heap (-val, index)
        heapq.heapify(heap)
        res = [-heap[0][0]]
        for i in range(1, len(nums) - k + 1):
            heapq.heappush(heap, (-nums[i + k - 1], i + k - 1))
            while heap[0][1] < i:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
