import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        not_primes = set()
        for i in range(2, 1 + math.ceil(math.sqrt(right))):
            for j in range(left, right + 1):
                if j % i == 0:
                    not_primes.add(j)

        primes = set(range(left, right + 1)).difference(not_primes)
        primes = sorted(list(primes))
        if len(primes) <= 1:
            return [-1, -1]

        closest = float("inf")
        res = None
        for k in range(1, len(primes)):
            if primes[k] - primes[k - 1] < closest:
                res = [primes[k - 1], primes[k]]
                closest = primes[k] - primes[k - 1]
        return res
