from typing import List


class Solution:
    def maxProfitInitial(self, prices: List[int]) -> int:
        # Time O(n^2), Memory O(1)
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
