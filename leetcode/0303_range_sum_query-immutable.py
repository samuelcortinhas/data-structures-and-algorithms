from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # Time O(n), Memory O(n)
        self.nums = nums
        self.prefix_sum = []
        total = 0
        for n in nums:
            total += n
            self.prefix_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        # Time O(1), Memory O(1)
        r = self.prefix_sum[right]
        l = self.prefix_sum[left - 1] if left > 0 else 0
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
