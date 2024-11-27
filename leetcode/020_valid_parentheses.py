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
            if b in comps:
                stack.append(b)
            else:
                if (len(stack) > 0) and (comps.get(stack[-1]) == b):
                    stack = stack[:-1]
                else:
                    return False

        return len(stack) == 0
