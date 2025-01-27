from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Time O(n), Memory O(1)
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            lr_min = min(left_max, right_max)
            if height[left] <= lr_min:
                w = lr_min - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                w = lr_min - height[right]
                right -= 1
                right_max = max(right_max, height[right])
            water += w * (w > 0)
        return water

    # def trap(self, height: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     maxes_from_left, maxes_from_right = [], []
    #     left_max, right_max = 0, 0

    #     for h in height:
    #         maxes_from_left.append(left_max)
    #         left_max = max(left_max, h)

    #     for h in height[::-1]:
    #         maxes_from_right.append(right_max)
    #         right_max = max(right_max, h)

    #     maxes_from_right = maxes_from_right[::-1]

    #     water = 0
    #     for i, h in enumerate(height):
    #         w = min(maxes_from_left[i], maxes_from_right[i]) - h
    #         if w > 0:
    #             water += w

    #     return water
