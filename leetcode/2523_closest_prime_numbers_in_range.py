import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Time O(n log log n), Memory O(n), where n=right
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, 1 + int(math.sqrt(right))):
            if sieve[i]:
                k = 2
                while k * i <= right:
                    sieve[k * i] = False
                    k += 1

        primes = [i for i in range(left, right + 1) if sieve[i]]
        closest = float("inf")
        res = [-1, -1]
        for k in range(1, len(primes)):
            if (d := (primes[k] - primes[k - 1])) < closest:
                res = [primes[k - 1], primes[k]]
                closest = d
        return res
