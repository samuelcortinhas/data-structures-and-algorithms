from typing import List


class Solution:
    # Greedy solution - does not work in all cases
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time O(amount/k), Memory O(1) where k = min(coins)
        coins.sort(reverse=True)
        total = 0
        count = 0
        for i in range(len(coins)):
            while total + coins[i] <= amount:
                count += 1
                total += coins[i]
        return count if total == amount else -1
