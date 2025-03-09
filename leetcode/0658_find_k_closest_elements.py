from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Time O(n + k), Memory O(1)
        closest = float("inf")
        closest_i = -1
        for i in range(len(arr)):
            if abs(arr[i] - x) < closest:
                closest = abs(arr[i] - x)
                closest_i = i

        left = right = closest_i
        while right - left + 1 < k:
            if left == 0 and right < len(arr) - 1:
                right += 1
            elif left > 0 and right == len(arr) - 1:
                left -= 1
            elif abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                left -= 1
            else:
                right += 1
        return arr[left : right + 1]
