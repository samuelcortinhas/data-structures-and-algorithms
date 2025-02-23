from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # actions: buy, sell, cooldown or hold
        # dfs + backtracking on these actions
        # Time O(4^n), Memory O(n)
        res = 0

        def dfs(i, action, profit):
            nonlocal res
            if i >= len(prices):
                res = max(res, profit)
                return

            if action == "buy":
                dfs(i + 1, "sell", profit - prices[i])
                dfs(i + 1, "hold", profit)

            elif action == "sell":
                dfs(i + 1, "cooldown", profit + prices[i])

            elif action == "hold":
                dfs(i + 1, "sell", profit)
                dfs(i + 1, "hold", profit)

            elif action == "cooldown":
                dfs(i + 1, "buy", profit)
                dfs(i + 1, "cooldown", profit)

        dfs(0, "buy", 0)
        dfs(0, "cooldown", 0)
        return res
