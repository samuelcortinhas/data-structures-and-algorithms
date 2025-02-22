from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time O(n^2 * m), Memory O(n), where n=len(s), m=len(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if s[i:].startswith(w):
                    dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
        return dp[0]
