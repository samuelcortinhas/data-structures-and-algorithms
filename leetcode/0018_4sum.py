from typing import List


class Solution:
    # outer loop + solve 3sum inside
    # equiv. 2 outer loops + solve 2sum II inside
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time O(n^3), Memory O(1)
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                diff = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == diff:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < len(nums) and nums[left] == nums[left - 1]:
                            left += 1
                    elif nums[left] + nums[right] > diff:
                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        left += 1
                        while left < len(nums) and nums[left] == nums[left - 1]:
                            left += 1
        return res
