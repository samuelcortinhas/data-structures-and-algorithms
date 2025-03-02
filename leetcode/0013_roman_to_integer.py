class Solution:
    def romanToInt(self, s: str) -> int:
        # Time O(n), Memory O(1)
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sub = {"V": 4, "X": 9, "L": 40, "C": 90, "D": 400, "M": 900}
        res = 0
        i = 0
        while i < len(s):
            if (
                i < len(s) - 2
                and val[s[i]] == val[s[i + 1]]
                and val[s[i]] == val[s[i + 2]]
            ):
                res += 3 * val[s[i]]
                i += 3
            elif i < len(s) - 1 and val[s[i]] == val[s[i + 1]]:
                res += 2 * val[s[i]]
                i += 2
            elif i < len(s) - 1 and val[s[i]] > val[s[i + 1]]:
                res += val[s[i]]
                i += 1
            elif i < len(s) - 1 and val[s[i]] < val[s[i + 1]]:
                res += sub[s[i + 1]]
                i += 2
            else:
                res += val[s[i]]
                i += 1
        return res
