import heapq


class MedianFinder:
    def __init__(self):
        # O(n) memory
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        # Time O(log n)
        r_min = self.right[0] if self.right else float("inf")

        if num < r_min:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        l = len(self.left)
        r = len(self.right)

        if l - 1 > r:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif r - 1 > l:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        # Time O(1)
        l = len(self.left)
        r = len(self.right)

        if l > r:
            return -self.left[0]
        elif l < r:
            return self.right[0]
        else:
            return (self.right[0] - self.left[0]) / 2


# class MedianFinder:
#     # Insertion sort
#     def __init__(self):
#         # Memory O(n)
#         self.nums = []

#     def addNum(self, num: int) -> None:
#         # Time O(n) - too slow
#         self.nums.append(num)
#         i = len(self.nums) - 1
#         while i > 0 and self.nums[i - 1] > self.nums[i]:
#             tmp = self.nums[i - 1]
#             self.nums[i - 1] = self.nums[i]
#             self.nums[i] = tmp
#             i -= 1

#     def findMedian(self) -> float:
#         # Time O(1)
#         n = len(self.nums)
#         if n % 2 == 1:
#             return self.nums[int((n - 1) / 2)]
#         else:
#             return (self.nums[int((n - 2) / 2)] + self.nums[int(n / 2)]) / 2
