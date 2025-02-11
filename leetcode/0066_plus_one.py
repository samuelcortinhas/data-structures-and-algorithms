from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time O(n), O(n)
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            rem = 1
            res = [0]
            for d in digits[-2::-1]:
                res.append((d + rem) % 10)
                rem = (d + rem) // 10
            if rem:
                res.append(1)
            return res[::-1]
