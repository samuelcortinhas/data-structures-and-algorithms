# Levenshtein distance
class Solution:
    # memory optimised bottom up dp solution
    def minDistance(self, word1: str, word2: str) -> int:
        # Time O(m*n), Memory O(m) where n=len(word1), m=len(word2)
        dp = [j for j in range(len(word2), -1, -1)]

        for i in range(len(word1) - 1, -1, -1):
            new_dp = [0] * (len(word2) + 1)
            new_dp[-1] = len(word1) - i
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    new_dp[j] = dp[j + 1]
                else:
                    new_dp[j] = 1 + min(dp[j], new_dp[j + 1], dp[j + 1])
            dp = new_dp
        return dp[0]

    # # bottom up dp solution
    # def minDistance(self, word1: str, word2: str) -> int:
    #     # Time O(m*n), Memory O(m*n) where n=len(word1), m=len(word2)
    #     dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    #     dp[-1] = [i for i in range(len(word2), -1, -1)]
    #     for i in range(len(word1)):
    #         dp[i][-1] = len(word1) - i

    #     for i in range(len(word1) - 1, -1, -1):
    #         for j in range(len(word2) - 1, -1, -1):
    #             if word1[i] == word2[j]:
    #                 dp[i][j] = dp[i + 1][j + 1]
    #             else:
    #                 dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

    #     return dp[0][0]
