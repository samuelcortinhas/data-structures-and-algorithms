from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Time O(n), Memory O(n)
        less, more = [], []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                more.append(n)

        n = len(nums) - len(less) - len(more)
        return less + [pivot] * n + more
