from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time O(n), Memory O(n)
        dp = {}  # (index, can_buy): max_profit

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            if can_buy:
                buy = dfs(i + 1, not can_buy) - prices[i]
                hold = dfs(i + 1, can_buy)
                dp[(i, can_buy)] = max(buy, hold)
            else:
                sell = dfs(i + 2, not can_buy) + prices[i]
                hold = dfs(i + 1, can_buy)
                dp[(i, can_buy)] = max(sell, hold)
            return dp[(i, can_buy)]

        return dfs(0, True)

    # def maxProfit(self, prices: List[int]) -> int:
    #     # actions: buy, sell, cooldown or hold
    #     # dfs + backtracking on these actions
    #     # Time O(4^n), Memory O(n)
    #     res = 0

    #     def dfs(i, action, profit):
    #         nonlocal res
    #         if i >= len(prices):
    #             res = max(res, profit)
    #             return

    #         if action == "buy":
    #             dfs(i + 1, "sell", profit - prices[i])
    #             dfs(i + 1, "hold", profit)

    #         elif action == "sell":
    #             dfs(i + 1, "cooldown", profit + prices[i])

    #         elif action == "hold":
    #             dfs(i + 1, "sell", profit)
    #             dfs(i + 1, "hold", profit)

    #         elif action == "cooldown":
    #             dfs(i + 1, "buy", profit)
    #             dfs(i + 1, "cooldown", profit)

    #     dfs(0, "buy", 0)
    #     dfs(0, "cooldown", 0)
    #     return res
