class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time O(n), Memory O(n)
        comps = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for b in s:
            if b in "([{":
                stack.append(b)
            else:
                if stack and (comps.get(stack[-1]) == b):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
