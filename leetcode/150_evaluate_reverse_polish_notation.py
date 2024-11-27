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
                stack.append(stack.pop() + stack.pop())
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif s == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(s))

        return stack[0]
