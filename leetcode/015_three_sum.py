from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time O(n^2), Memory O(1)
        nums.sort()
        triples = []

        for i, n in enumerate(nums):
            if n > 0:
                return triples

            if i > 0 and n == nums[i - 1]:
                continue

            # solve 2sum II
            prev = nums[0] - 1
            target = -n
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] == prev:
                    prev = nums[j]
                    j += 1
                    continue

                s = nums[j] + nums[k]
                if s > target:
                    k -= 1
                elif s < target:
                    prev = nums[j]
                    j += 1
                else:
                    triples.append([nums[i], nums[j], nums[k]])
                    prev = nums[j]
                    j += 1
        return triples

    # def threeSumV1(self, nums: List[int]) -> List[List[int]]:
    #     # Time O(n^2), Memory O(n)
    #     nums.sort()
    #     triples = []

    #     outer_seen = set()
    #     for i, n in enumerate(nums):
    #         if n > 0:
    #             return triples

    #         if n in outer_seen:
    #             continue
    #         outer_seen.add(n)

    #         # solve 2sum II
    #         inner_seen = set()
    #         target = -n
    #         j, k = i + 1, len(nums) - 1
    #         while j < k:
    #             if nums[j] in inner_seen:
    #                 j += 1
    #                 continue

    #             s = nums[j] + nums[k]
    #             if s > target:
    #                 k -= 1
    #             elif s < target:
    #                 inner_seen.add(nums[j])
    #                 j += 1
    #             else:
    #                 triples.append([nums[i], nums[j], nums[k]])
    #                 inner_seen.add(nums[j])
    #                 j += 1
    #     return triples
