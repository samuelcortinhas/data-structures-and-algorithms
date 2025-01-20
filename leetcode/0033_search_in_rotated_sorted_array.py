from typing import List


class Solution:
    def find_pivot(self, nums):
        # pivot = index to left of jump
        # assume len(nums) > 1
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:  # no rotation
            return right

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

    def search(self, nums: List[int], target: int) -> int:
        # Time O(log(n)), Memory O(1)
        if len(nums) == 1:
            return (nums[0] == target) - 1

        pivot = self.find_pivot(nums)

        offset = 0
        if pivot == len(nums) - 1:
            sub = nums
        elif nums[0] <= target and target <= nums[pivot]:
            sub = nums[: pivot + 1]
        elif nums[pivot + 1] <= target and target <= nums[-1]:
            sub = nums[pivot + 1 :]
            offset = pivot + 1
        else:
            return -1

        # classic binary search on sub
        left, right = 0, len(sub) - 1
        while left <= right:
            mid = (left + right) // 2
            if sub[mid] == target:
                return mid + offset
            elif sub[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
