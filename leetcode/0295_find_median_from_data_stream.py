class MedianFinder:
    # Insertion sort
    def __init__(self):
        # Memory O(n)
        self.nums = []

    def addNum(self, num: int) -> None:
        # Time O(n)
        self.nums.append(num)
        i = len(self.nums) - 1
        while i > 0 and self.nums[i - 1] > self.nums[i]:
            tmp = self.nums[i - 1]
            self.nums[i - 1] = self.nums[i]
            self.nums[i] = tmp
            i -= 1

    def findMedian(self) -> float:
        # Time O(1)
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[int((n - 1) / 2)]
        else:
            return (self.nums[int((n - 2) / 2)] + self.nums[int(n / 2)]) / 2
