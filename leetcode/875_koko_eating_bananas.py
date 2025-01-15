import math
from typing import List


class Solution:
    # idea: hours is monotonically decreasing as you increase k, e.g.
    # k = [1, 2, 3, 4, 5, ...]
    # hours = [30, 15, 11, 7, 3, 3, 3, ...]
    # once k>=max(piles), hours is constant
    # we want to find the smallest value of k s.t. hours <= target
    # use binary search over possible values of k

    def time_to_eat_bananas(self, piles, k):
        # Time O(n), Memory O(1)
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time O(n log(m)), Memory O(1) where n = len(piles), m = max(piles)
        left, right = 1, max(piles)
        lowest = right

        while left <= right:
            mid = (left + right) // 2
            if self.time_to_eat_bananas(piles, mid) > h:
                left = mid + 1
            else:
                right = mid - 1
                lowest = mid

        return lowest
