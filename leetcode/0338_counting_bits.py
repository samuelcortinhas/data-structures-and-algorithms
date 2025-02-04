from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time O(n log n), Memory O(n)
        def countOnes(n):
            count = 0
            while n:
                count += n & 1
                n = n >> 1
            return count

        return [countOnes(i) for i in range(n + 1)]
