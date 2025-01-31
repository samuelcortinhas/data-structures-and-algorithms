from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time O(n), Memory O(n)
        stack = []  # (start index, height)
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            top_i = i
            while stack and h < stack[-1][1]:
                top_i, top_h = stack.pop()
                area = (i - top_i) * top_h
                max_area = max(max_area, area)
            stack.append((top_i, h))
        return max_area
