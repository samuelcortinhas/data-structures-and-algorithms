from typing import List


class Solution:
    def isvalid(self, s, n):
        left = sum([1 for i in s if i == "("])
        right = len(s) - left
        return left >= right and left <= n and right <= n

    # def isvalid(self, s, n):
    #     stack = []
    #     for c in s:
    #         if c == "(":
    #             stack.append(c)
    #         elif len(stack) == 0:
    #             return False
    #         elif stack[-1] == "(":
    #             stack.pop()

    #     return (")" not in stack) and (
    #         sum([1 for i in stack if i == "("]) + len(s) <= 2 * n
    #     )

    def generateParenthesisV1(self, n: int) -> List[str]:
        stacks = ["("]
        new_stacks = []

        for i in range(2 * n - 1):
            for stack in stacks:
                if self.isvalid(stack + "(", n):
                    new_stacks.append(stack + "(")

                if self.isvalid(stack + ")", n):
                    new_stacks.append(stack + ")")

            stacks = new_stacks
            new_stacks = []

        return stacks
