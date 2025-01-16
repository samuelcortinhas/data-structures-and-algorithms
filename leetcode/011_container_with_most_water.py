from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time O(n), Memory O(1)
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

    # def maxAreaBruteForce(self, height: List[int]) -> int:
    #     # Time O(n^2), Memory O(1)
    #     largest_area = 0
    #     for i, h in enumerate(height):
    #         j = i + 1
    #         while j < len(height):
    #             area = (j - i) * min(h, height[j])
    #             largest_area = max(area, largest_area)
    #             j += 1
    #     return largest_area
