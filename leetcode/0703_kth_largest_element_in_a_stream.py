import heapq
from typing import List


class KthLargest:
    # MinHeap of size k
    def __init__(self, k: int, nums: List[int]):
        # Time O(n + (n-k)*log n), Memory O(n)
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # O(n)

        while len(self.heap) > k:  # O((n-k) * log n)
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Time O(log k), Memory O(k)
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
