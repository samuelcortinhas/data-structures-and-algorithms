class Solution:
    def reverseBits(self, n: int) -> int:
        # Time O(32), Memory O(1)
        res = 0
        for _ in range(32):
            res = res << 1
            res += n & 1
            n = n >> 1
        return res
