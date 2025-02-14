class Solution:
    def scoreOfString(self, s: str) -> int:
        # Time O(n), Memory O(1)
        res = 0
        for i in range(len(s) - 1):
            res += abs(ord(s[i + 1]) - ord(s[i]))
        return res

    # def scoreOfStringOneLiner(self, s: str) -> int:
    #     # Time O(n), Memory O(1)
    #     return sum([abs(ord(s[i+1])-ord(s[i])) for i in range(len(s)-1)])
