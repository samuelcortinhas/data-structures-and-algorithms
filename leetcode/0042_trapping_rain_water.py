from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Time O(n), Memory O(n)
        maxes_from_left, maxes_from_right = [], []
        left_max, right_max = 0, 0

        for h in height:
            maxes_from_left.append(left_max)
            left_max = max(left_max, h)

        for h in height[::-1]:
            maxes_from_right.append(right_max)
            right_max = max(right_max, h)

        maxes_from_right = maxes_from_right[::-1]

        water = 0
        for i, h in enumerate(height):
            w = min(maxes_from_left[i], maxes_from_right[i]) - h
            if w > 0:
                water += w

        return water
