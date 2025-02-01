from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time O(n), Memory O(n)
        seen = set(nums[:k])
        if len(seen) != len(nums[:k]):
            return True

        left, right = 0, k
        while right < len(nums):
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            seen.remove(nums[left])
            left += 1
            right += 1
        return False

    # def containsNearbyDuplicateSlow(self, nums: List[int], k: int) -> bool:
    #     # Time O(n*k), Memory O(1)
    #     for left in range(len(nums)):
    #         for right in range(left + 1, min(left + k + 1, len(nums))):
    #             if nums[left] == nums[right]:
    #                 return True
    #     return False
