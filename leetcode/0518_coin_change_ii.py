from typing import List


class Solution:
    # bottom up dp
    def change(self, amount: int, coins: List[int]) -> int:
        # Time O(n*m), Memory O(n*m), where n=amount, m=len(coins)
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for i in range(1, amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i - coins[j]][j]
        return dp[amount][0]

    # # Top down dp
    # def change(self, amount: int, coins: List[int]) -> int:
    #     # Time O(n*m), Memory O(n*m), where n=amount, m=len(coins)
    #     dp = {}

    #     def dfs(i, curr_amount):
    #         if curr_amount == amount:
    #             return 1
    #         if curr_amount > amount:
    #             return 0
    #         if i == len(coins):
    #             return 0
    #         if (i, curr_amount) in dp:
    #             return dp[(i, curr_amount)]

    #         dp[(i, curr_amount)] = dfs(i, curr_amount + coins[i]) + dfs(
    #             i + 1, curr_amount
    #         )
    #         return dp[(i, curr_amount)]

    #     return dfs(0, 0)
