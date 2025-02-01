from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time O(n*k), Memory O(1)
        for left in range(len(nums)):
            for right in range(left + 1, min(left + k + 1, len(nums))):
                if nums[left] == nums[right]:
                    return True
        return False
