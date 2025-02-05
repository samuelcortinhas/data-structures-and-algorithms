import math


class Solution:
    def reverse(self, x: int) -> int:
        # Time O(log |x|), Memory O(log |x|)
        int_min = -(2**31)
        int_max = 2**31 - 1
        res = 0
        while x:
            d = int(math.fmod(x, 10))
            x = int(x / 10)
            res = res * 10 + d
        if res > int_max or res < int_min:
            return 0
        return res
