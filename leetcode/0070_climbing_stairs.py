class Solution:
    # def __init__(self):
    #     self.cache = {1: 1, 2: 2}

    # def climbStairs(self, n: int) -> int:
    #     # Time O(n), Memory O(n)
    #     # Fibonacci
    #     if n in self.cache:
    #         return self.cache[n]

    #     self.cache[n - 2] = self.climbStairs(n - 2)
    #     self.cache[n - 1] = self.climbStairs(n - 1)

    #     return self.cache[n - 1] + self.cache[n - 2]

    # def climbStairsDP(self, n: int) -> int:
    #     # Time O(n), Memory O(n)
    #     cache = [0] * (n + 1)
    #     cache[0] = 1
    #     cache[1] = 1

    #     for i in range(2, n + 1):
    #         cache[i] = cache[i - 2] + cache[i - 1]

    #     return cache[-1]

    # def climbStairsMemoryEfficient(self, n: int) -> int:
    #     # Time O(n), Memory O(1)
    #     cache = [1, 1]
    #     for i in range(2, n + 1):
    #         tmp = cache[1]
    #         cache[1] = cache[0] + cache[1]
    #         cache[0] = tmp
    #     return cache[-1]

    def climbStairsOptimal(self, n: int) -> int:
        # Time O(n), Memory O(1)
        prev, curr = 1, 1
        for _ in range(2, n + 1):
            tmp = curr
            curr += prev
            prev = tmp
        return curr
