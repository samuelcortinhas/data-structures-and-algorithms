class Solution:
    # bottom up true dp
    def numDistinct(self, s: str, t: str) -> int:
        # Time O(m*n), Memory O(m) where n=len(s), m=len(t)
        dp = [0] * (1 + len(t))
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            new_dp = [0] * (1 + len(t))
            new_dp[-1] = 1
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    new_dp[j] = dp[j] + dp[j + 1]
                else:
                    new_dp[j] = dp[j]
            dp = new_dp
        return dp[0]

    # # top down dp with cache
    # def numDistinct(self, s: str, t: str) -> int:
    #     # Time O(m*n), Memory O(m*n) where n=len(s), m=len(t)
    #     dp = [[None] * len(t) for _ in range(len(s))]

    #     # i = index in s, j = index of t
    #     # if s[i] == t[j] do i+=1, j+=1 and i+=1
    #     # if s[i] != t[j] do i+=1
    #     def dfs(i, j):
    #         if j == len(t):
    #             return 1
    #         if i == len(s):
    #             return 0
    #         if dp[i][j] is not None:
    #             return dp[i][j]

    #         if s[i] == t[j]:
    #             dp[i][j] = dfs(i + 1, j + 1) + dfs(i + 1, j)
    #         else:
    #             dp[i][j] = dfs(i + 1, j)
    #         return dp[i][j]

    #     return dfs(0, 0)
