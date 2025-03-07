import math
from typing import List


class Solution:
    def __init__(self):
        self.primes = self.get_primes()

    @staticmethod
    def get_primes(upper_limit=10**6):
        primes = [True] * (upper_limit + 1)
        for i, x in enumerate(primes):
            if i < 2:
                continue
            if i > 1000:
                break
            if x:
                k = 2
                while k * i < upper_limit:
                    primes[k * i] = False
                    k += 1
        primes[0] = False
        primes[1] = False
        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [i + left for i, p in enumerate(self.primes[left : right + 1]) if p]
        if len(primes) <= 1:
            return [-1, -1]

        closest = float("inf")
        res = None
        for k in range(1, len(primes)):
            if primes[k] - primes[k - 1] < closest:
                res = [primes[k - 1], primes[k]]
                closest = primes[k] - primes[k - 1]
        return res
