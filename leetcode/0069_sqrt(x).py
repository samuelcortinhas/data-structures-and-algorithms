class Solution:
    # Time O(log n), Memory O(1)
    def mySqrt(self, x: int) -> int:
        # 1<x => 1 < sqrt(x) < x
        # y = sqrt(x) <=> y^2 = x
        if x == 0:
            return 0
        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            mid_sq = mid * mid
            if mid_sq > x:
                right = mid
            elif mid_sq < x:
                left = mid
            else:
                return mid
            if right == left + 1:
                return left
        return left
