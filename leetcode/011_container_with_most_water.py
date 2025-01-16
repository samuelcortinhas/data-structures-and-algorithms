from typing import List


class Solution:
    def maxAreaBruteForce(self, height: List[int]) -> int:
        # Time O(n^2), Memory O(1)
        largest_area = 0
        for i, h in enumerate(height):
            j = i + 1
            while j < len(height):
                area = (j - i) * min(h, height[j])
                largest_area = max(area, largest_area)
                j += 1
        return largest_area
