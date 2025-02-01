from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        # Floyd's cycle detection
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

    # def findDuplicateWithSet(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     seen = set()
    #     for n in nums:
    #         if n in seen:
    #             return n
    #         seen.add(n)
