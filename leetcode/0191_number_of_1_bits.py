class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time O(log n), Memory O(1)
        bits = 0
        while n:
            bits += n & 1
            n = n >> 1
        return bits
