from typing import List


class Solution:
    # Binary search + 2 pointer
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Time O(k + log n), Memory O(1)
        l, r = 0, len(arr) - 1
        # Find index of val closest to x
        val, idx = arr[0], 0
        while l <= r:
            m = (l + r) // 2
            curDiff, resDiff = abs(arr[m] - x), abs(val - x)
            if curDiff < resDiff or (curDiff == resDiff and arr[m] < val):
                val, idx = arr[m], m

            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                break

        left = right = idx
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

    # # Linear search + 2 pointer
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     # Time O(n + k), Memory O(1)
    #     closest = float("inf")
    #     closest_i = -1
    #     for i in range(len(arr)):
    #         if abs(arr[i] - x) < closest:
    #             closest = abs(arr[i] - x)
    #             closest_i = i

    #     left = right = closest_i
    #     while right - left + 1 < k:
    #         if left == 0 and right < len(arr) - 1:
    #             right += 1
    #         elif left > 0 and right == len(arr) - 1:
    #             left -= 1
    #         elif abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
    #             left -= 1
    #         else:
    #             right += 1
    #     return arr[left : right + 1]
