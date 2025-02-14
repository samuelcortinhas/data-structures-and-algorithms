from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Time O(3*n), Memory O(3)
        res = [0, 0, 0]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                res[0] = max(res[0], a)
                res[1] = max(res[1], b)
                res[2] = max(res[2], c)
        return res == target
