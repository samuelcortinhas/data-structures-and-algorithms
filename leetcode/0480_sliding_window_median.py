import heapq
from typing import List


class Solution:
    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def rebalance(self):
        l, r = len(self.left), len(self.right)
        if l > r + 1:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        elif r > l + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def add_to_stream(self, num):
        r_min = self.right[0] if self.right else float("inf")
        if num >= r_min:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        self.rebalance()

    def remove_from_stream(self, num):
        r_min = self.right[0] if self.right else float("inf")
        if num >= r_min:
            i = self.right.index(num)
            self.right[i] = self.right[-1]
            self.right.pop()
            heapq.heapify(self.right)
        else:
            i = self.left.index(-num)
            self.left[i] = self.left[-1]
            self.left.pop()
            heapq.heapify(self.left)
        self.rebalance()

    def get_median(self):
        l, r = len(self.left), len(self.right)
        if l == r:
            return (self.right[0] - self.left[0]) / 2
        elif l > r:
            return -self.left[0]
        else:
            return self.right[0]

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Time O(n*k), Memory O(k)
        for i in range(k):
            self.add_to_stream(nums[i])

        res = [self.get_median()]
        for j in range(k, len(nums)):
            self.add_to_stream(nums[j])
            self.remove_from_stream(nums[j - k])
            res.append(self.get_median())
        return res
