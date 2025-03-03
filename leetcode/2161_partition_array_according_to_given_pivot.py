from typing import List


class Solution:
    # 2 pointer - memory optimised solution
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Time O(n), Memory O(1)
        res = [pivot] * len(nums)
        left, right = 0, len(nums) - 1
        i, j = 0, len(nums) - 1
        while j >= 0:
            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                res[right] = nums[j]
                right -= 1
            i += 1
            j -= 1
        return res

    # # split into arrays
    # def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    #     # Time O(n), Memory O(n)
    #     less, more = [], []
    #     for n in nums:
    #         if n < pivot:
    #             less.append(n)
    #         elif n > pivot:
    #             more.append(n)

    #     n = len(nums) - len(less) - len(more)
    #     return less + [pivot] * n + more
