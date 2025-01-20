class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time O(n), Memory O(n)
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

    # def twoSumAlt(self, nums, target):
    #     # Time O(n), Memory O(n)
    #     hashmap = {v: i for i, v in enumerate(nums)}

    #     for i, x in enumerate(nums):
    #         diff = target - x

    #         j = hashmap.get(diff)
    #         if j and j != i:
    #             return [i, j]

    # def twoSumBruteForce(self, nums, target):
    #     # Time O(n^2), Memory O(1)
    #     for i, x in enumerate(nums):
    #         for j, y in enumerate(nums[i + 1 :]):
    #             if x + y == target:
    #                 return [i, j + i + 1]
