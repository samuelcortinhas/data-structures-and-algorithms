from typing import List


class Solution:
    # bottom up dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time O(m*n), Memory O(m), where n=len(coins), m=amount
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0 and dp[i - c] != float("inf"):
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float("inf") else -1

    # # top down dp: greedy + backtracking via dfs + cache
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # Time O(m*n), Memory O(m), where n=len(coins), m=amount
    #     dp = {0: 0}
    #     coins.sort(reverse=True)

    #     def dfs(remaining):
    #         if remaining in dp:
    #             return dp[remaining]
    #         for c in coins:
    #             if remaining - c >= 0:
    #                 dp[remaining] = min(
    #                     dp.get(remaining, float("inf")), 1 + dfs(remaining - c)
    #                 )
    #         return dp.get(remaining, float("inf"))

    #     dfs(amount)
    #     return dp.get(amount, -1) if dp.get(amount, -1) != float("inf") else -1

    # # Greedy solution - does not work in all cases
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # Time O(amount/k), Memory O(1) where k = min(coins)
    #     coins.sort(reverse=True)
    #     total = 0
    #     count = 0
    #     for i in range(len(coins)):
    #         while total + coins[i] <= amount:
    #             count += 1
    #             total += coins[i]
    #     return count if total == amount else -1
