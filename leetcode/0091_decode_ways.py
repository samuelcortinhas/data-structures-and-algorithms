class Solution:
    def numDecodings(self, s: str) -> int:
        # Time O(n), Memory O(n)
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if int(s[i : i + 2]) in range(10, 27):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
