import math
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time O(n), Memory O(n)
        lg2 = math.ceil(math.log2(1 + n))
        res = [0] * (n + 1)
        for i in range(lg2):
            k = 2**i
            res[k : 2 * k] = [r + 1 for r in res[:k]]
        return res[: n + 1]


#     def countBitsBruteForce(self, n: int) -> List[int]:
#         # Time O(n log n), Memory O(n)
#         def countOnes(n):
#             count = 0
#             while n:
#                 count += n & 1
#                 n = n >> 1
#             return count

#         return [countOnes(i) for i in range(n + 1)]
