class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Time O(n), Memory O(n)
        stack = []
        for s in tokens:
            if s == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif s == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif s == "-":
                stack.append(-(int(stack.pop()) - int(stack.pop())))
            elif s == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a / b))
            else:
                stack.append(s)

        return int(stack[0])
