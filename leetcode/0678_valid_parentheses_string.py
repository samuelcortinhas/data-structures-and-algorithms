class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time O(n), Memory O(1)
        leftmin, leftmax = 0, 0  # min/max num of "(" so far
        for c in s:
            if c == "(":
                leftmin += 1
                leftmax += 1
            elif c == ")":
                leftmin = max(leftmin - 1, 0)
                leftmax -= 1
                if leftmax < 0:
                    return False
            else:
                leftmin = max(leftmin - 1, 0)
                leftmax += 1
        return leftmin == 0
