class Solution:
    def reverseBits(self, n: int) -> int:
        # Time O(32), Memory O(1)
        res = 0
        for _ in range(32):
            bit = n & 1
            res = res << 1
            res += bit
            n = n >> 1
        return res
