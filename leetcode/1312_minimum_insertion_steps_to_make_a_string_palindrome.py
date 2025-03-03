class Solution:
    def minInsertions(self, s: str) -> int:
        # Time O(n^2), Memory O(n^2)
        dp = {}

        def step(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            if s[left] == s[right]:
                dp[(left, right)] = step(left + 1, right - 1)
                return dp[(left, right)]
            else:
                dp[(left, right)] = 1 + min(
                    step(left + 1, right), step(left, right - 1)
                )
                return dp[(left, right)]

        return step(0, len(s) - 1)
